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
print("--- files")
for f in rep["files"]:
    print("FILE %s | %s | %d KB" % (f["file"], f["name"], f["kb"]))
print("--- sheets (status counts are per ticker field: ok / requesting / invalid / empty)")
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
              "date cells: datetime %s, serial %s, text %s, other %s | %.0fs" % (
                  s["file"], s["sheet"], "daily" if s["per"] == "D" else "monthly", s["rows"], s["blocks"], s["fields"],
                  st.get("ok", 0), st.get("requesting", 0), st.get("invalid", 0), st.get("empty", 0),
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
    print("RSHEET %s|%s -> original %s | blocks %d | fields %d | ok %d | requesting %d | invalid %d | empty %d" % (
        s["file"], s["sheet"], s.get("original", "?"), s["blocks"], s["fields"], st.get("ok", 0),
        st.get("requesting", 0), st.get("invalid", 0), st.get("empty", 0)))
if rp:
    print("--- re-pull merge per original sheet (replaced = re-pull ok, took the place of the first-pull block; "
          "kept first = re-pull failed, first pull kept; added = only in the R file; median first valid date of the "
          "sheet's ok series before -> after)")
    tot = {}
    for key in sorted(rp):
        m = rp[key]
        for k in ("repulled", "replaced", "replaced_failed_first", "added", "kept_first"):
            tot[k] = tot.get(k, 0) + m.get(k, 0)
        print("MERGE %s | re-pulled %d | replaced %d (of which first pull had failed %d) | added %d | kept first %d | "
              "median first %s -> %s | ok series %d -> %d" % (
                  key, m.get("repulled", 0), m.get("replaced", 0), m.get("replaced_failed_first", 0),
                  m.get("added", 0), m.get("kept_first", 0), m.get("median_first_before") or "-",
                  m.get("median_first_after") or "-", m.get("series_before", 0), m.get("series_after", 0)))
    print("MERGE ALL | re-pulled %d | replaced %d (of which first pull had failed %d) | added %d | kept first %d" % (
        tot["repulled"], tot["replaced"], tot["replaced_failed_first"], tot["added"], tot["kept_first"]))
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
