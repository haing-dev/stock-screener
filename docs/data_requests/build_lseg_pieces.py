"""LSEG stage-B data in SMALL PIECES (v4, 2026-11-22). The v1-v3 files stalled: the user's LSEG allowance seems to run
out after a few million values a day. Each piece here asks for about 0.4-0.7 million values (estimate printed in the
folder's README), so a few pieces fit in a day and every saved piece is usable on its own.

Two priority groups:
  P  needed for the reference book (field dictionary v1.0 part 1): GICS today, close as traded (file 12 of v3), the
     19 quarterly items of the seven book measures (companies 1-850 and 1701-5065; 851-1700 are in Q2_v1), FY1
     consensus EPS by month.
  B  later, for the pods: the other quarterly items, annual accounts, the other consensus fields, short interest,
     actual EPS.
usage: python3 docs/data_requests/build_lseg_pieces.py COMPANIES.csv SELECTED_LINES.csv OUT_DIR"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_lseg_equity_probe as v1  # noqa: E402

COMP, LINES, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
comp = list(csv.DictReader(open(COMP)))
lines = list(csv.DictReader(open(LINES)))
RAW = {r["id"]: r["lseg_field"] for r in csv.DictReader(open(os.path.join(HERE, "..", "research", "equity", "field_dictionary_raw_v1.0.csv"))) if r["lseg_field"]}
PEND = "TR.F.TotRevenue.periodenddate"
CORE = ["R01", "R02", "R03", "R08", "R13", "R41", "R25", "R33", "R18", "R28", "R29", "R30", "R36", "R35", "R21", "R27", "R39"]
REST = [i for i in ["R%02d" % k for k in list(range(1, 23)) + list(range(24, 51))] if i not in CORE and i in RAW]
A_IDS = ["R01", "R07", "R08", "R09", "R11", "R12", "R13", "R14", "R15", "R16", "R18", "R25", "R30", "R33", "R41", "R42", "R44", "R51", "R52"]
QP = "Period=FQ0 Frq=FQ SDate=0 EDate=-79 ReportingState=Orig CH=Fd RH=IN"
AP = "Period=FY0 Frq=FY SDate=0 EDate=-26 ReportingState=Orig CH=Fd RH=IN"
EP = "SDate=2009-12-31 EDate=2026-10-31 Frq=M CH=Fd RH=IN"
F1 = "TR.EPSMean(Period=FY1).date;TR.EPSMean(Period=FY1)"
EREST = "TR.EPSMean(Period=FY2).date;TR.EPSMean(Period=FY2);TR.EPSMean(Period=NTM);TR.RevenueMean(Period=FY1);TR.EPSNumberofEstimates(Period=FY1);TR.LTGMean;TR.PriceTargetMean"
AF = "TR.EPSActValue.date;TR.EPSActValue;TR.EPSActValue.periodenddate"
AQ = "SDate=0 EDate=-70 Frq=FQ Period=FQ0 CH=Fd RH=IN"
GF = "TR.GICSSector;TR.GICSIndustryGroup;TR.GICSIndustry;TR.GICSSubIndustry;TR.GICSSubIndustryCode;TR.CommonName;TR.ExchangeName"
SF = "TR.ShortInterest.date;TR.ShortInterest"
SP = "SDate=2010-01-01 EDate=2026-10-31 Frq=M CH=Fd RH=IN"
UF = "TR.PriceClose.date;TR.PriceClose"
UP = "SDate=2009-12-31 EDate=2026-10-31 Frq=M Adjusted=0 curn=USD CH=Fd RH=IN"


def groups(ids, first_extra=""):
    out, cur = [], [PEND] + ([first_extra] if first_extra else [])
    for i in ids:
        f = RAW[i]
        if len(";".join(cur + [f])) > 250:
            out.append(";".join(cur))
            cur = [PEND]
        cur.append(f)
    out.append(";".join(cur))
    return out


QC = groups(CORE, "TR.F.OriginalAnnouncementDate")
QR = groups(REST)
AG = groups(A_IDS, "TR.F.OriginalAnnouncementDate")
for s in QC + QR + AG + [QP, AP, EP, F1, EREST, AF, AQ, GF, SF, SP, UF, UP]:
    assert len(s) <= 255, s
v1.SOURCES = [s for s in v1.SOURCES if s[0] != "S46"] + [("S46", "repo: docs/research/equity/LSEG_equity_probe2_2026-11-20.md, LSEG_measures_check_2026-11-22.md",
                                                       "field names confirmed on this PC; Q2_v1 (425-company blocks) loaded on 2026-11-21")]
INDEX = []


def nfields(f):
    return f.count(";") + 1


def book(name, title, rows, testrow, chunks, specs, rown, per_inst):
    """rows: the full id list; chunks: (lo, hi) slices of rows; specs: (sheet prefix, what, fields, params);
    per_inst: values per instrument (estimate, for the README)"""
    v1.P.clear()
    v1.END, v1.OUT, v1.NAME, v1.TITLE, v1.READ_DATE = "2026-11-22", OUT, name, title, "2026-11-22"
    lo0, hi0 = chunks[0][0], chunks[-1][1]
    v1.TEST = [testrow(r) for r in rows[lo0:hi0]]
    sheets = {}
    for j, (lo, hi) in enumerate(chunks):
        rng = "TestSet!$B$%d:$B$%d" % (4 + lo - lo0, 3 + hi - lo0)
        for pref, what, f, prm in specs:
            sh = "%s%d" % (pref, j + 1)
            sheets[sh] = rown
            v1.P.append(dict(group=pref, sheet=sh, what="rows %d-%d: %s" % (lo + 1, hi, what), f=v1.rd(rng, f, prm),
                             cite="cited", src="S46", pair="", kind="series", w=None))
    v1.ROWN = sheets
    v1.main()
    INDEX.append((name, title, len(v1.P), (hi0 - lo0) * per_inst))


def cut(lo, hi, size):
    return [(i, min(i + size, hi)) for i in range(lo, hi, size)]


def comp_row(r):
    return (r["COMPANY"], r["ISIN"], r["LINE_NAME"], r["TIME"], "")


def line_row(r):
    return (r["NAME"], r["ISIN"], r["DSCD"], r["TIME"], r["EXMNEM"])


N, NL = len(comp), len(lines)
seq = {"P": 0, "B": 0}


def nm(kind, stem):
    seq[kind] += 1
    return "%s%02d_LSEG_%s_v4.xlsx" % (kind, seq[kind], stem)


# ---------------------------------------------------------------- P: reference book
book(nm("P", "sector_GICS_all"), "LSEG GICS today, name, exchange (all companies)", comp, comp_row, cut(0, N, 1000),
     [("G", "GICS sector, group, industry, sub-industry, name, exchange (today)", GF, "")], 1100, 7)
for lo in range(0, NL, 1400):
    hi = min(lo + 1400, NL)
    book(nm("P", "unadjusted_close_l%04d-%04d" % (lo + 1, hi)), "LSEG month-end close as traded (Adjusted=0), lines %d-%d" % (lo + 1, hi),
         lines, line_row, cut(lo, hi, 350), [("U", "month-end close as traded", UF, UP)], 72000, 2 * 203)
qc_specs = [("C%d_" % (g + 1), "quarterly first-reported accounts, book items, group %d of %d" % (g + 1, len(QC)), f, QP) for g, f in enumerate(QC)]
for a, b in ((0, 850), (1700, N)):
    for lo in range(a, b, 425):
        hi = min(lo + 425, b)
        book(nm("P", "accounts_Qcore_c%04d-%04d" % (lo + 1, hi)), "LSEG quarterly accounts, book items (first reported), companies %d-%d" % (lo + 1, hi),
             comp, comp_row, cut(lo, hi, 213), qc_specs, 18000, 80 * (sum(nfields(f) for f in QC) - len(QC) + 1))
for lo in range(0, N, 1700):
    hi = min(lo + 1700, N)
    book(nm("P", "estimates_EFY1_c%04d-%04d" % (lo + 1, hi)), "LSEG FY1 consensus EPS by month, companies %d-%d" % (lo + 1, hi),
         comp, comp_row, cut(lo, hi, 340), [("F", "FY1 EPS mean by month", F1, EP)], 70000, 2 * 203)
# ---------------------------------------------------------------- B: later (pods)
qr_specs = [("R%d_" % (g + 1), "quarterly first-reported accounts, other items, group %d of %d" % (g + 1, len(QR)), f, QP) for g, f in enumerate(QR)]
for a, b in ((0, 850), (1700, N)):
    for lo in range(a, b, 250):
        hi = min(lo + 250, b)
        book(nm("B", "accounts_Qrest_c%04d-%04d" % (lo + 1, hi)), "LSEG quarterly accounts, other items (first reported), companies %d-%d" % (lo + 1, hi),
             comp, comp_row, cut(lo, hi, 125), qr_specs, 11000, 80 * (sum(nfields(f) for f in QR) - len(QR) + 1))
a_specs = [("A%d_" % (g + 1), "annual first-reported accounts, group %d of %d" % (g + 1, len(AG)), f, AP) for g, f in enumerate(AG)]
for lo in range(0, N, 1300):
    hi = min(lo + 1300, N)
    book(nm("B", "accounts_A_c%04d-%04d" % (lo + 1, hi)), "LSEG annual accounts (first reported, 27 years), companies %d-%d" % (lo + 1, hi),
         comp, comp_row, cut(lo, hi, 325), a_specs, 9500, 27 * (sum(nfields(f) for f in AG) - len(AG) + 1))
for lo in range(0, N, 500):
    hi = min(lo + 500, N)
    book(nm("B", "estimates_Erest_c%04d-%04d" % (lo + 1, hi)), "LSEG other consensus fields by month, companies %d-%d" % (lo + 1, hi),
         comp, comp_row, cut(lo, hi, 125), [("E", "FY2, 12-month EPS, revenue FY1, number of estimates, growth, target", EREST, EP)], 27000, 7 * 203)
for lo in range(0, N, 1700):
    hi = min(lo + 1700, N)
    book(nm("B", "short_S1_c%04d-%04d" % (lo + 1, hi)), "LSEG short interest by month from 2010, companies %d-%d" % (lo + 1, hi),
         comp, comp_row, cut(lo, hi, 340), [("S", "monthly short interest", SF, SP)], 70000, 2 * 202)
for lo in range(0, N, 2600):
    hi = min(lo + 2600, N)
    book(nm("B", "actual_EPS_c%04d-%04d" % (lo + 1, hi)), "LSEG quarterly actual EPS with report date, companies %d-%d" % (lo + 1, hi),
         comp, comp_row, cut(lo, hi, 520), [("X", "quarterly actual EPS with report date", AF, AQ)], 37000, 3 * 70)

with open(os.path.join(OUT, "README_order.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["file", "what", "formulas", "values_estimate"])
    for r in INDEX:
        w.writerow(r)
print("pieces:", len(INDEX), "P:", seq["P"], "B:", seq["B"])
for r in INDEX:
    print("%-55s %3d formulas  ~%5.2f M values" % (r[0], r[2], r[3] / 1e6))
