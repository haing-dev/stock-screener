"""Published, simple scores the screens are compared with (validation/PROTOCOL.md sections 4-5). Each uses only the
filed annual statements (CompanyData as of the formation date), never prices, except the Magic Formula's earnings
yield, which is added at formation.

  piotroski  - F-score 0-9 (Piotroski 2000)
  gross_prof - gross profit / total assets (Novy-Marx 2013)
  magic_roc  - EBIT / tangible capital (Greenblatt), combined with EBIT / EV at formation
  altman_z2  - Altman Z'' for non-manufacturers (Altman 1995): lower = closer to distress
  beneish_m  - Beneish M-score (Beneish 1999): higher = likelier earnings manipulation
"""


def _ratio(a, b):
    if a is None or b in (None, 0):
        return None
    return a / b


def _two_years(cd):
    ys = sorted(cd.label_end)
    return (ys[-1], ys[-2]) if len(ys) >= 2 else (ys[-1] if ys else None, None)


def piotroski(cd):
    y, p = _two_years(cd)
    if y is None or p is None:
        return None
    g = cd.get
    ni, ni0 = g("net_income", y), g("net_income", p)
    ta, ta0 = g("assets", y), g("assets", p)
    cfo = g("ocf", y)
    if None in (ni, ta, cfo) or not ta:
        return None
    score = 0
    roa = ni / ta
    roa0 = _ratio(ni0, ta0)
    score += roa > 0
    score += cfo > 0
    score += roa0 is not None and roa > roa0
    score += cfo > ni
    ltd, ltd0 = g("lt_debt_noncurrent", y) or 0, g("lt_debt_noncurrent", p) or 0
    lev, lev0 = _ratio(ltd, ta), _ratio(ltd0, ta0)
    score += lev is not None and lev0 is not None and lev <= lev0
    cr, cr0 = _ratio(g("assets_current", y), g("liabilities_current", y)), _ratio(g("assets_current", p),
                                                                                  g("liabilities_current", p))
    score += cr is not None and cr0 is not None and cr > cr0
    sh, sh0 = g("diluted_shares", y), g("diluted_shares", p)
    score += sh is not None and sh0 is not None and sh <= sh0
    rev, rev0 = g("revenue", y), g("revenue", p)
    gp, gp0 = g("gross_profit", y), g("gross_profit", p)
    if gp is None and rev is not None and g("cost_of_revenue", y) is not None:
        gp = rev - g("cost_of_revenue", y)
    if gp0 is None and rev0 is not None and g("cost_of_revenue", p) is not None:
        gp0 = rev0 - g("cost_of_revenue", p)
    gm, gm0 = _ratio(gp, rev), _ratio(gp0, rev0)
    score += gm is not None and gm0 is not None and gm > gm0
    at, at0 = _ratio(rev, ta), _ratio(rev0, ta0)
    score += at is not None and at0 is not None and at > at0
    return int(score)


def gross_prof(cd):
    y, _p = _two_years(cd)
    if y is None:
        return None
    g = cd.get
    gp = g("gross_profit", y)
    if gp is None and g("revenue", y) is not None and g("cost_of_revenue", y) is not None:
        gp = g("revenue", y) - g("cost_of_revenue", y)
    return _ratio(gp, g("assets", y))


def altman_z2(cd):
    y, _p = _two_years(cd)
    if y is None:
        return None
    g = cd.get
    ta = g("assets", y)
    ca, cl = g("assets_current", y), g("liabilities_current", y)
    re_, ebit, eq, tl = g("retained_earnings", y), g("operating_income", y), g("equity", y), g("liabilities", y)
    if tl is None and ta is not None and eq is not None:
        tl = ta - eq
    if None in (ta, ca, cl, ebit, eq, tl) or not ta or not tl:
        return None
    return 6.56 * (ca - cl) / ta + 3.26 * ((re_ or 0) / ta) + 6.72 * ebit / ta + 1.05 * eq / tl


def beneish_m(cd):
    y, p = _two_years(cd)
    if y is None or p is None:
        return None
    g = cd.get
    s, s0 = g("revenue", y), g("revenue", p)
    ta, ta0 = g("assets", y), g("assets", p)
    ni, cfo = g("net_income", y), g("ocf", y)
    if None in (s, s0, ta, ta0, ni, cfo) or not s or not s0 or not ta or not ta0:
        return None

    def idx(a, b):
        v = _ratio(a, b)
        return v if v is not None and v > 0 else 1.0
    ar, ar0 = g("accounts_receivable", y), g("accounts_receivable", p)
    dsri = idx(_ratio(ar, s), _ratio(ar0, s0)) if (ar is not None and ar0) else 1.0
    gp, gp0 = g("gross_profit", y), g("gross_profit", p)
    gm, gm0 = _ratio(gp, s), _ratio(gp0, s0)
    gmi = idx(gm0, gm) if (gm and gm0) else 1.0

    def aq(t):
        ca, ppe, sec, a = g("assets_current", t), g("ppe_net", t), g("lt_investments", t) or 0, g("assets", t)
        return (1 - (ca + ppe + sec) / a) if None not in (ca, ppe, a) and a else None
    aqi = idx(aq(y), aq(p)) if (aq(y) is not None and aq(p)) else 1.0
    sgi = s / s0
    dep, dep0, ppe, ppe0 = g("da", y), g("da", p), g("ppe_net", y), g("ppe_net", p)
    r1 = _ratio(abs(dep) if dep else None, (abs(dep) + ppe) if (dep and ppe is not None) else None)
    r0 = _ratio(abs(dep0) if dep0 else None, (abs(dep0) + ppe0) if (dep0 and ppe0 is not None) else None)
    depi = idx(r0, r1) if (r0 and r1) else 1.0
    sga, sga0 = g("sga", y), g("sga", p)
    sgai = idx(_ratio(sga, s), _ratio(sga0, s0)) if (sga and sga0) else 1.0

    def lev(t):
        cl, ltd, a = g("liabilities_current", t), g("lt_debt_noncurrent", t) or 0, g("assets", t)
        return ((cl + ltd) / a) if cl is not None and a else None
    lvgi = idx(lev(y), lev(p)) if (lev(y) is not None and lev(p)) else 1.0
    tata = (ni - cfo) / ta
    return (-4.84 + 0.920 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi + 0.115 * depi - 0.172 * sgai
            + 4.679 * tata - 0.327 * lvgi)


def magic_roc(rows):
    """EBIT / tangible capital of the latest year (already computed by metrics as roc_tangible)."""
    return rows[-1].get("roc_tangible") if rows else None


def all_scores(cd, rows):
    out = {}
    for k, fn in (("fscore", piotroski), ("gp_assets", gross_prof), ("z2", altman_z2), ("mscore", beneish_m)):
        try:
            out[k] = fn(cd)
        except (TypeError, ZeroDivisionError, ValueError):
            out[k] = None
    out["roc_tangible"] = magic_roc(rows)
    eq = cd.get("equity", max(cd.label_end)) if cd.label_end else None
    out["book_equity"] = eq
    return out
