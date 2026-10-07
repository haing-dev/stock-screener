"""The screens (seven from the first batch of interviews, six from the second). Each screen = a universe
(which industries it looks at) + gates (pass/fail rules) +
pillars (how passing companies are ranked).

Every gate returns PASS, FAIL, NO DATA or N/A (rule doesn't apply). A company is classified as:
  PASS  - every gate passes and there is no data-quality hold;
  CHECK - nothing fails, but some input is missing or a data-quality check needs a human look
          ('Check manually' list: these are potential candidates the data couldn't confirm);
  NEAR  - exactly one numeric rule fails, and it would pass with that threshold 20% looser;
  PRICE - every business rule passes; only the valuation rule fails ('quality OK - wait for a better price');
  ONE   - exactly one business rule fails, by more than 20% (e.g. a great business with more debt than the rule
          allows) - shown on the watch sheet so a strong company is never lost to a single rule;
  FAIL  - anything else.
So missing data never silently removes a company, and doubtful data never puts one on the main list.
"""
import pandas as pd

from .industry import (CLINICAL_STAGE, CYCLICAL, EMERGING_EXTRA_EXCLUDE, HEALTHCARE,
                       HEALTHCARE_PRODUCT, NEVER, REAL_ASSETS, in_ranges)

PASS, FAIL, NODATA, NA = "PASS", "FAIL", "NO DATA", "N/A"
HOLD_FLAG_MARKERS = ("isn't in SEC's XBRL data yet", "estimated from net income", "check free cash flow by hand",
                     "screened as a pre-revenue company",
                     "revenue jumps", "fiscal year-end changed", "multiple reporting currencies",
                     "non-standard tag", "debt may be missed", "debt partly missed", "Chapter 11",
                     "operating income not tagged for the latest year", "much older than the balance sheet")


def cfg_get(cfg, key):
    cur = cfg
    for k in key.split("."):
        cur = cur[k]
    return cur


def _cmp(val, op, thr):
    return val >= thr if op == ">=" else val <= thr


def _scaled(op, thr, s):
    """s > 0 = stricter, s < 0 = looser."""
    if op == ">=":
        return thr * (1 + s) if thr >= 0 else thr * (1 - s)
    return thr * (1 - s) if thr >= 0 else thr * (1 + s)


class Gate:
    def __init__(self, gid, name, metric=None, op=None, key=None, insight="", needs_price=False, fn=None,
                 fmt="num", near=True, fail_if=None, na_if=None, nodata_note=None, desc=None, valuation=False, one_ok=True):
        self.gid, self.name, self.metric, self.op, self.key = gid, name, metric, op, key
        self.valuation = valuation   # a price-multiple rule (failing only these = 'quality OK, price too high')
        self.one_ok = one_ok         # False for hard constraints (tradeable size/volume, a screen's defining test)
        self.insight, self.needs_price, self.fn, self.fmt, self.near = insight, needs_price, fn, fmt, near
        self.fail_if, self.na_if, self.nodata_note, self.desc = fail_if, na_if, nodata_note, desc

    def threshold(self, cfg, scope):
        if self.key is None:
            return None
        if self.key.startswith("/"):
            return cfg[self.key[1:]]
        k = self.key if "." in self.key else f"screens.{scope}.{self.key}"
        return cfg_get(cfg, k)

    def evaluate(self, ctx, cfg, scope, s=0.0):
        """Returns (status, value, threshold, note)."""
        if self.fn is not None:
            return self.fn(ctx, cfg, scope, s)
        thr = self.threshold(cfg, scope)
        if s and thr is not None:
            thr = _scaled(self.op, thr, s)
        if self.na_if is not None:
            na = self.na_if(ctx)
            if na:
                return NA, None, thr, na if isinstance(na, str) else "rule does not apply"
        val = ctx.get(self.metric)
        if val is None or (isinstance(val, float) and val != val):
            if self.fail_if is not None:
                why = self.fail_if(ctx)
                if why:
                    return FAIL, None, thr, why
            note = self.nodata_note(ctx) if callable(self.nodata_note) else (self.nodata_note or "input missing")
            return NODATA, None, thr, note
        return (PASS if _cmp(val, self.op, thr) else FAIL), val, thr, ""

    def rule_text(self, cfg, scope):
        if self.desc:
            return self.desc(cfg, scope) if callable(self.desc) else self.desc
        thr = self.threshold(cfg, scope)
        return f"{self.metric} {self.op} {thr}"


# quality warnings: a company that would PASS goes to 'Check manually' with this note instead (each screen picks
# the warnings that apply; the texts are built in pipeline.build_ctx as ctx['warn_<name>'])
QUALITY_WARNINGS = ("margin_collapse", "revenue_shrinking", "lost_money_2009")


class Screen:
    def __init__(self, sid, title, purpose, sources, universe, gates, pillars, weights, columns, rubric,
                 warnings=(), strict=False):
        # strict: a defining (hard) rule that couldn't be checked keeps the company off the 'price too high' and
        # 'missed 1 rule' lists (e.g. Owner-Operators without a measured insider stake)
        self.strict = strict
        self.sid, self.title, self.purpose, self.sources = sid, title, purpose, sources
        self.universe, self.gates, self.pillars, self.weights = universe, gates, pillars, weights
        self.columns, self.rubric = columns, rubric
        self.warnings = tuple(warnings)
        self.needs_price = any(g.needs_price for g in gates)

    def evaluate(self, ctx, cfg, priced=True):
        """priced=False: skip price gates (first pass, to decide who to price)."""
        res = {"gates": {}}
        fails, nodata, nas = [], [], []
        for g in self.gates:
            if g.needs_price and not priced:
                res["gates"][g.gid] = ("PENDING", None, g.threshold(cfg, self.sid), "needs price")
                continue
            st = g.evaluate(ctx, cfg, self.sid)
            res["gates"][g.gid] = st
            if st[0] == FAIL:
                fails.append(g)
            elif st[0] == NODATA:
                nodata.append(g)
            elif st[0] == NA:
                nas.append(g)
        holds = list(ctx.get("hold_reasons") or [])
        holds += [ctx["warn_" + k] for k in self.warnings if ctx.get("warn_" + k)]
        if priced and self.needs_price and ctx.get("val_issue") and ctx.get("price") is not None:
            holds.append("price/market cap: " + ctx["val_issue"])
        notes = [f"{g.gid} {g.name}: {res['gates'][g.gid][3] or 'no data'}" for g in nodata] + holds
        if not fails and not nodata and not holds:
            cls = PASS
        elif not fails:
            cls = "CHECK"
        elif self.strict and any(not g.one_ok for g in nodata):
            cls = FAIL
        elif priced and all(g.valuation for g in fails):
            cls = "PRICE"
        elif len(fails) == 1:
            g = fails[0]
            # 'failed 1 rule' only when every other business rule was actually verified (no missing data)
            unverified = [x for x in nodata if not x.needs_price]
            cls = "ONE" if (g.one_ok and len(unverified) <= 1) else FAIL
            if g.near and g.op:
                st = g.evaluate(ctx, cfg, self.sid, -cfg.get("sensitivity", 0.2))
                if st[0] == PASS:
                    cls = "NEAR"
        else:
            cls = FAIL
        res["class"] = cls
        res["failed"] = [g.gid for g in fails]
        res["no_data"] = [g.gid for g in nodata]
        res["check_notes"] = notes
        res["holds"] = holds
        if cls == PASS and priced:
            # robustness: still passes with every numeric threshold 20% stricter?
            ok = True
            for g in self.gates:
                if g.fn is None and g.op and g.key:
                    st = g.evaluate(ctx, cfg, self.sid, cfg.get("sensitivity", 0.2))
                    if st[0] == FAIL:
                        ok = False
                        break
            res["robust"] = ok
        return res

    def score(self, df, cfg=None):
        """Percentile-rank each pillar metric within df, average into pillars (0-100) and a weighted composite."""
        out = pd.DataFrame(index=df.index)
        weights = self.weights if self.weights is not None else (cfg or {}).get("pillar_weights", {})
        for pillar, metrics in self.pillars.items():
            parts = []
            for metric, hib in metrics:
                if metric not in df:
                    continue
                s = pd.to_numeric(df[metric], errors="coerce")
                if s.notna().sum() < 2:
                    continue
                parts.append(s.rank(pct=True, ascending=hib))
            out[pillar] = (pd.concat(parts, axis=1).mean(axis=1) * 100).round(1) if parts else float("nan")
        wsum = pd.Series(0.0, index=df.index)
        acc = pd.Series(0.0, index=df.index)
        for pillar, w in weights.items():
            if pillar in out:
                v = out[pillar]
                acc += v.fillna(0) * w
                wsum += v.notna() * w
        out["composite"] = (acc / wsum.replace(0, float("nan"))).astype(float).round(1)
        return out


# ====================================================================== universes
def screen_anyway(info, cfg):
    """config 'screen_anyway': tickers screened despite an excluded industry code (e.g. Morningstar is filed as an
    'investment adviser' but is a data business)."""
    over = cfg.get("screen_anyway") or {}
    return any(t in over for t in (info.get("all_tickers") or []) + [info.get("ticker")] if t)


def _excluded_core(info, cfg):
    from .pipeline import sic_match  # avoid import cycle at module load
    if screen_anyway(info, cfg):
        return None
    ex = sic_match(cfg["exclude_sic"], info.get("sic"))
    return ex


def u_core(info, m, cfg):
    if in_ranges(info.get("sic"), NEVER):
        return False, "fund / SPAC / REIT / shell"
    ex = _excluded_core(info, cfg)
    if ex:
        return False, f"excluded industry: {ex['label']}"
    return True, ""


def u_emerging(info, m, cfg):
    ok, why = u_core(info, m, cfg)
    if not ok:
        return ok, why
    r = in_ranges(info.get("sic"), EMERGING_EXTRA_EXCLUDE)
    if r:
        return False, f"excluded industry: {r[2]}"
    return True, ""


def u_healthcare(info, m, cfg):
    r = in_ranges(info.get("sic"), HEALTHCARE)
    return (True, r[2]) if r else (False, "not healthcare")


def _is_commercial(m, cfg):
    c = cfg["screens"]["hc_clinical"]
    rev = m.get("ttm_revenue_usd")
    op = m.get("ttm_operating_income")
    return rev is not None and rev >= c["max_revenue_usd"] and op is not None and op > 0


def u_hc_commercial(info, m, cfg):
    ok, why = u_healthcare(info, m, cfg)
    return (ok, why) if not ok else (True, why)


def u_hc_clinical(info, m, cfg):
    r = in_ranges(info.get("sic"), CLINICAL_STAGE)
    if not r:
        return False, "not a pharma / biotech / medtech code"
    if _is_commercial(m, cfg):
        return False, "commercial-stage (revenue and operating profit) - see Healthcare commercial"
    return True, r[2]


def u_cyclicals(info, m, cfg):
    r = in_ranges(info.get("sic"), CYCLICAL)
    return (True, r[2]) if r else (False, "not a capacity-cycle industry")


STRUCTURAL_EXCLUDE = [(6000, 6399, "banks, lenders, brokers, asset managers, insurers"),
                      (6500, 6799, "real estate, funds, holding companies, SPACs")]
STRUCTURAL_KEEP = [(6411, 6411, "insurance brokers")]


def u_special(info, m, cfg):
    if in_ranges(info.get("sic"), NEVER):
        return False, "fund / SPAC / REIT / shell"
    # EV / EBIT means nothing for balance-sheet businesses (banks, insurers, crypto treasuries, funds)
    r = in_ranges(info.get("sic"), STRUCTURAL_EXCLUDE)
    if r and not in_ranges(info.get("sic"), STRUCTURAL_KEEP) and not screen_anyway(info, cfg):
        return False, f"excluded industry: {r[2]}"
    if not info.get("event_types") and not m.get("event_types"):
        return False, "no qualifying event"
    return True, ", ".join(info["event_types"])


# ====================================================================== shared gate builders
def g_history(gid, key, insight="", near=False):
    return Gate(gid, "History", "years_with_data", ">=", key, insight, near=near, fmt="int",
                nodata_note="no annual history")


def _recent_fn(key):
    def fn(ctx, cfg, scope, s=0.0):
        thr = cfg[key[1:]] if key.startswith("/") else cfg_get(cfg, key if "." in key else f"screens.{scope}.{key}")
        v = ctx.get("years_since_latest_fy")
        if v is None:
            return NODATA, None, thr, "no annual report date"
        if v <= thr:
            return PASS, v, thr, ""
        if ctx.get("xbrl_lags_annual_report"):
            # the company DID file a recent annual report; SEC's XBRL data just doesn't have it yet
            return NODATA, v, thr, (f"annual report for the period ending {ctx['xbrl_lags_annual_report']} was filed "
                                    "but isn't in SEC's XBRL data yet")
        return FAIL, v, thr, ""
    return fn


def g_recent(gid, key="max_years_since_latest_fy"):
    return Gate(gid, "Recent report", "years_since_latest_fy", "<=", key,
                "Data must be current (latest annual report within ~1.5 years).", near=False, fmt="years",
                fn=_recent_fn(key))


def g_size(gid, key, metric="latest_revenue_usd", name="Size"):
    return Gate(gid, name, metric, ">=", key, "Big enough to own; tiny filers have patchier data.", near=False,
                fmt="usd", nodata_note=lambda c: f"no FX rate for {c.get('currency')}")


def _leverage_fn(key, basis="ttm"):
    """Net debt / EBITDA with sensible handling: net cash passes; negative EBITDA with net debt fails;
    if D&A is missing, EBIT is used (stricter - if it passes on EBIT it passes on EBITDA)."""
    def fn(ctx, cfg, scope, s=0.0):
        thr = cfg_get(cfg, key if "." in key else f"screens.{scope}.{key}")
        if s:
            thr = _scaled("<=", thr, s)
        nd = ctx.get("bs_net_debt")
        if nd is None:
            return NODATA, None, thr, "no balance sheet"
        if not ctx.get("bs_debt_found") and nd > 0:
            return NODATA, None, thr, "no standard debt tag found"
        ebitda = ctx.get("normalized_ebitda") if basis == "normalized" else ctx.get("ttm_ebitda")
        ebit = ctx.get("normalized_ebit") if basis == "normalized" else ctx.get("ttm_operating_income")
        if nd <= 0:
            return PASS, (nd / ebitda if ebitda and ebitda > 0 else None), thr, "net cash"
        if ebitda is None and ebit is not None and ebit > 0:
            r = nd / ebit
            if r <= thr:
                return PASS, r, thr, "D&A not tagged: tested on EBIT (stricter)"
            return NODATA, None, thr, f"D&A not tagged; net debt / EBIT = {r:.1f}x"
        if ebitda is None:
            return NODATA, None, thr, "EBITDA unavailable"
        if ebitda <= 0:
            return FAIL, None, thr, "net debt with zero or negative EBITDA"
        r = nd / ebitda
        return (PASS if r <= thr else FAIL), r, thr, ""
    return fn


def _gate_lev(gid, key, insight, basis="ttm", name="Leverage"):
    g = Gate(gid, name, "net_debt_to_ebitda" if basis == "ttm" else "net_debt_to_norm_ebitda", "<=", key, insight,
             fn=_leverage_fn(key, basis), fmt="mult")
    return g


# ====================================================================== 1. CORE COMPOUNDERS
def _g7(ctx, cfg, scope, s=0.0):
    thr = cfg["gates"]["min_fcf_conversion"]
    if s:
        thr = _scaled(">=", thr, s)
    v = ctx.get("fcf_conversion")
    if v is not None:
        return (PASS if v >= thr else FAIL), v, thr, ""
    if ctx.get("fcf_conversion_years", 0) >= 5:
        return FAIL, None, thr, "cumulative net income <= 0"
    if not ctx.get("capex_found"):
        oc = ctx.get("ocf_conversion")
        return NODATA, None, thr, ("capital expenditure isn't tagged with a standard XBRL tag" +
                                   (f"; operating cash flow / net income = {oc:.2f}" if oc else ""))
    return NODATA, None, thr, "fewer than 5 years with FCF and net income"


def _g8(ctx, cfg, scope, s=0.0):
    thr = cfg["gates"]["max_net_debt_to_ocf"]
    if s:
        thr = _scaled("<=", thr, s)
    v = ctx.get("net_debt_to_ocf")
    if v is not None:
        if not ctx.get("debt_found") and v > 0:
            return NODATA, v, thr, "no standard debt tag found"
        return (PASS if v <= thr else FAIL), v, thr, "" if ctx.get("debt_found") else "no debt tag: treated as debt-free"
    if ctx.get("ocf_avg_3y") is not None and ctx["ocf_avg_3y"] <= 0:
        return FAIL, None, thr, "operating cash flow <= 0"
    return NODATA, None, thr, "no operating cash flow"


CORE_GATES = [
    g_history("G1", "min_years_data", "Kantesaria: only own what stays dominant 10+ years; Hohn: good companies stay good."),
    g_recent("G2", "/max_years_since_latest_fy"),
    g_size("G3", "min_revenue_usd"),
    Gate("G4", "Consistent profits", "operating_loss_years", "<=", "gates.max_operating_loss_years",
         "Kantesaria: quality = growth AND predictability.", near=False, fmt="int"),
    Gate("G5a", "High returns (median)", "roic_median", ">=", "gates.min_median_roic",
         "Dorsey: >15% ROIC for >15 years is the signature of a moat.", fmt="pct"),
    Gate("G5b", "High returns (consistency)", "roic_share_above_floor", ">=", "gates.min_share_of_years_above_floor",
         "Returns must persist, not one good stretch.", fmt="pct"),
    Gate("G6", "Growth", "revenue_cagr", ">=", "gates.min_revenue_cagr",
         "Kantesaria: predictable but slow businesses underperform; Dorsey: runway.", fmt="pct",
         nodata_note="need >= 5 years of revenue, positive at both ends"),
    Gate("G7", "Cash conversion", "fcf_conversion", ">=", "gates.min_fcf_conversion",
         "Kantesaria/Gaonkar/Terry Smith: value is cash; FCF / net income over the window.", fn=_g7, fmt="mult"),
    Gate("G8", "Balance sheet", "net_debt_to_ocf", "<=", "gates.max_net_debt_to_ocf",
         "Gaonkar: avoid over-levered companies; Singer: survive first.", fn=_g8, fmt="mult"),
]
CORE_GATES[0].key = "/min_years_data"
CORE_GATES[2].key = "/min_revenue_usd"

CORE = Screen(
    "core", "Core Compounders",
    "Durable, high-return, predictable businesses with pricing power, held for years. Price-blind on purpose; "
    "valuation columns are shown to help decide timing.",
    "Kantesaria, Hohn, Dorsey, Terry Smith, Davis, Li Lu",
    u_core, CORE_GATES,
    {"predictability": [("revenue_growth_std", False), ("revenue_decline_years", False), ("operating_margin_std", False),
                        ("recession_2020_revenue_change", True)],
     "pricing_power": [("gross_margin_median", True), ("gross_margin_std", False),
                       ("gross_margin_change_2021_2023", True), ("operating_margin_median", True),
                       ("operating_margin_trend", True)],
     "returns_moat_direction": [("roic_median", True), ("cash_roic_median", True), ("roic_trend", True),
                                ("incremental_roic", True)],
     "growth_runway": [("revenue_cagr", True), ("nopat_cagr", True), ("fcf_per_share_cagr", True),
                       ("reinvestment_rate", True)],
     "capital_allocation": [("share_count_cagr", False), ("acquisitions_to_ocf", False),
                            ("sbc_to_revenue", False), ("goodwill_to_assets", False)],
     "balance_sheet": [("net_debt_to_ocf", False)]},
    None,  # weights from config pillar_weights
    ["revenue_cagr", "roic_median", "cash_roic_median", "roc_tangible_median", "reinvestment_rate",
     "gross_margin_median", "gross_margin_change_2021_2023", "operating_margin_median", "fcf_conversion",
     "net_debt_to_ocf", "share_count_cagr", "recession_2020_revenue_change", "recession_2020_op_income_change",
     "acquisitions_to_ocf", "sbc_to_revenue", "market_cap_usd", "ev_ebit", "earnings_yield", "fcf_yield", "pe"],
    "Moat durability and switching costs (Dorsey: can't be screened), management alignment and capital "
    "allocation, AI disruption exposure, why the market might misprice it.",
    warnings=("margin_collapse", "revenue_shrinking", "lost_money_2009"))


# ====================================================================== 2. EMERGING COMPOUNDERS
def _e_profitable(ctx, cfg, scope, s=0.0):
    e_ttm, e_fy = ctx.get("ttm_ebitda"), ctx.get("latest_fy_ebitda")
    op_ttm, op_fy = ctx.get("ttm_operating_income"), ctx.get("latest_fy_operating_income")
    if e_ttm is not None and e_fy is not None:
        ok = e_ttm > 0 and e_fy > 0
        return (PASS if ok else FAIL), e_ttm, 0, ""
    # D&A missing: EBIT > 0 implies EBITDA > 0
    if op_ttm is not None and op_fy is not None and op_ttm > 0 and op_fy > 0:
        return PASS, op_ttm, 0, "D&A not tagged: operating income > 0 (so EBITDA > 0)"
    if (e_ttm is not None and e_ttm <= 0) or (e_fy is not None and e_fy <= 0):
        return FAIL, e_ttm, 0, "EBITDA <= 0"
    return NODATA, None, 0, "EBITDA unavailable"


def _e_growth_now(ctx, cfg, scope, s=0.0):
    thr = cfg_get(cfg, f"screens.{scope}.min_recent_growth")
    if s:
        thr = _scaled(">=", thr, s)
    v = ctx.get("ytd_revenue_growth")
    src = "year-to-date vs prior year-to-date"
    if v is None:
        v = ctx.get("revenue_growth_latest_fy")
        src = "latest fiscal year"
    if v is None:
        return NODATA, None, thr, "no recent growth figure"
    return (PASS if v >= thr else FAIL), v, thr, src


def _e_gross_margin(ctx, cfg, scope, s=0.0):
    thr = cfg_get(cfg, f"screens.{scope}.min_gross_margin")
    if s:
        thr = _scaled(">=", thr, s)
    v = ctx.get("ttm_gross_margin")
    if v is None:
        v = ctx.get("gross_margin_latest")
    if v is None:
        if not ctx.get("gross_profit_reported"):
            cands = [c["tag"] for c in (ctx.get("data_gap_candidates") or {}).get("cost_of_revenue", [])]
            if cands:
                return NODATA, None, thr, f"cost of sales under a non-standard tag ({cands[0]})"
            return NA, None, thr, "no cost-of-sales line in any year (service business) - rule skipped"
        return NODATA, None, thr, "no gross profit / cost of revenue line"
    return (PASS if v >= thr else FAIL), v, thr, ""


def _e_valuation(ctx, cfg, scope, s=0.0):
    thr = cfg_get(cfg, "screens.emerging.max_ev_ebitda")
    if s:
        thr = _scaled("<=", thr, s)
    v = ctx.get("ev_ebitda")
    if v is not None:
        return (PASS if v <= thr else FAIL), v, thr, ""
    e = ctx.get("ev_ebit")
    if e is not None and e <= thr:
        # D&A not tagged: EV / EBIT is always >= EV / EBITDA, so passing on EBIT is a safe pass
        return PASS, e, thr, "EV/EBITDA unavailable: tested on EV/EBIT (stricter)"
    return NODATA, None, thr, ctx.get("val_issue") or "EV/EBITDA unavailable"


def _e_op_leverage(ctx, cfg, scope, s=0.0):
    a, b = ctx.get("ebitda_margin_change_3y"), ctx.get("operating_margin_change_3y")
    c = ctx.get("sga_ratio_change_3y")
    margin = a if a is not None else b
    vals = [x for x in (margin, -c if c is not None else None) if x is not None]
    if not vals:
        return NODATA, None, 0, "no margin or SG&A history"
    ok = (margin is not None and margin >= 0) or (c is not None and c <= 0)
    return (PASS if ok else FAIL), margin, 0, ("margin up over 3 years" if margin is not None and margin >= 0
                                              else ("SG&A / revenue falling" if ok else "margins and SG&A ratio both worsening"))


def _e_not_large(ctx, cfg, scope, s=0.0):
    thr = cfg_get(cfg, "screens.emerging.max_market_cap_usd")
    v = ctx.get("market_cap_usd")
    if v is not None:
        return (PASS if v <= thr else FAIL), v, thr, ""
    rev = ctx.get("ttm_revenue_usd") or ctx.get("latest_revenue_usd")
    if rev is not None and rev > thr:
        # market cap unverifiable (e.g. ADR ratio unknown), but revenue alone is above the size cap
        return FAIL, rev, thr, "market cap unverified, but revenue alone exceeds the cap"
    return NODATA, None, thr, ctx.get("val_issue") or "no market cap"


EMERGING_GATES = [
    Gate("E1", "History", "years_total", ">=", "min_years", "Need 3+ years to measure growth and margin trends.",
         near=False, fmt="int"),
    g_recent("E2", "screens.emerging.max_years_since_latest_fy"),
    Gate("E3", "Already profitable", "ttm_ebitda", ">=", None,
         "Haley: 88% of 104 multibaggers were EBITDA-positive five years earlier.", fn=_e_profitable, fmt="usd",
         near=False, desc="TTM and latest fiscal-year EBITDA > 0"),
    Gate("E4", "Fast growth", "revenue_cagr_3y", ">=", "min_revenue_cagr_3y",
         "Haley: median multibagger grew revenue ~21% a year (25th percentile ~14%).", fmt="pct",
         nodata_note="need revenue 3 years ago"),
    Gate("E5", "Growth not fading", "ytd_revenue_growth", ">=", "min_recent_growth",
         "Sacerdote: 'the biggest reason people blow up in tech is they miss on revenue'.", fn=_e_growth_now,
         fmt="pct", desc=lambda c, s: f"latest year-to-date (else fiscal-year) revenue growth >= "
                                      f"{cfg_get(c, 'screens.emerging.min_recent_growth'):.0%}"),
    Gate("E6", "Gross margin", "gross_margin_latest", ">=", "min_gross_margin",
         "Haley: median multibagger gross margin ~mid-40s, leaving room for operating leverage.",
         fn=_e_gross_margin, fmt="pct"),
    Gate("E7", "Operating leverage", "ebitda_margin_change_3y", ">=", None,
         "Haley: winners' SG&A/revenue fell; EBITDA margins expanded.", fn=_e_op_leverage, fmt="pct", near=False,
         desc="EBITDA (or operating) margin up over 3 years, or SG&A / revenue down"),
    Gate("E8", "Little dilution", "share_count_cagr_3y", "<=", "max_share_count_cagr_3y",
         "Haley: winners weren't heavily diluting; Druckenmiller/Davis: per-share value. Measured only after an "
         "IPO / spin-off (pre-listing share counts exclude converting preferred).", fmt="pct",
         nodata_note=lambda c: c.get("share_count_cagr_3y_basis") or "share-count history unavailable"),
    _gate_lev("E9", "max_net_debt_to_ebitda", "Haley: strong balance sheet as downside protection."),
    Gate("E10", "Size (market cap)", "market_cap_usd", ">=", "min_market_cap_usd",
         "Haley: study universe $150M-$10B; micro caps were Alta Fox's worst bucket.", needs_price=True,
         fmt="usd", near=False, nodata_note=lambda c: c.get("val_issue") or "no market cap"),
    Gate("E11", "Not already large", "market_cap_usd", "<=", "max_market_cap_usd",
         "Emerging = room to grow; large caps belong in Core.", needs_price=True, fmt="usd", near=False,
         fn=_e_not_large),
    Gate("E12", "Valuation", "ev_ebitda", "<=", "max_ev_ebitda",
         "Haley: winners started at ~10x forward EBITDA, generally <20x; the thesis must work without multiple "
         "expansion.", needs_price=True, fmt="mult", fn=_e_valuation),
    Gate("E13", "Liquidity", "adv_usd", ">=", "min_adv_usd",
         "Haley's study: average daily value traded > $200k.", needs_price=True, fmt="usd", near=False,
         nodata_note="no trading volume in the quote"),
]

EMERGING = Screen(
    "emerging", "Emerging Compounders",
    "Profitable small and mid caps growing fast, with operating leverage and little dilution, at a sensible "
    "price. Shorter history allowed (3+ years).",
    "Connor Haley (Alta Fox multibagger study), Sundheim, Sacerdote",
    u_emerging, EMERGING_GATES,
    {"growth": [("revenue_cagr_3y", True), ("ebitda_cagr_3y", True), ("ytd_revenue_growth", True)],
     "operating_leverage": [("ebitda_margin_change_3y", True), ("sga_ratio_change_3y", False)],
     "quality": [("gp_to_tangible_assets", True), ("roic_latest", True), ("gross_margin_latest", True)],
     "value": [("ev_ebitda", False), ("ev_sales", False)],
     "balance_sheet": [("net_debt_to_ebitda", False), ("share_count_cagr_3y", False)]},
    {"growth": 30, "operating_leverage": 20, "quality": 20, "value": 20, "balance_sheet": 10},
    ["market_cap_usd", "revenue_cagr_3y", "ytd_revenue_growth", "ebitda_cagr_3y", "gross_margin_latest",
     "ttm_ebitda_margin", "ebitda_margin_change_3y", "sga_ratio_change_3y", "gp_to_tangible_assets",
     "share_count_cagr_3y", "net_debt_to_ebitda", "ev_ebitda", "ev_sales", "pe", "adv_usd", "acquisitions_to_ocf"],
    "Why is it overlooked (Haley's most important question)? Durable advantage or niche dominance? Customer or "
    "supplier concentration (~70% is a kill)? Insider ownership >= ~5% and pay in stock? Acquisition-led growth?",
    warnings=("margin_collapse",))


# ====================================================================== 3. SPECIAL SITUATIONS
SPECIAL_GATES = [
    Gate("S1", "Recent report", "years_since_latest_fy", "<=", "max_years_since_latest_fy",
         "Must have filed financials recently.", near=False, fmt="years",
         nodata_note="no annual report yet (check the Form 10 / prospectus)"),
    Gate("S2", "Profitable business", "ttm_operating_income", ">", None,
         "Greenblatt: special situations work best in good businesses bought cheaply.",
         fn=lambda c, cfg, sc, s=0.0: ((PASS if c["ttm_operating_income"] > 0 else FAIL), c["ttm_operating_income"], 0, "")
         if c.get("ttm_operating_income") is not None else (NODATA, None, 0, "no operating income"),
         fmt="usd", near=False, desc="TTM operating income > 0"),
    _gate_lev("S3", "max_net_debt_to_ebitda", "Gaines: debt turns equity into an option bet."),
    Gate("S4", "Cheap", "ev_ebit", "<=", "max_ev_ebit",
         "Greenblatt: think in pre-tax EBIT multiples; 10x EBIT ~ a bond-equivalent yield.", needs_price=True,
         fmt="mult", nodata_note=lambda c: c.get("val_issue") or "EV/EBIT unavailable"),
    Gate("S5", "Size", "market_cap_usd", ">=", "min_market_cap_usd", "Tradeable size.", needs_price=True,
         fmt="usd", near=False, nodata_note=lambda c: c.get("val_issue") or "no market cap"),
    Gate("S6", "Liquidity", "adv_usd", ">=", "min_adv_usd", "Tradeable volume.", needs_price=True, fmt="usd",
         near=False, nodata_note="no trading volume in the quote"),
]
SPECIAL = Screen(
    "special", "Special Situations",
    "Spin-offs, post-bankruptcy companies and recent IPOs (events the market misprices because analysts and "
    "big funds skip messy situations), filtered for profitable businesses at low EBIT multiples. Every event "
    "found is listed on the Events sheet whether or not it passes.",
    "Greenblatt (spin-offs, stubs, post-bankruptcy), Haley (masking effect), Gaines",
    u_special, SPECIAL_GATES,
    {"value": [("earnings_yield", True), ("fcf_yield", True)],
     "quality": [("roc_tangible_latest", True), ("ttm_operating_margin", True)],
     "balance_sheet": [("net_debt_to_ebitda", False)],
     "freshness": [("months_since_event", False)]},
    {"value": 40, "quality": 30, "balance_sheet": 15, "freshness": 15},
    ["event_types", "event_date", "months_since_event", "event_filing_url", "market_cap_usd", "ev_ebit",
     "earnings_yield", "fcf_yield", "roc_tangible_latest", "ttm_operating_margin", "net_debt_to_ebitda",
     "ttm_revenue", "adv_usd"],
    "Read the Form 10 / reorganization plan: why is the parent spinning it off, who will sell (index funds, "
    "ex-creditors), management incentives and ownership, debt loaded on the spinco, 'temporary or permanent' "
    "problems, hidden assets.")


# ====================================================================== 4. FORTRESS
def _recession(key, rev_key, op_key):
    def fn(ctx, cfg, scope, s=0.0):
        c = cfg["screens"][scope]
        rmin, omin = c[rev_key], c[op_key]
        if s:
            rmin, omin = _scaled(">=", rmin, s), _scaled(">=", omin, s)
        rv, ov = ctx.get(f"recession_{key}_revenue_change"), ctx.get(f"recession_{key}_op_income_change")
        lowest = ctx.get(f"recession_{key}_min_op_income")
        if lowest is not None and lowest < 0:
            # an operating loss in a recession year fails the test even when the year before isn't in XBRL
            if ov is None or ov >= omin:
                return FAIL, rv, (rmin, omin), "operating loss in a recession fiscal year"
        if rv is None and ov is None:
            # fallback: net income (often tagged for one more year than revenue and operating income)
            ni, ni_loss = ctx.get(f"recession_{key}_ni_change"), ctx.get(f"recession_{key}_ni_loss")
            if ni_loss:
                return FAIL, None, (rmin, omin), "net loss in a recession fiscal year"
            if ni is not None:
                return ((PASS if ni >= omin else FAIL), ni, (rmin, omin),
                        f"revenue / operating income not in XBRL: net income {ni:+.1%} (fallback)")
            if key == "2009":
                if ctx.get("recession_2009_years_in_window"):
                    return NODATA, None, (rmin, omin), ("2008-09 figures only partly in XBRL (no prior year to "
                                                        "compare): check the FY2008-09 annual reports")
                if ctx.get("cycle_group"):
                    return NODATA, None, (rmin, omin), (f"cyclical industry ({ctx['cycle_group']}) and 2008-09 is "
                                                        "before its XBRL data: check how it did in 2008-09")
                if ctx.get("listed_before_2009"):
                    return NODATA, None, (rmin, omin), ("listed before 2009 but its 2008-09 results aren't in SEC's "
                                                        "XBRL data: check the FY2008-09 annual reports")
                return NA, None, (rmin, omin), "company too young for the 2008-09 recession"
            return NODATA, None, (rmin, omin), "no data for the 2020 fiscal years"
        ok = (rv is None or rv >= rmin) and (ov is None or ov >= omin)
        note = f"revenue {rv:+.1%}" if rv is not None else "revenue n/a"
        note += f", operating income {ov:+.1%}" if ov is not None else ", operating income n/a"
        return (PASS if ok else FAIL), rv, (rmin, omin), note
    return fn


def _coverage(ctx, cfg, scope, s=0.0):
    thr = cfg_get(cfg, f"screens.{scope}.min_interest_coverage")
    if s:
        thr = _scaled(">=", thr, s)
    v = ctx.get("interest_coverage")
    if v is None:
        if ctx.get("ttm_operating_income") is not None and ctx["ttm_operating_income"] <= 0:
            return FAIL, None, thr, "operating income <= 0"
        return NODATA, None, thr, "interest expense not tagged"
    if ctx.get("interest_coverage_estimated"):
        if v >= thr:
            return PASS, v, thr, "interest not tagged: assumed 10% on all debt (worst case) - still passes"
        return NODATA, v, thr, "interest expense not tagged (worst-case estimate at 10% of debt is below the bar)"
    return (PASS if v >= thr else FAIL), v, thr, ""


def _maturities(ctx, cfg, scope, s=0.0):
    v = ctx.get("maturities_covered")
    if v is None:
        return NODATA, None, None, "debt maturity schedule not tagged"
    return (PASS if v else FAIL), v, None, "" if v else "debt due within 2 years exceeds cash + 2 years of FCF"


def _fcf_years(ctx, cfg, scope, s=0.0):
    n, tot = ctx.get("fcf_positive_years"), ctx.get("fcf_years")
    if not tot or tot < 5:
        return NODATA, None, None, "fewer than 5 years of FCF (capex not tagged?)"
    allowed = cfg_get(cfg, f"screens.{scope}.max_negative_fcf_years")
    return (PASS if tot - n <= allowed else FAIL), n / tot, allowed, f"{n} of {tot} years FCF-positive"


def _inflation(ctx, cfg, scope, s=0.0):
    thr = cfg_get(cfg, f"screens.{scope}.min_margin_change_2021_2023")
    if s:
        thr = _scaled(">=", thr, s)
    v = ctx.get("gross_margin_change_2021_2023")
    src = "gross margin"
    if v is None:
        v = ctx.get("operating_margin_change_2021_2023")
        src = "operating margin"
    if v is None:
        return NODATA, None, thr, "no 2021 and 2023 margins"
    return (PASS if v >= thr else FAIL), v, thr, src


FORTRESS_GATES = [
    Gate("F1", "History", "years_with_data", ">=", "min_years", "A long record, including 2020.", near=False,
         fmt="int"),
    g_recent("F2", "screens.fortress.max_years_since_latest_fy"),
    g_size("F3", "screens.fortress.min_revenue_usd"),
    Gate("F4", "Held up in 2020", "recession_2020_revenue_change", ">=", None,
         "Druckenmiller: earnings that are good and sustainable in a recession protect the stock.",
         fn=_recession("2020", "min_recession_revenue_change", "min_recession_op_income_change"), fmt="pct",
         desc=lambda c, s: f"worst fiscal year ending Mar-2020..Jun-2021 vs prior year: revenue >= "
                           f"{c['screens'][s]['min_recession_revenue_change']:.0%}, operating income >= "
                           f"{c['screens'][s]['min_recession_op_income_change']:.0%}"),
    Gate("F5", "Held up in 2009", "recession_2009_revenue_change", ">=", None,
         "Same test for the 2008-09 recession. An operating loss in a recession year always fails.",
         fn=_recession("2009", "min_recession_2009_revenue_change", "min_recession_2009_op_income_change"),
         fmt="pct", desc=lambda c, s: f"fiscal years ending Sep-2008..Mar-2010: revenue >= "
                                      f"{c['screens'][s]['min_recession_2009_revenue_change']:.0%}, operating income >= "
                                      f"{c['screens'][s]['min_recession_2009_op_income_change']:.0%}; an operating loss "
                                      f"in the window fails; net income is the fallback when revenue/operating income "
                                      f"aren't in XBRL; no data = 'check manually' unless the company is younger "
                                      f"than the recession (N/A)"),
    Gate("F6", "Never lost money", "operating_loss_years", "<=", "max_operating_loss_years",
         "Fortress businesses don't post operating losses.", near=False, fmt="int"),
    Gate("F7", "Stable margins", "operating_margin_std", "<=", "max_operating_margin_std",
         "Predictability (Kantesaria); low volatility of operating margin over 10 years.", fmt="pct"),
    Gate("F8", "Decent returns", "roic_median", ">=", "min_median_roic",
         "Relaxed vs Core so asset-heavy toll collectors (rail, waste) qualify.", fmt="pct"),
    _gate_lev("F9", "max_net_debt_to_ebitda", "Singer: survive first; Gerber: leverage that can't refinance breaks."),
    Gate("F10", "Interest coverage", "interest_coverage", ">=", "min_interest_coverage",
         "Druckenmiller (2024): COVID-era debt rolls over at higher rates - test coverage at today's rates.",
         fn=_coverage, fmt="mult"),
    Gate("F11", "Refinancing", "maturities_covered", None, None,
         "Matt Mark/Gerber: maturities exceeding cash cause a liquidity crisis even with asset coverage.",
         fn=_maturities, fmt="bool", near=False, desc="debt due within 2 years <= cash + 2 years of FCF"),
    Gate("F12", "Cash every year", "fcf_positive_years", None, None, "Positive free cash flow almost every year.",
         fn=_fcf_years, fmt="pct", near=False,
         desc=lambda c, s: f"at most {c['screens'][s]['max_negative_fcf_years']} year(s) with negative FCF"),
    Gate("F13", "Inflation test", "gross_margin_change_2021_2023", ">=", "min_margin_change_2021_2023",
         "Hohn/Kantesaria: did margins hold through 2021-23 inflation?", fn=_inflation, fmt="pct"),
]
FORTRESS = Screen(
    "fortress", "Fortress",
    "Recession-proof earnings, stable margins and strong balance sheets: the sleeve to overweight when the "
    "macro turns. Returns can be lower than Core; resilience is the point.",
    "Druckenmiller, Hohn (toll collectors), Singer, Terry Smith, Gerber",
    u_core, FORTRESS_GATES,
    {"resilience": [("recession_2020_revenue_change", True), ("recession_2020_op_income_change", True),
                    ("recession_2009_revenue_change", True), ("recession_2009_op_income_change", True)],
     "stability": [("operating_margin_std", False), ("revenue_decline_years", False), ("gross_margin_std", False)],
     "returns": [("roic_median", True), ("cash_roic_median", True)],
     "balance_sheet": [("net_debt_to_ebitda", False), ("interest_coverage", True)],
     "value": [("fcf_yield", True), ("earnings_yield", True)]},
    {"resilience": 30, "stability": 20, "returns": 20, "balance_sheet": 20, "value": 10},
    ["recession_2020_revenue_change", "recession_2020_op_income_change", "recession_2009_revenue_change",
     "recession_2009_op_income_change", "operating_margin_std", "operating_margin_median", "roic_median",
     "net_debt_to_ebitda", "interest_coverage", "debt_due_2y_total", "gross_margin_change_2021_2023",
     "market_cap_usd", "fcf_yield", "earnings_yield", "pe"],
    "Is the resilience structural (essential, low-cost, recurring) or a one-off? Customer and contract "
    "durability, regulation, refinancing schedule, what would break it.",
    warnings=("margin_collapse", "revenue_shrinking"))


# ====================================================================== 5. HEALTHCARE
def _hc_gm(ctx, cfg, scope, s=0.0):
    thr = cfg_get(cfg, f"screens.{scope}.min_gross_margin_products")
    if s:
        thr = _scaled(">=", thr, s)
    if not in_ranges(ctx.get("sic"), [(a, b) for a, b in HEALTHCARE_PRODUCT]):
        return NA, None, thr, "services / distribution / insurance: gross margin not comparable"
    v = ctx.get("ttm_gross_margin")
    if v is None:
        v = ctx.get("gross_margin_latest")
    if v is None:
        return NODATA, None, thr, "no gross profit line"
    return (PASS if v >= thr else FAIL), v, thr, ""


def _hc_growth(ctx, cfg, scope, s=0.0):
    thr = cfg_get(cfg, f"screens.{scope}.min_revenue_cagr")
    if s:
        thr = _scaled(">=", thr, s)
    v = ctx.get("revenue_cagr")
    if v is None:
        v = ctx.get("revenue_cagr_3y")
    if v is None:
        return NODATA, None, thr, "no revenue history"
    return (PASS if v >= thr else FAIL), v, thr, ""


HC_COMMERCIAL_GATES = [
    Gate("H1", "History", "years_with_data", ">=", "min_years", "Enough history to judge durability.", near=False,
         fmt="int"),
    g_recent("H2", "screens.hc_commercial.max_years_since_latest_fy"),
    g_size("H3", "screens.hc_commercial.min_revenue_usd"),
    Gate("H4", "Consistent profits", "operating_loss_years_5y", "<=", "max_operating_loss_years_5y",
         "Commercial-stage: profitable in at least 4 of the last 5 years.", near=False, fmt="int"),
    Gate("H5", "High returns", "roic_median", ">=", "min_median_roic",
         "Terry Smith: pharma and health care are persistently high-ROIC sectors.", fmt="pct"),
    Gate("H6", "Gross margin (products)", "gross_margin_latest", ">=", "min_gross_margin_products",
         "Chen: commercial drugs earn 80-90% gross margins; devices/tools lower.", fn=_hc_gm, fmt="pct"),
    Gate("H7", "Cash conversion", "fcf_conversion", ">=", "min_fcf_conversion", "Profits must turn into cash.",
         fn=lambda c, cfg, sc, s=0.0: _g7_custom(c, cfg_get(cfg, f"screens.{sc}.min_fcf_conversion"), s), fmt="mult"),
    _gate_lev("H8", "max_net_debt_to_ebitda", "Avoid levered roll-ups."),
    Gate("H9", "Growing", "revenue_cagr", ">=", "min_revenue_cagr",
         "Revenue must be growing (patent cliffs show up as shrinking sales).", fn=_hc_growth, fmt="pct"),
]


def _g7_custom(ctx, thr, s):
    if s:
        thr = _scaled(">=", thr, s)
    v = ctx.get("fcf_conversion")
    if v is not None:
        return (PASS if v >= thr else FAIL), v, thr, ""
    if ctx.get("fcf_conversion_years", 0) >= 5:
        return FAIL, None, thr, "cumulative net income <= 0"
    if not ctx.get("capex_found"):
        return NODATA, None, thr, "capital expenditure isn't tagged with a standard XBRL tag"
    return NODATA, None, thr, "fewer than 5 years with FCF and net income"


HC_COMMERCIAL = Screen(
    "hc_commercial", "Healthcare - Commercial",
    "Profitable pharma, medtech, life-science tools, services and insurers with durable returns. The AI review "
    "checks what numbers can't: patent expiries, government-payer dependence, price-led growth.",
    "Terry Smith, Chen, Flynn, Johnson, Greenblatt (government payers), GEF panel",
    u_hc_commercial, HC_COMMERCIAL_GATES,
    {"returns": [("roic_median", True), ("cash_roic_median", True)],
     "margins": [("gross_margin_median", True), ("operating_margin_median", True), ("gross_margin_change_2021_2023", True)],
     "growth": [("revenue_cagr", True), ("revenue_cagr_3y", True)],
     "resilience": [("operating_margin_std", False), ("recession_2020_revenue_change", True)],
     "balance_sheet": [("net_debt_to_ebitda", False)]},
    {"returns": 30, "margins": 20, "growth": 20, "resilience": 15, "balance_sheet": 15},
    ["hc_segment", "revenue_cagr", "revenue_cagr_3y", "roic_median", "gross_margin_latest", "operating_margin_median",
     "rnd_to_revenue", "fcf_conversion", "net_debt_to_ebitda", "market_cap_usd", "ev_ebit", "fcf_yield", "pe"],
    "Patent expiries in the next 5 years as % of revenue (generics take 90-98% of volume within months); "
    "Medicare/Medicaid share of revenue; growth from price rises in old crowded classes; pipeline depth; "
    "trade-secret or installed-base moats.",
    warnings=("margin_collapse", "revenue_shrinking"))


def _runway(ctx, cfg, scope, s=0.0):
    thr = cfg_get(cfg, f"screens.{scope}.min_cash_runway_years")
    if s:
        thr = _scaled(">=", thr, s)
    v = ctx.get("cash_runway_years")
    if v is None:
        return NODATA, None, thr, "no operating cash flow or cash"
    return (PASS if v >= thr else FAIL), v, thr, "cash-flow positive" if v >= 99 else ""


def _debt_light(ctx, cfg, scope, s=0.0):
    thr = cfg_get(cfg, f"screens.{scope}.max_debt_to_liquid_assets")
    if s:
        thr = _scaled("<=", thr, s)
    liquid = ctx.get("liquid_assets")
    if not liquid:
        return NODATA, None, thr, "no cash on the balance sheet"
    debt = ctx.get("bs_debt") or 0
    v = debt / liquid
    return (PASS if v <= thr else FAIL), v, thr, "" if ctx.get("bs_debt_found") else "no debt tag (treated as none)"


def _fresh_bs(ctx, cfg, scope, s=0.0):
    thr = cfg_get(cfg, f"screens.{scope}.max_balance_sheet_age_days")
    d = ctx.get("bs_age_days")
    if d is None:
        return NODATA, None, thr, "no balance sheet"
    return (PASS if d <= thr else FAIL), d, thr, ""


HC_CLINICAL_GATES = [
    Gate("B1", "Recent balance sheet", "bs_age_days", "<=", "max_balance_sheet_age_days",
         "Cash burns fast: the cash figure must be recent.", fn=_fresh_bs, fmt="int", near=False),
    Gate("B2", "Cash runway", "cash_runway_years", ">=", "min_cash_runway_years",
         "Flynn/Chen: biotechs are cash-burning and financing-dependent; avoid forced raises at the bottom.",
         fn=_runway, fmt="years"),
    Gate("B3", "Little debt", "debt_to_liquid_assets", "<=", "max_debt_to_liquid_assets",
         "Debt or converts ahead of equity erode the cash floor.", fn=_debt_light, fmt="mult"),
    Gate("B4", "Size", "market_cap_usd", ">=", "min_market_cap_usd", "Tradeable size.", needs_price=True,
         fmt="usd", near=False, nodata_note=lambda c: c.get("val_issue") or "no market cap"),
    Gate("B5", "Liquidity", "adv_usd", ">=", "min_adv_usd", "Tradeable volume.", needs_price=True, fmt="usd",
         near=False, nodata_note="no trading volume in the quote"),
    Gate("B6", "Floor value", "ev_to_liquid_assets", "<=", "max_ev_to_liquid_assets",
         "Johnson (Caligan): buy a floor and get the binary cheaply - EV near or below cash. Greenblatt: net cash "
         "~ market cap with no burn is a 'free option'.", needs_price=True, fmt="mult",
         nodata_note=lambda c: c.get("val_issue") or "EV / cash unavailable"),
]
HC_CLINICAL = Screen(
    "hc_clinical", "Healthcare - Pre-revenue & clinical",
    "Pre-revenue and early-commercial pharma, biotech and medtech whose market value is near or below their "
    "cash, with at least 2 years of runway. Numbers can't judge the science (Chen) - this list is the floor-value "
    "options book; the AI review reads the pipeline.",
    "Dave Johnson (Caligan), Bihua Chen (Cormorant), Jim Flynn (Deerfield), Greenblatt",
    u_hc_clinical, HC_CLINICAL_GATES,
    {"floor": [("ev_to_liquid_assets", False)],
     "survival": [("cash_runway_years", True), ("debt_to_liquid_assets", False)],
     "traction": [("ttm_revenue", True), ("ytd_revenue_growth", True)],
     "dilution": [("share_count_change_latest", False)]},
    {"floor": 40, "survival": 30, "traction": 15, "dilution": 15},
    ["hc_stage", "market_cap_usd", "liquid_assets_usd", "ev_to_liquid_assets", "cash_runway_years",
     "annual_cash_burn", "debt_to_liquid_assets", "ttm_revenue", "ytd_revenue_growth", "share_count_change_latest",
     "adv_usd", "bs_date"],
    "Lead asset and phase; approved products and royalties; next binary catalyst and date; is the cash floor real "
    "(burn, converts, obligations)? Biology causal (genetic validation) or correlational? Crowded mechanism? "
    "Management's capital-allocation record. ~8 of 10 post-data collapses are deserved (Chen).")


# ====================================================================== 6. CAPACITY-CYCLE CYCLICALS
def _ev_norm(ctx, cfg, scope, s=0.0):
    thr = cfg_get(cfg, f"screens.{scope}.max_ev_normalized_ebit")
    if s:
        thr = _scaled("<=", thr, s)
    v = ctx.get("ev_normalized_ebit")
    if v is None:
        if ctx.get("normalized_ebit") is not None and ctx["normalized_ebit"] <= 0:
            return FAIL, None, thr, "average EBIT over the cycle <= 0"
        return NODATA, None, thr, ctx.get("val_issue") or "EV / normalized EBIT unavailable"
    return (PASS if v <= thr else FAIL), v, thr, ""


CYCLICAL_GATES = [
    Gate("C1", "Full cycle of history", "years_with_data", ">=", "min_years", "Need a full cycle to normalize.",
         near=False, fmt="int"),
    g_recent("C2", "screens.cyclicals.max_years_since_latest_fy"),
    g_size("C3", "screens.cyclicals.min_revenue_usd"),
    Gate("C4", "Mid-cycle returns", "roic_median", ">=", "min_median_roic",
         "Haley: mid-cycle ROIC >= 10% - a good business in a cyclical industry.", fmt="pct"),
    Gate("C5", "Survives downturns", "positive_ebit_years", ">=", "min_positive_ebit_years",
         "Profitable in most years of the cycle.", fmt="int"),
    _gate_lev("C6", "max_net_debt_to_norm_ebitda", "Gaines/Haley: no leverage that a trough can break "
              "(net debt / average EBITDA over the cycle).", basis="normalized", name="Normalized leverage"),
    Gate("C7", "Not at peak margins", "op_margin_percentile_10y", "<=", "max_margin_percentile",
         "Druckenmiller: buy when margins are depressed and capacity is leaving; avoid when the industry is "
         "expanding. Latest operating margin vs the company's own 10-year range.", fmt="pct",
         nodata_note="need 5+ years of margins"),
    Gate("C8", "Cheap on normalized earnings", "ev_normalized_ebit", "<=", "max_ev_normalized_ebit",
         "Greenblatt: value on normalized (cycle-average) EBIT; Haley: trough multiple on trough margins.",
         needs_price=True, fn=_ev_norm, fmt="mult"),
]
CYCLICALS = Screen(
    "cyclicals", "Capacity-cycle Cyclicals",
    "Good businesses in cyclical industries (materials, energy, transport, semis, housing, machinery), bought "
    "when margins are in the lower half of their own cycle and the price is low against cycle-average earnings. "
    "Industry-level trough signals rank the list.",
    "Druckenmiller (capacity cycle), Haley (trough multiple x trough margin), Greenblatt (normalized earnings), Gaines",
    u_cyclicals, CYCLICAL_GATES,
    {"industry_trough": [("industry_margin_percentile", False), ("industry_capex_to_da", False)],
     "company_trough": [("op_margin_percentile_10y", False)],
     "value": [("ev_normalized_ebit", False)],
     "quality": [("roic_median", True), ("positive_ebit_years", True)],
     "balance_sheet": [("net_debt_to_norm_ebitda", False)]},
    {"industry_trough": 25, "company_trough": 20, "value": 25, "quality": 20, "balance_sheet": 10},
    ["cycle_group", "industry_margin_percentile", "industry_capex_to_da", "industry_trough_zone",
     "op_margin_percentile_10y", "operating_margin_latest", "operating_margin_median", "roic_median",
     "positive_ebit_years", "net_debt_to_norm_ebitda", "market_cap_usd", "ev_normalized_ebit", "ev_ebit",
     "capex_to_da_3y"],
    "Where is the industry in its capacity cycle (closures vs announced expansions)? Is the company's low margin "
    "cyclical or structural (a 'temporary or permanent' problem)? Balance sheet through another down year?")


# ====================================================================== screens from the second batch of interviews
# Shared universe: operating companies outside balance-sheet finance (EV and margins mean nothing for banks, insurers,
# funds and real-estate holders). Used by Asset-Floor Value, Hidden Earnings and Red Flags.
def broad_ok(info, cfg):
    if in_ranges(info.get("sic"), NEVER):
        return False
    r = in_ranges(info.get("sic"), STRUCTURAL_EXCLUDE)
    return not (r and not in_ranges(info.get("sic"), STRUCTURAL_KEEP) and not screen_anyway(info, cfg))


def u_broad(info, m, cfg):
    if in_ranges(info.get("sic"), NEVER):
        return False, "fund / SPAC / REIT / shell"
    r = in_ranges(info.get("sic"), STRUCTURAL_EXCLUDE)
    if r and not in_ranges(info.get("sic"), STRUCTURAL_KEEP) and not screen_anyway(info, cfg):
        return False, f"excluded industry: {r[2]}"
    return True, info.get("sicDescription") or ""


def u_real_assets(info, m, cfg):
    if in_ranges(info.get("sic"), NEVER):
        return False, "fund / SPAC / REIT / shell"
    r = in_ranges(info.get("sic"), REAL_ASSETS)
    return (True, r[2]) if r else (False, "not a land, mineral, water, timber or pipeline owner")


def u_red_flags(info, m, cfg):
    ok, why = u_broad(info, m, cfg)
    if not ok:
        return ok, why
    # pre-revenue drug and device developers burn cash by design: they have their own screen
    if in_ranges(info.get("sic"), CLINICAL_STAGE) and not _is_commercial(m, cfg):
        return False, "clinical-stage healthcare (see the clinical screen)"
    return True, why


def _thr(cfg, scope, name, s=0.0, op=">="):
    t = cfg_get(cfg, f"screens.{scope}.{name}")
    return _scaled(op, t, s) if s else t


def g_price_size(gid, key="min_market_cap_usd", insight="Tradeable size."):
    return Gate(gid, "Size (market cap)", "market_cap_usd", ">=", key, insight, needs_price=True, fmt="usd",
                near=False, nodata_note=lambda c: c.get("val_issue") or "no market cap")


def g_liquidity(gid, key="min_adv_usd"):
    return Gate(gid, "Liquidity", "adv_usd", ">=", key, "Tradeable volume.", needs_price=True, fmt="usd", near=False,
                nodata_note="no trading volume in the quote")


def _fcf_custom(scope, key):
    def fn(ctx, cfg, sc, s=0.0):
        return _g7_custom(ctx, cfg_get(cfg, f"screens.{sc}.{key}"), s)
    return fn


# ---------------------------------------------------------------------- 7. OWNER-OPERATORS (Stahl)
def _insider(ctx, cfg, scope, s=0.0):
    thr = _thr(cfg, scope, "min_insider_share", s)
    v = ctx.get("insider_share")
    if v is None:
        if ctx.get("insider_share_unverified") is not None:
            return NODATA, None, thr, ("market cap unverified (" + (ctx.get("val_issue") or "share count") +
                                       ") - insider share can't be trusted")
        if not ctx.get("public_float"):
            return NODATA, None, thr, "no public float on the annual report's cover page"
        if ctx.get("insider_issue"):
            return NODATA, None, thr, ctx["insider_issue"]
        if ctx.get("price") is None:
            return NODATA, None, thr, ctx.get("val_issue") or "no price"
        return NODATA, None, thr, ctx.get("pf_close_note") or "no price on the public-float date"
    note = (f"public float ${ctx['public_float'] / 1e6:,.0f}M on {ctx.get('public_float_date')} at "
            f"${ctx.get('pf_close', 0):.2f}, against {ctx.get('insider_basis') or 'the share count'}")
    if v >= 0.5:
        note += " - controlled company: founder/family, or a parent company's subsidiary? (check the proxy)"
    return (PASS if v >= thr else FAIL), v, thr, note


OWNERS_GATES = [
    Gate("O1", "History", "years_with_data", ">=", "min_years", "Enough years to judge returns.", near=False,
         fmt="int"),
    g_recent("O2", "screens.owners.max_years_since_latest_fy"),
    g_size("O3", "screens.owners.min_revenue_usd"),
    Gate("O4", "Insider ownership", "insider_share", ">=", "min_insider_share",
         "Stahl: owner-operators run a company 'because they own more equity than anyone else' and earned 'the bulk "
         "of the return' in the S&P 500 back to 1957, yet index weighting by free float under-owns them. Insider "
         "share = 1 - the public float the company reports / its market value on that date.",
         needs_price=True, fn=_insider, fmt="pct"),
    Gate("O5", "Consistent profits", "operating_loss_years", "<=", "max_operating_loss_years",
         "A real business, not a lottery ticket.", near=False, fmt="int"),
    Gate("O6", "High returns", "roic_median", ">=", "min_median_roic",
         "Owners compound only if the business earns well on capital.", fmt="pct"),
    Gate("O7", "Cash conversion", "fcf_conversion", ">=", "min_fcf_conversion", "Profits must turn into cash.",
         fn=_fcf_custom("owners", "min_fcf_conversion"), fmt="mult"),
    _gate_lev("O8", "max_net_debt_to_ebitda", "Owners who borrow heavily can lose the company in one bad year."),
    g_price_size("O9"),
    g_liquidity("O10"),
    Gate("O11", "Valuation", "ev_ebit", "<=", "max_ev_ebit",
         "Stahl: owner-operators often carry the lowest valuations ('It shouldn't exist, yet it does').",
         needs_price=True, fmt="mult", nodata_note=lambda c: c.get("val_issue") or "EV/EBIT unavailable"),
]
OWNERS = Screen(
    "owners", "Owner-Operators",
    "Profitable, high-return companies where insiders own a large stake (at least 20% by default). Index funds "
    "weight by freely traded shares, so these are under-owned and often cheaper. Insider share comes from the "
    "public float each company reports on its annual report cover.",
    "Murray Stahl (Horizon Kinetics), Connor Haley (insider ownership), Watsa",
    u_core, OWNERS_GATES,
    {"ownership": [("insider_share", True)],
     "returns": [("roic_median", True), ("cash_roic_median", True)],
     "growth": [("revenue_cagr", True), ("fcf_per_share_cagr", True)],
     "capital_allocation": [("share_count_cagr", False), ("acquisitions_to_ocf", False)],
     "value": [("earnings_yield", True), ("fcf_yield", True)],
     "unindexed": [("market_cap_usd", False)]},
    {"ownership": 25, "returns": 20, "growth": 15, "capital_allocation": 15, "value": 15, "unindexed": 10},
    ["insider_share", "public_float_date", "market_cap_usd", "roic_median", "cash_roic_median", "revenue_cagr",
     "fcf_conversion", "share_count_cagr", "net_debt_to_ebitda", "ev_ebit", "fcf_yield", "pe", "adv_usd"],
    "Who are the insiders: founder/family (owner-operator) or a parent company (a subsidiary; minority holders "
    "may be second-class)? Is management paid 'independent of the long-term value of the shares' (an "
    "agent-operator)? Related-party dealings, share classes with extra votes, succession, and what the owner does "
    "with the cash (Stahl, Watsa).",
    warnings=("margin_collapse", "revenue_shrinking"))


# ---------------------------------------------------------------------- 8. HARD ASSETS & ROYALTIES (Stahl, Alfred)
def _low_reinvest(ctx, cfg, scope, s=0.0):
    thr = _thr(cfg, scope, "max_capex_to_ocf", s, "<=")
    if ctx.get("ocf_avg_3y") is not None and ctx["ocf_avg_3y"] <= 0:
        return FAIL, None, thr, "operating cash flow <= 0 over the last 3 years"
    v = ctx.get("capex_to_ocf_3y")
    if v is None:
        if not ctx.get("capex_found"):
            return NODATA, None, thr, "capital expenditure isn't tagged with a standard XBRL tag"
        return NODATA, None, thr, "no capex / operating cash flow for the last 3 years"
    return (PASS if v <= thr else FAIL), v, thr, ""


REAL_GATES = [
    Gate("R1", "History", "years_with_data", ">=", "min_years", "Enough years to see a cycle.", near=False,
         fmt="int"),
    g_recent("R2", "screens.real_assets.max_years_since_latest_fy"),
    g_size("R3", "screens.real_assets.min_revenue_usd"),
    Gate("R4", "Little reinvestment", "capex_to_ocf_3y", "<=", "max_capex_to_ocf",
         "Stahl: royalty and land owners need no reinvestment - 'a call option on everything'. Capex as a share "
         "of operating cash flow, last 3 years; producers and builders fail here.", fn=_low_reinvest, fmt="pct"),
    Gate("R5", "Royalty-like margins", "operating_margin_median", ">=", "min_operating_margin_median",
         "Owning the asset rather than working it shows up as very high margins (10-year median).", fmt="pct"),
    Gate("R6", "Consistent profits", "operating_loss_years", "<=", "max_operating_loss_years",
         "Profitable through commodity cycles.", near=False, fmt="int"),
    _gate_lev("R7", "max_net_debt_to_ebitda", "No leverage a commodity slump can break."),
    g_price_size("R8"),
    g_liquidity("R9"),
    Gate("R10", "Valuation", "ev_ebit", "<=", "max_ev_ebit",
         "Even a perfect royalty can be bought too dear.", needs_price=True, fmt="mult",
         nodata_note=lambda c: c.get("val_issue") or "EV/EBIT unavailable"),
]
REAL_ASSETS_SCREEN = Screen(
    "real_assets", "Hard Assets & Royalties",
    "Owners of land, minerals, royalties, water, timber and pipelines that need little reinvestment and earn "
    "very high margins - the assets Stahl expected to gain as disinflation ends. Excluded from Core as price "
    "takers; kept here only if they barely reinvest.",
    "Murray Stahl (Horizon Kinetics), Mike Alfred (Alpine Fox), Einhorn (supply discipline)",
    u_real_assets, REAL_GATES,
    {"margins": [("operating_margin_median", True), ("ttm_operating_margin", True)],
     "low_reinvestment": [("capex_to_ocf_3y", False)],
     "cash": [("fcf_yield", True), ("fcf_conversion", True)],
     "growth": [("revenue_cagr", True), ("revenue_cagr_3y", True)],
     "balance_sheet": [("net_debt_to_ebitda", False)]},
    {"margins": 25, "low_reinvestment": 25, "cash": 20, "growth": 15, "balance_sheet": 15},
    ["capex_to_ocf_3y", "operating_margin_median", "ttm_operating_margin", "revenue_cagr", "revenue_cagr_3y",
     "fcf_conversion", "net_debt_to_ebitda", "market_cap_usd", "ev_ebit", "fcf_yield", "pe", "adv_usd"],
    "Dormant assets the accounts don't value (land carried at no value, unexplored acreage, non-producing "
    "royalties); how much depends on one commodity price; trust termination dates; water and surface rights; "
    "who operates the assets and how reliably (Stahl, Alfred).")


# ---------------------------------------------------------------------- 9. ASSET-FLOOR VALUE (Watsa)
def _floor(ctx, cfg, scope, s=0.0):
    t_cash = _thr(cfg, scope, "max_mcap_to_net_cash", s, "<=")
    t_tb = _thr(cfg, scope, "max_price_to_tangible_book", s, "<=")
    nc, tb = ctx.get("mcap_to_net_cash"), ctx.get("price_to_tangible_book")
    if nc is None and tb is None:
        if ctx.get("mcap_to_net_cash_unverified") is not None or ctx.get("price_to_tangible_book_unverified") is not None:
            return NODATA, None, (t_cash, t_tb), "market cap unverified (" + (ctx.get("val_issue") or "") + ")"
        if ctx.get("price") is None:
            return NODATA, None, (t_cash, t_tb), ctx.get("val_issue") or "no price"
        if (ctx.get("net_cash") is not None and ctx["net_cash"] <= 0) and \
                (ctx.get("tangible_book") is not None and ctx["tangible_book"] <= 0):
            return FAIL, None, (t_cash, t_tb), "no net cash and no positive tangible book"
        return NODATA, None, (t_cash, t_tb), "no balance sheet to measure the floor"
    if nc is not None and nc <= t_cash and ctx.get("bs_debt_found"):
        return PASS, nc, (t_cash, t_tb), f"market cap {nc:.2f}x net cash (cash + investments - all debt)"
    if tb is not None and tb <= t_tb:
        return PASS, tb, (t_cash, t_tb), f"price {tb:.2f}x tangible book (equity - goodwill - intangibles)"
    if nc is not None and nc <= t_cash:
        # below cash only if it really has no debt: no debt tag at all needs a look at the balance sheet
        return NODATA, nc, (t_cash, t_tb), (f"market cap {nc:.2f}x cash, but no debt tag found: check the balance "
                                            "sheet")
    best = min(x for x in (nc, tb) if x is not None)
    return FAIL, best, (t_cash, t_tb), ""


def _not_burning(ctx, cfg, scope, s=0.0):
    thr = _thr(cfg, scope, "min_runway_if_burning", s)
    ocf = ctx.get("ttm_ocf")
    if ocf is None:
        return NODATA, None, thr, "no operating cash flow"
    if ocf >= 0:
        return PASS, ocf, thr, "cash flow positive"
    v = ctx.get("cash_runway_years")
    if v is None:
        return NODATA, None, thr, "no cash figure"
    return (PASS if v >= thr else FAIL), v, thr, f"burning cash: {v:.1f} years of runway"


def _profit_share(ctx, cfg, scope, s=0.0):
    thr = _thr(cfg, scope, "min_profitable_share", s)
    v = ctx.get("positive_ebit_share")
    if v is None:
        return NODATA, None, thr, "fewer than 3 years of operating results"
    return (PASS if v >= thr else FAIL), v, thr, ""


FLOOR_GATES = [
    Gate("K1", "History", "years_total", ">=", "min_years", "Enough years to see a record.", near=False, fmt="int"),
    g_recent("K2", "screens.asset_floor.max_years_since_latest_fy"),
    Gate("K3", "Recent balance sheet", "bs_age_days", "<=", "max_balance_sheet_age_days",
         "The floor is measured on the latest balance sheet, so it must be recent.", fn=_fresh_bs, fmt="int",
         near=False),
    Gate("K4", "Below a hard floor", "mcap_to_net_cash", "<=", None,
         "Watsa: buy below cash per share and you get the plants and inventories 'for free' (Seagram at $65 vs "
         "~$70 of cash doubled and tripled). Passes at market cap <= net cash, or price <= tangible book.",
         needs_price=True, fn=_floor, fmt="mult",
         desc=lambda c, s: (f"market cap at most {cfg_get(c, 'screens.asset_floor.max_mcap_to_net_cash'):.1f}× "
                            f"net cash, or price at most "
                            f"{cfg_get(c, 'screens.asset_floor.max_price_to_tangible_book'):.1f}× tangible book")),
    Gate("K5", "Not burning the floor", "ttm_ocf", ">=", None,
         "A floor a company is burning through isn't a floor.", fn=_not_burning, fmt="years",
         desc=lambda c, s: (f"operating cash flow positive, or at least "
                            f"{cfg_get(c, 'screens.asset_floor.min_runway_if_burning'):.0f} years of cash")),
    Gate("K6", "Usually profitable", "positive_ebit_share", ">=", "min_profitable_share",
         "Davis/Greenblatt: a cheap business that never earns is a value trap.", fn=_profit_share, fmt="pct"),
    _gate_lev("K7", "max_net_debt_to_ebitda", "Debt ahead of shareholders erodes the floor."),
    g_price_size("K8"),
    g_liquidity("K9"),
]
ASSET_FLOOR = Screen(
    "asset_floor", "Asset-Floor Value",
    "Companies priced at or below their net cash, or below tangible book, that still generate cash and are "
    "usually profitable. The extreme margin of safety: the market fears management will waste the assets.",
    "Prem Watsa (Fairfax), Greenblatt (net cash as a free option), Davis (value traps)",
    u_broad, FLOOR_GATES,
    {"floor": [("mcap_to_net_cash", False), ("price_to_tangible_book", False)],
     "cash": [("fcf_yield", True), ("fcf_yield_5y", True)],
     "quality": [("roic_median", True), ("positive_ebit_share", True)],
     "balance_sheet": [("net_debt_to_ebitda", False)]},
    {"floor": 40, "cash": 25, "quality": 20, "balance_sheet": 15},
    ["mcap_to_net_cash", "price_to_tangible_book", "net_cash", "tangible_book", "market_cap_usd", "fcf_yield",
     "fcf_yield_5y", "roic_median", "positive_ebit_share", "ttm_operating_margin", "net_debt_to_ebitda", "adv_usd",
     "bs_date"],
    "Why is it this cheap? Will management waste the cash (Seagram's did - but ~25 years later)? Is the cash "
    "trapped abroad, pledged or owed to a parent (VIE structures, China ADRs)? Are inventories and receivables "
    "real, or due for a write-down? Pensions, lawsuits or leases off the balance sheet? A catalyst - buybacks, a "
    "sale, an activist (Watsa)?")


# ---------------------------------------------------------------------- 10. TROUGH CYCLICAL CASH (Einhorn)
def _cash_years(ctx, cfg, scope, s=0.0):
    n, tot = ctx.get("fcf_positive_years"), ctx.get("fcf_years")
    if not tot or tot < 5:
        return NODATA, None, None, "fewer than 5 years of free cash flow (capex not tagged?)"
    allowed = cfg_get(cfg, f"screens.{scope}.max_negative_fcf_years")
    if ctx.get("fcf_avg_5y") is not None and ctx["fcf_avg_5y"] <= 0:
        return FAIL, n / tot, allowed, f"{n} of {tot} years FCF-positive, but the 5-year average is negative"
    return (PASS if tot - n <= allowed else FAIL), n / tot, allowed, f"{n} of {tot} years FCF-positive"


def _capex_discipline(ctx, cfg, scope, s=0.0):
    thr = _thr(cfg, scope, "max_capex_to_da_3y", s, "<=")
    v = ctx.get("capex_to_da_3y")
    if v is None:
        return NODATA, None, thr, "capex or depreciation not tagged"
    return (PASS if v <= thr else FAIL), v, thr, ""


def _fcf5_yield(ctx, cfg, scope, s=0.0):
    thr = _thr(cfg, scope, "min_fcf_yield_5y", s)
    v = ctx.get("fcf_yield_5y")
    if v is None:
        if ctx.get("fcf_avg_5y") is None:
            return NODATA, None, thr, "fewer than 4 of the last 5 years with free cash flow"
        return NODATA, None, thr, ctx.get("val_issue") or "no market cap"
    return (PASS if v >= thr else FAIL), v, thr, ""


TROUGH_GATES = [
    Gate("T1", "Full cycle of history", "years_with_data", ">=", "min_years", "Need a full cycle to judge.",
         near=False, fmt="int"),
    g_recent("T2", "screens.trough_cash.max_years_since_latest_fy"),
    g_size("T3", "screens.trough_cash.min_revenue_usd"),
    Gate("T4", "Margins below normal", "op_margin_percentile_10y", "<=", "max_margin_percentile",
         "Einhorn on Solvay: buy at the trough, not at mid-cycle. Latest operating margin vs the company's own "
         "10-year range.", fmt="pct", nodata_note="need 5+ years of margins"),
    Gate("T5", "Cash through the cycle", "fcf_positive_years", None, None,
         "A cash machine pays you to wait: free cash flow positive in most years, troughs included.",
         fn=_cash_years, fmt="pct", near=False,
         desc=lambda c, s: f"at most {c['screens'][s]['max_negative_fcf_years']} year(s) with negative FCF"),
    Gate("T6", "Not adding capacity", "capex_to_da_3y", "<=", "max_capex_to_da_3y",
         "Einhorn: 'higher prices aren't fueling new capacity instead they're fueling buybacks'. Capex / "
         "depreciation over 3 years near 1 = maintaining, not expanding.", fn=_capex_discipline, fmt="mult"),
    _gate_lev("T7", "max_net_debt_to_norm_ebitda", "A trough can't break it (net debt / cycle-average EBITDA).",
              basis="normalized", name="Normalized leverage"),
    Gate("T8", "Cash yield on the cycle", "fcf_yield_5y", ">=", "min_fcf_yield_5y",
         "Einhorn: Solvay's 5-year post-capex free cash flow roughly equalled its market cap. 5-year average free "
         "cash flow / market cap.", needs_price=True, fn=_fcf5_yield, fmt="pct"),
    g_price_size("T9"),
    g_liquidity("T10"),
]
TROUGH_CASH = Screen(
    "trough_cash", "Trough Cyclical Cash",
    "Cyclical producers at depressed margins that still throw off cash through the cycle, aren't adding "
    "capacity, and trade at a high cycle-average free-cash-flow yield. Industries returning cash instead of "
    "building rank higher.",
    "David Einhorn (Greenlight: Solvay, 'eventually is now'), Druckenmiller (capacity cycle), Stahl",
    u_cyclicals, TROUGH_GATES,
    {"cash_yield": [("fcf_yield_5y", True), ("fcf_yield", True)],
     "industry_discipline": [("industry_returns_to_capex", True), ("industry_capex_to_da", False)],
     "company_discipline": [("returns_to_capex_5y", True), ("capex_to_da_3y", False)],
     "trough": [("op_margin_percentile_10y", False), ("industry_margin_percentile", False)],
     "balance_sheet": [("net_debt_to_norm_ebitda", False)]},
    {"cash_yield": 30, "industry_discipline": 20, "company_discipline": 15, "trough": 20, "balance_sheet": 15},
    ["cycle_group", "fcf_yield_5y", "fcf_yield", "op_margin_percentile_10y", "industry_margin_percentile",
     "industry_returns_to_capex", "industry_capex_to_da", "returns_to_capex_5y", "capex_to_da_3y",
     "net_debt_to_norm_ebitda", "market_cap_usd", "ev_normalized_ebit", "adv_usd"],
    "Trough or mid-cycle (Einhorn on Solvay, Apr 2024)? Is supply leaving the industry (closures, no new "
    "capacity announced)? Is the bear case about one segment while most revenue sits elsewhere? Is the low "
    "margin cyclical or structural? Freight or regulation protecting regional prices?")


# ---------------------------------------------------------------------- 11. HIDDEN EARNINGS (Einhorn, Stahl, Sandler)
def _hidden_trigger(ctx, cfg, scope, s=0.0):
    thr = _thr(cfg, scope, "max_drawdown_12m", s, "<=")
    if ctx.get("disc_ops_material"):
        return PASS, None, thr, "unit sold or spun off: " + (ctx.get("disc_ops_note") or "discontinued operations")
    v = ctx.get("drawdown_12m")
    if v is None:
        if ctx.get("price") is None:
            return NODATA, None, thr, "no discontinued operations; no price to measure a fall"
        return NODATA, None, thr, "no discontinued operations; no 12-month price history"
    if v <= -0.9:
        return NODATA, v, thr, (f"price {v:.0%} from its 12-month high - check for a split, reverse split or "
                                "ticker change before trusting this")
    if ctx.get("splits_unknown") and v <= thr and any(abs((1 + v) * k - 1) < 0.04 for k in range(2, 11)):
        return NODATA, v, thr, (f"price {v:.0%} from its 12-month high - about what a stock split would show, and "
                                "the split list was unavailable: check before trusting this")
    note = f"price {v:.0%} from its 12-month high (${ctx.get('high_12m_used', 0):,.2f})"
    return (PASS if v <= thr else FAIL), v, thr, note


def _ttm_positive(metric, label):
    def fn(ctx, cfg, scope, s=0.0):
        v = ctx.get(metric)
        if v is None:
            return NODATA, None, 0, f"no {label}"
        return (PASS if v > 0 else FAIL), v, 0, ""
    return fn


HIDDEN_GATES = [
    Gate("X1", "History", "years_with_data", ">=", "min_years", "Enough years to know the business.", near=False,
         fmt="int"),
    g_recent("X2", "screens.hidden.max_years_since_latest_fy"),
    Gate("X3", "Something the market is ignoring", "drawdown_12m", "<=", "max_drawdown_12m",
         "Einhorn/Stahl: coverage fixates on a feared segment, and a spin-off or sale lifts the remaining "
         "business's numbers ('It's just a different way of calculating'). Sandler: quants bucket on trailing "
         "figures. Passes with material discontinued operations (last 3 years) or a price far below its 12-month "
         "high.", needs_price=True, fn=_hidden_trigger, fmt="pct",
         desc=lambda c, s: ("discontinued operations in the last 3 years, or price at least "
                            f"{-cfg_get(c, 'screens.hidden.max_drawdown_12m'):.0%} below its 12-month high")),
    Gate("X4", "Still earning", "ttm_operating_income", ">", None,
         "The remaining business must be profitable now (operating income excludes discontinued operations).",
         fn=_ttm_positive("ttm_operating_income", "operating income"), fmt="usd", near=False,
         desc="operating income, last 12 months, > 0"),
    Gate("X5", "Sales holding up", "revenue_cagr_3y", ">=", "min_revenue_cagr_3y",
         "Temporary or permanent (Greenblatt)? Revenue mustn't be in steady decline.", fmt="pct",
         nodata_note="need revenue 3 years ago"),
    Gate("X6", "Still generating cash", "ttm_fcf", ">", None, "Free cash flow positive over the last 12 months.",
         fn=_ttm_positive("ttm_fcf", "free cash flow (capex not tagged?)"), fmt="usd", near=False,
         desc="free cash flow, last 12 months, > 0"),
    Gate("X7", "Decent returns", "roic_median", ">=", "min_median_roic", "A good business behind the mess.",
         fmt="pct"),
    _gate_lev("X8", "max_net_debt_to_ebitda", "Gaines: debt turns a messy situation into an option bet."),
    Gate("X9", "Cheap", "ev_ebit", "<=", "max_ev_ebit",
         "Greenblatt: special situations work best bought cheaply.", needs_price=True, fmt="mult",
         nodata_note=lambda c: c.get("val_issue") or "EV/EBIT unavailable"),
    g_price_size("X10"),
    g_liquidity("X11"),
]
HIDDEN = Screen(
    "hidden", "Hidden Earnings",
    "Profitable, cash-generating businesses the market is looking past: parents that just sold or spun off a "
    "unit (their averages improve once it's gone), and sound companies whose price has fallen far below its "
    "12-month high. A shortlist for reading the segment notes.",
    "David Einhorn (Solvay), Murray Stahl (spin-off parents), Ricky Sandler (Zillow, quant buckets), Greenblatt",
    u_broad, HIDDEN_GATES,
    {"value": [("earnings_yield", True), ("fcf_yield", True)],
     "quality": [("roic_median", True), ("ttm_operating_margin", True)],
     "dislocation": [("drawdown_12m", False)],
     "balance_sheet": [("net_debt_to_ebitda", False)]},
    {"value": 35, "quality": 25, "dislocation": 20, "balance_sheet": 20},
    ["disc_ops_note", "drawdown_12m", "high_12m_used", "market_cap_usd", "ev_ebit", "fcf_yield", "earnings_yield",
     "roic_median", "ttm_operating_margin", "revenue_cagr_3y", "net_debt_to_ebitda", "adv_usd"],
    "Which segment is the market fixated on, and how much revenue sits elsewhere (Solvay: ~70% outside soda "
    "ash)? Is a trailing loss from a business being exited (Zillow)? What does the parent look like without the "
    "unit it shed? Why did the price fall - temporary or permanent - and who is forced to sell (index deletion, "
    "'AI loser' baskets with 'literally no buyers')?")


# ---------------------------------------------------------------------- 12. RED FLAGS (avoid list)
def _expensive(ctx, cfg, scope, s=0.0):
    thr = _thr(cfg, scope, "min_ev_sales", s)
    v = ctx.get("ev_sales")
    if v is None:
        if ctx.get("ev_sales_unverified") is not None:
            return NODATA, None, thr, "market cap unverified (" + (ctx.get("val_issue") or "") + ")"
        return NODATA, None, thr, ctx.get("val_issue") or "EV / sales unavailable"
    return (PASS if v >= thr else FAIL), v, thr, ""


def red_flag_signals(ctx, cfg, scope="red_flags"):
    c = cfg["screens"][scope]
    out = []
    g3, now = ctx.get("revenue_cagr_3y"), ctx.get("ytd_revenue_growth")
    src = "year-to-date"
    if now is None:
        now, src = ctx.get("revenue_growth_latest_fy"), "latest fiscal year"
    if g3 is not None and now is not None and g3 >= c["fading_min_cagr_3y"] and now < c["fading_ratio"] * g3:
        out.append(f"growth fading: {now:+.0%} ({src}) vs {g3:+.0%}/yr over 3 years (Cohen)")
    if ctx.get("gross_margin_down_3y"):
        out.append(f"gross margin down 3 years running ({ctx.get('gross_margin_change_3y', 0):+.1%}) (Nadella)")
    om = ctx.get("operating_margin_change_3y")
    op = ctx.get("ttm_operating_income")
    if op is not None and op <= 0:
        # a loss usually also shows as a margin drop: counted once, so one bad year isn't two signals
        out.append("losing money (operating loss, last 12 months) (Einhorn's 'bubble basket')")
    elif om is not None and om <= -c["margin_drop_3y"]:
        out.append(f"operating margin {om:+.1%} over 3 years")
    dil = ctx.get("share_count_cagr_3y")
    if dil is not None and dil >= c["dilution_3y"]:
        out.append(f"share count +{dil:.0%}/yr over 3 years")
    if g3 is not None and g3 < 0:
        out.append(f"revenue shrinking {g3:+.0%}/yr over 3 years")
    return out


def _deteriorating(ctx, cfg, scope, s=0.0):
    thr = cfg_get(cfg, f"screens.{scope}.min_signals")
    sig = red_flag_signals(ctx, cfg, scope)
    if not sig and ctx.get("revenue_cagr_3y") is None and ctx.get("operating_margin_change_3y") is None:
        return NODATA, None, thr, "not enough history to judge deterioration"
    return (PASS if len(sig) >= thr else FAIL), len(sig), thr, "; ".join(sig)


RED_GATES = [
    Gate("W1", "History", "years_total", ">=", "min_years", "Enough years to see a trend.", near=False, fmt="int"),
    g_recent("W2", "screens.red_flags.max_years_since_latest_fy"),
    Gate("W3", "Priced for perfection", "ev_sales", ">=", "min_ev_sales",
         "Overvaluation is the first half of a short (Einhorn); high EV/sales names de-rate even without misses "
         "(Druckenmiller).", needs_price=True, fn=_expensive, fmt="mult"),
    Gate("W4", "Something is breaking", "red_flag_count", ">=", "min_signals",
         "Einhorn: 'we've always insisted on over valuation combined with some kind of deterioration'. Signals: "
         "growth fading to under half its 3-year rate, gross margin down 3 years running, operating margin down "
         "5+ points, operating losses, 5%+ yearly dilution, shrinking revenue.", fn=_deteriorating, fmt="int",
         near=False,
         desc=lambda c, s: f"at least {cfg_get(c, 'screens.red_flags.min_signals')} deterioration signal(s)"),
    g_price_size("W5", insight="Big enough to matter to a portfolio."),
    g_liquidity("W6"),
]
RED_FLAGS = Screen(
    "red_flags", "Red Flags (avoid list)",
    "NOT a buy list: companies priced for perfection (high EV/sales) where something is already deteriorating. "
    "Use it to check what you own, and to avoid crowded names. 'Flagged' = every rule matched.",
    "David Einhorn (overvaluation + deterioration), Ricky Sandler, Eduardo Marques, Satya Nadella, Steve Cohen",
    u_red_flags, RED_GATES,
    {"expensive": [("ev_sales", True)],
     "deterioration": [("red_flag_count", True), ("operating_margin_change_3y", False),
                       ("gross_margin_change_3y", False)],
     "dilution": [("share_count_cagr_3y", True)]},
    {"expensive": 40, "deterioration": 45, "dilution": 15},
    ["red_flag_notes", "ev_sales", "ev_ebit", "pe", "revenue_cagr_3y", "ytd_revenue_growth",
     "operating_margin_change_3y", "gross_margin_change_3y", "share_count_cagr_3y", "market_cap_usd", "adv_usd"],
    "Is the deterioration real or a one-off (an acquisition, a mix shift)? Short interest and squeeze risk "
    "(Sandler sizes shorts to survive a 100% squeeze). Will AI deflate its service levels before earnings show "
    "it (Marques)? Insider selling, accounting changes, customer losses to startups or LLMs (Bravo).")

SECOND_BATCH = [OWNERS, REAL_ASSETS_SCREEN, ASSET_FLOOR, TROUGH_CASH, HIDDEN, RED_FLAGS]
for _s in SECOND_BATCH:
    _s.strict = True
AVOID_SCREENS = {"red_flags"}


FIRST_BATCH = [CORE, EMERGING, SPECIAL, FORTRESS, HC_COMMERCIAL, HC_CLINICAL, CYCLICALS]
SCREENS = FIRST_BATCH + SECOND_BATCH
BY_ID = {s.sid: s for s in SCREENS}
VALUATION_GATES = {"E12", "C8", "O11", "R10", "T8", "X9"}           # failing only these -> PRICE
# never 'failed 1 rule': tradeability (size / volume) and each screen's defining test (emerging = profitable and
# growing fast, special = profitable and cheap, clinical = cash runway, little debt and priced near cash, fortress =
# held up in recessions, healthcare = high returns, cyclicals = decent mid-cycle returns and not at peak margins)
HARD_GATES = {"E3", "E4", "E10", "E11", "E13", "S2", "S4", "S5", "S6", "B1", "B2", "B3", "B4", "B5", "B6",
              "F4", "F5", "H5", "C4", "C7",
              # second batch: owners = insider stake; hard assets = little reinvestment + royalty-like margins;
              # asset floor = below the floor and not burning it; trough cash = depressed margins; hidden earnings =
              # the trigger and a profitable remaining business; red flags = expensive AND deteriorating
              "O4", "O9", "O10", "R4", "R5", "R8", "R9", "K4", "K5", "K8", "K9", "T4", "T9", "T10",
              "X3", "X4", "X10", "X11", "W3", "W4", "W5", "W6"}
_ids = [g.gid for s_ in SCREENS for g in s_.gates]
assert len(_ids) == len(set(_ids)), "gate ids must be unique across screens"
for _s in SCREENS:
    for _g in _s.gates:
        _g.valuation = _g.gid in VALUATION_GATES
        _g.one_ok = _g.gid not in HARD_GATES


def data_holds(flags):
    return [f for f in flags if any(k in f for k in HOLD_FLAG_MARKERS)]
