"""Prices for the point-in-time backtest (validation/PROTOCOL.md sections 2-3), from Massive.

The monthly grid: for every month, its last trading day (formation day d: price rules, 12-month high, size) and the
first trading day of the next month (d+1: entry and exit at the open). Each is one 'all US stocks' request, stored
UNADJUSTED (as printed) and never re-downloaded. Splits and dividends come from Massive's reference lists; tickers
map to SEC CIKs through Massive's ticker reference, including delisted (inactive) tickers, so companies that later
disappeared stay in the universe.
"""
import os
from bisect import bisect_right
from datetime import date, timedelta

from .massive import TYPE_NAMES, MassiveAuthError, MassiveError, _load, _save, m_symbol, split_factor

STOCK_TYPES = {"CS", "ADRC", "OS", "GDR", "NYRS"}
EXCHANGES = {"NYSE": {"XNYS"}, "Nasdaq": {"XNAS"}, "NYSE American": {"XASE"}, "NYSE Arca": {"ARCX"}}


def month_ends(start, end):
    """[(year, month)] from start=(y, m) to end=(y, m) inclusive."""
    out = []
    y, m = start
    while (y, m) <= end:
        out.append((y, m))
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    return out


def _last_day(y, m):
    nxt = date(y + 1, 1, 1) if m == 12 else date(y, m + 1, 1)
    return nxt - timedelta(days=1)


class BTPrices:
    def __init__(self, massive, log=print):
        self.m, self.log = massive, log
        self.dir = os.path.join(massive.dir, "bt")
        self._tick = None
        self._splits = None
        self._divs = None

    # ------------------------------------------------------------ the monthly grid
    def _first_day_with_bars(self, d, step, tries=7):
        for _ in range(tries):
            if d.weekday() < 5:
                try:
                    bars = self.m.day(d, folder="bt", adjusted=False)
                except MassiveAuthError:
                    raise
                except MassiveError as e:
                    self.log(f"  Massive {d.isoformat()}: {e}")
                    return None, None
                if bars:
                    return d.isoformat(), bars
            d += timedelta(days=step)
        return None, None

    def grid(self, start, end):
        """[{'ym', 'd', 'bars_d', 'e', 'bars_e'}] per month: d = last trading day, e = first trading day after it.
        Months whose prices aren't available (plan history, future) are skipped."""
        out = []
        for y, m in month_ends(start, end):
            d, bd = self._first_day_with_bars(_last_day(y, m), -1)
            if not d:
                continue
            e, be = self._first_day_with_bars(date.fromisoformat(d) + timedelta(days=1), +1)
            if not e:
                continue
            out.append({"ym": f"{y:04d}-{m:02d}", "d": d, "bars_d": bd, "e": e, "bars_e": be})
        return out

    def bars(self, day):
        hit = _load(os.path.join(self.m.dir, "bt", f"{day}.json.gz"))
        return (hit or {}).get("bars") or {}

    # ------------------------------------------------------------ tickers -> CIK, including delisted ones
    def tickers(self, max_age_days=30):
        """{SYMBOL: [record, ...]} with record = {'cik', 'type', 'ex', 'name', 'active', 'delisted'}."""
        if self._tick is not None:
            return self._tick
        path = os.path.join(self.dir, "reference_tickers_all.json.gz")
        hit = _load(path)
        if hit and (self.m.today - date.fromisoformat(hit["fetched"])).days <= max_age_days:
            self._tick = hit["tickers"]
            return self._tick
        out = {}
        for active in ("true", "false"):
            try:
                data = self.m._get("/v3/reference/tickers", {"market": "stocks", "active": active, "limit": 1000})
                pages = 0
                while isinstance(data, dict):
                    for r in data.get("results") or []:
                        t = str(r.get("ticker") or "").upper()
                        if not t:
                            continue
                        rec = {"cik": int(r["cik"]) if str(r.get("cik") or "").isdigit() else None,
                               "type": r.get("type") or "", "ex": r.get("primary_exchange") or "",
                               "name": r.get("name") or "",
                               "active": bool(r["active"]) if "active" in r else active == "true",
                               "delisted": (r.get("delisted_utc") or "")[:10] or None}
                        lst = out.setdefault(t, [])
                        if rec not in lst:
                            lst.append(rec)
                    nxt = data.get("next_url")
                    pages += 1
                    if not nxt or pages > 400 or self.m.fixtures_dir:
                        break
                    data = self.m._get(None, url=nxt)
            except MassiveError as e:
                self.log(f"  Massive ticker reference ({'active' if active == 'true' else 'delisted'}) incomplete: {e}")
        if out:
            _save(path, {"fetched": self.m.today.isoformat(), "tickers": out})
        self._tick = out
        return out

    def resolve(self, symbol, day):
        """The ticker record a symbol stood for on `day`: the earliest delisting after that day, else the active
        listing (tickers are reused after a company leaves)."""
        recs = self.tickers().get(symbol) or []
        later = sorted((r for r in recs if r.get("delisted") and r["delisted"] > day), key=lambda r: r["delisted"])
        if later:
            return later[0]
        act = [r for r in recs if r.get("active")]
        return act[0] if act else None

    def universe(self, day, bars, exchanges, stats=None):
        """{cik: {'tickers': [...], 'type', 'ex'}} - stocks of the wanted exchanges with a price on `day`. A delisted
        ticker whose reference record has no exchange is kept (the grouped bars hold exchange-listed stocks only),
        so companies that later disappeared aren't dropped for a missing field. stats (dict) counts what was left
        out and why."""
        allowed = set().union(*(EXCHANGES.get(x, set()) for x in exchanges))
        out = {}
        for sym, b in bars.items():
            if not b or not b[1]:
                continue
            r = self.resolve(sym, day)
            why = None
            if not r:
                why = "no ticker record"
            elif r.get("type") not in STOCK_TYPES:
                why = "not a stock"
            elif not r.get("cik"):
                why = "stock without CIK"
            elif r.get("ex") not in allowed and (r.get("ex") or r.get("active")):
                why = "other exchange"
            if why:
                if stats is not None:
                    stats[why] = stats.get(why, 0) + 1
                continue
            u = out.setdefault(r["cik"], {"tickers": [], "type": r["type"], "ex": r["ex"], "name": r["name"]})
            u["tickers"].append(sym)
        return out

    # ------------------------------------------------------------ corporate actions
    def splits(self, since, max_age_days=7):
        """{SYMBOL: [(execution_date, split_from, split_to)]} since `since` - the whole list (the live client stops
        after 20 pages; a missed reverse split would look like a huge return here)."""
        if self._splits is not None:
            return self._splits
        path = os.path.join(self.dir, "reference_splits_all.json.gz")
        hit = _load(path)
        if hit and hit.get("since", "9999") <= since and \
                (self.m.today - date.fromisoformat(hit["fetched"])).days <= max_age_days:
            self._splits = {k: [tuple(x) for x in v] for k, v in hit["splits"].items()}
            return self._splits
        out = {}
        try:
            data = self.m._get("/v3/reference/splits", {"execution_date.gte": since, "limit": 1000})
            pages = 0
            while isinstance(data, dict):
                for r in data.get("results") or []:
                    t, d = r.get("ticker"), r.get("execution_date")
                    fr, to = r.get("split_from"), r.get("split_to")
                    if t and d and fr and to:
                        rec = (d, float(fr), float(to))
                        lst = out.setdefault(str(t).upper(), [])
                        if rec not in lst:
                            lst.append(rec)
                nxt = data.get("next_url")
                pages += 1
                if not nxt or pages > 1000 or self.m.fixtures_dir:
                    break
                data = self.m._get(None, url=nxt)
        except MassiveError as e:
            self.log(f"  Massive split list incomplete: {e}")
        for v in out.values():
            v.sort()
        _save(path, {"fetched": self.m.today.isoformat(), "since": since, "splits": out})
        self._splits = out
        return out

    def dividends(self, since, max_age_days=7):
        """{SYMBOL: [(ex_date, cash_amount)]} for cash dividends with ex-date on/after `since`."""
        if self._divs is not None:
            return self._divs
        path = os.path.join(self.dir, "reference_dividends.json.gz")
        hit = _load(path)
        if hit and hit.get("since", "9999") <= since and \
                (self.m.today - date.fromisoformat(hit["fetched"])).days <= max_age_days:
            self._divs = {k: [tuple(x) for x in v] for k, v in hit["divs"].items()}
            return self._divs
        out = {}
        try:
            data = self.m._get("/v3/reference/dividends", {"ex_dividend_date.gte": since, "limit": 1000})
            pages = 0
            while isinstance(data, dict):
                for r in data.get("results") or []:
                    t, d, c = r.get("ticker"), r.get("ex_dividend_date"), r.get("cash_amount")
                    if t and d and c and (r.get("currency") or "USD") == "USD":
                        out.setdefault(str(t).upper(), []).append((d, float(c)))
                nxt = data.get("next_url")
                pages += 1
                if not nxt or pages > 2000 or self.m.fixtures_dir:
                    break
                data = self.m._get(None, url=nxt)
        except MassiveError as e:
            self.log(f"  Massive dividend list incomplete: {e}")
        for v in out.values():
            v.sort()
        _save(path, {"fetched": self.m.today.isoformat(), "since": since, "divs": out})
        self._divs = out
        return out

    def last_close(self, symbol, after, until):
        """(date, close) of the last daily bar in (after, until], unadjusted - the exit price of a company that left
        the exchange between two grid dates. One request per symbol, cached."""
        path = os.path.join(self.dir, "last", f"{symbol}_{after}_{until}.json.gz")
        hit = _load(path)
        if hit is not None:
            return tuple(hit["v"]) if hit.get("v") else None
        try:
            data = self.m._get(f"/v2/aggs/ticker/{symbol}/range/1/day/{after}/{until}",
                               {"adjusted": "false", "sort": "desc", "limit": 50})
        except MassiveError:
            return None
        v = None
        for r in (data.get("results") or []) if isinstance(data, dict) else []:
            if r.get("c"):
                from datetime import datetime, timezone
                day = datetime.fromtimestamp(r["t"] / 1000, tz=timezone.utc).date().isoformat()
                if after < day <= until:
                    v = [day, r["c"]]
                    break
        _save(path, {"v": v})
        return tuple(v) if v else None


# ------------------------------------------------------------ returns
def holding_return(p0, p1, sym_splits, sym_divs, start, end):
    """Total return from price p0 (as printed on `start`) to p1 (as printed on `end`): splits executed in
    (start, end] change the number of shares held, cash dividends with ex-date in (start, end] are added (paid on the
    shares held at the time). Unadjusted prices + corporate actions -> no dependence on when data was downloaded."""
    if not p0 or p1 is None or p0 <= 0:
        return None
    shares, cash = 1.0, 0.0
    events = [(d, "s", fr, to) for d, fr, to in (sym_splits or []) if start < d <= end]
    events += [(d, "d", c, None) for d, c in (sym_divs or []) if start < d <= end]
    for d, kind, a, b in sorted(events, key=lambda x: (x[0], 0 if x[1] == "s" else 1)):
        if kind == "s" and a and b:
            shares *= b / a
        elif kind == "d":
            cash += a * shares
    return (p1 * shares + cash) / p0 - 1


def adjusted_close(close, sym_splits, on, asof):
    """A close printed on `on`, restated on the share basis of `asof` (splits in between)."""
    return close * split_factor(sym_splits, after=on, until=asof)


def type_name(code):
    return TYPE_NAMES.get(code, code) or None


def nearest_before(sorted_days, day):
    i = bisect_right(sorted_days, day)
    return sorted_days[i - 1] if i else None


__all__ = ["BTPrices", "holding_return", "adjusted_close", "month_ends", "type_name", "m_symbol", "nearest_before"]
