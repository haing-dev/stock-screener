"""Commodity trend pod, 6- and 12-month signs (synthetic test pod). Prints the REPORT.md figures."""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_lib"))
from synth import make_panel, sharpe, max_drawdown  # noqa: E402

COMMODITIES = ["cm_wti", "cm_brent", "cm_natgas", "cm_gold", "cm_silver", "cm_copper", "cm_corn", "cm_soy"]
HORIZONS = [6, 12]
RISK = 0.10
ONE_WAY_BP = 4.0
START, END = "1975-01", "2010-12"
ERAS = [("1975-01", "1992-12"), ("1993-01", "2010-12")]


def load():
    R = make_panel()["R"][COMMODITIES]
    return R.dropna(how="any")


def signal(R):
    s = pd.concat([np.sign(R.rolling(h).sum()) for h in HORIZONS], keys=HORIZONS).groupby(level=1).mean()
    return s.reindex(R.index)


def run(R, cost_mult=1.0):
    vol = R.rolling(36, min_periods=24).std() * np.sqrt(12)
    pos = signal(R) * RISK / vol
    pos = pos.div(np.sqrt(pos.notna().sum(axis=1).replace(0, np.nan)), axis=0).fillna(0.0)
    gross = (pos.shift(1) * R).sum(axis=1)
    cost = pos.diff().abs().sum(axis=1).shift(1).fillna(0.0) * ONE_WAY_BP / 1e4 * cost_mult
    net = gross - cost
    return gross.loc[START:END], cost.loc[START:END], net.loc[START:END]


def out(label, r):
    print(f"{label:<14} SR {sharpe(r):5.2f}  mean {r.mean() * 1200:5.2f}%  vol {r.std() * np.sqrt(12) * 100:5.2f}%  "
          f"maxDD {max_drawdown(r) * 100:6.1f}%")


if __name__ == "__main__":
    R = load()
    gross, cost, net = run(R)
    net2 = run(R, 2.0)[2]
    print(f"window {START}..{END}")
    out("net", net)
    out("gross", gross)
    out("net 2x costs", net2)
    for a, b in ERAS:
        out(f"net {a[:4]}-{b[:4]}", net.loc[a:b])
    print(f"costs {cost.mean() * 1200:.2f}%/yr")
