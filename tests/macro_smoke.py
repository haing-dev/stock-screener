"""Macro Compass checks: scores use only the past, the stage rule, no look-ahead in the odds, and a full build +
page on invented data (no network)."""
import gzip
import json
import os
import shutil
import tempfile

import numpy as np
import pandas as pd


def _fake_raw(raw):
    import macro.registry as R
    rng = np.random.default_rng(7)
    os.makedirs(raw, exist_ok=True)
    days = pd.date_range("1960-01-01", "2026-09-01", freq="MS")
    for sid, spec in R.FRED.items():
        idx = days[::3] if spec.get("q") else days
        v = 100 + np.cumsum(rng.normal(0, 1, len(idx)))
        if sid == "USREC":
            v = (rng.random(len(idx)) < 0.1).astype(int)
        pd.DataFrame({"date": idx.strftime("%Y-%m-%d"), "value": np.abs(v) + 1}).to_csv(os.path.join(raw, f"{sid}.csv"), index=False)
    for s in R.YAHOO + [i["etf"] for i in R.INDUSTRIES]:
        idx = pd.date_range("2002-01-01", "2026-10-01", freq="MS")
        px = 50 * np.exp(np.cumsum(rng.normal(0.006, 0.05, len(idx))))
        name = "Y_" + s.replace("-", "_").replace(".", "_")
        pd.DataFrame({"date": idx.strftime("%Y-%m-%d"), "value": px}).to_csv(os.path.join(raw, f"{name}.csv"), index=False)
    cols = sorted({c for i in R.INDUSTRIES for c in i["proxy"]})
    ind = {f"{y}-{m:02d}": {c: float(rng.normal(0.008, 0.05)) for c in cols} for y in range(1960, 2026) for m in range(1, 13)}
    ff = {k: {"Mkt-RF": float(rng.normal(0.006, 0.045)), "RF": 0.003} for k in ind}
    json.dump(ind, open(os.path.join(raw, "FR_IND.json"), "w"))
    json.dump(ff, open(os.path.join(raw, "FR_FF.json"), "w"))
    json.dump({"fred_key": False}, open(os.path.join(raw, "manifest.json"), "w"))


def run(check):
    import macro.engine as E
    import macro.registry as R
    p = E.expanding_pct(pd.Series([1.0, 2.0, 3.0, np.nan, 0.5]), 2)
    check("macro: percentile uses only past values", np.isnan(p[0]) and p[1] == 75.0 and np.isnan(p[3]) and p[4] == 12.5, str(p.tolist()))
    g = pd.Series([30.0] * 15 + [45.0] * 6 + [62.0] * 15 + [48.0] * 15, index=pd.period_range("2000-01", periods=51, freq="M"))
    st, _ = E.stages(g)
    seq = [s for i, s in enumerate(st) if s and (i == 0 or s != st.iloc[i - 1])]
    check("macro: stage rule walks the cycle", seq[-3:] == ["late", "contraction", "recovery"], str(seq))
    idx = pd.period_range("1960-01", periods=400, freq="M")
    rng = np.random.default_rng(1)
    D = pd.DataFrame({"AAA": rng.uniform(0, 100, 400)}, index=idx)
    rel = pd.DataFrame({"AAA": rng.normal(0, 0.1, 400)}, index=idx)
    a = E.odds(D, rel, 12, 0.10)["AAA"]
    rel2 = rel.copy()
    rel2.iloc[300:] = 5.0                    # change outcomes that are not yet known at month 299 + 12
    b = E.odds(D, rel2, 12, 0.10)["AAA"]
    check("macro: odds at t ignore outcomes not finished by t", a.iloc[:312].equals(b.iloc[:312]) and not a.iloc[320:].equals(b.iloc[320:]))
    tmp = tempfile.mkdtemp()
    cwd = os.getcwd()
    try:
        _fake_raw(os.path.join(tmp, "cache", "macro", "raw"))
        os.chdir(tmp)
        out = E.run(log=lambda *_: None)
        check("macro: full build on invented data", out["stage"][-1] in R.STAGES and set(out["horizons"]) == {"6", "12"}
              and len(out["industries"]) == 20 and all(len(v) == len(out["months"]) for v in out["horizons"]["12"]["backtest"]["etf"]["curves"].values()))
        import macro.site as SI
        SI.build("test-password", out_dir=os.path.join(tmp, "site"), log=lambda *_: None)
        check("macro: page built and data sealed", os.path.exists(os.path.join(tmp, "site", "data", "data.bin"))
              and json.load(open(os.path.join(tmp, "site", "data", "keyinfo.json")))["plain"] is False)
    finally:
        os.chdir(cwd)
        shutil.rmtree(tmp, ignore_errors=True)
