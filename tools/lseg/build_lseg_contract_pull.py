"""LSEG pull L11 (2026-11-24): contract identity for every futures root the specs use (TESTING_PROTOCOL 7.10 item 3,
7.6 step 8; SPEC_Curve_carry s3/s8, SPEC_Strip_reversion s3/s8, CHECK_3.2_B s4) plus the four missing daily Eurodollar
contracts 3, 5, 6, 7 (Strip reversion diagnostic R1).

Why: the pulled continuous series (CLc1 ... CLc24, <EDc1> ... <EDc12>) give closes only. They do not say which delivery
month a position held on a date, when it rolled, or whether serial months are positions. This file asks LSEG for:
  Calendar        every contract of every root, by delivery month 1972-2029 (expired RICs "CLZ5^9" = Dec 1995; live
                  RICs "CLF7"): expiry, last trade and first notice dates (RDP.Data over a range of RICs, the form that
                  worked for 17,000 ISINs in the size file). A month that is not listed returns an error: that answers
                  "which months are listed" (serial months).
  Calendar test   the same on 12 test contracts with ten candidate field names (only some names are known to exist).
  Contract sample two contracts per root, monthly over their life, and one contract daily around its expiry: matched
                  against the continuous series by lseg_check_v1, they show which position held the contract on each
                  date and on which day the continuous series rolled (the roll rule, not assumed).
  Identity probe  guesses that might give the held contract directly as a time series (TR.ExpiryDate with dates on a
                  continuation RIC; Datastream LTDT on a continuous series; the "CONT. LTDT" series NCLCS01 of probe 2).
  Curve depth     continuous positions beyond what L4a/L4b hold, where a 12-month-later contract needs them (heating
                  oil and gasoline 13-18, copper 13-18, gold and silver 13-14, platinum 7-8, soybeans 10-11, sugar 7-8,
                  coffee, cotton, cattle 7-9).
  ED daily        Datastream "<EDc3>", "<EDc5>", "<EDc6>", "<EDc7>" daily from 1989-12-29 (same form as L10's c1/c2/c4/c8).
Functions: only the four that returned dated data in the probes (RDP.Data, RDP.HistoricalPricing with
"RH:Timestamp", DSGRID, RHistory). GUESSES (to be confirmed by this refresh): every TR field name for contract dates,
the expired-RIC form for HistoricalPricing and for Datastream "<CLZ5^0>", Datastream explicit end dates, LTDT.
Layout: as lseg_pull_helpers.build (row 2 id, row 3 label, row 4 formula text, row 6 formula; Check sheet first),
block width per sheet; contract lists on sheets "Contracts" and "TestContracts" (root, RIC, delivery YYYY-MM, form).
usage: python3 build_lseg_contract_pull.py [out dir]      (reads lseg_roots.csv next to this file)"""
import csv
import datetime as dt
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter as L

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(HERE), "docs")
NAME = "L11_contract_identity"
END, ROW0 = "24-Nov-2026", 6
TODAY = dt.date(2026, 11, 24)
LAST_YEAR = 2029
CHUNK = 1000
MONTHS = "FGHJKMNQUVXZ"
DATED = "SORT:ASC TSREPEAT:NO CH:Fd RH:Timestamp"
DSOPT = "RowHeader=true;TimeSeriesList=true;ColHeader=true;DispSeriesDescription=false;YearlyTSFormat=false;QuarterlyTSFormat=false"
DSSTAT = "RowHeader=true;ColHeader=true;Heading=true;DispSeriesDescription=true"
CAL_FIELDS = ["TR.ExpiryDate", "TR.LastTradeDate", "TR.LastTradingDate", "TR.FirstNoticeDate"]   # guesses
TEST_FIELDS = ["TR.ExpiryDate", "TR.ExpirationDate", "TR.LastTradeDate", "TR.LastTradingDate", "TR.LastTradingDay",
               "TR.FirstNoticeDate", "TR.FirstNoticeDay", "TR.FirstDeliveryDate", "TR.LastDeliveryDate",
               "TR.FirstTradeDate"]                                                                 # guesses


def hp(ric, fields="CLOSE", start="01-Jan-1970", end=END, interval="P1M"):
    return '=RDP.HistoricalPricing("%s","%s","START:%s END:%s INTERVAL:%s SOURCE:RFV",,"%s")' % (
        ric, fields, start, end, interval, DATED)


def ds(code, dtype="", start="1969-12-31", end="-0D", frq="M"):
    return '=DSGRID("%s","%s","%s","%s","%s","%s","")' % (code, dtype, start, end, frq, DSOPT)


def dss(code, dtype):
    return '=DSGRID("%s","%s","Latest Value","","","%s","")' % (code, dtype, DSSTAT)


def rd_range(rng, field):
    return '=RDP.Data(%s,"%s","CH=Fd RH=IN")' % (rng, field)


def rd(ric, fields, params="CH=Fd RH=IN"):
    return '=RDP.Data("%s","%s","%s")' % (ric, fields, params)


def positions(txt):
    out = []
    for part in (txt or "").replace(",", ";").split(";"):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-")
            out += list(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return out


def read_roots(path=None):
    path = path or os.path.join(HERE, "lseg_roots.csv")
    with open(path, newline="", encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if not r["root"].startswith("#")]


def ric(root, year, month, expired):
    return "%s%s%d%s" % (root, MONTHS[month - 1], year % 10, ("^%d" % ((year // 10) % 10)) if expired else "")


def contract_list(roots):
    """[(root, ric, 'YYYY-MM', form)] for every root, month and year; both forms near today; the alternative root
    (HU for gasoline) up to its end year."""
    out = []
    for r in roots:
        y0 = max(int(r["first_year"]) - 1, 1972)
        for rr, y1 in ((r["ric_root"], LAST_YEAR), (r.get("ric_root_alt") or "", int(r.get("alt_until") or 0))):
            if not rr:
                continue
            for y in range(y0, y1 + 1):
                for m in range(1, 13):
                    deliv = dt.date(y, m, 1)
                    months_from_now = (deliv.year - TODAY.year) * 12 + deliv.month - TODAY.month
                    if months_from_now <= 2:
                        out.append((r["root"], ric(rr, y, m, True), "%d-%02d" % (y, m), "expired"))
                    if months_from_now >= -1:
                        out.append((r["root"], ric(rr, y, m, False), "%d-%02d" % (y, m), "live"))
    return out


def sample_years(r):
    fy = int(r["first_year"])
    if fy >= 2015:
        return []                                       # live-only roots: their history is sealed
    return [1995, 2005] if fy <= 1992 else [2002, 2008]


def build(out_dir=OUT, roots_path=None):
    roots = read_roots(roots_path)
    wb = Workbook()
    ck = wb.active
    ck.title = "Check"
    B = Font(bold=True)
    sheets, pos, rows, width, rown = {}, {}, [], {}, {}
    contracts = contract_list(roots)
    test = [(a, b, c, d) for (a, b, c, d) in contracts if (a, c) in {
        ("CL", "1995-12"), ("CL", "2005-12"), ("CL", "2027-03"), ("GC", "2005-12"), ("C", "2005-12"),
        ("HG", "2005-12"), ("ED", "1995-12"), ("ED", "2005-12"), ("FEI", "2005-12"), ("SRA", "2027-03"),
        ("RB", "2008-12"), ("LCO", "2005-12")}]

    def add(sheet, label, f, w=3, n=None):
        if sheet not in sheets:
            sheets[sheet], pos[sheet] = wb.create_sheet(sheet), 0
            width[sheet], rown[sheet] = w, n or 1000
        ws, c = sheets[sheet], 1 + pos[sheet] * width[sheet]
        pos[sheet] += 1
        pid = "L11-%03d" % (len(rows) + 1)
        ws.cell(2, c, pid).font = B
        ws.cell(3, c, label)
        ws.cell(4, c, "formula: " + f[1:])
        ws.cell(ROW0, c, f)
        rows.append((pid, sheet, label, f[1:], "'%s'!%s%d" % (sheet, L(c), ROW0),
                     "'%s'!%s%d:%s%d" % (sheet, L(c), ROW0, L(c + width[sheet] - 2), rown[sheet])))

    # A. Eurodollar daily contracts 3, 5, 6, 7 (Strip reversion R1); same form as L10-049..052
    ed = next(r for r in roots if r["root"] == "ED")
    for n in positions(ed["positions_d_l11"]):
        add("ED daily", "Eurodollar contract %d, daily" % n, ds("<EDc%d>" % n, start="1989-12-29", frq="D"), 3, 9800)
    # B. curve depth (monthly continuous positions beyond L4a/L4b)
    for r in roots:
        for n in positions(r["depth_m_l11"]):
            add("Curve depth", "%s contract %d" % (r["name"], n), hp("%sc%d" % (r["ric_root"], n)), 3, 700)
    # C. sample contracts: two monthly over their life, one daily around its expiry
    for r in roots:
        mcode = r["sample_month"].strip()
        if not mcode:
            continue
        m = MONTHS.index(mcode) + 1
        for y in sample_years(r):
            rr = r["ric_root_alt"] if r.get("ric_root_alt") and y <= int(r.get("alt_until") or 0) and y < 2006 \
                else r["ric_root"]
            code = ric(rr, y, m, True)
            if r["c_sid_m"].startswith("DS:"):
                f = ds("<%s>" % code, start="%d-12-31" % (y - 4), end="%d-12-31" % y)
                lab = "%s %s monthly over its life (Datastream form: GUESS)" % (r["name"], code)
            else:
                f = hp(code, start="01-Jan-%d" % (y - 3), end="31-Dec-%d" % y)
                lab = "%s %s monthly over its life (expired-RIC form: GUESS)" % (r["name"], code)
            add("Contract sample", lab, f, 3, 60)
        y = 2005 if int(r["first_year"]) <= 2003 else None
        if y:
            rr = r["ric_root"] if not (r.get("ric_root_alt") and y < 2006) else r["ric_root_alt"]
            code = ric(rr, y, m, True)
            d1 = dt.date(y, m, 1)
            s = dt.date(d1.year - (d1.month <= 4), (d1.month - 4 - 1) % 12 + 1, 1)
            e = dt.date(y + (m == 12), m % 12 + 1, 1) - dt.timedelta(days=1)
            if r["c_sid_m"].startswith("DS:"):
                f = ds("<%s>" % code, start=s.isoformat(), end=e.isoformat(), frq="D")
            else:
                f = hp(code, start=s.strftime("%d-%b-%Y"), end=e.strftime("%d-%b-%Y"), interval="P1D")
            add("Contract sample", "%s %s daily, 4 months to the end of its delivery month (GUESS form)" % (
                r["name"], code), f, 3, 160)
    # D. identity probe: the held contract as a time series, if LSEG has it (all GUESSES)
    for c in ("CLc1", "CLc12", "GCc1", "FEIc1"):
        add("Identity probe", "%s: TR.ExpiryDate as a monthly time series 2005-2006 (GUESS)" % c,
            rd(c, "TR.ExpiryDate.date;TR.ExpiryDate", "SDate=2004-12-01 EDate=2006-12-31 Frq=M CH=Fd RH=IN"), 4, 40)
    add("Identity probe", "continuation RICs now: TR.ExpiryDate of the contract held today (GUESS)",
        rd("CLc1,CLc2,CLc12,GCc1,GCc4,HGc1,Cc1,EDc1,FEIc1,FEIc8,SRAc1,SRAc8,SON3c1", "TR.ExpiryDate"), 4, 40)
    add("Identity probe", "continuation RICs now: first notice date (GUESS)",
        rd("CLc1,CLc2,GCc1,GCc4,HGc1,Cc1,LCc1", "TR.FirstNoticeDate"), 4, 40)
    add("Identity probe", "continuation RICs now: real-time expiry field EXPIR_DATE (GUESS)",
        rd("CLc1,CLc2,GCc1,SRAc1,FEIc1", "EXPIR_DATE"), 4, 40)
    add("Identity probe", "Datastream <CLc1> with datatype LTDT, monthly 2005-2006 (GUESS)",
        ds("<CLc1>", "LTDT", "2004-12-31", "2006-12-31"), 4, 40)
    add("Identity probe", "Datastream NCLCS00 with datatype LTDT (GUESS)", ds("NCLCS00", "LTDT", "2004-12-31",
                                                                            "2006-12-31"), 4, 40)
    add("Identity probe", "Datastream NCLCS01 (probe 2 header 'CONT. LTDT') with datatype LTDT (GUESS)",
        ds("NCLCS01", "LTDT", "2004-12-31", "2006-12-31"), 4, 40)
    add("Identity probe", "Datastream static LTDT of contract <CLZ5^0> (GUESS)", dss("<CLZ5^0>", "LTDT"), 4, 40)
    add("Identity probe", "Datastream <CLZ5^0> settlement monthly 2003-2005 (GUESS)",
        ds("<CLZ5^0>", "", "2002-12-31", "2005-12-31"), 4, 40)
    # E. calendar test: ten candidate field names on twelve contracts
    nt = len(test)
    for f in TEST_FIELDS:
        add("Calendar test", "test contracts: %s (GUESS)" % f, rd_range("TestContracts!$B$5:$B$%d" % (4 + nt), f), 3,
            nt + 12)
    # F. full calendar: chunks of CHUNK contracts x 4 field names
    for k, lo in enumerate(range(0, len(contracts), CHUNK)):
        hi = min(lo + CHUNK, len(contracts))
        rng = "Contracts!$B$%d:$B$%d" % (5 + lo, 4 + hi)
        for f in CAL_FIELDS:
            add("Calendar", "contracts %d-%d (%s ... %s): %s" % (lo + 1, hi, contracts[lo][1], contracts[hi - 1][1], f),
                rd_range(rng, f), 3, CHUNK + 12)
    # contract lists
    for title, lst in (("Contracts", contracts), ("TestContracts", test)):
        ws = wb.create_sheet(title)
        ws["A1"] = "%s: root, RIC, delivery month, form (expired RICs: month code + last year digit + ^decade digit)" % title
        for j, h in enumerate(("root", "RIC", "delivery", "form"), 1):
            ws.cell(4, j, h).font = B
        for i, row in enumerate(lst):
            for j, v in enumerate(row, 1):
                ws.cell(5 + i, j, v)
    # Check sheet (as lseg_pull_helpers.build)
    ck["A1"] = "LSEG pull L11: contract identity (calendar, roll samples, depth) + Eurodollar daily 3/5/6/7"
    ck["A1"].font = Font(bold=True, size=14)
    ck["A2"] = ("1. Open in Excel with Workspace signed in.   2. Wait until the number in B4 has not changed for one "
                "minute.   3. Press Ctrl+S (keep the file name). Errors in some blocks are expected (guesses).")
    r1, rn = 8, 7 + len(rows)
    ck["A4"] = "blocks with data"
    ck["A4"].font = B
    ck["B4"] = '=COUNTIF(F%d:F%d,">0")&" of %d"' % (r1, rn, len(rows))
    ck["B4"].font = Font(bold=True, size=13)
    ck["A5"] = "blocks showing an Excel error (add-in not loaded)"
    ck["B5"] = '=COUNTIF(E%d:E%d,"Excel error*")' % (r1, rn)
    for j, h in enumerate(("id", "sheet", "what", "formula", "status", "numbers found"), 1):
        ck.cell(7, j, h).font = B
    for k, (pid, sh, lab, ftxt, cell, rng) in enumerate(rows):
        r = r1 + k
        for j, v in enumerate((pid, sh, lab, ftxt), 1):
            ck.cell(r, j, v)
        ck.cell(r, 5, '=IF(ISERROR(%s),"Excel error (add-in not loaded?)",IF(F%d>0,"data","text: "&LEFT(%s&"",70)))'
                % (cell, r, cell))
        ck.cell(r, 6, '=SUMPRODUCT(--ISNUMBER(%s))' % rng)
    for col, w in zip("ABCDEF", (10, 16, 50, 60, 60, 14)):
        ck.column_dimensions[col].width = w
    os.makedirs(out_dir, exist_ok=True)
    p = os.path.join(out_dir, NAME + ".xlsx")
    wb.save(p)
    by = {}
    for _, sh, *_ in rows:
        by[sh] = by.get(sh, 0) + 1
    print("%s.xlsx | %d formulas | %s | contracts listed %d (+%d test)" % (
        NAME, len(rows), ", ".join("%s %d" % kv for kv in by.items()), len(contracts), len(test)))
    return p, rows, contracts


if __name__ == "__main__":
    build()
