"""End-of-day prices for every US-listed stock from Massive (formerly Polygon.io), free 'Basic' plan.

One request ('Daily Market Summary', /v2/aggs/grouped/...) returns open/high/low/close/volume for every US
stock on a given trading day, so the whole universe is priced daily for free. The last ~25 trading days are
kept on disk to compute average daily traded value (the liquidity rules).

Twelve Data stays as the backup: FX rates, and quotes for the few tickers Massive doesn't return.
The record returned per ticker has the same shape as prices.TwelveData.quotes(), so the rest of the screener
(valuation.value) doesn't care where a price came from.
"""
import gzip
import json
import os
import time
from datetime import date, datetime, timedelta

import requests

BASES = ("https://api.massive.com", "https://api.polygon.io")
TYPE_NAMES = {"CS": "Common Stock", "OS": "Ordinary Shares", "ADRC": "Depositary Receipt",
              "ADRP": "Depositary Receipt (preferred)", "ADRW": "Depositary Receipt (warrant)",
              "ADRR": "Depositary Receipt (right)", "PFD": "Preferred Stock", "ETF": "ETF", "ETN": "ETN",
              "WARRANT": "Warrant", "UNIT": "Unit", "RIGHT": "Right", "FUND": "Fund", "SP": "Structured Product",
              "GDR": "Depositary Receipt", "NYRS": "Depositary Receipt (NY registry)"}


class MassiveError(Exception):
    pass


class MassiveAuthError(MassiveError):
    """The key itself was refused (not just 'today's data isn't out yet')."""


def new_york_today():
    """The US market's calendar date (a GitHub runner's clock is UTC)."""
    try:
        from zoneinfo import ZoneInfo
        return datetime.now(ZoneInfo("America/New_York")).date()
    except Exception:  # noqa: BLE001 - no tz database: UTC minus 5 hours is close enough
        return (datetime.utcnow() - timedelta(hours=5)).date()


def m_symbol(sec_ticker):
    """SEC writes share classes with '-' (BRK-B); Massive uses '.' (BRK.B)."""
    return str(sec_ticker).upper().replace("-", ".")


def _load(path):
    try:
        with gzip.open(path, "rt", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError, EOFError):
        return None


def _save(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with gzip.open(tmp, "wt", encoding="utf-8") as f:
        json.dump(obj, f)
    os.replace(tmp, path)


class Massive:
    """Low-level client: rate-limited (free plan: 5 requests/minute), retrying, cached per trading day."""

    def __init__(self, api_key, cache_dir, per_minute=5, log=print, fixtures_dir=None, today=None):
        self.key = (api_key or "").strip()
        self.dir = os.path.join(cache_dir, "prices", "massive")
        self.per_minute = per_minute
        self.log = log
        self.fixtures_dir = fixtures_dir
        self.today = today or new_york_today()
        self.session = requests.Session()
        self._last = 0.0
        self.calls = 0

    def available(self):
        return bool(self.key) or bool(self.fixtures_dir)

    def _wait(self):
        gap = 60.0 / max(1, self.per_minute) + 0.5
        dt = time.monotonic() - self._last
        if self._last and dt < gap:
            time.sleep(gap - dt)
        self._last = time.monotonic()

    def _get(self, path, params=None, url=None):
        if self.fixtures_dir:
            return self._fixture(path)
        params = dict(params or {}, apiKey=self.key)
        last = None
        for attempt in range(6):
            base = BASES[0] if attempt < 4 else BASES[1]
            self._wait()
            self.calls += 1
            try:
                r = self.session.get(url or f"{base}{path}", params=params, timeout=90)
            except requests.RequestException as e:
                last = e
                time.sleep(5 * (attempt + 1))
                continue
            if r.status_code == 429:
                self.log("    Massive rate limit - waiting 65 seconds...")
                time.sleep(65)
                continue
            if r.status_code in (401, 403):
                txt = r.text[:300]
                if r.status_code == 403 and ("before end of day" in txt or "today" in txt.lower()
                                             or "NOT_AUTHORIZED" in txt and "/aggs/" in (url or path or "")):
                    raise MassiveError(f"not available yet on this plan (HTTP 403): {txt[:160]}")
                raise MassiveAuthError(f"Massive refused the request (HTTP {r.status_code}): {txt[:200]}")
            if r.status_code >= 500:
                last = MassiveError(f"HTTP {r.status_code}")
                time.sleep(10 * (attempt + 1))
                continue
            try:
                return r.json()
            except ValueError:
                last = MassiveError(f"non-JSON answer (HTTP {r.status_code})")
                time.sleep(5)
        raise MassiveError(f"Massive request failed: {last}")

    def _fixture(self, path):
        f = os.path.join(self.fixtures_dir, "massive", path.strip("/").replace("/", "_") + ".json")
        if not os.path.exists(f):
            return {"status": "OK", "resultsCount": 0, "results": []}
        with open(f, encoding="utf-8") as fh:
            return json.load(fh)

    # ------------------------------------------------------------ one trading day, all US stocks
    def day(self, d, refresh=False, folder=""):
        """{SYMBOL: [open, close, volume, vwap]} for trading day d (date or 'YYYY-MM-DD'); {} if the market was
        closed or the day isn't available yet. Cached for good once a day has data (folder 'hist' is never
        pruned: past dates used for the public-float check)."""
        d = d if isinstance(d, str) else d.isoformat()
        path = os.path.join(self.dir, folder, f"{d}.json.gz")
        hit = _load(path)
        if hit is not None and (hit.get("bars") or not refresh and hit.get("closed_checked")):
            return hit.get("bars") or {}
        recent = d >= (self.today - timedelta(days=1)).isoformat()
        try:
            data = self._get(f"/v2/aggs/grouped/locale/us/market/stocks/{d}", {"adjusted": "true"})
        except MassiveAuthError:
            raise
        except MassiveError:
            if recent:
                return {}      # the free plan only serves a day after its close: not out yet, try next run
            raise
        bars = {}
        for r in (data.get("results") or []) if isinstance(data, dict) else []:
            t, o, c, v = r.get("T"), r.get("o"), r.get("c"), r.get("v")
            if t and c:
                bars[str(t).upper()] = [o, c, v, r.get("vw")]
        past = d < (self.today - timedelta(days=4)).isoformat()
        # a past weekday with no data = market holiday (remember it); a recent empty day may simply not be out yet
        _save(path, {"date": d, "bars": bars, "closed_checked": bool(not bars and past)})
        return bars

    def recent_days(self, n=20, max_lookback=40):
        """The last n trading days that have data, newest first: [(date, bars)]."""
        out, errors = [], 0
        d = self.today
        for _ in range(max_lookback):
            if d.weekday() < 5:
                try:
                    bars = self.day(d, refresh=(d >= self.today - timedelta(days=4)))
                except MassiveAuthError as e:
                    self.log(f"  Massive: {e}")
                    break
                except MassiveError as e:
                    errors += 1
                    self.log(f"  Massive {d.isoformat()}: {e}")
                    if errors >= 5:
                        break
                    d -= timedelta(days=1)
                    continue
                if bars:
                    out.append((d.isoformat(), bars))
                    if len(out) >= n:
                        break
            d -= timedelta(days=1)
        self.prune(keep_after=(self.today - timedelta(days=60)).isoformat())
        return out

    def prune(self, keep_after):
        try:
            for f in os.listdir(self.dir):
                if f[:10] < keep_after and f[:4].isdigit() and not f.startswith("ref"):
                    os.remove(os.path.join(self.dir, f))
        except OSError:
            pass

    def close_on(self, symbol, day):
        """Close on (or up to 4 days before) a past date, from that day's all-stocks file (one request per date,
        cached). Free plan history covers ~2 years; None if unavailable."""
        try:
            d = date.fromisoformat(str(day)[:10])
        except ValueError:
            return None
        if (self.today - d).days > 720:
            return None
        for _ in range(5):
            if d.weekday() < 5:
                try:
                    bars = self.day(d, folder="hist")
                except MassiveError:
                    return None
                if bars:
                    b = bars.get(m_symbol(symbol))
                    return b[1] if b else None
            d -= timedelta(days=1)
        return None

    # ------------------------------------------------------------ reference data (names, listing types)
    def tickers(self, max_age_days=7):
        """{SYMBOL: (name, type)} for active US stock listings, cached a week."""
        path = os.path.join(self.dir, "reference_tickers.json.gz")
        hit = _load(path)
        try:
            if hit and datetime.now() - datetime.fromisoformat(hit["fetched"]) <= timedelta(days=max_age_days):
                return {k: tuple(v) for k, v in hit["tickers"].items()}
        except (KeyError, ValueError):
            pass
        out = {}
        try:
            data = self._get("/v3/reference/tickers", {"market": "stocks", "active": "true", "limit": 1000})
            pages = 0
            while isinstance(data, dict):
                for r in data.get("results") or []:
                    if r.get("ticker"):
                        out[str(r["ticker"]).upper()] = (r.get("name") or "", r.get("type") or "")
                nxt = data.get("next_url")
                pages += 1
                if not nxt or pages > 40 or self.fixtures_dir:
                    break
                data = self._get(None, url=nxt)
        except MassiveError as e:
            self.log(f"  Massive ticker list unavailable: {e}")
            return {k: tuple(v) for k, v in (hit or {}).get("tickers", {}).items()}
        if out:
            _save(path, {"fetched": datetime.now().isoformat(timespec="seconds"), "tickers": out})
        return out


class PriceSource:
    """What the pipeline calls 'prices': Massive first, Twelve Data as backup (and for FX)."""

    def __init__(self, massive, td=None, log=print, td_fallback_max=60, max_stale_days=7, adv_days=20):
        self.m, self.td, self.log = massive, td, log
        self.td_fallback_max = td_fallback_max
        self.max_stale_days = max_stale_days
        self.adv_days = adv_days
        self.today = massive.today
        self._days = None
        self._ref = None
        self.latest_day = None

    def available(self):
        return self.m.available() or (self.td is not None and self.td.available())

    def days(self):
        if self._days is None:
            self._days = self.m.recent_days(self.adv_days) if self.m.available() else []
            if self.m.available() and not self._days:
                self.log("  WARNING: no end-of-day data from Massive (key, plan or outage?) - Twelve Data backup only")
            if self._days:
                self.latest_day = self._days[0][0]
                self.log(f"  Massive: {len(self._days)} trading days loaded, latest {self.latest_day} "
                         f"({len(self._days[0][1])} US stocks)")
        return self._days

    def ref(self):
        if self._ref is None:
            self._ref = self.m.tickers() if self.m.available() else {}
        return self._ref

    def quote(self, sec_ticker):
        sym = m_symbol(sec_ticker)
        days = self.days()
        found = [(d, bars[sym]) for d, bars in days if sym in bars]
        if not found:
            return {"ok": False, "reason": "not in Massive's end-of-day data", "symbol": sym}
        d, (o, c, v, vw) = found[0]
        prev = found[1][1][1] if len(found) > 1 else None
        vols = [b[2] * (b[3] or b[1]) for _, b in found[:self.adv_days] if b[2] is not None]
        name, typ = self.ref().get(sym, ("", ""))
        rec = {"symbol": sym, "name": name or None, "exchange": "US", "currency": "USD", "price": c, "open": o,
               "price_date": d, "previous_close": prev, "source": "Massive",
               "avg_volume": (sum(vols) / len(vols) / c) if (vols and c) else None,
               "adv_days": len(vols), "listing_type": TYPE_NAMES.get(typ, typ) or None}
        problems = []
        if not c or c <= 0:
            problems.append("no valid price")
        age = (self.today - date.fromisoformat(d)).days
        if age > self.max_stale_days:
            problems.append(f"last trade {age} days ago")
        rec["ok"] = not problems
        rec["reason"] = "; ".join(problems)
        return rec

    def quotes(self, items, progress_label="Prices"):
        """items: [(sec_ticker, sec_exchange)] in priority order -> {sec_ticker: record}."""
        out, missing = {}, []
        for t, ex in items:
            q = self.quote(t)
            out[t] = q
            if not q["ok"]:
                missing.append((t, ex))
        ok = sum(1 for q in out.values() if q.get("ok"))
        self.log(f"{progress_label}: {ok}/{len(items)} priced from Massive end-of-day data")
        if missing and self.td is not None and self.td.available() and self.td_fallback_max:
            todo = missing[:self.td_fallback_max]
            self.log(f"  {len(missing)} not found there - asking Twelve Data for {len(todo)}")
            got = self.td.quotes(todo, progress_label="  Twelve Data backup")
            for t, _ in todo:
                q = got.get(t)
                if q and q.get("ok"):
                    q = dict(q, source="Twelve Data", open=q.get("open"))
                    out[t] = q
                elif q:
                    out[t] = dict(out[t], reason=out[t]["reason"] + " | Twelve Data: " + str(q.get("reason")))
        return out

    def instrument_types(self, max_age_days=7):
        """{TWELVE-DATA/MASSIVE SYMBOL: type name}. Massive's reference list first, Twelve Data's as backup."""
        types = {s: TYPE_NAMES.get(t, t) for s, (_, t) in self.ref().items() if t}
        if not types and self.td is not None and self.td.available():
            return self.td.instrument_types(max_age_days)
        return types

    def close_on(self, symbol, day):
        c = self.m.close_on(symbol, day) if self.m.available() else None
        if c is None and self.td is not None and self.td.available():
            c = self.td.close_on(symbol, day)
        return c

    def fx_rates(self, currencies, static):
        if self.td is not None and self.td.available():
            return self.td.fx_rates(currencies, static)
        out = {"USD": (1.0, "USD")}
        for c in currencies:
            if c and c != "USD" and static.get(c):
                out[c] = (float(static[c]), "config.json fx_to_usd (static)")
        return out
