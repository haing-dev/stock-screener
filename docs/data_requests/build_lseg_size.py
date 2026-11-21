"""LSEG size file (2026-11-21; plan v0.4 step 3, stage A0): year-end market value 2009-2025 for every
candidate US company (universe_candidates_v1.csv, built from the Datastream lists: type EQ, Datastream geography United
States, primary line, alive at some point 2010-2025; LSEG identifiers stay on the PC, never in the repo). The result
selects the companies that get monthly and account data (stage A / B): those that could be among the 1,500 largest.
Companies are given by ISIN (dead ones work by ISIN); companies without an ISIN are listed in the file for a later
Datastream pass.
usage: python3 docs/data_requests/build_lseg_size.py CANDIDATES.csv OUT_DIR"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_lseg_equity_probe as v1  # noqa: E402

CAND, OUT = sys.argv[1], sys.argv[2]
rows = list(csv.DictReader(open(CAND)))
withisin = [r for r in rows if r["ISIN"] and len(r["ISIN"]) == 12]
noisin = [r for r in rows if r not in withisin]
v1.END = "2026-11-21"
v1.OUT = OUT
v1.NAME = "LSEG_size_v1.xlsx"
v1.TITLE = "LSEG size file 1 (year-end market value 2009-2025, %d US candidates)" % len(withisin)
v1.READ_DATE = "2026-11-21"
v1.P.clear()
v1.TEST = [(r["NAME"], r["ISIN"], r["DSCD"], r["TIME"], r["EXMNEM"]) for r in withisin] + \
          [(r["NAME"], "", r["DSCD"], r["TIME"], r["EXMNEM"]) for r in noisin]
BLOCK = 1000
SETS = [["TR.CommonName"] + ["TR.CompanyMarketCap(SDate=%d-12-31)" % y for y in range(2009, 2015)],
        ["TR.CompanyMarketCap(SDate=%d-12-31)" % y for y in range(2015, 2021)],
        ["TR.CompanyMarketCap(SDate=%d-12-31)" % y for y in range(2021, 2026)]]   # Excel caps a text argument at 255 characters
n = len(withisin)
for k, lo in enumerate(range(0, n, BLOCK)):
    hi = min(lo + BLOCK, n)
    rng = "TestSet!$B$%d:$B$%d" % (4 + lo, 3 + hi)
    for j, fs in enumerate(SETS):
        v1.P.append(dict(group="1 Size", sheet="Size%d" % (j + 1), what="companies %d-%d: %s" % (lo + 1, hi, ("name, market value at year-ends 2009-2014", "market value at year-ends 2015-2020", "market value at year-ends 2021-2025")[j]),
                         f=v1.rd(rng, ";".join(fs), "curn=USD CH=Fd RH=IN"), cite="cited", src="S46", pair="", kind="static", w=None))
v1.ROWN = {"Size1": BLOCK + 10, "Size2": BLOCK + 10, "Size3": BLOCK + 10}
v1.SOURCES = v1.SOURCES + [("S46", "repo: docs/research/equity/LSEG_equity_probe2_2026-11-20.md",
                            "TR.CompanyMarketCap(SDate=...) over 17,000 screen rows and dead companies by ISIN returned values on this PC")]
if __name__ == "__main__":
    v1.main()
    print("with ISIN %d, without ISIN %d (listed at the end of TestSet, not pulled)" % (len(withisin), len(noisin)))
