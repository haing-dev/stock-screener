"""Commodity curve carry, directional (synthetic test pod).

Run: python backtest.py   (REPORT.md quotes this output)
"""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_lib"))
import synth  # noqa: E402

COMMODITIES = ("cm_wti", "cm_brent", "cm_natgas", "cm_gold", "cm_silver", "cm_copper", "cm_corn", "cm_soy")
ENERGY = ("cm_wti", "cm_brent", "cm_natgas")
TRADE_BP = {"cm_natgas": 6.0}
DEFAULT_BP = 4.0
RISK = 0.10
START, END = "1975-01", "2010-12"


class CurveCarry:
    def __init__(self, panel):
        self.R = panel["R"][list(COMMODITIES)]
        self.C = panel["CARRY"][list(COMMODITIES)]
        self.bp = pd.Series({k: TRADE_BP.get(k, DEFAULT_BP) for k in COMMODITIES}) / 1e4

    def target(self):
        vol = self.R.rolling(36, min_periods=24).std() * np.sqrt(12)
        raw = np.sign(self.C) * RISK / vol
        k = raw.notna().sum(axis=1)
        return raw.div(np.sqrt(k.where(k > 0)), axis=0).fillna(0.0)

    def returns(self, cost_mult=1.0, members=COMMODITIES):
        pos = self.target()[list(members)]
        held = pos.shift(1)
        gross = (held * self.R[list(members)].fillna(0.0)).sum(axis=1)
        cost = (held.diff().abs() * self.bp[list(members)]).sum(axis=1) * cost_mult
        return pd.DataFrame({"gross": gross, "cost": cost, "net": gross - cost}).loc[START:END]


def show(label, r):
    print(f"{label:<20} SR {synth.sharpe(r):5.2f}  mean {r.mean() * 1200:5.2f}%  "
          f"vol {r.std() * np.sqrt(12) * 100:5.2f}%  maxDD {synth.max_drawdown(r) * 100:6.1f}%")


if __name__ == "__main__":
    pod = CurveCarry(synth.make_panel())
    base, double = pod.returns(), pod.returns(2.0)
    print(f"{base.index[0]:%Y-%m}..{base.index[-1]:%Y-%m} ({len(base)} months)")
    show("net", base["net"])
    show("gross", base["gross"])
    show("net 2x costs", double["net"])
    show("net 1975-1992", base["net"].loc["1975":"1992"])
    show("net 1993-2010", base["net"].loc["1993":"2010"])
    show("net, energy legs", pod.returns(members=ENERGY)["net"])
    show("net, other legs", pod.returns(members=tuple(k for k in COMMODITIES if k not in ENERGY))["net"])
    print(f"costs {base['cost'].mean() * 1200:.2f}%/yr")
