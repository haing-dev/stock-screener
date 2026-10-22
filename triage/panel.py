"""The monthly panel: every US company at every month-end, as an investor could have seen it that day.

Built on the point-in-time backtest of qs/ (validation/PROTOCOL.md): Massive's 'all US stocks' bars for each
month-end (formation day d) and the next trading day (entry day e), unadjusted; SEC companyfacts entries filed before d;
the live pipeline's metrics and valuation, unchanged. Only US companies are kept: latest annual report a 10-K,
reporting in US dollars, common stock (Massive type CS) on NYSE, Nasdaq or NYSE American.

One record per company and month (cache/tri/panel/<ym>.json.gz):
  tk nm sic sym ex tks       ticker, name, SIC code, Massive symbol, exchange, all tickers
  px mc ev adv               close at d, market cap and EV (only when the share count checks out), avg daily $ traded
  dd r12                     close vs the highest of the previous 12 month-end closes; price change over 12 months
  ebit ebitda fcf rev ni     last 12 months (from 10-Qs and 10-Ks filed before d)
  fyebit fyebitda das        latest fiscal year operating income and EBITDA; depreciation share of EBITDA
  nd debtok                  net debt (debt - cash - investments) on the latest balance sheet; a debt tag was found
  yrs ytot ylf xlag          years with data, years in total, years since the latest fiscal year end, filed-not-in-XBRL
  rc3 rc ytdg fyg            revenue growth: 3 years, ~10 years, year-to-date, latest fiscal year
  roic roics gm gprep        median ROIC, share of years with ROIC >= 10%, gross margin, gross profit reported
  em3 om3 sga3 sh3           3-year change in EBITDA margin, operating margin, SG&A / revenue; share count growth
  fcfc lossy revfy rf        FCF / net income, operating-loss years, latest revenue, red-flag count
  u                          universes the company belongs to: broad, core, emerging
"""
import os
from datetime import date, timedelta

from qs.backtest import CompanyStore, contexts_at
from qs.backtest_support import read_json, write_json
from qs.btprices import adjusted_close
from qs.massive import m_symbol
from qs.screens import u_broad, u_core, u_emerging

from . import paths as P

EXCHANGES = ["NYSE", "Nasdaq", "NYSE American"]


def grid_path():
    return os.path.join(P.TRI, "grid.json.gz")


def univ_path():
    return os.path.join(P.TRI, "universe.json.gz")
INDEX_SYMBOLS = ("SPY", "IWM")


def _r(v, n=6):
    return None if v is None else round(float(v), n)


def is_us(info, u, ctx):
    la = info.get("latest_annual") or {}
    return la.get("form") in ("10-K", "10-KT") and (u or {}).get("type") == "CS" and ctx.get("currency") == "USD"


def record(c, ctx, info, cfg, r12):
    ok = bool(ctx.get("val_ok"))
    gm = ctx.get("ttm_gross_margin")
    if gm is None:
        gm = ctx.get("gross_margin_latest")
    uni = [k for k, fn in (("broad", u_broad), ("core", u_core), ("emerging", u_emerging)) if fn(info, ctx, cfg)[0]]
    return {
        "tk": ctx.get("ticker"), "nm": ctx.get("name"), "sic": str(ctx.get("sic") or ""), "sym": ctx.get("_sym"),
        "ex": ctx.get("exchange"), "tks": ctx.get("all_tickers") or [],
        "px": _r(ctx.get("price")), "mc": _r(ctx.get("market_cap_usd"), 0) if ok else None,
        "ev": _r(ctx.get("ev_usd"), 0) if ok else None, "adv": _r(ctx.get("adv_usd"), 0),
        "dd": _r(ctx.get("drawdown_12m")), "r12": _r(r12),
        "ebit": _r(ctx.get("ttm_operating_income"), 0), "ebitda": _r(ctx.get("ttm_ebitda"), 0),
        "fcf": _r(ctx.get("ttm_fcf"), 0), "rev": _r(ctx.get("ttm_revenue"), 0), "ni": _r(ctx.get("ttm_net_income"), 0),
        "fyebit": _r(ctx.get("latest_fy_operating_income"), 0), "fyebitda": _r(ctx.get("latest_fy_ebitda"), 0),
        "das": _r(ctx.get("da_share_of_ebitda")),
        "nd": _r(ctx.get("bs_net_debt"), 0), "debtok": bool(ctx.get("bs_debt_found")),
        "yrs": ctx.get("years_with_data"), "ytot": ctx.get("years_total"), "ylf": _r(ctx.get("years_since_latest_fy"), 3),
        "xlag": bool(ctx.get("xbrl_lags_annual_report")),
        "rc3": _r(ctx.get("revenue_cagr_3y")), "rc": _r(ctx.get("revenue_cagr")), "ytdg": _r(ctx.get("ytd_revenue_growth")),
        "fyg": _r(ctx.get("revenue_growth_latest_fy")),
        "roic": _r(ctx.get("roic_median")), "roics": _r(ctx.get("roic_share_above_floor")), "gm": _r(gm),
        "gprep": bool(ctx.get("gross_profit_reported")),
        "em3": _r(ctx.get("ebitda_margin_change_3y")), "om3": _r(ctx.get("operating_margin_change_3y")),
        "sga3": _r(ctx.get("sga_ratio_change_3y")), "sh3": _r(ctx.get("share_count_cagr_3y")),
        "fcfc": _r(ctx.get("fcf_conversion")), "lossy": ctx.get("operating_loss_years"),
        "revfy": _r(ctx.get("latest_revenue_usd"), 0), "rf": ctx.get("red_flag_count"), "u": uni,
    }


def price_change_12m(sym, d, px, hist, splits):
    """Close at d vs the month-end close about a year earlier (split-adjusted), or None."""
    dd = date.fromisoformat(d)
    cands = [x for x in hist if 340 <= (dd - date.fromisoformat(x)).days <= 390]
    if not cands or not px:
        return None
    x = min(cands, key=lambda k: abs((dd - date.fromisoformat(k)).days - 365))
    b = hist[x].get(sym)
    if not b or not b[1]:
        return None
    old = adjusted_close(b[1], splits.get(sym) or [], x, d)
    return px / old - 1 if old else None


def build(grid, univ, cfg, splits, log=print, refresh=False):
    """Write a panel file for every grid month not done yet. Returns the months written."""
    P.ensure(P.PANEL)
    store = CompanyStore()
    fx = {"USD": (1.0, "USD")}
    hist, done = {}, []
    for g in grid:
        hist[g["d"]] = g["bars_d"]
        for old in [k for k in hist if (date.fromisoformat(g["d"]) - date.fromisoformat(k)).days > 400]:
            hist.pop(old)
        path = os.path.join(P.PANEL, f"{g['ym']}.json.gz")
        if os.path.exists(path) and not refresh:
            continue
        u = univ.get(g["d"]) or {}
        ctxs, subs, _extra = contexts_at(g, u, store, cfg, splits, fx, hist)
        recs = {}
        for c, ctx in ctxs.items():
            if ctx.get("events_only") or not is_us(subs.get(c) or {}, u.get(c), ctx):
                continue
            sym = ctx.get("_sym")
            r12 = price_change_12m(sym, g["d"], ctx.get("price"), {k: v for k, v in hist.items() if k < g["d"]},
                                   splits)
            recs[str(c)] = record(c, ctx, subs.get(c) or {}, cfg, r12)
        write_json(path, {"ym": g["ym"], "d": g["d"], "e": g["e"], "companies": recs})
        done.append(g["ym"])
        log(f"  panel {g['ym']}: {len(recs)} US companies of {len(ctxs)}")
    return done


def load(ym):
    return read_json(os.path.join(P.PANEL, f"{ym}.json.gz"))


def months():
    if not os.path.isdir(P.PANEL):
        return []
    return sorted(f[:-len(".json.gz")] for f in os.listdir(P.PANEL) if f.endswith(".json.gz"))


# ------------------------------------------------------------------ the scan grid (twice a month)
SETTLE_DAYS = 3          # a scan day counts once its prices and the next day's open are surely out


def nominal_scans(start, until):
    """Nominal scan dates (the 15th and the month's last day) from month `start` (y, m) to day `until`."""
    out, (y, m) = [], start
    while date(y, m, 1) <= until:
        last = (date(y + (m == 12), m % 12 + 1, 1) - timedelta(days=1))
        for n in (date(y, m, 15), last):
            if n <= until:
                out.append(n)
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    return out


def latest_scan(today):
    return nominal_scans((today.year - 1, today.month), today - timedelta(days=SETTLE_DAYS))[-1]


def scan_grid(btp, start, today):
    """[{'ym': scan day (period id), 'd', 'bars_d', 'e', 'bars_e'}]: for each nominal date the last trading day on or
    before it (d) and the next trading day (e, entry). Unadjusted 'all US stocks' bars, cached per day."""
    out = []
    for n in nominal_scans(start, today - timedelta(days=SETTLE_DAYS)):
        d, bd = btp._first_day_with_bars(n, -1)
        if not d or (out and d <= out[-1]["d"]):
            continue
        e, be = btp._first_day_with_bars(date.fromisoformat(d) + timedelta(days=1), +1)
        if not e:
            continue
        out.append({"ym": d, "d": d, "bars_d": bd, "e": e, "bars_e": be})
    return out


# ------------------------------------------------------------------ the grid (shared with qs/validate.py's format)
def save_grid(grid, univ):
    P.ensure(P.TRI)
    write_json(grid_path(), [{k: g[k] for k in ("ym", "d", "e")} for g in grid])
    write_json(univ_path(), univ)


def load_grid(btp):
    return [dict(g, bars_d=btp.bars(g["d"]), bars_e=btp.bars(g["e"])) for g in (read_json(grid_path()) or [])]


def load_univ():
    raw = read_json(univ_path()) or {}
    return {d: {int(c): u for c, u in us.items()} for d, us in raw.items()}


# ------------------------------------------------------------------ daily mark-to-market
def mark(m, today=None, log=print):
    """Closes of the latest trading day Massive serves (one 'all US stocks' request), unadjusted:
    {'day': 'YYYY-MM-DD', 'closes': {SYMBOL: close}}. Kept in cache/tri/mark.json.gz."""
    today = today or m.today
    for back in range(0, 8):
        d = today - timedelta(days=back)
        if d.weekday() >= 5:
            continue
        try:
            bars = m.day(d, folder="mark", adjusted=False)
        except Exception as e:  # noqa: BLE001 - keep the previous mark
            log(f"  Massive {d}: {e}")
            continue
        if bars:
            out = {"day": d.isoformat(), "closes": {s: b[1] for s, b in bars.items() if b and b[1]}}
            write_json(P.MARK, out)
            log(f"Mark-to-market: {d} ({len(out['closes'])} closes)")
            return out
    return read_json(P.MARK)


def load_mark():
    return read_json(P.MARK)


def symbol(rec):
    return rec.get("sym") or m_symbol(rec.get("tk") or "")
