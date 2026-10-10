"""Share prices and FX rates from Twelve Data (https://twelvedata.com), cached on disk.

Only companies that already pass a screen's financial-statement rules are priced, so the number of API
credits used per run stays small. Every quote is checked before use:
  * the listing must be a US exchange and the currency USD,
  * the quote must be recent (config 'price_max_staleness_days'),
  * the price must be positive.
A quote failing any check is not used, and the company goes to the screen's 'Check manually' list with
the reason - it is never silently dropped.
"""
import gzip
import json
import os
import threading
import time
from collections import deque
from datetime import date, datetime, timedelta

import requests

BASE = "https://api.twelvedata.com"
US_EXCHANGES = {"NYSE", "NASDAQ", "NYSE AMERICAN", "NYSE ARCA", "CBOE", "BATS", "AMEX", "NYSEAMERICAN"}
EXCHANGE_PARAM = {"NYSE": "NYSE", "Nasdaq": "NASDAQ", "NYSE American": "NYSE AMERICAN", "CBOE": "CBOE"}


class PriceError(Exception):
    pass


class DailyLimitReached(PriceError):
    pass


ECB_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"


def ecb_rates_to_usd(timeout=20):
    """(date, {currency: US dollars per unit}) from the ECB's daily reference rates, or None."""
    import re
    import requests as _rq
    try:
        r = _rq.get(ECB_URL, timeout=timeout)
        if r.status_code != 200:
            return None
        xml = r.text
    except Exception:  # noqa: BLE001
        return None
    day = re.search(r"time=['\"](\d{4}-\d{2}-\d{2})['\"]", xml)
    per_eur = {m.group(1): float(m.group(2)) for m in re.finditer(r"currency=['\"]([A-Z]{3})['\"]\s+rate=['\"]([0-9.]+)['\"]", xml)}
    usd = per_eur.get("USD")
    if not usd:
        return None
    out = {c: usd / v for c, v in per_eur.items() if v > 0}
    out["EUR"] = usd
    out.pop("USD", None)
    return (day.group(1) if day else ""), out


def td_symbol(sec_ticker):
    """SEC writes share classes with '-' (BRK-B); Twelve Data uses '.' (BRK.B)."""
    return str(sec_ticker).upper().replace("-", ".")


def _f(x):
    try:
        v = float(x)
        return v if v == v else None
    except (TypeError, ValueError):
        return None


class TwelveData:
    def __init__(self, api_key, cache_dir, max_age_days=3, fixtures_dir=None, log=print, today=None,
                 max_stale_days=7):
        self.key = (api_key or "").strip()
        self.cache_path = os.path.join(cache_dir, "prices", "quotes.json.gz")
        self.fx_path = os.path.join(cache_dir, "prices", "fx.json.gz")
        self.max_age = timedelta(days=max_age_days)
        self.fixtures_dir = fixtures_dir
        self.log = log
        self.today = today or date.today()
        self.max_stale_days = max_stale_days
        self.session = requests.Session()
        self.per_minute = 8
        self.daily_limit = None
        self.daily_used = 0
        self.window = deque()
        self.lock = threading.Lock()
        self.cache = self._load(self.cache_path)
        self.fx_cache = self._load(self.fx_path)

    # ------------------------------------------------------------ plumbing
    @staticmethod
    def _load(path):
        try:
            with gzip.open(path, "rt", encoding="utf-8") as f:
                return json.load(f)
        except (OSError, ValueError, EOFError):
            return {}

    @staticmethod
    def _save(path, obj):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        tmp = path + ".tmp"
        with gzip.open(tmp, "wt", encoding="utf-8") as f:
            json.dump(obj, f)
        os.replace(tmp, path)

    def available(self):
        return bool(self.key) or bool(self.fixtures_dir)

    def _get(self, endpoint, params):
        if self.fixtures_dir:
            return self._fixture(endpoint, params)
        params = dict(params, apikey=self.key)
        last = None
        for attempt in range(5):
            try:
                r = self.session.get(f"{BASE}/{endpoint}", params=params, timeout=60)
            except requests.RequestException as e:
                last = e
                time.sleep(2 ** attempt)
                continue
            try:
                data = r.json()
            except ValueError:
                last = PriceError(f"Twelve Data returned non-JSON (HTTP {r.status_code})")
                time.sleep(2 ** attempt)
                continue
            if isinstance(data, dict) and data.get("status") == "error" and "symbol" not in data:
                code = data.get("code")
                msg = str(data.get("message", ""))
                if code == 429 or r.status_code == 429:
                    if "day" in msg.lower() or "daily" in msg.lower():
                        raise DailyLimitReached(msg)
                    self.log("    Twelve Data per-minute limit reached - waiting 65 seconds...")
                    time.sleep(65)
                    continue
                if code in (401, 403):
                    raise PriceError(f"Twelve Data refused the request ({code}): {msg}")
                return data
            return data
        raise PriceError(f"Twelve Data request failed: {last}")

    def _fixture(self, endpoint, params):
        path = os.path.join(self.fixtures_dir, "twelvedata", f"{endpoint}.json")
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        if endpoint == "quote":
            syms = params["symbol"].split(",")
            out = {s: data.get(s, {"code": 404, "status": "error", "message": f"**symbol** {s} not found"})
                   for s in syms}
            return out if len(syms) > 1 else out[syms[0]]
        if endpoint == "exchange_rate":
            return data.get(params["symbol"], {"code": 404, "status": "error", "message": "not found"})
        if endpoint == "stocks":
            ex = params.get("exchange")
            return {"status": "ok", "data": [r for r in data.get("data", []) if not ex or r.get("exchange") == ex]}
        if endpoint == "time_series":
            return data.get(params["symbol"], {"code": 404, "status": "error", "message": "not found"})
        return data

    def _spend(self, credits):
        """Sliding one-minute window so we never exceed the plan's credits per minute."""
        with self.lock:
            while True:
                now = time.monotonic()
                while self.window and now - self.window[0][0] > 61:
                    self.window.popleft()
                used = sum(c for _, c in self.window)
                if used + credits <= self.per_minute or not self.window:
                    self.window.append((now, credits))
                    self.daily_used += credits
                    return
                wait = 61 - (now - self.window[0][0])
                time.sleep(max(1.0, wait))

    def check_plan(self):
        """Read the plan's limits. Returns a dict for the setup check."""
        if self.fixtures_dir:
            self.per_minute = 120
            return {"plan_category": "fixture", "plan_limit": 120}
        data = self._get("api_usage", {})
        if isinstance(data, dict) and data.get("status") != "error":
            pl = data.get("plan_limit")
            if isinstance(pl, (int, float)) and pl > 0:
                self.per_minute = int(pl)
            dl = data.get("plan_daily_limit")
            if isinstance(dl, (int, float)) and dl > 0:
                self.daily_limit = int(dl)
                du = data.get("daily_usage")
                self.daily_used = int(du) if isinstance(du, (int, float)) else 0
        return data

    # ------------------------------------------------------------ quotes
    def _fresh(self, sym):
        c = self.cache.get(sym)
        if not c:
            return None
        try:
            if datetime.now() - datetime.fromisoformat(c["fetched"]) <= self.max_age:
                return c
        except (KeyError, ValueError):
            return None
        return None

    def quotes(self, items, progress_label="Prices"):
        """items: list of (sec_ticker, sec_exchange). Returns {sec_ticker: record}.
        record = {'ok': bool, 'reason': str, 'price', 'price_date', 'avg_volume', 'exchange', 'currency',
                  'name', 'fifty_two_week_high', 'fifty_two_week_low', 'symbol'}"""
        out, todo = {}, []
        for t, ex in items:
            sym = td_symbol(t)
            c = self._fresh(sym)
            if c:
                out[t] = c["record"]
            else:
                todo.append((t, ex, sym))
        if not todo:
            return out
        if not self.available():
            for t, ex, sym in todo:
                out[t] = {"ok": False, "reason": "no Twelve Data API key in config.json"}
            return out
        try:
            self.check_plan()
        except PriceError as e:
            self.log(f"  Twelve Data unavailable: {e}")
            for t, ex, sym in todo:
                out[t] = {"ok": False, "reason": f"price not fetched: {e}"}
            return out
        n = len(todo)
        eta = n / max(self.per_minute, 1)
        self.log(f"{progress_label}: {n} quotes to fetch from Twelve Data "
                 f"({self.per_minute} credits/minute on your plan, about {eta:.0f} min)")
        # batches keep the caller's order (most important candidates first, in case the daily limit is reached);
        # each batch holds one exchange so the exchange parameter applies to the whole batch
        batch_size = max(1, min(self.per_minute, 120))
        batches = []
        for t, ex, sym in todo:
            ex_param = EXCHANGE_PARAM.get(ex, "")
            if batches and batches[-1][0] == ex_param and len(batches[-1][1]) < batch_size:
                batches[-1][1].append((t, sym))
            else:
                batches.append((ex_param, [(t, sym)]))
        done = 0
        try:
            for ex_param, chunk in batches:
                if self.daily_limit and self.daily_used + len(chunk) > self.daily_limit:
                    raise DailyLimitReached("daily credit limit of your Twelve Data plan")
                self._spend(len(chunk))
                params = {"symbol": ",".join(s for _, s in chunk)}
                if ex_param:
                    params["exchange"] = ex_param
                data = self._get("quote", params)
                if len(chunk) == 1:
                    data = {chunk[0][1]: data}
                for t, sym in chunk:
                    rec = self._validate(data.get(sym) if isinstance(data, dict) else None, sym, self.max_stale_days,
                                         self.today)
                    out[t] = rec
                    self.cache[sym] = {"fetched": datetime.now().isoformat(timespec="seconds"), "record": rec}
                done += len(chunk)
                if done % (batch_size * 10) == 0 or done == n:
                    self.log(f"  {done}/{n} quotes")
                    self._save(self.cache_path, self.cache)
            # symbols the exchange-filtered batch couldn't find: retry one by one without the exchange filter
            # (the result must still be a US listing in USD, or it is rejected by _validate)
            retry = [(t, ex, sym) for t, ex, sym in todo
                     if t in out and not out[t].get("ok") and str(out[t].get("reason", "")).startswith("Twelve Data")]
            if retry:
                self.log(f"  retrying {len(retry)} symbols without the exchange filter")
            for t, ex, sym in retry:
                if self.daily_limit and self.daily_used + 1 > self.daily_limit:
                    raise DailyLimitReached("daily credit limit of your Twelve Data plan")
                self._spend(1)
                data = self._get("quote", {"symbol": sym, "country": "United States"})
                rec = self._validate(data, sym, self.max_stale_days, self.today)
                if not rec["ok"]:
                    rec["reason"] = f"{out[t].get('reason')} | retry: {rec['reason']}"
                out[t] = rec
                self.cache[sym] = {"fetched": datetime.now().isoformat(timespec="seconds"), "record": rec}
        except PriceError as e:
            left = [t for t, _, _ in todo if t not in out or (not out[t].get("ok") and t not in self.cache)]
            kind = "daily limit reached (run again)" if isinstance(e, DailyLimitReached) else f"error: {e}"
            self.log(f"  Stopped fetching prices: {e}. {len(left)} quotes still needed - they go to the 'Check "
                     f"manually' lists; run again later (fetched quotes are cached for {self.max_age.days} days).")
            for t in [t for t, _, _ in todo if t not in out]:
                out[t] = {"ok": False, "reason": f"price not fetched: Twelve Data {kind}"}
        except DailyLimitReached as e:  # pragma: no cover - subclass handled above
            left = [t for t, _, _ in todo if t not in out]
            self.log(f"  Stopped: {e}. {len(left)} quotes still needed - run again tomorrow (fetched quotes are "
                     f"cached for {self.max_age.days} days), or upgrade the plan.")
            for t in left:
                out[t] = {"ok": False, "reason": "price not fetched: Twelve Data daily limit reached (run again)"}
        finally:
            self._save(self.cache_path, self.cache)
        return out

    @staticmethod
    def _validate(q, sym, max_stale_days=7, today=None):
        today = today or date.today()
        if not isinstance(q, dict):
            return {"ok": False, "reason": "no quote returned", "symbol": sym}
        if q.get("status") == "error" or q.get("code"):
            return {"ok": False, "reason": f"Twelve Data: {str(q.get('message', 'error'))[:120]}", "symbol": sym}
        price = _f(q.get("close"))
        rec = {"symbol": sym, "name": q.get("name"), "exchange": q.get("exchange"), "currency": q.get("currency"),
               "price": price, "open": _f(q.get("open")), "price_date": str(q.get("datetime") or "")[:10],
               "avg_volume": _f(q.get("average_volume")), "previous_close": _f(q.get("previous_close"))}
        ftw = q.get("fifty_two_week") or {}
        rec["fifty_two_week_high"] = _f(ftw.get("high"))
        rec["fifty_two_week_low"] = _f(ftw.get("low"))
        problems = []
        if str(q.get("currency") or "").upper() != "USD":
            problems.append(f"quote currency {q.get('currency')} (expected USD)")
        if str(q.get("exchange") or "").upper() not in US_EXCHANGES:
            problems.append(f"quote is from exchange {q.get('exchange')} (expected a US listing)")
        if not price or price <= 0:
            problems.append("no valid price")
        try:
            age = (today - date.fromisoformat(rec["price_date"])).days
            if age > max_stale_days:
                problems.append(f"price is {age} days old")
        except ValueError:
            problems.append("quote has no date")
        rec["ok"] = not problems
        rec["reason"] = "; ".join(problems)
        return rec

    # ------------------------------------------------------------ listing type & historical prices
    def instrument_types(self, max_age_days=7):
        """{TWELVE-DATA SYMBOL: type} for NYSE and Nasdaq listings ('Common Stock', 'Depositary Receipt', ...).
        Two requests, cached for a week. Used to tell a foreign company's ordinary shares (1 share = 1 share)
        from an ADR (ratio unknown)."""
        path = os.path.join(os.path.dirname(self.cache_path), "listing_types.json.gz")
        c = self._load(path)
        try:
            if c and datetime.now() - datetime.fromisoformat(c["fetched"]) <= timedelta(days=max_age_days):
                return c["types"]
        except (KeyError, ValueError):
            pass
        if not self.available():
            return {}
        types = {}
        try:
            for ex in ("NYSE", "NASDAQ"):
                self._spend(1)
                d = self._get("stocks", {"exchange": ex})
                for r in (d.get("data") or []) if isinstance(d, dict) else []:
                    sym, typ = r.get("symbol"), r.get("type")
                    if sym and typ:
                        types[str(sym).upper()] = str(typ)
        except PriceError as e:
            self.log(f"  listing types not available: {e}")
            return c.get("types", {}) if c else {}
        if types:
            self._save(path, {"fetched": datetime.now().isoformat(timespec="seconds"), "types": types})
        return types

    def close_on(self, symbol, day):
        """Closing price on (or just before) a past date - 1 credit, cached for good."""
        key = f"{symbol}@{day}"
        hit = self.cache.get(key)
        if hit and hit.get("close"):
            return hit["close"]
        if not self.available():
            return None
        try:
            if self.daily_limit and self.daily_used + 1 > self.daily_limit:
                return None
            self._spend(1)
            d = self._get("time_series", {"symbol": symbol, "interval": "1day", "end_date": day, "outputsize": 5,
                                          "country": "United States"})
        except PriceError:
            return None
        vals = (d.get("values") or []) if isinstance(d, dict) else []
        best = None
        for v in vals:
            dt, cl = str(v.get("datetime") or "")[:10], _f(v.get("close"))
            if dt and dt <= day and cl and (best is None or dt > best[0]):
                best = (dt, cl)
        if best is None:
            return None
        self.cache[key] = {"fetched": datetime.now().isoformat(timespec="seconds"), "close": best[1], "date": best[0]}
        self._save(self.cache_path, self.cache)
        return best[1]

    # ------------------------------------------------------------ monthly history (historical multiples)
    def _hist_path(self):
        return os.path.join(os.path.dirname(self.cache_path), "monthly_history.json.gz")

    def history_cache(self):
        if not hasattr(self, "_hist"):
            self._hist = self._load(self._hist_path())
        return self._hist

    def save_history(self):
        if hasattr(self, "_hist"):
            self._save(self._hist_path(), self._hist)

    def monthly_history(self, symbol, months=132):
        """Split-adjusted month-end closes {'YYYY-MM': close} for the last `months` months (1 credit). Stored in
        the history cache with the fetch date; None on failure (nothing stored)."""
        if not self.available():
            return None
        if self.daily_limit and self.daily_used + 1 > self.daily_limit:
            raise DailyLimitReached("daily credit limit reached")
        self._spend(1)
        d = self._get("time_series", {"symbol": symbol, "interval": "1month", "outputsize": months,
                                      "country": "United States", "adjust": "splits"})
        vals = (d.get("values") or []) if isinstance(d, dict) else []
        series = {}
        for v in vals:
            dt, cl = str(v.get("datetime") or "")[:7], _f(v.get("close"))
            if len(dt) == 7 and cl and cl > 0:
                series[dt] = cl
        rec = {"fetched": self.today.isoformat(), "s": series}
        if not series:
            rec["error"] = str((d or {}).get("message") or "no monthly data")[:120] if isinstance(d, dict) else "no data"
        self.history_cache()[symbol] = rec
        return rec

    # ------------------------------------------------------------ FX
    def fx_rates(self, currencies, static):
        """{currency: (rate_to_usd, source)}. ECB reference rates first (one free request covers ~30 currencies),
        Twelve Data for the rest (1 credit each), else the config table."""
        out = {"USD": (1.0, "USD")}
        need = [c for c in sorted(set(currencies)) if c and c != "USD"]
        if not need:
            return out
        today = self.today.isoformat()
        ecb = None if self.fixtures_dir else ecb_rates_to_usd()
        for c in need:
            hit = self.fx_cache.get(c)
            if hit and hit.get("date") == today:
                out[c] = (hit["rate"], hit.get("src", "Twelve Data") + " " + hit["date"])
                continue
            if ecb and ecb[1].get(c):
                self.fx_cache[c] = {"rate": ecb[1][c], "date": today, "src": "ECB"}
                out[c] = (ecb[1][c], f"ECB {ecb[0]}")
                continue
            rate = None
            if self.available():
                try:
                    self._spend(1)
                    d = self._get("exchange_rate", {"symbol": f"{c}/USD"})
                    rate = _f(d.get("rate")) if isinstance(d, dict) else None
                except PriceError:
                    rate = None
            if rate and rate > 0:
                self.fx_cache[c] = {"rate": rate, "date": today}
                out[c] = (rate, "Twelve Data " + today)
            elif static.get(c):
                out[c] = (float(static[c]), "config.json fx_to_usd (static)")
        self._save(self.fx_path, self.fx_cache)
        return out
