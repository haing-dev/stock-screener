"""Layer 0 merge + checks + Obsidian vault builder.

python3 build.py            -> ledger/MTnnn.json (merged), status.json, vault/ (Obsidian notes)
Merged ledger = Sonnet claims + Opus cross-check additions (or, for the 5 pilot docs, Opus blind-read claims that the
Sonnet list does not already contain). Every quote is checked against its chunk; corrections are attached to claims.
"""
import json, os, re, unicodedata, collections

L = os.path.dirname(os.path.abspath(__file__))
STOP = set("the a an of to and or in on for is are be that this it as with by at from was were has have not but if than "
           "then so we they you i he she its their our will would can could should may might more less very just".split())
MECH = ["slow_reaction", "risk_premium", "overshoot", "cycle_persistence", "liquidity_flows", "policy_reaction",
        "crowding_positioning", "seasonality", "fiscal_debt", "structural_shift", "risk_management", "research_method",
        "behavioral"]
MECH_TXT = {"slow_reaction": "Slow reaction (trend)", "risk_premium": "Risk premium (carry, term premium)",
            "overshoot": "Overshoot (value, mean reversion)", "cycle_persistence": "Cycle persistence (economic trend, regimes)",
            "liquidity_flows": "Liquidity and flows", "policy_reaction": "Policy reaction (central banks, governments)",
            "crowding_positioning": "Crowding and positioning", "seasonality": "Seasonality",
            "fiscal_debt": "Fiscal and debt dynamics", "structural_shift": "Structural shifts",
            "risk_management": "Risk management and sizing", "research_method": "Research and testing method",
            "behavioral": "Behavioural", "new": "New mechanisms (unclassified)"}


def norm(s):
    s = unicodedata.normalize("NFKC", s or "").replace("’", "'").replace("‘", "'")
    return re.findall(r"[a-z0-9%$']+", s.replace("“", '"').replace("”", '"').lower())


def tri(t):
    return set(zip(t, t[1:], t[2:]))


def words(s):
    return {w for w in norm(s) if w not in STOP and len(w) > 2}


def chunks(sid):
    t = open(os.path.join(L, "docs", sid + ".txt")).read()
    head = t.split("\n---\n", 1)[0]
    parts = re.split(r"\n\[(C\d+)\]\n", t)
    return head, {parts[i]: parts[i + 1] for i in range(1, len(parts) - 1, 2)}


def qstatus(q, ch, allc):
    qt = " ".join(norm(q))
    if qt and qt in " ".join(norm(ch)):
        return "exact"
    whole = " ".join(norm(" ".join(allc.values())))
    if qt and qt in whole:
        return "other_chunk"
    g = tri(norm(q))
    return "near" if g and len(g & tri(whole.split())) / len(g) >= 0.6 else "not_found"


def same(a, b):
    try:
        if abs(int(a["chunk"][1:]) - int(b["chunk"][1:])) > 1:
            return False
    except Exception:
        pass
    qa, qb = tri(norm(a.get("quote"))), tri(norm(b.get("quote")))
    jq = len(qa & qb) / len(qa | qb) if qa and qb else 0
    wa, wb = words(a.get("claim", "")), words(b.get("claim", ""))
    jw = len(wa & wb) / len(wa | wb) if wa and wb else 0
    return max(1.5 * jq, jw) >= 0.25


def mech_key(m):
    m = (m or "").strip()
    return m if m in MECH else "new"


def load(p):
    try:
        return json.load(open(p))
    except Exception:
        return None


OPUS_X = set(open(os.path.join(L, "opus_cross_ids.txt")).read().split())


def merge(sid):
    s = load(os.path.join(L, "sonnet", sid + ".json"))
    if not s:
        return None
    claims = [dict(c, reader="sonnet") for c in s.get("claims", [])]
    x = load(os.path.join(L, "cross", sid + ".json"))
    b = load(os.path.join(L, "opus_blind_pilot", sid + ".blind.json"))
    added, corr, est, mode = [], [], None, None
    if x:
        xm = "opus" if sid in OPUS_X else "sonnet-xhigh"
        mode = xm + " cross-check"
        added = [dict(c, reader=xm) for c in x.get("added_claims", [])]
        corr = x.get("corrections", [])
        est = x.get("completeness_estimate")
    elif b:
        mode = "opus blind read (pilot)"
        added = [dict(c, reader="opus", claim_id=c["claim_id"].replace("-C", "-C", 1) + "b")
                 for c in b.get("claims", []) if not any(same(c, d) for d in claims)]
    cmap = {c["claim_id"]: c for c in corr if c.get("claim_id")}
    for c in claims:
        if c["claim_id"] in cmap:
            c["correction"] = cmap[c["claim_id"]]
    head, ch = chunks(sid)
    allc = claims + added
    for c in allc:
        c["quote_check"] = qstatus(c.get("quote", ""), ch.get(c.get("chunk", ""), ""), ch)
    meta = dict(re.findall(r"^([a-z ]+): (.*)$", head, re.M))
    title = head.splitlines()[0].lstrip("# ").strip()
    out = {"source_id": sid, "title": title, "meta": meta, "speakers": s.get("speakers", []),
           "summary": s.get("summary", ""), "approach_tags": s.get("approach_tags", []),
           "coverage": s.get("coverage", []), "chunks": len(ch), "crosscheck": mode, "completeness_estimate": est,
           "claims": allc, "n_sonnet": len(claims), "n_opus_added": len(added), "n_corrections": len(corr)}
    os.makedirs(os.path.join(L, "ledger"), exist_ok=True)
    json.dump(out, open(os.path.join(L, "ledger", sid + ".json"), "w"), indent=1, ensure_ascii=False)
    return out


def safe(s, n=90):
    s = re.sub(r'[\\/:*?"<>|#^\[\]]', "", s).strip()
    return re.sub(r"\s+", " ", s)[:n].rstrip(" .")


def esc(s):
    return (s or "").replace("\n", " ").strip()


def build_vault(ledgers):
    V = os.path.join(L, "vault")
    for d in ("Sources", "Mechanisms"):
        os.makedirs(os.path.join(V, d), exist_ok=True)
    by_mech = collections.defaultdict(list)
    rows = []
    for led in ledgers:
        sid = led["source_id"]
        fname = "%s - %s" % (sid, safe(led["title"]))
        m = led["meta"]
        fm = ["---", "source_id: %s" % sid, 'title: "%s"' % led["title"].replace('"', "'"),
              "date: %s" % m.get("upload date", ""), 'channel: "%s"' % m.get("channel", "").replace('"', "'"),
              "url: %s" % m.get("url", ""), "words: %s" % m.get("words", ""),
              "claims: %d" % len(led["claims"]), "added_by_crosscheck: %d" % led["n_opus_added"],
              "corrections: %d" % led["n_corrections"], 'crosscheck: "%s"' % (led["crosscheck"] or "pending"),
              "speakers: [%s]" % ", ".join('"%s"' % x.replace('"', "'") for x in led["speakers"]),
              "tags: [source, layer0]", "---"]
        body = ["# %s" % led["title"], "", "**Speakers:** " + "; ".join(led["speakers"]), "",
                "**Summary:** " + esc(led["summary"]), "", "**Approach:** " + ", ".join(led["approach_tags"]), ""]
        if led["completeness_estimate"]:
            body += ["**Cross-check completeness estimate of first read:** " + esc(str(led["completeness_estimate"])), ""]
        body += ["## Coverage", "", "| Chunk | Claims | Note |", "|---|---|---|"]
        for c in led["coverage"]:
            body.append("| %s | %s | %s |" % (c.get("chunk"), c.get("claims"), esc(c.get("note")).replace("|", "/")))
        body += ["", "## Claims", ""]
        bychunk = collections.defaultdict(list)
        for c in led["claims"]:
            bychunk[c.get("chunk", "C??")].append(c)
        for chk in sorted(bychunk, key=lambda k: int(re.sub(r"\D", "", k) or 0)):
            body.append("### %s" % chk)
            for c in bychunk[chk]:
                mk = mech_key(c.get("mechanism"))
                bid = re.sub(r"[^A-Za-z0-9-]", "-", c["claim_id"])
                flags = []
                if c["reader"] != "sonnet":
                    flags.append("added by %s cross-check" % c["reader"])
                if c.get("quote_check") != "exact":
                    flags.append("quote " + c.get("quote_check", "?"))
                if str(c.get("time_bound", "")).startswith("yes"):
                    flags.append("time-bound view")
                line = "- **%s** %s  #mech/%s%s" % (esc(c.get("speaker")), esc(c.get("claim")), mk,
                                                   (" _(%s)_" % ", ".join(flags)) if flags else "")
                det = []
                for k, lab in (("indicator", "indicator"), ("asset_class", "asset"), ("direction", "direction"),
                               ("horizon", "horizon"), ("conditions", "conditions"), ("testable", "testable"),
                               ("speaker_confidence", "confidence")):
                    if esc(c.get(k)) and esc(c.get(k)).lower() not in ("unspecified", "empty", ""):
                        det.append("%s: %s" % (lab, esc(c.get(k))))
                body.append(line)
                body.append("  > %s" % esc(c.get("quote")))
                if det:
                    body.append("  " + " · ".join(det))
                if c.get("correction"):
                    body.append("  **Correction (cross-check):** %s → %s" % (esc(c["correction"].get("issue")),
                                                                      esc(c["correction"].get("fix"))))
                body.append("  ^%s" % bid)
                by_mech[mk].append((fname, bid, esc(c.get("claim")), esc(c.get("speaker")), c.get("mechanism", "")))
            body.append("")
        open(os.path.join(V, "Sources", fname + ".md"), "w").write("\n".join(fm + body) + "\n")
        rows.append((sid, fname, m.get("upload date", ""), len(led["claims"]), led["n_opus_added"], led["crosscheck"] or "pending"))
    for mk, items in by_mech.items():
        lines = ["---", "tags: [mechanism]", "---", "# %s" % MECH_TXT.get(mk, mk), "",
                 "%d claims from %d sources. Each line links to the claim inside its source note." % (
                     len(items), len({i[0] for i in items})), ""]
        cur = None
        for fname, bid, claim, spk, raw in sorted(items):
            if fname != cur:
                lines += ["", "## [[%s]]" % fname]
                cur = fname
            extra = " (%s)" % raw if mk == "new" else ""
            lines.append("- [[%s#^%s|%s]] — %s%s" % (fname, bid, bid, claim, extra))
        open(os.path.join(V, "Mechanisms", safe(MECH_TXT.get(mk, mk), 60) + ".md"), "w").write("\n".join(lines) + "\n")
    idx = ["---", "tags: [index]", "---", "# Macro Transcripts: Layer 0 ledger", "",
           "Every claim from every transcript, with verbatim quotes (script-checked) and a completeness cross-check (Opus 5.5 high for the first 95 sources, Sonnet 5.5 xhigh for the rest; column below).",
           "Mechanism pages: " + ", ".join("[[%s]]" % safe(MECH_TXT[k], 60) for k in MECH_TXT if k in by_mech), "",
           "| ID | Source | Date | Claims | Added by cross-check | Cross-check |", "|---|---|---|---|---|---|"]
    for sid, fname, d, n, a, x in rows:
        idx.append("| %s | [[%s]] | %s | %d | %d | %s |" % (sid, fname, d, n, a, x))
    open(os.path.join(V, "00 Index.md"), "w").write("\n".join(idx) + "\n")


def main():
    man = json.load(open(os.path.join(L, "manifest.json")))
    leds, stat = [], collections.Counter()
    for m in man:
        led = merge(m["source_id"])
        if not led:
            stat["pending"] += 1
            continue
        leds.append(led)
        stat["merged"] += 1
        stat["crosschecked"] += led["crosscheck"] is not None
        stat["claims"] += len(led["claims"])
        stat["opus_added"] += led["n_opus_added"]
        for c in led["claims"]:
            stat["quote_" + c["quote_check"]] += 1
        covered = {c.get("chunk") for c in led["coverage"]}
        stat["coverage_incomplete"] += len(covered) < led["chunks"]
    build_vault(leds)
    json.dump(dict(stat), open(os.path.join(L, "status.json"), "w"), indent=1)
    print(dict(stat))


if __name__ == "__main__":
    main()
