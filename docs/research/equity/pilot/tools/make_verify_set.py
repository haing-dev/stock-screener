"""Build the blind verification set (A10 item 8) from checked claim files.

python3 make_verify_set.py SRC_DIR SEED OUT_DIR CLAIMS.checked.json [...]
Writes OUT_DIR/verify_items.json (what the verifier sees: id, doc, line, quote, context; no first-reader tags) and
OUT_DIR/verify_key.json (first-reader tags incl. 10 planted items; kept away from the verifier).
Selection: every claim tagged rule or threshold, a random 30% of the rest (seeded), and 10 planted items:
5 anecdotes (or examples) re-tagged as rules and 5 thresholds with the number altered (+-40% or more).
Items are shuffled and renumbered V001.. so the verifier cannot see the source id order.
"""
import hashlib
import json
import random
import re
import sys


def context(lines, line, before=6, after=6):
    a, b = max(0, line - 1 - before), min(len(lines), line + after)
    return "\n".join(re.sub(r"^\[L\d+\]\s*", "", x) for x in lines[a:b])


def alter(v):
    m = re.search(r"\d+(\.\d+)?", v)
    if not m:
        return None
    x = float(m.group(0))
    y = x * 1.6 if x < 50 else x * 0.5
    y = int(round(y)) if "." not in m.group(0) else round(y, 1)
    if y == x:
        y = x + 3
    return v[:m.start()] + str(y) + v[m.end():]


def main():
    src, seed, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    rng = random.Random(seed)
    claims = []
    for f in sys.argv[4:]:
        claims += [c for c in json.load(open(f, encoding="utf-8")) if c.get("found")]
    docs = {}
    for c in claims:
        d = c["id"].split("-")[0]
        if d not in docs:
            docs[d] = open("%s/%s.txt" % (src, d), encoding="utf-8").read().splitlines()
    rule_like = [c for c in claims if c["kind"] in ("rule", "threshold")]
    rest = [c for c in claims if c["kind"] not in ("rule", "threshold")]
    sample = rule_like + rng.sample(rest, round(0.3 * len(rest)))
    chosen = {c["id"] for c in sample}
    # planted 1: anecdotes / examples from outside the sample, re-tagged as rules
    pool_a = [c for c in rest if c["id"] not in chosen and c["kind"] == "anecdote"]
    pool_a += [c for c in rest if c["id"] not in chosen and c["kind"] == "example"]
    plant_a = pool_a[:0]
    for c in rng.sample(pool_a, len(pool_a)):
        if len(plant_a) == 5:
            break
        plant_a.append(c)
    # planted 2: claims with a number in the quote, number altered; thresholds first
    def has_num(c):
        return re.search(r"\d", c.get("value") or "") or re.search(r"\b\d+(\.\d+)?\b", c["quote"])
    pool_t = [c for c in claims if c["kind"] == "threshold" and has_num(c)]
    pool_t += [c for c in rule_like if c["kind"] == "rule" and re.search(r"\b\d+(\.\d+)?\b", c["quote"])]
    plant_t, seen = [], {c["id"] for c in plant_a}
    for c in pool_t:
        if len(plant_t) == 5:
            break
        if c["id"] in seen:
            continue
        v = c.get("value") or re.search(r"\d+(\.\d+)?%?", c["quote"]).group(0)
        nv = alter(v)
        if nv:
            plant_t.append((c, v, nv))
            seen.add(c["id"])
    items, key = [], []
    for c in sample:
        if c["id"] in {p[0]["id"] for p in plant_t}:
            continue
        items.append(c)
        key.append(dict(c, planted=""))
    for c in plant_a:
        items.append(c)
        key.append(dict(c, kind="rule", planted="anecdote_as_rule", true_kind=c["kind"]))
    for c, v, nv in plant_t:
        items.append(c)
        key.append(dict(c, kind="threshold", value=nv, planted="altered_threshold", true_value=v))
    order = list(range(len(items)))
    rng.shuffle(order)
    vis, kk = [], []
    for n, i in enumerate(order, 1):
        c, k = items[i], key[i]
        vid = "V%03d" % n
        vis.append({"vid": vid, "doc": c["id"].split("-")[0], "line": c["line_found"], "quote": c["quote"],
                    "context": context(docs[c["id"].split("-")[0]], c["line_found"])})
        kk.append(dict(k, vid=vid))
    json.dump(vis, open(out + "/verify_items.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(kk, open(out + "/verify_key.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    h = hashlib.sha256(open(out + "/verify_key.json", "rb").read()).hexdigest()
    print("items %d (rule-like %d, sample of rest %d, planted %d+%d); key sha256 %s"
          % (len(vis), len(rule_like) - len(plant_t), len(sample) - len(rule_like), len(plant_a), len(plant_t), h))


if __name__ == "__main__":
    main()
