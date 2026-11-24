"""Relative value between close substitutes, two versions averaged (synthetic test pod).

python backtest.py  -> headline, gross, double-cost, era and cost lines for REPORT.md
"""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_lib"))
import synth  # noqa: E402

PAIRS = (("bd_us10", "bd_ca10"), ("bd_de10", "bd_uk10"), ("eq_de", "eq_fr"),
         ("fx_aud", "fx_nzd"), ("cm_wti", "cm_brent"), ("cm_gold", "cm_silver"), ("cm_corn", "cm_soy"))
ANCHORS = (1, 6)                 # version 1: last month's spread move; version 2: gap to the 6-month mean
BP = {"eq": 2.0, "bd": 1.0, "st": 1.0, "fx": 2.0, "cm": 4.0}
RISK_PER_PAIR = 0.10
WIN = slice("1975-01", "2010-12")
ERAS = {"1975-1992": slice("1975-01", "1992-12"), "1993-2010": slice("1993-01", "2010-12")}


def annual_vol(x, n=36, m=24):
    return x.rolling(n, min_periods=m).std() * np.sqrt(12)


def pair_frame(R, a, b):
    va, vb = annual_vol(R[a]), annual_vol(R[b])
    u = R[a] / va.shift(1) - R[b] / vb.shift(1)
    su = annual_vol(u)
    lvl = u.cumsum()
    units = []
    for n in ANCHORS:
        gap = u if n == 1 else lvl - lvl.rolling(n).mean()
        z = np.clip(gap / (su / np.sqrt(12)), -2.0, 2.0)
        units.append(-z / 2.0)
    units = pd.concat(units, axis=1).mean(axis=1, skipna=False) * RISK_PER_PAIR / su
    return pd.DataFrame({"units": units, "na": 1.0 / va, "nb": -1.0 / vb})


def run(R, cost_mult=1.0):
    frames = {p: pair_frame(R, *p) for p in PAIRS}
    live = pd.concat([f["units"].notna() for f in frames.values()], axis=1).sum(axis=1)
    k = 1.0 / np.sqrt(live.where(live > 0))
    gross = pd.Series(0.0, index=R.index)
    cost = pd.Series(0.0, index=R.index)
    for (a, b), f in frames.items():
        u = (f["units"] * k).fillna(0.0)
        pa, pb = (u * f["na"]).fillna(0.0), (u * f["nb"]).fillna(0.0)
        gross += pa.shift(1) * R[a].fillna(0.0) + pb.shift(1) * R[b].fillna(0.0)
        cost += u.shift(1).diff().abs().fillna(0.0) * (BP[a[:2]] + BP[b[:2]]) / 1e4
    net = gross - cost_mult * cost
    return pd.DataFrame({"gross": gross, "cost": cost * cost_mult, "net": net})[WIN]


def fmt(r):
    return "SR %5.2f  mean %5.2f%%  vol %5.2f%%  maxDD %6.1f%%" % (
        synth.sharpe(r), r.mean() * 1200, r.std() * np.sqrt(12) * 100, synth.max_drawdown(r) * 100)


if __name__ == "__main__":
    R = synth.make_panel()["R"]
    res, res2 = run(R), run(R, 2.0)
    print("sample", res.index[0].strftime("%Y-%m"), "to", res.index[-1].strftime("%Y-%m"), "|", len(res), "months")
    print("net          ", fmt(res["net"]))
    print("gross        ", fmt(res["gross"]))
    print("net 2x costs ", fmt(res2["net"]))
    for name, s in ERAS.items():
        print("net", name, "", fmt(res["net"][s]))
    print("costs %.2f%%/yr" % (res["cost"].mean() * 1200))
