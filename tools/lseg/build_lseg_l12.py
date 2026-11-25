"""L12_identity_evidence.xlsx: evidence to check the rule-based contract calendar (lseg_rules.py), after the L11
refresh of 2026-11-24 showed that LSEG returns no contract dates on this licence (TR.ExpiryDate NULL, TR.LastTradeDate
"access denied", other names "no output").
Sheets (only forms that returned dated data in L11):
  Identity probe  TR.ExpiryDate as a dated MONTHLY series on continuation RICs (worked for CLc1 and GCc1 2005-06 in L11):
                  positions 1, 2 and the deepest a spec uses, full history, for every HistoricalPricing root. Each date
                  shows the expiry of the contract the position held: a direct check of the rule calendar.
  Contract sample expired contracts in the forms that worked in L11 (RDP.HistoricalPricing "CLZ5^9", Datastream
                  "<EDZ5^0>"): DAILY from 4 months before to the end of the delivery month (the last date with a price
                  = the observed last trading day; matched to c1 / c2 it shows the roll day) for four eras per root, one
                  serial-month contract per root that may list serial months (does LSEG's cN step through them?), and
                  MONTHLY over the life for two contracts per root (which position held it, at depth). Short sterling and
                  Euroswiss in the RIC form (their Datastream form was invalid in L11).
  Strip daily     Euribor (HistoricalPricing) and short sterling / Euroswiss (Datastream) contracts 3-8 daily (Strip
                  reversion: eight daily contracts).
usage: python3 build_lseg_l12.py [out dir]"""
import datetime as dt
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter as L

import build_lseg_contract_pull as B11

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out")
NAME = "L12_identity_evidence"
ROW0 = 6
END = "24-Nov-2026"
SERIAL = {"GC": 11, "SI": 2, "HG": 2, "PL": 2, "ED": 2, "FEI": 2, "FSS": 1}   # one serial (non-cycle) month per root
RIC_FORM = {"FSS", "FES"}                     # samples via HistoricalPricing RICs instead of Datastream


def eras(fy):
    ys = [y for y in (1986, 1993, 1999, 2004, 2009) if y >= fy + 1]
    return ys[-4:]


def build(out_dir=OUT):
    roots = B11.read_roots()
    wb = Workbook()
    ck = wb.active
    ck.title = "Check"
    bold = Font(bold=True)
    sheets, pos, rows, width, rown = {}, {}, [], {}, {}

    def add(sheet, label, f, w=3, n=1000):
        if sheet not in sheets:
            sheets[sheet], pos[sheet] = wb.create_sheet(sheet), 0
            width[sheet], rown[sheet] = w, n
        ws, c = sheets[sheet], 1 + pos[sheet] * w
        pos[sheet] += 1
        pid = "L12-%03d" % (len(rows) + 1)
        ws.cell(2, c, pid).font = bold
        ws.cell(3, c, label)
        ws.cell(4, c, "formula: " + f[1:])
        ws.cell(ROW0, c, f)
        rows.append((pid, sheet, label, f[1:], "'%s'!%s%d" % (sheet, L(c), ROW0),
                     "'%s'!%s%d:%s%d" % (sheet, L(c), ROW0, L(c + w - 2), n)))

    for r in roots:
        if int(r["first_year"]) >= 2015:
            continue                                       # live-only roots: history sealed
        root, rr, fy = r["root"], r["ric_root"], int(r["first_year"])
        is_ds = r["c_sid_m"].startswith("DS:")
        depth = B11.positions(r["depth_m"]) + B11.positions(r["depth_m_l11"])
        # A. TR.ExpiryDate dated series on continuation RICs (HistoricalPricing roots only: RIC continuations)
        if not is_ds:
            for n in sorted({1, 2, max(depth)}):
                add("Identity probe", "%sc%d: TR.ExpiryDate monthly %d-2026 (held contract's expiry)" % (rr, n, fy),
                    B11.rd("%sc%d" % (rr, n), "TR.ExpiryDate.date;TR.ExpiryDate",
                           "SDate=%d-01-01 EDate=2026-11-24 Frq=M CH=Fd RH=IN" % fy), 4, 560)
        m0 = B11.MONTHS.index(r["sample_month"].strip() or "Z") + 1
        use_ric = (not is_ds) or root in RIC_FORM

        def contract(y, m):
            base = r["ric_root_alt"] if r.get("ric_root_alt") and y < int(r.get("alt_until") or 0) else rr
            return B11.ric(base, y, m, True)

        def daily(y, m, why):
            code = contract(y, m)
            s = dt.date(y - (m <= 4), (m - 5) % 12 + 1, 1)
            e = dt.date(y + (m == 12), m % 12 + 1, 1) - dt.timedelta(days=1)
            if use_ric:
                f = B11.hp(code, start=s.strftime("%d-%b-%Y"), end=e.strftime("%d-%b-%Y"), interval="P1D")
            else:
                f = B11.ds("<%s>" % code, start=s.isoformat(), end=e.isoformat(), frq="D")
            add("Contract sample", "%s %s daily around expiry (%s)" % (r["name"], code, why), f, 3, 160)
        # B. daily around expiry, four eras; one serial month
        for y in eras(fy):
            daily(y, m0, "era %d" % y)
        if root in SERIAL:
            daily(2005 if fy < 2004 else 2009, SERIAL[root], "serial month")
        # C. monthly over the life, two contracts
        for y in [y for y in (1990, 2000) if y >= fy + 3][:2] or [2008]:
            code = contract(y, m0)
            if use_ric:
                f = B11.hp(code, start="01-Jan-%d" % (y - 4), end="31-Dec-%d" % y)
            else:
                f = B11.ds("<%s>" % code, start="%d-12-31" % (y - 5), end="%d-12-31" % y)
            add("Contract sample", "%s %s monthly over its life" % (r["name"], code), f, 3, 80)
    # D. strip contracts 3-8 daily
    for root, form in (("FEI", "hp"), ("FSS", "ds"), ("FES", "ds")):
        r = next(x for x in roots if x["root"] == root)
        s = "%d-01-01" % int(r["first_year"])
        for n in range(3, 9):
            if form == "hp":
                f = B11.hp("FEIc%d" % n, start="01-Jan-%s" % r["first_year"], interval="P1D")
            else:
                f = B11.ds("<%sc%d>" % (root, n), start=s, frq="D")
            add("Strip daily", "%s contract %d daily" % (r["name"], n), f, 3, 9000)
    # Check sheet
    ck["A1"] = "LSEG pull L12: contract identity evidence (expiry series, sample contracts, strip contracts 3-8)"
    ck["A1"].font = Font(bold=True, size=14)
    ck["A2"] = ("1. Open in Excel with Workspace signed in.   2. Wait until the number in B4 has not changed for one "
                "minute.   3. Press Ctrl+S (keep the file name). Errors in some blocks are expected.")
    r1, rn = 8, 7 + len(rows)
    ck["A4"] = "blocks with data"
    ck["A4"].font = bold
    ck["B4"] = '=COUNTIF(F%d:F%d,">0")&" of %d"' % (r1, rn, len(rows))
    ck["B4"].font = Font(bold=True, size=13)
    for j, h in enumerate(("id", "sheet", "what", "formula", "status", "numbers found"), 1):
        ck.cell(7, j, h).font = bold
    for k, (pid, sh, lab, ftxt, cell, rng) in enumerate(rows):
        rr_ = r1 + k
        for j, v in enumerate((pid, sh, lab, ftxt), 1):
            ck.cell(rr_, j, v)
        ck.cell(rr_, 5, '=IF(ISERROR(%s),"Excel error (add-in not loaded?)",IF(F%d>0,"data","text: "&LEFT(%s&"",70)))'
                % (cell, rr_, cell))
        ck.cell(rr_, 6, '=SUMPRODUCT(--ISNUMBER(%s))' % rng)
    for col, w in zip("ABCDEF", (10, 16, 50, 60, 60, 14)):
        ck.column_dimensions[col].width = w
    os.makedirs(out_dir, exist_ok=True)
    p = os.path.join(out_dir, NAME + ".xlsx")
    wb.save(p)
    by = {}
    for _, sh, *_ in rows:
        by[sh] = by.get(sh, 0) + 1
    print("%s.xlsx | %d formulas | %s" % (NAME, len(rows), ", ".join("%s %d" % kv for kv in by.items())))
    return p, rows


if __name__ == "__main__":
    build()
