"""Self-test of tools/bbgq/lib/rebuild_s4.py on SYNTHETIC data only (no statistic of real data is computed).

Covers: the interface (keys, PeriodIndex "M", floats, no value after the cut, >= 120 months in 1975-2010, finite),
the seal (inputs dated after the cut change nothing; a truncated run agrees with the full run up to the month before
its cut), no look-ahead (perturbing month t0 and later leaves every position before t0 and every return before t0
unchanged), the registered formulas on hand-made cases (cs_rank, trend score, k = 1 return and holding cut, costs,
scaler), signs (long trend, long high carry, long cheap), class rules (cm_aqr_ew in the Trend CM block only, sp_*
never held), caps, and the import rule of S4_INTERFACE s3.

Run: python3 tests/rebuild_s4_selftest.py   (prints PASS / FAIL lines; exit code 1 on any failure)
"""
import copy
import os
import re
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(os.path.dirname(HERE), "tools", "bbgq", "lib")
sys.path.insert(0, LIB)
import rebuild_s4 as RB  # noqa: E402

FAILS = []


def check(name, ok):
    print("%s %s" % ("PASS" if ok else "FAIL", name))
    if not ok:
        FAILS.append(name)


# ------------------------------------------------------------------------------------------------ synthetic inputs
EQ = ["eq_us_spx", "eq_gb_ftse", "eq_jp_nikkei", "eq_de_dax", "eq_br_ibov"]
FI = ["bd_us_10y", "bd_de_10y", "st_jp_2y"]
FX = ["fx_jpy", "fx_gbp", "fx_aud", "fx_mxn"]
CM = ["cm_wti", "cm_natgas", "cm_heatoil", "cm_gasoline", "cm_gold", "cm_aqr_ew"]
SP = ["sp_us_2s10s"]
COLS = EQ + FI + FX + CM + SP


def make_inputs(seed=7, end="2012-12"):
    rng = np.random.default_rng(seed)
    months = pd.period_range("1960-01", end, freq="M")
    T = len(months)
    trend = np.cumsum(rng.normal(0, 0.004, (T, len(COLS))), axis=0) * 0.2
    R = pd.DataFrame(rng.normal(0.002, 0.03, (T, len(COLS))) + trend * 0.05, index=months, columns=COLS)
    starts = {"eq_br_ibov": "1975-06", "fx_mxn": "1972-01", "cm_natgas": "1971-01", "cm_gasoline": "1985-01",
              "cm_gold": "1980-01", "st_jp_2y": "1966-01"}
    for c, s in starts.items():
        R.loc[R.index < pd.Period(s, "M"), c] = np.nan
    R.loc[R.index > pd.Period("2000-12", "M"), "cm_aqr_ew"] = np.nan
    days = pd.bdate_range("1970-01-02", pd.Period(end, "M").to_timestamp(how="end").normalize())
    D = pd.DataFrame(rng.normal(0, 0.008, (len(days), len(COLS) - 2)), index=days, columns=COLS[:-2])
    D.loc[D.index < pd.Timestamp("1980-01-01"), "fx_aud"] = np.nan
    vol = pd.DataFrame(0.10 + 0.05 * rng.random((T, len(COLS))), index=months, columns=COLS).where(R.notna())
    ccols = FI + FX + ["cm_wti", "cm_natgas", "cm_heatoil", "cm_gasoline"]
    C = pd.DataFrame(rng.normal(0.01, 0.02, (T, len(ccols))), index=months, columns=ccols).where(R[ccols].notna())
    vcols = [c for c in COLS if c.startswith(("fx_", "bd_", "eq_"))]
    V = pd.DataFrame(rng.normal(0.03, 0.01, (T, len(vcols))), index=months, columns=vcols)
    V.loc[V.index < pd.Period("1976-01", "M"), [c for c in vcols if c.startswith("eq_")]] = np.nan
    cost = {c: ((1.0, 4) if c.startswith(("bd_", "st_")) else (2.0, 4) if c.startswith(("eq_", "fx_")) else (4.0, 12))
            for c in COLS}
    return {"R": R, "D": D, "days": days, "C": C, "V": V, "vol": vol, "cost": cost,
            "em_borrow": ("eq_br_ibov",), "classes": {"EQ": ("eq_",), "FI": ("bd_", "st_"), "FX": ("fx_",),
                                                     "CM": ("cm_",)}, "meta": {"name": "synthetic"}}


# ------------------------------------------------------------------------------------------------ 1. interface
inp = make_inputs()
out = RB.part_returns(copy.deepcopy(inp))
check("all five keys", set(out) == set(RB.KEYS))
for k, s in out.items():
    ok = (isinstance(s, pd.Series) and isinstance(s.index, pd.PeriodIndex) and s.index.freqstr in ("M", "ME")
          and s.dtype == float)
    check("%s: Series, PeriodIndex M, float" % k, ok)
    check("%s: no value after the cut month" % k, not s[s.index > pd.Period("2010-12", "M")].notna().any())
    d = s[(s.index >= pd.Period("1975-01", "M")) & (s.index <= pd.Period("2010-12", "M"))].dropna()
    check("%s: >= 120 months in 1975-2010" % k, len(d) >= 120)
    check("%s: finite" % k, bool(np.isfinite(s.dropna()).all()))
check("VERSION constant", re.fullmatch(r"rebuild_s4-\d+\.\d+\.\d+", RB.VERSION) is not None)

# ------------------------------------------------------------------------------------------------ 2. seal
inp2 = copy.deepcopy(inp)
rng = np.random.default_rng(99)
late_m = inp2["R"].index > pd.Period("2010-12", "M")
for key in ("R", "C", "V", "vol"):
    X = inp2[key]
    X.loc[late_m[:len(X)] if len(X) == len(late_m) else X.index > pd.Period("2010-12", "M")] = \
        rng.normal(0, 0.5, X.loc[X.index > pd.Period("2010-12", "M")].shape)
late_d = inp2["D"].index > pd.Timestamp("2010-12-31")
inp2["D"].loc[late_d] = rng.normal(0, 0.2, inp2["D"].loc[late_d].shape)
out2 = RB.part_returns(inp2)
check("seal: inputs after 2010-12-31 change nothing",
      all(out[k].equals(out2[k]) for k in RB.KEYS))
sealed = {k: copy.deepcopy(v) for k, v in inp.items()}
for key in ("R", "C", "V", "vol"):
    sealed[key] = sealed[key].loc[sealed[key].index <= pd.Period("2010-12", "M")]
sealed["D"] = sealed["D"].loc[sealed["D"].index <= pd.Timestamp("2010-12-31")]
sealed["days"] = sealed["days"][sealed["days"] <= pd.Timestamp("2010-12-31")]
out3 = RB.part_returns(sealed)
check("seal: inputs already cut give the same output", all(out[k].equals(out3[k]) for k in RB.KEYS))
full = RB.build(copy.deepcopy(inp))
check("holding cut: 2010-12 earned return = R - first-day price return (not flagged)",
      abs(full["_R_earn"].loc[pd.Period("2010-12", "M"), "eq_us_spx"]
          - (inp["R"].loc[pd.Period("2010-12", "M"), "eq_us_spx"]
             - np.expm1(inp["D"].loc[pd.Timestamp("2010-12-01"), "eq_us_spx"]))) < 1e-15
      and not bool(full["_k1_flags"].loc[pd.Period("2010-12", "M"), "eq_us_spx"]))
for T in ("1990-06-30", "1998-06-30", "2003-11-30"):
    cutT = RB.part_returns(copy.deepcopy(inp), cut=T)
    PT = pd.Period(T[:7], "M")
    same = all(np.allclose(out[k][out[k].index < PT].values, cutT[k][cutT[k].index < PT].reindex(
        out[k][out[k].index < PT].index).values, rtol=0, atol=1e-13, equal_nan=True) for k in RB.KEYS)
    nothing_after = all(not cutT[k][cutT[k].index > PT].notna().any() for k in RB.KEYS)
    check("truncation at %s: equal to the full run before the cut month, nothing after it" % T,
          same and nothing_after)

# ------------------------------------------------------------------------------------------------ 3. no look-ahead
t0 = pd.Period("1995-03", "M")
inp4 = copy.deepcopy(inp)
for key in ("R", "C", "V", "vol"):
    X = inp4[key]
    m = X.index >= t0
    X.loc[m] = X.loc[m] * 1.7 + 0.01
first_day_t0 = inp4["days"][inp4["days"].to_period("M") == t0].min()
md = inp4["D"].index > first_day_t0
inp4["D"].loc[md] = inp4["D"].loc[md] * -2.0
b0, b4 = RB.build(copy.deepcopy(inp)), RB.build(inp4)
pos_same = all(np.allclose(b0[k]["pos"][b0[k]["pos"].index < t0].values,
                           b4[k]["pos"][b4[k]["pos"].index < t0].values, rtol=0, atol=1e-13, equal_nan=True)
               for k in RB.KEYS)
ret_same = all(np.allclose(b0[k]["net"][b0[k]["net"].index < t0].values,
                           b4[k]["net"][b4[k]["net"].index < t0].values, rtol=0, atol=1e-13, equal_nan=True)
               for k in RB.KEYS)
changed = any(not np.allclose(b0[k]["pos"].loc[t0:].values, b4[k]["pos"].loc[t0:].values, equal_nan=True)
              for k in RB.KEYS)
check("no look-ahead: positions before t0 unchanged when month t0 and later change", pos_same)
check("no look-ahead: net returns before t0 unchanged", ret_same)
check("control: the perturbation does change positions from t0", changed)

# ------------------------------------------------------------------------------------------------ 4. formulas by hand
sig = pd.DataFrame([[1.0, 2.0, 3.0, np.nan], [5.0, 5.0, 1.0, 2.0], [1.0, 2.0, np.nan, np.nan]],
                   index=pd.period_range("2000-01", periods=3, freq="M"), columns=list("abcd"))
w = RB.cs_rank(sig)
check("cs_rank row 1 = (-1.5, 0, 1.5)", np.allclose(w.iloc[0, :3].values, [-1.5, 0, 1.5]))
check("cs_rank: sum |w| = count, sum w = 0", np.isclose(w.iloc[1].abs().sum(), 4) and np.isclose(w.iloc[1].sum(), 0))
check("cs_rank: fewer than 3 markets -> no weight", w.iloc[2].isna().all())

Rh = pd.DataFrame({"x": [0.01] * 13 + [-0.5]}, index=pd.period_range("2000-01", periods=14, freq="M"))
sc = RB.trend_score(Rh)["x"]
check("trend score: missing until 12 months back exist", sc.iloc[:12].isna().all())
check("trend score: all three signs positive -> +1", np.isclose(sc.iloc[12], 1.0))
check("trend score: 1m and 3m negative, 12m negative too -> -1",
      np.isclose(sc.iloc[13], -1.0))   # 12-month compounded: 1.01^12 x 0.5 < 1
Rh2 = pd.DataFrame({"x": [0.05] * 11 + [-0.02] * 3}, index=pd.period_range("2000-01", periods=14, freq="M"))
check("trend score: 1m, 3m negative, 12m positive -> -1/3", np.isclose(RB.trend_score(Rh2)["x"].iloc[13], -1 / 3))

mo = pd.period_range("2001-01", "2001-03", freq="M")
dd = pd.bdate_range("2001-01-01", "2001-03-30")
Rk = pd.DataFrame({"eq_a": [0.02, 0.03, 0.01], "bd_b": [0.01, 0.0, 0.02]}, index=mo)
Dk = pd.DataFrame({"eq_a": 0.0, "bd_b": 0.0}, index=dd)
Dk.loc[pd.Timestamp("2001-02-01"), "eq_a"] = np.log(1.01)
Dk.loc[pd.Timestamp("2001-03-01"), "eq_a"] = np.log(0.98)
Dk.loc[pd.Timestamp("2001-02-01"), "bd_b"] = 0.004
Dk.loc[pd.Timestamp("2001-03-01"), "bd_b"] = np.nan
RE, FL = RB.k1_returns(Rk, Dk, dd, "2001-03-31")
check("k = 1: R(t) + pr(first day t+1) - pr(first day t)", np.isclose(RE.loc[mo[1], "eq_a"], 0.03 - 0.02 - 0.01))
check("k = 1: log -> price return", np.isclose(RE.loc[mo[0], "eq_a"], 0.02 + 0.01 - 0.0))
check("k = 1: bonds use the daily price return as is", np.isclose(RE.loc[mo[0], "bd_b"], 0.01 + 0.004))
check("k = 1: missing daily price -> k = 0 return, flagged",
      np.isclose(RE.loc[mo[1], "bd_b"], 0.0) and bool(FL.loc[mo[1], "bd_b"]))
check("k = 1: last month holding cut at the cut close", np.isclose(RE.loc[mo[2], "eq_a"], 0.01 - (0.98 - 1))
      and not bool(FL.loc[mo[2], "eq_a"]))
RE0, FL0 = RB.k1_returns(pd.DataFrame({"eq_a": [0.01, 0.02]}, index=pd.period_range("1969-11", periods=2, freq="M")),
                         Dk[["eq_a"]], dd, "2001-03-31")
check("k = 1: months without a calendar day are flagged and earn k = 0", bool(FL0.all().all()))

P = pd.DataFrame({"eq_a": [0.0, 1.0, 1.0, -0.5], "eq_em": [0.0, -2.0, -2.0, 0.0]},
                 index=pd.period_range("2002-01", periods=4, freq="M"))
cst = RB.costs(P, {"eq_a": (2.0, 4), "eq_em": (5.0, 0)}, ("eq_em",))
exp1 = 1.0 * 2e-4 + 1.0 * 2 * 2e-4 * 4 / 12 + 2.0 * 5e-4 + 2.0 * 0.01 / 12
check("costs: change + rolls + EM borrow, charged the month after the decision",
      np.isnan(cst.iloc[0]) and np.isclose(cst.iloc[2], exp1))
r = pd.Series(np.r_[np.full(23, np.nan), np.tile([0.01, -0.01], 20)], index=pd.period_range("1990-01", periods=63,
                                                                                            freq="M"))
k = RB.scaler(r)
check("scaler: none before 24 months of returns", k.iloc[:46].isna().all() and k.iloc[46:].notna().all())
check("scaler: 1 / (36-month std x sqrt 12)", np.isclose(k.iloc[-1], 1 / (r.iloc[-36:].std() * np.sqrt(12))))

# ------------------------------------------------------------------------------------------------ 5. signs and classes
b = RB.build(copy.deepcopy(inp))
tb = b["trend"]["blocks"]
check("cm_aqr_ew in the Trend CM block only", "cm_aqr_ew" in tb["CM"].columns and
      all("cm_aqr_ew" not in tb[c].columns for c in ("EQ", "FI", "FX")))
check("sp_* never held", all(not any(c.startswith("sp_") for c in b[k]["pos"].columns) for k in RB.KEYS))
check("cm_aqr_ew holds nothing after 2000-12 + 1",
      not b["trend"]["pos"].loc[pd.Period("2001-02", "M"):, "cm_aqr_ew"].fillna(0).abs().gt(0).any())
s = RB.trend_score(inp["R"]).reindex(tb["EQ"].index)
sel = tb["EQ"].notna() & s[tb["EQ"].columns].notna()
check("Trend sign: position has the sign of the score",
      not bool(((np.sign(tb["EQ"]) != np.sign(s[tb["EQ"].columns])) & sel).any().any()) and bool(sel.any().any()))
cb = b["carry"]["blocks"]
m = pd.Period("2005-06", "M")
fx = [c for c in cb["FX"].columns if pd.notna(cb["FX"].loc[m, c])]
ordc = inp["C"].loc[m, fx].sort_values().index
check("Carry v2: highest carry long, lowest short",
      cb["FX"].loc[m, ordc[-1]] > 0 and cb["FX"].loc[m, ordc[0]] < 0)
vb = b["value_eq"]["blocks"]["EQ"]
eqm = [c for c in vb.columns if pd.notna(vb.loc[m, c])]
ordv = inp["V"].loc[m, eqm].sort_values().index
check("Value: cheapest (highest yield) long, dearest short", vb.loc[m, ordv[-1]] > 0 and vb.loc[m, ordv[0]] < 0)
check("Value: only the 8 registered equity markets", set(vb.columns) <= set(RB.VALUE_EQ))
check("Carry part = FX v2 + CM blocks; legs alone have one block each",
      set(cb) == {"FX", "CM"} and set(b["carry_fx_v2"]["blocks"]) == {"FX"}
      and set(b["carry_energy"]["blocks"]) == {"CM"})
pos = b["trend"]["pos"]
lim = RB.CAP_K / inp["vol"].reindex(index=pos.index, columns=pos.columns)
check("per-market cap respected", bool((pos.abs() <= lim + 1e-12).where(pos.notna(), True).all().all()))
check("gross face value <= 5", bool((pos.abs().sum(axis=1) <= RB.GROSS_MAX + 1e-12).all()))
dbl = RB.build(copy.deepcopy(inp), cost_mult=2.0)
check("cost multiple 2 doubles the cost", np.allclose(dbl["trend"]["cost"].dropna(),
                                                      2 * b["trend"]["cost"].dropna()))

# ------------------------------------------------------------------------------------------------ 6. import rule
src = open(os.path.join(LIB, "rebuild_s4.py")).read()
bad = re.findall(r"^\s*(?:import|from)\s+(gm|gm_engine|a1_panel|a2_batch|diag_a2|core_v1|bbgdata|bbg_panel)\b", src,
                 re.M)
imps = set(re.findall(r"^\s*(?:import|from)\s+([A-Za-z_][\w.]*)", src, re.M))
check("imports only numpy / pandas (S4_INTERFACE s3 item 1)", not bad and imps <= {"numpy", "pandas"})
check("no file, network or environment access in the module",
      not re.search(r"\bopen\(|os\.environ|urllib|requests|socket|random\.", src))

print("REBUILD_S4 SELFTEST %s (%d failures)" % ("PASSED" if not FAILS else "FAILED", len(FAILS)))
sys.exit(1 if FAILS else 0)
