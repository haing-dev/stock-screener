"""L13 contract-level prices: exact contract identity for the pods that need contracts beyond position 2.
Why: the listing-rule fit (lseg_ident_v4, 2026-11-25) identifies positions 1-2 almost exactly (TR.ExpiryDate series)
but deeper positions only at 85-99% for most roots; Curve carry (legs 3 to ~16 months out) and Strip reversion
(quarterly contracts 1-8) need identity per observation (TESTING_PROTOCOL 7.10 item 3; SPEC_Curve_carry s3, s8).
Contract prices carry their identity in their code, so no rule is needed.
Form: Datastream DSGRID with several expired-contract codes per formula ("<CLZ5^9>,<CLF6^9>,...", the form that
returned data in L11/L12), one formula per root and two delivery years, monthly from January three years before the
first delivery year to December of the second (Curve carry: month-end settlements, k = 0 by TESTING_PROTOCOL 7.3
item 3); short-rate strips DAILY from January two years before (Strip reversion trades at the next settlement).
Contracts already expired by 2026-11-24 only (later ones come from the weekly file). Values after 2010-12 are sealed
by the reader. Files (each refreshed once by the user):
  L13a_contracts_energy_metals.xlsx   CL LCO NG HO RB GC SI HG PL (metals: all 12 months, serial months may be NA)
  L13b_contracts_ags.xlsx             C W S SB KC CT LC (their listed cycles; sugar with January/September too)
  L13c_contracts_strips_daily.xlsx    ED FEI SRA SON3 quarterly contracts, daily
usage: python3 build_lseg_l13.py [out dir]"""
import datetime as dt
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter as L

import build_lseg_contract_pull as B11
import lseg_rules as LR

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out")
TODAY = dt.date(2026, 11, 24)
ROW0 = 6
ALL = "FGHJKMNQUVXZ"
MONTHS = {"CL": ALL, "LCO": ALL, "NG": ALL, "HO": ALL, "RB": ALL, "GC": ALL, "SI": ALL, "HG": ALL, "PL": ALL,
          "C": "HKNUZ", "W": "HKNUZ", "S": "FHKNQUX", "SB": "FHKNUV", "KC": "HKNUZ", "CT": "HKNVZ", "LC": "GJMQVZ",
          "ED": "HMUZ", "FEI": "HMUZ", "SRA": "HMUZ", "SON3": "HMUZ"}
FILES = [("L13a_contracts_energy_metals", ["CL", "LCO", "NG", "HO", "RB", "GC", "SI", "HG", "PL"], "M"),
         ("L13b_contracts_ags", ["C", "W", "S", "SB", "KC", "CT", "LC"], "M"),
         ("L13c_contracts_strips_daily", ["ED", "FEI", "SRA", "SON3"], "D")]
LAST = {"ED": 2023}                       # Eurodollar futures ended in 2023
FIRST = {"RB": 2006}                      # RBOB from 2006 (unleaded HU contracts are not on LSEG)


def codes_for(root, rr, y):
    out = []
    for c in MONTHS[root]:
        m = LR.LD.MONTH_CODES.index(c) + 1
        if LR.dates(root, y, m)[0] >= TODAY:
            continue                                   # not yet expired: weekly file
        out.append("<%s>" % B11.ric(rr, y, m, True))
    return out


def build(out_dir=OUT):
    roots = {r["root"]: r for r in B11.read_roots()}
    paths = []
    for name, rlist, per in FILES:
        wb = Workbook()
        ck = wb.active
        ck.title = "Check"
        bold = Font(bold=True)
        rows, pos = [], {}
        sheets = {}
        for root in rlist:
            r = roots[root]
            rr = r["ric_root"]
            y0 = max(FIRST.get(root, int(r["first_year"])), 1975)
            y1 = min(LAST.get(root, 2026), 2026)
            sh = root
            ws = sheets.setdefault(sh, wb.create_sheet(sh))
            for ya in range(y0, y1 + 1, 2):
                codes = codes_for(root, rr, ya) + (codes_for(root, rr, ya + 1) if ya + 1 <= y1 else [])
                if not codes:
                    continue
                lst = ",".join(codes)
                assert len(lst) <= 250, (root, ya, len(lst))
                if per == "M":
                    f = B11.ds(lst, start="%d-01-31" % (ya - 3), end="%d-12-31" % min(ya + 1, y1), frq="M")
                    n = 12 * (min(ya + 1, y1) - ya + 4) + 12
                else:
                    f = B11.ds(lst, start="%d-01-01" % (ya - 2), end="%d-12-31" % min(ya + 1, y1), frq="D")
                    n = 262 * (min(ya + 1, y1) - ya + 3) + 20
                w = len(codes) + 2
                k = pos.get(sh, 0)
                c = 1 + k
                pos[sh] = k + w
                pid = "%s-%03d" % (name.split("_")[0], len(rows) + 1)
                ws.cell(2, c, pid).font = bold
                ws.cell(3, c, "%s deliveries %d-%d, %s (%d contracts)" % (r["name"], ya, min(ya + 1, y1),
                                                                         "monthly" if per == "M" else "daily",
                                                                         len(codes)))
                ws.cell(4, c, "formula: " + f[1:])
                ws.cell(ROW0, c, f)
                rows.append((pid, sh, ws.cell(3, c).value, f[1:], "'%s'!%s%d" % (sh, L(c), ROW0),
                             "'%s'!%s%d:%s%d" % (sh, L(c + 1), ROW0, L(c + w - 2), ROW0 + n)))
        ck["A1"] = "LSEG pull %s: contract-level prices (exact contract identity)" % name.split("_")[0]
        ck["A1"].font = Font(bold=True, size=14)
        ck["A2"] = ("1. Open in Excel with Workspace signed in.   2. Wait until the number in B4 has not changed for one "
                    "minute.   3. Press Ctrl+S (keep the file name). Some empty columns are expected (months not listed).")
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
        for col, w in zip("ABCDEF", (10, 10, 50, 60, 60, 14)):
            ck.column_dimensions[col].width = w
        os.makedirs(out_dir, exist_ok=True)
        p = os.path.join(out_dir, name + ".xlsx")
        wb.save(p)
        paths.append(p)
        print("%s.xlsx | %d formulas | contracts %d" % (name, len(rows),
                                                         sum(r[3].count("<") for r in rows)))
    return paths


if __name__ == "__main__":
    build()
