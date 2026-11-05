"""Score two independent paper reads: quote check, coverage, agreement both ways, merged ledger.
usage: score_paper.py SID  -> prints report; writes merged/SID.json (Sonnet claims + Opus-only claims)"""
import json, os, re, sys, unicodedata, collections
D = os.path.dirname(os.path.abspath(__file__))
STOP = set("the a an of to and or in on for is are be that this it as with by at from was were has have not but if than then so we they you i he she its their our will would can could should may might more less very just".split())
def norm(s):
    s = unicodedata.normalize("NFKC", s or "").replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').lower()
    return re.findall(r"[a-z0-9%$']+", s)
def tri(t): return set(zip(t, t[1:], t[2:]))
def words(s): return {w for w in norm(s) if w not in STOP and len(w) > 2}
sid = sys.argv[1]
t = open(os.path.join(D, "docs", sid + ".txt")).read()
parts = re.split(r"\n\[(C\d+)\]\n", t)
ch = {parts[i]: parts[i + 1] for i in range(1, len(parts) - 1, 2)}
whole = " ".join(norm(" ".join(ch.values())))
def q(c):
    qt = " ".join(norm(c.get("quote")))
    if qt and qt in " ".join(norm(ch.get(c.get("chunk"), ""))): return "exact"
    if qt and qt in whole: return "other_chunk"
    g = tri(norm(c.get("quote")))
    return "near" if g and len(g & tri(whole.split())) / len(g) >= 0.6 else "not_found"
def sim(a, b):
    qa, qb = tri(norm(a.get("quote"))), tri(norm(b.get("quote")))
    jq = len(qa & qb) / len(qa | qb) if qa and qb else 0
    wa = words(a.get("claim", "") + " " + a.get("exact_rule", "") + " " + a.get("reported_result", ""))
    wb = words(b.get("claim", "") + " " + b.get("exact_rule", "") + " " + b.get("reported_result", ""))
    jw = len(wa & wb) / len(wa | wb) if wa and wb else 0
    return max(1.5 * jq, jw)
def near(a, b):
    try: return abs(int(a["chunk"][1:]) - int(b["chunk"][1:])) <= 1
    except Exception: return True
def matched(src, ref, thr=0.25): return [any(near(r, s) and sim(r, s) >= thr for s in src) for r in ref]
R = {}
for eng in ("sonnet", "opus"):
    p = os.path.join(D, eng, sid + ".json")
    R[eng] = json.load(open(p)) if os.path.exists(p) else None
for eng, d in R.items():
    if not d: print(eng, "missing"); continue
    cl = d["claims"]; qs = collections.Counter(q(c) for c in cl)
    cov = {c["chunk"] for c in d["coverage"]}
    print("%-6s claims %d  quotes %s  coverage complete %s  types %s" % (eng, len(cl), dict(qs), cov >= set(ch),
          dict(collections.Counter(c.get("claim_type") for c in cl))))
if all(R.values()):
    s, o = R["sonnet"]["claims"], R["opus"]["claims"]
    ms, mo = matched(s, o), matched(o, s)
    print("Sonnet found %.0f%% of Opus claims; Opus found %.0f%% of Sonnet claims" % (100 * sum(ms) / len(o), 100 * sum(mo) / len(s)))
    only_o = [c for c, ok in zip(o, ms) if not ok]
    only_s = [c for c, ok in zip(s, mo) if not ok]
    print("Opus-only by type", dict(collections.Counter(c.get("claim_type") for c in only_o)))
    print("Sonnet-only by type", dict(collections.Counter(c.get("claim_type") for c in only_s)))
    # map every Opus claim to its best Sonnet match (so the Opus reasoning map can point at merged ids)
    idmap, extra = {}, []
    for c in o:
        best = max(((sim(c, x), x) for x in s if near(c, x)), default=(0, None), key=lambda t: t[0])
        if best[1] is not None and best[0] >= 0.25:
            idmap[c["claim_id"]] = best[1]["claim_id"]
        else:
            idmap[c["claim_id"]] = c["claim_id"] + "b"
            extra.append(dict(c, reader="opus", claim_id=c["claim_id"] + "b"))
    role = {idmap[c["claim_id"]]: c.get("role") for c in o if c.get("role")}
    merged = dict(R["sonnet"])
    merged["claims"] = [dict(c, reader="sonnet", role=c.get("role") or role.get(c["claim_id"], "")) for c in s] + extra
    for c in merged["claims"]: c["quote_check"] = q(c)
    def remap(x):
        if isinstance(x, dict): return {k: ([idmap.get(i, i) for i in v] if k == "claim_ids" else remap(v)) for k, v in x.items()}
        if isinstance(x, list): return [remap(v) for v in x]
        return x
    merged["reasoning"] = remap(R["opus"].get("reasoning", {}))
    known = {c["claim_id"] for c in merged["claims"]}
    dangling = sorted({i for i in re.findall(r"QP\d+-C\d+-[\w]+", json.dumps(merged["reasoning"])) if i not in known})
    print("reasoning sections", {k: (len(v) if isinstance(v, list) else 1) for k, v in merged["reasoning"].items()}, "dangling ids", dangling[:5])
    merged["crosscheck"] = "opus blind read + reasoning map (paper)"; merged["n_sonnet"] = len(s); merged["n_opus_added"] = len(extra)
    os.makedirs(os.path.join(D, "merged"), exist_ok=True)
    json.dump(merged, open(os.path.join(D, "merged", sid + ".json"), "w"), indent=1, ensure_ascii=False)
    json.dump({"opus_only": [(c["claim_id"], c["claim"]) for c in extra], "sonnet_only": [(c["claim_id"], c["claim"]) for c in only_s]},
              open(os.path.join(D, "merged", sid + ".diff.json"), "w"), indent=1, ensure_ascii=False)
