"""Price history for the portal: 52-week ranges (Massive) and month-end price history (Twelve Data), plus the
peer-valuation table built from them.

  * 52-week high/low: every stored company, from weekly high/low files Massive fills one trading day per request
    (backfilled within a request budget per run, then one day per run).
  * Historical multiples: for companies on a Pass or Near-miss list and their 10 closest peers, month-end closes
    for ~11 years (Twelve Data, 1 credit per company, cached; refetched after ~6 months or a split). Multiples
    at each fiscal year end = price then x diluted shares (restated to today's share basis) vs that year's
    earnings, EBIT, cash flow etc. from SEC filings.

Information only: nothing here feeds a screening rule.
"""
import math
import statistics
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta

LISTED = ("PASS", "CHECK", "NEAR", "PRICE", "ONE")
FINANCIALS = ((6000, 6399),)
FINANCIAL_KEEP = ((6411, 6411),)     # insurance brokers behave like service companies
MULT_LABEL = {"pe": "P/E", "ev_ebit": "EV/EBIT", "fcf_yield": "FCF yield", "ev_ebitda": "EV/EBITDA",
              "ev_sales": "EV/Sales", "pb": "P/B"}
LOWER_IS_CHEAPER = {"pe": True, "ev_ebit": True, "fcf_yield": False, "ev_ebitda": True, "ev_sales": True,
                    "pb": True}


def _sic(ctx):
    try:
        return int(str(ctx.get("sic") or "")[:4])
    except ValueError:
        return None


def _in(sic, ranges):
    return sic is not None and any(a <= sic <= b for a, b in ranges)


def listed_ciks(state):
    out = set()
    for cls in (state.get("classes") or {}).values():
        out.update(c for c, k in cls.items() if k in LISTED)
    return out


# ------------------------------------------------------------------ closest peers
def closest_peers(ctxs, n=10):
    """{cik: [up to n peer ciks]}: same 4-digit industry code first, then 3- and 2-digit, each ranked by how close
    revenue is (log distance). Companies without a code or revenue get none."""
    by = {4: {}, 3: {}, 2: {}}
    for c, x in ctxs.items():
        s = str(x.get("sic") or "").strip()
        if x.get("events_only") or not s.isdigit() or len(s) < 2 or not (x.get("latest_revenue_usd") or 0) > 0:
            continue
        for k in (4, 3, 2):
            by[k].setdefault(s[:k], []).append(c)
    out = {}
    for c, x in ctxs.items():
        s = str(x.get("sic") or "").strip()
        rev = x.get("latest_revenue_usd") or 0
        if x.get("events_only") or not s.isdigit() or len(s) < 2 or rev <= 0:
            continue
        chosen, seen = [], {c}
        for k in (4, 3, 2):
            pool = [p for p in by[k].get(s[:k], []) if p not in seen]
            pool.sort(key=lambda p: abs(math.log(ctxs[p]["latest_revenue_usd"] / rev)))
            for p in pool:
                if len(chosen) >= n:
                    break
                chosen.append(p)
                seen.add(p)
            if len(chosen) >= n:
                break
        out[c] = chosen
    return out


# ------------------------------------------------------------------ refresh (screen run and daily run)
def update(state, prices, cfg, daily=False, log=print, today=None):
    """52-week ranges for every company and month-end histories for listed companies + peers, within the request
    budgets in config 'portal'. Massive and Twelve Data run side by side (separate rate limits)."""
    today = today or date.today()
    pc = cfg.get("portal") or {}
    ctxs = state["ctxs"]
    peers = closest_peers(ctxs, int(pc.get("peers", 10)))
    state["peers10"] = peers
    if prices is None or not prices.available():
        return
    tick = sorted({x["ticker"] for x in ctxs.values() if not x.get("events_only")})
    m_budget = int(pc.get("range_days_per_daily_run" if daily else "range_days_per_screen_run", 100))
    t_budget = int(pc.get("history_per_daily_run" if daily else "history_per_screen_run", 200))

    def ranges():
        r = prices.ranges_52w(tick, budget=m_budget) if hasattr(prices, "ranges_52w") else {}
        need = int(pc.get("range_min_days", 240))
        n = 0
        for x in ctxs.values():
            v = r.get(x["ticker"])
            for k in ("hi_52w", "lo_52w", "range_days"):
                x.pop(k, None)
            if v and v["days"] >= need:
                x["hi_52w"], x["lo_52w"], x["range_days"] = v["hi"], v["lo"], v["days"]
                n += 1
        log(f"  52-week range available for {n} companies")

    def histories():
        td = getattr(prices, "td", None)
        if td is None or not td.available() or t_budget <= 0:
            return
        fetch_histories(state, td, peers, t_budget, int(pc.get("history_refresh_days", 180)), today, log)

    with ThreadPoolExecutor(max_workers=2) as ex:
        futs = [ex.submit(ranges), ex.submit(histories)]
        for f in futs:
            try:
                f.result()
            except Exception as e:  # noqa: BLE001 - price history is information only; never fail the run
                log(f"  WARNING: price history step failed: {type(e).__name__}: {e}")


def _needs(rec, ctx, refresh_days, today):
    if not rec:
        return True
    try:
        age = (today - date.fromisoformat(rec["fetched"][:10])).days
    except (KeyError, ValueError):
        return True
    if rec.get("error"):
        return age > 30
    if age > refresh_days:
        return True
    if any(d > rec["fetched"] for d, *_ in (ctx.get("recent_splits") or [])):
        return True           # split since the fetch: the adjusted series changed
    end = str(ctx.get("latest_fy_end") or "")[:7]
    return bool(end) and end not in rec.get("s", {}) and age > 30


def fetch_histories(state, td, peers, budget, refresh_days, today, log=print):
    from .prices import DailyLimitReached, PriceError, td_symbol
    ctxs = state["ctxs"]
    listed = sorted(listed_ciks(state), key=lambda c: -(ctxs[c].get("market_cap_usd") or 0) if c in ctxs else 0)
    order, seen = [], set()
    for group in ([c for c in listed if c in ctxs], [p for c in listed for p in peers.get(c, [])]):
        for c in group:
            if c not in seen and c in ctxs and not ctxs[c].get("events_only"):
                seen.add(c)
                order.append(c)
    cache = td.history_cache()
    todo = [c for c in order if _needs(cache.get(td_symbol(ctxs[c]["ticker"])), ctxs[c], refresh_days, today)]
    got = 0
    for c in todo[:budget]:
        try:
            td.monthly_history(td_symbol(ctxs[c]["ticker"]))
            got += 1
        except DailyLimitReached:
            log("  Twelve Data daily limit reached - price history continues next run")
            break
        except PriceError as e:
            log(f"  Twelve Data history: {e}")
            break
        if got % 50 == 0:
            td.save_history()
    td.save_history()
    have = sum(1 for c in order if (cache.get(td_symbol(ctxs[c]["ticker"])) or {}).get("s"))
    log(f"  Price history: {got} fetched this run; {have} of {len(order)} listed companies and peers covered, "
        f"{max(0, len(todo) - got)} still to fetch")


# ------------------------------------------------------------------ historical multiples
def _price_at(series, end):
    if not end:
        return None
    y, m = int(end[:4]), int(end[5:7])
    for _ in range(2):
        v = series.get(f"{y:04d}-{m:02d}")
        if v:
            return v
        m -= 1
        if m == 0:
            y, m = y - 1, 12
    return None


def year_multiples(ctx, model, series):
    """[(fy, {multiple: value})] at each fiscal year end, or (None, reason). USD reporters with a verified market
    cap only (ADR ratios and share classes make the rest unreliable)."""
    from .massive import split_factor
    if not model or not series:
        return None, "no price history yet"
    if model.get("currency") != "USD":
        return None, "reports in a foreign currency"
    years = model["years"]
    last = years[-1]
    mcap_now, px_now = ctx.get("market_cap_usd"), ctx.get("price")
    if not (mcap_now and px_now and last.get("shares_basis")):
        return None, "no verified market cap"
    f = split_factor(ctx.get("recent_splits") or [], after=last.get("end") or "")
    shares_today = last["shares_basis"] / (f or 1.0)
    k = mcap_now / (px_now * shares_today)
    if not 0.65 <= k <= 1.5:
        return None, "share count doesn't match the market cap (share classes?)"
    out = []
    for y in years:
        px, sh = _price_at(series, y.get("end")), y.get("shares_basis")
        if not px or not sh:
            continue
        mcap = px * sh / (f or 1.0) * k
        ev = mcap + (y.get("x_total_debt") or 0) - (y.get("x_cash_and_sti") or 0) + (y.get("minority_interest") or 0)
        m = {}
        ni, ebit, ebitda = y.get("net_income"), y.get("x_operating_income"), y.get("x_ebitda")
        rev, fcf, eq = y.get("revenue"), y.get("x_fcf"), y.get("equity")
        if ni and ni > 0:
            m["pe"] = mcap / ni
        if ebit and ebit > 0 and ev > 0:
            m["ev_ebit"] = ev / ebit
        if ebitda and ebitda > 0 and ev > 0:
            m["ev_ebitda"] = ev / ebitda
        if rev and rev > 0 and ev > 0:
            m["ev_sales"] = ev / rev
        if fcf is not None and mcap > 0:
            m["fcf_yield"] = fcf / mcap
        if eq and eq > 0:
            m["pb"] = mcap / eq
        out.append((y["fy"], m))
    return (out, "") if out else (None, "no fiscal-year-end prices")


def averages(ym):
    """{multiple: (avg of last 3 years, avg of last 10 years, years used)} - mean of the meaningful values."""
    out = {}
    for k in MULT_LABEL:
        vals = [m[k] for _, m in ym if k in m]
        if not vals:
            continue
        out[k] = (statistics.fmean(vals[-3:]), statistics.fmean(vals[-10:]), len(vals[-10:]))
    return out


def current_multiples(ctx):
    m = {k: ctx.get(k) for k in ("pe", "ev_ebit", "fcf_yield", "ev_ebitda", "ev_sales")}
    eq, mc = ctx.get("bs_equity"), ctx.get("market_cap_usd")
    if eq and eq > 0 and mc and ctx.get("currency") == "USD":
        m["pb"] = mc / eq
    return {k: v for k, v in m.items() if isinstance(v, (int, float)) and math.isfinite(v)
            and (k == "fcf_yield" or v > 0)}


def choose_multiples(ctx, peer_ctxs, models):
    """Which multiples the industry is valued on: financials -> P/E, P/B; loss-making -> EV/Sales; otherwise
    P/E, EV/EBIT and FCF yield, plus EV/EBITDA where the group spends little on capex (< 3% of sales)."""
    sic = _sic(ctx)
    if _in(sic, FINANCIALS) and not _in(sic, FINANCIAL_KEEP):
        return ["pe", "pb"]
    group = [ctx] + peer_ctxs
    ebits = [x.get("ttm_operating_income") for x in group if x.get("ttm_operating_income") is not None]
    if (ctx.get("ttm_operating_income") or 0) <= 0 or (ebits and statistics.median(ebits) <= 0):
        return ["ev_sales"]
    out = ["pe", "ev_ebit", "fcf_yield"]
    ratios = []
    for x in group:
        mdl = models.get(str(x.get("cik"))) or models.get(x.get("cik"))
        y = (mdl or {}).get("years", [{}])[-1] if mdl else {}
        if y.get("x_capex") is not None and y.get("revenue"):
            ratios.append(y["x_capex"] / y["revenue"])
    if ratios and statistics.median(ratios) < 0.03:
        out.append("ev_ebitda")
    return out


def _rel(k, now, ref):
    """Negative = cheaper than the reference (for every multiple, including FCF yield where higher is cheaper)."""
    if now is None or ref is None:
        return None
    if LOWER_IS_CHEAPER[k]:
        return (now / ref - 1) if (ref > 0 and now > 0) else None
    return (ref - now) / abs(ref) if ref else None


def _verdict(k, now, own, peer_med, band=0.10):
    """'cheap' / 'expensive' when the company is >10% cheaper / dearer than BOTH its own history and its peers'
    median (or the one available), 'mixed' when they disagree, 'in line' otherwise."""
    rel = [d for d in (_rel(k, now, own), _rel(k, now, peer_med)) if d is not None]
    if not rel:
        return None
    if all(d < -band for d in rel):
        return "cheap"
    if all(d > band for d in rel):
        return "expensive"
    if any(d < -band for d in rel) and any(d > band for d in rel):
        return "mixed"
    return "in line"


def peer_valuation(c, state, td_cache, ym_cache=None):
    """The company page's 'valuation against peers' table (information only)."""
    from .prices import td_symbol
    ctxs, models = state["ctxs"], state.get("models") or {}
    ym_cache = {} if ym_cache is None else ym_cache
    ctx = ctxs[c]
    peers = [p for p in (state.get("peers10") or {}).get(c, []) if p in ctxs]

    def ym(x):
        if x not in ym_cache:
            rec = td_cache.get(td_symbol(ctxs[x]["ticker"])) or {}
            r, why = year_multiples(ctxs[x], models.get(x), rec.get("s"))
            ym_cache[x] = (averages(r) if r else {}, why, r)
        return ym_cache[x]

    mults = choose_multiples(ctx, [ctxs[p] for p in peers], models)
    rows = []
    for x in [c] + peers:
        avg, why, _ = ym(x)
        now = current_multiples(ctxs[x])
        v = {}
        for k in mults:
            a = avg.get(k)
            v[k] = [now.get(k), a[0] if a else None, a[1] if a else None, a[2] if a else 0]
        rows.append({"t": ctxs[x]["ticker"], "n": ctxs[x].get("name"), "me": x == c,
                     "rev": ctxs[x].get("latest_revenue_usd"), "v": v, "why": "" if avg else why})
    verdict = {}
    for k in mults:
        now = rows[0]["v"][k][0]
        own = rows[0]["v"][k][2] if rows[0]["v"][k][2] is not None else rows[0]["v"][k][1]
        pv = [r["v"][k][0] for r in rows[1:] if r["v"][k][0] is not None]
        verdict[k] = {"v": _verdict(k, now, own, statistics.median(pv) if len(pv) >= 3 else None),
                      "peer_med": statistics.median(pv) if len(pv) >= 3 else None}
    votes = [x["v"] for x in verdict.values() if x["v"]]
    overall = None
    if votes:
        for lab in ("cheap", "expensive"):
            if votes.count(lab) > len(votes) / 2:
                overall = lab
        overall = overall or ("mixed" if "mixed" in votes or ("cheap" in votes and "expensive" in votes) else "in line")
    return {"mult": mults, "rows": rows, "verdict": verdict, "overall": overall}


def fy_prices(c, state, td_cache):
    """{fy: price at fiscal year end} for the Excel model (split-adjusted to today), when available."""
    from .prices import td_symbol
    ctx, mdl = state["ctxs"][c], (state.get("models") or {}).get(c)
    rec = td_cache.get(td_symbol(ctx["ticker"])) or {}
    if not mdl or not rec.get("s"):
        return {}
    return {y["fy"]: p for y in mdl["years"] if (p := _price_at(rec["s"], y.get("end")))}
