"""Helpers shared by build_lseg_pull.py (set 1) and build_lseg_pull2.py (set 2). Original header: LSEG Workspace pull set v1 (2026-11-12), built after probe v1 (tools/bbgq/results/lseg_probe_v1.txt).
Only methods that returned DATED data in the probe are used in the L files:
  RHistory (Workspace quotes: BID.Timestamp;BID.Close)   -> FX spot, forwards, implied vol, swaps
  RDP.Data (TR fields with .date)                         -> government yields, equity and volatility indexes
  DSGRID   (Datastream)                                   -> benchmark bond yields and return indexes, equity markets
P2 is a second probe: futures (how to get dates, which roots exist, curve depth), commodity indexes, MSCI, short
rates, swaps, economics with polls. Some codes are guesses; an error text is a useful answer.
Layout of every data sheet: one block per series, block width W columns; row 2 id, row 3 label, row 4 formula text,
row 6 the formula (results fill down and right). First sheet "Check": live status per block.
usage: python3 docs/data_requests/build_lseg_pull.py [out dir]"""
import os, sys
from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter as L

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "lseg_pull_2026-11-12")
END, ROW0, ROWN = "12-Nov-2026", 6, 15000

def rh(ric, fam="BID", start="01-Jan-1975"):
    return '=RHistory("%s","%s.Timestamp;%s.Close","START:%s INTERVAL:1MO",,"TSREPEAT:NO CH:Fd")' % (ric, fam, fam, start)
def rd(ric, f, start="1975-01-01"):
    return '=RDP.Data("%s","%s.date;%s","SDate=%s EDate=2026-11-12 Frq=M CH=Fd RH=IN")' % (ric, f, f, start)
DSOPT = "RowHeader=true;TimeSeriesList=true;ColHeader=true;DispSeriesDescription=false;YearlyTSFormat=false;QuarterlyTSFormat=false"
def ds(code, dt="", start="1969-12-31", frq="M"):
    return '=DSGRID("%s","%s","%s","-0D","%s","%s","")' % (code, dt, start, frq, DSOPT)
def hp(ric, fields="CLOSE", start="01-Jan-1970", interval="P1M", disp=None):
    f = '=RDP.HistoricalPricing("%s","%s","START:%s END:%s INTERVAL:%s SOURCE:RFV"' % (ric, fields, start, END, interval)
    return f + (',,"%s")' % disp if disp else ")")

def build(name, title, probes, W=6):
    wb = Workbook()
    ck = wb.active
    ck.title = "Check"
    B = Font(bold=True)
    pos, sheets, rows = {}, {}, []
    for i, (sh, lab, f) in enumerate(probes, 1):
        if sh not in sheets:
            sheets[sh], pos[sh] = wb.create_sheet(sh), 0
        ws, c = sheets[sh], 1 + pos[sh] * W
        pos[sh] += 1
        pid = "%s-%03d" % (name.split("_")[0], i)
        ws.cell(2, c, pid).font = B
        ws.cell(3, c, lab)
        ws.cell(4, c, "formula: " + f[1:])
        ws.cell(ROW0, c, f)
        rows.append((pid, sh, lab, f[1:], "'%s'!%s%d" % (sh, L(c), ROW0), "'%s'!%s%d:%s%d" % (sh, L(c), ROW0, L(c + W - 2), ROWN)))
    ck["A1"] = title; ck["A1"].font = Font(bold=True, size=14)
    ck["A2"] = ("1. Open in Excel with Workspace signed in.   2. Wait until the number in B4 has not changed for one minute.   "
                "3. Press Ctrl+S (keep the file name), then give the file to Claude. Errors in some blocks are expected.")
    r1, rn = 8, 7 + len(rows)
    ck["A4"] = "blocks with data"; ck["A4"].font = B
    ck["B4"] = '=COUNTIF(F%d:F%d,">0")&" of %d"' % (r1, rn, len(rows)); ck["B4"].font = Font(bold=True, size=13)
    ck["A5"] = "blocks showing an Excel error (add-in not loaded)"
    ck["B5"] = '=COUNTIF(E%d:E%d,"Excel error*")' % (r1, rn)
    for j, h in enumerate(("id", "sheet", "what", "formula", "status", "numbers found"), 1):
        ck.cell(7, j, h).font = B
    for k, (pid, sh, lab, ftxt, cell, rng) in enumerate(rows):
        r = r1 + k
        for j, v in enumerate((pid, sh, lab, ftxt), 1):
            ck.cell(r, j, v)
        ck.cell(r, 5, '=IF(ISERROR(%s),"Excel error (add-in not loaded?)",IF(F%d>0,"data","text: "&LEFT(%s&"",70)))' % (cell, r, cell))
        ck.cell(r, 6, '=SUMPRODUCT(--ISNUMBER(%s))' % rng)
    for col, w in zip("ABCDEF", (10, 16, 40, 60, 60, 14)):
        ck.column_dimensions[col].width = w
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, name + ".xlsx")
    wb.save(p)
    print("%-34s %4d formulas | %s" % (name + ".xlsx", len(rows), ", ".join("%s %d" % kv for kv in pos.items())))
    return len(rows)

