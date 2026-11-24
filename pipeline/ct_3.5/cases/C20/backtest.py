"""Short-horizon rates trend pod (synthetic test pod).

python backtest.py    # prints the REPORT.md figures
"""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_lib"))
import synth  # noqa: E402

RATES = ["bd_us10", "bd_de10", "bd_jp10", "bd_uk10", "bd_ca10", "bd_au10", "st_us2", "st_de2"]
LOOK = 2
PER_MARKET = 0.06
VOL_N, VOL_MIN = 36, 24
FI_BP = 1.0
PERIOD = ("1975-01", "2010-12")


def pod_returns(R, cost_mult=1.0):
    direction = np.sign(R.rolling(LOOK, min_periods=LOOK).sum())
    risk = R.rolling(VOL_N, min_periods=VOL_MIN).std() * np.sqrt(12)
    size = direction * PER_MARKET / risk
    n_live = size.notna().sum(axis=1)
    size = size.div(np.sqrt(n_live.where(n_live > 0)), axis=0).fillna(0.0)
    earned = size.shift(1).mul(R).sum(axis=1, min_count=1).fillna(0.0)
    paid = size.diff().abs().sum(axis=1).shift(1).fillna(0.0) * FI_BP / 1e4 * cost_mult
    return pd.DataFrame({"gross": earned, "cost": paid, "net": earned - paid})


def describe(name, r):
    print("%-14s SR %5.2f  mean %5.2f%%  vol %5.2f%%  maxDD %6.1f%%" % (
        name, synth.sharpe(r), 1200 * r.mean(), 100 * np.sqrt(12) * r.std(), 100 * synth.max_drawdown(r)))


if __name__ == "__main__":
    R = synth.make_panel()["R"][RATES]
    lo, hi = PERIOD
    a = pod_returns(R).loc[lo:hi]
    b = pod_returns(R, 2.0).loc[lo:hi]
    print("period %s..%s (%d months)" % (a.index[0].strftime("%Y-%m"), a.index[-1].strftime("%Y-%m"), len(a)))
    describe("net", a["net"])
    describe("gross", a["gross"])
    describe("net 2x costs", b["net"])
    describe("net 1975-1992", a["net"].loc["1975":"1992"])
    describe("net 1993-2010", a["net"].loc["1993":"2010"])
    print("costs %.2f%%/yr" % (1200 * a["cost"].mean()))
