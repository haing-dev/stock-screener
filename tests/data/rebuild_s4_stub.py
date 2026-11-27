"""STUB of the S4 rebuild, for tests/core_v1_smoke.py ONLY (docs/research/batches/S4_INTERFACE.md shape, not its
content). It is NOT the independent rebuild (tools/bbgq/lib/rebuild_s4.py, written by a separate agent) and never
ships to the PC. Each key gets a simple 12-month sign trend of an equal-weight basket of its class markets, scaled to
10% by a trailing 36-month volatility lagged one month: the right shape, deliberately not the engine's numbers."""
import numpy as np
import pandas as pd

VERSION = "rebuild_s4-stub-0.0.1"
KEYS = {"trend": ("eq_", "bd_", "st_", "fx_", "cm_"), "carry": ("fx_", "cm_"), "value_eq": ("eq_",),
        "carry_fx_v2": ("fx_",), "carry_energy": ("cm_",)}


def part_returns(inputs, cut="2010-12-31"):
    R = inputs["R"]
    end = pd.Period(pd.Timestamp(cut), "M")
    out = {}
    for k, pre in KEYS.items():
        cols = [c for c in R.columns if c.startswith(pre) and not c.startswith("sp_")]
        x = R[cols]
        lvl = (1 + x.fillna(0)).cumprod().where(x.notna().cummax())
        sig = np.sign(lvl / lvl.shift(12) - 1)
        g = (sig.shift(1) * x).mean(axis=1)
        v = g.rolling(36, min_periods=24).std() * np.sqrt(12)
        r = (g * 0.10 / v.shift(1)).replace([np.inf, -np.inf], np.nan)
        out[k] = r[r.index <= end].astype(float)
    return out
