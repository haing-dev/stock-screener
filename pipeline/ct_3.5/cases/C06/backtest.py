"""Pair reversion pod (synthetic test pod). `python backtest.py` prints every figure in REPORT.md."""
import os
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_lib"))
from synth import make_panel, sharpe, max_drawdown  # noqa: E402

PAIRS = [("bd_us10", "bd_ca10"), ("bd_de10", "bd_uk10"), ("eq_de", "eq_fr"), ("fx_aud", "fx_nzd"),
         ("cm_wti", "cm_brent"), ("cm_gold", "cm_silver"), ("cm_corn", "cm_soy"), ("fx_chf", "fx_sek")]
COST_BP = {"EQ": 2.0, "FI": 1.0, "FX": 2.0, "CM": 4.0}
WINDOW = ("1975-01", "2010-12")
ERAS = [("1975-01", "1992-12"), ("1993-01", "2010-12")]


@dataclass
class Pair:
    a: str
    b: str
    mean_months: int = 3
    vol_months: int = 36
    vol_min: int = 24
    clip: float = 2.0
    risk: float = 0.10

    def legs(self, R):
        ra, rb = R[self.a], R[self.b]
        va = ra.rolling(self.vol_months, min_periods=self.vol_min).std() * np.sqrt(12)
        vb = rb.rolling(self.vol_months, min_periods=self.vol_min).std() * np.sqrt(12)
        u = ra / va.shift(1) - rb / vb.shift(1)                      # unit-risk spread return of month t
        level = u.cumsum()
        dev = level - level.rolling(self.mean_months).mean()
        su = u.rolling(self.vol_months, min_periods=self.vol_min).std()
        z = (dev / su).clip(-self.clip, self.clip)
        k = -z / self.clip * self.risk / (su * np.sqrt(12))
        return pd.DataFrame({self.a: k / va, self.b: -k / vb})        # notional held from the close of t


def book(R, cost_mult=1.0):
    legs = [Pair(a, b).legs(R) for a, b in PAIRS]
    active = pd.concat([l.notna().all(axis=1) for l in legs], axis=1).sum(axis=1)
    scale = 1.0 / np.sqrt(active.replace(0, np.nan))
    pnl, cost = [], []
    for l in legs:
        pos = l.mul(scale, axis=0).fillna(0.0)
        held = pos.shift(1)
        pnl.append((held * R[l.columns].fillna(0.0)).sum(axis=1))
        bp = np.array([COST_BP[c[:2].upper().replace("BD", "FI").replace("ST", "FI")] for c in l.columns]) / 1e4
        cost.append((held.diff().abs() * bp).sum(axis=1))
    gross = pd.concat(pnl, axis=1).sum(axis=1)
    c = pd.concat(cost, axis=1).sum(axis=1) * cost_mult
    return pd.DataFrame({"gross": gross, "cost": c, "net": gross - c}).loc[WINDOW[0]:WINDOW[1]]


def show(label, r):
    print(f"{label:<18} SR {sharpe(r):5.2f}  mean {r.mean() * 1200:5.2f}%  vol {r.std() * np.sqrt(12) * 100:5.2f}%  "
          f"maxDD {max_drawdown(r) * 100:6.1f}%")


if __name__ == "__main__":
    R = make_panel()["R"]
    b1, b2 = book(R), book(R, cost_mult=2.0)
    print(f"months {len(b1)} ({b1.index[0]:%Y-%m}..{b1.index[-1]:%Y-%m})")
    show("net", b1["net"])
    show("gross", b1["gross"])
    show("net, 2x costs", b2["net"])
    for a, b in ERAS:
        show(f"net {a}..{b}", b1["net"].loc[a:b])
    print(f"costs {b1['cost'].mean() * 1200:.2f}%/yr")
