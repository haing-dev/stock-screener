"""Make the Obsidian vault the single traceable store.
- Fable/Foundation/*.md: foundation notes with every claim id linked to its claim block, blog ids linked to the
  Carver blog digest note, and code refs linked to GitHub at a fixed commit.
- Fable/Foundation/Carver blog digest.md (^B01..), 00 Foundation index.md
- Method/: every spec, unit list, priority list, speaker aliases, cross-check routing, pipeline overview
- _data/: raw JSON bundles (ledger, maps, investors, papers, Fable input packs) + README
usage: python3 build_fable.py <repo_commit>"""
import csv, glob, json, os, re, sys

L = os.path.dirname(os.path.abspath(__file__))
V = os.path.join(L, "vault")
COMMIT = sys.argv[1]
GH = "https://github.com/haing-dev/stock-screener/blob/%s/" % COMMIT
PATHS = {"CHANGES.md": "gm/CHANGES.md", "TESTING_PROTOCOL.md": "docs/research/global_macro/TESTING_PROTOCOL.md",
         "protocol_batch1.md": "docs/research/global_macro/protocol_batch1.md",
         "protocol_batch0.md": "docs/research/global_macro/protocol_batch0.md",
         "protocol_diagnostics.md": "docs/research/global_macro/protocol_diagnostics.md",
         "stats_audit": "docs/research/global_macro/stats_audit_2026-11-02.md",
         "stats_audit_2026-11-02.md": "docs/research/global_macro/stats_audit_2026-11-02.md",
         "gap_review_crosscheck": "docs/research/global_macro/gap_review_crosscheck_2026-10-31.md",
         "gap_review_crosscheck_2026-10-31.md": "docs/research/global_macro/gap_review_crosscheck_2026-10-31.md",
         "BLOOMBERG_PULL_GUIDE.md": "docs/data_requests/BLOOMBERG_PULL_GUIDE.md", "trials.csv": "gm/trials.csv"}
for f in glob.glob("/home/claude/stock-screener/gm/*.py"):
    PATHS[os.path.basename(f)] = "gm/" + os.path.basename(f)
bid = lambda i: re.sub(r"[^A-Za-z0-9-]", "-", i)


def notes():
    m = {}
    for d in ("Sources", "Papers"):
        for f in os.listdir(os.path.join(V, d)):
            if f.endswith(".md") and f[:2] in ("MT", "QP"):
                m[f.split(" - ")[0]] = f[:-3]
    return m


N = notes()


def linkify(t, blog=True, gh=None):
    def cl(m):
        i = m.group(0); src = i.split("-")[0]
        return "[[%s#^%s|%s]]" % (N[src], bid(i), i) if src in N else i
    t = re.sub(r"(?<![\[|#^A-Za-z0-9-])(?:MT\d{3}|QP\d{2})-C\d+-[A-Za-z0-9]+", cl, t)
    t = re.sub(r"(?<![\[|#^A-Za-z0-9/-])(?:MT\d{3}|QP\d{2})(?![-\w])", lambda m: "[[%s|%s]]" % (N[m.group(0)], m.group(0)) if m.group(0) in N else m.group(0), t)
    if blog:
        t = re.sub(r"(?<![\w\[|#^/-])B(0[1-9]|[12]\d|3[01])(?![\w-])", lambda m: "[[Carver blog digest#^B%s|B%s]]" % (m.group(1), m.group(1)), t)

    def code(m):
        name, a, b = m.group(1), m.group(2), m.group(3)
        key = name.split("/")[-1] if name.split("/")[-1] in PATHS else name
        p = PATHS.get(key) or (name if os.path.exists("/home/claude/stock-screener/" + name) else None)
        if not p:
            return m.group(0)
        return "[%s](%s%s#L%s%s)" % (m.group(0), gh or GH, p, a, "-L" + b if b else "")
    t = re.sub(r"(?<![\[/\w])((?:[\w-]+/)*[\w.-]+?(?:\.py|\.md|\.csv)?):(\d+)(?:-(\d+))?(?![\]\w])", code, t)
    return t


def main():
    F = os.path.join(V, "Fable", "Foundation"); os.makedirs(F, exist_ok=True)
    units = json.load(open(os.path.join(L, "foundation", "units.json")))
    # foundation notes
    done = []
    for u in units:
        src = os.path.join(L, "foundation", "%s_%s.md" % (u["id"], re.sub(r"[^A-Za-z0-9]+", "_", u["name"]).strip("_")))
        cands = glob.glob(os.path.join(L, "foundation", u["id"] + "_*.md"))
        if not cands:
            continue
        src = cands[0]
        name = "%s %s" % (u["id"], os.path.basename(src)[4:-3].replace("_", " "))
        body = open(src).read()
        if u["id"] == "U01":   # F1 cites QP01 claims by short id (C05-1)
            body = re.sub(r"(?<![\w-])C(\d{2})-([0-9]+|[A-Z][0-9]+)(?![\w-])", r"QP01-C\1-\2", body)
        head = ["---", "tags: [fable, foundation]", "unit: %s" % u["id"], 'name: "%s"' % u["name"], "model: %s, effort max" % (u.get("model") or "fable"),
                "inputs: _data/foundation_packs/%s.json" % u["id"], "code_commit: %s" % (u.get("code_commit") or COMMIT)[:7], "---",
                "> Claim ids link to the verbatim quote in its source note; B-ids link to the [[Carver blog digest]]; code refs link to GitHub at commit %s (the repo as it was when this note was written). Brief: [[FOUNDATION_SPEC]]." % (u.get("code_commit") or COMMIT)[:7], ""]
        open(os.path.join(F, name + ".md"), "w").write("\n".join(head) + linkify(body, gh="https://github.com/haing-dev/stock-screener/blob/%s/" % (u.get("code_commit") or COMMIT)) + "\n")
        done.append((u, name))
    # blog digest
    dg = json.load(open(os.path.join(L, "fable", "carver_blog_digest.json")))
    o = ["---", "tags: [source, blog, carver]", "---", "# Carver blog digest (qoppac.blogspot.com)", "",
         "31 posts. **Model-written extracts of the pages (WebFetch), not raw text: numbers and quotes are likely but unverified.** "
         "B12 has numbers Carver later corrected (B13). Used by [[U02 Rob Carver]].", ""]
    for b in dg:
        o += ["## %s %s" % (b["post_id"], b["title"]), "[%s](%s) · %s · topic: %s" % (b["date"], b["url"], b["date"], b["topic"]), ""]
        for k, h in (("key_rules", "Rules"), ("numbers", "Numbers"), ("caveats", "Caveats")):
            v = b.get(k) or []
            if isinstance(v, str): v = [v]
            if v: o += ["**%s:**" % h] + ["- " + str(x) for x in v]
        if b.get("reasoning"): o += ["", "**Reasoning:** " + str(b["reasoning"])]
        if b.get("quote"): o += ["", "> " + str(b["quote"])]
        o += ["^" + b["post_id"], ""]
    open(os.path.join(F, "Carver blog digest.md"), "w").write("\n".join(o) + "\n")
    # foundation index
    idx = ["---", "tags: [index, fable]", "---", "# Foundation (Fable max judgement notes)", "",
           "Order and scope: [[Foundation units]]. Brief: [[FOUNDATION_SPEC]]. Each note's exact input is in `_data/foundation_packs/`. "
           "U01 is the earlier F1 note (same content as [[F1 - Economic Trend (AQR) judgement]]).", "",
           "| Unit | Note | Topic |", "|---|---|---|"]
    names = dict((u["id"], n) for u, n in done)
    for u in units:
        idx.append("| %s | %s | %s |" % (u["id"], "[[%s]]" % names[u["id"]] if u["id"] in names else "_pending_", u.get("topic", "")))
    open(os.path.join(F, "00 Foundation index.md"), "w").write("\n".join(idx) + "\n")

    # Method
    M = os.path.join(V, "Method"); os.makedirs(M, exist_ok=True)
    specs = {"EXTRACT_SPEC": "EXTRACT_SPEC.md", "CROSSCHECK_SPEC": "CROSSCHECK_SPEC.md", "TRANSCRIPT_MAP_SPEC": "TRANSCRIPT_MAP_SPEC.md",
             "INVESTOR_SYNTH_SPEC": "INVESTOR_SYNTH_SPEC.md", "PAPER_SPEC": "papers/PAPER_SPEC.md", "F1_SPEC": "fable/F1_SPEC.md",
             "FOUNDATION_SPEC": "foundation/FOUNDATION_SPEC.md", "VARIANTS": "/home/claude/stock-screener/docs/research/fable/foundation/VARIANTS.md", "WORKFLOW": "/home/claude/stock-screener/docs/research/WORKFLOW.md", "X_EXTRACT_BRIEF": "X_EXTRACT_BRIEF.md"}
    for n, p in specs.items():
        open(os.path.join(M, n + ".md"), "w").write("---\ntags: [method, spec]\nfile: %s\n---\n" % p + open(os.path.join(L, p)).read())
    u = ["---", "tags: [method]", "---", "# Foundation units", "", "| Unit | Name | Inputs | Topic |", "|---|---|---|---|"]
    for x in units:
        ins = ", ".join(["investor " + s for s in x.get("investors", [])] + x.get("maps", []) + x.get("papers", []) + [os.path.basename(e) for e in x.get("extra", [])])
        u.append("| %s | %s | %s | %s |" % (x["id"], x["name"], linkify(ins, blog=False), x.get("topic", "")))
    open(os.path.join(M, "Foundation units.md"), "w").write("\n".join(u) + "\n")
    rows = list(csv.reader(open(os.path.join(L, "transcript_priority.csv"))))
    t = ["---", "tags: [method]", "---", "# Transcript priority (map tiers)", "", "| " + " | ".join(rows[0]) + " |", "|" + "---|" * len(rows[0])]
    t += ["| " + " | ".join(linkify(c.replace("|", "/"), blog=False) for c in r) + " |" for r in rows[1:]]
    open(os.path.join(M, "Transcript priority.md"), "w").write("\n".join(t) + "\n")
    al = json.load(open(os.path.join(L, "speaker_aliases.json")))
    a = ["---", "tags: [method]", "---", "# Speaker aliases (caption spellings)", "", "| Caption form | Resolved to |", "|---|---|"]
    def walk(d, pre=""):
        for k, v in (d.items() if isinstance(d, dict) else []):
            if isinstance(v, dict): walk(v, k)
            else: a.append("| %s | %s |" % (k, (pre + ": " if pre else "") + str(v).replace("|", "/")))
    walk(al)
    open(os.path.join(M, "Speaker aliases.md"), "w").write("\n".join(a) + "\n")
    ox = open(os.path.join(L, "opus_cross_ids.txt")).read().split()
    open(os.path.join(M, "Cross-check routing.md"), "w").write(
        "---\ntags: [method]\n---\n# Cross-check routing\n\nSecond reader per transcript: Opus high for these %d (incl. pilot); Sonnet xhigh for all others.\n\n%s\n"
        % (len(ox), ", ".join(linkify(i, blog=False) for i in ox)))
    ov = """---
tags: [method, index]
---
# Method: how every note was made (traceability)

**From 2026-11-11 all new work follows [[WORKFLOW]] (pod shop workflow v2.0: steps, agent per step, tests, budget).**
The steps below describe how the existing notes were made.

1. **Transcripts** (originals in the Macro Transcripts folder) are split into ~700-word chunks [Cnn].
2. **Layer 0 extraction** (Sonnet, [[EXTRACT_SPEC]]) -> claims with verbatim quotes; **cross-check** by a second blind
   reader ([[CROSSCHECK_SPEC]]; routing in [[Cross-check routing]]); a script checks every quote against the chunk text
   (exact / other_chunk / near / not_found). Result: notes in `Sources/`, one block id per claim (^MTnnn-Cxx-n).
3. **Papers** (Quant folder, [[PAPER_SPEC]]): Sonnet extraction + Opus blind second read with reasoning map -> `Papers/`.
4. **Argument maps** per transcript (Sonnet, [[TRANSCRIPT_MAP_SPEC]], order in [[Transcript priority]]), rendered
   inside each Sources note under "Argument map"; every element cites claim ids.
5. **Investor syntheses** across appearances (Sonnet, [[INVESTOR_SYNTH_SPEC]]) -> `Investors/`; name variants in [[Speaker aliases]].
6. **Fable judgement** ([[F1_SPEC]], [[FOUNDATION_SPEC]]; units in [[Foundation units]]) -> `Fable/Foundation/`.
   Each note's exact input is saved in `_data/foundation_packs/<unit>.json`.

**Trace any statement:** Fable note -> claim id link -> claim block (quote + chunk) in the Sources/Papers note ->
chunk in the original transcript or PDF page. Code refs link to GitHub at a fixed commit.
**Raw data:** `_data/` (see its README). Same files are on the macro-vault branch of haing-dev/stock-screener.
"""
    open(os.path.join(M, "00 Method.md"), "w").write(ov)

    # _data bundles
    D = os.path.join(V, "_data"); os.makedirs(os.path.join(D, "foundation_packs"), exist_ok=True)
    def bundle(pat, out):
        b = {os.path.basename(p)[:-5]: json.load(open(p)) for p in sorted(glob.glob(pat)) if not p.endswith(".diff.json")}
        json.dump(b, open(os.path.join(D, out), "w"), ensure_ascii=False)
        return len(b)
    n = {"ledger_transcripts.json": bundle(os.path.join(L, "ledger", "MT*.json"), "ledger_transcripts.json"),
         "maps_transcripts.json": bundle(os.path.join(L, "maps", "MT*.json"), "maps_transcripts.json"),
         "investors.json": bundle(os.path.join(L, "investors", "*.json"), "investors.json"),
         "papers_merged.json": bundle(os.path.join(L, "papers", "merged", "QP*.json"), "papers_merged.json")}
    for p in glob.glob(os.path.join(L, "foundation", "packs", "*.json")):
        json.dump(json.load(open(p)), open(os.path.join(D, "foundation_packs", os.path.basename(p)), "w"), ensure_ascii=False)
    json.dump(dg, open(os.path.join(D, "carver_blog_digest.json"), "w"), ensure_ascii=False, indent=1)
    open(os.path.join(D, "README.md"), "w").write(
        "---\ntags: [data]\n---\n# Raw data (JSON)\n\nEach file is a dict keyed by source id (MTnnn / QPnn / investor slug).\n\n" +
        "\n".join("- `%s`: %d entries" % (k, v) for k, v in n.items()) +
        "\n- `foundation_packs/Uxx.json`: the exact input given to Fable for each foundation unit\n- `carver_blog_digest.json`: B01-B31\n\n"
        "Built %s from the macro-vault branch working copy; code commit %s.\n" % (__import__("datetime").date.today(), COMMIT[:7]))
    print("foundation notes", len(done), "| method notes", len(os.listdir(M)), "| data", n)


if __name__ == "__main__":
    main()
