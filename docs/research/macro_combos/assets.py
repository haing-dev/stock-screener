"""What to hold in the non-stock share (and whether to add a non-stock sleeve when fully invested), given the live
4.0.0 stock exposure. Written 2026-10-29 before results. Retail-tradeable instruments only (ETF proxies):
  bills (BIL ~ 3-month T-bill), 10y (IEF; synthetic GS10 duration 7 before 2002-08), long (TLT; synthetic GS30 duration 15
  from 1977-03, else the 10y), short (SHY; synthetic GS2 duration 1.9), gold (GLD-like: COMEX month-end GC=F from 2000-09,
  monthly average London price before), defensive sectors (XLP/XLU/XLV equal weight).
Rules for the non-stock share (decided at month end t, earned in t+1; signals known at t):
  L0 bills | L1 live: 10y if stock-bond corr < 0 else bills | L2 long if corr < 0 else bills
  L3 L1, but gold instead of bills when inflation is hot | L4 L1, but gold instead of bills (whenever corr >= 0)
  L5 half L1, half gold | L6 by cause: growth-trend cut -> long if corr < 0 (else bills); Fed-tightening cut -> bills
  L7 L6 + gold instead of bills when inflation is hot | L8 walk-forward: in each situation (corr sign x inflation hot x
  cause) hold the candidate (bills/10y/long/gold) with the best average return in past months of that situation (>= 24
  months seen, else bills) | L9 absolute momentum: equal weight of 10y/long/gold with a positive 12-month return,
  else bills | L10 defensive sectors.
Sleeve tests while 100% in stocks: S1 10% gold always; S2 20% gold when inflation hot; S3 20% gold when hot and the
Fed is not tightening.
"""
import math
import os
import pickle
import sys
import warnings

warnings.filterwarnings("ignore")
import numpy as np    # noqa: E402
import pandas as pd   # noqa: E402

REPO = "/home/claude/stock-screener"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
os.chdir(REPO)
from macro import engine as E      # noqa: E402
from macro import registry as R    # noqa: E402

P = pickle.load(open(os.path.join(HERE, "panel.pkl"), "rb"))
grid, mkt, rf, ind, F, sc, share = P["grid"], P["mkt"], P["rf"], P["ind"], P["F"], P["sc"], P["share"]
T = len(grid)
Per = lambda s: pd.Period(s, "M")
OUT = []


def log(s=""):
    print(s, flush=True)
    OUT.append(str(s))


# ---------------- 4.0.0 exposure (same steps as engine.derisk)
X = R.SETTINGS["derisk"]
lo, hi = X["band"]
ff = F["FEDFUNDS"]
fed = ((ff - ff.rolling(24, min_periods=12).min()) >= 1.0).fillna(False)
unr = F["UNRATE"]
gtt = ((ind["spx_trend"] < 0) & (unr > unr.rolling(12).mean())).fillna(False)
warn_cut = ((share - lo) / (hi - lo)).clip(0, 1) * fed.astype(float)
e = np.minimum(1 - warn_cut, pd.Series(np.where(gtt, 0.0, 1.0), index=grid)).fillna(1.0)
cause_g = gtt                                        # growth-trend cut active
hot = P["hot"].astype(bool)
cneg = (ind["stockbond"] < 0).fillna(False)

# ---------------- asset returns (earned in month t)
fm = lambda s: E.fred_monthly(s, grid)
px = lambda s: E.monthly_px(s, grid).pct_change(fill_method=None)
syn = lambda y, d: y.shift(1) / 1200 - d * (y - y.shift(1)) / 100
b10 = px("Y_IEF").combine_first(syn(F["GS10"], 7))
b30 = px("Y_TLT").combine_first(syn(fm("GS30"), 15)).combine_first(b10)
bsh = px("Y_SHY").combine_first(syn(F["GS2"], 1.9)).combine_first(syn(fm("GS1"), 0.95))
gc = px("Y_GC_F")
g_avg = E._csv("GOLD")
g_avg = pd.Series(g_avg.values, index=g_avg.index.to_period("M")).reindex(grid).pct_change(fill_method=None)
gold = gc.combine_first(g_avg)
rets = P["rets"]
defs = rets[R.DEFENSIVE].mean(axis=1)
A = pd.DataFrame({"bills": rf, "10y": b10, "long": b30, "short": bsh, "gold": gold, "defsec": defs})
ov = gc.notna() & g_avg.notna()
log(f"gold check 2000-09+: month-end vs monthly-average returns corr {gc[ov].corr(g_avg[ov]):.2f}, "
    f"mean {gc[ov].mean()*1200:.1f} vs {g_avg[ov].mean()*1200:.1f}%/yr; avg-price return autocorr "
    f"{g_avg[ov].autocorr():.2f} vs {gc[ov].autocorr():.2f}")
tl = px("Y_TLT")
o2 = tl.notna()
log(f"long-bond check 2002-08+: synthetic GS30 d15 vs TLT corr {syn(fm('GS30'), 15)[o2].corr(tl[o2]):.2f}, "
    f"{syn(fm('GS30'), 15)[o2].mean()*1200:.1f} vs {tl[o2].mean()*1200:.1f}%/yr")
log("asset CAGR 1975-2026: " + ", ".join(f"{c} {((1 + A[c][(grid >= Per('1975-02'))].fillna(0)).prod() ** (12 / len(grid[grid >= Per('1975-02')])) - 1) * 100:.1f}%" for c in A))


# ---------------- defensive rules: weights over A columns, decided at t
def W(**k):
    d = pd.DataFrame(0.0, index=grid, columns=A.columns)
    for c, v in k.items():
        d[c] = v.astype(float) if isinstance(v, pd.Series) else v
    return d


L = {}
L["L0 bills"] = W(bills=1.0)
L["L1 10y if corr<0 (live)"] = W(**{"10y": cneg, "bills": ~cneg})
L["L2 long if corr<0"] = W(long=cneg, bills=~cneg)
L["L3 L1, gold not bills when hot"] = W(**{"10y": cneg, "gold": ~cneg & hot, "bills": ~cneg & ~hot})
L["L4 L1, gold not bills"] = W(**{"10y": cneg, "gold": ~cneg})
L["L5 half L1, half gold"] = W(**{"10y": 0.5 * cneg, "bills": 0.5 * ~cneg, "gold": pd.Series(0.5, index=grid)})
l6l = cneg & cause_g
L["L6 by cause"] = W(long=l6l, bills=~l6l)
L["L7 by cause + gold when hot"] = W(long=l6l, gold=~l6l & hot, bills=~l6l & ~hot)
L["L10 defensive sectors"] = W(defsec=1.0)
mom12 = (1 + A[["10y", "long", "gold"]]).rolling(12).apply(np.prod, raw=True) - 1
pos = (mom12 > 0)
npos = pos.sum(axis=1)
w9 = W()
for c in ("10y", "long", "gold"):
    w9[c] = (pos[c] / npos.replace(0, np.nan)).fillna(0.0)
w9["bills"] = (npos == 0).astype(float)
L["L9 absolute momentum"] = w9
# L8 walk-forward by situation: average of next-month returns seen so far (all months, not just cut months)
cands = ["bills", "10y", "long", "gold"]
sit = (cneg.astype(int).astype(str) + hot.astype(int).astype(str) + cause_g.astype(int).astype(str))
nxt = A[cands].shift(-1)                                   # return earned after a decision at t
w8 = W()
for t in range(T):
    s_ = sit.iloc[t]
    past = (sit.iloc[:max(0, t - 0)] == s_) & nxt.iloc[:t].notna().all(axis=1)   # outcomes finished by t
    past = past & (pd.Series(range(t), index=grid[:t]) < t - 1)
    if past.sum() >= 24:
        best = nxt.iloc[:t][past.values].mean().idxmax()
    else:
        best = "bills"
    w8.iloc[t, w8.columns.get_loc(best)] = 1.0
L["L8 walk-forward by situation"] = w8


def run(wdef, sleeve=None):
    eh = e.shift(1)
    wd = wdef.shift(1)
    alt = (wd * A.fillna(0)).sum(axis=1)                    # missing proxies count as 0 only before they exist
    alt = alt.where(~(wd * A.isna()).any(axis=1) | True, rf)
    r = eh * mkt + (1 - eh) * alt
    if sleeve is not None:                                  # (weight, asset) while 100% in stocks
        sw = sleeve[0].shift(1).fillna(0) * (eh > 1 - 1e-9)
        r = r - sw * mkt + sw * A[sleeve[1]].fillna(0)
    return r


def st(r, a, b):
    m = (grid >= Per(a)) & (grid <= Per(b))
    x, f = r[m], rf[m]
    lv = np.r_[1, (1 + x.values).cumprod()]
    return (lv[-1] ** (12 / len(x)) - 1) * 100, (lv / np.maximum.accumulate(lv) - 1).min() * 100, (x - f).mean() / x.std() * math.sqrt(12)


def line(nm, r):
    c = [st(r, *w) for w in (("1975-02", "2000-12"), ("2001-01", "2026-10"), ("1975-02", "2026-10"), ("1966-01", "1974-12"))]
    return (f"{nm:<36} " + " | ".join(f"{a:5.1f}% {b:4.0f}% {s:4.2f}" for a, b, s in c))


log("\n== non-stock share rules (stock exposure = live 4.0.0). Cells: CAGR / worst fall / Sharpe for "
    "1975-2000 | 2001-2026 | 1975-2026 | 1966-1974 (untouched; long = 10y before 1977)")
log(f"{'S&P 500':<36} " + line("", mkt)[37:])
R_ = {}
for nm, w in L.items():
    R_[nm] = run(w)
    log(line(nm, R_[nm]))
log("\n== sleeves while fully invested (non-stock share per L1)")
for nm, sl in (("S1 10% gold always", (pd.Series(0.1, index=grid), "gold")),
               ("S2 20% gold when inflation hot", (0.2 * hot.astype(float), "gold")),
               ("S3 20% gold when hot, Fed not tightening", (0.2 * (hot & ~fed).astype(float), "gold")),
               ("S4 20% long bonds when corr<0", (0.2 * cneg.astype(float), "long"))):
    log(line(nm, run(L["L1 10y if corr<0 (live)"], sl)))

# where the non-stock share actually sat, and per-cause average monthly returns of each asset in cut months
cut = e.shift(1) < 1 - 1e-9
log("\n== average return per month in months with a cut, by cause (descriptive only), %")
for nm, msk in (("growth-trend cut", cut & cause_g.shift(1).fillna(False)), ("Fed-tightening cut only", cut & ~cause_g.shift(1).fillna(False))):
    m = msk & (grid >= Per("1975-02"))
    log(f"  {nm} ({int(m.sum())} months): " + ", ".join(f"{c} {A[c][m].mean()*100:+.2f}" for c in A) + f", S&P {mkt[m].mean()*100:+.2f}")
open(os.path.join(HERE, "log_assets.txt"), "w").write("\n".join(OUT))
pickle.dump({"A": A, "L": L, "e": e, "R": R_}, open(os.path.join(HERE, "assets.pkl"), "wb"))
