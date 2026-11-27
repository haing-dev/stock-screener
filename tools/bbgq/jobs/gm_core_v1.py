"""gm_core_v1: Core book v1 (TESTING_PROTOCOL 7.6 step 6; gm/CHANGES.md "Core book v1", 2026-11-27) on the PC.

1. Checks (else STOP before any Bloomberg value is read): gm code = the reference's (lib\\engine_ref.json); sha256 of
   lib\\engine_ref.json = the gm-2.2.1 reference; config.ENGINE_VERSION gm-2.2.1 and the config hashes of BASE,
   CANDIDATE, A1_INCUMBENT, A2_CHALLENGER; lib files core_v1.py, diag_a2.py, a2_batch.py, a1_panel.py, gm_engine.py,
   bbg_panel.py, bbgdata.py = the registered sha256 (LIB_SHA); lib\\rebuild_s4.py = REBUILD_SHA and imports nothing
   from the engine or these libraries; the book / pod rows of lib\\gm\\trials.csv = the registered digest;
   local\\results\\gm_a2_v1.txt = the A2 run (A2 facts as at the diagnostics); local\\results\\gm_diag_v1.txt = the
   diagnostics run with A3 empty (DIAG JOB DONE; D1 candidate half blocked, D2 and D3 closed); Bloomberg store lock id =
   LOCK_v2; free inputs = the shipped zip.
2. Free arm vs engine_ref.json; the A1 panel rebuilt (a1_panel-1.1.0), extension-only, its id = the registered A1 PANEL
   ID, compared with work\\a1\\a1_panel_e7f98d4439fc.pkl when present (STOP on a difference). Nothing is written to work\\.
3. The raw inputs of S4_INTERFACE.md v2 from the engine's loaders (no signal code), checked to reproduce the engine's
   currency / energy carry and equity value measures exactly; then the rebuild run on them and validated BEFORE any
   statistic (STOP if either fails).
4. core_v1.report: as-run check against the A2 report first (STOP on a difference), then S1-S4, the live-source check,
   the verdicts, Core book v1, the Incubator rule and the reported lines; summary statistics over >= 60 months only.
5. TRIAL ROW line (gm/trials.csv family "book", one row) for the coordinator.
Needs: lib\\gm\\ (gm-2.2.1), lib\\gm_engine.py, lib\\bbgdata.py, lib\\bbg_panel.py, lib\\a1_panel.py, lib\\a2_batch.py,
lib\\diag_a2.py, lib\\core_v1.py, lib\\rebuild_s4.py, lib\\engine_ref.json, lib\\live_sources.csv,
lib\\untouched_markets.csv, work\\bbg\\ (LOCK_v2 store), work\\free\\gm_free_inputs.zip, results\\gm_a2_v1.txt,
results\\gm_diag_v1.txt; work\\a1\\ (optional: the A1 panel file). Expected run time: about 6,000 book runs for the
placebos (a few seconds each on the PC)."""
import os
import sys

sys.dont_write_bytecode = True          # C4 (CHECK_CORE): importing the lib modules writes no __pycache__
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
print("=== gm_core_v1 ===")

# the registered build of the lib files (CORE_V1_BUILD hash table; gm/CHANGES.md "Core book v1" item 7)
LIB_SHA = {"core_v1.py": "ee01320501fd1ec1f1fcc8b89dca91000e7644f728ed67cbb9e4ac674b04549e",
           "diag_a2.py": "3264a5381c13b124d2566d02f263e21905f4e901680c1af7c2134f0bd558be1b",
           "a2_batch.py": "35339f673f351f43315ad3c7010ba733b6fb8990a6a41feb1ef20de324de58c6",
           "a1_panel.py": "eb9ef3f7fbd12760e174f9ef1df8573890bed6ca8d36f7d4e5c63eadd822ebb5",
           "gm_engine.py": "ac43a33cd8943719ba0efb9bb246473c7bbf59018a6d3b7398f64520eeebd721",
           "bbg_panel.py": "e0b67a42793e67c129ec8a6c3ed2082390933ea9317898b59b8854387ecf1dcd",
           "bbgdata.py": "0b26bb21b50671dca7c2153d3d66a2a09f7f33eeaa7c96ca536b69bbca8e6351"}
# the independent rebuild (gm/CHANGES.md "Core book v1" item 4e): set by a dated line under the entry, after the
# rebuild is delivered and accepted, BEFORE the job is queued. None = not registered yet: the job STOPs.
REBUILD_SHA = None


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
    import core_v1 as CV
    import diag_a2 as DG
    import a2_batch as A2
    import a1_panel as A1
    import bbgdata
    import bbg_panel
    import gm_engine as GE
    from gm import config as CF
    print("%s | %s | %s | %s | %s | %s | %s | engine %s | %s" % (
        CV.VERSION, DG.VERSION, A2.VERSION, A1.VERSION, bbgdata.VERSION, bbg_panel.VERSION, GE.VERSION,
        CF.ENGINE_VERSION, ", ".join("%s %s" % kv for kv in GE.lib_versions().items())))
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
    print("%s lib engine_ref.json | sha256 %s | registered %s" % ("PASS" if got == CV.REF_SHA else "FAIL", got[:16],
                                                                 CV.REF_SHA[:16]))
    if got != CV.REF_SHA:
        stop("engine_ref.json is not the registered gm-2.2.1 reference")
    hs = {"BASE": CF.cfg_hash(CF.BASE), "CANDIDATE": CF.cfg_hash(CF.CANDIDATE),
          "A1_INCUMBENT": CF.cfg_hash(CF.A1_INCUMBENT), "A2_CHALLENGER": CF.cfg_hash(CF.A2_CHALLENGER)}
    okc = CF.ENGINE_VERSION == CV.ENGINE and hs == CV.CFG_HASHES and CF.A1_INCUMBENT["name"] == CV.FINAL_NAME
    print("%s engine %s and config hashes %s | registered %s, %s" % (
        "PASS" if okc else "FAIL", CF.ENGINE_VERSION, ", ".join("%s %s" % kv for kv in sorted(hs.items())), CV.ENGINE,
        ", ".join("%s %s" % kv for kv in sorted(CV.CFG_HASHES.items()))))
    if not okc:
        stop("config is not the registered gm-2.2.1 arms")
    badl = []
    for n, want_sha in sorted(LIB_SHA.items()):
        got = sha(os.path.join(LIB, n))
        print("%s lib %s | sha256 %s | registered %s" % ("PASS" if got == want_sha else "FAIL", n, got[:16],
                                                       want_sha[:16]))
        badl += [n] if got != want_sha else []
    if badl:
        stop("lib file differs from the registered build: %s" % ", ".join(badl))
    rbp = os.path.join(LIB, "rebuild_s4.py")
    if REBUILD_SHA is None:
        stop("REBUILD_SHA not registered (gm/CHANGES.md 'Core book v1' item 4e): the job is not ready to queue")
    if not os.path.exists(rbp):
        stop("lib\\rebuild_s4.py missing")
    got = sha(rbp)
    print("%s lib rebuild_s4.py | sha256 %s | registered %s" % ("PASS" if got == REBUILD_SHA else "FAIL", got[:16],
                                                               REBUILD_SHA[:16]))
    if got != REBUILD_SHA:
        stop("rebuild_s4.py differs from the registered rebuild")
    fb = CV.forbidden_imports(rbp)
    print("%s rebuild_s4.py imports none of %s | found: %s" % ("PASS" if not fb else "FAIL", ", ".join(CV.FORBIDDEN),
                                                              ", ".join(fb) or "none"))
    if fb:
        stop("the rebuild imports the engine or the job's libraries (not independent)")
    dg, nrow, _lines = DG.trial_rows_digest(os.path.join(gm_dir, "trials.csv"))
    okt = dg == CV.TRIAL_ROWS_SHA and nrow == CV.TRIAL_ROWS_N
    print("%s lib gm\\trials.csv book / pod rows | %d rows | digest %s | registered %d rows, %s" % (
        "PASS" if okt else "FAIL", nrow, dg[:16], CV.TRIAL_ROWS_N, CV.TRIAL_ROWS_SHA[:16]))
    if not okt:
        stop("the book / pod rows of the trial log differ from the registered ones")
    a2rep = os.environ.get("A2_REPORT", os.path.join(os.getcwd(), "results", CV.A2_REPORT))
    facts, why = DG.a2_facts(a2rep)
    print("%s A2 report %s: %s%s" % ("PASS" if facts else "FAIL", CV.A2_REPORT, why, "" if not facts else
                                     " | A2 VERDICT FAIL, A2-final book %s (%s)" % (CV.FINAL_NAME, CV.FINAL_HASH)))
    if not facts:
        stop("the gm_a2_v1 report is not usable (%s)" % why)
    drep = os.environ.get("DIAG_REPORT", os.path.join(os.getcwd(), "results", CV.DIAG_REPORT))
    okd, why = CV.diag_facts(drep)
    print("%s diagnostics report %s: %s | A3 empty (%s)" % ("PASS" if okd else "FAIL", CV.DIAG_REPORT, why,
                                                            "; ".join(CV.DIAG_NEEDS)))
    if not okd:
        stop("the gm_diag_v1 report does not show the diagnostics run with A3 empty (%s)" % why)
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
    ok = a1["panel_id"] == CV.A1_PANEL_ID
    print("%s A1 PANEL ID %s | registered %s" % ("PASS" if ok else "FAIL", a1["panel_id"], CV.A1_PANEL_ID))
    if not ok:
        stop("the rebuilt A1 panel is not the registered one")
    cmp_ = A2.compare_saved(WORK, a1)
    print("%s A1 panel file work\\a1\\a1_panel_%s.pkl: %s" % ("FAIL" if cmp_.startswith("differs") else "PASS",
                                                              a1["panel_id"][:12], cmp_ if cmp_ != "absent" else
                                                              "absent (the rebuild, id checked, is used; nothing "
                                                              "written)"))
    if cmp_.startswith("differs"):
        stop("the saved A1 panel differs from the rebuild (%s)" % cmp_)
    for k, v in sorted(a1["added"].items()):
        print("EXTENDED %s %s | %s..%s | %d months" % (k[0], k[1], v[0], v[1], v[2]))
except SystemExit:
    raise
except Exception as e:  # noqa: BLE001
    stop("A1 panel failed: %s" % frames(e))

# ---- 3. the raw inputs (interface v2), checked; the independent rebuild, validated before any statistic
try:
    from gm import execution as EX
    from gm import seal as SL
    Tseal = SL.resolve(SL.DESIGN)
    R_, D_, S_, g_ = SL.cut_inputs(Tseal, a1["R"], free["D"], a1["S"], free["gspc"])
    days = EX.nyse_days(gspc=g_)
    dy_adm = [r for r in a1["admitted"] if r["kind"] == "dy"]
    if dy_adm:
        stop("A1 admitted a dividend-yield extension; interface v2 has no form for it (gm/CHANGES.md 'Core book v1' M2)")
    raw = CV.raw_from_engine(M, free, a1, store)
    rows_rc = CV.raw_check(raw, S_)
    for r in rows_rc:
        print("%s raw inputs reproduce the engine's measure | %s | markets %d | max abs diff %.1e | missing pattern %d" % (
            "PASS" if r["pass"] else "FAIL", r["group"], r["n"], r["maxdiff"], r["missing"]))
    if not all(r["pass"] for r in rows_rc):
        stop("the raw inputs do not reproduce the engine's measures (interface v2 section 3 item 0)")
    inp = CV.rebuild_inputs(R_, D_, days, raw,
                            {"config": CF.A1_INCUMBENT["name"], "config_hash": CF.cfg_hash(CF.A1_INCUMBENT),
                             "panel_id": a1["panel_id"], "engine": CF.ENGINE_VERSION})
    print("rebuild inputs | %s" % " | ".join("%s %s" % (k, getattr(v, "shape", len(v) if hasattr(v, "__len__") else ""))
                                             for k, v in inp.items()))
    import rebuild_s4 as RB
    t = time.time()
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        rb = RB.part_returns(inp, cut="2010-12-31")
    okr, why, nm = CV.validate_rebuild(rb)
    print("%s rebuild %s | %s | months in 1975-01..2010-12: %s | %.0fs" % (
        "PASS" if okr else "FAIL", getattr(RB, "VERSION", "?"), why, ", ".join("%s %d" % kv for kv in nm.items()),
        time.time() - t))
    if not okr:
        stop("the rebuild output breaks the interface (%s); no S4 line, no statistic" % why)
except SystemExit:
    raise
except Exception as e:  # noqa: BLE001
    stop("rebuild failed: %s" % frames(e))

# ---- 4. the registered run
try:
    t = time.time()
    res = CV.report(a1["R"], free["D"], a1["S"], free["gspc"], {"R": free["R"], "S": free["S"]}, rb, out=print,
                    facts=facts, trials_path=os.path.join(gm_dir, "trials.csv"),
                    rb_version=getattr(RB, "VERSION", "?"))
    print("report %.0fs" % (time.time() - t))
except CV.AsRunMismatch:
    stop("the A2-final book does not reproduce the A2 report (nothing else printed)")
except Exception as e:  # noqa: BLE001
    stop("report failed: %s" % frames(e))

# ---- 5. trial row
try:
    row = CV.trial_row(res, a1["panel_id"], CF.ENGINE_VERSION)
    print("TRIAL ROW " + json.dumps(row, sort_keys=True))
except Exception as e:  # noqa: BLE001
    stop("trial row failed: %s" % frames(e))
print("CORE V1 JOB DONE")
print("=== END === %.0fs" % (time.time() - T0))
