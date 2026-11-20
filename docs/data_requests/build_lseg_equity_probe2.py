"""LSEG Workspace EQUITY test file 2 (2026-11-20; plan v0.4 step 2): one small workbook that answers, before the data files
are built: (1) which TR.F field name returns each raw item of the field dictionary
(docs/research/equity/field_dictionary_raw_v0.1.csv), as first reported; (2) the US company list incl. companies that
died 2010-2025, with identifiers, sector and market value on a past date; (3) estimates, prices, short interest and
ownership across MANY companies in one formula; (4) how much one formula can carry (companies x fields x years).
Same block layout, Check / Index / Sources / TestSet sheets and reader as probe v1 (build_lseg_equity_probe.py, imported).
Many names are guesses on purpose: an error text is a useful answer. Nothing in the file is a data value.
usage: python3 docs/data_requests/build_lseg_equity_probe2.py [out dir]"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_lseg_equity_probe as v1  # noqa: E402

END = "2026-11-20"
v1.END = END
v1.OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "lseg_equity_probe2_2026-11-20")
v1.NAME = "LSEG_equity_probe_v2.xlsx"
v1.TITLE = "LSEG Workspace equity test file 2 (field names, company list, sizes)"
v1.READ_DATE = "2026-11-17 / 2026-11-20"
v1.ROWN = {"Universe": 150000, "Limits": 150000, "Short": 30000}
v1.SOURCES = v1.SOURCES + [
    ("S44", "https://kaxanuk-data-curator.readthedocs.io/en/dev/data_providers/lseg_workspace.html", "field map of an open-source LSEG loader: about 110 TR.F.* names (income statement, balance sheet, cash flow) with Period=FQ0; TR.CLOSEPRICE(Adjusted=0/1), TR.Volume, TR.DivExDate, TR.CAExDate"),
    ("S45", "https://community.developers.lseg.com/discussion/133655", "TR.F.PriceToBookValuePerShr, TR.SharesOutstanding.calcdate with SDate / EDate / Frq"),
    ("S46", "repo: tools/bbgq/results/lseg_eq_probe_v1.txt", "on this PC (18 Nov): TR.F.TotRevenue / TotAssets / NetCashFlowOp / ComShrOutsTot with ReportingState=Orig; TR.EPSMean history; TR.TotalReturn, TR.CompanyMarketCap, TR.SharesOutstanding, TR.Volume monthly; Datastream RI, SHORTINT, EPS1NE, DEADUS1, LS&PCOMP<MMYY>; SCREEN active or inactive"),
    ("S47", "Ince and Porter (2006), Journal of Financial Research 29(4)", "Datastream US research lists FAMERA..FAMERZ and dead lists DEADUS1..DEADUS6"),
]
rd, hist, ds, dss, SCR_ALL = v1.rd, v1.hist, v1.ds, v1.dss, v1.SCR_ALL
v1.P.clear()


def add(group, sheet, what, f, cite, src="", pair="", kind="series", w=None):
    v1.P.append(dict(group=group, sheet=sheet, what=what, f=f, cite=cite, src=src, pair=pair, kind=kind, w=w))


# ------------------------------------------------------------------ test set: 21 live, 11 that left the market 2017-2024
def cusip9(c8):
    t = 0
    for i, ch in enumerate(c8):
        v = int(ch) if ch.isdigit() else ord(ch) - 55
        if i % 2:
            v *= 2
        t += v // 10 + v % 10
    return c8 + str((10 - t % 10) % 10)


def isin(c8):
    body = "US" + cusip9(c8)
    digits = "".join(str(int(ch)) if ch.isdigit() else str(ord(ch) - 55) for ch in body)
    t = 0
    for i, ch in enumerate(reversed(digits)):
        v = int(ch) * (2 if i % 2 == 0 else 1)
        t += v // 10 + v % 10
    return body + str((10 - t % 10) % 10)


assert isin("90184L10") == "US90184L1026" and isin("03783310") == "US0378331005"
LIVE = [("Apple", "AAPL.O"), ("Microsoft", "MSFT.O"), ("JPMorgan Chase", "JPM.N"), ("Exxon Mobil", "XOM.N"), ("Johnson & Johnson", "JNJ.N"),
        ("Coca-Cola", "KO.N"), ("General Electric", "GE.N"), ("Kraft Heinz", "KHC.O"), ("Super Micro Computer", "SMCI.O"), ("Nvidia", "NVDA.O"),
        ("Costco", "COST.O"), ("Visa", "V.N"), ("Union Pacific", "UNP.N"), ("Texas Instruments", "TXN.O"), ("Moody's", "MCO.N"),
        ("Fair Isaac", "FICO.N"), ("Pool Corp", "POOL.O"), ("Texas Pacific Land", "TPL.N"), ("Watsco", "WSO.N"), ("Crocs", "CROX.O"),
        ("Boot Barn", "BOOT.N")]
DEAD = [("Twitter (private 2022)", "90184L10"), ("Celgene (acquired 2019)", "15102010"), ("Monsanto (acquired 2018)", "61166W10"),
        ("Time Warner (acquired 2018)", "88731730"), ("Sears Holdings (bankrupt 2018)", "81235010"), ("SVB Financial (failed 2023)", "78486Q10"),
        ("Bed Bath & Beyond (bankrupt 2023)", "07589610"), ("First Republic (failed 2023)", "33616C10"), ("Whole Foods (acquired 2017)", "96683710"),
        ("Linear Technology (acquired 2017)", "53567810"), ("Activision Blizzard (acquired 2023)", "00507V10")]
v1.TEST = [(n, r, "", "", "live") for n, r in LIVE] + [(n, isin(c), isin(c), "", "dead") for n, c in DEAD]
N = len(v1.TEST)
TS = "TestSet!$B$4:$B$%d" % (3 + N)
TS_LIVE = "TestSet!$B$4:$B$%d" % (3 + len(LIVE))
TS_DEAD = "TestSet!$B$%d:$B$%d" % (4 + len(LIVE), 3 + N)
DS_LIVE = ",".join("<%s>" % r for _, r in LIVE)
DS_DEAD = ",".join(isin(c) for _, c in DEAD)
assert len(DS_LIVE) <= 255 and len(DS_DEAD) <= 255
FY = "Period=FY0 Frq=FY SDate=0 EDate=-17 "
FQ = "Period=FQ0 Frq=FQ SDate=0 EDate=-70 "
ORIG = "ReportingState=Orig CH=Fd RH=IN"
SPX = "0#.SPX"
SCR_ACT = 'SCREEN(U(IN(Equity(active,public,primary))),IN(TR.ExchangeCountryCode,""US""),CURN=USD)'
SCR_BOTH = 'SCREEN(U(IN(Equity(active or inactive,public,primary))),IN(TR.ExchangeCountryCode,""US""),CURN=USD)'
SCRP = "curn=USD RH=In CH=Fd"

# ------------------------------------------------------------------ 1 field names (one block per name; Apple, annual, as first reported)
G, S = "1 Field names", "Fields"
RAW = list(csv.DictReader(open(os.path.join(HERE, "..", "research", "equity", "field_dictionary_raw_v0.1.csv"))))
ALT = "alternates (field:c cited / :g guess)"
for r in RAW:
    cands = [(r["lseg_field"], r["cited_or_guess"])] + [(a.split(":")[0], {"c": "cited", "g": "guess"}[a.split(":")[1]]) for a in r[ALT].split(";") if a]
    for k, (f, c) in enumerate(cands):
        add(G, S, "%s %s%s: %s (Apple, annual, first reported)" % (r["id"], r["item"], "" if k == 0 else " alt %d" % k, f),
            rd("AAPL.O", "%s.periodenddate;%s" % (f, f), FY + ORIG), c, ("S44,S46" if c == "cited" else "") , pair="%s:%d" % (r["id"], k))

# ------------------------------------------------------------------ 2 forms: quarters, dates, many companies at once
G, S = "2 Forms", "Forms"
CORE = ["TR.F.TotRevenue", "TR.F.EBIT", "TR.F.NetIncAfterTax", "TR.F.NetCashFlowOp", "TR.F.CAPEXNetCF", "TR.F.TotAssets", "TR.F.DebtTot", "TR.F.ComEqTot"]
for f in ("TR.F.TotRevenue", "TR.F.NetIncAfterTax", "TR.F.NetCashFlowOp", "TR.F.CAPEXNetCF", "TR.F.TotAssets"):
    for state in ("Orig", "Rsdt"):
        add(G, S, "KHC %s quarterly, ReportingState=%s" % (f, state), rd("KHC.O", "%s.periodenddate;%s" % (f, f), FQ + "ReportingState=%s CH=Fd RH=IN" % state),
            "cited", "S44,S46", pair="FQ-%s-%s" % (f.split(".")[-1], state))
add(G, S, "is quarterly cash flow per quarter or year to date? (GE operating cash flow with period length)",
    rd("GE.N", "TR.F.NetCashFlowOp.periodenddate;TR.F.NetCashFlowOp;TR.F.NetCashFlowOp.PeriodLength;TR.F.NetCashFlowOp.fperiod", FQ + ORIG), "guess", "S18")
add(G, S, "last twelve months form (Period=LTM guess), revenue and EBIT, quarterly steps", rd("GE.N", "TR.F.TotRevenue.periodenddate;TR.F.TotRevenue;TR.F.EBIT", "Period=LTM Frq=FQ SDate=0 EDate=-70 " + ORIG), "guess")
add(G, S, "announcement dates, annual, whole test set in one formula (period end, original announcement, source date)",
    rd(TS, "TR.F.TotRevenue.periodenddate;TR.F.OriginalAnnouncementDate;TR.F.SourceDate", FY + ORIG), "cited", "S18,S19,S46")
add(G, S, "announcement dates, quarterly, whole test set", rd(TS, "TR.F.TotRevenue.periodenddate;TR.F.OriginalAnnouncementDate", FQ + ORIG), "cited", "S19,S46")
add(G, S, "8 core fields x whole test set x 18 years, annual, first reported (relative dates)",
    rd(TS, "TR.F.TotRevenue.periodenddate;" + ";".join(CORE), FY + ORIG), "cited", "S44,S46")
add(G, S, "same with absolute dates (SDate=2008-01-01 EDate=today, Frq=FY)",
    rd(TS, "TR.F.TotRevenue.periodenddate;" + ";".join(CORE), "Period=FY0 Frq=FY SDate=2008-01-01 EDate=%s " % END + ORIG), "cited", "S17,S44")
add(G, S, "8 core fields x whole test set x 70 quarters, first reported", rd(TS, "TR.F.TotRevenue.periodenddate;" + ";".join(CORE), FQ + ORIG), "cited", "S44,S46")
add(G, S, "dead companies only: revenue, net income, total assets, annual (by ISIN)",
    rd(TS_DEAD, "TR.F.TotRevenue.periodenddate;TR.F.TotRevenue;TR.F.NetIncAfterTax;TR.F.TotAssets", FY + ORIG), "cited", "S13,S44")
add(G, S, "depth for 10-year measures: Apple 8 core fields annual back 30 years", rd("AAPL.O", "TR.F.TotRevenue.periodenddate;" + ";".join(CORE), "Period=FY0 Frq=FY SDate=0 EDate=-30 " + ORIG), "cited", "S44,S46")
add(G, S, "fiscal period label and currency of the report (Apple)", rd("AAPL.O", "TR.F.TotRevenue.fperiod;TR.F.TotRevenue.currency;TR.F.TotRevenue", FY + ORIG), "cited", "S17")
add(G, S, "vendor ratios as first reported? price to book, return on equity guesses (Apple)", rd("AAPL.O", "TR.F.PriceToBookValuePerShr.periodenddate;TR.F.PriceToBookValuePerShr;TR.F.ReturnAvgComEqPct;TR.F.ROIC", FY + "CH=Fd RH=IN"), "guess", "S45")
add(G, S, "Datastream Worldscope cross-check items for the live test set: sales, EBIT, net income, yearly", ds(DS_LIVE[:120].rsplit(",", 1)[0], "WC01001,WC18191,WC01751", "2007-12-31", "Y"), "cited", "S7")

# ------------------------------------------------------------------ 3 company list incl. dead companies, identifiers, sector
G, S = "3 Universe", "Universe"
add(G, S, "US primary common, active or inactive: name, retire date, CUSIP, ISIN, CIK, GICS sector, first trade date (7 fields x about 17,000)",
    rd(SCR_BOTH, "TR.CommonName;TR.RetireDate;TR.CUSIP;TR.ISIN;TR.CIKNUMBER;TR.GICSSector;TR.FirstTradeDate", SCRP), "cited", "S1,S10,S12,S14,S16", kind="list")
add(G, S, "same list: market value on 2010-12-31 and 2018-12-31 (point-in-time size for every company incl. dead)",
    rd(SCR_BOTH, "TR.CompanyMarketCap(SDate=2010-12-31);TR.CompanyMarketCap(SDate=2018-12-31)", SCRP), "guess", "S1", kind="list")
add(G, S, "screen by past size: active or inactive with market value above $300m on 2010-12-31",
    rd('SCREEN(U(IN(Equity(active or inactive,public,primary))),IN(TR.ExchangeCountryCode,""US""),TR.CompanyMarketCap(SDate=2010-12-31)>=300000000,CURN=USD)', "TR.CommonName;TR.RetireDate", SCRP), "guess", "S1", kind="list")
add(G, S, "screen inactive with retire date from 2010 (filter guess)",
    rd('SCREEN(U(IN(Equity(inactive,public,primary))),IN(TR.ExchangeCountryCode,""US""),TR.RetireDate>=20100101,CURN=USD)', "TR.CommonName;TR.RetireDate", SCRP), "guess", "S1,S16", kind="list")
add(G, S, "screen without 'primary' (all share classes; count against the primary list)",
    rd('SCREEN(U(IN(Equity(active or inactive,public))),IN(TR.ExchangeCountryCode,""US""),CURN=USD)', "TR.CommonName;TR.RetireDate", SCRP), "guess", "S1", kind="list")
for f, c in [("TR.GICSSector;TR.GICSIndustryGroup;TR.GICSIndustry;TR.GICSSubIndustry", "guess"), ("TR.GICSSectorCode;TR.GICSIndustryGroupCode;TR.GICSSubIndustryCode", "guess"),
             ("TR.TRBCEconomicSector;TR.TRBCBusinessSector;TR.TRBCIndustryGroup", "guess"), ("TR.HeadquartersCountry;TR.ExchangeName;TR.InstrumentType", "guess"),
             ("TR.IPODate;TR.FirstTradeDate;TR.CompanyIncorporationDate", "guess"), ("TR.RetireDate;TR.OrganizationStatusCode;TR.InstrumentIsActive", "guess"),
             ("TR.CUSIP;TR.ISIN;TR.SEDOL;TR.CIKNUMBER;TR.OrganizationId;TR.TickerSymbol", "cited")]:
    add(G, S, "test set: " + f.replace("TR.", "").replace(";", ", "), rd(TS, f), c, "S10,S12,S14" if c == "cited" else "", kind="static")
add(G, S, "sector on a past date (GICS sector with SDate=2010-12-31, guess), test set", rd(TS, "TR.GICSSector(SDate=2010-12-31);TR.GICSIndustryGroup(SDate=2010-12-31)"), "guess", kind="static")
for k in range(2, 8):
    add(G, S, "Datastream US dead list DEADUS%d (name, ISIN, last date)" % k, dss("DEADUS%d" % k, "NAME,ISIN,TIME"), "cited", "S47,S46", kind="list")
for code in ("FAMERA", "FAMERB", "FAMERZ"):
    add(G, S, "Datastream US research list %s (name, ISIN, status)" % code, dss(code, "NAME,ISIN,ESTAT"), "cited", "S47", kind="list")
for code, c in [("LS&PCOMP1210", "cited"), ("LS&PCOMP1217", "cited"), ("LS&P1500", "guess"), ("LS&P15001210", "guess"), ("LFRUSS1L", "guess"), ("LFRUSS1L1210", "guess"), ("LFRUSS3L1215", "guess")]:
    add(G, S, "Datastream index list %s (name, ISIN)" % code, dss(code, "NAME,ISIN"), c, "S3,S4,S5,S46", kind="list")
add(G, S, "Datastream sector codes for the dead test companies (GICS guess datatypes) ", dss(DS_DEAD, "NAME,GGISN,INDM,ICBIN"), "guess", "", kind="static")

# ------------------------------------------------------------------ 4 estimates across companies
G, S = "4 Estimates", "Estimates"
MON = "SDate=2009-12-31 EDate=%s Frq=M CH=Fd RH=IN" % END
add(G, S, "EPS mean FY1, monthly from 2009-12, whole test set in one formula", rd(TS, "TR.EPSMean.date;TR.EPSMean;TR.EPSMean.periodenddate", "Period=FY1 " + MON), "cited", "S24,S25,S46")
add(G, S, "EPS mean FY2 and next 12 months, monthly, live test set", rd(TS_LIVE, "TR.EPSMean(Period=FY2).date;TR.EPSMean(Period=FY2);TR.EPSMean(Period=NTM)", MON), "guess", "S26")
for f, c in [("TR.EPSNumIncEstimates", "guess"), ("TR.NumberOfAnalysts", "guess"), ("TR.EPSNumUp", "guess"), ("TR.EPSNumDown", "guess"), ("TR.EPSNumberofEstimates", "guess"),
             ("TR.RevenueMean", "cited"), ("TR.EBITDAMean", "guess"), ("TR.EBITMean", "guess"), ("TR.FCFMean", "guess"), ("TR.DPSMean", "guess"),
             ("TR.LTGMean", "guess"), ("TR.PriceTargetMean", "guess"), ("TR.RecMean", "guess"), ("TR.EPSSmartEst", "guess")]:
    add(G, S, "Apple %s FY1 monthly from 2009-12" % f, hist("AAPL.O", f, "2009-12-31", extra="Period=FY1 "), c, "S25" if c == "cited" else "")
add(G, S, "actual EPS and its report date, quarterly, whole test set", rd(TS, "TR.EPSActValue.date;TR.EPSActValue;TR.EPSActValue.periodenddate", "SDate=0 EDate=-70 Frq=FQ Period=FQ0 CH=Fd RH=IN"), "cited", "S27,S46")
add(G, S, "surprise fields (guesses): TR.EPSActSurprise, TR.EPSSurprisePct, TR.EPSMeanEstLastQtr (Apple, quarterly)",
    rd("AAPL.O", "TR.EPSActValue.date;TR.EPSActSurprise;TR.EPSSurprisePct", "SDate=0 EDate=-70 Frq=FQ Period=FQ0 CH=Fd RH=IN"), "guess")
add(G, S, "actual revenue and EBITDA, quarterly (TR.RevenueActValue, TR.EBITDAActValue guesses)", rd("AAPL.O", "TR.RevenueActValue.date;TR.RevenueActValue;TR.EBITDAActValue", "SDate=0 EDate=-70 Frq=FQ Period=FQ0 CH=Fd RH=IN"), "guess")
add(G, S, "dead companies: EPS mean FY1 monthly (by ISIN)", rd(TS_DEAD, "TR.EPSMean.date;TR.EPSMean", "Period=FY1 " + MON), "cited", "S13,S24")
add(G, S, "Datastream I/B/E/S for the live test set: EPS1, EPS2, number of estimates, up / down revisions (EPS1UP, EPS1DN guesses), monthly",
    ds("<AAPL.O>,<MSFT.O>,<GE.N>,<CROX.O>", "EPS1,EPS2,EPS1NE,EPS1UP,EPS1DN,LTMN", "2009-12-31"), "guess", "S6,S43,S46")

# ------------------------------------------------------------------ 5 prices, returns, size, volume
G, S = "5 Prices", "Prices"
add(G, S, "total return per month (TR.TotalReturn1Mo guess), whole test set from 2009-12", rd(TS, "TR.TotalReturn1Mo.date;TR.TotalReturn1Mo", MON), "guess")
add(G, S, "TR.TotalReturn monthly, whole test set (worked for one stock)", rd(TS, "TR.TotalReturn.date;TR.TotalReturn", MON), "cited", "S46")
add(G, S, "close, market value, shares, volume monthly, whole test set", rd(TS, "TR.PriceClose.date;TR.PriceClose;TR.CompanyMarketCap;TR.SharesOutstanding;TR.Volume", MON), "cited", "S46")
add(G, S, "unadjusted and adjusted close (cited Adjusted=0/1), Apple monthly", rd("AAPL.O", "TR.CLOSEPRICE(Adjusted=0).date;TR.CLOSEPRICE(Adjusted=0);TR.CLOSEPRICE(Adjusted=1)", MON), "cited", "S44")
add(G, S, "average daily volume and turnover value (TR.AvgDailyVolume3M, TR.AvgDailyValTraded30D guesses), test set today", rd(TS, "TR.AvgDailyVolume3M;TR.AvgDailyValTraded30D;TR.AvgDailyVolume30D"), "guess", kind="static")
add(G, S, "daily close and volume from 2009-12, Crocs (one small stock, about 4,300 rows)", rd("CROX.O", "TR.PriceClose.date;TR.PriceClose;TR.Volume", "SDate=2009-12-31 EDate=%s Frq=D CH=Fd RH=IN" % END), "cited", "S46")
add(G, S, "Datastream total return index RI, live test set, monthly from 2009-12", ds(DS_LIVE, "RI", "2009-12-31"), "cited", "S42,S46")
add(G, S, "Datastream RI, dead test companies by ISIN, monthly from 2009-12 (padding after the last date is expected)", ds(DS_DEAD, "RI", "2009-12-31"), "cited", "S46")
add(G, S, "Datastream MV, P, UP, VO, NOSH for the dead test companies", ds(DS_DEAD[:64].rsplit(",", 1)[0], "MV,P,UP,VO,NOSH", "2009-12-31"), "cited", "S6,S46")
add(G, S, "dividends: ex date and amount (cited), Coca-Cola from 2009", rd("KO.N", "TR.DivExDate;TR.DivUnadjustedGross;TR.DivAnnouncementDate", "SDate=2009-12-31 EDate=%s CH=Fd RH=IN" % END), "cited", "S44")
add(G, S, "splits: ex date and terms (cited), Apple and Nvidia", rd("AAPL.O,NVDA.O", "TR.CAExDate;TR.CATermsNewShares;TR.CATermsOldShares", "CAEventType=SSP SDate=2009-12-31 EDate=%s CH=Fd RH=IN" % END), "cited", "S44")
add(G, S, "US 10-year Treasury yield monthly (US10YT=RR) for the yield-gap measure", '=RHistory("US10YT=RR","BID.Timestamp;BID.Close","START:31-Dec-2009 INTERVAL:1MO",,"TSREPEAT:NO CH:Fd")', "cited", "S40")
add(G, S, "S&P 500 total return index (.SPXTR guess) and SPY, monthly", rd(".SPXTR,SPY.P", "TR.PriceClose.date;TR.PriceClose", MON), "guess", "S40")

# ------------------------------------------------------------------ 6 short interest and ownership
G, S = "6 Short and owners", "Short"
add(G, S, "Datastream short interest SHORTINT, live test set, monthly from 2009-12", ds(DS_LIVE, "SHORTINT", "2009-12-31"), "cited", "S46")
add(G, S, "Datastream short interest SHORTINT, dead test companies", ds(DS_DEAD, "SHORTINT", "2009-12-31"), "cited", "S46")
add(G, S, "Datastream free float and strategic holdings (NOSHFF, NOSHST guesses), live test set", ds(DS_LIVE, "NOSHFF", "2009-12-31"), "guess", "S6")
add(G, S, "Workspace short interest today (TR.ShortInterest, TR.ShortInterestPctFloat, TR.DaysToCover), test set", rd(TS, "TR.ShortInterest;TR.ShortInterestPctFloat;TR.DaysToCover"), "guess", "S34,S46", kind="static")
add(G, S, "Workspace free float (TR.FreeFloatPct, TR.FreeFloat guesses), test set", rd(TS, "TR.FreeFloatPct;TR.FreeFloat"), "guess", kind="static")
add(G, S, "insider and institutional ownership totals (guesses), test set", rd(TS, "TR.InsiderOwnershipPct;TR.PctInsiderShrsOutHeld;TR.InstitutionalOwnershipPct;TR.TtlInstOwnPct"), "guess", kind="static")
add(G, S, "holders by type on 2015-12-31: name, investor type, % held, top 30 (Texas Pacific Land)", rd("TPL.N", "TR.InvestorFullName;TR.InvestorType;TR.PctOfSharesOutHeld;TR.SharesHeld.calcdate", "SDate=2015-12-31 StartNum=1 EndNum=30 CH=Fd RH=IN"), "cited", "S30,S31,S46", kind="list")
add(G, S, "insider transactions 2010 onward, whole live test set in one formula",
    rd(TS_LIVE, "TR.TransactionDate;TR.InsiderFullName;TR.InsiderRole;TR.AdjSharesTraded;TR.TransactionType;TR.TransactionPrice", "SDate=2010-01-01 EDate=%s CH=Fd RH=IN" % END), "cited", "S33,S46", kind="list")

# ------------------------------------------------------------------ 7 sizes: how much one formula carries (largest last)
G, S = "7 Sizes", "Limits"
add(G, S, "S&P 500 x 8 core fields x 18 years annual, first reported (about 9,000 rows x 9)", rd(SPX, "TR.F.TotRevenue.periodenddate;" + ";".join(CORE), FY + ORIG), "cited", "S2,S44,S46", kind="list")
add(G, S, "S&P 500 x 4 fields x 70 quarters, first reported (about 35,000 rows)", rd(SPX, "TR.F.TotRevenue.periodenddate;" + ";".join(CORE[:4]), FQ + ORIG), "cited", "S2,S44,S46", kind="list")
add(G, S, "S&P 500 x announcement dates x 70 quarters", rd(SPX, "TR.F.TotRevenue.periodenddate;TR.F.OriginalAnnouncementDate", FQ + ORIG), "cited", "S19", kind="list")
add(G, S, "S&P 500 x total return monthly from 2009-12 (about 100,000 rows)", rd(SPX, "TR.TotalReturn.date;TR.TotalReturn", MON), "cited", "S46", kind="list")
add(G, S, "S&P 500 x EPS mean FY1 monthly from 2009-12 (about 100,000 rows)", rd(SPX, "TR.EPSMean.date;TR.EPSMean", "Period=FY1 " + MON), "cited", "S24,S46", kind="list")
add(G, S, "all active US companies x 4 fields, latest year, first reported (about 14,000 rows)", rd(SCR_ACT, "TR.F.TotRevenue.periodenddate;" + ";".join(CORE[:4]), "Period=FY0 " + ORIG), "cited", "S1,S44", kind="list")
add(G, S, "active or inactive US companies x revenue x 5 years (about 85,000 rows)", rd(SCR_BOTH, "TR.F.TotRevenue.periodenddate;TR.F.TotRevenue", "Period=FY0 Frq=FY SDate=0 EDate=-4 " + ORIG), "cited", "S1,S44", kind="list")
add(G, S, "Datastream S&P 500 list of Dec 2010 (LS&PCOMP1210) x RI monthly 2009-12 to today (past members incl. dead)", ds("LS&PCOMP1210", "RI", "2009-12-31"), "cited", "S3,S4,S46", w=520)
add(G, S, "Datastream dead list DEADUS1 x RI monthly from 2009-12 (6,286 series: expected too large; the message gives the limit)", ds("DEADUS1", "RI", "2009-12-31"), "cited", "S46,S47", w=8)

if __name__ == "__main__":
    v1.main()
