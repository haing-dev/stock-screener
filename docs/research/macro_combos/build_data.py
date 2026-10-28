"""Rebuild the Macro Compass point-in-time panel in memory from the cached raw data (no repo files written).

Run from anywhere: python3 build_data.py   -> writes panel.pkl next to this script.
Uses the tool's own code (macro/engine.py, macro/registry.py) unchanged; checks that the rebuilt v3.2 exposure
matches the published compass.json.gz series exactly (to its 1% rounding).
"""
import gzip
import json
import os
import pickle
import sys
import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
REPO = "/home/claude/stock-screener"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
os.chdir(REPO)
from macro import engine as E          # noqa: E402
from macro import registry as R        # noqa: E402

BUILD_DATE = pd.Timestamp("2026-10-23")   # date of the cached raw download / published build


def build():
    grid = E.month_grid(BUILD_DATE)
    rets, src, mkt = E.build_returns(grid)
    last = mkt.last_valid_index()
    grid = grid[grid <= last]
    rets, src, mkt = rets.reindex(grid), src.reindex(grid), mkt.reindex(grid)
    ind, F = E.calc_all(grid, rets, mkt)
    sc = E.scores(ind)
    pl = E.pillars(sc)
    S = R.SETTINGS
    econ = pl[["growth", "internals"]].mean(axis=1, skipna=True)
    g6 = econ.rolling(S["stage_smooth"], min_periods=3).mean()
    stage, d12 = E.stages(g6)
    infl6 = pl["inflation"].rolling(S["stage_smooth"], min_periods=3).mean()
    reg, hot, high = E.regimes(stage, infl6, pl["stress"])

    # ---- v3.2 de-risk rule, unrounded (same steps as engine.derisk)
    X = S["derisk"]
    core = [i["id"] for i in R.INDICATORS if i["pillar"] in X["pillars"]]
    lv_m = E.level(mkt)
    fall, hz = X["event"]
    fut = pd.concat([lv_m.shift(-k) for k in range(1, hz + 1)], axis=1).min(axis=1, skipna=False)
    ev = (fut / lv_m - 1 <= -fall).astype(float)
    ev[fut.isna() | lv_m.isna()] = np.nan
    okf = ev.notna().astype(float)
    bad = (sc[core] >= X["worst"]).astype(float)
    avail = sc[core].notna().astype(float)
    hits = bad.mul(ev.fillna(0), axis=0).mul(okf, axis=0).cumsum().shift(hz)
    n_w = bad.mul(okf, axis=0).cumsum().shift(hz)
    base = (ev.fillna(0).cumsum() / okf.cumsum().replace(0, np.nan)).shift(hz)
    k = X["shrink"]
    w = ((hits + k * base.values[:, None]) / (n_w + k)).div(base, axis=0).fillna(1.0).clip(upper=5)
    share = ((w * bad).sum(axis=1) / (w * avail).sum(axis=1).replace(0, np.nan)).fillna(0.0)
    share = share.where(avail.sum(axis=1) >= 10, 0.0)
    lo, hi = X["band"]
    e_rule = 1 - (1 - X["min_stocks"]) * ((share - lo) / (hi - lo)).clip(0, 1)

    # ---- T-bill (Ken French RF, forward-filled for the latest months)
    _, ff = E.load_french()
    rf = pd.Series({pd.Period(k_, "M"): v.get("RF", np.nan) for k_, v in ff.items()}, dtype=float).reindex(grid).ffill()

    # ---- check vs the published build
    d = json.load(gzip.open(os.path.join(REPO, "cache", "macro", "out", "compass.json.gz"), "rt"))
    pub_e = pd.Series(d["derisk"]["exposure"], index=pd.PeriodIndex(d["months"], freq="M"), dtype=float)
    pub_s = pd.Series(d["derisk"]["share"], index=pd.PeriodIndex(d["months"], freq="M"), dtype=float)
    pub_m = pd.Series(d["market"], index=pd.PeriodIndex(d["months"], freq="M"), dtype=float)
    chk = {
        "months": f"{grid[0]}..{grid[-1]} ({len(grid)})",
        "max_abs_diff_exposure_pct": float((np.round(e_rule * 100) - pub_e.reindex(grid)).abs().max()),
        "max_abs_diff_share_pct": float((np.round(share * 1000) / 10 - pub_s.reindex(grid)).abs().max()),
        "max_rel_diff_market_level": float((E.level(mkt).round(4) / pub_m.reindex(grid) - 1).abs().max()),
        "hot_equal": bool((pd.Series(d["hot"], index=pd.PeriodIndex(d["months"], freq="M")).reindex(grid).values == hot.values).all()),
        "stage_equal": bool(all((a == b) or (a is None and not isinstance(b, str))
                                for a, b in zip(d["stage"], [s if isinstance(s, str) else None for s in stage.values]))),
    }

    # ---- extra raw series for the tests
    ief = E.monthly_px("Y_IEF", grid).pct_change(fill_method=None)
    vix_m = ind["vix"]                       # month-end VIX (Yahoo ^VIX same-day close, FRED VIXCLS fallback), 1990+
    cape_m = E._csv("CAPE")
    cape_m = pd.Series(cape_m.values, index=cape_m.index.to_period("M")).groupby(level=0).last().reindex(grid)
    panel = dict(grid=grid, rets=rets, src=src, mkt=mkt, rf=rf, ind=ind, F=F, sc=sc, pl=pl, g6=g6, d12=d12,
                 stage=stage, infl6=infl6, reg=reg, hot=hot, high=high, share=share, e_rule=e_rule, wts=w,
                 ief=ief, vix=vix_m, cape=cape_m, check=chk)
    with open(os.path.join(HERE, "panel.pkl"), "wb") as f:
        pickle.dump(panel, f)
    return panel


if __name__ == "__main__":
    p = build()
    for k_, v in p["check"].items():
        print(f"{k_}: {v}")
