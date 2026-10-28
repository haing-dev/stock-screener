"""Macro Compass: factorial test of rule combinations (research only; no repo file changed). Written 2026-10-28
before any result of this grid was computed.

Each variant = one choice per layer (exposure set at month end t, earns month t+1; cash = T-bills unless bonds):
 W  warning signal   W0 none | W1 track-record-weighted warning share (live) | W2 equal-weighted share
                     cut intensity I = clip((share - 15%) / 20%, 0, 1)
 G  confirmation     G0 none | G1 S&P below 10-month average | G2 half the cut on the warning, full cut only with G1 |
    of the cut       G3 unemployment above its 12-month average | G4 G1 or G3 | G5 Fed tightening (funds rate >= 1 pt
                     above its 24-month low) | G6 narrowing market (leadership or breadth score >= 60)
 X  extra cut (min)  X0 none | X1 S&P below trend AND unemployment rising -> floor | X2 S&P below trend -> floor |
                     X3 inflation hot AND Fed tightening -> halfway to floor
 R  re-entry         R0 immediate | R1 keep the lowest exposure of the last 3 months | R2 raise exposure only while the
                     S&P is above its 10-month average (bear-rally guard) | R3 raise at most 25 pts per month
 D  depth (floor)    50% | 25% | 0% stocks at full warning
 B  defensive asset  T-bills | 10-year Treasuries if the 12-month stock-bond correlation < 0 | Treasuries always
 S  sector overlay   none | 12-1 momentum top 5 / bottom 5 (1.5x / 0.5x) only while 100% invested | momentum always
 e = min(1 - I x (1 - floor) x gate, extra cut), then the re-entry rule. Duplicate exposure paths are removed.
Judged on 1975-2000 (fit half) and 2001-2026 (check half) separately; full = 1975-02..2026-10.
Overfitting checks: CSCV probability of backtest overfitting (16 blocks), White reality check on the best Sharpe gain
vs the live rule (stationary bootstrap, mean block 12, 1000 draws), per-layer paired average effects.
"""
import itertools
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
EMP = HERE                      # panel.pkl written here by build_data.py
sys.path.insert(0, REPO)
os.chdir(REPO)
from macro import engine as E      # noqa: E402
from macro import registry as R    # noqa: E402

P = pickle.load(open(os.path.join(EMP, "panel.pkl"), "rb"))
grid, mkt, rf, ind, F, sc = P["grid"], P["mkt"], P["rf"], P["ind"], P["F"], P["sc"]
T = len(grid)
Per = lambda s: pd.Period(s, "M")
OUT = []


def log(s=""):
    print(s, flush=True)
    OUT.append(str(s))


# ---------------------------------------------------------------- signals
X = R.SETTINGS["derisk"]
core = [i["id"] for i in R.INDICATORS if i["pillar"] in X["pillars"]]
bad = (sc[core] >= X["worst"]).astype(float)
av = sc[core].notna().astype(float)
share_w = P["share"]
share_e = (bad.sum(axis=1) / av.sum(axis=1).replace(0, np.nan)).fillna(0).where(av.sum(axis=1) >= 10, 0.0)
lo, hi = X["band"]
I = {"W0": pd.Series(0.0, index=grid),
     "W1": ((share_w - lo) / (hi - lo)).clip(0, 1),
     "W2": ((share_e - lo) / (hi - lo)).clip(0, 1)}
trend_dn = (ind["spx_trend"] < 0)
trend_up = ~trend_dn
unr = F["UNRATE"]
unr_up = unr > unr.rolling(12).mean()
ff = F["FEDFUNDS"]
fed_tight = (ff - ff.rolling(24, min_periods=12).min()) >= 1.0
narrow = (sc["leadership"] >= 60) | (sc["breadth"] >= 60)
hot = P["hot"].astype(bool)
G = {"G0": pd.Series(1.0, index=grid), "G1": trend_dn.astype(float), "G2": 0.5 + 0.5 * trend_dn.astype(float),
     "G3": unr_up.astype(float), "G4": (trend_dn | unr_up).astype(float), "G5": fed_tight.astype(float),
     "G6": narrow.astype(float)}
XC = {"X0": None, "X1": trend_dn & unr_up, "X2": trend_dn, "X3": hot & fed_tight}


def reentry(e, mode):
    if mode == "R0":
        return e
    if mode == "R1":
        return e.rolling(3, min_periods=1).min()
    a, out, prev = e.values, np.empty(T), 1.0
    tu = trend_up.values
    for t in range(T):
        x = a[t]
        if x > prev:
            if mode == "R2" and not tu[t]:
                x = prev
            elif mode == "R3":
                x = min(x, prev + 0.25)
        out[t] = x
        prev = x
    return pd.Series(out, index=grid)


# ---------------------------------------------------------------- returns blocks
y10 = F["GS10"]
bond = (y10.shift(1) / 1200 - 7 * (y10 - y10.shift(1)) / 100)            # synthetic 10-year Treasury (as in the report)
corr_neg = ind["stockbond"] < 0
rets = P["rets"]
avail = rets.shift(-1).notna()
neutral = pd.DataFrame("neutral", index=grid, columns=rets.columns)
w_eq = E.tilt_weights(neutral, avail)
ew = E.portfolio(w_eq, rets)
mom = E.cumret(rets, 12).shift(1)
rk = mom.rank(axis=1, ascending=False)
nav = mom.notna().sum(axis=1)
sig = neutral.copy()
sig[rk <= 5] = "over"
sig[rk.gt(nav - 5, axis=0)] = "under"
wm = E.tilt_weights(sig, avail)
ACT = (E.portfolio(wm, rets) - ew).fillna(0.0)                          # momentum tilt, earned month t+1
ATURN = (wm - w_eq).diff().abs().sum(axis=1).fillna(0.0)

WIN = {"A": ("1975-02", "2000-12"), "B": ("2001-01", "2026-10"), "F": ("1975-02", "2026-10")}
SEL = {k: ((grid >= Per(a)) & (grid <= Per(b))) for k, (a, b) in WIN.items()}

# ---------------------------------------------------------------- engines
engines, seen = [], {}
for w, g, x, r, d in itertools.product(I, G, XC, ("R0", "R1", "R2", "R3"), (0.5, 0.25, 0.0)):
    if w == "W0" and g != "G0":
        continue
    e = 1 - I[w] * (1 - d) * G[g]
    if XC[x] is not None:
        cut = d if x in ("X1", "X2") else (1 + d) / 2
        e = np.minimum(e, pd.Series(np.where(XC[x], cut, 1.0), index=grid))
    e = reentry(pd.Series(e, index=grid).fillna(1.0), r)
    key = np.round(e[SEL["F"] | SEL["A"]].values, 6).tobytes()
    name = f"{w}-{g}-{x}-{r}-D{int(d * 100)}"
    if key in seen:
        continue
    seen[key] = name
    engines.append((name, dict(W=w, G=g, X=x, R=r, D=d), e))
log(f"distinct exposure engines: {len(engines)}")

names, facs, cols, eqs, turns = [], [], [], [], []
rfv, mv, bv, actv = rf.values, mkt.values, bond.values, ACT.values
cn = corr_neg.shift(1).fillna(False).astype(bool).values
for name, fac, e in engines:
    eh = e.shift(1).values
    full_prev = (e.shift(1) > 1 - 1e-9).values
    for b in ("T", "B2", "B1"):
        alt = rfv if b == "T" else (np.where(cn, bv, rfv) if b == "B2" else bv)
        if fac["W"] == "W0" and fac["X"] == "X0" and b != "T":
            continue
        for s in ("S0", "S2", "S1"):
            act = 0.0 if s == "S0" else (actv * full_prev if s == "S2" else actv)
            stk = mv + act
            rr = eh * stk + (1 - eh) * alt
            tr = np.abs(np.diff(np.r_[eh[0], eh]))
            if s != "S0":
                tr = tr + np.nan_to_num(eh) * (ATURN.shift(1).fillna(0).values * (full_prev if s == "S2" else 1))
            names.append(f"{name}-{b}-{s}")
            facs.append(dict(fac, B=b, S=s))
            cols.append(rr)
            eqs.append(eh)
            turns.append(tr)
Rm = np.column_stack(cols)
EQ = np.column_stack(eqs)
TR = np.column_stack(turns)
N = Rm.shape[1]
log(f"variants: {N}")
fac_df = pd.DataFrame(facs, index=names)


def stats_block(sel):
    r, f, eh = Rm[sel], rfv[sel][:, None], EQ[sel]
    lv = np.vstack([np.ones(N), np.cumprod(1 + r, axis=0)])
    yrs = r.shape[0] / 12
    cagr = (lv[-1] ** (1 / yrs) - 1) * 100
    dd = (lv / np.maximum.accumulate(lv, axis=0) - 1).min(axis=0) * 100
    ex = r - f
    sh = ex.mean(axis=0) / r.std(axis=0, ddof=1) * math.sqrt(12)
    avg = eh.mean(axis=0)
    st = avg * mv[sel][:, None] + (1 - avg) * f                 # same-average-exposure stock/T-bill mix
    st_sh = (st - f).mean(axis=0) / st.std(axis=0, ddof=1) * math.sqrt(12)
    lvs = np.vstack([np.ones(N), np.cumprod(1 + st, axis=0)])
    st_dd = (lvs / np.maximum.accumulate(lvs, axis=0) - 1).min(axis=0) * 100
    net = r - 0.001 * TR[sel]
    lvn = np.cumprod(1 + net, axis=0)
    cagr_net = (lvn[-1] ** (1 / yrs) - 1) * 100
    roll12 = pd.DataFrame(r).rolling(12).apply(lambda z: np.prod(1 + z) - 1, raw=True).min().values * 100 if False else None
    de = np.abs(np.diff(eh, axis=0))
    return pd.DataFrame({"cagr": cagr, "maxdd": dd, "sharpe": sh, "avg_eq": avg * 100, "static_sharpe": st_sh,
                         "static_dd": st_dd, "cagr_net": cagr_net, "chg_yr": (de > 0.005).sum(axis=0) / yrs},
                        index=names)


S = {k: stats_block(SEL[k]) for k in WIN}
res = pd.concat({k: v for k, v in S.items()}, axis=1)
res.columns = [f"{a}_{b}" for a, b in res.columns]
res = res.join(fac_df)
RULE = "W1-G0-X0-R0-D50-T-S0"
SPX = "W0-G0-X0-R0-D50-T-S0"
assert RULE in res.index and SPX in res.index
for k in WIN:
    res[f"{k}_dsh"] = res[f"{k}_sharpe"] - res.loc[RULE, f"{k}_sharpe"]
res["worst_half_dsh"] = res[["A_dsh", "B_dsh"]].min(axis=1)
res["vs_static"] = res["F_sharpe"] - res["F_static_sharpe"]
res.to_csv(os.path.join(HERE, "grid_results.csv"))

pd.set_option("display.width", 250)
pd.set_option("display.max_columns", 40)


def show(df, n=None):
    c = ["A_cagr", "A_maxdd", "A_sharpe", "B_cagr", "B_maxdd", "B_sharpe", "F_cagr", "F_cagr_net", "F_maxdd",
         "F_sharpe", "F_avg_eq", "F_chg_yr", "vs_static", "worst_half_dsh"]
    d = df[c].round(2)
    return d.head(n).to_string() if n else d.to_string()


log("\n== baselines")
log(show(res.loc[[SPX, RULE]]))

# ---------------------------------------------------------------- per-layer paired effects
log("\n== average effect of each choice vs the layer's base choice, all else equal (Sharpe pts; share of pairs better)")
BASEL = {"W": "W1", "G": "G0", "X": "X0", "R": "R0", "D": 0.5, "B": "T", "S": "S0"}
eff_rows = []
for lay, base in BASEL.items():
    others = [c for c in BASEL if c != lay]
    key = res[others].astype(str).agg("|".join, axis=1)
    bmap = res[res[lay] == base].assign(k=key[res[lay] == base]).set_index("k")
    for lev in sorted(res[lay].unique(), key=str):
        if lev == base:
            continue
        sub = res[res[lay] == lev]
        k2 = key[sub.index]
        ok = k2.isin(bmap.index)
        if ok.sum() == 0:
            continue
        a = sub[ok.values]
        b = bmap.loc[k2[ok.values].values]
        row = {"layer": lay, "choice": lev, "pairs": int(ok.sum())}
        for w in ("A", "B", "F"):
            dd = a[f"{w}_sharpe"].values - b[f"{w}_sharpe"].values
            row[f"{w}_dSharpe"] = dd.mean()
            row[f"{w}_better"] = (dd > 0).mean()
        row["F_dCAGR"] = (a["F_cagr"].values - b["F_cagr"].values).mean()
        row["F_dMaxDD"] = (a["F_maxdd"].values - b["F_maxdd"].values).mean()
        eff_rows.append(row)
eff = pd.DataFrame(eff_rows)
log(eff.round(3).to_string(index=False))
eff.to_csv(os.path.join(HERE, "layer_effects.csv"), index=False)

# ---------------------------------------------------------------- rankings
cand = res[(res["A_maxdd"] >= res.loc[RULE, "A_maxdd"] - 3) & (res["B_maxdd"] >= res.loc[RULE, "B_maxdd"] - 3)]
log(f"\n== top 25 by the worse of the two halves' Sharpe gain vs the live rule (worst fall within 3 pts of the rule in both halves; {len(cand)} of {N})")
log(show(cand.sort_values("worst_half_dsh", ascending=False), 25))
log("\n== top 15 by full-period Sharpe (any drawdown)")
log(show(res.sort_values("F_sharpe", ascending=False), 15))
log("\n== top 15 by full-period CAGR with worst fall no deeper than -30%")
log(show(res[res["F_maxdd"] >= -30].sort_values("F_cagr", ascending=False), 15))
log("\n== top 15 by smallest worst fall with CAGR >= the S&P 500's")
log(show(res[res["F_cagr"] >= res.loc[SPX, "F_cagr"]].sort_values("F_maxdd", ascending=False), 15))

# ---------------------------------------------------------------- CSCV PBO
sel = SEL["F"]
Z = Rm[sel] - rfv[sel][:, None]
nb = 16
blocks = np.array_split(np.arange(Z.shape[0]), nb)
bs = np.array([Z[b].sum(axis=0) for b in blocks])
bq = np.array([(Z[b] ** 2).sum(axis=0) for b in blocks])
bn = np.array([len(b) for b in blocks])
lam = []
for comb in itertools.combinations(range(nb), nb // 2):
    m = np.zeros(nb, bool)
    m[list(comb)] = True

    def srs(mask):
        n = bn[mask].sum()
        mu = bs[mask].sum(axis=0) / n
        var = bq[mask].sum(axis=0) / n - mu ** 2
        return mu / np.sqrt(var)
    isr, osr = srs(m), srs(~m)
    best = np.argmax(isr)
    rank = (osr < osr[best]).mean()
    lam.append(math.log(max(rank, 1e-6) / max(1 - rank, 1e-6)))
lam = np.array(lam)
log(f"\n== CSCV over all {N} variants, 16 blocks ({len(lam)} splits): probability the in-sample best is below the "
    f"median out of sample (PBO) = {(lam <= 0).mean():.2f}; median out-of-sample rank of the in-sample best = "
    f"{np.median(1 / (1 + np.exp(-lam))):.2f}")

# ---------------------------------------------------------------- White reality check on Sharpe gain vs rule
rng = np.random.default_rng(20261028)
Tn = Z.shape[0]
B_ = 1000
L = 12
idx = np.empty((B_, Tn), dtype=np.int64)
idx[:, 0] = rng.integers(0, Tn, B_)
jump = rng.random((B_, Tn)) < 1.0 / L
fresh = rng.integers(0, Tn, (B_, Tn))
for t in range(1, Tn):
    idx[:, t] = np.where(jump[:, t], fresh[:, t], (idx[:, t - 1] + 1) % Tn)
ir = res.index.get_loc(RULE)


def shv(M):
    return M.mean(axis=0) / M.std(axis=0, ddof=1)


obs = shv(Z) - shv(Z)[ir]
mx = []
dist_top = {}
top = res.sort_values("F_sharpe", ascending=False).index[:10]
ti = [res.index.get_loc(n) for n in top]
for b in range(B_):
    Zb = Z[idx[b]]
    d = shv(Zb) - shv(Zb)[ir]
    mx.append(np.max(d - obs))
    for n, j in zip(top, ti):
        dist_top.setdefault(n, []).append(d[j])
mx = np.array(mx)
log(f"\n== reality check (monthly Sharpe gain vs the live rule, best of {N}): observed best gain "
    f"{obs.max() * math.sqrt(12):+.3f}/yr; p-value of the best after searching everything = {(mx >= obs.max()).mean():.3f}")
for n in top:
    a = np.array(dist_top[n])
    log(f"  {n:<28} gain {obs[res.index.get_loc(n)] * math.sqrt(12):+.3f}  share of bootstrap draws with gain <= 0: {(a <= 0).mean():.3f}")

open(os.path.join(HERE, "log.txt"), "w").write("\n".join(OUT))
pickle.dump({"names": names, "R": Rm, "EQ": EQ, "grid": grid, "rf": rfv, "mkt": mv}, open(os.path.join(HERE, "grid.pkl"), "wb"))
