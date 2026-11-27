"""Global Macro Book v1 (2026-10-30): combine the signal families into one risk-managed, costed paper book.

Pipeline, all point in time (positions decided at month end t, earn month t+1):
 1. Family positions per market (signals.py definitions): price trend, economic trend, carry, value, cross-sectional
    momentum. Each family-and-asset-class block is scaled to unit ex-ante volatility (trailing 36-month realised vol of
    the block, lagged), so blocks are comparable.
 2. Family risk shares (plan section 3, fixed before the holdout): trend 30, econ 30, carry 20, value 15, momentum 5
    (the 10% earmarked for WRDS revisions moved to trend and econ, as the plan prescribes when it is not live).
    Asset classes get equal risk.
 3. Whole book scaled to 10% annual vol (trailing 36-month realised vol of the unscaled book, lagged); gross notional
    capped at 5x; one market capped at 10% of the risk budget (position x vol <= 0.1 x 10% ... approximated by a
    notional-vol cap).
 4. Costs: one-way cost per market type on every change in position, plus futures rolls; EM equity shorts pay 1%/yr
    borrow. Results also at twice the costs.

Placeholders (not yet in v1; marked so the site and the plan show them):
 - BLOOMBERG (next week): per-commodity excess-return history before 2000 and futures curves -> commodity carry for
   metals, grains, softs and livestock; replaces the AQR index stand-in.
 - EQUITY VALUE / CARRY: needs country valuations and dividend yields (WRDS research, or MSCI P/E, P/B, D/Y live).
 - WRDS REVISIONS (family 3.6): research only; weight moved to trend and econ.
 - RISK SCALER (early-warning, 30-100% of risk): separate test, next version.
 - ECON POINT-IN-TIME: econ uses revised OECD data; first-release vintages needed before it counts.
Design period 1990-2010, extra check 1975-89. The holdout 2011-2026 is not printed (run once after freezing).
"""
import os
import pickle

import numpy as np
import pandas as pd

from . import panel as P
from . import signals as G

FAMILY_W = {"trend": 0.30, "econ": 0.30, "carry": 0.20, "value": 0.15, "xsmom": 0.05}
VOL_TARGET = 0.10
GROSS_CAP = 5.0
MARKET_RISK_CAP = 0.10          # one market at most 10% of the book's risk (position x vol <= 0.1 x 10%... see cap())
PLACEHOLDERS = ["BLOOMBERG commodity curves and pre-2000 commodity returns",
                "EQUITY value for emerging markets (only DM + US by dividend yield so far); equity carry (failed)",
                "WRDS revisions (research only)", "Early-warning risk scaler (tested, not adopted)",
                "Econ growth theme on first-release data (left out in v1.1)"]
EM_EQ = ("eq_cn", "eq_kr_kospi", "eq_tw", "eq_in", "eq_br_ibov", "eq_mx_ipc", "eq_za")
EM_FX = ("fx_mxn", "fx_brl", "fx_krw", "fx_zar")


def cost_bp(k):
    """One-way cost (bp of notional) and futures rolls per year."""
    if k.startswith("eq_"):
        return (5.0, 0) if k in EM_EQ else ((1.0, 4) if k.startswith("eq_us") else (2.0, 4))
    if k.startswith(("bd_", "st_")):
        return 1.0, 4
    if k.startswith("fx_"):
        return (8.0, 4) if k in EM_FX else (2.0, 4)
    if k.startswith("cm_"):
        return (6.0, 12) if k in ("cm_natgas",) else ((4.0, 12) if k in ("cm_wti", "cm_brent", "cm_heatoil",
                                                                         "cm_gasoline") else (4.0, 5))
    return 3.0, 4


def trend_signal(R, cfg, vol, S=None):
    """Price-trend score in [-1, 1] per market (see config.BASE['trend'])."""
    t = cfg["trend"]
    X = R
    if t.get("spot") and S is not None:                  # strip the carry accrual: trend on price moves only
        C = S["C"].reindex(index=R.index)
        cols = [c for c in C.columns if c in R.columns and c.startswith(("bd_", "st_", "fx_"))]
        X = R.copy()
        X[cols] = R[cols] - C[cols].shift(1) / 12
    hz = t.get("horizons", (1, 3, 12))
    if t.get("kind", "sign") == "sign":
        lvl = (1 + X.fillna(0)).cumprod().where(X.notna().cummax())
        return sum(np.sign(lvl / lvl.shift(h) - 1) for h in hz) / len(hz)
    cap = t.get("cap", 2.0)
    lr = np.log1p(X)
    parts = [(lr.rolling(h, min_periods=h).sum() / (vol * np.sqrt(h / 12))).clip(-cap, cap) / cap for h in hz]
    return sum(parts) / len(parts)


def cluster_factor(R, cols, window=60):
    """Within-class weight factor: 1 / (sum of positive correlations with the class), mean 1 across available
    markets, from the trailing 60 months (point in time)."""
    X = R[cols]
    out = pd.DataFrame(np.nan, index=R.index, columns=cols)
    for i in range(window, len(R.index)):
        w = X.iloc[i - window + 1:i + 1]
        ok = [c for c in cols if w[c].notna().sum() >= 24]
        if len(ok) < 2:
            continue
        cm = w[ok].corr(min_periods=24).clip(lower=0).fillna(0)
        f = 1 / cm.sum(axis=1)
        out.loc[R.index[i], ok] = (f / f.mean()).values
    return out


def family_positions(R, cfg=None, daily=None, S=None, vol_days=None, components=False, score_perm=None):
    """Unscaled position (notional per unit capital) per family, per market: score x 40% / vol, weighted in class.
    S: optional signal override {"E", "C", "V", optional "ET": {theme: scores}} (gm/variants.py).
    gm-2.1.0 options (default off = today's code path, unchanged): a config "grid" (E7), components=True (E9 masks),
    score_perm (E10 placebo), vol_days (E8 tranche sampling day of the daily volatility). With any of grid, components
    or score_perm the version path below is used (family_positions_v); it returns (positions, vol, components)."""
    from . import config as CF
    from . import vol as VM
    cfg = cfg or CF.BASE
    S = S if S is not None else pickle.load(open(os.path.join(P.OUT, "signals.pkl"), "rb"))
    if cfg.get("grid") or components or score_perm is not None:
        return family_positions_v(R, cfg, daily, S, vol_days, score_perm)
    vol = VM.estimate(R, cfg, daily) if vol_days is None else VM.estimate(R, cfg, daily, sample_days=vol_days)
    trend = trend_signal(R, cfg, vol, S)
    xsm = np.log1p(R).shift(1).rolling(11, min_periods=11).sum()
    V = S["V"][[c for c in S["V"].columns if c.startswith(("fx_", "bd_", "eq_"))]]  # commodity value: failed, out
    C = S["C"][[c for c in S["C"].columns if not c.startswith("eq_")]]       # equity carry: weak in design, out
    C = G.x1_seasonal(C, cfg.get("x1_seasonal"))                           # E13 (gm-2.2.0): only with the config key
    fams = {"trend": (trend, "dir"), "econ": (S["E"], "dir"), "carry": (C, "half"), "value": (V, "cs"),
            "xsmom": (xsm, "cs")}
    if cfg.get("econ_structure", "score_avg") == "themes":        # one block per theme x asset class
        ET = S.get("ET") or G.econ_theme_scores(R)
        del fams["econ"]
        for t in cfg.get("econ_themes", G.ECON_THEMES):
            fams["econ_" + t] = (ET[t], "dir")
    fams = {f: v for f, v in fams.items() if _fw(cfg, f) > 0}
    cf_cache = {}
    out = {}
    for f, (X, kind) in fams.items():
        X = X.reindex(index=R.index)
        pos = {}
        for c, pre in G.CLASSES.items():
            cols = [k for k in X.columns if k.startswith(pre) and k in R and k != "cm_aqr_ew" or
                    (k == "cm_aqr_ew" and f in ("trend",) and k in X.columns)]
            cols = [k for k in cols if k in R.columns]
            if not cols:
                continue
            if kind == "dir":
                w = X[cols].clip(-1, 1)
            elif kind == "cs":
                w = G.cs_rank(X, cols)
            else:
                w = (G.cs_rank(X, cols).fillna(0) * 0.5 + np.sign(X[cols]) * 0.5).where(X[cols].notna())
            p = w * 0.40 / vol[cols]
            if cfg.get("within_class", "equal") == "cluster":
                key = (c, tuple(cols))
                if key not in cf_cache:
                    cf_cache[key] = cluster_factor(R, cols)
                p = p * cf_cache[key].fillna(1.0)
            n = p.notna().sum(axis=1)
            p = p.div(n.where(n > 0), axis=0)
            if c == "CM":                                # alternative commodities: at most 30% of commodity risk
                from .bloomberg import ALT_COMMOD
                alt = [k for k in p.columns if k in ALT_COMMOD]
                if alt:
                    core = [k for k in p.columns if k not in alt]
                    ra = (p[alt].abs() * vol[alt]).sum(axis=1)
                    rc = (p[core].abs() * vol[core]).sum(axis=1)
                    f_alt = (0.3 / 0.7 * rc / ra.where(ra > 0)).clip(upper=1).fillna(1)
                    p[alt] = p[alt].mul(f_alt, axis=0)
            pos[c] = p
        out[f] = pos
    return out, vol


def _trend_version(R, h, shape, vol_v, cap=2.0):
    """E7 Trend version (SPEC_Trend s3 steps 2-3): 'sign' = sign of the compounded h-month excess return (no value if
    lvl(t-h) is missing); 'graded' = clip(sum of ln(1 + R) over h months / (vol_v x sqrt(h / 12)), -cap, cap) / cap."""
    if shape == "sign":
        lvl = (1 + R.fillna(0)).cumprod().where(R.notna().cummax())
        return np.sign(lvl / lvl.shift(h) - 1)
    lr = np.log1p(R)
    return (lr.rolling(h, min_periods=h).sum() / (vol_v * np.sqrt(h / 12))).clip(-cap, cap) / cap


def _need(S, key, what):
    if key not in S:
        raise KeyError("signals dict has no %r (%s): compute it with gm.signals (gm_engine.run does) before a grid "
                       "run" % (key, what))
    return S[key]


def family_versions(R, cfg, daily, S, vol, vol_days=None):
    """E7: {family: [(X, kind, vol_v), ...]} in version order (1-based numbering = list position + 1).
    Without a grid each family has its single form, except Carry, always split into v1 (sign) and v2 (rank)."""
    from . import config as CF
    from . import vol as VM
    grid = cfg.get("grid") or {}
    fams = {}
    if "trend" in grid:
        vols = {}
        vers = []
        for h, shape, vm in grid["trend"]:
            if vm not in vols:
                vc = CF.variant(CF.CANDIDATE, vol={"model": vm}) if vm == "hybrid" else {"vol": {"model": "m36"}}
                same = cfg.get("vol", {}) == vc["vol"] or (vm == "m36" and cfg.get("vol", {}).get("model") == "m36")
                vols[vm] = vol if same else VM.estimate(R, vc, daily, sample_days=vol_days)
            vers.append((_trend_version(R, h, shape, vols[vm], cfg["trend"].get("cap", 2.0)), "dir", vols[vm]))
        fams["trend"] = vers
    else:
        fams["trend"] = [(trend_signal(R, cfg, vol, S), "dir", vol)]
    if cfg.get("econ_structure", "score_avg") == "themes":
        ET = S.get("ET") or G.econ_theme_scores(R)
        for t in cfg.get("econ_themes", G.ECON_THEMES):
            fams["econ_" + t] = [(ET[t], "dir", vol)]
    elif "econ" in grid:
        fams["econ"] = [(S["E"] if sh == "tanh" else _need(S, "E_" + sh, "Economic trend shape " + sh), "dir", vol)
                        for sh in grid["econ"]]
    else:
        fams["econ"] = [(S["E"], "dir", vol)]
    C = S["C"][[c for c in S["C"].columns if not c.startswith("eq_")]]       # equity carry: weak in design, out
    C = G.x1_seasonal(C, cfg.get("x1_seasonal"))                           # E13 (gm-2.2.0): only with the config key
    cv = grid.get("carry", ("dir", "cs"))
    fams["carry"] = [(np.sign(C) if k == "dir" else C, k, vol) for k in cv]
    V = S["V"][[c for c in S["V"].columns if c.startswith(("fx_", "bd_", "eq_"))]]  # commodity value: failed, out
    vers = []
    for v in grid.get("value", (1,)):
        X = V if v == 1 else _need(S, "V2", "Value version 2")
        vers.append((X[[c for c in X.columns if c.startswith(("fx_", "bd_", "eq_"))]], "cs", vol))
    fams["value"] = vers
    xsm = np.log1p(R).shift(1).rolling(11, min_periods=11).sum()
    fams["xsmom"] = [(xsm, "cs", vol)]
    return fams


def _perm_rows(w, score_perm, fam, cls):
    """E10 placebo: rows of w inside the window moved by the permutation (all markets jointly).
    score_perm = {"start": first window label, "perm": index array over the window, optional "only": set of
    (family, class) to move (default all)}."""
    if score_perm is None:
        return w
    only = score_perm.get("only")
    if only is not None and (fam, cls) not in only and (fam, "*") not in only:
        return w
    perm = np.asarray(score_perm["perm"])
    i0 = w.index.get_loc(pd.Period(score_perm["start"], "M"))
    n = min(len(perm), len(w) - i0)
    if n < len(perm):
        raise ValueError("placebo window runs past the data")
    out = w.copy()
    out.iloc[i0:i0 + n] = w.iloc[i0:i0 + n].values[perm]
    return out


def family_positions_v(R, cfg, daily, S, vol_days=None, score_perm=None):
    """E7 / E9 / E10 version path. Each version is a complete pod: w (score clipped to [-1, 1], or the class rank) x
    0.40 / vol_v, divided by the count of markets in its class with a position (n_v); pod position = sum over versions
    of p_v / V, a missing version adding 0, no position where no version has one (closed here, gm/CHANGES.md
    gm-2.1.0 item 3). Returns (fam_pos {family: {class: frame}}, vol, comp {family: {class: [term_v, ...]}}),
    term_v = p_v / V (so the terms of a class sum to its pod position)."""
    from . import vol as VM
    vol = VM.estimate(R, cfg, daily) if vol_days is None else VM.estimate(R, cfg, daily, sample_days=vol_days)
    fams = {f: v for f, v in family_versions(R, cfg, daily, S, vol, vol_days).items() if _fw(cfg, f) > 0 or
            f in ("trend", "econ", "carry", "value")}
    cf_cache, out, comp = {}, {}, {}
    for f, versions in fams.items():
        V = len(versions)
        pos, cpos = {}, {}
        for c, pre in G.CLASSES.items():
            terms = []
            for X, kind, vol_v in versions:
                X = X.reindex(index=R.index)
                cols = [k for k in X.columns if k.startswith(pre) and k in R and k != "cm_aqr_ew" or
                        (k == "cm_aqr_ew" and f in ("trend",) and k in X.columns)]
                cols = [k for k in cols if k in R.columns]
                if not cols:
                    continue
                w = X[cols].clip(-1, 1) if kind == "dir" else G.cs_rank(X, cols)
                w = _perm_rows(w, score_perm, f, c)
                p = w * 0.40 / vol_v[cols]
                if cfg.get("within_class", "equal") == "cluster":
                    key = (c, tuple(cols))
                    if key not in cf_cache:
                        cf_cache[key] = cluster_factor(R, cols)
                    p = p * cf_cache[key].fillna(1.0)
                n = p.notna().sum(axis=1)
                terms.append(p.div(n.where(n > 0), axis=0))
            if not terms:
                continue
            cols = sorted(set().union(*[t.columns for t in terms]), key=list(R.columns).index)
            terms = [t.reindex(columns=cols) / V for t in terms]
            have = sum(t.notna().astype(int) for t in terms) > 0
            p = sum(t.fillna(0) for t in terms).where(have)
            if c == "CM":                                # alternative commodities: at most 30% of commodity risk
                from .bloomberg import ALT_COMMOD
                alt = [k for k in p.columns if k in ALT_COMMOD]
                if alt:
                    core = [k for k in p.columns if k not in alt]
                    ra = (p[alt].abs() * vol[alt]).sum(axis=1)
                    rc = (p[core].abs() * vol[core]).sum(axis=1)
                    f_alt = (0.3 / 0.7 * rc / ra.where(ra > 0)).clip(upper=1).fillna(1)
                    p[alt] = p[alt].mul(f_alt, axis=0)
                    for t in terms:
                        t[alt] = t[alt].mul(f_alt, axis=0)
            pos[c] = p
            cpos[c] = terms
        out[f] = pos
        comp[f] = cpos
    out = {f: v for f, v in out.items() if _fw(cfg, f) > 0}
    return out, vol, comp


def mask_components(comp, mask):
    """E9: {class: masked position} = the sum of the class terms whose (pod, class, version) the mask holds
    (mask = list of (pod, class or '*', version (1-based) or '*')); classes with no masked term are left out."""
    out = {}
    for pod, cls, ver in mask:
        for c, terms in comp.get(pod, {}).items():
            if cls != "*" and c != cls:
                continue
            for i, t in enumerate(terms):
                if ver != "*" and i + 1 != ver:
                    continue
                key = (pod, c)
                out.setdefault(key, []).append(t)
    res = {}
    for key, ts in out.items():
        have = sum(t.notna().astype(int) for t in ts) > 0
        res[key] = sum(t.fillna(0) for t in ts).where(have)
    return res


def cap_positions(pos, cap, groups=None):
    """Per-market cap (book.py: each column clipped to +-cap). E11 (gm-2.1.0): a group (spread pod) is never clipped
    column by column: all members are multiplied by min(1, min over members with a position of cap_j / |x_j|), with
    cap_j = the member's own cap, or the cap of the group's 'cap_from' member for every member (Curve carry: both legs
    take the front leg's cap). groups = list of {"members": [...], "cap_from": None or a member}; None = today."""
    if not groups:
        return pos.clip(lower=-cap, upper=cap)
    grouped = [m for g in groups for m in g["members"]]
    out = pos.copy()
    rest = [c for c in pos.columns if c not in grouped]
    out[rest] = pos[rest].clip(lower=-cap[rest], upper=cap[rest])
    for g in groups:
        mem = [m for m in g["members"] if m in pos.columns]
        if not mem:
            continue
        cj = pd.concat([cap[g["cap_from"]]] * len(mem), axis=1, keys=mem) if g.get("cap_from") else cap[mem]
        ratio = (cj / pos[mem].abs().where(pos[mem].abs() > 0)).min(axis=1).clip(upper=1).fillna(1)
        out[mem] = pos[mem].mul(ratio, axis=0)
    return out


def _scaler(r, window=36, minp=24):
    """The block scaler's convention: 1 / (trailing realised volatility x sqrt(12)), lagged one month, at most 50."""
    return (1.0 / (r.rolling(window, min_periods=minp).std() * np.sqrt(12))).shift(1).clip(upper=50)


def _fw(cfg, f):
    """Family risk share; econ theme blocks share the econ weight equally."""
    fw = cfg["family_w"]
    if f.startswith("econ_"):
        return fw.get("econ", 0) / len(cfg.get("econ_themes", G.ECON_THEMES))
    return fw.get(f, 0)


def scenario_scale(pos, R, limit, windows):
    """Scale each month's book so that today's positions lose at most `limit` in any stress window that ended
    before that month (point in time)."""
    moves = {k: ((1 + R.loc[a:b]).prod(min_count=1) - 1, pd.Period(b, "M")) for k, (a, b) in windows.items()}
    f = pd.Series(1.0, index=pos.index)
    for t in pos.index:
        worst = 0.0
        for k, (mv, end) in moves.items():
            if end >= t:
                continue
            loss = float((pos.loc[t] * mv.reindex(pos.columns)).sum(min_count=1) or 0.0)
            worst = min(worst, loss)
        if worst < -limit:
            f[t] = limit / -worst
    return pos.mul(f, axis=0), f


def run(R, cost_mult=1.0, cfg=None, daily=None, S=None, seal="design", R_earn=None, vol_days=None, parts=None,
        score_perm=None, pos_fix=None):
    """seal (E5, gm-1.2.3): 'design' (default) = a design run sealed at config.SEAL_END (2010-12-31): inputs dated
    later are dropped before anything is computed and the outputs are checked (gm/seal.py); None = live paper run or
    the one-shot holdout run only (gm/run.py, gm/holdout.py).
    gm-2.1.0 options (all None = today's book, unchanged):
      R_earn      E6 / E8: the return each holding earns (the k = 1 or tranche form, gm/execution.py); positions,
                  signals, scalers and caps still read R (known at the decision close)
      vol_days    E8: label -> decision day; the daily volatility is sampled there (tranches)
      parts       E9: {part: mask} (config.CORE_PARTS / SHADOW_PARTS): the book holds only the masked components, each
                  part's summed scaled-block return rescaled to unit volatility and weighted 1 / n (family shares unused)
      score_perm  E10: placebo move of the score arrays (see _perm_rows)
      pos_fix     E8: final positions to impose where not missing (tranche 0's position for markets without daily
                  data), after the caps
    A config "grid" (E7) and "cap_groups" (E11) act through family_positions and cap_positions."""
    from . import config as CF
    from . import seal as SL
    cfg = cfg or CF.BASE
    T = SL.resolve(seal)
    if T is not None:
        if S is None:
            S = pickle.load(open(os.path.join(P.OUT, "signals.pkl"), "rb"))
        R, daily, S, R_earn, pos_fix = SL.cut_inputs(T, R, daily, S, R_earn, pos_fix)
    if parts is not None:
        return _run_parts(R, cost_mult, cfg, daily, S, T, R_earn, vol_days, parts, score_perm, pos_fix)
    if cfg.get("grid") or score_perm is not None:
        fam, vol, _ = family_positions(R, cfg, daily, S, vol_days=vol_days, score_perm=score_perm)
    else:
        fam, vol = family_positions(R, cfg, daily, S, vol_days=vol_days)
    fw = cfg["family_w"]
    total = pd.DataFrame(0.0, index=R.index, columns=R.columns)
    by_fam = {f: pd.DataFrame(0.0, index=R.index, columns=R.columns) for f in fam}
    blocks = {}
    bw = cfg.get("block_vol_months", 36)
    for f, pos in fam.items():
        for c, p in pos.items():
            r = (p.shift(1) * R[p.columns]).sum(axis=1, min_count=1)
            k = (1.0 / (r.rolling(bw, min_periods=24).std() * np.sqrt(12))).shift(1).clip(upper=50)
            blocks[(f, c)] = r * k
            scaled = p.mul(k, axis=0) * _fw(cfg, f)
            total[scaled.columns] = total[scaled.columns].add(scaled.fillna(0), fill_value=0)
            by_fam[f][scaled.columns] = by_fam[f][scaled.columns].add(scaled.fillna(0), fill_value=0)
    active = pd.concat(blocks, axis=1).notna().any(axis=1)
    return _finish(R, cost_mult, cfg, T, R_earn, pos_fix, total, by_fam, blocks, active, vol)


def _run_parts(R, cost_mult, cfg, daily, S, T, R_earn, vol_days, parts, score_perm, pos_fix):
    """E9 (gm-2.1.0): equal-risk book of parts. Masked block b = sum of a class's masked components (term p_v / V),
    block scaler k_b (36 months, at least 24, lagged, at most 50); part return = sum over its blocks of r_b(t) x
    k_b(t-1) (the return of the scaled block position); part scaler k_P by the same convention; total position =
    sum over parts of (1 / n) x k_P x sum over blocks of k_b x p_b, n = number of parts; then the book scaler, the
    caps and the costs of run(). Active months (where the book scaler reads a return): months with a scaled part
    return r_P x k_P, the convention of run()'s blocks (r x k), so the scaler never reads the warm-up zeros."""
    _, vol, comp = family_positions(R, cfg, daily, S, vol_days=vol_days, components=True, score_perm=score_perm)
    bw = cfg.get("block_vol_months", 36)
    n = len(parts)
    total = pd.DataFrame(0.0, index=R.index, columns=R.columns)
    by_part = {q: pd.DataFrame(0.0, index=R.index, columns=R.columns) for q in parts}
    blocks, part_ret, part_scaled = {}, {}, {}
    for q, mask in parts.items():
        mb = mask_components(comp, mask)
        inner = pd.DataFrame(0.0, index=R.index, columns=R.columns)
        rets = []
        for key, p in mb.items():
            r = (p.shift(1) * R[p.columns]).sum(axis=1, min_count=1)
            k = (1.0 / (r.rolling(bw, min_periods=24).std() * np.sqrt(12))).shift(1).clip(upper=50)
            blocks[(q,) + key] = r * k.shift(1)
            rets.append(r * k.shift(1))
            sc = p.mul(k, axis=0)
            inner[sc.columns] = inner[sc.columns].add(sc.fillna(0), fill_value=0)
        if not rets:
            continue
        rp = pd.concat(rets, axis=1).sum(axis=1, min_count=1)
        kp = _scaler(rp, bw)
        part_ret[q] = rp
        part_scaled[q] = rp * kp                 # as book.py's blocks table (r x k): defines the active months
        sc = inner.mul(kp, axis=0) / n
        total = total.add(sc.fillna(0), fill_value=0)
        by_part[q] = by_part[q].add(sc.fillna(0), fill_value=0)
    active = pd.DataFrame(part_scaled).notna().any(axis=1) if part_scaled else pd.Series(False, index=R.index)
    out = _finish(R, cost_mult, cfg, T, R_earn, pos_fix, total, by_part, blocks, active, vol, check=False)
    out["part_ret"] = pd.DataFrame(part_ret)
    out["part_scaled"] = pd.DataFrame(part_scaled)
    out["parts"] = {q: list(m) for q, m in parts.items()}
    from . import seal as SL
    return SL.check_output(out, T, "gm.book.run(parts)") if T is not None else out


def _finish(R, cost_mult, cfg, T, R_earn, pos_fix, total, by_fam, blocks, active, vol, check=True):
    """Book scaler, caps, costs and outputs (today's run() lines; gm-2.1.0 adds R_earn, pos_fix, cap groups)."""
    from . import config as CF
    from . import seal as SL
    raw = (total.shift(1) * R.fillna(0)).sum(axis=1).where(active)
    s = (cfg.get("book_vol", VOL_TARGET) / (raw.rolling(36, min_periods=24).std() * np.sqrt(12))).shift(1)
    pos = total.mul(s, axis=0)
    cap = (cfg.get("market_risk_cap", MARKET_RISK_CAP) * cfg.get("book_vol", VOL_TARGET) * 3) / vol
    pos = cap_positions(pos, cap, cfg.get("cap_groups"))
    gw = pd.Series({k: cfg.get("gross_weights", {}).get(k, 1.0) for k in pos.columns})
    g = (pos.abs() * gw).sum(axis=1)                    # e.g. 3-month rate futures counted 2-year equivalent
    pos = pos.mul((cfg.get("gross_cap", GROSS_CAP) / g).clip(upper=1), axis=0)
    if pos_fix is not None:
        fx = pos_fix.reindex(index=pos.index, columns=pos.columns)
        pos = fx.combine_first(pos)
    scen = pd.Series(1.0, index=R.index)
    if cfg.get("scenario_limit"):
        pos, scen = scenario_scale(pos, R, cfg["scenario_limit"], CF.STRESS_WINDOWS)
    lag = 1 + int(cfg.get("delay_months", 0))
    RE = R if R_earn is None else R_earn.reindex(index=R.index, columns=R.columns)
    gross = (pos.shift(lag) * RE).sum(axis=1, min_count=1).where(active & s.notna())
    one_way = pd.Series({k: cost_bp(k)[0] / 1e4 for k in R.columns})
    rolls = pd.Series({k: cost_bp(k)[1] for k in R.columns})
    trade = pos.diff().abs()
    tc = (trade * one_way).sum(axis=1) + (pos.abs() * one_way * 2 * rolls / 12).sum(axis=1)
    borrow = (pos[[k for k in EM_EQ if k in pos]].clip(upper=0).abs() * 0.01 / 12).sum(axis=1)
    net = gross - cost_mult * (tc.shift(lag) + borrow.shift(lag))
    turnover = trade.sum(axis=1)
    shrink = (pos.abs().sum(axis=1) / total.mul(s, axis=0).abs().sum(axis=1)).fillna(1)   # effect of the caps
    fam_pos = {f: v.mul(s * shrink, axis=0) for f, v in by_fam.items()}
    out = {"pos": pos, "gross": gross, "net": net, "blocks": pd.DataFrame(blocks), "turnover": turnover,
           "cost": (tc + borrow), "fam_pos": fam_pos, "vol": vol, "scenario_scale": scen, "cfg": cfg,
           "seal": None if T is None else str(T.date())}
    if not check:
        return out
    return SL.check_output(out, T, "gm.book.run") if T is not None else out


def placebo_net_fn(R, cfg, daily, S, start, only=None, runner=None, **kw):
    """E10 (7.7 T3): -> f(perm) giving the net return of the book or pod with its score arrays moved by the date map perm
    inside the window starting at `start` (perm None = the identity map, i.e. the pod itself on the same code path).
    runner: the book function (default gm.book.run; e.g. gm.execution.run_k1 with a day list) taking the same keywords
    plus score_perm."""
    run_ = runner or run

    def f(perm):
        if perm is None:
            from . import seal as SL
            T = SL.resolve(kw.get("seal", "design"))
            end = pd.Period(R.index[-1], "M") if T is None else min(pd.Period(R.index[-1], "M"), pd.Period(T, "M"))
            perm = np.arange((end - pd.Period(start, "M")).n + 1)
        sp = {"start": start, "perm": perm}
        if only is not None:
            sp["only"] = only
        return run_(R, cfg=cfg, daily=daily, S=S, score_perm=sp, **kw)["net"]
    return f


def stats(r, spx=None):
    r = r.dropna()
    if len(r) < 24:
        return "n/a"
    cum = (1 + r).cumprod()
    dd = (cum / cum.cummax() - 1).min()
    out = "ret %.1f%% vol %.1f%% SR %.2f maxDD %.0f%% worst12m %.0f%%" % (
        r.mean() * 1200, r.std() * np.sqrt(12) * 100, r.mean() / r.std() * np.sqrt(12), dd * 100,
        ((1 + r).rolling(12).apply(np.prod, raw=True) - 1).min() * 100)
    if spx is not None:
        out += " corrSPX %.2f" % r.corr(spx.reindex(r.index))
    return out


def main():
    D = pickle.load(open(os.path.join(P.OUT, "panel.pkl"), "rb"))
    R = D["R"]
    base, x2 = run(R), run(R, cost_mult=2.0)
    spx = R["eq_us_spx"]
    print("Global Macro Book v1 (paper). Design 1990-2010 and extra check 1975-89; holdout 2011-2026 not shown.")
    for a, b in (("1975-01", "1989-12"), ("1990-01", "2010-12")):
        print(" %s..%s" % (a[:4], b[:4]))
        print("   gross     ", stats(base["gross"].loc[a:b], spx))
        print("   net       ", stats(base["net"].loc[a:b], spx))
        print("   net x2cost", stats(x2["net"].loc[a:b]))
        print("   turnover %.1fx/yr, costs %.2f%%/yr" % (base["turnover"].loc[a:b].mean() * 12,
                                                        base["cost"].loc[a:b].mean() * 1200))
        bl = base["blocks"].loc[a:b]
        fam_sr = {f: round(float(bl[f].mean(axis=1).mean() / bl[f].mean(axis=1).std() * np.sqrt(12)), 2)
                  for f in FAMILY_W if f in bl.columns.get_level_values(0)}
        print("   family SR (unit-vol blocks, equal class weight):", fam_sr)
    net = base["net"]
    for lab, a, b in (("1987 crash Oct-Nov", "1987-10", "1987-11"), ("1994 bonds", "1994-02", "1994-11"),
                      ("1998 LTCM Aug-Oct", "1998-08", "1998-10"), ("2000-02 bear", "2000-04", "2002-09"),
                      ("2008 crisis", "2008-01", "2008-12")):
        rr, sp = net.loc[a:b], spx.loc[a:b]
        print("   %-20s book %+.1f%%  S&P excess %+.1f%%" % (lab, ((1 + rr).prod() - 1) * 100, ((1 + sp).prod() - 1) * 100))
    last = pd.Period(pd.Timestamp.today(), "M") - 1          # last complete month
    p = base["pos"].loc[last]
    vol = R.rolling(36, min_periods=12).std().loc[last] * np.sqrt(12)
    risk = (p * vol).dropna()
    risk = risk[risk.abs() > 1e-4].sort_values()
    print("\nCurrent positions as of %s (risk = notional x vol; book target 10%%):" % last)
    print("   largest shorts:", ", ".join("%s %.1f%%" % (k, v * 100) for k, v in risk.head(6).items()))
    print("   largest longs: ", ", ".join("%s %.1f%%" % (k, v * 100) for k, v in risk.tail(6)[::-1].items()))
    by_class = {c: round(float(p[[k for k in p.index if k.startswith(pre)]].abs().sum()), 2) for c, pre in G.CLASSES.items()}
    print("   gross notional by class:", by_class, "total %.2f" % p.abs().sum())
    print("Placeholders:", "; ".join(PLACEHOLDERS))
    pickle.dump({"base": base, "x2": x2}, open(os.path.join(P.OUT, "book_v1.pkl"), "wb"))


if __name__ == "__main__":
    main()
