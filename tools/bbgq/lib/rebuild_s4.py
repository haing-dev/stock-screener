"""rebuild_s4: independent rebuild of the Core parts of the existing macro book from the written specs alone
(TESTING_PROTOCOL 7.6 step 6 check S4; WORKFLOW 4.5: design net Sharpe and annualised mean each within 15% relative).

Written by a separate agent WITHOUT reading the engine's signal / book code (gm/signals.py, gm/book.py, gm/vol.py,
gm/execution.py, gm/config.py, the A2 / diagnostics / Core-book libraries) or any engine result. Sources:
docs/research/specs/SPEC_Trend.md, SPEC_Carry.md, SPEC_Value.md; TESTING_PROTOCOL 7.2-7.4 and 7.6; gm/CHANGES.md rule
text (E4, E5, E6, E9, E13, gm-2.2.1, the gm-2.1.0 closed items); the input layer (gm/panel.py, gm/daily.py,
gm/seal.py, tools/bbgq/lib/a1_panel.py) for data formats only; the interface docs/research/batches/S4_INTERFACE.md.
Every reading the written rules leave open is listed in docs/research/batches/S4_REBUILD_NOTES.md as N1, N2, ...
(cited in the code below).

API (S4_INTERFACE s1):  part_returns(inputs, cut="2010-12-31") -> {"trend", "carry", "value_eq", "carry_fx_v2",
"carry_energy": monthly NET return Series at k = 1, PeriodIndex "M", each part held alone at the 10% target}.
build(inputs, cut) returns the same plus positions and intermediate pieces (for the self-test).

Only the standard library, numpy and pandas. No file, network or environment access; no randomness; no printing.
"""
import numpy as np
import pandas as pd

VERSION = "rebuild_s4-1.0.0"
SEAL = "2010-12-31"
SQ12 = np.sqrt(12.0)

# -------------------------------------------------------------------------------------------- registered constants
TREND_LOOKBACKS = (1, 3, 12)       # A2-final Trend form (CANDIDATE): mean of the signs of 1-, 3-, 12-month returns
SIZE = 0.40                        # position per unit score = 0.40 / vol (SPEC_Trend s3 step 5, SPEC_Carry s3)
SCALE_WIN, SCALE_MIN, SCALE_CAP = 36, 24, 50.0   # block and part scaler (SPEC_Trend s5; CHANGES gm-2.1.0 closed 5)
TARGET = 0.10                      # book volatility target (SPEC_Trend s5)
CAP_K = 0.10 * 0.10 * 3            # per-market cap = 0.10 x 0.10 x 3 / vol (SPEC_Trend s5)
GROSS_MAX = 5.0                    # gross face value at most 5x (SPEC_Trend s5)
BORROW = 0.01                      # 1 %/yr on short emerging equity positions (SPEC_Trend s9)
RANK_MIN = 3                       # cs_rank needs at least 3 markets with a value (SPEC_Carry s3, SPEC_Value s3)
AQR = "cm_aqr_ew"                  # Trend market, CM block only (gm-2.2.1)
ENERGY = ("cm_wti", "cm_natgas", "cm_heatoil", "cm_gasoline")      # Carry CM markets (SPEC_Carry s4)
VALUE_EQ = ("eq_us_spx", "eq_gb_ftse", "eq_jp_nikkei", "eq_au_asx", "eq_ca_tsx", "eq_hk_hsi", "eq_de_dax",
            "eq_fr_cac")           # SPEC_Value s4 (the other 10 indexes have no dividend yield)
DEFAULT_CLASSES = {"EQ": ("eq_",), "FI": ("bd_", "st_"), "FX": ("fx_",), "CM": ("cm_",)}
KEYS = ("trend", "carry", "value_eq", "carry_fx_v2", "carry_energy")


# =================================================================================================== seal (7.3 item 5)
def _end_of(cut):
    return pd.Timestamp(cut).normalize() + pd.Timedelta(hours=23, minutes=59, seconds=59)


def _cut(x, cut):
    """The input without rows dated after the cut: monthly frames keep months up to the cut's month, daily frames and
    calendars keep days up to the cut's close."""
    if x is None:
        return None
    if isinstance(x, pd.PeriodIndex):
        return x[x <= pd.Period(pd.Timestamp(cut), "M")]
    if isinstance(x, pd.DatetimeIndex):
        return x[x <= _end_of(cut)]
    idx = x.index
    if isinstance(idx, pd.PeriodIndex):
        return x.loc[idx <= pd.Period(pd.Timestamp(cut), "M")].copy()
    if isinstance(idx, pd.DatetimeIndex):
        return x.loc[idx <= _end_of(cut)].copy()
    raise TypeError("input without a Period or Datetime index")


def _check_sealed(s, cut, where):
    late = s.index > pd.Period(pd.Timestamp(cut), "M")
    if bool(s[late].notna().any()):
        raise RuntimeError("seal breached in %s" % where)


# =================================================================================================== class lists
def class_members(columns, classes, cls):
    """Markets of a class by prefix (inputs["classes"]); sp_* spreads belong to no class. cm_aqr_ew is a Trend market
    of the CM block only (gm-2.2.1): it carries the cm_ prefix, so the prefix rule already puts it there alone."""
    pre = tuple(classes[cls])
    return [c for c in columns if str(c).startswith(pre)]


# =================================================================================================== signal pieces
def cs_rank(sig, min_n=RANK_MIN):
    """SPEC_Carry s3 step 5 / SPEC_Value s3 step 6: ranks in class demeaned, scaled to sum |w| = 1, times the count;
    only with at least min_n markets with a value (N6: ties take the average rank; markets ranked = those with a
    value that month)."""
    rk = sig.rank(axis=1, method="average")
    n = rk.notna().sum(axis=1)
    dm = rk.sub(rk.mean(axis=1), axis=0)
    s = dm.abs().sum(axis=1)
    w = dm.div(s.where(s > 0), axis=0).mul(n, axis=0)
    ok = n.ge(min_n) & s.gt(0)
    return w.where(np.repeat(ok.values[:, None], w.shape[1], axis=1)).where(sig.notna())


def sign0(x):
    """sign, 0 if exactly 0, missing stays missing (SPEC_Carry s3 version 1, SPEC_Trend s3 step 2)."""
    return np.sign(x)


def size_in_class(w, vol, cols):
    """p = clip(w, -1, 1) x 0.40 / vol, divided by the count of markets in the class with a position that month
    (SPEC_Trend s3 step 5; SPEC_Carry s3; SPEC_Value s3). A market without a vol has no position (N7)."""
    cols = [c for c in cols if c in w.columns]
    if not cols:
        return None
    v = vol.reindex(index=w.index, columns=cols)
    p = w[cols].clip(-1, 1) * SIZE / v.where(v > 0)
    n = p.notna().sum(axis=1)
    return p.div(n.where(n > 0), axis=0)


def trend_level(R):
    """Compounded level: cumulative product of (1 + R, gaps as 0), defined where data exist (SPEC_Trend s3)."""
    return (1 + R.fillna(0.0)).cumprod().where(R.notna())


def trend_score(R, lookbacks=TREND_LOOKBACKS):
    """A2-final Trend: mean over h of sign(lvl(t) / lvl(t - h) - 1). N1: no score unless every lookback has a value."""
    lvl = trend_level(R)
    parts = [sign0(lvl / lvl.shift(h) - 1) for h in lookbacks]
    total = parts[0]
    for p in parts[1:]:
        total = total + p                       # NaN wherever one lookback is missing
    return total / len(parts)


def combine_versions(vs):
    """Pod position = mean of the version positions, a missing version counted as 0; a market-month where no version
    has a position holds none (SPEC_Trend s3 step 6, SPEC_Carry s3; CHANGES gm-2.1.0 closed 3)."""
    vs = [v for v in vs if v is not None]
    cols = sorted(set().union(*[set(v.columns) for v in vs]))
    idx = vs[0].index
    tot = sum(v.reindex(index=idx, columns=cols).fillna(0.0) for v in vs)
    has = sum(v.reindex(index=idx, columns=cols).notna().astype(int) for v in vs) > 0
    return (tot / len(vs)).where(has)


# =================================================================================================== k = 1 returns
def nyse_firsts(days, months):
    """First NYSE day of each month (NaT where the calendar has none)."""
    d = pd.DatetimeIndex(days).normalize().sort_values()
    if not len(d):
        return pd.Series(pd.NaT, index=months)
    first = pd.Series(d, index=d.to_period("M")).groupby(level=0).min()
    return first.reindex(months)


def k1_returns(R, D, days, cut):
    """7.3 item 2 and CHANGES gm-2.1.0 closed item 2. Earned return in month t of the holding decided at month-end t-1:
    R(t) + pr(m, first NYSE day of t+1) - pr(m, first NYSE day of t), pr = that day's price return (bd_/st_: the daily
    file's price return; others: exp(log return) - 1). Where a needed price is missing: R(t), flagged. Holding cut:
    where the first day of t+1 lies after the cut (or after the calendar), the holding ends at the close of month-end
    t: R(t) - pr(m, first day of t), not flagged (if that price is missing: R(t), flagged). Returns (R_earn, flags)."""
    T = _end_of(cut)
    months = R.index
    f_now = nyse_firsts(days, months)
    nxt = months + 1
    f_next = nyse_firsts(days, nxt)
    f_next.index = months
    last_cal = pd.DatetimeIndex(days).max().to_period("M") if len(days) else None
    after = np.array([(pd.notna(z) and z > T) or (pd.isna(z) and (last_cal is None or nm > last_cal))
                      or nm > pd.Period(pd.Timestamp(cut), "M")
                      for z, nm in zip(f_next.values, nxt)], dtype=bool)
    i_now = pd.DatetimeIndex(f_now.values)
    i_next = pd.DatetimeIndex(f_next.values)
    RE = R.copy()
    FL = pd.DataFrame(False, index=months, columns=R.columns)
    for m in R.columns:
        r = R[m].to_numpy(dtype=float)
        if D is None or m not in D.columns:
            FL[m] = ~np.isnan(r)
            continue
        x = D[m].dropna()
        x = x[~x.index.duplicated(keep="last")]
        pr = x if str(m).startswith(("bd_", "st_")) else np.expm1(x)
        p0 = pr.reindex(i_now).to_numpy(dtype=float)
        p1 = pr.reindex(i_next).to_numpy(dtype=float)
        full = ~after & ~np.isnan(p0) & ~np.isnan(p1)
        cutc = after & ~np.isnan(p0)
        RE[m] = np.where(full, r + p1 - p0, np.where(cutc, r - p0, r))
        FL[m] = ~(full | cutc) & ~np.isnan(r)
    return RE, FL


# =================================================================================================== scalers, caps, costs
def held_return(pos, R):
    """Return over month t of the position held from month-end t-1 on the k = 0 panel returns (the scalers read k = 0
    returns: CHANGES gm-2.1.0 closed 2); missing in months without a held position."""
    held = pos.shift(1)
    r = (held * R.reindex(index=pos.index, columns=pos.columns)).sum(axis=1, min_count=1)
    return r.where(held.notna().any(axis=1))


def scaler(r, target=1.0, cap=SCALE_CAP):
    """target / (36-month realised volatility of r, at least 24 months, x sqrt(12)); k(t) uses r up to and including
    month t and multiplies the position decided at month-end t (N4)."""
    v = r.rolling(SCALE_WIN, min_periods=SCALE_MIN).std() * SQ12
    k = target / v.where(v > 0)
    return k.clip(upper=cap) if cap is not None else k


def costs(pos, table, em_borrow, mult=1.0):
    """Cost of the position decided at month-end t, charged in month t+1 (N8): one-way bp x |change| + rolls
    (2 x one-way bp x rolls per year / 12 x |position|) + borrow 1 %/yr on short emerging equity positions."""
    P = pos.fillna(0.0)
    dP = (P - P.shift(1).fillna(0.0)).abs()
    bp = pd.Series({m: float(table[m][0]) for m in P.columns}) / 1e4
    ro = pd.Series({m: float(table[m][1]) for m in P.columns})
    c = dP.mul(bp, axis=1) + P.abs().mul(2.0 * bp * ro / 12.0, axis=1)
    em = [m for m in P.columns if m in set(em_borrow)]
    if em:
        c[em] = c[em] + (-P[em].clip(upper=0.0)) * BORROW / 12.0
    return mult * c.sum(axis=1).shift(1)


def hold_alone(blocks, R, RE, vol, table, em_borrow, cost_mult=1.0):
    """One part held alone (TESTING_PROTOCOL 7.4 E9; CHANGES gm-2.1.0 closed item 5 with n = 1): every class block
    scaled to unit volatility on its own returns (multiplier capped at 50); part = sum of the scaled blocks, scaled to
    unit volatility on the part return sum_b r_b(t) k_b(t-1); weight 1/n = 1; book scaled to 10% on its own return;
    per-market cap 0.03 / vol; gross face value at most 5x; costs; net return at k = 1."""
    scaled, rets = [], []
    for name in sorted(blocks):
        P = blocks[name]
        if P is None or not P.notna().any().any():
            continue
        r = held_return(P, R)
        k = scaler(r)
        scaled.append(P.mul(k, axis=0))
        rets.append(r * k.shift(1))
    if not scaled:
        raise ValueError("part without positions")
    idx = R.index
    cols = sorted(set().union(*[set(x.columns) for x in scaled]))
    tot = sum(x.reindex(index=idx, columns=cols).fillna(0.0) for x in scaled)
    has = sum(x.reindex(index=idx, columns=cols).notna().astype(int) for x in scaled) > 0
    part = tot.where(has)
    r_part = pd.concat([x.reindex(idx) for x in rets], axis=1).sum(axis=1, min_count=1)
    k_part = scaler(r_part)
    n_parts = 1
    r_pre = r_part * k_part.shift(1) / n_parts                  # the book's return before its own scaler
    k_book = scaler(r_pre, target=TARGET, cap=None)            # N5: no multiplier cap on the book scaler
    pos = part.mul(k_part / n_parts, axis=0).mul(k_book, axis=0)
    v = vol.reindex(index=idx, columns=cols)
    lim = CAP_K / v.where(v > 0)
    pos = pos.clip(lower=-lim, upper=lim)                      # N7: NaN limit leaves the value as is
    gross = pos.abs().sum(axis=1)
    pos = pos.mul((GROSS_MAX / gross.where(gross > GROSS_MAX)).fillna(1.0), axis=0)
    held = pos.shift(1)
    g = (held * RE.reindex(index=idx, columns=cols)).sum(axis=1, min_count=1)
    active = held.abs().sum(axis=1) > 0
    c = costs(pos, table, em_borrow, cost_mult)
    net = (g.fillna(0.0) - c.fillna(0.0)).where(active)
    return {"pos": pos, "net": net, "gross": g.where(active), "cost": c.where(active), "k_part": k_part,
            "k_book": k_book}


# =================================================================================================== the parts
def _prepare(inputs, cut):
    R = _cut(inputs["R"], cut).astype(float)
    D = _cut(inputs["D"], cut) if inputs.get("D") is not None else None
    days = _cut(pd.DatetimeIndex(inputs["days"]).normalize(), cut)
    C = _cut(inputs["C"], cut).reindex(R.index).astype(float)
    V = _cut(inputs["V"], cut).reindex(R.index).astype(float)
    vol = _cut(inputs["vol"], cut).reindex(R.index).astype(float)
    classes = inputs.get("classes") or DEFAULT_CLASSES
    table = inputs["cost"]
    em = tuple(inputs.get("em_borrow", ()))
    return R, D, days, C, V, vol, classes, table, em


def trend_blocks(R, vol, classes):
    """SPEC_Trend s3 / s4: every class of the 61 markets plus cm_aqr_ew in CM; the A2-final single form."""
    s = trend_score(R)
    out = {}
    for cls in ("EQ", "FI", "FX", "CM"):
        cols = class_members(R.columns, classes, cls)
        out[cls] = size_in_class(s, vol, cols)
    return out


def carry_blocks(C, vol, classes):
    """SPEC_Carry s3: FX version 2 (rank) as the Core component (its term p_v2 / 2 of the pod average; 7.2 item 5);
    CM = (version 1 sign + version 2 rank) / 2, missing version = 0. C already holds E13 for natgas, gasoline."""
    fx = [c for c in class_members(C.columns, classes, "FX")]
    cm = [c for c in ENERGY if c in C.columns]
    out = {}
    if fx:
        p2 = size_in_class(cs_rank(C[fx]), vol, fx)
        out["FX"] = p2 / 2.0
    if cm:
        p1 = size_in_class(sign0(C[cm]), vol, cm)
        p2 = size_in_class(cs_rank(C[cm]), vol, cm)
        out["CM"] = combine_versions([p1, p2])
    return out


def value_eq_block(V, vol):
    """SPEC_Value s3 / s4: equities, dividend yield (E4 already in V), rank in class, long cheap. Version 2's equity
    leg equals version 1, so the pod average of the two equals one version (the A2-final book has version 1 only)."""
    eq = [c for c in VALUE_EQ if c in V.columns]
    return {"EQ": size_in_class(cs_rank(V[eq]), vol, eq)}


def build(inputs, cut=SEAL, cost_mult=1.0):
    R, D, days, C, V, vol, classes, table, em = _prepare(inputs, cut)
    RE, FL = k1_returns(R, D, days, cut)
    tb, cb, vb = trend_blocks(R, vol, classes), carry_blocks(C, vol, classes), value_eq_block(V, vol)
    spec = {"trend": tb, "carry": cb, "value_eq": vb,
            "carry_fx_v2": {"FX": cb.get("FX")}, "carry_energy": {"CM": cb.get("CM")}}
    out = {}
    for k in KEYS:
        res = hold_alone(spec[k], R, RE, vol, table, em, cost_mult)
        res["blocks"] = spec[k]
        out[k] = res
    out["_k1_flags"] = FL
    out["_R_earn"] = RE
    return out


def part_returns(inputs, cut=SEAL):
    """S4_INTERFACE s1: monthly NET returns at k = 1, cost multiple 1, each part held alone."""
    res = build(inputs, cut)
    out = {}
    for k in KEYS:
        s = res[k]["net"].astype(float)
        s = s[s.index <= pd.Period(pd.Timestamp(cut), "M")]
        s = s.where(np.isfinite(s))
        _check_sealed(s, cut, k)
        out[k] = s
    return out
