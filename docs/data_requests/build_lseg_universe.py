"""LSEG universe file v1 (2026-11-20; plan v0.4 step 3a): the US company list INCLUDING dead companies, from Datastream
lists (the Workspace screen misses most dead companies: docs/research/equity/LSEG_equity_probe2_2026-11-20.md), plus
the retests left open by test file 2 (short-interest history, four account items, ownership totals).
Per list two static blocks joined on the Datastream code: A = DSCD, NAME, ISIN, TIME (last date), BDATE (first date);
B = DSCD, TYPE, MAJOR, GEOGN, EXMNEM, INDM, ISINID. Same block layout as the probes (build_lseg_equity_probe.py).
usage: python3 docs/data_requests/build_lseg_universe.py [out dir]"""
import os
import string
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_lseg_equity_probe as v1  # noqa: E402

END = "2026-11-20"
v1.END = END
v1.OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "lseg_universe_2026-11-20")
v1.NAME = "LSEG_universe_v1.xlsx"
v1.TITLE = "LSEG universe file 1 (US company list incl. dead companies; retests)"
v1.READ_DATE = "2026-11-17 / 2026-11-20"
v1.ROWN = {"Dead": 20000, "Research": 20000}
v1.SOURCES = v1.SOURCES + [
    ("S46", "repo: tools/bbgq/results/lseg_eq_probe_v2.txt", "on this PC (20 Nov): DEADUS2..DEADUS7 and FAMERA / FAMERB / FAMERZ return NAME, ISIN, TIME, ESTAT; INDM and ICBIN work; SHORTINT failed for code lists"),
    ("S47", "Ince and Porter (2006), Journal of Financial Research 29(4)", "Datastream US research lists FAMERA..FAMERZ, dead lists DEADUS1..DEADUS6; filters TYPE = EQ, MAJOR = Y, GEOGN"),
]
rd, ds, dss = v1.rd, v1.ds, v1.dss
v1.P.clear()
v1.TEST = [("Apple", "AAPL.O", "US0378331005", "", "live"), ("General Electric", "GE.N", "US3696043013", "", "live"),
           ("Kraft Heinz", "KHC.O", "US5007541064", "", "live"), ("JPMorgan Chase", "JPM.N", "US46625H1005", "", "live"),
           ("Twitter (private 2022)", "US90184L1026", "US90184L1026", "", "dead")]


def add(group, sheet, what, f, cite, src="", pair="", kind="series", w=None):
    v1.P.append(dict(group=group, sheet=sheet, what=what, f=f, cite=cite, src=src, pair=pair, kind=kind, w=w))


A = "DSCD,NAME,ISIN,TIME,BDATE"
B = "DSCD,TYPE,MAJOR,GEOGN,EXMNEM,INDM,ISINID"
for k in range(1, 11):
    c = "cited" if k <= 7 else "guess"
    add("1 Dead lists", "Dead", "DEADUS%d part A: code, name, ISIN, last date, first date" % k, dss("DEADUS%d" % k, A), c, "S46,S47", pair="DEADUS%d:A" % k, kind="list", w=8)
    add("1 Dead lists", "Dead", "DEADUS%d part B: code, type, major flag, country, exchange, industry, primary flag" % k, dss("DEADUS%d" % k, B), c, "S46,S47", pair="DEADUS%d:B" % k, kind="list", w=10)
for ch in string.ascii_uppercase:
    add("2 Research lists", "Research", "FAMER%s part A: code, name, ISIN, last date, first date" % ch, dss("FAMER" + ch, A), "cited", "S46,S47", pair="FAMER%s:A" % ch, kind="list", w=8)
    add("2 Research lists", "Research", "FAMER%s part B: code, type, major flag, country, exchange, industry, primary flag" % ch, dss("FAMER" + ch, B), "cited", "S46,S47", pair="FAMER%s:B" % ch, kind="list", w=10)

# ------------------------------------------------------------------ retests
G, S = "3 Retests", "Retests"
FY = "Period=FY0 Frq=FY SDate=0 EDate=-17 ReportingState=Orig CH=Fd RH=IN"
for f, c in [("TR.F.GoodwNet", "cited"), ("TR.F.Goodw", "guess"), ("TR.F.MinIntrNonCtrlIntrTot", "cited"), ("TR.F.MinIntrEq", "guess"), ("TR.F.PrefShHoldEq", "cited"),
             ("TR.F.DebtIssuedLTSTCF", "cited"), ("TR.F.DebtIssuedLTCF", "cited"), ("TR.F.DebtLTSTIssuanceRetTotCF", "guess"), ("TR.F.AcctNotesRcvblTradeNet", "cited"),
             ("TR.F.TradeAcctTradeNotesRcvblNet", "guess"), ("TR.F.DefRevST", "guess"), ("TR.F.IntrExpn", "cited"), ("TR.F.DeprAmort", "cited"), ("TR.F.IncTaxPaidReimbIndirCF", "cited")]:
    add(G, S, "%s, GE and Kraft Heinz, annual, first reported" % f, rd("GE.N,KHC.O", "%s.periodenddate;%s" % (f, f), FY), c, "S44" if c == "cited" else "")
SI0 = "2009-12-31"
for code, lab in [("US0378331005", "Apple by ISIN alone (worked on 18 Nov)"), ("US0378331005,US3696043013", "Apple and GE by ISIN"), ("@AAPL", "Apple by mnemonic"),
                  ("@AAPL,U:GE,U:JPM,@KHC", "four companies by mnemonic"), ("992816", "Apple by Datastream code"), ("<AAPL.O>", "Apple by Workspace code"),
                  ("US90184L1026", "dead Twitter by ISIN")]:
    add(G, S, "Datastream short interest SHORTINT monthly: " + lab, ds(code, "SHORTINT", SI0), "guess", "S46")
add(G, S, "Datastream short interest, other datatype guesses (SHORTINTP, SHRTINT), Apple", ds("@AAPL", "SHORTINTP,SHRTINT", SI0), "guess")
add(G, S, "Workspace short interest history, cited TR form with Frq=M from 2010 (Apple)", '=TR("AAPL.O","TR.ShortInterest;TR.ShortInterest.date","SDate=2010-01-01 EDate=%s Frq=M CH=Fd RH=IN")' % END, "cited", "S34")
add(G, S, "Workspace short interest history, twice monthly (Frq=D, 2024 only)", rd("AAPL.O", "TR.ShortInterest.date;TR.ShortInterest", "SDate=2024-01-01 EDate=2024-12-31 Frq=D CH=Fd RH=IN"), "cited", "S34")
for f in ("TR.CategoryOwnershipPct;TR.InstrStatTypeValue", "TR.PctOfSharesOutHeld(SDate=2015-12-31,StatType=1)", "TR.InsiderPctOwnership", "TR.StrategicEntitiesOwnershipPct",
          "TR.InstitutionalInvestorsPct", "TR.SharesHeldByInsiders;TR.SharesHeldByInstitutions"):
    add(G, S, "ownership totals guess: " + f, rd("AAPL.O,GE.N,KHC.O", f), "guess", kind="static")
add(G, S, "Datastream strategic holdings % (NOSHST, NOSHEM, NOSHIC, NOSHOF guesses), Apple and GE monthly", ds("@AAPL,U:GE", "NOSHFF,NOSHST,NOSHEM,NOSHIC,NOSHOF", SI0), "guess", "S6")
add(G, S, "Datastream company static: GICS and SIC guesses (GGISN, SIC1, WC07021, WC06010 general industry), test set", dss("US0378331005,US3696043013,US90184L1026", "NAME,SIC1,WC07021,WC06010,INDM,ICBSSC"), "guess", "S7", kind="static")
add(G, S, "Datastream historical industry code by year (WC07021 SIC, yearly) for Apple and GE", ds("@AAPL,U:GE", "WC07021", "2007-12-31", "Y"), "guess", "S7")

if __name__ == "__main__":
    v1.main()
