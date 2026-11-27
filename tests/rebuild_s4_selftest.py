"""Self-test of tools/bbgq/lib/rebuild_s4.py (1.1.0, interface v2: RAW inputs) on SYNTHETIC data only (no statistic
of real data is computed).

Covers: the interface (keys, PeriodIndex "M", floats, no value after the cut, >= 120 months in 1975-2010, finite);
the seal (raw inputs dated after the cut change nothing; pre-cut inputs give the same output; a truncated run agrees
with the full run up to the month before its cut); no look-ahead (perturbing every raw monthly input from month t0
and the daily input after t0's first day leaves positions, returns AND the derived carry, value and vol measures
before t0 unchanged; controls show the perturbation bites); hand cases of cs_rank, trend score, the registered gap
rule, k = 1 returns and holding cut, costs, scalers, the currency carry lag, energy carry, E13, the dividend yield
with E4 and the US clip, and the hybrid volatility (daily fast, monthly fallback, blend with slow, point in time);
M1 (rank weights are not clipped, Trend's score is); signs (long trend, long high carry, long cheap); class rules
(cm_aqr_ew in the Trend CM block only, sp_* never held); caps; the import rule of S4_INTERFACE s3.

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


FXCC = {"fx_jpy": "JP", "fx_gbp": "GB", "fx_aud": "AU", "fx_mxn": "MX"}
FRENCH7 = ["eq_de_dax", "eq_gb_ftse", "eq_fr_cac", "eq_jp_nikkei", "eq_ca_tsx", "eq_au_asx", "eq_hk_hsi"]


def make_inputs(seed=7, end="2012-12"):
    """RAW inputs in the shape of S4_INTERFACE v2 s2 (smaller universe; data after 2010-12 present to test the seal)."""
    rng = np.random.default_rng(seed)
    months = pd.period_range("1960-01", end, freq="M")
    T = len(months)
    trend = np.cumsum(rng.normal(0, 0.004, (T, len(COLS))), axis=0) * 0.2
    R = pd.DataFrame(rng.normal(0.002, 0.03, (T, len(COLS))) + trend * 0.05, index=months, columns=COLS)
    starts = {"eq_br_ibov": "1975-06", "fx_mxn": "1972-01", "cm_natgas": "1971-01", "cm_gasoline": "1985-01",
              "cm_gold": "1980-01", "st_jp_2y": "1966-01"}
    for c, st in starts.items():
        R.loc[R.index < pd.Period(st, "M"), c] = np.nan
    R.loc[R.index > pd.Period("2000-12", "M"), "cm_aqr_ew"] = np.nan
    R.loc[pd.Period("1988-04", "M"), "eq_jp_nikkei"] = np.nan          # an interior gap
    days = pd.bdate_range("1962-01-02", pd.Period(end, "M").to_timestamp(how="end").normalize())
    D = pd.DataFrame(rng.normal(0, 0.008, (len(days), len(COLS) - 3)), index=days,
                     columns=[c for c in COLS if c not in ("cm_aqr_ew", "sp_us_2s10s", "cm_gold")])
    D.loc[D.index < pd.Timestamp("1980-01-01"), "fx_aud"] = np.nan
    rate = pd.DataFrame(5 + np.cumsum(rng.normal(0, 0.2, (T, 5)), axis=0), index=months,
                        columns=["US", "JP", "GB", "AU", "MX"])
    rate.loc[rate.index < pd.Period("1971-06", "M"), "MX"] = np.nan
    eia = {}
    for m, st in (("cm_wti", "1983-04"), ("cm_natgas", "1990-05"), ("cm_heatoil", "1983-04"),
                  ("cm_gasoline", "1985-01")):
        f1 = 50 * np.exp(np.cumsum(rng.normal(0, 0.05, T)))
        seas = 0.02 * np.sin(2 * np.pi * np.array([p.month for p in months]) / 12) if m == "cm_natgas" else 0
        f2 = f1 * (1 + rng.normal(0, 0.01, T) + seas)
        f = pd.DataFrame({1: f1, 2: f2}, index=months)
        f.loc[f.index < pd.Period(st, "M")] = np.nan
        eia[m] = f
    fw = pd.DataFrame(np.nan, index=months, columns=FRENCH7)
    fwo = fw.copy()
    for m in ("eq_gb_ftse", "eq_jp_nikkei", "eq_de_dax"):
        base = rng.normal(0.005, 0.04, T)
        fwo[m] = base
        fw[m] = base + np.abs(rng.normal(0.003, 0.001, T))
    fw.loc[fw.index < pd.Period("1975-01", "M")] = np.nan
    fwo.loc[fwo.index < pd.Period("1975-01", "M")] = np.nan
    usp = pd.Series(rng.normal(0.006, 0.04, T), index=months)
    ust = (usp + np.abs(rng.normal(0.0018, 0.0005, T))).where(months >= pd.Period("1993-02", "M"))
    cost = {c: ((1.0, 4) if c.startswith(("bd_", "st_")) else (2.0, 4) if c.startswith(("eq_", "fx_")) else (4.0, 12))
            for c in COLS}
    return {"R": R, "D": D, "days": days, "rate3m": rate, "fx_rate_country": dict(FXCC), "eia": eia,
            "french_with": fw, "french_without": fwo, "us_total": ust, "us_price": usp, "cost": cost,
            "em_borrow": ("eq_br_ibov",), "classes": {"EQ": ("eq_",), "FI": ("bd_", "st_"), "FX": ("fx_",),
                                                     "CM": ("cm_",)}, "meta": {"name": "synthetic"}}


MONTHLY_KEYS = ("R", "rate3m", "french_with", "french_without", "us_total", "us_price")


def monthly_frames(x):
    """Every monthly raw frame of an inputs dict (eia frames included), as (container, key) pairs."""
    out = [(x, k) for k in MONTHLY_KEYS]
    out += [(x["eia"], m) for m in x["eia"]]
    return out


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
for cont, key in monthly_frames(inp2):
    X = cont[key]
    late = X.index > pd.Period("2010-12", "M")
    cont[key] = X.mask(np.repeat(late[:, None], X.shape[1], 1) if X.ndim == 2 else late,
                       rng.normal(0, 0.5, X.shape) * 3 + 1)
late_d = inp2["D"].index > pd.Timestamp("2010-12-31")
inp2["D"].loc[late_d] = rng.normal(0, 0.2, inp2["D"].loc[late_d].shape)
out2 = RB.part_returns(inp2)
check("seal: inputs after 2010-12-31 change nothing",
      all(out[k].equals(out2[k]) for k in RB.KEYS))
sealed = copy.deepcopy(inp)
for cont, key in monthly_frames(sealed):
    cont[key] = cont[key].loc[cont[key].index <= pd.Period("2010-12", "M")]
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
for cont, key in monthly_frames(inp4):
    X = cont[key]
    m = X.index >= t0
    cont[key] = X.mask(np.repeat(m[:, None], X.shape[1], 1) if X.ndim == 2 else m, X * 1.7 + 0.01)
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
meas_same = all(np.allclose(b0[k][b0[k].index < t0].values, b4[k][b4[k].index < t0].values, rtol=0, atol=1e-13,
                            equal_nan=True) for k in ("_C", "_V", "_vol"))
meas_changed = all(not np.allclose(b0[k].loc[t0:].values, b4[k].loc[t0:].values, equal_nan=True)
                   for k in ("_C", "_V", "_vol"))
check("no look-ahead: carry, value and vol measures before t0 unchanged", meas_same)
check("control: each measure changes from t0", meas_changed)
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
sc_aqr = RB.trend_score(inp["R"][["cm_aqr_ew"]])
check("cm_aqr_ew after its data end: gap rule read literally (flat level after 2000-12: score 0 from 2001-12)",
      bool((sc_aqr.loc[pd.Period("2001-12", "M"):, "cm_aqr_ew"] == 0).all())
      and bool(sc_aqr.loc[pd.Period("2001-04", "M"):pd.Period("2001-11", "M"), "cm_aqr_ew"].abs().eq(1 / 3).all()))
s = RB.trend_score(inp["R"]).reindex(tb["EQ"].index)
sel = tb["EQ"].notna() & s[tb["EQ"].columns].notna()
check("Trend sign: position has the sign of the score",
      not bool(((np.sign(tb["EQ"]) != np.sign(s[tb["EQ"].columns])) & sel).any().any()) and bool(sel.any().any()))
cb = b["carry"]["blocks"]
m = pd.Period("2005-06", "M")
fx = [c for c in cb["FX"].columns if pd.notna(cb["FX"].loc[m, c])]
ordc = b["_C"].loc[m, fx].sort_values().index
check("Carry v2: highest carry long, lowest short",
      cb["FX"].loc[m, ordc[-1]] > 0 and cb["FX"].loc[m, ordc[0]] < 0)
vb = b["value_eq"]["blocks"]["EQ"]
eqm = [c for c in vb.columns if pd.notna(vb.loc[m, c])]
ordv = b["_V"].loc[m, eqm].sort_values().index
check("Value: cheapest (highest yield) long, dearest short", vb.loc[m, ordv[-1]] > 0 and vb.loc[m, ordv[0]] < 0)
check("Value: only the 8 registered equity markets", set(vb.columns) <= set(RB.VALUE_EQ))
check("Carry part = FX v2 + CM blocks; legs alone have one block each",
      set(cb) == {"FX", "CM"} and set(b["carry_fx_v2"]["blocks"]) == {"FX"}
      and set(b["carry_energy"]["blocks"]) == {"CM"})
pos = b["trend"]["pos"]
lim = RB.CAP_K / b["_vol"].reindex(index=pos.index, columns=pos.columns)
check("per-market cap respected", bool((pos.abs() <= lim + 1e-12).where(pos.notna(), True).all().all()))
check("gross face value <= 5", bool((pos.abs().sum(axis=1) <= RB.GROSS_MAX + 1e-12).all()))
dbl = RB.build(copy.deepcopy(inp), cost_mult=2.0)
check("cost multiple 2 doubles the cost", np.allclose(dbl["trend"]["cost"].dropna(),
                                                      2 * b["trend"]["cost"].dropna()))


# ------------------------------------------------------------------------------------------------ 5b. M1: clip Trend only
mm = pd.period_range("2000-01", periods=2, freq="M")
w3 = RB.cs_rank(pd.DataFrame([[1.0, 2.0, 3.0], [3.0, 1.0, 2.0]], index=mm, columns=["a", "b", "c"]))
vv = pd.DataFrame(0.2, index=mm, columns=["a", "b", "c"])
p_rank = RB.size_in_class(w3, vv, ["a", "b", "c"])
check("M1: rank weights are not clipped (|w| 1.5 -> p = 1.5 x 0.40 / vol / 3)",
      np.isclose(p_rank.loc[mm[0], "c"], 1.5 * 0.40 / 0.2 / 3) and np.isclose(p_rank.loc[mm[0], "a"], -1.5 * 0.40 / 0.2 / 3))
p_clip = RB.size_in_class(w3, vv, ["a", "b", "c"], clip=True)
check("M1: Trend's sizing clips to [-1, 1]", np.isclose(p_clip.loc[mm[0], "c"], 1.0 * 0.40 / 0.2 / 3))
vb_full = b["value_eq"]["blocks"]["EQ"]
nn = vb_full.notna().sum(axis=1)
unit = (vb_full.mul(nn, axis=0) * b["_vol"][vb_full.columns] / 0.40).abs()
check("M1 in the build: Value equity weights above 1 survive (rank of 4 markets: 1.5 x 4 / 4 ... max > 1)",
      float(unit.max().max()) > 1.0 + 1e-9)
cbf = b["carry"]["blocks"]["FX"]
nfx = cbf.notna().sum(axis=1)
ufx = (cbf.mul(2 * nfx, axis=0) * b["_vol"][cbf.columns] / 0.40).abs()
check("M1 in the build: Carry FX v2 rank weights above 1 survive", float(ufx.max().max()) > 1.0 + 1e-9)

# ------------------------------------------------------------------------------------------------ 5c. measures by hand
mo = pd.period_range("2000-01", periods=4, freq="M")
rt = pd.DataFrame({"US": [5.0, 4.0, 3.0, 2.0], "JP": [1.0, 1.0, 2.0, np.nan]}, index=mo)
cf = RB.carry_fx(rt, {"fx_jpy": "JP"})["fx_jpy"]
check("carry FX: (local - US) / 100 of the PREVIOUS month", np.isnan(cf.iloc[0]) and np.isclose(cf.iloc[1], -0.04)
      and np.isclose(cf.iloc[2], -0.03) and np.isclose(cf.iloc[3], -0.01))
e = {"cm_wti": pd.DataFrame({1: [110.0, 100.0, 90.0, np.nan], 2: [100.0, 100.0, 0.0, 50.0]}, index=mo)}
ce = RB.carry_energy(e)["cm_wti"]
check("carry energy: 12 x (F1 / F2 - 1), missing where F2 <= 0 or F1 missing",
      np.isclose(ce.iloc[0], 1.2) and np.isclose(ce.iloc[1], 0.0) and np.isnan(ce.iloc[2]) and np.isnan(ce.iloc[3]))
mx = pd.period_range("1990-01", "2000-12", freq="M")
pat = pd.Series([float(p.month) for p in mx], index=mx)
adj = RB.x1_adjust(pat)
check("E13: removes a pure calendar pattern (constant after adjustment)", np.allclose(adj.dropna(), 6.5))
check("E13: first value after 12 months + five earlier same-month values (1995-12)",
      str(adj.first_valid_index()) == "1995-12")
pat2 = pat.copy()
pat2.loc[pd.Period("1998-03", "M"):] += 100.0
adj2 = RB.x1_adjust(pat2)
check("E13: point in time (a later change leaves earlier values)",
      np.allclose(adj.loc[:pd.Period("1998-02", "M")].dropna(), adj2.loc[:pd.Period("1998-02", "M")].dropna()))
e2 = {"cm_natgas": pd.DataFrame({1: 1 + pat / 100, 2: pd.Series(1.0, index=mx)}, index=mx),
      "cm_wti": pd.DataFrame({1: 1 + pat / 100, 2: pd.Series(1.0, index=mx)}, index=mx)}
ce2 = RB.carry_energy(e2)
check("E13 applies to natgas only, not WTI", np.allclose(ce2["cm_wti"], 12 * pat / 100)
      and np.allclose(ce2["cm_natgas"].dropna(), 12 * 6.5 / 100))
md = pd.period_range("1990-01", periods=60, freq="M")
fw = pd.DataFrame({"eq_gb_ftse": 0.012}, index=md)
fwo = pd.DataFrame({"eq_gb_ftse": 0.010}, index=md)
fw.loc[md[30], "eq_gb_ftse"] = np.nan
ust = pd.Series(0.02, index=md)
ust.iloc[:3] = np.nan
usp = pd.Series(0.0, index=md)
dy = RB.dividend_yield(fw, fwo, ust, usp)
check("dividend yield (E4): 12-month sum ending at t - 12, first at month 24",
      dy["eq_gb_ftse"].iloc[:23].isna().all() and np.isclose(dy["eq_gb_ftse"].iloc[23], 0.024))
check("dividend yield: a missing month removes the 12 sums that need it (12 months later under the lag)",
      dy["eq_gb_ftse"].iloc[42:54].isna().all() and np.isclose(dy["eq_gb_ftse"].iloc[41], 0.024)
      and np.isclose(dy["eq_gb_ftse"].iloc[54], 0.024))
check("dividend yield US: no lag, all 12 months needed, clipped at 0.10",
      dy["eq_us_spx"].iloc[:14].isna().all() and np.isclose(dy["eq_us_spx"].iloc[14], 0.10))
usn = pd.Series(-0.01, index=md)
check("dividend yield US: clipped at 0 below", np.isclose(RB.dividend_yield(fw, fwo, usn, usp)["eq_us_spx"].iloc[-1], 0))

# ------------------------------------------------------------------------------------------------ 5d. volatility by hand
mv = pd.period_range("1990-01", "2005-12", freq="M")
Rv = pd.DataFrame({"a": np.tile([0.03, -0.03], len(mv) // 2), "b": np.tile([0.02, -0.02], len(mv) // 2)}, index=mv)
dv = pd.bdate_range("1990-01-01", "2005-12-31")
Dv = pd.DataFrame({"a": np.tile([0.01, -0.01], len(dv) // 2 + 1)[:len(dv)]}, index=dv)
vh = RB.vol_hybrid(Rv, Dv)
fast_a, slow_a = 0.01 * np.sqrt(252), Rv["a"].iloc[-120:].std() * np.sqrt(12)
check("vol: daily fast = sqrt(252 x EWMA of squared daily returns)",
      np.isclose(vh.loc[mv[5], "a"], fast_a))
check("vol: hybrid = max(0.7 fast + 0.3 slow, 0.75 slow) once 36 months exist",
      np.isclose(vh.loc[mv[-1], "a"], max(0.7 * fast_a + 0.3 * slow_a, 0.75 * slow_a)))
fast_b = 0.02 * np.sqrt(12)
slow_b = Rv["b"].iloc[-120:].std() * np.sqrt(12)
check("vol: no daily data -> monthly EWMA fast (sqrt(12 x EWMA of squared R))", np.isclose(vh.loc[mv[20], "b"], fast_b))
check("vol: monthly fast blended with slow", np.isclose(vh.loc[mv[-1], "b"], max(0.7 * fast_b + 0.3 * slow_b,
                                                                                    0.75 * slow_b)))
check("vol: nothing before 12 months without daily data; daily from 40 days",
      vh["b"].iloc[:11].isna().all() and vh["a"].iloc[0:1].isna().all() and pd.notna(vh.loc[mv[1], "a"]))
Dv2 = Dv.copy()
Dv2.loc[Dv2.index > pd.Timestamp("1999-06-30")] *= 5
vh2 = RB.vol_hybrid(Rv, Dv2)
check("vol: point in time (later daily data leave earlier month-ends)",
      np.allclose(vh.loc[:pd.Period("1999-06", "M")], vh2.loc[:pd.Period("1999-06", "M")], equal_nan=True)
      and not np.isclose(vh.loc[pd.Period("1999-07", "M"), "a"], vh2.loc[pd.Period("1999-07", "M"), "a"]))

# ------------------------------------------------------------------------------------------------ 5e. registered gap rule
Rg = pd.DataFrame({"x": [0.01, 0.02, np.nan, 0.03, -0.05] + [0.01] * 10}, index=pd.period_range("2000-01", periods=15,
                                                                                                 freq="M"))
lv = RB.trend_level(Rg)["x"]
check("gap rule: the level exists at a gap month and stays flat there", np.isclose(lv.iloc[2], lv.iloc[1]))
Rg2 = Rg.copy()
Rg2.iloc[0] = np.nan
check("gap rule: level missing only before the first return", np.isnan(RB.trend_level(Rg2)["x"].iloc[0])
      and RB.trend_level(Rg2)["x"].iloc[1:].notna().all())
check("gap rule: a score exists at and after the gap once 12 months back exist",
      RB.trend_score(Rg)["x"].iloc[12:].notna().all())

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
