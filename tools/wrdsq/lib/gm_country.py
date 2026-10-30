"""Global Macro Book - country equity research that runs ON WRDS Cloud (data stays there; prints statistics only).

Datasets (made by the gm_country_pull job, stored in ~/wrdsq/data):
  jkp_ctry   country x month aggregates from contrib_global_factor.global_factor (Jensen-Kelly-Pedersen):
             n stocks, total ME (USD), aggregate B/M, E/P, D/P, next-month value-weighted USD excess return
  ibes_ctry  I/B/E/S country-code x month analyst-revision counts (fiscal year 1 EPS); 'US_FILE' = US file
v2 (2026-10-30): universe = the plan's 25 liquid markets (AMP 2013's 18 developed + 7 large EM), fixed before testing.
v1 used all 95 JKP countries; frontier markets with extreme country-months dominated (2008-2025 vol 219%).
Tests (monthly, rank-weighted, dollar-neutral, $1 long / $1 short, USD excess returns, gross):
  value_bm (aggregate B/M), value_ep (aggregate E/P), value_dp (dividend yield), momentum_12_1,
  revisions (3-month average of (up - down) / estimates), combo = mean of value_bm and momentum,
  combo3 = mean of value composite, momentum and revisions. v3: value composite (avg rank of B/M, E/P, D/P),
  directional time-series momentum for comparison, investable-stock filter in the pull (no micro/nano caps,
  stock returns within -95%..+300%), I/B/E/S codes mapped by estimate currency (glcountry not subscribed).
"""
import numpy as np
import pandas as pd

UNIVERSE = ["USA", "GBR", "DEU", "FRA", "JPN", "CAN", "AUS", "HKG", "CHE", "SWE", "NLD", "ITA", "ESP", "DNK", "NOR",
            "BEL", "AUT", "PRT", "CHN", "KOR", "TWN", "IND", "BRA", "MEX", "ZAF"]
NAMES = {"USA": ["united states", "usa", "u.s."], "GBR": ["united kingdom", "great britain", "u.k."], "DEU": ["germany"],
         "FRA": ["france"], "JPN": ["japan"], "CAN": ["canada"], "AUS": ["australia"], "HKG": ["hong kong"],
         "CHE": ["switzerland"], "SWE": ["sweden"], "NLD": ["netherlands", "holland"], "ITA": ["italy"], "ESP": ["spain"],
         "DNK": ["denmark"], "NOR": ["norway"], "BEL": ["belgium"], "AUT": ["austria"], "PRT": ["portugal"],
         "CHN": ["china"], "KOR": ["korea"], "TWN": ["taiwan"], "IND": ["india"], "BRA": ["brazil"], "MEX": ["mexico"],
         "ZAF": ["south africa"]}
MIN_STOCKS = 30
PERIODS = (("1990-01", "2007-12"), ("2008-01", "2025-12"), ("1990-01", "2025-12"))


def _rank_weights(sig):
    r = sig.rank(axis=1)
    w = r.sub(r.mean(axis=1), axis=0)
    return w.div(w.abs().sum(axis=1) / 2, axis=0)


def _stats(x, a, b):
    x = x[(x.index >= pd.Period(a, "M")) & (x.index <= pd.Period(b, "M"))].dropna()
    if len(x) < 24:
        return "n/a"
    m, s = x.mean() * 12, x.std() * np.sqrt(12)
    lv = (1 + x).cumprod()
    return "%5.1f%%/yr vol %4.1f%% SR %5.2f t %5.2f worst %4.0f%% n %d" % (
        m * 100, s * 100, m / s, x.mean() / x.std() * np.sqrt(len(x)), (lv / lv.cummax() - 1).min() * 100, len(x))


CUR2ISO = {"GBP": "GBR", "BPN": "GBR", "DEM": "DEU", "FRF": "FRA", "JPY": "JPN", "CAD": "CAN", "AUD": "AUS", "HKD": "HKG",
           "CHF": "CHE", "SEK": "SWE", "NLG": "NLD", "ITL": "ITA", "ESP": "ESP", "DKK": "DNK", "NOK": "NOR", "BEF": "BEL",
           "ATS": "AUT", "PTE": "PRT", "CNY": "CHN", "RMB": "CHN", "KRW": "KOR", "TWD": "TWN", "INR": "IND", "BRL": "BRA",
           "MXN": "MEX", "MXP": "MEX", "ZAR": "ZAF"}


def _ibes_map(sql, codes, out):
    """Map I/B/E/S country codes to ISO3 by the currency their analysts' estimates are in (pre-euro currencies tell the
    euro-area countries apart). ibes.glcountry is not in the subscription."""
    q = ("with idc as (select ticker, max(country) as country from ibes.idsum group by ticker) "
         "select i.country, s.curcode, (s.statpers < '1999-01-01') as pre, count(*) as n from ibes.statsum_epsint s "
         "join idc i on s.ticker=i.ticker where s.fpi='1' and s.measure='EPS' group by 1,2,3")
    try:
        g = sql(q)
    except Exception as e:  # noqa: BLE001
        out("currency map query failed: %s" % str(e)[:150])
        return {"US_FILE": "USA"}
    g["country"] = g["country"].astype(str).str.strip()
    g["curcode"] = g["curcode"].astype(str).str.strip()
    best, diag = {}, []
    for c, x in g.groupby("country"):
        pre = x[x["pre"].astype(bool)]
        y = pre if len(pre) and pre["n"].sum() > 500 else x
        y = y.groupby("curcode")["n"].sum().sort_values(ascending=False)
        if len(y):
            diag.append((int(x["n"].sum()), c, y.index[0], y.iloc[0] / y.sum(), " ".join(y.index[:3])))
        if len(y) and y.iloc[0] / y.sum() > 0.6:
            best[c] = (y.index[0], int(x["n"].sum()))
    out("largest I/B/E/S codes (rows, code, top currency, share, top 3): " + "; ".join(
        "%s %s %.0f%% [%s]" % (c, cur, sh * 100, t3) for n, c, cur, sh, t3 in sorted(diag, reverse=True)[:30]))
    m = {"US_FILE": "USA", "LB": "BRA"}   # I/B/E/S reports Brazil in USD (code LB, L = Latin America)
    for cur, iso in CUR2ISO.items():
        cands = [(n, c) for c, (cc, n) in best.items() if cc == cur]
        if cands and iso not in m.values():
            m[max(cands)[1]] = iso
    return m


def run(load, out, sql=None, dataset="jkp_ctry"):
    d = load(dataset)
    d["eom"] = pd.to_datetime(d["eom"]).dt.to_period("M")
    d = d[d["excntry"].isin(UNIVERSE) & (d["n"] >= MIN_STOCKS)]
    piv = lambda c: d.pivot_table(index="eom", columns="excntry", values=c)
    ret_lead, bm, ep, dp = piv("ret_lead_vw"), piv("bm_agg"), piv("ep_agg"), piv("dp_agg")
    out("dataset %s" % dataset)
    cov = d.groupby("excntry")["eom"].agg(["min", "max", "count"])
    out("coverage (first, last, months with >= %d investable stocks): " % MIN_STOCKS + "; ".join(
        "%s %s-%s %d" % (c, r["min"], r["max"], r["count"]) for c, r in cov.iterrows()))
    out("universe countries absent: %s" % (", ".join(c for c in UNIVERSE if c not in cov.index) or "none"))
    ret = ret_lead.shift(1)
    mom = (1 + ret).rolling(11).apply(np.prod, raw=True).shift(1) - 1
    sig = {"value_bm": np.log(bm.where(bm > 0)), "value_ep": ep, "value_dp": dp, "momentum_12_1": mom}
    rk = lambda x: x.rank(axis=1, pct=True)
    sig["value_composite"] = (rk(sig["value_bm"]) + rk(ep) + rk(dp)) / 3
    # analyst revisions breadth
    rev_ok = False
    try:
        v = load("ibes_ctry")
        codes = set(v["country"].astype(str).str.strip())
        mp = _ibes_map(sql, codes, out) if sql else {"US_FILE": "USA"}
        out("I/B/E/S codes mapped: %s" % ", ".join("%s=%s" % (k, mp[k]) for k in sorted(mp, key=lambda k: mp[k])))
        missing = [c for c in UNIVERSE if c not in mp.values()]
        out("universe countries without I/B/E/S code: %s" % (", ".join(missing) or "none"))
        v = v.copy()
        v["iso"] = v["country"].astype(str).str.strip().map(mp)
        v = v.dropna(subset=["iso"])
        v["eom"] = pd.to_datetime(v["m"]).dt.to_period("M")
        v["br"] = (v["up"] - v["dn"]) / v["nest"].where(v["nest"] > 0)
        br = v.pivot_table(index="eom", columns="iso", values="br").reindex(ret_lead.index)
        sig["revisions_3m"] = br.rolling(3, min_periods=2).mean()
        rev_ok = True
    except Exception as e:  # noqa: BLE001
        out("revisions not available: %s" % str(e)[:200])
    ok = ret_lead.notna() & mom.notna()
    strat = {}
    for k, s in sig.items():
        s = s.reindex_like(ret_lead).where(ok)
        strat[k] = (_rank_weights(s.where(s.notna())) * ret_lead).sum(axis=1, min_count=8)
    # directional (time-series) momentum: long countries up over 12-1 months, short those down; 1/N, vol-scaled
    vol = ret.rolling(36, min_periods=24).std()
    tsw = (np.sign(mom) / vol).where(ok)
    tsw = tsw.div(tsw.abs().sum(axis=1), axis=0)
    strat["ts_momentum_12_1"] = (tsw * ret_lead).sum(axis=1, min_count=8)
    strat = pd.DataFrame(strat)
    strat["combo_value_mom"] = strat[["value_composite", "momentum_12_1"]].mean(axis=1, skipna=False)
    if rev_ok:
        strat["combo_value_rev"] = strat[["value_composite", "revisions_3m"]].mean(axis=1)
        strat["combo3_val_mom_rev"] = strat[["value_composite", "momentum_12_1", "revisions_3m"]].mean(axis=1)
    # robustness for value composite, revisions and value+revisions: signal used one month later; costs 10 bp per
    # 100% one-way turnover; turnover per year
    rob = {}
    for k in ["value_composite", "revisions_3m"] if rev_ok else ["value_composite"]:
        sg = sig[k].reindex_like(ret_lead).where(ok)
        for lag in (0, 1):
            w = _rank_weights(sg.shift(lag).where(ok))
            gross = (w * ret_lead).sum(axis=1, min_count=8)
            to = w.fillna(0).diff().abs().sum(axis=1) / 2
            rob["%s lag%d" % (k, lag)] = (gross, gross - 0.001 * to * 2, to)
    if rev_ok:
        for lag in (0, 1):
            g = (rob["value_composite lag%d" % lag][0] + rob["revisions_3m lag%d" % lag][0]) / 2
            n = (rob["value_composite lag%d" % lag][1] + rob["revisions_3m lag%d" % lag][1]) / 2
            t = (rob["value_composite lag%d" % lag][2] + rob["revisions_3m lag%d" % lag][2]) / 2
            rob["combo_value_rev lag%d" % lag] = (g, n, t)
    out("robustness (net = after 10 bp per unit traded each side; turnover = one-way per year):")
    for k, (g, n, t) in rob.items():
        out("   %-26s net 1990-2025 %s | 2008-2025 %s | turnover %.1fx/yr" % (
            k, _stats(n, "1990-01", "2025-12"), _stats(n, "2008-01", "2025-12"), t.loc["1990-01":].mean() * 12))
    out("universe (%d): %s; countries per month: %s" % (len(UNIVERSE), " ".join(UNIVERSE), ", ".join(
        "%d:%d" % (y, ok.loc[str(y)].sum(axis=1).median()) for y in (1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025))))
    out("largest single country-month return used: %.0f%%; months with |ret| > 50%%: %d" % (
        ret_lead.where(ok).abs().max().max() * 100, int((ret_lead.where(ok).abs() > 0.5).sum().sum())))
    out("strategy returns: gross, monthly, dollar-neutral ($1 long, $1 short), USD excess of T-bills")
    for k in strat:
        out("\n" + k)
        for a, b in PERIODS:
            out("   %s..%s  %s" % (a, b, _stats(strat[k], a, b)))
    out("\ncorrelations 1990-2025:\n" + strat.loc["1990-01":].corr().round(2).to_string())
    last = ok.index[ok.sum(axis=1) > 8][-1]
    for k, s in sig.items():
        r = s.reindex_like(ret_lead).loc[last].where(ok.loc[last]).dropna().sort_values()
        out("%s %s  lowest 5: %s | highest 5: %s" % (k, last, ", ".join(r.index[:5]), ", ".join(r.index[-5:])))
    if rev_ok:
        cv = (sig["value_composite"].rank(axis=1, pct=True) + sig["revisions_3m"].rank(axis=1, pct=True)).reindex_like(ret_lead)
        r = cv.loc[last].where(ok.loc[last]).dropna().sort_values()
        out("value+revisions %s  lowest 5: %s | highest 5: %s" % (last, ", ".join(r.index[:5]), ", ".join(r.index[-5:])))
    out("(high B/M, E/P, D/P = cheap; high momentum = strong; high revisions = analysts raising estimates)")
