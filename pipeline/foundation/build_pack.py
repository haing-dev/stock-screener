"""Build one foundation unit's Fable input: foundation/packs/<UID>.json (syntheses/maps/paper maps + every cited claim
with its verbatim quote). usage: build_pack.py U02"""
import json, os, re, sys
L = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U = {u["id"]: u for u in json.load(open(os.path.join(L, "foundation", "units.json")))}[sys.argv[1]]
claims = {}
def load_ledger(src):
    if src.startswith("QP"):
        m = json.load(open(os.path.join(L, "papers", "merged", src + ".json"))); return m["claims"]
    led = json.load(open(os.path.join(L, "ledger", src + ".json")))["claims"]
    mp = os.path.join(L, "maps", src + ".json")
    if os.path.exists(mp): led += json.load(open(mp)).get("added_claims", [])
    return led
cache = {}
def claim(cid):
    src = cid.split("-")[0]
    if src not in cache: cache[src] = {c["claim_id"]: c for c in load_ledger(src)}
    c = cache[src].get(cid)
    if c: claims[cid] = {k: c.get(k) for k in ("claim_id", "speaker", "quote", "claim", "mechanism", "indicator", "exact_rule", "reported_result", "conditions", "time_bound", "correction", "quote_check") if c.get(k)}
pack = {"unit": U, "items": []}
own = 0
for s in U.get("investors", []):
    syn = json.load(open(os.path.join(L, "investors", s + ".json")))
    pack["items"].append({"type": "investor_synthesis", "slug": s, "data": syn})
    # every claim the person made in their sources (not only those the synthesis cites)
    rx = re.compile(U.get("speaker_match", {}).get(s) or s.split("_")[-1], re.I)
    for src in syn.get("sources", []):
        for c in load_ledger(src):
            if rx.search(str(c.get("speaker", ""))):
                claim(c["claim_id"]); own += 1
for m in U.get("maps", []):
    p = os.path.join(L, "maps", m + ".json")
    if os.path.exists(p): pack["items"].append({"type": "transcript_map", "source_id": m, "title": json.load(open(os.path.join(L, "ledger", m + ".json")))["title"], "data": json.load(open(p))})
    else: pack["items"].append({"type": "missing_map", "source_id": m})
for q in U.get("papers", []):
    mm = json.load(open(os.path.join(L, "papers", "merged", q + ".json")))
    pack["items"].append({"type": "paper", "source_id": q, "summary": mm.get("summary"), "reasoning": mm.get("reasoning")})
    for c in mm["claims"]: claim(c["claim_id"])        # papers: full ledger
for x in U.get("extra", []):
    pack["items"].append({"type": "extra", "file": x, "data": json.load(open(os.path.join(L, x)))})
for cid in sorted(set(re.findall(r"(?:MT|QP)\d+-C\d+-[A-Za-z0-9]+", json.dumps(pack["items"])))):
    claim(cid)
pack["claims"] = [claims[k] for k in sorted(claims)]
os.makedirs(os.path.join(L, "foundation", "packs"), exist_ok=True)
out = os.path.join(L, "foundation", "packs", U["id"] + ".json")
json.dump(pack, open(out, "w"), ensure_ascii=False)
print(U["id"], U["name"], "own claims", own, "items", len(pack["items"]), "claims", len(pack["claims"]), "~%dk tokens" % (os.path.getsize(out) // 4000))
