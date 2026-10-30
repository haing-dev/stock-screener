"""Global Macro Book - country equity research that runs ON WRDS Cloud (data stays there; prints statistics only).

Datasets (made by the gm_country_pull job, stored in ~/wrdsq/data):
  jkp_ctry   country x month aggregates from contrib_global_factor.global_factor (Jensen-Kelly-Pedersen):
             n stocks, total ME (USD), aggregate B/M, E/P, D/P, next-month value-weighted USD excess return
  ibes_ctry  country x month analyst-revision counts from I/B/E/S summary files (fiscal year 1 EPS)
Tests (pre-registered 2026-10-30, Asness-Moskowitz-Pedersen style, monthly, rank-weighted dollar-neutral):
  value = aggregate B/M; value_ep = aggregate E/P; momentum = 12-1 month return; combo = 50/50 value + momentum
Universe: countries with >= 30 stocks that month; signals need 12 months of history. Periods 1990-2007 | 2008-2025.
"""
import numpy as np
import pandas as pd

MIN_STOCKS = 30
PERIODS = (("1990-01", "2007-12"), ("2008-01", "2025-12"), ("1990-01", "2025-12"))


def _panel(load):
    d = load("jkp_ctry")
    d["eom"] = pd.to_datetime(d["eom"]).dt.to_period("M")
    d = d[d["n"] >= MIN_STOCKS]
    piv = lambda c: d.pivot_table(index="eom", columns="excntry", values=c)
    return piv("ret_lead_vw"), piv("bm_agg"), piv("ep_agg"), piv("n")


def _rank_weights(sig):
    """Rank-weighted, dollar-neutral, $1 long / $1 short (AMP 2013 eq. 1)."""
    r = sig.rank(axis=1)
    w = r.sub(r.mean(axis=1), axis=0)
    return w.div(w.abs().sum(axis=1) / 2, axis=0)


def _stats(x, a, b):
    x = x[(x.index >= pd.Period(a, "M")) & (x.index <= pd.Period(b, "M"))].dropna()
    if len(x) < 24:
        return "n/a"
    m, s = x.mean() * 12, x.std() * np.sqrt(12)
    t = x.mean() / x.std() * np.sqrt(len(x))
    lv = (1 + x).cumprod()
    return "%5.1f%%/yr vol %4.1f%% SR %5.2f t %5.2f worst %4.0f%% n %d" % (
        m * 100, s * 100, m / s, t, (lv / lv.cummax() - 1).min() * 100, len(x))


def run(load, out):
    ret_lead, bm, ep, n = _panel(load)
    # realized return in month t = next-month return recorded at t-1
    ret = ret_lead.shift(1)
    mom = (1 + ret).rolling(11).apply(np.prod, raw=True).shift(1) - 1          # months t-11..t-1 (skip month t)
    sig = {"value_bm": np.log(bm.where(bm > 0)), "value_ep": ep, "momentum_12_1": mom}
    ok = ret_lead.notna() & mom.notna()
    strat = {}
    for k, s in sig.items():
        s = s.where(ok & s.notna())
        w = _rank_weights(s)
        strat[k] = (w * ret_lead).sum(axis=1, min_count=5)                          # return earned in month t+1
    strat = pd.DataFrame(strat)
    strat["combo_bm_mom"] = 0.5 * strat["value_bm"] / strat["value_bm"].std() + 0.5 * strat["momentum_12_1"] / strat["momentum_12_1"].std()
    strat["combo_bm_mom"] *= strat["value_bm"].std()                                 # back to value's volatility scale
    out("countries per month (>= %d stocks): " % MIN_STOCKS +
        ", ".join("%s %d" % (y, ok.loc[str(y)].sum(axis=1).median()) for y in (1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025)
                  if str(y) in ok.index.astype(str).str[:4].values))
    out("strategy returns are gross, monthly, dollar-neutral ($1 long, $1 short), in USD excess of T-bills")
    for k in strat:
        out("\n" + k)
        for a, b in PERIODS:
            out("   %s..%s  %s" % (a, b, _stats(strat[k], a, b)))
    c = strat.loc["1990-01":].corr()
    out("\ncorrelations 1990-2025:\n" + c.round(2).to_string())
    # current tilts (signal ranks only, no data values): top / bottom 5 countries by each signal at the last month
    last = ok.index[ok.sum(axis=1) > 5][-1]
    for k, s in sig.items():
        r = s.loc[last].where(ok.loc[last]).dropna().sort_values()
        out("%s %s  lowest 5: %s | highest 5: %s   (high B/M or E/P = cheap; high momentum = strong)" % (
            k, last, ", ".join(r.index[:5]), ", ".join(r.index[-5:])))
    # revisions coverage (mapping of I/B/E/S country codes is built from this)
    try:
        v = load("ibes_ctry")
        g = v.groupby("country").agg(first=("m", "min"), last=("m", "max"), months=("m", "count"), firms=("nfirm", "median"))
        g = g.sort_values("firms", ascending=False)
        out("\nI/B/E/S revision coverage by country code (median firms/month), top 60:")
        out(", ".join("%s:%d(%s-%s)" % (i, r.firms, str(r["first"])[:4], str(r["last"])[:4]) for i, r in g.head(60).iterrows()))
    except Exception as e:  # noqa: BLE001
        out("ibes_ctry not available: %s" % str(e)[:120])
