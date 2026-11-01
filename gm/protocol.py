"""Adoption protocol runner (docs/research/global_macro/TESTING_PROTOCOL.md, pre-registered 2026-11-01).

python -m gm.protocol batch0|batch1|diag
Each challenger is compared with its incumbent on design months only (1975-01..2010-12). Results are appended to
gm/trials.csv and written to docs/research/global_macro/protocol_<batch>.md.
"""
import datetime as dt
import json
import os
import pickle
import sys

import numpy as np
import pandas as pd

from . import book as B
from . import config as CF
from . import panel as P
from . import stats as ST
from . import trials as TR
from . import variants as VA

DOC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "research", "global_macro")
ALPHA, MIN_DSR, NI_MARGIN, MAX_DD_WORSE, MIN_WINDOW, MIN_ERA = 0.05, 0.05, -0.10, 0.02, 120, 60
ERAS = (("1975-01", "1989-12"), ("1990-01", "2010-12"))
WIN = ("1975-01", "2010-12")


def load():
    R = pickle.load(open(os.path.join(P.OUT, "panel.pkl"), "rb"))["R"]
    S = pickle.load(open(os.path.join(P.OUT, "signals.pkl"), "rb"))
    D = pickle.load(open(os.path.join(P.OUT, "daily.pkl"), "rb"))
    return R, S, D


def book(cfg, R, S, D, cost_mult=1.0):
    return B.run(R, cost_mult=cost_mult, cfg=cfg, daily=D, S=S)


def compare(name, inc, cha, D):
    """inc/cha = (cfg, R, S). Returns the test record (p unadjusted)."""
    rb, rc = book(*inc, D), book(*cha, D)
    nb, nc = ST.cut(rb["net"], *WIN), ST.cut(rc["net"], *WIN)
    j = pd.concat([nb, nc], axis=1).dropna()
    rec = {"name": name, "window": "%s..%s" % (j.index[0], j.index[-1]) if len(j) else "-", "n": len(j)}
    if len(j) < MIN_WINDOW:
        rec.update(status="insufficient data", p=1.0)
        return rec, rc
    t = ST.paired_sr_test(j.iloc[:, 0], j.iloc[:, 1])
    rec.update(dsr=t["dsr"], p=t["p"], lb_pooled=t["lb95"], se=t.get("se", 0.0),
               sr_inc=ST.sharpe(j.iloc[:, 0]), sr_cha=ST.sharpe(j.iloc[:, 1]))
    eras = {}
    for a, b in ERAS:
        e = pd.concat([ST.cut(rb["net"], a, b), ST.cut(rc["net"], a, b)], axis=1).dropna()
        if len(e) < MIN_ERA:
            eras[a[:4]] = {"n": len(e), "pass": True, "note": "no data"}
            continue
        te = ST.paired_sr_test(e.iloc[:, 0], e.iloc[:, 1])
        eras[a[:4]] = {"n": len(e), "dsr": te["dsr"], "lb95": te["lb95"], "identical": te.get("identical", False),
                       "pass": bool(te.get("identical", False) or te["lb95"] > NI_MARGIN)}
    rec["eras"] = eras
    x2b, x2c = book(*inc, D, cost_mult=2.0), book(*cha, D, cost_mult=2.0)
    j2 = pd.concat([ST.cut(x2b["net"], *WIN), ST.cut(x2c["net"], *WIN)], axis=1).dropna()
    rec["dsr_2x"] = ST.sharpe(j2.iloc[:, 1]) - ST.sharpe(j2.iloc[:, 0])
    rec["dd_inc"], rec["dd_cha"] = ST.maxdd(j.iloc[:, 0]), ST.maxdd(j.iloc[:, 1])
    rec["wm_inc"], rec["wm_cha"] = float(j.iloc[:, 0].min()), float(j.iloc[:, 1].min())
    rec["alpha_t"] = ST.nw_alpha_t(j.iloc[:, 1] - j.iloc[:, 0], j.iloc[:, 0])
    rec["skew_inc"], rec["skew_cha"] = float(j.iloc[:, 0].skew()), float(j.iloc[:, 1].skew())
    return rec, rc


def decide(recs):
    adj = ST.holm({r["name"]: r.get("p", 1.0) for r in recs})
    for r in recs:
        r["p_holm"] = adj[r["name"]]
        if r.get("status") == "insufficient data":
            r["checks"], r["adopt"] = {}, False
            continue
        r["checks"] = {"1 superiority (Holm p<0.05)": r["p_holm"] < ALPHA,
                       "2 size (dSR>=0.05)": r["dsr"] >= MIN_DSR,
                       "3 non-inferior in each era": all(e["pass"] for e in r["eras"].values()),
                       "4 dSR>0 at 2x costs": r["dsr_2x"] > 0,
                       "5 tail: max fall not >2pt, worst month not >1pt worse":
                           r["dd_cha"] >= r["dd_inc"] - MAX_DD_WORSE and r["wm_cha"] >= r["wm_inc"] - 0.01}
        r["adopt"] = all(r["checks"].values())
    return recs


def log(recs, batch, cfgs):
    for r in recs:
        res_cfg = cfgs[r["name"]]
        TR.log_row({"when": dt.datetime.utcnow().strftime("%Y-%m-%d %H:%M"), "trial": "%s %s" % (batch, r["name"]),
                    "family": "book", "hash": CF.cfg_hash(res_cfg), "sr_9010": round(r.get("sr_cha", np.nan), 3),
                    "t_9010": "", "maxdd_9010": round(r.get("dd_cha", np.nan), 3), "sr_7589": "", "turnover": "",
                    "note": "protocol %s: dSR %+.3f p_holm %.3f adopt %s (window %s)" % (
                        batch, r.get("dsr", np.nan), r["p_holm"], r["adopt"], r["window"]),
                    "config": json.dumps(res_cfg, sort_keys=True, default=list)})


def write(recs, batch, extra=""):
    L = ["# Protocol results: %s (%s)" % (batch, dt.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")), "",
         "Rules: TESTING_PROTOCOL.md. Window = design months 1975-01..2010-12 where the challenger has data. "
         "Sharpe = annualised, net of costs. dSR = challenger minus incumbent.", "",
         "| Challenger | Window | SR inc | SR cha | dSR | boot SE | p | Holm p | dSR 2x cost | max fall inc / cha | "
         "1975-89 dSR (95% LB) | 1990-2010 dSR (95% LB) | alpha t | Adopt |", "|" + "---|" * 14]
    for r in recs:
        if r.get("status"):
            L.append("| %s | %s | | | | | | | | | | | | %s |" % (r["name"], r["window"], r["status"]))
            continue
        era = []
        for k in ("1975", "1990"):
            e = r["eras"][k]
            era.append("identical" if e.get("identical") else ("n/a" if "dsr" not in e else "%+.2f (%+.2f)" % (
                e["dsr"], e["lb95"])))
        L.append("| %s | %s | %.2f | %.2f | %+.3f | %.3f | %.4f | %.4f | %+.3f | %.1f%% / %.1f%% | %s | %s | %.1f | %s |" % (
            r["name"], r["window"], r["sr_inc"], r["sr_cha"], r["dsr"], r["se"], r["p"], r["p_holm"], r["dsr_2x"],
            r["dd_inc"] * 100, r["dd_cha"] * 100, era[0], era[1], r["alpha_t"], "YES" if r["adopt"] else "no"))
    L += ["", "Failed checks:"]
    for r in recs:
        bad = [k for k, v in r.get("checks", {}).items() if not v]
        L.append("- %s: %s" % (r["name"], ", ".join(bad) if bad else ("none" if r.get("checks") else r.get("status"))))
    if extra:
        L += ["", extra]
    os.makedirs(DOC, exist_ok=True)
    out = os.path.join(DOC, "protocol_%s.md" % batch)
    open(out, "w").write("\n".join(L) + "\n")
    print("\n".join(L))


def batch0():
    R, S, D = load()
    base, hyb = CF.BASE, CF.variant(CF.BASE, vol={"model": "hybrid"})
    cand = CF.CANDIDATE
    tests = {"B0.1 hybrid volatility": ((base, R, S), (hyb, R, S)),
             "B0.2 family shares 45/25/15/15": ((hyb, R, S), (cand, R, S))}
    recs, cfgs = [], {}
    for name, (inc, cha) in tests.items():
        rec, _ = compare(name, inc, cha, D)
        recs.append(rec)
        cfgs[name] = cha[0]
    recs = decide(recs)
    log(recs, "batch0", cfgs)
    write(recs, "batch0")


def batch1(incumbent=None):
    R, S, D = load()
    inc_cfg = incumbent or CF.CANDIDATE
    recs, cfgs = [], {}
    for name, fn in VA.BATCH1.items():
        try:
            cha = fn(inc_cfg, R, S)
            rec, _ = compare(name, (inc_cfg, R, S), cha, D)
            cfgs[name] = cha[0]
        except Exception as e:  # noqa: BLE001  (registered challenger that fails to build counts with p = 1)
            rec, cfgs[name] = {"name": name, "window": "-", "n": 0, "status": "build failed: %s" % e, "p": 1.0}, inc_cfg
        recs.append(rec)
        print(name, {k: v for k, v in rec.items() if k in ("dsr", "p", "n", "status")}, flush=True)
    recs = decide(recs)
    log(recs, "batch1", cfgs)
    write(recs, "batch1")


def diag():
    R, S, D = load()
    from .plumbing import aqr_tsmom
    res = book(CF.CANDIDATE, R, S, D)
    net = res["net"]
    L = ["# Diagnostics for the gm-2.0 candidate (design periods only)", ""]
    for a, b in ERAS:
        x = ST.cut(net, a, b)
        L.append("- %s..%s: SR %.2f, Lo-adjusted SR %.2f, skew %.2f, first-order autocorrelation %.2f" % (
            a[:4], b[:4], ST.sharpe(x), ST.lo_sharpe(x), x.skew(), x.autocorr(1)))
        neg = x[x < 0]
        L.append("  Sortino %.2f, worst month %.1f%%, compound growth %.1f%%/yr, rolling 36m vol min/median/max "
                 "%.1f/%.1f/%.1f%%" % (x.mean() / np.sqrt((neg ** 2).sum() / len(x)) * np.sqrt(12), x.min() * 100,
                                       ((1 + x).prod() ** (12 / len(x)) - 1) * 100,
                                       *(x.rolling(36).std().dropna().quantile([0, .5, 1]).values * np.sqrt(12) * 100)))
    pos = res["pos"]
    contrib = (pos.shift(1) * R).loc["1975-01":"2010-12"].sum().sort_values(ascending=False)
    L += ["", "Sharpe 1975-2010 (net) with a top-contributing market removed (positions zeroed, costs kept):"]
    full = ST.sharpe(ST.cut(net, *WIN))
    L.append("- full book: %.2f; without 2008: %.2f" % (full, ST.sharpe(ST.cut(net, *WIN).drop(
        [m for m in ST.cut(net, *WIN).index if m.year == 2008]))))
    for k in contrib.index[:5]:
        alt = net - (pos[k].shift(1) * R[k]).fillna(0)
        L.append("- without %s (contributed %.0f%% of capital in total): %.2f" % (k, contrib[k] * 100,
                                                                                 ST.sharpe(ST.cut(alt, *WIN))))
    bl = res["blocks"]
    tr = bl["trend"].mean(axis=1) if "trend" in bl.columns.get_level_values(0) else None
    aq = aqr_tsmom()
    col = [c for c in aq.columns if str(c).strip().upper() == "TSMOM"] or [aq.columns[0]]
    aqs = pd.to_numeric(aq[col[0]], errors="coerce")
    j = pd.concat([ST.cut(tr, "1990-01", "2010-12"), aqs], axis=1).dropna()
    L += ["", "Trend family (unit-vol blocks, equal class weight, gross) vs AQR TSMOM factor, 1990-2010 "
          "(%d months): our SR %.2f, AQR SR %.2f, correlation %.2f" % (
              len(j), ST.sharpe(j.iloc[:, 0]), ST.sharpe(j.iloc[:, 1]), j.corr().iloc[0, 1])]
    world = R[["eq_us_spx", "eq_eu_stoxx50", "eq_jp_nikkei", "eq_gb_ftse"]].mean(axis=1, skipna=True)
    for a, b in ERAS:
        L.append("- smile %s..%s (book return by world-equity quintile, %%/yr): %s" % (
            a[:4], b[:4], ST.smile(ST.cut(net, a, b), world)))
    L += ["", "1987 crash (Oct-Nov), gross contribution by family x class (percent of capital):"]
    fp = res["fam_pos"]
    for f, p in fp.items():
        c = (p.shift(1) * R).loc["1987-10":"1987-11"].sum()
        by = {cl: round(float(c[[k for k in c.index if k.startswith(pre)]].sum() * 100), 2)
              for cl, pre in {"EQ": "eq_", "FI": ("bd_", "st_"), "FX": "fx_", "CM": "cm_"}.items()}
        L.append("- %s: %s" % (f, by))
    out = os.path.join(DOC, "protocol_diagnostics.md")
    open(out, "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    {"batch0": batch0, "batch1": batch1, "diag": diag}[sys.argv[1] if len(sys.argv) > 1 else "diag"]()
