"""Per-company metrics computed from the clean annual series, trailing-twelve-month figures and the latest
balance sheet. Every metric is a plain formula on reported XBRL values; see the Rules sheet.

Price-dependent metrics (market cap, EV multiples) are added later by valuation.py.
"""
import statistics
from datetime import date

from .extract import _d


def _avg(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


def _ratio(a, b):
    if a is None or b is None or b == 0:
        return None
    return a / b


def _cagr(first, last, years):
    if first is None or last is None or years <= 0 or first <= 0 or last <= 0:
        return None
    return (last / first) ** (1.0 / years) - 1


def _sum_or_none(*xs):
    vals = [x for x in xs if x is not None]
    return sum(vals) if vals else None


def _median(xs):
    xs = [x for x in xs if x is not None]
    return statistics.median(xs) if xs else None


def _pctile_of_last(xs):
    """Where the last value sits within the series (0 = lowest, 1 = highest)."""
    xs = [x for x in xs if x is not None]
    if len(xs) < 5:
        return None
    last = xs[-1]
    below = sum(1 for x in xs[:-1] if x < last)
    equal = sum(1 for x in xs[:-1] if x == last)
    return (below + 0.5 * equal) / (len(xs) - 1)


def _cash(g, y=None):
    """Cash + short-term investments; the combined tag if only that exists; None if nothing is tagged."""
    c, s = g("cash", y), g("st_investments", y)
    if c is None and s is None:
        return g("cash_and_sti_combined", y)
    return (c or 0) + (s or 0)


# recession windows: fiscal years ending in these ranges are compared with the year before
RECESSIONS = {"2020": ("2020-03-31", "2021-06-30"), "2009": ("2008-09-30", "2010-03-31")}
# market downturns for Core's 'no loss in a downturn on falling sales' rule (fiscal years ending in the window)
DOWNTURNS = {"2008-09": ("2008-09-30", "2010-03-31"),        # financial crisis
             "2015-16": ("2015-09-30", "2016-12-31"),        # industrial / energy recession
             "2020": ("2020-03-31", "2021-06-30"),           # COVID
             "2022": ("2022-06-30", "2023-06-30")}           # rate shock / bear market


def total_debt(cd, y=None, at=None):
    """Interest-bearing debt at a fiscal year end (y) or a balance-sheet date (at). Takes the LARGEST of the
    available tag combinations (conservative for leverage tests). None if no debt tag is found at all."""
    if at is not None:
        def g(c, _y=None):
            p = cd.bs_at(c, at)
            return p.val if p else None
    else:
        g = cd.get
    cands = []
    if g("debt_combined", y) is not None:
        cands.append(g("debt_combined", y))
    # ShortTermBorrowings often already includes commercial paper: take the larger, don't add
    sb, cp = g("st_borrowings", y), g("commercial_paper", y)
    st = max(sb, cp) if (sb is not None and cp is not None) else _sum_or_none(sb, cp)
    if g("lt_debt_incl_current", y) is not None:
        cands.append(g("lt_debt_incl_current", y) + (st or 0))
    if g("lt_debt_noncurrent", y) is not None:
        cur = g("debt_current", y)
        if cur is None:
            cur = _sum_or_none(g("lt_debt_current", y), st) or 0
        cands.append(g("lt_debt_noncurrent", y) + cur)
    bnc, bc = g("ifrs_bonds_noncurrent", y), g("ifrs_bonds_current", y)
    if bnc is not None or bc is not None:
        cur = g("debt_current", y)
        if cur is None:
            cur = _sum_or_none(g("lt_debt_current", y), st) or 0
        cands.append((g("lt_debt_noncurrent", y) or 0) + (bnc or 0) + (bc or 0) + cur)
    # convertible notes and other notes/loans/credit lines (often the only debt tags at small companies)
    extra = [x for x in (g("convertible_debt", y), g("other_debt", y)) if x is not None]
    if extra:
        cur = g("debt_current", y)
        cands.append(max(extra) + ((cur or 0) if not cands else 0))
    if not cands:
        cur = g("debt_current", y)
        if cur is None:
            cur = _sum_or_none(g("lt_debt_current", y), st)
        if cur is not None:
            cands.append(cur)
    lsc = g("liabilities_subject_to_compromise", y)
    if lsc:
        cands = [c + lsc for c in cands] or [lsc]
    return max(cands) if cands else None


def _year_rows(cd, cfg):
    g = cd.get
    tax_lo, tax_hi = cfg.get("tax_rate_bounds", [0.0, 0.40])
    ic, tc = {}, {}
    for y in sorted(cd.label_end):
        assets, cl = g("assets", y), g("liabilities_current", y)
        cash = _cash(g, y) or 0
        cur_debt = g("debt_current", y)
        if cur_debt is None:
            cur_debt = _sum_or_none(g("lt_debt_current", y), g("st_borrowings", y), g("commercial_paper", y)) or 0
        debt = total_debt(cd, y)
        lti = g("lt_investments", y) or 0
        if assets is not None and cl is not None:
            ic[y] = assets - cash - lti - (cl - cur_debt)
        elif g("equity", y) is not None:
            ic[y] = g("equity", y) + (debt or 0) - cash
        # Greenblatt tangible capital: net working capital (ex cash, ex debt) + net fixed assets
        ca, ppe = g("assets_current", y), g("ppe_net", y)
        if ca is not None and cl is not None and ppe is not None:
            tc[y] = max(ca - cash - (cl - cur_debt), 0) + ppe

    rev_s = cd.series.get("revenue") or {}
    op_s = cd.series.get("operating_income") or {}
    tax_s = cd.series.get("income_tax") or {}

    def pretax(y):
        """Pretax income; if no pretax tag exists (Range Resources, Navios): net income + income tax (tax = 0 when
        the company reports no income tax at all, e.g. shipping partnerships)."""
        p = g("pretax_income", y)
        if p is not None:
            return p, False
        n = g("net_income", y)
        if n is not None and (y in tax_s or not tax_s):
            return n + (g("income_tax", y) or 0), True
        return None, False

    no_rev = not rev_s
    if no_rev:   # e.g. clinical-stage biotech: no revenue tagged at all -> revenue = 0
        years = [y for y in sorted(cd.label_end) if (y in op_s or pretax(y)[0] is not None)]
    else:
        years = [y for y in sorted(rev_s) if (y in op_s or pretax(y)[0] is not None)]
    # One EBIT definition for every year: if the latest year has no operating-income line, every year uses
    # pretax income + interest - other non-operating income (mixing tagged and approximated years would distort
    # margins and trends; earlier 'operating income' tags are sometimes segment totals, e.g. TJX).
    approx_all = bool(years) and g("operating_income", years[-1]) is None

    def nonop_includes_interest():
        """'NonoperatingIncomeExpense' is sometimes the TOTAL below operating income (interest included) and
        sometimes only 'other income'. Decide from years where operating income is tagged too; else from size."""
        errs_a, errs_b = [], []
        for y in years:
            o, p = g("operating_income", y), g("pretax_income", y)
            n, i = g("nonoperating_income", y), abs(g("interest_expense", y) or 0)
            if None not in (o, p, n) and o:
                errs_a.append(abs(p + i - n - o) / abs(o))
                errs_b.append(abs(p - n - o) / abs(o))
        if errs_a:
            return _median(errs_b) < _median(errs_a)
        f = cd.fact("nonoperating_income", years[-1]) if years else None
        if f is None or f.tag != "NonoperatingIncomeExpense":
            return False
        i = abs(g("interest_expense", years[-1]) or 0)
        return bool(i) and f.val <= -0.5 * i
    nonop_has_interest = nonop_includes_interest() if years else False
    if approx_all and any(g("operating_income", y) is not None for y in years):
        cd.flags.add("operating income not tagged in the latest year - EBIT = pretax income + interest - other "
                     "non-operating income, used for every year for consistency")
    # capital expenditure: a year without a capex tag gets the company's median capex / revenue from the years
    # that have one (asset-light companies change tags often: Veeva, ePlus), so cash tests aren't left blank
    raw_capex = {}
    for y in years:
        cp, cs = g("capex_ppe", y), g("capex_software", y)
        rv = 0.0 if no_rev else g("revenue", y)
        cx = None
        if cp is not None or cs is not None:
            cx = abs(cp or 0) + abs(cs or 0)
            # only software capex found while the company owns material PP&E: PP&E capex is missing -> unknown
            if cp is None and rv and rv > 0 and (g("ppe_net", y) or 0) > 0.05 * rv:
                cx = None
        raw_capex[y] = cx
    known_years = [y for y in years if raw_capex[y] is not None and not no_rev and g("revenue", y)]
    known = [raw_capex[y] / g("revenue", y) for y in known_years]
    # only when capex is known for at least 3 years including a recent one (else the estimate could be stale)
    capex_ratio = (_median(known) if len(known) >= 3 and years and max(known_years) >= years[-1] - 2 else None)
    estimated = []
    rows = []
    for y in years:
        rev = 0.0 if no_rev else g("revenue", y)
        gp = g("gross_profit", y)
        if gp is None and g("cost_of_revenue", y) is not None and rev is not None:
            gp = rev - g("cost_of_revenue", y)
        op = None if approx_all else g("operating_income", y)
        op_approx = False
        pre_v, pre_est = pretax(y)
        if op is None:
            if pre_v is not None:
                # pretax + interest - other non-operating income (if tagged); when the non-operating total already
                # contains the interest, adding interest back as well would count it twice
                interest = 0 if nonop_has_interest else abs(g("interest_expense", y) or 0)
                op = pre_v + interest - (g("nonoperating_income", y) or 0)
                op_approx = True
            else:
                op = g("operating_income", y)
        ni, ocf = g("net_income", y), g("ocf", y)
        capex = raw_capex[y]
        if capex is None and capex_ratio is not None and rev and ocf is not None:
            capex = capex_ratio * rev
            estimated.append(y)
        fcf = (ocf - capex) if (ocf is not None and capex is not None) else None
        pre, tx = pre_v, g("income_tax", y)
        t = cfg["default_tax_rate"]
        if pre and tx is not None and pre > 0:
            t = min(max(tx / pre, tax_lo), tax_hi)
        nopat = op * (1 - t) if op is not None else None
        ic_now, ic_prev = ic.get(y), ic.get(y - 1)
        ic_avg = _avg([ic_now, ic_prev]) if ic_now is not None else None
        roic, neg_ic = None, False
        if nopat is not None and ic_avg is not None:
            if ic_avg > 0.02 * (rev or 0) and ic_avg > 0:
                roic = nopat / ic_avg
            elif nopat > 0:
                roic, neg_ic = 1.0, True   # customer-funded / near-zero capital: cap at 100%
        if roic is not None:
            roic = min(roic, 1.0)
        cash_roic = None
        if fcf is not None and ic_avg is not None and ic_avg > 0.02 * (rev or 0) and ic_avg > 0:
            cash_roic = min(fcf / ic_avg, 1.0)
        elif fcf is not None and fcf > 0 and ic_avg is not None:
            cash_roic = 1.0
        roc_t = None
        if op is not None and tc.get(y) is not None:
            if tc[y] > 0 and tc[y] > 0.02 * (rev or 0):
                roc_t = min(op / tc[y], 2.0)
            else:
                roc_t = 2.0 if op > 0 else None
        da = g("da", y)
        ebitda = (op + abs(da)) if (op is not None and da is not None) else None
        gw, intang, assets = g("goodwill", y), g("intangibles", y), g("assets", y)
        rows.append({
            "fy": y, "fy_end": cd.label_end.get(y), "revenue": rev, "gross_profit": gp,
            "gross_margin": _ratio(gp, rev), "operating_income": op, "operating_margin": _ratio(op, rev),
            "sga": g("sga", y), "sga_ratio": _ratio(g("sga", y), rev), "da": da, "ebitda": ebitda,
            "ebitda_margin": _ratio(ebitda, rev),
            "net_income": ni, "ocf": ocf, "capex": capex, "fcf": fcf, "fcf_margin": _ratio(fcf, rev),
            "capex_to_ocf": _ratio(capex, ocf) if (ocf and ocf > 0) else None,
            "capex_to_da": _ratio(capex, abs(da)) if da else None,
            "sbc": g("sbc", y), "rnd": g("rnd", y), "acquisitions": g("acquisitions", y),
            "buybacks": g("buybacks", y), "dividends": g("dividends", y), "equity_issued": g("equity_issued", y),
            "interest_expense": g("interest_expense", y), "tax_rate_used": t,
            "nopat": nopat, "invested_capital": ic_now, "roic": roic, "cash_roic": cash_roic, "neg_ic": neg_ic,
            "tangible_capital": tc.get(y), "roc_tangible": roc_t,
            "operating_income_approximated": op_approx, "pretax_estimated": pre_est,
            "capex_estimated": y in estimated,
            "total_debt": total_debt(cd, y), "cash_and_sti": _cash(g, y) or 0,
            "equity": g("equity", y), "assets": assets, "goodwill": gw, "intangibles": intang,
            "debt_due_1y": g("debt_due_1y", y), "debt_due_2y": g("debt_due_2y", y),
        })
    if estimated:
        in_window = [y for y in estimated if y > years[-1] - int(cfg.get("lookback_years", 10))]
        if len(in_window) > 2:
            # too much of the 10-year window rests on the estimate: a human should look (hold)
            cd.flags.add(f"capex estimated for {len(in_window)} of the last 10 years (not tagged) at the company's "
                         f"median capex / revenue ({capex_ratio:.1%}) - check free cash flow by hand")
        else:
            cd.flags.add(f"capex not tagged for {len(estimated)} year(s) ({min(estimated)}-{max(estimated)}) - "
                         f"estimated at the company's median capex / revenue ({capex_ratio:.1%})")
    if rows and rows[-1]["pretax_estimated"] and any(not r["pretax_estimated"] for r in rows[:-1]):
        # the latest year lost its pretax / operating-income tags: net income can carry one-off gains (hold)
        cd.flags.add("pretax and operating income not tagged for the latest year - estimated from net income "
                     "(one-off gains or discontinued operations would inflate it)")
    elif any(r["pretax_estimated"] for r in rows):
        cd.flags.add("no pretax-income tag - pretax income = net income + income tax")
    return rows


def compute(cd, cfg, today=None, allow_no_revenue=False):
    """Returns ((metrics dict, per-year rows), None) or (None, reason).
    allow_no_revenue: drug developers / medtech (clinical-stage codes) are screened with revenue = 0 when no revenue
    tag exists even if they had a profitable year (e.g. an upfront licence payment under a company-specific tag)."""
    today = today or date.today()
    rev_s = cd.series.get("revenue") or {}
    if not (cd.series.get("revenue") or {}):
        # no revenue tag and nothing to derive it from: only a business with no sales yet (biotech, explorer) may
        # be screened as 'revenue = 0'; anything with a gross profit or an operating profit has sales we can't see
        gp_any = bool(cd.series.get("gross_profit"))
        op_pos = any(f.val > 0 for f in (cd.series.get("operating_income") or {}).values())
        if (gp_any or op_pos) and not allow_no_revenue:
            return None, ("revenue not found in standard XBRL tags (company-specific tag) - not screened; check "
                          "by hand (see Data_Gaps for candidate tags)")
        if gp_any or op_pos:
            cd.flags.add("revenue not found in standard tags - screened as a pre-revenue company (check by hand)")
    all_rows = _year_rows(cd, cfg)
    if not all_rows:
        if not rev_s:
            return None, "no annual revenue or operating results found in XBRL (standard tags)"
        return None, "no years with both revenue and operating (or pretax) income"
    latest = max(r["fy"] for r in all_rows)
    L = int(cfg["lookback_years"])
    rows = [r for r in all_rows if latest - L < r["fy"] <= latest]
    if not rows:
        return None, "no recent years with both revenue and operating (or pretax) income"
    by_all = {r["fy"]: r for r in all_rows}
    by = {r["fy"]: r for r in rows}
    ys = [r["fy"] for r in rows]
    first3, last3 = ys[:3], ys[-3:]

    def col(k, yrs=ys):
        return [by_all[y][k] for y in yrs if y in by_all and by_all[y][k] is not None]

    m = {"currency": cd.currency, "latest_fy": latest, "latest_fy_end": cd.label_end.get(latest),
         "first_fy_in_window": ys[0], "years_with_data": len(ys), "years_total": len(all_rows),
         "first_fy_available": all_rows[0]["fy"]}
    m["no_revenue_tagged"] = not rev_s
    newest = max(cd.label_end)
    end = cd.label_end.get(newest)
    m["years_since_latest_fy"] = round((today - _d(end)).days / 365.25, 2) if end else None
    if newest > latest:
        cd.flags.add(f"FY{newest} reported but its revenue/operating income isn't in standard tags (non-standard tag?)")

    # ---------- size
    lr = by[ys[-1]]
    m["latest_revenue"] = lr["revenue"]
    fx = (cfg.get("fx_to_usd") or {}).get(cd.currency)
    m["fx_static"] = fx
    m["latest_revenue_usd"] = m["latest_revenue"] * fx if (fx and m["latest_revenue"] is not None) else None

    # ---------- core gates (10-year window)
    m["operating_loss_years"] = sum(1 for r in rows if r["operating_income"] is not None and r["operating_income"] <= 0)
    m["operating_loss_years_5y"] = sum(1 for r in rows[-5:] if r["operating_income"] is not None and r["operating_income"] <= 0)
    roics = col("roic")
    m["roic_years"] = len(roics)
    m["roic_median"] = _median(roics)
    floor = cfg["gates"]["roic_floor"]
    m["roic_share_above_floor"] = (sum(1 for x in roics if x >= floor) / len(roics)) if roics else None
    span = ys[-1] - ys[0]
    m["revenue_cagr"] = _cagr(by[ys[0]]["revenue"], lr["revenue"], span) if span >= 5 else None
    pairs = [(r["fcf"], r["net_income"]) for r in rows if r["fcf"] is not None and r["net_income"] is not None]
    if len(pairs) >= 5:
        s_ni = sum(p[1] for p in pairs)
        m["fcf_conversion"] = (sum(p[0] for p in pairs) / s_ni) if s_ni > 0 else None
    else:
        m["fcf_conversion"] = None
    m["fcf_conversion_years"] = len(pairs)
    m["capex_found"] = any(r["capex"] is not None for r in rows)
    ocf_ni = [(r["ocf"], r["net_income"]) for r in rows if r["ocf"] is not None and r["net_income"] is not None]
    s_ni2 = sum(p[1] for p in ocf_ni)
    m["ocf_conversion"] = (sum(p[0] for p in ocf_ni) / s_ni2) if (len(ocf_ni) >= 5 and s_ni2 > 0) else None
    debt_latest = lr["total_debt"]
    m["debt_found"] = debt_latest is not None
    nd = (debt_latest or 0) - lr["cash_and_sti"]
    m["net_debt"] = nd
    ocf3 = _avg(col("ocf", last3))
    m["ocf_avg_3y"] = ocf3
    m["net_debt_to_ocf"] = (nd / ocf3) if (ocf3 and ocf3 > 0) else None

    # ---------- predictability
    growth = []
    for a, b in zip(ys, ys[1:]):
        ra, rb = by[a]["revenue"], by[b]["revenue"]
        if b == a + 1 and ra and rb and ra > 0:
            growth.append(rb / ra - 1)
    m["revenue_growth_std"] = statistics.pstdev(growth) if len(growth) >= 4 else None
    m["revenue_decline_years"] = sum(1 for x in growth if x < 0) if growth else None
    oms = col("operating_margin")
    m["operating_margin_std"] = statistics.pstdev(oms) if len(oms) >= 4 else None

    # ---------- pricing power
    gms = col("gross_margin")
    m["gross_margin_median"] = statistics.median(gms) if len(gms) >= 4 else None
    m["gross_margin_std"] = statistics.pstdev(gms) if len(gms) >= 4 else None
    m["operating_margin_median"] = _median(oms)
    m["gross_margin_latest"] = lr["gross_margin"]
    m["operating_margin_latest"] = lr["operating_margin"]

    def chg(k, a=2021, b=2023):
        if a in by_all and b in by_all and by_all[a][k] is not None and by_all[b][k] is not None:
            return by_all[b][k] - by_all[a][k]
        return None
    m["gross_margin_change_2021_2023"] = chg("gross_margin")
    m["operating_margin_change_2021_2023"] = chg("operating_margin")
    m["operating_margin_trend"] = (_avg(col("operating_margin", last3)) - _avg(col("operating_margin", first3))
                                   if len(ys) >= 6 and col("operating_margin", last3) and col("operating_margin", first3) else None)

    # ---------- returns & moat direction
    r_first, r_last = col("roic", first3), col("roic", last3)
    m["roic_trend"] = (_avg(r_last) - _avg(r_first)) if (len(ys) >= 6 and r_first and r_last) else None
    n_f, n_l = _avg(col("nopat", first3)), _avg(col("nopat", last3))
    ic_f, ic_l = _avg(col("invested_capital", first3)), _avg(col("invested_capital", last3))
    m["incremental_roic"] = ((n_l - n_f) / (ic_l - ic_f)
                             if None not in (n_f, n_l, ic_f, ic_l) and (ic_l - ic_f) > 0 and len(ys) >= 6 else None)
    if m["incremental_roic"] is not None:
        m["incremental_roic"] = max(min(m["incremental_roic"], 2.0), -1.0)
    m["cash_roic_median"] = _median(col("cash_roic"))
    m["roc_tangible_median"] = _median(col("roc_tangible"))
    m["roc_tangible_latest"] = lr["roc_tangible"]
    # reinvestment rate: share of operating cash flow reinvested (capex + acquisitions), last 5 years
    l5 = ys[-5:]
    s_ocf5 = sum(col("ocf", l5))
    s_reinv5 = sum(col("capex", l5)) + sum(abs(x) for x in col("acquisitions", l5))
    m["reinvestment_rate"] = (s_reinv5 / s_ocf5) if s_ocf5 > 0 and col("capex", l5) else None

    # ---------- growth & runway
    mid_span = (_avg(last3) - _avg(first3)) if len(ys) >= 6 else 0
    m["nopat_cagr"] = _cagr(n_f, n_l, mid_span) if mid_span else None
    f_f, f_l = _avg(col("fcf", first3)), _avg(col("fcf", last3))
    fcf_cagr = _cagr(f_f, f_l, mid_span) if mid_span else None
    m["fcf_cagr"] = fcf_cagr

    def cagr_n(k, n):
        yb = latest - n
        if yb in by_all and by_all[yb][k] is not None and lr[k] is not None:
            return _cagr(by_all[yb][k], lr[k], n)
        return None
    m["revenue_cagr_3y"] = cagr_n("revenue", 3)
    m["revenue_cagr_5y"] = cagr_n("revenue", 5)
    m["ebitda_cagr_3y"] = cagr_n("ebitda", 3)
    m["operating_income_cagr_3y"] = cagr_n("operating_income", 3)
    prev = by_all.get(latest - 1)
    m["revenue_growth_latest_fy"] = (_ratio(lr["revenue"], prev["revenue"]) - 1
                                     if prev and prev["revenue"] and prev["revenue"] > 0 and lr["revenue"] is not None else None)
    p3 = by_all.get(latest - 3)
    m["operating_margin_change_3y"] = (lr["operating_margin"] - p3["operating_margin"]
                                       if p3 and lr["operating_margin"] is not None and p3["operating_margin"] is not None else None)
    m["ebitda_margin_change_3y"] = (lr["ebitda_margin"] - p3["ebitda_margin"]
                                    if p3 and lr["ebitda_margin"] is not None and p3["ebitda_margin"] is not None else None)
    m["sga_ratio_change_3y"] = (lr["sga_ratio"] - p3["sga_ratio"]
                                if p3 and lr["sga_ratio"] is not None and p3["sga_ratio"] is not None else None)
    m["revenue_growth_2y"] = (_ratio(lr["revenue"], by_all[latest - 2]["revenue"]) - 1
                              if (latest - 2) in by_all and by_all[latest - 2]["revenue"] and by_all[latest - 2]["revenue"] > 0
                              and lr["revenue"] is not None else None)

    # ---------- capital allocation
    ratios = cd.share_ratios

    def share_cagr(n):
        yrs = [y for y in range(latest - n + 1, latest + 1) if y in ratios]
        if len(yrs) >= min(3, n):
            prod = 1.0
            for y in yrs:
                prod *= ratios[y]["ratio"]
            return prod ** (1.0 / len(yrs)) - 1, len(yrs)
        return None, len(yrs)
    m["share_count_cagr"], m["share_count_years"] = share_cagr(5)
    m["share_count_cagr_3y"], _ = share_cagr(3)
    m["share_count_change_latest"] = (ratios[latest]["ratio"] - 1) if latest in ratios else None
    m["fcf_per_share_cagr"] = (((1 + fcf_cagr) / (1 + m["share_count_cagr"])) - 1
                               if fcf_cagr is not None and m["share_count_cagr"] is not None else None)
    s_ocf = sum(col("ocf"))
    s_acq = sum(abs(x) for x in col("acquisitions"))
    m["acquisitions_to_ocf"] = (s_acq / s_ocf) if s_ocf > 0 else None
    m["acquisitions_tagged"] = bool(col("acquisitions"))
    sbc3 = [(by[y]["sbc"], by[y]["revenue"]) for y in last3 if by[y]["sbc"] is not None and by[y]["revenue"]]
    m["sbc_to_revenue"] = (sum(a for a, _ in sbc3) / sum(b for _, b in sbc3)) if (sbc3 and sum(b for _, b in sbc3) > 0) else 0.0
    m["goodwill_to_assets"] = _ratio(lr["goodwill"] or 0, lr["assets"]) if lr["assets"] else None
    m["latest_equity_negative"] = lr["equity"] is not None and lr["equity"] < 0
    s_fcf = sum(col("fcf"))
    s_ret = sum(abs(x) for x in col("buybacks")) + sum(abs(x) for x in col("dividends"))
    m["shareholder_returns_to_fcf"] = (s_ret / s_fcf) if s_fcf > 0 else None
    rnd3 = [(by[y]["rnd"], by[y]["revenue"]) for y in last3 if by[y]["rnd"] is not None and by[y]["revenue"]]
    m["rnd_to_revenue"] = (sum(a for a, _ in rnd3) / sum(b for _, b in rnd3)) if (rnd3 and sum(b for _, b in rnd3) > 0) else None
    m["fcf_margin_latest3"] = _ratio(sum(col("fcf", last3)), sum(col("revenue", last3))) if col("fcf", last3) else None
    m["any_negative_ic_year"] = any(r["neg_ic"] for r in rows)
    m["op_income_approx_years"] = sum(1 for r in rows if r["operating_income_approximated"])
    m["restated_years"] = cd.restated("revenue", ys, cfg["flags"]["restatement_tolerance"]) + \
        cd.restated("operating_income", ys, cfg["flags"]["restatement_tolerance"])
    # per-share growth bought with debt: share count falling while net debt rises (5 years)
    y5 = latest - 5
    if y5 in by_all and m["share_count_cagr"] is not None:
        nd5 = (by_all[y5]["total_debt"] or 0) - by_all[y5]["cash_and_sti"]
        m["net_debt_change_5y"] = nd - nd5
        m["buybacks_debt_funded"] = bool(m["share_count_cagr"] < -0.01 and nd - nd5 > 0
                                         and (ocf3 or 0) > 0 and (nd - nd5) > 1.0 * ocf3)
    else:
        m["net_debt_change_5y"], m["buybacks_debt_funded"] = None, None

    # ---------- resilience (Fortress)
    m["fcf_positive_years"] = sum(1 for r in rows if r["fcf"] is not None and r["fcf"] > 0)
    m["fcf_years"] = sum(1 for r in rows if r["fcf"] is not None)
    for key, (lo, hi) in RECESSIONS.items():
        rev_chg, op_chg, n = None, None, 0
        in_window = [r for r in all_rows if r["fy_end"] and lo <= r["fy_end"][:10] <= hi]
        m[f"recession_{key}_years_in_window"] = len(in_window)
        ops = [r["operating_income"] for r in in_window if r["operating_income"] is not None]
        m[f"recession_{key}_min_op_income"] = min(ops) if ops else None
        for r in in_window:
            if True:
                p = by_all.get(r["fy"] - 1)
                if not p:
                    continue
                n += 1
                if p["revenue"] and p["revenue"] > 0 and r["revenue"] is not None:
                    c = r["revenue"] / p["revenue"] - 1
                    rev_chg = c if rev_chg is None else min(rev_chg, c)
                if p["operating_income"] is not None and r["operating_income"] is not None:
                    if p["operating_income"] > 0:
                        c = r["operating_income"] / p["operating_income"] - 1
                    else:
                        c = 0.0 if r["operating_income"] >= p["operating_income"] else -1.0
                    op_chg = c if op_chg is None else min(op_chg, c)
        m[f"recession_{key}_revenue_change"] = rev_chg
        m[f"recession_{key}_op_income_change"] = op_chg
        # fallback when revenue / operating income aren't in XBRL for the year before: net income
        ni_s = cd.series.get("net_income") or {}
        ni_chg, ni_loss = None, False
        for lab, end in cd.label_end.items():
            if lo <= end[:10] <= hi and lab in ni_s:
                if ni_s[lab].val < 0:
                    ni_loss = True
                p = ni_s.get(lab - 1)
                if p is not None and p.val > 0:
                    c = ni_s[lab].val / p.val - 1
                    ni_chg = c if ni_chg is None else min(ni_chg, c)
        m[f"recession_{key}_ni_change"] = ni_chg
        m[f"recession_{key}_ni_loss"] = ni_loss

    # ---------- downturns (Core): an operating loss in a downturn fiscal year while sales fell vs the year before.
    # Only downturns inside the company's SEC data are tested (verifiable); a one-off charge in a year when sales
    # still grew (Mastercard's 2008 settlement) doesn't count.
    ni_s = cd.series.get("net_income") or {}
    failed, tested, unjudged = [], [], []
    for key, (lo, hi) in DOWNTURNS.items():
        yrs = sorted(lab for lab, end in cd.label_end.items() if lo <= end[:10] <= hi)
        judged = False
        for lab in yrs:
            r, p = by_all.get(lab), by_all.get(lab - 1)
            op = r["operating_income"] if r else None
            loss = (op < 0) if op is not None else (lab in ni_s and ni_s[lab].val < 0)
            rev, prev = (r["revenue"] if r else None), (p["revenue"] if p else None)
            if op is None and lab not in ni_s:
                continue
            if rev is None or prev is None or prev <= 0:
                if loss:
                    unjudged.append(f"FY{lab}")
                continue
            judged = True
            if loss and rev < prev:
                failed.append(f"FY{lab} ({key}): operating loss as sales fell {rev / prev - 1:+.0%}")
        if judged:
            tested.append(key)
    m["downturn_failures"] = failed
    m["downturns_tested"] = tested
    m["downturn_unjudged"] = unjudged

    # ---------- cycle position (Cyclicals) and over-earning
    oms_all = col("operating_margin")
    m["op_margin_percentile_10y"] = _pctile_of_last(oms_all)
    med = m["operating_margin_median"]
    m["op_margin_vs_median"] = (lr["operating_margin"] / med) if (med and med > 0 and lr["operating_margin"] is not None) else None
    m["op_margin_minus_median"] = ((lr["operating_margin"] - med) if (med is not None and lr["operating_margin"]
                                                                      is not None) else None)
    # margins far above the company's own history right after a revenue surge (also catches short histories
    # with losses in the median, e.g. a memory maker at a boom peak)
    m["over_earning"] = bool(m["op_margin_vs_median"] is not None and m["op_margin_vs_median"] > 1.5
                             and (m["revenue_growth_2y"] or 0) > 0.5)
    # a history of losses gives no meaningful median: flag only very high margins (>= 30%) after a surge here;
    # the cyclical-industry condition is applied in the pipeline (a growth company turning profitable is not a peak)
    m["over_earning_short_history"] = bool(not m["over_earning"] and lr["operating_margin"] is not None
                                           and lr["operating_margin"] >= 0.30 and (med is None or med <= 0)
                                           and (m["revenue_growth_2y"] or 0) > 0.5)
    ebits = col("operating_income")
    m["normalized_ebit"] = _avg(ebits) if len(ebits) >= 5 else None
    ebitdas = col("ebitda")
    m["normalized_ebitda"] = _avg(ebitdas) if len(ebitdas) >= 5 else None
    m["positive_ebit_years"] = sum(1 for x in ebits if x > 0)
    m["capex_to_da_latest"] = lr["capex_to_da"]
    m["capex_to_da_3y"] = _ratio(sum(col("capex", last3)), sum(abs(x) for x in col("da", last3))) if col("da", last3) else None
    m["capex_to_ocf_3y"] = _ratio(sum(col("capex", last3)), sum(col("ocf", last3))) if sum(col("ocf", last3)) > 0 else None

    # ---------- trailing twelve months and the latest balance sheet
    def ttm(c):
        p = cd.ttm(c)
        return p.val if p else None
    t_rev, t_op_p = cd.ttm("revenue"), cd.ttm("operating_income")
    m["ttm_end"] = t_rev.end if t_rev else None
    m["ttm_method"] = t_rev.method if t_rev else None
    m["ttm_revenue"] = t_rev.val if t_rev else None
    t_op = t_op_p.val if t_op_p else None
    if lr["operating_income_approximated"] or t_op is None:
        t_pre = ttm("pretax_income")
        if t_pre is None and ttm("net_income") is not None and lr.get("pretax_estimated"):
            t_pre = ttm("net_income") + (ttm("income_tax") or 0)
        if t_pre is not None:
            t_op = t_pre + abs(ttm("interest_expense") or 0) - (ttm("nonoperating_income") or 0)
    m["ttm_operating_income"] = t_op
    t_da = ttm("da")
    m["ttm_da"] = t_da
    m["ttm_ebitda"] = (t_op + abs(t_da)) if (t_op is not None and t_da is not None) else None
    m["ttm_net_income"] = ttm("net_income")
    m["ttm_ocf"] = ttm("ocf")
    cp, cs = ttm("capex_ppe"), ttm("capex_software")
    m["ttm_capex"] = (abs(cp or 0) + abs(cs or 0)) if (cp is not None or cs is not None) else None
    m["ttm_fcf"] = (m["ttm_ocf"] - m["ttm_capex"]) if (m["ttm_ocf"] is not None and m["ttm_capex"] is not None) else None
    gp_t = ttm("gross_profit")
    if gp_t is None and ttm("cost_of_revenue") is not None and m["ttm_revenue"] is not None:
        gp_t = m["ttm_revenue"] - ttm("cost_of_revenue")
    m["ttm_gross_profit"] = gp_t
    m["ttm_interest_expense"] = ttm("interest_expense")
    m["ttm_interest_paid"] = ttm("interest_paid")
    m["ytd_revenue_growth"] = None
    if t_rev and t_rev.extra.get("ytd_prior"):
        m["ytd_revenue_growth"] = t_rev.extra["ytd_current"] / t_rev.extra["ytd_prior"] - 1
        m["ytd_days"] = t_rev.extra.get("ytd_days")
    m["ttm_revenue_growth_vs_fy"] = (m["ttm_revenue"] / lr["revenue"] - 1
                                     if m["ttm_revenue"] and lr["revenue"] and lr["revenue"] > 0 else None)
    m["ttm_operating_margin"] = _ratio(t_op, m["ttm_revenue"])
    m["ttm_ebitda_margin"] = _ratio(m["ttm_ebitda"], m["ttm_revenue"])
    m["ttm_gross_margin"] = _ratio(gp_t, m["ttm_revenue"])

    bs_date = cd.latest_bs_date()
    m["bs_date"] = bs_date
    if bs_date and m["ttm_end"] and (_d(bs_date) - _d(m["ttm_end"])).days > 450:
        cd.flags.add(f"income and cash-flow figures (to {m['ttm_end']}) are much older than the balance sheet "
                     f"({bs_date}) - non-standard tag in recent filings?")

    def bs(c):
        if bs_date is None:
            return None
        p = cd.bs_at(c, bs_date)
        return p.val if p else None
    cash_l = _cash(lambda c, _y=None: bs(c)) if bs_date else None
    m["bs_cash_and_sti"] = cash_l
    m["bs_lt_investments"] = bs("lt_investments")
    m["bs_debt"] = total_debt(cd, at=bs_date) if bs_date else None
    m["bs_debt_source"] = "latest balance sheet"
    if m["bs_debt"] is None and debt_latest is not None:
        # the annual report tags debt but the latest 10-Q doesn't (custom tag): use the annual figure
        m["bs_debt"], m["bs_debt_source"] = debt_latest, f"FY{latest} annual report (not tagged at {bs_date})"
    m["bs_debt_found"] = m["bs_debt"] is not None
    if cash_l is None:
        cash_l = 0.0
    m["bs_minority_interest"] = bs("minority_interest")
    m["bs_preferred"] = bs("preferred_equity")
    m["bs_equity"] = bs("equity")
    m["bs_assets"] = bs("assets")
    m["bs_net_debt"] = ((m["bs_debt"] or 0) - cash_l) if (bs_date and m["bs_cash_and_sti"] is not None) else None
    ebitda_basis = m["ttm_ebitda"] if m["ttm_ebitda"] is not None else lr["ebitda"]
    m["net_debt_to_ebitda"] = (m["bs_net_debt"] / ebitda_basis) if (ebitda_basis and ebitda_basis > 0 and
                                                                    m["bs_net_debt"] is not None) else None
    ie = abs(m["ttm_interest_expense"]) if m["ttm_interest_expense"] is not None else None
    if ie is None and m["ttm_interest_paid"] is not None:
        ie = abs(m["ttm_interest_paid"])
    if t_op is not None:
        if ie is not None and ie > 0:
            m["interest_coverage"] = t_op / ie
        elif (m["bs_debt"] or 0) <= 0.05 * (m["ttm_revenue"] or 1):
            m["interest_coverage"] = 99.0  # essentially no debt
        elif m["bs_debt"] and t_op > 0:
            # interest not tagged (e.g. Apple folds it into 'other income'): assume a punitive 10% rate on all
            # tagged debt - a floor for the true coverage, so a pass here is a safe pass
            m["interest_coverage"] = t_op / (0.10 * m["bs_debt"])
            m["interest_coverage_estimated"] = True
        else:
            m["interest_coverage"] = None
    else:
        m["interest_coverage"] = None
    # ---------- data-quality holds on debt (phrases are matched by screens.HOLD_FLAG_MARKERS)
    rev_t = m["ttm_revenue"] or lr["revenue"] or 0
    assets_t = m.get("bs_assets") or lr["assets"] or 0
    # the interest bill implies debt of about interest / 8%
    ie_tag = (cd.ttm("interest_expense").tag if cd.ttm("interest_expense") else "") or ""
    if ie and ie >= 5e6 and not m["bs_debt_found"]:
        # no debt tag at all: any material interest bill is suspicious
        if (rev_t > 0 and ie > 0.005 * rev_t) or (assets_t and ie / 0.08 > 0.05 * assets_t):
            cd.flags.add("debt not found in standard tags but interest expense is material - debt may be missed")
    elif ie and ie >= 5e6 and m["bs_debt"] and ie / m["bs_debt"] > 0.15:
        # some debt found: flag only if the debt NOT found is material (implied missing debt > 5% of total assets);
        # IFRS 'finance costs' include FX and other charges, so they are not used here
        missing = ie / 0.08 - m["bs_debt"]
        if assets_t and missing > 0.05 * assets_t and ie_tag != "FinanceCosts":
            cd.flags.add(f"interest is {ie / m['bs_debt']:.0%} of tagged debt - debt partly missed?")
    lsc = bs("liabilities_subject_to_compromise")
    reorg = ttm("reorganization_items")
    m["in_chapter_11"] = bool(lsc and lsc > 0)
    m["reorganization_items_ttm"] = reorg
    if m["in_chapter_11"]:
        cd.flags.add("liabilities subject to compromise / reorganization items: company may still be in Chapter 11")
    if lr["operating_income_approximated"] and all(r["operating_income_approximated"] for r in rows):
        # the company never shows an operating-income line (JNJ, LLY, ADP, Nucor...): EBIT = pretax income +
        # interest expense in every year - the standard definition, consistent across the window
        cd.flags.add("no operating-income line in the filings - EBIT = pretax income + interest expense (all years)")
    d1 = lr["debt_due_1y"]
    d2 = lr["debt_due_2y"]
    m["debt_due_2y_total"] = _sum_or_none(d1, d2)
    fcf_basis = m["ttm_fcf"] if m["ttm_fcf"] is not None else lr["fcf"]
    if m["debt_due_2y_total"] is not None:
        m["maturities_covered"] = (cash_l + max(fcf_basis or 0, 0) * 2) >= m["debt_due_2y_total"]
    elif (m["bs_debt"] or 0) <= 0.05 * (m["ttm_revenue"] or 1) or (m["bs_net_debt"] is not None and m["bs_net_debt"] <= 0):
        m["maturities_covered"] = True
    elif m["bs_debt"] and (cash_l + max(fcf_basis or 0, 0) * 2) >= m["bs_debt"]:
        m["maturities_covered"] = True   # no schedule tagged, but cash + 2 years of FCF cover ALL the debt
    else:
        m["maturities_covered"] = None

    # ---------- small-cap quality (Haley): gross profit / tangible assets
    tang = None
    if lr["assets"] is not None:
        tang = lr["assets"] - (lr["goodwill"] or 0) - (lr["intangibles"] or 0)
    m["gp_to_tangible_assets"] = _ratio(lr["gross_profit"], tang) if tang and tang > 0 else None

    # ---------- biotech survival
    burn = -m["ttm_ocf"] if (m["ttm_ocf"] is not None and m["ttm_ocf"] < 0) else 0.0
    m["annual_cash_burn"] = burn if m["ttm_ocf"] is not None else None
    liquid = (m["bs_cash_and_sti"] or 0) + (m["bs_lt_investments"] or 0)
    m["liquid_assets"] = liquid if (bs_date and m["bs_cash_and_sti"] is not None) else None
    if m["ttm_ocf"] is None:
        m["cash_runway_years"] = None
    elif burn <= 0:
        m["cash_runway_years"] = 99.0
    else:
        m["cash_runway_years"] = liquid / burn

    # ---------- hard floors (Watsa): net cash and tangible book at the latest balance sheet
    m["net_cash"] = None
    if m["liquid_assets"] is not None:
        m["net_cash"] = m["liquid_assets"] - (m["bs_debt"] or 0) - (m["bs_preferred"] or 0) - \
            (m["bs_minority_interest"] or 0)
    m["tangible_book"] = None
    if m["bs_equity"] is not None:
        # a 10-Q that doesn't tag goodwill / intangibles: use the latest annual figure rather than zero
        gw_b = bs("goodwill")
        gw_b = gw_b if gw_b is not None else (lr["goodwill"] or 0)
        in_b = bs("intangibles")
        in_b = in_b if in_b is not None else (lr["intangibles"] or 0)
        eq_pt = cd.bs_at("equity", bs_date)
        nci = (m["bs_minority_interest"] or 0) if (eq_pt is not None and eq_pt.tag in (
            "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest", "Equity")) else 0
        m["tangible_book"] = m["bs_equity"] - nci - gw_b - in_b - (m["bs_preferred"] or 0)

    # ---------- inputs for the screens from the second batch of interviews
    # (Owner-Operators, Hard Assets & Royalties, Asset-Floor Value, Trough Cyclical Cash, Hidden Earnings, Red Flags)
    fcf5 = col("fcf", l5)
    m["fcf_avg_5y"] = _avg(fcf5) if len(fcf5) >= 4 else None          # cycle-average free cash flow (Einhorn)
    cap5 = col("capex", l5)
    ret5 = sum(abs(x) for x in col("buybacks", l5)) + sum(abs(x) for x in col("dividends", l5))
    m["returns_to_capex_5y"] = (ret5 / sum(cap5)) if (cap5 and sum(cap5) > 0) else None
    ebits_all = col("operating_income")
    m["positive_ebit_share"] = (sum(1 for x in ebits_all if x > 0) / len(ebits_all)) if len(ebits_all) >= 3 else None
    # gross margin falling three years in a row (Nadella: AI adds a real marginal cost to software)
    l4 = [y for y in range(latest - 3, latest + 1)]
    gm4 = [by_all[y]["gross_margin"] if y in by_all else None for y in l4]
    if None not in gm4:
        m["gross_margin_change_3y"] = gm4[-1] - gm4[0]
        m["gross_margin_down_3y"] = all(b < a for a, b in zip(gm4, gm4[1:])) and gm4[-1] - gm4[0] <= -0.02
    else:
        m["gross_margin_change_3y"], m["gross_margin_down_3y"] = None, None
    # discontinued operations in the last three fiscal years or the latest twelve months (a unit sold or spun off)
    m["disc_ops_material"], m["disc_ops_note"] = False, None
    floor_share = float(cfg.get("disc_ops_min_share_of_revenue", 0.01))
    dsc = cd.series.get("disc_ops") or {}
    dsr = cd.series.get("disc_ops_revenue") or {}
    found = []
    for y in range(latest - 2, latest + 1):
        rev_y = (by_all.get(y) or {}).get("revenue")
        for s_, what in ((dsc, "income"), (dsr, "revenue")):
            f = s_.get(y)
            if f is not None and f.val and rev_y and abs(f.val) >= floor_share * abs(rev_y):
                found.append(f"FY{y} discontinued-operations {what} {f.val / 1e6:,.0f}M")
                break
    # 10-Q year-to-date figures after the latest fiscal year (a spin-off or sale happening now)
    fy_end_latest = cd.label_end.get(latest) or ""
    rev_ref = abs(lr["revenue"] or 0)
    for concept, what in (("disc_ops", "income"), ("disc_ops_revenue", "revenue")):
        best = None
        for tax, tag in cd._tags(concept):
            for (qs_, qe), e in (cd._q_durations(tax, tag, "money") or {}).items():
                try:
                    val = float(e["val"])
                except (TypeError, ValueError, KeyError):
                    continue
                if qe <= fy_end_latest or not val or qs_ < fy_end_latest:
                    continue
                dur = (_d(qe) - _d(qs_)).days
                if best is None or (qe, dur) > (best[0], best[1]):
                    best = (qe, dur, val)
        if best and rev_ref:
            qe, days, val = best
            days = max(days, 1)
            if abs(val) >= floor_share * rev_ref * days / 365.0:
                found.append(f"discontinued-operations {what} {val / 1e6:,.0f}M in the {days // 30} months to {qe}")
                break
    if found:
        m["disc_ops_material"] = True
        m["disc_ops_note"] = "; ".join(found[:2])

    # ---------- shares for market cap
    dei = cd.dei_latest("EntityCommonStockSharesOutstanding")
    m["dei_shares"] = dei["val"] if dei else None
    m["dei_shares_date"] = dei["end"] if dei else None
    ds = cd.latest_diluted_shares()
    m["diluted_shares_latest"] = ds.val if ds else None
    m["diluted_shares_date"] = ds.end if ds else None
    m["diluted_shares_filed"] = (ds.extra.get("filed") or None) if ds else None
    fl = cd.dei_latest("EntityPublicFloat")
    m["public_float"] = fl["val"] if fl and fl["unit"] == "USD" else None
    m["public_float_date"] = fl["end"] if fl else None
    # share count around the float date, so insider share isn't distorted by shares issued or bought back since
    near = cd.dei_shares_near(m["public_float_date"]) if m["public_float_date"] else None
    m["dei_shares_near_float"] = near["val"] if near else None
    m["dei_shares_near_float_date"] = near["end"] if near else None
    # share count implied by the income statement (multi-class companies often tag share counts only per class)
    eps, ni_fy = cd.get("eps_diluted", latest), lr["net_income"]
    m["eps_shares"] = (ni_fy / eps) if (eps and ni_fy and eps > 0.01 and ni_fy > 0) else None
    m["eps_shares_date"] = cd.label_end.get(latest) if m["eps_shares"] else None
    _ef = cd.fact("eps_diluted", latest)
    m["eps_shares_filed"] = ((_ef.filed or "")[:10] or None) if (_ef is not None and m["eps_shares"]) else None

    # ---------- quality warnings (Core / Fortress / Healthcare / Emerging only - a trough is the point in Cyclicals)
    med_om, t_om = m["operating_margin_median"], m["ttm_operating_margin"]
    m["gross_profit_reported"] = bool(cd.series.get("gross_profit") or cd.series.get("cost_of_revenue"))
    m["margin_collapse"] = bool(med_om is not None and med_om > 0.05 and t_om is not None and t_om < 0.5 * med_om)
    m["lost_money_2009"] = bool((m.get("recession_2009_min_op_income") is not None
                                 and m["recession_2009_min_op_income"] < 0) or m.get("recession_2009_ni_loss"))
    m["revenue_shrinking"] = bool(m.get("revenue_cagr_3y") is not None and m["revenue_cagr_3y"] < -0.02)
    return (m, all_rows), None


# ---------------------------------------------------------------- statement model (Excel) and price history
# raw tagged lines kept per fiscal year for the 3-statement model; derived lines come from _year_rows
MODEL_RAW = ("revenue", "cost_of_revenue", "gross_profit", "selling_marketing", "general_admin", "sga", "rnd",
             "da", "sbc", "interest_expense", "interest_income", "nonoperating_income", "pretax_income",
             "income_tax", "net_income", "eps_diluted", "diluted_shares", "basic_shares",
             "cash", "st_investments", "accounts_receivable", "inventory", "assets_current", "ppe_net", "goodwill",
             "intangibles", "lt_investments", "assets", "accounts_payable", "accrued_liabilities",
             "deferred_revenue_current", "liabilities_current", "deferred_revenue_noncurrent", "liabilities",
             "minority_interest", "preferred_equity", "equity", "retained_earnings", "liabilities_and_equity",
             "ocf", "capex_ppe", "capex_software", "acquisitions", "cfi", "debt_issued", "debt_repaid",
             "buybacks", "dividends", "equity_issued", "cff", "fx_effect")
MODEL_DERIVED = ("operating_income", "ebitda", "capex", "fcf", "total_debt", "cash_and_sti", "nopat",
                 "invested_capital", "roic", "cash_roic", "tax_rate_used")


def model_years(cd, rows, n=10):
    """Per fiscal year (last n with revenue and operating results): the statement lines for the Excel model and
    the inputs for historical multiples. 'shares_basis' = diluted shares restated to the latest year's basis with
    the split-proof within-filing ratios, so it can be multiplied by a split-adjusted price of that year."""
    rows = rows[-n:]
    if not rows:
        return None
    latest = rows[-1]["fy"]
    basis = {}
    s_last = cd.get("diluted_shares", latest)
    if s_last:
        basis[latest] = s_last
        for y in range(latest, rows[0]["fy"], -1):
            if y not in basis:
                break
            r = cd.share_ratios.get(y)
            if r and r.get("ratio"):
                basis[y - 1] = basis[y] / r["ratio"]
            else:
                a, b = cd.get("diluted_shares", y), cd.get("diluted_shares", y - 1)
                if a and b:
                    basis[y - 1] = basis[y] * b / a
    years = []
    for r in rows:
        y = r["fy"]
        d = {"fy": y, "end": cd.label_end.get(y)}
        for k in MODEL_RAW:
            v = cd.get(k, y)
            if v is not None:
                d[k] = v
        for k in MODEL_DERIVED:
            if r.get(k) is not None:
                d["x_" + k] = r[k]
        if basis.get(y):
            d["shares_basis"] = basis[y]
        years.append(d)
    return {"currency": cd.currency, "years": years}


EVIDENCE_CONCEPTS = ["revenue", "gross_profit", "cost_of_revenue", "sga", "operating_income", "pretax_income",
                     "income_tax", "net_income", "ocf", "capex_ppe", "capex_software", "da", "interest_expense",
                     "interest_paid", "acquisitions", "buybacks", "dividends", "equity_issued", "sbc", "assets", "assets_current",
                     "liabilities_current", "ppe_net", "equity", "cash", "st_investments", "lt_investments",
                     "debt_combined", "lt_debt_incl_current", "lt_debt_noncurrent", "debt_current",
                     "lt_debt_current", "st_borrowings", "commercial_paper", "debt_due_1y", "debt_due_2y",
                     "goodwill", "intangibles"]
TTM_EVIDENCE = ["revenue", "gross_profit", "operating_income", "net_income", "ocf", "capex_ppe", "capex_software",
                "da", "interest_expense"]
BS_EVIDENCE = ["cash", "st_investments", "lt_investments", "debt_combined", "lt_debt_incl_current",
               "lt_debt_noncurrent", "debt_current", "lt_debt_current", "st_borrowings", "commercial_paper",
               "minority_interest", "preferred_equity", "equity", "assets"]


def evidence_rows(cd, years):
    out = []
    for c in EVIDENCE_CONCEPTS:
        for y in years:
            f = cd.fact(c, y)
            if f is not None:
                out.append(f.as_row())
    for y in years:
        r = cd.share_ratios.get(y)
        if r:
            out.append({"concept": "diluted_shares_yoy_ratio", "fy": y, "value": r["ratio"], "unit": "ratio",
                        "taxonomy": "us-gaap/ifrs", "tag": r["tag"] + " (same-filing ratio vs prior year)",
                        "period_start": None, "period_end": cd.label_end.get(y), "form": None, "filed": None,
                        "accession": r["accn"], "first_reported_value": None, "first_reported_accession": None})
    for c in TTM_EVIDENCE:
        p = cd.ttm(c)
        if p is not None and p.method != "FY":
            row = p.as_row()
            row["concept"] = c + " (TTM)"
            out.append(row)
    bd = cd.latest_bs_date()
    if bd:
        for c in BS_EVIDENCE:
            p = cd.bs_at(c, bd)
            if p is not None:
                row = p.as_row()
                row["concept"] = c + " (latest balance sheet)"
                out.append(row)
    for tag in ("EntityCommonStockSharesOutstanding", "EntityPublicFloat"):
        d = cd.dei_latest(tag)
        if d:
            out.append({"concept": tag, "fy": "cover page", "value": d["val"], "unit": d["unit"], "taxonomy": "dei",
                        "tag": tag, "period_start": None, "period_end": d["end"], "form": d["form"], "filed": None,
                        "accession": d["accn"], "first_reported_value": None, "first_reported_accession": None})
    return out


def post_event_dilution(cd, m, event_date, today=None):
    """Share-count growth measured only AFTER an IPO / spin-off. Before the listing, weighted share counts exclude
    the preferred stock that converts at the IPO, so the raw 3-year figure shows huge 'dilution' that never hit
    public shareholders. Uses annual ratios whose two fiscal years both end > 1 year after the event; otherwise
    cover-page share counts (first one after the event vs the latest, at least 9 months apart)."""
    ev = _d(event_date)
    latest = m.get("latest_fy")
    good = [y for y, r in cd.share_ratios.items()
            if latest - 3 < y <= latest and cd.label_end.get(y - 1) and (_d(cd.label_end[y - 1]) - ev).days > 365]
    if good:
        prod = 1.0
        for y in good:
            prod *= cd.share_ratios[y]["ratio"]
        return prod ** (1.0 / len(good)) - 1, f"{len(good)} post-listing fiscal year(s)"
    units = ((cd.facts.get("dei") or {}).get("EntityCommonStockSharesOutstanding") or {})
    by_filing = {}   # (end, accn) -> [filed, total across share classes]
    for unit, ents in units.items():
        for e in ents:
            end = (e.get("end") or "")[:10]
            if not end or e.get("val") is None or (_d(end) - ev).days < 30:
                continue
            k = by_filing.setdefault((end, e.get("accn")), [e.get("filed") or "", 0.0])
            k[1] += float(e["val"])
    pts = {}
    for (end, accn), (filed, v) in by_filing.items():   # per date keep the latest filing (amendments win)
        if end not in pts or filed > pts[end][0]:
            pts[end] = (filed, v)
    if len(pts) >= 2:
        e0, e1 = min(pts), max(pts)
        v0, v1 = pts[e0][1], pts[e1][1]
        yrs = (_d(e1) - _d(e0)).days / 365.25
        if yrs >= 0.75 and v0 > 0:
            return (v1 / v0) ** (1 / yrs) - 1, f"cover-page shares {e0} -> {e1}"
    return None, "less than one full fiscal year of share counts since the listing"
