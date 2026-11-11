"""gm_trunc_v1: truncation test of the book engine on the PC (WORKFLOW v2.1 step 0.5, gate "truncation test passes").
Same code as tools/bbgq/engine_trunc.py (gm_engine.truncation_report) on the shipped free inputs (work\\free).
For each cut date T (1980-2010): every input cut at T at the loader level, every stage compared with the full run for
decision months <= T (counts of differing market-months, largest absolute difference, first and last differing
month, market names), each stage also run ALONE to separate its own look-ahead from an inherited one, and every failure
attributed to a place in the gm code with a proposed fix. Design period only. No data value is printed."""
import os
import sys

sys.path[:0] = [os.path.join(os.getcwd(), "lib"), os.path.join(os.getcwd(), "pylib")]

import time  # noqa: E402
import traceback  # noqa: E402

T0 = time.time()
WORK = os.environ.get("BBG_WORK", os.path.join(os.getcwd(), "work"))
FREE = os.path.join(WORK, "free")
print("=== gm_trunc_v1 ===")
try:
    import gm_engine as GE
    print("gm_engine", GE.VERSION, "| " + ", ".join("%s %s" % kv for kv in GE.lib_versions().items()))
    st = GE.ensure_free_inputs(FREE)
    if st["manifest"] is None:
        raise RuntimeError("work\\free\\gm_free_inputs.zip not found")
    print("free inputs: %d files, unpacked now %d, not matching the manifest %d" % (
        len(st["manifest"]["files"]), st["extracted"], len(st["bad"])))
    dates = [a for a in sys.argv[1:] if a[:2] in ("19", "20")] or list(GE.CUT_DATES)
    GE.truncation_report(FREE, dates, print)
except Exception as e:  # noqa: BLE001
    print("TRUNCATION TEST STOPPED", type(e).__name__, str(e)[:300])
    print("".join(traceback.format_exc().splitlines(True)[-8:]))
print("=== END === %.0fs" % (time.time() - T0))
