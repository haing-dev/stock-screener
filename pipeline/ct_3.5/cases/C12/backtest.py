"""Value pod for bonds, currencies and equity indexes (synthetic test pod).

Prints the numbers that REPORT.md quotes.
"""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_lib"))
import synth  # noqa: E402


class ValuePod:
    classes = ("FI", "FX", "EQ")
    cost_bp = {"FI": 1.0, "FX": 2.0, "EQ": 2.0}
    risk = 0.10
    clip = 2.0
    vol_window = (36, 24)
    sample = ("1975-01", "2010-12")
    eras = (("1975-01", "1992-12"), ("1993-01", "2010-12"))

    def __init__(self, panel):
        self.R = panel["R"]
        self.V = panel["VALUE"]
        self.klass = panel["CLASS"]

    def members(self, c):
        return [k for k in self.R.columns if self.klass[k] == c]

    def standardise(self, V):
        return V.apply(lambda s: (s - s.mean()) / s.std())

    def weights(self, c):
        cols = self.members(c)
        n, m = self.vol_window
        vol = self.R[cols].rolling(n, min_periods=m).std() * np.sqrt(12)
        score = self.standardise(self.V[cols]).clip(-self.clip, self.clip) / self.clip
        w = score * self.risk / vol
        k = w.notna().sum(axis=1)
        return w.div(np.sqrt(k.where(k > 0)), axis=0).fillna(0.0)

    def run(self, cost_mult=1.0):
        gross = pd.Series(0.0, index=self.R.index)
        cost = pd.Series(0.0, index=self.R.index)
        for c in self.classes:
            w = self.weights(c).shift(1)
            gross += (w * self.R[w.columns].fillna(0.0)).sum(axis=1)
            cost += w.diff().abs().sum(axis=1) * self.cost_bp[c] / 1e4
        out = pd.DataFrame({"gross": gross, "cost": cost * cost_mult})
        out["net"] = out["gross"] - out["cost"]
        return out.loc[self.sample[0]:self.sample[1]]


def stats(r):
    return f"SR {synth.sharpe(r):5.2f}  mean {r.mean() * 1200:5.2f}%  vol {r.std() * np.sqrt(12) * 100:5.2f}%  " \
           f"maxDD {synth.max_drawdown(r) * 100:6.1f}%"


if __name__ == "__main__":
    pod = ValuePod(synth.make_panel())
    a, b = pod.run(), pod.run(2.0)
    print("window", a.index[0].strftime("%Y-%m"), "-", a.index[-1].strftime("%Y-%m"), "months", len(a))
    print("net          ", stats(a["net"]))
    print("gross        ", stats(a["gross"]))
    print("net 2x costs ", stats(b["net"]))
    for lo, hi in ValuePod.eras:
        print(f"net {lo[:4]}-{hi[:4]}", stats(a["net"].loc[lo:hi]))
    print("costs %.2f%%/yr" % (a["cost"].mean() * 1200))
