"""Smoke test of the X1 diagnostic statistic and the E13 seasonal adjustment (gm/CHANGES.md "X1 outcome", 2026-11-27)
on SYNTHETIC data only (no cache, no market data).
  X1   calendar_share = 1 - SS_within / SS_total (= R^2 on 12 month dummies, by least squares); 'insufficient' when a
       calendar month has fewer than 5 values; a pure seasonal series has share 1, white noise about 11 / n
  E13  x1_adjust by hand (the SPEC_Carry s3 formula, loop form); point in time (changing c after t leaves the adjusted
       value at t unchanged); no value before 12 + five earlier same-calendar months; a pure seasonal pattern is removed;
       only the markets of the config key change; BASE / CANDIDATE positions identical with or without the code path
python3 tests/gm_x1_smoke.py      (also run from tests/run_tests.py)
"""
import os
import sys

import numpy as np
import pandas as pd

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, REPO)

from gm import book as B  # noqa: E402
from gm import config as CF  # noqa: E402
from gm import diag_x1 as X1  # noqa: E402
from gm import signals as G  # noqa: E402

IDX = pd.period_range("1980-01", "2015-12", freq="M")


def adjust_by_hand(c):
    """SPEC_Carry s3 in loop form."""
    v = c.values
    n = len(v)
    d = np.full(n, np.nan)
    for i in range(11, n):
        w = v[i - 11:i + 1]
        if np.all(np.isfinite(w)):
            d[i] = v[i] - w.mean()
    out = np.full(n, np.nan)
    for i in range(n):
        if not np.isfinite(v[i]):
            continue
        prev = [d[j] for j in range(i) if c.index[j].month == c.index[i].month and np.isfinite(d[j])]
        if len(prev) >= 5:
            out[i] = v[i] - np.mean(prev)
    return pd.Series(out, index=c.index)


def run(check):
    rng = np.random.default_rng(5)
    # ---- X1 statistic
    noise = pd.Series(rng.normal(0, 1, len(IDX)), index=IDX)
    seas = pd.Series(np.tile(np.arange(12.0), len(IDX) // 12), index=IDX)
    r = X1.calendar_share(seas)
    check("X1: a pure calendar pattern has share 1", r["share"] is not None and abs(r["share"] - 1) < 1e-12)
    dummies = np.column_stack([(IDX.month == m).astype(float) for m in range(1, 13)])
    y = (seas * 0.3 + noise).values
    beta, *_ = np.linalg.lstsq(dummies, y, rcond=None)
    r2 = 1 - ((y - dummies @ beta) ** 2).sum() / ((y - y.mean()) ** 2).sum()
    got = X1.calendar_share(pd.Series(y, index=IDX))["share"]
    check("X1: share equals the R^2 of 12 calendar-month dummies (least squares)", abs(got - r2) < 1e-12,
          "%s %s" % (got, r2))
    check("X1: white noise gives a small share (about 11 / n)", X1.calendar_share(noise)["share"] < 0.1)
    short = noise.loc["1980-01":"1984-04"]            # May..Dec have 4 values
    rs = X1.calendar_share(short)
    check("X1: a calendar month with fewer than 5 values -> insufficient (no share, gate closed)",
          rs["share"] is None and rs["min_count"] == 4)
    ok5 = noise.loc["1980-01":"1984-12"]
    check("X1: exactly 5 values per calendar month is enough", X1.calendar_share(ok5)["share"] is not None)
    check("X1: gate constants as registered (0.25, 5)", X1.X1_GATE == 0.25 and X1.X1_MIN_OBS == 5)

    # ---- E13 adjustment
    c = pd.Series(rng.normal(0, 0.2, len(IDX)) + 0.5 * np.sin(2 * np.pi * IDX.month / 12), index=IDX)
    c.iloc[40:43] = np.nan                            # a gap
    a = G.x1_adjust(c)
    h = adjust_by_hand(c)
    check("E13: x1_adjust equals the SPEC_Carry s3 formula by hand", np.allclose(a.values, h.values, equal_nan=True,
                                                                              rtol=0, atol=1e-12))
    first = G.x1_adjust(c.ffill()).first_valid_index()        # no gap: first d 1980-12, five Decembers 1980-84
    check("E13: no adjusted value before 12 months + five earlier same-calendar month-ends (first 1985-12)",
          str(first) == "1985-12" and str(a.first_valid_index()) == "1986-12", "%s %s" % (first, a.first_valid_index()))
    c2 = c.copy()
    c2.loc["2000-07":] = c2.loc["2000-07":] + 100.0
    a2 = G.x1_adjust(c2)
    check("E13: point in time: changing the carry from 2000-07 on leaves every adjusted value up to 2000-06 unchanged",
          np.allclose(a.loc[:"2000-06"].values, a2.loc[:"2000-06"].values, equal_nan=True, rtol=0, atol=0))
    pure = pd.Series(np.tile(np.array([1.0, 3, 2, 5, 4, 0, -1, 2, 3, 1, 0, 2]), len(IDX) // 12), index=IDX)
    ap = G.x1_adjust(pure).dropna()
    check("E13: a pure, constant calendar pattern is removed (adjusted carry = its annual mean)",
          np.allclose(ap.values, pure.mean(), atol=1e-12))
    C = pd.DataFrame({"cm_wti": c, "cm_natgas": c * 2, "cm_heatoil": c * 3, "cm_gasoline": c * 4})
    Cx = G.x1_seasonal(C, ("cm_natgas", "cm_gasoline"))
    check("E13: only the markets of the key change", Cx["cm_wti"].equals(C["cm_wti"]) and
          Cx["cm_heatoil"].equals(C["cm_heatoil"]) and not Cx["cm_natgas"].equals(C["cm_natgas"]))
    check("E13: registered markets and configs (X1_MARKETS natgas, gasoline; BASE and CANDIDATE without the key; "
          "A1_INCUMBENT and the A2 challenger with it)",
          CF.X1_MARKETS == ("cm_natgas", "cm_gasoline") and "x1_seasonal" not in CF.BASE and
          "x1_seasonal" not in CF.CANDIDATE and CF.A1_INCUMBENT["x1_seasonal"] == CF.X1_MARKETS and
          CF.A2_CHALLENGER["x1_seasonal"] == CF.X1_MARKETS and
          {k: v for k, v in CF.A1_INCUMBENT.items() if k not in ("name", "x1_seasonal")} ==
          {k: v for k, v in CF.CANDIDATE.items() if k != "name"})

    # ---- book: CANDIDATE unchanged; A1_INCUMBENT differs only through the carry of the two markets
    mk = ["eq_us_spx", "eq_gb_ftse", "eq_jp_nikkei", "bd_us_10y", "bd_de_10y", "bd_jp_10y", "fx_eur", "fx_jpy",
          "fx_gbp", "cm_wti", "cm_natgas", "cm_heatoil", "cm_gasoline"]
    R = pd.DataFrame(rng.normal(0.003, 0.035, (len(IDX), len(mk))), index=IDX, columns=mk)
    S = {k: pd.DataFrame(rng.normal(0, 1, (len(IDX), len(mk))), index=IDX, columns=mk) for k in ("E", "C", "V")}
    S["E"] = np.tanh(S["E"] / 2)
    S["C"][["cm_natgas", "cm_gasoline"]] = S["C"][["cm_natgas", "cm_gasoline"]].add(
        np.sin(2 * np.pi * IDX.month / 12), axis=0)
    fp0, _ = B.family_positions(R, CF.CANDIDATE, None, S)
    fpx, _ = B.family_positions(R, CF.A1_INCUMBENT, None, S)
    same_other = all(fp0[f][c].equals(fpx[f][c]) for f in fp0 if f != "carry" for c in fp0[f])
    cm0, cmx = fp0["carry"]["CM"], fpx["carry"]["CM"]
    check("E13 book: A1_INCUMBENT changes only the Carry family (every other family position identical)", same_other)
    check("E13 book: the Carry CM block differs, the other Carry classes do not",
          not cm0.equals(cmx) and all(fp0["carry"][c].equals(fpx["carry"][c]) for c in fp0["carry"] if c != "CM"))
    v0, _, _ = B.family_positions(R, CF.A1_INCUMBENT, None, S, components=True)
    check("E13 book: the version path (components) gives the same Carry position as the old path",
          all(np.allclose(v0["carry"][c].values, fpx["carry"][c].values, equal_nan=True, rtol=0, atol=1e-12)
              for c in fpx["carry"]))
    sx = dict(S, C=G.x1_seasonal(S["C"], CF.X1_MARKETS))
    fpm, _ = B.family_positions(R, CF.CANDIDATE, None, sx)
    check("E13 book: the key equals feeding the adjusted carry into CANDIDATE",
          all(fpm["carry"][c].equals(fpx["carry"][c]) for c in fpx["carry"]))


if __name__ == "__main__":
    fails = []

    def check(name, ok, detail=""):
        print(("PASS " if ok else "FAIL ") + name + ("" if ok else "  " + str(detail)[:300]))
        if not ok:
            fails.append(name)
    run(check)
    print("GM X1 SMOKE " + ("PASSED" if not fails else "FAILED: %d" % len(fails)))
    sys.exit(1 if fails else 0)
