"""Web portal support: keep the screen state between runs, re-price it daily, and export the (encrypted)
data files the static site in site/ reads.

  state  (cache/state/state.json.gz)  - every screened company's metrics ('ctx') and which screens it belongs to,
                                        written by the 15-day screen run, re-priced by the daily job
  site/data/*.bin                      - gzip'd JSON, AES-GCM encrypted with a key derived from PORTAL_PASSWORD
                                        (PBKDF2-SHA256); the browser decrypts with the same password
"""
import base64
import gzip
import json
import math
import os
import statistics
from collections import Counter, defaultdict
from datetime import date, datetime

from . import __version__
from .config import CACHE_DIR, ROOT
from .report import _fmt_val
from .industry import model_template
from .screens import BY_ID, SCREENS

STATE_PATH = os.path.join(CACHE_DIR, "state", "state.json.gz")
SITE_DATA = os.path.join(ROOT, "site", "data")
PBKDF2_ITER = 250000

# price-dependent fields written by valuation.value() - cleared before every re-pricing
VAL_KEYS = ("price", "price_date", "price_open", "price_source", "market_cap_usd", "ev_usd", "val_ok", "val_issue",
            "shares_used", "shares_source", "adv_usd", "listing_type", "mcap_to_public_float", "float_check",
            "ev_ebit", "ev_ebitda", "ev_sales", "pe", "earnings_yield", "fcf_yield", "ev_normalized_ebit",
            "ev_incl_lt_investments_usd", "ev_to_liquid_assets", "mcap_to_liquid_assets",
            "price_to_tangible_book", "mcap_to_net_cash", "fcf_yield_5y", "insider_share", "insider_issue", "insider_basis",
            "drawdown_12m", "high_12m_used", "funding_gap_to_mcap", "cash_after_burn_usd",
            "mcap_to_cash_after_burn")

# metric: (label, format, which direction is better[, True = only positive values are meaningful, e.g. P/E])
METRICS = {
    "pe": ("P/E", "x", "low", True),
    "ev_ebitda": ("EV/EBITDA", "x", "low", True),
    "ev_ebit": ("EV/EBIT", "x", "low", True),
    "ev_sales": ("EV/Sales", "x", "low", True),
    "ev_normalized_ebit": ("EV / avg EBIT", "x", "low", True),
    "ev_to_liquid_assets": ("EV / cash", "x", "low"),
    "fcf_yield": ("FCF yield", "pct", "high"),
    "roic_median": ("ROIC (10y median)", "pct", "high"),
    "revenue_cagr_5y": ("Revenue CAGR (5y)", "pct", "high"),
    "roic_latest": ("ROIC (latest)", "pct", "high"),
    "revenue_cagr": ("Sales growth /yr", "pct", "high"),
    "revenue_cagr_3y": ("Sales growth /yr (3y)", "pct", "high"),
    "gross_margin_latest": ("Gross margin", "pct", "high"),
    "ttm_operating_margin": ("Op. margin (TTM)", "pct", "high"),
    "operating_margin_median": ("Op. margin (10y median)", "pct", "high"),
    "net_debt_to_ebitda": ("Net debt / EBITDA", "x", "low"),
    "net_debt_to_norm_ebitda": ("Net debt / avg EBITDA", "x", "low"),
    "op_margin_percentile_10y": ("Margin in own 10y range", "pct", "low"),
    "cash_runway_years": ("Cash runway (years)", "yrs", "high"),
    "debt_to_liquid_assets": ("Debt / cash", "x", "low"),
    "market_cap_usd": ("Market cap", "usd", None),
    "ttm_revenue_usd": ("Revenue (TTM)", "usd", None),
    "insider_share": ("Insider share", "pct", None),
    "capex_to_ocf_3y": ("Capex / op. cash flow", "pct", "low"),
    "mcap_to_net_cash": ("Mkt cap / net cash", "x", "low", True),
    "price_to_tangible_book": ("Price / tangible book", "x", "low", True),
    "fcf_yield_5y": ("FCF yield (5y avg)", "pct", "high"),
    "returns_to_capex_5y": ("Buybacks+divs / capex", "x", "high"),
    "drawdown_12m": ("From 12m high", "pct", None),
    "red_flag_count": ("Red flags", "n", None),
    "operating_margin_change_3y": ("Op. margin chg (3y)", "pct", "high"),
}
PRICE_METRICS = {"pe", "ev_ebitda", "ev_ebit", "ev_sales", "ev_normalized_ebit", "ev_to_liquid_assets", "fcf_yield",
                 "market_cap_usd", "insider_share", "mcap_to_net_cash", "price_to_tangible_book", "fcf_yield_5y",
                 "drawdown_12m"}
# the same columns on every screen (company, price vs open and the 52-week range are fixed columns on the site)
TABLE_METRICS = ["pe", "ev_ebit", "fcf_yield", "roic_median", "revenue_cagr_5y"]
SCREEN_METRICS = {}
SCREEN_GROUPS = {"owners": "From the new interviews", "red_flags": "Avoid list", "tech": "Technology"}
STATUS_KEEP = ("PASS", "CHECK", "NEAR", "PRICE", "ONE")


# ------------------------------------------------------------------ json helpers
def _jsonable(o):
    try:
        import numpy as np
        if isinstance(o, np.bool_):
            return bool(o)
        if isinstance(o, np.integer):
            return int(o)
        if isinstance(o, np.floating):
            return float(o)
    except ImportError:  # pragma: no cover
        pass
    if isinstance(o, (set, frozenset)):
        return sorted(o)
    if isinstance(o, (date, datetime)):
        return o.isoformat()
    return str(o)


def _clean(x):
    """NaN/inf -> None (browsers' JSON.parse rejects NaN)."""
    if isinstance(x, float):
        return x if math.isfinite(x) else None
    if isinstance(x, dict):
        return {k: _clean(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_clean(v) for v in x]
    return x


def write_gz_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with gzip.open(tmp, "wt", encoding="utf-8") as f:
        json.dump(obj, f, default=_jsonable)
    os.replace(tmp, path)


def read_gz_json(path):
    try:
        with gzip.open(path, "rt", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError, EOFError):
        return None


# ------------------------------------------------------------------ state
def classes_of(results):
    return {sid: {str(c): r["class"] for c, r in res.items()} for sid, res in results.items()}


def save_state(results, ctxs, records, run_info, today, path=STATE_PATH, models=None):
    state = {
        "version": 1, "screener_version": __version__, "screened_on": today.isoformat(),
        "priced_on": today.isoformat(), "run_info": run_info,
        "ctxs": {str(c): ctx for c, ctx in ctxs.items()},
        "membership": {sid: {str(c): r.get("universe_note", "") for c, r in res.items()}
                       for sid, res in results.items()},
        "classes": classes_of(results),
        "records": {str(c): {k: rec.get(k) for k in ("ticker", "name", "exchange", "sic", "industry", "stage")}
                    for c, rec in records.items()},
        "models": {str(c): mdl for c, mdl in (models or {}).items()},
    }
    write_gz_json(path, state)
    return state


def load_state(path=STATE_PATH):
    return read_gz_json(path)


def evaluate_state(state, cfg):
    """Apply every screen to the stored companies (same code path as the screen run)."""
    results = {}
    ctxs = state["ctxs"]
    for sid, mem in state["membership"].items():
        s = BY_ID[sid]
        res = {}
        for c, note in mem.items():
            ctx = ctxs.get(c)
            if ctx is None:
                continue
            r = s.evaluate(ctx, cfg, priced=True)
            r["universe_note"] = note
            res[c] = r
        results[sid] = res
    return results


def reprice(state, prices, cfg, today, log=print):
    """Daily job: new end-of-day prices for every stored company, then re-apply the screens."""
    from .prices import td_symbol
    from .valuation import value
    ctxs = state["ctxs"]
    last = {}
    for c, ctx in ctxs.items():
        if ctx.get("price") and ctx.get("price_date"):
            adv = ctx.get("adv_usd")
            last[c] = {"ok": True, "reason": "", "symbol": ctx["ticker"], "name": None, "price": ctx["price"],
                       "open": ctx.get("price_open"), "price_date": ctx["price_date"],
                       "avg_volume": (adv / ctx["price"]) if adv else None, "listing_type": ctx.get("listing_type"),
                       "source": (ctx.get("price_source") or "").replace(" (last known)", "") + " (last known)"}
        for k in list(ctx):
            if k in VAL_KEYS or k.endswith("_unverified"):
                del ctx[k]
    # splits since the screen run: today's prices are on the new basis, so the stored 12-month high and share
    # counts must be too
    if hasattr(prices, "splits"):
        from datetime import timedelta
        from .massive import m_symbol, split_factor
        sp = prices.splits((today - timedelta(days=760)).isoformat())
        for ctx in ctxs.values():
            if sp is None:
                if prices.m.available():
                    ctx["splits_unknown"] = True
                continue
            ctx.pop("splits_unknown", None)
            mine = sp.get(m_symbol(ctx["ticker"])) or []
            ctx["recent_splits"] = mine
            if ctx.get("high_12m") and ctx.get("high_12m_asof"):
                ctx["high_12m"] *= split_factor(mine, after=ctx["high_12m_asof"], until=today.isoformat())
                ctx["high_12m_asof"] = today.isoformat()
    order = sorted(ctxs, key=lambda c: -(ctxs[c].get("latest_revenue_usd") or 0))
    quotes = prices.quotes([(ctxs[c]["ticker"], ctxs[c].get("exchange")) for c in order])
    stale_days = cfg.get("price_max_staleness_days", 7)
    kept = 0
    for c in order:
        q = quotes.get(ctxs[c]["ticker"])
        old = last.get(c)
        if (not q or not q.get("ok")) and old:
            try:
                age = (today - date.fromisoformat(old["price_date"])).days
            except ValueError:
                age = 999
            if age <= stale_days:
                quotes[ctxs[c]["ticker"]] = old     # no new quote today: keep the last good one (up to 7 days)
                kept += 1
    if kept:
        log(f"  {kept} companies keep their last known price (no new quote today)")
    currencies = {ctx.get("currency") for ctx in ctxs.values() if ctx.get("currency")}
    static = {k: v for k, v in (cfg.get("fx_to_usd") or {}).items() if isinstance(v, (int, float))}
    fx = prices.fx_rates(currencies, static)
    foreign = any(str(ctx.get("latest_annual_form") or "").startswith("20-F") for ctx in ctxs.values())
    types = prices.instrument_types() if foreign else {}
    for c in order:
        ctx = ctxs[c]
        rate = (fx.get(ctx.get("currency")) or (ctx.get("fx_rate"), None))[0]
        info = {"all_tickers": ctx.get("all_tickers") or [ctx["ticker"]], "name": ctx.get("name"),
                "latest_annual": {"form": ctx.get("latest_annual_form")}}
        ctx.update(value(ctx, info, quotes.get(ctx["ticker"]), rate, today, td=prices,
                         listing_type=types.get(td_symbol(ctx["ticker"]))))
    results = evaluate_state(state, cfg)
    state["classes"] = classes_of(results)
    state["priced_on"] = today.isoformat()
    log(f"Re-priced {sum(1 for c in ctxs.values() if c.get('price'))}/{len(ctxs)} companies")
    return results


# ------------------------------------------------------------------ peers
def _sic(ctx):
    s = str(ctx.get("sic") or "").strip()
    return s if s.isdigit() and len(s) >= 2 else None


def metric_value(ctx, k):
    """(value, verified?) - doubtful market-cap based figures are kept for display only."""
    v = ctx.get(k)
    if v is None and ctx.get(k + "_unverified") is not None:
        return ctx[k + "_unverified"], False
    if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
        return None, True
    return v, True


def peer_groups(ctxs, min_size=6):
    """Peers = companies with the same 4-digit SIC code; if fewer than min_size, the 3-digit group, then 2-digit.
    Returns ({group_id: group}, {cik: group_id}). Medians use verified values only (multiples: positive only)."""
    lv = {4: defaultdict(list), 3: defaultdict(list), 2: defaultdict(list)}
    for c, ctx in ctxs.items():
        s = _sic(ctx)
        if not s or ctx.get("events_only"):
            continue
        for n in (4, 3, 2):
            lv[n][s[:n]].append(c)
    assign, groups = {}, {}
    for c, ctx in ctxs.items():
        s = _sic(ctx)
        if not s or ctx.get("events_only"):
            continue
        for n in (4, 3, 2):
            members = lv[n][s[:n]]
            if len(members) >= min_size:
                gid = f"{n}:{s[:n]}"
                assign[c] = gid
                if gid not in groups:
                    groups[gid] = members
                break
    out = {}
    for gid, members in groups.items():
        n, code = gid.split(":")
        names = Counter((ctxs[m].get("industry") or "").strip() for m in members if ctxs[m].get("industry"))
        top = names.most_common(1)[0][0].title() if names else "Industry"
        label = top if n == "4" else f"Broader industry group SIC {code}{'x' * (4 - int(n))} (most common: {top})"
        med = {}
        for k, spec in METRICS.items():
            pos_only = len(spec) > 3 and spec[3]
            vals = []
            for m in members:
                v, ok = metric_value(ctxs[m], k)
                if v is None or not ok:
                    continue
                if pos_only and v <= 0:
                    continue
                vals.append(v)
            if len(vals) >= 3:
                med[k] = statistics.median(vals)
        big = sorted(members, key=lambda m: -(ctxs[m].get("latest_revenue_usd") or 0))[:8]
        out[gid] = {"label": label, "sic": code, "n": len(members), "med": med,
                    "top": [[ctxs[m]["ticker"], ctxs[m].get("name")] for m in big]}
    return out, assign


# ------------------------------------------------------------------ export
def _op_text(op):
    return {">=": "at least", "<=": "at most", ">": "above", "<": "below"}.get(op, op or "")


RULE_UNITS = {"years_with_data": " years of data", "years_total": " years of data",
              "years_since_latest_fy": " years since the last annual report",
              "operating_loss_years": " operating-loss years in 10", "operating_loss_years_5y":
              " loss year(s) in the last 5", "positive_ebit_years": " profitable years of the last 10",
              "bs_age_days": " days old", "fcf_conversion": " (free cash flow after stock pay / net income)",
              "net_debt_to_ocf": " (net debt / operating cash flow)",
              "net_debt_to_ebitda": " (net debt / EBITDA)", "net_debt_to_norm_ebitda": " (net debt / cycle-average EBITDA)",
              "interest_coverage": " (EBIT / interest)", "cash_runway_years": " years of cash",
              "debt_to_liquid_assets": " (debt / cash)", "ev_to_liquid_assets": " (EV / cash)",
              "ev_ebitda": " EV/EBITDA", "ev_ebit": " EV/EBIT", "ev_normalized_ebit": " EV / cycle-average EBIT",
              "roic_median": " ROIC, 10-year median", "roic_share_above_floor": " of years with ROIC above 10%",
              "revenue_cagr": " revenue growth a year", "revenue_cagr_3y": " revenue growth a year over 3 years",
              "share_count_cagr_3y": " share-count growth a year", "gross_margin_latest": " gross margin",
              "operating_margin_std": " swing in operating margin (std. dev.)",
              "op_margin_percentile_10y": " of its own 10-year margin range", "market_cap_usd": " market cap",
              "latest_revenue_usd": " revenue", "adv_usd": " traded a day",
              "gross_margin_change_2021_2023": " change in margin 2021-23",
              "insider_share": " owned by insiders", "capex_to_ocf_3y": " of operating cash flow spent on capex (3y)",
              "operating_margin_median": " operating margin, 10-year median", "positive_ebit_share": " of years profitable",
              "capex_to_da_3y": " (capex / depreciation, 3y)", "fcf_yield_5y": " 5-year average FCF yield",
              "ev_sales": " EV/Sales", "drawdown_12m": " from the 12-month high",
              "mcap_to_cash_after_burn": " (market cap / cash left after a year of burn, net of debt)",
              "sbc_to_fcf_3y": " stock pay / free cash flow (3y)", "incremental_roic_3y": " return on new capital (3y)"}


def _thr_text(thr, fmt):
    if isinstance(thr, (int, float)) and not isinstance(thr, bool):
        if fmt == "mult":
            return f"{thr:.1f}\u00d7" if thr < 100 else f"{thr:.0f}\u00d7"
        if fmt == "years":
            return f"{thr:.1f}"
        if fmt == "pct":
            return f"{thr:.0%}" if abs(thr * 100 - round(thr * 100)) < 1e-9 else f"{thr:.1%}"
    return _fmt_val(thr, fmt)


def rule_label(g, cfg, sid):
    if g.desc:
        return g.desc(cfg, sid) if callable(g.desc) else g.desc
    try:
        thr = g.threshold(cfg, sid)
    except (KeyError, TypeError):
        thr = None
    if thr is None or not g.op:
        return g.name
    unit = RULE_UNITS.get(g.metric, "")
    if g.metric == "ev_ebitda" and g.fmt == "mult":
        unit = " EV/EBITDA"
    return f"{_op_text(g.op)} {_thr_text(thr, g.fmt)}{unit}"


GATE_CODE = {"PASS": "P", "FAIL": "F", "NO DATA": "D", "N/A": "N", "PENDING": "D"}

# near-miss reasons on the site: "Miss due to <what> being <value> (needs <threshold>)" or "Miss due to insufficient
# information on <what>". SUBJECT names the measured quantity per metric; FAIL_TEXT replaces the whole phrase for rules
# whose value alone doesn't explain the miss.
SUBJECT = {
    "years_with_data": "years of data", "years_total": "years of data", "latest_revenue_usd": "revenue",
    "operating_loss_years": "operating-loss years in 10", "roic_median": "10-year median ROIC",
    "roic_share_above_floor": "share of years with ROIC above 10%", "revenue_cagr": "revenue growth a year",
    "fcf_conversion": "cash conversion (FCF after stock pay / net income)",
    "net_debt_to_ocf": "net debt / operating cash flow", "downturn_failures": "downturn record",
    "revenue_cagr_3y": "3-year revenue growth a year", "ttm_ebitda": "trailing EBITDA",
    "ytd_revenue_growth": "latest revenue growth", "gross_margin_latest": "gross margin",
    "ebitda_margin_change_3y": "3-year margin change", "share_count_cagr_3y": "share-count growth a year",
    "net_debt_to_ebitda": "net debt / EBITDA", "market_cap_usd": "market cap", "ev_ebitda": "EV/EBITDA",
    "adv_usd": "daily trading value", "ttm_operating_income": "trailing operating income", "ev_ebit": "EV/EBIT",
    "recession_2020_revenue_change": "the 2020 recession result", "recession_2009_revenue_change":
    "the 2008-09 recession result", "operating_loss_years_5y": "loss years in the last 5",
    "operating_margin_std": "operating-margin swing", "interest_coverage": "interest coverage",
    "maturities_covered": "debt maturities", "fcf_positive_years": "years of positive free cash flow",
    "gross_margin_change_2021_2023": "the 2021-23 margin change", "bs_age_days": "balance-sheet age (days)",
    "cash_runway_years": "cash runway", "debt_to_liquid_assets": "debt / cash", "ev_to_liquid_assets": "EV / cash",
    "mcap_to_cash_after_burn": "market cap / cash left after a year of burn", "positive_ebit_years":
    "profitable years of the last 10", "net_debt_to_norm_ebitda": "net debt / cycle-average EBITDA",
    "op_margin_percentile_10y": "margin position in its 10-year range", "ev_normalized_ebit":
    "EV / cycle-average EBIT", "insider_share": "insider ownership", "capex_to_ocf_3y": "capex / operating cash flow",
    "operating_margin_median": "10-year median operating margin", "mcap_to_net_cash": "price vs net cash",
    "ttm_ocf": "operating cash flow", "positive_ebit_share": "share of profitable years", "capex_to_da_3y":
    "capex / depreciation", "fcf_yield_5y": "5-year average FCF yield", "drawdown_12m": "the drop from the 12-month high",
    "ttm_fcf": "trailing free cash flow", "ev_sales": "EV/Sales", "red_flag_count": "warning signs",
    "rule_of_40": "growth + free cash flow after stock pay", "sbc_to_fcf_3y": "stock pay / free cash flow",
    "incremental_roic_3y": "3-year return on new capital", "dso_change_3y": "the change in receivable days",
    "operating_margin_change_3y": "the 3-year operating-margin change",
}
# 'needs ...' for rules whose threshold isn't one config number
NEED_TEXT = {
    "A5": lambda c: f"the 3-year rate minus {c['screens']['tech']['max_growth_fade'] * 100:.0f} points",
    "A7": lambda c: f"{c['screens']['tech']['min_gross_margin_software']:.0%} for software, rising for hardware",
    "A8": lambda c: "a rise",
    "A13": lambda c: (f"at most +{c['screens']['tech']['max_dso_change_days']:.0f} days for software; hardware "
                      "inventory below its 5-year high"),
    "A16": lambda c: (f"growth in points / {c['screens']['tech']['growth_points_per_sales_multiple']:g}, at most "
                      f"{c['screens']['tech']['max_ev_sales']:.0f}\u00d7"),
}
FAIL_TEXT = {
    "F11": "debt due within 2 years exceeding cash plus 2 years of free cash flow",
    "K4": "a price above both net cash and tangible book",
    "X3": "no recent spin-off or sale and a price within 40% of its 12-month high",
}
UNIT = {"years": " yrs", "int": ""}


def _nice(v, fmt):
    """Short display value for the site's reasons."""
    if v is None:
        return ""
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, (tuple, list)):
        return " / ".join(_nice(x, fmt) for x in v if x is not None)
    if not isinstance(v, (int, float)):
        return str(v)
    if fmt == "pct":
        return f"{v * 100:.0f}%" if abs(v) >= 0.1 else f"{v * 100:.1f}%"
    if fmt == "mult":
        return f"{v:.1f}\u00d7" if abs(v) < 100 else f"{v:.0f}\u00d7"
    if fmt == "usd":
        a = abs(v)
        return (f"${v / 1e9:.1f}B" if a >= 1e9 else f"${v / 1e6:.0f}M" if a >= 1e6 else f"${v / 1e3:.0f}K")
    if fmt == "years":
        return "cash-flow positive" if v >= 99 else f"{v:.1f} yrs"
    if fmt == "int":
        return f"{v:.0f}"
    return f"{v:.3g}" if isinstance(v, float) else str(v)


def _need(g, cfg, sid):
    if g.gid in NEED_TEXT:
        try:
            return NEED_TEXT[g.gid](cfg)
        except (KeyError, TypeError):
            return ""
    try:
        thr = g.threshold(cfg, sid)
    except (KeyError, TypeError):
        thr = None
    if thr is None or not g.op or isinstance(thr, bool):
        return ""
    return f"{_op_text(g.op)} {_nice(thr, g.fmt)}{UNIT.get(g.fmt, '') if g.fmt == 'int' else ''}"


def screen_payload(s, results, ctxs, cfg):
    gates = [{"id": g.gid, "name": g.name, "rule": rule_label(g, cfg, s.sid), "why": g.insight,
              "hard": not g.one_ok, "valuation": bool(g.valuation), "price": bool(g.needs_price),
              "hidden": bool(getattr(g, "hidden", False)), "what": SUBJECT.get(g.metric, g.name.lower()),
              "need": _need(g, cfg, s.sid), "ftxt": FAIL_TEXT.get(g.gid, "")} for g in s.gates]
    rows = []
    for c, r in results.items():
        codes, vals, notes = [], [], {}
        for g in s.gates:
            st, val, thr, note = r["gates"][g.gid]
            codes.append(GATE_CODE.get(st, "D"))
            vals.append("" if val is None else _nice(val, g.fmt))
            if note:
                notes[g.gid] = note
        rows.append({"c": c, "g": "".join(codes), "v": vals, "nt": notes, "h": list(r.get("holds", [])),
                     "cls": r["class"], "nr": r["failed"][0] if r["class"] == "NEAR" and r.get("failed") else None})
    from .screens import AVOID_SCREENS
    from .thesis import THESIS
    return {"id": s.sid, "title": s.title, "purpose": s.purpose, "gates": gates, "thesis": THESIS.get(s.sid),
            "metrics": SCREEN_METRICS.get(s.sid, TABLE_METRICS), "rows": rows,
            "avoid": s.sid in AVOID_SCREENS, "strict": bool(getattr(s, "strict", False))}


def company_payload(c, ctx, summaries, group_id, pv=None, has_model=False, holders=None, insiders=None):
    m, unverified, nm = {}, [], {}
    adr = "ADR ratio unknown" in (ctx.get("val_issue") or "")
    for k in METRICS:
        v, ok = metric_value(ctx, k)
        if v is not None:
            if not ok and adr:
                continue     # off by the ADR ratio (TSMC: 5x): show nothing rather than a wrong number
            m[k] = v
            if not ok:
                unverified.append(k)
        elif ctx.get(k + "_nm"):
            nm[k] = ctx[k + "_nm"]
    s = summaries.get(c) or {}
    ev = None
    if ctx.get("event_types"):
        ev = {"types": ctx.get("event_types"), "date": ctx.get("event_date"), "url": ctx.get("event_filing_url")}
    px = None
    if ctx.get("price") is not None:
        px = {"o": ctx.get("price_open"), "c": ctx.get("price"), "d": ctx.get("price_date"),
              "hi": ctx.get("hi_52w"), "lo": ctx.get("lo_52w")}
    return {"t": ctx["ticker"], "n": ctx.get("name"), "ex": ctx.get("exchange"), "sic": ctx.get("sic"),
            "ind": ctx.get("industry"), "cur": ctx.get("currency"), "px": px,
            "m": m, "mu": unverified, "nm": nm, "vi": ctx.get("val_issue") or "", "pg": group_id,
            "sum": s.get("text"), "url": ctx.get("latest_annual_url"), "fy": ctx.get("latest_fy"), "ev": ev,
            "other": ctx.get("other_tickers") or "", "pv": pv, "mdl": bool(has_model), "ho": holders, "ins": insiders}


SALT_PATH = os.path.join(ROOT, "data", "portal_salt.json")


class Sealer:
    """gzip + AES-256-GCM. Key = PBKDF2-SHA256(password, salt). The salt is kept in data/portal_salt.json (public
    by design; committed so 'remember on this device' survives daily rebuilds). Without a password, files are only
    gzip'd (local testing only - export refuses that unless asked)."""

    def __init__(self, password, salt_path=SALT_PATH):
        self.password = password or ""
        info = {}
        if os.path.exists(salt_path):
            try:
                with open(salt_path, encoding="utf-8") as f:
                    info = json.load(f)
            except (OSError, ValueError):
                info = {}
        if self.password:
            if info.get("salt"):
                salt = base64.b64decode(info["salt"])
            else:
                salt = os.urandom(16)
                os.makedirs(os.path.dirname(salt_path), exist_ok=True)
                with open(salt_path, "w", encoding="utf-8") as f:
                    json.dump({"salt": base64.b64encode(salt).decode(), "_note": "public salt for the portal key"}, f)
            from cryptography.hazmat.primitives import hashes
            from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
            kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=PBKDF2_ITER)
            self.key = kdf.derive(self.password.encode("utf-8"))
            self.info = {"plain": False, "salt": base64.b64encode(salt).decode(), "iter": PBKDF2_ITER,
                         "kdf": "PBKDF2-SHA256", "cipher": "AES-256-GCM"}
        else:
            self.key = None
            self.info = {"plain": True}

    def seal(self, obj):
        raw = gzip.compress(json.dumps(_clean(obj), default=_jsonable, separators=(",", ":")).encode("utf-8"), 9,
                            mtime=0)
        if self.key is None:
            return raw
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
        nonce = os.urandom(12)
        return nonce + AESGCM(self.key).encrypt(nonce, raw, None)

    def open(self, blob):
        if self.key is None:
            return json.loads(gzip.decompress(blob))
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
        return json.loads(gzip.decompress(AESGCM(self.key).decrypt(blob[:12], blob[12:], None)))


def _write_bytes(path, b):
    tmp = path + ".tmp"
    with open(tmp, "wb") as f:
        f.write(b)
    os.replace(tmp, path)


def export_site(state, results, cfg, summaries, password, out_dir=SITE_DATA, today=None, log=print,
                allow_plain=False, salt_path=SALT_PATH):
    today = today or date.today()
    if not password and not allow_plain:
        raise SystemExit("PORTAL_PASSWORD is not set - refusing to publish unencrypted data.")
    os.makedirs(out_dir, exist_ok=True)
    keyinfo_path = os.path.join(out_dir, "keyinfo.json")
    sealer = Sealer(password, salt_path)
    ctxs = state["ctxs"]
    groups, assign = peer_groups(ctxs, int((cfg.get("portal") or {}).get("peer_min_companies", 6)))
    shown = set()
    for res in results.values():
        shown.update(res)
    from . import history as hist
    from .prices import TwelveData
    td_cache = TwelveData._load(os.path.join(CACHE_DIR, "prices", "monthly_history.json.gz"))
    if "peers10" not in state:
        state["peers10"] = hist.closest_peers(ctxs, int((cfg.get("portal") or {}).get("peers", 10)))
    listed = hist.listed_ciks(state)
    models = state.get("models") or {}
    ym_cache = {}
    from . import holders as hold
    hdata = hold.load() if (cfg.get("portal") or {}).get("holders", {}).get("enabled", True) else {}
    hcfg = (cfg.get("portal") or {}).get("holders") or {}
    passive = hcfg.get("passive") or ()
    from . import insiders as insd
    idata = insd.load()
    companies = {}
    for c in shown:
        pv = None
        if c in listed and not ctxs[c].get("events_only"):
            try:
                pv = hist.peer_valuation(c, state, td_cache, ym_cache)
            except Exception as e:  # noqa: BLE001 - information only
                log(f"  peer valuation failed for {ctxs[c].get('ticker')}: {type(e).__name__}: {e}")
        ent = (hdata.get("by_cik") or {}).get(str(c))
        ho = None
        if ent:
            ho = {"top": hold.top_active(ent, ctxs[c].get("shares_used"), passive), "n": ent.get("n"),
                  "sp": ent.get("sp") or [], **hold.moves(ent, passive)}
        ins = (idata.get("by_cik") or {}).get(str(c))
        companies[c] = company_payload(c, ctxs[c], summaries, assign.get(c), pv, c in models, ho, ins)
    files = {}
    shards = int((cfg.get("portal") or {}).get("model_shards", 64))
    for c in shown:
        mdl = models.get(c)
        if not mdl:
            continue
        name = f"model_{int(c) % shards:02d}"
        last = (mdl.get("years") or [{}])[-1]
        tpl = model_template(ctxs[c].get("sic"), last.get("revenue"), last.get("rnd"), last.get("x_operating_income"))
        files.setdefault(name, {})[c] = dict(mdl, px=hist.fy_prices(c, state, td_cache), t=ctxs[c]["ticker"],
                                             n=ctxs[c].get("name"), ind=ctxs[c].get("industry"),
                                             fye=ctxs[c].get("latest_fy_end"), tpl=tpl)
    counts = {}
    for s in SCREENS:
        if s.sid not in results:
            continue
        p = screen_payload(s, results[s.sid], ctxs, cfg)
        files[f"screen_{s.sid}"] = p
        counts[s.sid] = {k: sum(1 for r in p["rows"] if r["cls"] == k) for k in ("PASS", "CHECK", "NEAR", "PRICE", "ONE")}
        counts[s.sid]["universe"] = len(p["rows"])
    files["companies"] = {"companies": companies, "peers": groups, "metrics": METRICS}
    gaps = []
    for c, rec in (state.get("records") or {}).items():
        st = rec.get("stage") or ""
        if st == "screened" or st.startswith("not screened: ") and "check by hand" not in st:
            continue
        if c in ctxs and not ctxs[c].get("events_only"):
            continue
        gaps.append({"t": rec.get("ticker"), "n": rec.get("name"), "ind": rec.get("industry"), "why": st})
    excluded = Counter(rec.get("stage") for rec in (state.get("records") or {}).values()
                       if (rec.get("stage") or "").startswith("not screened: ") and "check by hand" not in rec["stage"])
    files["meta"] = {
        "version": __version__, "model_shards": shards, "built": datetime.now().isoformat(timespec="minutes"),
        "screened_on": state.get("screened_on"), "priced_on": state.get("priced_on"),
        "price_day": max((c.get("price_date") or "" for c in ctxs.values()), default=None),
        "screens": [{"id": s.sid, "title": s.title, "counts": counts.get(s.sid, {}), "group": SCREEN_GROUPS.get(s.sid)}
                    for s in SCREENS if s.sid in counts],
        "universe": len(state.get("records") or {}), "screened": len(ctxs),
        "gaps": sorted(gaps, key=lambda g: str(g["t"])), "excluded": excluded.most_common(),
        "summaries": sum(1 for c in companies.values() if c.get("sum")), "companies": len(companies),
        "run_info": state.get("run_info") or {},
        "holders_period": hdata.get("period"), "holders_prev_period": hdata.get("prev_period"),
        "insider_quarters": idata.get("quarters") or [],
    }
    # nothing changed since the last publish (e.g. a re-run): tell the workflow to skip publishing. The digest
    # covers the plaintext (encryption makes every build look new); the build time is left out.
    import hashlib
    h = hashlib.sha256()
    for name in sorted(files):
        obj = files[name]
        if name == "meta":
            obj = {k: v for k, v in obj.items() if k != "built"}
        h.update(name.encode())
        h.update(json.dumps(_clean(obj), default=_jsonable, sort_keys=True, separators=(",", ":")).encode())
    # the site's own code too, so a code-only change (new screen, new card) still publishes
    site_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site")
    for root, dirs, fnames in os.walk(site_dir):
        dirs[:] = sorted(d for d in dirs if d != "data")
        for fn in sorted(fnames):
            try:
                with open(os.path.join(root, fn), "rb") as f:
                    h.update(fn.encode())
                    h.update(f.read())
            except OSError:
                pass
    digest = h.hexdigest()
    dig_path = os.path.join(CACHE_DIR, "state", "site_digest.txt")
    try:
        with open(dig_path, encoding="utf-8") as f:
            same = f.read().strip() == digest
    except OSError:
        same = False
    os.makedirs(os.path.dirname(dig_path), exist_ok=True)
    with open(dig_path, "w", encoding="utf-8") as f:
        f.write(digest)
    out_env = os.environ.get("GITHUB_OUTPUT")
    if out_env:
        with open(out_env, "a", encoding="utf-8") as f:
            f.write(f"publish={'false' if same else 'true'}\n")
    if same:
        log("Portal data unchanged since the last publish")
    written = set()
    for name, obj in files.items():
        _write_bytes(os.path.join(out_dir, name + ".bin"), sealer.seal(obj))
        written.add(name + ".bin")
    info = dict(sealer.info, check=base64.b64encode(sealer.seal({"ok": True})).decode())
    with open(keyinfo_path + ".tmp", "w", encoding="utf-8") as f:
        json.dump(info, f)
    os.replace(keyinfo_path + ".tmp", keyinfo_path)
    for f in os.listdir(out_dir):
        if f.endswith(".bin") and f not in written:
            os.remove(os.path.join(out_dir, f))
    log(f"Portal data written to {out_dir}: {len(companies)} companies, {len(groups)} peer groups"
        + ("" if password else "  (NOT encrypted - no PORTAL_PASSWORD set)"))
    return files
