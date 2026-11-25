"""Tests of the LSEG source pieces on MOCK workbooks (invented numbers, real layouts). Run: python3 tests/test_lseg.py
Covers: formula parsing of every real pull template (repo docs/data_requests/lseg_pull_2026-11-12, read-only), the reader
statuses (ok / empty / invalid / no-dates / copy / wrong-series), future-dated rows, the 2011+ seal, the as-of guard
(market and economics delays), holdout / live refusal, untouched hiding, duplicates, the lock (reproducible, changes with
a value), the contract calendar and roll rule, the three PC jobs run as the runner runs them (cwd = local, lib/), their
export whitelist (no mock value in any job output), the L11 and weekly builders, and the weekly live ingest."""
import datetime as dt
import glob
import importlib
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CODE = os.path.join(ROOT, "code")
REPO_TEMPLATES = "/home/claude/stock-screener/docs/data_requests/lseg_pull_2026-11-12"
TMP = os.path.join(HERE, "tmp")
sys.path.insert(0, CODE)
sys.path.insert(0, HERE)

import lsegdata as LD  # noqa: E402
import make_mocks as MM  # noqa: E402
import pandas as pd  # noqa: E402

FAILS = []


def ok(cond, msg):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        FAILS.append(msg)


def run_job(local, name, env_extra):
    env = dict(os.environ, BBG_WORK=os.path.join(local, "work"), **env_extra)
    p = subprocess.run([sys.executable, os.path.join("jobs", name)], cwd=local, env=env, capture_output=True,
                       text=True, timeout=1800)
    out = p.stdout + p.stderr
    with open(os.path.join(TMP, name.replace(".py", "") + "_%d.txt" % len(glob.glob(os.path.join(
            TMP, name.replace(".py", "") + "_*.txt")))), "w") as f:
        f.write(out)
    return out


def leaks(out):
    nums = set(re.findall(r"(?<![\w.])-?\d+\.\d{4}(?!\d)", out))
    return sorted(nums & MM.VALUES)


def main():
    if os.path.isdir(TMP):
        shutil.rmtree(TMP)
    os.makedirs(TMP)
    # ------------------------------------------------------------------ 1. every real template formula parses
    import openpyxl
    n = bad = 0
    fns = {}
    for p in sorted(glob.glob(os.path.join(REPO_TEMPLATES, "*.xlsx"))):
        wb = openpyxl.load_workbook(p, read_only=True)
        for ws in wb.worksheets:
            if ws.title == "Check":
                continue
            rows = list(ws.iter_rows(min_row=1, max_row=4, values_only=True))
            if len(rows) < 4:
                continue
            for c, v in enumerate(rows[1]):
                if isinstance(v, str) and LD.PID.match(v):
                    n += 1
                    spec = LD.parse_formula(rows[3][c])
                    if spec is None or (not spec["expected"] and spec["per"] != "S"):
                        bad += 1
                    else:
                        fns[spec["fn"]] = fns.get(spec["fn"], 0) + 1
        wb.close()
    ok(n > 1500 and bad == 0, "every block formula of the %d real pull-template blocks parses (unparsed %d; %s)" % (
        n, bad, fns))
    rep0 = LD.build([REPO_TEMPLATES], os.path.join(TMP, "work_templates"))
    st0 = {e["status"] for e in rep0["entries"]}
    ok(len(rep0["files"]) == 14 and len(rep0["entries"]) > 1500 and st0 <= {"empty", "wrong-series"},
       "reader runs end to end on the 14 real (unrefreshed) L templates: %d expected series, statuses %s" % (
           len(rep0["entries"]), sorted(st0)))
    s = LD.parse_formula('formula: DSGRID("GSCITOT,GSCIEXR,GSCISPT","","1969-12-31","-0D","M","x","")')
    ok(s["expected"] == [("GSCITOT", "X"), ("GSCIEXR", "X"), ("GSCISPT", "X")], "DSGRID multi-code expected series")
    s = LD.parse_formula('formula: RDP.HistoricalPricing("CLc1","CLOSE","START:01-Jan-1970 END:12-Nov-2026 '
                         'INTERVAL:P1M SOURCE:RFV")')
    ok(s["dated"] is False, "HistoricalPricing without RH:Timestamp is recognised as undated")

    # ------------------------------------------------------------------ 2. mock pull files + build (no L11)
    pull = os.path.join(TMP, "pull_2026-11-12")
    l11dir = os.path.join(TMP, "09_contract_identity")
    os.makedirs(l11dir)
    MM.make_pull(pull)
    work = os.path.join(TMP, "work_direct")
    rep = LD.build([pull, l11dir], work)
    cat = LD.read_catalog(work)

    def st(code, field=None, file=None):
        r = cat[(cat["code"] == code) & ((cat["field"] == field) if field else True) &
                ((cat["file"] == file) if file else True)]
        return list(r["status"])
    ok(any("not read" in w and "P2_probe" in w for w in rep["warnings"]), "probe file P2 listed, not read")
    ok(st("BMUS10Y", "RY") == ["ok"] and st("BMUS10Y", "RI") == ["ok"], "DSGRID two datatypes -> two ok series")
    ok(st("BMNW30Y") == ["invalid", "invalid"], "DSGRID $$ER block -> invalid (both datatypes)")
    ok(st("FEIc1") == ["no-dates"], "HistoricalPricing without dates -> no-dates")
    ok(st("CEDCS00") == ["wrong-series"], "CEDCS00 -> wrong-series (exclusion list)")
    ok(sorted(st("GSCLTOT") + st("GSNGTOT") + st("GSGCTOT")) == ["copy"] * 3, "three codes with identical arrays -> copy")
    ok(st("GSSBTOT") == ["ok"] and st("GSKCTOT") == ["ok"], "a shared run (not whole arrays) stays ok")
    ok(st(".CESICNY") == ["empty"], "block without any output -> empty")
    ok(st("<BAXc2>") == ["invalid"], "invalid Datastream code -> invalid")
    eur = cat[(cat["code"] == "EUR=")].iloc[0]
    ok(int(eur["n_future"]) == 1 and eur["last"] == "2026-10-31", "RHistory label after the save day dropped (1 row)")
    ok(eur["date_rule"] == "calendar_me", "RHistory monthly date rule = calendar month-end labels")
    ok(cat[cat["code"] == "BMUS10Y"].iloc[0]["date_rule"] == "last_weekday", "Datastream monthly = last weekday")
    ok(cat[cat["code"] == "US10YT=RR"].iloc[0]["status"] == "ok", "RDP.Data with instrument column -> ok")
    ok(cat[cat["code"] == "TRY="].iloc[0]["untouched"] == 1, "TRY= flagged untouched")
    edl8 = cat[(cat["code"] == "<EDc1>") & (cat["per"] == "M")]
    ok(len(edl8) == 2 and (edl8["duplicate_of"] != "").sum() == 1 and edl8["series_id"].str.contains("#").sum() == 1,
       "same id in L8 and L10 -> one primary, one #suffix duplicate")
    ok(int((cat["n_hol_design"] > 0).sum()) > 0, "holiday month-ends flagged")
    design = pd.read_pickle(os.path.join(work, "lseg", "design", "long.pkl"))
    sealed = pd.read_pickle(os.path.join(work, "lseg", "sealed", "long.pkl"))
    ok(design["obs"].max() <= pd.Timestamp("2010-12-31") and sealed["obs"].min() > pd.Timestamp("2010-12-31") and
       len(sealed) > 0, "seal: design table ends 2010-12-31, sealed table holds only later observations")
    ok(len(rep["calendar"]) == 0, "no calendar without L11")

    # ------------------------------------------------------------------ 3. as-of guard, seal, holdout, live, untouched
    P = LD.Panel(work)
    v = P.asof("2005-06-30")
    s = v.series("HP:CLc1|CLOSE", "M")
    ok(s.index.max() <= pd.Timestamp("2005-06-30") and len(s) > 200, "asof 2005-06-30: no CL observation after the date")
    s = v.series("RH:EUR=|BID")
    ok(s.index.max() == pd.Timestamp("2005-06-30"), "asof month-end: RHistory label of that month known (delay 0)")
    c = v.series("DS:USCONPRCE|X")
    ok(c.index.max() == pd.Timestamp("2005-04-29"), "economics delay 45 days: May value (obs 05-31) not known on 06-30")
    k = v.known("DS:USCONPRCE|X")
    ok(k.index.max() <= pd.Timestamp("2005-06-30"), "known(): indexed by the day each value became known")
    m = LD.Panel(work).asof("2005-06-29").monthly("HP:CLc1|CLOSE", "D")
    ok(m.index.max() == pd.Timestamp("2005-06-30") and len(m) > 100, "monthly() of a daily series: month labels")
    try:
        P.asof("2011-01-03")
        ok(False, "asof after the seal refused")
    except LD.HoldoutSealed:
        ok(True, "asof after the seal refused (HoldoutSealed)")
    try:
        LD.Panel(work, holdout_key="guess")
        ok(False, "holdout key refused")
    except LD.HoldoutSealed:
        ok(True, "holdout key refused while none is registered")
    try:
        LD.Panel(work, live=True)
        ok(False, "live mode refused")
    except LD.HoldoutSealed:
        ok(True, "live mode refused while LIVE_START is not registered")
    log = open(os.path.join(work, "lseg", "sealed_access.log")).read()
    ok("refused" in log and log.count("\n") >= 3, "refused attempts logged in sealed_access.log")
    ok("RH:TRY=|BID" not in P.ids() and "RH:TRY=|BID" in LD.Panel(work, allow_untouched=True).ids(),
       "untouched TRY= hidden by default, visible with allow_untouched")
    try:
        v.series("DS:CEDCS00|X")
        ok(False, "wrong series not served")
    except KeyError:
        ok(True, "wrong series not served")

    # ------------------------------------------------------------------ 4. lock: reproducible; changes with a value
    lock1 = rep["lock_id"]
    rep2 = LD.build([pull, l11dir], work)
    ok(rep2["lock_id"] == lock1 and os.path.isdir(os.path.join(work, "lseg", "history")),
       "rebuild of the same files gives the same lock id; old manifest moved to history/")
    p = os.path.join(pull, "L2b_rates_workspace.xlsx")
    wb = openpyxl.load_workbook(p)
    ws = wb["Yield 10y"]
    ws.cell(20, 3, ws.cell(20, 3).value + 0.5)
    wb.save(p)
    t = MM.PULL.timestamp()
    os.utime(p, (t, t))
    rep3 = LD.build([pull, l11dir], work)
    ok(rep3["lock_id"] != lock1, "one changed value gives a new lock id")
    import json
    lj = json.load(open(os.path.join(work, "lseg", "lock.json")))
    ok(lj["lock_id"] == rep3["lock_id"] and "M|HP:CLc1|CLOSE" in lj["series"], "lock.json: lock id and per-series dates")

    # ------------------------------------------------------------------ 5. PC jobs before L11 (as the runner runs them)
    local = os.path.join(TMP, "local")
    os.makedirs(os.path.join(local, "lib"))
    os.makedirs(os.path.join(local, "jobs"))
    for f in ["lsegdata.py"] + list(LD.CONFIG_FILES) + ["lseg_spec_needs.csv"]:
        shutil.copy(os.path.join(CODE, f), os.path.join(local, "lib", f))
    for f in glob.glob(os.path.join(CODE, "jobs", "*.py")):
        shutil.copy(f, os.path.join(local, "jobs"))
    env = {"LSEG_DIRS": pull + ";" + l11dir}
    out = run_job(local, "lseg_build_v1.py", env)
    ok("LOCK " in out and "=== END ===" in out and "BUILD FAILED" not in out, "lseg_build_v1 runs (before L11)")
    ok("CALENDAR none" in out, "build reports no calendar before L11")
    ok(not leaks(out), "lseg_build_v1 output holds no data value (export whitelist) %s" % leaks(out)[:3])
    out = run_job(local, "lseg_check_v1.py", {})
    ok("=== END ===" in out and "LOAD FAILED" not in out and "Traceback" not in out, "lseg_check_v1 runs (before L11)")
    ok("IDENTITY VERDICT CL | NONE" in out and "contract calendar" in out and "roll rule check" in out,
       "identity before L11: NONE, says the calendar and the roll-rule check are missing")
    ok(re.search(r"NEED MISSING \| SPEC_Strip_reversion \| root:ED:1-8 D .*missing: c3", out) is not None,
       "need: Eurodollar daily contracts 3/5/6/7 reported missing")
    ok(re.search(r"NEED (OK|SHORT) \| SPEC_Card3_relative_value_risk \| DS:@:USSP500\|A12FE", out) is not None,
       "need: forward EPS found")
    ok("GAP M DS:GOLDBLN|X" in out, "gap over 2 months reported")
    ok("STALE M DS:CRUDOIL|X" in out, "stale run reported")
    ok(re.search(r"RUN M \| GSKCTOT\|X = GSSBTOT\|X", out) is not None, "identical value run shared by two codes")
    ok("COPY member" in out and "GSNGTOT" in out, "copy group members listed")
    ok("DSDATE holiday month-ends DS:<EDc1>|X" in out, "Datastream holiday month-ends reported for Eurodollar")
    ok("LABEL HP:CLc1|CLOSE" in out, "monthly vs daily label check")
    ok(not leaks(out), "lseg_check_v1 output holds no data value %s" % leaks(out)[:3])

    # ------------------------------------------------------------------ 6. L11 (contract identity) and rebuild
    _, clist = MM.make_l11(l11dir, os.path.join(TMP, "l11_template"))
    out = run_job(local, "lseg_build_v1.py", env)
    ok("FILE L11 |" in out and "CALENDAR CL |" in out, "build reads L11 and its calendar")
    ok(not leaks(out), "lseg_build_v1 output (with L11) holds no data value %s" % leaks(out)[:3])
    out = run_job(local, "lseg_check_v1.py", {})
    ok("IDENTITY VERDICT HO | COMPLETE" in out, "heating oil identity COMPLETE (calendar + depth 18 + roll rule agrees)")
    ok("IDENTITY VERDICT ED | COMPLETE" in out, "Eurodollar identity COMPLETE (quarterly strip inside positions 1-8)")
    ok(re.search(r"IDENTITY VERDICT CL \| PARTIAL .*depth", out) is not None, "WTI PARTIAL: far leg beyond the pulled depth")
    ok(re.search(r"IDENTITY ED \| calendar: .* listed months HMUZ", out) is not None, "listed months (no serial) reported")
    ok(re.search(r"IDENTITY HO \| sample contracts stored \d+ \| observations: agree \d+, disagree 0", out) is not None,
       "roll rule on HO samples: no disagreement")
    ok(re.search(r"IDENTITY VERDICT LCO \| NONE", out) is not None, "root without calendar dates or samples: NONE")
    ok(re.search(r"NEED OK \| SPEC_Strip_reversion \| root:ED:1-8 D", out) is not None,
       "Eurodollar daily 1-8 complete after L11")
    ok("PROBE Calendar test" in out and "PROBE series L11" in out, "probe blocks reported")
    ok(not leaks(out), "lseg_check_v1 output (with L11) holds no data value %s" % leaks(out)[:3])
    # calendar API directly
    lockw = os.path.join(local, "work")
    cal = pd.read_pickle(os.path.join(lockw, "lseg", "calendar.pkl"))
    C = LD.Calendar(cal, LD.roots_config(CODE))
    d = dt.date(2005, 6, 15)
    h = C.held("CL", 3, d)
    true = MM.CL.held(3, d)
    ok(h is not None and h[1] == true["deliv"] and h[2].date() == true["lt"], "Calendar.held(CL, 3, day) = true contract")
    ok(C.held("LCO", 1, d) is None, "Calendar.held without calendar dates -> None")

    # ------------------------------------------------------------------ 7. weekly live file
    wdir = os.path.join(TMP, "10_weekly_live")
    os.makedirs(wdir)
    wpath = MM.make_weekly(wdir, os.path.join(TMP, "weekly_template"))
    wenv = {"LSEG_WEEKLY": wpath}
    out = run_job(local, "lseg_weekly_v1.py", wenv)
    ok(re.search(r"INGEST 1 \| rows added [1-9]", out) is not None, "weekly ingest 1 adds rows")
    ok("STALE Curves | HOc5|CLOSE" in out, "stale weekly series reported")
    ok(re.search(r"IDENTITY vs locked calendar .* agree [1-9]\d* \| disagree 0", out) is not None,
       "live identity agrees with the locked calendar + roll rule")
    ok(not leaks(out), "lseg_weekly_v1 output holds no data value %s" % leaks(out)[:3])
    out = run_job(local, "lseg_weekly_v1.py", wenv)
    ok("ALREADY INGESTED" in out, "the same saved file is not ingested twice")
    wpath = MM.make_weekly(wdir, os.path.join(TMP, "weekly_template2"), saved=MM.WEEKLY_SAVED + dt.timedelta(days=7),
                           shift=0.01)
    out = run_job(local, "lseg_weekly_v1.py", wenv)
    ok(re.search(r"INGEST 2 \| rows added [1-9]\d* \| rows revised [1-9]", out) is not None,
       "second week: new rows added, changed values kept as revisions (append-only)")
    # live mode with LIVE_START set in-process (as the registration would)
    LD.LIVE_START = "2026-11-01"
    try:
        PL = LD.Panel(lockw, live=True)
        s = PL.asof("2026-11-27").series("HP:CLc1|CLOSE", "D")
        ok(s.index.max() > pd.Timestamp("2026-11-01") and s.index.min() < pd.Timestamp("2000-01-01"),
           "live mode: history (design + sealed) plus the weekly rows")
        ok(s.index.max() <= pd.Timestamp("2026-11-27"), "live mode: as-of guard holds")
        try:
            PL.asof("2008-01-31")
            ok(False, "live mode refuses as-of dates before LIVE_START")
        except LD.HoldoutSealed:
            ok(True, "live mode refuses as-of dates before LIVE_START")
    finally:
        LD.LIVE_START = None

    # ------------------------------------------------------------------ 8. builders
    p, rows, contracts = MM.BCP.build(os.path.join(TMP, "l11_check"))
    ed = [r for r in rows if r[1] == "ED daily"]
    ok([r[2] for r in ed] == ["Eurodollar contract %d, daily" % k for k in (3, 5, 6, 7)],
       "L11 holds Eurodollar daily contracts 3, 5, 6, 7")
    ok(len(rows) < 250 and len(contracts) < 15000, "L11 stays small (%d formulas, %d contracts)" % (len(rows),
                                                                                                    len(contracts)))
    wb = openpyxl.load_workbook(p, read_only=True)
    bad = 0
    for ws in wb.worksheets:
        if ws.title in ("Check", "Contracts", "TestContracts"):
            continue
        r = list(ws.iter_rows(min_row=1, max_row=4, values_only=True))
        for c, v in enumerate(r[1]):
            if isinstance(v, str) and v.startswith("L11-") and LD.parse_formula(r[3][c]) is None:
                bad += 1
    ok(bad == 0, "every L11 formula is readable by lsegdata")
    print("ALL LSEG TESTS PASSED" if not FAILS else "%d TEST(S) FAILED" % len(FAILS))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
