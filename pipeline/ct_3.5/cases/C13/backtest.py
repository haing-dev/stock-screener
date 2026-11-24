"""Trend pod, 12-month sign (synthetic test pod). Prints the numbers used in REPORT.md."""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_lib"))
from synth import make_panel, sharpe, max_drawdown  # noqa: E402

LOOKBACK = 12
RISK = 0.10
VOL_WIN, VOL_MIN = 36, 24
COST_BP = {"EQ": 2.0, "FI": 1.0, "FX": 2.0, "CM": 4.0}
START, END = "1975-01", "2010-12"
ERAS = (("1975-01", "1992-12"), ("1993-01", "2010-12"))


def positions(R, klass):
    vol = R.rolling(VOL_WIN, min_periods=VOL_MIN).std() * np.sqrt(12)
    sig = np.sign(R.rolling(LOOKBACK, min_periods=LOOKBACK).sum())
    raw = sig * RISK / vol
    out = []
    for c in ("EQ", "FI", "FX", "CM"):
        cols = [k for k in R.columns if klass[k] == c]
        block = raw[cols]
        n = block.notna().sum(axis=1).replace(0, np.nan)
        out.append(block.div(n, axis=0))
    return pd.concat(out, axis=1)[R.columns]


def run(cost_mult=1.0):
    P = make_panel()
    R, klass = P["R"], P["CLASS"]
    pos = positions(R, klass).fillna(0.0)
    held = pos.shift(1)
    gross = (held * R.fillna(0.0)).sum(axis=1)
    bp = pd.Series({k: COST_BP[klass[k]] / 1e4 for k in R.columns})
    trades = held.diff().abs()
    cost = (trades * bp).sum(axis=1)
    net = gross - cost_mult * cost
    w = slice(START, END)
    return gross[w], net[w], cost[w], trades[w].sum(axis=1)


def line(name, r):
    print(f"{name:<22} SR {sharpe(r):6.2f}  mean {r.mean() * 1200:6.2f}%  vol {r.std() * np.sqrt(12) * 100:6.2f}%"
          f"  maxDD {max_drawdown(r) * 100:6.1f}%")


if __name__ == "__main__":
    gross, net, cost, turn = run()
    _, net2, _, _ = run(cost_mult=2.0)
    print(f"window {net.index[0]:%Y-%m}..{net.index[-1]:%Y-%m}  months {len(net)}")
    line("net", net)
    line("gross", gross)
    line("net, costs x2", net2)
    for a, b in ERAS:
        line(f"net {a[:4]}-{b[:4]}", net[a:b])
    print(f"costs {cost.mean() * 1200:.2f}%/yr  turnover {turn.mean() * 12:.1f}x notional/yr")
