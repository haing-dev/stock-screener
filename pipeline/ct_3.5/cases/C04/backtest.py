"""Cross-sectional momentum across bond and note futures, 12-1 (synthetic test pod).

python backtest.py prints what REPORT.md reports.
"""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_lib"))
import synth  # noqa: E402

LOOKBACK, SKIP = 12, 1
MIN_MARKETS = 3
RISK = 0.10
BP = 1.0
WINDOW = ("1975-01", "2010-12")
ERAS = (("1975-01", "1992-12"), ("1993-01", "2010-12"))


def momentum(R):
    """Sum of monthly returns from t-LOOKBACK+1-SKIP to t-SKIP, known at the close of t."""
    return R.shift(SKIP).rolling(LOOKBACK, min_periods=LOOKBACK).sum()


def rank_weights(m):
    r = m.rank(axis=1)
    r = r.sub(r.mean(axis=1), axis=0)
    w = r.div(r.abs().sum(axis=1), axis=0)
    return w.where(m.notna().sum(axis=1) >= MIN_MARKETS, axis=0)


def backtest(R, cost_mult=1.0):
    vol = R.rolling(36, min_periods=24).std() * np.sqrt(12)
    w = rank_weights(momentum(R))
    pos = (w * RISK / vol * np.sqrt(w.notna().sum(axis=1)).values[:, None]).fillna(0.0)
    held = pos.shift(1)
    gross = (held * R.fillna(0.0)).sum(axis=1)
    cost = held.diff().abs().sum(axis=1) * BP / 1e4 * cost_mult
    out = pd.DataFrame({"gross": gross, "cost": cost, "net": gross - cost})
    return out.loc[WINDOW[0]:WINDOW[1]]


def fmt(r):
    return "SR %5.2f  mean %5.2f%%  vol %5.2f%%  maxDD %6.1f%%" % (
        synth.sharpe(r), r.mean() * 1200, r.std() * np.sqrt(12) * 100, synth.max_drawdown(r) * 100)


if __name__ == "__main__":
    P = synth.make_panel()
    fi = [k for k in P["R"].columns if P["CLASS"][k] == "FI"]
    R = P["R"][fi]
    res, res2 = backtest(R), backtest(R, 2.0)
    print("window %s..%s, %d months, %d markets" % (res.index[0].strftime("%Y-%m"), res.index[-1].strftime("%Y-%m"),
                                                   len(res), len(fi)))
    print("net           " + fmt(res["net"]))
    print("gross         " + fmt(res["gross"]))
    print("net 2x costs  " + fmt(res2["net"]))
    for a, b in ERAS:
        print("net %s-%s " % (a[:4], b[:4]) + fmt(res["net"].loc[a:b]))
    print("costs %.2f%%/yr" % (res["cost"].mean() * 1200))
