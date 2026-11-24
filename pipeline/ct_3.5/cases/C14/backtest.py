"""Rates and currencies trend pod (synthetic test pod).

python backtest.py
"""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_lib"))
import synth  # noqa: E402

SPEC = dict(
    classes=("FI", "FX"),
    horizons=(3, 12),
    risk=0.10,
    vol=(36, 24),
    bp={"FI": 1.0, "FX": 2.0},
    window=("1975-01", "2010-12"),
    eras=(("1975-01", "1992-12"), ("1993-01", "2010-12")),
)


def build(panel):
    R = panel["R"]
    cols = [k for k in R.columns if panel["CLASS"][k] in SPEC["classes"]]
    R = R[cols]
    n, m = SPEC["vol"]
    vol = R.rolling(n, min_periods=m).std() * np.sqrt(12)
    score = sum(np.sign(R.rolling(h, min_periods=h).sum()) for h in SPEC["horizons"]) / len(SPEC["horizons"])
    pos = score * SPEC["risk"] / vol
    live = pos.notna().sum(axis=1)
    pos = pos.div(np.sqrt(live.where(live > 0)), axis=0).fillna(0.0)
    bp = pd.Series({k: SPEC["bp"][panel["CLASS"][k]] / 1e4 for k in cols})
    return R, pos, bp


def returns(R, pos, bp, cost_mult=1.0):
    held = pos.shift(1)
    gross = held.mul(R.fillna(0.0)).sum(axis=1)
    cost = held.diff().abs().mul(bp).sum(axis=1) * cost_mult
    return gross, cost, gross - cost


def row(label, r):
    print("%-16s SR %5.2f  mean %5.2f%%  vol %5.2f%%  maxDD %6.1f%%" % (
        label, synth.sharpe(r), r.mean() * 1200, r.std() * np.sqrt(12) * 100, synth.max_drawdown(r) * 100))


if __name__ == "__main__":
    R, pos, bp = build(synth.make_panel())
    a, b = SPEC["window"]
    gross, cost, net = (s.loc[a:b] for s in returns(R, pos, bp))
    net2 = returns(R, pos, bp, 2.0)[2].loc[a:b]
    print("window %s..%s (%d months)" % (net.index[0].strftime("%Y-%m"), net.index[-1].strftime("%Y-%m"), len(net)))
    row("net", net)
    row("gross", gross)
    row("net 2x costs", net2)
    for lo, hi in SPEC["eras"]:
        row("net %s-%s" % (lo[:4], hi[:4]), net.loc[lo:hi])
        row("gross %s-%s" % (lo[:4], hi[:4]), gross.loc[lo:hi])
    print("costs %.2f%%/yr" % (cost.mean() * 1200))
    yr = net.groupby(net.index.year).sum()
    print("best year %d %+.1f%%, worst year %d %+.1f%%" % (yr.idxmax(), yr.max() * 100, yr.idxmin(), yr.min() * 100))
