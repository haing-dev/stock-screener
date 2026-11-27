"""diag_plumbing: identity checks of tools/bbgq/lib/diag_a2.py on the FREE panel in the cloud (gm/CHANGES.md
"Diagnostics after A2" item 11). Prints differences and PASS / FAIL only: no Sharpe, mean, share, slope or gate of any
diagnostic (those are computed on the A1 panel by the PC job gm_diag_v1 only).

python3 tools/bbgq/diag_plumbing.py
Checks (A2-final config A1_INCUMBENT, free panel, design months, every loader cut at 2010-12-31):
  1. D2 rebuild of the positions from their intermediates = gm.book.run's positions (both paths of the engine)
  2. X2 / Carry 5 split: income + price = total for every leg
  3. theme scores (gm.signals.econ_theme_scores) reproduce the econ score E, and the theme parts add to the held
     Economic trend position
  4. D1 P&L markets = Trend's book markets without cm_aqr_ew (count)
"""
import contextlib
import io
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path[:0] = [REPO, os.path.join(HERE, "lib")]

import a1_panel as A1  # noqa: E402
import diag_a2 as DG  # noqa: E402
import gm_engine as GE  # noqa: E402


def main():
    from gm import config as CF
    from gm import execution as EX
    from gm import seal as SL
    from gm import signals as G
    t0 = time.time()
    M = GE.setup()
    free = A1.free_inputs(M)
    with GE.Cut(M, A1.SEAL), contextlib.redirect_stdout(io.StringIO()):
        ET = M["G"].econ_theme_scores(free["R"])
    T = SL.resolve(SL.DESIGN)
    R, D, S, gspc, ET = SL.cut_inputs(T, free["R"], free["D"], free["S"], free["gspc"], ET)
    cfg = CF.A1_INCUMBENT
    days = EX.nyse_days(gspc=gspc)
    bk = DG.book_k1(R, D, S, days, cfg)
    ok = True
    rb = DG.rebuild(R, D, S, cfg)
    r2 = DG.d2(rb, bk["pos"])
    p1 = r2["rebuild_diff"] <= 1e-12 and r2["rebuild_missing"] == 0
    ok &= p1
    print("%s D2 rebuild = book.run positions | max abs diff %.1e | missing pattern diff %d" % (
        "PASS" if p1 else "FAIL", r2["rebuild_diff"], r2["rebuild_missing"]))
    pos_v, pos_c = bk["fam_pos"]["value"], bk["fam_pos"]["carry"]
    mx = 0.0
    for pos in (pos_v, pos_c):
        for c, pre in G.CLASSES.items():
            cols = [k for k in pos.columns if k.startswith(pre)]
            tot, inc, pri, _cov = DG.income_split(pos, cols, S["C"], bk["R_earn"])
            if tot.notna().any():
                mx = max(mx, float((inc + pri - tot).abs().max()))
    p2 = mx < 1e-15
    ok &= p2
    print("%s X2 / Carry 5 split: income + price = total, every leg | max abs diff %.1e" % ("PASS" if p2 else "FAIL", mx))
    _contrib, sdiff, ediff = DG.theme_split(bk, S["E"], ET, bk["R_earn"])
    p3 = sdiff < 1e-12 and ediff < 1e-12
    ok &= p3
    print("%s theme split: theme parts add to the held Economic trend position (max diff %.1e); theme scores reproduce "
          "E (max diff %.1e)" % ("PASS" if p3 else "FAIL", sdiff, ediff))
    fam, _vol, _score = DG.trend_parts(R, D, S, cfg)
    allm, mk = DG.trend_markets(fam)
    p4 = len(mk) == 61 and len(allm) == 62 and "cm_aqr_ew" in allm
    ok &= p4
    print("%s D1 markets: %d Trend book markets, %d without cm_aqr_ew" % ("PASS" if p4 else "FAIL", len(allm), len(mk)))
    print("DIAG PLUMBING %s | %.0fs | no diagnostic statistic computed or printed" % ("PASS" if ok else "FAIL",
                                                                                      time.time() - t0))
    return ok


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
