"""Descriptive: crash-triage calls at 3, 6 and 12 months vs XBI (published sample 2020-2026). usage: python3 horizons.py <repo copy>"""
import sys, os, json, math, statistics as st, collections, io, contextlib
REPO = sys.argv[1]
os.chdir(REPO)
sys.path.insert(0, os.path.join(REPO, "pipeline"))
import fit
from returns import total_return, plus
rows = {k: fit.prepare(k) for k in fit.KINDS}
def tstat(v):
    return (sum(v) / len(v)) / (st.stdev(v) / math.sqrt(len(v))) if len(v) > 2 and st.stdev(v) > 0 else float("nan")
for k in fit.KINDS:
    res = collections.defaultdict(lambda: collections.defaultdict(list))
    tp = collections.defaultdict(list)
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
        for h in (91, 182, 365):
            d1 = plus(x["asof"], h)
            a, _ = total_return(x["cik"], x["asof"], d1)
            b, _ = total_return("XBI", x["asof"], d1)
            if a is None or b is None:
                continue
            res[v][h].append(min(a, 5.0) - b)
            if v == "overdone":
                tp[(bool(s.get("top_pick")), h)].append(min(a, 5.0) - b)
    for v in ("overdone", "close", "justified"):
        print(k, v, " | ".join(f"{h}d n={len(z)} mean_ex={sum(z)/len(z):+.3f} med_ex={st.median(z):+.3f} sd={st.stdev(z):.2f} t={tstat(z):+.2f} beat={sum(e>0 for e in z)/len(z):.2f}"
                                for h, z in sorted(res[v].items())))
    for (t, h), z in sorted(tp.items()):
        print(k, "overdone top_pick" if t else "overdone other", f"{h}d n={len(z)} mean_ex={sum(z)/len(z):+.3f} med_ex={st.median(z):+.3f} t={tstat(z):+.2f} beat={sum(e>0 for e in z)/len(z):.2f}")
