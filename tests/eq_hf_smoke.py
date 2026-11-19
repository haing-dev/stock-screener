#!/usr/bin/env python3
"""Smoke test of tools/equity/wrds/eq_hf.py report on invented data (no WRDS)."""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools", "equity", "wrds"))
import eq_hf  # noqa: E402

rng = np.random.default_rng(1)
D = {}
D["eq_hf_names"] = pd.DataFrame({"mgrno": [1, 2, 3, 4, 5], "mgrname": ["TONTINE ASSET", "ALPHA LP", "BETA CAPITAL",
                                 "GAMMA HK", "DELTA SMALL"], "country": ["UNITED STATES", "UNITED KINGDOM",
                                 "UNITED STATES", "HONG KONG", "UNITED STATES"],
                                 "rdate1": "2000-03-31", "rdate2": "2026-03-31"})
D["eq_hf_spy"] = pd.DataFrame({"permno": 84398, "yyyymm": [y * 100 + m for y in range(2020, 2026) for m in range(1, 13)
                                                            if y * 100 + m >= 202010], "mthretx": 0.01, "mthret": 0.011})
D["eq_hf_spyname"] = pd.DataFrame({"ticker": ["SPY"]})
D["eq_hf_last"] = pd.DataFrame({"mgrno": [1, 2, 3, 4, 5], "nall": 30, "vall": [9e9, 3e9, 2e9, 5e9, 1e8]})
for d in eq_hf.QENDS:
    D["eq_hf_q_%s" % d[:7].replace("-", "")] = pd.DataFrame({
        "mgrno": [1, 2, 3, 4, 5], "nall": 30, "vall": [9e9, 3e9, 2e9, 5e9, 1e8], "ncrsp": 25, "vcrsp": 1, "n20": 20,
        "v20": [5e9, 2e9, 1e9, 3e9, 5e7], "mw_end": rng.normal(0.05, 0.1, 5), "ew_end": rng.normal(0.03, 0.1, 5),
        "n_end": 20, "mw_next": rng.normal(0.05, 0.1, 5), "ew_next": rng.normal(0.03, 0.1, 5), "n_next": 20})
lines = []
for k in (1, 2, 3):
    eq_hf.report(lambda n: D[n].copy(), lines.append, k, 3)
txt = "\n".join(lines)
assert "rank stR" in txt and "TONTINE" in txt and "GAMMA" in txt and "DELTA" not in txt.split("part 2")[1]
assert "ALPHA LP" in txt.split("part 2")[1]
# chaining check against the website's published Gendell quarters
mw = [13.72, 31.49, 4.03, 26.5, -1.59, -18.07, 66.4, 33.28, 1.3, 21.38, 51.32, -11.94]
c = eq_hf._chain(np.array(mw) / 100)
assert abs(c - 4.7652) < 1e-3 and abs(eq_hf._ann(c, 3) - 0.7931) < 1e-3
print(txt[:3000])
print("EQ_HF SMOKE PASSED")
