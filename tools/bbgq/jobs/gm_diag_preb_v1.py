"""gm_diag_preb_v1: the pre-B diagnostics of TESTING_PROTOCOL 7.5 order item 3 (7.6 step 7; gm/CHANGES.md "Pre-B
diagnostics", 2026-11-27) on the PC.

1. Checks (else STOP before any Bloomberg or LSEG value is read): gm code = the reference's (lib\\engine_ref.json);
   sha256 of lib\\engine_ref.json = the gm-2.2.1 reference; config.ENGINE_VERSION gm-2.2.1 and the config hashes of
   BASE, CANDIDATE, A1_INCUMBENT, A2_CHALLENGER; lib files diag_preb.py, diag_a2.py, a2_batch.py, a1_panel.py,
   gm_engine.py, bbg_panel.py, bbgdata.py, lsegdata.py, lseg_rules.py = the registered sha256 (LIB_SHA); the book /
   pod rows of lib\\gm\\trials.csv = the registered digest (41 rows); results\\gm_a2_v1.txt = the A2 run (A2 facts);
   results\\gm_diag_v1.txt = the diagnostics run (A3 empty); results\\gm_core_v1.txt = Core book v1 (CORE V1 JOB DONE,
   CORE BOOK V1 EMPTY); Bloomberg store lock id = LOCK_v2; LSEG store lock id = LOCK_LSEG_v5 (read from its manifest
   before any table is loaded); work\\free\\gm_card_inputs.zip = LOCK_CARD_v1 file by file (card_inputs.py, before a
   value is parsed); free inputs = the shipped zip.
2. Free arm vs engine_ref.json; the A1 panel rebuilt (a1_panel-1.1.0), extension-only, its id = the registered A1 PANEL
   ID, compared with work\\a1\\a1_panel_e7f98d4439fc.pkl when present (STOP on a difference). Nothing is written to work\\.
3. The free card inputs under the 2010-12-31 cut: panel.fx_usd_value (EUR, JPY, GBP, AUD, CAD), TB3MS and the OECD
   3-month rates of C2-D1 (DE then EZ).
4. diag_preb.report: as-run check of the A2-final book against the A2 report first (STOP on a difference), then R1,
   C1-D1, C1-D2, C2-D1, C3-D1, C5-D1, C5-D2, F0 and the blocked list; values over >= 60 months only (else count and
   sign); no LSEG or Bloomberg value is printed.
5. TRIAL ROW lines (gm/trials.csv family "diag", one per diagnostic run) for the coordinator.
Needs: lib\\gm\\ (gm-2.2.1), lib\\gm_engine.py, lib\\bbgdata.py, lib\\bbg_panel.py, lib\\a1_panel.py, lib\\a2_batch.py,
lib\\diag_a2.py, lib\\diag_preb.py, lib\\card_inputs.py, lib\\lsegdata.py, lib\\lseg_rules.py (+ the lsegdata config CSVs), lib\\engine_ref.json,
lib\\live_sources.csv, lib\\untouched_markets.csv, work\\bbg\\ (LOCK_v2 store), work\\lseg\\ (LOCK_LSEG_v5 store),
work\\free\\gm_free_inputs.zip, work\\free\\gm_card_inputs.zip, results\\gm_a2_v1.txt, results\\gm_diag_v1.txt, results\\gm_core_v1.txt; work\\a1\\
(optional: the A1 panel file)."""
import os
import sys

sys.dont_write_bytecode = True          # importing the lib modules writes no __pycache__
sys.path[:0] = [os.path.join(os.getcwd(), "lib"), os.path.join(os.getcwd(), "pylib")]

import contextlib  # noqa: E402
import hashlib  # noqa: E402
import io  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402
import traceback  # noqa: E402

T0 = time.time()
WORK = os.environ.get("BBG_WORK", os.path.join(os.getcwd(), "work"))
FREE = os.path.join(WORK, "free")
LIB = os.path.join(os.getcwd(), "lib")
print("=== gm_diag_preb_v1 ===")

# the registered build of the lib files (PREB_BUILD hash table; gm/CHANGES.md "Pre-B diagnostics" item 9)
LIB_SHA = {"diag_preb.py": "5273944bcb9811ccba83510da3359996e28def8eb8b89a4408ed3efad855c64e",
           "diag_a2.py": "3264a5381c13b124d2566d02f263e21905f4e901680c1af7c2134f0bd558be1b",
           "a2_batch.py": "35339f673f351f43315ad3c7010ba733b6fb8990a6a41feb1ef20de324de58c6",
           "a1_panel.py": "eb9ef3f7fbd12760e174f9ef1df8573890bed6ca8d36f7d4e5c63eadd822ebb5",
           "gm_engine.py": "ac43a33cd8943719ba0efb9bb246473c7bbf59018a6d3b7398f64520eeebd721",
           "bbg_panel.py": "e0b67a42793e67c129ec8a6c3ed2082390933ea9317898b59b8854387ecf1dcd",
           "bbgdata.py": "0b26bb21b50671dca7c2153d3d66a2a09f7f33eeaa7c96ca536b69bbca8e6351",
           "lsegdata.py": "0d1b500ddb2e931ab4069ac8fd6fed0c16778da85b2665d3fcafadfae16198de",
           "lseg_rules.py": "5686999172a22c76b7190f8df210c93ffc09a6737f32301df030080dccc42da9",
           "card_inputs.py": "4091f84bcbb11f43061bcc0330520a4a5580cb775895148a38849c0fbcab7b80"}
CARD_ZIP = os.path.join(FREE, "gm_card_inputs.zip")      # LOCK_CARD_v1 (gm/CHANGES.md data entry "card inputs")


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
    import diag_preb as PB
    import diag_a2 as DG
    import a2_batch as A2
    import a1_panel as A1
    import bbgdata
    import bbg_panel
    import gm_engine as GE
    import lsegdata as LD
    import lseg_rules as LR
    import card_inputs as CIN
    from gm import config as CF
    print("%s | %s | %s | %s | %s | %s | %s | %s | %s | engine %s | %s" % (
        PB.VERSION, DG.VERSION, A2.VERSION, A1.VERSION, bbgdata.VERSION, bbg_panel.VERSION, GE.VERSION, LD.VERSION,
        LR.VERSION + " | " + CIN.VERSION, CF.ENGINE_VERSION, ", ".join("%s %s" % kv for kv in GE.lib_versions().items())))
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
    got = sha(os.path.join(LIB, "engine_ref.json"))
    print("%s lib engine_ref.json | sha256 %s | registered %s" % ("PASS" if got == PB.REF_SHA else "FAIL", got[:16],
                                                                 PB.REF_SHA[:16]))
    if got != PB.REF_SHA:
        stop("engine_ref.json is not the registered gm-2.2.1 reference")
    hs = {"BASE": CF.cfg_hash(CF.BASE), "CANDIDATE": CF.cfg_hash(CF.CANDIDATE),
          "A1_INCUMBENT": CF.cfg_hash(CF.A1_INCUMBENT), "A2_CHALLENGER": CF.cfg_hash(CF.A2_CHALLENGER)}
    okc = CF.ENGINE_VERSION == PB.ENGINE and hs == PB.CFG_HASHES and CF.A1_INCUMBENT["name"] == PB.FINAL_NAME
    print("%s engine %s and config hashes %s | registered %s, %s" % (
        "PASS" if okc else "FAIL", CF.ENGINE_VERSION, ", ".join("%s %s" % kv for kv in sorted(hs.items())), PB.ENGINE,
        ", ".join("%s %s" % kv for kv in sorted(PB.CFG_HASHES.items()))))
    if not okc:
        stop("config is not the registered gm-2.2.1 arms")
    badl = []
    for n, want_sha in sorted(LIB_SHA.items()):
        p = os.path.join(LIB, n)
        got = sha(p) if os.path.exists(p) else "missing"
        print("%s lib %s | sha256 %s | registered %s" % ("PASS" if got == want_sha else "FAIL", n, got[:16],
                                                       want_sha[:16]))
        badl += [n] if got != want_sha else []
    if badl:
        stop("lib file differs from the registered build: %s" % ", ".join(badl))
    dg, nrow, _lines = DG.trial_rows_digest(os.path.join(gm_dir, "trials.csv"))
    okt = dg == PB.TRIAL_ROWS_SHA and nrow == PB.TRIAL_ROWS_N
    print("%s lib gm\\trials.csv book / pod rows | %d rows | digest %s | registered %d rows, %s" % (
        "PASS" if okt else "FAIL", nrow, dg[:16], PB.TRIAL_ROWS_N, PB.TRIAL_ROWS_SHA[:16]))
    if not okt:
        stop("the book / pod rows of the trial log differ from the registered ones")
    res_dir = os.environ.get("RESULTS_DIR", os.path.join(os.getcwd(), "results"))
    facts, why = DG.a2_facts(os.path.join(res_dir, PB.A2_REPORT))
    print("%s A2 report %s: %s" % ("PASS" if facts else "FAIL", PB.A2_REPORT, why))
    if not facts:
        stop("the gm_a2_v1 report is not usable (%s)" % why)
    okd, why = PB.diag_facts(os.path.join(res_dir, PB.DIAG_REPORT))
    print("%s diagnostics report %s: %s" % ("PASS" if okd else "FAIL", PB.DIAG_REPORT, why))
    if not okd:
        stop("the gm_diag_v1 report is not usable (%s)" % why)
    okk, why = PB.core_facts(os.path.join(res_dir, PB.CORE_REPORT))
    print("%s Core book v1 report %s: %s" % ("PASS" if okk else "FAIL", PB.CORE_REPORT, why))
    if not okk:
        stop("the gm_core_v1 report is not usable (%s): 7.5 order item 3 runs after Core book v1" % why)
    lock = bbgdata.Panel(WORK)
    print("%s Bloomberg store lock id %s | registered LOCK_v2 %s" % ("PASS" if lock.lock_id == PB.LOCK_V2 else "FAIL",
                                                                     lock.lock_id, PB.LOCK_V2))
    if lock.lock_id != PB.LOCK_V2:
        stop("the Bloomberg store is not LOCK_v2 (nothing read)")
    del lock
    lid, why = PB.lseg_lock_of(WORK)
    print("%s LSEG store lock id %s | registered LOCK_LSEG_v5 %s | %s" % (
        "PASS" if lid == PB.LSEG_LOCK else "FAIL", lid, PB.LSEG_LOCK, why))
    if lid != PB.LSEG_LOCK:
        stop("the LSEG store is not LOCK_LSEG_v5 (nothing read)")
    if not os.path.exists(CARD_ZIP):
        stop("work\\free\\gm_card_inputs.zip not found (LOCK_CARD_v1)")
    try:
        CI_ = CIN.Inputs.from_zip(CARD_ZIP)
    except CIN.CardInputsError as e:
        print("FAIL card inputs: %s" % e)
        stop("the card inputs zip is not LOCK_CARD_v1")
    okci = CI_.lock_id == PB.CARD_LOCK == CIN.LOCK_ID
    print("%s card inputs gm_card_inputs.zip | %d files, each = its LOCK_CARD_v1 sha256 | lock id %s | registered %s | "
          "commit %s" % ("PASS" if okci else "FAIL", len(CIN.FILES), CI_.lock_id[:16], PB.CARD_LOCK[:16],
                         CIN.COMMIT[:12]))
    if not okci:
        stop("the card inputs lock id is not LOCK_CARD_v1")
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

# ---- 2. free arm, the A1 panel (compared with the saved file, never written)
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
    ok = a1["panel_id"] == PB.A1_PANEL_ID
    print("%s A1 PANEL ID %s | registered %s" % ("PASS" if ok else "FAIL", a1["panel_id"], PB.A1_PANEL_ID))
    if not ok:
        stop("the rebuilt A1 panel is not the registered one")
    cmp_ = A2.compare_saved(WORK, a1)
    print("%s A1 panel file work\\a1\\a1_panel_%s.pkl: %s" % ("FAIL" if cmp_.startswith("differs") else "PASS",
                                                              a1["panel_id"][:12], cmp_ if cmp_ != "absent" else
                                                              "absent (the rebuild, id checked, is used; nothing "
                                                              "written)"))
    if cmp_.startswith("differs"):
        stop("the saved A1 panel differs from the rebuild (%s)" % cmp_)
except SystemExit:
    raise
except Exception as e:  # noqa: BLE001
    stop("A1 panel failed: %s" % frames(e))

# ---- 3. free card inputs under the 2010-12-31 cut
try:
    import pandas as pd
    P = M["P"]
    with GE.Cut(M, A1.SEAL), contextlib.redirect_stdout(io.StringIO()):
        fxv = pd.DataFrame({c: P.fx_usd_value(c) for c in PB.R5_CUR})
        rates = {"TB3MS": P.F("TB3MS")}
        for cc, names in PB.RATE_SERIES.items():
            rates[cc] = P.first(*[P.F(n) for n in names])
    print("card inputs | fx values %s | rates %s" % (
        ", ".join("%s %d months" % (c, int(fxv[c].notna().sum())) for c in fxv.columns),
        ", ".join("%s %s.. (%d)" % (k, v.first_valid_index(), int(v.notna().sum())) for k, v in rates.items())))
except Exception as e:  # noqa: BLE001
    stop("card inputs failed: %s" % frames(e))

# ---- 4. the registered diagnostics
try:
    t = time.time()
    lseg = PB.LsegView(LD.Panel(WORK))
    if lseg.panel.lock_id != PB.LSEG_LOCK:
        stop("the loaded LSEG store is not LOCK_LSEG_v5")
    res = PB.report(a1["R"], free["D"], a1["S"], free["gspc"], fxv, rates, lseg, CI_, out=print, facts=facts)
    print("report %.0fs" % (time.time() - t))
except SystemExit:
    raise
except PB.AsRunMismatch:
    stop("the A2-final book does not reproduce the A2 report (nothing else printed)")
except Exception as e:  # noqa: BLE001
    stop("report failed: %s" % frames(e))

# ---- 5. trial rows
try:
    for row in PB.trial_rows(res, a1["panel_id"], CF.ENGINE_VERSION):
        print("TRIAL ROW " + json.dumps(row, sort_keys=True))
except Exception as e:  # noqa: BLE001
    stop("trial rows failed: %s" % frames(e))
print("PREB JOB DONE")
print("=== END === %.0fs" % (time.time() - T0))
