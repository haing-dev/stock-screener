"""bbg_check_v2: data check of the Bloomberg research tables (WORKFLOW v2.1 step 0.3), after the re-pull.
Same checks as bbg_check_v1, plus: each re-pulled series that replaced a first-pull copy is compared with that copy over
their common design months (counts only: months compared, months equal within 1e-6 relative); the SERIES lines end
with the source of the row (first or R<n>).
DESIGN tables (dates <= 2010-12-31) in full: valid range and count, gaps, stale runs, robust jumps, non-positive prices,
duplicates that disagree, short series; then the must-have list. SEALED tables: structure only, from the catalog
(no sealed table is opened). Untouched markets: structure only (no value-based test).
Prints counts, flag codes, names and date ranges only (export whitelist): no data value, no per-date line."""
import os
import sys

sys.path[:0] = [os.path.join(os.getcwd(), "lib"), os.path.join(os.getcwd(), "pylib")]

import datetime as dt  # noqa: E402
import time  # noqa: E402
import traceback  # noqa: E402
from collections import Counter  # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------- thresholds (fixed before the first run)
GAP_MONTHS = 1        # BDH monthly pulls use Fill=P (carry forward), so any blank month inside the range is unexpected
GAP_DAYS = 6          # daily pulls use Fill=B: holidays are blank; up to 5 weekdays in a row (year-end) is normal
STALE_MONTHS = 6      # Fill=P repeats a dead series; quarterly data repeat 3 months, so 6 = at least one missed update
STALE_DAYS = 10       # two weeks without any change in a traded price or rate is unusual (holidays last 1-5 days)
STALE_EXEMPT_SHEETS = {"PolicyMoney"}   # policy rates stay flat for months by design
JUMP_Z = 10.0         # robust z (median / 1.4826 MAD) of a change; fat tails give 5-8, beyond 10 is mostly a bad print
JUMP_MIN_CHANGES = 24  # MAD needs enough changes to be meaningful
DUP_TOL = 1e-6        # same ticker and field pulled twice should match to rounding (relative tolerance)
DUP_SHARE = 0.01      # flag when more than 1% of the overlapping observations disagree
MIN_MONTHS = 120      # fewer than 10 design years cannot support both design eras (1975-1992, 1993-2010)
MIN_DAYS = 1250       # about 5 design years of daily data: the weekly-implementation check runs on 1990-2010
MUST_MIN_MONTHS = 60  # a must-have series needs 5 design years (60 months = the export whitelist's minimum window)
MUST_MIN_DAYS = 250
REL_LATE_DAYS = 120   # a release more than 4 months after the observation date is unusual (annual data aside)
REPULL_TOL = 1e-6     # a re-pulled value equals the first-pull value when |a - b| <= 1e-6 x max(|a|, |b|)

T0 = time.time()
WORK = os.environ.get("BBG_WORK", os.path.join(os.getcwd(), "work"))
print("=== bbg_check_v2 ===", dt.datetime.now().strftime("%Y-%m-%d %H:%M"))
try:
    import bbgdata
    import pandas as pd
    CAT, T, LOCK = bbgdata.load_design(WORK, allow_untouched=True)
except Exception as e:  # noqa: BLE001
    print("LOAD FAILED", type(e).__name__, str(e)[:300])
    print("=== END === %.0fs" % (time.time() - T0))
    sys.exit(0)
print("bbgdata", bbgdata.VERSION, "| lock id", LOCK, "| seal date", bbgdata.SEAL_DATE.date())
for per in ("M", "D"):
    df = T[per]
    print("DESIGN TABLE %s | rows %d | series %d | grid %s to %s" % (
        "monthly" if per == "M" else "daily", df.shape[0], df.shape[1],
        df.index[0].date() if len(df) else "-", df.index[-1].date() if len(df) else "-"))

STATUS_FLAG = {"requesting": "REQ", "invalid": "INV", "empty": "EMPTY", "copy": "COPY"}


def longest_run(mask):
    """Length of the longest run of True values."""
    if not mask.any():
        return 0
    m = np.concatenate([[0], mask.astype(np.int8), [0]])
    d = np.diff(m)
    return int((np.flatnonzero(d == -1) - np.flatnonzero(d == 1)).max())


def n_runs_at_least(mask, k):
    if not mask.any():
        return 0
    m = np.concatenate([[0], mask.astype(np.int8), [0]])
    d = np.diff(m)
    return int(((np.flatnonzero(d == -1) - np.flatnonzero(d == 1)) >= k).sum())


def check_series(r, s, primary):
    """-> (flags list, info dict with counts and dates). s: design Series on the table grid."""
    flags, info = [], {}
    daily = r.per == "D"
    v = s.dropna()
    n = len(v)
    info["n"] = n
    info["first"] = v.index[0].date() if n else None
    info["last"] = v.index[-1].date() if n else None
    if n == 0:
        flags.append("NODESIGN")
        return flags, info
    inside = s.loc[v.index[0]:v.index[-1]].isna().to_numpy()
    gmax = longest_run(inside)
    info["missing"] = int(inside.sum())
    info["gap_max"] = gmax
    if gmax >= (GAP_DAYS if daily else GAP_MONTHS):
        flags.append("GAP(%d)" % n_runs_at_least(inside, GAP_DAYS if daily else GAP_MONTHS))
    if n < (MIN_DAYS if daily else MIN_MONTHS):
        flags.append("SHORT")
    if r.untouched:
        flags.append("UNT")
        return flags, info                     # untouched markets: structure only
    if r.kind == "date":
        obs = v.index.values.astype("datetime64[ns]")
        rel = v.to_numpy().astype("datetime64[ns]")
        lag = (rel - obs) / np.timedelta64(1, "D")
        info["rel_before"] = int((lag < 0).sum())
        info["rel_junk"] = int((lag < -bbgdata.RELEASE_SLACK_DAYS).sum())
        info["rel_late"] = int((lag > REL_LATE_DAYS).sum())
        if info["rel_junk"]:
            flags.append("RELJUNK(%d)" % info["rel_junk"])
        if info["rel_late"]:
            flags.append("RELLATE(%d)" % info["rel_late"])
        return flags, info
    x = v.to_numpy(dtype="float64")
    if r.sheet not in STALE_EXEMPT_SHEETS:
        same = np.diff(x) == 0
        run = longest_run(same) + 1 if same.any() else 1
        if run >= (STALE_DAYS if daily else STALE_MONTHS):
            flags.append("STALE(%d)" % n_runs_at_least(same, (STALE_DAYS if daily else STALE_MONTHS) - 1))
    if r.kind == "price":
        nonpos = int((x <= 0).sum())
        if nonpos:
            flags.append("NONPOS(%d)" % nonpos)
    if r.kind in ("price", "rate"):
        if r.kind == "price":
            pos = x[x > 0]
            ch = np.diff(np.log(pos)) if len(pos) > 1 else np.array([])
        else:
            ch = np.diff(x)
        ch = ch[ch != 0]                      # carried-forward values say nothing about the size of real moves
        if len(ch) >= JUMP_MIN_CHANGES:
            med = np.median(ch)
            mad = 1.4826 * np.median(np.abs(ch - med))
            if mad > 0:
                nj = int((np.abs(ch - med) / mad > JUMP_Z).sum())
                if nj:
                    flags.append("JUMP(%d)" % nj)
    if primary is not None:
        a, b = s.align(primary, join="inner")
        both = a.notna() & b.notna()
        a, b = a[both].to_numpy(dtype="float64"), b[both].to_numpy(dtype="float64")
        info["dup_overlap"] = len(a)
        if len(a):
            bad = int((np.abs(a - b) > DUP_TOL * np.maximum(1.0, np.abs(b))).sum())
            info["dup_bad"] = bad
            if bad > DUP_SHARE * len(a):
                flags.append("DUPDIFF(%d/%d)" % (bad, len(a)))
        else:
            flags.append("DUPNOOVERLAP")
    return flags, info


# ---------------------------------------------------------------- per sheet
results = {}
try:
    order = []
    for r in CAT.itertuples():
        key = (r.file, r.sheet)
        if key not in order:
            order.append(key)
    sid_ok = {(r.per, r.series_id) for r in CAT.itertuples() if r.series_id}
    total = Counter()
    print("--- flags by sheet (codes: REQ INV EMPTY = block failed; NODESIGN = no value up to 2010; GAP GAP runs; "
          "SHORT; STALE runs; JUMP count; NONPOS count; DUPDIFF disagreeing/overlap; RELJUNK RELLATE release dates; "
          "UNT = untouched, structure only)")
    for key in order:
        rows = CAT[(CAT["file"] == key[0]) & (CAT["sheet"] == key[1])]
        cnt, flagged = Counter(), []
        for r in rows.itertuples():
            if r.status != "ok":
                fl, info = [STATUS_FLAG.get(r.status, r.status.upper())], {"n": 0}
            else:
                try:
                    prim = None
                    if r.duplicate_of and (r.per, r.duplicate_of) in sid_ok:
                        prim = T[r.per][r.duplicate_of]
                    fl, info = check_series(r, T[r.per][r.series_id], prim)
                except Exception as e:  # noqa: BLE001
                    fl, info = ["ERROR:%s" % type(e).__name__], {"n": 0}
            results[(r.file, r.sheet, r.col, r.field)] = (r, fl, info)
            cnt["series"] += 1
            if not fl or fl == ["UNT"]:
                cnt["clean"] += 1
            for f in fl:
                cnt[f.split("(")[0]] += 1
            if fl and fl != ["UNT"]:                    # untouched without a structural flag: counted, not listed
                flagged.append("%s|%s [%s]" % (r.ticker, r.field, ",".join(fl)))
        total.update(cnt)
        print("SHEET %s|%s | %s" % (key[0], key[1], ", ".join("%s %d" % kv for kv in sorted(cnt.items()))))
        for i in range(0, len(flagged), 6):
            print("   " + "; ".join(flagged[i:i + 6]))
    print("ALL SHEETS | %s" % ", ".join("%s %d" % kv for kv in sorted(total.items())))
except Exception as e:  # noqa: BLE001
    print("SHEET CHECK FAILED", type(e).__name__, str(e)[:300])
    print("".join(traceback.format_exc().splitlines(True)[-6:]))

# ---------------------------------------------------------------- release-date rule (confirms the dating convention)
try:
    rb = rj = rl = rn = 0
    for (r, fl, info) in results.values():
        if r.kind == "date" and "rel_before" in info:
            rn += info["n"]
            rb += info["rel_before"]
            rj += info["rel_junk"]
            rl += info["rel_late"]
    print("--- release dates (design): %d dated cells; before the observation date %d; more than %d days before %d "
          "(ignored, fixed delay used); more than %d days after %d" % (rn, rb, bbgdata.RELEASE_SLACK_DAYS, rj,
                                                                     REL_LATE_DAYS, rl))
except Exception as e:  # noqa: BLE001
    print("RELEASE SUMMARY FAILED", type(e).__name__)

# ---------------------------------------------------------------- re-pull: replaced series vs their first-pull copy
try:
    rf_path = os.path.join(WORK, "bbg", "design", "replaced_first.pkl")
    has_src = "source" in CAT.columns
    rep_rows = CAT[(CAT["source"] != "first") & (CAT["first_pull_status"] == "ok")] if has_src else CAT.iloc[:0]
    print("--- re-pull: replaced series vs the first-pull copy over common design months (equal = within %g "
          "relative)" % REPULL_TOL)
    if not os.path.exists(rf_path) or not len(rep_rows):
        print("no replaced series with a first-pull copy (no re-pull workbook, or nothing replaced)")
    else:
        RF = pd.read_pickle(rf_path)
        if len(RF) and RF.index.max() > bbgdata.SEAL_DATE:
            raise RuntimeError("replaced_first.pkl holds dates after the seal date")
        allc = Counter()
        diff_list = []
        for (f, sh), g in rep_rows.groupby(["file", "sheet"], sort=True):
            c = Counter()
            for r in g.itertuples():
                if r.kind == "date" or r.per != "M" or r.series_id not in RF.columns or r.series_id not in T["M"]:
                    c["not compared"] += 1
                    continue
                a, b = T["M"][r.series_id].align(RF[r.series_id], join="inner")
                both = a.notna() & b.notna()
                x, y = a[both].to_numpy(dtype="float64"), b[both].to_numpy(dtype="float64")
                n = len(x)
                eq = int((np.abs(x - y) <= REPULL_TOL * np.maximum(np.abs(x), np.abs(y))).sum()) if n else 0
                c["series"] += 1
                c["months compared"] += n
                c["months equal"] += eq
                if n == 0:
                    c["no common month"] += 1
                elif eq == n:
                    c["all equal"] += 1
                else:
                    c["some differ"] += 1
                    diff_list.append("%s|%s %s|%s (%d/%d differ)" % (f, sh, r.ticker, r.field, n - eq, n))
            allc.update(c)
            print("REPULL %s|%s | replaced series %d | compared %d | months compared %d | months equal %d | all equal "
                  "%d | some differ %d | no common month %d | not compared %d" % (
                      f, sh, len(g), c["series"], c["months compared"], c["months equal"], c["all equal"],
                      c["some differ"], c["no common month"], c["not compared"]))
        print("REPULL ALL | compared %d | months compared %d | months equal %d | all equal %d | some differ %d | "
              "no common month %d" % (allc["series"], allc["months compared"], allc["months equal"],
                                     allc["all equal"], allc["some differ"], allc["no common month"]))
        for i in range(0, len(diff_list), 4):
            print("   " + "; ".join(diff_list[i:i + 4]))
except Exception as e:  # noqa: BLE001
    print("RE-PULL COMPARISON FAILED", type(e).__name__, str(e)[:300])

# ---------------------------------------------------------------- copies and shorter re-pulls (from the catalog)
try:
    has_src = "source" in CAT.columns
    print("--- copied blocks per original sheet (status copy = identical numbers under %d+ different tickers in one "
          "workbook; counts are ticker fields: first-pull copies replaced by an ok re-pull / still unusable)" % bbgdata.COPY_MIN_TICKERS)
    rows = []
    for (f, sh), g in CAT.groupby(["file", "sheet"], sort=True):
        rem = int((g["status"] == "copy").sum())
        repl = int((g["first_pull_status"] == "copy").sum()) if has_src else 0
        kept_rcopy = int(g["repull_status"].str.contains(":copy").sum()) if has_src else 0
        if rem or repl or kept_rcopy:
            rows.append((f, sh, repl, rem, kept_rcopy))
            print("COPIES %s|%s | first-pull copies replaced %d | still copy (unusable) %d | re-pulled copies ignored %d"
                  % (f, sh, repl, rem, kept_rcopy))
    if not rows:
        print("no copied block")
    else:
        print("COPIES ALL | first-pull copies replaced %d | still copy (unusable) %d | re-pulled copies ignored %d" % (
            sum(r[2] for r in rows), sum(r[3] for r in rows), sum(r[4] for r in rows)))
    if has_src:
        sh_ = CAT[CAT["repull_status"].str.contains(":shorter")]
        print("--- shorter re-pulls (re-pull ok but fewer design observations: first pull kept): %d" % len(sh_))
        for (f, sh), g in sh_.groupby(["file", "sheet"], sort=True):
            print("SHORTER %s|%s | %d | %s" % (f, sh, len(g), "; ".join("%s|%s (%s)" % (r.ticker, r.field,
                                                                                         r.repull_status)
                                                                       for r in g.itertuples())))
except Exception as e:  # noqa: BLE001
    print("COPY / SHORTER SUMMARY FAILED", type(e).__name__, str(e)[:300])

# ---------------------------------------------------------------- per series ranges (design)
print("=== SERIES (file|sheet|ticker|field|status|first|last|design count|missing inside range|source) ===")
for (r, fl, info) in results.values():
    print("%s|%s|%s|%s|%s|%s|%s|%d|%d|%s" % (r.file, r.sheet, r.ticker, r.field, r.status, info.get("first") or "-",
                                            info.get("last") or "-", info.get("n", 0), info.get("missing", 0),
                                            getattr(r, "source", "first") or "first"))

# ---------------------------------------------------------------- must-have list
# Sources: gm/bloomberg.py (COMMOD_ER, CURVE_ROOT, EQ_INDEX, eco/surprise, breakeven, short_rate_market,
# implied_path) and gm/signals.py SURPRISE_MAP; Batch 2 plan in docs/research/global_macro/TESTING_PROTOCOL.md
# (short-rate futures ~1 year forward + spot 3m rates for US/UK/euro/Canada/Australia/Japan; commodity carry from
# 2nd/3rd/12m contracts; equity value composite; growth on first-release data; bond futures vs yield-built returns).
CORE_ER = [("WTI", "SPGSCLP", "BCOMCL"), ("Brent", "SPGSBRP", "BCOMCO"), ("natural gas", "SPGSNGP", "BCOMNG"),
           ("heating oil", "SPGSHOP", "BCOMHO"), ("gasoline", "SPGSRBP", "BCOMRB"), ("gold", "SPGSGCP", "BCOMGC"),
           ("silver", "SPGSSIP", "BCOMSI"), ("copper", "SPGSICP", "BCOMHG"), ("platinum", "SPGSPLP", None),
           ("corn", "SPGSCNP", "BCOMCN"), ("wheat", "SPGSWHP", "BCOMWH"), ("soybeans", "SPGSSOP", "BCOMSY"),
           ("sugar", "SPGSSBP", "BCOMSB"), ("coffee", "SPGSKCP", "BCOMKC"), ("cotton", "SPGSCTP", "BCOMCT"),
           ("live cattle", "SPGSLCP", "BCOMLC")]
CURVES = [("WTI", "CL", "CL13"), ("Brent", "CO", "CO13"), ("natural gas", "NG", "NG13"), ("heating oil", "HO", "HO13"),
          ("gasoline", "XB", "XB13"), ("gold", "GC", "GC7"), ("silver", "SI", "SI6"), ("copper", "HG", "HG13"),
          ("platinum", "PL", "PL5"), ("corn", "C ", "C 6"), ("wheat", "W ", "W 6"), ("soybeans", "S ", "S 8"),
          ("sugar", "SB", "SB5"), ("coffee", "KC", "KC6"), ("cotton", "CT", "CT6"), ("live cattle", "LC", "LC7")]
MSCI = ["MXUS", "MXJP", "MXGB", "MXDE", "MXFR", "MXCA", "MXAU", "MXHK", "MXCN", "MXKR", "MXTW", "MXIN", "MXBR",
        "MXMX", "MXZA", "MXEM"]
ECO = ["NAPMPMI", "NFP TCH", "USURTOT", "IP CHNG", "RSTAMOM", "MPMIEZMA", "GRIFPBUS", "GRIPIYOY", "GRUEPR", "MPMIGBMA",
       "UKIPIYOY", "UKUEILOR", "JNTSMFG", "JNIPYOY", "JNUE", "CANLXEMR", "AULFUNEM", "CPMINDX", "CHVAIOY"]
EQTR = ["SPX", "NDX", "RTY", "SX5E", "DAX", "UKX", "CAC", "NKY", "SPTSX", "AS51", "HSI", "SHSZ300", "KOSPI", "TWSE",
        "SENSEX", "IBOV", "MEXBOL", "TOP40"]
ALT_ER = [("cocoa", "SPGSCCP", None), ("lean hogs", "SPGSLHP", "BCOMLH"), ("feeder cattle", "SPGSFCP", None),
          ("KC wheat", "SPGSKWP", "BCOMKW"), ("soybean meal", None, "BCOMSM"), ("soybean oil", None, "BCOMBO"),
          ("aluminium", "SPGSIAP", "BCOMAL"), ("zinc", "SPGSIZP", "BCOMZS"), ("nickel", "SPGSIKP", "BCOMNI"),
          ("lead", "SPGSILP", None), ("gasoil", "SPGSGOP", None)]
PX = "PX_LAST"
MUST = []   # (group, [(ticker, field), ...] alternatives, per)
for n, g, b in CORE_ER:
    MUST.append(("commodity ER %s" % n, [(t + " Index", PX) for t in (g, b) if t], "M"))
for n, root, far in CURVES:
    MUST.append(("curve %s 1st" % n, [(root + "1 Comdty", PX)], "M"))
    MUST.append(("curve %s 2nd" % n, [(root + "2 Comdty", PX)], "M"))
    MUST.append(("curve %s ~12m" % n, [(far + " Comdty", PX), (root + "12 Comdty", PX)], "M"))
for n, alts in [("US", ["ED4", "SFR4"]), ("UK", ["L 4", "SFI4"]), ("euro", ["ER4"]), ("Canada", ["BA4"]),
                ("Australia", ["IR4"]), ("Japan", ["YE4"])]:
    MUST.append(("short-rate future ~1y %s" % n, [(a + " Comdty", PX) for a in alts], "M"))
MUST.append(("short-rate future front US", [("ED1 Comdty", PX), ("SFR1 Comdty", PX)], "M"))
for n, alts in [("US", ["USGG3M"]), ("UK", ["BP0003M", "SONIO/N"]), ("euro", ["EUR003M"]), ("Canada", ["CDOR03", "CAONREPO"]),
                ("Australia", ["BBSW3M"]), ("Japan", ["TI0003M"])]:
    MUST.append(("spot 3m rate %s" % n, [(a + " Index", PX) for a in alts], "M"))
for n, y2, y10 in [("US", "USGG2YR", "USGG10YR"), ("Germany", "GDBR2", "GDBR10"), ("UK", "GUKG2", "GUKG10"),
                   ("Japan", "GJGB2", "GJGB10"), ("Canada", "GCAN2YR", "GCAN10YR"), ("Australia", "GACGB2", "GACGB10")]:
    MUST.append(("yield 2y %s" % n, [(y2 + " Index", PX)], "M"))
    MUST.append(("yield 10y %s" % n, [(y10 + " Index", PX)], "M"))
for t in MSCI:
    MUST.append(("valuation P/E %s" % t, [(t + " Index", "BEST_PE_RATIO"), (t + " Index", "PE_RATIO")], "M"))
    MUST.append(("valuation P/B %s" % t, [(t + " Index", "PX_TO_BOOK_RATIO")], "M"))
    MUST.append(("valuation D/P %s" % t, [(t + " Index", "EQY_DVD_YLD_12M")], "M"))
    MUST.append(("forward EPS %s" % t, [(t + " Index", "BEST_EPS")], "M"))
for t in ECO:
    for f in ("ACTUAL_RELEASE", "BN_SURVEY_MEDIAN", "ECO_RELEASE_DT"):
        MUST.append(("first release %s %s" % (t, f), [(t + " Index", f)], "M"))
for t in ("CESIUSD", "CESIEUR", "CESIGBP", "CESIJPY", "CESICAD", "CESIAUD", "CESICNY", "CESIG10", "CESIEM"):
    MUST.append(("surprise index %s" % t, [(t + " Index", PX)], "M"))
for t in ("USGGBE10", "DEGGBE10", "UKGGBE10"):
    MUST.append(("breakeven %s" % t, [(t + " Index", PX)], "M"))
for r in ("TU", "FV", "TY", "US", "RX", "G ", "JB", "CN", "XM"):
    MUST.append(("bond future %s1" % r.strip(), [(r + "1 Comdty", PX)], "M"))
for t in EQTR:
    alts = [(t + " Index", "TOT_RETURN_INDEX_GROSS_DVDS")] + ([(t + " Index", PX)] if t in ("DAX", "IBOV") else [])
    MUST.append(("equity TR %s" % t, alts, "M"))
for n, g, b in ALT_ER:
    MUST.append(("untouched alt commodity ER %s" % n, [(t + " Index", PX) for t in (g, b) if t], "M"))

try:
    idx = {}
    for r in CAT.itertuples():
        idx.setdefault((r.per, r.ticker, r.field), []).append(r)
    ok_groups, bad = 0, []
    print("--- must-have (usable = read ok with at least %d design months / %d design days)" % (MUST_MIN_MONTHS,
                                                                                               MUST_MIN_DAYS))
    for name, alts, per in MUST:
        best, line = None, None
        for tk, f in alts:
            for r in idx.get((per, tk, f), []):
                res = results.get((r.file, r.sheet, r.col, r.field))
                n = res[2].get("n", 0) if res else 0
                if best is None or (r.status == "ok", n) > best[0]:
                    best = ((r.status == "ok", n), r, n)
        if best is None:
            line = "MISSING (not in any file)"
        else:
            _, r, n = best
            need = MUST_MIN_DAYS if per == "D" else MUST_MIN_MONTHS
            where = "%s|%s|%s|%s" % (r.file, r.sheet, r.ticker, r.field)
            if r.status == "ok" and n >= need:
                line = "ok via %s (design count %d%s)" % (where, n, ", untouched: structure only" if r.untouched else "")
                ok_groups += 1
            else:
                line = "NOT USABLE via %s (status %s, design count %d)" % (where, r.status, n)
        if not line.startswith("ok"):
            bad.append(name)
        print("MUST %s | %s" % (name, line))
    print("MUST SUMMARY | groups %d | usable %d | not usable %d" % (len(MUST), ok_groups, len(bad)))
    if bad:
        print("MUST NOT USABLE: " + "; ".join(bad))
except Exception as e:  # noqa: BLE001
    print("MUST-HAVE CHECK FAILED", type(e).__name__, str(e)[:300])

# ---------------------------------------------------------------- sealed: structure only (from the catalog)
try:
    man = bbgdata.Panel(WORK, allow_untouched=True).manifest
    print("--- sealed tables (structure only; not opened)")
    for k in ("sealed/monthly.pkl", "sealed/daily.pkl"):
        t = man["tables"][k]
        print("SEALED TABLE %s | rows %d | columns %d | grid %s to %s" % (k, t["rows"], t["columns"], t["first"] or "-",
                                                                         t["last"] or "-"))
    st = CAT[CAT["series_id"] != ""]
    for (f, s), g in st.groupby(["file", "sheet"], sort=False):
        after = g[g["n_sealed"] > 0]
        print("SEALED %s|%s | series %d | with any value after 2010: %d | last date %s" % (
            f, s, len(g), len(after), max(after["last"]) if len(after) else "-"))
except Exception as e:  # noqa: BLE001
    print("SEALED STRUCTURE FAILED", type(e).__name__, str(e)[:300])
print("=== END === %.0fs" % (time.time() - T0))
