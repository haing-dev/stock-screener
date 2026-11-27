"""core_plumbing: identity checks of tools/bbgq/lib/core_v1.py on the FREE panel in the cloud (gm/CHANGES.md "Core book
v1" item 8). Prints differences, ids, counts and PASS / FAIL only: no Sharpe, mean, alpha, p-value, placebo share,
drawdown or verdict of any part or book (those are computed on the A1 panel by the PC job gm_core_v1 only).

python3 tools/bbgq/core_plumbing.py [--rebuild]
--rebuild: also run tools/bbgq/lib/rebuild_s4.py (the independent rebuild) on the free-panel interface inputs and print
only whether its output passes the interface checks (keys, index, cut, months); for the coordinator before REBUILD_SHA
is registered. No statistic of the rebuild or the engine is printed.
Checks (A2-final config A1_INCUMBENT, free panel, design months, every loader cut at 2010-12-31):
  1. the Core and shadow masks partition each pod's components (positions add up exactly)
  2. the identity date map of the placebo engine reproduces each part alone exactly (S1 / T3 plumbing)
  3. the S4 interface inputs build with the documented keys and shapes; the stub rebuild's output validates
     (tests/data/rebuild_s4_stub.py; the independent rebuild is NOT run here)
  4. the live-source check runs: markets held at the 2010-12 decision per Core candidate and missing free inputs
"""
import contextlib
import io
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path[:0] = [REPO, os.path.join(HERE, "lib"), os.path.join(REPO, "tests", "data")]

import a1_panel as A1  # noqa: E402
import core_v1 as CV  # noqa: E402
import gm_engine as GE  # noqa: E402
import rebuild_s4_stub as STUB  # noqa: E402


def main():
    from gm import book as B
    from gm import config as CF
    from gm import execution as EX
    from gm import seal as SL
    t0 = time.time()
    M = GE.setup()
    free = A1.free_inputs(M)
    T = SL.resolve(SL.DESIGN)
    R, D, S, gspc = SL.cut_inputs(T, free["R"], free["D"], free["S"], free["gspc"])
    cfg = CF.A1_INCUMBENT
    days = EX.nyse_days(gspc=gspc)
    MK = CV.masks()
    ok = True
    with contextlib.redirect_stdout(io.StringIO()):
        _, _vol, comp = B.family_positions(R, cfg, D, S, components=True)
    worst = 0.0
    for pod in ("trend", "econ", "carry", "value"):
        allc = B.mask_components(comp, [(pod, "*", "*")])
        got = {}
        for p in CV.CORE + CV.SHADOW:
            for key, v in B.mask_components(comp, [x for x in MK[p] if x[0] == pod]).items():
                got[key] = got.get(key, 0) + v.fillna(0)
        for key, v in allc.items():
            worst = max(worst, float((got.get(key, 0) - v.fillna(0)).abs().max().max()))
    p1 = worst < 1e-15
    ok &= p1
    print("%s masks: Core + shadow parts partition each pod's components | max abs diff %.1e" % (
        "PASS" if p1 else "FAIL", worst))
    worst, miss = 0.0, 0
    for p in CV.CORE + CV.SHADOW:
        bk = CV.alone(R, D, S, days, cfg, MK[p])
        w = CV.window(bk["net"])
        fn = B.placebo_net_fn(R, cfg, D, S, str(w.index[0]), runner=EX.run_k1, days=days, parts={"alone": MK[p]})
        with contextlib.redirect_stdout(io.StringIO()):
            x = fn(None)
        d = (x - bk["net"]).abs().max()
        miss += int((x.isna() != bk["net"].isna()).sum())
        worst = max(worst, float(d if d == d else 0.0))
    p2 = worst == 0.0 and miss == 0
    ok &= p2
    print("%s S1 / T3: the identity date map reproduces each of the %d parts alone | max abs diff %.1e | missing "
          "pattern diff %d" % ("PASS" if p2 else "FAIL", len(CV.CORE + CV.SHADOW), worst, miss))
    inp = CV.rebuild_inputs(R, D, S, days, cfg, {"config": cfg["name"]})
    need = {"R", "D", "days", "C", "V", "vol", "cost", "em_borrow", "classes", "meta"}
    p3 = set(inp) == need and inp["R"].shape[1] == inp["vol"].shape[1] and set(inp["cost"]) == set(inp["R"].columns)
    okv, why, nm = CV.validate_rebuild(STUB.part_returns(inp))
    p3 = p3 and okv
    ok &= p3
    print("%s S4 interface inputs: %s | stub output validates: %s (months per key in 1975-2010: %s)" % (
        "PASS" if p3 else "FAIL", " | ".join("%s %s" % (k, getattr(v, "shape", len(v) if hasattr(v, "__len__") else ""))
                                             for k, v in inp.items()), why, ", ".join("%d" % v for v in nm.values())))
    for p in CV.CORE:
        bk = CV.alone(R, D, S, days, cfg, MK[p])
        okl, held, ms = CV.live_check(bk["pos"], p, R, S)
        print("%s live-source check runs | %s | held at %s: %d markets | missing free inputs: %s" % (
            "PASS" if held else "FAIL", p, CV.LAST_DECISION, len(held), ", ".join("%s (%s)" % m for m in ms) or "none"))
        ok &= bool(held)
    if "--rebuild" in sys.argv:
        import rebuild_s4 as RB
        fb = CV.forbidden_imports(os.path.join(HERE, "lib", "rebuild_s4.py"))
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            out = RB.part_returns(CV.rebuild_inputs(R, D, S, days, cfg, {"config": cfg["name"]}), cut="2010-12-31")
        okr, why, nm = CV.validate_rebuild(out)
        p5 = okr and not fb
        ok &= p5
        print("%s real rebuild %s on the free-panel inputs: forbidden imports %s | interface %s | months per key: %s" % (
            "PASS" if p5 else "FAIL", getattr(RB, "VERSION", "?"), ", ".join(fb) or "none", why,
            ", ".join("%s %d" % kv for kv in nm.items())))
    print("CORE PLUMBING %s | %.0fs | no statistic of any part or book computed or printed" % (
        "PASS" if ok else "FAIL", time.time() - t0))
    return ok


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
