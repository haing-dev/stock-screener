"""gm_b1_v1: Batch B1 = Curve carry (TESTING_PROTOCOL 7.6 step 8; gm/CHANGES.md "Batch B1: Curve carry", 2026-11-28)
on the PC.

1. Checks (else STOP before any Bloomberg or LSEG value is read): gm code = the reference's (lib\\engine_ref.json);
   sha256 of lib\\engine_ref.json = the gm-2.2.1 reference; config.ENGINE_VERSION gm-2.2.1 and the config hashes of
   BASE, CANDIDATE, A1_INCUMBENT, A2_CHALLENGER; lib files b1_curve.py, diag_a2.py, a2_batch.py, a1_panel.py,
   gm_engine.py, bbg_panel.py, bbgdata.py, lsegdata.py, lseg_rules.py = the registered sha256 (LIB_SHA); the book / pod
   rows of lib\\gm\\trials.csv = the registered digest (41 rows); results\\gm_a2_v1.txt = the A2 run (A2 facts);
   results\\gm_core_v1.txt = Core book v1 (CORE V1 JOB DONE, CORE BOOK V1 EMPTY); results\\gm_diag_preb_v1.txt = the
   pre-B run (PREB JOB DONE); Bloomberg store lock id = LOCK_v2; LSEG store lock id = LOCK_LSEG_v5 (read from its
   manifest before any table is loaded); free inputs = the shipped zip.
2. Free arm vs engine_ref.json; the A1 panel rebuilt (a1_panel-1.1.0), extension-only, its id = the registered A1 PANEL
   ID, compared with work\\a1\\a1_panel_e7f98d4439fc.pkl when present (STOP on a difference); the A2-final book as run
   against the A2 report (STOP on a difference); its commodity blocks of Carry and Trend at k = 0 (reported overlap).
3. LSEG design part (lsegdata.load_design, held-back instruments hidden); the pod truncation gate at the 8 cut dates
   (STOP on a FAIL; PASS / FAIL and counts only).
4. b1_curve.report: DATA and WINDOW lines (counts), T1-T3 (T4 not applicable), the verdict, the reported lines; values
   over >= 60 months only (else count and sign); no LSEG or Bloomberg value is printed.
5. TRIAL ROW lines (gm/trials.csv: one "pod" row, one "diag" row) for the coordinator. Nothing is written to lib\\, to
   the Bloomberg or LSEG stores or to work\\a1\\; gm_engine.ensure_free_inputs (as in every earlier job) rewrites
   work\\free\\inputs_manifest.json and unpacks missing free input files (CHECK_B1 C3). 1.0.1 (CHECK_B1): the five
   LSEG config lists are pinned (LIB_SHA and the store manifest, C2).
Needs: lib\\gm\\ (gm-2.2.1), lib\\gm_engine.py, lib\\bbgdata.py, lib\\bbg_panel.py, lib\\a1_panel.py, lib\\a2_batch.py,
lib\\diag_a2.py, lib\\b1_curve.py, lib\\lsegdata.py, lib\\lseg_rules.py (+ the lsegdata config CSVs), lib\\engine_ref.json,
lib\\live_sources.csv, lib\\untouched_markets.csv, work\\bbg\\ (LOCK_v2 store), work\\lseg\\ (LOCK_LSEG_v5 store),
work\\free\\gm_free_inputs.zip, results\\gm_a2_v1.txt, results\\gm_core_v1.txt, results\\gm_diag_preb_v1.txt; work\\a1\\
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
print("=== gm_b1_v1 ===")

# the registered build of the lib files (B1_BUILD hash table; gm/CHANGES.md "Batch B1: Curve carry" item 10)
LIB_SHA = {"b1_curve.py": "2f5b859c359c9caad2a74356463d40c869050a5a0a1fe52a9a5414c4750ff526",
           "diag_a2.py": "3264a5381c13b124d2566d02f263e21905f4e901680c1af7c2134f0bd558be1b",
           "a2_batch.py": "35339f673f351f43315ad3c7010ba733b6fb8990a6a41feb1ef20de324de58c6",
           "a1_panel.py": "eb9ef3f7fbd12760e174f9ef1df8573890bed6ca8d36f7d4e5c63eadd822ebb5",
           "gm_engine.py": "ac43a33cd8943719ba0efb9bb246473c7bbf59018a6d3b7398f64520eeebd721",
           "bbg_panel.py": "e0b67a42793e67c129ec8a6c3ed2082390933ea9317898b59b8854387ecf1dcd",
           "bbgdata.py": "0b26bb21b50671dca7c2153d3d66a2a09f7f33eeaa7c96ca536b69bbca8e6351",
           "lsegdata.py": "0d1b500ddb2e931ab4069ac8fd6fed0c16778da85b2665d3fcafadfae16198de",
           "lseg_rules.py": "5686999172a22c76b7190f8df210c93ffc09a6737f32301df030080dccc42da9",
           # 1.0.1 C2: the LSEG config lists = the LOCK_LSEG_v5 config hashes (lseg_roots.csv sets identity)
           "lseg_engine_map.csv": "8812f20d4d6dadcbfe5171cbe92b03a57f65ba01599a6d17d842130864bbaa15",
           "lseg_exclusions.csv": "8e2ca054128ce420543d8e06252af14255a8492064a647e73e69dde90fb45bf9",
           "lseg_live_sources.csv": "37e42068a8ae7f36ee12ece245c3c17b6cc27ac6f51b52078d54e1a891c4c77f",
           "lseg_roots.csv": "7a8caf01fbc70108af78be145337b41ac7e0050fc3f326211c997dc1a9991ee3",
           "lseg_untouched.csv": "17ec5fb38c2cc3b3f337adac2478d04c100fb949bcbcfe159fd53f26ef705185"}
LSEG_CFG = ("lseg_engine_map.csv", "lseg_exclusions.csv", "lseg_live_sources.csv", "lseg_roots.csv",
            "lseg_untouched.csv")


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
    import b1_curve as BC
    import diag_a2 as DG
    import a2_batch as A2
    import a1_panel as A1
    import bbgdata
    import bbg_panel
    import gm_engine as GE
    import lsegdata as LD
    import lseg_rules as LR
    from gm import config as CF
    print("%s | %s | %s | %s | %s | %s | %s | %s | %s | engine %s | %s" % (
        BC.VERSION, DG.VERSION, A2.VERSION, A1.VERSION, bbgdata.VERSION, bbg_panel.VERSION, GE.VERSION, LD.VERSION,
        LR.VERSION, CF.ENGINE_VERSION, ", ".join("%s %s" % kv for kv in GE.lib_versions().items())))
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
    print("%s lib engine_ref.json | sha256 %s | registered %s" % ("PASS" if got == BC.REF_SHA else "FAIL", got[:16],
                                                                 BC.REF_SHA[:16]))
    if got != BC.REF_SHA:
        stop("engine_ref.json is not the registered gm-2.2.1 reference")
    hs = {"BASE": CF.cfg_hash(CF.BASE), "CANDIDATE": CF.cfg_hash(CF.CANDIDATE),
          "A1_INCUMBENT": CF.cfg_hash(CF.A1_INCUMBENT), "A2_CHALLENGER": CF.cfg_hash(CF.A2_CHALLENGER)}
    okc = CF.ENGINE_VERSION == BC.ENGINE and hs == BC.CFG_HASHES and CF.A1_INCUMBENT["name"] == BC.FINAL_NAME
    print("%s engine %s and config hashes %s | registered %s, %s" % (
        "PASS" if okc else "FAIL", CF.ENGINE_VERSION, ", ".join("%s %s" % kv for kv in sorted(hs.items())), BC.ENGINE,
        ", ".join("%s %s" % kv for kv in sorted(BC.CFG_HASHES.items()))))
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
    okt = dg == BC.TRIAL_ROWS_SHA and nrow == BC.TRIAL_ROWS_N
    print("%s lib gm\\trials.csv book / pod rows | %d rows | digest %s | registered %d rows, %s" % (
        "PASS" if okt else "FAIL", nrow, dg[:16], BC.TRIAL_ROWS_N, BC.TRIAL_ROWS_SHA[:16]))
    if not okt:
        stop("the book / pod rows of the trial log differ from the registered ones")
    res_dir = os.environ.get("RESULTS_DIR", os.path.join(os.getcwd(), "results"))
    facts, why = DG.a2_facts(os.path.join(res_dir, BC.A2_REPORT))
    print("%s A2 report %s: %s" % ("PASS" if facts else "FAIL", BC.A2_REPORT, why))
    if not facts:
        stop("the gm_a2_v1 report is not usable (%s)" % why)
    okk, why = BC.core_facts(os.path.join(res_dir, BC.CORE_REPORT))
    print("%s Core book v1 report %s: %s" % ("PASS" if okk else "FAIL", BC.CORE_REPORT, why))
    if not okk:
        stop("the gm_core_v1 report is not usable (%s): B1 reads alpha against the EMPTY Core book v1" % why)
    okp, why = BC.preb_facts(os.path.join(res_dir, BC.PREB_REPORT))
    print("%s pre-B report %s: %s" % ("PASS" if okp else "FAIL", BC.PREB_REPORT, why))
    if not okp:
        stop("the gm_diag_preb_v1 report is not usable (%s): 7.6 step 8 runs after step 7" % why)
    lock = bbgdata.Panel(WORK)
    print("%s Bloomberg store lock id %s | registered LOCK_v2 %s" % ("PASS" if lock.lock_id == BC.LOCK_V2 else "FAIL",
                                                                     lock.lock_id, BC.LOCK_V2))
    if lock.lock_id != BC.LOCK_V2:
        stop("the Bloomberg store is not LOCK_v2 (nothing read)")
    del lock
    lid, why = BC.lseg_lock_of(WORK)
    print("%s LSEG store lock id %s | registered LOCK_LSEG_v5 %s | %s" % (
        "PASS" if lid == BC.LSEG_LOCK else "FAIL", lid, BC.LSEG_LOCK, why))
    if lid != BC.LSEG_LOCK:
        stop("the LSEG store is not LOCK_LSEG_v5 (nothing read)")
    man = json.load(open(os.path.join(WORK, "lseg", "manifest.json"), encoding="utf-8"))
    badc = [n for n in LSEG_CFG if (man.get("config") or {}).get(n) != LIB_SHA[n]]
    print("%s LSEG config lists in lib = the store manifest's config hashes | %d files | differing: %s" % (
        "PASS" if not badc else "FAIL", len(LSEG_CFG), ", ".join(badc) or "none"))
    if badc:
        stop("the LSEG config lists differ from the locked ones (nothing read)")
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

# ---- 2. free arm, the A1 panel (compared with the saved file, never written), the A2-final book as run
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
    ok = a1["panel_id"] == BC.A1_PANEL_ID
    print("%s A1 PANEL ID %s | registered %s" % ("PASS" if ok else "FAIL", a1["panel_id"], BC.A1_PANEL_ID))
    if not ok:
        stop("the rebuilt A1 panel is not the registered one")
    cmp_ = A2.compare_saved(WORK, a1)
    print("%s A1 panel file work\\a1\\a1_panel_%s.pkl: %s" % ("FAIL" if cmp_.startswith("differs") else "PASS",
                                                              a1["panel_id"][:12], cmp_ if cmp_ != "absent" else
                                                              "absent (the rebuild, id checked, is used; nothing "
                                                              "written)"))
    if cmp_.startswith("differs"):
        stop("the saved A1 panel differs from the rebuild (%s)" % cmp_)
    from gm import book as B
    from gm import execution as EX
    from gm import seal as SL
    R, D, S, gspc = SL.cut_inputs(SL.resolve(SL.DESIGN), a1["R"], free["D"], a1["S"], free["gspc"])
    days = EX.nyse_days(gspc=gspc)
    DG.as_run(R, D, S, days, CF.A1_INCUMBENT, facts, print)
    with contextlib.redirect_stdout(io.StringIO()):
        bk0 = B.run(R, cfg=CF.A1_INCUMBENT, daily=D, S=S)
    blocks = {"carry": bk0["blocks"].get(("carry", "CM")), "trend": bk0["blocks"].get(("trend", "CM"))}
    print("A2-final book k = 0 commodity blocks | carry %s | trend %s (reported overlap only)" % (
        "present" if blocks["carry"] is not None else "absent", "present" if blocks["trend"] is not None else "absent"))
except SystemExit:
    raise
except DG.AsRunMismatch:
    stop("the A2-final book does not reproduce the A2 report (nothing else printed)")
except Exception as e:  # noqa: BLE001
    stop("A1 panel / A2-final book failed: %s" % frames(e))

# ---- 3. LSEG design part and the pod truncation gate
try:
    t = time.time()
    cat, long, lock_id, _cal = LD.load_design(WORK, allow_untouched=False)
    if lock_id != BC.LSEG_LOCK:
        stop("the loaded LSEG store is not LOCK_LSEG_v5")
    roots = LD.roots_config()
    tab = BC.contract_table(cat, long, roots)
    prep = BC.prepare(tab)
    full = (tab, prep, BC.run(prep))
    ok, _tr = BC.truncation(cat, long, roots, GE.CUT_DATES, print, full=full)
    print("%s B1 truncation | %d cut dates | %.0fs" % ("PASS" if ok else "FAIL", len(GE.CUT_DATES), time.time() - t))
    if not ok:
        stop("the pod fails the truncation test (no statistic printed)")
except SystemExit:
    raise
except Exception as e:  # noqa: BLE001
    stop("LSEG / truncation failed: %s" % frames(e))

# ---- 4. the registered B1 run
try:
    t = time.time()
    res = BC.report(prep, spx=R["eq_us_spx"], blocks=blocks, out=print, trials_path=os.path.join(gm_dir, "trials.csv"))
    print("report %.0fs" % (time.time() - t))
except SystemExit:
    raise
except Exception as e:  # noqa: BLE001
    stop("report failed: %s" % frames(e))

# ---- 5. trial rows
try:
    for row in BC.trial_rows(res, CF.ENGINE_VERSION):
        print("TRIAL ROW " + json.dumps(row, sort_keys=True))
except Exception as e:  # noqa: BLE001
    stop("trial rows failed: %s" % frames(e))
print("B1 JOB DONE")
print("=== END === %.0fs" % (time.time() - T0))
