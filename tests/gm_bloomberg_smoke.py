"""Smoke test for the Bloomberg adapter with a SYNTHETIC workbook (random numbers in the exact layout of
docs/data_requests/build_bloomberg.py). Checks the plumbing only: parsing, alternative commodity markets, commodity
carry from curves, the equity value composite and the growth-surprise theme. Writes nothing to the real cache.

python3 tests/gm_bloomberg_smoke.py
"""
import os
import sys
import tempfile

import numpy as np
import pandas as pd
from openpyxl import Workbook

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "data_requests"))

import build_bloomberg as BB  # noqa: E402
from gm import bloomberg as BBG  # noqa: E402


def fake_workbook(path):
    rng = np.random.default_rng(1)
    dates = pd.date_range("1990-01-31", "2026-09-30", freq="ME")
    wb = Workbook()
    wb.active.title = "Read me"

    def sheet(name, cols, fields):
        s = wb.create_sheet(name)
        step = len(fields) + 2
        for j, (label, tk) in enumerate(cols):
            c = 1 + step * j
            s.cell(2, c, label)
            s.cell(3, c, tk)
            s.cell(4, c, "date")
            for i, f in enumerate(fields):
                s.cell(4, c + 1 + i, f)
            lvl = 100 * np.exp(np.cumsum(rng.normal(0.003, 0.05, len(dates))))
            for r, d in enumerate(dates):
                s.cell(5 + r, c, d.to_pydatetime())
                for i, f in enumerate(fields):
                    v = {"PE_RATIO": 15, "BEST_PE_RATIO": 14, "PX_TO_BOOK_RATIO": 2, "EQY_DVD_YLD_12M": 3,
                         "ECO_RELEASE_DT": None}.get(f)
                    if f in ("ACTUAL_RELEASE", "BN_SURVEY_MEDIAN"):
                        v = 50 + rng.normal(0, 2)
                    elif f == "BEST_EPS":
                        v = float(lvl[r]) / 15
                    elif v is not None:
                        v = v * (1 + rng.normal(0, 0.1))
                    else:
                        v = float(lvl[r])
                    if v is not None:
                        s.cell(5 + r, c + 1 + i, float(v))

    rets = [(n + " GSCI ER", g) for n, g, b, *_ in BB.C + BB.ALT if g]
    curves = []
    for n, g, b, c1, c2, c12 in BB.C + BB.ALT:
        curves += [(n + " 1st", c1), (n + " 2nd", c2), (n + " ~12m", c12)]
    sheet("Economics", BB.ECO, ["ECO_RELEASE_DT", "ACTUAL_RELEASE", "BN_SURVEY_MEDIAN", "PX_LAST"])
    sheet("Returns", rets, ["PX_LAST"])
    sheet("Curves", curves[:30], ["PX_LAST"])
    sheet("RatesFutures", BB.RATES_FUT[:6], ["PX_LAST"])
    sheet("EquityValuation", BB.EQ_VAL, ["PE_RATIO", "BEST_PE_RATIO", "PX_TO_BOOK_RATIO", "EQY_DVD_YLD_12M", "BEST_EPS"])
    wb.save(path)


def main():
    tmp = tempfile.mkdtemp()
    path = os.path.join(tmp, "Bloomberg_macro_UBC.xlsx")
    fake_workbook(path)
    BBG.PATH = path
    BBG._CACHE.clear()
    wb = BBG.load()
    assert {"Economics", "Returns", "Curves", "EquityValuation"} <= set(wb), wb.keys()
    r = BBG.commodity_return("cm_cocoa")
    assert r.notna().sum() > 300, "alternative commodity return missing"
    c = BBG.commodity_carry("cm_wti")
    assert c.notna().sum() > 300, "curve carry missing"
    v = BBG.value_composite(["eq_us_spx", "eq_jp_nikkei", "eq_br_ibov", "eq_in"])
    assert v.notna().sum().sum() > 1000, "value composite missing"
    s = BBG.surprise("NAPMPMI Index")
    assert s.notna().sum() > 300, "surprise missing"
    m = BBG.short_rate_market()
    assert m.notna().sum() > 300, "short-rate market missing"
    from gm import panel as P
    R, SRC, FLAG, rf = P.build()
    alts = [k for k in R.columns if k in BBG.ALT_COMMOD]
    assert len(alts) >= 5, alts
    print("BLOOMBERG SMOKE PASSED: sheets %s; alternative markets %d; carry rows %d; value cells %d" % (
        sorted(wb), len(alts), c.notna().sum(), v.notna().sum().sum()))


if __name__ == "__main__":
    main()
