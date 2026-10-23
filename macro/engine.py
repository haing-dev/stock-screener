"""Macro Compass engine: raw downloads -> monthly point-in-time indicators -> scores -> pillars -> stage ->
industry odds (6 and 12 months) -> ETF backtest and baselines -> cache/macro/out/compass.json.gz.

Point in time: every economic number enters the grid only after its release delay (registry.FRED lag), first
published values when FRED_API_KEY is set; scores are percentiles of each indicator's own past; the odds at month t
use only outcomes that had finished by t. Nothing is fitted to the full history.
"""
import csv
import gzip
import json
import math
import os
import time

import numpy as np
import pandas as pd

from . import registry as R

RAW = os.path.join("cache", "macro", "raw")
OUT = os.path.join("cache", "macro", "out")
S = R.SETTINGS


# ------------------------------------------------------------------ loading
def _csv(name):
    p = os.path.join(RAW, f"{name}.csv")
    if not os.path.exists(p):
        return None
    df = pd.read_csv(p)
    if df.empty:
        return None
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.dropna()
    return pd.Series(df["value"].values, index=df["date"])


def month_grid(end=None):
    end = end or pd.Timestamp.utcnow().tz_localize(None)
    return pd.period_range(S["start"], pd.Period(end, "M"), freq="M")


def fred_monthly(sid, grid):
    """Month-end value of a FRED series on the grid, after its release delay."""
    s = _csv(sid)
    if s is None:
        return pd.Series(np.nan, index=grid)
    spec = R.FRED[sid]
    if spec.get("q"):
        per = s.index.to_period("M") + 2          # quarter starts -> its last month
    else:
        per = s.index.to_period("M")
    m = pd.Series(s.values, index=per).groupby(level=0).last()
    m.index = m.index + spec.get("lag", 0)
    m = m.reindex(grid)
    # the last published value stays known until the next one (also bridges months never published, e.g. the
    # Oct-2025 shutdown, and the current month before its average is out)
    return m.ffill(limit=3 if spec.get("q") else 2)


def monthly_px(name, grid):
    s = _csv(name)
    if s is None:
        return pd.Series(np.nan, index=grid)
    m = pd.Series(s.values, index=s.index.to_period("M")).groupby(level=0).last()
    return m.reindex(grid)


def load_french():
    def j(tag):
        p = os.path.join(RAW, f"{tag}.json")
        return json.load(open(p)) if os.path.exists(p) else {}
    ind, ff = j("FR_IND"), j("FR_FF")
    return ind, ff


# ------------------------------------------------------------------ return panel
def build_returns(grid):
    """Monthly total returns for the 20 industries (ETF where it trades, else French proxy) and the market
    (SPY, else French market). Returns (rets DataFrame, source DataFrame 'etf'/'proxy', market Series)."""
    ind, ff = load_french()
    rets, src = {}, {}
    for it in R.INDUSTRIES:
        px = monthly_px("Y_" + it["etf"], grid)
        er = px.pct_change(fill_method=None)
        pr = pd.Series({pd.Period(k, "M"): np.mean([v[c] for c in it["proxy"] if c in v and v[c] > -0.99])
                        for k, v in ind.items() if any(c in v for c in it["proxy"])}, dtype=float).reindex(grid)
        r = er.where(er.notna(), pr)
        rets[it["etf"]] = r
        src[it["etf"]] = pd.Series(np.where(er.notna(), "etf", np.where(pr.notna(), "proxy", "")), index=grid)
    spy = monthly_px("Y_SPY", grid).pct_change(fill_method=None)
    fm = pd.Series({pd.Period(k, "M"): v.get("Mkt-RF", np.nan) + v.get("RF", 0) for k, v in ff.items()},
                   dtype=float).reindex(grid)
    mkt = spy.where(spy.notna(), fm)
    return pd.DataFrame(rets), pd.DataFrame(src), mkt


def level(r):
    return (1 + r.fillna(0)).cumprod().where(r.notna().cummax())


def cumret(r, n):
    """n-month trailing compounded return ending at t."""
    return (1 + r).rolling(n, min_periods=n).apply(np.prod, raw=True) - 1


# ------------------------------------------------------------------ indicator calculations
def calc_all(grid, rets, mkt):
    F = {sid: fred_monthly(sid, grid) for sid in R.FRED}
    cape = _csv("CAPE")
    capem = (pd.Series(cape.values, index=cape.index.to_period("M")).groupby(level=0).last().reindex(grid)
             if cape is not None else pd.Series(np.nan, index=grid))
    dxy = monthly_px("Y_DX_Y_NYB", grid)
    twex = F["TWEXMMTH"].combine_first(F["DTWEXBGS"])
    ewy, smh = monthly_px("Y_EWY", grid).pct_change(fill_method=None), monthly_px("Y_SMH", grid).pct_change(fill_method=None)
    lv = {k: level(rets[k]) for k in rets}
    vix = monthly_px("Y_VIX", grid).combine_first(F["VIXCLS"])          # Yahoo is same-day; FRED a day late
    ind_fr, _ = load_french()

    def ret_of(code):
        """Monthly returns of an industry series, or of an extra ETF spliced onto a French proxy."""
        if code in rets:
            return rets[code]
        er = monthly_px("Y_" + code, grid).pct_change(fill_method=None)
        proxy = {"XLY": ["Rtail", "Autos", "Clths", "Meals"]}.get(code, [])
        pr = pd.Series({pd.Period(k, "M"): np.mean([v[c] for c in proxy if c in v]) for k, v in ind_fr.items()
                        if proxy and any(c in v for c in proxy)}, dtype=float).reindex(grid)
        return er.where(er.notna(), pr)

    def zs(x):
        return x / x.expanding(min_periods=60).std()

    def yoy(s):
        return (s / s.shift(12) - 1) * 100

    def r6(k):
        return cumret(rets[k], 6)

    out = {}
    for ind in R.INDICATORS:
        c, a = ind["calc"][0], ind["calc"][1:]
        if c == "sahm":
            u3 = F[a[0]].rolling(3).mean()
            v = u3 - u3.shift(1).rolling(12).min()
        elif c == "yoy":
            v = yoy(F[a[0]])
        elif c == "chg6pct":
            v = (F[a[0]] / F[a[0]].shift(6) - 1) * 100
        elif c == "chg6":
            v = F[a[0]] - F[a[0]].shift(6)
        elif c == "chg12":
            v = F[a[0]] - F[a[0]].shift(12)
        elif c == "spread":
            v = F[a[0]] - F[a[1]]
        elif c == "spreadchg6":
            d = F[a[0]] - F[a[1]]
            v = d - d.shift(6)
        elif c == "gapchg12":
            d = F[a[0]] - F[a[1]]
            v = d - d.shift(12)
        elif c == "accel":
            p = F[a[0]]
            v = (((p / p.shift(3)) ** 4 - 1) - (p / p.shift(12) - 1)) * 100
        elif c == "y10ngdp":
            v = F["GS10"] - yoy(F["GDP"].ffill(limit=3))
        elif c == "dollar":
            d1 = (dxy / dxy.shift(12) - 1) * 100
            d2 = (twex / twex.shift(12) - 1) * 100
            v = d1.combine_first(d2)
        elif c == "realyield":
            v = F["GS10"] - yoy(F["CPILFESL"])
        elif c == "netliq":
            nl = F["WALCL"] / 1000 - F["WTREGEN"] / 1000 - F["RRPONTSYD"].fillna(0)   # $bn
            v = nl - nl.shift(3)
        elif c == "level":
            v = vix if a[0] == "VIXCLS" else F[a[0]]
        elif c == "ratio":
            v = F[a[0]] / F[a[1]].ffill(limit=3)
        elif c == "cape":
            v = capem
        elif c == "rally":
            v = cumret(mkt, 6) / (mkt.rolling(6).std() * math.sqrt(6))
        elif c == "cycdef":
            cyc = sum(r6(k) for k in R.CYCLICAL) / len(R.CYCLICAL)
            dfn = sum(r6(k) for k in R.DEFENSIVE) / len(R.DEFENSIVE)
            v = (cyc - dfn) * 100
        elif c == "rel6":
            v = (r6(a[0]) - cumret(mkt, 6)) * 100
        elif c == "rel12":
            v = (cumret(rets[a[0]], 12) - cumret(mkt, 12)) * 100
        elif c == "relpair6":
            v = (cumret(ret_of(a[0]), 6) - cumret(ret_of(a[1]), 6)) * 100
        elif c == "relpx3":
            pa, pb = monthly_px("Y_" + a[0], grid), monthly_px("Y_" + a[1], grid)
            v = ((pa / pa.shift(3)) - (pb / pb.shift(3))) * 100
        elif c == "trend":
            lm = level(mkt)
            v = (lm / lm.rolling(10).mean() - 1) * 100
        elif c == "breakout":
            d = dxy.combine_first(twex * (dxy / twex).dropna().median() if dxy.notna().any() else twex)
            v = (d / d.shift(1).rolling(12).max() - 1) * 100
        elif c == "dd12px":
            lsm = lv["SMH"]
            v = (lsm / lsm.rolling(12).max() - 1) * 100
        elif c == "reldd24":
            rl = lv[a[0]] / level(mkt)
            v = (rl / rl.rolling(24).max() - 1) * 100
        elif c == "stockbond":
            g10 = F["GS10"]
            bond = g10.shift(1) / 1200 - 7 * (g10 - g10.shift(1)) / 100
            v = mkt.rolling(12).corr(bond)
        elif c == "squeeze":
            d1 = (dxy / dxy.shift(12) - 1) * 100
            dol = d1.combine_first((twex / twex.shift(12) - 1) * 100)
            oil = (F["WTISPLC"] / F["WTISPLC"].shift(12) - 1) * 100
            rate = F["GS10"] - F["GS10"].shift(12)
            v = 0.5 * zs(dol) + 0.25 * zs(oil) + 0.25 * zs(rate)
        elif c == "breadth":
            above = pd.DataFrame({k: (lv[k] > lv[k].rolling(10).mean()).where(lv[k].rolling(10).mean().notna())
                                  for k in lv})
            v = above.mean(axis=1) * 100
        elif c == "breakdowns":
            dd = pd.DataFrame({k: (lv[k] / lv[k].rolling(12).max() - 1 <= -0.20).where(lv[k].rolling(12).max().notna())
                               for k in lv})
            v = dd.mean(axis=1) * 100
        elif c == "leadership":
            med = pd.DataFrame({k: cumret(rets[k], 12) for k in rets}).median(axis=1)
            v = (cumret(mkt, 12) - med) * 100
        elif c == "korea":
            v = (cumret(ewy, 6) - cumret(smh, 6)) * 100
        elif c == "cufe":
            cu, fe = F["PCOPPUSDM"], F["PIORECRUSDM"]
            v = ((cu / cu.shift(6)) - (fe / fe.shift(6))) * 100
        else:
            raise ValueError(c)
        out[ind["id"]] = v.astype(float).replace([np.inf, -np.inf], np.nan)
    return pd.DataFrame(out), F


# ------------------------------------------------------------------ scores, pillars, stage
def expanding_pct(x, min_n):
    """Percentile (0-100) of each value within its own history up to and including that month."""
    vals, out = [], []
    for v in x.values:
        if np.isnan(v):
            out.append(np.nan)
            continue
        vals.append(v)
        n = len(vals)
        if n < min_n:
            out.append(np.nan)
            continue
        a = np.asarray(vals)
        out.append(100.0 * ((a < v).sum() + 0.5 * (a == v).sum()) / n)
    return pd.Series(out, index=x.index)


def scores(ind):
    sc = {}
    for i in R.INDICATORS:
        sc[i["id"]] = expanding_pct(ind[i["id"]] * i["dir"], S["score_min_years"] * 12)
    return pd.DataFrame(sc)


def pillars(sc):
    out = {}
    for pid, _, _ in R.PILLARS:
        cols = [i["id"] for i in R.INDICATORS if i["pillar"] == pid]
        p = sc[cols]
        out[pid] = p.mean(axis=1).where(p.notna().sum(axis=1) >= 2)
    return pd.DataFrame(out)


def stages(g):
    """Stage from growth pressure g (already smoothed): level (weak from 50+hyst, solid from 50-hyst) and
    direction (change over stage_lookback months beyond +-stage_band); both hold their last reading inside the bands;
    a new stage needs stage_confirm months in a row."""
    band, hy, conf, lb = S["stage_band"], S["stage_hysteresis"], S["stage_confirm"], S["stage_lookback"]
    d = g - g.shift(lb)
    direction = high = cur = prev = None
    run, st = 0, []
    for v, dd in zip(g.values, d.values):
        if np.isnan(v) or np.isnan(dd):
            st.append(cur)
            continue
        if dd >= band:
            direction = "up"
        elif dd <= -band:
            direction = "down"
        elif direction is None:
            direction = "up" if dd > 0 else "down"
        if high is None:
            high = v >= 50
        elif v >= 50 + hy:
            high = True
        elif v <= 50 - hy:
            high = False
        r = ("contraction" if direction == "up" else "recovery") if high else ("late" if direction == "up" else "expansion")
        run = run + 1 if r == prev else 1
        prev = r
        if cur is None or (r != cur and run >= conf):
            cur = r
        st.append(cur)
    return pd.Series(st, index=g.index), d


# ------------------------------------------------------------------ state of the economy
def flag(x, on, off):
    """True from the month x reaches `on` until it falls back to `off` (hysteresis)."""
    out, cur = [], False
    for v in x.values:
        if not np.isnan(v):
            cur = v >= on if not cur else v > off
        out.append(cur if not np.isnan(v) or out else False)
    return pd.Series(out, index=x.index)


def regimes(stage, infl6, stress):
    hot = flag(infl6, *S["inflation_hot"])
    high = flag(stress, *S["stress_high"])
    reg = []
    for st, h in zip(stage.values, hot.values):
        if not isinstance(st, str):
            reg.append(None)
        elif h and st in ("expansion", "late"):
            reg.append("overheating")
        elif h and st == "contraction":
            reg.append("stagflation")
        else:
            reg.append(st)
    return pd.Series(reg, index=stage.index), hot, high


def forward_rel(rets, mkt, h):
    """Industry minus market compounded return over the next h months (from the end of month t)."""
    fwd_m = cumret(mkt, h).shift(-h)
    return pd.DataFrame({k: cumret(rets[k], h).shift(-h) - fwd_m for k in rets})


# ------------------------------------------------------------------ sector calls: investor rules + history check
def investor_tilts(reg, high):
    """+1 / -1 / 0 per industry and month from RULES[state] plus the STRESS overlay."""
    etfs = [i["etf"] for i in R.INDUSTRIES]
    t = pd.DataFrame(0, index=reg.index, columns=etfs)
    for i, (r, hs) in enumerate(zip(reg.values, high.values)):
        if not isinstance(r, str):
            continue
        for rule in [R.RULES[r]] + ([R.STRESS] if hs else []):
            for e in rule["over"]:
                t.iat[i, etfs.index(e)] += 1
            for e in rule["under"]:
                t.iat[i, etfs.index(e)] -= 1
    return np.sign(t).where(pd.Series([isinstance(r, str) for r in reg.values], index=reg.index), np.nan, axis=0)


def calls(tilt, reg, high, rel, h, band):
    """A tilt stands only if, in past months of the same situation (same state and stress; else same state) whose
    h-month outcome had finished, the industry's average return vs the market had the same sign. Returns the calls
    and, for every month, the evidence used (pooled odds of lagging / beating the market by `band`)."""
    k_shrink, mn = 20.0, S["evidence_min_months"]
    key = np.array([f"{r}|{bool(x)}" for r, x in zip(reg.values, high.values)], dtype=object)
    regv = np.array([r if isinstance(r, str) else "" for r in reg.values], dtype=object)
    T_ = len(reg)
    act = pd.DataFrame(None, index=reg.index, columns=tilt.columns, dtype=object)
    ev = {}
    for e in tilt.columns:
        r = rel[e].values
        tv = tilt[e].values
        rows = []
        for t in range(T_):
            if not regv[t] or np.isnan(tv[t]):
                rows.append(None)
                continue
            lim = t - h
            past = np.arange(0, max(0, lim + 1))
            past = past[~np.isnan(r[past])] if len(past) else past
            if len(past) < mn:
                rows.append({"pool": None})
                act.iat[t, act.columns.get_loc(e)] = "neutral"
                continue
            same = past[key[past] == key[t]]
            pool, label = (same, "state+stress") if len(same) >= mn else (past[regv[past] == regv[t]], "state")
            rp = r[past]
            br, bo = float((rp <= -band).mean()), float((rp >= band).mean())
            if len(pool) < mn:
                rows.append({"pool": None, "base_risk": br, "base_opp": bo})
                act.iat[t, act.columns.get_loc(e)] = "neutral"
                continue
            q = r[pool]
            n = len(q)
            pr = ((q <= -band).sum() + k_shrink * br) / (n + k_shrink)
            po = ((q >= band).sum() + k_shrink * bo) / (n + k_shrink)
            m = float(q.mean())
            agrees = None if tv[t] == 0 else bool(np.sign(m) == tv[t])
            a = "neutral" if tv[t] == 0 or not agrees else ("over" if tv[t] > 0 else "under")
            act.iat[t, act.columns.get_loc(e)] = a
            rows.append({"pool": label, "n": n, "mean_rel": m, "p_risk": pr, "p_opp": po, "base_risk": br,
                         "base_opp": bo, "agrees": agrees})
        ev[e] = rows
    return act, ev


# ------------------------------------------------------------------ backtest
def tilt_weights(sig, avail):
    """sig: DataFrame of 'over'/'under'/'neutral'/None; avail: bool DataFrame (return exists next month)."""
    w = pd.DataFrame(1.0, index=sig.index, columns=sig.columns)
    w[sig == "over"] = 1 + S["tilt_size"]
    w[sig == "under"] = 1 - S["tilt_size"]
    w = w.where(avail, 0.0)
    return w.div(w.sum(axis=1).replace(0, np.nan), axis=0)


def portfolio(w, rets):
    """Weights decided at the end of month t earn month t+1 returns."""
    r = (w.shift(1) * rets.fillna(0)).sum(axis=1).where(w.shift(1).sum(axis=1) > 0)
    return r


def stats(r, rf=None):
    r = r.dropna()
    if len(r) < 12:
        return None
    lv = (1 + r).cumprod()
    yrs = len(r) / 12
    return {"cagr": round((lv.iloc[-1] ** (1 / yrs) - 1) * 100, 1), "vol": round(r.std() * math.sqrt(12) * 100, 1),
            "maxdd": round(((lv / lv.cummax()) - 1).min() * 100, 1), "months": len(r),
            "from": str(r.index[0]), "to": str(r.index[-1])}


def backtest(rets, src, mkt, act, rel, h, band, start, raw=None):
    idx = rets.index[rets.index >= pd.Period(start, "M")]
    etf_ok = (src == "etf")
    avail = etf_ok.shift(-1, fill_value=False) if start == S["etf_backtest_start"] else rets.shift(-1).notna()
    R_ = rets.where(etf_ok) if start == S["etf_backtest_start"] else rets
    sig = act.reindex(idx)
    eq = tilt_weights(pd.DataFrame("neutral", index=idx, columns=rets.columns), avail.reindex(idx))
    tw = tilt_weights(sig, avail.reindex(idx))
    lvl = level(rets)
    mom = cumret(rets, 12).shift(1)                      # 12-1 month momentum
    rk = mom.reindex(idx).rank(axis=1, ascending=False)
    nav = mom.reindex(idx).notna().sum(axis=1)
    msig = pd.DataFrame("neutral", index=idx, columns=rets.columns)
    msig[rk <= 5] = "over"
    msig[rk.gt(nav - 5, axis=0)] = "under"
    trend = (lvl > lvl.rolling(10).mean()).reindex(idx)
    tsig = pd.DataFrame(np.where(trend, "over", "under"), index=idx, columns=rets.columns)
    rr = R_.reindex(idx)
    rsig = pd.DataFrame(np.where(raw.reindex(idx) > 0, "over", np.where(raw.reindex(idx) < 0, "under", "neutral")),
                        index=idx, columns=rets.columns) if raw is not None else sig
    curves = {"compass": portfolio(tw, rr), "investor": portfolio(tilt_weights(rsig, avail.reindex(idx)), rr),
              "equal": portfolio(eq, rr), "momentum": portfolio(tilt_weights(msig, avail.reindex(idx)), rr),
              "trend": portfolio(tilt_weights(tsig, avail.reindex(idx)), rr), "market": mkt.reindex(idx).shift(0)}
    curves["market"] = curves["market"].where(curves["equal"].notna())
    # call accuracy: share of calls followed by the event, vs all months
    relx = rel.reindex(idx)
    okm = avail.reindex(idx) & relx.notna()
    hit = {}
    for tag, sg in (("", sig), ("investor_", rsig)):
        for a, ev in (("under", relx <= -band), ("over", relx >= band)):
            m = (sg == a) & okm
            nm = int(m.values.sum())
            hit[tag + a] = {"calls": nm, "hit": round(100.0 * (ev & m).values.sum() / nm, 1) if nm else None,
                            "base": round(100.0 * (ev & okm).values.sum() / max(1, okm.values.sum()), 1)}
    return curves, hit


# ------------------------------------------------------------------ report card for single indicators
def report_card(sc, mkt, rec):
    fwd = cumret(mkt, 12).shift(-12)
    out = {}
    for i in R.INDICATORS:
        s = sc[i["id"]]
        ok = s.notna() & fwd.notna()
        if ok.sum() < 120:
            out[i["id"]] = None
            continue
        worst = ok & (s >= 80)
        lead = None
        starts = rec[(rec == 1) & (rec.shift(1) == 0)].index
        pre = [s.get(p - 6) for p in starts if (p - 6) in s.index and not np.isnan(s.get(p - 6, np.nan))]
        if pre:
            lead = round(float(np.mean(pre)), 0)
        out[i["id"]] = {"worst_fifth_fwd": round(float(fwd[worst].mean()) * 100, 1) if worst.sum() >= 12 else None,
                        "normal_fwd": round(float(fwd[ok].mean()) * 100, 1), "months": int(ok.sum()),
                        "pre_recession": lead, "recessions": len(pre)}
    return out


# ------------------------------------------------------------------ live record
def live_scores(rets, mkt, grid):
    """Score the calls in the append-only ledger whose horizon has ended."""
    from .record import read
    rows = read()
    if not rows:
        return {"rows": 0, "first": None, "scored": {}}
    last_done = grid[-2] if len(grid) > 1 else grid[-1]          # the current month is still under way
    out = {"rows": len(rows), "first": min(r["month"] for r in rows), "scored": {}}
    for h in map(str, S["horizons"]):
        band = S["outcome_band"][int(h)]
        agg = {a: {"calls": 0, "hit": 0, "rel_sum": 0.0} for a in ("over", "under", "neutral")}
        pending = 0
        for r in rows:
            if r["horizon"] != h or r["action"] not in agg:
                continue
            t0 = pd.Period(r["month"], "M")
            t1 = t0 + int(h)
            if t1 > last_done:
                pending += 1
                continue
            win = (grid > t0) & (grid <= t1)
            rel = float((1 + rets[r["etf"]][win]).prod() - (1 + mkt[win]).prod())
            g = agg[r["action"]]
            g["calls"] += 1
            g["rel_sum"] += rel
            g["hit"] += int(rel <= -band if r["action"] == "under" else rel >= band if r["action"] == "over" else 0)
        out["scored"][h] = {"pending": pending, **{a: {"calls": g["calls"], "hit": round(100 * g["hit"] / g["calls"], 1)
                                                      if g["calls"] else None,
                                                      "avg_rel": round(100 * g["rel_sum"] / g["calls"], 1) if g["calls"] else None}
                                                  for a, g in agg.items()}}
    return out


# ------------------------------------------------------------------ run
def _ser(s, nd=1):
    return [None if (v is None or (isinstance(v, float) and np.isnan(v))) else (round(float(v), nd) if isinstance(v, (float, np.floating)) else v)
            for v in s.values]


def _r(v, nd=1, mul=1):
    return None if v is None else round(float(v) * mul, nd)


def run(log=print):
    t0 = time.time()
    man = json.load(open(os.path.join(RAW, "manifest.json"))) if os.path.exists(os.path.join(RAW, "manifest.json")) else {}
    grid = month_grid()
    rets, src, mkt = build_returns(grid)
    # the grid ends at the last month with a market return (the current month while it is under way)
    last = mkt.last_valid_index()
    grid = grid[grid <= last]
    rets, src, mkt = rets.reindex(grid), src.reindex(grid), mkt.reindex(grid)
    ind, F = calc_all(grid, rets, mkt)
    sc = scores(ind)
    pl = pillars(sc)
    econ = pl[["growth", "internals"]].mean(axis=1, skipna=True)             # economy data + the inside of the market
    g6 = econ.rolling(S["stage_smooth"], min_periods=3).mean()               # one noisy month can't swing the stage
    stage, d12 = stages(g6)
    infl6 = pl["inflation"].rolling(S["stage_smooth"], min_periods=3).mean()
    reg, hot, high = regimes(stage, infl6, pl["stress"])
    tilt = investor_tilts(reg, high)
    rec = F["USREC"].reindex(grid)
    out = {"version": R.VERSION, "updated": time.strftime("%Y-%m-%d", time.gmtime()), "asof": str(grid[-1]),
           "fred_key": man.get("fred_key"), "months": [str(p) for p in grid], "settings": S,
           "stage": [s_ if isinstance(s_, str) else None for s_ in stage],
           "regime": [s_ if isinstance(s_, str) else None for s_ in reg], "hot": [bool(x) for x in hot],
           "stress_high": [bool(x) for x in high], "econ6": _ser(g6), "econ_d12": _ser(d12), "infl6": _ser(infl6),
           "recession": _ser(rec, 0), "pillars": {k: _ser(pl[k]) for k in pl}, "scores": {k: _ser(sc[k], 0) for k in sc},
           "values": {k: _ser(ind[k], 2) for k in ind}, "horizons": {}, "industries": [], "market": _ser(level(mkt), 4)}
    for it in R.INDUSTRIES:
        e = it["etf"]
        first_etf = src[e][src[e] == "etf"].index.min()
        out["industries"].append({"etf": e, "name": it["name"], "etf_from": str(first_etf) if pd.notna(first_etf) else None,
                                  "tilt": _ser(tilt[e], 0), "rel_level": _ser(level(rets[e]) / level(mkt), 4)})
    for h in S["horizons"]:
        band = S["outcome_band"][h]
        rel = forward_rel(rets, mkt, h)
        act, ev = calls(tilt, reg, high, rel, h, band)
        hz = {"band": band, "now": {}, "actions": {e: [a if isinstance(a, str) else None for a in act[e]] for e in act},
              "backtest": {}, "recent": {}}
        for i in range(max(0, len(grid) - 3), len(grid)):
            hz["recent"][str(grid[i])] = {e: [_r((ev[e][i] or {}).get(k), 1, 100) for k in ("p_risk", "p_opp", "base_risk", "base_opp")]
                                          for e in act}
        for e in act:
            x = ev[e][-1] or {}
            hz["now"][e] = {"action": act[e].iloc[-1], "tilt": _r(tilt[e].iloc[-1], 0), "pool": x.get("pool"),
                            "n": x.get("n"), "mean_rel": _r(x.get("mean_rel"), 1, 100), "agrees": x.get("agrees"),
                            "p_risk": _r(x.get("p_risk"), 1, 100), "p_opp": _r(x.get("p_opp"), 1, 100),
                            "base_risk": _r(x.get("base_risk"), 1, 100), "base_opp": _r(x.get("base_opp"), 1, 100)}
        have = act.notna().sum(axis=1)
        long_start = str(have[have >= len(act.columns) / 2].index.min())
        for name, start in (("etf", S["etf_backtest_start"]), ("long", long_start)):
            curves, hit = backtest(rets, src, mkt, act, rel, h, band, start, raw=tilt)
            hz["backtest"][name] = {"stats": {k: stats(v) for k, v in curves.items()}, "hit": hit,
                                    "curves": {k: _ser(level(v.dropna()).reindex(grid), 4) for k, v in curves.items()},
                                    "start": start}
        out["horizons"][str(h)] = hz
    out["report"] = report_card(sc, mkt, rec)
    out["live"] = live_scores(rets, mkt, grid)
    out["meta"] = {"pillars": R.PILLARS, "stages": R.STAGES, "rules": R.RULES, "stress_rule": R.STRESS,
                   "indicators": [{k: i[k] for k in ("id", "pillar", "name", "plain", "who", "dir")} for i in R.INDICATORS]}
    os.makedirs(OUT, exist_ok=True)
    with gzip.open(os.path.join(OUT, "compass.json.gz"), "wt") as f:
        json.dump(out, f, separators=(",", ":"))
    now = out["horizons"]["12"]["now"]
    log(f"build: {len(grid)} months to {grid[-1]}; state {reg.iloc[-1]} (stage {stage.iloc[-1]}, inflation hot "
        f"{bool(hot.iloc[-1])}, stress high {bool(high.iloc[-1])}); stress {pl['stress'].iloc[-1]:.0f}; "
        f"12m calls {sum(1 for v in now.values() if v['action']=='over')} over / "
        f"{sum(1 for v in now.values() if v['action']=='under')} under; {time.time()-t0:.0f}s")
    for h in ("6", "12"):
        b = out["horizons"][h]["backtest"]["etf"]["stats"]
        log(f"  {h}m ETF backtest: " + "; ".join(f"{k} {v['cagr']}%/yr dd {v['maxdd']}%" for k, v in b.items() if v))
    return out
