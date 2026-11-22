"""LSEG unadjusted month-end close (2026-11-22; plan v0.4 step 3, stage A fix). The monthly files' TR.PriceClose is
split-adjusted to today's share basis while TR.SharesOutstanding is as reported, so close x shares is wrong before a
split and the $5 price floor (R3) would use adjusted prices. This file pulls the close as traded (Adjusted=0) for the
5,537 selected lines, plus a check block (Apple and Nvidia, adjusted and unadjusted, around their splits).
usage: python3 docs/data_requests/build_lseg_unadjusted.py SELECTED.csv OUT_DIR"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_lseg_equity_probe as v1  # noqa: E402

SEL, OUT = sys.argv[1], sys.argv[2]
rows = list(csv.DictReader(open(SEL)))
BLOCK = 500
FIELDS = "TR.PriceClose.date;TR.PriceClose"
PARAMS = "SDate=2009-12-31 EDate=2026-10-31 Frq=M Adjusted=0 curn=USD CH=Fd RH=IN"
v1.P.clear()
v1.END, v1.OUT, v1.READ_DATE = "2026-11-22", OUT, "2026-11-22"
v1.NAME = "12_LSEG_monthly_unadjusted_close_v3.xlsx"
v1.TITLE = "LSEG month-end close as traded (Adjusted=0), %d lines, 2009-12 to 2026-10" % len(rows)
v1.TEST = [(r["NAME"], r["ISIN"], r["DSCD"], r["TIME"], r["EXMNEM"]) for r in rows]
sheets = {}
for k, lo in enumerate(range(0, len(rows), BLOCK)):
    hi = min(lo + BLOCK, len(rows))
    sh = "U%d" % (k + 1)
    sheets[sh] = 105000
    v1.P.append(dict(group="1 Unadjusted close", sheet=sh, what="lines %d-%d: month-end close as traded" % (lo + 1, hi),
                     f=v1.rd("TestSet!$B$%d:$B$%d" % (4 + lo, 3 + hi), FIELDS, PARAMS), cite="guess", src="S46", pair="",
                     kind="series", w=None))
sheets["Check2"] = 400
for ric in ("AAPL.O", "NVDA.O"):
    for adj in ("1", "0"):
        v1.P.append(dict(group="2 Check", sheet="Check2", what="%s close Adjusted=%s 2014-2024" % (ric, adj),
                         f=v1.rd(ric, FIELDS, "SDate=2014-01-31 EDate=2024-12-31 Frq=M Adjusted=%s CH=Fd RH=IN" % adj),
                         cite="guess", src="S46", pair="", kind="series", w=None))
v1.ROWN = sheets
v1.main()
