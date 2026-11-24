"""Cross-asset value pod: equities, currencies, commodities (synthetic test pod).

python backtest.py -> all figures used in REPORT.md
"""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_lib"))
from synth import make_panel, sharpe, max_drawdown  # noqa: E402

CLASSES = ("EQ", "FX", "CM")
MIN_HISTORY = 60
CLIP = 2.0
RISK = 0.10
COSTS = {"EQ": 2.0, "FX": 2.0, "CM": 4.0}
SAMPLE = slice("1975-01", "2010-12")
ERAS = {"1975-1992": slice("1975-01", "1992-12"), "1993-2010": slice("1993-01", "2010-12")}


def value_score(V):
    mean = V.expanding(min_periods=MIN_HISTORY).mean()
    sd = V.expanding(min_periods=MIN_HISTORY).std()
    return ((V - mean) / sd).clip(-CLIP, CLIP) / CLIP


def class_block(R, V):
    vol = R.rolling(36, min_periods=24).std() * np.sqrt(12)
    raw = value_score(V) * RISK / vol
    live = raw.notna().sum(axis=1)
    return raw.div(np.sqrt(live.where(live > 0)), axis=0)


def run(cost_mult=1.0):
    P = make_panel()
    klass = P["CLASS"]
    gross, cost = [], []
    for c in CLASSES:
        cols = [k for k in P["R"].columns if klass[k] == c]
        R, V = P["R"][cols], P["VALUE"][cols]
        pos = class_block(R, V).fillna(0.0)
        held = pos.shift(1)
        gross.append((held * R.fillna(0.0)).sum(axis=1))
        cost.append(held.diff().abs().sum(axis=1) * COSTS[c] / 1e4)
    g = pd.concat(gross, axis=1).sum(axis=1)
    k = pd.concat(cost, axis=1).sum(axis=1) * cost_mult
    by_class = pd.concat(gross, axis=1, keys=CLASSES) - pd.concat(cost, axis=1, keys=CLASSES) * cost_mult
    return g[SAMPLE], (g - k)[SAMPLE], k[SAMPLE], by_class[SAMPLE]


def line(label, r):
    print(f"{label:<16} SR {sharpe(r):5.2f}  mean {r.mean() * 1200:5.2f}%  vol {r.std() * np.sqrt(12) * 100:5.2f}%  "
          f"maxDD {max_drawdown(r) * 100:6.1f}%")


if __name__ == "__main__":
    gross, net, cost, by_class = run()
    _, net2, _, _ = run(2.0)
    print(f"sample {net.index[0]:%Y-%m}..{net.index[-1]:%Y-%m} ({len(net)} months)")
    line("net", net)
    line("gross", gross)
    line("net 2x costs", net2)
    for name, s in ERAS.items():
        line(f"net {name}", net[s])
    for c in CLASSES:
        line(f"net {c} only", by_class[c])
    print(f"costs {cost.mean() * 1200:.2f}%/yr")
