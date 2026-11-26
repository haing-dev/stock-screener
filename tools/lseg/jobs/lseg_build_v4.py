"""lseg_build_v4: build the LSEG research store on the PC (TESTING_PROTOCOL 7.10 item 3, steps 1 and 3: reader, lock,
2011+ seal). Calls lsegdata.build(dirs, BBG_WORK): catalog, design and sealed long tables, contract calendar, manifest,
LOCK and lock.json under local\\work\\lseg.
Folders read (all L*.xlsx; P probes and other files are listed, not read): env LSEG_DIRS (';'-separated), else
<Documents>\\WRDS results\\lseg\\pull_2026-11-12 and G:\\My Drive\\Screener project\\LSEG\\09_contract_identity (L11).
Prints METADATA ONLY (export whitelist, tools/bbgq/README.md): file / sheet / block names, codes, counts, date ranges,
hashes and the lock id; at the end the whole lock.json (dates, counts and hashes only). No data value is printed.
Needs in local\\lib: lsegdata.py and its five CSVs (lseg_live_sources, lseg_exclusions, lseg_untouched,
lseg_engine_map, lseg_roots)."""
import os
import sys

sys.path[:0] = [os.path.join(os.getcwd(), "lib"), os.path.join(os.getcwd(), "pylib")]

import datetime as dt  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402
import traceback  # noqa: E402
from collections import Counter  # noqa: E402

T0 = time.time()
WORK = os.environ.get("BBG_WORK", os.path.join(os.getcwd(), "work"))
print("=== lseg_build_v4 ===", dt.datetime.now().strftime("%Y-%m-%d %H:%M"))
print("python", sys.version.split()[0])
for m in ("numpy", "pandas", "openpyxl"):
    try:
        print("module", m, getattr(__import__(m), "__version__", "ok"))
    except Exception:  # noqa: BLE001
        print("module", m, "MISSING")
os.makedirs(WORK, exist_ok=True)

try:
    import lsegdata as LD
    dirs = LD.default_dirs()
    print("lsegdata", LD.VERSION, "| seal date", LD.SEAL_DATE.date(), "| work", "ok" if os.path.isdir(WORK) else "-")
    for d in dirs:
        print("DIR %s | %s" % (d, "found" if os.path.isdir(d) else "NOT FOUND"))
    rep = LD.build(dirs, WORK)
except Exception as e:  # noqa: BLE001
    print("BUILD FAILED", type(e).__name__, str(e)[:300])
    print("".join(traceback.format_exc().splitlines(True)[-8:]))
    print("=== END === %.0fs" % (time.time() - T0))
    sys.exit(0)

man = rep["manifest"]
print("--- workbooks (newest file per key is used)")
for c in rep["candidates"]:
    print("CANDIDATE %s | %s | %s" % (c["key"], c["name"], "USED" if c["used"] else "not used"))
for f in rep["files"]:
    w = man["workbooks"][f["key"]]
    print("FILE %s | %s | %d KB | saved %s | sha256 %s | expected series %d | calendar rows %d | %.0fs" % (
        f["key"], f["name"], f["kb"], f["pull_date"], w["sha256"][:16], f["entries"], f["calendar_rows"], f["seconds"]))
print("--- sheets (blocks; status counts of the expected series)")
for sh in rep["sheets"]:
    st = ", ".join("%s %d" % kv for kv in sorted(sh["status"].items()))
    print("SHEET %s|%s | rows %d | blocks %d | %s%s" % (sh["file"], sh["sheet"], sh["rows"], sh["blocks"], st or "-",
                                                     " | calendar rows %d" % sh["calendar_rows"] if sh["calendar_rows"]
                                                     else ""))
cnt = man["counts"]
print("--- status of every expected series (block x code x field)")
print("STATUS | " + " | ".join("%s %d" % (k, cnt["status"].get(k, 0)) for k in LD.STATUSES))
for k, v in cnt["status_by_file"].items():
    print("STATUS %s | %s" % (k, " | ".join("%s %d" % (s, v.get(s, 0)) for s in LD.STATUSES)))
ents = rep["entries"]
print("--- failed or excluded series (code, field, status, first error text)")
for e in ents:
    if e["status"] in ("invalid", "empty", "no-dates", "wrong-series"):
        print("FAILED %s %s %s | %s | %s|%s | %s | %s" % (e["file"], e["sheet"], e["block"], e["fn"], e["code"],
                                                       e["field"], e["status"], (e["wrong_reason"] or e["error"])[:90]))
print("--- copies (identical value arrays under %d or more different instruments: status copy)" % LD.COPY_MIN_CODES)
if not rep["copies"]:
    print("no copy group found")
for g in rep["copies"]:
    print("COPYGROUP %s | blocks %d | instruments %d | %s" % (g["per"], g["blocks"], g["instruments"],
                                                            "; ".join(g["examples"])))
print("--- rows dropped while reading (counts)")
print("DROPPED | " + " | ".join("%s %d" % kv for kv in cnt["rows_dropped"].items()))
fut = [e for e in ents if e["n_future"]]
if fut:
    print("FUTURE-DATED rows (month labels after the file's save day; dropped) in %d series, e.g. %s" % (
        len(fut), ", ".join("%s|%s" % (e["code"], e["field"]) for e in fut[:6])))
print("--- stored tables")
print("STORED series | monthly %d | daily %d | duplicates kept with #suffix %d | untouched (hidden by default) %d | "
      "mapped to an engine id %d" % (cnt["stored"]["M"], cnt["stored"]["D"], cnt["duplicates_stored"],
                                     cnt["untouched_series"], cnt["engine_mapped"]))
for k, t in man["tables"].items():
    print("TABLE %s | rows %d | series %s | %s .. %s | content sha256 %s" % (k, t["rows"], t.get("series", ""),
                                                                           t.get("first", ""), t.get("last", ""),
                                                                           t["content_sha256"][:16]))
rules = Counter(e["date_rule"] for e in ents if e["series_id"] and e["per"] == "M")
print("DATE RULE (monthly series, design dates) | " + " | ".join("%s %d" % kv for kv in sorted(rules.items())))
by_fn = Counter((e["fn"], e["date_rule"]) for e in ents if e["series_id"] and e["per"] == "M")
for (fn, r), n in sorted(by_fn.items()):
    print("DATE RULE %s | %s %d" % (fn, r or "-", n))
print("--- contract calendar")
cal = rep["calendar"]
if not len(cal):
    print("CALENDAR none (no L11 calendar rows yet): contract identity cannot be derived")
else:
    for r, g in cal.groupby("root"):
        print("CALENDAR %s | contracts %d | listed %d | delivery %s .. %s | with last trade %d | with first notice %d | "
              "with expiry %d" % (r, len(g), int(g["listed"].sum()), g["delivery"].min(), g["delivery"].max(),
                                  int(g["last_trade"].notna().sum()), int(g["first_notice"].notna().sum()),
                                  int(g["expiry"].notna().sum())))
print("--- warnings")
for w in rep["warnings"]:
    print("WARN", w)
print("--- lock")
print("CODE %s sha256 %s" % (man["code_version"], man["code_sha256"]))
for k, v in man["config"].items():
    print("CONFIG %s sha256 %s" % (k, v))
print("LOCK %s" % rep["lock_id"])
print("=== lock.json (metadata for the repo: docs/research/lseg/LOCK_LSEG_v4.json) ===")
with open(os.path.join(WORK, "lseg", "lock.json"), encoding="utf-8") as f:
    print(json.dumps(json.load(f), sort_keys=True, separators=(",", ":")))
print("=== END === %.0fs" % (time.time() - T0))
