"""Bond carry pod, two versions averaged (synthetic test pod).

python backtest.py -> figures for REPORT.md
"""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_lib"))
from synth import make_panel, sharpe, max_drawdown  # noqa: E402

MARKETS = ["bd_us10", "bd_de10", "bd_jp10", "bd_uk10", "bd_ca10", "bd_au10", "st_us2", "st_de2"]
RISK = 0.06
MIN_RANKED = 3
BP = 1.0
WINDOW = ("1975-01", "2010-12")
ERAS = (("1975-01", "1992-12"), ("1993-01", "2010-12"))


def v_sign(C):
    return np.sign(C)


def v_rank(C):
    r = C.rank(axis=1)
    r = r.sub(r.mean(axis=1), axis=0)
    n = C.notna().sum(axis=1)
    w = r.div(r.abs().sum(axis=1), axis=0).mul(n, axis=0)
    return w.where(n >= MIN_RANKED, axis=0)


VERSIONS = {"sign": v_sign, "rank": v_rank}


def holdings(R, C):
    vol = R.rolling(36, min_periods=24).std() * np.sqrt(12)
    n = vol.notna().sum(axis=1)
    per = {}
    for name, f in VERSIONS.items():
        per[name] = (f(C) * RISK / vol).div(np.sqrt(n.where(n > 0)), axis=0).fillna(0.0)
    pod = sum(per.values()) / len(per)
    return pod, per


def pnl(pos, R, cost_mult=1.0):
    held = pos.shift(1)
    gross = (held * R.fillna(0.0)).sum(axis=1)
    cost = held.diff().abs().sum(axis=1) * BP / 1e4 * cost_mult
    return gross, cost, gross - cost


def line(label, r):
    print(f"{label:<17} SR {sharpe(r):5.2f}  mean {r.mean() * 1200:5.2f}%  vol {r.std() * np.sqrt(12) * 100:5.2f}%  "
          f"maxDD {max_drawdown(r) * 100:6.1f}%")


if __name__ == "__main__":
    P = make_panel()
    R, C = P["R"][MARKETS], P["CARRY"][MARKETS]
    pod, per = holdings(R, C)
    a, b = WINDOW
    g, c, n = (x.loc[a:b] for x in pnl(pod, R))
    n2 = pnl(pod, R, 2.0)[2].loc[a:b]
    print(f"window {n.index[0]:%Y-%m}..{n.index[-1]:%Y-%m}, {len(n)} months")
    line("net (pod)", n)
    line("gross (pod)", g)
    line("net 2x costs", n2)
    for lo, hi in ERAS:
        line(f"net {lo[:4]}-{hi[:4]}", n.loc[lo:hi])
    for name, p in per.items():
        line(f"net, {name} only", pnl(p, R)[2].loc[a:b])
    print(f"costs {c.mean() * 1200:.2f}%/yr")
