"""L14 contract-level prices in SMALL files (replaces L13a-c, which were too large for LSEG to load at once).
Same purpose and form as build_lseg_l13.py (Datastream DSGRID, several expired-contract codes per formula), changed:
  * one delivery year per formula (at most 12 codes), and at most MAX_SERIES contract series per file;
  * design deliveries only (up to 2012: every Curve carry leg decided by 2010-12 and every strip contract 1-8 held
    by then); contracts delivering 2013 and later (holdout years) are pulled later, after the freeze;
  * roots whose continuous positions are already identified by the listing rule at >= 99.5% at every depth
    (lseg_ident_v4: NG, HO, GC, KC) are not pulled; their legs come from the continuous series;
  * silver and copper: all 12 months from 2000 (serial months listed), cycle months before; platinum and cattle
    their cycles; sugar March/May/July/October plus January and September before 1990.
Monthly files: Jan three years before the delivery year to Dec of it (front-leg history for the leg cap).
Daily strip files (Eurodollar, Euribor quarterly): Jan two years before to Dec of the delivery year.
usage: python3 build_lseg_l14.py [out dir]      -> L14a ... files + L14_README.txt"""
import datetime as dt
import os
import string
import sys

from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter as L

import build_lseg_contract_pull as B11
import lseg_rules as LR

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out")
ROW0 = 6
LAST_DELIVERY = 2012
MAX_SERIES = {"M": 360, "D": 60}
ALL = "FGHJKMNQUVXZ"
ORDER = [("CL", "M"), ("LCO", "M"), ("RB", "M"), ("SI", "M"), ("HG", "M"), ("PL", "M"), ("C", "M"), ("W", "M"),
         ("S", "M"), ("SB", "M"), ("CT", "M"), ("LC", "M"), ("ED", "D"), ("FEI", "D")]
FIRST = {"RB": 2006}


def months(root, y):
    if root == "CL" or root == "LCO" or root == "RB":
        return ALL
    if root in ("SI", "HG"):
        return ALL if y >= 2000 else LR.CYCLE[root]
    if root == "SB":
        return "FHKNUV" if y < 1990 else "HKNV"
    return LR.CYCLE[root]


def formulas(roots):
    out = []
    for root, per in ORDER:
        r = roots[root]
        y0 = max(FIRST.get(root, int(r["first_year"])), 1974)
        for y in range(y0, LAST_DELIVERY + 1):
            codes = ["<%s>" % B11.ric(r["ric_root"], y, LR.LD.MONTH_CODES.index(c) + 1, True) for c in months(root, y)]
            if per == "M":
                f = B11.ds(",".join(codes), start="%d-01-31" % (y - 3), end="%d-12-31" % y, frq="M")
                n = 12 * 4 + 12
            else:
                f = B11.ds(",".join(codes), start="%d-01-01" % (y - 2), end="%d-12-31" % y, frq="D")
                n = 262 * 3 + 20
            out.append((root, per, y, codes, f, n, r["name"]))
    return out


def write(name, items):
    wb = Workbook()
    ck = wb.active
    ck.title = "Check"
    bold = Font(bold=True)
    rows, pos, sheets = [], {}, {}
    for root, per, y, codes, f, n, rname in items:
        if root not in sheets:
            sheets[root] = wb.create_sheet(root)
        ws = sheets[root]
        w = len(codes) + 2
        c = 1 + pos.get(root, 0)
        pos[root] = pos.get(root, 0) + w
        pid = "%s-%03d" % (name.split("_")[0], len(rows) + 1)
        lab = rname if y == 0 else "%s deliveries %d, %s (%d contracts)" % (
            rname, y, "monthly" if per == "M" else "daily", len(codes))
        ws.cell(2, c, pid).font = bold
        ws.cell(3, c, lab)
        ws.cell(4, c, "formula: " + f[1:])
        ws.cell(ROW0, c, f)
        rows.append((pid, root, lab, f[1:], "'%s'!%s%d" % (root, L(c), ROW0),
                     "'%s'!%s%d:%s%d" % (root, L(c + 1), ROW0, L(c + w - 2), ROW0 + n)))
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
    return wb


def build(out_dir=OUT):
    roots = {r["root"]: r for r in B11.read_roots()}
    items = formulas(roots)
    files, cur, cur_n, cur_per = [], [], 0, None
    for it in items:
        per, k = it[1], len(it[3])
        if cur and (per != cur_per or cur_n + k > MAX_SERIES[per]):
            files.append(cur)
            cur, cur_n = [], 0
        cur.append(it)
        cur_n += k
        cur_per = per
    if cur:
        files.append(cur)
    os.makedirs(out_dir, exist_ok=True)
    readme = ["L14 contract files: refresh in any order (open, wait until B4 stops changing, Ctrl+S).", ""]
    names = []
    for i, fl in enumerate(files):
        tag = "L14" + string.ascii_lowercase[i]
        roots_in = []
        for it in fl:
            if it[0] not in roots_in:
                roots_in.append(it[0])
        name = "%s_%s" % (tag, "-".join(roots_in))
        wb = write(name, fl)
        wb.save(os.path.join(out_dir, name + ".xlsx"))
        nser = sum(len(it[3]) for it in fl)
        names.append(name)
        readme.append("%s.xlsx | %d formulas | %d contract series | %s" % (name, len(fl), nser,
                                                                        "monthly" if fl[0][1] == "M" else "daily"))
        print(readme[-1])
    with open(os.path.join(out_dir, "L14_README.txt"), "w") as f:
        f.write("\n".join(readme) + "\n")
    return names


if __name__ == "__main__":
    build()
