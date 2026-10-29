"""Re-validation after the audit (2026-10-29). Fixes: Yahoo month dating, exact month-end Treasury pricing, gold signal
known at t, no gold before 1975, costs 0.2% per 100% traded (sensitivity 0.1/0.3/0.5).
New out-of-sample tests the audit asked for:
 (a) squeeze rebuilt back to 1982 from the trade-weighted dollar (1973+), WTI and the 10y yield, same formula
     (0.5 z(dollar 12m) + 0.25 z(oil 12m) + 0.25 z(10y 12m change), z = value / expanding st.dev., min 36 months),
     scored by expanding percentile (min 60 months). Threshold 80 was set on 1997-2026 evidence -> 1982-1996 is
     out of sample.
 (b) each layer's contribution with and without the others; concentration of gains.
 (c) walk-forward layer selection: each January, keep a layer only if it improved the Sharpe over all past data."""
import lab
lab.COST = 0.002
from base import *  # noqa
import exp_combo as X  # noqa  (uses lab.run -> new cost)
from exp_exp import C

gold_k = S["gold_known"]
gold_up_k = (gold_k > ma(gold_k, 10)).fillna(False)
com_up = above_ma("commod").fillna(False)
h3 = (cpi_yy > 3).fillna(False)
SLEEVE = {"gold": 0.1 * (h3 & gold_up_k), "commod": 0.1 * (h3 & com_up)}

# (a) extended squeeze
tw = csvm = None
import os
raw = "/home/claude/stock-screener/cache/macro/raw/"
def rawm(n):
    s = pd.read_csv(raw + n + ".csv").dropna()
    s = s[pd.to_numeric(s["value"], errors="coerce").notna()]
    return pd.Series(s["value"].astype(float).values, index=pd.to_datetime(s["date"]).dt.to_period("M")).groupby(level=0).last().reindex(grid)
twex = rawm("TWEXMMTH")
dxy = S["px_DX-Y.NYB"]
dol = (dxy / dxy.shift(12) - 1).combine_first(twex / twex.shift(12) - 1) * 100
oil = F["WTISPLC"]
oil12 = (oil / oil.shift(12) - 1) * 100
r12 = gs10 - gs10.shift(12)
z = lambda x: x / x.expanding(min_periods=36).std()
sq_raw = 0.5 * z(dol) + 0.25 * z(oil12) + 0.25 * z(r12)
sq_ext = pctl(sq_raw, 60)
sq_live = sc["squeeze"]
o = sq_live.notna() & sq_ext.notna()
print(f"extended squeeze from {sq_ext.first_valid_index()}; agreement with live score where both exist: corr {sq_ext[o].corr(sq_live[o]):.2f}, both>=80 {((sq_ext>=80)&(sq_live>=80))[o].sum()} of live>=80 {(sq_live>=80)[o].sum()} months")
spx_l = lvl(R["spx"])
melt = (((spx_l / spx_l.shift(12) - 1) > 0.25) & ((gs10 - gs10.shift(12)) > 1.5)).fillna(False)


def book(sq=None, mu=False, sleeve=True, tilt=True, d="D7", sq_th=80):
    e = e41.copy()
    if sq is not None:
        e = np.minimum(e, pd.Series(np.where((sq >= sq_th).fillna(False), 0.0, 1.0), index=grid))
    if mu:
        e = np.minimum(e, pd.Series(np.where(melt, 0.0, 1.0), index=grid))
    return X.build(e, X.D_[d], SLEEVE if sleeve else {}, "L4" if tilt else "L0")


W = (("1975-02", "1981-12"), ("1982-01", "1996-12"), ("1997-01", "2026-10"), ("1975-02", "2026-10"))
print("\n== after fixes, 0.2% cost. CAGR / worst / Sharpe: 1975-81 | 1982-96 (squeeze OOS) | 1997-2026 | 1975-2026")
print(line("S&P 500", R["spx"], W))
r_live = run(W41)
print(line("live 4.1", r_live, W))
V = {"live + extended squeeze": book(sq_ext, sleeve=False, tilt=False, d="D0"),
     "live + live squeeze (from 1997)": book(sq_live, sleeve=False, tilt=False, d="D0"),
     "live + melt-up": book(None, True, sleeve=False, tilt=False, d="D0"),
     "live + sleeve": book(None, False, True, False, "D0"),
     "live + sector tilt": book(None, False, False, True, "D0"),
     "live + D7": book(None, False, False, False, "D7"),
     "c5 (live squeeze)": book(sq_live, True),
     "c5 with extended squeeze": book(sq_ext, True),
     "c5 ext, no melt-up": book(sq_ext, False),
     "c5 ext, no sleeve": book(sq_ext, True, False),
     "c5 ext, no tilt": book(sq_ext, True, True, False),
     "tilt + sleeve only (no new cuts)": book(None, False, True, True)}
RES = {}
for k, w in V.items():
    RES[k] = run(w)
    print(line(k, RES[k], W))
for th in (70, 75, 85, 90):
    print(line(f"live + extended squeeze >= {th}", run(book(sq_ext, sleeve=False, tilt=False, d="D0", sq_th=th)), W))
print("\n== cost sensitivity (1975-2026 CAGR): live / c5-ext")
for c in (0.001, 0.002, 0.003, 0.005):
    print(f"  {c:.1%}: {stats(run(W41, cost=c))['cagr']:.1f} / {stats(run(V['c5 with extended squeeze'], cost=c))['cagr']:.1f}")
lab.COST = 0.002
# (b) concentration
d_ = (RES["c5 with extended squeeze"] - r_live)[grid >= Per("1975-02")]
top = d_.sort_values(ascending=False)
print(f"\nconcentration: best 10 months of (c5ext - live) = {top.iloc[:10].sum() / d_.sum():.0%} of the total gain; "
      f"months: {', '.join(str(p) for p in top.index[:10])}")
# squeeze OOS episodes 1982-1996
on = (sq_ext >= 80) & (grid <= Per("1996-12")) & (grid >= Per("1982-01"))
print("extended squeeze >= 80 in 1982-96:", ", ".join(str(p) for p in grid[on.fillna(False).values]))
# (c) walk-forward layer selection
layers = {"sq": lambda: (sq_ext >= 80).fillna(False), "mu": lambda: melt}
lab_r = {}
choice = []
r_wf = pd.Series(np.nan, index=grid)
combos = {(a, b): run(book(sq_ext if a else None, b)) for a in (0, 1) for b in (0, 1)}
for t in range(T):
    p = grid[t]
    if p.month == 1 or t == 0:
        past = (grid < p) & (grid >= Per("1975-02"))
        best, bsh = (0, 0), -9
        for k_, r_ in combos.items():
            x = r_[past].dropna()
            if len(x) < 60:
                continue
            s_ = (x - rf[past][x.index]).mean() / x.std()
            if s_ > bsh + 0.01 or (k_ == (0, 0) and bsh == -9):
                best, bsh = k_, s_
        cur = best
    choice.append(cur)
    r_wf.iloc[t] = combos[cur].iloc[t]
print(line("walk-forward choice of the two cuts (yearly)", r_wf, W))
print("  layers chosen in Jan of: " + ", ".join(f"{grid[t].year}:{choice[t]}" for t in range(T) if grid[t].month == 1 and grid[t].year % 5 == 0 and grid[t].year >= 1980))
