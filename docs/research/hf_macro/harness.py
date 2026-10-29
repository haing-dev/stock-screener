"""Hypothesis harness. A hypothesis module defines HYP = [dict(...)] with keys:
  id        short unique id, e.g. "X017"
  source    "Speaker - transcript file" (from transcript_rules/batch*.md)
  desc      one line, plain words
  kind      one of:
     "cut"       cond -> stocks capped at `level` (default 0.0) on top of the base exposure
     "gate"      cond -> macro warnings are acted on (in addition to the Fed-tightening gate)
     "block"     cond -> no warning/growth cut is applied that month (re-entry override); stocks = 100%
     "defensive" cond -> the non-stock share is held in `asset` (instead of T-bills) while cond holds
     "sleeve"    cond -> `w` (default 0.1) of the whole book in `asset`, taken pro rata from everything else
     "location"  cond -> share `s` (default 0.5) of the equity part moved from the S&P into `assets` (equal weight)
     "overlay"   weights(): function returning a DataFrame of extra weights (may be negative = short via inverse
                 ETF/futures), added on top of the base book; net long book must stay <= 100% invested
  cond      function () -> boolean pd.Series on grid, KNOWN AT THE END OF MONTH t (apply publication lags yourself:
            monthly FRED data observed for month m is usually published in m+1 -> .shift(1); quarterly data dated
            at quarter start -> .shift(4) or more; Yahoo month-end prices need no lag)
  asset/assets/w/s/level as needed (asset names must be columns of lab.R)
Base books: "live" = Macro Compass 4.1 rule; "c5" = candidate 5.0 (live + squeeze/melt-up cuts + inflation sleeve +
sector momentum + Treasury condition). Each hypothesis is evaluated against both.
"""
import importlib
import math
import os
import sys
import traceback

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from robust5 import *  # noqa  (lab, base, exp_combo objects; candidate 5.0 = r5/e5)

h3 = (cpi_yy > 3).fillna(False)
X5 = {"gold": 0.1 * (h3 & gold_up), "commod": 0.1 * (h3 & com_up)}
sqc_ = (sc["squeeze"] >= 80).fillna(False)
_spx = lvl(R["spx"])
muc_ = (((_spx / _spx.shift(12) - 1) > 0.25) & ((gs10 - gs10.shift(12)) > 1.5)).fillna(False)


def base_e(kind_gate=None, block=None):
    gate = fed | kind_gate if kind_gate is not None else fed
    e = 1 - I * gate.astype(float)
    cut_g = gtt.copy()
    e = np.minimum(e, pd.Series(np.where(cut_g, 0.0, 1.0), index=grid))
    return pd.Series(e, index=grid).fillna(1.0)


def books(h):
    """Returns {'live': W, 'c5': W} for hypothesis h."""
    k = h["kind"]
    c = h["cond"]().reindex(grid).fillna(False).astype(bool) if "cond" in h else None
    out = {}
    for bk in ("live", "c5"):
        gate_extra = c if k == "gate" else None
        e = base_e(gate_extra)
        if bk == "c5":
            e = np.minimum(e, pd.Series(np.where(sqc_ | muc_, 0.0, 1.0), index=grid))
        if k == "cut":
            e = np.minimum(e, pd.Series(np.where(c, h.get("level", 0.0), 1.0), index=grid))
        if k == "block":
            e = e.where(~c, 1.0)
        d = dict(D_["D0"] if bk == "live" else D_["D7"])
        x = dict(X5) if bk == "c5" else {}
        l = "L4" if bk == "c5" else "L0"
        W = build(e, d, x, l)
        if k == "defensive":
            rest = W.drop(columns=[col for col in W.columns if col.startswith("sec_")]).copy()
            nonstock = (1 - e) * (1 - sum((v.astype(float) for v in x.values()), pd.Series(0.0, index=grid)))
            # move T-bill part (non-stock minus Treasuries) into the asset while cond holds
            tb = nonstock - W.get("t30y", 0.0)
            W[h["asset"]] = W.get(h["asset"], 0.0) + tb.clip(lower=0) * c.astype(float)
        if k == "sleeve":
            w = h.get("w", 0.1) * c.astype(float)
            W = W.mul(1 - w, axis=0)
            W[h["asset"]] = W.get(h["asset"], 0.0) + w
        if k == "location":
            s = h.get("s", 0.5) * c.astype(float)
            moved = W["spx"] * s
            W["spx"] = W["spx"] - moved
            for a in h["assets"]:
                W[a] = W.get(a, 0.0) + moved / len(h["assets"])
        if k == "overlay":
            OW = h["weights"]().reindex(grid).fillna(0.0)
            for a in OW.columns:
                W[a] = W.get(a, 0.0) + OW[a]
        out[bk] = W
    return out


def fallback(W, h):
    """Where a hypothesis asset has no data yet, keep the S&P/T-bill instead (so long windows stay comparable)."""
    W = W.copy()
    for a in W.columns:
        if a in ("spx",) or a.startswith("sec_") or a not in R:
            continue
        miss = R[a].shift(-1).isna() & (pd.Series(range(T), index=grid) < T - 1)
        if miss.any() and h["kind"] in ("location",):
            W.loc[miss, "spx"] = W.loc[miss, "spx"] + W.loc[miss, a]
        W.loc[miss, a] = 0.0
    return W


WINS = {"A": ("1975-02", "2000-12"), "B": ("2001-01", "2026-10"), "F": ("1975-02", "2026-10"),
        "S1": ("1997-02", "2011-12"), "S2": ("2012-01", "2026-10")}
REF = {"live": run(W41), "c5": r5}


def evaluate(h):
    res = {"id": h["id"], "kind": h["kind"], "desc": h["desc"][:90], "source": h.get("source", "")[:60]}
    try:
        B = books(h)
        c = h["cond"]().reindex(grid).fillna(False) if "cond" in h else None
        res["on_share"] = float(c[grid >= Per("1975-01")].mean()) if c is not None else np.nan
        res["first"] = str(c[c].index.min()) if c is not None and c.any() else ""
        for bk, W in B.items():
            r = run(fallback(W, h))
            for wk, (a, b) in WINS.items():
                s, s0 = stats(r, a, b), stats(REF[bk], a, b)
                res[f"{bk}_{wk}_dsh"] = s["sh"] - s0["sh"]
                res[f"{bk}_{wk}_dcagr"] = s["cagr"] - s0["cagr"]
                res[f"{bk}_{wk}_ddd"] = s["dd"] - s0["dd"]
        res["error"] = ""
    except Exception as ex:
        res["error"] = (type(ex).__name__ + ": " + str(ex))[:200]
    return res


def main(mods):
    rows = []
    for m in mods:
        mod = importlib.import_module(m)
        for h in mod.HYP:
            rows.append(evaluate(h))
    df = pd.DataFrame(rows)
    df.to_csv("harness_results.csv", index=False)
    return df


if __name__ == "__main__":
    df = main(sys.argv[1:])
    print(df[["id", "kind", "desc", "on_share", "live_A_dsh", "live_B_dsh", "c5_A_dsh", "c5_B_dsh", "c5_F_dcagr", "c5_F_ddd", "c5_S1_dsh", "c5_S2_dsh", "error"]].round(3).to_string())
