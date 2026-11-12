"""Forecast ledger step 2.3 (script): scorecard from outcomes.csv, as fixed in SCORING_RULES.md v1 sections 4-6.
Forecast-scoring statistics only: no book, pod or backtest returns, no table of market returns.

usage: python3 tools/fcast/scorecard.py <macro-vault worktree> [YYYY-MM-DD]
  -> docs/research/forecasts/SCORECARD_<date>.md and <vault>/pipeline/forecasts/SCORECARD_<date>.md"""
import collections, csv, datetime as dt, json, math, os, re, sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
DOCS = os.path.join(REPO, "docs", "research", "forecasts")
MIN_N, MIN_MONTHS, MIN_SPEAKER, MIN_CAL = 20, 6, 15, 20
DRAWS, BLOCK, SEED = 2000, 12, 20261112


def boot_ci(months, values, draws=DRAWS, block=BLOCK, seed=SEED):
    """Circular block bootstrap over calendar months (rows of one month move together), 90% percentile interval."""
    if not len(values):
        return float("nan"), float("nan")
    per = pd.PeriodIndex(months, freq="M")
    allm = pd.period_range(per.min(), per.max(), freq="M")
    K = len(allm)
    if K <= block:              # one circular block covers the whole cell: no spread, no interval (rule gap 27)
        return float("nan"), float("nan")
    pos = np.array([(p.year - allm[0].year) * 12 + p.month - allm[0].month for p in per])
    sums, cnts = np.zeros(K), np.zeros(K)
    np.add.at(sums, pos, np.asarray(values, float))
    np.add.at(cnts, pos, 1.0)
    rng = np.random.default_rng(seed)
    nb = int(math.ceil(K / block))
    stats = []
    for _ in range(draws):
        st = rng.integers(0, K, size=nb)
        idx = ((st[:, None] + np.arange(block)[None, :]) % K).ravel()[:K]
        c = cnts[idx].sum()
        if c > 0:
            stats.append(sums[idx].sum() / c)
    return float(np.percentile(stats, 5)), float(np.percentile(stats, 95))


def fnum(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def fbool(x):
    return {"True": 1.0, "False": 0.0, True: 1.0, False: 0.0}.get(x)


def bmonth(r):
    sd, mr = r.get("start_date") or "", r.get("made_r") or ""
    if len(sd) == 10 and sd > mr:
        return sd[:7]
    return (pd.Timestamp(mr) + pd.Timedelta(days=1)).strftime("%Y-%m")


def hbucket(h):
    h = float(h)
    return "<=3m" if h <= 3 else ">3-12m" if h <= 12 else ">12-36m" if h <= 36 else ">36-60m"


def verdict(lo, hi):
    if lo != lo:
        return "no interval"
    return "above" if lo > 0 else "below" if hi < 0 else "not distinguishable"


def pct(x):
    return "" if x is None or x != x else "%.0f%%" % (100 * x)


def pp(x):
    return "" if x is None or x != x else "%+.0f pp" % (100 * x)


def ci_pp(lo, hi, f=pp):
    return "" if lo != lo else "[%s, %s]" % (f(lo), f(hi))


HDR = ("| Cell | n resolved | n open | start months | hit rate [90%] | sign-only hit | hit - base rate [90%] (n) | vs base |"
       " hit - trend [90%] (n) | vs trend | agrees with trend | move (band units) | Brier skill (n) |")
SEP = "|" + "---|" * 13


def cell(label, res, n_open, top_source=True):
    n = len(res)
    months = [bmonth(r) for r in res]
    nm = len(set(months))
    if n < MIN_N or nm < MIN_MONTHS:
        return ["| %s | too few (%d) | %d | %d |%s" % (label, n, n_open, nm, " |" * 10)]
    hit = [fbool(r["hit"]) for r in res]
    lo, hi = boot_ci(months, hit)
    sg = [fbool(r["sign_hit"]) for r in res if fbool(r.get("sign_hit")) is not None]
    bp = [(m, fbool(r["hit"]) - fnum(r["base_p"])) for m, r in zip(months, res) if fnum(r.get("base_p")) is not None]
    tp = [(m, fbool(r["hit"]) - fbool(r["trend_hit"])) for m, r in zip(months, res) if fbool(r.get("trend_hit")) is not None]
    ag = [fbool(r["agree_trend"]) for r in res if fbool(r.get("agree_trend")) is not None]
    mv = [fnum(r["move_band"]) for r in res if fnum(r.get("move_band")) is not None]
    br = [(m, fnum(r["probability"]), fnum(r["base_p"]), fbool(r["hit"])) for m, r in zip(months, res)
          if fnum(r.get("probability")) is not None and fnum(r.get("base_p")) is not None]
    out = []

    def mean_ci(pairs):
        if len(pairs) < MIN_N or len({m for m, _ in pairs}) < MIN_MONTHS:
            return "too few (%d)" % len(pairs), ""
        v = [x for _, x in pairs]
        l, h = boot_ci([m for m, _ in pairs], v)
        return "%s %s (%d)" % (pp(float(np.mean(v))), ci_pp(l, h), len(v)), verdict(l, h)

    bs, bv = mean_ci(bp)
    ts, tv = mean_ci(tp)
    if len(br) >= MIN_N:
        bf = np.mean([(q - y) ** 2 for _, q, _, y in br])
        bb = np.mean([(p - y) ** 2 for _, _, p, y in br])
        bl, bh = boot_ci([m for m, *_ in br], [(p - y) ** 2 - (q - y) ** 2 for _, q, p, y in br])
        bstr = "%.2f [%+.3f, %+.3f] (%d)" % (1 - bf / bb if bb > 0 else float("nan"), bl, bh, len(br))
    else:
        bstr = "too few (%d)" % len(br)
    out.append("| %s | %d | %d | %d | %s %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
        label, n, n_open, nm, pct(np.mean(hit)), ci_pp(lo, hi, pct), pct(np.mean(sg)) if sg else "", bs, bv, ts, tv,
        pct(np.mean(ag)) if ag else "", "%+.2f" % np.mean(mv) if mv else "", bstr))
    if top_source:
        src = collections.Counter(r["source_id"] for r in res)
        s, k = src.most_common(1)[0]
        if k / n > 0.20:
            out += cell("%s, without %s (%d%% of cell)" % (label, s, round(100 * k / n)),
                        [r for r in res if r["source_id"] != s], n_open, top_source=False)
    return out


def table(title, groups, note=""):
    L = ["", "### " + title, ""] + ([note, ""] if note else []) + [HDR, SEP]
    for label, (res, n_open) in groups:
        L += cell(label, res, n_open)
    return L


def split(rows, key):
    d = collections.OrderedDict()
    for r in sorted(rows, key=key):
        d.setdefault(key(r), []).append(r)
    return d


def main():
    vault = sys.argv[1]
    day = sys.argv[2] if len(sys.argv) > 2 else dt.date.today().isoformat()
    F = os.path.join(vault, "pipeline", "forecasts")
    rows = list(csv.DictReader(open(os.path.join(F, "outcomes.csv"))))
    stamp = rows[0].get("cache_fetched", "") if rows else ""
    rules = rows[0].get("rules", "") if rows else ""
    res = [r for r in rows if r["status"] == "resolved"]
    opn = [r for r in rows if r["status"] == "open"]
    L = ["# Forecast ledger scorecard (%s)" % day, "",
         "Rules: %s (docs/research/forecasts/SCORING_RULES.md). Scorer: tools/fcast/score.py, scorecard.py. Cache "
         "`fetched` stamps: %s. Descriptive only: never used for weights, pod selection or design." % (rules, stamp),
         "Outcome data dated 2011+ are used here solely to resolve these recorded forecasts (and each forecast's own "
         "trend baseline); base rates use 1990-2010 only. Nothing here is a return of the book, a pod or a backtest, "
         "and no market return is shown as such.", ""]
    L += ["## What this does and does not show", "",
          "It shows how often the dated views in the ledger came true under fixed mechanical rules, and whether that "
          "beats two naive forecasters: calling the direction at its 1990-2010 base rate, and extending the last 12 "
          "months. It does not show that any investor has skill: the views were selected by interviewers and by the "
          "argument maps, coded by one model (agreement below), mostly made in 2024-26 and still largely open, and "
          "they overlap heavily in time, so the resolved rows reflect few independent market episodes. Rows the coder "
          "marked not resolvable, not_forecast, year-dated or on variables without a free series are counted, not "
          "scored. Nothing here is an input to any pod, weight or selection.", ""]
    # funnel
    st = collections.Counter(r["status"] for r in rows)
    scorable = st["resolved"] + st["open"]
    L += ["## Funnel", "",
          "Ledger rows %d. Scorable (pass the mechanical tests: pool, date, horizon, series, direction) %d = resolved %d "
          "+ open %d. Unscorable %d (not pooled %d, excluded %d, duplicates %d, unscored %d)." % (
              len(rows), scorable, st["resolved"], st["open"], len(rows) - scorable, st["not pooled"], st["excluded"],
              st["duplicate"], st["unscored"]), "",
          "| Pool | rows | excluded | duplicate | unscored | open | resolved |", "|---|---|---|---|---|---|---|"]
    names = {"A": "A headline (forecast, coder yes)", "B": "B (forecast, coder partly)", "C": "C stance",
             "D": "D conditional (condition ignored)", "E": "E structural", "": "not pooled"}
    for p in ["A", "B", "C", "D", "E", ""]:
        rr = [r for r in rows if r["pool"] == p]
        c = collections.Counter(r["status"] for r in rr)
        L.append("| %s | %d | %d | %d | %d | %d | %d |" % (names[p], len(rr), c["excluded"], c["duplicate"],
                                                          c["unscored"], c["open"], c["resolved"]))
    L += ["", "Reasons (rows not resolved and not open):", "", "| Status | Reason | rows |", "|---|---|---|"]
    rc = collections.Counter((r["status"], re.sub(r"\(.*\)$", "", r["reason"]).strip() if r["status"] == "unscored"
                              and r["reason"].startswith("no free series") else r["reason"])
                             for r in rows if r["status"] not in ("resolved", "open"))
    for (s, why), k in sorted(rc.items(), key=lambda x: -x[1]):
        L.append("| %s | %s | %d |" % (s, why, k))
    L += ["", "By variable code (pooled rows only):", "",
          "| Code | pooled | resolved | open | unscored | excluded | duplicate | main unscored reason |", "|---|---|---|---|---|---|---|---|"]
    pooled = [r for r in rows if r["pool"]]
    for code, rr in sorted(split(pooled, lambda r: r["variable_code"]).items(), key=lambda x: -len(x[1])):
        c = collections.Counter(r["status"] for r in rr)
        why = collections.Counter(r["reason"] for r in rr if r["status"] == "unscored").most_common(1)
        L.append("| %s | %d | %d | %d | %d | %d | %d | %s |" % (code, len(rr), c["resolved"], c["open"], c["unscored"],
                                                                c["excluded"], c["duplicate"], why[0][0] if why else ""))
    # headline pools
    def grp(sel):
        return ([r for r in res if sel(r)], sum(1 for r in opn if sel(r)))
    L += ["", "## Hit rates and baselines", "",
          "Cells need >= %d resolved rows from >= %d start months; intervals: circular block bootstrap over start "
          "months, blocks of 12, 2,000 draws, seed 20261112, 90%%. 'vs base' / 'vs trend': above = interval above 0. "
          "Move = change in the stated direction divided by the dead band (flat calls and events excluded)." % (MIN_N, MIN_MONTHS)]
    L += table("Pools (coder resolvable yes = A, partly = B; stated vs default horizon)", [
        ("A (coder yes, stated horizon)", grp(lambda r: r["pool"] == "A")),
        ("B, stated horizon (coder partly)", grp(lambda r: r["pool"] == "B" and r["h_source"] == "stated")),
        ("B, default horizon (coder partly)", grp(lambda r: r["pool"] == "B" and r["h_source"] == "default")),
        ("A+B", grp(lambda r: r["pool"] in ("A", "B"))),
        ("A+B stated horizon", grp(lambda r: r["pool"] in ("A", "B") and r["h_source"] == "stated")),
        ("A+B default horizon", grp(lambda r: r["pool"] in ("A", "B") and r["h_source"] == "default")),
        ("C stance", grp(lambda r: r["pool"] == "C")),
        ("C stance, coder yes", grp(lambda r: r["pool"] == "C" and r["resolvable"] == "yes")),
        ("C stance, coder partly", grp(lambda r: r["pool"] == "C" and r["resolvable"] == "partly")),
        ("D conditional (condition ignored)", grp(lambda r: r["pool"] == "D")),
        ("E structural", grp(lambda r: r["pool"] == "E"))])
    for name, sel in (("pool A (headline)", lambda r: r["pool"] == "A"),
                      ("pools A+B (A and B together; extra view, not a rules-v1 headline)", lambda r: r["pool"] in ("A", "B"))):
        sub_r = [r for r in res if sel(r)]
        sub_o = [r for r in opn if sel(r)]
        for dim, key in (("call type", lambda r: r["call_type"]), ("variable family", lambda r: r["group"]),
                         ("horizon bucket", lambda r: hbucket(r["h"])), ("year made", lambda r: r["made_r"][:4])):
            ks = sorted({key(r) for r in sub_r + sub_o})
            L += table("By %s, %s" % (dim, name), [(k, ([r for r in sub_r if key(r) == k],
                                                         sum(1 for r in sub_o if key(r) == k))) for k in ks])
    # calibration
    pr = [r for r in res if fnum(r.get("probability")) is not None]
    L += ["", "## Stated probabilities", "", "Resolved rows with a stated probability: %d (all pools). Brier skill is in "
          "the tables above (shown at n >= %d). Calibration buckets (shown at n >= %d):" % (len(pr), MIN_N, MIN_CAL), "",
          "| Bucket | n | mean stated | hit rate |", "|---|---|---|---|"]
    for lo in (0, 0.2, 0.4, 0.6, 0.8):
        b = [r for r in pr if lo <= fnum(r["probability"]) < lo + 0.2 or (lo == 0.8 and fnum(r["probability"]) == 1.0)]
        L.append("| %.1f-%.1f | %s | %s | %s |" % (lo, lo + 0.2, len(b) if len(b) >= MIN_CAL else "too few (%d)" % len(b),
                                                     pct(np.mean([fnum(r["probability"]) for r in b])) if len(b) >= MIN_CAL else "",
                                                     pct(np.mean([fbool(r["hit"]) for r in b])) if len(b) >= MIN_CAL else ""))
    # per speaker
    ab = [r for r in res if r["pool"] in ("A", "B")]
    sp = split(ab, lambda r: r["who"])
    L += ["", "## Per speaker (pools A+B)", "",
          "**Descriptive only; not a skill estimate; never used for weights or selection.** Speakers with >= %d "
          "resolved rows, alphabetical, no intervals." % MIN_SPEAKER, "",
          "| Speaker | n | hit rate | hit - base rate (n) |", "|---|---|---|---|"]
    shown = 0
    for who, rr in sorted(sp.items()):
        if len(rr) < MIN_SPEAKER:
            continue
        shown += 1
        bp = [fbool(r["hit"]) - fnum(r["base_p"]) for r in rr if fnum(r.get("base_p")) is not None]
        L.append("| %s | %d | %s | %s (%d) |" % (who, len(rr), pct(np.mean([fbool(r["hit"]) for r in rr])),
                                                 pp(np.mean(bp)) if bp else "", len(bp)))
    if not shown:
        L.append("| (no speaker reaches %d resolved rows) | | | |" % MIN_SPEAKER)
    # open rows
    q = collections.Counter(pd.Timestamp(r["resolve_date"]).to_period("Q").strftime("%Y-Q%q") for r in opn if r.get("resolve_date"))
    L += ["", "## Open rows by expected resolution quarter", "", "| Quarter | open rows |", "|---|---|"]
    L += ["| %s | %d |" % (k, v) for k, v in sorted(q.items())]
    # gaps, limits, agreement
    gp = os.path.join(HERE, "rule_gaps.md")
    L += ["", "## Rule gaps (narrowest reading applied; SCORING_RULES.md unchanged)", ""]
    L += open(gp).read().strip().splitlines() if os.path.exists(gp) else ["(none recorded)"]
    lev = collections.Counter(r["level_use"].split(" (")[0] + (" (" + r["level_use"].split(" (")[1] if " (" in r["level_use"] else "")
                              for r in res if r.get("level_use"))
    if lev:
        L += ["", "Level use among resolved rows: " + "; ".join("%s: %d" % kv for kv in sorted(lev.items()))]
    rules_txt = open(os.path.join(DOCS, "SCORING_RULES.md")).read()
    m = re.search(r"## 7\. Known limits\n(.*?)\n## 8", rules_txt, re.S)
    L += ["", "## Known limits (SCORING_RULES.md section 7)", "", m.group(1).strip() if m else ""]
    ag = [p for p in os.listdir(DOCS) if p.startswith("CODING_AGREEMENT")]
    if ag:
        t = open(os.path.join(DOCS, sorted(ag)[-1])).read()
        m = re.search(r"## Agreement.*?\n(```.*?```)", t, re.S)
        L += ["", "## Coding agreement (%s)" % sorted(ag)[-1], "", m.group(1) if m else ""]
    txt = "\n".join(L) + "\n"
    for d in (DOCS, F):
        with open(os.path.join(d, "SCORECARD_%s.md" % day), "w") as f:
            f.write(txt)
    print("scorecard written | resolved %d | open %d | rows %d" % (len(res), len(opn), len(rows)))


if __name__ == "__main__":
    main()
