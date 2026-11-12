"""LSEG Workspace probe workbook v1 (2026-11-12): about 60 test formulas that show which Workspace / Datastream Excel
functions work on the user's licence, how far the history goes, and which code families exist. Some codes are
deliberate guesses: an error text is a useful answer. The saved file stays on the PC; job tools/bbgq/jobs/lseg_probe_v1.py
reports metadata only (status, counts, date range, error text).
usage: python3 docs/data_requests/build_lseg_probe.py [out dir]"""
import os, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter as L

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "lseg_probe")
END = "12-Nov-2026"
W, ROW0, ROWN = 6, 6, 15000          # block width, formula row, last row counted

def hp(ric, fields="CLOSE", start="01-Jan-1970", interval="P1M", source=" SOURCE:RFV"):
    return '=RDP.HistoricalPricing("%s","%s","START:%s END:%s INTERVAL:%s%s")' % (ric, fields, start, END, interval, source)

def rd(ric, f, start="1990-01-01", frq="M"):
    return '=RDP.Data("%s","%s.date;%s","SDate=%s EDate=2026-11-12 Frq=%s CH=Fd RH=IN")' % (ric, f, f, start, frq)

DSOPT = "RowHeader=true;TimeSeriesList=true;ColHeader=true;DispSeriesDescription=false;YearlyTSFormat=false;QuarterlyTSFormat=false"
def ds(code, dt="", start="1970-01-01", frq="M"):
    return '=DSGRID("%s","%s","%s","-0D","%s","%s","")' % (code, dt, start, frq, DSOPT)

P = []   # (sheet, label, formula)
for ric, lab in [("EUR=", "EUR/USD spot"), ("JPY=", "USD/JPY spot"), ("US10YT=RR", "US 10y Treasury"), ("US2YT=RR", "US 2y Treasury"),
                 ("DE10YT=RR", "Germany 10y"), ("JP10YT=RR", "Japan 10y"), ("CLc1", "WTI crude, 1st contract"),
                 ("CLc2", "WTI crude, 2nd contract"), ("CLc12", "WTI crude, 12th contract"), ("LCOc1", "Brent, 1st contract"),
                 ("GCc1", "Gold, 1st contract"), ("HGc1", "Copper, 1st contract"), ("Cc1", "Corn, 1st contract"),
                 ("NGc1", "Natural gas, 1st contract"), ("TYc1", "US 10y note future"), ("FGBLc1", "Bund future"),
                 ("ESc1", "S&P 500 e-mini future"), ("SRAc1", "3m SOFR future"), ("FFc1", "Fed funds future"),
                 ("EDc1", "Eurodollar future (ended 2023)"), (".SPX", "S&P 500 index"), (".VIX", "VIX"), (".DXY", "Dollar index"),
                 (".MOVE", "MOVE index"), ("EUR3M=", "EUR/USD 3m forward points"), ("EUR3MO=", "EUR/USD 3m implied vol"),
                 ("USDSROIS10Y=", "USD SOFR swap 10y"), ("USNFAR=ECI", "US nonfarm payrolls (economic code)"),
                 ("USCPNY=ECI", "US CPI y/y (economic code)")]:
    P.append(("HP monthly", lab, hp(ric)))
P.append(("HP other", "EUR/USD spot, daily from 1990", hp("EUR=", start="01-Jan-1990", interval="P1D")))
P.append(("HP other", "WTI 1st contract, daily from 1990", hp("CLc1", start="01-Jan-1990", interval="P1D")))
P.append(("HP other", "S&P 500, weekly from 1990", hp(".SPX", start="01-Jan-1990", interval="P1W")))
P.append(("HP other", "EUR/USD monthly, no SOURCE", hp("EUR=", source="")))
P.append(("HP other", "US 10y Treasury, yield field", hp("US10YT=RR", fields="B_YLD_1")))
P.append(("HP other", "WTI 1st contract, open interest", hp("CLc1", fields="OPINT_1")))
P.append(("HP other", "EUR/USD monthly, bid and ask", hp("EUR=", fields="BID;ASK")))
for ric, f, lab in [("AAPL.O", "TR.PriceClose", "Apple close (sanity check)"), (".SPX", "TR.PriceClose", "S&P 500 close"),
                    ("CLc1", "TR.PriceClose", "WTI 1st contract close"), ("EUR=", "TR.PriceClose", "EUR/USD close"),
                    ("US10YT=RR", "TR.BIDYIELD", "US 10y bid yield"), (".SPX", "TR.TotalReturn1Mo", "S&P 500 1m total return"),
                    ("USNFAR=ECI", "TR.PriceClose", "US nonfarm payrolls (economic code)")]:
    P.append(("Data", lab, rd(ric, f)))
P.append(("Data", "old TR function", '=TR(".SPX","TR.PriceClose.date;TR.PriceClose","SDate=2015-01-01 EDate=2026-11-12 Frq=M CH=Fd RH=IN")'))
P.append(("Data", "old RHistory function", '=RHistory("EUR=","BID.Timestamp;BID.Close","START:01-Jan-1990 INTERVAL:1MO",,"TSREPEAT:NO CH:Fd")'))
for code, dt, lab in [("S&PCOMP", "PI", "S&P 500 price index"), ("S&PCOMP", "RI", "S&P 500 total return index"),
                      ("S&PCOMP", "PE", "S&P 500 price/earnings"), ("TOTMKUS", "DY", "US total market dividend yield"),
                      ("MSWRLD$", "RI", "MSCI World total return"), ("BMUS10Y", "RY", "US 10y benchmark yield"),
                      ("BMUS10Y", "RI", "US 10y benchmark return index"), ("BMBD10Y", "RY", "Germany 10y benchmark yield"),
                      ("BMJP10Y", "RY", "Japan 10y benchmark yield"), ("USEURSP", "", "USD per EUR (WM/R)"),
                      ("JAPAYE$", "", "JPY per USD"), ("CRUDOIL", "", "WTI spot"), ("GOLDBLN", "", "Gold bullion"),
                      ("LCPCASH", "", "LME copper cash"), ("GSCITOT", "", "S&P GSCI total return"),
                      ("NCLCS00", "", "WTI continuous future"), ("USCONPRCE", "", "US CPI"), ("USUN%TOTQ", "", "US unemployment rate"),
                      ("USCNFBUSQ", "", "US ISM manufacturing"), ("<EUR=>", "", "a Workspace code inside Datastream")]:
    P.append(("Datastream", lab, ds(code, dt)))
P.append(("Datastream", "S&P 500 price index, daily from 1990", ds("S&PCOMP", "PI", "1990-01-01", "D")))
P.append(("Datastream", "S&P 500, start written as -56Y", ds("S&PCOMP", "PI", "-56Y")))
P.append(("Datastream", "S&P 500, start written as BDATE", ds("S&PCOMP", "PI", "BDATE")))
P.append(("Datastream", "two datatypes in one call", ds("BMUS10Y", "RY,RI")))

wb = Workbook()
ck = wb.active
ck.title = "Check"
B, RED, GRN = Font(bold=True), PatternFill("solid", fgColor="F8CBAD"), PatternFill("solid", fgColor="C6E0B4")
sheets, pos, rows = {}, {}, []
for i, (sh, lab, f) in enumerate(P, 1):
    if sh not in sheets:
        sheets[sh] = wb.create_sheet(sh)
        pos[sh] = 0
    ws, c = sheets[sh], 1 + pos[sh] * W
    pos[sh] += 1
    pid = "P%02d" % i
    ws.cell(2, c, pid).font = B
    ws.cell(3, c, lab)
    ws.cell(4, c, "formula: " + f[1:])
    ws.cell(ROW0, c, f)
    rng = "'%s'!%s%d:%s%d" % (sh, L(c), ROW0, L(c + W - 2), ROWN)
    rows.append((pid, sh, lab, f[1:], "'%s'!%s%d" % (sh, L(c), ROW0), rng))
ck["A1"] = "LSEG Workspace probe v1"; ck["A1"].font = Font(bold=True, size=14)
ck["A2"] = ("1. Open this file in Excel with Workspace signed in (the Workspace tab must be visible).   "
            "2. Wait until the number in B4 has not changed for one minute (about 3 to 5 minutes in all).   "
            "3. Press Ctrl+S to save it here, then tell Claude 'saved'. Errors in some blocks are expected: that is what the test is for.")
r1, rn = 8, 7 + len(rows)
ck["A4"] = "blocks with data"; ck["A4"].font = B
ck["B4"] = '=COUNTIF(F%d:F%d,">0")&" of %d"' % (r1, rn, len(rows)); ck["B4"].font = Font(bold=True, size=13)
ck["A5"] = "blocks showing an Excel error (add-in not loaded)"
ck["B5"] = '=COUNTIF(E%d:E%d,"Excel error*")' % (r1, rn)
for j, h in enumerate(("id", "sheet", "what", "formula", "status", "numbers found"), 1):
    ck.cell(7, j, h).font = B
for k, (pid, sh, lab, ftxt, cell, rng) in enumerate(rows):
    r = r1 + k
    ck.cell(r, 1, pid); ck.cell(r, 2, sh); ck.cell(r, 3, lab); ck.cell(r, 4, ftxt)
    ck.cell(r, 5, '=IF(ISERROR(%s),"Excel error (add-in not loaded?)",IF(F%d>0,"data","text: "&LEFT(%s&"",70)))' % (cell, r, cell))
    ck.cell(r, 6, '=SUMPRODUCT(--ISNUMBER(%s))' % rng)
for col, w in zip("ABCDEF", (6, 14, 38, 60, 60, 14)):
    ck.column_dimensions[col].width = w
os.makedirs(OUT, exist_ok=True)
p = os.path.join(OUT, "LSEG_probe_v1.xlsx")
wb.save(p)
print(p, "| probes", len(rows), "| by sheet", {k: v for k, v in pos.items()})
