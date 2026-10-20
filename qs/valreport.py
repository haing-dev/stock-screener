"""validation/out/report.md - every verdict next to the numbers behind it (PROTOCOL section 6)."""
import json
import os

from .backtest_support import OUT
from .screens import BY_ID, SCREENS


def _load(name):
    try:
        with open(os.path.join(OUT, name), encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def _pct(x, d=1):
    return "-" if x is None else f"{x * 100:.{d}f}%"


def _num(x, d=2):
    return "-" if x is None else f"{x:.{d}f}"


def _a(a):
    if not a or a.get("alpha") is None:
        return "-"
    return f"{a['alpha'] * 1200:+.1f}% (t {a['t']:.1f})"


def screen_table(st):
    lines = ["| Screen | Verdict | Alpha P1, %/yr (t) | 1st half | 2nd half | DSR | PBO | Placebo pct | IC (t) | "
             "vs best baseline (t) | Avg names | Thin months |",
             "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for s in SCREENS:
        x = (st.get("screens") or {}).get(s.sid)
        if not x:
            continue
        p1 = x["lists"]["P1"]
        ic = x.get("ic") or (None, None)
        base = x.get("baselines") or {}
        bt = [(k, (b.get("diff_alpha") or {}).get("t")) for k, b in base.items()]
        bt = [b for b in bt if b[1] is not None]
        worst = min(bt, key=lambda b: b[1]) if bt else None
        lines.append(" | ".join([
            f"| {s.title}", f"**{x.get('verdict')}**", _a(p1["alpha"]), _a(x["halves"][0]), _a(x["halves"][1]),
            _num(x.get("dsr")), _num(x.get("pbo")), _num(x.get("placebo_percentile")),
            "-" if ic[0] is None else f"{ic[0]:.3f} ({ic[1]:.1f})",
            "-" if not worst else f"{worst[0]} {worst[1]:+.1f}", f"{p1['avg_names']:.0f}", f"{p1['thin_months']} |"]))
    return "\n".join(lines)


def write_report(cfg):
    st = _load("stats.json") or {}
    audit = _load("audit_summary.json")
    fid = _load("fidelity.json")
    L = ["# Validation report", "",
         f"Pre-registration check: **{st.get('preregistration', 'not run')}** (validation/freeze.json). Backtest months: "
         f"{st.get('months', 0)} ({st.get('first')} .. {st.get('last')}). Verdicts are mechanical "
         "(validation/PROTOCOL.md section 6); 'too little history' means no statistical claim either way.", "",
         "## Backtest (point in time)", "", screen_table(st) if st else "No statistics yet.", ""]
    rc = st.get("reality_check") or {}
    L += [f"Across all 14 screens (P1 minus own universe): White's Reality Check p = {_num(rc.get('rc_p'), 3)}, "
          f"Hansen's SPA p = {_num(rc.get('spa_p'), 3)} (small = at least one screen beats its universe after "
          "accounting for testing 14).", ""]
    rf = st.get("red_flags_auc") or {}
    if rf:
        L += ["## Red Flags", "",
              f"Bad outcome (-50% within 12 months) in {_pct(rf.get('bad_rate'))} of {rf.get('n')} company-months. "
              f"AUC: flagged {_num(rf.get('auc_flagged'))}, number of flags {_num(rf.get('auc_flag_count'))}, "
              f"Altman Z'' {_num(rf.get('auc_altman_z2'))}, Beneish M {_num(rf.get('auc_beneish_m'))}.", ""]
    L += ["## Robustness", "", "Alpha of P1 (%/yr) with every numeric threshold moved (negative = looser):", "",
          "| Screen | -30% | -20% | -10% | frozen | +10% | +20% | +30% | Gate that adds most | Gate that costs most |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for s in SCREENS:
        x = (st.get("screens") or {}).get(s.sid)
        if not x:
            continue
        g = x.get("grid") or {}
        cells = [("-" if not g.get(k) or g[k].get("alpha") is None else f"{g[k]['alpha'] * 1200:+.1f}")
                 for k in ("-0.3", "-0.2", "-0.1", "0", "0.1", "0.2", "0.3")]
        loo = [(k, v.get("contribution")) for k, v in (x.get("loo") or {}).items() if v.get("contribution") is not None]
        best = max(loo, key=lambda z: z[1]) if loo else None
        worst = min(loo, key=lambda z: z[1]) if loo else None
        L.append(f"| {s.title} | " + " | ".join(cells) +
                 f" | {best[0] + f' {best[1] * 1200:+.1f}' if best else '-'} | "
                 f"{worst[0] + f' {worst[1] * 1200:+.1f}' if worst else '-'} |")
    L += ["", "A gate's contribution = P1 alpha minus the alpha with that gate removed (positive = the gate helps).", ""]
    jac = st.get("live_vs_reconstruction_jaccard") or {}
    fw = st.get("forward")
    L += ["## Forward record (after pre-registration)", ""]
    if fw:
        L += [f"{fw.get('months')} months of live lists.", "", screen_table(fw), ""]
    else:
        L += ["No live lists recorded yet (branch 'history').", ""]
    if jac:
        L += ["Agreement of the live PASS lists with the point-in-time reconstruction (average Jaccard): " +
              ", ".join(f"{BY_ID[k].title} {_num(v)}" for k, v in jac.items() if k in BY_ID), ""]
    L += ["## Independent checks", ""]
    if audit:
        L += [f"- Data reconciliation ({audit.get('formation')}): {audit.get('within_2pct')} of {audit.get('compared')} "
              f"values within 2% of SEC's Financial Statement Data Sets ({_pct(audit.get('share_within_2pct'))}; "
              "pass >= 95%). Human recheck: audit_reconciliation.csv and audit_gates.csv.",
              "- Star audit: audit_stars.csv (50 starred passes) awaits a reviewer (pass >= 90%)."]
    else:
        L += ["- Data reconciliation: not run yet."]
    if fid:
        ok = [(m["who"], sid, v) for m in fid["managers"] for sid, v in m["screens"].items() if v["rate"] is not None]
        L += [f"- Style fidelity (13F {fid.get('period')}, formation {fid.get('formation')}): "
              f"{sum(1 for _w, _s, v in ok if v['passes'])} of {len(ok)} manager-screen pairs at >= 3x the universe "
              "rate.", "", "| Manager | Screen | Holdings in universe | PASS or NEAR | Rate | Universe rate | Ratio |",
              "| --- | --- | --- | --- | --- | --- | --- |"]
        for who, sid, v in ok:
            L.append(f"| {who} | {BY_ID[sid].title} | {v['holdings_in_universe']} | {v['pass_or_near']} | "
                     f"{_pct(v['rate'])} | {_pct(v['universe_rate'])} | {_num(v['ratio'], 1)} |")
    else:
        L += ["- Style fidelity: not run yet."]
    L += ["- Re-implementation by an independent agent: see validation/reimplementation.md.", "",
          "## Caveats", "",
          "- Point-in-time SEC data starts with XBRL (2009-11); rules needing 8-10 years of history pass only later.",
          "- Fixed calendar windows (2021-23 margin change, 2009/2020 recession tests) are missing data before those "
          "years; FX uses static rates; 13F and insider data play no part in the rules.",
          "- Exits without a next-month price use Massive's last daily close when looked up, else -30% (Shumway).",
          "- Returns run open to open between the first trading days of consecutive months, matched to calendar-month "
          "factors."]
    path = os.path.join(OUT, "report.md")
    os.makedirs(OUT, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    return path
