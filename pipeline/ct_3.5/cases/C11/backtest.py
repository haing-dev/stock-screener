"""Trend pod, three horizons averaged, EWMA risk (synthetic test pod). Output feeds REPORT.md."""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_lib"))
from synth import make_panel, sharpe, max_drawdown  # noqa: E402

HORIZONS = (1, 3, 12)
HALF_LIFE = 6
MIN_MONTHS = 12
MARKET_RISK = 0.06
COST = {"EQ": 2.0, "FI": 1.0, "FX": 2.0, "CM": 4.0}
WINDOW = ("1975-01", "2010-12")


def ewma_vol(R):
    return (R ** 2).ewm(halflife=HALF_LIFE, min_periods=MIN_MONTHS).mean().pow(0.5) * np.sqrt(12)


def trend_score(R):
    parts = [np.sign(R.rolling(h, min_periods=h).sum()) for h in HORIZONS]
    return sum(parts) / len(parts)


def target(R, klass):
    raw = trend_score(R) * MARKET_RISK / ewma_vol(R)
    blocks = []
    for c in sorted(set(klass.values())):
        cols = [k for k in R.columns if klass[k] == c]
        live = raw[cols].notna().sum(axis=1)
        blocks.append(raw[cols].div(np.sqrt(live.where(live > 0)), axis=0))
    return pd.concat(blocks, axis=1)[R.columns].fillna(0.0)


def simulate(cost_mult=1.0):
    P = make_panel()
    R, klass = P["R"], P["CLASS"]
    pos = target(R, klass)
    bp = pd.Series({k: COST[klass[k]] for k in R.columns}) / 1e4
    trade = pos.diff().abs()
    gross = (pos.shift(1) * R).sum(axis=1, min_count=1).fillna(0.0)
    cost = (trade.shift(1) * bp).sum(axis=1) * cost_mult
    df = pd.DataFrame({"gross": gross, "cost": cost, "net": gross - cost})
    return df.loc[WINDOW[0]:WINDOW[1]], trade.loc[WINDOW[0]:WINDOW[1]].sum(axis=1)


def p(label, r):
    print(f"{label:<14}SR {sharpe(r):5.2f}  mean {r.mean() * 1200:5.2f}%  vol {r.std() * np.sqrt(12) * 100:5.2f}%  "
          f"maxDD {max_drawdown(r) * 100:6.1f}%")


if __name__ == "__main__":
    df, turnover = simulate()
    df2, _ = simulate(2.0)
    print(f"{df.index[0]:%Y-%m}..{df.index[-1]:%Y-%m}, {len(df)} months")
    p("net", df["net"])
    p("gross", df["gross"])
    p("net 2x cost", df2["net"])
    p("net 1975-92", df["net"].loc["1975":"1992"])
    p("net 1993-2010", df["net"].loc["1993":"2010"])
    print(f"costs {df['cost'].mean() * 1200:.2f}%/yr, turnover {turnover.mean() * 12:.1f}x/yr")
