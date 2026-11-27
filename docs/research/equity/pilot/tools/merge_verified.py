"""Merge first-reader claims, blind tags and the third reading into verified claims (A13 item 6).

python3 merge_verified.py KEY TAGS THIRD THIRD_MAP OUT_DIR CLAIMS.checked.json [...]
Per claim: rule_status = both (both readers rule-like) | third (split, third reader said rule) | no;
computable_final = weaker of the two readers' tags where both tagged (no < proxy < yes), else the first reader's;
second_* = the verifier's tags where the claim was in the verification set. Planted items are mapped back to their
real claims (the planted tags are ignored). Writes OUT_DIR/<DOC>.verified.json.
"""
import json
import sys

RANK = {"no": 0, "proxy": 1, "yes": 2}


def main():
    key = json.load(open(sys.argv[1], encoding="utf-8"))
    tags = {t["vid"]: t for t in json.load(open(sys.argv[2], encoding="utf-8"))}
    third = {t["tid"]: t["answer"] for t in json.load(open(sys.argv[3], encoding="utf-8"))}
    tmap = json.load(open(sys.argv[4], encoding="utf-8"))
    third_by_vid = {v: third[t] for t, v in tmap.items()}
    by_id = {k["id"]: k for k in key}
    out = sys.argv[5]
    rl = lambda s: s in ("rule", "threshold")
    for f in sys.argv[6:]:
        claims = json.load(open(f, encoding="utf-8"))
        for c in claims:
            k = by_id.get(c["id"])
            c["rule_status"] = "no"
            if k is None:
                continue
            t = tags[k["vid"]]
            c.update(second_kind=t["kind"], second_part=t["part"], second_computable=t["computable"],
                     second_value=t.get("value", ""), second_measure=t.get("measure", ""), vid=k["vid"])
            first_rl = rl(c["kind"])  # the real first-reader tag, also for planted items
            if first_rl and rl(t["kind"]):
                c["rule_status"] = "both"
            elif first_rl and third_by_vid.get(k["vid"]) == "rule":
                c["rule_status"] = "third"
            a, b = c.get("computable", "no"), t["computable"]
            c["computable_final"] = a if RANK.get(a, 0) <= RANK.get(b, 0) else b
        for c in claims:
            c.setdefault("computable_final", c.get("computable", "no"))
        doc = claims[0]["id"].split("-")[0]
        json.dump(claims, open("%s/%s.verified.json" % (out, doc), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(doc, len(claims), "rules:", sum(c["rule_status"] != "no" for c in claims),
              "(both %d, third %d)" % (sum(c["rule_status"] == "both" for c in claims),
                                        sum(c["rule_status"] == "third" for c in claims)))


if __name__ == "__main__":
    main()
