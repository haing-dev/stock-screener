"""LSEG company data files (2026-11-21; plan v0.4 step 3, stage B), for the 5,065 selected companies (one primary line
each; companies_v1.csv, PC only). Field names from docs/research/equity/field_dictionary_raw_v1.0.csv (confirmed on
this PC). Four kinds of workbook:
  Q<n>  quarterly accounts AS FIRST REPORTED (ReportingState=Orig), about 80 quarters back from the latest, with period
        end and original announcement date; 7 field groups (Excel caps a text argument at 255 characters)
  A1    annual accounts as first reported, 27 fiscal years back (for 10-year measures)
  E<n>  monthly consensus 2009-12..2026-10 (EPS FY1 / FY2 / next 12 months, revenue FY1, number of estimates, long-term
        growth, price target) and quarterly actual EPS with report date
  S1    sector (GICS names and codes, today) and monthly short interest from 2010
usage: python3 docs/data_requests/build_lseg_company_data.py COMPANIES.csv OUT_DIR"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_lseg_equity_probe as v1  # noqa: E402

COMP, OUT = sys.argv[1], sys.argv[2]
rows = list(csv.DictReader(open(COMP)))
RAW = {r["id"]: r["lseg_field"] for r in csv.DictReader(open(os.path.join(HERE, "..", "research", "equity", "field_dictionary_raw_v1.0.csv"))) if r["lseg_field"]}
Q_IDS = ["R%02d" % i for i in list(range(1, 23)) + list(range(24, 51))]          # all but goodwill (open), employees, EV
A_IDS = ["R01", "R07", "R08", "R09", "R11", "R12", "R13", "R14", "R15", "R16", "R18", "R25", "R30", "R33", "R41", "R42", "R44", "R51", "R52"]
PEND = "TR.F.TotRevenue.periodenddate"


def groups(ids, first_extra=""):
    """pack field names into ';'-joined strings of at most 250 characters, each starting with the period end"""
    out, cur = [], [PEND] + ([first_extra] if first_extra else [])
    for i in ids:
        f = RAW[i]
        if len(";".join(cur + [f])) > 250:
            out.append(";".join(cur)); cur = [PEND]
        cur.append(f)
    out.append(";".join(cur))
    return out


QG = groups(Q_IDS, "TR.F.OriginalAnnouncementDate")
AG = groups(A_IDS, "TR.F.OriginalAnnouncementDate")
QP = "Period=FQ0 Frq=FQ SDate=0 EDate=-79 ReportingState=Orig CH=Fd RH=IN"
AP = "Period=FY0 Frq=FY SDate=0 EDate=-26 ReportingState=Orig CH=Fd RH=IN"
EF = "TR.EPSMean(Period=FY1).date;TR.EPSMean(Period=FY1);TR.EPSMean(Period=FY2);TR.EPSMean(Period=NTM);TR.RevenueMean(Period=FY1);TR.EPSNumberofEstimates(Period=FY1);TR.LTGMean;TR.PriceTargetMean"
EP = "SDate=2009-12-31 EDate=2026-10-31 Frq=M CH=Fd RH=IN"
AF = "TR.EPSActValue.date;TR.EPSActValue;TR.EPSActValue.periodenddate"
AQ = "SDate=0 EDate=-70 Frq=FQ Period=FQ0 CH=Fd RH=IN"
GF = "TR.GICSSector;TR.GICSIndustryGroup;TR.GICSIndustry;TR.GICSSubIndustry;TR.GICSSubIndustryCode;TR.CommonName;TR.ExchangeName"
SF = "TR.ShortInterest.date;TR.ShortInterest"
SP = "SDate=2010-01-01 EDate=2026-10-31 Frq=M CH=Fd RH=IN"
for s in QG + AG + [EF, EP, AF, AQ, GF, SF, SP, QP, AP]:
    assert len(s) <= 255, s
v1.SOURCES = [s for s in v1.SOURCES if s[0] != "S46"] + [("S46", "repo: docs/research/equity/LSEG_equity_probe2_2026-11-20.md, LSEG_universe_v1_2026-11-20.md",
                                                       "field names confirmed on this PC (accounts first reported, estimates, actuals, GICS, short interest Frq=M)")]


def book(name, title, chunks, specs, rown):
    """chunks: list of (lo, hi) rows of the company list; specs: list of (sheet prefix, what, fields, params, kind)"""
    v1.P.clear()
    v1.END, v1.OUT, v1.NAME, v1.TITLE, v1.READ_DATE = "2026-11-21", OUT, name, title, "2026-11-21"
    lo0, hi0 = chunks[0][0], chunks[-1][1]
    part = rows[lo0:hi0]
    v1.TEST = [(r["COMPANY"], r["ISIN"], r["LINE_NAME"], r["TIME"], "") for r in part]
    sheets = {}
    for j, (lo, hi) in enumerate(chunks):
        rng = "TestSet!$B$%d:$B$%d" % (4 + lo - lo0, 3 + hi - lo0)
        for g, (pref, what, f, prm, kind) in enumerate(specs):
            sh = "%s%d" % (pref, j + 1)
            sheets[sh] = rown
            v1.P.append(dict(group=pref, sheet=sh, what="companies %d-%d: %s" % (lo + 1, hi, what), f=v1.rd(rng, f, prm),
                             cite="cited", src="S46", pair="", kind=kind, w=None))
    v1.ROWN = sheets
    v1.main()


def cut(n, size, start=0, stop=None):
    stop = len(rows) if stop is None else stop
    return [(i, min(i + size, stop)) for i in range(start, stop, size)]


N = len(rows)
# Q: 6 workbooks of about 850 companies, chunks of 425
for k, lo in enumerate(range(0, N, 850), 1):
    ch = cut(N, 425, lo, min(lo + 850, N))
    specs = [("G%d_" % (g + 1), "quarterly first-reported accounts, field group %d of %d" % (g + 1, len(QG)), f, QP, "series") for g, f in enumerate(QG)]
    book("LSEG_accounts_Q%d_v1.xlsx" % k, "LSEG quarterly accounts part %d (first reported; companies %d-%d)" % (k, lo + 1, min(lo + 850, N)), ch, specs, 36000)
# A1
specs = [("A%d_" % (g + 1), "annual first-reported accounts, field group %d of %d" % (g + 1, len(AG)), f, AP, "series") for g, f in enumerate(AG)]
book("LSEG_accounts_A1_v1.xlsx", "LSEG annual accounts (first reported, 27 fiscal years)", cut(N, 1000), specs, 28000)
# E: 3 workbooks; monthly consensus in chunks of 250, actuals in chunks of the workbook
for k, lo in enumerate(range(0, N, 1700), 1):
    hi = min(lo + 1700, N)
    ch = cut(N, 250, lo, hi)
    v1.P.clear()
    specs = [("E", "monthly consensus (EPS FY1 / FY2 / 12 months, revenue FY1, estimates, growth, target)", EF, EP, "series")]
    book("LSEG_estimates_E%d_v1.xlsx" % k, "LSEG estimates part %d (companies %d-%d)" % (k, lo + 1, hi), ch, specs, 52000)
# actual EPS goes into the S workbook to keep E files lighter
v1.P.clear()
specs = [("S", "monthly short interest from 2010", SF, SP, "series")]
book("LSEG_short_S1_v1.xlsx", "LSEG short interest (monthly from 2010)", cut(N, 250), specs, 52000)
specs = [("G", "GICS sector, industry group, industry, sub-industry (today), name, exchange", GF, "", "static"),
         ("X", "quarterly actual EPS with report date", AF, AQ, "series")]
book("LSEG_sector_actuals_S2_v1.xlsx", "LSEG sector and actual EPS", cut(N, 1000), specs, 72000)
print("Q groups:", len(QG), [len(g) for g in QG]); print("A groups:", len(AG))
