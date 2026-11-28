"""b1_trunc_mock: the Batch B1 pod truncation gate (gm/CHANGES.md "Batch B1: Curve carry" item 7) in the cloud, on the
MOCK LSEG store of tests/b1_curve_smoke.py (invented contract prices; no LSEG value). At the 8 cut dates of
gm_engine.CUT_DATES the pod is rebuilt with every observation dated after T removed and compared stage by stage with
the full run for months <= T. Prints PASS / FAIL and counts only. The PC job gm_b1_v1 runs the same gate on
LOCK_LSEG_v5 before any statistic.
python3 tools/bbgq/b1_trunc_mock.py"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path[:0] = [REPO, os.path.join(HERE, "lib"), os.path.join(REPO, "tools", "lseg"), os.path.join(REPO, "tests")]

import b1_curve as BC  # noqa: E402
import b1_curve_smoke as SM  # noqa: E402
import gm_engine as GE  # noqa: E402

if __name__ == "__main__":
    cat, long, roots, _truth = SM.build_mock()
    tab = BC.contract_table(cat, long, roots)
    prep = BC.prepare(tab)
    ok, res = BC.truncation(cat, long, roots, GE.CUT_DATES, print, full=(tab, prep, BC.run(prep)))
    print("%s | %s | mock store (invented prices) | cut dates %d | stages per date %d | B1 POD TRUNCATION %s" % (
        BC.VERSION, GE.VERSION, len(GE.CUT_DATES), next(iter(res.values()))[1], "PASS" if ok else "FAIL"))
