"""Descriptive re-read of the crash-triage backtest (already-published sample 2020-2026): dispersion, skew, fragility.
usage: python3 analyse.py <repo copy>"""
import sys, os, json, math, statistics as st, collections
REPO = sys.argv[1]
os.chdir(REPO)
sys.path.insert(0, os.path.join(REPO, "pipeline"))
import fit
from returns import total_return

rows = {k: fit.prepare(k) for k in fit.KINDS}
as_of, names = fit.top_performers(rows["crash"] + rows["slide"])
for k in fit.KINDS:
    for x in rows[k]:
        if "tbu" in x:
            continue
        f = x.get("fund")
        if not f:
            x["top"] = None
            continue
        tops = as_of(x["asof"][:7] + "-01")
        hit = sorted((tops[fc] + (fc,) for fc, *_ in f["list"] if fc in tops), key=lambda t: t[0])
        x["top"] = [(names.get(t[-1], t[-1]), t[0], t[2], t[3]) for t in hit]
        x["top_later"] = []
        for fc, n, _, d in f["later"]:
            t = as_of(d[:7] + "-01").get(fc)
            if t:
                x["top_later"].append((names.get(fc, n), t[0], t[2], t[3], d))
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        fit.score_kind(k, rows[k])

def tstat(v):
    return (sum(v) / len(v)) / (st.stdev(v) / math.sqrt(len(v))) if len(v) > 2 and st.stdev(v) > 0 else float("nan")

out = {}
for k in fit.KINDS:
    held = collections.defaultdict(list)
    for x in rows[k]:
        if "tbu" in x or x.get("y") is None:
            continue
        p = fit.kdir(k, "scores") / f"{x['id']}.json"
        if not p.exists():
            continue
        s = json.loads(p.read_text())
        v = s.get("verdict")
        if v == "tbu" or (s.get("upgraded") and s.get("call_date") != x["asof"]):
            continue
        b, _ = total_return("XBI", x["asof"], x["d365"])
        if b is None:
            continue
        held[v].append({"abs": x["abs"], "ex": min(x["abs"], 5.0) - b, "m": x["asof"][:7], "y": x["asof"][:4], "cik": x["cik"],
                        "top_pick": bool(s.get("top_pick"))})
    for v, L in held.items():
        ex = [e["ex"] for e in L]
        ab = [min(e["abs"], 5.0) for e in L]
        n = len(L)
        bym = collections.defaultdict(list)
        for e in L:
            bym[e["m"]].append(e["ex"])
        mm = [sum(z) / len(z) for z in bym.values()]
        srt = sorted(L, key=lambda e: -e["ex"])
        drop = max(1, round(0.02 * n))
        trimmed = [e["ex"] for e in srt[drop:]]
        pos = sum(e["ex"] for e in L if e["ex"] > 0)
        top5 = sum(e["ex"] for e in srt[:5])
        byy = collections.defaultdict(list)
        for e in L:
            byy[e["y"]].append(e["ex"])
        out[(k, v)] = dict(n=n, companies=len({e["cik"] for e in L}), mean_abs=sum(ab) / n, median_abs=st.median(ab),
                           mean_ex=sum(ex) / n, median_ex=st.median(ex), sd_ex=st.stdev(ex) if n > 1 else float("nan"),
                           t_naive=tstat(ex), months=len(mm), t_month=tstat(mm), beat_xbi=sum(e > 0 for e in ex) / n,
                           dropped=drop, mean_ex_wo_top2pct=sum(trimmed) / len(trimmed) if trimmed else float("nan"),
                           top5_share_of_gains=top5 / pos if pos else float("nan"),
                           by_year={y: (len(z), round(sum(z) / len(z), 3)) for y, z in sorted(byy.items())},
                           loss_gt_50=sum(a <= -0.5 for a in ab) / n, gain_gt_100=sum(a >= 1.0 for a in ab) / n)
for (k, v), d in sorted(out.items()):
    print(k, v)
    for kk, vv in d.items():
        print("   ", kk, round(vv, 3) if isinstance(vv, float) else vv)
