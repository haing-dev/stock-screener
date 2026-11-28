"""gm_b2_v1: Batch B2 = Strip reversion and the ten card rule layers judged in B2 (TESTING_PROTOCOL 7.6 step 9;
gm/CHANGES.md "Batch B2", 2026-11-28) on the PC.

1. Checks (else STOP before any Bloomberg or LSEG value is read): gm code = the reference's (lib\\engine_ref.json);
   sha256 of lib\\engine_ref.json = the gm-2.2.1 reference; config.ENGINE_VERSION gm-2.2.1 and the four config hashes;
   lib files b2_batch.py, diag_preb.py, card_inputs.py, diag_a2.py, a2_batch.py, a1_panel.py, gm_engine.py,
   bbg_panel.py, bbgdata.py, lsegdata.py, lseg_rules.py and the five LSEG config lists = LIB_SHA (the lists also = the
   store manifest); the book / pod rows of lib\\gm\\trials.csv = the registered digest (42 rows); results\\gm_a2_v1.txt
   (A2 facts), gm_core_v1.txt (CORE BOOK V1 EMPTY), gm_diag_preb_v1.txt (PREB JOB DONE and the outcomes of entry item
   2), gm_b1_v1.txt (B1 JOB DONE, Curve carry SHELVED); Bloomberg store LOCK_v2; LSEG store LOCK_LSEG_v5 (manifest,
   before any table); work\\free\\gm_card_inputs.zip = LOCK_CARD_v1 file by file; free inputs = the shipped zip.
2. Free arm vs engine_ref.json; the A1 panel rebuilt, extension-only, id = the registered A1 PANEL ID, compared with
   work\\a1\\a1_panel_e7f98d4439fc.pkl when present; the A2-final book as run against the A2 report.
3. Free card inputs under the 2010-12-31 cut (panel.fx_usd_value, TB3MS and the 3-month rates of the pre-B job).
4. LSEG design part (diag_preb.LsegView as of 2010-12-31): the Eurodollar and Euribor daily contracts, the S&P 500
   forward EPS. Identity with the pre-B diagnostics (entry item 9; STOP on a difference); the B2 truncation gate at
   the 8 cut dates (entry item 10; STOP on a FAIL; PASS / FAIL and counts only).
5. b2_batch.report: DATA / WINDOW lines (counts), T1-T3 per item (T4 not applicable), the verdicts, the reported lines,
   the falsifiers, the netting report; values over >= 60 months only (else count and sign); no LSEG or Bloomberg value.
6. TRIAL ROW lines (13). Nothing is written to lib\\, to the Bloomberg or LSEG stores or to work\\a1\\;
   gm_engine.ensure_free_inputs (as in every job) rewrites work\\free\\inputs_manifest.json and unpacks missing free
   input files.
Needs: lib\\gm\\ (gm-2.2.1), lib\\gm_engine.py, lib\\bbgdata.py, lib\\bbg_panel.py, lib\\a1_panel.py, lib\\a2_batch.py,
lib\\diag_a2.py, lib\\diag_preb.py, lib\\card_inputs.py, lib\\b2_batch.py, lib\\lsegdata.py, lib\\lseg_rules.py (+ the
lsegdata config CSVs), lib\\engine_ref.json, work\\bbg\\ (LOCK_v2), work\\lseg\\ (LOCK_LSEG_v5), work\\free\\gm_free_inputs.zip,
work\\free\\gm_card_inputs.zip, results\\gm_a2_v1.txt, gm_core_v1.txt, gm_diag_preb_v1.txt, gm_b1_v1.txt; work\\a1\\
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
print("=== gm_b2_v1 ===")

# the registered build of the lib files (B2_BUILD hash table; gm/CHANGES.md "Batch B2" item 13)
LIB_SHA = {"b2_batch.py": "48b308d7f45f44edc36ddb2f8050656e65e5c625dadb8e139b2a83926e0130ae",
           "diag_preb.py": "2e9cadd9d41250b8009ca159e23fc69f5c73d44bc79dd9cca51cc8aa4a4ee102",
           "card_inputs.py": "4091f84bcbb11f43061bcc0330520a4a5580cb775895148a38849c0fbcab7b80",
           "diag_a2.py": "3264a5381c13b124d2566d02f263e21905f4e901680c1af7c2134f0bd558be1b",
           "a2_batch.py": "35339f673f351f43315ad3c7010ba733b6fb8990a6a41feb1ef20de324de58c6",
           "a1_panel.py": "eb9ef3f7fbd12760e174f9ef1df8573890bed6ca8d36f7d4e5c63eadd822ebb5",
           "gm_engine.py": "ac43a33cd8943719ba0efb9bb246473c7bbf59018a6d3b7398f64520eeebd721",
           "bbg_panel.py": "e0b67a42793e67c129ec8a6c3ed2082390933ea9317898b59b8854387ecf1dcd",
           "bbgdata.py": "0b26bb21b50671dca7c2153d3d66a2a09f7f33eeaa7c96ca536b69bbca8e6351",
           "lsegdata.py": "0d1b500ddb2e931ab4069ac8fd6fed0c16778da85b2665d3fcafadfae16198de",
           "lseg_rules.py": "5686999172a22c76b7190f8df210c93ffc09a6737f32301df030080dccc42da9",
           "lseg_engine_map.csv": "8812f20d4d6dadcbfe5171cbe92b03a57f65ba01599a6d17d842130864bbaa15",
           "lseg_exclusions.csv": "8e2ca054128ce420543d8e06252af14255a8492064a647e73e69dde90fb45bf9",
           "lseg_live_sources.csv": "37e42068a8ae7f36ee12ece245c3c17b6cc27ac6f51b52078d54e1a891c4c77f",
           "lseg_roots.csv": "7a8caf01fbc70108af78be145337b41ac7e0050fc3f326211c997dc1a9991ee3",
           "lseg_untouched.csv": "17ec5fb38c2cc3b3f337adac2478d04c100fb949bcbcfe159fd53f26ef705185"}
LSEG_CFG = ("lseg_engine_map.csv", "lseg_exclusions.csv", "lseg_live_sources.csv", "lseg_roots.csv",
            "lseg_untouched.csv")
CARD_ZIP = os.path.join(FREE, "gm_card_inputs.zip")      # LOCK_CARD_v1
CARD_ZIP_SHA = "4f84b01d07ad59da05ad7e8ca4e78b31b1ed687941c6852da804c685be1b068d"
N_PLACEBO = int(os.environ.get("B2_N_PLACEBO", "1000"))    # registered 1,000 (tests may lower it)


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
    import b2_batch as B2
    import diag_preb as PB
    import card_inputs as CIN
    import diag_a2 as DG
    import a2_batch as A2
    import a1_panel as A1
    import bbgdata
    import bbg_panel
    import gm_engine as GE
    import lsegdata as LD
    import lseg_rules as LR
    from gm import config as CF
    print("%s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | engine %s | %s" % (
        B2.VERSION, PB.VERSION, CIN.VERSION, DG.VERSION, A2.VERSION, A1.VERSION, bbgdata.VERSION, bbg_panel.VERSION,
        GE.VERSION, LD.VERSION, LR.VERSION, CF.ENGINE_VERSION,
        ", ".join("%s %s" % kv for kv in GE.lib_versions().items())))
    ref = json.load(open(os.path.join(LIB, "engine_ref.json"), encoding="utf-8"))
except Exception as e:  # noqa: BLE001
    stop("setup failed: %s" % frames(e))

if N_PLACEBO != B2.NPLACEBO:
    print("NOTE placebos %d (registered %d): a test run, not the registered run" % (N_PLACEBO, B2.NPLACEBO))

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
    print("%s lib engine_ref.json | sha256 %s | registered %s" % ("PASS" if got == B2.REF_SHA else "FAIL", got[:16],
                                                                 B2.REF_SHA[:16]))
    if got != B2.REF_SHA:
        stop("engine_ref.json is not the registered gm-2.2.1 reference")
    hs = {"BASE": CF.cfg_hash(CF.BASE), "CANDIDATE": CF.cfg_hash(CF.CANDIDATE),
          "A1_INCUMBENT": CF.cfg_hash(CF.A1_INCUMBENT), "A2_CHALLENGER": CF.cfg_hash(CF.A2_CHALLENGER)}
    okc = CF.ENGINE_VERSION == B2.ENGINE and hs == B2.CFG_HASHES and CF.A1_INCUMBENT["name"] == B2.FINAL_NAME
    print("%s engine %s and config hashes %s | registered %s, %s" % (
        "PASS" if okc else "FAIL", CF.ENGINE_VERSION, ", ".join("%s %s" % kv for kv in sorted(hs.items())), B2.ENGINE,
        ", ".join("%s %s" % kv for kv in sorted(B2.CFG_HASHES.items()))))
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
    okt = dg == B2.TRIAL_ROWS_SHA and nrow == B2.TRIAL_ROWS_N
    print("%s lib gm\\trials.csv book / pod rows | %d rows | digest %s | registered %d rows, %s" % (
        "PASS" if okt else "FAIL", nrow, dg[:16], B2.TRIAL_ROWS_N, B2.TRIAL_ROWS_SHA[:16]))
    if not okt:
        stop("the book / pod rows of the trial log differ from the registered ones")
    res_dir = os.environ.get("RESULTS_DIR", os.path.join(os.getcwd(), "results"))
    facts, why = DG.a2_facts(os.path.join(res_dir, B2.A2_REPORT))
    print("%s A2 report %s: %s" % ("PASS" if facts else "FAIL", B2.A2_REPORT, why))
    if not facts:
        stop("the gm_a2_v1 report is not usable (%s)" % why)
    for fn, chk, what in ((B2.CORE_REPORT, B2.core_facts, "B2 reads alpha against the EMPTY Core book v1"),
                          (B2.PREB_REPORT, B2.preb_facts, "B2's contents are the registered pre-B outcomes"),
                          (B2.B1_REPORT, B2.b1_facts, "7.6 step 9 runs after B1; Curve carry not moved")):
        okk, why = chk(os.path.join(res_dir, fn))
        print("%s report %s: %s" % ("PASS" if okk else "FAIL", fn, why))
        if not okk:
            stop("the %s report is not usable (%s): %s" % (fn, why, what))
    lock = bbgdata.Panel(WORK)
    print("%s Bloomberg store lock id %s | registered LOCK_v2 %s" % ("PASS" if lock.lock_id == B2.LOCK_V2 else "FAIL",
                                                                     lock.lock_id, B2.LOCK_V2))
    if lock.lock_id != B2.LOCK_V2:
        stop("the Bloomberg store is not LOCK_v2 (nothing read)")
    del lock
    lid, why = B2.lseg_lock_of(WORK)
    print("%s LSEG store lock id %s | registered LOCK_LSEG_v5 %s | %s" % (
        "PASS" if lid == B2.LSEG_LOCK else "FAIL", lid, B2.LSEG_LOCK, why))
    if lid != B2.LSEG_LOCK:
        stop("the LSEG store is not LOCK_LSEG_v5 (nothing read)")
    man = json.load(open(os.path.join(WORK, "lseg", "manifest.json"), encoding="utf-8"))
    badc = [n for n in LSEG_CFG if (man.get("config") or {}).get(n) != LIB_SHA[n]]
    print("%s LSEG config lists in lib = the store manifest's config hashes | %d files | differing: %s" % (
        "PASS" if not badc else "FAIL", len(LSEG_CFG), ", ".join(badc) or "none"))
    if badc:
        stop("the LSEG config lists differ from the locked ones (nothing read)")
    if not os.path.exists(CARD_ZIP):
        stop("work\\free\\gm_card_inputs.zip not found (LOCK_CARD_v1)")
    try:
        CI_ = CIN.Inputs.from_zip(CARD_ZIP)
    except CIN.CardInputsError as e:
        print("FAIL card inputs: %s" % type(e).__name__)
        stop("the card inputs zip is not LOCK_CARD_v1")
    okci = CI_.lock_id == B2.CARD_LOCK == CIN.LOCK_ID
    print("%s card inputs gm_card_inputs.zip | %d files, each = its LOCK_CARD_v1 sha256 | lock id %s | registered %s" % (
        "PASS" if okci else "FAIL", len(CIN.FILES), CI_.lock_id[:16], B2.CARD_LOCK[:16]))
    if not okci:
        stop("the card inputs lock id is not LOCK_CARD_v1")
    zs = sha(CARD_ZIP)
    print("%s card inputs zip sha256 %s | LOCK_CARD_v1 zip_sha256 %s | informational (content pinned file by file)" % (
        "PASS" if zs == CARD_ZIP_SHA else "NOTE", zs[:16], CARD_ZIP_SHA[:16]))
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
    ok = a1["panel_id"] == B2.A1_PANEL_ID
    print("%s A1 PANEL ID %s | registered %s" % ("PASS" if ok else "FAIL", a1["panel_id"], B2.A1_PANEL_ID))
    if not ok:
        stop("the rebuilt A1 panel is not the registered one")
    cmp_ = A2.compare_saved(WORK, a1)
    print("%s A1 panel file work\\a1\\a1_panel_%s.pkl: %s" % ("FAIL" if cmp_.startswith("differs") else "PASS",
                                                              a1["panel_id"][:12], cmp_ if cmp_ != "absent" else
                                                              "absent (the rebuild, id checked, is used; nothing "
                                                              "written)"))
    if cmp_.startswith("differs"):
        stop("the saved A1 panel differs from the rebuild (%s)" % cmp_)
    from gm import execution as EX
    from gm import seal as SL
    R, D, S, gspc = SL.cut_inputs(SL.resolve(SL.DESIGN), a1["R"], free["D"], a1["S"], free["gspc"])
    days = EX.nyse_days(gspc=gspc)
    DG.as_run(R, D, S, days, CF.A1_INCUMBENT, facts, print)
except SystemExit:
    raise
except DG.AsRunMismatch:
    stop("the A2-final book does not reproduce the A2 report (nothing else printed)")
except Exception as e:  # noqa: BLE001
    stop("A1 panel / A2-final book failed: %s" % frames(e))

# ---- 3. free card inputs under the 2010-12-31 cut
try:
    import pandas as pd
    P = M["P"]
    with GE.Cut(M, A1.SEAL), contextlib.redirect_stdout(io.StringIO()):
        fxv = pd.DataFrame({c: P.fx_usd_value(c) for c in PB.R5_CUR})
        rates = {"TB3MS": P.F("TB3MS")}
        for cc, names in PB.RATE_SERIES.items():
            rates[cc] = P.first(*[P.F(n) for n in names])
    print("card inputs | fx values %s | TB3MS %s.. (%d)" % (
        ", ".join("%s %d months" % (c, int(fxv[c].notna().sum())) for c in fxv.columns),
        rates["TB3MS"].first_valid_index(), int(rates["TB3MS"].notna().sum())))
except Exception as e:  # noqa: BLE001
    stop("card inputs failed: %s" % frames(e))

# ---- 4. LSEG design part, identity with the pre-B diagnostics, the B2 truncation gate
try:
    t = time.time()
    lseg = PB.LsegView(LD.Panel(WORK))
    if lseg.panel.lock_id != B2.LSEG_LOCK:
        stop("the loaded LSEG store is not LOCK_LSEG_v5")
    con = B2.strip_contracts(lseg)
    contracts = {r: {k: lseg.daily(s) for k, s in c.items()} for r, c in con.items()}
    eps = lseg.monthly(PB.EPS_SID)
    print("LSEG | strip contracts %s | forward EPS months %d" % (
        ", ".join("%s %d" % (r, len(c)) for r, c in con.items()), int(eps.notna().sum())))
    sp = B2.strip_prepare(contracts, days)
    r1 = PB.r1(contracts["ED"], days)
    badi, mine = B2.strip_identity(sp, r1)
    print("%s IDENTITY Strip reversion vs diag_preb.r1 | eligible %d / %d | qualifying %d / %d | differing fields: %s" % (
        "PASS" if not badi else "FAIL", mine["eligible"], r1["eligible"], mine["qualifying"], r1["qualifying"],
        ", ".join(badi) or "none"))
    inp = B2.card_inputs_view(R, D, gspc, CI_, fxv, rates["TB3MS"], eps, days)
    rules = B2.card_rules(inp)
    idn = B2.identity(inp, rules, rates)
    for name in B2.RULES:
        okn, det = idn[name]
        print("%s IDENTITY %s vs diag_preb 1.1.1 | %s" % ("PASS" if okn else "FAIL", name, det))
    f0bad = []
    for name in B2.RULES:
        f, _m = B2.f0_b2(rules[name], B2.rule_run(rules[name], inp))
        print("%s F0 on the B2 positions | %s | held months %d | episodes %d | %s" % (
            "PASS" if f["judgeable"] else "FAIL", name, f["held"], f["episodes"],
            "judged in B2 (= pre-B)" if f["judgeable"] else "NOT the pre-B outcome"))
        f0bad += [] if f["judgeable"] else [name]
    if badi or not all(v[0] for v in idn.values()) or f0bad:
        stop("the B2 positions are not the pre-B positions (no statistic printed)")
    print("identity %.0fs" % (time.time() - t))
    t = time.time()
    ok, _tr = B2.truncation(lambda T: B2.build_cut(T, R, D, gspc, CI_, fxv, rates["TB3MS"], eps, contracts),
                            GE.CUT_DATES, print)
    print("%s B2 truncation | %d cut dates | %.0fs" % ("PASS" if ok else "FAIL", len(GE.CUT_DATES), time.time() - t))
    if not ok:
        stop("B2 fails the truncation test (no statistic printed)")
except SystemExit:
    raise
except Exception as e:  # noqa: BLE001
    stop("LSEG / identity / truncation failed: %s" % frames(e))

# ---- 5. the registered B2 run
try:
    t = time.time()
    res = B2.report(sp, rules, inp, R["eq_us_spx"], out=print, trials_path=os.path.join(gm_dir, "trials.csv"),
                    n_placebo=N_PLACEBO)
    print("report %.0fs" % (time.time() - t))
except SystemExit:
    raise
except Exception as e:  # noqa: BLE001
    stop("report failed: %s" % frames(e))

# ---- 6. trial rows
try:
    for row in B2.trial_rows(res, CF.ENGINE_VERSION):
        print("TRIAL ROW " + json.dumps(row, sort_keys=True))
except Exception as e:  # noqa: BLE001
    stop("trial rows failed: %s" % frames(e))
print("B2 JOB DONE")
print("=== END === %.0fs" % (time.time() - T0))
