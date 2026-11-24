"""Curve reversion pod: 2-year note against 10-year bond, risk matched (synthetic test pod).

Usage: python backtest.py
"""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_lib"))
from synth import make_panel, sharpe, max_drawdown  # noqa: E402

CURVES = {"US": ("st_us2", "bd_us10"), "DE": ("st_de2", "bd_de10")}
MEAN_MONTHS = 3
VOL_MONTHS, VOL_MIN = 36, 24
TARGET = 0.10
ONE_WAY = 1.0e-5
ROLLS_PER_YEAR = 4
FIRST, LAST = "1975-01", "2010-12"
ERAS = (("1975-01", "1992-12"), ("1993-01", "2010-12"))


def curve_positions(R, short_leg, long_leg):
    rs, rl = R[short_leg].to_numpy(), R[long_leg].to_numpy()
    T = len(rs)
    vs = pd.Series(rs).rolling(VOL_MONTHS, min_periods=VOL_MIN).std().to_numpy() * np.sqrt(12)
    vl = pd.Series(rl).rolling(VOL_MONTHS, min_periods=VOL_MIN).std().to_numpy() * np.sqrt(12)
    u = np.full(T, np.nan)
    u[1:] = rs[1:] / vs[:-1] - rl[1:] / vl[:-1]          # steepener-sign unit-risk return of month t
    su = pd.Series(u).rolling(VOL_MONTHS, min_periods=VOL_MIN).std().to_numpy()
    level = np.nancumsum(np.nan_to_num(u))
    level[np.isnan(u)] = np.nan
    mean = pd.Series(level).rolling(MEAN_MONTHS).mean().to_numpy()
    z = np.clip((level - mean) / su, -2, 2)
    k = -z / 2 * TARGET / (su * np.sqrt(12))
    ps, pl = k / vs, -k / vl
    return np.nan_to_num(ps), np.nan_to_num(pl)


def backtest(cost_mult=1.0):
    R = make_panel()["R"]
    idx = R.index
    n_live = np.zeros(len(idx))
    legs = {}
    for cc, (s, l) in CURVES.items():
        ps, pl = curve_positions(R, s, l)
        legs[cc] = (s, l, ps, pl)
        n_live += (np.abs(ps) > 0).astype(float)
    scale = np.where(n_live > 0, 1 / np.sqrt(np.maximum(n_live, 1)), 0.0)
    gross = np.zeros(len(idx))
    cost = np.zeros(len(idx))
    for s, l, ps, pl in legs.values():
        for leg, p in ((s, ps), (l, pl)):
            p = p * scale
            r = np.nan_to_num(R[leg].to_numpy())
            gross[1:] += p[:-1] * r[1:]
            traded = np.abs(np.diff(p))
            cost[2:] += traded[:-1] * ONE_WAY
            cost[1:] += np.abs(p[:-1]) * 2 * ROLLS_PER_YEAR / 12 * ONE_WAY
    out = pd.DataFrame({"gross": gross, "cost": cost * cost_mult}, index=idx)
    out["net"] = out["gross"] - out["cost"]
    return out.loc[FIRST:LAST]


def describe(r):
    return f"SR {sharpe(r):5.2f} | mean {r.mean() * 1200:5.2f}% | vol {r.std() * np.sqrt(12) * 100:5.2f}% | " \
           f"maxDD {max_drawdown(r) * 100:6.1f}%"


if __name__ == "__main__":
    base, double = backtest(), backtest(2.0)
    print(f"{FIRST}..{LAST}: {len(base)} months, first {base.index[0]:%Y-%m}")
    print("net         ", describe(base["net"]))
    print("gross       ", describe(base["gross"]))
    print("net 2x cost ", describe(double["net"]))
    for a, b in ERAS:
        print(f"net {a[:4]}-{b[:4]}", describe(base["net"].loc[a:b]))
    print(f"cost {base['cost'].mean() * 1200:.2f}% a year")
