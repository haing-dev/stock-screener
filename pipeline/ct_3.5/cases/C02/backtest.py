"""Soft-print rule layer on bonds (synthetic test pod). Prints the figures in REPORT.md."""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_lib"))
from synth import make_panel, sharpe, max_drawdown  # noqa: E402

BONDS = ["bd_us10", "bd_de10", "bd_jp10", "bd_uk10", "bd_ca10", "bd_au10"]
AVG_MONTHS = 12
RISK = 0.10
BP = 1.0
WINDOW = ("1975-01", "2010-12")
ERAS = [("1975-01", "1992-12"), ("1993-01", "2010-12")]


def rule_state(cpi):
    """True at month-end t when the latest published monthly CPI change is below the average of the 12 before it.

    The CPI for reference month m is published in month m+1, so at the close of t the latest print is t-1.
    """
    published = cpi.shift(1)
    m = np.log(published).diff() * 1200
    prior = m.shift(1).rolling(AVG_MONTHS).mean()
    return (m < prior) & prior.notna()


def run(cost_mult=1.0):
    P = make_panel()
    R = P["R"][BONDS]
    on = rule_state(P["MACRO"]["us_cpi"])
    vol = R.rolling(36, min_periods=24).std() * np.sqrt(12)
    n = vol.notna().sum(axis=1).replace(0, np.nan)
    pos = (RISK / vol).div(np.sqrt(n), axis=0).where(on, 0.0).fillna(0.0)
    held = pos.shift(1)
    gross = (held * R.fillna(0.0)).sum(axis=1)
    cost = held.diff().abs().sum(axis=1) * BP / 1e4 * cost_mult
    res = pd.DataFrame({"gross": gross, "cost": cost, "net": gross - cost, "on": on.shift(1).fillna(False)})
    return res.loc[WINDOW[0]:WINDOW[1]]


def report(name, r):
    print(f"{name:<20}SR {sharpe(r):5.2f}  mean {r.mean() * 1200:5.2f}%  vol {r.std() * np.sqrt(12) * 100:5.2f}%  "
          f"maxDD {max_drawdown(r) * 100:6.1f}%")


if __name__ == "__main__":
    res, res2 = run(), run(2.0)
    print(f"{res.index[0]:%Y-%m}..{res.index[-1]:%Y-%m}  months {len(res)}  on-months {int(res['on'].sum())}")
    report("net", res["net"])
    report("gross", res["gross"])
    report("net, 2x costs", res2["net"])
    for a, b in ERAS:
        report(f"net {a[:4]}-{b[:4]}", res["net"].loc[a:b])
    on = res.loc[res["on"], "net"]
    print(f"on-month mean {on.mean() * 100:.2f}%  hit rate {(on > 0).mean() * 100:.0f}%  "
          f"costs {res['cost'].mean() * 1200:.2f}%/yr")
