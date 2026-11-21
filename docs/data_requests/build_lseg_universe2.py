"""LSEG universe file 2 (2026-11-21): the Datastream US dead lists are alphabetical and DEADUS1-10 end at the letter S
(docs/research/equity/LSEG_universe_v1_2026-11-20.md, section "WRDS check"). This file pulls the rest (DEADUS11..16,
guesses) in the same two parts per list as file 1, and repeats the Datastream single-series retests that hit a login
error in file 1.
usage: python3 docs/data_requests/build_lseg_universe2.py [out dir]"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_lseg_equity_probe as v1  # noqa: E402

END = "2026-11-21"
v1.END = END
v1.OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "lseg_universe_2026-11-20")
v1.NAME = "LSEG_universe_v2.xlsx"
v1.TITLE = "LSEG universe file 2 (US dead lists T to Z; Datastream retests)"
v1.READ_DATE = "2026-11-17 / 2026-11-21"
v1.ROWN = {"Dead": 20000}
v1.SOURCES = v1.SOURCES + [
    ("S46", "repo: docs/research/equity/LSEG_universe_v1_2026-11-20.md", "on this PC (20 Nov): DEADUS1..DEADUS10 return 6,050 to 7,770 names each, in alphabetical order, ending at S"),
    ("S47", "Ince and Porter (2006), Journal of Financial Research 29(4)", "Datastream US dead lists DEADUS1..DEADUS6 (more lists were added since)"),
]
rd, ds, dss = v1.rd, v1.ds, v1.dss
v1.P.clear()
v1.TEST = [("Apple", "AAPL.O", "US0378331005", "", "live"), ("General Electric", "GE.N", "US3696043013", "", "live"),
           ("Twitter (private 2022)", "US90184L1026", "US90184L1026", "", "dead")]


def add(group, sheet, what, f, cite, src="", pair="", kind="series", w=None):
    v1.P.append(dict(group=group, sheet=sheet, what=what, f=f, cite=cite, src=src, pair=pair, kind=kind, w=w))


A = "DSCD,NAME,ISIN,TIME,BDATE"
B = "DSCD,TYPE,MAJOR,GEOGN,EXMNEM,INDM,ISINID"
for k in range(11, 17):
    add("1 Dead lists", "Dead", "DEADUS%d part A: code, name, ISIN, last date, first date" % k, dss("DEADUS%d" % k, A), "guess", "S46,S47", pair="DEADUS%d:A" % k, kind="list", w=8)
    add("1 Dead lists", "Dead", "DEADUS%d part B: code, type, major flag, country, exchange, industry, primary flag" % k, dss("DEADUS%d" % k, B), "guess", "S46,S47", pair="DEADUS%d:B" % k, kind="list", w=10)
for code in ("DEADUS", "DEADUSA", "DEADUST"):
    add("1 Dead lists", "Dead", "other list name guess %s: code, name" % code, dss(code, "DSCD,NAME"), "guess", "", kind="list", w=5)

G, S = "2 Retests", "Retests"
SI0 = "2009-12-31"
for code, lab in [("US0378331005", "Apple by ISIN alone"), ("@AAPL", "Apple by mnemonic"), ("US90184L1026", "dead Twitter by ISIN")]:
    add(G, S, "Datastream short interest SHORTINT monthly: " + lab, ds(code, "SHORTINT", SI0), "guess", "S46")
add(G, S, "Datastream company static: SIC and industry codes (SIC1, WC07021, WC06010, INDM, ICBSSC)", dss("US0378331005,US3696043013,US90184L1026", "NAME,SIC1,WC07021,WC06010,INDM,ICBSSC"), "guess", "S7", kind="static")
add(G, S, "Datastream industry code by year (WC07021, yearly) for Apple and GE", ds("@AAPL,U:GE", "WC07021", "2007-12-31", "Y"), "guess", "S7")
add(G, S, "Datastream identifiers for the join with WRDS: ticker, CUSIP, SEDOL (MNEM, WC06004, CUSIP, SECD, LOC)", dss("US0378331005,US3696043013,US90184L1026", "NAME,MNEM,WC06004,CUSIP,SECD,LOC"), "guess", "S7", kind="static")
add(G, S, "Workspace goodwill name guesses (TR.F.GoodwNet, TR.F.Goodwill, TR.F.GoodwIntangNet), GE annual first reported",
    rd("GE.N", "TR.F.GoodwNet.periodenddate;TR.F.GoodwNet;TR.F.Goodwill;TR.F.GoodwIntangNet", "Period=FY0 Frq=FY SDate=0 EDate=-17 ReportingState=Orig CH=Fd RH=IN"), "guess")
add(G, S, "Workspace goodwill, restated view (no ReportingState), GE annual", rd("GE.N", "TR.F.GoodwNet.periodenddate;TR.F.GoodwNet", "Period=FY0 Frq=FY SDate=0 EDate=-17 CH=Fd RH=IN"), "guess")

if __name__ == "__main__":
    v1.main()
