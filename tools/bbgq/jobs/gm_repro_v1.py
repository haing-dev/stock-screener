"""gm_repro_v1: run the book engine (gm/, unchanged) on the PC on the shipped free inputs and compare it with the cloud
reference lib\\engine_ref.json (WORKFLOW v2.1 step 0.5, gate "match within tolerance"). DESIGN PERIOD ONLY: every
compared number is computed from months up to 2010-12 (gm computes later months internally; they are never printed).
Prints per item PASS / FAIL with the largest absolute difference and the tolerance (book returns 1e-8, positions 1e-6,
statistics 1e-6, counts exact), the library versions and the run time. No data value is printed.
Needs: lib\\gm\\ (gm package), lib\\gm_engine.py, lib\\engine_ref.json, work\\free\\gm_free_inputs.zip (unpacked on first
use into work\\free\\research and work\\free\\raw)."""
import os
import sys

sys.path[:0] = [os.path.join(os.getcwd(), "lib"), os.path.join(os.getcwd(), "pylib")]

import json  # noqa: E402
import time  # noqa: E402
import traceback  # noqa: E402

T0 = time.time()
WORK = os.environ.get("BBG_WORK", os.path.join(os.getcwd(), "work"))
FREE = os.path.join(WORK, "free")
print("=== gm_repro_v1 ===")
try:
    import gm_engine as GE
    print("gm_engine", GE.VERSION, "| " + ", ".join("%s %s" % kv for kv in GE.lib_versions().items()))
    ref = json.load(open(os.path.join(os.getcwd(), "lib", "engine_ref.json"), encoding="utf-8"))
    print("reference: gm commit %s, libraries %s" % (ref["code"]["gm_commit"][:10], ", ".join(
        "%s %s" % kv for kv in ref["libraries"].items())))
except Exception as e:  # noqa: BLE001
    print("SETUP FAILED", type(e).__name__, str(e)[:300])
    print("=== END === %.0fs" % (time.time() - T0))
    sys.exit(0)

n_fail = 0
# ---- code: the gm package on the PC is the one the reference ran
try:
    import gm
    here = GE.gm_code_hashes(os.path.dirname(os.path.abspath(gm.__file__)))
    want = ref["code"]["gm_files_sha256"]
    bad = sorted(k for k in set(here) | set(want) if here.get(k) != want.get(k))
    print("%s gm code | %d files compared | differing or missing: %s" % ("PASS" if not bad else "FAIL", len(want),
                                                                          ", ".join(bad) or "none"))
    n_fail += bool(bad)
    if "gm_data_sha256" in ref["code"]:
        hd, wd = GE.gm_data_hashes(os.path.dirname(os.path.abspath(gm.__file__))), ref["code"]["gm_data_sha256"]
        badd = sorted(k for k in set(hd) | set(wd) if hd.get(k) != wd.get(k))
        print("%s gm data files | %d compared | differing or missing: %s" % ("PASS" if not badd else "FAIL", len(wd),
                                                                              ", ".join(badd) or "none"))
        n_fail += bool(badd)
    cfg = GE.config_hashes()
    badc = [k for k in cfg if cfg[k] != ref["configs"].get(k)]
    print("%s config hashes | %s" % ("PASS" if not badc else "FAIL", ", ".join("%s %s" % kv for kv in cfg.items())))
    n_fail += bool(badc)
except Exception as e:  # noqa: BLE001
    print("FAIL gm code check", type(e).__name__, str(e)[:200])
    n_fail += 1

# ---- inputs: unpack if needed, verify against the shipped manifest and the reference file list
try:
    t = time.time()
    st = GE.ensure_free_inputs(FREE)
    if st["manifest"] is None:
        raise RuntimeError("work\\free\\gm_free_inputs.zip not found")
    man = st["manifest"]
    same, how = GE.inputs_match(man, ref)
    ok = not st["bad"] and same
    print("%s free inputs | %d files | already in place %d | unpacked now %d | not matching the manifest %d | "
          "%s %s the reference | %d converted xls | %.0fs" % (
              "PASS" if ok else "FAIL", len(man["files"]), st["ok"], st["extracted"], len(st["bad"]), how,
              "match" if same else "DO NOT MATCH", len(man.get("converted", [])), time.time() - t))
    if st["bad"]:
        print("   not matching: " + ", ".join(st["bad"][:20]))
    n_fail += not ok
except Exception as e:  # noqa: BLE001
    print("FAIL free inputs", type(e).__name__, str(e)[:300])
    print("=== END === %.0fs" % (time.time() - T0))
    sys.exit(0)

# ---- engine run and comparison (design period only)
try:
    t = time.time()
    res = GE.run(free_dir=FREE)
    print("engine run %.0fs (panel, signals, daily, BASE and CANDIDATE books)" % (time.time() - t))
    fp = GE.fingerprint(res)
    rows = GE.compare(fp, ref)
    print("--- comparison with the reference (design period; max abs diff vs tolerance)")
    for r in rows:
        print("%s %s | values %d | missing or extra %d | max abs diff %.1e | tol %.0e" % (
            "PASS" if r["pass"] else "FAIL", r["item"], r["n"], r["missing"], r["maxdiff"], r["tol"]))
    nf = sum(1 for r in rows if not r["pass"])
    n_fail += nf
    grp = {}
    for r in rows:
        g = r["item"].split(" (")[0].split(" |")[0]
        grp[g] = max(grp.get(g, 0.0), r["maxdiff"])
    print("REPRO SUMMARY | items %d | pass %d | fail %d | largest diff per group: %s" % (
        len(rows), len(rows) - nf, nf, ", ".join("%s %.1e" % kv for kv in grp.items())))
except Exception as e:  # noqa: BLE001
    print("FAIL engine run", type(e).__name__, str(e)[:300])
    print("".join(traceback.format_exc().splitlines(True)[-8:]))
    n_fail += 1
print("REPRODUCTION %s" % ("PASS" if n_fail == 0 else "FAIL (%d failed checks)" % n_fail))
print("=== END === %.0fs" % (time.time() - T0))
