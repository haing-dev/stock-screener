"""Smoke test for block 3 (WORKFLOW v2.1 step 0.5): the book engine packaged for the PC.

1. builds tools/bbgq/engine_pkg (build_engine.py), lays it out like Documents\\WRDS results\\local in a temp folder and
   runs jobs/gm_repro_v1.py there as the PC runner does: must print REPRODUCTION PASS against lib/engine_ref.json;
   with BBGQ_ALT_PYTHON=<python of another environment, e.g. pandas 3.1.1 / numpy 2.5.4 without xlrd> it runs the job
   there too;
2. one truncation date with jobs/gm_trunc_v1.py: the cut must be complete (no input after T reaches the engine), no
   stage may fail on its own (every failure inherited from the inputs), and the known causes must be named;
3. the Bloomberg adapter on mock workbooks (tests/bbgq_smoke.make_mocks): jobs/gm_bbg_map_v1.py, the as-of guard, held-back
   markets invisible, and an engine run with Bloomberg commodity inputs that leaves every other market's returns unchanged;
4. a whitelist scan of every job output: no line with a date and a decimal value, no date after 2010.
Design period only. python3 tests/bbgq_engine_smoke.py [--keep]   prints "BBGQ ENGINE SMOKE OK" (about 12 minutes)
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BBGQ = os.path.join(REPO, "tools", "bbgq")
PKG = os.path.join(BBGQ, "engine_pkg")
TRUNC_DATE = "1995-12-31"
DATE_RE = re.compile(r"\b(19|20)\d{2}-\d{2}(-\d{2})?\b")
LATE_RE = re.compile(r"\b20(1[1-9]|[2-9]\d)-(0[1-9]|1[0-2])\b")
DEC_RE = re.compile(r"(?<![\w.])-?\d+\.\d+(?![\w.])")


def scan(text, name):
    bad = []
    for line in text.splitlines():
        if DATE_RE.search(line) and DEC_RE.search(line):
            bad.append("dated line with a decimal value: " + line[:140])
        if LATE_RE.search(line):
            bad.append("date after 2010: " + line[:140])
    assert not bad, "%s output breaks the whitelist: %s" % (name, bad[:5])


def run_job(local, name, args=(), python=None, bbg_dir=""):
    env = dict(os.environ, BBG_DIR=bbg_dir, BBG_WORK=os.path.join(local, "work"),
               PYTHONPATH=os.path.join(local, "lib") + os.pathsep + os.path.join(local, "pylib"))
    t = time.time()
    p = subprocess.run([python or sys.executable, os.path.join("jobs", name + ".py")] + list(args), cwd=local, env=env,
                       capture_output=True, text=True, timeout=3600)
    assert p.returncode == 0, "%s exit %d: %s" % (name, p.returncode, p.stderr[-2000:])
    assert "=== END ===" in p.stdout, "%s did not finish:\n%s\n%s" % (name, p.stdout[-3000:], p.stderr[-2000:])
    print("  %s ok in %.0fs (%d lines)" % (name, time.time() - t, p.stdout.count("\n")))
    return p.stdout


def main():
    keep = "--keep" in sys.argv
    tmp = tempfile.mkdtemp(prefix="bbgq_engine_")
    try:
        # 1. package and reproduction
        p = subprocess.run([sys.executable, os.path.join(BBGQ, "build_engine.py")], capture_output=True, text=True,
                           timeout=1800)
        assert p.returncode == 0 and "engine_pkg built" in p.stdout, p.stdout[-2000:] + p.stderr[-2000:]
        print("  " + p.stdout.splitlines()[0])
        local = os.path.join(tmp, "local")
        os.makedirs(os.path.join(local, "pylib"))
        for d in ("lib", "jobs", "work"):
            shutil.copytree(os.path.join(PKG, d), os.path.join(local, d))
        out_r = run_job(local, "gm_repro_v1")
        assert "REPRODUCTION PASS" in out_r and "FAIL" not in out_r, out_r[-3000:]
        assert "unpacked now 239" in out_r or re.search(r"unpacked now \d+", out_r), out_r[:2000]
        print("  " + [ln for ln in out_r.splitlines() if ln.startswith("REPRO SUMMARY")][0][:150])
        outs = {"gm_repro_v1": out_r}
        alt = os.environ.get("BBGQ_ALT_PYTHON")
        if alt:
            out_a = run_job(local, "gm_repro_v1", python=alt)
            vers = [ln for ln in out_a.splitlines() if ln.startswith("gm_engine")][0]
            assert "REPRODUCTION PASS" in out_a, out_a[-3000:]
            print("  other environment (%s): REPRODUCTION PASS" % vers.split("| ")[1])
            outs["gm_repro_v1 (other python)"] = out_a

        # 2. one truncation date
        out_t = run_job(local, "gm_trunc_v1", [TRUNC_DATE])
        assert "CUT %s | inputs after T seen by the engine: none" % TRUNC_DATE in out_t, out_t[-3000:]
        m = re.search(r"TRUNC %s \| (PASS|FAIL) \| end-to-end failing stages (\d+) of (\d+) \| stages failing alone "
                      r"(\d+)" % TRUNC_DATE, out_t)
        assert m, out_t[-3000:]
        assert m.group(4) == "0", "a stage fails on its own (look-ahead inside gm rules):\n" + out_t[-4000:]
        for cid in ("C1 |", "C2 |", "C3 |"):
            assert cid in out_t, "cause %s not reported:\n%s" % (cid, out_t[-4000:])
        assert "not attributed" not in out_t and "unattributed" not in out_t, out_t[-4000:]
        print("  truncation at %s: %s, %s of %s stages differ end-to-end, 0 alone; causes C1 C2 C3 named" % (
            TRUNC_DATE, m.group(1), m.group(2), m.group(3)))
        outs["gm_trunc_v1"] = out_t

        # 3. Bloomberg adapter on mock workbooks
        sys.path.insert(0, os.path.join(REPO, "tests"))
        import bbgq_smoke as BS
        bbg = os.path.join(tmp, "pulled results")
        truth = {"release": {}}
        t = time.time()
        BS.make_mocks(bbg, truth)
        print("  mock workbooks written in %.0fs" % (time.time() - t))
        shutil.copy(os.path.join(BBGQ, "jobs", "bbg_build_v1.py"), os.path.join(local, "jobs"))
        run_job(local, "bbg_build_v1", bbg_dir=bbg)
        out_m = run_job(local, "gm_bbg_map_v1")
        assert "MAP FAILED" not in out_m and "DRY RUN FAILED" not in out_m, out_m[-3000:]
        assert re.search(r"markets whose RETURN would come from Bloomberg: 1[0-9]", out_m), out_m[-3000:]
        assert "SPGSCCP Index|PX_LAST | held back" in out_m          # alternative commodity: untouched, invisible
        assert "SHEET Returns" in out_m and "SHEET Curves" in out_m
        outs["gm_bbg_map_v1"] = out_m
        for name, out in outs.items():
            scan(out, name)
            bad = BS.whitelist_scan(out, truth["values"])
            assert not bad, "%s prints mock values: %s" % (name, bad[:3])

        sys.path[:0] = [os.path.join(local, "lib")]
        import bbgdata
        import bbg_panel as BP
        import gm_engine as GE
        work = os.path.join(local, "work")
        try:
            BP.Source(work, asof="2011-01-31")
            raise AssertionError("adapter served a date after the seal")
        except bbgdata.HoldoutSealed:
            pass
        src = BP.Source(work, asof="2010-12-31")
        cm = [k for k in GE.gm_modules()["BBG"].COMMOD_ER if k not in GE.gm_modules()["BBG"].ALT_COMMOD]
        wb = src.workbook(markets=cm, sheets=("Returns", "Curves"))
        assert "SPGSCLP Index" in wb["Returns"] and "SPGSCCP Index" not in wb["Returns"]
        assert all(df.index.max() <= GE.DESIGN_END for b in wb.values() for df in b.values())
        assert not any(t.startswith("MX") for t in wb.get("Curves", {}))
        free_dir = os.path.join(work, "free")
        M = GE.setup(free_dir)
        t = time.time()
        base = GE.run(M=M)
        withb = GE.run(M=M, bbg=wb)
        E = GE.DESIGN_END
        Rf, Rb = base["R"].loc[:E], withb["R"].loc[:E]
        other = [c for c in Rf.columns if not c.startswith("cm_")]
        assert Rf[other].equals(Rb[other]), "Bloomberg commodity inputs changed a non-commodity market"
        changed = [c for c in cm if c in Rf and not Rf[c].equals(Rb[c])]
        assert len(changed) >= 10, changed
        assert not any(c in Rb.columns for c in GE.gm_modules()["BBG"].ALT_COMMOD), "held-back market entered the book"
        n_carry_b = int(withb["S"]["C"].loc[:E].reindex(columns=cm).notna().any().sum())
        n_carry_f = int(base["S"]["C"].loc[:E].reindex(columns=cm).notna().any().sum())
        assert n_carry_b > n_carry_f, (n_carry_b, n_carry_f)
        print("  adapter: %d commodity markets switched to Bloomberg returns, commodity carry for %d markets (free "
              "data: %d), other markets unchanged, held-back markets absent (%.0fs)" % (
                  len(changed), n_carry_b, n_carry_f, time.time() - t))
        print("  whitelist: %d job outputs clean (no dated value rows, nothing after 2010, no mock values)" % len(outs))
        print("BBGQ ENGINE SMOKE OK")
    finally:
        if keep:
            print("kept", tmp)
        else:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
