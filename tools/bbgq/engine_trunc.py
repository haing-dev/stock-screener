"""engine_trunc: truncation test of the book engine (WORKFLOW v2.1 step 0.5, gate "truncation test passes").

python3 tools/bbgq/engine_trunc.py [YYYY-MM-DD ...]     (default: gm_engine.CUT_DATES, 1980-2010)
Same code as the PC job jobs/gm_trunc_v1.py (gm_engine.truncation_report), here on the repo cache.

For each cut date T the engine is rerun with every input cut at T at the LOADER level (no observation dated after T
reaches gm; gm's rules are not touched) and every stage is compared with the full run for decision months <= T:
panel returns, the signal families (econ, carry, value, price trend), the volatility estimates, the family positions,
the positions and the book returns, for BASE and CANDIDATE. A second pass runs each stage ALONE (its inputs taken from
the full run and cut at T), which separates a stage's own look-ahead from one inherited from an earlier stage. Every
failure is attributed to a place in the code (gm_engine.CAUSES) with a one-line proposed fix. Nothing is fixed.
Design period only: compared months end at min(T, 2010-12).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path[:0] = [REPO, os.path.join(HERE, "lib")]

import gm_engine as GE  # noqa: E402

if __name__ == "__main__":
    dates = sys.argv[1:] or list(GE.CUT_DATES)
    GE.truncation_report(None, dates, print)
