"""Research (not used by the page): de-risking with market-trend confirmation. Run: python3 macro/research_trend.py"""
import sys, warnings, math; sys.path.insert(0, "."); warnings.filterwarnings("ignore")
import numpy as np, pandas as pd
from macro import research_derisk as RD
d, grid, sc, val, lvl, rf = RD.load()
m = lvl.pct_change(fill_method=None)
ids, early, confirm = RD.groups("core28")
ev = RD.event(lvl, 0.15, 12)
w = RD.weights(sc, ids, ev, 12, "lift")
share = RD.share(sc, w, ids)
g = ((share - 0.15) / 0.20).clip(0, 1)                   # 0..1 graded warning strength
tr10 = (val["spx_trend"] < 0).fillna(False)             # S&P below its 10-month average
ma6 = lvl / lvl.rolling(6).mean() - 1
tr6 = (ma6 < 0).fillna(False)
dd12 = (lvl / lvl.rolling(12).max() - 1)
tr_dd5 = (dd12 <= -0.05).fillna(False)
on33 = share >= 1 / 3
on30 = share >= 0.30
on25 = share >= 0.25
R = {}
R["live 3.1: one switch 1/3, equal votes"] = np.where(RD.share(sc, RD.weights(sc, ids, ev, 12, "equal"), ids) >= 1/3, 0.5, 1.0)
R["current 3.2: graded + track-record"] = 1 - 0.5 * g
R["one switch 1/3 + track-record (option 1)"] = np.where(on33, 0.5, 1.0)
for nm, tr in (("10-month avg", tr10), ("6-month avg", tr6), ("5% off 12-month high", tr_dd5)):
    R[f"graded, cut only if S&P below {nm}"] = np.where(tr, 1 - 0.5 * g, 1.0)
    R[f"graded, max 10% cut unless S&P below {nm}"] = np.where(tr, 1 - 0.5 * g, 1 - 0.1 * g)
    R[f"graded, max 25% cut unless S&P below {nm}"] = np.where(tr, 1 - 0.5 * g, 1 - 0.25 * g)
    for t, on in (("1/3", on33), ("0.30", on30), ("0.25", on25)):
        R[f"switch {t} AND S&P below {nm}"] = np.where(on & tr, 0.5, 1.0)
        R[f"switch {t} -> 80%, + S&P below {nm} -> 50%"] = np.where(on & tr, 0.5, np.where(on, 0.8, 1.0))
R["trend only (S&P below 10-month avg)"] = np.where(tr10, 0.5, 1.0)

def evaluate(e, start, end=None):
    e = pd.Series(e, index=grid, dtype=float)
    r = e.shift(1) * m + (1 - e.shift(1)) * rf
    sel = (grid > pd.Period(start, "M")) & ((grid <= pd.Period(end, "M")) if end else True)
    rr, mm = r[sel].dropna(), m[sel].dropna()
    def st(x):
        lv = (1 + x).cumprod(); y = len(x) / 12
        return (lv.iloc[-1] ** (1 / y) - 1) * 100, ((lv / lv.cummax()) - 1).min() * 100, (x - rf.reindex(x.index)).mean() / x.std() * math.sqrt(12)
    c, dd, sh = st(rr)
    # episodes: runs of months with part in cash; diff = rule minus S&P over the months held
    cut = (e < 1 - 1e-9).values
    idx = np.where(sel)[0]
    i, prot, lost, npos, nneg = idx[0] - 1, 0.0, 0.0, 0, 0
    while i < idx[-1]:
        if cut[i]:
            j = i
            while j + 1 < idx[-1] and cut[j + 1]: j += 1
            h = slice(i + 1, j + 2)
            dlt = ((1 + r.iloc[h]).prod() - (1 + m.iloc[h]).prod()) * 100
            if dlt >= 1: prot += dlt; npos += 1
            elif dlt <= -1: lost += dlt; nneg += 1
            i = j + 1
        else:
            i += 1
    return c, dd, sh, prot, npos, lost, nneg, e.shift(1)[sel].mean() * 100

sp = {k: evaluate(np.ones(len(grid)), *v) for k, v in {"1975-2026": ("1975-01",), "2006-2026": ("2006-08",), "1975-2000": ("1975-01", "2000-12"), "2001-2026": ("2000-12",)}.items()}
print("S&P 500:", "; ".join(f"{k} {v[0]:.1f}%/yr worst {v[1]:.0f}% Sharpe {v[2]:.2f}" for k, v in sp.items()))
rows = []
for nm, e in R.items():
    out = {k: evaluate(e, *v) for k, v in {"all": ("1975-01",), "06": ("2006-08",), "h1": ("1975-01", "2000-12"), "h2": ("2000-12",)}.items()}
    rows.append((nm, out))
def show(nm, o):
    a, s6, h1, h2 = o["all"], o["06"], o["h1"], o["h2"]
    print(f"{nm[:52]:52s} | 1975+: {a[0]:4.1f}%/yr worst {a[1]:4.0f}% Sh {a[2]:.2f} | protected +{a[3]:3.0f} pts in {a[4]:2d}, lost {a[5]:4.0f} pts in {a[6]:2d}, avg stocks {a[7]:3.0f}%"
          f" | 2006+: {s6[0]:4.1f}% worst {s6[1]:4.0f}% | halves Sharpe {h1[2]:.2f}/{h2[2]:.2f}")
for nm, o in rows: show(nm, o)
