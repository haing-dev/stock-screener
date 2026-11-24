"""Equity index relative momentum (synthetic test pod). Output -> REPORT.md."""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_lib"))
from synth import make_panel, sharpe, max_drawdown  # noqa: E402

INDEXES = ["eq_us", "eq_jp", "eq_de", "eq_uk", "eq_fr", "eq_au", "eq_hk", "eq_kr"]
WINDOW_MONTHS = 6
GAP = 1
RISK = 0.10
ONE_WAY = 2.0e-4
FROM, TO = "1975-01", "2010-12"


def run(cost_mult=1.0):
    R = make_panel()["R"][INDEXES]
    x = R.to_numpy()
    T, N = x.shape
    sd = R.rolling(36, min_periods=24).std().to_numpy() * np.sqrt(12)
    past = R.shift(GAP).rolling(WINDOW_MONTHS, min_periods=WINDOW_MONTHS).sum().to_numpy()
    pos = np.zeros((T, N))
    for t in range(T):
        ok = ~np.isnan(past[t]) & ~np.isnan(sd[t])
        if ok.sum() < 3:
            continue
        rk = pd.Series(past[t, ok]).rank().to_numpy()
        rk = rk - rk.mean()
        w = rk / np.abs(rk).sum()
        pos[t, ok] = w * RISK / sd[t, ok] * np.sqrt(ok.sum())
    gross = np.r_[0.0, np.nansum(pos[:-1] * np.nan_to_num(x[1:]), axis=1)]
    trades = np.r_[0.0, 0.0, np.abs(np.diff(pos, axis=0))[:-1].sum(axis=1)]
    cost = trades * ONE_WAY * cost_mult
    df = pd.DataFrame({"gross": gross, "cost": cost, "net": gross - cost}, index=R.index)
    return df.loc[FROM:TO]


def say(tag, r):
    print(f"{tag:<15} SR {sharpe(r):5.2f}  mean {r.mean() * 1200:5.2f}%  vol {r.std() * np.sqrt(12) * 100:5.2f}%  "
          f"maxDD {max_drawdown(r) * 100:6.1f}%")


if __name__ == "__main__":
    d, d2 = run(), run(2.0)
    print(f"{d.index[0]:%Y-%m} to {d.index[-1]:%Y-%m}: {len(d)} months")
    say("net", d["net"])
    say("gross", d["gross"])
    say("net 2x costs", d2["net"])
    say("net 1975-1992", d["net"].loc["1975":"1992"])
    say("net 1993-2010", d["net"].loc["1993":"2010"])
    print(f"costs {d['cost'].mean() * 1200:.2f}%/yr")
