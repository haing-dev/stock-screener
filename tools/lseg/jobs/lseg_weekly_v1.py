"""lseg_weekly_v1: read the saved weekly LSEG live file and append it to the live store (TESTING_PROTOCOL 7.10 item 3
step 4; WORKFLOW s6 W1). It only READS the saved workbook (no Excel, no remote control); the same saved file is never
ingested twice (file hash in local\\work\\lseg\\live\\ingests.csv), so the job may be queued every week or more often.
File: env LSEG_WEEKLY, else G:\\My Drive\\Screener project\\LSEG\\10_weekly_live\\LSEG_weekly_live.xlsx.
Store: local\\work\\lseg\\live\\ (live_long.pkl append-only with ingest number and time; identity_live.csv; ingests.csv
with the table hash after each ingest). Prints METADATA ONLY: file, save time, rows added / revised per root or code,
stale series (last value older than STALE_BD business days before the save day), failed blocks, identity rows and
their agreement with the locked contract calendar (counts). No data value is printed."""
import os
import sys

sys.path[:0] = [os.path.join(os.getcwd(), "lib"), os.path.join(os.getcwd(), "pylib")]

import datetime as dt  # noqa: E402
import re  # noqa: E402
import time  # noqa: E402
import traceback  # noqa: E402
from collections import Counter  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

STALE_BD = 3            # a daily series whose last value is more than 3 business days before the save day is stale
STALE_MONTHS = 1        # a monthly series without the last completed month-end is stale
HORIZON_MONTHS = 24     # warn when the locked calendar lists fewer than 24 months of contracts beyond today

T0 = time.time()
WORK = os.environ.get("BBG_WORK", os.path.join(os.getcwd(), "work"))
PATH = os.environ.get("LSEG_WEEKLY") or r"G:\My Drive\Screener project\LSEG\10_weekly_live\LSEG_weekly_live.xlsx"
print("=== lseg_weekly_v1 ===", dt.datetime.now().strftime("%Y-%m-%d %H:%M"))
if not os.path.exists(PATH):
    print("WEEKLY FILE NOT FOUND", PATH)
    print("=== END ===")
    sys.exit(0)
try:
    import lsegdata as LD
    rep = LD.live_ingest(PATH, WORK)
except Exception as e:  # noqa: BLE001
    print("INGEST FAILED", type(e).__name__, str(e)[:300])
    print("".join(traceback.format_exc().splitlines(True)[-6:]))
    print("=== END ===")
    sys.exit(0)
print("FILE %s | saved %s | sha256 %s" % (rep["file"], rep["saved"], rep["sha256"][:16]))
if rep["already"]:
    print("ALREADY INGESTED: this saved file is in the live store; nothing added (refresh and save it again for new rows)")
    print("=== END === %.0fs" % (time.time() - T0))
    sys.exit(0)
saved = dt.datetime.strptime(rep["saved"], "%Y-%m-%d %H:%M").date()
ents = rep["entries"]
print("INGEST %d | rows added %d | rows revised %d | rows refused (dated <= seal) %d | live table rows %d | table sha256 %s"
      % (rep["ingest"], rep["log"]["rows_added"], rep["log"]["rows_revised"], rep["refused"], rep["table_rows"],
         rep["log"]["table_sha256"][:16]))
st = Counter((e["sheet"], e["status"]) for e in ents)
for sh in sorted({e["sheet"] for e in ents}):
    print("SHEET %s | %s" % (sh, " | ".join("%s %d" % (s, st[(sh, s)]) for s in LD.STATUSES if st[(sh, s)])))


def group(code):
    m = re.match(r"^<?([A-Za-z0-9@:]+?)c\d+>?$", code)
    return m.group(1) if m else code


add_g, rev_g = Counter(), Counter()
for (sid, per), n in rep["added"].items():
    add_g[group(sid.split(":", 1)[1].split("|")[0])] += n
for (sid, per), n in rep["revised"].items():
    rev_g[group(sid.split(":", 1)[1].split("|")[0])] += n
for g in sorted(set(add_g) | set(rev_g)):
    print("ROWS %s | added %d | revised %d" % (g, add_g[g], rev_g[g]))
print("--- stale or failed series")
n_stale = 0
for e in ents:
    if e["status"] != "ok":
        print("FAILED %s %s | %s|%s | %s | %s" % (e["sheet"], e["block"], e["code"], e["field"], e["status"],
                                                 e["error"][:80]))
        continue
    last = e["obs"][-1]
    if e["per"] == "D":
        lag = int(np.busday_count(np.datetime64(last, "D"), np.datetime64(saved, "D")))
        stale = lag > STALE_BD
        txt = "%d business days" % lag
    else:
        want = (pd.Timestamp(saved).to_period("M") - STALE_MONTHS).to_timestamp(how="end").date()
        stale = LD.month_end(last) < want
        txt = "last month-end %s" % LD.month_end(last).isoformat()
    if stale:
        n_stale += 1
        print("STALE %s | %s|%s | last value %s before the save day (%s)" % (e["sheet"], e["code"], e["field"], txt,
                                                                           last.isoformat()))
print("STALE series %d of %d ok" % (n_stale, sum(1 for e in ents if e["status"] == "ok")))
print("--- identity of the live positions (as LSEG states it today)")
idr = rep.get("identity_rows", [])
byf = Counter((r["field"], r["date"] is not None) for r in idr)
for f in sorted({r["field"] for r in idr}):
    print("IDENTITY %s | positions %d | with a date %d" % (f, byf[(f, True)] + byf[(f, False)], byf[(f, True)]))
calp = os.path.join(WORK, "lseg", "calendar.pkl")
if os.path.exists(calp) and idr:
    cal = pd.read_pickle(calp)
    C = LD.Calendar(cal, LD.roots_config())
    agree = dis = unk = 0
    for r in idr:
        if r["field"].upper() != "TR.EXPIRYDATE" or r["date"] is None:
            continue
        m = re.match(r"^([A-Z0-9]+?)c(\d+)$", r["ric"])
        if not m:
            continue
        h = C.held(m.group(1), int(m.group(2)), saved)
        if h is None or pd.isna(h[4]):
            unk += 1
        elif h[4].date() == r["date"]:
            agree += 1
        else:
            dis += 1
    print("IDENTITY vs locked calendar + roll rule (expiry of the held contract) | agree %d | disagree %d | calendar "
          "cannot say %d" % (agree, dis, unk))
    for root, g in cal[cal["listed"]].groupby("root"):
        ahead = (pd.Period(g["delivery"].max(), "M") - pd.Timestamp(saved).to_period("M")).n
        if ahead < HORIZON_MONTHS:
            print("CALENDAR HORIZON %s | listed contracts reach only %d months ahead: extend the L11 calendar" % (root,
                                                                                                             ahead))
else:
    print("IDENTITY no locked calendar yet (L11 not built into the store) or no identity rows")
for w in rep["warnings"]:
    print("WARN", w)
print("=== END === %.0fs" % (time.time() - T0))
