"""LSEG monthly files (2026-11-21; plan v0.4 step 3, stage A): month-end close, shares, company market value, monthly
volume and one-month total return, 2009-12 .. 2026-10, for the lines selected from the size file (companies among the
2,500 largest at any year-end 2009-2025; preferred, debt, fund and warrant lines dropped). Identifiers stay on the PC.
One workbook per part (about 2,000 lines); blocks of 250 lines (about 50,000 rows each).
usage: python3 docs/data_requests/build_lseg_monthly.py SELECTED.csv OUT_DIR"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_lseg_equity_probe as v1  # noqa: E402

SEL, OUT = sys.argv[1], sys.argv[2]
rows = list(csv.DictReader(open(SEL)))
PART, BLOCK = 2000, 250
FIELDS = "TR.PriceClose.date;TR.PriceClose;TR.SharesOutstanding;TR.CompanyMarketCap;TR.Volume;TR.TotalReturn1Mo"
PARAMS = "SDate=2009-12-31 EDate=2026-10-31 Frq=M curn=USD CH=Fd RH=IN"
assert len(FIELDS) <= 255 and len(PARAMS) <= 255
parts = [rows[i:i + PART] for i in range(0, len(rows), PART)]
for p, part in enumerate(parts, 1):
    v1.P.clear()
    v1.END = "2026-11-21"
    v1.OUT = OUT
    v1.NAME = "LSEG_monthly_part%d_v1.xlsx" % p
    v1.TITLE = "LSEG monthly file part %d of %d (%d lines; month-end 2009-12 to 2026-10)" % (p, len(parts), len(part))
    v1.READ_DATE = "2026-11-21"
    v1.TEST = [(r["NAME"], r["ISIN"], r["DSCD"], r["TIME"], r["EXMNEM"]) for r in part]
    sheets = {}
    for k, lo in enumerate(range(0, len(part), BLOCK)):
        hi = min(lo + BLOCK, len(part))
        sh = "M%d" % (k // 2 + 1)          # two blocks per sheet
        sheets[sh] = 60000
        v1.P.append(dict(group="1 Monthly", sheet=sh, what="lines %d-%d: month-end close, shares, company value, volume, 1-month total return" % (lo + 1, hi),
                         f=v1.rd("TestSet!$B$%d:$B$%d" % (4 + lo, 3 + hi), FIELDS, PARAMS), cite="cited", src="S46", pair="", kind="series", w=None))
    if p == 1:
        sheets["Check2"] = 6000
        v1.P.append(dict(group="2 Volume check", sheet="Check2", what="Crocs: is monthly TR.Volume the month's total? daily volume 2024 (sum it by month)",
                         f=v1.rd("CROX.O", "TR.Volume.date;TR.Volume", "SDate=2024-01-01 EDate=2024-12-31 Frq=D CH=Fd RH=IN"), cite="cited", src="S46", pair="", kind="series", w=None))
        v1.P.append(dict(group="2 Volume check", sheet="Check2", what="Crocs: monthly TR.Volume 2024", f=v1.rd("CROX.O", "TR.Volume.date;TR.Volume", "SDate=2024-01-01 EDate=2024-12-31 Frq=M CH=Fd RH=IN"),
                         cite="cited", src="S46", pair="", kind="series", w=None))
    v1.ROWN = sheets
    v1.SOURCES = [s for s in v1.SOURCES if s[0] != "S46"] + [("S46", "repo: docs/research/equity/LSEG_equity_probe2_2026-11-20.md",
                                                           "S&P 500 x monthly TR.TotalReturn (about 94,000 rows) and close / market value / shares / volume monthly for 32 companies returned on this PC")]
    v1.main()
