"""gm_a1_v1: Batch A1, data swap (TESTING_PROTOCOL 7.6 step 2; gm/CHANGES.md "data: A1 data rule", 2026-11-27) on the PC.

1. Checks: gm code = the reference's (lib\\engine_ref.json); Bloomberg store lock id = LOCK_v2
   d85a46cb2853646b24796f294f3ccab1d1507188c402e978fd59f5196ea41fc9 (else STOP before any value is read); free inputs
   = the shipped zip (work\\free).
2. Every registered candidate series (blocks 1-3) and report-line series (bond futures): ADMITTED / REJECTED with the
   reasons, status, first date in the lock, overlap months, correlation (printed only over >= 60 months), extension
   months. This is also the LOCK_v2 part of the 7.6 step 2 metadata listing. Metadata only: no data value.
3. The A1 panel (free panel + admitted backward extensions, design months only) and its id; extension-only checked.
   The values go only to work\\a1\\a1_panel_<id12>.pkl.
4. The registered A1 report: A1_INCUMBENT (CANDIDATE gm-2.0.3 + E13) at k = 1 (k = 0 beside) on the A1 data against
   the same on free data, one block at a time, then all blocks; design window 1975-01..2010-12; summary statistics only
   (export whitelist: statistics over >= 60 months). Report only: no adoption test.
5. TRIAL ROW (gm/trials.csv family "data") for the coordinator to log.
Needs: lib\\gm\\ (gm-2.2.0), lib\\gm_engine.py, lib\\bbgdata.py, lib\\bbg_panel.py, lib\\a1_panel.py, lib\\engine_ref.json,
lib\\live_sources.csv, lib\\untouched_markets.csv, work\\bbg\\ (LOCK_v2 store), work\\free\\gm_free_inputs.zip."""
import os
import sys

sys.path[:0] = [os.path.join(os.getcwd(), "lib"), os.path.join(os.getcwd(), "pylib")]

import json  # noqa: E402
import time  # noqa: E402
import traceback  # noqa: E402

T0 = time.time()
WORK = os.environ.get("BBG_WORK", os.path.join(os.getcwd(), "work"))
FREE = os.path.join(WORK, "free")
LIB = os.path.join(os.getcwd(), "lib")
print("=== gm_a1_v1 ===")


def stop(msg):
    print("STOP: " + msg)
    print("=== END === %.0fs" % (time.time() - T0))
    sys.exit(0)


try:
    import a1_panel as A1
    import bbgdata
    import bbg_panel
    import gm_engine as GE
    from gm import config as CF
    print("%s | %s | %s | %s | engine %s | %s" % (A1.VERSION, bbgdata.VERSION, bbg_panel.VERSION, GE.VERSION,
                                                  CF.ENGINE_VERSION, ", ".join("%s %s" % kv for kv in
                                                                               GE.lib_versions().items())))
    ref = json.load(open(os.path.join(LIB, "engine_ref.json"), encoding="utf-8"))
except Exception as e:  # noqa: BLE001
    stop("setup failed: %s %s" % (type(e).__name__, str(e)[:300]))

# ---- 1. checks
try:
    import gm
    here = GE.gm_code_hashes(os.path.dirname(os.path.abspath(gm.__file__)))
    want = ref["code"]["gm_files_sha256"]
    bad = sorted(k for k in set(here) | set(want) if here.get(k) != want.get(k))
    print("%s gm code vs reference | %d files | differing or missing: %s" % ("PASS" if not bad else "FAIL", len(want),
                                                                            ", ".join(bad) or "none"))
    if bad:
        stop("the gm code on the PC is not the registered engine")
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
    print("".join(traceback.format_exc().splitlines(True)[-6:]))
    stop("checks failed: %s %s" % (type(e).__name__, str(e)[:300]))

# ---- 2. candidates
try:
    t = time.time()
    M = GE.setup(FREE)
    free = A1.free_inputs(M)
    store = A1.Store(WORK)
    rows, rep = A1.evaluate(store, free)
    print("--- candidate series (A1 rule, 7.6 step 2; LOCK_v2 as of 2010-12-31; %.0fs)" % (time.time() - t))
    print("verdict | block | market | ticker field | status | first in lock | first used | free first | overlap | "
          "corr | extension | instrument | reasons")
    for r in rows:
        print(A1.fmt_row(r))
    print("--- report line R (7.1 F7): bond futures vs yield-built returns (reported, never used)")
    for r in rep:
        print(A1.fmt_row(r))
    for b in (1, 2, 3):
        rb = [r for r in rows if r["block"] == b]
        print("BLOCK %d (%s) | candidates %d | admitted %d | rejected %d" % (
            b, A1.BLOCK_NAMES[b], len(rb), sum(r["verdict"] == "admitted" for r in rb),
            sum(r["verdict"] != "admitted" for r in rb)))
except Exception as e:  # noqa: BLE001
    print("".join(traceback.format_exc().splitlines(True)[-8:]))
    stop("candidate evaluation failed: %s %s" % (type(e).__name__, str(e)[:300]))

# ---- 3. A1 panel, one block at a time, then all
try:
    arms = [("free", None)]
    for b in (1, 2, 3):
        if any(r["verdict"] == "admitted" and r["block"] == b for r in rows):
            a = A1.build(store, free, (b,), rows, M, digest)
            A1.assert_extension_only(free, a)
            arms.append(("block %d alone" % b, a))
    a_all = A1.build(store, free, (1, 2, 3), rows, M, digest)
    A1.assert_extension_only(free, a_all)
    if len(arms) > 2:
        arms.append(("all blocks (A1 panel)", a_all))
    elif len(arms) == 2:
        arms[1] = ("all blocks (A1 panel) = %s" % arms[1][0], a_all)
    print("EXTENSION-ONLY CHECK PASS (no free month changed; only months before each free start filled)")
    print("A1 PANEL ID %s | admitted series %d | blocks %s | LOCK_v2 %s | free inputs %s | %s" % (
        a_all["panel_id"], len(a_all["admitted"]), ",".join(str(b) for b in a_all["blocks"]), A1.LOCK_V2[:16],
        digest[:16], A1.VERSION))
    for k, v in sorted(a_all["added"].items()):
        print("EXTENDED %s %s | %s..%s | %d months" % (k[0], k[1], v[0], v[1], v[2]))
    p = A1.save_panel(WORK, a_all)
    print("A1 panel values written to work\\a1\\%s (PC only)" % os.path.basename(p))
except Exception as e:  # noqa: BLE001
    print("".join(traceback.format_exc().splitlines(True)[-8:]))
    stop("A1 panel failed: %s %s" % (type(e).__name__, str(e)[:300]))

# ---- 4. the registered report
try:
    t = time.time()
    if len(arms) == 1:
        print("NO SERIES ADMITTED: the A1 panel equals the free panel; the report has the free arm only")
    res = A1.report(free, arms, CF.A1_INCUMBENT)
    print("report %.0fs" % (time.time() - t))
    last = arms[-1][0]
    row = A1.trial_row(CF.A1_INCUMBENT, res[last], a_all["panel_id"], CF.ENGINE_VERSION, A1.LOCK_V2)
    row["config"] = json.dumps(CF.A1_INCUMBENT, sort_keys=True, default=list)
    print("TRIAL ROW " + json.dumps(row, sort_keys=True))
except Exception as e:  # noqa: BLE001
    print("".join(traceback.format_exc().splitlines(True)[-8:]))
    stop("report failed: %s %s" % (type(e).__name__, str(e)[:300]))
print("A1 JOB DONE")
print("=== END === %.0fs" % (time.time() - T0))
