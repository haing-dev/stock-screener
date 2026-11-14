"""bbg_visit_merge_v1: copy the 13 Nov visit files (R8-R12) into the Bloomberg 'pulled results' folder on the PC, then run
the bbg_build_v2 and bbg_check_v2 code unchanged (lock v2). Metadata and counts only."""
import os, glob, shutil
_SRC = r"C:\Users\admin\Documents\WRDS results\lseg\pull_2026-11-12\bloomber 13 Nov 2026"
_DST = os.environ.get("BBG_DIR", "")
print("=== bbg_visit_merge_v1: copy ===")
if os.path.isdir(_DST):
    for _f in sorted(glob.glob(os.path.join(_SRC, "R*.xlsx"))):
        shutil.copy2(_f, os.path.join(_DST, os.path.basename(_f))); print("copied", os.path.basename(_f))
else:
    print("BBG_DIR not found; nothing copied")
"""bbg_build_v2: build the Bloomberg research tables on the PC (WORKFLOW v2.1 steps 0.2 and 0.4), now with the
re-pull workbooks R1..R7 (bbgdata 1.1.0: a re-pulled block that came back ok replaces the first-pull block).
Calls bbgdata.build(BBG_DIR, BBG_WORK): catalog, design tables (<= 2010-12-31), sealed tables (later), manifest, lock.
New against v1: per R file its sheets (with the original sheet they belong to) and block counts; per original sheet the
re-pulled / replaced / added / kept-first counts and the median first valid date before and after the re-pull.
Prints METADATA ONLY (export whitelist, tools/bbgq/README.md): file / sheet / field names, counts, shares of cell
types, date ranges of the table grids, hashes and the lock id. No data value is printed."""
import os
import sys

sys.path[:0] = [os.path.join(os.getcwd(), "lib"), os.path.join(os.getcwd(), "pylib")]

import datetime as dt  # noqa: E402
import time  # noqa: E402
import traceback  # noqa: E402

T0 = time.time()
BBG_DIR = os.environ.get("BBG_DIR", "")
WORK = os.environ.get("BBG_WORK", os.path.join(os.getcwd(), "work"))
print("=== bbg_build_v2 ===", dt.datetime.now().strftime("%Y-%m-%d %H:%M"))
print("python", sys.version.split()[0])
for m in ("numpy", "pandas", "openpyxl"):
    try:
        print("module", m, getattr(__import__(m), "__version__", "ok"))
    except Exception:  # noqa: BLE001
        print("module", m, "MISSING")
print("BBG_DIR", "ok" if os.path.isdir(BBG_DIR) else "NOT FOUND", "| BBG_WORK", "ok" if os.path.isdir(WORK) else "created")
os.makedirs(WORK, exist_ok=True)


def pct(a, n):
    return "%d%%" % round(100.0 * a / n) if n else "-"


try:
    import bbgdata
    print("bbgdata", bbgdata.VERSION, "| seal date", bbgdata.SEAL_DATE.date())
    rep = bbgdata.build(BBG_DIR, WORK)
except Exception as e:  # noqa: BLE001
    print("BUILD FAILED", type(e).__name__, str(e)[:300])
    print("".join(traceback.format_exc().splitlines(True)[-6:]))
    print("=== END === %.0fs" % (time.time() - T0))
    sys.exit(0)

man = rep["manifest"]
print("--- workbook candidates (every file found; first pull: the newest per digit; re-pull: no _CUT first, then the "
      "most ok blocks after copy detection, then the most design observations, then the newest)")
for c in rep.get("candidates", []):
    print("CANDIDATE %s | %s | _CUT %s | ok blocks %s | design observations %s | modified %s | %s" % (
        c["file"], c["name"], "yes" if c["cut"] else "no", "-" if c["ok_blocks"] is None else c["ok_blocks"],
        "-" if c["design_obs"] is None else c["design_obs"], c["mtime"], "USED" if c["used"] else "not used"))
print("--- copied blocks (identical value arrays under %d or more different tickers in one workbook: status copy, "
      "not usable)" % bbgdata.COPY_MIN_TICKERS)
cps = rep.get("copies", [])
if not cps:
    print("no copy group found")
for g in cps:
    print("COPYGROUP %s | blocks %d | different tickers %d | numbers per block %d | by sheet: %s" % (
        g["file"], g["blocks"], g["tickers"], g["values"], ", ".join("%s %d" % kv for kv in sorted(g["sheets"].items()))))
    print("   examples: " + ", ".join(g["examples"]))
cpsheet = {}
for g in cps:
    for sh, n in g["sheets"].items():
        cpsheet[(g["file"], sh)] = cpsheet.get((g["file"], sh), 0) + n
for (f, sh), n in sorted(cpsheet.items()):
    print("COPIES %s|%s | blocks %d" % (f, sh, n))
print("--- files")
for f in rep["files"]:
    print("FILE %s | %s | %d KB" % (f["file"], f["name"], f["kb"]))
print("--- sheets (status counts are per ticker field: ok / requesting / invalid / empty / copy)")
for s in rep["sheets"]:
    if s.get("skipped"):
        print("SHEET %s|%s | skipped" % (s["file"], s["sheet"]))
    elif s.get("error"):
        print("SHEET %s|%s | ERROR %s" % (s["file"], s["sheet"], s["error"]))
    else:
        st = s["status"]
        dts = s["date_types"]
        nd = sum(v for k, v in dts.items() if k != "blank")
        print("SHEET %s|%s | %s | rows %d | blocks %d | fields %d | ok %d | requesting %d | invalid %d | empty %d | "
              "copy %d | date cells: datetime %s, serial %s, text %s, other %s | %.0fs" % (
                  s["file"], s["sheet"], "daily" if s["per"] == "D" else "monthly", s["rows"], s["blocks"], s["fields"],
                  st.get("ok", 0), st.get("requesting", 0), st.get("invalid", 0), st.get("empty", 0), st.get("copy", 0),
                  pct(dts.get("datetime", 0), nd), pct(dts.get("serial", 0), nd), pct(dts.get("text date", 0), nd),
                  pct(dts.get("string", 0) + dts.get("number", 0) + dts.get("other", 0), nd), s["seconds"]))
        if s["no_ticker"]:
            print("   blocks without a ticker: %d" % s["no_ticker"])
rp = rep.get("repull") or {}
rsheets = [s for s in rep["sheets"] if str(s["file"]).startswith("R")]
print("--- re-pull workbooks (R files): %d" % len({s["file"] for s in rsheets}))
if not rsheets:
    print("no re-pull workbook found: first-pull data only")
for s in rsheets:
    if s.get("skipped") or s.get("error"):
        continue
    st = s["status"]
    print("RSHEET %s|%s -> original %s | blocks %d | fields %d | ok %d | requesting %d | invalid %d | empty %d | "
          "copy %d" % (s["file"], s["sheet"], s.get("original", "?"), s["blocks"], s["fields"], st.get("ok", 0),
                       st.get("requesting", 0), st.get("invalid", 0), st.get("empty", 0), st.get("copy", 0)))
if rp:
    print("--- re-pull merge per original sheet (replaced = re-pull ok and not shorter, took the place of the current "
          "block; kept = re-pull failed or was a copy; shorter = re-pull ok but fewer design observations, current "
          "kept; added = only in the R file; copies = first-pull copy blocks replaced / still unusable; median first "
          "valid date of the sheet's ok series before -> after)")
    keys = ("repulled", "replaced", "replaced_failed_first", "replaced_copy_first", "added", "kept_first",
            "kept_repull_copy", "shorter", "later_R_won")
    tot = dict.fromkeys(keys, 0)
    tot_c = [0, 0]
    for key in sorted(rp):
        m = rp[key]
        c = m["counts"]
        for k in keys:
            tot[k] += c.get(k, 0)
        tot_c[0] += m.get("first_copies_replaced", 0)
        tot_c[1] += m.get("first_copies_remaining", 0)
        print("MERGE %s | re-pulled %d | replaced %d (first pull had failed %d, was a copy %d) | added %d | kept %d "
              "(re-pull was a copy %d) | shorter, first kept %d | later R file won %d | first-pull copies replaced %d, "
              "remaining %d | median first %s -> %s | ok series %d -> %d" % (
                  key, c.get("repulled", 0), c.get("replaced", 0), c.get("replaced_failed_first", 0),
                  c.get("replaced_copy_first", 0), c.get("added", 0), c.get("kept_first", 0),
                  c.get("kept_repull_copy", 0), c.get("shorter", 0), c.get("later_R_won", 0),
                  m.get("first_copies_replaced", 0), m.get("first_copies_remaining", 0),
                  m.get("median_first_before") or "-", m.get("median_first_after") or "-", m.get("series_before", 0),
                  m.get("series_after", 0)))
        if m.get("shorter"):
            print("   shorter re-pulls (first pull kept): " + "; ".join(m["shorter"]))
    print("MERGE ALL | re-pulled %d | replaced %d (first pull had failed %d, was a copy %d) | added %d | kept %d "
          "(re-pull was a copy %d) | shorter, first kept %d | later R file won %d | first-pull copies replaced %d, "
          "remaining %d" % (tot["repulled"], tot["replaced"], tot["replaced_failed_first"], tot["replaced_copy_first"],
                            tot["added"], tot["kept_first"], tot["kept_repull_copy"], tot["shorter"],
                            tot["later_R_won"], tot_c[0], tot_c[1]))
print("--- cell types by field name (share of non-blank data cells: numeric / date / string)")
for f, c in rep["field_types"].items():
    n = c["numeric"] + c["date"] + c["string"]
    print("FIELD %s | cells %d | numeric %s | date %s | string %s" % (f, n, pct(c["numeric"], n), pct(c["date"], n),
                                                                       pct(c["string"], n)))
rf = rep["release_formats"]
print("release-date cell formats (%s): %s" % (bbgdata.RELEASE_FIELD, ", ".join("%s %d" % (k, v) for k, v in
                                                                          sorted(rf.items())) or "none"))
print("--- tables")
for k, t in sorted(man["tables"].items()):
    print("TABLE %s | rows %d | columns %d | grid %s to %s" % (k, t["rows"], t["columns"], t["first"] or "-",
                                                               t["last"] or "-"))
c = man["counts"]
print("--- catalog")
print("blocks %d | ticker fields %d | status %s" % (c["blocks"], c["fields"], ", ".join(
    "%s %d" % kv for kv in sorted(c["status"].items()))))
print("stored series: monthly %d, daily %d | of which duplicates kept for comparison %d" % (
    c["stored"]["M"], c["stored"]["D"], c["duplicates_stored"]))
print("stored by kind: " + ", ".join("%s %d" % kv for kv in sorted(c["kind"].items())))
print("stored by live source: " + ", ".join("%s %d" % kv for kv in sorted(c["live_source"].items())))
print("stored with a release-date rule: %d" % c["release_dated"])
print("untouched: %d tickers listed, %d found in the files, %d stored series hidden by default" % (
    c["untouched_listed"], c["untouched_tickers"], c["untouched_series"]))
print("--- hashes")
for d, w in sorted(man["workbooks"].items()):
    print("RAW %s | %s | sha256 %s | %d bytes | mtime %s" % (d, w["name"], w["sha256"], w["size"], w["mtime"]))
for k, v in sorted(man["config"].items()):
    print("CONFIG %s | sha256 %s" % (k, v))
for k, t in sorted(man["tables"].items()):
    print("TABLE %s | content sha256 %s" % (k, t["content_sha256"]))
print("CATALOG catalog.csv | sha256 %s | rows %d" % (man["catalog"]["sha256"], man["catalog"]["rows"]))
print("CODE %s | sha256 %s" % (man["code_version"], man["code_sha256"]))
for w in man["warnings"]:
    print("WARNING", w)
print("build time %s | build %.0fs" % (man["build_time"], rep["seconds"]))
print("LOCK ID", rep["lock_id"])
print("=== END === %.0fs" % (time.time() - T0))
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
