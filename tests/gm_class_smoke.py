"""Smoke test of the gm-2.2.1 fix (gm/CHANGES.md "gm-2.2.1 fix": cm_aqr_ew a Trend market of the CM block only) on
SYNTHETIC data (no cache): every class block of every family holds only markets with that class's prefix; cm_aqr_ew
appears only in the CM block of Trend; both code paths (old family_positions for BASE and CANDIDATE, the version path
for the A2 challenger and the component masks). python3 tests/gm_class_smoke.py   (also run from tests/run_tests.py)
"""
import os
import sys

import numpy as np
import pandas as pd

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, REPO)

from gm import book as B  # noqa: E402
from gm import config as CF  # noqa: E402
from gm import signals as G  # noqa: E402

GRID = pd.period_range("1960-01", "2010-12", freq="M")
MK = ["eq_us_spx", "eq_gb_ftse", "bd_us_10y", "st_de_2y", "fx_jpy", "fx_gbp", "cm_wti", "cm_gold", "cm_aqr_ew"]


def scenario(seed=4):
    rng = np.random.default_rng(seed)
    n = len(GRID)
    R = pd.DataFrame(rng.normal(0.003, 0.03, (n, len(MK))), index=GRID, columns=MK)
    R.loc[R.index < pd.Period("1968-01", "M")] = np.nan
    R.loc[R.index > pd.Period("2000-12", "M"), "cm_aqr_ew"] = np.nan
    S = {k: pd.DataFrame(rng.normal(0, 1, (n, len(MK))), index=GRID, columns=MK).where(R.notna())
         for k in ("E", "C", "V", "V2")}
    S["E"] = np.tanh(S["E"] / 2)
    S["E_sign"] = np.sign(S["E"])
    days = pd.bdate_range("1968-01-02", "2010-12-31")
    D = pd.DataFrame(rng.normal(0, 0.008, (len(days), 3)), index=days, columns=["eq_us_spx", "bd_us_10y", "fx_jpy"])
    return R, D, S


def bad_cols(fam):
    """[(family, class, column)] where a block holds a column of another class (cm_aqr_ew allowed only in trend/CM)."""
    out = []
    for f, blocks in fam.items():
        for c, p in blocks.items():
            cols = p.columns if isinstance(p, pd.DataFrame) else set().union(*[t.columns for t in p])
            for k in cols:
                if k == "cm_aqr_ew":
                    if not (c == "CM" and f == "trend"):
                        out.append((f, c, k))
                elif not k.startswith(G.CLASSES[c]):
                    out.append((f, c, k))
    return out


def run(check):
    R, D, S = scenario()
    for name in ("BASE", "CANDIDATE", "A1_INCUMBENT"):
        fam, _vol = B.family_positions(R, getattr(CF, name), D, S)
        bad = bad_cols(fam)
        check("gm-2.2.1 class blocks (%s, old path): every block holds only its class's markets; cm_aqr_ew only in "
              "trend/CM" % name, not bad and "cm_aqr_ew" in fam["trend"]["CM"].columns, bad[:5])
    fam, _vol, comp = B.family_positions(R, CF.A2_CHALLENGER, D, S)
    bad = bad_cols(fam) + bad_cols(comp)
    check("gm-2.2.1 class blocks (A2 challenger, version path and components): only the class's markets; cm_aqr_ew "
          "only in trend/CM", not bad and "cm_aqr_ew" in fam["trend"]["CM"].columns and
          all("cm_aqr_ew" in t.columns for t in comp["trend"]["CM"]), bad[:5])
    fam, _vol, comp = B.family_positions(R, CF.CANDIDATE, D, S, components=True)
    check("gm-2.2.1 class blocks (CANDIDATE, components=True): only the class's markets",
          not bad_cols(fam) and not bad_cols(comp), (bad_cols(fam) + bad_cols(comp))[:5])
    bk = B.run(R, cfg=CF.CANDIDATE, daily=D, S=S)
    t = bk["fam_pos"]["trend"]
    check("gm-2.2.1 cm_aqr_ew still holds a Trend position (CM block) and none in any other family",
          float(t["cm_aqr_ew"].abs().sum()) > 0 and all(float(bk["fam_pos"][f]["cm_aqr_ew"].abs().sum()) == 0
                                                        for f in bk["fam_pos"] if f != "trend"))


if __name__ == "__main__":
    fails = []

    def check(name, ok, detail=""):
        print(("PASS " if ok else "FAIL ") + name + ("" if ok else "  " + str(detail)[:400]))
        if not ok:
            fails.append(name)
    run(check)
    print("GM CLASS SMOKE " + ("PASSED" if not fails else "FAILED: %d" % len(fails)))
    sys.exit(1 if fails else 0)
