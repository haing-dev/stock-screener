"""Pilot scoring: quote precision, coverage completeness, reader agreement (Sonnet extraction vs Opus blind read)."""
import json, os, re, sys, unicodedata

P = os.path.dirname(os.path.abspath(__file__))
STOP = set("the a an of to and or in on for is are be that this it as with by at from was were has have not but if than "
           "then so we they you i he she its their our will would can could should may might more less very just".split())


def norm(s):
    s = unicodedata.normalize("NFKC", s).replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"').lower()
    return re.findall(r"[a-z0-9%$']+", s)


def chunks(sid):
    t = open(os.path.join(P, "docs", sid + ".txt")).read()
    parts = re.split(r"\n\[(C\d+)\]\n", t)
    return {parts[i]: parts[i + 1] for i in range(1, len(parts) - 1, 2)}


def tri(tokens):
    return set(zip(tokens, tokens[1:], tokens[2:]))


def words(s):
    return {w for w in norm(s) if w not in STOP and len(w) > 2}


def load(model, sid):
    p = os.path.join(P, "out", model, sid + ".json")
    return json.load(open(p)) if os.path.exists(p) else None


def quote_status(q, ch, allc):
    qt = " ".join(norm(q))
    if qt and qt in " ".join(norm(ch)):
        return "exact"
    if qt and qt in " ".join(norm(" ".join(allc.values()))):
        return "other chunk"
    g = tri(norm(q))
    cov = len(g & tri(norm(" ".join(allc.values())))) / len(g) if g else 0
    return "near" if cov >= 0.6 else "NOT FOUND"


def sim(a, b):
    qa, qb = tri(norm(a["quote"])), tri(norm(b["quote"]))
    jq = len(qa & qb) / len(qa | qb) if qa and qb else 0
    wa, wb = words(a["claim"] + " " + a.get("indicator", "")), words(b["claim"] + " " + b.get("indicator", ""))
    jw = len(wa & wb) / len(wa | wb) if wa and wb else 0
    return max(jq * 1.5, jw)


def near(a, b):
    try:
        return abs(int(a["chunk"][1:]) - int(b["chunk"][1:])) <= 1
    except Exception:
        return True


def matched(src, ref, thr=0.25):
    return [any(near(r, s) and sim(r, s) >= thr for s in src) for r in ref]


def main():
    man = json.load(open(os.path.join(P, "manifest.json")))
    rows = []
    for m in man:
        sid = m["source_id"]
        ch = chunks(sid)
        rec = {"sid": sid, "words": m["words"], "chunks": m["chunks"]}
        out = {}
        for model in ("sonnet", "opus"):
            d = load(model, sid)
            if not d:
                rec[model] = None
                continue
            out[model] = d
            cl = d.get("claims", [])
            qs = [quote_status(c.get("quote", ""), ch.get(c.get("chunk", ""), ""), ch) for c in cl]
            cov = {c["chunk"] for c in d.get("coverage", [])}
            rec[model] = {"claims": len(cl), "exact": qs.count("exact"), "other_chunk": qs.count("other chunk"),
                          "near": qs.count("near"), "not_found": qs.count("NOT FOUND"),
                          "coverage_complete": cov >= set(ch), "testable_yes": sum(str(c.get("testable", "")).startswith("yes") for c in cl),
                          "time_bound": sum(str(c.get("time_bound", "")).startswith("yes") for c in cl)}
            rec[model + "_bad"] = [(c.get("claim_id"), s, c.get("quote", "")[:70]) for c, s in zip(cl, qs) if s == "NOT FOUND"]
        if len(out) == 2:
            s_cl, o_cl = out["sonnet"]["claims"], out["opus"]["claims"]
            rec["recall_sonnet_of_opus"] = sum(matched(s_cl, o_cl)) / max(len(o_cl), 1)
            rec["recall_opus_of_sonnet"] = sum(matched(o_cl, s_cl)) / max(len(s_cl), 1)
            rec["opus_only"] = [(c["claim_id"], c["claim"][:110]) for c, ok in zip(o_cl, matched(s_cl, o_cl)) if not ok]
        rows.append(rec)
    json.dump(rows, open(os.path.join(P, "score.json"), "w"), indent=1)
    for r in rows:
        print(r["sid"], r["words"], "words", r["chunks"], "chunks")
        for model in ("sonnet", "opus"):
            print("  ", model, r.get(model))
        if "recall_sonnet_of_opus" in r:
            print("   agreement: Sonnet found %.0f%% of Opus claims; Opus found %.0f%% of Sonnet claims" % (
                100 * r["recall_sonnet_of_opus"], 100 * r["recall_opus_of_sonnet"]))
        for k in ("sonnet_bad", "opus_bad"):
            if r.get(k):
                print("   ", k, r[k])


if __name__ == "__main__":
    main()
