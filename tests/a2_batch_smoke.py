"""Smoke test of the Batch A2 code (tools/bbgq/lib/a2_batch.py, job tools/bbgq/jobs/gm_a2_v1.py; gm/CHANGES.md "A2",
2026-11-27) on SYNTHETIC panels and MOCK Bloomberg stores only (no cache, no market data, no real panel).

Checks:
  decisive        the A2 verdict line is gm.stats.noninferiority on the two k = 1 net series over 1975-01..2010-12;
                  identical books pass with dSR 0; a challenger with a steady drag fails H1; one with a deep extra
                  month fails H3
  as run          an incumbent that does not reproduce the registered A1 Sharpe ratios stops the report before any other
                  statistic is printed
  splits          Trend's class-average + relative parts add up to the held Trend position (both books); the unscaled
                  parts sum to the engine's Trend position; carry + price = total
  P4, inflation   P4 reads only earlier months, first value 1978-01, removes a known market beta; the selection
                  inflation equals the stats_audit formula and, on the shipped trial log, the registered N 39 / 0.26
  fragility       the year removal equals a direct computation
  panel checks    check_panel_id; compare_saved absent / same / differs
  seal            values dated after 2010-12 in every input change nothing
  printing        every registered line type is printed; no planted data value; no number with 5 or more decimals
  job             in the PC layout, every lib file and the trial log PASS and a store that is not LOCK_v2 stops it
                  before any value is read; a changed a2_batch.py or trial log stops it at the hash check
python3 tests/a2_batch_smoke.py      (also run from tests/run_tests.py)
"""
import math
import os
import pickle
import re
import shutil
import statistics
import subprocess
import sys
import tempfile

import numpy as np
import pandas as pd

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path[:0] = [REPO, os.path.join(REPO, "tools", "bbgq", "lib"), os.path.dirname(os.path.abspath(__file__))]

import a2_batch as A2  # noqa: E402
from gm import book as B  # noqa: E402
from gm import config as CF  # noqa: E402
from gm import execution as EX  # noqa: E402
from gm import stats as ST  # noqa: E402

GRID = pd.period_range("1960-01", "2010-12", freq="M")
MK = ["eq_us_spx", "eq_gb_ftse", "eq_jp_nikkei", "eq_de_dax", "bd_us_10y", "bd_us_5y", "bd_de_10y", "st_de_2y",
      "fx_jpy", "fx_gbp", "fx_aud", "fx_cad", "cm_wti", "cm_gold", "cm_copper", "cm_natgas"]


def scenario(seed=11, late=False):
    """Synthetic A1-like panel R, signals S (E, E_sign, C, V, V2), daily D and ^GSPC levels with known structure."""
    rng = np.random.default_rng(seed)
    n = len(GRID)
    common = rng.normal(0, 0.02, n)
    R = pd.DataFrame({k: 0.6 * common + rng.normal(0.003, 0.03, n) for k in MK}, index=GRID)
    R.loc[R.index < pd.Period("1970-01", "M")] = np.nan
    R.loc[R.index < pd.Period("1985-02", "M"), "cm_wti"] = np.nan
    R.loc[R.index < pd.Period("1994-02", "M"), "cm_natgas"] = np.nan

    def ar(scale=1.0):
        x = np.zeros((n, len(MK)))
        e = rng.normal(0, 1, (n, len(MK)))
        for t in range(1, n):
            x[t] = 0.9 * x[t - 1] + e[t]
        return pd.DataFrame(x * scale, index=GRID, columns=MK)
    E = np.tanh(ar(0.5) / 2)
    C = ar(0.01)
    V = ar(0.02)
    S = {"E": E, "E_sign": np.sign(E), "C": C, "V": V, "V2": ar(0.02)}
    for k in S:
        S[k] = S[k].where(R.notna())
    days = pd.bdate_range("1970-01-02", "2010-12-31")
    dcols = ["eq_us_spx", "eq_gb_ftse", "bd_us_10y", "fx_jpy", "fx_gbp", "cm_wti", "cm_gold"]
    D = pd.DataFrame(rng.normal(0, 0.008, (len(days), len(dcols))), index=days, columns=dcols)
    D.loc[:"1984-12-31", "cm_wti"] = np.nan
    D.loc[:"1999-12-31", "cm_gold"] = np.nan
    gspc = pd.Series(np.exp(np.cumsum(rng.normal(0.0003, 0.01, len(days)))) * 100, index=days)
    if late:
        g2 = pd.period_range("1960-01", "2012-12", freq="M")
        R = R.reindex(g2)
        R.loc[R.index > pd.Period("2010-12", "M")] = 9.87654321
        S = {k: v.reindex(g2) for k, v in S.items()}
        for k in S:
            S[k].loc[S[k].index > pd.Period("2010-12", "M")] = 9.87654321
        d2 = pd.bdate_range("2011-01-03", "2012-12-31")
        D = pd.concat([D, pd.DataFrame(0.123456789, index=d2, columns=dcols)])
        gspc = pd.concat([gspc, pd.Series(9876.54321, index=d2)])
    return R, D, S, gspc


def run(check):
    tmp = tempfile.mkdtemp(prefix="a2_smoke_")
    try:
        _run(check, tmp)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _run(check, tmp):
    R, D, S, gspc = scenario()
    trials = os.path.join(REPO, "gm", "trials.csv")
    lines = []
    res = A2.report(R, D, S, gspc, out=lines.append, trials_path=trials, frag_markets=["eq_us_spx", "fx_jpy"])
    txt = "\n".join(lines)

    # ---- decisive
    i1, c1 = res["inc"][("k1", 1.0)]["net"], res["cha"][("k1", 1.0)]["net"]
    i2, c2 = res["inc"][("k1", 2.0)]["net"], res["cha"][("k1", 2.0)]["net"]
    j = pd.concat([ST.cut(i1, *A2.WIN), ST.cut(c1, *A2.WIN)], axis=1).dropna()
    direct = ST.noninferiority(j.iloc[:, 0], j.iloc[:, 1], ST.cut(i2, *A2.WIN), ST.cut(c2, *A2.WIN))
    h = res["hyg"]["k1"]
    check("A2 decisive = gm.stats.noninferiority on the k = 1 nets, pooled 1975-01..2010-12 (lb95, H1, H3, pass)",
          abs(h["lb95"] - direct["lb95"]) < 1e-12 and h["H1"] == direct["H1"] and h["H3"] == direct["H3"] and
          h["pass"] == direct["pass"] and h["n"] == len(j) and j.index[0] >= pd.Period("1975-01", "M"),
          (h, direct))
    vline = [x for x in lines if x.startswith("A2 VERDICT")]
    check("A2 verdict line matches the decisive result and names the A2-final book",
          len(vline) == 1 and vline[0].startswith("A2 VERDICT " + ("PASS" if direct["pass"] else "FAIL")) and
          (CF.A2_CHALLENGER["name"] if direct["pass"] else CF.A1_INCUMBENT["name"]) in vline[0], vline)
    check("A2 H2 (double costs) is the dSR of the two books at cost multiple 2 (reported)",
          abs(h["H2_dsr_2x"] - (ST.sharpe(ST.cut(c2, *A2.WIN).loc[j.index[0]:]) -
                                 ST.sharpe(ST.cut(i2, *A2.WIN).loc[j.index[0]:]))) < 0.05)
    same = []
    A2.report(R, D, S, gspc, out=same.append, cha_cfg=CF.A1_INCUMBENT, do_fragility=False)
    sv = [x for x in same if x.startswith("A2 VERDICT")][0]
    hk = [x for x in same if x.startswith("HYGIENE | k1")][0]
    check("A2 identical books: dSR 0, H1 PASS, H3 PASS, verdict PASS", sv.startswith("A2 VERDICT PASS") and
          "dSR +0.000" in hk and "H1 PASS" in hk and "H3 PASS" in hk, hk)
    rng = np.random.default_rng(5)
    base = pd.Series(rng.normal(0.01, 0.03, 432), index=pd.period_range("1975-01", "2010-12", freq="M"))
    near = base + rng.normal(0, 0.001, 432)
    drag = base - 0.006
    deep = base.copy()
    deep.iloc[200] = base.min() - 0.08
    hn, hd, hp = (A2.hygiene(base, x, base, x, *A2.WIN) for x in (near, drag, deep))
    check("A2 H1: a near-identical challenger passes, a steady drag of 0.6%/month fails (lb95 <= -0.10)",
          hn["H1"] and not hd["H1"] and hd["lb95"] <= -0.10, (hn["lb95"], hd["lb95"]))
    check("A2 H3: one extra month 8 points worse fails the tail test (worst month > 1 point worse)",
          not hp["H3"] and not hp["pass"], hp["tail"])

    # ---- as run
    ar_lines = []
    try:
        A2.report(R, D, S, gspc, out=ar_lines.append, as_run={"k1": 9.999, "k0": 9.999, "d1": 9.999})
        raised = False
    except A2.AsRunMismatch:
        raised = True
    check("A2 as-run check: a mismatch raises before any other statistic is printed (one FAIL line only)",
          raised and len(ar_lines) == 1 and ar_lines[0].startswith("FAIL incumbent as run"), ar_lines)
    got = {t: round(ST.sharpe(ST.cut(res["inc"][(t, 1.0)]["net"], *A2.WIN)), 3) for t in ("k1", "k0", "d1")}
    ok_lines = []
    A2.report(R, D, S, gspc, out=ok_lines.append, as_run=got, do_fragility=False)
    check("A2 as-run check: the incumbent's own values pass", ok_lines[0].startswith("PASS incumbent as run"),
          ok_lines[:1])

    # ---- splits
    for nm, cfg, bb in (("incumbent", CF.A1_INCUMBENT, res["inc"]), ("challenger", CF.A2_CHALLENGER, res["cha"])):
        bk = bb[("k1", 1.0)]
        sp = A2.trend_split(R, D, S, cfg, bk)
        held = bk["fam_pos"]["trend"].fillna(0)
        check("A2 Trend split (%s): class-average + relative = the held Trend position (max diff < 1e-9)" % nm,
              sp["maxdiff_parts"] < 1e-9 and sp["maxdiff_held"] < 1e-9 and
              float((sp["avg"] + sp["rel"] - held).abs().max().max()) < 1e-9, (sp["maxdiff_parts"], sp["maxdiff_held"]))
        parts = A2.trend_raw_parts(R, cfg, D, S)
        fam = B.family_positions(R, cfg, D, S)
        fam = fam[0]
        md = max(float((parts[c][0] - fam["trend"][c]).abs().max().max()) for c in parts)
        mn = sum(int((parts[c][0].isna() != fam["trend"][c].isna()).sum().sum()) for c in parts)
        check("A2 Trend split (%s): the unscaled pod position equals the engine's Trend position (diff 0)" % nm,
              md < 1e-12 and mn == 0, (md, mn))
        tot, car, pri, cov = A2.carry_price(bk, S["C"])
        check("A2 carry + price = total (bonds and currencies, %s); covered share in [0, 1]" % nm,
              float((car + pri - tot).abs().max()) < 1e-15 and 0 <= cov <= 1)

    # ---- P4, inflation
    rng = np.random.default_rng(9)
    m = pd.Series(rng.normal(0.005, 0.045, 432), index=pd.period_range("1975-01", "2010-12", freq="M"))
    r = 0.5 * m + pd.Series(rng.normal(0.004, 0.02, 432), index=m.index)
    w = A2.p4(r, m)
    m2, r2 = m.copy(), r.copy()
    m2.loc["2000-01":] = m2.loc["2000-01":] * -3
    r2.loc["2000-01":] = 0.1
    w2 = A2.p4(r2, m2)
    check("A2 P4: first value 1978-01 (month 37), point in time (later months change nothing before them)",
          str(w.first_valid_index()) == "1978-01" and np.allclose(w.loc[:"1999-12"].dropna(), w2.loc[:"1999-12"]
                                                                 .dropna()))
    check("A2 P4: a known market beta 0.5 is removed (correlation of w with m near 0)",
          abs(w.corr(m)) < 0.1 and r.corr(m) > 0.5, (w.corr(m), r.corr(m)))
    log = os.path.join(tmp, "trials.csv")
    srs = np.round(rng.normal(1.4, 0.1, 25), 3)
    pd.DataFrame({"trial": ["t%d" % i for i in range(30)], "family": ["book"] * 20 + ["pod"] * 5 + ["fix"] * 5,
                  "sr_9010": list(srs) + [9.0] * 5}).to_csv(log, index=False)
    si = A2.selection_inflation(log)
    nd = statistics.NormalDist()
    g = 0.5772156649
    z = (1 - g) * nd.inv_cdf(1 - 1 / 25) + g * nd.inv_cdf(1 - 1 / (25 * math.e))
    check("A2 selection inflation: book + pod rows only, the stats_audit formula", si["n"] == 25 and
          abs(si["inflation"] - z * np.std(srs, ddof=1)) < 1e-3, (si, z * np.std(srs, ddof=1)))
    sr = A2.selection_inflation(trials)
    check("A2 selection inflation on the shipped trial log: N 39, inflation 0.26 (registered, CHANGES A2 item 4l)",
          sr["n"] == 39 and round(sr["inflation"], 2) == 0.26 and A2.file_sha(trials) == A2.TRIALS_SHA, sr)

    # ---- fragility
    fr = res["fragility"]
    yrs = {}
    for y in range(1975, 2011):
        jj = j[j.index.year != y]
        yrs[y] = ST.sharpe(jj.iloc[:, 1]) - ST.sharpe(jj.iloc[:, 0])
    full = ST.sharpe(j.iloc[:, 1]) - ST.sharpe(j.iloc[:, 0])
    wy = min(yrs, key=yrs.get)
    check("A2 fragility: the year removal equals a direct computation (largest loss and its year)",
          fr["year"][0] == wy and abs(fr["year"][1] - (full - yrs[wy])) < 1e-12 and abs(fr["full"] - full) < 1e-12,
          (fr["year"], wy, full - yrs[wy]))
    check("A2 fragility: markets and classes re-run (2 markets tried, a class named)",
          fr["n_markets"] == 2 and fr["class"][0] in ("EQ", "FI", "FX", "CM"))

    # ---- panel checks
    a1 = {"panel_id": A2.A1_PANEL_ID, "R": R.loc[:"2010-12"], "S": {k: v for k, v in S.items()}}
    check("A2 panel id: the registered id passes, another fails",
          A2.check_panel_id(a1) and not A2.check_panel_id(dict(a1, panel_id="0" * 64)))
    work = os.path.join(tmp, "work")
    check("A2 saved panel: absent when no file", A2.compare_saved(work, a1) == "absent")
    os.makedirs(os.path.join(work, "a1"))
    p = os.path.join(work, "a1", "a1_panel_%s.pkl" % A2.A1_PANEL_ID[:12])
    with open(p, "wb") as f:
        pickle.dump({"R": a1["R"], "S": a1["S"], "admitted": [], "panel_id": A2.A1_PANEL_ID, "version": "x"}, f)
    check("A2 saved panel: same when the file equals the rebuild", A2.compare_saved(work, a1) == "same")
    R2 = a1["R"].copy()
    R2.iloc[300, 3] += 1e-9
    with open(p, "wb") as f:
        pickle.dump({"R": R2, "S": a1["S"], "admitted": [], "panel_id": A2.A1_PANEL_ID, "version": "x"}, f)
    check("A2 saved panel: a one-cell difference is found", A2.compare_saved(work, a1) == "differs: R")
    S2 = dict(a1["S"], V2=a1["S"]["V2"].where(pd.Series(a1["S"]["V2"].index > pd.Period("1990-01", "M"),
                                                         index=a1["S"]["V2"].index), axis=0))
    with open(p, "wb") as f:
        pickle.dump({"R": a1["R"], "S": S2, "admitted": [], "panel_id": A2.A1_PANEL_ID, "version": "x"}, f)
    check("A2 saved panel: a signal difference is found", A2.compare_saved(work, a1) == "differs: signal V2")

    # ---- seal
    Rl, Dl, Sl, gl = scenario(late=True)
    late_lines = []
    A2.report(Rl, Dl, Sl, gl, out=late_lines.append, trials_path=trials, frag_markets=["eq_us_spx", "fx_jpy"])
    check("A2 seal: values dated after 2010-12 in every input change nothing in the report",
          late_lines == lines, next((a + " || " + b for a, b in zip(late_lines, lines) if a != b), ""))

    # ---- printing
    need = {"HYGIENE | k1": 1, "HYGIENE | k0": 1, "HYGIENE | d1": 1, "ERA | ": 6, "VERSION | ": 22, "POD | ": 10,
            "TRANCHE | ": 11, "SPLIT | ": 22, "CARRYPRICE | ": 8, "VALUE | ": 3, "ECON-TREND | ": 2, "FLAGGED | ": 2,
            "P4 | ": 2, "FRAGILITY | ": 4, "BOOK | ": 36, "selection inflation": 1, "tuned knobs": 1,
            "A2 VERDICT": 1}
    cnt = {k: sum(1 for x in lines if x.startswith(k)) for k in need}
    check("A2 report: every registered line type is printed (counts)", cnt == need,
          {k: (cnt[k], need[k]) for k in need if cnt[k] != need[k]})
    check("A2 report: the split checks pass in the printed lines",
          sum(1 for x in lines if x.startswith("SPLIT") and "check:" in x and x.endswith("PASS")) == 2)
    planted = set()
    for x in np.concatenate([R.dropna().values.ravel()[::97], S["C"].dropna().values.ravel()[::89],
                             S["V"].dropna().values.ravel()[::89]]):
        planted.add("%.6f" % x)
        planted.add("%.5f" % x)
    hits = [x for x in planted if x in txt]
    check("A2 printing: no planted data value appears", not hits, hits[:5])
    long_dec = re.findall(r"\d\.\d{5,}", txt)
    check("A2 printing: no number with 5 or more decimals", not long_dec, long_dec[:5])
    tr = A2.trial_row(res, A2.A1_PANEL_ID, CF.ENGINE_VERSION)
    check("A2 trial row: family book, challenger hash a5b83bdf45, note names panel, parent and verdict",
          tr["family"] == "book" and tr["hash"] == A2.CHA_HASH == CF.cfg_hash(CF.A2_CHALLENGER) and
          "e7f98d4439fccf91" in tr["note"] and "465b5ecd4f" in tr["note"] and res["verdict"] in tr["note"], tr)
    check("A2 registered constants: incumbent hash, AS_RUN = the A1 report's k1 / k0 / d1",
          CF.cfg_hash(CF.A1_INCUMBENT) == A2.INC_HASH and A2.AS_RUN == {"k1": 1.439, "k0": 1.480, "d1": 1.052})

    # ---- the job in the PC layout
    import a1_panel_smoke as A1S
    loc = os.path.join(tmp, "local")
    lib = os.path.join(loc, "lib")
    os.makedirs(lib)
    shutil.copytree(os.path.join(REPO, "gm"), os.path.join(lib, "gm"),
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    bq = os.path.join(REPO, "tools", "bbgq")
    for rel in ("lib/gm_engine.py", "lib/bbg_panel.py", "lib/bbgdata.py", "lib/a1_panel.py", "lib/a2_batch.py",
                "live_sources.csv", "untouched_markets.csv", "engine_ref.json"):
        shutil.copy(os.path.join(bq, rel), os.path.join(lib, os.path.basename(rel)))
    blocks, _free = A1S.scenario()
    A1S.write_store(os.path.join(loc, "work"), blocks)
    env = dict(os.environ, BBG_WORK=os.path.join(loc, "work"), PYTHONPATH="")
    job = os.path.join(bq, "jobs", "gm_a2_v1.py")

    def go():
        q = subprocess.run([sys.executable, job], cwd=loc, env=env, capture_output=True, text=True, timeout=600)
        return q.stdout, q.returncode, q.stderr
    o, rc, err = go()
    check("A2 job (PC layout): gm code, 5 lib files and the trial log PASS; a non-LOCK_v2 store -> STOP before any "
          "value is read", "PASS gm code vs reference" in o and o.count("PASS lib ") == 6 and
          "FAIL Bloomberg store lock id" in o and "STOP: the Bloomberg store is not LOCK_v2 (nothing read)" in o and
          rc == 0, (o + err)[-800:])
    with open(os.path.join(lib, "a2_batch.py"), "a") as f:
        f.write("\n# changed\n")
    o2, rc2, err2 = go()
    check("A2 job: a changed a2_batch.py stops it at the hash check", "FAIL lib a2_batch.py" in o2 and
          "STOP: lib file differs from the registered build: a2_batch.py" in o2 and "lock id" not in o2,
          (o2 + err2)[-600:])
    shutil.copy(os.path.join(bq, "lib", "a2_batch.py"), os.path.join(lib, "a2_batch.py"))
    with open(os.path.join(lib, "gm", "trials.csv"), "a") as f:
        f.write("2026-11-28,x,book,,1.0,,,,,,\n")
    o3, rc3, err3 = go()
    check("A2 job: a changed trial log stops it before the store is opened",
          "FAIL lib gm\\trials.csv" in o3 and "STOP: the trial log differs" in o3 and "lock id" not in o3,
          (o3 + err3)[-600:])
    check("A2 job output: no number with 5+ decimals", not re.findall(r"\d\.\d{5,}", o + o2 + o3))


if __name__ == "__main__":
    fails = []

    def check(name, ok, detail=""):
        print(("PASS " if ok else "FAIL ") + name + ("" if ok else "  " + str(detail)[:600]))
        if not ok:
            fails.append(name)
    run(check)
    print("A2 BATCH SMOKE " + ("PASSED" if not fails else "FAILED: %d" % len(fails)))
    sys.exit(1 if fails else 0)
