"""Research (not used by the page): can the de-risking rule warn earlier and more precisely?

Ideas tested against the live rule (3.1.0: >= 1/3 of the 28 core indicators in their worst fifth -> 50% stocks):
  1. weight each indicator by its own track record, walk-forward (only outcomes finished by then):
     'lift' = how much more often than normal a 15%+ fall (or 10%+ in 6 months) followed its worst-fifth readings,
     shrunk toward 1 with 24 pseudo-months; 'edge' = only the part above normal (useless indicators get 0);
  2. two steps: slow early warnings (economy, inflation, credit spreads) cut to 80%, fast confirmation (market
     prices) cuts a further 30 points to 50%; or a graded cut that grows with the share of warnings;
  3. faster way back in: after the market itself broke (S&P below its 10-month average or VIX / junk bonds in their
     worst fifth), go back to 100% once it heals, for up to 12 months even if slow signals are still bad;
  4. checking weekly instead of monthly (needs weekly data: run in GitHub Actions, see weekly()).
Monthly part runs on the built data (python -m macro.research_derisk). Results: cache/macro/out/derisk_research.*"""
import gzip
import itertools
import json
import math
import os
import time

import numpy as np
import pandas as pd

from . import registry as R

OUT = os.path.join("cache", "macro", "out")
RAW = os.path.join("cache", "macro", "raw")
SPLITS = {"1975-2000": ("1975-02", "2000-12"), "2001-2026": ("2001-01", None), "1975-2026": ("1975-02", None)}
CREDIT = ["baa", "baa_chg"]


# ------------------------------------------------------------------ data
def load():
    d = json.load(gzip.open(os.path.join(OUT, "compass.json.gz"), "rt"))
    grid = pd.PeriodIndex(d["months"], freq="M")
    sc = pd.DataFrame({k: pd.Series(v, index=grid, dtype=float) for k, v in d["scores"].items()})
    val = pd.DataFrame({k: pd.Series(v, index=grid, dtype=float) for k, v in d["values"].items()})
    lvl = pd.Series(d["market"], index=grid, dtype=float)
    ff = json.load(open(os.path.join(RAW, "FR_FF.json")))
    rf = pd.Series({pd.Period(k, "M"): v.get("RF", np.nan) for k, v in ff.items()}, dtype=float).reindex(grid).ffill()
    return d, grid, sc, val, lvl, rf


def groups(universe):
    pil = {i["id"]: i["pillar"] for i in R.INDICATORS}
    core = [k for k, p in pil.items() if p in ("growth", "internals", "inflation", "stress")]
    ids = core if universe == "core28" else list(pil)
    early = [k for k in ids if pil[k] in ("growth", "inflation", "liquidity", "froth") or k in CREDIT]
    confirm = [k for k in ids if k not in early]
    return ids, early, confirm


def event(lvl, fall, months):
    """1 if the S&P 500 falls `fall` or more below month t's level within the next `months` months."""
    fut = pd.concat([lvl.shift(-k) for k in range(1, months + 1)], axis=1).min(axis=1, skipna=False)
    ev = (fut / lvl - 1 <= -fall).astype(float)
    ev[fut.isna() | lvl.isna()] = np.nan
    return ev


def weights(sc, ids, ev, horizon, kind, k=24.0):
    """Walk-forward weight of each indicator at each month t, from outcomes finished by t (s <= t - horizon)."""
    if kind == "equal":
        return pd.DataFrame(1.0, index=sc.index, columns=ids)
    bad = (sc[ids] >= 80).astype(float).where(sc[ids].notna())
    okm = ev.notna()
    okf = okm.astype(float)
    hits = bad.fillna(0).mul(ev.fillna(0), axis=0).mul(okf, axis=0).cumsum().shift(horizon)
    n = bad.fillna(0).mul(okf, axis=0).cumsum().shift(horizon)
    base = (ev.fillna(0).cumsum() / okm.cumsum().replace(0, np.nan)).shift(horizon)
    lift = ((hits + k * base.values[:, None]) / (n + k)).div(base, axis=0)
    lift = lift.fillna(1.0)
    return (lift if kind == "lift" else (lift - 1).clip(lower=0)).clip(upper=5)


def share(sc, w, ids):
    bad = (sc[ids] >= 80).astype(float)
    avail = sc[ids].notna().astype(float)
    num = (w[ids] * bad).sum(axis=1)
    den = (w[ids] * avail).sum(axis=1)
    s = (num / den.replace(0, np.nan)).fillna(0.0)
    return s.where(avail.sum(axis=1) >= 10, 0.0)


def fast_ok(sc, val):
    """The market itself looks healed: S&P above its 10-month average, VIX and junk bonds out of their worst fifth."""
    trend = val["spx_trend"] > 0
    vix = sc["vix"].isna() | (sc["vix"] < 80)
    junk = sc["junk"].isna() | (sc["junk"] < 80)
    return (trend & vix & junk).fillna(False)


# ------------------------------------------------------------------ rules
def exposure(shares, spec, ok):
    kind = spec["structure"]
    a, e_, c = shares["all"], shares["early"], shares["confirm"]
    if kind == "one":
        eb = np.where(a >= spec["t"] - 1e-9, 0.5, 1.0)
        deep_lvl = 0.5
    elif kind == "two":
        eb = 1.0 - 0.2 * (e_ >= spec["te"] - 1e-9) - 0.3 * (c >= spec["tc"] - 1e-9)
        deep_lvl = 0.7 if spec.get("deep") == "any" else 0.5
    elif kind == "graded":
        lo, hi = spec["band"]
        eb = 1.0 - 0.5 * np.clip((a - lo) / (hi - lo), 0, 1)
        deep_lvl = 0.75
    elif kind == "and_trend":                   # indicators warn AND the market confirms (S&P below 10-month avg)
        eb = np.where((a >= spec["t"] - 1e-9) & ~shares["trend_up"], 0.5, 1.0)
        deep_lvl = 0.5
    elif kind == "or_trend":                    # indicators warn OR the market breaks
        eb = np.where((a >= spec["t"] - 1e-9) | ~shares["trend_up"], 0.5, 1.0)
        deep_lvl = 0.5
    elif kind == "two_trend":                   # indicators warn -> 80%; market breaks as well -> 50%
        eb = 1.0 - 0.2 * (a >= spec["t"] - 1e-9) - 0.3 * ((a >= spec["t"] - 1e-9) & ~shares["trend_up"])
        deep_lvl = 0.5
    elif kind == "trend":                       # baseline: S&P below its 10-month average -> 50%
        eb = np.where(~shares["trend_up"], 0.5, 1.0)
        deep_lvl = 0.5
    else:
        raise ValueError(kind)
    eb = np.asarray(eb, dtype=float)
    if spec.get("reentry") != "fast":
        return eb
    e = eb.copy()
    okv = np.asarray(ok, dtype=bool)
    in_ep, mute_until, mute = False, -1, spec.get("mute", 12)
    for t in range(len(eb)):
        if t <= mute_until:
            if okv[t]:
                e[t] = 1.0
                continue
            mute_until = -1                       # the market broke again: follow the rule
        if in_ep and okv[t]:
            in_ep, mute_until, e[t] = False, t + mute, 1.0
            continue
        if eb[t] <= deep_lvl + 1e-9 and not okv[t]:
            in_ep = True
        e[t] = eb[t]
    return e


# ------------------------------------------------------------------ scoring
def falls(lvl, start="1975-01", depth=0.15):
    """Peak-to-trough falls of `depth` or more (month-end total-return levels)."""
    x = lvl[lvl.index >= pd.Period(start, "M")].dropna()
    out, peak_i, i = [], 0, 0
    v = x.values
    while i < len(v):
        if v[i] >= v[peak_i]:
            peak_i = i
        elif v[i] / v[peak_i] - 1 <= -depth:
            j = i
            trough_i = i
            while j < len(v) and v[j] < v[peak_i]:
                if v[j] < v[trough_i]:
                    trough_i = j
                j += 1
            k10 = next(q for q in range(peak_i, trough_i + 1) if v[q] / v[peak_i] - 1 <= -0.10)
            out.append({"peak": x.index[peak_i], "trough": x.index[trough_i], "depth": v[trough_i] / v[peak_i] - 1,
                        "down10": x.index[k10], "recovered": j < len(v)})
            peak_i = j if j < len(v) else len(v) - 1
            i = j
            continue
        i += 1
    return out


def metrics(e, mret, rf, ev15, lvl, window, fall_list):
    e = pd.Series(e, index=mret.index)
    r = (e.shift(1) * mret + (1 - e.shift(1)) * rf)
    a, b = window
    sel = (r.index >= pd.Period(a, "M")) & (r.index <= (pd.Period(b, "M") if b else r.index[-1]))
    rr, mm, ff = r[sel].dropna(), mret[sel].dropna(), rf[sel]
    def st(x):
        lv = (1 + x).cumprod()
        yrs = len(x) / 12
        return {"cagr": (lv.iloc[-1] ** (1 / yrs) - 1) * 100, "maxdd": ((lv / lv.cummax()) - 1).min() * 100,
                "vol": x.std() * math.sqrt(12) * 100,
                "sharpe": (x - ff.reindex(x.index)).mean() / x.std() * math.sqrt(12)}
    s, m = st(rr), st(mm)
    dec = e.shift(1)[sel].dropna()                         # exposure held in each month of the window
    avg = dec.mean()
    static = avg * mm + (1 - avg) * ff.reindex(mm.index)
    sst = st(static)
    cut_dec = e[(e.index >= pd.Period(a, "M") - 1) & (e.index < (pd.Period(b, "M") if b else e.index[-1]))]
    cut = cut_dec < 1 - 1e-9
    prec = float(ev15[cut[cut].index].mean()) if cut.any() else float("nan")
    runs = int(((cut.astype(int).diff() == 1).sum()) + (1 if len(cut) and cut.iloc[0] else 0))
    leads, saved, caught = [], [], 0
    nfalls = 0
    starts = list(cut[(cut.astype(int).diff() == 1) | ((cut.index == cut.index[0]) & cut)].index) if len(cut) else []
    true_starts = set()
    for f in fall_list:
        if not (f["peak"] >= pd.Period(a, "M") - 1 and (b is None or f["trough"] <= pd.Period(b, "M"))):
            continue
        nfalls += 1
        win = e[(e.index >= f["peak"] - 6) & (e.index <= f["trough"])]
        first = win[win < 1 - 1e-9]
        ld = (first.index[0] - f["peak"]).n if len(first) else None
        leads.append(ld)
        if len(first) and first.index[0] < f["down10"]:      # cut decided before the month the S&P was 10% down
            caught += 1
        true_starts |= {s_ for s_ in starts if f["peak"] - 6 <= s_ <= f["trough"]}
        seg = r[(r.index > f["peak"]) & (r.index <= f["trough"])].dropna()
        sl = (1 + seg).cumprod()
        saved.append((min(0.0, (sl / sl.cummax().clip(lower=1)).min() - 1) * 100, f["depth"] * 100))
    false_alarms = len([s_ for s_ in starts if s_ not in true_starts])
    return {"cagr": s["cagr"], "maxdd": s["maxdd"], "vol": s["vol"], "sharpe": s["sharpe"],
            "sp_cagr": m["cagr"], "sp_maxdd": m["maxdd"], "sp_sharpe": m["sharpe"],
            "static_cagr": sst["cagr"], "static_maxdd": sst["maxdd"], "avg_exposure": avg * 100,
            "months_cut": float(cut.mean() * 100), "alarms": runs, "precision": prec * 100,
            "leads": leads, "falls": saved, "caught": caught, "nfalls": nfalls, "false_alarms": false_alarms}


# ------------------------------------------------------------------ grid
def specs():
    out = []
    W = [("equal", None), ("lift", "15/12"), ("edge", "15/12"), ("lift", "10/6"), ("edge", "10/6")]
    S = ([{"structure": "one", "t": t} for t in (0.2, 0.25, 0.3, 1 / 3, 0.4)]
         + [{"structure": "two", "te": te, "tc": tc} for te in (0.25, 1 / 3, 0.4) for tc in (0.25, 1 / 3, 0.4)]
         + [{"structure": "graded", "band": bd} for bd in ((0.1, 0.4), (0.15, 0.35), (0.2, 0.5))]
         + [{"structure": k, "t": t} for k in ("and_trend", "or_trend", "two_trend") for t in (0.2, 0.25, 1 / 3)])
    for (w, evd), u, s, re in itertools.product(W, ("core28", "all43"), S, ("none", "fast")):
        out.append(dict(s, weights=w, event=evd, universe=u, reentry=re))
    return out


def label(sp):
    s = sp["structure"]
    st = (f"one switch at {sp['t']:.2f}" if s == "one" else f"two steps (early {sp['te']:.2f}, confirm {sp['tc']:.2f})"
          if s == "two" else f"graded {sp['band'][0]:.2f}-{sp['band'][1]:.2f}" if s == "graded"
          else f"indicators {sp['t']:.2f} AND S&P below trend" if s == "and_trend"
          else f"indicators {sp['t']:.2f} OR S&P below trend" if s == "or_trend"
          else f"indicators {sp['t']:.2f} -> 80%, + S&P below trend -> 50%" if s == "two_trend" else "trend only")
    w = "equal votes" if sp.get("weights") in (None, "equal") else f"{sp['weights']} weights ({sp['event']})"
    return f"{st} | {w} | {sp.get('universe', '')} | re-entry {sp.get('reentry', 'none')}"


def run(log=print):
    t0 = time.time()
    d, grid, sc, val, lvl, rf = load()
    mret = lvl.pct_change(fill_method=None)
    ev = {"15/12": event(lvl, 0.15, 12), "10/6": event(lvl, 0.10, 6)}
    hz = {"15/12": 12, "10/6": 6}
    fl = falls(lvl)
    ok = fast_ok(sc, val)
    trend_up = (val["spx_trend"] > 0).fillna(True)
    cache = {}

    def shares_for(wkind, evd, universe):
        key = (wkind, evd, universe)
        if key not in cache:
            ids, early, confirm = groups(universe)
            w = weights(sc, ids, ev[evd or "15/12"], hz[evd or "15/12"], wkind)
            cache[key] = {"all": share(sc, w, ids).values, "early": share(sc, w, early).values,
                          "confirm": share(sc, w, confirm).values, "trend_up": trend_up.values}
        return cache[key]

    res = []
    base_specs = [{"structure": "one", "t": 1 / 3, "weights": "equal", "event": None, "universe": "core28",
                   "reentry": "none", "name": "LIVE RULE"},
                  {"structure": "trend", "weights": "equal", "event": None, "universe": "core28", "reentry": "none",
                   "name": "TREND ONLY (S&P below 10-month average)"},
                  {"structure": "trend", "weights": "equal", "event": None, "universe": "core28", "reentry": "fast",
                   "name": "TREND ONLY + re-entry"}]
    for sp in base_specs + specs():
        sh = shares_for(sp["weights"], sp["event"], sp["universe"])
        e = exposure(sh, sp, ok.values)
        row = {"spec": sp, "label": sp.get("name") or label(sp)}
        for nm, win in SPLITS.items():
            row[nm] = metrics(e, mret, rf, ev["15/12"], lvl, win, fl)
        row["exposure"] = e
        res.append(row)
    live = res[0]
    log(f"research: {len(res)} rules simulated in {time.time() - t0:.0f}s; falls of 15%+ since 1975: "
        + ", ".join(f"{f['peak']}->{f['trough']} {f['depth'] * 100:.0f}%" for f in fl))
    return res, live, fl, grid


def summarise(res, live, fl, log=print):
    H1, H2, F = "1975-2000", "2001-2026", "1975-2026"
    def fmt(m):
        return (f"{m['cagr']:5.1f}%/yr  worst {m['maxdd']:6.1f}%  Sharpe {m['sharpe']:.2f}  avg stocks {m['avg_exposure']:3.0f}%"
                f"  (same-cash fixed mix: {m['static_cagr']:4.1f}%/yr worst {m['static_maxdd']:6.1f}%)  alarms {m['alarms']:2d}"
                f"  precision {m['precision']:3.0f}%  caught {m['caught']}/{m['nfalls']} falls in time, {m['false_alarms']} false alarms")
    lines = []
    sp = live[F]
    lines.append(f"S&P 500 always invested: 1975-2000 {live[H1]['sp_cagr']:.1f}%/yr worst {live[H1]['sp_maxdd']:.0f}% Sharpe {live[H1]['sp_sharpe']:.2f};"
                 f" 2001-2026 {live[H2]['sp_cagr']:.1f}%/yr worst {live[H2]['sp_maxdd']:.0f}% Sharpe {live[H2]['sp_sharpe']:.2f};"
                 f" all {sp['sp_cagr']:.1f}%/yr worst {sp['sp_maxdd']:.0f}% Sharpe {sp['sp_sharpe']:.2f}")
    for r in res[:3]:
        lines.append(f"{r['label']}")
        for nm in (H1, H2, F):
            lines.append(f"   {nm}: {fmt(r[nm])}")
    grid = res[3:]

    def better(a, b, nm):
        return (a[nm]["sharpe"] > b[nm]["sharpe"] + 0.005, a[nm]["maxdd"] > b[nm]["maxdd"] + 0.5)

    def tally(pairs, title):
        n = len(pairs)
        if not n:
            return
        out = [title + f" ({n} like-for-like pairs)"]
        for nm in (H1, H2):
            s_ = sum(better(a, b, nm)[0] for a, b in pairs)
            d_ = sum(better(a, b, nm)[1] for a, b in pairs)
            both = sum(all(better(a, b, nm)) for a, b in pairs)
            ds = np.median([a[nm]["sharpe"] - b[nm]["sharpe"] for a, b in pairs])
            dd = np.median([a[nm]["maxdd"] - b[nm]["maxdd"] for a, b in pairs])
            dc = np.median([a[nm]["cagr"] - b[nm]["cagr"] for a, b in pairs])
            out.append(f"   {nm}: better Sharpe {s_}/{n}, smaller worst fall {d_}/{n}, both {both}/{n};"
                       f" median change: return {dc:+.2f}%/yr, worst fall {dd:+.1f} pts, Sharpe {ds:+.3f}")
        lines.extend(out)

    key = lambda r, drop: tuple(sorted((k, str(v)) for k, v in r["spec"].items() if k not in drop))
    # idea 1: track-record weights vs equal votes (same structure, universe, re-entry)
    eq = {key(r, ("weights", "event")): r for r in grid if r["spec"]["weights"] == "equal"}
    for wk in ("lift", "edge"):
        for evd in ("15/12", "10/6"):
            pairs = [(r, eq[key(r, ("weights", "event"))]) for r in grid
                     if r["spec"]["weights"] == wk and r["spec"]["event"] == evd]
            tally(pairs, f"IDEA 1 weights '{wk}' ({evd}) vs equal votes")
    # idea 2: two steps vs one switch at the same confirm threshold; graded vs one switch at 1/3
    one = {(r["spec"]["weights"], r["spec"]["event"], r["spec"]["universe"], r["spec"]["reentry"], round(r["spec"]["t"], 3)): r
           for r in grid if r["spec"]["structure"] == "one"}
    pairs = [(r, one[(r["spec"]["weights"], r["spec"]["event"], r["spec"]["universe"], r["spec"]["reentry"], round(r["spec"]["tc"], 3))])
             for r in grid if r["spec"]["structure"] == "two"]
    tally(pairs, "IDEA 2 two steps vs one switch (confirm threshold = switch threshold)")
    pairs = [(r, one[(r["spec"]["weights"], r["spec"]["event"], r["spec"]["universe"], r["spec"]["reentry"], 0.333)])
             for r in grid if r["spec"]["structure"] == "graded"]
    tally(pairs, "IDEA 2b graded cut vs one switch at 1/3")
    for k_, ttl in (("and_trend", "IDEA 2c indicators AND market confirmation vs indicators alone"),
                    ("two_trend", "IDEA 2d indicators -> 80%, + market confirmation -> 50% vs indicators alone"),
                    ("or_trend", "IDEA 2e indicators OR market break vs indicators alone")):
        pairs = [(r, one[(r["spec"]["weights"], r["spec"]["event"], r["spec"]["universe"], r["spec"]["reentry"], round(r["spec"]["t"], 3))])
                 for r in grid if r["spec"]["structure"] == k_]
        tally(pairs, ttl)
    tr = res[1]
    for k_ in ("and_trend", "or_trend", "two_trend", "one"):
        g_ = [r for r in grid if r["spec"]["structure"] == k_]
        for nm in (H1, H2):
            lines.append(f"   {k_} vs TREND ONLY {nm}: better Sharpe {sum(r[nm]['sharpe'] > tr[nm]['sharpe'] + 0.005 for r in g_)}/{len(g_)},"
                         f" smaller worst fall {sum(r[nm]['maxdd'] > tr[nm]['maxdd'] + 0.5 for r in g_)}/{len(g_)}")
    # idea 3: fast re-entry vs none
    nore = {key(r, ("reentry",)): r for r in grid if r["spec"]["reentry"] == "none"}
    pairs = [(r, nore[key(r, ("reentry",))]) for r in grid if r["spec"]["reentry"] == "fast"]
    tally(pairs, "IDEA 3 fast re-entry vs none")
    # universe: all 43 vs core 28
    core = {key(r, ("universe",)): r for r in grid if r["spec"]["universe"] == "core28"}
    pairs = [(r, core[key(r, ("universe",))]) for r in grid if r["spec"]["universe"] == "all43"]
    tally(pairs, "EXTRA all 43 indicators vs the 28 core")
    # vs the live rule
    for nm in (H1, H2):
        s_ = sum(r[nm]["sharpe"] > live[nm]["sharpe"] + 0.005 for r in grid)
        d_ = sum(r[nm]["maxdd"] > live[nm]["maxdd"] + 0.5 for r in grid)
        both = sum(r[nm]["sharpe"] > live[nm]["sharpe"] + 0.005 and r[nm]["maxdd"] > live[nm]["maxdd"] + 0.5 for r in grid)
        lines.append(f"vs LIVE RULE {nm}: {s_}/{len(grid)} rules have a better Sharpe, {d_} a smaller worst fall, {both} both")
    both_halves = [r for r in grid if all(r[nm]["sharpe"] > live[nm]["sharpe"] + 0.005 and r[nm]["maxdd"] >= live[nm]["maxdd"] - 0.5
                                          for nm in (H1, H2))]
    lines.append(f"rules better than the live rule in BOTH halves (higher Sharpe, worst fall no worse): {len(both_halves)}/{len(grid)}")
    from collections import Counter
    for fld in ("structure", "weights", "universe", "reentry"):
        lines.append(f"   ... by {fld}: {dict(Counter(str(r['spec'][fld]) for r in both_halves))}")
    tr_both = [r for r in grid if all(r[nm]["sharpe"] > res[1][nm]["sharpe"] + 0.005 and r[nm]["maxdd"] >= res[1][nm]["maxdd"] - 0.5 for nm in (H1, H2))]
    lines.append(f"rules better than TREND ONLY in BOTH halves: {len(tr_both)}/{len(grid)}")
    for r in sorted(tr_both, key=lambda r: -(r[H1]['sharpe'] + r[H2]['sharpe']))[:6]:
        lines.append(f"   {r['label']}: 1975-2000 Sharpe {r[H1]['sharpe']:.2f} worst {r[H1]['maxdd']:.0f}%; 2001-2026 Sharpe {r[H2]['sharpe']:.2f} worst {r[H2]['maxdd']:.0f}%")
    # honest selection: choose on 1975-2000 only, judge on 2001-2026
    cand = [r for r in grid if r[H1]["maxdd"] >= live[H1]["maxdd"] - 0.5]
    top = sorted(cand, key=lambda r: -r[H1]["sharpe"])[:8]
    lines.append("TOP 8 chosen on 1975-2000 only (Sharpe, worst fall no worse than the live rule) -> how they did 2001-2026:")
    for r in top:
        lines.append(f"   {r['label']}")
        lines.append(f"      1975-2000: {fmt(r[H1])}")
        lines.append(f"      2001-2026: {fmt(r[H2])}")
    lines.append(f"   live rule 2001-2026: {fmt(live[H2])}")
    # hindsight view (full period best) for reference
    hind = sorted(grid, key=lambda r: -r[F]["sharpe"])[:5]
    lines.append("HINDSIGHT best 5 on 1975-2026 (for reference only, chosen with the answers known):")
    for r in hind:
        lines.append(f"   {r['label']}: {fmt(r[F])}")
    # per-fall detail for live, trend and the H1 winner
    sel = [("live rule", live), ("trend only", res[1]), ("1975-2000 winner", top[0] if top else None)]
    lines.append("Falls of 15%+ (S&P peak -> trough): months from the peak to the first cut (window from 6 months before the peak; negative = before the peak); worst fall with the rule vs S&P")
    for f_i, f in enumerate(fl):
        cells = []
        for nm, r in sel:
            if r is None:
                continue
            m = r[F]
            ld = m["leads"][f_i] if f_i < len(m["leads"]) else None
            sv = m["falls"][f_i] if f_i < len(m["falls"]) else None
            cells.append(f"{nm}: {'no cut' if ld is None else f'{ld:+d} mo'} / {sv[0]:.0f}%" if sv else f"{nm}: -")
        lines.append(f"   {f['peak']} -> {f['trough']} S&P {f['depth'] * 100:.0f}%: " + "; ".join(cells))
    for ln in lines:
        log(ln)
    return top, both_halves


def main():
    res, live, fl, grid = run()
    top, both = summarise(res, live, fl)
    os.makedirs(OUT, exist_ok=True)
    rows = []
    for r in res:
        row = {"label": r["label"], **{f"{nm}_{k}": v for nm in SPLITS for k, v in r[nm].items() if not isinstance(v, list)}}
        rows.append(row)
    pd.DataFrame(rows).to_csv(os.path.join(OUT, "derisk_research.csv"), index=False)
    return res, live, fl, top


# ------------------------------------------------------------------ idea 4: check weekly (needs network: Actions)
FAST = ["vix", "spx_trend", "junk", "banks", "dollar_break", "chips_break", "breadth", "breakdowns", "transports",
        "homebuilders", "cyc_def", "staples_disc"]
DDIR = os.path.join("cache", "macro", "daily")
FR_D_IND, FR_D_FF = "49_Industry_Portfolios_daily_CSV.zip", "F-F_Research_Data_Factors_daily_CSV.zip"
WEEKLY_RULES = [
    ("Live rule", {"structure": "one", "t": 1 / 3, "weights": "equal", "event": None, "universe": "core28", "reentry": "none"}),
    ("Trend only", {"structure": "trend", "weights": "equal", "event": None, "universe": "core28", "reentry": "none"}),
    ("Indicators 0.25 OR trend, track-record weights",
     {"structure": "or_trend", "t": 0.25, "weights": "lift", "event": "15/12", "universe": "core28", "reentry": "none"}),
    ("One switch 0.30, track-record weights, fast re-entry",
     {"structure": "one", "t": 0.30, "weights": "lift", "event": "15/12", "universe": "core28", "reentry": "fast"}),
    ("Graded 0.15-0.35, equal votes",
     {"structure": "graded", "band": (0.15, 0.35), "weights": "equal", "event": None, "universe": "core28", "reentry": "none"}),
]


def _yahoo_daily(sym):
    from .fetch import _get
    js = _get(f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}",
              params={"period1": 0, "period2": 9999999999, "interval": "1d", "events": "div,split",
                      "includeAdjustedClose": "true"}).json()
    res = js["chart"]["result"][0]
    adj = res["indicators"].get("adjclose", [{}])[0].get("adjclose") or res["indicators"]["quote"][0]["close"]
    s = pd.Series(adj, index=pd.to_datetime(res["timestamp"], unit="s").normalize(), dtype=float).dropna()
    return s[~s.index.duplicated(keep="last")]


def _french_daily(fname):
    import csv
    import io
    import zipfile
    from .fetch import FRENCH_URL, _get
    z = zipfile.ZipFile(io.BytesIO(_get(FRENCH_URL + fname).content))
    text = z.read(z.namelist()[0]).decode("latin-1")
    rows, header = {}, None
    for row in csv.reader(io.StringIO(text)):
        cells = [c.strip() for c in row]
        if not any(cells):
            if rows:
                break
            continue
        if cells[0] == "" and len(cells) > 1 and not rows:
            header = cells
            continue
        if header is None or not (len(cells[0]) == 8 and cells[0].isdigit()):
            if rows:
                break
            continue
        vals = []
        for v in cells[1:len(header)]:
            try:
                x = float(v)
                vals.append(np.nan if x <= -99 else x / 100.0)
            except ValueError:
                vals.append(np.nan)
        rows[cells[0]] = vals
    df = pd.DataFrame.from_dict(rows, orient="index", columns=header[1:len(header)])
    df.index = pd.to_datetime(df.index, format="%Y%m%d")
    return df


def fetch_daily(log=print):
    os.makedirs(DDIR, exist_ok=True)
    syms = sorted(set(["SPY", "^VIX", "HYG", "IEF", "DX-Y.NYB", "SOXX", "XLY"] + [i["etf"] for i in R.INDUSTRIES]))
    bad = []
    for s_ in syms:
        p = os.path.join(DDIR, s_.replace("^", "").replace("-", "_").replace(".", "_") + ".csv")
        if os.path.exists(p):
            continue
        try:
            _yahoo_daily(s_).rename("v").to_csv(p, index_label="date")
        except Exception as e:                       # noqa: BLE001
            bad.append(f"{s_}:{str(e)[:40]}")
        time.sleep(0.5)
    for tag, fn in (("FR_D_IND", FR_D_IND), ("FR_D_FF", FR_D_FF)):
        p = os.path.join(DDIR, tag + ".csv.gz")
        if not os.path.exists(p):
            try:
                _french_daily(fn).to_csv(p, index_label="date")
            except Exception as e:                   # noqa: BLE001
                bad.append(f"{tag}:{str(e)[:60]}")
    log(f"daily data: {len(syms)} symbols + French daily; failed {bad}")


def _dl(name):
    p = os.path.join(DDIR, name.replace("^", "").replace("-", "_").replace(".", "_") + ".csv")
    if not os.path.exists(p):
        return pd.Series(dtype=float)
    s_ = pd.read_csv(p, parse_dates=["date"], index_col="date")["v"]
    return s_[~s_.index.duplicated(keep="last")].sort_index()


def daily_panel():
    ind = pd.read_csv(os.path.join(DDIR, "FR_D_IND.csv.gz"), parse_dates=["date"], index_col="date")
    ff = pd.read_csv(os.path.join(DDIR, "FR_D_FF.csv.gz"), parse_dates=["date"], index_col="date")
    spy = _dl("SPY")
    days = ind.index.union(spy.index)
    days = days[days >= pd.Timestamp("1985-01-01")]
    def splice(etf_px, proxy_cols):
        er = etf_px.reindex(days).pct_change(fill_method=None) if len(etf_px) else pd.Series(np.nan, index=days)
        er[etf_px.reindex(days).isna()] = np.nan
        cols = [c for c in proxy_cols if c in ind.columns]
        pr = ind[cols].reindex(days).mean(axis=1) if cols else pd.Series(np.nan, index=days)
        return er.where(er.notna(), pr)
    sec = pd.DataFrame({it["etf"]: splice(_dl(it["etf"]), it["proxy"]) for it in R.INDUSTRIES})
    xly = splice(_dl("XLY"), ["Rtail", "Autos", "Clths", "Meals"])
    mk = spy.reindex(days).pct_change(fill_method=None)
    mk[spy.reindex(days).isna()] = np.nan
    fm = (ff["Mkt-RF"] + ff["RF"]).reindex(days)
    mkt = mk.where(mk.notna(), fm)
    rf = ff["RF"].reindex(days).ffill().fillna(0)
    lvl = lambda r: (1 + r.fillna(0)).cumprod().where(r.notna().cummax())
    return {"days": days, "sec": sec.apply(lvl), "xly": lvl(xly), "mkt_r": mkt, "mkt": lvl(mkt), "rf": rf,
            "vix": _dl("^VIX").reindex(days).ffill(limit=3), "dxy": _dl("DX-Y.NYB").reindex(days).ffill(limit=3),
            "hyg": _dl("HYG").reindex(days), "ief": _dl("IEF").reindex(days)}


def weekly_values(P):
    """Fast indicators each Friday, defined like the monthly ones (month-based windows use completed month-ends)."""
    days = P["days"]
    wk = pd.Series(days, index=days).groupby(days.to_period("W-FRI")).last()      # last trading day of each week
    me = pd.Series(days, index=days).groupby(days.to_period("M")).last()          # last trading day of each month
    prev = wk.dt.to_period("M") - 1
    def at(x, dates):
        return x.reindex(dates.values).values
    def me_roll(x, n, fn):                       # rolling stat over the n month-ends up to the previous month
        m = x.reindex(me.values)
        m.index = me.index
        r = getattr(m.rolling(n, min_periods=n), fn)()
        return r.reindex(prev.values).values
    L, M = P["sec"], P["mkt"]
    W = pd.DataFrame(index=wk.index)
    W["vix"] = at(P["vix"], wk)
    lm = at(M, wk)
    W["spx_trend"] = (lm / ((me_roll(M, 9, "sum") + lm) / 10) - 1) * 100
    h, i_ = P["hyg"], P["ief"]
    hw, iw = pd.Series(at(h, wk), index=wk.index), pd.Series(at(i_, wk), index=wk.index)
    W["junk"] = ((hw / hw.shift(13)) - (iw / iw.shift(13))) * 100
    def r26(x):
        xw = pd.Series(at(x, wk), index=wk.index)
        return xw / xw.shift(26) - 1
    W["banks"] = (r26(L["KBE"]) - r26(M)) * 100
    dx = at(P["dxy"], wk)
    W["dollar_break"] = (dx / me_roll(P["dxy"], 12, "max") - 1) * 100
    ls = at(L["SMH"], wk)
    W["chips_break"] = (ls / np.fmax(me_roll(L["SMH"], 11, "max"), ls) - 1) * 100
    up, down, av = 0, 0, 0
    for c in L.columns:
        lc = at(L[c], wk)
        m10 = (me_roll(L[c], 9, "sum") + lc) / 10
        hi12 = np.fmax(me_roll(L[c], 11, "max"), lc)
        ok = ~np.isnan(lc) & ~np.isnan(m10) & ~np.isnan(hi12)
        up = up + np.where(ok, lc > m10, 0)
        down = down + np.where(ok, lc / hi12 - 1 <= -0.20, 0)
        av = av + ok
    W["breadth"] = np.where(av > 0, up / np.maximum(av, 1) * 100, np.nan)
    W["breakdowns"] = np.where(av > 0, down / np.maximum(av, 1) * 100, np.nan)
    W["transports"] = (r26(L["IYT"]) - r26(L["XLI"])) * 100
    rl = L["ITB"] / M
    rw = at(rl, wk)
    W["homebuilders"] = (rw / np.fmax(me_roll(rl, 23, "max"), rw) - 1) * 100
    W["cyc_def"] = (sum(r26(L[k]) for k in R.CYCLICAL) / len(R.CYCLICAL) - sum(r26(L[k]) for k in R.DEFENSIVE) / len(R.DEFENSIVE)) * 100
    W["staples_disc"] = (r26(L["XLP"]) - r26(P["xly"])) * 100
    W["friday"] = wk.values
    W["prev_month"] = prev.values
    return W


def weekly(log=print):
    fetch_daily(log)
    d, grid, sc, val, lvl, rf_m = load()
    P = daily_panel()
    W = weekly_values(P)
    pil = {i["id"]: i for i in R.INDICATORS}
    mret = lvl.pct_change(fill_method=None)
    ev = {"15/12": event(lvl, 0.15, 12), "10/6": event(lvl, 0.10, 6)}
    hz = {"15/12": 12, "10/6": 6}
    # worst-fifth level of each fast indicator from its monthly history known at each month-end
    thr = {}
    for k in FAST:
        x = val[k] * pil[k]["dir"]
        thr[k] = x.expanding(min_periods=120).quantile(0.8)
    pm = pd.PeriodIndex(W["prev_month"], freq="M")
    ok_w = W["friday"] >= pd.Timestamp("1990-01-01")
    W = W[ok_w.values]
    pm = pm[ok_w.values]
    flags, avail = {}, {}
    for k in pil:
        if k in FAST:
            v = W[k].values * pil[k]["dir"]
            t_ = thr[k].reindex(pm).values
            flags[k] = np.where(np.isnan(v) | np.isnan(t_), 0.0, v >= t_)
            avail[k] = (~np.isnan(v) & ~np.isnan(t_)).astype(float)
        else:
            s_ = sc[k].reindex(pm).values
            flags[k] = np.where(np.isnan(s_), 0.0, s_ >= 80)
            avail[k] = (~np.isnan(s_)).astype(float)
    trend_up_w = ~(W["spx_trend"].values < 0)
    vix_ok = ~(flags["vix"] > 0)
    junk_ok = ~(flags["junk"] > 0)
    fast_ok_w = (W["spx_trend"].values > 0) & vix_ok & junk_ok
    days = P["days"]
    days = days[days >= pd.Timestamp("1990-01-01")]
    mret_d, rf_d = P["mkt_r"].reindex(days), P["rf"].reindex(days)
    me_days = pd.Series(days, index=days).groupby(days.to_period("M")).last()
    ok_m = fast_ok(sc, val)
    trend_up_m = (val["spx_trend"] > 0).fillna(True)

    def wshares(spec):
        ids, early, confirm = groups(spec["universe"])
        evd = spec["event"] or "15/12"
        wm = weights(sc, ids, ev[evd], hz[evd], spec["weights"]).reindex(pm)
        def sh(g):
            num = sum(wm[k].values * flags[k] for k in g)
            den = sum(wm[k].values * avail[k] for k in g)
            n_av = sum(avail[k] for k in g)
            out = np.where(den > 0, num / np.where(den > 0, den, 1), 0.0)
            return np.where(n_av >= 10, out, 0.0)
        return {"all": sh(ids), "early": sh(early), "confirm": sh(confirm), "trend_up": trend_up_w}

    def mshares(spec):
        ids, early, confirm = groups(spec["universe"])
        evd = spec["event"] or "15/12"
        w = weights(sc, ids, ev[evd], hz[evd], spec["weights"])
        return {"all": share(sc, w, ids).values, "early": share(sc, w, early).values,
                "confirm": share(sc, w, confirm).values, "trend_up": trend_up_m.values}

    def daily_exposure(dec_dates, dec_vals):
        e = pd.Series(np.nan, index=days)
        nxt = days.searchsorted(pd.DatetimeIndex(dec_dates), side="right")   # effective the next trading day
        for j, v in zip(nxt, dec_vals):
            if j < len(days):
                e.iloc[j] = v
        return e.ffill().fillna(1.0)

    def dstats(e):
        r = e * mret_d + (1 - e) * rf_d
        r = r.dropna()
        lv_ = (1 + r).cumprod()
        yrs = len(r) / 252
        ex = r - rf_d.reindex(r.index)
        sw = int((e.diff().abs() > 1e-9).sum())
        return {"cagr": (lv_.iloc[-1] ** (1 / yrs) - 1) * 100, "maxdd": ((lv_ / lv_.cummax()) - 1).min() * 100,
                "vol": r.std() * math.sqrt(252) * 100, "sharpe": ex.mean() / r.std() * math.sqrt(252),
                "avg": e.mean() * 100, "switches": sw / yrs, "r": r}

    mk_l = (1 + mret_d.fillna(0)).cumprod()
    dfalls = []                                  # daily falls of 15%+ since 1990
    v_, ix = mk_l.values, mk_l.index
    pk, i = 0, 0
    while i < len(v_):
        if v_[i] >= v_[pk]:
            pk = i
        elif v_[i] / v_[pk] - 1 <= -0.15:
            j, tr = i, i
            while j < len(v_) and v_[j] < v_[pk]:
                if v_[j] < v_[tr]:
                    tr = j
                j += 1
            k10 = next(q for q in range(pk, tr + 1) if v_[q] / v_[pk] - 1 <= -0.10)
            dfalls.append((ix[pk], ix[tr], v_[tr] / v_[pk] - 1, ix[k10]))
            pk = j if j < len(v_) else len(v_) - 1
            i = j
            continue
        i += 1
    sp = dstats(pd.Series(1.0, index=days))
    log(f"weekly test {days[0].date()} to {days[-1].date()} (daily returns; S&P 500 {sp['cagr']:.1f}%/yr, worst {sp['maxdd']:.0f}%, Sharpe {sp['sharpe']:.2f})")
    log("falls of 15%+: " + ", ".join(f"{a.date()}->{b.date()} {c * 100:.0f}%" for a, b, c, _ in dfalls))
    rows = {}
    for name, spec in WEEKLY_RULES:
        em = exposure(mshares(spec), spec, ok_m.values)
        mdates = [me_days.get(p_) for p_ in grid if p_ in me_days.index]
        mvals = [em[grid.get_loc(p_)] for p_ in grid if p_ in me_days.index]
        e_m = daily_exposure(mdates, mvals)
        ew = exposure(wshares(spec), dict(spec, mute=52), fast_ok_w)
        e_w = daily_exposure(W["friday"].values, ew)
        for tag, e in (("monthly", e_m), ("weekly", e_w)):
            st_ = dstats(e)
            fl_ = []
            for a, b, c, k10 in dfalls:
                win = e[(e.index > a - pd.Timedelta(days=183)) & (e.index <= b)]
                first = win[win < 1 - 1e-9]
                lead = None if not len(first) else round((first.index[0] - a).days / 7)
                intime = bool(len(first) and first.index[0] <= k10)
                seg = st_["r"][(st_["r"].index > a) & (st_["r"].index <= b)]
                sl = (1 + seg).cumprod()
                fl_.append((lead, intime, min(0.0, (sl / sl.cummax().clip(lower=1)).min() - 1) * 100))
            rows[(name, tag)] = (st_, fl_)
        a_, b_ = rows[(name, "monthly")][0], rows[(name, "weekly")][0]
        log(f"{name}:")
        for tag in ("monthly", "weekly"):
            st_, fl_ = rows[(name, tag)]
            log(f"   checked {tag:<7}: {st_['cagr']:5.1f}%/yr  worst {st_['maxdd']:6.1f}%  Sharpe {st_['sharpe']:.2f}  avg stocks {st_['avg']:3.0f}%"
                f"  changes/yr {st_['switches']:.1f}  falls cut in time {sum(f[1] for f in fl_)}/{len(fl_)}")
    log("per fall: weeks from the S&P peak to the first cut (window from 26 weeks before) / worst fall with the rule (S&P in brackets)")
    for fi, (a, b, c, k10) in enumerate(dfalls):
        cells = []
        for name, _ in WEEKLY_RULES[:3]:
            for tag in ("monthly", "weekly"):
                ld, it, wf = rows[(name, tag)][1][fi]
                cells.append(f"{name.split(',')[0][:18]} {tag[0]}: {'-' if ld is None else f'{ld:+d}w'} {wf:.0f}%")
        log(f"   {a.date()} ({c * 100:.0f}%): " + " | ".join(cells))
    return rows


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "weekly":
        weekly()
    else:
        main()
