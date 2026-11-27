"""Smoke test of Core book v1 (tools/bbgq/lib/core_v1.py, job tools/bbgq/jobs/gm_core_v1.py; gm/CHANGES.md "Core
book v1", 2026-11-27) on SYNTHETIC panels and MOCK Bloomberg stores only (no cache, no market data, no real panel).
The rebuild is the STUB tests/data/rebuild_s4_stub.py (shape only), never the independent tools/bbgq/lib/rebuild_s4.py.

Checks:
  masks        Core and shadow parts partition every pod's components (positions add up exactly)
  S1           the identity date map reproduces the part-alone net exactly; the placebo p is placebo_runs' share
  S2, S3       equal direct computations (mean of the 2x-cost part; tail_test of the books with / without)
  S4           rebuild = engine passes with difference 0; x 1.10 passes on the mean, x 1.20 fails; Sharpe uses own months
  interface    v2 raw inputs: keys, no engine-built measure, copies; raw_check passes on consistent inputs and fails
               on a changed or missing value; the check formulas by hand; validate_rebuild refuses a missing key, a non-monthly index, a month
               after the cut, an infinite value, too few months; forbidden_imports finds gm / gm_engine / core_v1
  live         a held market without a free return at 2010-12 fails the check
  verdicts     Core = S1-S4 + live; a broken rebuild makes every part not Core -> CORE BOOK V1 EMPTY, alpha against a
               zero book = the part's mean, T4 not applicable, trial row without Sharpe columns
  Incubator    T1 = alpha_boot against Core book v1; T4 = t4_tail
  seal         values dated after 2010-12 change nothing; printing: no 5+ decimals, values with counts >= 60 months
  diag facts   A3-empty report accepted; one without 'D2: closed' refused
  job          in the PC layout: REBUILD_SHA unset -> STOP before the store; with the stub registered every check passes
               up to the store (mock, not LOCK_v2 -> STOP); a stub importing gm -> STOP; no diag report -> STOP
python3 tests/core_v1_smoke.py      (also run from tests/run_tests.py)
"""
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile

import numpy as np
import pandas as pd

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [REPO, os.path.join(REPO, "tools", "bbgq", "lib"), HERE, os.path.join(HERE, "data")]

import a2_batch_smoke as S2  # noqa: E402
import core_v1 as CV  # noqa: E402
import diag_a2_smoke as DS  # noqa: E402
import rebuild_s4_stub as STUB  # noqa: E402
from gm import book as B  # noqa: E402
from gm import config as CF  # noqa: E402
from gm import execution as EX  # noqa: E402
from gm import stats as ST  # noqa: E402

NPL = 20      # placebos in the smoke test (the job uses the registered 1,000)


def diag_text(d2="closed", done=True):
    L = ["=== gm_diag_v1 ===",
         "DIAG SUMMARY | D1: candidate half blocked; structural half reported | D2: %s | D3: closed | D4: Trend closed"
         ", Carry closed | S1: reported | D5: slow reaction | D6: closed | X2: EQ no entry | M1: S&P alone | "
         "FALSIFIERS: T1 does not hold" % d2]
    if done:
        L.append("DIAG JOB DONE")
    return "\n".join(L) + "\n"


def planted(R, seed=5):
    """A slow drift in each market's design months (AR(1) 0.99), so 1/3/12-month trends pay and Trend passes its
    placebo; months after 2010-12 (the late scenario) are left as planted by a2_batch_smoke."""
    rng = np.random.default_rng(seed)
    idx = pd.period_range("1960-01", "2010-12", freq="M")
    x = np.zeros((len(idx), R.shape[1]))
    e = rng.normal(0, 1, x.shape)
    for t in range(1, len(idx)):
        x[t] = 0.99 * x[t - 1] + e[t]
    drift = pd.DataFrame(x * 0.0025, index=idx, columns=R.columns).reindex(R.index).fillna(0.0)
    drift.loc[drift.index > pd.Period("2010-12", "M")] = 0.0
    return R + drift


def synth_raw(seed=8):
    """Synthetic interface-v2 raw inputs on the design grid for the scenario's markets (fx_jpy, fx_gbp, fx_aud, fx_cad;
    cm_wti, cm_natgas; eq_gb_ftse, eq_jp_nikkei, eq_de_dax and the US)."""
    rng = np.random.default_rng(seed)
    idx = pd.period_range("1960-01", "2010-12", freq="M")
    n = len(idx)

    def walk(x0, sd):
        return x0 + np.cumsum(rng.normal(0, sd, n))
    rate = pd.DataFrame({c: np.clip(walk(5.0, 0.2), 0.1, None) for c in ("US", "JP", "GB", "AU", "CA")}, index=idx)
    rate.loc[:pd.Period("1969-12", "M")] = np.nan
    eia = {}
    for m, start in (("cm_wti", "1983-04"), ("cm_natgas", "1990-04")):
        f1 = pd.Series(np.exp(walk(3.0, 0.08)), index=idx)
        f2 = f1 * np.exp(rng.normal(0, 0.02, n))
        F = pd.DataFrame({1: f1, 2: f2}, index=idx)
        F.loc[:pd.Period(start, "M") - 1] = np.nan
        eia[m] = F
    cols = ["eq_gb_ftse", "eq_jp_nikkei", "eq_de_dax"]
    fw = pd.DataFrame(rng.normal(0.008, 0.04, (n, 3)), index=idx, columns=cols)
    fx = fw - np.abs(rng.normal(0.003, 0.001, (n, 3)))
    fw.loc[:pd.Period("1974-12", "M")] = np.nan
    fx.loc[:pd.Period("1974-12", "M")] = np.nan
    ust = pd.Series(rng.normal(0.008, 0.04, n), index=idx)
    usp = ust - np.abs(rng.normal(0.0018, 0.0005, n))
    ust.loc[:pd.Period("1993-01", "M")] = np.nan
    return {"rate3m": rate, "fx_rate_country": {"fx_jpy": "JP", "fx_gbp": "GB", "fx_aud": "AU", "fx_cad": "CA"},
            "eia": eia, "french_with": fw, "french_without": fx, "us_total": ust, "us_price": usp}


def scenario(late=False):
    """a2_batch_smoke's panel with a planted trend; the Core parts' carry and value measures replaced by the spec
    formulas on synth_raw (so the raw check holds); months after 2010-12 of the late form keep a planted value."""
    R, D, S, gspc = S2.scenario(late=late)
    raw = synth_raw()
    C, V = CV.measures_from_raw(raw)
    S = {k: v.copy() for k, v in S.items()}
    for key, X in (("C", C), ("V", V)):
        for c in X.columns:
            col = X[c].reindex(S[key].index)
            if late:
                col[col.index > pd.Period("2010-12", "M")] = 9.87654321
            S[key][c] = col
    return planted(R), D, S, gspc, raw


def run(check):
    tmp = tempfile.mkdtemp(prefix="core_smoke_")
    try:
        _run(check, tmp)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _run(check, tmp):
    R, D, S, gspc, raw = scenario()
    cfg = CF.A1_INCUMBENT
    days = EX.nyse_days(gspc=gspc)
    M = CV.masks()
    free = {"R": R, "S": S}

    # ---- masks partition each pod
    _, _vol, comp = B.family_positions(R, cfg, D, S, components=True)
    worst = 0.0
    for pod in ("trend", "econ", "carry", "value"):
        allc = B.mask_components(comp, [(pod, "*", "*")])
        parts = [M[p] for p in CV.CORE + CV.SHADOW]
        got = {}
        for m in parts:
            for key, v in B.mask_components(comp, [x for x in m if x[0] == pod]).items():
                got[key] = got.get(key, 0) + v.fillna(0)
        for key, v in allc.items():
            worst = max(worst, float((got.get(key, 0) - v.fillna(0)).abs().max().max()))
    check("masks: Core + shadow parts partition every pod's components (max diff %.1e)" % worst, worst < 1e-15)

    # ---- interface inputs
    inp = CV.rebuild_inputs(R, D, days, raw, {"config": cfg["name"]})
    check("interface v2: rebuild_inputs has exactly the documented keys", set(inp) == set(CV.INPUT_KEYS), sorted(inp))
    check("interface v2: no engine-built measure or volatility in the inputs",
          not {"C", "V", "vol", "S", "E"} & set(inp))
    check("interface v2: rate3m in percent with a US column, eia contracts 1 and 2, French with / without, a cost for "
          "every market", "US" in inp["rate3m"].columns and all(list(F.columns) == [1, 2] for F in inp["eia"].values())
          and list(inp["french_with"].columns) == list(inp["french_without"].columns) and
          set(inp["cost"]) == set(R.columns) and inp["classes"]["FI"] == ("bd_", "st_"))
    inp["R"].iloc[:, 0] = 99.0
    inp["eia"]["cm_wti"].iloc[:, 0] = 99.0
    inp["rate3m"].iloc[:, 0] = 99.0
    check("interface: the inputs are copies (changing them leaves the panel and the raw inputs alone)",
          not (R.iloc[:, 0] == 99.0).any() and not (raw["eia"]["cm_wti"].iloc[:, 0] == 99.0).any() and
          not (raw["rate3m"].iloc[:, 0] == 99.0).any())
    rc = CV.raw_check(raw, S)
    check("raw check: the raw inputs reproduce the scenario's carry and value measures (3 groups PASS)",
          len(rc) == 3 and all(r["pass"] for r in rc), rc)
    Sb = {k: v.copy() for k, v in S.items()}
    Sb["C"].loc[pd.Period("1995-06", "M"), "fx_jpy"] += 1e-6
    Sv = {k: v.copy() for k, v in S.items()}
    Sv["V"].loc[pd.Period("1990-03", "M"), "eq_de_dax"] = np.nan
    check("raw check: a changed currency carry value fails the currency group only; a missing value fails the value group",
          [r["pass"] for r in CV.raw_check(raw, Sb)] == [False, True, True] and
          [r["pass"] for r in CV.raw_check(raw, Sv)] == [True, True, False])
    Cm, Vm = CV.measures_from_raw(raw)
    t = pd.Period("1999-07", "M")
    hand_fx = (raw["rate3m"].at[t - 1, "JP"] - raw["rate3m"].at[t - 1, "US"]) / 100
    hand_cm = 12 * (raw["eia"]["cm_wti"].at[t, 1] / raw["eia"]["cm_wti"].at[t, 2] - 1)
    dd = raw["french_with"]["eq_gb_ftse"] - raw["french_without"]["eq_gb_ftse"]
    hand_v = float(dd.loc[t - 23:t - 12].sum())
    check("raw check formulas by hand: FX carry lagged one month, energy 12 x (F1 / F2 - 1), E4 = the 12-month sum "
          "ending at t - 12", abs(Cm.at[t, "fx_jpy"] - hand_fx) < 1e-15 and abs(Cm.at[t, "cm_wti"] - hand_cm) < 1e-15
          and abs(Vm.at[t, "eq_gb_ftse"] - hand_v) < 1e-15)
    rb = STUB.part_returns(CV.rebuild_inputs(R, D, days, raw))
    ok, why, nm = CV.validate_rebuild(rb)
    check("validate: the stub's output passes", ok, why)
    for lab, bad in (("a missing key", {k: v for k, v in rb.items() if k != "carry"}),
                     ("a non-monthly index", dict(rb, trend=rb["trend"].set_axis(rb["trend"].index.to_timestamp()))),
                     ("a month after the cut", dict(rb, trend=pd.concat([rb["trend"], pd.Series(
                         [0.0], index=pd.PeriodIndex(["2011-01"], freq="M"))]))),
                     ("an infinite value", dict(rb, trend=rb["trend"].where(rb["trend"].index != pd.Period(
                         "1990-01", "M"), np.inf))),
                     ("too few months", dict(rb, value_eq=rb["value_eq"].where(rb["value_eq"].index >=
                                                                               pd.Period("2005-01", "M"))))):
        ok_, why_, _ = CV.validate_rebuild(bad)
        check("validate: %s is refused (%s)" % (lab, why_), not ok_)
    src = os.path.join(tmp, "rb_src.py")
    for code, want in (("import numpy as np\nimport pandas as pd\n", []), ("import gm\n", ["gm"]),
                       ("from gm.book import run\n", ["gm"]), ("import numpy, gm_engine\n", ["gm_engine"]),
                       ("x = __import__('core_v1')\n", ["core_v1"]),
                       ("import importlib\nm = importlib.import_module(\"diag_a2\")\n", ["diag_a2"]),
                       ("# import gm in a comment is text only\nimport os\n", [])):
        open(src, "w").write(code)
        check("forbidden imports: %r -> %s" % (code.strip()[:40], want), CV.forbidden_imports(src) == want,
              CV.forbidden_imports(src))
    check("forbidden imports: the stub imports none",
          CV.forbidden_imports(os.path.join(HERE, "data", "rebuild_s4_stub.py")) == [])

    # ---- S1 identity, S2, S3, S4 logic, live check, alpha
    bk = CV.alone(R, D, S, days, cfg, M["trend"])
    win = CV.window(bk["net"])
    fn = B.placebo_net_fn(R, cfg, D, S, str(win.index[0]), runner=EX.run_k1, days=days, parts={"alone": M["trend"]})
    d0 = (fn(None) - bk["net"]).abs().max()
    check("S1: the identity date map reproduces the part alone exactly (max diff %.1e)" % d0, d0 == 0 or d0 < 1e-15)
    pl = CV.s1(R, D, S, days, cfg, M["trend"], win, n=NPL)
    check("S1: p = share of placebo Sharpe ratios >= the part's; pass iff p < 0.05",
          abs(pl["p"] - np.mean(np.asarray(pl["placebo_sr"]) >= pl["sr"])) < 1e-15 and pl["pass"] == (pl["p"] < 0.05)
          and pl["n"] == NPL and pl["window"] == (str(win.index[0]), "2010-12"))
    with_bk = CV.run_parts(R, D, S, days, cfg, {p: M[p] for p in CV.CORE})
    wo = CV.run_parts(R, D, S, days, cfg, {q: M[q] for q in CV.CORE if q != "trend"})
    tl = CV.s3(with_bk["net"], wo["net"])
    tl2 = ST.tail_test(ST.cut(wo["net"], *CV.WIN), ST.cut(with_bk["net"], *CV.WIN))
    check("S3: tail_test(without, with) on 1975-2010 as run", tl == tl2)
    e = bk["net"]
    r0 = CV.s4_row(e, e)
    r1 = CV.s4_row(e, e * 1.10)
    r2 = CV.s4_row(e, e * 1.20)
    check("S4: rebuild = engine passes with 0 difference; x1.10 passes (mean 0.10, Sharpe 0); x1.20 fails on the mean",
          r0["pass"] and r0["rel_sr"] < 1e-12 and r0["rel_mean"] < 1e-12 and r1["pass"] and
          abs(r1["rel_mean"] - 0.10) < 1e-9 and r1["rel_sr"] < 1e-9 and not r2["pass"] and
          abs(r2["rel_mean"] - 0.20) < 1e-9, (r0, r1, r2))
    e2 = e.copy()
    e2.loc[:pd.Period("1985-12", "M")] = np.nan
    r3 = CV.s4_row(e, e2)
    check("S4: each series over its own months (a shorter rebuild has fewer months and fewer common months)",
          r3["n_rb"] < r3["n_eng"] and r3["n_common"] == r3["n_rb"])
    ok_l, held, miss = CV.live_check(bk["pos"], "trend", R, S)
    R_miss = R.copy()
    if held:
        R_miss.loc[pd.Period("2010-12", "M"), held[0]] = np.nan
    ok_m, _h, miss_m = CV.live_check(bk["pos"], "trend", R_miss, S)
    check("live: every held market has a free return -> PASS; one without -> FAIL naming it",
          ok_l and not miss and len(held) > 0 and not ok_m and miss_m and miss_m[0][0] == held[0], (held, miss_m))
    bkv = CV.alone(R, D, S, days, cfg, M["value"])
    S_miss = {k: v.copy() for k, v in S.items()}
    hv = CV.live_check(bkv["pos"], "value", R, S)[1]
    if hv:
        S_miss["V"].loc[pd.Period("2010-12", "M"), hv[0]] = np.nan
    check("live: value without its free V measure at 2010-12 -> FAIL", bool(hv) and
          not CV.live_check(bkv["pos"], "value", R, S_miss)[0])
    az = CV.alpha(bk["net"], None, zero=True)
    check("alpha: against a zero book = the part's own mean, beta 0",
          abs(az["alpha"] - ST.cut(bk["net"], *CV.WIN).mean()) < 1e-15 and az["beta"] == 0.0)
    la = CV.alpha(bk["net"], wo["net"])
    j = pd.concat([ST.cut(bk["net"], *CV.WIN), ST.cut(wo["net"], *CV.WIN)], axis=1).dropna()
    la2 = ST.alpha_boot(j.iloc[:, 0], j.iloc[:, 1])
    check("alpha: leave-one-out = gm.stats.alpha_boot on common window months", la["alpha"] == la2["alpha"] and
          la["p"] == la2["p"])

    # ---- the report with a rebuild equal to the engine (S4 passes; the non-empty branch is exercised)
    rbe = {k: CV.alone(R, D, S, days, cfg, M[p])["net"] for k, p in (("trend", "trend"), ("carry", "carry"),
                                                                     ("value_eq", "value"), ("carry_fx_v2", "carry_fx_v2"),
                                                                     ("carry_energy", "carry_energy"))}
    lines = []
    res = CV.report(R, D, S, gspc, free, rbe, out=lines.append, n_placebo=NPL,
                    trials_path=os.path.join(REPO, "gm", "trials.csv"), rb_version="engine-copy")
    txt = "\n".join(lines)
    check("S4 with a rebuild equal to the engine: PASS for all three parts", all(res["parts"][p]["S4"] for p in CV.CORE))
    check("the synthetic run has a non-empty Core book and at least one candidate that is not Core (both branches)",
          res["core"] and len(res["core"]) < 3, {p: {x: res["parts"][p].get(x) for x in ("S1", "S2", "S3", "LIVE")}
                                                for p in CV.CORE})
    failed = [p for p in CV.CORE if p not in res["core"]]
    check("a candidate that is not Core takes the Incubator rule against Core book v1",
          all(any(x.startswith("INCUBATOR | %s |" % q) for x in lines) for q in failed) and
          all(q in res["incubator"] for q in failed), failed)
    for pre in ("PARTS |", "PART | trend", "PART | econ", "S1 | trend", "S2 | carry", "S3 | value", "S4 | trend",
                "S4 REPORTED | carry_fx_v2", "LIVE | trend", "LOO | value", "VERDICT | trend", "INCUBATOR | econ",
                "CORE V1 VERDICT |", "selection inflation", "tuned knobs"):
        check("report prints %r" % pre, pre in txt)
    consistent = all(res["parts"][p]["core"] == all(res["parts"][p][x] for x in ("S1", "S2", "S3", "S4", "LIVE"))
                     for p in CV.CORE)
    check("verdicts: Core = S1 and S2 and S3 and S4 and live, per part", consistent)
    s2d = ST.cut(CV.alone(R, D, S, days, cfg, M["carry"], cost_mult=2.0)["net"], *CV.WIN).mean() > 0
    check("S2: the verdict equals the direct mean of the 2x-cost part", res["parts"]["carry"]["S2"] == bool(s2d))
    if res["core"]:
        cb = res["books"][("k1", 1.0)]["net"]
        cb2 = CV.run_parts(R, D, S, days, cfg, {p: M[p] for p in res["core"]})["net"]
        check("Core book v1 = the Core parts at equal risk (E9)", (cb - cb2).abs().max() < 1e-15)
        tl4 = ST.t4_tail(ST.cut(cb, *CV.WIN), ST.cut(CV.alone(R, D, S, days, cfg, M["econ"])["net"], *CV.WIN), 0.5)
        check("Incubator: econ's T4 = t4_tail(Core book v1, econ)", ("T4 %s" % ("PASS" if tl4["pass"] else "FAIL"))
              in [x for x in lines if x.startswith("INCUBATOR | econ")][0])
        check("BOOK lines at k1 / k0 / d1 and P4 printed for a non-empty Core book",
              all("BOOK | core_v1 | %s | costs x1 | 1975-2010" % t in txt for t in ("k1", "k0", "d1")) and
              "P4 | core_v1" in txt)
    tr = CV.trial_row(res, CV.A1_PANEL_ID, CF.ENGINE_VERSION)
    check("trial row: family book, hash = cfg_hash(A1_INCUMBENT + core_parts), note names panel, parent, verdicts",
          tr["family"] == "book" and tr["hash"] == CV.core_hash(cfg, res["core"]) and "e7f98d4439fccf91" in tr["note"]
          and "77374d7bef" in tr["note"] and ("sr_9010" in tr) == (not res["empty"]))
    nums = re.findall(r"(-?\d+\.\d+) \((\d+)\)", txt)
    check("printing: every value printed with a month count has >= 60 months", all(int(n) >= 60 for _v, n in nums),
          [x for x in nums if int(x[1]) < 60][:5])
    check("printing: no number with 5+ decimals", not re.findall(r"\d\.\d{5,}", txt))

    # ---- empty branch: a rebuild far from the engine fails S4 for every part
    rbx = {k: v * 3.0 for k, v in rb.items()}
    lines_e = []
    res_e = CV.report(R, D, S, gspc, free, rbx, out=lines_e.append, n_placebo=NPL)
    te = "\n".join(lines_e)
    inc_lines = [x for x in lines_e if x.startswith("INCUBATOR |") and "insufficient" not in x]
    check("empty branch: every part fails S4 -> CORE BOOK V1 EMPTY, no holdout, BASE 'no Core book'",
          res_e["empty"] and "CORE BOOK V1 EMPTY" in te and "no holdout run" in te and '"no Core book"' in te)
    check("empty branch: Incubator lines read 'T4 not applicable' and the three failed candidates are tested too",
          inc_lines and all("T4 not applicable" in x for x in inc_lines) and
          {x.split("|")[1].strip() for x in inc_lines} >= set(CV.CORE) | set(CV.SHADOW), inc_lines)
    a_e = CV.alpha(CV.alone(R, D, S, days, cfg, M["econ"])["net"], None, zero=True)
    check("empty branch: econ's T1 alpha is its own mean", ("%.2f" % (a_e["alpha"] * 1200)) in
          [x for x in lines_e if x.startswith("INCUBATOR | econ")][0])
    tre = CV.trial_row(res_e, CV.A1_PANEL_ID, CF.ENGINE_VERSION)
    check("empty branch: trial row without Sharpe columns, note says EMPTY", "sr_9010" not in tre and
          "EMPTY" in tre["note"])

    # ---- seal: values after 2010-12 change nothing
    Rl, Dl, Sl, gl, _rawl = scenario(late=True)
    lines_l = []
    CV.report(Rl, Dl, Sl, gl, {"R": Rl, "S": Sl}, rbe, out=lines_l.append, n_placebo=NPL,
              trials_path=os.path.join(REPO, "gm", "trials.csv"), rb_version="engine-copy")
    check("seal: planted values after 2010-12 change no printed line", lines_l == lines,
          [(a, b) for a, b in zip(lines, lines_l) if a != b][:2])

    # ---- diag facts
    dp = os.path.join(tmp, "gm_diag_v1.txt")
    open(dp, "w").write(diag_text())
    check("diag facts: the A3-empty report is accepted", CV.diag_facts(dp) == (True, "ok"))
    open(dp, "w").write(diag_text(d2="OPEN"))
    check("diag facts: a report without 'D2: closed' is refused", not CV.diag_facts(dp)[0])
    open(dp, "w").write(diag_text(done=False))
    check("diag facts: a report without DIAG JOB DONE is refused", not CV.diag_facts(dp)[0])
    check("registered constants: config hashes and engine as the gm-2.2.1 entry",
          {k: CF.cfg_hash(getattr(CF, k)) for k in CV.CFG_HASHES} == CV.CFG_HASHES and CF.ENGINE_VERSION == CV.ENGINE)

    # ---- the job in the PC layout
    import a1_panel_smoke as A1S
    loc = os.path.join(tmp, "local")
    lib = os.path.join(loc, "lib")
    os.makedirs(lib)
    shutil.copytree(os.path.join(REPO, "gm"), os.path.join(lib, "gm"),
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    bq = os.path.join(REPO, "tools", "bbgq")
    for rel in ("lib/gm_engine.py", "lib/bbg_panel.py", "lib/bbgdata.py", "lib/a1_panel.py", "lib/a2_batch.py",
                "lib/diag_a2.py", "lib/core_v1.py", "live_sources.csv", "untouched_markets.csv", "engine_ref.json"):
        shutil.copy(os.path.join(bq, rel), os.path.join(lib, os.path.basename(rel)))
    stub = os.path.join(HERE, "data", "rebuild_s4_stub.py")
    shutil.copy(stub, os.path.join(lib, "rebuild_s4.py"))
    blocks, _free = A1S.scenario()
    A1S.write_store(os.path.join(loc, "work"), blocks)
    env = dict(os.environ, BBG_WORK=os.path.join(loc, "work"), PYTHONPATH="")
    env.pop("PYTHONDONTWRITEBYTECODE", None)          # the job itself must keep lib\ free of .pyc (C4)
    job_src = open(os.path.join(bq, "jobs", "gm_core_v1.py"), encoding="utf-8").read()
    core_sha = hashlib.sha256(open(os.path.join(bq, "lib", "core_v1.py"), "rb").read()).hexdigest()
    job_src = re.sub(r'"core_v1.py": "[^"]*"', '"core_v1.py": "%s"' % core_sha, job_src)   # the build note pins it
    job0 = os.path.join(tmp, "gm_core_v1_unset.py")
    open(job0, "w", encoding="utf-8").write(job_src)
    stub_sha = hashlib.sha256(open(stub, "rb").read()).hexdigest()
    job1 = os.path.join(tmp, "gm_core_v1_stub.py")
    open(job1, "w", encoding="utf-8").write(job_src.replace("REBUILD_SHA = None", 'REBUILD_SHA = "%s"' % stub_sha))

    def go(job):
        q = subprocess.run([sys.executable, job], cwd=loc, env=env, capture_output=True, text=True, timeout=600)
        return q.stdout + q.stderr
    o0 = go(job0)
    check("job (PC layout): REBUILD_SHA unset -> STOP after the lib checks, before the store",
          "PASS gm code vs reference" in o0 and o0.count("PASS lib ") == 8 and
          "STOP: REBUILD_SHA not registered" in o0 and "lock id" not in o0, o0[-900:])
    o1 = go(job1)
    check("job: the stub registered -> rebuild sha and import scan PASS; no diag report -> STOP before the store",
          "PASS lib rebuild_s4.py" in o1 and "PASS rebuild_s4.py imports none" in o1 and
          "FAIL A2 report gm_a2_v1.txt: missing" in o1 and "lock id" not in o1, o1[-900:])
    os.makedirs(os.path.join(loc, "results"))
    open(os.path.join(loc, "results", "gm_a2_v1.txt"), "w").write(DS.a2_report_text())
    o2 = go(job1)
    check("job: A2 report PASS, no diagnostics report -> STOP before the store",
          "PASS A2 report gm_a2_v1.txt: ok" in o2 and "FAIL diagnostics report gm_diag_v1.txt: missing" in o2 and
          "lock id" not in o2, o2[-900:])
    open(os.path.join(loc, "results", "gm_diag_v1.txt"), "w").write(diag_text())
    o3 = go(job1)
    check("job: diagnostics report PASS (A3 empty), a non-LOCK_v2 store -> STOP before any value is read",
          "PASS diagnostics report gm_diag_v1.txt: ok" in o3 and "FAIL Bloomberg store lock id" in o3 and
          "STOP: the Bloomberg store is not LOCK_v2 (nothing read)" in o3, o3[-900:])
    with open(os.path.join(lib, "rebuild_s4.py"), "a") as f:
        f.write("\nimport gm\n")
    o4 = go(job1.replace("_stub", "_stub"))
    check("job: a changed rebuild_s4.py stops it at the sha check", "FAIL lib rebuild_s4.py" in o4 and
          "STOP: rebuild_s4.py differs" in o4 and "lock id" not in o4, o4[-600:])
    gm_sha = hashlib.sha256(open(os.path.join(lib, "rebuild_s4.py"), "rb").read()).hexdigest()
    job2 = os.path.join(tmp, "gm_core_v1_gm.py")
    open(job2, "w", encoding="utf-8").write(job_src.replace("REBUILD_SHA = None", 'REBUILD_SHA = "%s"' % gm_sha))
    o5 = go(job2)
    check("job: a rebuild that imports gm stops it (not independent)", "FAIL rebuild_s4.py imports none" in o5 and
          "STOP: the rebuild imports the engine" in o5 and "lock id" not in o5, o5[-600:])
    shutil.copy(stub, os.path.join(lib, "rebuild_s4.py"))
    with open(os.path.join(lib, "core_v1.py"), "a") as f:
        f.write("\n# changed\n")
    o6 = go(job1)
    check("job: a changed core_v1.py stops it at the hash check", "FAIL lib core_v1.py" in o6 and
          "STOP: lib file differs from the registered build: core_v1.py" in o6, o6[-600:])
    check("job output: no number with 5+ decimals", not re.findall(r"\d\.\d{5,}", o0 + o1 + o2 + o3 + o4 + o5 + o6))
    pyc = [os.path.join(d, x) for d, _s, fs in os.walk(lib) for x in fs if x.endswith(".pyc")]
    check("job (C4): sys.dont_write_bytecode, so no .pyc is written under lib\\ (lib modules and the gm package)",
          not pyc, pyc[:3])


if __name__ == "__main__":
    fails = []

    def check(name, ok, detail=""):
        print(("PASS " if ok else "FAIL ") + name + ("" if ok else "  " + str(detail)[:600]))
        if not ok:
            fails.append(name)
    run(check)
    print("CORE V1 SMOKE " + ("PASSED" if not fails else "FAILED: %d" % len(fails)))
    sys.exit(1 if fails else 0)
