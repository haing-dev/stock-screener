"""Exp 4 (pre-registered 2026-10-29 after Exp 1-3; layer options = only the ones that did not lose in either half):
 E exposure: E0 live 4.1 | E1 + squeeze cut to 0 | E2 + melt-up cut to 0 | E3 E1+E2 | E4 E3 + midterm May-Sep cut 50%
 D non-stock: D0 live | D7 long T only if 10y >= Fed funds | D6 2y instead of bills (1976+)
 X sleeve: X0 none | X1 20% gold when CPI>3% and gold above 10m avg | X2 20% commodities when CPI>3% and commodity
           index above 10m avg | X3 10% + 10%
 L equity location (equity part): L0 S&P | L1 China cycle up -> 50% Korea/Taiwan/China | L2 commodity boom -> 50%
           exporters | L3 L1+L2 (25% each when both) | L4 sector momentum top/bottom 5 (1.5x/0.5x) while 100% invested
 Countries enter only where their data exist (else S&P). Windows 1975-2000 | 2001-2026 | 1975-2026, plus 1997-2026.
 Overfitting checks: CSCV PBO over all variants; bootstrap of the best vs live; neighbours."""
import itertools
import pickle

from base import *  # noqa
from exp_exp import C
from exp_loc import china_up, com_boom, EXPORTERS

hot = (cpi_yy > 3).fillna(False)
gold_up = above_ma("gold").fillna(False)
com_up = above_ma("commod").fillna(False)
E_ = {"E0": e41,
      "E1": np.minimum(e41, pd.Series(np.where(C["squeeze"], 0.0, 1.0), index=grid)),
      "E2": np.minimum(e41, pd.Series(np.where(C["meltup"], 0.0, 1.0), index=grid))}
E_["E3"] = np.minimum(E_["E1"], E_["E2"])
E_["E4"] = np.minimum(E_["E3"], pd.Series(np.where(C["midterm"], 0.5, 1.0), index=grid))
g_l = gtt & cneg
D_ = {"D0": {"t30y": g_l}, "D7": {"t30y": g_l & curve_ok}, "D6": {"t30y": g_l, "t2y": ~g_l}}
X_ = {"X0": {}, "X1": {"gold": 0.2 * (hot & gold_up)}, "X2": {"commod": 0.2 * (hot & com_up)},
      "X3": {"gold": 0.1 * (hot & gold_up), "commod": 0.1 * (hot & com_up)}}
CH = ["eq_korea", "eq_taiwan", "eq_hongkong"]


def have(cols):
    return R[cols].shift(-1).notna().all(axis=1) | (pd.Series(range(T), index=grid) == T - 1)


ch_ok = china_up & have(CH)
ex_ok = com_boom & have(EXPORTERS)
# sector momentum active weights relative to the S&P (as in the 3.x research)
rets = P["rets"]
import sys
sys.path.insert(0, "/home/claude/stock-screener")
from macro import engine as EN  # noqa
mo = EN.cumret(rets, 12).shift(1)
rk = mo.rank(axis=1, ascending=False)
nav = mo.notna().sum(axis=1)
sig = pd.DataFrame("neutral", index=grid, columns=rets.columns)
sig[rk <= 5] = "over"
sig[rk.gt(nav - 5, axis=0)] = "under"
avail = rets.shift(-1).notna()
w_eq = EN.tilt_weights(pd.DataFrame("neutral", index=grid, columns=rets.columns), avail)
w_m = EN.tilt_weights(sig, avail)
DW = (w_m - w_eq).fillna(0.0)                              # active sector weights, sum 0


def build(e, d, x, l):
    W = pd.DataFrame(0.0, index=grid, columns=["spx"])
    xs = sum((v.astype(float) for v in x.values()), pd.Series(0.0, index=grid)) if x else pd.Series(0.0, index=grid)
    eq = e * (1 - xs)                                        # sleeve taken pro rata from the whole book
    rest = (1 - e) * (1 - xs)
    for a, w in d.items():
        W[a] = W.get(a, 0.0) + rest * w.astype(float)
    for a, w in x.items():
        W[a] = W.get(a, 0.0) + w.astype(float)
    if l == "L0":
        W["spx"] = eq
    elif l in ("L1", "L2", "L3"):
        c1 = ch_ok.astype(float) if l in ("L1", "L3") else 0.0
        c2 = ex_ok.astype(float) if l in ("L2", "L3") else 0.0
        s1 = 0.5 * c1 if l == "L1" else 0.25 * c1 if l == "L3" else 0.0
        s2 = 0.5 * c2 if l == "L2" else 0.25 * c2 if l == "L3" else 0.0
        W["spx"] = eq * (1 - s1 - s2)
        for c in CH:
            W[c] = eq * s1 / len(CH)
        for c in EXPORTERS:
            W[c] = W.get(c, 0.0) + eq * s2 / len(EXPORTERS)
    elif l == "L4":
        W["spx"] = eq
        full = (e > 1 - 1e-9).astype(float) * eq
        for c in DW.columns:
            W["sec_" + c] = DW[c] * full
    return W


names, cols = [], []
for (ek, e), (dk, d), (xk, x), lk in itertools.product(E_.items(), D_.items(), X_.items(), ("L0", "L1", "L2", "L3", "L4")):
    nm = f"{ek}-{dk}-{xk}-{lk}"
    r = run(build(e, d, x, lk))
    names.append(nm)
    cols.append(r)
RR = pd.concat(cols, axis=1, keys=names)
WALL = WIN_LONG + (("1997-02", "2026-10"),)


def st_all(r):
    out = []
    for a, b in WALL:
        s = stats(r, a, b)
        out += [s["cagr"], s["dd"], s["sh"]]
    return out


tab = pd.DataFrame([st_all(RR[n]) for n in names], index=names,
                   columns=[f"{w}_{m}" for w in ("A", "B", "F", "S") for m in ("cagr", "dd", "sh")])
base_ = tab.loc["E0-D0-X0-L0"]
tab["dA"] = tab["A_sh"] - base_["A_sh"]
tab["dB"] = tab["B_sh"] - base_["B_sh"]
tab["worst"] = tab[["dA", "dB"]].min(axis=1)
tab.to_csv("combo_results.csv")
pd.set_option("display.width", 250)
print("live:", base_.round(2).to_dict())
print("\n== top 25 by the worse half's Sharpe gain vs live (worst fall within 3 pts of live in both halves)")
ok = tab[(tab["A_dd"] >= base_["A_dd"] - 3) & (tab["B_dd"] >= base_["B_dd"] - 3)]
print(ok.sort_values("worst", ascending=False).head(25).round(2).to_string())
print("\n== top 15 by full-period CAGR (worst fall >= -25%)")
print(tab[tab["F_dd"] >= -25].sort_values("F_cagr", ascending=False).head(15).round(2).to_string())
# layer effects
fac = pd.DataFrame([n.split("-") for n in names], index=names, columns=["E", "D", "X", "L"])
t2 = tab.join(fac)
print("\n== average effect of each choice (Sharpe pts fit/check half; CAGR full), all else equal")
for lay, b0 in (("E", "E0"), ("D", "D0"), ("X", "X0"), ("L", "L0")):
    oth = [c for c in ("E", "D", "X", "L") if c != lay]
    key = t2[oth].agg("|".join, axis=1)
    bm = t2[t2[lay] == b0].assign(k=key).set_index("k")
    for lev in sorted(t2[lay].unique()):
        if lev == b0:
            continue
        s = t2[t2[lay] == lev]
        bb = bm.loc[key[s.index].values]
        print(f"  {lay}={lev}: dSharpe {np.nanmean(s['A_sh'].values - bb['A_sh'].values):+.3f} / "
              f"{np.nanmean(s['B_sh'].values - bb['B_sh'].values):+.3f}; dCAGR {np.nanmean(s['F_cagr'].values - bb['F_cagr'].values):+.2f}; "
              f"dWorst {np.nanmean(s['F_dd'].values - bb['F_dd'].values):+.1f}; 1997+ dCAGR {np.nanmean(s['S_cagr'].values - bb['S_cagr'].values):+.2f}")
# CSCV PBO
sel = (grid >= Per("1975-02")) & (grid <= Per("2026-10"))
Z = (RR[sel].values - rf[sel].values[:, None])
nb = 16
blocks = np.array_split(np.arange(Z.shape[0]), nb)
bs = np.array([np.nansum(Z[b], axis=0) for b in blocks]); bq = np.array([np.nansum(Z[b] ** 2, axis=0) for b in blocks]); bn = np.array([len(b) for b in blocks])
lam = []
for comb in itertools.combinations(range(nb), nb // 2):
    m = np.zeros(nb, bool); m[list(comb)] = True
    def srs(mask):
        n = bn[mask].sum(); mu = bs[mask].sum(axis=0) / n; return mu / np.sqrt(bq[mask].sum(axis=0) / n - mu ** 2)
    i_, o_ = srs(m), srs(~m); b_ = np.nanargmax(i_); rnk = (o_ < o_[b_]).mean()
    lam.append(rnk)
lam = np.array(lam)
print(f"\nCSCV ({len(names)} variants): probability the in-sample best ranks below the median out of sample = {(lam <= 0.5).mean():.2f}; median OOS rank {np.median(lam):.2f}")
pickle.dump({"RR": RR, "tab": tab}, open("combo.pkl", "wb"))
