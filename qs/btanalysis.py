"""From formation and return files to the per-screen statistics and the mechanical verdicts of
validation/PROTOCOL.md section 6."""
import numpy as np

from .btstats import (COST_PER_SIDE, LISTS, MIN_MONTHS, MIN_NAMES, alpha, auc, deflated_sharpe, mean_t,
                      pbo_cscv, placebo_percentile, reality_check, sharpe, sic_division, spearman, terciles)
from .screens import PASS, SCREENS

GRID = ("-0.3", "-0.2", "-0.1", "0", "0.1", "0.2", "0.3")


def next_ym(ym):
    y, m = int(ym[:4]), int(ym[5:])
    return f"{y + 1:04d}-01" if m == 12 else f"{y:04d}-{m + 1:02d}"


class Panel:
    """months: [(ym_held, formation, returns)] - formation made at the end of month ym, held over next_ym(ym)."""

    def __init__(self, months):
        self.months = months
        self.yms = [next_ym(f["ym"]) for f, _r in months]
        self._mom = self._momentum()

    def _momentum(self):
        """{index: {cik: 12-1 month return}} from the panel's own monthly returns."""
        out, hist = {}, []
        for i, (_f, rets) in enumerate(self.months):
            mom = {}
            if len(hist) >= 12:
                window = hist[-12:-1]            # months t-12 .. t-2 (skip the latest month)
                for c in rets:
                    vals = [h.get(c) for h in window]
                    if all(v is not None for v in vals):
                        mom[c] = float(np.prod([1 + v for v in vals]) - 1)
            out[i] = mom
            hist.append({c: v[0] for c, v in rets.items()})
        return out

    def char_bench(self, i):
        """{cik: cell mean return} - size x book-to-market x momentum terciles (DGTW-style) over the full universe."""
        form, rets = self.months[i]
        comp = form["companies"]
        avail = {c: v[0] for c, v in rets.items() if c in comp}
        size = terciles({c: comp[c].get("mcap") for c in avail})
        bm = terciles({c: (comp[c]["be"] / comp[c]["mcap"]) if comp[c].get("be") and comp[c].get("mcap") else None
                       for c in avail})
        mom = terciles({c: self._mom[i].get(c) for c in avail})
        cells = {}
        for c, r in avail.items():
            key = (size.get(c), bm.get(c, -1), mom.get(c, -1))
            cells.setdefault(key, []).append(r)
        means = {k: float(np.mean(v)) for k, v in cells.items()}
        return {c: means[(size.get(c), bm.get(c, -1), mom.get(c, -1))] for c in avail}


def _ew(cs, rets):
    v = [rets[c][0] for c in cs if c in rets]
    return (float(np.mean(v)), len(v)) if v else (None, 0)


def _vw(cs, rets, comp):
    pairs = [(rets[c][0], comp[c].get("mcap") or 0) for c in cs if c in rets and (comp.get(c) or {}).get("mcap")]
    w = sum(p[1] for p in pairs)
    return (sum(r * m for r, m in pairs) / w, len(pairs)) if w > 0 else (None, 0)


def picks(form, sid, which, shift="0", loo_gate=None):
    res = form["screens"].get(sid) or {}
    if which in ("P1", "P3"):
        base = [c for c, r in res.items() if r[0] == PASS]
    elif which == "P2":
        base = [c for c, r in res.items() if r[0] == PASS and not r[1]]
    else:
        base = [c for c, r in res.items() if r[0] == "NEAR"]
    if shift != "0":
        base = list((form.get("grid") or {}).get(sid, {}).get(shift, []))
    if loo_gate:
        base = sorted(set(base) | set((form.get("loo") or {}).get(sid, {}).get(loo_gate, [])))
    return base


def series(panel, sid, which="P1", shift="0", loo_gate=None, net=True):
    """Monthly portfolio returns, the screen's own-universe returns and diagnostics."""
    port, univ, ns, thin = [], [], [], 0
    prev = None
    for form, rets in panel.months:
        comp = form["companies"]
        uni = list((form["screens"].get(sid) or {}).keys())
        u_ew, _ = _ew(uni, rets)
        u_vw, _ = _vw(uni, rets, comp)
        cs = picks(form, sid, which, shift, loo_gate)
        held = [c for c in cs if c in rets]
        bench = u_vw if which == "P3" else u_ew
        if len(held) < MIN_NAMES:
            r, thin = bench, thin + 1
            held_set = None
        else:
            r = (_vw(held, rets, comp) if which == "P3" else _ew(held, rets))[0]
            held_set = set(held)
        if net and r is not None and held_set is not None:
            if prev is None:
                turnover = 1.0
            else:
                turnover = 1 - len(held_set & prev) / len(held_set)
            r -= 2 * COST_PER_SIDE * turnover if prev is not None else COST_PER_SIDE
        prev = held_set if held_set is not None else prev
        port.append(r)
        univ.append(bench)
        ns.append(len(held))
    return {"port": port, "univ": univ, "n": ns, "thin_months": thin}


def _excess(a, b):
    return [x - y if (x is not None and y is not None) else None for x, y in zip(a, b)]


def _alpha_halves(x, yms, factors, rf_adjust):
    h = len(x) // 2
    return [alpha(x[:h], yms[:h], factors, rf_adjust), alpha(x[h:], yms[h:], factors, rf_adjust)]


def baseline_series(panel, sid, kind):
    """Top-ranked names of the screen's universe by a published score, as many names as the screen holds that
    month (at least MIN_NAMES), equal-weighted, net of the same costs."""
    out, prev = [], None
    for form, rets in panel.months:
        comp = form["companies"]
        uni = [c for c in (form["screens"].get(sid) or {}) if c in rets]
        n = max(MIN_NAMES, len([c for c in picks(form, sid, "P1") if c in rets]))
        if kind == "magic":
            ey = {c: comp[c].get("ey") for c in uni if comp[c].get("ey") is not None and comp[c].get("roc") is not None}
            r1 = {c: i for i, c in enumerate(sorted(ey, key=lambda c: -ey[c]))}
            r2 = {c: i for i, c in enumerate(sorted(ey, key=lambda c: -comp[c]["roc"]))}
            ranked = sorted(ey, key=lambda c: r1[c] + r2[c])
        else:
            key = {"fscore": "fs", "grossprof": "gp"}[kind]
            ranked = sorted([c for c in uni if comp[c].get(key) is not None], key=lambda c: -comp[c][key])
        top = ranked[:n]
        if len(top) < MIN_NAMES:
            out.append(_ew(uni, rets)[0])
            continue
        r = _ew(top, rets)[0]
        cur = set(top)
        r -= COST_PER_SIDE if prev is None else 2 * COST_PER_SIDE * (1 - len(cur & prev) / len(cur))
        prev = cur
        out.append(r)
    return out


def ic_series(panel, sid):
    out = []
    for form, rets in panel.months:
        res = form["screens"].get(sid) or {}
        xs, ys = [], []
        for c, r in res.items():
            if c in rets and r[4]:
                xs.append(r[3] / r[4])
                ys.append(rets[c][0])
        out.append(spearman(np.array(xs), np.array(ys)) if len(xs) >= 10 else None)
    return out


def placebo_input(panel, sid):
    months = []
    for form, rets in panel.months:
        comp = form["companies"]
        uni = [c for c in (form["screens"].get(sid) or {}) if c in rets]
        cs = [c for c in picks(form, sid, "P1") if c in rets]
        if len(cs) < MIN_NAMES or not uni:
            continue
        size = terciles({c: comp[c].get("mcap") for c in uni})
        cell = {c: (size.get(c), sic_division(comp[c].get("sic"))) for c in uni}
        members = {}
        for c in uni:
            members.setdefault(cell[c], []).append(rets[c][0])
        members = {k: np.array(v, float) for k, v in members.items()}
        months.append(([rets[c][0] for c in cs], [cell[c] for c in cs], members,
                       float(np.mean([rets[c][0] for c in uni]))))
    return months


def red_flag_auc(panel, horizon=12):
    """AUC for a bad outcome within 12 months (cumulative return <= -50% at a month end, delistings included)."""
    rows = []
    n = len(panel.months)
    for i, (form, _rets) in enumerate(panel.months):
        if i + horizon > n:
            break
        res = form["screens"].get("red_flags") or {}
        comp = form["companies"]
        for c, r in res.items():
            cum, worst, seen = 1.0, 1.0, 0
            for j in range(i, i + horizon):
                rr = panel.months[j][1].get(c)
                if rr is None:
                    break
                cum *= 1 + rr[0]
                worst = min(worst, cum)
                seen += 1
            if seen == 0:
                continue
            bad = worst <= 0.5
            rows.append((r[0] == PASS, comp[c].get("rf"), comp[c].get("z2"), comp[c].get("ms"), bad))
    if not rows:
        return {}
    labels = [r[4] for r in rows]
    return {"n": len(rows), "bad_rate": sum(labels) / len(labels),
            "auc_flagged": auc([1.0 if r[0] else 0.0 for r in rows], labels),
            "auc_flag_count": auc([r[1] for r in rows], labels),
            "auc_altman_z2": auc([(-r[2]) if r[2] is not None else None for r in rows], labels),
            "auc_beneish_m": auc([r[3] for r in rows], labels)}


def analyse(panel, factors, n_trials_hint=None):
    """Everything in PROTOCOL sections 4-6, per screen."""
    yms = panel.yms
    out = {"months": len(yms), "first": yms[0] if yms else None, "last": yms[-1] if yms else None, "screens": {}}
    all_srs, d_matrix, sids = [], [], []
    per = {}
    for s in SCREENS:
        sid = s.sid
        st = {"lists": {}}
        base = series(panel, sid, "P1")
        for which in LISTS:
            ser = base if which == "P1" else series(panel, sid, which)
            ex = _excess(ser["port"], ser["univ"])
            st["lists"][which] = {"alpha": alpha(ser["port"], yms, factors), "ls_alpha": alpha(ex, yms, factors, False),
                                  "mean_excess": mean_t(ex), "thin_months": ser["thin_months"],
                                  "avg_names": float(np.mean(ser["n"])) if ser["n"] else 0}
            all_srs.append(sharpe(ex))
        ex1 = _excess(base["port"], base["univ"])
        st["halves"] = _alpha_halves(base["port"], yms, factors, True)
        cb = []
        for i, (form, rets) in enumerate(panel.months):
            cs = [c for c in picks(form, sid, "P1") if c in rets]
            if len(cs) < MIN_NAMES:
                cb.append(0.0)
                continue
            bench = panel.char_bench(i)
            cb.append(float(np.mean([rets[c][0] - bench[c] for c in cs if c in bench])))
        st["char_matched"] = mean_t(cb)
        grid_ex = []
        st["grid"] = {}
        for sh in GRID:
            ser = base if sh == "0" else series(panel, sid, "P1", shift=sh)
            e = _excess(ser["port"], ser["univ"])
            grid_ex.append([v if v is not None else 0.0 for v in e])
            st["grid"][sh] = alpha(ser["port"], yms, factors)
            all_srs.append(sharpe(e))
        st["pbo"] = pbo_cscv(np.array(grid_ex).T) if grid_ex and len(grid_ex[0]) else None
        st["loo"] = {}
        a0 = st["lists"]["P1"]["alpha"].get("alpha")
        for g in s.gates:
            ser = series(panel, sid, "P1", loo_gate=g.gid)
            a = alpha(ser["port"], yms, factors)
            st["loo"][g.gid] = {"alpha_without": a.get("alpha"),
                                "contribution": (a0 - a["alpha"]) if (a0 is not None and a.get("alpha") is not None)
                                else None}
        st["baselines"] = {}
        for kind in ("fscore", "magic", "grossprof"):
            b = baseline_series(panel, sid, kind)
            diff = _excess(base["port"], b)
            st["baselines"][kind] = {"alpha": alpha(b, yms, factors), "diff_alpha": alpha(diff, yms, factors, False)}
        st["ic"] = mean_t(ic_series(panel, sid))
        st["placebo_percentile"] = placebo_percentile(placebo_input(panel, sid))
        per[sid] = (st, ex1)
        d_matrix.append([v if v is not None else 0.0 for v in ex1])
        sids.append(sid)
    n_trials = n_trials_hint or len([x for x in all_srs if x is not None])
    for sid, (st, ex1) in per.items():
        st["dsr"] = deflated_sharpe(ex1, [x for x in all_srs if x is not None])
        st["n_trials"] = n_trials
        st["verdict"], st["why"] = verdict(sid, st, len(yms))
        out["screens"][sid] = st
    if d_matrix and len(d_matrix[0]) >= 24:
        out["reality_check"] = reality_check(np.array(d_matrix).T)
    out["red_flags_auc"] = red_flag_auc(panel)
    v = out["screens"].get("red_flags")
    if v is not None:
        v["verdict"], v["why"] = red_flag_verdict(v, out["red_flags_auc"], len(yms))
    return out


def verdict(sid, st, months):
    p1 = st["lists"]["P1"]
    a = p1["alpha"]
    if months < MIN_MONTHS or p1["thin_months"] > months / 2:
        return "too little history", f"{months} months, {p1['thin_months']} with fewer than {MIN_NAMES} names"
    t = a.get("t")
    if t is None:
        return "too little history", "alpha not estimable"
    halves = [h.get("alpha") for h in st["halves"]]
    same_sign = all(x is not None for x in halves) and (halves[0] > 0) == (halves[1] > 0) == (a["alpha"] > 0)
    plac = st.get("placebo_percentile")
    base_ok = all((b["diff_alpha"].get("t") or 0) >= 2 for b in st["baselines"].values())
    base_better = [k for k, b in st["baselines"].items() if (b["diff_alpha"].get("t") or 0) <= -2]
    why = f"alpha {a['alpha'] * 1200:.1f}%/yr, t {t:.2f}"
    if t <= -2:
        return "harmful", why
    if base_better:
        return "replace with baseline", why + f"; {', '.join(base_better)} did better (difference t <= -2)"
    if (t >= 3 and same_sign and (st.get("dsr") or 0) >= 0.95 and st.get("pbo") is not None and st["pbo"] <= 0.2
            and plac is not None and plac >= 0.95 and base_ok):
        return "edge", why
    if t >= 2 and plac is not None and plac >= 0.90:
        return "promising", why + "; not every 'edge' condition met"
    return "no evidence", why


def red_flag_verdict(st, aucs, months):
    a = st["lists"]["P1"]["alpha"]
    if months < MIN_MONTHS:
        return "too little history", f"{months} months"
    t = a.get("t")
    fa = aucs.get("auc_flagged")
    comp = [aucs.get("auc_altman_z2"), aucs.get("auc_beneish_m")]
    if t is not None and t <= -2 and fa is not None and fa >= 0.70 and all(fa > (c or 0) for c in comp):
        return "works", f"alpha t {t:.2f}, AUC {fa:.2f}"
    return "no evidence", f"alpha t {t if t is None else round(t, 2)}, AUC {fa if fa is None else round(fa, 2)}"
