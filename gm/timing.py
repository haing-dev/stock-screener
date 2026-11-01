"""Trade-timing test: how much of the book's return depends on trading exactly at month end?

Positions are decided from month-end data at the end of month t (as always). They are then applied k trading days
late: the month's P&L runs from trading day k+1 after the month end to trading day k after the next month end.
k = 0 is the normal book. Only markets with free daily data are used (same subset for every k), price moves only
(carry and dividends accrue whatever the timing). Design periods only.

python -m gm.timing
"""
import os
import pickle

import numpy as np
import pandas as pd

from . import book as B
from . import config as CF
from . import daily as DL
from . import panel as P
from . import stats as ST

DELAYS = (0, 1, 3, 5, 10)


def delayed_pnl(pos, D, k):
    """pos: monthly positions (PeriodIndex, decided at month end). D: daily returns. Returns monthly P&L series."""
    D = D.fillna(0.0)
    days = D.index
    m_end = pd.Series(days, index=days).groupby(days.to_period("M")).max()   # last trading day per month
    loc = {p: days.get_loc(d) for p, d in m_end.items()}
    cols = [c for c in pos.columns if c in D.columns]
    cum = D[cols].cumsum()
    out = {}
    for t in pos.index:
        if t not in loc or (t + 1) not in loc:
            continue
        i0, i1 = loc[t] + k, loc[t + 1] + k
        if i1 >= len(days):
            continue
        move = cum.iloc[i1] - cum.iloc[i0]
        out[t + 1] = float((pos.loc[t, cols].fillna(0) * move).sum())
    return pd.Series(out)


def grid(cfg, D=None, R=None, label=""):
    R = R if R is not None else pickle.load(open(os.path.join(P.OUT, "panel.pkl"), "rb"))["R"]
    D = D if D is not None else DL.build()
    res = B.run(R, cfg=cfg, daily=D)
    rows = []
    books = {"book": res["pos"]}
    books.update({f: v for f, v in res["fam_pos"].items()})
    for name, pos in books.items():
        line = {"variant": label, "part": name}
        for k in DELAYS:
            pnl = delayed_pnl(pos, D, k)
            line["SR k=%d (1990-2010)" % k] = round(ST.sharpe(ST.cut(pnl, *ST.DESIGN)), 2)
            line["SR k=%d (2000-10)" % k] = round(ST.sharpe(ST.cut(pnl, "2000-01", "2010-12")), 2)
        rows.append(line)
    return pd.DataFrame(rows)


def main():
    R = pickle.load(open(os.path.join(P.OUT, "panel.pkl"), "rb"))["R"]
    D = DL.build()
    print("daily coverage: %d markets" % D.shape[1])
    out = []
    for label, cfg in (("BASE 1/3/12 sign", CF.BASE),
                       ("BASE slow 6/12", CF.variant(CF.BASE, trend={"horizons": (6, 12)})),
                       ("CAND 1/3/12 cont", CF.CANDIDATE),
                       ("CAND slow 6/12", CF.variant(CF.CANDIDATE, trend={"horizons": (6, 12)}))):
        out.append(grid(cfg, D, R, label))
    df = pd.concat(out)
    pd.set_option("display.width", 250)
    print(df.to_string(index=False))
    return df


if __name__ == "__main__":
    main()
