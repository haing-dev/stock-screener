"""Paper vault notes: vault/Papers/<QPnn - title>.md with Argument map (reasoning, linked to claim blocks) + claims.
python3 build_papers.py  (reads merged/QPnn.json, writes ../vault/Papers/ and ../vault/Papers/00 Papers index.md)"""
import collections, glob, json, os, re

D = os.path.dirname(os.path.abspath(__file__))
V = os.path.join(D, "..", "vault", "Papers")
MECH = {"slow_reaction", "risk_premium", "overshoot", "cycle_persistence", "liquidity_flows", "policy_reaction",
        "crowding_positioning", "seasonality", "fiscal_debt", "structural_shift", "risk_management", "research_method", "behavioral"}


def esc(s):
    return re.sub(r"\s+", " ", str(s or "")).strip()


def safe(s, n=90):
    return re.sub(r"\s+", " ", re.sub(r'[\\/:*?"<>|#^\[\]]', "", s)).strip()[:n].rstrip(" .")


def bid(i):
    return re.sub(r"[^A-Za-z0-9-]", "-", i)


def main():
    os.makedirs(V, exist_ok=True)
    idx = ["---", "tags: [index, papers]", "---", "# Quant papers: Layer 0 ledger + argument maps", "",
           "Each note: argument map (question, thesis, foundations, mechanism chain, design rationale, evidence, regimes, "
           "gaps, relations, forward-looking inputs) linked to verbatim-checked claims. Two independent readers "
           "(Sonnet + Opus blind); the argument map is Opus's, '(reader)' marks inference beyond the authors.", "",
           "| ID | Paper | Claims | Opus-only | Quotes exact |", "|---|---|---|---|---|"]
    for p in sorted(glob.glob(os.path.join(D, "merged", "QP*.json"))):
        if p.endswith(".diff.json"):
            continue
        m = json.load(open(p))
        sid = m["source_id"]
        head = open(os.path.join(D, "docs", sid + ".txt")).read().split("\n---\n", 1)[0]
        title = head.splitlines()[0].lstrip("# ").strip()
        fname = "%s - %s" % (sid, safe(title))
        link = lambda ids: ", ".join("[[%s#^%s|%s]]" % (fname, bid(i), i.split("-", 1)[1]) for i in ids or [])
        R = m.get("reasoning", {})
        L = ["---", "source_id: %s" % sid, 'title: "%s"' % title.replace('"', "'"), "type: paper",
             "claims: %d" % len(m["claims"]), "opus_only: %d" % m.get("n_opus_added", 0), "tags: [paper, layer0]", "---",
             "# " + title, "", "**Authors:** " + "; ".join(m.get("speakers", [])), "", "**Summary:** " + esc(m.get("summary")), "",
             "## Argument map", ""]
        if R.get("question"):
            L += ["**Question:** " + esc(R["question"]), ""]
        th = R.get("thesis") or {}
        if th:
            L += ["**Thesis:** %s (%s)" % (esc(th.get("statement")), link(th.get("claim_ids"))), ""]
        sections = [("Foundations (premises)", "foundations", lambda e: "%s _[%s, %s; support: %s]_" % (esc(e.get("premise")), e.get("type", ""), e.get("stated", ""), esc(e.get("support")))),
                    ("Mechanism chain", "mechanism_chain", lambda e: "%s. %s → %s: %s _[%s]_" % (e.get("step", ""), esc(e.get("from")), esc(e.get("to")), esc(e.get("why")), e.get("evidence", ""))),
                    ("Design rationale", "design_rationale", lambda e: "**%s**: %s. Alternatives: %s. Sensitivity: %s" % (esc(e.get("choice")), esc(e.get("reason_given")), esc(e.get("alternatives")), esc(e.get("sensitivity")))),
                    ("Evidence map", "evidence_map", lambda e: "%s. Tests: %s. Rules out: %s. Does not rule out: %s. Strength: %s" % (esc(e.get("result")), esc(e.get("tests")), esc(e.get("rules_out")), esc(e.get("does_not_rule_out")), esc(e.get("strength")))),
                    ("Regimes", "regimes", lambda e: "%s → %s" % (esc(e.get("condition")), esc(e.get("effect")))),
                    ("Gaps and conflicts", "gaps_and_conflicts", lambda e: "[%s] %s" % (e.get("type", ""), esc(e.get("issue")))),
                    ("Relations to other strategies", "relations", lambda e: "%s: **%s**. %s" % (esc(e.get("other_idea")), e.get("relation", ""), esc(e.get("why"))))]
        for head_, key, fmt in sections:
            items = R.get(key) or []
            if items:
                L += ["### " + head_]
                for e in items:
                    L.append("- " + fmt(e) + (" (%s)" % link(e.get("claim_ids")) if e.get("claim_ids") else ""))
                L.append("")
        if R.get("forward_looking_inputs"):
            L += ["### Forward-looking inputs (reader synthesis)", esc(R["forward_looking_inputs"]), ""]
        if R.get("reader_inferences"):
            L += ["### Reader inferences (not stated by the authors)"] + ["- " + esc(x) for x in R["reader_inferences"]] + [""]
        L += ["## Claims", ""]
        by = collections.defaultdict(list)
        for c in m["claims"]:
            by[c.get("chunk", "C??")].append(c)
        for chk in sorted(by, key=lambda k: int(re.sub(r"\D", "", k) or 0)):
            L.append("### %s (page %d)" % (chk, int(re.sub(r"\D", "", chk) or 0)))
            for c in by[chk]:
                mk = c.get("mechanism", "") if c.get("mechanism", "") in MECH else "new"
                flags = [x for x in (c.get("claim_type"), c.get("role")) if x]
                if c.get("reader") == "opus":
                    flags.append("Opus only")
                if c.get("quote_check") != "exact":
                    flags.append("quote " + str(c.get("quote_check")))
                L.append("- %s _(%s)_ #mech/%s" % (esc(c.get("claim")), ", ".join(flags), mk))
                L.append("  > " + esc(c.get("quote")))
                det = ["%s: %s" % (k, esc(c.get(k))) for k in ("exact_rule", "data_needed", "reported_result", "exhibit", "conditions")
                       if esc(c.get(k)) and esc(c.get(k)).lower() not in ("empty", "n/a", "none")]
                if det:
                    L.append("  " + " · ".join(det))
                L.append("  ^" + bid(c["claim_id"]))
            L.append("")
        open(os.path.join(V, fname + ".md"), "w").write("\n".join(L) + "\n")
        qx = sum(c.get("quote_check") == "exact" for c in m["claims"])
        idx.append("| %s | [[%s]] | %d | %d | %d/%d |" % (sid, fname, len(m["claims"]), m.get("n_opus_added", 0), qx, len(m["claims"])))
    open(os.path.join(V, "00 Papers index.md"), "w").write("\n".join(idx) + "\n")
    print("papers:", len(idx) - 7)


if __name__ == "__main__":
    main()
