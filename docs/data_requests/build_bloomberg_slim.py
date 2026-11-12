"""Bloomberg visit set, slim version (2026-11-12). LSEG Workspace on the user's PC now covers most of the old re-pull
set R1-R7 (see tools/bbgq/results/lseg_pull_2026-11-12_read.txt), so the campus visit only needs what LSEG cannot
supply, plus a small cross-check sample. Same block layout, same sheet names ('<file digit> <sheet>') and the same
Check sheet as the old set, so the reader (bbgdata-1.2.0) merges these files unchanged.
  R8   only on Bloomberg, rates: ended short-rate futures (Eurodollar, short sterling, BA, Euroyen, Euroswiss), extra
       bond futures, breakevens, CTA benchmarks, swaps
  R9   only on Bloomberg, other: credit, commodity fundamentals, 8 equity indexes, non-deliverable FX forwards
  R10  cross-check sample: about 45 series that LSEG also has, to compare the two sources
  R11  LME and other commodity curves that were still loading (lowest priority)
usage: python3 docs/data_requests/build_bloomberg_slim.py [out dir]"""
import collections, csv, os, re, sys
import openpyxl
sys.argv = sys.argv[:1] + ([sys.argv[1]] if len(sys.argv) > 1 else [])
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_bloomberg_repull as R   # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "bloomberg_visit_2026-11-13")
sel = R.select()


def root(tk):
    return re.sub(r"\s*\d+$", "", tk.rsplit(" ", 1)[0]).strip()


def pick(digit, sheet, keep):
    return [b for b in sel.get((digit, sheet), []) if keep(b[1])]


ENDED = {"ED", "L", "BA", "YE", "ES"}
XBOND = {"UXY", "KE", "KAA", "BTS", "FBON", "FB", "CV", "CF", "JBA"}
NDF = ("KWN", "NTN", "IRN", "IHN", "PPN", "CCN", "BCN", "CHN", "CLN", "MRN", "RUB")
LSEG_COM = {"CL", "CO", "NG", "HO", "XB", "GC", "SI", "HG", "PL", "PA", "C", "W", "S", "SB", "KC", "CT", "LC", "CC", "JO", "LH", "FC",
            "KW", "SM", "BO", "QS"}                      # commodity roots LSEG delivered with curves
A = {("1", "RatesFutures"): pick("1", "RatesFutures", lambda t: root(t) in ENDED),
     ("3", "RatesFutExtra"): pick("3", "RatesFutExtra", lambda t: root(t) in ENDED | XBOND),
     ("1", "Breakevens"): pick("1", "Breakevens", lambda t: True),
     ("1", "Benchmarks"): pick("1", "Benchmarks", lambda t: True),
     ("3", "Swaps"): pick("3", "Swaps", lambda t: True)}
B = {("3", "Credit"): pick("3", "Credit", lambda t: True),
     ("5", "ComFundamentals"): pick("5", "ComFundamentals", lambda t: True),
     ("4", "EquityIndexes"): pick("4", "EquityIndexes", lambda t: True),
     ("5", "ComFront"): pick("5", "ComFront", lambda t: root(t) not in LSEG_COM),
     ("5", "ComCurve"): pick("5", "ComCurve", lambda t: root(t) not in LSEG_COM),
     ("1", "Curves"): pick("1", "Curves", lambda t: root(t) not in LSEG_COM),
     ("3", "FXForwards"): pick("3", "FXForwards", lambda t: t.startswith(NDF))}
XC = {("1", "Curves"): ["CL1 Comdty", "CL2 Comdty", "CO1 Comdty", "NG1 Comdty", "GC1 Comdty", "HG1 Comdty", "C 1 Comdty", "S 1 Comdty",
                        "SB1 Comdty", "LC1 Comdty"],
      ("1", "Returns"): ["SPGSCLP Index", "SPGSGCP Index", "SPGSICP Index", "SPGSCNP Index", "BCOMCL Index"],
      ("1", "BondFutures"): ["TY1 Comdty", "RX1 Comdty", "JB1 Comdty", "G 1 Comdty"],
      ("1", "Yields"): ["USGG2YR Index", "USGG10YR Index", "GDBR10 Index", "GJGB10 Index", "GUKG10 Index"],
      ("1", "SpotRates3m"): ["US0003M Index", "EUR003M Index"],
      ("1", "RatesFutures"): ["ER1 Comdty", "ER4 Comdty", "FF1 Comdty", "SFR1 Comdty"],
      ("1", "Surprise"): ["CESIUSD Index", "CESIEUR Index"],
      ("3", "FXSpot"): ["EURUSD Curncy", "USDJPY Curncy", "GBPUSD Curncy", "AUDUSD Curncy", "USDMXN Curncy", "USDKRW Curncy"],
      ("3", "FXForwards"): ["EUR3M Curncy", "JPY3M Curncy", "MXN3M Curncy"],
      ("3", "FXVol"): ["EURUSDV3M Curncy", "USDJPYV3M Curncy"],
      ("3", "YieldsExtra"): ["USGG3M Index", "GSPG10YR Index"],
      ("3", "FXBasis"): ["EUBSV1 Curncy", "JYBSV1 Curncy"]}
C = {k: pick(k[0], k[1], lambda t, v=v: t in v) for k, v in XC.items()}

B1 = {k: B[k] for k in [("3", "Credit"), ("5", "ComFundamentals"), ("4", "EquityIndexes"), ("3", "FXForwards")]}
B2 = {k: B[k] for k in [("5", "ComFront"), ("5", "ComCurve"), ("1", "Curves")]}
# one R number per file: the reader keeps only one workbook per number
PLAN = [("R8_bloomberg_only_rates.xlsx", "PRIORITY 1, only on Bloomberg: ended short-rate futures, extra bond futures, breakevens, benchmarks, swaps", A),
        ("R9_bloomberg_only_credit_fundamentals.xlsx", "PRIORITY 2, only on Bloomberg: credit, commodity fundamentals, equity indexes, non-deliverable forwards", B1),
        ("R10_crosscheck_sample.xlsx", "PRIORITY 3, cross-check sample: series LSEG also has, to compare the two sources", C),
        ("R11_other_commodity_curves.xlsx", "PRIORITY 4 (only if there is time): LME and other commodity curves that were still loading", B2)]
os.makedirs(OUT, exist_ok=True)
master = []
for k, (fname, title, part) in enumerate(PLAN, 1):
    R_sel = {key: v for key, v in part.items() if v}
    parts = [(d, s, 0, None) for (d, s) in R_sel]
    n, nexp, rows = R.build_file(OUT, k, fname, title, parts, R_sel)
    p = os.path.join(OUT, fname)
    wb = openpyxl.load_workbook(p)                       # fix the two title lines written for the old 7-file set
    ck = wb["Check"]
    ck.cell(1, 1).value = "%s (file %d of 4 for the Bloomberg visit): %s" % (fname.split("_")[0], k, title)
    ck.cell(2, 1).value = "Bloomberg visit of 13 Nov 2026, slim set. %d series. Monthly history from 1969. The old files R1-R7 are no longer needed." % n
    wb.save(p)
    print("%-34s %4d series | sheets: %s" % (fname, n, ", ".join("%s (%d)" % (s, c) for s, c in collections.Counter(r[0] for r in rows).items())))
    master += [(fname, r[0], r[1], r[2], r[5].isoformat() if r[5] else "") for r in rows]
with open(os.path.join(OUT, "visit_tickers.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(("file", "sheet", "label", "ticker", "should_start_by"))
    w.writerows(master)
print("total series", len(master), "(old set: 1,283)")
