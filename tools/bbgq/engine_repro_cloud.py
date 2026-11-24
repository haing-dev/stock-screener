"""engine_repro_cloud: k = 0 reproduction of the reference (tools/bbgq/engine_ref.json) in the cloud on the repo cache.

python3 tools/bbgq/engine_repro_cloud.py [REF]       (default REF = tools/bbgq/engine_ref.json)
Runs gm_engine.run (sealed design run, BASE and CANDIDATE at k = 0, the existing paths only), takes the design-period
fingerprint and compares it item by item with the reference (gm_engine.compare: 24 items). Prints only PASS / FAIL,
counts and the largest absolute difference per item: no statistic of any path is printed.
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path[:0] = [REPO, os.path.join(HERE, "lib")]

import gm_engine as GE  # noqa: E402


def main(ref_path):
    ref = json.load(open(ref_path, encoding="utf-8"))
    t0 = time.time()
    M = GE.setup()
    res = GE.run(M=M)
    fp = GE.fingerprint(res, M)
    rows = GE.compare(fp, ref)
    print("engine %s | reference %s (made %s, gm commit %s) | run %.0fs" % (
        GE.VERSION, os.path.basename(ref_path), ref.get("made"), ref["code"]["gm_commit"][:10], time.time() - t0))
    for r in rows:
        print("%s | %-70s | n %4d | missing %d | max abs diff %.1e | tol %.0e" % (
            "PASS" if r["pass"] else "FAIL", r["item"][:70], r["n"], r["missing"], r["maxdiff"], r["tol"]))
    npass = sum(r["pass"] for r in rows)
    mx = max(r["maxdiff"] for r in rows)
    print("REPRO SUMMARY | %d of %d items PASS | largest difference over all items %.1e | %s" % (
        npass, len(rows), mx, "REPRODUCTION PASS" if npass == len(rows) else "REPRODUCTION FAIL"))
    return npass == len(rows), mx


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "engine_ref.json"))
