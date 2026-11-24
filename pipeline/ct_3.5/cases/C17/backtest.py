"""After-the-fall rule layer on equity indexes (synthetic test pod). Prints the REPORT.md numbers."""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_lib"))
import synth  # noqa: E402

INDEXES = ["eq_us", "eq_jp", "eq_de", "eq_uk", "eq_fr", "eq_au", "eq_hk", "eq_kr"]
HIGH_MONTHS = 12
FALL = 0.20
RISK = 0.10
BP = 2.0
WIN = ("1975-01", "2010-12")
ERAS = (("1975-01", "1992-12"), ("1993-01", "2010-12"))


def fall_from_high(R):
    level = (1.0 + R.fillna(0.0)).cumprod().where(R.notna())
    high = level.rolling(HIGH_MONTHS, min_periods=HIGH_MONTHS).max()
    return level / high - 1.0


def run(cost_mult=1.0):
    R = synth.make_panel()["R"][INDEXES]
    on = fall_from_high(R) <= -FALL
    vol = R.rolling(36, min_periods=24).std() * np.sqrt(12)
    live = vol.notna().sum(axis=1)
    pos = (RISK / vol).div(np.sqrt(live.where(live > 0)), axis=0).where(on, 0.0).fillna(0.0)
    held = pos.shift(1)
    gross = (held * R.fillna(0.0)).sum(axis=1)
    cost = held.diff().abs().sum(axis=1) * BP / 1e4 * cost_mult
    frame = pd.DataFrame({"gross": gross, "cost": cost, "net": gross - cost,
                          "markets_on": on.shift(1).fillna(False).sum(axis=1)})
    return frame.loc[WIN[0]:WIN[1]]


def show(label, r):
    print("%-15s SR %5.2f  mean %5.2f%%  vol %5.2f%%  maxDD %6.1f%%" % (
        label, synth.sharpe(r), r.mean() * 1200, r.std() * np.sqrt(12) * 100, synth.max_drawdown(r) * 100))


if __name__ == "__main__":
    f, f2 = run(), run(2.0)
    on_months = f["markets_on"] > 0
    print("%s..%s: %d months, rule on (any market) in %d, market-months on %d" % (
        f.index[0].strftime("%Y-%m"), f.index[-1].strftime("%Y-%m"), len(f), on_months.sum(), f["markets_on"].sum()))
    show("net", f["net"])
    show("gross", f["gross"])
    show("net 2x costs", f2["net"])
    for a, b in ERAS:
        show("net %s-%s" % (a[:4], b[:4]), f["net"].loc[a:b])
    show("net, on months", f.loc[on_months, "net"])
    print("costs %.2f%%/yr" % (f["cost"].mean() * 1200))
