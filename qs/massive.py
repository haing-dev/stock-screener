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
    def day(self, d, refresh=False, folder="", fresh_days=None, adjusted=True):
        """{SYMBOL: [open, close, volume, vwap]} for trading day d (date or 'YYYY-MM-DD'); {} if the market was
        closed or the day isn't available yet. Cached for good once a day has data (folder 'hist' is never
        pruned: past dates used for the public-float check). fresh_days: re-download a cached day older than
        that - closes are split-adjusted as of the download, so a split since then would make old closes wrong."""
        d = d if isinstance(d, str) else d.isoformat()
        path = os.path.join(self.dir, folder, f"{d}.json.gz")
        hit = _load(path)
        if hit is not None and fresh_days is not None:
            try:
                age = (self.today - date.fromisoformat(str(hit.get("fetched") or "")[:10])).days
            except ValueError:
                age = 10 ** 6
            if age > fresh_days:
                hit = None
        if hit is not None and (hit.get("bars") or not refresh and hit.get("closed_checked")):
            return hit.get("bars") or {}
        recent = d >= (self.today - timedelta(days=1)).isoformat()
        try:
            data = self._get(f"/v2/aggs/grouped/locale/us/market/stocks/{d}",
                             {"adjusted": "true" if adjusted else "false"})
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
                bars[str(t).upper()] = [o, c, v, r.get("vw"), r.get("h"), r.get("l")]
        past = d < (self.today - timedelta(days=4)).isoformat()
        # a past weekday with no data = market holiday (remember it); a recent empty day may simply not be out yet
        _save(path, {"date": d, "bars": bars, "closed_checked": bool(not bars and past),
                     "fetched": self.today.isoformat()})
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

    def close_on(self, symbol, day, fresh_days=None, adjusted=True):
        """Close on (or up to 4 days before) a past date, from that day's all-stocks file (one request per date,
        cached). adjusted=False: the close as it actually printed that day (never changes, cached for good) -
        used with share counts from the same date. Free plan history covers ~2 years; None if unavailable."""
        folder = "hist" if adjusted else "hist_raw"
        if not adjusted:
            fresh_days = None
        try:
            d = date.fromisoformat(str(day)[:10])
        except ValueError:
            return None
        if (self.today - d).days > 720 or d > self.today:
            return None
        for _ in range(5):
            if d.weekday() < 5:
                try:
                    bars = self.day(d, folder=folder, fresh_days=fresh_days, adjusted=adjusted)
                except MassiveError:
                    return None
                if bars:
                    b = bars.get(m_symbol(symbol))
                    return b[1] if b else None
            d -= timedelta(days=1)
        return None

    # ------------------------------------------------------------ 52-week range (weekly high/low aggregates)
    def _week_path(self, monday):
        return os.path.join(self.dir, "weeks", f"{monday}.json.gz")

    def backfill_weeks(self, symbols, splits, budget, days=371, log_every=25):
        """Fold each trading day of the last `days` into weekly high/low files (one all-stocks request per day not
        yet folded in, at most `budget` requests this run). Values are split-adjusted as of the day they were
        downloaded; a week file is kept on one basis ('asof') using the split list. Returns (days added, missing)."""
        if splits is None:
            return 0, None
        want = {m_symbol(t) for t in symbols}
        added, missing, spent = 0, 0, 0
        weeks = {}
        d = self.today - timedelta(days=1)
        stop = self.today - timedelta(days=days)
        while d >= stop:
            if d.weekday() < 5:
                monday = (d - timedelta(days=d.weekday())).isoformat()
                w = weeks.get(monday)
                if w is None:
                    w = weeks[monday] = _load(self._week_path(monday)) or {"days": [], "closed": [], "hl": {},
                                                                             "asof": None}
                ds = d.isoformat()
                if ds not in w["days"] and ds not in w["closed"]:
                    if spent >= budget:
                        missing += 1
                    else:
                        cached = _load(os.path.join(self.dir, f"{ds}.json.gz"))
                        cb = (cached or {}).get("bars") or {}
                        if cb and len(next(iter(cb.values()))) >= 6:
                            bars, fetched = cb, (cached.get("fetched") or self.today.isoformat())
                        else:
                            spent += 1
                            try:
                                bars = self.day(d, fresh_days=0)    # re-download a day cached without high/low
                            except MassiveError as e:
                                self.log(f"  Massive {ds}: {e}")
                                d -= timedelta(days=1)
                                continue
                            fetched = self.today.isoformat()
                        if not bars:
                            if ds < (self.today - timedelta(days=4)).isoformat():
                                w["closed"].append(ds)
                                w["dirty"] = True
                        else:
                            asof = w["asof"] or fetched
                            new_asof = max(asof, fetched)
                            hl = w["hl"]
                            if new_asof != asof:      # bring the week onto the newer basis
                                for sym, (h, lo) in list(hl.items()):
                                    f = split_factor(splits.get(sym), after=asof, until=new_asof)
                                    if f != 1.0:
                                        hl[sym] = [h * f, lo * f]
                            for sym in want:
                                b = bars.get(sym)
                                if not b or len(b) < 6 or b[4] is None or b[5] is None:
                                    continue
                                f = split_factor(splits.get(sym), after=fetched, until=new_asof)
                                h, lo = b[4] * f, b[5] * f
                                cur = hl.get(sym)
                                hl[sym] = [max(cur[0], h), min(cur[1], lo)] if cur else [h, lo]
                            w["asof"] = new_asof
                            w["days"].append(ds)
                            w["dirty"] = True
                            added += 1
                            if log_every and added % log_every == 0:
                                self.log(f"  52-week range: {added} days added")
            d -= timedelta(days=1)
        for monday, w in weeks.items():
            if w.pop("dirty", False):
                _save(self._week_path(monday), w)
        self.prune(keep_after=(self.today - timedelta(days=60)).isoformat())
        self._prune_weeks()
        return added, missing

    def _prune_weeks(self, keep_days=400):
        folder = os.path.join(self.dir, "weeks")
        cut = (self.today - timedelta(days=keep_days)).isoformat()
        try:
            for f in os.listdir(folder):
                if f[:10] < cut:
                    os.remove(os.path.join(folder, f))
        except OSError:
            pass

    def ranges_52w(self, symbols, splits):
        """{sec_ticker: {'hi', 'lo', 'days'}} over the last 52 weeks from the weekly files, split-adjusted to today
        (None without a split list)."""
        if splits is None:
            return {}
        first = self.today - timedelta(days=364)
        monday0 = first - timedelta(days=first.weekday())
        files = []
        d = monday0
        while d <= self.today:
            w = _load(self._week_path(d.isoformat()))
            if w:
                files.append(w)
            d += timedelta(days=7)
        out = {}
        for t in symbols:
            sym = m_symbol(t)
            hi = lo = None
            n = 0
            for w in files:
                v = w["hl"].get(sym)
                if not v:
                    continue
                f = split_factor(splits.get(sym), after=w["asof"])
                h, l_ = v[0] * f, v[1] * f
                hi = h if hi is None else max(hi, h)
                lo = l_ if lo is None else min(lo, l_)
                n += sum(1 for x in w["days"] if x >= first.isoformat())
            if hi is not None:
                out[t] = {"hi": hi, "lo": lo, "days": n}
        return out

    def month_end_days(self, months=12):
        """The last trading day of each of the last `months` calendar months: [(date, bars)], UNADJUSTED closes
        (one all-stocks request per month, cached for good; splits are applied by the caller from the split list)."""
        out = []
        first = self.today.replace(day=1)
        for _ in range(months):
            d = first - timedelta(days=1)             # last calendar day of the previous month
            first = d.replace(day=1)
            for _ in range(6):
                if d.weekday() < 5:
                    try:
                        bars = self.day(d, folder="hist_raw", adjusted=False)
                    except MassiveAuthError:
                        raise
                    except MassiveError as e:
                        self.log(f"  Massive {d.isoformat()}: {e}")
                        bars = {}
                    if bars:
                        out.append((d.isoformat(), bars))
                        break
                d -= timedelta(days=1)
        return out

    def splits(self, since, max_age_days=1):
        """{SYMBOL: [(execution_date, split_from, split_to)]} for splits executed on or after `since`, from Massive's
        reference list (cached a day). None if it couldn't be read - callers then treat split-sensitive figures
        as unverified."""
        path = os.path.join(self.dir, "reference_splits.json.gz")
        since = since if isinstance(since, str) else since.isoformat()
        hit = _load(path)
        try:
            if hit and hit.get("since", "9999") <= since and \
                    (self.today - date.fromisoformat(hit["fetched"][:10])).days < max_age_days:
                return {k: [tuple(x) for x in v] for k, v in hit["splits"].items()}
        except (KeyError, ValueError):
            pass
        out = {}
        frm = since
        try:
            if hit and hit.get("since", "9999") <= since and hit.get("fetched"):
                # incremental: only splits executed since a few days before the last download (usually one request)
                frm = (date.fromisoformat(hit["fetched"][:10]) - timedelta(days=5)).isoformat()
                out = {k: [tuple(x) for x in v if x[0] >= since] for k, v in hit["splits"].items()}
                out = {k: v for k, v in out.items() if v}
        except (KeyError, ValueError, TypeError):
            out, frm = {}, since
        try:
            data = self._get("/v3/reference/splits", {"execution_date.gte": frm, "limit": 1000})
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
                if not nxt or pages > 20 or self.fixtures_dir:
                    break
                data = self._get(None, url=nxt)
        except MassiveError as e:
            self.log(f"  Massive split list unavailable: {e}")
            return None
        for v in out.values():
            v.sort()
        _save(path, {"fetched": self.today.isoformat(), "since": since, "splits": out})
        return out

    # ------------------------------------------------------------ reference data (names, listing types)
    def tickers(self, max_age_days=30):
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


def split_factor(splits, after, until=None):
    """Price multiplier for splits executed after `after` (and on/before `until`): a 2-for-1 split (from 1 to 2)
    halves old prices -> 0.5. Share counts move the other way (1 / factor)."""
    f = 1.0
    for d, fr, to in splits or []:
        if d > str(after)[:10] and (until is None or d <= str(until)[:10]) and fr and to:
            f *= fr / to
    return f


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
        d, (o, c, v, vw, *_hl) = found[0]
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
            # tickers Twelve Data couldn't price either are skipped for 30 days (saves its credits)
            path = os.path.join(self.m.dir, "unpriceable.json.gz")
            skip = _load(path) or {}
            cut = (self.today - timedelta(days=30)).isoformat()
            skip = {t: d for t, d in skip.items() if d >= cut}
            todo = [x for x in missing if x[0] not in skip][:self.td_fallback_max]
            self.log(f"  {len(missing)} not found there - asking Twelve Data for {len(todo)}"
                     f" ({sum(1 for x in missing if x[0] in skip)} skipped: not priceable last time)")
            got = self.td.quotes(todo, progress_label="  Twelve Data backup") if todo else {}
            for t, _ in todo:
                q = got.get(t)
                if q and q.get("ok"):
                    q = dict(q, source="Twelve Data", open=q.get("open"))
                    out[t] = q
                    skip.pop(t, None)
                elif q:
                    out[t] = dict(out[t], reason=out[t]["reason"] + " | Twelve Data: " + str(q.get("reason")))
                    if "limit" not in str(q.get("reason")).lower():
                        skip[t] = self.today.isoformat()
            _save(path, skip)
        return out

    def instrument_types(self, max_age_days=7):
        """{TWELVE-DATA/MASSIVE SYMBOL: type name}. Massive's reference list first, Twelve Data's as backup."""
        types = {s: TYPE_NAMES.get(t, t) for s, (_, t) in self.ref().items() if t}
        if not types and self.td is not None and self.td.available():
            return self.td.instrument_types(max_age_days)
        return types

    def close_on(self, symbol, day, fresh_days=12, allow_td=True, adjusted=True):
        """Split-adjusted close on a past date (re-downloaded after fresh_days so later splits are reflected), or
        the unadjusted close (adjusted=False: Massive only - Twelve Data prices are always adjusted)."""
        c = self.m.close_on(symbol, day, fresh_days=fresh_days, adjusted=adjusted) if self.m.available() else None
        if c is None and adjusted and allow_td and self.td is not None and self.td.available():
            c = self.td.close_on(symbol, day)
        return c

    def splits(self, since):
        return self.m.splits(since) if self.m.available() else None

    def ranges_52w(self, symbols, budget=0):
        """52-week high/low per ticker. Spends at most `budget` Massive requests first to fill missing days."""
        if not self.m.available():
            return {}
        from datetime import timedelta as _td
        sp = self.splits((self.today - _td(days=760)).isoformat())
        if budget:
            try:
                added, missing = self.m.backfill_weeks(symbols, sp, budget)
                if missing is None:
                    self.log("  52-week range skipped: split list unavailable")
                else:
                    self.log(f"  52-week range: {added} trading days added, {missing} still to fetch")
            except MassiveAuthError as e:
                self.log(f"  Massive: {e}")
        return self.m.ranges_52w(symbols, sp)

    def month_end_highs(self, symbols, months=12, splits=None):
        """{sec_ticker: (highest month-end close of the last `months` months, its date)} from Massive (12 requests
        for the whole market). Closes are downloaded unadjusted and adjusted here with the split list, so a split
        can never pass for a price fall. Month-end closes slightly understate the true 12-month high, so a drawdown
        measured from them is never overstated. {} without Massive or without a split list (Twelve Data quotes
        carry a 52-week high instead)."""
        if not self.m.available() or splits is None:
            return {}
        try:
            days = self.m.month_end_days(months)
        except MassiveAuthError as e:
            self.log(f"  Massive: {e}")
            return {}
        out = {}
        for t in symbols:
            sym = m_symbol(t)
            best = None
            for d, bars in days:
                b = bars.get(sym)
                if not b or not b[1]:
                    continue
                c = b[1] * split_factor(splits.get(sym), after=d)
                if best is None or c > best[0]:
                    best = (c, d)
            if best:
                out[t] = best
        self.log(f"  12-month highs from {len(days)} month-end closes for {len(out)} companies")
        return out

    def fx_rates(self, currencies, static):
        if self.td is not None and self.td.available():
            return self.td.fx_rates(currencies, static)
        out = {"USD": (1.0, "USD")}
        for c in currencies:
            if c and c != "USD" and static.get(c):
                out[c] = (float(static[c]), "config.json fx_to_usd (static)")
        return out
