"""gm_a2_v1: Batch A2, version grids, hygiene H1-H4 (TESTING_PROTOCOL 7.6 step 3, 7.7; gm/CHANGES.md "A2", 2026-11-27)
on the PC.

1. Checks (else STOP before any Bloomberg value is read): gm code = the reference's (lib\\engine_ref.json); lib files
   a2_batch.py, a1_panel.py, gm_engine.py, bbg_panel.py, bbgdata.py = the registered sha256 (LIB_SHA below);
   lib\\gm\\trials.csv = the registered trial log (selection inflation, CHANGES A2 item 4l); Bloomberg store lock id =
   LOCK_v2 d85a46cb2853646b24796f294f3ccab1d1507188c402e978fd59f5196ea41fc9; free inputs = the shipped zip (work\\free).
2. Free arm vs engine_ref.json (signal sums, market months). Then the A1 panel is rebuilt (a1_panel-1.1.0: evaluate +
   build, all blocks), extension-only asserted, its id checked against the registered A1 PANEL ID
   e7f98d4439fccf91f3451bc4b9e78079e3bc2cc2452931363b28520460b6cb43 and compared with work\\a1\\a1_panel_e7f98d4439fc.pkl
   when that file exists (STOP on any difference).
   The incumbent's as-run values come from local\\results\\gm_a1_v2.txt (the A1 rerun under gm-2.2.1; gm/CHANGES.md
   gm-2.2.1 item 4c): STOP if the file is missing, has no "A1 JOB DONE", names another A1 PANEL ID or lacks one of the
   three "all blocks (A1 panel) | k1 / k0 / d1 | 1975-2010" lines.
3. The registered A2 report (a2_batch.report): the incumbent as run is checked against those values first (STOP on a
   difference); decisive H1 / H3 at k = 1 on 1975-01..2010-12; the reported lines (k = 0, one-month delay, eras, books,
   versions, pods, classes, tranches, Trend split, carry / price, Value and Economic trend next to Trend, flagged share,
   P4, fragility, selection inflation, knobs); the A2 VERDICT line. Summary statistics over >= 60 months only.
4. TRIAL ROW (gm/trials.csv family "book") for the coordinator to log.
Needs: lib\\gm\\ (gm-2.2.1), lib\\gm_engine.py, lib\\bbgdata.py, lib\\bbg_panel.py, lib\\a1_panel.py, lib\\a2_batch.py,
lib\\engine_ref.json, lib\\live_sources.csv, lib\\untouched_markets.csv, work\\bbg\\ (LOCK_v2 store),
work\\free\\gm_free_inputs.zip; results\\gm_a1_v2.txt; work\\a1\\ (optional: the A1 panel file)."""
import os
import sys

sys.path[:0] = [os.path.join(os.getcwd(), "lib"), os.path.join(os.getcwd(), "pylib")]

import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402
import traceback  # noqa: E402

T0 = time.time()
WORK = os.environ.get("BBG_WORK", os.path.join(os.getcwd(), "work"))
FREE = os.path.join(WORK, "free")
LIB = os.path.join(os.getcwd(), "lib")
print("=== gm_a2_v1 ===")

# the registered build of the lib files (A2_BUILD hash table; gm/CHANGES.md A2 item 7)
LIB_SHA = {"a2_batch.py": "87b24d8f558da20f6b5403d67006629b87edf45cea2d7e36cfa71605b014797b",
           "a1_panel.py": "eb9ef3f7fbd12760e174f9ef1df8573890bed6ca8d36f7d4e5c63eadd822ebb5",
           "gm_engine.py": "ac43a33cd8943719ba0efb9bb246473c7bbf59018a6d3b7398f64520eeebd721",
           "bbg_panel.py": "e0b67a42793e67c129ec8a6c3ed2082390933ea9317898b59b8854387ecf1dcd",
           "bbgdata.py": "0b26bb21b50671dca7c2153d3d66a2a09f7f33eeaa7c96ca536b69bbca8e6351"}


def frames(e):
    """Exception type and code frames only (no message text); numbers with 3+ decimals scrubbed anyway."""
    tb = traceback.extract_tb(e.__traceback__)[-6:]
    txt = "%s at %s" % (type(e).__name__, " <- ".join("%s:%d %s" % (os.path.basename(f.filename), f.lineno, f.name)
                                                       for f in reversed(tb)))
    import re as _re
    return _re.sub(r"-?\d+\.\d{3,}", "<num>", txt)


def stop(msg):
    print("STOP: " + msg)
    print("=== END === %.0fs" % (time.time() - T0))
    sys.exit(0)


def sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


try:
    import a2_batch as A2
    import a1_panel as A1
    import bbgdata
    import bbg_panel
    import gm_engine as GE
    from gm import config as CF
    print("%s | %s | %s | %s | %s | engine %s | %s" % (A2.VERSION, A1.VERSION, bbgdata.VERSION, bbg_panel.VERSION,
                                                       GE.VERSION, CF.ENGINE_VERSION,
                                                       ", ".join("%s %s" % kv for kv in GE.lib_versions().items())))
    ref = json.load(open(os.path.join(LIB, "engine_ref.json"), encoding="utf-8"))
except Exception as e:  # noqa: BLE001
    stop("setup failed: %s" % frames(e))

# ---- 1. checks
try:
    import gm
    gm_dir = os.path.dirname(os.path.abspath(gm.__file__))
    here = GE.gm_code_hashes(gm_dir)
    want = ref["code"]["gm_files_sha256"]
    bad = sorted(k for k in set(here) | set(want) if here.get(k) != want.get(k))
    print("%s gm code vs reference | %d files | differing or missing: %s" % ("PASS" if not bad else "FAIL", len(want),
                                                                            ", ".join(bad) or "none"))
    if bad:
        stop("the gm code on the PC is not the registered engine")
    badl = []
    for n, want_sha in sorted(LIB_SHA.items()):
        got = sha(os.path.join(LIB, n))
        print("%s lib %s | sha256 %s | registered %s" % ("PASS" if got == want_sha else "FAIL", n, got[:16],
                                                       want_sha[:16]))
        badl += [n] if got != want_sha else []
    if badl:
        stop("lib file differs from the registered build: %s" % ", ".join(badl))
    trials = os.path.join(gm_dir, "trials.csv")
    got = sha(trials)
    print("%s lib gm\\trials.csv | sha256 %s | registered %s" % ("PASS" if got == A2.TRIALS_SHA else "FAIL", got[:16],
                                                                A2.TRIALS_SHA[:16]))
    if got != A2.TRIALS_SHA:
        stop("the trial log differs from the registered one (selection inflation, CHANGES A2 item 4l)")
    a1rep = os.environ.get("A1_REPORT", os.path.join(os.getcwd(), "results", A2.A1_REPORT))
    as_run, why = A2.as_run_from_a1(a1rep)
    print("%s A1 report %s: %s%s" % ("PASS" if as_run else "FAIL", A2.A1_REPORT, why, "" if not as_run else
                                     " | as run " + ", ".join("%s %.3f" % kv for kv in sorted(as_run.items()))))
    if not as_run:
        stop("the gm_a1_v2 report is not usable (%s): queue gm_a1_v2 first" % why)
    lock = bbgdata.Panel(WORK)
    print("%s Bloomberg store lock id %s | registered LOCK_v2 %s" % ("PASS" if lock.lock_id == A1.LOCK_V2 else "FAIL",
                                                                     lock.lock_id, A1.LOCK_V2))
    if lock.lock_id != A1.LOCK_V2:
        stop("the Bloomberg store is not LOCK_v2 (nothing read)")
    del lock
    st = GE.ensure_free_inputs(FREE)
    if st["manifest"] is None:
        stop("work\\free\\gm_free_inputs.zip not found")
    same, how = GE.inputs_match(st["manifest"], ref)
    digest = GE.original_digest(st["manifest"])
    print("%s free inputs | %d files | not matching the manifest %d | %s %s the reference | digest %s" % (
        "PASS" if (same and not st["bad"]) else "FAIL", len(st["manifest"]["files"]), len(st["bad"]), how,
        "match" if same else "DO NOT MATCH", digest[:16]))
    if st["bad"] or not same:
        stop("free inputs differ from the reference")
except SystemExit:
    raise
except Exception as e:  # noqa: BLE001
    stop("checks failed: %s" % frames(e))

# ---- 2. free arm, the A1 panel
try:
    t = time.time()
    M = GE.setup(FREE)
    free = A1.free_inputs(M)
    fr = A1.check_free_vs_ref(free, ref)
    for r in fr:
        print("%s free arm vs reference | %s | n %d | missing %d | max abs diff %.1e" % (
            "PASS" if r["pass"] else "FAIL", r["item"], r["n"], r["missing"], r["maxdiff"]))
    if not all(r["pass"] for r in fr):
        stop("the free arm differs from the reference engine path (no Bloomberg value read)")
    store = A1.Store(WORK)
    assert store.lock_id == A1.LOCK_V2, "store lock id is not LOCK_v2"
    rows, _rep = A1.evaluate(store, free)
    a1 = A1.build(store, free, (1, 2, 3), rows, M, digest)
    A1.assert_extension_only(free, a1)
    print("EXTENSION-ONLY CHECK PASS | admitted series %d | %.0fs" % (len(a1["admitted"]), time.time() - t))
    ok = A2.check_panel_id(a1)
    print("%s A1 PANEL ID %s | registered %s" % ("PASS" if ok else "FAIL", a1["panel_id"], A2.A1_PANEL_ID))
    if not ok:
        stop("the rebuilt A1 panel is not the registered one")
    cmp_ = A2.compare_saved(WORK, a1)
    print("%s A1 panel file work\\a1\\a1_panel_%s.pkl: %s" % ("FAIL" if cmp_.startswith("differs") else "PASS",
                                                              a1["panel_id"][:12], cmp_ if cmp_ != "absent" else
                                                              "absent (the rebuild, id checked, is used)"))
    if cmp_.startswith("differs"):
        stop("the saved A1 panel differs from the rebuild (%s)" % cmp_)
    for k, v in sorted(a1["added"].items()):
        print("EXTENDED %s %s | %s..%s | %d months" % (k[0], k[1], v[0], v[1], v[2]))
except SystemExit:
    raise
except Exception as e:  # noqa: BLE001
    stop("A1 panel failed: %s" % frames(e))

# ---- 3. the registered A2 report
try:
    t = time.time()
    res = A2.report(a1["R"], free["D"], a1["S"], free["gspc"], out=print, as_run=as_run,
                    trials_path=os.path.join(gm_dir, "trials.csv"))
    print("report %.0fs" % (time.time() - t))
except A2.AsRunMismatch:
    stop("the incumbent does not reproduce the A1 run (nothing else printed)")
except Exception as e:  # noqa: BLE001
    stop("report failed: %s" % frames(e))

# ---- 4. trial row
try:
    row = A2.trial_row(res, a1["panel_id"], CF.ENGINE_VERSION)
    row["config"] = json.dumps(CF.A2_CHALLENGER, sort_keys=True, default=list)
    print("TRIAL ROW " + json.dumps(row, sort_keys=True))
except Exception as e:  # noqa: BLE001
    stop("trial row failed: %s" % frames(e))
print("A2 JOB DONE")
print("=== END === %.0fs" % (time.time() - T0))
