"""eq_prof (runs on WRDS Cloud): construction profile of the roster and control investors (plan v0.5 section 5;
V04_REGISTRATION.md addendum A10 item 12; used by item 5 a, b, d). Seal-exempt descriptive job (tools/equity/seal_exempt.json
`construction_profile`, SEAL_LOG.md). It reads ONLY the stored conviction panel `eq_conv_panel` (per manager, quarter
and stock: weight, weight rank, new / addition flags). No price, no return, no company name is read or printed.

Per investor (all 13F filers of the investor pooled), from 13F quarter-ends 2009-12 .. 2025-12:
- how many names: positions, positions of at least 1% of the portfolio, effective number of names (1 / sum of squared
  weights); medians over quarters
- how concentrated: largest weight, weight of the 5 and of the 10 largest; medians over quarters
- how a position starts: weight of a new position in its first quarter (median, positions that reach 1% at some time)
- how long positions are held: holding spells of positions that reach 1% at some time and whose entry was observed;
  Kaplan-Meier median in quarters (a spell still open at the last filing is counted as "at least that long") and the
  share still held after 1, 3 and 5 years
- how much is new: weight of new positions per quarter, times four (share of the portfolio that is new each year)
- how they buy: additions as a share of all buys (new positions + additions)
Limits: 13F shows US-listed long positions at quarter-ends only; a firm with several funds files one portfolio.

Job names: eq_prof_v<n>: run(load, save, out)
1.0.0 (2026-11-22): first version.
"""
import json

import numpy as np
import pandas as pd

# >>> FROZEN INPUT
MGR = json.loads("[{\"name\": \"Joel Greenblatt\", \"group\": \"roster\", \"mgrnos\": [\"10969\", \"12775\"]}, {\"name\": \"Terry Smith\", \"group\": \"roster\", \"mgrnos\": [\"13408\"]}, {\"name\": \"Dev Kantesaria\", \"group\": \"roster\", \"mgrnos\": [\"14460\"]}, {\"name\": \"Chris Hohn\", \"group\": \"roster\", \"mgrnos\": [\"11194\"]}, {\"name\": \"Glenn Greenberg\", \"group\": \"roster\", \"mgrnos\": [\"16080\"]}, {\"name\": \"Val Zlatev\", \"group\": \"roster\", \"mgrnos\": [\"7142\"]}, {\"name\": \"Derek Pilecki\", \"group\": \"roster\", \"mgrnos\": [\"8799\"]}, {\"name\": \"Bill Nygren and Alex Fitch\", \"group\": \"roster\", \"mgrnos\": [\"43485\"]}, {\"name\": \"Murray Stahl\", \"group\": \"roster\", \"mgrnos\": [\"44850\", \"49373\"]}, {\"name\": \"Pat Dorsey\", \"group\": \"roster\", \"mgrnos\": [\"14201\"]}, {\"name\": \"Chris Davis\", \"group\": \"roster\", \"mgrnos\": [\"78320\"]}, {\"name\": \"Joseph Shaposhnik\", \"group\": \"roster\", \"mgrnos\": []}, {\"name\": \"Alex Sacerdote\", \"group\": \"roster\", \"mgrnos\": [\"11405\"]}, {\"name\": \"David Einhorn\", \"group\": \"roster\", \"mgrnos\": [\"42315\"]}, {\"name\": \"Stan Druckenmiller\", \"group\": \"roster\", \"mgrnos\": [\"13021\", \"23704\"]}, {\"name\": \"Todd Kantor\", \"group\": \"roster\", \"mgrnos\": [\"13431\"]}, {\"name\": \"Bob Robotti\", \"group\": \"roster\", \"mgrnos\": [\"10247\"]}, {\"name\": \"Fred Martin\", \"group\": \"roster\", \"mgrnos\": [\"23050\"]}, {\"name\": \"Brad Gerstner\", \"group\": \"roster\", \"mgrnos\": [\"13112\"]}, {\"name\": \"Chris Bloomstran\", \"group\": \"roster\", \"mgrnos\": [\"11757\"]}, {\"name\": \"Li Lu\", \"group\": \"roster\", \"mgrnos\": [\"14546\"]}, {\"name\": \"Warren Buffett\", \"group\": \"control\", \"mgrnos\": [\"8350\"]}, {\"name\": \"Henry Ellenbogen\", \"group\": \"control\", \"mgrnos\": [\"9442\"]}, {\"name\": \"Jim Chanos\", \"group\": \"control\", \"mgrnos\": [\"12867\"]}, {\"name\": \"John Lennon\", \"group\": \"control\", \"mgrnos\": [\"9090\"]}, {\"name\": \"Peter Keefe\", \"group\": \"control\", \"mgrnos\": [\"5300\"]}, {\"name\": \"Tobias Carlisle\", \"group\": \"control\", \"mgrnos\": []}, {\"name\": \"Arnold Van Den Berg\", \"group\": \"control\", \"mgrnos\": [\"15095\"]}, {\"name\": \"Eddy Elfenbein\", \"group\": \"control\", \"mgrnos\": []}]")
# <<< FROZEN INPUT

VERSION = "eq_prof-1.0.0"
BIG = 0.01          # a position "that matters": at least 1% of the portfolio at some quarter-end


def flag(s):
    return s.astype(str).str.lower().isin(["true", "1", "1.0"])


def km(dur, event):
    """Kaplan-Meier: returns (median duration or None if not reached, function S(t) = share lasting more than t)"""
    dur, event = np.asarray(dur, float), np.asarray(event, bool)
    ts = np.sort(np.unique(dur[event]))
    s, steps = 1.0, []
    for t in ts:
        at_risk = (dur >= t).sum()
        if at_risk > 0:
            s *= 1 - ((dur == t) & event).sum() / at_risk
        steps.append((t, s))
    med = next((t for t, v in steps if v <= 0.5), None)

    def surv(t):
        v = 1.0
        for a, b in steps:
            if a <= t:
                v = b
        return v
    return med, surv


def profile(d):
    """d: panel rows of one investor (one or more filers). Returns a dict of aggregates."""
    d = d.sort_values(["mgrno", "yyyymm"]).copy()
    cal = {m: {q: i for i, q in enumerate(sorted(x.yyyymm.unique()))} for m, x in d.groupby("mgrno")}
    d["qi"] = [cal[m][q] for m, q in zip(d.mgrno, d.yyyymm)]
    last = d.groupby("mgrno").qi.transform("max")
    g = d.groupby(["mgrno", "yyyymm"])
    names = g.size()
    names_big = g.w.apply(lambda w: int((w >= BIG).sum()))
    eff = g.w.apply(lambda w: 1.0 / float((w ** 2).sum()))
    top1 = g.w.max()
    top5 = g.w.apply(lambda w: float(w.nlargest(5).sum()))
    top10 = g.w.apply(lambda w: float(w.nlargest(10).sum()))
    # holding spells: consecutive quarter-ends in the filer's own calendar
    d = d.sort_values(["mgrno", "permno", "qi"])
    brk = (d.groupby(["mgrno", "permno"]).qi.diff() != 1).astype(int)
    d["spell"] = brk.groupby([d.mgrno, d.permno]).cumsum()
    d["last_qi"] = last
    sp = d.groupby(["mgrno", "permno", "spell"]).agg(start=("qi", "min"), end=("qi", "max"), n=("qi", "size"),
                                                     wmax=("w", "max"), w0=("w", "first"), last_qi=("last_qi", "first"))
    sp = sp[(sp.start > 0) & (sp.wmax >= BIG)]                  # entry observed, position that matters
    exited = sp.end < sp.last_qi
    med, surv = km(sp.n.to_numpy(), exited.to_numpy()) if len(sp) else (None, lambda t: float("nan"))
    newq = d[d.qi > 0].assign(nw=lambda x: x.w.where(flag(x.new), 0.0)).groupby(["mgrno", "yyyymm"]).nw.sum()
    n_new, n_add = int(flag(d.new).sum()), int(flag(d["add"]).sum())
    return dict(filers=d.mgrno.nunique(), quarters=int(g.ngroups), names=float(names.median()), names_big=float(names_big.median()),
                eff_names=float(eff.median()), top1=float(top1.median()), top5=float(top5.median()), top10=float(top10.median()),
                top1_p90=float(top1.quantile(0.9)), spells=int(len(sp)), spells_open=int((~exited).sum()),
                start_w=float(sp.w0.median()) if len(sp) else float("nan"),
                hold_med=med, held_1y=surv(4), held_3y=surv(12), held_5y=surv(20),
                new_per_year=float(newq.mean() * 4) if len(newq) else float("nan"),
                add_share=n_add / (n_new + n_add) if n_new + n_add else float("nan"))


def run(load, save, out):
    out("%s  construction profile (descriptive; V04_REGISTRATION A10 item 12)" % VERSION)
    p = load("eq_conv_panel")
    p["w"] = pd.to_numeric(p.w, errors="coerce")
    p = p.dropna(subset=["w"])
    out("panel rows %d; filers %d; quarters %d .. %d" % (len(p), p.mgrno.nunique(), int(p.yyyymm.min()), int(p.yyyymm.max())))
    out("columns: investor | group | filers | filer-quarters | names | names >= 1% | effective names | largest weight % | "
        "top-5 % | top-10 % | largest weight 90th pct % | new position starts at % | spells (still open) | "
        "median holding in quarters | still held after 1y / 3y / 5y % | new per year % | additions share of buys %")
    rows = []
    for r in MGR:
        ids = [int(x) for x in r["mgrnos"]]
        d = p[p.mgrno.isin(ids)]
        if not len(d):
            out("%s | %s | no 13F" % (r["name"], r["group"]))
            continue
        a = profile(d)
        hm = "not reached (> %d)" % int(d.groupby("mgrno").yyyymm.nunique().max() - 1) if a["hold_med"] is None else "%d" % a["hold_med"]
        out("%s | %s | %d | %d | %.0f | %.0f | %.1f | %.0f | %.0f | %.0f | %.0f | %.1f | %d (%d) | %s | %.0f / %.0f / %.0f | %.0f | %.0f" % (
            r["name"], r["group"], a["filers"], a["quarters"], a["names"], a["names_big"], a["eff_names"], 100 * a["top1"],
            100 * a["top5"], 100 * a["top10"], 100 * a["top1_p90"], 100 * a["start_w"], a["spells"], a["spells_open"], hm,
            100 * a["held_1y"], 100 * a["held_3y"], 100 * a["held_5y"], 100 * a["new_per_year"], 100 * a["add_share"]))
        rows.append(dict(name=r["name"], group=r["group"], **{k: (v if v is not None else -1) for k, v in a.items()}))
    save("eq_prof_table", pd.DataFrame(rows))
    out("table stored on WRDS: eq_prof_table. ALL DONE")
