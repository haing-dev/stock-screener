"""Strategy lab: monthly weights over instruments (decided at the end of month t, earned in t+1), costs, stats."""
import math
import os
import pickle

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
D = pickle.load(open(os.path.join(HERE, "rpanel.pkl"), "rb"))
grid, R, S, rf, P = D["grid"], D["R"], D["S"], D["rf"], D["P"]
T = len(grid)
Per = lambda s: pd.Period(s, "M")
COST = 0.001            # 0.10% per 100% of the portfolio traded
FEE = {"trend": 0.015 / 12, "trend_cm": 0.015 / 12, "commod": 0.006 / 12, "usd": 0.0, "gold": 0.0025 / 12}


def run(W, cost=None, name=""):
    """W: DataFrame (grid x assets) of weights (cash = 1 - sum, earns T-bills). Returns monthly net return Series."""
    cost = COST if cost is None else cost
    W = W.reindex(grid).fillna(0.0)
    cols = list(W.columns)
    A = R.reindex(columns=[c for c in cols if c != "tbill"]).copy()
    for c, f in FEE.items():
        if c in A:
            A[c] = A[c] - f
    Wh = W.shift(1).fillna(0.0)
    miss = A.isna() & (Wh[A.columns] != 0)
    r = (Wh[A.columns] * A.fillna(0)).sum(axis=1) + (1 - Wh.sum(axis=1)) * rf
    if "tbill" in W:
        pass                                               # tbill weight is part of 1 - sum handled as cash
    r[miss.any(axis=1)] = np.nan                           # a held asset without data -> month not valid
    turn = W.diff().abs().sum(axis=1).shift(1).fillna(0)
    return r - cost * turn


def stats(r, a="1975-02", b="2026-10"):
    m = (grid >= Per(a)) & (grid <= Per(b))
    x = r[m]
    if x.isna().any() or len(x) < 24:
        return dict(cagr=np.nan, dd=np.nan, sh=np.nan, vol=np.nan, n=int(x.notna().sum()))
    f = rf[m]
    lv = np.r_[1, (1 + x.values).cumprod()]
    return dict(cagr=(lv[-1] ** (12 / len(x)) - 1) * 100, dd=(lv / np.maximum.accumulate(lv) - 1).min() * 100,
                sh=(x - f).mean() / x.std() * math.sqrt(12), vol=x.std() * math.sqrt(12) * 100, n=len(x))


WIN_LONG = (("1975-02", "2000-12"), ("2001-01", "2026-10"), ("1975-02", "2026-10"))
WIN_SHORT = (("1997-02", "2011-12"), ("2012-01", "2026-10"), ("1997-02", "2026-10"))


def line(nm, r, wins=WIN_LONG, width=52):
    out = []
    for a, b in wins:
        s = stats(r, a, b)
        out.append(f"{s['cagr']:5.1f}% {s['dd']:4.0f}% {s['sh']:4.2f}")
    return f"{nm[:width]:<{width}} " + " | ".join(out)


def first_full(cols):
    return max(R[c].first_valid_index() for c in cols if c in R)


def lvl(r):
    return (1 + r.fillna(0)).cumprod()


def ma(x, n):
    return x.rolling(n, min_periods=n).mean()


def mom(c, n=12, skip=0):
    lv_ = lvl(R[c]).where(R[c].notna().cummax())
    return lv_.shift(skip) / lv_.shift(n) - 1


def above_ma(c, n=10):
    lv_ = lvl(R[c]).where(R[c].notna().cummax())
    return lv_ > ma(lv_, n)


def pctl(x, min_n=60):
    """Expanding percentile (0-100) known at t."""
    vals, out = [], []
    for v in x.values:
        if np.isnan(v):
            out.append(np.nan)
            continue
        vals.append(v)
        out.append(np.nan if len(vals) < min_n else (np.asarray(vals) <= v).mean() * 100)
    return pd.Series(out, index=x.index)
