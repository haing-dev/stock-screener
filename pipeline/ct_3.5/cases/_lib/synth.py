"""Synthetic monthly futures panel for the step 3.5 checker test (no market data).

make_panel(seed) -> dict with
  R      : monthly excess returns (month-end index 1970-01..2015-12), 32 markets in 4 classes, NaN before a
           market's first month. Return of month t is earned over month t (from the end of t-1 to the end of t).
  CARRY  : carry of each market observed at the month-end close (% a year; FI yield minus 3m rate, FX rate gap vs
           USD, CM annualised front/second contract roll yield, EQ dividend yield minus 3m rate).
  VALUE  : valuation level observed at the month-end close (log units; FI real-yield level, FX log real exchange
           rate, CM log real price, EQ log earnings yield). Only changes and comparisons over time are meaningful:
           every market has its own unknown offset.
  MACRO  : US consumer price index by REFERENCE month (index 1970-01..2015-12). The value for reference month t is
           published around the 15th of month t+1, so at the close of month t the latest known value is t-1.
  CLASS  : market -> class ("EQ", "FI", "FX", "CM").
  START  : market -> first month with a return.

Everything is deterministic given the seed. Every backtest in cases/ calls make_panel() with the default seed.
"""
import numpy as np
import pandas as pd

SEED = 20261124
FIRST, LAST = "1970-01-31", "2015-12-31"

# id, class, first month, annual vol
MARKETS = [
    ("eq_us", "EQ", "1970-01", 0.16), ("eq_jp", "EQ", "1970-01", 0.19), ("eq_de", "EQ", "1970-01", 0.20),
    ("eq_uk", "EQ", "1970-01", 0.17), ("eq_fr", "EQ", "1972-01", 0.20), ("eq_au", "EQ", "1977-01", 0.17),
    ("eq_hk", "EQ", "1980-01", 0.27), ("eq_kr", "EQ", "1990-01", 0.30),
    ("bd_us10", "FI", "1970-01", 0.075), ("bd_de10", "FI", "1970-01", 0.060), ("bd_jp10", "FI", "1972-01", 0.055),
    ("bd_uk10", "FI", "1970-01", 0.085), ("bd_ca10", "FI", "1975-01", 0.075), ("bd_au10", "FI", "1985-01", 0.085),
    ("st_us2", "FI", "1977-01", 0.022), ("st_de2", "FI", "1991-01", 0.018),
    ("fx_eur", "FX", "1999-01", 0.10), ("fx_jpy", "FX", "1972-01", 0.11), ("fx_gbp", "FX", "1972-01", 0.10),
    ("fx_chf", "FX", "1972-01", 0.115), ("fx_aud", "FX", "1976-01", 0.11), ("fx_cad", "FX", "1972-01", 0.06),
    ("fx_nzd", "FX", "1976-01", 0.12), ("fx_sek", "FX", "1975-01", 0.105),
    ("cm_wti", "CM", "1983-04", 0.32), ("cm_brent", "CM", "1988-07", 0.31), ("cm_natgas", "CM", "1990-04", 0.48),
    ("cm_gold", "CM", "1975-01", 0.17), ("cm_silver", "CM", "1975-01", 0.28), ("cm_copper", "CM", "1989-01", 0.25),
    ("cm_corn", "CM", "1970-01", 0.24), ("cm_soy", "CM", "1970-01", 0.23),
]
# pairs that share most of their risk; the spread between the two legs mean-reverts
PAIRS = [("bd_us10", "bd_ca10"), ("bd_de10", "bd_uk10"), ("eq_de", "eq_fr"), ("fx_aud", "fx_nzd"),
         ("cm_wti", "cm_brent"), ("cm_gold", "cm_silver"), ("cm_corn", "cm_soy"), ("fx_chf", "fx_sek"),
         ("bd_us10", "st_us2"), ("bd_de10", "st_de2")]

TREND_SCALE = {"EQ": 0.55, "FI": 0.85, "FX": 1.0, "CM": 1.15}
CARRY_COEF = {"EQ": 0.02, "FI": 0.10, "FX": 0.11, "CM": 0.10}
VALUE_KAPPA = {"EQ": 0.022, "FI": 0.014, "FX": 0.020, "CM": 0.016}
CLASS_BETA = {"EQ": 0.75, "FI": 0.65, "FX": 0.45, "CM": 0.45}


def _t(rng, df, size):
    x = rng.standard_t(df, size=size)
    return x / np.sqrt(df / (df - 2.0))


def make_panel(seed=SEED):
    rng = np.random.default_rng(seed)
    idx = pd.date_range(FIRST, LAST, freq="ME")
    T, N = len(idx), len(MARKETS)
    ids = [m[0] for m in MARKETS]
    cls = np.array([m[1] for m in MARKETS])
    sig = np.array([m[3] for m in MARKETS]) / np.sqrt(12.0)
    year = idx.year.values

    # volatility regime (global + class), log AR(1)
    h = np.zeros(T)
    for t in range(1, T):
        h[t] = 0.92 * h[t - 1] + 0.22 * rng.standard_normal()
    vm = np.exp(h - h.mean())
    vm = vm / np.sqrt(np.mean(vm ** 2))
    hc = {}
    for c in ("EQ", "FI", "FX", "CM"):
        z = np.zeros(T)
        for t in range(1, T):
            z[t] = 0.9 * z[t - 1] + 0.18 * rng.standard_normal()
        hc[c] = np.exp(z - z.mean())
        hc[c] = hc[c] / np.sqrt(np.mean(hc[c] ** 2))

    # class factors with dated shocks
    F = {c: _t(rng, 4, T) for c in ("EQ", "FI", "FX", "CM")}
    def at(s):
        return int(np.searchsorted(idx, pd.Timestamp(s) + pd.offsets.MonthEnd(0)))
    for s, v in (("1973-11", -2.5), ("1974-09", -2.8), ("1987-10", -5.5), ("1990-08", -2.4), ("1998-08", -3.2),
                 ("2001-09", -2.6), ("2002-07", -2.2), ("2008-09", -2.8), ("2008-10", -4.5), ("2011-08", -2.5)):
        F["EQ"][at(s)] += v
    for s, v in (("1979-10", -3.0), ("1980-02", -2.6), ("1987-04", -1.8), ("1994-02", -2.2), ("1994-04", -2.0),
                 ("2003-07", -2.0), ("2013-06", -2.3), ("2008-11", 3.0)):
        F["FI"][at(s)] += v
    for s, v in (("1980-01", 2.8), ("1986-01", -2.5), ("1990-08", 3.0), ("2008-07", -2.6), ("2008-10", -3.5),
                 ("2014-11", -2.8)):
        F["CM"][at(s)] += v

    # inflation (US) and its release reaction
    pi = np.zeros(T)
    e = np.zeros(T)
    base = np.interp(year + idx.month.values / 12.0, [1970, 1974, 1980, 1983, 1990, 1998, 2008, 2015],
                     [5.0, 9.0, 12.0, 4.0, 5.0, 2.0, 3.5, 1.0])
    for t in range(1, T):
        e[t] = 0.30 * e[t - 1] + rng.standard_normal()
        pi[t] = base[t] + 0.35 * e[t]
    cpi = 40.0 * np.exp(np.cumsum(pi / 1200.0 + 0.0008 * e))

    # carry, trend and value states
    car = np.zeros((T, N))
    mu = np.zeros((T, N))
    phi_c, phi_m = 0.97, 0.955
    car[0] = rng.standard_normal(N)
    mu[0] = rng.standard_normal(N) * 0.16
    for t in range(1, T):
        car[t] = phi_c * car[t - 1] + np.sqrt(1 - phi_c ** 2) * rng.standard_normal(N)
        mu[t] = phi_m * mu[t - 1] + np.sqrt(1 - phi_m ** 2) * 0.16 * rng.standard_normal(N)
    era_trend = np.where(year < 1993, 1.25, 0.75)
    tsc = np.array([TREND_SCALE[c] for c in cls])
    ccf = np.array([CARRY_COEF[c] for c in cls])
    kap = np.array([VALUE_KAPPA[c] for c in cls])
    beta = np.array([CLASS_BETA[c] for c in cls])
    anchor = rng.standard_normal(N) * 1.5
    fxm = cls == "FX"

    z = np.zeros((T, N))             # standardised returns
    x = np.zeros((T, N))             # value state (sigma units)
    x[0] = anchor + rng.standard_normal(N) * 3.0
    idio = _t(rng, 5, (T, N))
    for t in range(1, T):
        f = np.array([F[c][t] for c in cls])
        scale = vm[t] * np.array([hc[c][t] for c in cls])
        drift = (mu[t - 1] * tsc * era_trend[t] + ccf * car[t - 1] - kap * (x[t - 1] - anchor))
        z[t] = drift + scale * (beta * f + np.sqrt(1 - beta ** 2) * idio[t])
        # reaction to the CPI print for reference month t-1 (published during month t)
        z[t, cls == "FI"] -= 0.32 * e[t - 1]
        z[t, cls == "EQ"] -= 0.10 * e[t - 1]
        # carry unwinds in FX
        if idx[t].strftime("%Y-%m") in ("1976-09", "1976-10", "1992-09", "1998-10", "2008-10", "2008-11"):
            cz = car[t - 1, fxm]
            z[t, fxm] -= 1.6 * (cz - cz.mean())
        x[t] = x[t - 1] + z[t]

    # pairs: leg b shares leg a's risk, the spread mean-reverts fast
    col = {m: i for i, m in enumerate(ids)}
    for a, b in PAIRS:
        ia, ib = col[a], col[b]
        s = np.zeros(T)
        for t in range(1, T):
            s[t] = 0.80 * s[t - 1] + 0.55 * rng.standard_normal()
        ds = np.diff(s, prepend=0.0)
        common = z[:, ia]
        own = 0.35 * z[:, ib] + 0.0
        z[:, ib] = 0.94 * common + own * 0.34 - 0.5 * ds * 0.5
        z[:, ia] = common + 0.5 * ds * 0.5
        x[:, ib] = np.cumsum(z[:, ib]) + anchor[ib]

    R = pd.DataFrame(z * sig, index=idx, columns=ids)

    # observables
    lvl = {"EQ": (2.0, 1.0), "FI": (1.5, 1.2), "FX": (0.0, 2.2), "CM": (-1.0, 4.0)}
    C = np.zeros((T, N))
    for j, c in enumerate(cls):
        a0, a1 = lvl[c]
        C[:, j] = a0 + a1 * car[:, j] + 0.15 * rng.standard_normal(T)
    CARRY = pd.DataFrame(C, index=idx, columns=ids).round(3)
    offs = rng.standard_normal(N) * 0.8
    VALUE = pd.DataFrame(-(x * sig * np.sqrt(12) * 0.5) + offs, index=idx, columns=ids)
    VALUE = VALUE + pd.DataFrame(0.02 * rng.standard_normal((T, N)), index=idx, columns=ids)

    start = {m[0]: pd.Timestamp(m[2]) + pd.offsets.MonthEnd(0) for m in MARKETS}
    for k, s0 in start.items():
        R.loc[R.index < s0, k] = np.nan
        CARRY.loc[CARRY.index < s0, k] = np.nan
        VALUE.loc[VALUE.index < s0, k] = np.nan
    MACRO = pd.DataFrame({"us_cpi": cpi}, index=idx)
    return {"R": R, "CARRY": CARRY, "VALUE": VALUE, "MACRO": MACRO,
            "CLASS": {m[0]: m[1] for m in MARKETS}, "START": start}


# --- shared helpers (plain statistics, no look-ahead) ---------------------------------------------------------------
def sharpe(r):
    r = pd.Series(r).dropna()
    return float(r.mean() / r.std() * np.sqrt(12)) if len(r) > 2 and r.std() > 0 else float("nan")


def max_drawdown(r):
    w = (1 + pd.Series(r).dropna()).cumprod()
    return float((w / w.cummax() - 1).min())
