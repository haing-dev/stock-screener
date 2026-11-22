"""LSEG piece P19 (2026-11-22): sector for every company from Datastream (static, latest value).

Why: piece P01 (Workspace TR.GICS*, today's code) is empty for 1,874 of 5,065 companies, nearly all of them dead
(acquired or delisted before 2026). Among the 1,500 largest companies GICS is known for 66% in 2010 and 99% in 2025,
so a book that drops stocks without a sector would drop the companies that later died (survivorship bias).
Datastream keeps static data of dead companies: probe 2 (E-133) returned NAME, GGISN, INDM and ICBIN for all 11 dead
test companies. This piece asks for those four (cited) plus WC07021 (Worldscope SIC code 1, a guess) for ALL 5,065
companies, so that the companies with both P01 GICS and a Datastream code give the crosswalk for the ones without.

One DSGRID per 15 ISINs (Excel caps a text argument at 255 characters); about 25,000 values in all.
usage: python3 docs/data_requests/build_lseg_sector_fix.py COMPANIES.csv OUT_DIR"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_lseg_equity_probe as v1  # noqa: E402

COMP, OUT = sys.argv[1], sys.argv[2]
comp = list(csv.DictReader(open(COMP)))
FIELDS = "NAME,GGISN,INDM,ICBIN,WC07021"
PER, PER_SHEET = 15, 40

v1.P.clear()
v1.END, v1.OUT, v1.READ_DATE = "2026-11-22", OUT, "2026-11-22"
v1.NAME = "P19_LSEG_sector_Datastream_all_v4.xlsx"
v1.TITLE = "LSEG piece P19: Datastream sector of every company (incl. dead), static"
v1.TEST = [(r["COMPANY"], r["ISIN"], r["LINE_NAME"], r["TIME"], "") for r in comp]
v1.SOURCES = [s for s in v1.SOURCES if s[0] != "S47"] + [("S47", "repo: docs/research/equity/LSEG_pieces_P_read_2026-11-22.md",
                                                       "P01 GICS empty for dead companies; probe 2 E-133: NAME, GGISN, INDM, ICBIN returned for 11 dead test companies")]
rown = {}
for k, lo in enumerate(range(0, len(comp), PER)):
    chunk = comp[lo:lo + PER]
    codes = ",".join(r["ISIN"] for r in chunk)
    sh = "D%d" % (k // PER_SHEET + 1)
    rown[sh] = 40
    v1.add("D", sh, "companies %d-%d: Datastream NAME, GICS industry (GGISN), industry (INDM, ICBIN), SIC (WC07021, a guess)" % (lo + 1, lo + len(chunk)),
           v1.dss(codes, FIELDS), "cited", "S47", kind="static", w=9)
v1.ROWN = rown
v1.main()
print("formulas", len(v1.P), "sheets", len(rown), "companies", len(comp))
