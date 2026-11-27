"""rebuild_s4: independent rebuild of the Core parts of the existing macro book from the written specs alone
(TESTING_PROTOCOL 7.6 step 6 check S4; WORKFLOW 4.5: design net Sharpe and annualised mean each within 15% relative).

Written by a separate agent WITHOUT reading the engine's signal / book code (gm/signals.py, gm/book.py, gm/vol.py,
gm/execution.py, gm/config.py, the A2 / diagnostics / Core-book libraries) or any engine result. Sources:
docs/research/specs/SPEC_Trend.md, SPEC_Carry.md, SPEC_Value.md; TESTING_PROTOCOL 7.2-7.4 and 7.6; gm/CHANGES.md rule
text (E4, E5, E6, E9, E13, gm-2.2.1, the gm-2.1.0 closed items); the input layer (gm/panel.py, gm/daily.py,
gm/seal.py, tools/bbgq/lib/a1_panel.py) for data formats only; the interface docs/research/batches/S4_INTERFACE.md.
Every reading the written rules leave open is listed in docs/research/batches/S4_REBUILD_NOTES.md as N1, N2, ...
(cited in the code below).

API (S4_INTERFACE v2 s1):  part_returns(inputs, cut="2010-12-31") -> {"trend", "carry", "value_eq", "carry_fx_v2",
"carry_energy": monthly NET return Series at k = 1, PeriodIndex "M", each part held alone at the 10% target}.
inputs = the RAW inputs of interface v2 s2 (R, D, days, rate3m, fx_rate_country, eia, french_with, french_without,
us_total, us_price, cost, em_borrow, classes, meta); the carry measure, the value measure and the hybrid volatility
are derived here from the spec text (interface v2 s2a). build(inputs, cut) returns the same plus positions, measures
and intermediate pieces (for the self-test).

1.1.0 (2026-11-27): M1 of the independent check (rank and sign weights are no longer clipped; only Trend's score is,
N16); interface v2 (raw inputs: measures C, V and vol derived here, N17-N23); registered gap rule of SPEC_Trend s3
(N2 amended, N24).

Only the standard library, numpy and pandas. No file, network or environment access; no randomness; no printing.
"""
import numpy as np
import pandas as pd

VERSION = "rebuild_s4-1.1.0"
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
X1_MARKETS = ("cm_natgas", "cm_gasoline")   # E13: the X1 gate opened for these two (gm/CHANGES.md "X1 outcome")
X1_MIN = 5                         # at least five earlier same-calendar values (SPEC_Carry s3)
FRENCH7 = ("eq_de_dax", "eq_gb_ftse", "eq_fr_cac", "eq_jp_nikkei", "eq_ca_tsx", "eq_au_asx", "eq_hk_hsi")
DY_LAG = 12                        # E4: non-US dividend yield ending at t - 12
DAILY_DAYS = 252                   # trading days a year for the daily EWMA (N21)


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


def size_in_class(w, vol, cols, clip=False):
    """p = w x 0.40 / vol (SPEC_Carry s3 lines 50-52, SPEC_Value s3 line 58: ranks and signs are NOT clipped), or
    clip(w, -1, 1) x 0.40 / vol for Trend's score only (clip=True; SPEC_Trend s3 lines 49, 62; N16); divided by the
    count of markets in the class with a position that month (a zero position counts, N25). A market without a vol
    has no position (N7)."""
    cols = [c for c in cols if c in w.columns]
    if not cols:
        return None
    v = vol.reindex(index=w.index, columns=cols)
    x = w[cols].clip(-1, 1) if clip else w[cols]
    p = x * SIZE / v.where(v > 0)
    n = p.notna().sum(axis=1)
    return p.div(n.where(n > 0), axis=0)


def trend_level(R):
    """Compounded level (SPEC_Trend s3 with its 2026-11-27 amendment, the registered gap rule N2): cumulative product of
    (1 + R) with a month without a return adding 0, existing at every month from the market's first return onward
    (interior gaps and, read literally, months after its last return too: N24); missing only before the first
    return."""
    started = R.notna().cummax()
    return (1 + R.fillna(0.0)).cumprod().where(started)


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


# =================================================================================================== measures (S4_INTERFACE v2 s2a)
def carry_fx(rate3m, fx_rate_country):
    """SPEC_Carry s3 step 2: (local 3-month rate - US 3-month rate) / 100, lagged 1 month: the value at month-end t uses
    the monthly-average rates of month t - 1 (rates in percent a year -> decimal a year). Missing if either is missing."""
    us = rate3m["US"]
    out = {}
    for m, cc in fx_rate_country.items():
        if cc in rate3m.columns:
            out[m] = ((rate3m[cc] - us) / 100.0).shift(1)
    return pd.DataFrame(out, index=rate3m.index)


def _contract(f, n):
    for key in (n, str(n)):
        if key in f.columns:
            return f[key].astype(float)
    return pd.Series(np.nan, index=f.index)


def x1_adjust(c):
    """E13 (SPEC_Carry s3; CHANGES "X1 outcome" closed item 3): d(t) = carry(t) minus the mean of the 12 month-ends up
    to and including t (all 12 present); adjusted carry(t) = carry(t) minus the mean of d over all EARLIER month-ends of
    the same calendar month (strictly before t; at least five values of d); missing where carry or that mean is
    missing (N19)."""
    d = c - c.rolling(12, min_periods=12).mean()
    out = pd.Series(np.nan, index=c.index)
    cal = np.array([p.month for p in c.index])
    for mo in range(1, 13):
        sel = cal == mo
        ds = d[sel]
        prior_sum = ds.fillna(0.0).cumsum().shift(1)
        prior_n = ds.notna().astype(int).cumsum().shift(1)
        seas = prior_sum / prior_n.where(prior_n >= X1_MIN)
        out[sel] = (c[sel] - seas).values
    return out


def carry_energy(eia):
    """SPEC_Carry s3 step 3: 12 x (F1 / F2 - 1) from NYMEX contracts 1 and 2 at month-end t (positive =
    backwardation); E13 for cm_natgas and cm_gasoline only (CHANGES "X1 outcome"). Missing where F2 is not positive."""
    out = {}
    for m in ENERGY:
        if m not in eia:
            continue
        f1, f2 = _contract(eia[m], 1), _contract(eia[m], 2)
        c = 12.0 * (f1 / f2.where(f2 > 0) - 1.0)
        out[m] = x1_adjust(c) if m in X1_MARKETS else c
    return pd.DataFrame(out)


def dividend_yield(french_with, french_without, us_total, us_price):
    """SPEC_Value s3 item 1 with E4 (TESTING_PROTOCOL 7.4; CHANGES gm-1.2.3 closed item 3): seven countries = 12-month
    sum of (Ken French return with minus without dividends), all 12 months needed, the sum ENDING AT t - 12 used at t
    (no carry-forward, not clipped: N20); US = 12-month sum of (SPY total return - ^GSPC price return), all 12 needed,
    clipped to [0, 0.10], at t (no lag). Higher = cheaper."""
    out = {}
    for m in FRENCH7:
        if m in french_with.columns and m in french_without.columns:
            dsum = (french_with[m] - french_without[m]).rolling(12, min_periods=12).sum()
            out[m] = dsum.shift(DY_LAG)
    us = (us_total - us_price).rolling(12, min_periods=12).sum().clip(lower=0.0, upper=0.10)
    out["eq_us_spx"] = us
    return pd.DataFrame(out, index=french_with.index)


def vol_m36(R):
    """SPEC_Trend s3 step 4: 36-month standard deviation of monthly R, at least 12 months, x sqrt(12)."""
    return R.rolling(36, min_periods=12).std() * SQ12


def _month_end_rows(daily, months):
    """The row of a daily frame at the last day at or before each month's last calendar day (N22)."""
    ends = months.to_timestamp(how="end").normalize()
    return daily.reindex(pd.DatetimeIndex(ends), method="ffill").set_axis(months)


def vol_hybrid(R, D):
    """SPEC_Trend s3 step 4 ("hybrid", the A2-final model for every pod and the cap), annualised:
    fast = sqrt(252 x EWMA of daily squared returns, half-life 35 days, at least 40 daily values) where the market has
    such an estimate at month-end t (D's values as given: log returns, price returns for bd_/st_), else
    sqrt(12 x EWMA of monthly squared R, half-life 6 months, at least 12); slow = 120-month standard deviation of R,
    at least 36, x sqrt(12); hybrid = max(0.7 fast + 0.3 slow, 0.75 slow); fast alone until slow exists; m36 where
    neither exists. EWMAs: no mean removed, half-lives on the input's own time axis (daily rows of D, months of R),
    pandas ewm defaults (adjust=True, a missing value keeps the last estimate) (N21-N23)."""
    months = R.index
    fast_m = np.sqrt((R ** 2).ewm(halflife=6, min_periods=12).mean() * 12.0)
    fast = fast_m.copy()
    if D is not None and len(D):
        cols = [c for c in D.columns if c in R.columns]
        if cols:
            Dd = D[cols].sort_index()
            Dd = Dd[~Dd.index.duplicated(keep="last")]
            dv = (Dd ** 2).ewm(halflife=35, min_periods=40).mean()
            fd = np.sqrt(_month_end_rows(dv, months) * DAILY_DAYS)
            fast[cols] = fd.combine_first(fast_m[cols])
    slow = R.rolling(120, min_periods=36).std() * SQ12
    hyb = np.maximum(0.7 * fast + 0.3 * slow, 0.75 * slow)
    hyb = hyb.where(slow.notna() & fast.notna(), fast)
    hyb = hyb.where(hyb.notna(), vol_m36(R))
    return hyb.where(hyb > 0)


# =================================================================================================== the parts
def _prepare(inputs, cut):
    """Every raw input cut at the seal BEFORE any measure is computed (7.3 item 5; N15); then the measures."""
    R = _cut(inputs["R"], cut).astype(float)
    D = _cut(inputs["D"], cut).astype(float) if inputs.get("D") is not None else None
    days = _cut(pd.DatetimeIndex(inputs["days"]).normalize(), cut)
    idx = R.index
    rate = _cut(inputs["rate3m"], cut).reindex(idx).astype(float)
    eia = {m: _cut(f, cut).reindex(idx) for m, f in inputs["eia"].items()}
    fw = _cut(inputs["french_with"], cut).reindex(idx).astype(float)
    fwo = _cut(inputs["french_without"], cut).reindex(idx).astype(float)
    ust = _cut(inputs["us_total"], cut).reindex(idx).astype(float)
    usp = _cut(inputs["us_price"], cut).reindex(idx).astype(float)
    C = pd.concat([carry_fx(rate, inputs["fx_rate_country"]), carry_energy(eia)], axis=1).reindex(idx)
    V = dividend_yield(fw, fwo, ust, usp).reindex(idx)
    C = C[[c for c in C.columns if c in R.columns]]         # a measure counts only for a market of the panel (N11)
    V = V[[c for c in V.columns if c in R.columns]]
    vol = vol_hybrid(R, D)
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
        out[cls] = size_in_class(s, vol, cols, clip=True)
    return out


def carry_blocks(C, vol, classes):
    """SPEC_Carry s3: FX version 2 (rank) as the Core component (its term p_v2 / 2 of the pod average; 7.2 item 5);
    CM = (version 1 sign + version 2 rank) / 2, missing version = 0. C holds E13 for natgas and gasoline."""
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
    """SPEC_Value s3 / s4: equities, dividend yield (with E4), rank in class, long cheap. Version 2's equity
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
    out["_C"], out["_V"], out["_vol"] = C, V, vol
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
