"""Execution forms of the gm-2.1.0 feature version (registered 2026-11-24, gm/CHANGES.md; TESTING_PROTOCOL 7.3).

  nyse_days        NYSE open days = the dates of the daily ^GSPC closes in the free daily file (gm/daily.py EQ_DAILY)
  k1_returns  E6   the k = 1 return of every market-month with its flag (7.3 item 2) and the holding cut (7.3 item 5)
  run_k1      E6   a book (gm.book.run) that earns the k = 1 returns; positions, scalers and caps as at k = 0
  tranches    E8   the four weekly tranches (offsets 0 / 5 / 10 / 15 NYSE days, k = 1 trades, seal and holding cut)
  spx_daily_excess E14  daily S&P 500 excess return for card 4 (SPEC_Card4 s3)
  flag_share_by_year    share of gross position in flagged market-months, by year (the k = 1 report line)

Every function is a DESIGN path: by default nothing dated after the seal (config.SEAL_END, 2010-12-31) is read, every
holding ends at the seal close at the latest, and outputs pass gm.seal.check_output. Nothing here prints a statistic.
"""
import numpy as np
import pandas as pd

from . import seal as SL

BONDLIKE = ("bd_", "st_")          # gm/daily.py: bonds and notes hold -duration x yield change (a price return already)


# --------------------------------------------------------------------------------------------------------- calendar
def nyse_days(seal="design", gspc=None):
    """NYSE open days (DatetimeIndex) = dates of the daily ^GSPC closes (gm/daily.py yahoo_daily('^GSPC')), cut at the
    seal. gspc: an optional level Series (tests)."""
    if gspc is None:
        from . import daily as DL
        gspc = DL.yahoo_daily("^GSPC")
    T = SL.resolve(seal)
    days = pd.DatetimeIndex(gspc.dropna().index).normalize().unique().sort_values()
    days = days[days.dayofweek < 5]
    if T is not None:
        days = days[days <= T]
    return days


def month_ends(days):
    """Period (month) -> last NYSE day of that month."""
    s = pd.Series(days, index=days)
    return s.groupby(days.to_period("M")).max()


def month_firsts(days):
    s = pd.Series(days, index=days)
    return s.groupby(days.to_period("M")).min()


def offset_days(days, j_days):
    """Period -> the NYSE day j_days after the month's last NYSE day (None when it lies past the last day)."""
    me = month_ends(days)
    pos = days.get_indexer(pd.DatetimeIndex(me.values)) + j_days
    vals = [days[p] if p < len(days) else pd.NaT for p in pos]
    return pd.Series(vals, index=me.index)


# --------------------------------------------------------------------------------------------------------- prices
def price_returns(D):
    """Daily price return per market from gm/daily.py build(): bonds and notes as they are (-duration x yield change),
    every other market exp(log return) - 1. Missing = no price that day."""
    out = D.copy()
    cols = [c for c in D.columns if not c.startswith(BONDLIKE)]
    out[cols] = np.expm1(D[cols])
    return out


def levels(D):
    """Price level per market on D's days, carried over days without a price ('uses its last price'); missing before
    the market's first daily price."""
    pr = price_returns(D)
    L = (1 + pr.fillna(0)).cumprod()
    return L.where(pr.notna().cummax())


def _asof(L, days):
    """Rows of L at the last row at or before each day (NaN for NaT / before the start)."""
    out = np.full((len(days), L.shape[1]), np.nan)
    d = pd.DatetimeIndex(days)
    ok = ~d.isna()
    if ok.any() and len(L):
        pos = np.searchsorted(L.index.values, d[ok].values, side="right") - 1
        good = pos >= 0
        sub = np.full((ok.sum(), L.shape[1]), np.nan)
        sub[good] = L.values[pos[good]]
        out[ok] = sub
    return out


# --------------------------------------------------------------------------------------------------------- E6 k = 1
def k1_returns(R, D, days=None, seal="design"):
    """E6 (7.3 item 2): k = 1 return for the holding that earns month t (decided at month-end t-1):
        R(t) - r(first NYSE day of t) + r(first NYSE day of t+1)
    r = the market's daily price return that day. Where the market has no price on either day the k = 0 return R(t)
    is used and the market-month is flagged. Holding cut (7.3 item 5): where the first NYSE day of t+1 lies after the
    seal or after the last NYSE day of the data, the holding ends at the close of month-end t (no plus term, not
    flagged). Returns (R1, flags) on R's index and columns; flags False where R is missing."""
    T = SL.resolve(seal)
    if T is not None:
        R, D = SL.cut_inputs(T, R, D)
    days = nyse_days(seal) if days is None else days
    if T is not None:
        days = days[days <= T]
    pr = price_returns(D).reindex(columns=R.columns)
    first = month_firsts(days)
    R1 = R.copy()
    flags = pd.DataFrame(False, index=R.index, columns=R.columns)
    fd_now = pd.DatetimeIndex([first.get(t, pd.NaT) for t in R.index])
    fd_next = pd.DatetimeIndex([first.get(t + 1, pd.NaT) for t in R.index])
    minus = pd.DataFrame(pr.reindex(fd_now).values, index=R.index, columns=R.columns)
    plus = pd.DataFrame(pr.reindex(fd_next).values, index=R.index, columns=R.columns)
    cut = pd.Series(fd_next.isna(), index=R.index)         # no first day of t+1 in the data: holding ends at month-end t
    plus = plus.where(~cut, 0.0)
    no_day = pd.Series(fd_now.isna(), index=R.index)
    bad = minus.isna() | plus.isna()
    bad = bad | pd.DataFrame(np.repeat(no_day.values[:, None], R.shape[1], 1), index=R.index, columns=R.columns)
    have = R.notna()
    flags = bad & have
    R1 = R.where(flags, R - minus + plus)
    R1 = R1.where(have)
    if T is not None:
        SL.check_output({"R1": R1, "flags": flags.where(have)}, T, "gm.execution.k1_returns")
    return R1, flags


def run_k1(R, cfg, daily, S, days=None, cost_mult=1.0, seal="design", **kw):
    """E6: a book at k = 1: gm.book.run with R_earn = the k = 1 returns (positions identical to k = 0)."""
    from . import book as B
    R1, flags = k1_returns(R, daily, days, seal)
    out = B.run(R, cost_mult=cost_mult, cfg=cfg, daily=daily, S=S, seal=seal, R_earn=R1, **kw)
    out["k1_flags"] = flags
    out["R_earn"] = R1
    out["timing"] = "k1"
    return out


def flag_share_by_year(pos, flags):
    """The k = 1 report line: by calendar year, the share of gross position (sum of |position| held into a month) in
    flagged market-months. pos: decided positions (label = decision month); flags: on the earning month."""
    held = pos.shift(1).abs()
    f = flags.reindex(index=held.index, columns=held.columns).fillna(False).astype(bool)
    tot = held.sum(axis=1)
    fl = held.where(f, 0.0).sum(axis=1)
    y = held.index.year
    return (fl.groupby(y).sum() / tot.groupby(y).sum().replace(0, np.nan))


# --------------------------------------------------------------------------------------------------------- E8 tranches
def shift_panel(R, L, days_at, first_daily, me):
    """Monthly panel sampled at a day per label instead of month-end:
        X(t) = R(t) - pr(month-end t-1 -> day(t-1)) + pr(month-end t -> day(t))
    pr(a -> b) = L(last price at or before b) / L(last price at or before a) - 1 ('uses its last price'). A market
    whose first daily price is after month-end t-1, or a label outside the calendar (before its first month), has no
    daily data for label t: X = R there, flagged. A label whose day lies past the horizon (no decision): X missing.
    Returns (X, flags)."""
    idx = R.index
    me_t = pd.DatetimeIndex([me.get(t, pd.NaT) for t in idx])
    me_p = pd.DatetimeIndex([me.get(t - 1, pd.NaT) for t in idx])
    d_t = pd.DatetimeIndex([days_at.get(t, pd.NaT) for t in idx])
    d_p = pd.DatetimeIndex([days_at.get(t - 1, pd.NaT) for t in idx])
    Lc = L.reindex(columns=R.columns)
    a1, b1 = _asof(Lc, me_p), _asof(Lc, d_p)
    a2, b2 = _asof(Lc, me_t), _asof(Lc, d_t)
    pr_prev = pd.DataFrame(b1 / a1 - 1, index=idx, columns=R.columns)
    pr_now = pd.DataFrame(b2 / a2 - 1, index=idx, columns=R.columns)
    valid = pd.Series(~(me_t.isna() | me_p.isna() | d_t.isna() | d_p.isna()), index=idx)
    mp = pd.Series(me_p, index=idx)
    has = pd.DataFrame({c: (valid & (mp >= first_daily[c])).values if pd.notna(first_daily.get(c, pd.NaT)) else
                        np.zeros(len(idx), bool) for c in R.columns}, index=idx)
    X = (R - pr_prev + pr_now).where(has, R)
    last_month = max(me.index) if len(me) else None
    beyond = pd.Series([last_month is not None and t <= last_month and pd.isna(days_at.get(t, pd.NaT)) and
                        t >= min(me.index) for t in idx], index=idx)
    X = X.where(~beyond, axis=0)
    X = X.where(R.notna())
    return X, (~has) & R.notna() & ~pd.DataFrame(np.repeat(beyond.values[:, None], R.shape[1], 1), index=idx,
                                                   columns=R.columns)


def tranche_days(days, j, horizon):
    """Decision day d_j (label -> the (5j)-th NYSE day after month-end; missing when past the horizon: the decision
    does not exist) and the holding point e_j = the next NYSE day, capped at the horizon (the holding cut)."""
    dj = offset_days(days, 5 * j)
    ej = offset_days(days, 5 * j + 1)
    dj = dj.where(dj <= horizon)
    ej = ej.where(ej <= horizon).fillna(horizon)
    return dj, ej


def tranches(R, cfg, daily, S, days=None, cost_mult=1.0, seal="design", **kw):
    """E8 (7.3 item 6): four tranches j = 0..3, each a full book run holding a quarter of the pod.
    Tranche 0 = the E6 monthly k = 1 path (run_k1, its flags included). Tranche j >= 1: decision at the close of the
    (5j)-th NYSE day after month-end t, traded at the close of the next NYSE day, held to the same point after the next
    decision day; price trend, momentum and every volatility read the shifted panel X_j and the daily EWMA at d_j(t);
    Economic trend, Carry and Value use their month-end t values. A market without daily data (first daily price after
    month-end t-1) uses R in X_j, holds tranche 0's final position and earns tranche 0's k = 1 return, flagged.
    Returns {"tranche": {j: book}, "net": quarter-sum net, "gross": quarter-sum gross, "flags": {j: frame}}."""
    from . import book as B
    T = SL.resolve(seal)
    if T is not None:
        R, daily, S = SL.cut_inputs(T, R, daily, S)
    days = nyse_days(seal) if days is None else days
    if T is not None:
        days = days[days <= T]
    horizon = days[-1]
    me = month_ends(days)
    L = levels(daily)
    first_daily = {c: L[c].first_valid_index() for c in L.columns}
    b0 = run_k1(R, cfg, daily, S, days, cost_mult, seal, **kw)
    R1, f0 = b0["R_earn"], b0["k1_flags"]
    out = {"tranche": {0: b0}, "flags": {0: f0}, "days": {}}
    for j in (1, 2, 3):
        dj, ej = tranche_days(days, j, horizon)
        X, nod_x = shift_panel(R, L, dj, first_daily, me)
        Y, nod_y = shift_panel(R, L, ej, first_daily, me)
        Y = Y.where(~nod_y, R1)                       # no daily data: tranche 0's k = 1 return
        fix = b0["pos"].where(nod_y.shift(-1).fillna(False).astype(bool))   # decision label u: no daily data at u+1
        fix = fix.where(pd.Series(dj.reindex(R.index).notna().values, index=R.index), axis=0)
        vd = pd.Series(dj.reindex(R.index).values, index=R.index)
        bj = B.run(X, cost_mult=cost_mult, cfg=cfg, daily=daily, S=S, seal=seal, R_earn=Y, vol_days=vd,
                   pos_fix=fix, **kw)
        bj["pos"] = bj["pos"].where(pd.Series(vd.notna().values, index=R.index), axis=0)   # no decision after the seal
        bj["X"], bj["R_earn"] = X, Y
        out["tranche"][j] = bj
        out["flags"][j] = nod_y.astype(bool)
        out["days"][j] = (dj, ej)
    nets = pd.concat({j: b["net"] for j, b in out["tranche"].items()}, axis=1)
    gr = pd.concat({j: b["gross"] for j, b in out["tranche"].items()}, axis=1)
    out["net"] = (nets.fillna(0).sum(axis=1) / 4).where(nets.notna().any(axis=1))
    out["gross"] = (gr.fillna(0).sum(axis=1) / 4).where(gr.notna().any(axis=1))
    if T is not None:
        SL.check_output({"net": out["net"], "gross": out["gross"],
                         "pos": {j: b["pos"] for j, b in out["tranche"].items()}}, T, "gm.execution.tranches")
    return out


# --------------------------------------------------------------------------------------------------------- E14 card 4
def spx_daily_excess(R, gspc=None, seal="design"):
    """E14 (SPEC_Card4 s3): for NYSE day d in month m, e(d) = ^GSPC price return of d + c(m) / N(m), c(m) = panel
    eq_us_spx excess return of m minus the SUM of the month's daily price returns, N(m) = ^GSPC days in m; so a rule
    held all month earns exactly the panel's monthly excess return. Days after the seal are not read."""
    if gspc is None:
        from . import daily as DL
        gspc = DL.yahoo_daily("^GSPC")
    T = SL.resolve(seal)
    lv = gspc.dropna()
    lv.index = pd.DatetimeIndex(lv.index).normalize()
    lv = lv[~lv.index.duplicated(keep="last")].sort_index()
    lv = lv[lv.index.dayofweek < 5]
    if T is not None:
        lv = lv[lv.index <= T]
        R = SL.cut_inputs(T, R)
    r = (lv / lv.shift(1) - 1).iloc[1:]
    if len(lv):
        r = r[r.index.to_period("M") > lv.index[0].to_period("M")]      # the first month lacks its first day
    m = r.index.to_period("M")
    s = r.groupby(m).sum()
    n = r.groupby(m).count()
    panel = R["eq_us_spx"].reindex(s.index)
    c = panel - s
    e = r + (c / n).reindex(m).values
    e = e.where(pd.Series(panel.reindex(m).notna().values, index=r.index))
    if T is not None:
        SL.check_output({"e": e}, T, "gm.execution.spx_daily_excess")
    return e
