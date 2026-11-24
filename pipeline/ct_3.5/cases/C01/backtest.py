"""Ranked carry across rates, currencies and commodities (synthetic test pod).

python backtest.py   # every number in REPORT.md comes from this output
"""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_lib"))
from synth import make_panel, sharpe, max_drawdown  # noqa: E402

CLASSES = ["FI", "FX", "CM"]
COST_BP = {"FI": 1.0, "FX": 2.0, "CM": 4.0}
MIN_IN_CLASS = 3
CLASS_RISK = 0.06
PRINT_CHECK = 6.0
START = "1975-01"
END = "2010-12"
ERAS = [("1975-01", "1992-12"), ("1993-01", "2010-12")]


def usable_months(R):
    z = R / R.rolling(36, min_periods=24).std().shift(1)
    return ~(z.abs() > PRINT_CHECK).any(axis=1)


def ranked(c):
    r = c.rank(axis=1)
    r = r.sub(r.mean(axis=1), axis=0)
    w = r.div(r.abs().sum(axis=1), axis=0)
    return w.where(c.notna().sum(axis=1) >= MIN_IN_CLASS, axis=0)


def positions(P):
    out = {}
    for cl in CLASSES:
        cols = [k for k in P["R"].columns if P["CLASS"][k] == cl]
        vol = P["R"][cols].rolling(36, min_periods=24).std() * np.sqrt(12)
        w = ranked(P["CARRY"][cols])
        p = w * CLASS_RISK / vol * np.sqrt(len(cols))
        out[cl] = p.fillna(0.0)
    return out


def pnl(P, cost_mult=1.0):
    gross = pd.Series(0.0, index=P["R"].index)
    cost = pd.Series(0.0, index=P["R"].index)
    for cl, p in positions(P).items():
        h = p.shift(1)
        gross = gross + (h * P["R"][p.columns].fillna(0.0)).sum(axis=1)
        cost = cost + h.diff().abs().sum(axis=1) * COST_BP[cl] / 1e4
    df = pd.DataFrame({"gross": gross, "cost": cost * cost_mult})
    df["net"] = df["gross"] - df["cost"]
    df = df[usable_months(P["R"])]
    return df.loc[START:END]


def show(label, r):
    print(f"{label:<24}SR {sharpe(r):5.2f}  mean {r.mean() * 1200:5.2f}%  vol {r.std() * np.sqrt(12) * 100:5.2f}%  "
          f"maxDD {max_drawdown(r) * 100:6.1f}%")


if __name__ == "__main__":
    P = make_panel()
    df, df2 = pnl(P), pnl(P, 2.0)
    print(f"sample {df.index[0]:%Y-%m}..{df.index[-1]:%Y-%m} ({len(df)} months)")
    show("net", df["net"])
    show("gross", df["gross"])
    show("net 2x costs", df2["net"])
    for a, b in ERAS:
        s = df["net"].loc[a:b]
        show(f"net {s.index[0]:%Y-%m}..{b}", s)
    print(f"costs {df['cost'].mean() * 1200:.2f}%/yr")
