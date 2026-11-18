"""LSEG Workspace EQUITY probe v1 (2026-11-17): about 160 test formulas that show what the user's Workspace / Datastream
licence returns for STOCK-level data (plan docs/research/equity/EQUITY_POD_SHOP_PLAN_v0.3.md section 9, step E1.1 of
EQUITY_POD_SHOP_DESIGN_v0.2.md). Questions: universe incl. dead companies, identifiers to join with WRDS, accounts as
first reported vs restated with dates, past consensus, holders / insiders / short interest, prices incl. dead
companies, fund returns, StarMine scores, request-size limits.
Many field names are guesses on purpose: an error text is a useful answer. Every formula is marked 'cited' (the
name or form appears in a source listed on the Sources sheet) or 'guess'. Nothing in the file is a data value.
Layout (same as build_lseg_probe.py / lseg_pull_helpers.py): one block per formula; row 2 id, row 3 label, row 4
formula text, row 6 the formula. Blocks have their own width (wider for multi-column answers); the reader finds
blocks by the ids in row 2. Sheets: Check (live status), Index (static list for the reader: group, cited/guess,
pairs), Sources, TestSet (the 12 test companies, referenced by some formulas), data sheets.
The saved file stays on the PC; job tools/bbgq/jobs/lseg_eq_probe_v1.py reports metadata only.
usage: python3 docs/data_requests/build_lseg_equity_probe.py [out dir]"""
import os
import re
import sys
from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter as L

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "lseg_equity_probe_2026-11-17")
NAME = "LSEG_equity_probe_v1.xlsx"
END = "2026-11-17"
ROW0 = 6
ROWN = {"Universe": 150000, "Limits": 150000, "Holders": 60000}   # last row counted on the Check sheet (default 15000)

# ------------------------------------------------------------------ sources (S ids are used in the Index)
SOURCES = [
    ("S1", "https://community.developers.lseg.com/discussion/18416", "SCREEN(U(IN(Equity(active or inactive,public,primary))/*UNV:Public*/),IN(TR.ExchangeCountryCode,\"US\"),...,CURN=USD) in Excel; TR.CommonName, TR.CompanyMarketCap, TR.ExchangeCountry; 'curn=USD RH=In CH=Fd'"),
    ("S2", "https://community.developers.lseg.com/discussion/97692/historical-index-constituents-python-api/p1", "instrument '0#.SPX' with TR.IndexConstituentRIC, TR.IndexConstituentName and SDate (works to about 2000; coverage varies by index)"),
    ("S3", "https://www.uni-ulm.de/fileadmin/website_uni_ulm/allgemein/Update_Introduction_Datastream_May_2025.pdf", "Datastream: constituent list L<index> + MMYY; research lists F<country> (numbered sub-lists); dead lists DEAD<country>; WS/WSCOPE lists (active and dead); RI, UP, P, TIME; WC02999"),
    ("S4", "https://libanswers.london.edu/faq/175663", "Datastream historical constituent list = list code + MMYY (LFTSE1000199 = FTSE 100 in Jan 1999)"),
    ("S5", "https://community.developers.lseg.com/discussion/102231/trouble-downloading-constituent-list-russell-3000-for-a-particular-date-using-datastream-excel-ad", "Datastream Russell 3000 list LFRUSS3L + MMYY (LFRUSS3L0505)"),
    ("S6", "https://www.ifm.unibe.ch/e39710/e39716/e274093/files495520/DATASTREAM.pdf", "Datastream datatypes RI, P, UP, MV, NOSH, VO, VP, ISIN, DSCD, MNEM, NAME, BDATE, TIME; I/B/E/S EPS1, EPS1D, EPS2, EPS2D, A12FE; Worldscope WC01001, WC05301; lists WSCOPEUS, WSUS1..WSUS22"),
    ("S7", "https://datacenter.safe-frankfurt.de/documents/DDL_WS_content_guide.txt", "Worldscope items WC01001 net sales, WC01751 net income to common, WC01706, WC02999 total assets, WC04860 operating cash flow, WC05301 common shares, WC05350 fiscal year end date, WC07015 inactive date, WC07035 latest interim date"),
    ("S8", "https://community.developers.lseg.com/discussion/61761/how-to-check-the-status-of-instrument-active-or-inactive-using-dsws", "Datastream equity status datatype ESTAT"),
    ("S9", "https://community.developers.lseg.com/discussion/134295/how-can-i-extract-daily-data-for-all-datastream-indices-in-excel-using-a-formula-similar-to-dsgrid", "static DSGRID form: DSGRID(\"LFTSE100\",\"WSCD,SECD,NAME,TIME,WC05661\",\"Latest Value\",\"\",\"\",\"RowHeader=true;ColHeader=true;Heading=true;DispSeriesDescription=true\")"),
    ("S10", "https://community.developers.lseg.com/discussion/132701/how-to-access-historical-cusips-via-eikon-api", "TR.CUSIP, TR.CUSIP.Date (history with SDate/EDate/Frq), TR.RIC, TR.OrganizationId; PermID as instrument"),
    ("S11", "https://community.developers.lseg.com/discussion/23618", "TR.ISINCode, TR.OrganizationStatusCode; delisted RIC suffix such as ^C16"),
    ("S12", "https://community.developers.lseg.com/discussion/33401", "TR.ISIN and TR.ISINcode; RIC, ISIN or SEDOL input lists give the same result"),
    ("S13", "https://community.developers.lseg.com/discussion/24004/using-isins-cusips-rather-than-rics-with-eikon-data-api", "ISINs and CUSIPs work as instruments in =TR / get_data (not in RHistory)"),
    ("S14", "https://community.developers.lseg.com/discussion/76260/my-initial-query-i-was-testing-cik-versus-ticker-the-cik-is-pulling-in-some-null-results-compa/p1", "TR.CIKNUMBER; CIK as instrument; TR.F.PeriodEndDate, TR.F.TotAssets, TR.F.ComEqTot, TR.F.DebtTot, TR.BSPeriodEndDate, TR.TotalAssetsReported with SDate=0,EDate=-19,Period=FQ0,Frq=FQ"),
    ("S15", "https://community.developers.lseg.com/discussion/63068", "delisted RIC = RIC + ^<month letter><yy> (A = January)"),
    ("S16", "https://community.developers.lseg.com/discussion/75090/how-can-i-transcode-from-normal-ric-to-delisted-ric-so-that-i-can-query-the-price", "delisted RIC example PEUP.PA^A21; TR.RetireDate gives the delisting date"),
    ("S17", "https://community.developers.lseg.com/discussion/116250/fundamental-data-difference-between-tr-f-and-tr-fields-with-missing-data", "TR.F.TotRevenue, TR.F.TotRevenue.fperiod, TR.Revenue; SDate -30Y, FRQ FY, Curn, Scale"),
    ("S18", "https://community.developers.lseg.com/discussion/132467/company-fundamental-fundupdtype-sometimes-returns-nat-sometimes-value-ie-original-restated", "TR.TotalRevenue with .calcdate .date .periodenddate .source .PeriodLength; TR.F.SourceDate, TR.F.SourceDate.FundUpdType, TR.F.TotRevenue.FundUpdType; Period=FY0 SDate=0 EDate=-2"),
    ("S19", "https://community.developers.lseg.com/discussion/132921/how-to-return-result-of-tr-f-originalannouncementdate-in-local-timezone", "TR.F.OriginalAnnouncementDate(Period=FY0,Frq=FY,SDate=1D)"),
    ("S20", "https://community.developers.lseg.com/discussion/134162/is-there-a-way-to-pull-up-monthly-data", "TR.F.StatementDate, TR.F.OriginalAnnouncementDate(StType=INC|BAL|CAS), TR.F.TOTLIAB, TR.F.INCBEFTAX, TR.F.COMEQTOT, TR.REVENUESMARTEST; field.Date sub-field"),
    ("S21", "https://community.developers.lseg.com/discussion/132192/question-related-to-workspace-python-api-for-case-14761377", "parameter reportingState Rsdt / Orig: 'Rsdt is the most recent period and Orig is the initial update for that period'"),
    ("S22", "https://refinitivsso.cloud.answerhub.com/questions/63038/duplicate-reported-date-with-different-data-points.html", "ReportingState=Orig with TR.F.EBIT, TR.F.OriginalAnnouncementDate, TR.F.EBIT.calcdate, TR.ISOriginalAnnouncementDate, ConsolBasis=Consolidated"),
    ("S23", "https://community.developers.lseg.com/discussion/132843/financial-data-quarterly-wrong-date", "TR.TotAssets with .date, FRQ=FQ, Period=FQ0"),
    ("S24", "https://community.developers.lseg.com/discussion/111351/eps-mean-by-date", "TR.EPSMean.date; TR.EPSMean(Period=FY1,Frq=D,SDate=0,EDate=-50)"),
    ("S25", "https://community.developers.lseg.com/discussion/67306/historical-estimates", "TR.EPSMean, TR.EPSMean.periodenddate, TR.RevenueMean with SDate and Period"),
    ("S26", "https://community.developers.lseg.com/discussion/131565/analyst-forecast-data-and-actual-eps-data-for-all-us-firms/p1", "Excel parameter string 'Period=.. SDate=.. EDate=.. Frq=.. CH=IN RH=calcdate'; Period NTM, Frq M from 2000; TR.EPSActValue; instrument ranges"),
    ("S27", "https://community.developers.lseg.com/discussion/16838/is-it-possible-to-pull-history-on-non-price-volume-fields-such-as-tr-epsactvalue-get-timeseries", "TR.EPSActValue.date; TR.EPSActValue with SDate=0, EDate=-7, Frq=FQ, Period=FI0"),
    ("S28", "https://community.developers.lseg.com/discussion/132308/i-want-to-get-the-future-earning-reports-date-for-a-given-stock-and-also-the-past-earning-reports-d", "=RDP.Data(\"VOD.L\",\"TR.PreferredMeasureActReportDate\",\"SDate=2025-05-01 CH=Fd RH=IN\"); TR.ExpectedReportDate"),
    ("S29", "https://community.developers.lseg.com/discussion/133189/unable-to-retrieve-quarterly-equity-shareholder-data-for-rog-s-from-2014q1-to-2024q2-using-standard", "holders by quarter in Excel: TR.InvestorFullName;TR.InvAddrCountry,TR.SharesHeld.CalcDate;TR.SharesHeld with 'Sdate=2014-01-01 EDate=2024-04-01 Frq=Q Date=CalcDate CH=Fd RH=IN'"),
    ("S30", "https://community.developers.lseg.com/discussion/94150", "TR.InvestorFullName, TR.SharesHeld, TR.SharesHeld.calcdate, TR.PctOfSharesOutHeld with SDate"),
    ("S31", "https://community.developers.lseg.com/discussion/131468/holdings-data-on-the-ultimate-parent-level", "TR.HoldingsDate, TR.SharesHeldValue, TR.FilingType, TR.UltPrntPctOfShrsOutHld(.InvestorPermId); StartNum / EndNum"),
    ("S32", "https://community.developers.lseg.com/discussion/85010", "TR.InvestorFullName.investorpermid; investor PermID 4297651992 = The Vanguard Group, Inc."),
    ("S33", "https://community.developers.lseg.com/discussion/33941/missing-information-on-insider-transactions", "insider fields TR.TransactionDate, TR.InsiderFullName, TR.InsiderRole, TR.AdjSharesTraded, TR.TransactionType, TR.TransactionPrice with SDate=0D EDate=-30AY"),
    ("S34", "https://community.developers.lseg.com/discussion/41736/retrieve-null-data-when-using-tr-shortinterest", "=TR(\".FTSE\",\"TR.ShortInterest(Scale=0)\",\"SDate=2018-12-03 Frq=D CH=Fd;date RH=IN\") (returned NULL for that user)"),
    ("S35", "https://community.developers.lseg.com/discussion/54807/total-returns-for-funds", "Lipper codes LP<digits> (LP68167376); TR.FundRollingPerformance(RollTimeFrame=10Y Interval=M) with Curn=Native"),
    ("S36", "https://community.developers.lseg.com/discussion/97686/how-to-extract-fund-net-asset-value-given-fund-lipper-id-at-the-end-of-each-month/p1", "TR.NETASSETVAL.Date; TR.NETASSETVAL for LP60010877 with SDate/EDate/Frq=M"),
    ("S37", "https://community.developers.lseg.com/discussion/61628/how-to-extract-multiple-years-of-eq-scores", "=TR(\"PEUP.PA\",\"TR.EQCtryRank\",\"Period:FY0;FY-20 CH=Fd RH=fpa\") (StarMine earnings quality by fiscal period, from 2005 there)"),
    ("S38", "https://community.developers.lseg.com/discussion/133967/starmine-data-through-workspace-api", "TR.EQCountryListRank, TR.ARMIntraSectorScore (Data Item Browser: no time series)"),
    ("S39", "https://community.developers.lseg.com/discussion/133855/accesing-historical-starmine-value-momentum-model-scores", "TR.ValMoCountryRank with .Date (no time series)"),
    ("S40", "repo: tools/bbgq/results/lseg_probe_v1.txt", "on this PC: RDP.Data(\"AAPL.O\",\"TR.PriceClose.date;TR.PriceClose\",\"SDate=1990-01-01 ... Frq=M CH=Fd RH=IN\") monthly from 1990; old TR function works; DSGRID options string"),
    ("S41", "repo: tools/bbgq/results/lseg_probe_v2.txt", "on this PC: RHistory(\"<RIC>\",\".Timestamp;.Close\",\"START:.. INTERVAL:1MO\",,\"TSREPEAT:NO CH:Fd\"); TR.CLOSEPRICE"),
    ("S42", "repo: tools/bbgq/results/lseg_pull_2026-11-12_read_v1c.txt", "on this PC: Datastream accepts Workspace codes as \"<RIC>\"; DSGRID(\"@:USSP500\",\"A12FE\",...) from 1985"),
    ("S43", "https://libguides.princeton.edu/datastream/forecasts", "I/B/E/S in Datastream = company code + I/B/E/S datatype; most complete for fiscal year 1 and 2"),
]

# ------------------------------------------------------------------ test set (identifiers are inputs, not data)
#           label, Workspace instrument, ISIN, delisted-RIC guess, kind
TEST = [("Apple", "AAPL.O", "US0378331005", "", "live"), ("Microsoft", "MSFT.O", "US5949181045", "", "live"),
        ("JPMorgan Chase", "JPM.N", "US46625H1005", "", "live"), ("Exxon Mobil", "XOM.N", "US30231G1022", "", "live"),
        ("Johnson & Johnson", "JNJ.N", "US4781601046", "", "live"), ("Coca-Cola", "KO.N", "US1912161007", "", "live"),
        ("Lehman Brothers (bankrupt 2008)", "US5249081002", "US5249081002", "LEH.N^I08", "dead"),
        ("Enron (bankrupt 2001)", "US2935611069", "US2935611069", "ENE.N^A02", "dead"),
        ("Twitter (taken private 2022)", "US90184L1026", "US90184L1026", "TWTR.N^K22", "dead"),
        ("General Electric (restated 2005 and 2009)", "GE.N", "US3696043013", "", "restated"),
        ("Kraft Heinz (restated 2016-17 in 2019)", "KHC.O", "US5007541064", "", "restated"),
        ("Super Micro Computer (restated FY2015-17 in 2019)", "SMCI.O", "US86800U1043", "", "restated")]
TS_RANGE = "TestSet!$B$4:$B$15"
TS_ISINS = ",".join(t[2] for t in TEST)
ISIN = {t[1]: t[2] for t in TEST}
LEH, ENE, TWTR = "US5249081002", "US2935611069", "US90184L1026"

DSOPT = "RowHeader=true;TimeSeriesList=true;ColHeader=true;DispSeriesDescription=false;YearlyTSFormat=false;QuarterlyTSFormat=false"
DSSTAT = "RowHeader=true;ColHeader=true;Heading=true;DispSeriesDescription=true"
SCR_ALL = 'SCREEN(U(IN(Equity(active or inactive,public,primary))/*UNV:Public*/),IN(TR.ExchangeCountryCode,""US""),CURN=USD)'


def inst(x):
    return x if x.startswith("TestSet!") else '"%s"' % x


def rd(x, fields, params="CH=Fd RH=IN", fn="RDP.Data"):
    return '=%s(%s,"%s","%s")' % (fn, inst(x), fields, params)


def hist(x, f, start="1980-01-01", frq="M", extra=""):
    return rd(x, "%s.date;%s" % (f, f), "%sSDate=%s EDate=%s Frq=%s CH=Fd RH=IN" % (extra, start, END, frq))


def ds(codes, dt, start="1979-12-31", frq="M"):
    return '=DSGRID("%s","%s","%s","-0D","%s","%s","")' % (codes, dt, start, frq, DSOPT)


def dss(codes, dt):
    return '=DSGRID("%s","%s","Latest Value","","","%s","")' % (codes, dt, DSSTAT)


P = []   # dicts: group, sheet, what, f, cite, src, pair, kind, w


def add(group, sheet, what, f, cite, src="", pair="", kind="series", w=None):
    P.append(dict(group=group, sheet=sheet, what=what, f=f, cite=cite, src=src, pair=pair, kind=kind, w=w))


# ------------------------------------------------------------------ 1 universe incl. dead companies
G, S = "1 Universe", "Universe"
add(G, S, "SCREEN US primary common, active OR inactive (cited form, with UNV comment)", rd(SCR_ALL, "TR.CommonName", "curn=USD RH=In CH=Fd"), "cited", "S1", kind="list")
add(G, S, "same SCREEN without the /*UNV:Public*/ comment, plus retire date",
    rd('SCREEN(U(IN(Equity(active or inactive,public,primary))),IN(TR.ExchangeCountryCode,""US""),CURN=USD)', "TR.CommonName;TR.RetireDate", "curn=USD RH=In CH=Fd"), "cited", "S1,S16", kind="list")
add(G, S, "SCREEN active only (to compare the count)",
    rd('SCREEN(U(IN(Equity(active,public,primary))),IN(TR.ExchangeCountryCode,""US""),CURN=USD)', "TR.CommonName", "curn=USD RH=In CH=Fd"), "cited", "S1", kind="list")
add(G, S, "SCREEN inactive only (guessed keyword 'inactive' alone)",
    rd('SCREEN(U(IN(Equity(inactive,public,primary))),IN(TR.ExchangeCountryCode,""US""),CURN=USD)', "TR.CommonName;TR.RetireDate", "curn=USD RH=In CH=Fd"), "guess", "S1", kind="list")
add(G, S, "SCREEN active or inactive, identifiers for the WRDS join (CUSIP, ISIN, CIK)",
    rd(SCR_ALL, "TR.CommonName;TR.CUSIP;TR.ISIN;TR.CIKNUMBER", "curn=USD RH=In CH=Fd"), "cited", "S1,S10,S12,S14", kind="list")
add(G, S, "S&P 500 members today (chain 0#.SPX)", rd("0#.SPX", "TR.IndexConstituentRIC;TR.IndexConstituentName"), "cited", "S2", kind="list")
add(G, S, "S&P 500 members on 2000-01-03", rd("0#.SPX", "TR.IndexConstituentRIC;TR.IndexConstituentName", "SDate=2000-01-03 CH=Fd RH=IN"), "cited", "S2", kind="list")
add(G, S, "S&P 500 members on 1990-01-02 (depth test)", rd("0#.SPX", "TR.IndexConstituentRIC;TR.IndexConstituentName", "SDate=1990-01-02 CH=Fd RH=IN"), "cited", "S2", kind="list")
add(G, S, "Russell 3000 members on 2005-06-30 (chain 0#.RUA guessed)", rd("0#.RUA", "TR.IndexConstituentRIC;TR.IndexConstituentName", "SDate=2005-06-30 CH=Fd RH=IN"), "guess", "S2", kind="list")
add(G, S, "Datastream S&P 500 list today (LS&PCOMP)", dss("LS&PCOMP", "NAME,ISIN,DSCD"), "cited", "S3,S9", kind="list")
add(G, S, "Datastream S&P 500 list Jan 2000 (LS&PCOMP0100)", dss("LS&PCOMP0100", "NAME,ISIN,DSCD"), "cited", "S3,S4", kind="list")
add(G, S, "Datastream S&P 500 list Jan 1990 (LS&PCOMP0190; depth guess)", dss("LS&PCOMP0190", "NAME,ISIN,DSCD"), "cited", "S3,S4", kind="list")
add(G, S, "Datastream Russell 3000 list Jan 2005 (LFRUSS3L0105)", dss("LFRUSS3L0105", "NAME,ISIN"), "cited", "S5", kind="list")
add(G, S, "Datastream US dead list DEADUS1 (DEAD+country cited; numbering guessed)", dss("DEADUS1", "NAME,ISIN,WC07015"), "guess", "S3,S7", kind="list")
add(G, S, "Datastream US dead list DEADUS (no number)", dss("DEADUS", "NAME,ISIN,WC07015"), "guess", "S3", kind="list")
add(G, S, "Datastream US research list FUSA (F+country cited; code guessed)", dss("FUSA", "NAME,ISIN,ESTAT"), "guess", "S3,S8", kind="list")
add(G, S, "Datastream Worldscope US list WSCOPEUS (active and dead)", dss("WSCOPEUS", "NAME,ISIN,ESTAT"), "cited", "S6,S8", kind="list")
add(G, S, "Datastream Worldscope US sub-list WSUS1", dss("WSUS1", "NAME,ISIN,ESTAT,WC07015"), "cited", "S6,S7,S8", kind="list")

# ------------------------------------------------------------------ 2 identifiers
G, S = "2 Identifiers", "Ids"
for f, c, src in [("TR.CUSIP", "cited", "S10"), ("TR.ISIN", "cited", "S12"), ("TR.ISINCode", "cited", "S11"), ("TR.SEDOL", "guess", ""),
                  ("TR.SEDOLCode", "guess", ""), ("TR.TickerSymbol", "guess", ""), ("TR.RIC", "cited", "S10"),
                  ("TR.OrganizationId", "cited", "S10"), ("TR.CIKNUMBER", "cited", "S14"),
                  ("TR.CommonName", "cited", "S1"), ("TR.OrganizationStatusCode", "cited", "S11"), ("TR.RetireDate", "cited", "S16")]:
    add(G, S, "%s for the 12 test companies (TestSet sheet)" % f, rd(TS_RANGE, f), c, src + (",S26" if src else "S26"), kind="static")
add(G, S, "CUSIP history with dates (Apple)", rd("AAPL.O", "TR.CUSIP.Date;TR.CUSIP", "SDate=1980-01-01 EDate=%s Frq=D CH=Fd RH=IN" % END), "cited", "S10")
add(G, S, "CIK as instrument (Apple 0000320193)", rd("0000320193", "TR.CommonName;TR.RIC;TR.ISIN"), "cited", "S14", kind="static")
add(G, S, "CUSIP as instrument (Lehman 524908100)", rd("524908100", "TR.CommonName;TR.RetireDate;TR.ISIN"), "cited", "S13", kind="static")
add(G, S, "delisted RIC guess Lehman LEH.N^I08", rd("LEH.N^I08", "TR.CommonName;TR.ISIN;TR.RetireDate"), "guess", "S15,S16", kind="static")
add(G, S, "delisted RIC guess Enron ENE.N^A02", rd("ENE.N^A02", "TR.CommonName;TR.ISIN;TR.RetireDate"), "guess", "S15,S16", kind="static")
add(G, S, "delisted RIC guess Twitter TWTR.N^K22", rd("TWTR.N^K22", "TR.CommonName;TR.ISIN;TR.RetireDate"), "guess", "S15,S16", kind="static")
add(G, S, "Datastream static codes for the test set by ISIN (ISIN, DSCD, MNEM, NAME)", dss(TS_ISINS, "ISIN,DSCD,MNEM,NAME"), "cited", "S6,S9", kind="static")
add(G, S, "Datastream status and dates for the test set (ESTAT, BDATE, TIME, WC07015)", dss(TS_ISINS, "ESTAT,BDATE,TIME,WC07015"), "cited", "S3,S6,S7,S8", kind="static")
add(G, S, "Datastream Worldscope code / CUSIP-like items for the test set (WC06004 CUSIP, WC06008 ISIN; guesses)", dss(TS_ISINS, "WC06004,WC06008,WC06006"), "guess", "", kind="static")

# ------------------------------------------------------------------ 3 accounts: first reported vs restated
G, S = "3 Accounts", "Accounts"
ANN = "Period=FY0 Frq=FY SDate=0 EDate=-46 "
QTR = "Period=FQ0 Frq=FQ SDate=0 EDate=-180 "
pairs = [("KHC.O", "TR.F.TotRevenue", "cited", "S17", ANN, "annual"), ("KHC.O", "TR.F.NetIncAfterMinorInt", "guess", "", ANN, "annual"),
         ("KHC.O", "TR.F.TotAssets", "cited", "S14", ANN, "annual"), ("GE.N", "TR.F.TotRevenue", "cited", "S17", ANN, "annual"),
         ("GE.N", "TR.F.NetIncAfterMinorInt", "guess", "", ANN, "annual"), ("GE.N", "TR.F.TotAssets", "cited", "S14", ANN, "annual"),
         ("GE.N", "TR.F.NetCashFlowOp", "guess", "", ANN, "annual"),
         ("SMCI.O", "TR.F.TotRevenue", "cited", "S17", ANN, "annual"), ("AAPL.O", "TR.F.TotRevenue", "cited", "S17", ANN, "annual (control)"),
         ("KHC.O", "TR.F.TotRevenue", "cited", "S17", QTR, "quarterly"), ("GE.N", "TR.F.NetIncAfterMinorInt", "guess", "", QTR, "quarterly")]
for k, (ric, f, c, src, per, lab) in enumerate(pairs, 1):
    for state in ("Orig", "Rsdt"):
        add(G, S, "%s %s %s, ReportingState=%s" % (ric, f, lab, state),
            rd(ric, "%s.periodenddate;%s" % (f, f), per + "ReportingState=%s CH=Fd RH=IN" % state),
            c if c == "guess" else "cited", ",".join(x for x in (src, "S14,S21,S22") if x), pair="PR%02d-%s" % (k, state))
add(G, S, "KHC annual dates: period end, original announcement, source date, original/restated flag, statement date",
    rd("KHC.O", "TR.F.TotRevenue.periodenddate;TR.F.OriginalAnnouncementDate;TR.F.SourceDate;TR.F.SourceDate.FundUpdType;TR.F.TotRevenue.FundUpdType;TR.F.StatementDate", ANN + "CH=Fd RH=IN"),
    "cited", "S18,S19,S20")
add(G, S, "KHC quarterly dates: same fields", rd("KHC.O", "TR.F.TotRevenue.periodenddate;TR.F.OriginalAnnouncementDate;TR.F.SourceDate;TR.F.TotRevenue.FundUpdType", QTR + "CH=Fd RH=IN"), "cited", "S18,S19")
add(G, S, "KHC revenue calcdate (when the value was computed)", rd("KHC.O", "TR.F.TotRevenue.periodenddate;TR.F.TotRevenue.calcdate;TR.F.TotRevenue", ANN + "CH=Fd RH=IN"), "cited", "S22")
add(G, S, "older field TR.TotalRevenue with source and period length (KHC)", rd("KHC.O", "TR.TotalRevenue.periodenddate;TR.TotalRevenue;TR.TotalRevenue.source;TR.TotalRevenue.PeriodLength", ANN + "CH=Fd RH=IN"), "cited", "S18")
add(G, S, "older announcement date TR.ISOriginalAnnouncementDate (GE)", rd("GE.N", "TR.ISOriginalAnnouncementDate", ANN + "CH=Fd RH=IN"), "cited", "S22")
add(G, S, "TR.F.PeriodEndDate + TR.F.TotAssets quarterly (cited form)", rd("GE.N", "TR.F.PeriodEndDate;TR.F.TotAssets", QTR + "CH=Fd RH=IN"), "cited", "S14")
add(G, S, "depth: Apple revenue annual from 1980", rd("AAPL.O", "TR.F.TotRevenue.periodenddate;TR.F.TotRevenue", ANN + "CH=Fd RH=IN"), "cited", "S17")
add(G, S, "depth: Apple revenue quarterly", rd("AAPL.O", "TR.F.TotRevenue.periodenddate;TR.F.TotRevenue", QTR + "CH=Fd RH=IN"), "cited", "S17")
add(G, S, "dead company: Enron revenue (by ISIN)", rd(ENE, "TR.F.TotRevenue.periodenddate;TR.F.TotRevenue", ANN + "CH=Fd RH=IN"), "cited", "S13,S17")
add(G, S, "dead company: Lehman total assets (by ISIN)", rd(LEH, "TR.F.TotAssets.periodenddate;TR.F.TotAssets", ANN + "CH=Fd RH=IN"), "cited", "S13,S14")
add(G, S, "alt spelling net income: TR.F.NetIncAvailToComShr (KHC)", rd("KHC.O", "TR.F.NetIncAvailToComShr.periodenddate;TR.F.NetIncAvailToComShr", ANN + "CH=Fd RH=IN"), "guess")
add(G, S, "alt spelling operating cash flow: TR.F.NetCashFlowOpAct (GE)", rd("GE.N", "TR.F.NetCashFlowOpAct.periodenddate;TR.F.NetCashFlowOpAct", ANN + "CH=Fd RH=IN"), "guess")
add(G, S, "alt spelling shares: TR.F.ComShrOutsTot (GE)", rd("GE.N", "TR.F.ComShrOutsTot.periodenddate;TR.F.ComShrOutsTot", ANN + "CH=Fd RH=IN"), "guess")
add(G, S, "older fields: TR.NetIncome / TR.CashFromOperatingActivities (GE)", rd("GE.N", "TR.NetIncome;TR.CashFromOperatingActivities", ANN + "CH=Fd RH=IN"), "guess")
RST = ",".join(ISIN[x] for x in ("KHC.O", "GE.N", "SMCI.O"))
add(G, S, "Datastream Worldscope revenue WC01001, yearly, KHC/GE/SMCI", ds(RST, "WC01001", frq="Y"), "cited", "S6,S7")
add(G, S, "Datastream Worldscope net income WC01751, yearly", ds(RST, "WC01751", frq="Y"), "cited", "S7")
add(G, S, "Datastream Worldscope total assets WC02999, yearly", ds(RST, "WC02999", frq="Y"), "cited", "S3,S7")
add(G, S, "Datastream Worldscope operating cash flow WC04860 and common shares WC05301, yearly", ds(RST, "WC04860,WC05301", frq="Y"), "cited", "S6,S7")
add(G, S, "Datastream Worldscope revenue WC01001 quarterly (does Q frequency exist?)", ds(RST, "WC01001", frq="Q"), "guess", "S7")
add(G, S, "Datastream Worldscope fiscal year end / latest interim dates (static)", dss(RST + "," + ENE, "WC05350,WC07035,WC07015"), "cited", "S7,S9", kind="static")
add(G, S, "Datastream Worldscope revenue for dead Enron and Lehman, yearly", ds(ENE + "," + LEH, "WC01001", frq="Y"), "cited", "S7")

# ------------------------------------------------------------------ 4 estimates as they stood
G, S = "4 Estimates", "Estimates"
for ric, per in [("AAPL.O", "FY1"), ("AAPL.O", "FY2"), ("GE.N", "FY1"), (LEH, "FY1")]:
    add(G, S, "%s consensus EPS mean %s, monthly from 1990" % (ric, per), hist(ric, "TR.EPSMean", "1990-01-01", extra="Period=%s " % per), "cited", "S24,S26" + (",S13" if ric.startswith("US") else ""))
add(G, S, "AAPL revenue mean FY1 monthly from 1990", hist("AAPL.O", "TR.RevenueMean", "1990-01-01", extra="Period=FY1 "), "cited", "S25,S26")
add(G, S, "AAPL number of EPS estimates FY1 (TR.EPSNumIncEstimates guess)", hist("AAPL.O", "TR.EPSNumIncEstimates", "1990-01-01", extra="Period=FY1 "), "guess")
add(G, S, "AAPL number of EPS estimates FY1 (TR.NumOfEst guess)", hist("AAPL.O", "TR.NumOfEst", "1990-01-01", extra="Period=FY1 "), "guess")
add(G, S, "AAPL EPS mean next 12 months (Period=NTM)", hist("AAPL.O", "TR.EPSMean", "2000-01-01", extra="Period=NTM "), "cited", "S26")
add(G, S, "AAPL EPS mean FY1, cited Excel form RH=calcdate", rd("AAPL.O", "TR.EPSMean", "Period=FY1 SDate=1990-01-01 EDate=%s Frq=M CH=IN RH=calcdate" % END), "cited", "S26")
add(G, S, "AAPL EPS mean FY1 with fiscal period end of each snapshot", rd("AAPL.O", "TR.EPSMean.date;TR.EPSMean.periodenddate;TR.EPSMean", "Period=FY1 SDate=1990-01-01 EDate=%s Frq=M CH=Fd RH=IN" % END), "cited", "S25")
add(G, S, "AAPL EPS mean FY1 daily, last 50 days (cited relative form)", rd("AAPL.O", "TR.EPSMean.date;TR.EPSMean", "Period=FY1 Frq=D SDate=0 EDate=-50 CH=Fd RH=IN"), "cited", "S24")
add(G, S, "AAPL StarMine SmartEstimate revenue (TR.REVENUESMARTEST) monthly", hist("AAPL.O", "TR.REVENUESMARTEST", "2000-01-01", extra="Period=FY1 "), "cited", "S20")
add(G, S, "AAPL actual EPS quarterly, last 120 quarters", rd("AAPL.O", "TR.EPSActValue.date;TR.EPSActValue", "SDate=0 EDate=-120 Frq=FQ Period=FI0 CH=Fd RH=IN"), "cited", "S27")
add(G, S, "AAPL actual EPS annual, last 40 years", rd("AAPL.O", "TR.EPSActValue.date;TR.EPSActValue", "SDate=0 EDate=-40 Frq=FY Period=FY0 CH=Fd RH=IN"), "cited", "S27")
add(G, S, "AAPL past report dates from 1990 (cited single-SDate form)", rd("AAPL.O", "TR.PreferredMeasureActReportDate", "SDate=1990-01-01 CH=Fd RH=IN"), "cited", "S28")
add(G, S, "AAPL past report dates, quarterly series form", rd("AAPL.O", "TR.PreferredMeasureActReportDate", "SDate=0 EDate=-120 Frq=FQ Period=FQ0 CH=Fd RH=IN"), "cited", "S28")
add(G, S, "AAPL report date of actual EPS (TR.EPSActReportDate guess)", rd("AAPL.O", "TR.EPSActReportDate", "SDate=0 EDate=-120 Frq=FQ Period=FQ0 CH=Fd RH=IN"), "guess")
add(G, S, "test set: next expected report date", rd(TS_RANGE, "TR.ExpectedReportDate"), "cited", "S28,S26", kind="static")
add(G, S, "Datastream I/B/E/S EPS1 / EPS1D / EPS2 for Apple by ISIN, monthly", ds(ISIN["AAPL.O"], "EPS1,EPS1D,EPS2"), "cited", "S6,S43")
add(G, S, "Datastream I/B/E/S EPS1 for KHC, GE, Lehman, Enron, monthly", ds(",".join([ISIN["KHC.O"], ISIN["GE.N"], LEH, ENE]), "EPS1"), "cited", "S6,S43")
add(G, S, "Datastream I/B/E/S number of estimates EPS1NE (guess)", ds(ISIN["AAPL.O"], "EPS1NE"), "guess", "S43")
add(G, S, "Datastream I/B/E/S 12m forward EPS A12FE on a company (code worked for the S&P aggregate)", ds(ISIN["AAPL.O"], "A12FE"), "cited", "S6,S42")

# ------------------------------------------------------------------ 5 holders, insiders, short interest
G, S = "5 Holders", "Holders"
H4 = "TR.InvestorFullName;TR.SharesHeld.CalcDate;TR.SharesHeld"
add(G, S, "KO top 20 holders each quarter 2014-2024 (cited Excel form + StartNum/EndNum)", rd("KO.N", H4, "Sdate=2014-01-01 EDate=2024-04-01 Frq=Q Date=CalcDate StartNum=1 EndNum=20 CH=Fd RH=IN"), "cited", "S29,S31", kind="list")
add(G, S, "KO top 20 holders each quarter 1995-2013 (depth)", rd("KO.N", H4, "Sdate=1995-01-01 EDate=2013-12-31 Frq=Q Date=CalcDate StartNum=1 EndNum=20 CH=Fd RH=IN"), "cited", "S29,S31", kind="list")
add(G, S, "KO holders as of 2005-12-31 with % of shares out", rd("KO.N", "TR.InvestorFullName;TR.SharesHeld;TR.SharesHeld.calcdate;TR.PctOfSharesOutHeld", "SDate=2005-12-31 StartNum=1 EndNum=50 CH=Fd RH=IN"), "cited", "S30,S31", kind="list")
add(G, S, "KO holders as of 1999-12-31", rd("KO.N", "TR.InvestorFullName;TR.SharesHeld;TR.SharesHeld.calcdate", "SDate=1999-12-31 StartNum=1 EndNum=50 CH=Fd RH=IN"), "cited", "S30,S31", kind="list")
add(G, S, "KO holders as of 1990-12-31 (depth)", rd("KO.N", "TR.InvestorFullName;TR.SharesHeld;TR.SharesHeld.calcdate", "SDate=1990-12-31 StartNum=1 EndNum=50 CH=Fd RH=IN"), "cited", "S30,S31", kind="list")
add(G, S, "AAPL holders today: holdings date, value, filing type", rd("AAPL.O", "TR.InvestorFullName;TR.HoldingsDate;TR.SharesHeld;TR.SharesHeldValue;TR.FilingType", "StartNum=1 EndNum=100 CH=Fd RH=IN"), "cited", "S31", kind="list")
add(G, S, "AAPL holders with investor PermID (for the 13F join)", rd("AAPL.O", "TR.InvestorFullName;TR.InvestorFullName.investorpermid;TR.InvAddrCountry", "StartNum=1 EndNum=100 CH=Fd RH=IN"), "cited", "S29,S32", kind="list")
add(G, S, "AAPL ultimate-parent holders", rd("AAPL.O", "TR.UltPrntPctOfShrsOutHld;TR.UltPrntPctOfShrsOutHld.InvestorPermId", "StartNum=1 EndNum=100 CH=Fd RH=IN"), "cited", "S31", kind="list")
add(G, S, "dead company: Lehman holders as of 2007-12-31 (by ISIN)", rd(LEH, "TR.InvestorFullName;TR.SharesHeld;TR.SharesHeld.calcdate", "SDate=2007-12-31 StartNum=1 EndNum=50 CH=Fd RH=IN"), "cited", "S13,S30", kind="list")
add(G, S, "manager side: Vanguard (investor PermID 4297651992) name", rd("4297651992", "TR.InvestorFullName;TR.CommonName"), "guess", "S32", kind="static")
add(G, S, "manager side: Vanguard portfolio as of 2015-12-31 (field guesses TR.PortfolioHoldingName / TR.PortfolioHoldingRIC)", rd("4297651992", "TR.PortfolioHoldingName;TR.PortfolioHoldingRIC;TR.PortfolioSharesHeld", "SDate=2015-12-31 CH=Fd RH=IN"), "guess", "S32", kind="list")
add(G, S, "manager side: Vanguard holdings (field guesses TR.HoldingRIC / TR.HoldingName)", rd("4297651992", "TR.HoldingRIC;TR.HoldingName;TR.HoldingShares", "SDate=2015-12-31 CH=Fd RH=IN"), "guess", "S32", kind="list")
INS = "TR.TransactionDate;TR.InsiderFullName;TR.InsiderRole;TR.AdjSharesTraded;TR.TransactionType;TR.TransactionPrice"
add(G, S, "AAPL insider transactions, full history (cited fields)", rd("AAPL.O", INS, "SDate=0D EDate=-30AY CH=Fd RH=IN"), "cited", "S33", kind="list")
add(G, S, "KHC insider transactions, full history", rd("KHC.O", INS, "SDate=0D EDate=-30AY CH=Fd RH=IN"), "cited", "S33", kind="list")
add(G, S, "dead company: Enron insider transactions (by ISIN)", rd(ENE, INS, "SDate=0D EDate=-30AY CH=Fd RH=IN"), "cited", "S13,S33", kind="list")
add(G, S, "AAPL short interest, cited TR form, monthly from 2000", '=TR("AAPL.O","TR.ShortInterest(Scale=0)","SDate=2000-01-01 EDate=%s Frq=M CH=Fd;date RH=IN")' % END, "cited", "S34")
add(G, S, "AAPL short interest with .date, RDP.Data, twice-monthly as daily from 2000", hist("AAPL.O", "TR.ShortInterest", "2000-01-01", frq="D"), "cited", "S34")
add(G, S, "KO short interest as % of float (TR.ShortInterestPctFloat guess)", hist("KO.N", "TR.ShortInterestPctFloat", "2000-01-01"), "guess")
add(G, S, "KO days to cover (TR.DaysToCover guess)", hist("KO.N", "TR.DaysToCover", "2000-01-01"), "guess")
add(G, S, "Datastream short interest datatype SHORTINT (guess), Apple", ds(ISIN["AAPL.O"], "SHORTINT"), "guess")

# ------------------------------------------------------------------ 6 prices and returns
G, S = "6 Prices", "Prices"
add(G, S, "6 live large caps in one formula (TestSet B4:B9), close monthly from 1980", hist("TestSet!$B$4:$B$9", "TR.PriceClose"), "cited", "S40,S26")
for t in TEST[6:]:
    add(G, S, "%s close, monthly from 1980" % t[0], hist(t[1], "TR.PriceClose"), "cited", "S40" + (",S13" if t[4] == "dead" else ""))
add(G, S, "12 test companies Datastream total return index RI in one grid, monthly from 1980", ds(TS_ISINS, "RI"), "cited", "S3,S6")
for t in TEST[6:9]:
    add(G, S, "%s Datastream RI alone, monthly from 1980" % t[0], ds(t[2], "RI"), "cited", "S3,S6")
add(G, S, "Lehman Datastream P, UP, MV, NOSH, VO monthly", ds(LEH, "P,UP,MV,NOSH,VO"), "cited", "S3,S6")
add(G, S, "Enron Datastream P, UP, MV, NOSH, VO monthly", ds(ENE, "P,UP,MV,NOSH,VO"), "cited", "S3,S6")
add(G, S, "Twitter Datastream P, UP, MV, NOSH, VO monthly", ds(TWTR, "P,UP,MV,NOSH,VO"), "cited", "S3,S6")
add(G, S, "Apple via Workspace code inside Datastream <AAPL.O>, RI", ds("<AAPL.O>", "RI"), "cited", "S42")
add(G, S, "Apple Datastream mnemonic @AAPL (guess), RI", ds("@AAPL", "RI"), "guess")
add(G, S, "JPMorgan Datastream mnemonic U:JPM (guess), RI", ds("U:JPM", "RI"), "guess")
add(G, S, "Apple total return TR.TotalReturn monthly (guess)", hist("AAPL.O", "TR.TotalReturn"), "guess")
add(G, S, "Apple market cap TR.CompanyMarketCap monthly", hist("AAPL.O", "TR.CompanyMarketCap"), "cited", "S1")
add(G, S, "Lehman market cap TR.CompanyMarketCap monthly", hist(LEH, "TR.CompanyMarketCap"), "cited", "S1,S13")
add(G, S, "Apple shares outstanding TR.SharesOutstanding monthly (guess)", hist("AAPL.O", "TR.SharesOutstanding"), "guess")
add(G, S, "Enron shares outstanding TR.SharesOutstanding monthly (guess)", hist(ENE, "TR.SharesOutstanding"), "guess")
add(G, S, "Apple volume TR.Volume monthly (guess)", hist("AAPL.O", "TR.Volume"), "guess")
add(G, S, "Apple close price TR.CLOSEPRICE monthly (worked for futures)", hist("AAPL.O", "TR.CLOSEPRICE"), "cited", "S41")
add(G, S, "Lehman close daily 2008 (by ISIN)", hist(LEH, "TR.PriceClose", "2008-01-01", frq="D"), "cited", "S13,S40")
add(G, S, "Lehman delisted RIC guess LEH.N^I08 close monthly", hist("LEH.N^I08", "TR.PriceClose"), "guess", "S15")
add(G, S, "Twitter delisted RIC guess TWTR.N^K22 close monthly", hist("TWTR.N^K22", "TR.PriceClose"), "guess", "S15")
add(G, S, "Lehman RHistory on delisted RIC guess LEH.N^I08", '=RHistory("LEH.N^I08",".Timestamp;.Close","START:01-Jan-1980 INTERVAL:1MO",,"TSREPEAT:NO CH:Fd")', "guess", "S15,S41")
add(G, S, "test set: retire date and status code (delisting)", rd(TS_RANGE, "TR.RetireDate;TR.OrganizationStatusCode"), "cited", "S11,S16,S26", kind="static")
add(G, S, "test set: delisting reason (TR.DelistingReason guess)", rd(TS_RANGE, "TR.DelistingReason;TR.DelistedDate"), "guess", "S26", kind="static")

# ------------------------------------------------------------------ 7 fund returns
G, S = "7 Funds", "Funds"
add(G, S, "Lipper fund LP68167376 rolling 10-year monthly performance (cited form)", '=TR("LP68167376","TR.FundRollingPerformance(RollTimeFrame=10Y Interval=M)","Curn=Native CH=Fd RH=IN")', "cited", "S35")
add(G, S, "Lipper fund LP60010877 NAV monthly from 1990", hist("LP60010877", "TR.NETASSETVAL", "1990-01-01"), "cited", "S36")
add(G, S, "Fundsmith Equity (ISIN GB00B41YBW71) NAV monthly", hist("GB00B41YBW71", "TR.NETASSETVAL", "2010-01-01"), "guess", "S36,S13")
add(G, S, "Vanguard 500 Index Admiral (ISIN US9229087104) NAV monthly", hist("US9229087104", "TR.NETASSETVAL", "1990-01-01"), "guess", "S36,S13")
add(G, S, "Fundsmith and Vanguard 500: Lipper id (TR.FundLipperID guess)", rd("GB00B41YBW71,US9229087104", "TR.FundLipperID;TR.FundName"), "guess", "", kind="static")
add(G, S, "Fundsmith rolling 10-year monthly performance by ISIN", '=TR("GB00B41YBW71","TR.FundRollingPerformance(RollTimeFrame=10Y Interval=M)","Curn=Native CH=Fd RH=IN")', "guess", "S35")
add(G, S, "SPY ETF (SPY.P) close monthly from 1993", hist("SPY.P", "TR.PriceClose", "1993-01-01"), "guess", "S40")
add(G, S, "SPY ETF NAV monthly", hist("SPY.P", "TR.NETASSETVAL", "1993-01-01"), "guess", "S36")
add(G, S, "Datastream RI for Fundsmith and SPY by ISIN", ds("GB00B41YBW71,US78462F1030", "RI"), "guess", "S6")
add(G, S, "Datastream RI for Vanguard 500 Admiral by ISIN", ds("US9229087104", "RI"), "guess", "S6")

# ------------------------------------------------------------------ 8 StarMine
G, S = "8 StarMine", "StarMine"
add(G, S, "Earnings quality country rank by fiscal year, cited TR form (KHC)", '=TR("KHC.O","TR.EQCtryRank","Period:FY0;FY-20 CH=Fd RH=fpa")', "cited", "S37")
add(G, S, "Earnings quality country rank, RDP.Data FY series (GE)", rd("GE.N", "TR.EQCtryRank.date;TR.EQCtryRank", "Period=FY0 Frq=FY SDate=0 EDate=-20 CH=Fd RH=IN"), "cited", "S37")
add(G, S, "Earnings quality country rank, monthly series (expected to fail)", hist("AAPL.O", "TR.EQCtryRank", "2000-01-01"), "cited", "S37")
add(G, S, "EQ country list rank today, test set", rd(TS_RANGE, "TR.EQCountryListRank"), "cited", "S38,S26", kind="static")
add(G, S, "ARM intra-sector score today, test set", rd(TS_RANGE, "TR.ARMIntraSectorScore"), "cited", "S38,S26", kind="static")
add(G, S, "ARM intra-sector score monthly (expected to fail)", hist("AAPL.O", "TR.ARMIntraSectorScore", "2000-01-01"), "cited", "S38")
add(G, S, "Value-momentum country rank today and FQ history", rd("AAPL.O", "TR.ValMoCountryRank.Date;TR.ValMoCountryRank", "SDate=0 EDate=-10 Frq=FQ CH=Fd RH=IN"), "cited", "S39")
add(G, S, "Price momentum country rank monthly (TR.PriceMoCountryRank guess)", hist("AAPL.O", "TR.PriceMoCountryRank", "2000-01-01"), "guess")
add(G, S, "ARM country rank monthly (TR.ARMCountryRank guess)", hist("AAPL.O", "TR.ARMCountryRank", "2000-01-01"), "guess")
add(G, S, "Short interest model country rank (TR.SIModelCountryRank guess)", rd(TS_RANGE, "TR.SIModelCountryRank"), "guess", "S26", kind="static")

# ------------------------------------------------------------------ 9 limits (wide grids last on the sheet)
G, S = "9 Limits", "Limits"
add(G, S, "S&P 500 members x 1 field (market cap): about 500 rows", rd("0#.SPX", "TR.CompanyMarketCap"), "cited", "S1,S2", kind="list")
add(G, S, "S&P 500 members x 6 fields at once", rd("0#.SPX", "TR.CommonName;TR.CUSIP;TR.ISIN;TR.CompanyMarketCap;TR.PriceClose;TR.ExchangeCountry"), "cited", "S1,S2,S10,S12,S40", kind="list")
add(G, S, "SCREEN active US primary x market cap: several thousand rows",
    rd('SCREEN(U(IN(Equity(active,public,primary))),IN(TR.ExchangeCountryCode,""US""),CURN=USD)', "TR.CompanyMarketCap", "curn=USD RH=In CH=Fd"), "cited", "S1", kind="list")
add(G, S, "1 stock, 46 years monthly (IBM close from 1980)", hist("IBM.N", "TR.PriceClose"), "cited", "S40")
add(G, S, "1 stock, 40 years daily (IBM close from 1985, about 10,500 rows)", hist("IBM.N", "TR.PriceClose", "1985-01-01", frq="D"), "cited", "S40")
add(G, S, "AAPL all holders today (thousands of rows)", rd("AAPL.O", "TR.InvestorFullName;TR.SharesHeld"), "cited", "S30", kind="list")
add(G, S, "Datastream S&P 500 list x MV monthly 2010-2026 (wide grid, about 500 columns)", ds("LS&PCOMP", "MV", "2009-12-31"), "cited", "S3,S6", w=8)

# ------------------------------------------------------------------ build
FIELDS_RE = re.compile(r'"([^"]*)"')


def ncols(f):
    """rough number of output columns, used to size the block so answers do not run into the next block"""
    args = FIELDS_RE.findall(f.replace('""', ''))
    if f.startswith("=DSGRID"):
        codes = args[0].count(",") + 1
        dts = args[1].count(",") + 1 if args[1] else 1
        return 1 + (dts if "Latest Value" in f else codes * dts)
    if f.startswith("=RHistory"):
        return 3
    fields = args[1] if not f.split("(", 1)[1].startswith("TestSet!") else args[0]
    n = fields.count(";") + fields.count(",") + 1
    if "RH=calcdate" in f or "TR.FundRolling" in f:
        n += 1
    return 2 + n


def literals(f):
    out, i = [], 0
    while i < len(f):
        if f[i] == '"':
            j, s = i + 1, ""
            while j < len(f):
                if f[j] == '"' and j + 1 < len(f) and f[j + 1] == '"':
                    s += '"'
                    j += 2
                elif f[j] == '"':
                    break
                else:
                    s += f[j]
                    j += 1
            out.append(s)
            i = j + 1
        else:
            i += 1
    return out


def main():
    wb = Workbook()
    ck = wb.active
    ck.title = "Check"
    ix = wb.create_sheet("Index")
    so = wb.create_sheet("Sources")
    ts = wb.create_sheet("TestSet")
    B = Font(bold=True)
    sheets, pos, rows = {}, {}, []
    for i, p in enumerate(P, 1):
        f = p["f"]
        assert f.startswith("=") and len(f) <= 8192, (i, len(f))
        for lit in literals(f):
            assert len(lit) <= 255, (i, len(lit), lit[:60])
        assert f.count("(") == f.count(")"), (i, f)
        sh = p["sheet"]
        if sh not in sheets:
            sheets[sh], pos[sh] = wb.create_sheet(sh), 1
        ws, c = sheets[sh], pos[sh]
        w = p["w"] or max(6, ncols(f) + 2)
        pos[sh] += w
        pid = "E-%03d" % i
        ws.cell(2, c, pid).font = B
        ws.cell(3, c, p["what"])
        ws.cell(4, c, "formula: " + f[1:])
        ws.cell(ROW0, c, f)
        rn = ROWN.get(sh, 15000)
        rows.append(dict(p, pid=pid, cell="'%s'!%s%d" % (sh, L(c), ROW0),
                         rng="'%s'!%s%d:%s%d" % (sh, L(c), ROW0, L(c + w - 2), rn), col=L(c), width=w))
    # Check sheet (live status, as in the macro probes)
    ck["A1"] = "LSEG Workspace equity probe v1 (stocks)"
    ck["A1"].font = Font(bold=True, size=14)
    ck["A2"] = ("1. Open in Excel with Workspace signed in (Workspace and Datastream tabs visible).   2. Wait until no cell on any sheet says "
                "Retrieving and the number in B4 has not changed for two minutes.   3. Press Ctrl+S (keep the file name). Errors in some "
                "blocks are expected: many names are guesses and an error is the answer.")
    r1, rn = 8, 7 + len(rows)
    ck["A4"] = "blocks with data"
    ck["A4"].font = B
    ck["B4"] = '=COUNTIF(H%d:H%d,">0")&" of %d"' % (r1, rn, len(rows))
    ck["B4"].font = Font(bold=True, size=13)
    ck["A5"] = "blocks showing an Excel error (add-in not loaded)"
    ck["B5"] = '=COUNTIF(G%d:G%d,"Excel error*")' % (r1, rn)
    for j, h in enumerate(("id", "group", "sheet", "what it tests", "name cited or guess", "sources", "status", "numbers found"), 1):
        ck.cell(7, j, h).font = B
    for k, r in enumerate(rows):
        rr = r1 + k
        for j, v in enumerate((r["pid"], r["group"], r["sheet"], r["what"], r["cite"], r["src"]), 1):
            ck.cell(rr, j, v)
        ck.cell(rr, 7, '=IF(ISERROR(%s),"Excel error (add-in not loaded?)",IF(H%d>0,"data","text: "&LEFT(%s&"",70)))' % (r["cell"], rr, r["cell"]))
        ck.cell(rr, 8, '=SUMPRODUCT(--ISNUMBER(%s))' % r["rng"])
    for col, wd in zip("ABCDEFGH", (8, 14, 11, 70, 12, 16, 50, 14)):
        ck.column_dimensions[col].width = wd
    # Index sheet (static; the reader uses it for groups, cited/guess, pairs, list kind)
    hdr = ("id", "group", "sheet", "column", "block width", "what it tests", "name cited or guess", "sources", "kind", "pair", "formula")
    for j, h in enumerate(hdr, 1):
        ix.cell(1, j, h).font = B
    for k, r in enumerate(rows, 2):
        for j, v in enumerate((r["pid"], r["group"], r["sheet"], r["col"], str(r["width"]), r["what"], r["cite"], r["src"], r["kind"], r["pair"], r["f"][1:]), 1):
            ix.cell(k, j, v)
    for col, wd in zip("ABCDEFGHIJK", (8, 14, 11, 7, 7, 70, 12, 18, 8, 12, 90)):
        ix.column_dimensions[col].width = wd
    # Sources
    for j, h in enumerate(("id", "url or file", "what it shows (read 2026-11-17)"), 1):
        so.cell(1, j, h).font = B
    for k, (sid, url, note) in enumerate(SOURCES, 2):
        so.cell(k, 1, sid)
        so.cell(k, 2, url)
        so.cell(k, 3, ("formula text: " + note[1:]) if note.startswith("=") else note)   # never a live formula
    so.cell(len(SOURCES) + 3, 1, "'cited' = the field or function name (or the parameter form) appears in the source; it does NOT mean it works on this licence. "
                                  "'guess' = not found in a source; the probe tells.")
    so.column_dimensions["B"].width = 80
    so.column_dimensions["C"].width = 120
    # TestSet
    ts["A1"] = "Test companies (formulas on the data sheets refer to B4:B15). Dead companies are given by ISIN."
    for j, h in enumerate(("company", "Workspace instrument", "ISIN", "delisted RIC (guess)", "kind"), 1):
        ts.cell(3, j, h).font = B
    for k, t in enumerate(TEST, 4):
        for j, v in enumerate(t, 1):
            ts.cell(k, j, v)
    for col, wd in zip("ABCDE", (48, 20, 16, 18, 10)):
        ts.column_dimensions[col].width = wd
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, NAME)
    wb.save(path)
    by_g = {}
    for r in rows:
        by_g.setdefault(r["group"], [0, 0])
        by_g[r["group"]][0 if r["cite"] == "cited" else 1] += 1
    print(path, "| formulas", len(rows), "| cited", sum(v[0] for v in by_g.values()), "| guess", sum(v[1] for v in by_g.values()))
    for g, (c, q) in by_g.items():
        print("  %-14s %3d formulas (cited %d, guess %d)" % (g, c + q, c, q))
    return path


if __name__ == "__main__":
    main()
