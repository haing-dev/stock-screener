"""Directional carry pod: bonds, currencies, commodities (synthetic test pod).

python backtest.py  -> the figures in REPORT.md
"""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_lib"))
import synth  # noqa: E402

BLOCKS = {"FI": 1.0, "FX": 2.0, "CM": 4.0}     # class -> one-way cost, bp of notional
MARKET_RISK = 0.05
VOL = dict(window=36, min_periods=24)
SAMPLE = slice("1975-01", "2010-12")
ERAS = (slice("1975-01", "1992-12"), slice("1993-01", "2010-12"))


def block_returns(P, cl, cost_mult=1.0):
    cols = [k for k in P["R"].columns if P["CLASS"][k] == cl]
    R, C = P["R"][cols], P["CARRY"][cols]
    vol = R.rolling(**VOL).std() * np.sqrt(12)
    w = np.sign(C) * MARKET_RISK / vol
    w = w.div(np.sqrt(w.notna().sum(axis=1).where(lambda n: n > 0)), axis=0).fillna(0.0)
    held = w.shift(1)
    gross = (held * R.fillna(0.0)).sum(axis=1)
    cost = held.diff().abs().sum(axis=1) * BLOCKS[cl] / 1e4 * cost_mult
    return gross, cost


def combine(P, classes, cost_mult=1.0):
    parts = [block_returns(P, c, cost_mult) for c in classes]
    gross = sum(p[0] for p in parts)
    cost = sum(p[1] for p in parts)
    return gross[SAMPLE], cost[SAMPLE], (gross - cost)[SAMPLE]


def stat(label, r):
    print(f"{label:<26} SR {synth.sharpe(r):5.2f}  mean {r.mean() * 1200:5.2f}%  "
          f"vol {r.std() * np.sqrt(12) * 100:5.2f}%  maxDD {synth.max_drawdown(r) * 100:6.1f}%")


if __name__ == "__main__":
    P = synth.make_panel()
    g, c, n = combine(P, ("FI", "FX", "CM"))
    n2 = combine(P, ("FI", "FX", "CM"), 2.0)[2]
    print(f"sample {n.index[0]:%Y-%m}..{n.index[-1]:%Y-%m} ({len(n)} months)")
    stat("net, FI+FX+CM", n)
    stat("gross, FI+FX+CM", g)
    stat("net 2x costs, FI+FX+CM", n2)
    for e in ERAS:
        stat(f"net {e.start[:4]}-{e.stop[:4]}, FI+FX+CM", n[e])
    print(f"costs {c.mean() * 1200:.2f}%/yr")
    for cl in BLOCKS:
        stat(f"net, {cl} only", combine(P, (cl,))[2])
    gx, cx, nx = combine(P, ("FX", "CM"))
    stat("net, FX+CM", nx)
    stat("net 2x costs, FX+CM", combine(P, ("FX", "CM"), 2.0)[2])
    for e in ERAS:
        stat(f"net {e.start[:4]}-{e.stop[:4]}, FX+CM", nx[e])
