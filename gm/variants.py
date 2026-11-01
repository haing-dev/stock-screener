"""Challenger builders for the adoption protocol (docs/research/global_macro/TESTING_PROTOCOL.md).

Each builder takes the incumbent (cfg, R, S) and returns a challenger (cfg, R, S) with exactly one registered change.
S = {"E", "C", "V"} as in cache/gm/signals.pkl (optionally "ET": theme scores).
"""
import copy

import numpy as np
import pandas as pd

from . import config as CF
from . import panel as P
from . import signals as G

DURATION = {2: 1.9, 5: 4.6, 10: 8.5, 30: 18.0}


def _copy(S):
    return {k: (v.copy() if hasattr(v, "copy") else copy.deepcopy(v)) for k, v in S.items()}


def econ_themes(cfg, R, S):
    """E1: economic trend as theme x asset-class blocks (each vol-scaled), themes equal risk."""
    return CF.variant(cfg, econ_structure="themes"), R, S


def us_3m_rate(cfg, R, S):
    """S1: synthetic US 3-month short-rate market from month-end 3m T-bill rates (FRED DTB3, daily -> month end)."""
    y = P.F("DTB3").reindex(R.index)
    r = (-0.25 * y.diff() / 100).rename("st_us_3m")
    R2 = R.copy()
    R2["st_us_3m"] = r
    S2 = _copy(S)
    S2["E"]["st_us_3m"] = S["E"]["st_us_2y"]                 # same country, same bond signs
    if "ET" in S2:
        for t in S2["ET"]:
            S2["ET"][t]["st_us_3m"] = S["ET"][t]["st_us_2y"]
    gw = dict(cfg.get("gross_weights", {}))
    gw["st_us_3m"] = 0.25 / 1.9
    return CF.variant(cfg, gross_weights=gw), R2, S2


def bond_value_composite(cfg, R, S):
    """V1: bond value = average cross-sectional rank of the real yield and the 5-year rise in the 10-year yield."""
    S2 = _copy(S)
    cols = [k for k in S["V"].columns if k.startswith("bd_") and k in G.BD and G.BD[k][1] >= 10]
    rise = pd.DataFrame({k: G.yield_of(*G.BD[k]) - G.yield_of(*G.BD[k]).shift(60) for k in cols}).reindex(S["V"].index)
    ry = S["V"][cols]
    a = ry.rank(axis=1, pct=True)
    b = rise.rank(axis=1, pct=True)
    S2["V"][cols] = ((a + b) / 2).where(ry.notna() & rise.notna(), a)
    return cfg, R, S2


def fx_value_skip(cfg, R, S):
    """V2: currency value = minus the real appreciation from t-60 to t-12 (skips the trend window)."""
    S2 = _copy(S)
    us_p = G.cpi_yoy("US").ffill(limit=18).shift(1)
    for k, (cur, cc) in G.FX_CC.items():
        if k not in S["V"].columns:
            continue
        fxv = P.fx_usd_value(cur)
        lp = G.cpi_yoy(G.FX_MACRO.get(cc, cc)).ffill(limit=18).shift(1)
        gap = ((lp - us_p) / 100 / 12).shift(12).rolling(48, min_periods=48).sum()
        real_chg = np.log(fxv.shift(12) / fxv.shift(60)) + gap
        S2["V"][k] = (-real_chg).reindex(S["V"].index)
    return cfg, R, S2


def bond_carry_duration(cfg, R, S):
    """C1: bond carry per unit of duration (changes the cross-sectional half only; signs unchanged)."""
    S2 = _copy(S)
    for k in S["C"].columns:
        if k in G.BD:
            S2["C"][k] = S["C"][k] / DURATION[G.BD[k][1]]
    return cfg, R, S2


BATCH1 = {"E1 econ theme blocks": econ_themes, "S1 US 3m short-rate market": us_3m_rate,
          "V1 bond value composite": bond_value_composite, "V2 FX value skip 12m": fx_value_skip,
          "C1 bond carry per duration": bond_carry_duration}
