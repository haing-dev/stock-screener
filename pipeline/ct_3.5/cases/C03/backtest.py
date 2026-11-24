"""Currency carry, ranked (synthetic test pod).

Run: python backtest.py   -> prints the figures quoted in REPORT.md
"""
import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_lib"))
import synth  # noqa: E402

CFG = {
    "markets": ["fx_eur", "fx_jpy", "fx_gbp", "fx_chf", "fx_aud", "fx_cad", "fx_nzd", "fx_sek"],
    "min_markets": 3,
    "risk": 0.10,
    "vol_months": 36,
    "vol_min": 24,
    "cost_bp": 2.0,
    "window": ("1975-01", "2010-12"),
    "eras": [("1975-01", "1992-12"), ("1993-01", "2010-12")],
}


def rank_weights(row):
    """Demeaned ranks of the carry values present, scaled so that the absolute weights sum to 1."""
    ok = ~np.isnan(row)
    w = np.full(row.shape, np.nan)
    if ok.sum() < CFG["min_markets"]:
        return w
    r = pd.Series(row[ok]).rank().values
    r = r - r.mean()
    w[ok] = r / np.abs(r).sum()
    return w


def simulate(panel, cost_mult=1.0):
    mk = CFG["markets"]
    R = panel["R"][mk].values
    C = panel["CARRY"][mk].values
    dates = panel["R"].index
    T, N = R.shape
    vol = pd.DataFrame(R).rolling(CFG["vol_months"], min_periods=CFG["vol_min"]).std().values * np.sqrt(12)

    pos = np.zeros((T, N))
    for t in range(T):
        w = rank_weights(C[t])
        p = w * CFG["risk"] / vol[t]
        pos[t] = np.where(np.isnan(p), 0.0, p)

    gross = np.zeros(T)
    cost = np.zeros(T)
    for t in range(1, T):
        r = np.where(np.isnan(R[t]), 0.0, R[t])
        gross[t] = pos[t - 1] @ r
        prev = pos[t - 2] if t >= 2 else np.zeros(N)
        cost[t] = np.abs(pos[t - 1] - prev).sum() * CFG["cost_bp"] / 1e4
    out = pd.DataFrame({"gross": gross, "cost": cost * cost_mult}, index=dates)
    out["net"] = out["gross"] - out["cost"]
    a, b = CFG["window"]
    return out.loc[a:b]


def stats(r):
    return (synth.sharpe(r), r.mean() * 1200, r.std() * np.sqrt(12) * 100, synth.max_drawdown(r) * 100)


if __name__ == "__main__":
    panel = synth.make_panel()
    res = simulate(panel)
    res2 = simulate(panel, cost_mult=2.0)
    print("months", len(res), "first", res.index[0].strftime("%Y-%m"), "last", res.index[-1].strftime("%Y-%m"))
    print("net        SR %.2f mean %.2f%% vol %.2f%% maxDD %.1f%%" % stats(res["net"]))
    print("gross      SR %.2f mean %.2f%% vol %.2f%% maxDD %.1f%%" % stats(res["gross"]))
    print("net x2cost SR %.2f mean %.2f%% vol %.2f%% maxDD %.1f%%" % stats(res2["net"]))
    for a, b in CFG["eras"]:
        print("era %s..%s SR %.2f mean %.2f%% vol %.2f%% maxDD %.1f%%" % ((a, b) + stats(res["net"].loc[a:b])))
    print("cost %.2f%%/yr" % (res["cost"].mean() * 1200))
    worst = res["net"].nsmallest(3)
    print("worst months", ", ".join(f"{d:%Y-%m} {v * 100:.1f}%" for d, v in worst.items()))
