"""b2_trunc_mock: the Batch B2 truncation gate (gm/CHANGES.md "Batch B2" item 10) in the cloud, on the synthetic panel,
invented card inputs and the MOCK LSEG strips of tests/b2_mocks.py (no LSEG, Bloomberg or FRED value). At the 8 cut
dates of gm_engine.CUT_DATES every B2 path (Strip reversion and the ten rule layers) is rebuilt with every input dated
after T removed and compared stage by stage with the full run; then the two planted look-aheads (controls) must FAIL.
Prints PASS / FAIL and counts only. The PC job gm_b2_v1 runs the same gate on the registered inputs before any statistic.
python3 tools/bbgq/b2_trunc_mock.py"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path[:0] = [REPO, os.path.join(HERE, "lib"), os.path.join(REPO, "tools", "lseg"), os.path.join(REPO, "tests")]

import b2_batch as B2  # noqa: E402
import b2_batch_smoke as SM  # noqa: E402
import b2_mocks as M  # noqa: E402
import gm_engine as GE  # noqa: E402

if __name__ == "__main__":
    m = M.inputs(late=True)
    b = SM.build(m)

    def bc(plant):
        return lambda T: B2.build_cut(T, b["R"], b["D"], b["gspc"], m["ci"], b["fxv"], b["tb3"], b["eps"],
                                      b["contracts"], plant=plant)
    ok, res = B2.truncation(bc(None), GE.CUT_DATES, print)
    c1, _r = B2.truncation(bc("vol_next"), GE.CUT_DATES[-2:-1], print, label="CONTROL vol_next")
    c2, _r = B2.truncation(bc("normal_next"), GE.CUT_DATES[-2:-1], print, label="CONTROL normal_next")
    print("%s | %s | mock inputs (invented) | cut dates %d | stages per date %d | B2 TRUNCATION %s | controls %s" % (
        B2.VERSION, GE.VERSION, len(GE.CUT_DATES), next(iter(res.values()))[1], "PASS" if ok else "FAIL",
        "FAIL as required" if (not c1 and not c2) else "DID NOT FAIL"))
