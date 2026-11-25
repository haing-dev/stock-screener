"""Weekly LSEG live file (TESTING_PROTOCOL 7.10 item 3 step 4; WORKFLOW s6 W1): the latest ~10 weeks of every series a
registered pod would read live from LSEG, refreshed and saved by the user, read by the PC job lseg_weekly_v1 (it only
reads the saved file). Built once; dates are relative (TODAY()), so the same file is refreshed every week.

Series (from the specs' live-source rows):
  Curves         daily closes of continuous positions c1..cK of the 16 Curve carry commodities (K = the positions the
                 front leg >= 3 months out and the contract 12 months later can occupy; card 5 R1 reads CL c1, HG c1)
  Strips         daily settlements of the live short-rate strips: 3m SOFR c1-12 (Strip reversion's live dollar strip),
                 Euribor c1-12, 3m SONIA c1-8 (T10 strip markets, Strip reversion currencies)
  Monthly        S&P 500 12-month forward EPS (IBES aggregate, card 3 R4), last 13 month-ends
  Identity now   expiry / last trade / first notice of the contract each live position holds today (field names: the
                 L11 calendar-test GUESSES; rebuild with the confirmed names once L11 is read)
Layout as the pull files (Check sheet first; row 2 id, row 3 label, row 4 formula text, row 6 formula); positions listed
on sheet "Positions". The text date format "dd-mmm-yyyy" in TEXT() assumes an English Excel (as the pull files' dates).
usage: python3 build_lseg_weekly.py [out dir]"""
import csv
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter as L

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(HERE), "docs")
NAME = "LSEG_weekly_live"
ROW0, DAYS_BACK = 6, 70
DATED = "SORT:ASC TSREPEAT:NO CH:Fd RH:Timestamp"
DSOPT = "RowHeader=true;TimeSeriesList=true;ColHeader=true;DispSeriesDescription=false;YearlyTSFormat=false;QuarterlyTSFormat=false"
ID_FIELDS = ["TR.ExpiryDate", "TR.LastTradeDate", "TR.FirstNoticeDate"]     # GUESSES until L11 confirms the names
CURVE_CAP = 18
STRIPS = [("SRA", "3m SOFR", 12), ("FEI", "Euribor", 12), ("SON3", "3m SONIA", 8)]


def hp_rel(ric, fields="CLOSE", days=DAYS_BACK):
    start = '"&TEXT(TODAY()-%d,"dd-mmm-yyyy")&"' % days
    end = '"&TEXT(TODAY(),"dd-mmm-yyyy")&"'
    return ('=RDP.HistoricalPricing("%s","%s","START:%s END:%s INTERVAL:P1D SOURCE:RFV",,"%s")'
            % (ric, fields, start, end, DATED))


def positions(txt):
    out = []
    for part in (txt or "").replace(",", ";").split(";"):
        part = part.strip()
        if part:
            a, _, b = part.partition("-")
            out += list(range(int(a), int(b or a) + 1))
    return out


def build(out_dir=OUT, roots_path=None):
    with open(roots_path or os.path.join(HERE, "lseg_roots.csv"), newline="", encoding="utf-8") as f:
        roots = [r for r in csv.DictReader(f) if not r["root"].startswith("#")]
    wb = Workbook()
    ck = wb.active
    ck.title = "Check"
    B = Font(bold=True)
    sheets, pos, rows, width, rown = {}, {}, [], {}, {}
    plist = []

    def add(sheet, label, f, w=3, n=80):
        if sheet not in sheets:
            sheets[sheet], pos[sheet], width[sheet], rown[sheet] = wb.create_sheet(sheet), 0, w, n
        ws, c = sheets[sheet], 1 + pos[sheet] * width[sheet]
        pos[sheet] += 1
        pid = "W-%03d" % (len(rows) + 1)
        ws.cell(2, c, pid).font = B
        ws.cell(3, c, label)
        ws.cell(4, c, "formula: " + f[1:])
        ws.cell(ROW0, c, f)
        rows.append((pid, sheet, label, f[1:], "'%s'!%s%d" % (sheet, L(c), ROW0),
                     "'%s'!%s%d:%s%d" % (sheet, L(c), ROW0, L(c + width[sheet] - 2), rown[sheet])))

    for r in roots:
        if "curve12" not in (r.get("need") or ""):
            continue
        k = min(max(positions(r["depth_m"]) + positions(r["depth_m_l11"])), CURVE_CAP)
        for n in range(1, k + 1):
            ric = "%sc%d" % (r["ric_root"], n)
            add("Curves", "%s contract %d, daily" % (r["name"], n), hp_rel(ric))
            plist.append((r["root"], ric, n))
    for root, name, k in STRIPS:
        for n in range(1, k + 1):
            ric = "%sc%d" % (root, n)
            add("Strips", "%s contract %d, daily" % (name, n), hp_rel(ric))
            plist.append((root, ric, n))
    add("Monthly", "S&P 500 12-month forward EPS (IBES aggregate), last 13 month-ends",
        '=DSGRID("@:USSP500","A12FE","-13M","-0D","M","%s","")' % DSOPT, 3, 30)
    ws = wb.create_sheet("Positions")
    ws["A1"] = "Live continuous positions (root, RIC, position): the Identity now blocks read this list"
    for j, h in enumerate(("root", "RIC", "position"), 1):
        ws.cell(4, j, h).font = B
    for i, row in enumerate(plist):
        for j, v in enumerate(row, 1):
            ws.cell(5 + i, j, v)
    rng = "Positions!$B$5:$B$%d" % (4 + len(plist))
    for f in ID_FIELDS:
        add("Identity now", "contract held today by each live position: %s (GUESS)" % f,
            '=RDP.Data(%s,"%s","CH=Fd RH=IN")' % (rng, f), 3, len(plist) + 12)
    ck["A1"] = "LSEG weekly live file (refresh and save once a week)"
    ck["A1"].font = Font(bold=True, size=14)
    ck["A2"] = ("1. Open in Excel with Workspace signed in; wait until B4 has not changed for one minute.   "
                "2. Press Ctrl+S (same name, same folder).   3. Tell Claude 'weekly saved'.")
    r1, rn = 8, 7 + len(rows)
    ck["A4"] = "blocks with data"
    ck["A4"].font = B
    ck["B4"] = '=COUNTIF(F%d:F%d,">0")&" of %d"' % (r1, rn, len(rows))
    ck["B4"].font = Font(bold=True, size=13)
    ck["A5"] = "blocks showing an Excel error (add-in not loaded)"
    ck["B5"] = '=COUNTIF(E%d:E%d,"Excel error*")' % (r1, rn)
    for j, h in enumerate(("id", "sheet", "what", "formula", "status", "numbers found"), 1):
        ck.cell(7, j, h).font = B
    for k, (pid, sh, lab, ftxt, cell, rg) in enumerate(rows):
        r = r1 + k
        for j, v in enumerate((pid, sh, lab, ftxt), 1):
            ck.cell(r, j, v)
        ck.cell(r, 5, '=IF(ISERROR(%s),"Excel error (add-in not loaded?)",IF(F%d>0,"data","text: "&LEFT(%s&"",70)))'
                % (cell, r, cell))
        ck.cell(r, 6, '=SUMPRODUCT(--ISNUMBER(%s))' % rg)
    for col, w in zip("ABCDEF", (10, 14, 45, 60, 50, 14)):
        ck.column_dimensions[col].width = w
    os.makedirs(out_dir, exist_ok=True)
    p = os.path.join(out_dir, NAME + ".xlsx")
    wb.save(p)
    by = {}
    for _, sh, *_ in rows:
        by[sh] = by.get(sh, 0) + 1
    print("%s.xlsx | %d formulas | %s | live positions %d" % (NAME, len(rows), ", ".join("%s %d" % kv for kv in by.items()),
                                                              len(plist)))
    return p, rows, plist


if __name__ == "__main__":
    build()
