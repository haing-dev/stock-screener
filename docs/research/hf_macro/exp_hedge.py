"""Exp 5 (pre-registered 2026-10-29): hedges and fast exits on top of candidate 5.0.
 H1 daily crash cap: on any day the S&P closes >= 10% below its 20-day high, stocks go to 50% until the month-end
    decision (rest in T-bills). H1b: 7%. H1c: cut to 0%.
 H2 protective puts: stock part held as CBOE PPUT (S&P + 5% out-of-the-money monthly puts) instead of the S&P while
    warnings are 15%+ (but no cut is on) and VIX < 20 (cheap insurance, Tropin/Bessent); H2b always.
 H3 sentiment: AAII bulls-minus-bears in its bottom 10% (fear) -> no cut that month (re-entry); top 10% (euphoria) and
    warnings >= 15% -> 50% stocks.
Windows 1990-2000 | 2001-2026 | 1990-2026 (daily data 1970+, PPUT 1986+, AAII 1987+); and 1975+ for H1."""
from robust5 import *  # noqa
import os

RD = "/home/claude/stock-screener/cache/macro/raw/research"
d = pd.read_csv(os.path.join(RD, "D__GSPC.csv"), parse_dates=["date"]).set_index("date")["value"]
dr = d.pct_change()
mon = d.index.to_period("M")
hi20 = d.rolling(20, min_periods=5).max()
rfd = rf.reindex(mon).values / 21


def crash_cap(e, th=0.10, to=0.5):
    """Monthly stock return replaced by a daily path: after a trigger day, exposure capped at `to` for the rest of the
    month. Returns an adjusted monthly S&P series to use as the stock asset, scaled to exposure e."""
    trig = (d <= (1 - th) * hi20)
    out = {}
    for p, g in dr.groupby(mon):
        tg = trig[g.index].values
        cap = np.zeros(len(g))
        on = False
        for i in range(len(g)):
            cap[i] = on
            if tg[i]:
                on = True
        out[p] = (g.values, cap)
    return out


paths = crash_cap(None)


def apply_cap(r_strategy, e, th=0.10, to=0.5):
    trig = (d <= (1 - th) * hi20)
    adj = r_strategy.copy()
    eh = e.shift(1)
    for p, g in dr.groupby(mon):
        if p not in adj.index or np.isnan(adj.get(p, np.nan)):
            continue
        tg = trig[g.index].values
        if not tg[:-1].any():
            continue
        x = eh.get(p, np.nan)
        if np.isnan(x) or x <= to:
            continue
        on, extra = False, 0.0
        lv = 1.0
        # difference from holding x of stocks vs `to` of stocks on capped days (rest T-bills)
        for i, ret in enumerate(g.values):
            if on:
                extra += (to - x) * (ret - rf.get(p, 0) / 21)
            if tg[i]:
                on = True
        adj[p] = adj[p] + extra
    return adj


W5 = (("1975-02", "2000-12"), ("2001-01", "2026-10"), ("1975-02", "2026-10"))
print("== CAGR / worst / Sharpe: 1975-2000 | 2001-2026 | 1975-2026")
print(line("candidate 5.0", r5, W5))
for th, to in ((0.10, 0.5), (0.07, 0.5), (0.10, 0.0), (0.15, 0.0)):
    print(line(f"H1 crash cap {th:.0%} below 20d high -> {to:.0%}", apply_cap(r5, e5, th, to), W5))

# H2 puts
pp = pd.read_csv(os.path.join(RD, "cboe_ppt_history.csv"))
pp.columns = [c.strip().upper() for c in pp.columns]
dc = [c for c in pp.columns if "DATE" in c][0]
vc = [c for c in pp.columns if c != dc][0]
pp = pd.Series(pd.to_numeric(pp[vc], errors="coerce").values, index=pd.to_datetime(pp[dc]).dt.to_period("M")).groupby(level=0).last().reindex(grid)
ppr = pp.pct_change(fill_method=None)
o = ppr.notna() & R["spx"].notna()
print(f"\nPPUT vs S&P (overlap {o.sum()} months): {ppr[o].mean()*1200:.1f} vs {R['spx'][o].mean()*1200:.1f}%/yr, vol {ppr[o].std()*346:.1f} vs {R['spx'][o].std()*346:.1f}")
vix = S["px_^VIX"].combine_first(P["vix"])
W90 = (("1990-01", "2000-12"), ("2001-01", "2026-10"), ("1990-01", "2026-10"))
for nm, cond in (("H2 puts when warnings >= 15%, no cut, VIX < 20", (share >= 0.15) & (e5 > 0.999) & (vix < 20)),
                 ("H2b puts always", pd.Series(True, index=grid))):
    cnd = cond.shift(1).fillna(False) & ppr.notna()
    adj = r5 + e5.shift(1) * (ppr - R["spx"]).where(cnd, 0.0)
    print(line(nm, adj, W90), f"(on {cond[grid >= Per('1990-01')].mean():.0%} of months)")
print(line("candidate 5.0", r5, W90))

# H3 AAII
try:
    aa = pd.read_excel(os.path.join(RD, "aaii_sentiment.xls"), header=None)
    hdr = 3
    names_ = [str(x).strip() for x in aa.iloc[hdr]]
    ib, ie = names_.index("Bullish"), names_.index("Bearish")
    body = aa.iloc[hdr + 1:]
    dt = pd.to_datetime(body.iloc[:, 0], errors="coerce")
    ok_ = dt.notna().values
    bb = pd.to_numeric(body.iloc[:, ib], errors="coerce").values[ok_] - pd.to_numeric(body.iloc[:, ie], errors="coerce").values[ok_]
    bb = pd.Series(bb, index=dt[ok_].dt.to_period("M").values).groupby(level=0).mean().reindex(grid)
    pb = pctl(bb, 60)
    fear, euph = (pb <= 10).fillna(False), (pb >= 90).fillna(False)
    e_h3 = e5.where(~fear, np.maximum(e5, e41.where(~fear, 1.0)))
    e_h3 = pd.Series(np.where(fear, 1.0, e5), index=grid)
    r_h3a = run(build(e_h3, D_["D7"], xx, "L4"))
    e_h3b = np.minimum(e5, pd.Series(np.where(euph & (share >= 0.15), 0.5, 1.0), index=grid))
    r_h3b = run(build(e_h3b, D_["D7"], xx, "L4"))
    print(line("H3a no cut in fear months (AAII bottom 10%)", r_h3a, W90))
    print(line("H3b euphoria + warnings -> 50%", r_h3b, W90))
except Exception as ex:
    print("AAII failed", ex)
