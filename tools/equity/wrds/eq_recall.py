"""eq_recall (runs on WRDS Cloud): recall test of an investor recipe on the investor's own conviction purchases
(gate G8; V04_REGISTRATION.md addendum A10 item 9 and A13 item 13; spec docs/research/equity/pilot/RECALL_SPEC_v1.md;
recipe docs/research/equity/pilot/recipe/RECIPE_v1.md). Seal-exempt job 9 `recall` (tools/equity/seal_exempt.json).

pull(sql, save, load, out, budget=N)   stores rc_* data sets on WRDS (resumable; one table per step). eq_ref's ref_*
                                       data sets are reused where they are stored (else pulled under rc_* with the
                                       same query): msf, dv_<year>, link, fq, gics, ibes, names. New: rc_funda
                                       (Compustat annual), rc_fqx (extra quarterly items), rc_t10 (10-year constant-
                                       maturity Treasury from the WRDS FRB tables; the step stops with a clear message
                                       if no such table is found)
run(load, save, out)                   (1.1.0: every recipe of TARGETS in order, then one summary table)
                                       universe at each quarter-end 2009-12 .. 2025-09 (eq_ref's R3 universe), the
                                       recipe's measures and pass flags (decisive and full form), conviction purchases
                                       from eq_conv_panel, recall, base rate by sector x size-third cells, lift, the
                                       2,000-draw quarter bootstrap (seed 20261127), the two baselines, per-criterion
                                       rejection shares and the masked cross table. Prints counts, ratios and intervals
                                       only (no company, no identifier, no row). Stores the pass panel (1.1.0:
                                       rc_pass_<recipe>) and the summary (1.1.0: rc_recall_summary_v11) on WRDS.

No forward return is computed or read: monthly returns are read only up to the last evaluation quarter-end (2025-09)
and every measure at quarter-end t uses data up to t (12-month price and return windows end at t). Seal-exempt modules
may import no lib module, so the eq_ref engine parts needed here (universe, GICS history, quarterly accounts, book
score) are copied from eq_ref 1.1.0 with the changes noted at each copy.

Recipes: the criteria of a recipe live in ONE function (kantesaria_v1) that returns pass flags per criterion; the
decisive entry and the full-form versions are compositions of those flags (kantesaria_v1_entry, kantesaria_v1_full),
registered in RECIPES so later recipes are added beside it. 1.1.0: one such triple per recipe (see 1.1.0 below);
RECIPES also holds each recipe's eligible set ('house' = A8 2a exclusions out, as 1.0.3; 'all' = the recipe states
that the house exclusions do not apply: pilecki_v1, nygren_v1), labels, NOT IMPLEMENTED ids and coverage columns.
Percentiles of the new recipes: pct01 (0 = lowest, 1 = highest) inside the group the recipe names, over the recipe's
eligible set at t; a missing measure fails its criterion unless the recipe says otherwise (lilu_v1 AVOID: missing =
not excluded; stahl_v1 B4: no estimate = 0).

1.0.0 (2026-11-27): first version. 1.0.1 (same day, after an independent review, before run() was ever executed;
pull() unchanged): stop when the 10-year Treasury is missing at any evaluation quarter-end; the reference-book revision
measure takes the last CRSP split factor from the untruncated price file (as eq_ref); the AAPL direction check prints
only the direction; a single-version decisive result is flagged. 1.0.2 (after eq_recall_pull_v1, which stopped at the
Treasury step: the first table found, frb_all_old.rates_daily, is not readable by this account): every candidate FRB
table is tried in order, plus frb.rates_daily / rates_monthly, and the first readable one is used; run() unchanged.
1.0.3 (after eq_recall_pull_v1b: no FRB table on WRDS is readable by this account; A13 item 19): the step prints the
FRB tables it saw (names and their 10-year-like column names: metadata only) and, when no WRDS candidate is readable,
uses the same series from its public source: the Federal Reserve H.15 10-year constant-maturity yield as published by
FRED (DGS10), last daily value of each month 2008-06 .. 2025-12, embedded below (taken from branch macro-data
research/DGS10.csv, 2026-11-01 download). src = "public.fred.dgs10"; run() unchanged.
1.1.0 (2026-11-28; V04_REGISTRATION A13 item 21, registered before any 1.1.0 run): nine more recipes beside
kantesaria_v1, each a flag function + a decisive entry (+ a full form where the recipe states it clearly), evaluated
in order by run(): kantesaria_v1 (numbers identical to eq_recall_v1: same panel, same seed), kantesaria_v2 (the
registered revision round, RECIPE_v2.md), druckenmiller_v1, stahl_v1, hohn_v1, zlatev_v1, pilecki_v1, nygren_v1,
lilu_v1; sosin_v1 is written but not measured (13F filer 21801 is not in eq_conv_panel). New pulls (resumable, WRDS
subscription tables only): rc_fqx2 (comp.fundq cshfdq, ppentq, dvpsxq), rc_funda2 (comp.funda seq, mib, txt, pi),
rc_ibes2 (ibes.statsum_epsus FY1, FY2 and long-term growth with fpedats), rc_idx (tfn.s34 holdings of the three
largest index managers, by name in tfn.s34names). Bootstrap seed 20261127 for every investor.
NOT IMPLEMENTED rule: a decisive criterion whose data is not on WRDS, or that cannot be evaluated with prices up to t,
is left out; the decisive entry is evaluated without it and every printed line block of that investor carries the
label "decisive minus <ids>". Per investor: pilecki_v1 minus B4 (December sleeve: chosen at the November month-end,
after t). All other decisive criteria are implemented. Full forms: implemented for kantesaria_v1, kantesaria_v2,
stahl_v1, hohn_v1, zlatev_v1, pilecki_v1, nygren_v1, lilu_v1; NOT for druckenmiller_v1 (the recipe does not say how
its eleven grid lines combine).
1.1.1 (2026-11-28; A13 item 22, after the independent review of 1.1.0 and before any 1.1.x result): S1 price / FY2 EPS
(zlatev_v1 P1) and price / value (nygren_v1 P4, sosin_v1) on one share basis: the unadjusted I/B/E/S summary
(ibes.statsumu_epsus, new data set rc_ibes2u, fpi 1 and 2) against the CRSP price at t as traded; if the table is not
readable, the pull stores a marker and those criteria are labelled "provisional (split basis)". S2 reference-book
baseline scored on the recipe's own set for recipes with the house exclusions off; share of counted purchases without a
reference score printed; above 50% c5 is "not informative" and the gate rests on the other four conditions. S3
pilecki_v1 small groups ranked among all eligible financials at t. S4 the Sosin line prints no filer number. N1 lilu_v1
on his own set (all industries), the house-set result as a second line. N5 index managers per quarter-end printed.
1.1.2 (2026-11-28; A13 item 23, after eq_recall_v2, whose report the runner cut at 60,000 characters inside the lilu_v1
block, so lilu_v1 and the summary table were not seen): output only. run_part(load, save, out, part=k) runs the same
computation for the recipes of PARTS[k] (1 = kantesaria_v1, kantesaria_v2, druckenmiller_v1, stahl_v1; 2 = the rest),
so each job step stays under the runner's per-step limit; the summary of a part is stored as rc_recall_summary_v11_p<k>.
run() unchanged (all recipes, one step). No measure, recipe, statistic or seed changed: numbers must equal eq_recall_v2.
"""
import json
import time

import numpy as np
import pandas as pd

# >>> FROZEN INPUT
CFG = json.loads("{\"y0\": 2007, \"y1\": 2025, \"form0\": 200901, \"form1\": 202511, \"ret0\": 201001, \"ret1\": 202512, \"top_n\": 1500, \"min_price\": 5.0, \"min_dv\": 2000000.0, \"top_frac\": 0.1, \"keep_frac\": 0.2, \"hold\": 12, \"cost_big\": 0.001, \"cost_small\": 0.0025, \"big_n\": 500, \"basket_cost\": 0.001, \"max_missing\": 3, \"stale_days\": 270, \"q_lag_days\": 45, \"ibes_tol_days\": 35, \"cap\": 0.025}")
INVESTORS = json.loads("[{\"name\": \"Joel Greenblatt\", \"group\": \"roster\", \"mgrnos\": [\"10969\", \"12775\"], \"quant\": true}, {\"name\": \"Terry Smith\", \"group\": \"roster\", \"mgrnos\": [\"13408\"]}, {\"name\": \"Dev Kantesaria\", \"group\": \"roster\", \"mgrnos\": [\"14460\"]}, {\"name\": \"Chris Hohn\", \"group\": \"roster\", \"mgrnos\": [\"11194\"]}, {\"name\": \"Glenn Greenberg\", \"group\": \"roster\", \"mgrnos\": [\"16080\"]}, {\"name\": \"Val Zlatev\", \"group\": \"roster\", \"mgrnos\": [\"7142\"]}, {\"name\": \"Derek Pilecki\", \"group\": \"roster\", \"mgrnos\": [\"8799\"]}, {\"name\": \"Bill Nygren and Alex Fitch\", \"group\": \"roster\", \"mgrnos\": [\"43485\"]}, {\"name\": \"Murray Stahl\", \"group\": \"roster\", \"mgrnos\": [\"44850\", \"49373\"]}, {\"name\": \"Pat Dorsey\", \"group\": \"roster\", \"mgrnos\": [\"14201\"]}, {\"name\": \"Chris Davis\", \"group\": \"roster\", \"mgrnos\": [\"78320\"]}, {\"name\": \"Joseph Shaposhnik\", \"group\": \"roster\", \"mgrnos\": []}, {\"name\": \"Alex Sacerdote\", \"group\": \"roster\", \"mgrnos\": [\"11405\"]}, {\"name\": \"David Einhorn\", \"group\": \"roster\", \"mgrnos\": [\"42315\"]}, {\"name\": \"Stan Druckenmiller\", \"group\": \"roster\", \"mgrnos\": [\"13021\", \"23704\"]}, {\"name\": \"Todd Kantor\", \"group\": \"roster\", \"mgrnos\": [\"13431\"]}, {\"name\": \"Bob Robotti\", \"group\": \"roster\", \"mgrnos\": [\"10247\"]}, {\"name\": \"Fred Martin\", \"group\": \"roster\", \"mgrnos\": [\"23050\"]}, {\"name\": \"Brad Gerstner\", \"group\": \"roster\", \"mgrnos\": [\"13112\"]}, {\"name\": \"Chris Bloomstran\", \"group\": \"roster\", \"mgrnos\": [\"11757\"]}, {\"name\": \"Li Lu\", \"group\": \"roster\", \"mgrnos\": [\"14546\"]}, {\"name\": \"Warren Buffett\", \"group\": \"control\", \"mgrnos\": [\"8350\"]}, {\"name\": \"Henry Ellenbogen\", \"group\": \"control\", \"mgrnos\": [\"9442\"]}, {\"name\": \"Jim Chanos\", \"group\": \"control\", \"mgrnos\": [\"12867\"]}, {\"name\": \"John Lennon\", \"group\": \"control\", \"mgrnos\": [\"9090\"]}, {\"name\": \"Peter Keefe\", \"group\": \"control\", \"mgrnos\": [\"5300\"]}, {\"name\": \"Tobias Carlisle\", \"group\": \"control\", \"mgrnos\": []}, {\"name\": \"Arnold Van Den Berg\", \"group\": \"control\", \"mgrnos\": [\"15095\"]}, {\"name\": \"Eddy Elfenbein\", \"group\": \"control\", \"mgrnos\": []}]")
TARGETS = json.loads("[{\"name\": \"Dev Kantesaria\", \"mgrnos\": [\"14460\"], \"recipe\": \"kantesaria_v1\"}, {\"name\": \"Dev Kantesaria\", \"mgrnos\": [\"14460\"], \"recipe\": \"kantesaria_v2\"}, {\"name\": \"Stan Druckenmiller\", \"mgrnos\": [\"13021\", \"23704\"], \"recipe\": \"druckenmiller_v1\"}, {\"name\": \"Murray Stahl\", \"mgrnos\": [\"44850\", \"49373\"], \"recipe\": \"stahl_v1\"}, {\"name\": \"Chris Hohn\", \"mgrnos\": [\"11194\"], \"recipe\": \"hohn_v1\"}, {\"name\": \"Val Zlatev\", \"mgrnos\": [\"7142\"], \"recipe\": \"zlatev_v1\"}, {\"name\": \"Derek Pilecki\", \"mgrnos\": [\"8799\"], \"recipe\": \"pilecki_v1\"}, {\"name\": \"Bill Nygren and Alex Fitch\", \"mgrnos\": [\"43485\"], \"recipe\": \"nygren_v1\"}, {\"name\": \"Li Lu\", \"mgrnos\": [\"14546\"], \"recipe\": \"lilu_v1\"}, {\"name\": \"Cliff Sosin\", \"mgrnos\": [\"21801\"], \"recipe\": \"sosin_v1\"}]")
# <<< FROZEN INPUT

VERSION = "eq_recall-1.1.2"
COM = ("securitytype = 'EQTY' and securitysubtype = 'COM' and sharetype = 'NS' and primaryexch in ('N','A','Q')")
MEASURES = ["ey", "bp", "mom", "roe", "acc", "pio", "rev"]
GROUPS = {"value": ["ey", "bp"], "momentum": ["mom"], "quality": ["roe", "acc", "pio"], "expectations": ["rev"]}
HIGH_GOOD = {"ey": 1, "bp": 1, "mom": 1, "roe": 1, "acc": -1, "pio": 1, "rev": 1}

# registered constants of the recall test (RECALL_SPEC_v1; A10 item 9)
T0, T1 = 200912, 202509            # evaluation quarter-ends t (the quarter-end before each purchase quarter)
Q0, Q1 = 201003, 202512            # purchase quarters 2010-2025 (13F quarter-ends)
ANN_LAG_DAYS = 90                  # a fiscal year is known 90 days after its datadate (A13 item 13)
ANN_STALE_DAYS = 550               # latest known fiscal year older than this at t = annual accounts missing
FUNDA0, FQX0, DATA_END = "1996-01-01", "2004-01-01", "2025-09-30"
# 1.0.3: public fallback = FRED DGS10 (Federal Reserve H.15, same series as frb tcmnom_y10), last daily value per month
DGS10_ME = ("20080630:3.99,20080731:3.99,20080829:3.83,20080930:3.85,20081031:4.01,20081128:2.93,20081231:2.25,20090130:2.87,20090227:3.02,20090331:2.71,20090430:3.16,20090529:3.47,20090630:3.53,20090731:3.52,20090831:3.4,20090930:3.31,20091030:3.41,20091130:3.21,20091231:3.85,20100129:3.63,20100226:3.61,20100331:3.84,20100430:3.69,20100528:3.31,20100630:2.97,20100730:2.94,20100831:2.47,20100930:2.53,20101029:2.63,20101130:2.81,20101231:3.3,20110131:3.42,20110228:3.42,20110331:3.47,20110429:3.32,20110531:3.05,20110630:3.18,20110729:2.82,20110831:2.23,20110930:1.92,20111031:2.17,20111130:2.08,20111230:1.89,20120131:1.83,20120229:1.98,20120330:2.23,20120430:1.95,20120531:1.59,20120629:1.67,20120731:1.51,20120831:1.57,20120928:1.65,20121031:1.72,20121130:1.62,20121231:1.78,20130131:2.02,20130228:1.89,20130328:1.87,20130430:1.7,20130531:2.16,20130628:2.52,20130731:2.6,20130830:2.78,20130930:2.64,20131031:2.57,20131129:2.75,20131231:3.04,20140131:2.67,20140228:2.66,20140331:2.73,20140430:2.67,20140530:2.48,20140630:2.53,20140731:2.58,20140829:2.35,20140930:2.52,20141031:2.35,20141128:2.18,20141231:2.17,20150130:1.68,20150227:2,20150331:1.94,20150430:2.05,20150529:2.12,20150630:2.35,20150731:2.2,20150831:2.21,20150930:2.06,20151030:2.16,20151130:2.21,20151231:2.27,20160129:1.94,20160229:1.74,20160331:1.78,20160429:1.83,20160531:1.84,20160630:1.49,20160729:1.46,20160831:1.58,20160930:1.6,20161031:1.84,20161130:2.37,20161230:2.45,20170131:2.45,20170228:2.36,20170331:2.4,20170428:2.29,20170531:2.21,20170630:2.31,20170731:2.3,20170831:2.12,20170929:2.33,20171031:2.38,20171130:2.42,20171229:2.4,20180131:2.72,20180228:2.87,20180329:2.74,20180430:2.95,20180531:2.83,20180629:2.85,20180731:2.96,20180831:2.86,20180928:3.05,20181031:3.15,20181130:3.01,20181231:2.69,20190131:2.63,20190228:2.73,20190329:2.41,20190430:2.51,20190531:2.14,20190628:2,20190731:2.02,20190830:1.5,20190930:1.68,20191031:1.69,20191129:1.78,20191231:1.92,20200131:1.51,20200228:1.13,20200331:0.7,20200430:0.64,20200529:0.65,20200630:0.66,20200731:0.55,20200831:0.72,20200930:0.69,20201030:0.88,20201130:0.84,20201231:0.93,20210129:1.11,20210226:1.44,20210331:1.74,20210430:1.65,20210528:1.58,20210630:1.45,20210730:1.24,20210831:1.3,20210930:1.52,20211029:1.55,20211130:1.43,20211231:1.52,20220131:1.79,20220228:1.83,20220331:2.32,20220429:2.89,20220531:2.85,20220630:2.98,20220729:2.67,20220831:3.15,20220930:3.83,20221031:4.1,20221130:3.68,20221230:3.88,20230131:3.52,20230228:3.92,20230331:3.48,20230428:3.44,20230531:3.64,20230630:3.81,20230731:3.97,20230831:4.09,20230929:4.59,20231031:4.88,20231130:4.37,20231229:3.88,20240131:3.99,20240229:4.25,20240328:4.2,20240430:4.69,20240531:4.51,20240628:4.36,20240731:4.09,20240830:3.91,20240930:3.81,20241031:4.28,20241129:4.18,20241231:4.58,20250131:4.58,20250228:4.24,20250331:4.23,20250430:4.17,20250530:4.41,20250630:4.24,20250731:4.37,20250829:4.23,20250930:4.16,20251031:4.11,20251128:4.02,20251231:4.18")
T10_TOL_DAYS = 40                  # last Treasury value on or before t, at most this old
NBOOT, SEED, MIN_N = 2000, 20261127, 20
GATE = {"lift": 2.0, "lo": 1.25, "recall": 0.25}
REF_TOP = 0.8                      # reference-book screen: inside-sector book percentile >= 0.8 (top fifth)
LABELS = ["held-out failed", "recipe covers 7 of 22 buy rules (decisive)"]
FUNDA_COLS = ["revt", "ni", "epsfx", "epspx", "oiadp", "oibdp", "capx", "oancf", "stkco", "aqc", "at", "intan", "dltt",
              "dlc", "che", "csho", "cshfd", "ajex"]
FQX_COLS = ["capxy", "oibdpq", "intanq", "stkcoq", "stkcoy"]
REF_BASES = ["msf", "link", "fq", "gics", "ibes", "names"]
# 1.1.0: inputs of the other recipes (V04_REGISTRATION A13 item 21)
FQX2_COLS = ["cshfdq", "ppentq", "dvpsxq"]          # diluted shares (R15), net PPE (R22), dividends per share (R16)
FUNDA2_COLS = ["seq", "mib", "txt", "pi"]          # equity, minorities (R34 = seq + mib), income tax (R12), pre-tax (R11)
IBES0 = "%d-06-01" % CFG["y0"]
IDX_PATTERNS = ["VANGUARD GROUP", "BLACKROCK", "STATE STREET", "BARCLAYS GLOBAL INV"]  # O05: the three largest index
IDX0, IDX1 = "2009-06-30", "2025-06-30"            # managers (BGI = BlackRock's index arm before its 2009-12 purchase)
NEW_SETS = ["rc_fqx2", "rc_funda2", "rc_ibes2", "rc_idx", "rc_ibes2u"]  # 1.1.1: + rc_ibes2u
FIRM_WIDE = {"Murray Stahl": "Horizon Kinetics", "Bill Nygren and Alex Fitch": "Harris Associates",
             "Chris Davis": "Davis Selected"}      # A6: firm-wide 13F filers ("firm, not person")


# ----------------------------------------------------------------------------------------------------------- pulls
def _ref_queries(sql, out):
    """eq_ref 1.1.0 pull queries (verbatim), used only when the ref_* data set is not stored"""
    y0, y1 = CFG["y0"], CFG["y1"]
    q = [("msf", lambda: sql(
        "select permno, permco, yyyymm, mthret::float8 as ret, abs(mthprc)::float8 as prc, shrout::float8 as shrout, "
        "mthcumfacpr::float8 as cfpr, usincflg from crsp.msf_v2 where yyyymm between %d01 and %d12 and %s"
        % (y0, y1, COM)))]
    for y in range(y0 + 1, y1 + 1):
        q.append(("dv_%d" % y, lambda y=y: sql(
            "select permno, (extract(year from dlycaldt) * 100 + extract(month from dlycaldt))::int as yyyymm, "
            "percentile_cont(0.5) within group (order by abs(dlyprc) * dlyvol)::float8 as mdv, count(*) as nd "
            "from crsp.dsf_v2 where dlycaldt between '%d-01-01' and '%d-12-31' and %s and dlyprc is not null "
            "and dlyvol is not null group by 1, 2" % (y, y, COM))))
    q.append(("link", lambda: sql(
        "select gvkey, lpermno as permno, linkprim, linkdt, linkenddt from crsp.ccmxpf_lnkhist "
        "where linktype in ('LC','LU') and linkprim in ('P','C') and lpermno is not null")))
    q.append(("fq", lambda: sql(
        "select gvkey, datadate, fyearq, fqtr, rdq, saleq, cogsq, oiadpq, niq, oancfy, atq, ceqq, cheq, dlcq, dlttq, "
        "pstkq, mibq, actq, lctq, cshoq, ajexq from comp.fundq where indfmt = 'INDL' and datafmt = 'STD' and "
        "popsrc = 'D' and consol = 'C' and datadate between '%d-01-01' and '%d-12-31'" % (y0 - 3, y1))))

    def gics():
        try:
            g = sql("select gvkey, indfrom, indthru, gsector, ggroup, gind, gsubind from comp.co_hgic")
            g["src"] = "co_hgic"
            return g
        except Exception as e:  # noqa: BLE001
            out("comp.co_hgic not readable (%s); current GICS from comp.company" % str(e)[:80])
            g = sql("select gvkey, gsector, ggroup, gind, gsubind from comp.company")
            g["indfrom"], g["indthru"], g["src"] = None, None, "company"
            return g
    q.append(("gics", gics))

    def ibes():
        cols = list(sql("select * from ibes.statsum_epsus limit 1").columns)
        cur = "curcode" if "curcode" in cols else None
        qq = ("select ticker, cusip, statpers, meanest::float8 as meanest, numest%s from ibes.statsum_epsus where "
              "fpi = '1' and measure = 'EPS' and statpers between '%d-06-01' and '%d-12-31' and meanest is not null"
              % ((", " + cur) if cur else "", y0, y1))
        return sql(qq)
    q.append(("ibes", ibes))
    q.append(("names", lambda: sql(
        "select distinct permno, cusip, namedt, coalesce(nameenddt, date '2099-12-31') as nend "
        "from crsp.stocknames_v2 where cusip is not null")))
    return q


def _select_existing(sql, out, schema, table, keys, items, where):
    """select keys + items from schema.table; an item the table does not have comes back as an empty column"""
    have = {str(c).lower() for c in sql("select * from %s.%s limit 1" % (schema, table)).columns}
    miss = [c for c in items if c not in have]
    if miss:
        out("%s.%s has no column(s) %s: stored as empty" % (schema, table, ", ".join(miss)))
    sel = keys + [("%s::float8 as %s" % (c, c)) if c in have else ("null::float8 as %s" % c) for c in items]
    return sql("select %s from %s.%s where %s" % (", ".join(sel), schema, table, where))


def _pick_t10(cols_by_table):
    """(schema, table, date column, value column) of the 10-year constant-maturity nominal Treasury yield, or None"""
    def value_col(cols):
        if "tcmnom_y10" in cols:
            return "tcmnom_y10"
        for c in sorted(cols):
            if "tcm" in c and ("y10" in c or "10y" in c) and "ii" not in c and "real" not in c and "tips" not in c:
                return c
        return None

    def date_col(cols):
        if "date" in cols:
            return "date"
        d = sorted(c for c in cols if "date" in c)
        return d[0] if d else None

    def order(k):
        s, t = k
        return ({"rates_daily": 0, "rates_monthly": 1}.get(t, 2), 0 if s == "frb" else 1, s, t)
    picks = []
    for k in sorted(cols_by_table, key=order):
        v, d = value_col(cols_by_table[k]), date_col(cols_by_table[k])
        if v and d:
            picks.append((k[0], k[1], d, v))
    return picks  # 1.0.2: every candidate in order (the first readable one is used)


def _t10(sql, out):
    tabs = {}
    try:
        c = sql("select table_schema, table_name, column_name from information_schema.columns "
                "where left(table_schema, 3) = 'frb'")
        for s, t, col in c[["table_schema", "table_name", "column_name"]].itertuples(index=False):
            tabs.setdefault((str(s).lower(), str(t).lower()), set()).add(str(col).lower())
    except Exception as e:  # noqa: BLE001
        out("information_schema not readable (%s); trying frb.rates_daily / frb.rates_monthly" % str(e)[:80])
    if not tabs:
        for t in ("rates_daily", "rates_monthly"):
            try:
                tabs[("frb", t)] = {str(x).lower() for x in sql("select * from frb.%s limit 1" % t).columns}
            except Exception:  # noqa: BLE001
                pass
    for (s_, t_), cols in sorted(tabs.items()):  # 1.0.3: metadata only (table and column names)
        c10 = sorted(c for c in cols if "10" in c)
        out("FRB table seen: %s.%s (%d columns; 10-year-like: %s)" % (s_, t_, len(cols), ", ".join(c10[:8]) or "none"))
    picks = _pick_t10(tabs)
    for k in (("frb", "rates_daily"), ("frb", "rates_monthly")):  # 1.0.2: always also try the standard tables
        if k not in tabs:
            picks.append((k[0], k[1], "date", "tcmnom_y10"))
    if not picks:
        raise RuntimeError("STOP: no 10-year constant-maturity Treasury column found in the WRDS FRB tables (%d frb "
                           "tables seen); RECALL_SPEC_v1 says the job stops here" % len(tabs))
    for s, t, d, v in picks:  # 1.0.2: the first candidate this account may read wins (1.0.1 stopped at frb_all_old)
        try:
            df = sql("select %s as date, %s::float8 as y10 from %s.%s where %s between '2008-06-01' and '%s' and %s is "
                     "not null" % (d, v, s, t, d, DATA_END, v))
        except Exception as e:  # noqa: BLE001
            out("10-year Treasury: %s.%s not readable (%s)" % (s, t, str(e).splitlines()[0][:90]))
            continue
        if not len(df):
            out("10-year Treasury: %s.%s.%s has no values in 2008-06 .. %s" % (s, t, v, DATA_END))
            continue
        out("10-year Treasury: %s.%s column %s (date column %s)" % (s, t, v, d))
        df["src"] = "%s.%s.%s" % (s, t, v)
        return df
    out("10-year Treasury: no WRDS FRB table readable among %d candidates; using the public H.15 series (FRED DGS10, "
        "embedded month-end values)" % len(picks))  # 1.0.3
    df = public_t10()
    df["src"] = "public.fred.dgs10"
    return df


def public_t10():
    """FRED DGS10 last daily value of each month 2008-06 .. 2025-12 (1.0.3)"""
    rows = [x.split(":") for x in DGS10_ME.split(",")]
    return pd.DataFrame({"date": pd.to_datetime([d for d, _ in rows], format="%Y%m%d").strftime("%Y-%m-%d"),
                         "y10": [float(v) for _, v in rows]})


def pull(sql, save, load, out, budget=7000):
    t0 = time.time()

    def have(name):
        try:
            load(name)
            return True
        except Exception:  # noqa: BLE001
            return False

    def step(name, fn):
        if have(name):
            return
        if time.time() - t0 > budget:
            out("budget reached before %s" % name)
            return
        try:
            df = fn()
            save(name, df)
            out("%-14s rows %9d  cols %2d  %5.0f s" % (name, len(df), df.shape[1], time.time() - t0))
        except Exception as e:  # noqa: BLE001
            out("%-14s FAILED: %s" % (name, str(e)[:300]))

    out("%s pull" % VERSION)
    reused = []
    for base, fn in _ref_queries(sql, out):
        if have("ref_" + base):
            reused.append("ref_" + base)
            continue
        step("rc_" + base, fn)
    out("reused eq_ref data sets: %d (%s)" % (len(reused), ", ".join(reused[:8]) + (" ..." if len(reused) > 8 else "")))
    fwhere = ("indfmt = 'INDL' and datafmt = 'STD' and popsrc = 'D' and consol = 'C' and datadate between '%s' and "
              "'%s'" % (FUNDA0, DATA_END))
    step("rc_funda", lambda: _select_existing(sql, out, "comp", "funda", ["gvkey", "datadate", "fyear"], FUNDA_COLS,
                                              fwhere))
    qwhere = ("indfmt = 'INDL' and datafmt = 'STD' and popsrc = 'D' and consol = 'C' and datadate between '%s' and "
              "'%s'" % (FQX0, DATA_END))
    step("rc_fqx", lambda: _select_existing(sql, out, "comp", "fundq", ["gvkey", "datadate", "fyearq", "fqtr"], FQX_COLS,
                                            qwhere))
    step("rc_t10", lambda: _t10(sql, out))
    # 1.1.0: inputs of the other recipes
    step("rc_fqx2", lambda: _select_existing(sql, out, "comp", "fundq", ["gvkey", "datadate", "fyearq", "fqtr"],
                                             FQX2_COLS, qwhere))
    step("rc_funda2", lambda: _select_existing(sql, out, "comp", "funda", ["gvkey", "datadate", "fyear"], FUNDA2_COLS,
                                               fwhere))
    step("rc_ibes2", lambda: _ibes2(sql))
    step("rc_idx", lambda: _idx(sql, out))
    step("rc_ibes2u", lambda: _ibes2u(sql, out))  # 1.1.1 (S1)
    left = [n for n in _needed() if not (have(n) or (n.startswith("ref_") and have("rc_" + n[4:])))]
    if "rc_t10" in left:
        out("STOP: the 10-year Treasury yield is not available (RECALL_SPEC_v1: the job stops and says so)")
    out("ALL PULLS COMPLETE" if not left else "left for the next run: %s" % ", ".join(left))


def _needed():
    return (["ref_" + b for b in REF_BASES] + ["ref_dv_%d" % y for y in range(CFG["y0"] + 1, CFG["y1"] + 1)]
            + ["rc_funda", "rc_fqx", "rc_t10"] + NEW_SETS)


def _ibes2(sql):
    """1.1.0: I/B/E/S summary EPS for FY1 and FY2 (fpi 1, 2) and long-term growth (fpi 0), with the period end date"""
    cols = list(sql("select * from ibes.statsum_epsus limit 1").columns)
    cur = ", curcode" if "curcode" in cols else ""
    return sql("select ticker, cusip, statpers, fpi, fpedats, meanest::float8 as meanest, numest%s from "
               "ibes.statsum_epsus where fpi in ('0', '1', '2') and measure = 'EPS' and statpers between '%s' and "
               "'%d-12-31' and meanest is not null" % (cur, IBES0, CFG["y1"]))


def _ibes2u(sql, out):
    """1.1.1 (S1): the UNADJUSTED I/B/E/S summary EPS (ibes.statsumu_epsus) for FY1 and FY2, same fields and date rule
    as rc_ibes2: per-share figures on the share basis of the statistic date. If the table is not readable by this
    account, a one-row marker is stored (column 'unreadable') and run() labels the two criteria provisional."""
    try:
        cols = list(sql("select * from ibes.statsumu_epsus limit 1").columns)
        cur = ", curcode" if "curcode" in cols else ""
        return sql("select ticker, cusip, statpers, fpi, fpedats, meanest::float8 as meanest, numest%s from "
                   "ibes.statsumu_epsus where fpi in ('1', '2') and measure = 'EPS' and statpers between '%s' and "
                   "'%d-12-31' and meanest is not null" % (cur, IBES0, CFG["y1"]))
    except Exception as e:  # noqa: BLE001
        out("ibes.statsumu_epsus not readable (%s): Zlatev P1 and Nygren P4 will be labelled 'provisional (split "
            "basis)'" % str(e).splitlines()[0][:90])
        return pd.DataFrame({"unreadable": [1]})


def _idx(sql, out):
    """1.1.0 (O05): 13F shares held by the three largest index managers, summed per quarter-end and CUSIP (first
    versions, fdate = rdate, as eq_conv). Managers found by name in tfn.s34names; the names found are printed
    (metadata only)."""
    nm = sql("select distinct mgrno, mgrname from tfn.s34names")
    up = nm.mgrname.astype(str).str.upper()
    hit = nm[np.logical_or.reduce([up.str.contains(p_, regex=False) for p_ in IDX_PATTERNS])]
    ids = sorted({int(x) for x in hit.mgrno})
    for p_ in IDX_PATTERNS:
        h = hit[hit.mgrname.astype(str).str.upper().str.contains(p_, regex=False)]
        out("index managers '%s': %d 13F ids (%s)" % (p_, h.mgrno.nunique(), "; ".join(
            sorted({str(x)[:40] for x in h.mgrname})[:12])))
    if not ids:
        raise RuntimeError("no index manager found by name in tfn.s34names")
    return sql("select rdate, cusip, sum(shares)::float8 as sh, count(distinct mgrno) as nmgr from tfn.s34 where "
               "fdate = rdate and rdate between '%s' and '%s' and mgrno in (%s) and shares > 0 group by rdate, cusip"
               % (IDX0, IDX1, ",".join(map(str, ids))))


# ------------------------------------------------------------------------------------------------------- helpers
def ym_add(ym, k):
    i = (ym // 100) * 12 + (ym % 100 - 1) + k
    return (i // 12) * 100 + i % 12 + 1


def ym_end(ym):
    return pd.Timestamp(year=ym // 100, month=ym % 100, day=1) + pd.offsets.MonthEnd(0)


def keynorm(s):
    """copied from eq_ref 1.1.0 (unchanged)"""
    n = pd.to_numeric(s, errors="coerce")
    if len(s) and n.notna().mean() > 0.99:
        return n.map(lambda v: "%d" % v if pd.notna(v) else None)
    return s.astype(object).where(s.notna(), None).map(lambda v: None if v is None else str(v))


def to_bool(s):
    return s.astype(str).str.lower().isin(["true", "1", "1.0"])


def mask_ids(names):
    """copied from eq_ref 1.1.0 (the same masked labels as the say-do tables for the same list)"""
    import hashlib
    order = sorted(names, key=lambda n: hashlib.sha256(n.encode()).hexdigest())
    return {n: "M%02d" % (i + 1) for i, n in enumerate(order)}


def get(load, base):
    """eq_ref's stored data set ref_<base>, else this job's copy rc_<base>"""
    try:
        return load("ref_" + base)
    except Exception:  # noqa: BLE001
        return load("rc_" + base)


def quarter_ends(a, b):
    r, x = [], a
    while x <= b:
        r.append(x)
        x = ym_add(x, 3)
    return r


# ---------------------------------------------------------------------------------------------- accounts (Compustat)
def quarterly_table(fq):
    """copied from eq_ref 1.1.0 (unchanged): one row per gvkey-quarter with TTM flows, balances, year-ago values"""
    f = fq.copy()
    f["gvkey"] = keynorm(f.gvkey)
    f["datadate"] = pd.to_datetime(f.datadate)
    f["rdq"] = pd.to_datetime(f.rdq)
    for c in ("fyearq", "fqtr"):
        f[c] = pd.to_numeric(f[c], errors="coerce")
    f = f.dropna(subset=["fyearq", "fqtr"]).sort_values(["gvkey", "datadate"])
    f = f.drop_duplicates(["gvkey", "fyearq", "fqtr"], keep="last")
    f["qi"] = (f.fyearq * 4 + f.fqtr).astype(int)
    if "oancfy" not in f.columns:
        f["oancfy"] = np.nan
    num = ["saleq", "cogsq", "oiadpq", "niq", "oancfy", "atq", "ceqq", "cheq", "dlcq", "dlttq", "pstkq", "mibq",
           "actq", "lctq", "cshoq", "ajexq"]
    for c in num:
        f[c] = pd.to_numeric(f[c], errors="coerce")
    g = f.groupby("gvkey", sort=False)
    prev_ytd = g.oancfy.shift(1)
    prev_same_year = (g.fyearq.shift(1) == f.fyearq) & (g.qi.shift(1) == f.qi - 1)
    if "cfoq" in f.columns:
        f["cfoq"] = pd.to_numeric(f.cfoq, errors="coerce")
    else:
        f["cfoq"] = np.where(f.fqtr == 1, f.oancfy, np.where(prev_same_year, f.oancfy - prev_ytd, np.nan))
    f["gpq"] = f.saleq - f.cogsq
    g = f.groupby("gvkey", sort=False)

    def lag(col, k):
        v = g[col].shift(k)
        ok = g.qi.shift(k) == f.qi - k
        return v.where(ok)

    for c in ("saleq", "gpq", "oiadpq", "niq", "cfoq"):
        s = f[c].copy()
        for k in (1, 2, 3):
            s = s + lag(c, k)
        f[c[:-1] + "_ttm"] = s
    for c in ("sale_ttm", "gp_ttm", "ni_ttm", "cfo_ttm"):
        f[c + "_l4"] = lag(c, 4)
    for c in ("atq", "ceqq", "dlttq", "actq", "lctq"):
        f[c + "_l4"] = lag(c, 4)
    f["atq_l8"] = lag("atq", 8)
    f["shares_adj"] = f.cshoq * f.ajexq
    f["shares_adj_l4"] = lag("shares_adj", 4)
    f["avail"] = (f.rdq + pd.Timedelta(days=1)).where(f.rdq.notna(), f.datadate + pd.Timedelta(days=CFG["q_lag_days"]))
    return f


def account_measures(q):
    """copied from eq_ref 1.1.0 (unchanged): book measures from one quarter row; money in Compustat millions"""
    m = pd.DataFrame(index=q.index)
    avg_ceq = (q.ceqq + q.ceqq_l4) / 2
    avg_at = (q.atq + q.atq_l4) / 2
    m["roe"] = (q.ni_ttm / avg_ceq).where(avg_ceq > 0)
    m["acc"] = ((q.ni_ttm - q.cfo_ttm) / avg_at).where(avg_at > 0)
    roa = (q.ni_ttm / q.atq_l4).where(q.atq_l4 > 0)
    roa_l4 = (q.ni_ttm_l4 / q.atq_l8).where(q.atq_l8 > 0)
    cfo_a = (q.cfo_ttm / q.atq_l4).where(q.atq_l4 > 0)
    avg_at_l4 = (q.atq_l4 + q.atq_l8) / 2
    lev = (q.dlttq / avg_at).where(avg_at > 0)
    lev_l4 = (q.dlttq_l4 / avg_at_l4).where(avg_at_l4 > 0)
    cr = (q.actq / q.lctq).where(q.lctq > 0)
    cr_l4 = (q.actq_l4 / q.lctq_l4).where(q.lctq_l4 > 0)
    gm = (q.gp_ttm / q.sale_ttm).where(q.sale_ttm > 0)
    gm_l4 = (q.gp_ttm_l4 / q.sale_ttm_l4).where(q.sale_ttm_l4 > 0)
    tu = (q.sale_ttm / q.atq_l4).where(q.atq_l4 > 0)
    tu_l4 = (q.sale_ttm_l4 / q.atq_l8).where(q.atq_l8 > 0)

    def sig(cond, *inputs):
        ok = pd.concat(inputs, axis=1).notna().all(axis=1)
        return cond.astype(float).where(ok)

    parts = [sig(roa > 0, roa), sig(q.cfo_ttm > 0, q.cfo_ttm), sig(roa > roa_l4, roa, roa_l4),
             sig(cfo_a > roa, cfo_a, roa), sig(lev < lev_l4, lev, lev_l4), sig(cr > cr_l4, cr, cr_l4),
             sig(q.shares_adj <= q.shares_adj_l4, q.shares_adj, q.shares_adj_l4), sig(gm > gm_l4, gm, gm_l4),
             sig(tu > tu_l4, tu, tu_l4)]
    P = pd.concat(parts, axis=1)
    nok = P.notna().sum(axis=1)
    m["pio"] = (P.sum(axis=1) / nok * 9).where(nok >= 7)
    m["ebit_ttm"] = q.oiadp_ttm
    m["ceq"] = q.ceqq
    m["netdebt"] = q.dlcq.fillna(0) + q.dlttq.fillna(0) + q.pstkq.fillna(0) + q.mibq.fillna(0) - q.cheq.fillna(0)
    m["netdebt_ok"] = q[["dlcq", "dlttq", "cheq"]].notna().any(axis=1)
    return m


def recall_quarter_measures(q):
    """recipe inputs from the quarterly table (TTM = four consecutive quarters, as eq_ref): capex (capxy year to date,
    differenced inside the fiscal year), share-based pay (stkcoq one quarter; else stkcoy differenced), EBITDA
    (oibdpq), tangible assets (atq - intanq, now and four quarters earlier), net debt for B01 (dlcq + dlttq - cheq)"""
    f = q
    for c in FQX_COLS:
        f[c] = pd.to_numeric(f[c], errors="coerce") if c in f.columns else np.nan

    def lag(col, k):
        g = f.groupby("gvkey", sort=False)
        return g[col].shift(k).where(g.qi.shift(k) == f.qi - k)

    prev_same_year = (lag("fyearq", 1) == f.fyearq)

    def ytd_to_q(col):
        return pd.Series(np.where(f.fqtr == 1, f[col], np.where(prev_same_year, f[col] - lag(col, 1), np.nan)),
                         index=f.index)
    f["rq_capq"] = ytd_to_q("capxy")
    sbc_y = ytd_to_q("stkcoy")
    f["rq_sbcq"] = f.stkcoq.where(f.stkcoq.notna(), sbc_y)

    def ttm(col):
        s = f[col].copy()
        for k in (1, 2, 3):
            s = s + lag(col, k)
        return s
    m = pd.DataFrame(index=f.index)
    m["rq_sale_ttm"] = f.sale_ttm
    m["rq_cfo_ttm"] = f.cfo_ttm
    m["rq_capx_ttm"] = ttm("rq_capq")
    m["rq_sbc_ttm"] = ttm("rq_sbcq")
    m["rq_oibdp_ttm"] = ttm("oibdpq")
    m["rq_tang"] = f.atq - f.intanq
    m["rq_tang_l4"] = lag("atq", 4) - lag("intanq", 4)
    m["rq_nd"] = f.dlcq.fillna(0) + f.dlttq.fillna(0) - f.cheq.fillna(0)
    m["rq_nd_ok"] = f[["dlcq", "dlttq", "cheq"]].notna().any(axis=1)
    return m


def recall_quarter_measures2(f):
    """1.1.0: quarterly inputs of the other recipes (TTM flows from quarterly_table; lags need consecutive fiscal
    quarters): 3-year revenue growth (DRU B1), gross margin and its change over 4 quarters (ZLA B3a, B3b), diluted
    shares against 12 quarters before (STA C04), tangible book per share growth with dividends (PIL B2), dividends per
    share of the last 4 quarters on the latest quarter's share basis (NYG V10), revenue and revenue per diluted share
    growth over 12 quarters (NYG A2), Greenblatt return on capital (LIL Q02), operating margin against the median of
    its last 20 quarters (LIL A2), net income TTM, tangible equity"""
    for c in FQX2_COLS:
        f[c] = pd.to_numeric(f[c], errors="coerce") if c in f.columns else np.nan
    g = f.groupby("gvkey", sort=False)

    def lagk(s, k):
        return s.groupby(f.gvkey, sort=False).shift(k).where(g.qi.shift(k) == f.qi - k)

    m = pd.DataFrame(index=f.index)
    sale = f.sale_ttm
    s12 = lagk(sale, 12)
    ratio = (sale / s12).where(s12 > 0)
    m["rq_gr3"] = (np.sign(ratio) * np.abs(ratio) ** (1.0 / 3) - 1).where(ratio > 0, -1.0).where(ratio.notna())
    m["rq_gr1"] = (sale / f.sale_ttm_l4 - 1).where(f.sale_ttm_l4 > 0)
    m["rq_saleg12"] = (sale / s12 - 1).where(s12 > 0)
    gm = (f.gp_ttm / sale).where(sale > 0)
    m["rq_gm"] = gm
    m["rq_dgm"] = gm - (f.gp_ttm_l4 / f.sale_ttm_l4).where(f.sale_ttm_l4 > 0)
    shd = f.cshfdq * f.ajexq
    shd12 = lagk(shd, 12)
    m["rq_c04q"] = (shd / shd12).where(shd12 > 0)
    rps = (sale / shd).where(shd > 0)
    rps12 = lagk(rps, 12)
    m["rq_rpsg"] = (rps / rps12 - 1).where(rps12 > 0)
    tbv = f.ceqq - f.intanq
    shs = f.cshoq * f.ajexq
    tbvps = (tbv / shs).where(shs > 0)
    tb12 = lagk(tbvps, 12)
    dpsa = f.dvpsxq.fillna(0) / f.ajexq.where(f.ajexq > 0)       # no dividend reported = 0; latest-basis per share
    d12 = sum(lagk(dpsa, k) for k in range(12))
    m["rq_tbg"] = ((tbvps + d12) / tb12 - 1).where(tb12 > 0)
    m["rq_dps4q"] = f.ajexq * sum(lagk(dpsa, k) for k in range(4))  # on the share basis of the latest quarter
    den = f.actq - f.cheq.fillna(0) - f.lctq + f.dlcq.fillna(0) + f.ppentq
    m["rq_q02"] = (f.oiadp_ttm / den).where(den > 0)
    opm = (f.oiadp_ttm / sale).where(sale > 0)
    O = pd.concat([lagk(opm, k) for k in range(20)], axis=1)
    m["rq_opmdev"] = opm - O.median(axis=1).where(O.notna().sum(axis=1) >= 12)
    m["rq_ni_ttm"] = f.ni_ttm
    m["rq_tbv"] = tbv
    return m


def annual_table(fa):
    """one row per gvkey-fiscal year with the recipe's history measures (lags require consecutive fiscal years)"""
    a = fa.copy()
    a["gvkey"] = keynorm(a.gvkey)
    a["datadate"] = pd.to_datetime(a.datadate).astype("datetime64[ns]")
    a["fyear"] = pd.to_numeric(a.fyear, errors="coerce")
    for c in FUNDA_COLS:
        a[c] = pd.to_numeric(a[c], errors="coerce") if c in a.columns else np.nan
    for c in FUNDA2_COLS:  # 1.1.0
        a[c] = pd.to_numeric(a[c], errors="coerce") if c in a.columns else np.nan
    a = a.dropna(subset=["gvkey", "fyear", "datadate"]).sort_values(["gvkey", "fyear", "datadate"])
    a = a.drop_duplicates(["gvkey", "fyear"], keep="last").reset_index(drop=True)

    def lag(col, k):
        v = a[col] if isinstance(col, str) else col
        ok = (a.gvkey.shift(k) == a.gvkey) & (a.fyear.shift(k) == a.fyear - k)
        return v.shift(k).where(ok)

    def cagr(cur, base, years):
        ratio = (cur / base).where(base > 0)
        g = np.sign(ratio) * np.abs(ratio) ** (1.0 / years) - 1
        return g.where(ratio > 0, -1.0).where(ratio.notna())

    m = pd.DataFrame({"gvkey": a.gvkey, "datadate": a.datadate, "fyear": a.fyear})
    m["avail"] = a.datadate + pd.Timedelta(days=ANN_LAG_DAYS)
    ok = a.revt.notna() & a.ni.notna()
    cont = ok & lag(ok.astype(float), 1).eq(1.0)
    seg = (~cont).cumsum()
    m["fy_run"] = (a.groupby(seg).cumcount() + 1).where(ok, 0)                    # B1
    ni_l = [lag("ni", k) for k in range(10)]
    N = pd.concat(ni_l, axis=1)
    m["s01"] = (N < 0).sum(axis=1).where(N.notna().all(axis=1))                   # S01 (B2)
    m["g01"] = cagr(a.revt, lag("revt", 5), 5)                                    # G01 (B3)
    eps = a.epsfx.where(a.epsfx.notna(), a.epspx)
    eps_adj = (eps / a.ajex).where(a.ajex > 0)
    m["g02"] = cagr(eps_adj, lag(eps_adj, 5), 5)                                  # G02 (B3)
    rev_l = [lag("revt", k) for k in range(10)]
    gr = pd.concat([(rev_l[k] / rev_l[k + 1] - 1).where(rev_l[k + 1] > 0) for k in range(9)], axis=1)
    m["s03"] = gr.std(axis=1, ddof=0).where(gr.notna().all(axis=1))               # S03 (B4): 9 growth rates, 10 FY
    opm = (a.oiadp / a.revt).where(a.revt > 0)
    m["g06"] = opm - lag(opm, 3)                                                  # G06 (B5)
    O = pd.concat([lag(opm, k) for k in range(10)], axis=1)
    m["s02"] = O.std(axis=1, ddof=0).where(O.notna().all(axis=1))                 # S02 (B8)
    sh = a.cshfd.where(a.cshfd.notna(), a.csho) * a.ajex
    sh_l3 = lag(sh, 3)
    m["c04"] = (sh / sh_l3).where(sh_l3 > 0)                                      # C04 (B9)
    A = pd.concat([lag("aqc", k) for k in range(3)], axis=1)
    C = pd.concat([lag("oancf", k) for k in range(3)], axis=1)
    cfo3 = C.sum(axis=1).where(C.notna().all(axis=1))
    m["c06"] = (A.fillna(0).sum(axis=1) / cfo3).where(cfo3 > 0)                   # C06 (A5), missing aqc = none
    m["c06_strict"] = m.c06.where(A.notna().all(axis=1))
    m["aqc_filled"] = A.isna().any(axis=1) & cfo3.gt(0)
    m["sbc_ann"] = a.stkco
    # 1.1.0: kantesaria_v2 (B5 on 5 fiscal years, B13 grid 3 / 5 / 9, A5 on two 3-year windows)
    m["g06_5"] = opm - lag(opm, 5)
    m["g06_9"] = opm - lag(opm, 9)
    m["c06_prev"] = lag(m.c06, 3)
    m["c06_strict_prev"] = lag(m.c06_strict, 3)
    # 1.1.0: hohn_v1 S04* = years of the last 10 with Q01 > 15% (or Q01 denominator <= 0 and EBIT > 0). Q01 = EBIT x
    # (1 - income tax / pre-tax income) / average over the year of (total equity incl. minorities + total debt - cash);
    # tax rate missing when pre-tax income <= 0; missing debt / cash / minorities = 0; equity missing = Q01 missing
    den = a.seq + a.mib.fillna(0) + a.dltt.fillna(0) + a.dlc.fillna(0) - a.che.fillna(0)
    avg = (den + lag(den, 1)) / 2
    tax = (a.txt / a.pi).where(a.pi > 0)
    q01 = (a.oiadp * (1 - tax) / avg).where(avg > 0)
    yok = (((avg > 0) & (q01 > 0.15)) | ((avg <= 0) & (a.oiadp > 0))).astype(float)
    Y = pd.concat([lag(yok, k) for k in range(10)], axis=1)
    m["s04star"] = Y.sum(axis=1).where(Y.notna().all(axis=1))
    m["q01_ann"] = q01
    return m


# --------------------------------------------------------------------------------------------------------- panel
def price_direction(msf, out):
    """copied from eq_ref 1.1.0 ibes_revision (unchanged logic): CRSP price factor direction from AAPL's 2020-08 split"""
    a = msf[(msf.permno == 14593) & msf.yyyymm.isin([202007, 202009])].set_index("yyyymm").cfpr
    s = 1.0
    if len(a) == 2 and a.loc[202007] > 0:
        s = 1.0 if a.loc[202009] / a.loc[202007] > 1 else -1.0
        out("CRSP price factor direction check: %+d" % s)  # 1.0.1: no company or value printed
    else:
        out("AAPL factor check not available; direction +1 assumed")
    return s


def build_panel(D, out):
    """copied from eq_ref 1.1.0 build_panel. Changes: (1) the next-month return (ret_next) is NOT computed (this job
    reads no forward return); (2) the recipe's quarterly inputs (recall_quarter_measures) are joined at t with the
    same as-of rule; (3) the as-of keys are cast to datetime64[ns] (pandas versions differ); (4) returns (u, msf,
    price direction, GICS source); (5) 1.1.0: the other recipes' quarterly inputs (recall_quarter_measures2) too."""
    msf = D["msf"].copy()
    msf["mcap"] = msf.prc * msf.shrout * 1000.0
    msf = msf[msf.usincflg.astype(str).str.upper() == "Y"]
    msf = msf.sort_values(["permno", "yyyymm"]).drop_duplicates(["permno", "yyyymm"], keep="last")
    msf["mi"] = (msf.yyyymm // 100) * 12 + msf.yyyymm % 100 - 1
    co = msf.groupby(["permco", "yyyymm"]).mcap.sum().rename("mcap_co")
    msf = msf.join(co, on=["permco", "yyyymm"])
    msf["nlines"] = msf.groupby(["permco", "yyyymm"]).permno.transform("nunique")
    g = msf.groupby("permno", sort=False)
    cnt = pd.Series(0.0, index=msf.index)
    acc = pd.Series(0.0, index=msf.index)
    for k in range(1, 12):
        v = g.ret.shift(k)
        ok = (g.mi.shift(k) == msf.mi - k) & v.notna()
        acc = acc + np.log1p(v.clip(lower=-0.9999)).where(ok, 0.0)
        cnt = cnt + ok.astype(float)
    msf["mom"] = np.expm1(acc).where(cnt >= 9)
    dv = D["dv"].copy()
    dv = dv.sort_values(["permno", "yyyymm"])
    dv["mi"] = (dv.yyyymm // 100) * 12 + dv.yyyymm % 100 - 1
    gd = dv.groupby("permno", sort=False)
    a = [dv.mdv] + [gd.mdv.shift(k).where(gd.mi.shift(k) == dv.mi - k) for k in (1, 2)]
    dv["mdv3"] = pd.concat(a, axis=1).median(axis=1, skipna=True)
    msf = msf.merge(dv[["permno", "yyyymm", "mdv3"]], on=["permno", "yyyymm"], how="left")
    msf["size_rank"] = msf.groupby("yyyymm").mcap.rank(ascending=False, method="first")
    u = msf[(msf.size_rank <= CFG["top_n"]) & (msf.yyyymm >= ym_add(CFG["form0"], -3)) & (msf.yyyymm <= CFG["form1"])].copy()
    u["in_univ"] = (u.prc >= CFG["min_price"]) & (u.mdv3 >= CFG["min_dv"])
    u["t_end"] = [ym_end(x) for x in u.yyyymm]
    lk = D["link"].copy()
    lk["gvkey"] = keynorm(lk.gvkey)
    lk["linkdt"] = pd.to_datetime(lk.linkdt)
    lk["linkenddt"] = pd.to_datetime(lk.linkenddt).fillna(pd.Timestamp("2099-12-31"))
    lk["pri"] = (lk.linkprim == "P").astype(int)
    x = u[["permno", "yyyymm", "t_end"]].merge(lk, on="permno", how="inner")
    x = x[(x.linkdt <= x.t_end) & (x.t_end <= x.linkenddt)].sort_values(["permno", "yyyymm", "pri"])
    x = x.drop_duplicates(["permno", "yyyymm"], keep="last")[["permno", "yyyymm", "gvkey"]]
    u = u.merge(x, on=["permno", "yyyymm"], how="left")
    gi = D["gics"].copy()
    gi["gvkey"] = keynorm(gi.gvkey)
    src = str(gi.src.iloc[0]) if len(gi) else "none"
    if src == "co_hgic":
        gi["indfrom"] = pd.to_datetime(gi.indfrom)
        gi["indthru"] = pd.to_datetime(gi.indthru).fillna(pd.Timestamp("2099-12-31"))
        y = u[["permno", "yyyymm", "t_end", "gvkey"]].dropna(subset=["gvkey"]).merge(gi, on="gvkey", how="inner")
        y = y[(y.indfrom <= y.t_end) & (y.t_end <= y.indthru)].drop_duplicates(["permno", "yyyymm"], keep="last")
    else:
        y = u[["permno", "yyyymm", "gvkey"]].dropna(subset=["gvkey"]).merge(gi.drop_duplicates("gvkey"), on="gvkey", how="inner")
    u = u.merge(y[["permno", "yyyymm", "gsector", "ggroup", "gind", "gsubind"]], on=["permno", "yyyymm"], how="left")
    for c in ("gsector", "ggroup", "gind", "gsubind"):
        u[c] = u[c].astype(str).str.replace(r"\.0$", "", regex=True).replace({"nan": np.nan, "None": np.nan})
    excl = (u.ggroup.isin(["4010", "4030", "4040"]) | (u.gsector == "60") | (u.gsubind == "35201010"))
    u["excluded"] = excl
    q = quarterly_table(D["fq"])
    am = account_measures(q)
    rq = recall_quarter_measures(q)
    rq2 = recall_quarter_measures2(q)  # 1.1.0
    q = pd.concat([q[["gvkey", "datadate", "avail"]], am, rq, rq2], axis=1).dropna(subset=["avail"]).sort_values("avail")
    left = u[["permno", "yyyymm", "t_end", "gvkey"]].dropna(subset=["gvkey"]).sort_values("t_end")
    left = left.rename(columns={"t_end": "avail_key"})
    q = q.rename(columns={"avail": "avail_key"})
    left["gvkey"] = left.gvkey.astype(str)
    q["gvkey"] = q.gvkey.astype(str)
    left["avail_key"] = left.avail_key.astype("datetime64[ns]")
    q["avail_key"] = q.avail_key.astype("datetime64[ns]")
    q["datadate"] = q.datadate.astype("datetime64[ns]")
    out("account join: %d of %d universe line-months have a gvkey; %d keys in the quarterly table, %d shared" % (
        len(left), len(u), q.gvkey.nunique(), len(set(left.gvkey) & set(q.gvkey))))
    j = pd.merge_asof(left, q, on="avail_key", by="gvkey", direction="backward")
    j = j[(j.avail_key - j.datadate).dt.days <= CFG["stale_days"]]
    u = u.merge(j.drop(columns=["avail_key", "gvkey"]), on=["permno", "yyyymm"], how="left")
    ev = u.mcap_co + u.netdebt * 1e6
    u["ey"] = (u.ebit_ttm * 1e6 / ev).where((ev > 0) & u.netdebt_ok.fillna(False).astype(bool))
    u["bp"] = (u.ceq * 1e6 / u.mcap_co).where(u.mcap_co > 0)
    s = price_direction(msf, out)
    u["rev"] = ibes_revision(D, u, msf, s)
    u["t_end"] = u.t_end.astype("datetime64[ns]")
    out("GICS source: %s; universe months %d..%d" % (src, int(u.yyyymm.min()), int(u.yyyymm.max())))
    return u, msf, s, src


def ibes_revision(D, u, msf, s):
    """copied from eq_ref 1.1.0 (the factor direction is passed in instead of computed here)"""
    ib = D["ibes"].copy()
    if "curcode" in ib:
        ib = ib[ib.curcode.astype(str).str.upper().isin(["USD", "NONE", "NAN"])]
    ib["statpers"] = pd.to_datetime(ib.statpers)
    nm = D["names"].copy()
    nm["namedt"], nm["nend"] = pd.to_datetime(nm.namedt), pd.to_datetime(nm.nend)
    x = ib.merge(nm, on="cusip", how="inner")
    x = x[(x.statpers >= x.namedt) & (x.statpers <= x.nend)].sort_values(["permno", "statpers"])
    x = x.drop_duplicates(["permno", "statpers"], keep="last")[["permno", "statpers", "meanest"]]
    x = x.sort_values("statpers")

    def at(ends):
        k = pd.DataFrame({"permno": u.permno.values, "key": ends, "row": np.arange(len(u))}).sort_values("key")
        r = pd.merge_asof(k, x.rename(columns={"statpers": "key"}), on="key", by="permno", direction="backward",
                          tolerance=pd.Timedelta(days=CFG["ibes_tol_days"]))
        return r.sort_values("row").meanest.to_numpy()

    e_now = at(pd.to_datetime([ym_end(v) for v in u.yyyymm]).values)
    e_l3 = at(pd.to_datetime([ym_end(ym_add(v, -3)) for v in u.yyyymm]).values)
    last = D["cf_last"] if "cf_last" in D else msf.sort_values("yyyymm").groupby("permno").cfpr.last()
    cf_last = u.permno.map(last).to_numpy(float)
    cf_t = pd.merge(u[["permno", "yyyymm"]], msf[["permno", "yyyymm", "cfpr"]], on=["permno", "yyyymm"], how="left").cfpr.to_numpy(float)
    padj = u.prc.to_numpy(float) * np.power(cf_t / cf_last, s)
    rev = (e_now - e_l3) / padj
    rev[~np.isfinite(rev) | (padj <= 0)] = np.nan
    return rev


def rank_panel(u):
    """copied from eq_ref 1.1.0 (unchanged): inside-sector percentile of the reference-book score"""
    r = u[u.in_univ & ~u.excluded & u.gsector.notna()].copy()
    for m in MEASURES:
        v = r[m] * HIGH_GOOD[m]
        r["rk_" + m] = v.groupby([r.yyyymm, r.gsector]).rank(pct=True)
    miss = r[["rk_" + m for m in MEASURES]].isna().sum(axis=1)
    r["n_missing"] = miss
    for m in MEASURES:
        r["rk_" + m] = r["rk_" + m].fillna(0.5)
    for gname, ms in GROUPS.items():
        r["g_" + gname] = r[["rk_" + m for m in ms]].mean(axis=1)
    r["score"] = r[["g_" + gn for gn in GROUPS]].mean(axis=1)
    r = r[r.n_missing <= CFG["max_missing"]].copy()
    r["sec_pct"] = r.groupby(["yyyymm", "gsector"]).score.rank(pct=True)
    return r


def price_measures(msf, u, s):
    """P03 (close / highest month-end close of months t-11..t - 1, split-adjusted with the CRSP factor) and the
    12-month compound total return of months t-11..t minus the same for the value-weighted eligible universe (P3).
    At least 9 of the 12 months present. Only months up to T1 are read."""
    m = msf[msf.yyyymm <= T1][["permno", "yyyymm", "mi", "ret", "prc", "cfpr"]].copy()
    m = m.sort_values(["permno", "mi"]).reset_index(drop=True)
    m["padj"] = m.prc * np.power(m.cfpr.where(m.cfpr > 0), s)
    hi = m.padj.copy()
    pc = m.padj.notna().astype(int)
    acc = np.log1p(m.ret.clip(lower=-0.9999)).fillna(0.0)
    rc = m.ret.notna().astype(int)
    for k in range(1, 12):
        ok = (m.permno.shift(k) == m.permno) & (m.mi.shift(k) == m.mi - k)
        v = m.padj.shift(k).where(ok)
        hi = np.fmax(hi, v)
        pc = pc + v.notna().astype(int)
        rv = m.ret.shift(k).where(ok)
        acc = acc + np.log1p(rv.clip(lower=-0.9999)).fillna(0.0)
        rc = rc + rv.notna().astype(int)
    m["p03"] = (m.padj / hi - 1).where((pc >= 9) & m.padj.notna() & (hi > 0))
    m["r12"] = np.expm1(acc).where(rc >= 9)
    # value-weighted eligible universe: lines eligible at the end of month m-1, weights = line market value then
    e = u[u.in_univ & u.gsector.notna() & ~u.excluded][["permno", "yyyymm", "mcap"]].copy()
    e["ym"] = [ym_add(int(x), 1) for x in e.yyyymm]
    e = e[e.ym <= T1].merge(m[["permno", "yyyymm", "ret"]].rename(columns={"yyyymm": "ym"}), on=["permno", "ym"],
                            how="inner").dropna(subset=["ret", "mcap"])
    e["wr"] = e.mcap * e.ret
    vw = e.groupby("ym").wr.sum() / e.groupby("ym").mcap.sum()
    mk = {}
    for t in quarter_ends(T0, T1):
        ms = [ym_add(t, -k) for k in range(12)]
        if all(x in vw.index for x in ms):
            mk[t] = float(np.prod([1 + vw.loc[x] for x in ms]) - 1)
    return m[["permno", "yyyymm", "p03", "r12"]], mk


def treasury_at(t10, ts):
    """last 10-year yield on or before each date (decimal); at most T10_TOL_DAYS old"""
    y = t10.copy()
    y["date"] = pd.to_datetime(y.date).astype("datetime64[ns]")
    y["y10"] = pd.to_numeric(y.y10, errors="coerce")
    y = y.dropna(subset=["date", "y10"]).sort_values("date")
    scale = 100.0 if y.y10.median() > 0.5 else 1.0
    k = pd.DataFrame({"date": pd.to_datetime(ts).astype("datetime64[ns]")}).sort_values("date")
    r = pd.merge_asof(k, y[["date", "y10"]], on="date", direction="backward", tolerance=pd.Timedelta(days=T10_TOL_DAYS))
    return dict(zip(r.date, r.y10 / scale)), scale


def recall_panel(D, u, msf, s, out):
    """eligible stocks at each quarter-end t (R3 universe, price and liquidity, GICS sector known) with every recipe
    measure. 1.1.0: the rows of house-excluded industries (A8 2a; column 'excluded') are kept, for the recipes that
    state that the house exclusions do not apply to them (recipe_set); the size-third cells are made per recipe set
    (add_cells), so the house set and its cells are those of 1.0.3."""
    qe = quarter_ends(T0, T1)
    E = u[u.yyyymm.isin(qe) & u.in_univ & u.gsector.notna()].copy()
    H = E[~E.excluded]
    out("eligible stock-quarters: %d at %d quarter-ends (median %d per quarter-end)" % (
        len(H), H.yyyymm.nunique(), int(H.groupby("yyyymm").size().median()) if len(H) else 0))
    out("with the house-excluded industries (recipes for which the house exclusions do not apply): %d" % len(E))
    # annual accounts known at t
    A = annual_table(D["funda"])
    A = A.sort_values("avail")
    left = E[["permno", "yyyymm", "t_end", "gvkey"]].dropna(subset=["gvkey"]).rename(columns={"t_end": "avail"})
    left["avail"] = left.avail.astype("datetime64[ns]")
    left = left.sort_values("avail")
    left["gvkey"] = left.gvkey.astype(str)
    A["gvkey"] = A.gvkey.astype(str)
    j = pd.merge_asof(left, A.rename(columns={"datadate": "fy_datadate"}), on="avail", by="gvkey", direction="backward")
    j = j[(j.avail - j.fy_datadate).dt.days <= ANN_STALE_DAYS]
    keep = ["fy_run", "s01", "g01", "g02", "s03", "g06", "s02", "c04", "c06", "c06_strict", "aqc_filled", "sbc_ann",
            "g06_5", "g06_9", "c06_prev", "c06_strict_prev", "s04star", "q01_ann"]  # 1.1.0: last six
    E = E.merge(j[["permno", "yyyymm"] + keep], on=["permno", "yyyymm"], how="left")
    E["fy_run"] = E.fy_run.fillna(0)
    # prices
    pm, mk = price_measures(msf, u, s)
    E = E.merge(pm, on=["permno", "yyyymm"], how="left")
    E["mkt12"] = E.yyyymm.map(mk)
    E["p3rel"] = E.r12 - E.mkt12
    # Treasury
    yt, scale = treasury_at(D["t10"], [ym_end(t) for t in qe])
    E["y10"] = [yt.get(ym_end(int(t)), np.nan) for t in E.yyyymm]
    out("10-year Treasury source %s (scale /%g); quarter-ends with a value: %d of %d" % (
        str(D["t10"].src.iloc[0]) if "src" in D["t10"] and len(D["t10"]) else "?", scale,
        sum(1 for t in qe if np.isfinite(yt.get(ym_end(t), np.nan))), len(qe)))
    gap = [t for t in qe if not np.isfinite(yt.get(ym_end(t), np.nan))]
    if gap:  # 1.0.1: a quarter-end without a Treasury value would fail P1 for every stock: stop instead
        raise RuntimeError("STOP: 10-year Treasury missing at %d evaluation quarter-end(s) (first %s)" % (len(gap), gap[0]))
    # quarterly measures at t
    E["c01"] = (E.rq_capx_ttm / E.rq_sale_ttm).where(E.rq_sale_ttm > 0)
    sbc_q = E.rq_sbc_ttm
    E["sbc_src"] = np.where(sbc_q.notna(), "quarterly", np.where(E.sbc_ann.notna(), "annual", "none"))
    sbc = sbc_q.where(sbc_q.notna(), E.sbc_ann)
    fcf = E.rq_cfo_ttm - E.rq_capx_ttm
    mc = E.mcap_co.where(E.mcap_co > 0)
    E["p1gap"] = ((fcf - sbc.fillna(0)) * 1e6 / mc) - E.y10
    E["p1gap_strict"] = ((fcf - sbc) * 1e6 / mc) - E.y10
    ebitda = E.rq_oibdp_ttm
    E["b01"] = (E.rq_nd / ebitda).where((ebitda > 0) & E.rq_nd_ok.fillna(False).astype(bool))
    avg_tang = (E.rq_tang + E.rq_tang_l4) / 2
    E["b7"] = (E.ebit_ttm / avg_tang).where(avg_tang > 0)
    recall_extra(D, E, msf, s, out)  # 1.1.0
    return E


def add_cells(E):
    """size thirds inside sector and t (company market value), made on the recipe's own eligible set (1.0.3 code)"""
    pct = E.groupby(["yyyymm", "gsector"]).mcap_co.rank(pct=True, method="first")
    E["third"] = np.ceil(pct * 3).clip(1, 3)
    E["cell"] = E.yyyymm.astype(str) + "|" + E.gsector.astype(str) + "|" + E.third.astype(int).astype(str)
    return E


def recipe_set(E, rec):
    """the recipe's eligible set: the house set (A8 2a exclusions out, as 1.0.3) unless the recipe states that the
    house exclusions do not apply (universe 'all'), with its own size-third cells"""
    P = E if rec.get("universe") == "all" else E[~E.excluded.astype(bool)]
    return add_cells(P.reset_index(drop=True).copy())


def price_measures2(msf, s):
    """1.1.0: P02 momentum 6-1 (compound return of months t-5 .. t-1, at least 4 of the 5), PIL A2 (month-end
    split-adjusted close at t at or below the lowest of months t-11 .. t-1), LIL B2 (the lowest close of months
    t-11 .. t was set in months t-2 .. t; full form: t-5 .. t, t-11 .. t). Price windows: at least 9 of the 12
    months t-11 .. t present and the close at t present (as P03). Only months up to T1 are read."""
    m = msf[msf.yyyymm <= T1][["permno", "yyyymm", "mi", "ret", "prc", "cfpr"]].copy()
    m = m.sort_values(["permno", "mi"]).reset_index(drop=True)
    m["padj"] = m.prc * np.power(m.cfpr.where(m.cfpr > 0), s)
    L, acc, rc = [m.padj], pd.Series(0.0, index=m.index), pd.Series(0, index=m.index)
    for k in range(1, 12):
        ok = (m.permno.shift(k) == m.permno) & (m.mi.shift(k) == m.mi - k)
        L.append(m.padj.shift(k).where(ok))
        if k <= 5:
            rv = m.ret.shift(k).where(ok)
            acc = acc + np.log1p(rv.clip(lower=-0.9999)).fillna(0.0)
            rc = rc + rv.notna().astype(int)
    W = pd.concat(L, axis=1)
    okw = (W.notna().sum(axis=1) >= 9) & m.padj.notna()
    m["p02"] = np.expm1(acc).where(rc >= 4)
    m["low12new"] = (m.padj <= W.iloc[:, 1:].min(axis=1)).astype(float).where(okw)
    for nm_, k in (("lowq", 3), ("low6", 6), ("low12", 12)):
        rest = W.iloc[:, k:].min(axis=1) if k < 12 else pd.Series(np.inf, index=m.index)
        m[nm_] = (W.iloc[:, :k].min(axis=1) <= rest.fillna(np.inf)).astype(float).where(okw)
    return m[["permno", "yyyymm", "p02", "low12new", "lowq", "low6", "low12"]]


def cusip8(s):
    """1.1.0: CUSIP as 8 characters (a CUSIP read back as a number loses its leading zeros)"""
    return s.astype(str).str.strip().str.replace(r"\.0$", "", regex=True).str.zfill(8)


def ibes2_at(D, E, msf, s):
    """1.1.0: FY1 mean, number of estimates and period end, FY2 mean and long-term growth mean (latest within 35 days
    before t, by CUSIP through CRSP names as eq_ref), and the CRSP price at t on the I/B/E/S share basis (as E01)"""
    res = _ibes_match(D["ibes2"], D["names"], E, ("1", "2", "0"))
    E["fy1"] = res["1"].meanest.to_numpy(float)
    E["n1"] = pd.to_numeric(res["1"].numest, errors="coerce").to_numpy(float)
    E["fpe1"] = pd.to_datetime(res["1"].fpedats).values
    E["fy2"] = res["2"].meanest.to_numpy(float)
    E["ltg"] = res["0"].meanest.to_numpy(float) / 100.0       # I/B/E/S long-term growth is in percent
    last = D["cf_last"] if "cf_last" in D else msf.sort_values("yyyymm").groupby("permno").cfpr.last()
    cf_last = E.permno.map(last).to_numpy(float)
    cf_t = pd.merge(E[["permno", "yyyymm"]], msf[["permno", "yyyymm", "cfpr"]], on=["permno", "yyyymm"],
                    how="left").cfpr.to_numpy(float)
    padj = E.prc.to_numpy(float) * np.power(cf_t / cf_last, s)
    padj[~np.isfinite(padj) | (padj <= 0)] = np.nan
    E["padj_ib"] = padj
    E["e04"] = (E.fy2 / E.fy1 - 1).where(E.fy1 > 0)
    # 1.1.1 (S1): price-to-estimate criteria on one share basis = unadjusted FY1 / FY2 against the price at t as traded
    u_ = D.get("ibes2u")
    if u_ is not None and "unreadable" not in u_.columns:
        ru = _ibes_match(u_, D["names"], E, ("1", "2"))
        E["fy1b"] = ru["1"].meanest.to_numpy(float)
        E["fy2b"] = ru["2"].meanest.to_numpy(float)
        E["px_ib"] = E.prc.where(E.prc > 0).astype(float)
        E["ib_basis"] = "unadjusted"
    else:                                  # provisional (split basis): the 1.1.0 method
        E["fy1b"], E["fy2b"], E["px_ib"], E["ib_basis"] = E.fy1, E.fy2, E.padj_ib, "provisional"
    E["pfy2"] = (E.px_ib / E.fy2b).where(E.fy2b > 0)


def _ibes_match(ib, names, E, fpis):
    """1.1.0 matching (moved here in 1.1.1, unchanged): by CUSIP through CRSP names, latest statistic within 35 days
    before t, per fpi"""
    ib = ib.copy()
    if "curcode" in ib:
        ib = ib[ib.curcode.astype(str).str.upper().isin(["USD", "NONE", "NAN"])]
    ib["statpers"] = pd.to_datetime(ib.statpers)
    ib["fpedats"] = pd.to_datetime(ib.fpedats, errors="coerce")
    ib["fpi"] = ib.fpi.astype(str).str.replace(r"\.0$", "", regex=True)
    nm = names.copy()
    nm["namedt"], nm["nend"] = pd.to_datetime(nm.namedt), pd.to_datetime(nm.nend)
    ib["cusip"], nm["cusip"] = cusip8(ib.cusip), cusip8(nm.cusip)
    x = ib.merge(nm, on="cusip", how="inner")
    x = x[(x.statpers >= x.namedt) & (x.statpers <= x.nend)].sort_values(["permno", "fpi", "statpers"])
    x = x.drop_duplicates(["permno", "fpi", "statpers"], keep="last")
    ends = pd.to_datetime([ym_end(int(v)) for v in E.yyyymm]).values
    k = pd.DataFrame({"permno": E.permno.values, "key": ends, "row": np.arange(len(E))}).sort_values("key")
    k["key"] = k.key.astype("datetime64[ns]")
    res = {}
    for f_ in fpis:
        y = x[x.fpi == f_][["permno", "statpers", "meanest", "numest", "fpedats"]].rename(columns={"statpers": "key"})
        y["key"] = y.key.astype("datetime64[ns]")
        r = pd.merge_asof(k, y.sort_values("key"), on="key", by="permno", direction="backward",
                          tolerance=pd.Timedelta(days=CFG["ibes_tol_days"])).sort_values("row")
        res[f_] = r
    return res


def o05_at(D, E, msf):
    """1.1.0 (STA B3): O05 = shares held by the three largest index managers at the last 13F quarter-end before t
    (filed by t) / CRSP shares outstanding at that quarter-end (line level); no holding found = missing"""
    h = D["idx"].copy()
    h["rdate"] = pd.to_datetime(h.rdate)
    nm = D["names"].copy()
    nm["namedt"], nm["nend"] = pd.to_datetime(nm.namedt), pd.to_datetime(nm.nend)
    h["cusip"], nm["cusip"] = cusip8(h.cusip), cusip8(nm.cusip)
    x = h.merge(nm, on="cusip", how="inner")
    x = x[(x.rdate >= x.namedt) & (x.rdate <= x.nend)].drop_duplicates(["rdate", "cusip"])
    x["ym"] = x.rdate.dt.year * 100 + x.rdate.dt.month
    x = x.groupby(["permno", "ym"], as_index=False).sh.sum()
    sh = msf[["permno", "yyyymm", "shrout"]].rename(columns={"yyyymm": "ym"})
    x = x.merge(sh, on=["permno", "ym"], how="inner")
    x["o05"] = (x.sh / (x.shrout * 1000.0)).where(x.shrout > 0)
    k = pd.DataFrame({"permno": E.permno.values, "ym": [ym_add(int(v), -3) for v in E.yyyymm]})
    E["o05"] = k.merge(x[["permno", "ym", "o05"]], on=["permno", "ym"], how="left").o05.to_numpy(float)


def recall_extra(D, E, msf, s, out):
    """1.1.0: the measures of the other recipes, on every eligible row (row order kept)"""
    mc = E.mcap_co.where(E.mcap_co > 0)
    fcf = E.rq_cfo_ttm - E.rq_capx_ttm
    E["rq_fcfm"] = (fcf / E.rq_sale_ttm).where(E.rq_sale_ttm > 0)               # Q06
    E["b04"] = (-E.rq_nd * 1e6 / mc).where(E.rq_nd_ok.fillna(False).astype(bool))  # B04
    E["v04"] = fcf * 1e6 / mc                                                 # V04
    E["v02"] = E.rq_ni_ttm * 1e6 / mc                                         # V02
    E["v07"] = E.rq_tbv * 1e6 / mc                                            # V07
    pm = price_measures2(msf, s)
    for c in ("p02", "low12new", "lowq", "low6", "low12"):
        E[c] = E[["permno", "yyyymm"]].merge(pm[["permno", "yyyymm", c]], on=["permno", "yyyymm"],
                                               how="left")[c].to_numpy(float)
    ibes2_at(D, E, msf, s)
    o05_at(D, E, msf)
    # NYG V10: dividends per share of the last 4 quarters (latest quarter's basis) / price at t on that basis
    dd = pd.to_datetime(E.datadate)
    ym_dd = (dd.dt.year * 100 + dd.dt.month).astype("Int64")
    cf = msf[["permno", "yyyymm", "cfpr"]]
    cf_dd = pd.DataFrame({"permno": E.permno.values, "yyyymm": ym_dd.values}).merge(
        cf, on=["permno", "yyyymm"], how="left").cfpr.to_numpy(float)
    cf_t = E[["permno", "yyyymm"]].merge(cf, on=["permno", "yyyymm"], how="left").cfpr.to_numpy(float)
    p_dd = E.prc.to_numpy(float) * np.power(cf_t / cf_dd, s)
    p_dd[~np.isfinite(p_dd) | (p_dd <= 0)] = np.nan
    E["v10"] = E.rq_dps4q.to_numpy(float) / p_dd
    # today's GICS (last co_hgic spell; PIL: 2023 structure for names coded 45102020 or group 4040 at the date)
    gi = D["gics"].copy()
    gi["gvkey"] = keynorm(gi.gvkey)
    if "indfrom" in gi and gi.indfrom.notna().any():
        gi = gi.assign(_f=pd.to_datetime(gi.indfrom)).sort_values(["gvkey", "_f"])
    gi = gi.drop_duplicates("gvkey", keep="last")
    for c in ("gsector", "ggroup", "gsubind"):
        v = gi.set_index("gvkey")[c].astype(str).str.replace(r"\.0$", "", regex=True)
        E[c + "_now"] = E.gvkey.astype(str).map(v).where(E.gvkey.notna())
    out("1.1.0 measures: FY1 found %.0f%%, FY2 %.0f%%, long-term growth %.0f%% (median %.3f), index-fund ownership "
        "%.0f%% (median %.3f), Greenblatt return on capital %.0f%%, S04* %.0f%%, dividend yield %.0f%% of eligible "
        "stock-quarters" % (100 * E.fy1.notna().mean(), 100 * E.fy2.notna().mean(), 100 * E.ltg.notna().mean(),
                            E.ltg.median(), 100 * E.o05.notna().mean(), E.o05.median(), 100 * E.rq_q02.notna().mean(),
                            100 * E.s04star.notna().mean(), 100 * E.v10.notna().mean()))
    ix = D["idx"]
    if "nmgr" in ix and len(ix):  # 1.1.1 (N5): index managers found at each quarter-end (largest count over CUSIPs)
        per = pd.to_numeric(ix.nmgr, errors="coerce").groupby(ix.rdate).max()
        out("index managers found per 13F quarter-end: median %.0f (min %.0f, max %.0f) over %d quarter-ends" % (
            per.median(), per.min(), per.max(), len(per)))
    out("I/B/E/S basis of price / estimate criteria (ZLA P1, NYG P4): %s" % E.ib_basis.iloc[0] if len(E) else "-")


# ------------------------------------------------------------------------------------------------------- recipes
def kantesaria_v1(P):
    """Kantesaria recipe v1 (RECIPE_v1.md sections 1-3): pass flags per criterion, True = the stock passes it (for an
    AVOID rule: True = not excluded). A missing measure fails its criterion. C-MED = better than the median over the
    whole eligible universe at the same quarter-end (all sectors, before the AVOID exclusions).
    Decisive: B1-B6, P1, P2, P3, A1-A5. Strict-missing variants (reported only): P1_strict (share pay missing = P1
    missing), A5_strict (acquisitions missing = C06 missing). Full form: B7-B10; B11 grid (B3, B4, B6, B7, B8 at the
    50th / 67th / 80th percentile: columns <B>_50/_67/_80); P4 grid (P4_0, P4_1, P4_2); A6 grid (A6_1, A6_2, A6_3);
    A7; A8 (narrow healthcare); A9 (A4 plus homebuilding)."""
    F = pd.DataFrame(index=P.index)

    def better(col, q, high=True):
        v = P[col]
        thr = v.groupby(P.yyyymm).transform(lambda x: x.quantile(q if high else 1 - q))
        return (v > thr) if high else (v < thr)
    sec, grp, ind, sub = P.gsector, P.ggroup, P.gind, P.gsubind
    F["B1"] = P.fy_run >= 10
    F["B2"] = P.s01 == 0
    F["B3"] = better("g01", 0.5) & better("g02", 0.5)
    F["B4"] = better("s03", 0.5, high=False)
    F["B5"] = P.g06 > 0
    F["B6"] = better("c01", 0.5, high=False)
    F["P1"] = P.p1gap > 0
    F["P2"] = P.p03 <= -0.40
    F["P3"] = P.p3rel < 0
    F["A1"] = ~sec.eq("35")
    F["A2"] = ~(grp.eq("4520") | ind.eq("151040"))
    F["A3"] = ~(sec.isin(["10", "15"]) | sub.eq("30202010"))
    F["A4"] = ~(sec.isin(["55", "60"]) | grp.isin(["4010", "4040"])
                | sub.isin(["40102010", "40201050", "40202010", "40204010"]))
    F["A5"] = P.c06 <= 0.50
    F["P1_strict"] = P.p1gap_strict > 0
    F["A5_strict"] = P.c06_strict <= 0.50
    F["B7"] = better("b7", 0.5)
    F["B8"] = better("s02", 0.5, high=False)
    F["B9"] = P.c04 < 1.0
    F["B10"] = P.mcap_co >= 2e9
    for k in (50, 67, 80):
        q = k / 100.0
        F["B3_%d" % k] = better("g01", q) & better("g02", q)
        F["B4_%d" % k] = better("s03", q, high=False)
        F["B6_%d" % k] = better("c01", q, high=False)
        F["B7_%d" % k] = better("b7", q)
        F["B8_%d" % k] = better("s02", q, high=False)
    F["P4_0"] = P.p1gap > 0
    F["P4_1"] = P.p1gap >= 0.01
    F["P4_2"] = P.p1gap >= 0.02
    for k in (1, 2, 3):
        F["A6_%d" % k] = P.b01 <= k                                  # EBITDA <= 0 or missing = excluded
    F["A7"] = P.nlines.fillna(1) <= 1
    F["A8"] = ~ind.isin(["351010", "352010", "352020"])
    F["A9"] = F.A4 & ~sub.eq("25201030")
    return F.fillna(False).astype(bool)


def kantesaria_v1_entry(F, strict=False):
    """decisive entry: B1-B6 AND P1 AND (P2 OR P3) AND none of A1-A5"""
    p1 = F.P1_strict if strict else F.P1
    a5 = F.A5_strict if strict else F.A5
    return F.B1 & F.B2 & F.B3 & F.B4 & F.B5 & F.B6 & p1 & (F.P2 | F.P3) & F.A1 & F.A2 & F.A3 & F.A4 & a5


def kantesaria_v1_full(F):
    """full form: every combination of the grids (B11 x P4 x A6 x A1/A8 x A4/A9 = 3 x 3 x 3 x 2 x 2 = 108 versions),
    each a full entry rule; statistics are computed per version and averaged"""
    cols = {}
    for g in (50, 67, 80):
        buy = (F.B1 & F.B2 & F["B3_%d" % g] & F["B4_%d" % g] & F.B5 & F["B6_%d" % g] & F["B7_%d" % g] & F["B8_%d" % g]
               & F.B9 & F.B10)
        for p in (0, 1, 2):
            price = F["P4_%d" % p] & (F.P2 | F.P3)
            for lv in (1, 2, 3):
                for hc in ("A1", "A8"):
                    for rt in ("A4", "A9"):
                        avoid = F[hc] & F.A2 & F.A3 & F[rt] & F.A5 & F["A6_%d" % lv] & F.A7
                        cols["g%d_p%d_l%d_%s_%s" % (g, p, lv, hc, rt)] = buy & price & avoid
    return pd.DataFrame(cols, index=F.index)


# ------------------------------------------------------------------------------------- 1.1.0: helpers for the recipes
def pct01(v, keys):
    """percentile inside groups, 0 = lowest, 1 = highest value (average rank of ties: (rank - 1) / (n - 1)); a group
    with one value = 0.5; missing stays missing"""
    r = v.groupby(keys).rank(method="average")
    n = v.notna().astype(float).groupby(keys).transform("sum")
    return ((r - 1) / (n - 1)).where(n > 1, 0.5).where(v.notna())


def _or(F, c):
    """flag of criterion c; 'X|Y' not stored = X OR Y"""
    if c in F:
        return F[c]
    out_ = None
    for p_ in c.split("|"):
        out_ = F[p_] if out_ is None else (out_ | F[p_])
    return out_


def kantesaria_v2(P):
    """Kantesaria recipe v2 (RECIPE_v2.md; the registered revision round after the v1 recall result, A10 item 9):
    the kantesaria_v1 flags with C2 B5 = operating margin of the latest fiscal year minus 5 fiscal years before > 0
    (B13 grid 3 / 5 / 9 years: B13_3, B13_5, B13_9) and C4 A5 = excluded only when acquisitions / operating cash flow
    > 0.50 in BOTH the latest 3-year sum and the 3-year sum before it (missing either window = fails, as v1's missing
    measure; A5_strict on the strict acquisition reading); A10 = v1's one-window A5 (full form). B4 (C1) and P2, P3
    (C3, inside P5) are full form only."""
    F = kantesaria_v1(P).copy()
    v1a5, v1a5s = F.A5.copy(), F.A5_strict.copy()
    F["B5"] = (P.g06_5 > 0).fillna(False)
    for k, c in ((3, "g06"), (5, "g06_5"), (9, "g06_9")):
        F["B13_%d" % k] = (P[c] > 0).fillna(False)
    F["A5"] = (P.c06.notna() & P.c06_prev.notna() & ~((P.c06 > 0.50) & (P.c06_prev > 0.50))).astype(bool)
    F["A5_strict"] = (P.c06_strict.notna() & P.c06_strict_prev.notna()
                      & ~((P.c06_strict > 0.50) & (P.c06_strict_prev > 0.50))).astype(bool)
    F["A10"], F["A10_strict"] = v1a5, v1a5s
    return F


def kantesaria_v2_entry(F, strict=False):
    """decisive entry: B1, B2, B3, B5 (5 years), B6 AND P1 AND none of A1-A5 (A5 on two windows)"""
    p1 = F.P1_strict if strict else F.P1
    a5 = F.A5_strict if strict else F.A5
    return F.B1 & F.B2 & F.B3 & F.B5 & F.B6 & p1 & F.A1 & F.A2 & F.A3 & F.A4 & a5


def kantesaria_v2_full(F):
    """full form: every combination of the grids, each a full entry rule, averaged: B11 (B3, B4, B6, B7, B8 at the
    50th / 67th / 80th percentile) x B13 (3 / 5 / 9 years) x P4 (gap > 0 / >= 1 / >= 2 points) x P5 (no trigger /
    P2 OR P3) x A6 (1 / 2 / 3) x A1/A8 x A4/A9 x A5/A10 = 3 x 3 x 3 x 2 x 3 x 2 x 2 x 2 = 1,296 versions; B9, B10, A7
    in every version"""
    cols = {}
    for g in (50, 67, 80):
        for w in (3, 5, 9):
            buy = (F.B1 & F.B2 & F["B3_%d" % g] & F["B4_%d" % g] & F["B13_%d" % w] & F["B6_%d" % g] & F["B7_%d" % g]
                   & F["B8_%d" % g] & F.B9 & F.B10)
            for p in (0, 1, 2):
                for trig in (0, 1):
                    price = F["P4_%d" % p] & ((F.P2 | F.P3) if trig else True)
                    for lv in (1, 2, 3):
                        for hc in ("A1", "A8"):
                            for rt in ("A4", "A9"):
                                for aq in ("A5", "A10"):
                                    avoid = F[hc] & F.A2 & F.A3 & F[rt] & F[aq] & F["A6_%d" % lv] & F.A7
                                    cols["g%d_w%d_p%d_t%d_l%d_%s_%s_%s" % (g, w, p, trig, lv, hc, rt, aq)] = \
                                        buy & price & avoid
    return pd.DataFrame(cols, index=F.index)


def druckenmiller_v1(P):
    """Druckenmiller recipe v1 (batch2/DRU/recipe/RECIPE_v1.md): branch G = B1 3-year revenue growth (TTM vs TTM 12
    quarters before, compound) >= 0.20 AND B2 1-year revenue growth >= 0.20 AND B3 P02 momentum 6-1 > 0; branch C = B4
    GICS sector 10, 15, 20 or 25 AND B5 IND_EBIT < 0 (sum of EBIT TTM over the eligible stocks of the same GICS
    industry at t, at least 3 with EBIT present). Pass = G OR C. No price criterion; A1 is a weight rule (portfolio)."""
    F = pd.DataFrame(index=P.index)
    F["B1"] = P.rq_gr3 >= 0.20
    F["B2"] = P.rq_gr1 >= 0.20
    F["B3"] = P.p02 > 0
    F["B4"] = P.gsector.isin(["10", "15", "20", "25"])
    keys = [P.yyyymm, P.gind]
    tot = P.ebit_ttm.groupby(keys).transform("sum")
    cnt = P.ebit_ttm.notna().astype(float).groupby(keys).transform("sum")
    F["B5"] = tot.where(cnt >= 3) < 0
    F = F.fillna(False).astype(bool)
    F["G"] = F.B1 & F.B2 & F.B3
    F["C"] = F.B4 & F.B5
    return F


def druckenmiller_v1_entry(F, strict=False):
    return F.G | F.C


def stahl_v1(P):
    """Stahl recipe v1 (batch2/STA/recipe/RECIPE_v1.md): B1 Q06 FCF margin TTM > 0 OR B04 net cash / market value
    >= 0; B2 C04 (diluted shares x adjustment factor now / 12 quarters before) <= 1.00; B3 O05 below the sector median
    AND C04 < 1.00; B4 E05 (FY1 estimates; none = 0, which passes) below the sector median. Pass = B1 AND B2 AND (B3 OR B4). Sector
    percentiles inside GICS sector at t among the eligible set; a missing measure fails. Full form: B3g, B4g below the
    sector percentile 0.33 / 0.50 (2 x 2 entry versions; the recipe's P1, S2, Z2g change ranking and size only)."""
    F = pd.DataFrame(index=P.index)
    keys = [P.yyyymm, P.gsector]
    F["B1"] = (P.rq_fcfm > 0) | (P.b04 >= 0)
    F["B2"] = P.rq_c04q <= 1.0
    po, pe = pct01(P.o05, keys), pct01(P.n1.fillna(0), keys)
    F["B3"] = (po < 0.5) & (P.rq_c04q < 1.0)
    none = P.n1.isna() | (P.n1 <= 0)                      # "no estimate = 0, which passes"
    F["B4"] = none | (pe < 0.5)
    for c in (33, 50):
        F["B3g_%d" % c] = (po < c / 100.0) & (P.rq_c04q < 1.0)
        F["B4g_%d" % c] = none | (pe < c / 100.0)
    F = F.fillna(False).astype(bool)
    F["B3|B4"] = F.B3 | F.B4
    return F


def stahl_v1_entry(F, strict=False):
    return F.B1 & F.B2 & (F.B3 | F.B4)


def stahl_v1_full(F):
    return pd.DataFrame({"b3_%d_b4_%d" % (a, b): F.B1 & F.B2 & (F["B3g_%d" % a] | F["B4g_%d" % b])
                         for a in (33, 50) for b in (33, 50)}, index=F.index)


HOH_A2_GRP = ["4010", "2510", "2550", "3010", "4030"]


def hohn_v1(P):
    """Hohn recipe v1 (batch2/HOH/recipe/RECIPE_v1.md): A1 not sector 25; A2 not groups 4010, 2510, 2550, 3010, 4030,
    sectors 10, 15, sub-industries 30203010, 40203010; B1 S04* = 10 of the last 10 fiscal years; B1i sub-industry
    20305010 / 20305020 AND no loss year in 10; B2 S02 in the more stable half of the sector (percentile <= 0.5, low
    = stable); P1 V13 = FCF yield TTM - 10-year Treasury >= 0 (FCF yield <= 0 fails). Pass = A1, A2, (B1 OR B1i), B2,
    P1. Full form: + B4 (S03 stable half), A3 (20302010, 50102010, industry 502010), P1g gap >= 0 / 1 / 2 points (3
    versions)."""
    F = pd.DataFrame(index=P.index)
    sec, grp, ind, sub = P.gsector, P.ggroup, P.gind, P.gsubind
    keys = [P.yyyymm, P.gsector]
    F["A1"] = ~sec.eq("25")
    F["A2"] = ~(grp.isin(HOH_A2_GRP) | sec.isin(["10", "15"]) | sub.isin(["30203010", "40203010"]))
    F["B1"] = P.s04star == 10
    F["B1i"] = sub.isin(["20305010", "20305020"]) & (P.s01 == 0)
    F["B2"] = pct01(P.s02, keys) <= 0.5
    gap = P.v04 - P.y10
    F["P1"] = (P.v04 > 0) & (gap >= 0)
    F["B4"] = pct01(P.s03, keys) <= 0.5
    F["A3"] = ~(sub.isin(["20302010", "50102010"]) | ind.eq("502010"))
    for k in (0, 1, 2):
        F["P1g_%d" % k] = (P.v04 > 0) & (gap >= k / 100.0)
    F = F.fillna(False).astype(bool)
    F["B1|B1i"] = F.B1 | F.B1i
    return F


def hohn_v1_entry(F, strict=False):
    return F.A1 & F.A2 & (F.B1 | F.B1i) & F.B2 & F.P1


def hohn_v1_full(F):
    return pd.DataFrame({"p%d" % k: F.A1 & F.A2 & F.A3 & (F.B1 | F.B1i) & F.B2 & F.B4 & F["P1g_%d" % k]
                         for k in (0, 1, 2)}, index=F.index)


ZLA_B1 = ["453010", "452010", "452020"]
ZLA_A1 = ["451030", "451020", "451010", "502030", "255020", "255030"]


def zlatev_v1(P):
    """Zlatev recipe v1 (batch2/ZLA/recipe/RECIPE_v1.md; long side): B1 GICS industry 453010, 452010, 452020; B3a gross
    margin TTM >= the median among the B1 stocks at t; B3b gross margin TTM minus 4 quarters before >= 0; B4a net debt
    / EBITDA TTM < 2.0 (EBITDA <= 0 = fail; net cash passes); B4b FCF margin TTM > 0; P1 price / FY2 consensus EPS
    <= 20 (FY2 <= 0 = fail; price on the I/B/E/S share basis); A1 not 451030, 451020, 451010, 502030, 255020, 255030.
    Full form: B1-g (+ sub-industry 45203015) x B3a-g (top 1/2, 1/3 of that B1 set) x B4a-g (< 1, < 2, < 3) x P1-g
    (<= 15, <= 20), plus A2 (E04 FY2 / FY1 - 1 >= 0; FY1 <= 0 = fail) = 24 versions."""
    F = pd.DataFrame(index=P.index)
    b1 = P.gind.isin(ZLA_B1)
    b1g = b1 | P.gsubind.eq("45203015")
    F["B1"] = b1
    F["B1g"] = b1g
    for nm_, base in (("", b1), ("g", b1g)):
        for q, tag in ((0.5, "2"), (2.0 / 3, "3")):
            thr = P.rq_gm.where(base).groupby(P.yyyymm).transform(lambda x: x.quantile(q))
            F["B3a%s_%s" % (nm_, tag)] = P.rq_gm >= thr
    F["B3a"] = F["B3a_2"]
    F["B3b"] = P.rq_dgm >= 0
    for k in (1, 2, 3):
        F["B4a_%d" % k] = P.b01 < k
    F["B4a"] = F["B4a_2"]
    F["B4b"] = P.rq_fcfm > 0
    for k in (15, 20):
        F["P1_%d" % k] = P.pfy2 <= k
    F["P1"] = F["P1_20"]
    F["A1"] = ~P.gind.isin(ZLA_A1)
    F["A2"] = P.e04 >= 0
    return F.fillna(False).astype(bool)


def zlatev_v1_entry(F, strict=False):
    return F.B1 & F.B3a & F.B3b & F.B4a & F.B4b & F.P1 & F.A1


def zlatev_v1_full(F):
    cols = {}
    for b in ("", "g"):
        for tag in ("2", "3"):
            for k in (1, 2, 3):
                for p in (15, 20):
                    cols["b1%s_t%s_l%d_p%d" % (b or "d", tag, k, p)] = (
                        F["B1" + b] & F["B3a%s_%s" % (b, tag)] & F.B3b & F["B4a_%d" % k] & F.B4b & F["P1_%d" % p]
                        & F.A1 & F.A2)
    return pd.DataFrame(cols, index=F.index)


def pil_groups(P):
    """PIL: GICS industry group on the March 2023 structure: sector 40 groups; group 4040 (pre-2016 real estate) and
    sub-industry 45102020 (pre-2023 data processing) by today's code (4040: today's group if today in sector 40, else
    not financial; 45102020: 4020 if today 40201060)"""
    grp = P.ggroup.where(P.gsector.eq("40") & ~P.ggroup.eq("4040"))
    r4040 = P.ggroup.eq("4040")
    grp = grp.where(~r4040, P.ggroup_now.where(P.gsector_now.eq("40")))
    pay = P.gsubind.eq("45102020") & P.gsubind_now.eq("40201060")
    return grp.where(~pay, "4020")


def pil_small(P, grp, fin):
    """1.1.1 (S3): eligible financials whose industry group has fewer than 10 eligible financials at t"""
    size = fin.astype(float).groupby([P.yyyymm, grp]).transform("sum")
    return fin & (size < 10)


def pil_note(P):
    grp = pil_groups(P)
    fin = grp.isin(["4010", "4020", "4030"])
    return ("comparison-group fallback (group with fewer than 10 eligible financials at t; ranked among all eligible "
            "financials): %d of %d financial stock-quarters" % (int(pil_small(P, grp, fin).sum()), int(fin.sum())))


def pilecki_v1(P):
    """Pilecki recipe v1 (batch2/PIL/recipe/RECIPE_v1.md; house exclusions do not apply): A1 financials only (pil_groups
    in 4010, 4020, 4030); comparison group = that group, or all eligible financials (sector 40) at t when fewer than 10
    eligible financials are in it at t (1.1.1, S3); B1 ROE TTM rank in the comparison group > 0.5 (missing = 0.5); B2 (groups 4010, 4030 only) tangible book per
    share now plus dividends per share of the last 12 quarters over tangible book per share 12 quarters before > 1;
    B3 P02 > 0; P1 value score (4010, 4030: mean of the in-group ranks of V02 and V07; 4020: rank of V02; missing rank
    = 0.5) ranked in the comparison group >= 0.70; A2 not a new 12-month low (missing = fail). B4 (December sleeve) is
    NOT IMPLEMENTED: it is chosen at the November month-end, after t. Full form: B1 rank > 0.5 / > 1/3 (2 versions)."""
    F = pd.DataFrame(index=P.index)
    grp = pil_groups(P)
    fin = grp.isin(["4010", "4020", "4030"])
    small = pil_small(P, grp, fin)

    def rk(v):
        """1.1.1 (S3): inside the group; rows of a group with fewer than 10 eligible financials at t are ranked among
        all eligible financials (sector 40) at t"""
        vv = v.where(fin)
        a = pct01(vv.where(~small), [P.yyyymm, grp])
        b = pct01(vv, [P.yyyymm])
        return a.where(~small, b.where(small))
    r_roe = rk(P.roe).fillna(0.5)
    bs = grp.isin(["4010", "4030"])
    score = ((rk(P.v02).fillna(0.5) + rk(P.v07).fillna(0.5)) / 2).where(bs, rk(P.v02).fillna(0.5)).where(fin)
    F["A1"] = fin
    F["B1"] = r_roe > 0.5
    F["B1_33"] = r_roe > 1.0 / 3
    F["B2"] = (P.rq_tbg > 0) | ~bs
    F["B3"] = P.p02 > 0
    F["P1"] = rk(score) >= 0.70
    F["A2"] = P.low12new == 0
    return F.fillna(False).astype(bool)


def pilecki_v1_entry(F, strict=False):
    return F.A1 & F.A2 & F.B1 & F.B2 & F.B3 & F.P1


def pilecki_v1_full(F):
    return pd.DataFrame({"b1_50": pilecki_v1_entry(F), "b1_33": F.A1 & F.A2 & F.B1_33 & F.B2 & F.B3 & F.P1},
                        index=F.index)


def ntm_eps(P):
    """NTM consensus EPS: FY1 and FY2 means weighted by the share of FY1 still ahead at t (LSEG's NTM definition);
    both needed"""
    t_end = pd.to_datetime([ym_end(int(v)) for v in P.yyyymm])
    w1 = ((pd.to_datetime(P.fpe1).values - t_end.values) / np.timedelta64(1, "D")) / 365.25
    w1 = pd.Series(np.clip(w1, 0.0, 1.0), index=P.index)
    return w1 * P.fy1b + (1 - w1) * P.fy2b  # 1.1.1 (S1): on the price's share basis


def nygren_value(P, floor=0.08, gsrc="ltg"):
    """NYG section 0: E1 = NTM consensus EPS (FY1 and FY2 means weighted by the share of FY1 still ahead at t, the
    LSEG NTM definition; both needed), g_raw = long-term growth mean (else E04; gsrc 'e04' = E04 only), g = g_raw
    clipped to [0, 10%], r = max(floor, 10-year Treasury: the 7-year is not loaded, so the 10-year stands in, flagged),
    V = sum_{t=1..7} E1 (1+g)^(t-1) / (1+r)^t + E1 (1+g)^6 / r / (1+r)^7; V missing if E1 <= 0 or g_raw missing"""
    e1 = ntm_eps(P)
    graw = P.e04 if gsrc == "e04" else P.ltg.where(P.ltg.notna(), P.e04)
    g = graw.clip(lower=0.0, upper=0.10)
    r = np.maximum(floor, P.y10)
    V = sum(e1 * (1 + g) ** (k - 1) / (1 + r) ** k for k in range(1, 8)) + e1 * (1 + g) ** 6 / r / (1 + r) ** 7
    V = V.where((e1 > 0) & graw.notna())
    return V, graw, g


def nygren_v1(P):
    """Nygren / Fitch recipe v1 (batch2/NYG/recipe/RECIPE_v1.md; house exclusions do not apply): B1 best rank (1 =
    largest) of revenue TTM, net income TTM or common equity inside the eligible set <= 250; B2 V10 (dividends per share
    of the last 4 quarters / price) + g >= 8%; P4 PV = price (I/B/E/S basis) / V < 0.70 (V: nygren_value); A1 g_raw <
    0 excluded; A2 revenue up over 12 quarters while revenue per diluted share is not up excluded (missing = fails);
    A3 V missing excluded. Full form: the decisive book and the 9 one-at-a-time books G1-G9, averaged (G1 B2 9%, G2 P4
    0.60, G3 r floor 9%, G4 growth = E04 only; G5-G9 change selling and size only, so their entry = decisive)."""
    F = pd.DataFrame(index=P.index)
    rk = [P[c].groupby(P.yyyymm).rank(ascending=False, method="min") for c in ("rq_sale_ttm", "rq_ni_ttm", "ceq")]
    F["B1"] = pd.concat(rk, axis=1).min(axis=1) <= 250
    V, graw, g = nygren_value(P)
    pv = P.px_ib / V
    F["B2"] = (P.v10 + g) >= 0.08
    F["P4"] = pv < 0.70
    F["A1"] = graw >= 0
    F["A2"] = P.rq_saleg12.notna() & P.rq_rpsg.notna() & ~((P.rq_saleg12 > 0) & (P.rq_rpsg <= 0))
    F["A3"] = V.notna()
    F["G1_B2"] = (P.v10 + g) >= 0.09
    F["G2_P4"] = pv < 0.60
    V3, _, g3 = nygren_value(P, floor=0.09)
    F["G3_B2"], F["G3_P4"], F["G3_A3"] = (P.v10 + g3) >= 0.08, (P.px_ib / V3) < 0.70, V3.notna()
    V4, gr4, g4 = nygren_value(P, gsrc="e04")
    F["G4_B2"], F["G4_P4"], F["G4_A1"], F["G4_A3"] = (P.v10 + g4) >= 0.08, (P.px_ib / V4) < 0.70, gr4 >= 0, V4.notna()
    return F.fillna(False).astype(bool)


def nygren_v1_entry(F, strict=False):
    return F.B1 & F.B2 & F.P4 & F.A1 & F.A2 & F.A3


def nygren_v1_full(F):
    d = nygren_v1_entry(F)
    cols = {"G0_decisive": d}
    cols["G1"] = F.B1 & F.G1_B2 & F.P4 & F.A1 & F.A2 & F.A3
    cols["G2"] = F.B1 & F.B2 & F.G2_P4 & F.A1 & F.A2 & F.A3
    cols["G3"] = F.B1 & F.G3_B2 & F.G3_P4 & F.A1 & F.A2 & F.G3_A3
    cols["G4"] = F.B1 & F.G4_B2 & F.G4_P4 & F.G4_A1 & F.A2 & F.G4_A3
    for k in (5, 6, 7, 8, 9):
        cols["G%d" % k] = d
    return pd.DataFrame(cols, index=F.index)


def lilu_v1(P):
    """Li Lu recipe v1 (batch2/LIL/recipe/RECIPE_v1.md): B1 Q02 (EBIT TTM / (current assets - cash - current
    liabilities + short-term debt + net PPE)) sector percentile >= 0.667; B2 the lowest month-end close of months
    t-11 .. t was set in months t-2 .. t; P1 book / price >= 1.0 OR P2 EBIT / EV sector percentile >= 0.8; A1 accruals
    in the worst fifth of the sector (reversed percentile < 0.2) excluded; A2 operating margin TTM minus the median of
    its last 20 quarters in the highest fifth of the sector (> 0.8) excluded; AVOID measure missing = not excluded.
    Full form: the central version and 9 one-at-a-time versions averaged (B1 0.5 / 0.8; B2 low set within 6 / 12
    months; P2 0.667 / 0.9; S6 1 / 2 / 5% = selling only, entry = central)."""
    F = pd.DataFrame(index=P.index)
    keys = [P.yyyymm, P.gsector]
    q02, ey = pct01(P.rq_q02, keys), pct01(P.ey, keys)
    F["B1"] = q02 >= 0.667
    F["B2"] = P.lowq == 1
    F["P1"] = P.bp >= 1.0
    F["P2"] = ey >= 0.8
    F["A1"] = ~(pct01(-P.acc, keys) < 0.2)
    F["A2"] = ~(pct01(P.rq_opmdev, keys) > 0.8)
    F["B1_50"], F["B1_80"] = q02 >= 0.5, q02 >= 0.8
    F["B2_6"], F["B2_12"] = P.low6 == 1, P.low12 == 1
    F["P2_67"], F["P2_90"] = ey >= 0.667, ey >= 0.9
    F = F.fillna(False).astype(bool)
    F["P1|P2"] = F.P1 | F.P2
    return F


def lilu_v1_entry(F, strict=False):
    return F.B1 & F.B2 & (F.P1 | F.P2) & F.A1 & F.A2


def lilu_v1_full(F):
    d = lilu_v1_entry(F)
    av = F.A1 & F.A2
    cols = {"central": d, "b1_50": F.B1_50 & F.B2 & (F.P1 | F.P2) & av, "b1_80": F.B1_80 & F.B2 & (F.P1 | F.P2) & av,
            "b2_6": F.B1 & F.B2_6 & (F.P1 | F.P2) & av, "b2_12": F.B1 & F.B2_12 & (F.P1 | F.P2) & av,
            "p2_67": F.B1 & F.B2 & (F.P1 | F.P2_67) & av, "p2_90": F.B1 & F.B2 & (F.P1 | F.P2_90) & av,
            "s6_1": d, "s6_2": d, "s6_5": d}
    return pd.DataFrame(cols, index=F.index)


def sosin_v1(P):
    """Sosin recipe v1 (batch2/SOS/recipe/RECIPE_v1.md), written but NOT measured: 13F filer 21801 is not in
    eq_conv_panel. B1 gross margin TTM above the median of its GICS industry (industry with >= 5 eligible stocks, else
    group, else sector); B2 Q01 (latest fiscal year, as hohn_v1's S04*) above the sector median, EBIT TTM > 0 only
    (loss stocks exempt); P1 EBIT / EV sector percentile >= 0.5 for EBIT TTM > 0, forward earnings yield (NTM EPS /
    price) > 0 and sector percentile >= 0.5 for loss stocks."""
    F = pd.DataFrame(index=P.index)
    prof = P.ebit_ttm > 0
    lvl = P.gind.copy()
    for c in ("ggroup", "gsector"):
        n = lvl.notna().astype(float).groupby([P.yyyymm, lvl]).transform("sum")
        lvl = lvl.where(n >= 5, P[c])
    sk = [P.yyyymm, P.gsector]
    F["B1"] = pct01(P.rq_gm, [P.yyyymm, lvl]) > 0.5
    F["B2"] = ~prof | (pct01(P.q01_ann.where(prof), sk) > 0.5)
    v03 = (ntm_eps(P) / P.px_ib).where(P.px_ib > 0)
    F["P1"] = (prof & (pct01(P.ey.where(prof), sk) >= 0.5)) | (
        ~prof & (v03 > 0) & (pct01(v03.where(~prof), sk) >= 0.5))
    return F.fillna(False).astype(bool)


def sosin_v1_entry(F, strict=False):
    return F.B1 & F.B2 & F.P1


RECIPES = {
    "kantesaria_v1": {
        "flags": kantesaria_v1, "entry": kantesaria_v1_entry, "full": kantesaria_v1_full,
        "criteria": [("B1", "10+ consecutive fiscal years of revenue and net income", ["fy_run"]),
                     ("B2", "no loss year in the last 10", ["s01"]),
                     ("B3", "revenue and EPS growth 5y above the universe median", ["g01", "g02"]),
                     ("B4", "revenue-growth s.d. 10y below the universe median", ["s03"]),
                     ("B5", "operating margin up over 3 years", ["g06"]),
                     ("B6", "capex / revenue TTM below the universe median", ["c01"]),
                     ("P1", "FCF after share pay / market value above the 10y Treasury", ["p1gap"]),
                     ("P2", "40%+ below the 12-month high", ["p03"]),
                     ("P3", "trailed the value-weighted universe over 12 months", ["p3rel"]),
                     ("P2|P3", "one of the two price triggers", ["p03", "p3rel"]),
                     ("A1", "health care (sector 35)", []),
                     ("A2", "technology hardware 4520, metals and mining 151040", []),
                     ("A3", "energy, materials, agricultural products", []),
                     ("A4", "utilities, real estate, banks, mortgage / consumer finance", []),
                     ("A5", "acquisitions > 50% of operating cash flow, 3 years", ["c06"])],
        "full_extra": [("B7", "EBIT / tangible assets above the median"), ("B8", "operating-margin s.d. 10y below the "
                       "median"), ("B9", "diluted shares fell over 3 years"), ("B10", "market value >= $2bn"),
                       ("A6_1", "net debt / EBITDA <= 1"), ("A6_2", "net debt / EBITDA <= 2"),
                       ("A6_3", "net debt / EBITDA <= 3"), ("A7", "one listed common line")],
        # 1.1.0 (layout of the v1 report kept exactly for this recipe)
        "strict": True, "universe": "house", "labels": LABELS, "v1_layout": True,
        "coverage": ["fy_run", "s01", "g01", "g02", "s03", "g06", "c01", "p1gap", "p03", "p3rel", "c06", "b7", "s02",
                     "c04", "b01"],
    },
    "kantesaria_v2": {
        "flags": kantesaria_v2, "entry": kantesaria_v2_entry, "full": kantesaria_v2_full, "strict": True,
        "universe": "house",
        "labels": ["revision after seeing recall v1: same 29 purchases, not independent evidence"] + LABELS,
        "criteria": [("B1", "10+ consecutive fiscal years of revenue and net income", ["fy_run"]),
                     ("B2", "no loss year in the last 10", ["s01"]),
                     ("B3", "revenue and EPS growth 5y above the universe median", ["g01", "g02"]),
                     ("B5", "operating margin up over 5 fiscal years (v2, C2)", ["g06_5"]),
                     ("B6", "capex / revenue TTM below the universe median", ["c01"]),
                     ("P1", "FCF after share pay / market value above the 10y Treasury", ["p1gap"]),
                     ("A1", "health care (sector 35)", []),
                     ("A2", "technology hardware 4520, metals and mining 151040", []),
                     ("A3", "energy, materials, agricultural products", []),
                     ("A4", "utilities, real estate, banks, mortgage / consumer finance", []),
                     ("A5", "acquisitions > 50% of operating cash flow in both 3-year windows (v2, C4)",
                      ["c06", "c06_prev"])],
        "full_extra": [("B4", "revenue-growth s.d. 10y below the median (v2: full form)"),
                       ("B13_3", "operating margin up over 3 years (v1 reading)"),
                       ("B13_9", "operating margin up over 9 years"),
                       ("B7", "EBIT / tangible assets above the median"), ("B8", "operating-margin s.d. 10y below the "
                       "median"), ("B9", "diluted shares fell over 3 years"), ("B10", "market value >= $2bn"),
                       ("P2|P3", "price trigger (P5 version ii = v1 reading)"),
                       ("A6_1", "net debt / EBITDA <= 1"), ("A6_2", "net debt / EBITDA <= 2"),
                       ("A6_3", "net debt / EBITDA <= 3"), ("A7", "one listed common line"),
                       ("A10", "acquisitions > 50%, latest 3-year window only (v1 reading)")],
        "coverage": ["fy_run", "s01", "g01", "g02", "g06_5", "c01", "p1gap", "c06", "c06_prev", "s03", "b7", "s02"],
    },
    "druckenmiller_v1": {
        "flags": druckenmiller_v1, "entry": druckenmiller_v1_entry, "full": None,
        "full_note": "not implemented: the recipe does not state how its eleven grid lines combine",
        "universe": "house", "no_price": True,
        "labels": ["thin", "held-out failed", "13F = equity longs only", "recipe covers 3 of 11 buy rules (decisive)"],
        "criteria": [("B1", "revenue growth 3y (TTM vs 12 quarters before) >= 20%", ["rq_gr3"]),
                     ("B2", "revenue growth 1y >= 20%", ["rq_gr1"]),
                     ("B3", "momentum 6-1 > 0", ["p02"]),
                     ("G", "branch G: B1 and B2 and B3", ["rq_gr3", "rq_gr1", "p02"]),
                     ("B4", "cyclical sector 10, 15, 20, 25", []),
                     ("B5", "industry EBIT TTM sum < 0 (>= 3 members)", []),
                     ("C", "branch C: B4 and B5", []),
                     ("G|C", "either branch", [])],
        "full_extra": [], "coverage": ["rq_gr3", "rq_gr1", "p02", "ebit_ttm"],
    },
    "stahl_v1": {
        "flags": stahl_v1, "entry": stahl_v1_entry, "full": stahl_v1_full, "universe": "house", "no_price": True,
        "labels": ["thin", "held-out failed", "recipe covers 3 of 6 buy rules (decisive), stand-ins only",
                   "13F filer firm-wide (A6: Horizon Kinetics, firm, not person)"],
        "criteria": [("B1", "FCF margin TTM > 0 or net cash >= 0", ["rq_fcfm", "b04"]),
                     ("B2", "diluted shares not up over 12 quarters", ["rq_c04q"]),
                     ("B3", "index-fund ownership below the sector median and shares down", ["o05", "rq_c04q"]),
                     ("B4", "FY1 analyst count below the sector median (none = 0)", []),
                     ("B3|B4", "one of the two neglect tests", [])],
        "full_extra": [("B3g_33", "B3 below the sector 33rd percentile"), ("B4g_33", "B4 below the 33rd percentile")],
        "coverage": ["rq_fcfm", "b04", "rq_c04q", "o05", "n1"],
    },
    "hohn_v1": {
        "flags": hohn_v1, "entry": hohn_v1_entry, "full": hohn_v1_full, "universe": "house",
        "labels": ["thin", "recipe covers 5 of 14 buy rules (decisive)"],
        "criteria": [("A1", "consumer discretionary (sector 25)", []),
                     ("A2", "banks, autos, retail, insurance, energy, materials, tobacco, asset managers", []),
                     ("B1", "Q01 > 15% in 10 of the last 10 fiscal years (S04*)", ["s04star"]),
                     ("B1i", "airports / toll roads with no loss year in 10", ["s01"]),
                     ("B1|B1i", "barrier route", ["s04star"]),
                     ("B2", "operating-margin s.d. 10y in the stable half of the sector", ["s02"]),
                     ("P1", "FCF yield TTM minus the 10y Treasury >= 0", ["v04"])],
        "full_extra": [("B4", "revenue-growth s.d. 10y in the stable half of the sector"),
                       ("A3", "airlines, wireless, media"), ("P1g_1", "FCF yield gap >= 1 point"),
                       ("P1g_2", "FCF yield gap >= 2 points")],
        "coverage": ["s04star", "s01", "s02", "v04", "s03"],
    },
    "zlatev_v1": {
        "flags": zlatev_v1, "entry": zlatev_v1_entry, "full": zlatev_v1_full, "universe": "house",
        "labels": ["thin", "long/short, longs only tested", "recipe covers 3 of 5 buy rules (decisive)"],
        "criteria": [("B1", "semis, communications equipment, tech hardware (GICS industries)", []),
                     ("B3a", "gross margin TTM >= median of the B1 stocks", ["rq_gm"]),
                     ("B3b", "gross margin TTM not below a year ago", ["rq_dgm"]),
                     ("B4a", "net debt / EBITDA TTM < 2", ["b01"]),
                     ("B4b", "FCF margin TTM > 0", ["rq_fcfm"]),
                     ("P1", "price / FY2 consensus EPS <= 20", ["pfy2"]),
                     ("A1", "software, IT services, internet", [])],
        "full_extra": [("B1g", "B1 plus electronic components"), ("B3a_3", "gross margin in the top third"),
                       ("B4a_1", "net debt / EBITDA < 1"), ("B4a_3", "net debt / EBITDA < 3"),
                       ("P1_15", "price / FY2 EPS <= 15"), ("A2", "FY2 / FY1 EPS growth >= 0")],
        "coverage": ["rq_gm", "rq_dgm", "b01", "rq_fcfm", "pfy2", "e04"],
    },
    "pilecki_v1": {
        "flags": pilecki_v1, "entry": pilecki_v1_entry, "full": pilecki_v1_full, "universe": "all", "note": pil_note,
        "not_implemented": ["B4"],
        "labels": ["thin", "financials only", "recipe covers 2 of 7 buy rules fully (decisive)",
                   "house exclusions do not apply (recipe section 0)"],
        "criteria": [("A1", "financials (GICS 2023 groups 4010, 4020, 4030)", []),
                     ("B1", "ROE TTM above the comparison-group median", ["roe"]),
                     ("B2", "tangible book per share + dividends up over 12 quarters (banks, insurers)", ["rq_tbg"]),
                     ("B3", "momentum 6-1 > 0", ["p02"]),
                     ("P1", "value score in the cheapest 30% of the comparison group", ["v02"]),
                     ("A2", "a new 12-month low (excluded)", ["low12new"])],
        "full_extra": [("B1_33", "ROE rank > 1/3")],
        "coverage": ["roe", "rq_tbg", "p02", "v02", "v07", "low12new"],
    },
    "nygren_v1": {
        "flags": nygren_v1, "entry": nygren_v1_entry, "full": nygren_v1_full, "universe": "all",
        "labels": ["thin", "recipe covers 2 of 8 buy rules fully (decisive)",
                   "13F filer firm-wide (A6: Harris Associates, firm, not person)",
                   "r uses the 10-year Treasury (7-year not loaded; recipe P2 flag)",
                   "house exclusions do not apply (recipe section 3)"],
        "criteria": [("B1", "best size rank (revenue, net income, equity) <= 250", ["rq_sale_ttm"]),
                     ("B2", "dividend yield + growth >= 8%", ["v10", "ltg"]),
                     ("P4", "price / seven-year consensus value < 0.70", ["fy1", "fy2"]),
                     ("A1", "consensus growth < 0 (excluded)", []),
                     ("A2", "size up, revenue per share not (excluded; missing = fails)", ["rq_saleg12", "rq_rpsg"]),
                     ("A3", "no value (excluded)", ["fy1", "fy2"])],
        "full_extra": [("G1_B2", "B2 at 9%"), ("G2_P4", "P4 at 0.60"), ("G3_P4", "r floor 9%"),
                       ("G4_P4", "growth = E04 only")],
        "coverage": ["rq_sale_ttm", "v10", "ltg", "e04", "fy1", "fy2", "rq_saleg12", "rq_rpsg"],
    },
    "lilu_v1": {
        "flags": lilu_v1, "entry": lilu_v1_entry, "full": lilu_v1_full, "universe": "all", "also_house": True,
        "labels": ["thin", "recipe covers 3 of 6 buy rules (decisive)", "house exclusions do not apply (recipe section "
                   "0; 1.1.1, N1)"],
        "criteria": [("B1", "Greenblatt return on capital in the sector's top third", ["rq_q02"]),
                     ("B2", "new 12-month low during the quarter", ["lowq"]),
                     ("P1", "book / price >= 1", ["bp"]),
                     ("P2", "EBIT / EV in the sector's cheapest fifth", ["ey"]),
                     ("P1|P2", "one of the two price tests", ["bp", "ey"]),
                     ("A1", "accruals in the sector's worst fifth (excluded; missing = not)", []),
                     ("A2", "margin vs own 5-year median in the sector's top fifth (excluded)", [])],
        "full_extra": [("B1_50", "return on capital top half"), ("B1_80", "top fifth"), ("B2_6", "low within 6 months"),
                       ("P2_67", "EBIT / EV cheapest third"), ("P2_90", "cheapest tenth")],
        "coverage": ["rq_q02", "lowq", "bp", "ey", "acc", "rq_opmdev"],
    },
    "sosin_v1": {
        "flags": sosin_v1, "entry": sosin_v1_entry, "full": None, "universe": "house", "measured": False,
        "labels": ["thin", "held-out failed", "no 13F profile"], "criteria": [], "full_extra": [], "coverage": [],
    },
}


# ---------------------------------------------------------------------------------------------------- statistics
def attach(X, E, cols):
    """counted purchases X (permno, t) joined to the eligible panel E: p_<c> = the stock's pass flag, b_<c> = the pass
    rate of its cell (quarter-end, sector, size third) among eligible stocks. Rows not in E are dropped."""
    rates = E.groupby("cell")[cols].mean()
    k = E[["permno", "yyyymm", "cell"] + cols].rename(columns={"yyyymm": "t"})
    k = k.rename(columns={c: "p_" + c for c in cols})
    Y = X.merge(k, on=["permno", "t"], how="inner")
    R = rates.rename(columns={c: "b_" + c for c in cols})
    Y = Y.merge(R, left_on="cell", right_index=True, how="left")
    for c in cols:
        Y["p_" + c] = Y["p_" + c].astype(float)
    return Y


def summarize(sets, cols, nboot=NBOOT, seed=SEED, min_n=MIN_N):
    """sets: {name: frame with t, p_<c>, b_<c>}. Per (set, column): n, recall = mean p, base = mean b, lift =
    recall / base. 'avg' = mean over the measurable sets (n >= min_n) and the columns. Bootstrap: quarters drawn with
    replacement from the quarters with a counted purchase in any set (the same draws for every set and column); per
    draw recall and base are recomputed on the purchases of the drawn quarters; 90% interval = 5th and 95th
    percentiles of the averaged lift over draws where it is defined."""
    qs = sorted(set().union(*[set(int(x) for x in d.t) for d in sets.values()])) if sets else []
    Q = len(qs)
    qi = {q: i for i, q in enumerate(qs)}
    per, Ld, Rd, Bd = [], [], [], []
    C = None
    if nboot and Q:
        rng = np.random.default_rng(seed)
        draws = rng.integers(0, Q, size=(nboot, Q))
        C = np.zeros((nboot, Q))
        np.add.at(C, (np.repeat(np.arange(nboot), Q), draws.ravel()), 1.0)
    for s, d in sets.items():
        n = len(d)
        if n < min_n:
            per.append(dict(set=s, col=None, n=n, recall=np.nan, base=np.nan, lift=np.nan, measurable=False))
            continue
        idx = np.array([qi[int(x)] for x in d.t])
        n_q = np.bincount(idx, minlength=Q).astype(float)
        for c in cols:
            p_q = np.bincount(idx, weights=d["p_" + c].to_numpy(float), minlength=Q)
            b_q = np.bincount(idx, weights=d["b_" + c].to_numpy(float), minlength=Q)
            P, B = p_q.sum(), b_q.sum()
            per.append(dict(set=s, col=c, n=n, recall=P / n, base=B / n, lift=P / B if B > 0 else np.nan,
                            measurable=True))
            if C is not None:
                Pd, Bdr, Nd = C @ p_q, C @ b_q, C @ n_q
                with np.errstate(divide="ignore", invalid="ignore"):
                    Ld.append(np.where(Bdr > 0, Pd / Bdr, np.nan))
                    Rd.append(np.where(Nd > 0, Pd / Nd, np.nan))
                    Bd.append(np.where(Nd > 0, Bdr / Nd, np.nan))
    ok = [r for r in per if r["measurable"]]
    res = dict(per=per, measurable=bool(ok), quarters=Q)
    if ok:
        res["recall"] = float(np.mean([r["recall"] for r in ok]))
        res["base"] = float(np.mean([r["base"] for r in ok]))
        lifts = np.array([r["lift"] for r in ok], float)
        fin = np.isfinite(lifts)
        res["lift"] = float(lifts[fin].mean()) if fin.any() else float("nan")
        res["lift_undefined"] = int((~fin).sum())      # versions whose cells never pass (base 0): left out of the mean
        res["n"] = {r["set"]: r["n"] for r in ok}
        if Ld and fin.any():
            with np.errstate(invalid="ignore"):
                L = np.vstack(Ld)[fin]
                good = np.isfinite(L).all(axis=0)
                avg = L[:, good].mean(axis=0)
            res["draws_used"] = int(good.sum())
            res["lo"] = float(np.percentile(avg, 5)) if len(avg) else float("nan")
            res["hi"] = float(np.percentile(avg, 95)) if len(avg) else float("nan")
    return res


def investor_purchases(cp, inv):
    """conviction purchases of one investor 2010-2025 (13F quarter q) with t = the quarter-end before q; per stock and
    quarter one purchase (several 13F filers of one investor pooled); version a / b as R2; a filer flagged
    quantitative book: all new positions in both versions (A10 item 9)"""
    ms = {int(x) for x in inv["mgrnos"]}
    d = cp[cp.mgrno.isin(ms)].copy()
    if inv.get("quant"):
        d["a"], d["b"] = d.new, d.new
    else:
        d["a"], d["b"] = d.conv_a, d.conv_b
    d = d[d.a | d.b]
    d = d.groupby(["yyyymm", "permno"], as_index=False).agg(a=("a", "max"), b=("b", "max"))
    d["a"], d["b"] = d.a.astype(bool), d.b.astype(bool)
    d["t"] = [ym_add(int(x), -3) for x in d.yyyymm]
    d["name"] = inv["name"]
    return d


def load_conv(load):
    cp = load("eq_conv_panel")
    for c in ("new", "add", "conv_a", "conv_b"):
        cp[c] = to_bool(cp[c])
    cp["mgrno"] = pd.to_numeric(cp.mgrno, errors="coerce").astype("Int64")
    cp["yyyymm"] = pd.to_numeric(cp.yyyymm, errors="coerce").astype(int)
    cp["permno"] = pd.to_numeric(cp.permno, errors="coerce")
    cp = cp.dropna(subset=["mgrno", "permno"])
    cp["mgrno"] = cp.mgrno.astype(int)
    cp["permno"] = cp.permno.astype(int)
    return cp[(cp.yyyymm >= Q0) & (cp.yyyymm <= Q1)]


def sets_for(P, E, cols):
    """version sets a and b (and the union, 'either') of counted purchases, attached to E"""
    out = {}
    for v in ("a", "b"):
        out[v] = attach(P[P[v]][["t", "permno"]], E, cols)
    out["either"] = attach(P[["t", "permno"]], E, cols)
    return out


def fmt(x, pct=False):
    if x is None or not np.isfinite(x):
        return "   -  "
    return ("%5.1f%%" % (100 * x)) if pct else ("%6.2f" % x)


# ------------------------------------------------------------------------------------------------------------ run
def load_inputs(load):
    D = {b: get(load, b) for b in REF_BASES}
    parts = []
    for y in range(CFG["y0"] + 1, CFG["y1"] + 1):
        try:
            parts.append(get(load, "dv_%d" % y))
        except Exception:  # noqa: BLE001
            pass
    D["dv"] = pd.concat(parts, ignore_index=True)
    D["funda"], D["fqx"], D["t10"] = load("rc_funda"), load("rc_fqx"), load("rc_t10")
    D["fqx2"], D["funda2"], D["ibes2"], D["idx"] = load("rc_fqx2"), load("rc_funda2"), load("rc_ibes2"), load("rc_idx")
    D["ibes2u"] = load("rc_ibes2u")  # 1.1.1 (S1)
    # no monthly data after the last evaluation quarter-end is read (no forward return)
    D["cf_last"] = D["msf"].sort_values("yyyymm").groupby("permno").cfpr.last()  # 1.0.1: split factor only, no return
    D["msf"] = D["msf"][pd.to_numeric(D["msf"].yyyymm) <= T1].copy()
    D["dv"] = D["dv"][pd.to_numeric(D["dv"].yyyymm) <= T1].copy()
    fq = D["fq"].copy()
    fx = D["fqx"].copy()
    fx2 = D["fqx2"].copy()
    for f_ in (fq, fx, fx2):
        f_["gvkey"] = keynorm(f_.gvkey)
        f_["datadate"] = pd.to_datetime(f_.datadate)
        for c in ("fyearq", "fqtr"):
            f_[c] = pd.to_numeric(f_[c], errors="coerce")
    fx = fx.sort_values(["gvkey", "datadate"]).drop_duplicates(["gvkey", "datadate", "fyearq", "fqtr"], keep="last")
    D["fq"] = fq.merge(fx[["gvkey", "datadate", "fyearq", "fqtr"] + [c for c in FQX_COLS if c in fx.columns]],
                       on=["gvkey", "datadate", "fyearq", "fqtr"], how="left")
    # 1.1.0: the extra quarterly and annual items, joined the same way (left joins: no row added or dropped)
    fx2 = fx2.sort_values(["gvkey", "datadate"]).drop_duplicates(["gvkey", "datadate", "fyearq", "fqtr"], keep="last")
    D["fq"] = D["fq"].merge(fx2[["gvkey", "datadate", "fyearq", "fqtr"] + [c for c in FQX2_COLS if c in fx2.columns]],
                            on=["gvkey", "datadate", "fyearq", "fqtr"], how="left")
    fa, fa2 = D["funda"].copy(), D["funda2"].copy()
    for f_ in (fa, fa2):
        f_["gvkey"] = keynorm(f_.gvkey)
        f_["datadate"] = pd.to_datetime(f_.datadate)
        f_["fyear"] = pd.to_numeric(f_.fyear, errors="coerce")
    fa2 = fa2.sort_values(["gvkey", "datadate"]).drop_duplicates(["gvkey", "datadate", "fyear"], keep="last")
    D["funda"] = fa.merge(fa2[["gvkey", "datadate", "fyear"] + [c for c in FUNDA2_COLS if c in fa2.columns]],
                          on=["gvkey", "datadate", "fyear"], how="left")
    return D


def _line(label, res):
    if not res["measurable"]:
        return "%-44s not measurable (fewer than %d counted purchases)" % (label, MIN_N)
    return "%-44s recall %s  base %s  lift %s  90%% [%s, %s]%s" % (
        label, fmt(res["recall"], True), fmt(res["base"], True), fmt(res["lift"]), fmt(res.get("lo", np.nan)),
        fmt(res.get("hi", np.nan)), ("  (%d version-sets with no passer in their cells left out of the lift)"
                                     % res["lift_undefined"]) if res.get("lift_undefined") else "") + (
        "  (interval on %d of %d draws: the others have a cell set with no passer)" % (res["draws_used"], NBOOT)
        if res.get("draws_used", NBOOT) < NBOOT else "")


def _per_set(res):
    return "; ".join("%s: n %d, recall %s, base %s, lift %s" % (r["set"], r["n"], fmt(r["recall"], True),
                                                               fmt(r["base"], True), fmt(r["lift"]))
                     for r in res["per"])


def recipe_labels(rec, name, extra=None):
    """labels printed with every result block: READING_STATUS labels, 'decisive minus <ids>', firm-wide 13F filer;
    1.1.1: run-time labels (provisional split basis)"""
    lab = list(rec.get("labels", [])) + list(extra or [])
    if rec.get("not_implemented"):
        lab.append("decisive minus %s" % ", ".join(rec["not_implemented"]))
    return lab


def evaluate(tgt, E_all, u, r, cp, out, save, r_all=None, extra=None):
    """one recipe on one investor: the section set of the eq_recall_v1 report. kantesaria_v1 keeps the v1 layout
    line for line; every other recipe repeats its labels under each section header."""
    rec = RECIPES[tgt["recipe"]]
    v1 = rec.get("v1_layout", False)
    labels = recipe_labels(rec, tgt["name"], extra)
    lab_txt = "; ".join(labels)

    def head(txt):
        out(txt)
        if not v1:
            out("labels: %s" % lab_txt)
    E = recipe_set(E_all, rec)
    F = rec["flags"](E)
    FV = rec["full"](F) if rec.get("full") else None
    fcols = list(FV.columns) if FV is not None else []
    assert not set(fcols) & {"dec", "dec_strict", "ref"}, "full-form version name clashes with a fixed column"
    add = {"dec": rec["entry"](F).values}
    if rec.get("strict"):
        add["dec_strict"] = rec["entry"](F, strict=True).values
    if FV is not None:
        add.update({c: FV[c].values for c in fcols})
    for c, _, _ in rec["criteria"]:
        add["f_" + c] = _or(F, c).values
    for c, _ in rec["full_extra"]:
        add["f_" + c] = _or(F, c).values
    E = pd.concat([E, pd.DataFrame(add, index=E.index)], axis=1)
    rr_ = r_all if (rec.get("universe") == "all" and r_all is not None) else r   # 1.1.1 (S2): the recipe's own set
    rk = rr_[["permno", "yyyymm", "sec_pct"]]
    E = E.merge(rk, on=["permno", "yyyymm"], how="left")
    E["ref"] = E.sec_pct.fillna(0) >= REF_TOP
    out("\n# %s: recipe %s (eligible stock-quarters %d%s)" % (
        tgt["name"], tgt["recipe"], len(E), "; house exclusions do not apply" if rec.get("universe") == "all" else ""))
    out("labels: %s" % lab_txt)

    # ---------------------------------------------------------------- 1. coverage and pass rates (plumbing)
    head("\n## 1. Eligible universe, measure coverage and decisive pass rate (Q4 quarter-ends; last = 2025-09)")
    mcols = rec["coverage"]
    out("t        elig  pass  rate%  ref%  " + " ".join("%6s" % c[:6] for c in mcols))
    for t in [y * 100 + 12 for y in range(T0 // 100, T1 // 100)] + [T1]:
        d = E[E.yyyymm == t]
        if not len(d):
            continue
        cov = " ".join("%6.0f" % (100 * (d[c] > 0).mean() if c == "fy_run" else 100 * d[c].notna().mean()) for c in mcols)
        out("%d  %5d %5d  %5.1f %5.1f  %s" % (t, len(d), int(d.dec.sum()), 100 * d.dec.mean(), 100 * d.ref.mean(), cov))
    out("coverage = % of eligible stocks with the measure (fy_run: with any run); rate = decisive pass rate; ref = "
        "reference-book top fifth inside sector")
    if rec.get("note"):
        out(rec["note"](E))
    if tgt["recipe"].startswith("kantesaria"):
        out("share-pay source among eligible: quarterly %.1f%%, annual %.1f%%, none (decisive: 0; strict: missing) %.1f%%; "
            "acquisitions filled as none where missing: %.1f%%" % tuple(
                [100 * (E.sbc_src == k).mean() for k in ("quarterly", "annual", "none")] + [100 * E.aqc_filled.fillna(False).astype(bool).mean()]))

    # ---------------------------------------------------------------- purchases
    inv = {"name": tgt["name"], "mgrnos": tgt["mgrnos"]}
    for i_ in INVESTORS:
        if i_["name"] == tgt["name"]:
            inv = dict(i_)
    Pk = investor_purchases(cp, inv)
    cols = ["dec"] + (["dec_strict"] if rec.get("strict") else []) + ["ref"] + fcols
    S = sets_for(Pk, E, cols)
    inu = u[u.in_univ & u.gsector.notna()][["permno", "yyyymm", "excluded"]].rename(columns={"yyyymm": "t"})
    pu = Pk.merge(inu, on=["permno", "t"], how="left")
    excl_n = int((pu.excluded == True).sum()) if rec.get("universe") != "all" else 0  # noqa: E712
    head("\n## 2. %s: conviction purchases 2010-2025 evaluated at the quarter-end before purchase" % tgt["name"])
    out("purchases: either %d (version a %d, b %d); in the eligible universe at t: either %d (a %d, b %d); in the "
        "universe but in a house-excluded industry (A8 2a, not counted): %d; not in the universe: %d" % (
            len(Pk), int(Pk.a.sum()), int(Pk.b.sum()), len(S["either"]), len(S["a"]), len(S["b"]),
            excl_n, int(pu.excluded.isna().sum())))
    if not v1 and tgt["name"] in FIRM_WIDE:
        out("13F filer is firm-wide (%s; A6): purchases are the firm's, not only this investor's" % FIRM_WIDE[tgt["name"]])
    out("quarters with a counted purchase: %d; bootstrap: %d draws of quarters, seed %d" % (
        len(set(S["either"].t)), NBOOT, SEED))
    ab = {k: S[k] for k in ("a", "b")}
    dec = summarize(ab, ["dec"])
    ref = summarize(ab, ["ref"])
    out(_line("DECISIVE (average of versions a and b)", dec))
    only = [x["set"] for x in dec["per"] if not x["measurable"]]
    if only and dec["measurable"]:
        out("   NOTE: decisive = one version only (%s not measurable: fewer than 20 purchases)" % ", ".join(only))
    out("   per version: " + _per_set(dec))
    eit = summarize({"either": S["either"]}, ["dec"])
    out(_line("decisive on 'either version' (reported)", eit))
    strict = summarize(ab, ["dec_strict"]) if rec.get("strict") else None
    if strict is not None:
        out(_line("decisive, strict missing (reported)", strict))
    if FV is not None:
        full = summarize(ab, fcols)
        out(_line("FULL FORM, %d versions averaged (reported)" % len(fcols), full))
    else:
        full = {"measurable": False}
        out("FULL FORM: %s" % rec.get("full_note", "not implemented"))
    house = None
    if rec.get("also_house"):  # 1.1.1 (N1): the same recipe on the house set, reported
        EH = recipe_set(E_all, {"universe": "house"})
        EH["dec"] = rec["entry"](rec["flags"](EH)).values
        SH = sets_for(Pk, EH, ["dec"])
        house = summarize({k: SH[k] for k in ("a", "b")}, ["dec"])
        out(_line("decisive on the house set (reported)", house))
    # baselines
    ctrl = [i for i in INVESTORS if i["group"] == "control" and i["mgrnos"]]
    Pc = pd.concat([investor_purchases(cp, i) for i in ctrl], ignore_index=True) if ctrl else Pk.iloc[0:0]
    Sc = sets_for(Pc, E, ["dec"])
    base1 = summarize({k: Sc[k] for k in ("a", "b")}, ["dec"])
    head("\n## 3. Baselines")
    out(_line("(1) recipe on pooled control purchases", base1))
    out("   per version: " + _per_set(base1))
    out(_line("(2) reference-book top fifth on this investor", ref))
    out("   per version: " + _per_set(ref))
    Ye = S["either"][["t", "permno"]].merge(E[["permno", "yyyymm", "sec_pct"]].rename(columns={"yyyymm": "t"}),
                                            on=["permno", "t"], how="left")
    noref = float(Ye.sec_pct.isna().mean()) if len(Ye) else float("nan")   # 1.1.1 (S2)
    c5_info = not (noref > 0.5)
    if not v1 or not c5_info:
        out("   counted purchases without a reference-book score: %s%s" % (
            fmt(noref, True), "" if c5_info else " (above 50%: condition c5 not informative)"))

    # ---------------------------------------------------------------- gate
    head("\n## 4. Gate (A10 item 9): decisive form")
    if rec.get("no_price"):
        out("no PRICE criterion in the decisive form: the recipe is tested as written")
    if rec.get("not_implemented"):
        out("NOT IMPLEMENTED in the decisive form: %s (evaluated without; label 'decisive minus')"
            % ", ".join(rec["not_implemented"]))
    if not dec["measurable"]:
        verdict = "NOT MEASURABLE"
        out("fewer than %d counted purchases: not measurable" % MIN_N)
    else:
        c1 = dec["lift"] >= GATE["lift"]
        c2 = dec.get("lo", np.nan) > GATE["lo"]
        c3 = dec["recall"] >= GATE["recall"]
        c4 = dec["lift"] > base1.get("lift", np.nan) if base1["measurable"] else False
        c5 = dec["lift"] > ref.get("lift", np.nan) if ref["measurable"] else False
        out("lift >= %.2f: %s; interval lower end > %.2f: %s; recall >= %.0f%%: %s; lift above control baseline: %s; "
            "lift above reference-book baseline: %s" % (GATE["lift"], "yes" if c1 else "NO", GATE["lo"],
                                                        "yes" if c2 else "NO", 100 * GATE["recall"], "yes" if c3 else "NO",
                                                        "yes" if c4 else "NO",
                                                        ("yes" if c5 else "NO") if c5_info else "not informative"))
        if c5_info:
            verdict = "PASS" if (c1 and c2 and c3 and c4 and c5) else "FAIL"
        else:  # 1.1.1 (S2): decided on the other four conditions
            verdict = ("PASS" if (c1 and c2 and c3 and c4) else "FAIL") + " (on four conditions; c5 not informative)"
    out("RECALL GATE: %s  (labels: %s)" % (verdict, lab_txt))

    # ---------------------------------------------------------------- per criterion
    head("\n## 5. Per criterion: share of the counted purchases it rejects (average of versions a and b)")
    out("criterion  rejects  of which measure missing  | universe rejects  | description")
    rows = []
    for c, desc, meas in rec["criteria"] + [(c, d, []) for c, d in rec["full_extra"]]:
        shares, missing = [], []
        for v in ("a", "b"):
            Y = S[v].merge(E[["permno", "yyyymm", "f_" + c] + meas].rename(columns={"yyyymm": "t"}),
                           on=["permno", "t"], how="left")
            if not len(Y):
                continue
            rej = ~Y["f_" + c].astype(bool)
            shares.append(rej.mean())
            missing.append((rej & Y[meas].isna().any(axis=1)).mean() if meas else 0.0)
        sh = float(np.mean(shares)) if shares else np.nan
        mi = float(np.mean(missing)) if missing else np.nan
        uni = float((~E["f_" + c]).mean())
        tag = "" if c in [x[0] for x in rec["criteria"]] else " (full form)"
        out("%-9s  %s   %s                   | %s           | %s%s" % (c, fmt(sh, True), fmt(mi, True), fmt(uni, True),
                                                                        desc, tag))
        rows.append(dict(kind="criterion", key=c, rejects=sh, missing=mi, universe=uni))
    out("(universe rejects = share of all eligible stock-quarters failing it; context only)")

    # ---------------------------------------------------------------- cross table
    head("\n## 6. Cross table: decisive recipe %s on every roster and control investor (lift, average of a and b; "
         "masked ids as in the say-do tables)" % tgt["recipe"])
    mask = mask_ids(sorted({i["name"] for i in INVESTORS}))
    cross = []
    for i_ in INVESTORS:
        if not i_["mgrnos"]:
            continue
        Pi = investor_purchases(cp, i_)
        Si = sets_for(Pi, E, ["dec"])
        ri = summarize({k: Si[k] for k in ("a", "b")}, ["dec"], nboot=0)
        cross.append((mask[i_["name"]], i_["group"], ri))
    cross.sort()
    for mid, grp, ri in cross:
        out("%s  %-7s  lift %s" % (mid, grp, fmt(ri["lift"]) if ri["measurable"] else "n < %d" % MIN_N))
        rows.append(dict(kind="cross", key=mid, lift=ri.get("lift", np.nan) if ri["measurable"] else np.nan))
    ros = [i for i in INVESTORS if i["group"] == "roster" and i["mgrnos"]]
    Pr = pd.concat([investor_purchases(cp, i) for i in ros], ignore_index=True)
    Sr = sets_for(Pr, E, ["dec"])
    rr = summarize({k: Sr[k] for k in ("a", "b")}, ["dec"], nboot=0)
    out("ROSTER pooled   lift %s" % fmt(rr.get("lift", np.nan)))
    out("CONTROL pooled  lift %s" % fmt(base1.get("lift", np.nan)))

    for nm_, res in (("decisive", dec), ("either", eit), ("strict", strict), ("full", full), ("control", base1),
                     ("reference", ref), ("house", house)):
        if res is None:
            continue
        rows.append(dict(kind="result", key=nm_, recall=res.get("recall"), base=res.get("base"), lift=res.get("lift"),
                         lo=res.get("lo"), hi=res.get("hi")))
    rows.append(dict(kind="verdict", key=verdict))
    R_ = pd.DataFrame(rows)
    R_.insert(0, "recipe", tgt["recipe"])
    keepc = ["permno", "yyyymm", "cell", "dec"] + (["dec_strict"] if rec.get("strict") else []) + ["ref"] + [
        "f_" + c for c, _, _ in rec["criteria"]]
    save("rc_pass_" + tgt["recipe"], E[keepc].copy())
    nn = dec.get("n", {}) if dec["measurable"] else {x["set"]: x["n"] for x in dec["per"]}
    summ = dict(name=tgt["name"], recipe=tgt["recipe"], n="a %s, b %s" % (nn.get("a", len(S["a"])), nn.get("b", len(S["b"]))),
                recall=dec.get("recall"), base=dec.get("base"), lift=dec.get("lift"), lo=dec.get("lo"),
                hi=dec.get("hi"), gate=verdict, labels=lab_txt)
    return R_, summ


PARTS = {1: ["kantesaria_v1", "kantesaria_v2", "druckenmiller_v1", "stahl_v1"],
         2: ["hohn_v1", "zlatev_v1", "pilecki_v1", "nygren_v1", "lilu_v1", "sosin_v1"]}  # 1.1.2: output split only


def run_part(load, save, out, part=1):
    """1.1.2: run() for the recipes of PARTS[part] only (same computation; output under the runner's per-step limit)"""
    keep = PARTS[part]
    _run(load, save, out, [t for t in TARGETS if t["recipe"] in keep], "rc_recall_summary_v11_p%d" % part)


def run(load, save, out):
    _run(load, save, out, TARGETS, "rc_recall_summary_v11")


def _run(load, save, out, targets, summary_name):
    t0 = time.time()
    out("%s  recall test (RECALL_SPEC_v1; V04_REGISTRATION A10 item 9, A13 items 13 and 21)" % VERSION)
    out("recipes in order: %s" % ", ".join(x["recipe"] for x in targets))
    miss = []
    for n in _needed() + ["eq_conv_panel"]:
        try:
            load(n)
        except Exception:  # noqa: BLE001
            if n.startswith("ref_"):
                try:
                    load("rc_" + n[4:])
                    continue
                except Exception:  # noqa: BLE001
                    pass
            miss.append(n)
    if "rc_t10" in miss:
        out("STOP: no 10-year Treasury yield stored (rc_t10); RECALL_SPEC_v1: the job stops and says so")
    if miss:
        out("PULLS INCOMPLETE (%s): nothing computed" % ", ".join(miss))
        return
    D = load_inputs(load)
    out("inputs: " + ", ".join("%s %d" % (k, len(v)) for k, v in D.items()))
    u, msf, s, src = build_panel(D, out)
    if src != "co_hgic":
        out("STOP: GICS history (comp.co_hgic) not available; RECIPE_v1 does not accept today's GICS for A1-A4")
        return
    r = rank_panel(u)
    r_all = rank_panel(u.assign(excluded=False))  # 1.1.1 (S2): reference score with the house exclusions off
    E = recall_panel(D, u, msf, s, out)
    prov = "unreadable" in D["ibes2u"].columns     # 1.1.1 (S1)
    extra = {"zlatev_v1": ["P1 provisional (split basis)"], "nygren_v1": ["P4 provisional (split basis)"]} if prov else {}
    out("panel built %.0f s" % (time.time() - t0))
    cp = load_conv(load)
    parts, summ = [], []
    for tgt in targets:
        rec = RECIPES[tgt["recipe"]]
        if not rec.get("measured", True):
            out("\n# %s: recipe %s" % (tgt["name"], tgt["recipe"]))
            out("Sosin: not in eq_conv_panel (13F filer to be added by an eq_conv input change); not measured")
            summ.append(dict(name=tgt["name"], recipe=tgt["recipe"], n="-", recall=np.nan, base=np.nan, lift=np.nan,
                             lo=np.nan, hi=np.nan, gate="NOT MEASURED", labels="; ".join(recipe_labels(rec, tgt["name"]))))
            continue
        R_, s_ = evaluate(tgt, E, u, r, cp, out, save, r_all=r_all, extra=extra.get(tgt["recipe"]))
        parts.append(R_)
        summ.append(s_)
        out("(%s done %.0f s)" % (tgt["recipe"], time.time() - t0))
    out("\n# Summary: decisive form, average of versions a and b (labels in each block above)")
    out("%-28s %-17s %-14s %7s %7s %7s  %-17s %s" % ("investor", "recipe", "n", "recall", "base", "lift", "90% interval",
                                                     "gate"))
    for x in summ:
        out("%-28s %-17s %-14s %7s %7s %7s  [%s, %s]  %s" % (
            x["name"][:28], x["recipe"], x["n"], fmt(x["recall"], True), fmt(x["base"], True), fmt(x["lift"]),
            fmt(x["lo"]), fmt(x["hi"]), x["gate"]))
    save(summary_name, pd.concat(parts, ignore_index=True) if parts else pd.DataFrame())
    out("\nstored on WRDS: rc_pass_<recipe> (pass flags per eligible stock-quarter), " + summary_name + " (the numbers "
        "above); eq_recall_v1's rc_pass_panel and rc_recall_summary are kept")
    out("done %.0f s" % (time.time() - t0))
