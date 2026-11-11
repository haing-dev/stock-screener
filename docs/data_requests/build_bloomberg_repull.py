"""Re-pull workbooks (R1-R7) for the series that came back cut off or still loading in the first Bloomberg pull.

Source of truth for WHAT to pull: the data check of lock v1 (tools/bbgq/results/bbg_check_v1.txt, metadata only):
  file 1: the ten sheets whose history starts in 2009-06 (all tickers except invalid ones)
  file 3: all eight sheets (history starts in 2004-04)
  file 5: only the tickers saved while 'Requesting Data'      file 4: the 8 EquityIndexes tickers still loading
Same block layout and BDH formula as the first pull (row 2 label, row 3 ticker, row 4 'date' + fields, row 5 BDH).
Data sheets are named '<original file digit> <original sheet>' so the reader can put each series back in its place.
New: a Check sheet with a live STATUS line (WAIT / WRONG NUMBERS / HISTORY CUT OFF / READY) and, per series, the month its history
should start by, taken from another copy of the same ticker in the first pull (daily files, file 5, file 3).

Run: python3 docs/data_requests/build_bloomberg_repull.py [out_dir]
"""
import collections
import csv
import datetime as dt
import os
import sys

import openpyxl
from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter as L

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CHECK = os.path.join(REPO, "tools", "bbgq", "results", "bbg_check_v1.txt")
F = "Arial"
YEL = PatternFill("solid", start_color="FFFF00")
GREEN = PatternFill("solid", start_color="C6EFCE", end_color="C6EFCE")
RED = PatternFill("solid", start_color="FFC7CE", end_color="FFC7CE")
AMBER = PatternFill("solid", start_color="FFEB9C", end_color="FFEB9C")
MON = '"Per=M","Days=A","Fill=P","Dir=V","Dts=S"'
M0 = "12/31/1969"
LAST = 900                      # last row the Check formulas look at (683 months from 1969 + room)
CUT = {"1": dt.date(2009, 6, 30), "3": dt.date(2004, 4, 30)}      # where the first pull was cut off
F1_SHEETS = ["RatesFutures", "SpotRates3m", "Yields", "BondFutures", "Breakevens", "Benchmarks", "Surprise", "FXBasis",
             "Curves", "Returns"]

# (file name, title, [(original file digit, original sheet, first block, last block or None)])
PLAN = [
    ("R1_rates_yields_bondfutures.xlsx", "short-rate futures, 3m rates, yields, bond futures, breakevens, benchmarks, surprise",
     [("1", s, 0, None) for s in F1_SHEETS[:8]]),
    ("R2_commodity_curves_returns.xlsx", "commodity curves and commodity excess-return indexes",
     [("1", "Curves", 0, None), ("1", "Returns", 0, None)]),
    ("R3_commodities_missing_A.xlsx", "commodities that were still loading: front contracts, indexes, fundamentals, curve part 1; 8 equity indexes",
     [("5", "ComFront", 0, None), ("5", "ComIndexes", 0, None), ("5", "ComFundamentals", 0, None),
      ("4", "EquityIndexes", 0, None), ("5", "ComCurve", 0, 100)]),
    ("R4_commodities_missing_B.xlsx", "commodities that were still loading: curve part 2",
     [("5", "ComCurve", 100, None)]),
    ("R5_yields_swaps_credit.xlsx", "extra yields, swaps, credit",
     [("3", "YieldsExtra", 0, None), ("3", "Swaps", 0, None), ("3", "Credit", 0, None)]),
    ("R6_fx_spot_forwards_ratesfut.xlsx", "FX spot, FX forwards, cross-currency basis, extra short-rate futures",
     [("3", "FXSpot", 0, None), ("3", "FXForwards", 0, None), ("3", "FXBasis", 0, None), ("3", "RatesFutExtra", 0, None)]),
    ("R7_fx_vol.xlsx", "FX implied volatility, risk reversals, butterflies",
     [("3", "FXVol", 0, None)]),
]


def read_check():
    """-> status[(file, sheet, ticker)] (worst over fields), first[(ticker, field)] = earliest first date of any copy."""
    lines = open(CHECK, encoding="utf-8").read().splitlines()
    a = next(i for i, l in enumerate(lines) if l.startswith("=== SERIES"))
    b = next(i for i, l in enumerate(lines) if l.startswith("--- must-have"))
    status, first = {}, {}
    for l in lines[a + 1:b]:
        p = [x.strip() for x in l.split("|")]
        if len(p) < 8:
            continue
        f, sh, tk, fld, st, d0 = p[:6]
        k = (f, sh, tk)
        if st != "ok" or k not in status:
            status[k] = st if st != "ok" else status.get(k, "ok")
        if st == "ok" and d0 != "-":
            d = dt.date.fromisoformat(d0)
            if (f == "1" and sh in F1_SHEETS and d >= CUT["1"]) or (f == "3" and d >= CUT["3"]):
                continue                                   # a cut-off copy says nothing about the true start
            if (tk, fld) not in first or d < first[(tk, fld)]:
                first[(tk, fld)] = d
    return status, first


def blocks_file1():
    """(sheet -> [(label, ticker, fields)]) from the v4 template of file 1."""
    wb = openpyxl.load_workbook(os.path.join(HERE, "Bloomberg_macro_UBC.xlsx"), read_only=True)
    out = {}
    for ws in wb.worksheets:
        if ws.title not in F1_SHEETS:
            continue
        r2, r3, r4 = [list(r) for r in ws.iter_rows(min_row=2, max_row=4, values_only=True)]
        bl = []
        for c, tk in enumerate(r3):
            if not (isinstance(tk, str) and tk.strip()):
                continue
            fields, k = [], c + 1
            while k < len(r4) and isinstance(r4[k], str) and r4[k].strip() and r4[k].strip().lower() != "date":
                fields.append(r4[k].strip())
                k += 1
            bl.append((str(r2[c] or "").strip(), tk.strip(), ",".join(fields)))
        out[ws.title] = bl
    wb.close()
    return out


def blocks_v5():
    out = collections.defaultdict(list)
    for r in csv.DictReader(open(os.path.join(HERE, "bloomberg_v5", "bloomberg_v5_tickers.csv"))):
        out[(r["file"][:1], r["sheet"])].append((r["label"], r["ticker"], r["fields"]))
    return out


def select():
    """-> {(digit, sheet): [(label, ticker, fields, expected first date or None)]} = what to re-pull."""
    status, first = read_check()
    f1, v5 = blocks_file1(), blocks_v5()
    sel = {}
    for digit, sheet in sorted({(d, s) for _f, _t, parts in PLAN for d, s, _a, _b in parts}):
        src = f1[sheet] if digit == "1" else v5[(digit, sheet)]
        keep = []
        for lab, tk, fields in src:
            st = status.get((digit, sheet, tk), "missing")
            if digit in ("1", "3"):
                ok = st != "invalid"                       # everything that is a real ticker
            else:
                ok = st == "requesting"                    # only what was saved while still loading
            if ok:
                keep.append((lab, tk, fields, first.get((tk, fields.split(",")[0]))))
        sel[(digit, sheet)] = keep
    return sel


def data_sheet(wb, name, blocks):
    s = wb.create_sheet(name)
    s.cell(1, 1, "Monthly from 1969 (a series starts when it starts). Yellow = ticker. Do not edit; look at the Check sheet.").font = Font(name=F, italic=True)
    pos = []
    c = 1
    for lab, tk, fields, _exp in blocks:
        fl = fields.split(",")
        s.cell(2, c, lab).font = Font(name=F, bold=True)
        t = s.cell(3, c, tk)
        t.font = Font(name=F)
        t.fill = YEL
        s.cell(4, c, "date").font = Font(name=F, italic=True)
        for i, f in enumerate(fl):
            s.cell(4, c + 1 + i, f).font = Font(name=F, italic=True)
        s.cell(5, c, '=BDH(%s3,"%s","%s","",%s)' % (L(c), fields, M0, MON)).font = Font(name=F)
        s.column_dimensions[L(c)].width = 11
        for i in range(len(fl)):
            s.column_dimensions[L(c + 1 + i)].width = 13
        s.column_dimensions[L(c + len(fl) + 1)].width = 2
        pos.append(c)
        c += len(fl) + 2
    s.freeze_panes = "A5"
    return pos


STEPS = [
    "1. Open this file in Excel on the Bloomberg terminal (Bloomberg tab visible). If a yellow bar says Protected View, click Enable Editing.",
    "2. Stay on this sheet and watch the STATUS line. Do nothing while it says WAIT (a few minutes).",
    "3. READY (green): save it the same way as last time, keeping the file name. Then open the next file (R1 to R7, in this order).",
    "4. Still WAIT or NOT LOADED after 15 minutes: Bloomberg tab > Refresh Workbook and wait again. No change: save anyway, go on.",
    "5. WRONG NUMBERS or HISTORY CUT OFF (red): close Excel completely WITHOUT saving, open this file again and wait. Still red: save it anyway with _CUT at the end",
    "   of the name and go on to the next file. Tell Claude which files were red.",
    "6. '#N/A Limit' anywhere = the terminal's download allowance is used up. Save, stop, continue another day.",
    "Research and paper trading only. The data stays on your PC: never on GitHub, never shared.",
]
T0 = 24      # first table row on the Check sheet


def build_file(out_dir, k, fname, title, parts, sel):
    wb = Workbook()
    ck = wb.active
    ck.title = "Check"
    rows = []                                              # (sheet name, label, ticker, date col, first value col, expected)
    for digit, sheet, a, b in parts:
        blocks = sel[(digit, sheet)][a:b]
        name = "%s %s" % (digit, sheet)
        pos = data_sheet(wb, name, blocks)
        for (lab, tk, _f, exp), c in zip(blocks, pos):
            rows.append((name, lab, tk, c, c + 1, exp))
    n = len(rows)
    r1, rn = T0 + 1, T0 + n
    ck.cell(1, 1, "%s of 7: %s" % (fname.split("_")[0], title)).font = Font(name=F, bold=True, size=13)
    ck.cell(2, 1, "Re-pull of 13 Nov 2026. %d series. Monthly history from 1969." % n).font = Font(name=F, italic=True)
    ck.cell(4, 1, "STATUS").font = Font(name=F, bold=True, size=14)
    rng = lambda col: "%s%d:%s%d" % (col, r1, col, rn)     # noqa: E731
    ck.cell(6, 1, "series in this file"); ck.cell(6, 2, n)
    ck.cell(7, 1, "loaded"); ck.cell(7, 2, '=COUNTIF(%s,"ok")' % rng("D"))
    ck.cell(8, 1, "still loading"); ck.cell(8, 2, '=COUNTIF(%s,"loading")' % rng("D"))
    ck.cell(9, 1, "no data or wrong ticker"); ck.cell(9, 2, '=COUNTIF(%s,"no data")' % rng("D"))
    ck.cell(10, 1, "history cut off"); ck.cell(10, 2, '=COUNTIF(%s,"CUT")' % rng("H"))
    ck.cell(11, 1, "history checked and complete"); ck.cell(11, 2, '=COUNTIF(%s,"ok")' % rng("H"))
    ck.cell(12, 1, "not on a Bloomberg terminal"); ck.cell(12, 2, '=COUNTIF(%s,"no Bloomberg")' % rng("D"))
    ck.cell(13, 1, "same numbers as another series"); ck.cell(13, 2, '=COUNTIF(%s,"COPY")' % rng("K"))
    st = ck.cell(4, 2, '=IF(B12>0,"NOT CONNECTED: open this file on the Bloomberg terminal",'
                       'IF(B8>0,"WAIT: "&B8&" of "&B6&" series still loading",'
                       'IF(B7<0.5*B6,"NOT LOADED: only "&B7&" of "&B6&" series have data: see step 4",'
                       'IF(B13>=5,"WRONG NUMBERS: "&B13&" series hold the numbers of another series: see step 5",'
                       'IF(B10>=3,"HISTORY CUT OFF in "&B10&" series: see step 5",'
                       '"READY: save now (step 3)")))))')
    st.font = Font(name=F, bold=True, size=14)
    ck.conditional_formatting.add("B4", FormulaRule(formula=['ISNUMBER(SEARCH("READY",$B$4))'], fill=GREEN))
    ck.conditional_formatting.add("B4", FormulaRule(formula=['ISNUMBER(SEARCH("WAIT",$B$4))'], fill=AMBER))
    ck.conditional_formatting.add("B4", FormulaRule(formula=['OR(ISNUMBER(SEARCH("CUT",$B$4)),ISNUMBER(SEARCH("NOT ",$B$4)),ISNUMBER(SEARCH("WRONG",$B$4)))'], fill=RED))
    for i, t in enumerate(STEPS):
        ck.cell(14 + i, 1, t).font = Font(name=F)
    for j, h in enumerate(("sheet", "label", "ticker", "status", "first month with data", "months with data",
                           "should start by", "history", "cut-off month of the first pull", "fingerprint", "copy")):
        ck.cell(T0, j + 1, h).font = Font(name=F, bold=True)
    for i, (name, lab, tk, c, v, exp) in enumerate(rows):
        r = r1 + i
        q = "'%s'!" % name
        dcell = "%s%s5" % (q, L(c))
        dcol = "%s%s5:%s%d" % (q, L(c), L(c), LAST)
        vcol = "%s%s5:%s%d" % (q, L(v), L(v), LAST)
        ck.cell(r, 1, name)
        ck.cell(r, 2, lab)
        ck.cell(r, 3, tk).fill = YEL
        ck.cell(r, 4, '=IF(ISERROR(%s),"no Bloomberg",IF(ISNUMBER(%s),IF(COUNT(%s)>0,"ok","no data"),IF(ISNUMBER(SEARCH("Requesting",%s&"")),"loading","no data")))'
                % (dcell, dcell, vcol, dcell))
        ck.cell(r, 5, '=IFERROR(INDEX(%s,MATCH(TRUE,INDEX(ISNUMBER(%s),0),0)),"")' % (dcol, vcol)).number_format = "mmm yyyy"
        ck.cell(r, 6, '=IFERROR(COUNT(%s),0)' % vcol)
        if exp is not None:
            ck.cell(r, 7, exp).number_format = "mmm yyyy"
        if name[0] in CUT:                                 # no other copy to compare with: same cut month as last time = cut again
            ck.cell(r, 9, CUT[name[0]]).number_format = "mmm yyyy"
        ck.cell(r, 8, '=IF(AND(D%d="ok",ISNUMBER(E%d)),IF(ISNUMBER(G%d),IF(E%d>G%d+45,"CUT","ok"),IF(AND(ISNUMBER(I%d),ABS(E%d-I%d)<20),"CUT","")),"")'
                % (r, r, r, r, r, r, r, r))
        # first pull, files 1 and 3: hundreds of blocks held the numbers of ONE other series (bbg_diag_v2). A block whose
        # count and sum of values equal another block's, more often than its ticker is listed, is such a copy.
        ck.cell(r, 10, '=IF(D%d="ok",IFERROR(F%d&"|"&SUM(%s),""),"")' % (r, r, vcol))
        ck.cell(r, 11, '=IF(J%d="","",IF(COUNTIF(J$%d:J$%d,J%d)>COUNTIF(C$%d:C$%d,C%d),"COPY",""))' % (r, r1, rn, r, r1, rn, r))
    ck.conditional_formatting.add("H%d:H%d" % (r1, rn), FormulaRule(formula=['$H%d="CUT"' % r1], fill=RED))
    ck.conditional_formatting.add("K%d:K%d" % (r1, rn), FormulaRule(formula=['$K%d="COPY"' % r1], fill=RED))
    ck.conditional_formatting.add("D%d:D%d" % (r1, rn), FormulaRule(formula=['$D%d="loading"' % r1], fill=AMBER))
    for col, w in zip("ABCDEFGHIJK", (30, 44, 30, 14, 20, 16, 16, 10, 28, 24, 8)):
        ck.column_dimensions[col].width = w
    ck.column_dimensions["B"].alignment = Alignment(wrap_text=False)
    ck.freeze_panes = "A%d" % r1
    wb.active = 0
    wb.save(os.path.join(out_dir, fname))
    return n, sum(1 for x in rows if x[5] is not None), rows


def main(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    sel = select()
    master = []
    for k, (fname, title, parts) in enumerate(PLAN, 1):
        n, nexp, rows = build_file(out_dir, k, fname, title, parts, sel)
        print("%-36s %4d series | %3d with a known start month | sheets: %s" % (
            fname, n, nexp, ", ".join("%s (%d)" % (s, c) for s, c in collections.Counter(r[0] for r in rows).items())))
        master += [(fname, r[0], r[1], r[2], r[5].isoformat() if r[5] else "") for r in rows]
    with open(os.path.join(out_dir, "repull_tickers.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(("file", "sheet", "label", "ticker", "should_start_by"))
        w.writerows(master)
    print("total series", len(master), "| unique tickers", len({m[3] for m in master}))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "bloomberg_repull_2026-11-13"))
