"""Forecast ledger step 2.1a (script): pull every dated view out of the transcript argument maps and every forecast
out of the X-post source (MT228) into one raw file, one view per line, with the verbatim quotes it cites.
usage: python3 tools/fcast/pull.py <macro-vault worktree> [batch size]   -> <vault>/pipeline/forecasts/"""
import glob, json, os, random, re, sys

V = sys.argv[1]
BATCH = int(sys.argv[2]) if len(sys.argv) > 2 else 180
OUT = os.path.join(V, "pipeline", "forecasts")
os.makedirs(os.path.join(OUT, "batches"), exist_ok=True)
AL = json.load(open(os.path.join(V, "pipeline", "speaker_aliases.json")))["aliases"]
CANON = {a.lower(): k for k, vs in AL.items() for a in list(vs) + [k]}


def canon(name):
    base = re.sub(r"\s*\(.*$", "", name or "").strip()
    return CANON.get(base.lower(), base)


rows = []
for p in sorted(glob.glob(os.path.join(V, "pipeline", "maps", "MT*.json"))):
    m = json.load(open(p))
    sid = m["source_id"]
    led = json.load(open(os.path.join(V, "ledger", sid + ".json")))
    claims = {c["claim_id"]: c for c in led["claims"] + m.get("added_claims", [])}
    meta = led.get("meta") or {}
    n = 0
    for sp in m.get("speakers", []):
        for v in sp.get("current_views") or []:
            n += 1
            rows.append({"view_id": "%s-V%03d" % (sid, n), "source_id": sid, "title": led.get("title", ""),
                         "upload_date": meta.get("upload date", ""), "speaker": canon(sp.get("name")),
                         "speaker_as_written": sp.get("name"), "role": sp.get("role", ""), "as_of_text": v.get("as_of", ""),
                         "view": v.get("view", ""), "reasoning": v.get("reasoning", ""), "claim_ids": v.get("claim_ids", []),
                         "quotes": [{"claim_id": c, "quote": (claims[c].get("quote") or "")[:500]} for c in v.get("claim_ids", [])[:4] if c in claims]})
x = json.load(open(os.path.join(V, "raw", "sonnet", "MT228.json")))
n = 0
for c in x["claims"]:
    if c.get("kind") != "forecast":
        continue
    n += 1
    rows.append({"view_id": "MT228-V%03d" % n, "source_id": "MT228", "title": "X posts of John Galt (@AtlasShrug1)",
                 "upload_date": c.get("as_of", ""), "speaker": "John Galt", "speaker_as_written": "John Galt", "role": "X posts",
                 "as_of_text": c.get("as_of", ""), "view": c.get("claim", ""),
                 "reasoning": "; ".join(str(c.get(k)) for k in ("forecast", "conditions", "horizon") if c.get(k)),
                 "claim_ids": [c["claim_id"]], "quotes": [{"claim_id": c["claim_id"], "quote": (c.get("quote") or "")[:500]}]})
with open(os.path.join(OUT, "views_raw.jsonl"), "w") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
nb = 0
for i in range(0, len(rows), BATCH):
    nb += 1
    with open(os.path.join(OUT, "batches", "batch_%02d.jsonl" % nb), "w") as f:
        for r in rows[i:i + BATCH]:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
random.seed(20261111)
ids = sorted(r["view_id"] for r in rows)
sample = sorted(random.sample(ids, round(0.2 * len(ids))))
want = set(sample)
with open(os.path.join(OUT, "recode_sample.jsonl"), "w") as f:      # the 20% an independent model codes blind
    for r in rows:
        if r["view_id"] in want:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("views", len(rows), "| sources", len({r["source_id"] for r in rows}), "| speakers", len({r["speaker"] for r in rows}),
      "| batches", nb, "| blind recode sample", len(sample))
