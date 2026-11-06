"""investors/<slug>.json -> vault/Investors/<Name>.md (links to Sources/Papers notes and claim blocks)."""
import glob, json, os, re

L = os.path.dirname(os.path.abspath(__file__))
V = os.path.join(L, "vault", "Investors")


def notes():
    m = {}
    for d in ("Sources", "Papers"):
        for f in os.listdir(os.path.join(L, "vault", d)):
            if f.endswith(".md") and f[:2] in ("MT", "QP"):
                m[f.split(" - ")[0]] = f[:-3]
    return m


def main():
    os.makedirs(V, exist_ok=True)
    N = notes()
    e = lambda x: re.sub(r"\s+", " ", str(x or "")).strip()
    bid = lambda i: re.sub(r"[^A-Za-z0-9-]", "-", i)

    def lk(ids):
        out = []
        for i in ids or []:
            src = i.split("-")[0]
            out.append("[[%s#^%s|%s]]" % (N.get(src, src), bid(i), i) if src in N else i)
        return ", ".join(out)

    def sl(ss):
        return ", ".join("[[%s|%s]]" % (N[s], s) if s in N else s for s in ss or [])

    idx = ["---", "tags: [index, investors]", "---", "# Investors", "",
           "One synthesis per person, merged across all their mapped appearances (argument maps + papers). Every item links "
           "to verified claims. '(reader)' marks inference beyond what they said.", "",
           "| Investor | Sources | Period | Fingerprint |", "|---|---|---|---|"]
    for p in sorted(glob.glob(os.path.join(L, "investors", "*.json"))):
        d = json.load(open(p))
        nm = d.get("name", os.path.basename(p))
        fp = " ".join("#approach/%s" % (t["tag"] if isinstance(t, dict) else t) for t in d.get("fingerprint", []))
        o = ["---", "tags: [investor]", 'name: "%s"' % nm, "sources: %d" % len(d.get("sources", [])), "---", "# " + nm, "",
             e(d.get("one_paragraph")), "", "**Sources (%d, %s):** %s" % (len(d.get("sources", [])), e(d.get("period")), sl(d.get("sources"))),
             "", "**Fingerprint:** " + fp, ""]
        sec = [("Core beliefs", "core_beliefs", lambda x: "%s _(stated %s×; %s)_" % (e(x.get("belief")), x.get("times_stated", "?"), e(x.get("stable")))),
               ("Mechanisms", "mechanisms", lambda x: "**%s**: %s. Fails when: %s" % (e(x.get("name")), " → ".join(e(s) for s in x.get("chain", [])), e(x.get("fails_when")))),
               ("Playbook", "playbook", lambda x: "[%s] %s. Why: %s" % (x.get("element", ""), e(x.get("rule")), e(x.get("why")))),
               ("Views over time", "views_timeline", lambda x: "(%s) %s. Reasoning: %s" % (e(x.get("as_of")), e(x.get("view")), e(x.get("reasoning")))),
               ("Disagreements", "disagreements", lambda x: "With **%s** on %s: %s vs %s" % (e(x.get("with")), e(x.get("topic")), e(x.get("their_position")), e(x.get("other_position")))),
               ("Internal tensions", "internal_tensions", lambda x: e(x.get("issue"))),
               ("Testable hypotheses", "testable_hypotheses", lambda x: "%s. Data: %s" % (e(x.get("hypothesis")), e(x.get("data_needed"))))]
        for h, k, f in sec:
            items = d.get(k) or []
            if items:
                o.append("## " + h)
                for x in items:
                    o.append("- " + f(x) + (" (%s)" % lk(x.get("claim_ids")) if x.get("claim_ids") else "") +
                             (" — %s" % sl(x.get("sources"))) * bool(x.get("sources") and not x.get("claim_ids")))
                o.append("")
        if d.get("evidence_style"):
            o += ["## Evidence style", e(d["evidence_style"]), ""]
        if d.get("how_views_changed"):
            o += ["## How views changed", e(d["how_views_changed"]), ""]
        for h, k in (("Blind spots (reader)", "blind_spots"), ("Reader inferences", "reader_inferences")):
            if d.get(k):
                o += ["## " + h] + ["- " + e(x) for x in d[k]] + [""]
        open(os.path.join(V, nm + ".md"), "w").write("\n".join(o) + "\n")
        idx.append("| [[%s]] | %d | %s | %s |" % (nm, len(d.get("sources", [])), e(d.get("period")), fp))
    open(os.path.join(V, "00 Investors index.md"), "w").write("\n".join(idx) + "\n")
    print("investors", len(idx) - 8)


if __name__ == "__main__":
    main()
