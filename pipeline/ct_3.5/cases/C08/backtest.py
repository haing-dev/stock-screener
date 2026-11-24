"""Disinflation rule layer on North American rates (synthetic test pod).

Run `python backtest.py`; REPORT.md quotes its output.
"""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_lib"))
import synth  # noqa: E402

LEGS = ("bd_us10", "bd_ca10", "st_us2")
SHORT_H, LONG_H = 3, 12
LEG_RISK = 0.10
COST_BP_FI = 1.0
SAMPLE = ("1975-01", "2010-12")
ERA_CUTS = (("1975-01", "1992-12"), ("1993-01", "2010-12"))


def inflation_rates(cpi):
    lc = np.log(cpi)
    short = (lc - lc.shift(SHORT_H)) * 1200 / SHORT_H
    long_ = (lc - lc.shift(LONG_H)) * 1200 / LONG_H
    return short, long_


def signal(macro):
    short, long_ = inflation_rates(macro["us_cpi"])
    return ((short < long_) & long_.notna()).astype(float)


def leg_positions(R, on):
    v = R.rolling(36, min_periods=24).std() * np.sqrt(12)
    live = v.notna().sum(axis=1)
    w = (LEG_RISK / v).div(np.sqrt(live.where(live > 0)), axis=0)
    return w.mul(on, axis=0).fillna(0.0)


def simulate(cost_mult=1.0):
    panel = synth.make_panel()
    R = panel["R"][list(LEGS)]
    on = signal(panel["MACRO"])
    pos = leg_positions(R, on)
    pnl = pos.shift(1).mul(R.fillna(0.0)).sum(axis=1)
    tc = pos.diff().abs().sum(axis=1).shift(1) * COST_BP_FI / 1e4
    frame = pd.DataFrame({"gross": pnl, "cost": tc * cost_mult})
    frame["net"] = frame["gross"] - frame["cost"]
    frame["on"] = on.shift(1)
    return frame.loc[SAMPLE[0]:SAMPLE[1]]


def summary(r):
    return "SR %5.2f  mean %5.2f%%  vol %5.2f%%  maxDD %6.1f%%" % (
        synth.sharpe(r), 1200 * r.mean(), 100 * np.sqrt(12) * r.std(), 100 * synth.max_drawdown(r))


if __name__ == "__main__":
    f1, f2 = simulate(), simulate(2.0)
    print("sample %s..%s, %d months, rule on in %d" % (f1.index[0].strftime("%Y-%m"), f1.index[-1].strftime("%Y-%m"),
                                                        len(f1), int(f1["on"].sum())))
    print("net            ", summary(f1["net"]))
    print("gross          ", summary(f1["gross"]))
    print("net, x2 costs  ", summary(f2["net"]))
    for a, b in ERA_CUTS:
        print("net %s-%s      " % (a[:4], b[:4]), summary(f1["net"].loc[a:b]))
    on_r = f1.loc[f1["on"] == 1, "net"]
    print("on months: mean %.2f%%, positive %.0f%%; costs %.2f%%/yr" % (
        100 * on_r.mean(), 100 * (on_r > 0).mean(), 1200 * f1["cost"].mean()))
