"""Track record, factor regressions and per-cell evidence for each triage (shown on the site's Backtest and Track
record pages). Pure functions on the scored events, so every number can be recomputed from the published data.

  calls       one-year results per call (events with a full year): median, average (each return capped at +500%),
              the similar stocks' average, share that beat their similar stocks, up 20%+, down 50%+
  track       Buy candidates with a full year: average return month by month after buying, against their similar
              stocks and the index ETF over the same months
  years       $10,000 split equally over one year's Buy candidates, each held a year (or to the latest close)
  evidence    for every cell: one-year return minus the similar stocks' return, green vs red (all calls)
  regression  calendar-time portfolios: each month, the equal-weighted return of every event held that month (a call
              is held for the 12 months after its entry). Regressed on the Fama-French five factors and momentum
              (Kenneth French data library), Newey-West t-statistics. Buy candidates, Watch, Avoid, and Buy minus
              Avoid (long-short, no risk-free rate taken off).
"""
import math
import statistics as st
from collections import defaultdict

import numpy as np

from qs.btstats import FACTORS, ols_nw

from . import rules as R

CALLS = ("overdone", "close", "justified")
CAP = 500.0


def mean(v):
    v = [x for x in v if x is not None]
    return sum(v) / len(v) if v else None


def _r1(v):
    return None if v is None else round(v, 1)


def calls_table(items):
    out = {}
    for v in CALLS:
        g = [x for x in items if x.get("verdict") == v and x.get("played") and x.get("ret") is not None]
        if not g:
            continue
        a = [x["ret"] for x in g]
        c = [x["ctrl_ret"] for x in g if x.get("ctrl_ret") is not None]
        ix = [x["idx_ret"] for x in g if x.get("idx_ret") is not None]
        beat = [x["ret"] > x["ctrl_ret"] for x in g if x.get("ctrl_ret") is not None]
        out[v] = {"n": len(g), "median": _r1(st.median(a)), "mean": _r1(mean([min(x, CAP) for x in a])),
                  "ctrl_mean": _r1(mean(c)), "idx_mean": _r1(mean(ix)),
                  "beat": round(100 * sum(beat) / len(beat)) if beat else None,
                  "up20": round(100 * sum(x >= 20 for x in a) / len(a)), "down50": round(100 * sum(x <= -50 for x in a) / len(a))}
    return out


def avg_path(paths, carry=False):
    out, n = [], max((len(p) for p in paths), default=0)
    for k in range(n):
        v = [p[k] if len(p) > k else (p[-1] if carry and p else None) for p in paths]
        v = [min(x, CAP) for x in v if x is not None]
        if not v:
            break
        out.append(round(sum(v) / len(v), 2))
    return out


def track(items):
    buys = [x for x in items if x.get("verdict") == "overdone" and x.get("played") and x.get("path")
            and x.get("ctrl_path") and x.get("idx_path") and len(x["path"]) == 13]
    if not buys:
        return None
    return {"n": len(buys), "own": avg_path([x["path"] for x in buys]), "ctrl": avg_path([x["ctrl_path"] for x in buys]),
            "idx": avg_path([x["idx_path"] for x in buys])}


def years(items):
    out = {}
    buys = [x for x in items if x.get("verdict") == "overdone" and x.get("path")]
    for y in sorted({x["call_date"][:4] for x in buys}):
        g = [x for x in buys if x["call_date"][:4] == y]
        pth = {"own": avg_path([x["path"] for x in g], True),
               "ctrl": avg_path([x.get("ctrl_path") or [] for x in g if x.get("ctrl_path")], True),
               "idx": avg_path([x.get("idx_path") or [] for x in g if x.get("idx_path")], True)}
        fin = lambda k: round(10000 * (1 + pth[k][-1] / 100)) if pth[k] else None  # noqa: E731
        out[y] = {"n": len(g), "open": sum(1 for x in g if not x.get("played")), "own": fin("own"), "ctrl": fin("ctrl"),
                  "idx": fin("idx"), "path": pth}
    return out


def evidence(kind, items):
    """{cell: {'g': {...}, 'n': {...}, 'r': {...}}} - excess one-year return over the similar stocks."""
    done = [x for x in items if x.get("played") and x.get("ret") is not None and x.get("ctrl_ret") is not None
            and x.get("verdict") in CALLS]
    out = {}
    for k, label, w in R.KINDS[kind]["cells"]:
        row = {}
        for col in ("g", "n", "r"):
            ex = [x["ret"] - x["ctrl_ret"] for x in done
                  if (x["factors"].get(k) or ["n", "N/A"])[1] != "N/A" and x["factors"][k][0] == col]
            if ex:
                row[col] = {"n": len(ex), "median": _r1(st.median(ex)), "mean": _r1(mean([min(e, CAP) for e in ex])),
                            "beat": round(100 * sum(e > 0 for e in ex) / len(ex))}
        na = sum(1 for x in done if (x["factors"].get(k) or ["n", "N/A"])[1] == "N/A")
        out[k] = {"label": label, "weight": w, "cols": row, "na": na}
    return out


def portfolios(items, series):
    """{call: {YYYY-MM: monthly return}} - calendar-time portfolios of held events: equal-weighted each scan period
    (rebalanced twice a month), compounded to calendar months for the monthly factor data."""
    acc = {v: defaultdict(list) for v in CALLS}
    for x in items:
        v = x.get("verdict")
        if v not in CALLS:
            continue
        for per, r in (series.get(x["id"]) or {}).items():
            acc[v][per].append(r)
    out = {}
    for v, m in acc.items():
        mon = defaultdict(lambda: 1.0)
        for per, rs in sorted(m.items()):
            mon[per[:7]] *= 1 + sum(rs) / len(rs)
        out[v] = {ym: g - 1 for ym, g in sorted(mon.items())}
    return out


def regress(series, factors, rf=True):
    yms = [ym for ym in sorted(series) if ym in factors and all(factors[ym].get(k) is not None for k in FACTORS)]
    if len(yms) < 12:
        return {"n": len(yms), "alpha": None}
    y = [series[ym] - (factors[ym].get("RF", 0.0) if rf else 0.0) for ym in yms]
    X = np.array([[factors[ym][k] for k in FACTORS] for ym in yms])
    b, t, n = ols_nw(y, X)
    if b is None:
        return {"n": n, "alpha": None}
    yy = np.asarray(y)
    fit = np.column_stack([np.ones(len(yy)), X]) @ b
    ss_res, ss_tot = float(((yy - fit) ** 2).sum()), float(((yy - yy.mean()) ** 2).sum())
    return {"n": n, "first": yms[0], "last": yms[-1], "mean_m": round(float(np.mean(series_list(series, yms))) * 100, 2),
            "alpha_m": round(float(b[0]) * 100, 3), "alpha_y": round(((1 + float(b[0])) ** 12 - 1) * 100, 1),
            "t": round(float(t[0]), 2), "r2": round(1 - ss_res / ss_tot, 2) if ss_tot > 0 else None,
            "betas": {k: [round(float(bb), 2), round(float(tt), 1)] for k, bb, tt in zip(FACTORS, b[1:], t[1:])}}


def series_list(series, yms):
    return [series[ym] for ym in yms]


def regression(items, series, factors):
    if not factors:
        return None
    p = portfolios(items, series)
    out = {v: regress(p[v], factors) for v in CALLS if p[v]}
    ls = {ym: p["overdone"][ym] - p["justified"][ym] for ym in p["overdone"] if ym in p["justified"]}
    if ls:
        out["long_short"] = regress(ls, factors, rf=False)
    out["months_held"] = {v: len(p[v]) for v in CALLS}
    return out


def summary(kind, items, series, factors):
    return {"calls": calls_table(items), "track": track(items), "years": years(items),
            "evidence": evidence(kind, items), "regression": regression(items, series, factors)}


def finite(v):
    return v is not None and not (isinstance(v, float) and (math.isnan(v) or math.isinf(v)))
