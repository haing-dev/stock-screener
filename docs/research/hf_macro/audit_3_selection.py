"""Audit 3: selection bias. (a) walk-forward choice among the 300 Exp-4 variants, (b) deflated Sharpe of the gain
over live, (c) the squeeze/melt-up modes and thresholds as picked in Exp 3 vs alternatives, out of sample."""
import itertools
import math
import pickle

import numpy as np
import pandas as pd
from scipy import stats as st
from audit_lib import *  # noqa

C = pickle.load(open(os.path.join(HERE, "combo.pkl"), "rb"))
RR, tab = C["RR"], C["tab"]
r0 = live()
r5 = RR["E3-D7-X3-L4"]
names = list(RR.columns)
print(f"variants: {len(names)}; candidate rank by full-period CAGR: "
      f"{int((tab['F_cagr'] > tab.loc['E3-D7-X3-L4','F_cagr']).sum()) + 1}; by full Sharpe "
      f"{int((tab['F_sh'] > tab.loc['E3-D7-X3-L4','F_sh']).sum()) + 1}")

# (a) walk-forward: each January pick the variant with the best Sharpe from 1975-02 to the previous December
ex = RR.sub(rf, axis=0)
start = Per("1975-02")
out = pd.Series(np.nan, index=grid)
picks = {}
for yr in range(1985, 2027):
    a, b = start, Per(f"{yr - 1}-12")
    m = (grid >= a) & (grid <= b)
    sh = ex[m].mean() / RR[m].std()
    best = sh.idxmax()
    picks[yr] = best
    mm = (grid >= Per(f"{yr}-01")) & (grid <= Per(f"{yr}-12"))
    out[mm] = RR.loc[mm, best]
print("\n== walk-forward selection among the 300 variants (re-picked every January by past Sharpe since 1975)")
for a, b in (("1985-01", "2026-10"), ("1997-01", "2026-10"), ("2001-01", "2026-10")):
    print(f"  {a}..{b}: walk-forward {stats(out, a, b)['cagr']:.2f}% Sharpe {stats(out, a, b)['sh']:.2f} | "
          f"candidate 5.0 {stats(r5, a, b)['cagr']:.2f}% {stats(r5, a, b)['sh']:.2f} | live {stats(r0, a, b)['cagr']:.2f}% "
          f"{stats(r0, a, b)['sh']:.2f} | S&P {stats(R0['spx'], a, b)['cagr']:.2f}%")
chg = [(y, p) for i, (y, p) in enumerate(picks.items()) if i == 0 or p != list(picks.values())[i - 1]]
print("  picks (year: variant, when it changes):", chg)

# (b) deflated Sharpe of the active return (candidate - live) given the number of variants tried
m = (grid >= Per("1975-02")) & (grid <= Per("2026-10"))
act = RR[m].sub(r0[m], axis=0)
ir = act.mean() / act.std()              # monthly IR of every variant vs live
ir = ir.drop("E0-D0-X0-L0").dropna()
print("  IR across variants: mean %.3f sd %.3f n %d" % (ir.mean(), ir.std(), len(ir)))
x = act["E3-D7-X3-L4"]
Tn = len(x)
sr = x.mean() / x.std()
g3, g4 = st.skew(x), st.kurtosis(x, fisher=False)
emc = 0.5772156649


def dsr(sr, sr_var, N, Tn, g3, g4):
    sr0 = math.sqrt(sr_var) * ((1 - emc) * st.norm.ppf(1 - 1 / N) + emc * st.norm.ppf(1 - 1 / (N * math.e)))
    z = (sr - sr0) * math.sqrt(Tn - 1) / math.sqrt(1 - g3 * sr + (g4 - 1) / 4 * sr ** 2)
    return sr0, st.norm.cdf(z)


print(f"\n== deflated Sharpe of the gain over live (monthly IR {sr:.3f} = {sr*math.sqrt(12):.2f}/yr, skew {g3:.2f}, kurt {g4:.1f})")
print(f"  naive p(IR>0): {st.norm.cdf(sr * math.sqrt(Tn - 1) / math.sqrt(1 - g3 * sr + (g4 - 1) / 4 * sr ** 2)):.4f}")
# effective number of independent trials from the eigenvalues of the variant correlation matrix
aa = act.drop(columns=["E0-D0-X0-L0"]).dropna(axis=1)
aa = aa.loc[:, aa.std() > 1e-12]
print(f"  variants with full data and non-zero gain: {aa.shape[1]}")
cm = np.corrcoef(aa.values.T)
ev = np.linalg.eigvalsh(cm)
n_eff = (ev.sum() ** 2) / (ev ** 2).sum()
for N, lab_ in ((299, "Exp 4 grid (299)"), (299 + 42 + 9 + 9, "Exp 2-4 (~360)"), (max(2, round(n_eff)), f"effective N from correlations ({n_eff:.1f})")):
    sr0, p = dsr(sr, ir.var(), N, Tn, g3, g4)
    print(f"  N={N:4d} {lab_:38s}: expected max IR under no skill {sr0*math.sqrt(12):.2f}/yr -> DSR prob {p:.3f}")

# (c) halves: was the squeeze/melt-up mode picked on the same data? test the choice on each half separately
print("\n== Exp 3 mode choice per half (Sharpe): 1975-2000 | 2001-2026")
for k in ("squeeze", "meltup"):
    for mode in ("gate", "cut50", "cut0"):
        c = X.C[k]
        if mode == "gate":
            e = X.exposure(gate=X.fed | c)
        else:
            e = np.minimum(X.e41, pd.Series(np.where(c, 0.5 if mode == "cut50" else 0.0, 1.0), index=grid))
        r = run(X.W_from(e, X.live_def))
        print(f"  {k:8s} {mode:6s}: {stats(r, '1975-02', '2000-12')['sh']:.2f} | {stats(r, '2001-01', '2026-10')['sh']:.2f}")
print("  live           : %.2f | %.2f" % (stats(r0, '1975-02', '2000-12')['sh'], stats(r0, '2001-01', '2026-10')['sh']))
pickle.dump({"wf": out, "picks": picks}, open(os.path.join(HERE, "audit_wf.pkl"), "wb"))
