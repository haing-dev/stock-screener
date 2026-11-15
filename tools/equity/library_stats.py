"""Counts for the transcript library built by DocProcessor (G:\\My Drive\\Transcripts\\Processed Transcripts).

Reads only `_system/manifest.json` (titles, speakers, dates, word counts: no transcript text) and prints a
Markdown note with the numbers the equity plan relies on. The split into document kinds and the investor list are
HEURISTICS from the catalog fields (role words next to each speaker); step E0.1 replaces them with a coded inventory.

    python3 tools/equity/library_stats.py PATH/TO/_system/manifest.json [FOLDER] > note.md
"""
import collections
import json
import re
import sys

INV = re.compile(r"fund|capital|partners|asset management|portfolio manager|investor|hedge|\bcio\b|chief investment|"
                 r"advisors|investment|analyst|trader|wealth|equity|endowment|allocator", re.I)
EXE = re.compile(r"\bceo\b|chief executive|founder|president|chairman|cfo|coo|cto", re.I)
SEC = re.compile(r"not present|cited|discussed|case study|\bclip|not a (live )?speaker|book under review|referenced|"
                 r"subject of", re.I)
HOST = re.compile(r"\bhost\b|interviewer|moderator", re.I)
HOSTS = {"Clay Finck", "Clay Fink", "William Green", "Stig Brodersen", "Kyle Grieve", "Wilfred Frost",
         "Barry Ritholtz", "Nicolai Tangen", "Trey Lockerbie", "Brad Gerstner", "Bill Gurley", "Ted Seides",
         "Patrick O'Shaughnessy", "Host", "Amir", "Ethan", "Interviewer", "Stig", "Clay", "Kyle", "Owen", "Simon",
         "host", "unnamed host", "Unnamed host", "Podcast host"}
ALIAS = {"Toby": "Tobias Carlisle", "Toby Carlisle": "Tobias Carlisle", "Hari": "Hari Ramachandra",
         "Rob Vinall": "Robert Vinall", "Nikolai Tangen": "Nicolai Tangen", "Nikolai": "Nicolai Tangen",
         "Sir Chris Hohn": "Chris Hohn"}
TECH = {"valuation": r"valuation|intrinsic value|dcf|discounted cash|multiple|owner earnings|reverse dcf|"
                     r"margin of safety",
        "analysis and accounting": r"accounting|financial statement|moat|competitive advantage|unit economics|roic|"
                                   r"return on (invested )?capital|checklist|due diligence|scuttlebutt",
        "screening and idea sourcing": r"screen|idea generation|idea sourcing|quant|factor|magic formula|backtest",
        "portfolio construction and sizing": r"portfolio construction|position siz|concentrat|diversif|kelly|"
                                             r"portfolio management|sell discipline|when to sell",
        "risk management": r"risk management|drawdown|hedg|leverage|permanent loss|tail risk|stop.?loss",
        "short selling": r"short sell|short-sell|shorting|short thesis|short book|long.?short"}


# Stricter patterns for the same areas: whole phrases, no bare "multiple", "quant", "leverage", "hedg" or "concentrat"
# (the loose patterns also match "hedge fund", "multiple times", and so on).
STRICT = {"valuation": r"valuation|intrinsic value|\bdcf\b|discounted cash|owner earnings|margin of safety|"
                       r"earnings yield|free cash flow yield",
          "analysis and accounting": r"accounting|financial statements?|\bmoats?\b|competitive advantage|"
                                     r"unit economics|\broic\b|return on (invested )?capital|checklist|"
                                     r"due diligence|scuttlebutt",
          "screening and idea sourcing": r"\bscreen(s|ing|er|ers)?\b|idea generation|idea sourcing|magic formula|"
                                         r"backtest|quantitative (value|investing)|factor investing",
          "portfolio construction and sizing": r"portfolio construction|position siz|concentrated portfolio|"
                                               r"diversification|kelly|portfolio management|sell discipline|"
                                               r"when to sell",
          "risk management": r"risk management|drawdowns?|hedging|permanent (capital )?loss|tail risk|stop.?loss",
          "short selling": r"short sell|short-sell|shorting|short thesis|short book|long.?short"}


def split_speakers(s):
    out, depth, cur = [], 0, ""
    for c in s:
        if c == "(":
            depth += 1
        if c == ")":
            depth = max(0, depth - 1)
        if c == ";" and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += c
    if cur.strip():
        out.append(cur.strip())
    return out


def parse(d):
    """-> (investors present, executives, secondary figures, other guests) for one document."""
    inv, exe, sec, oth = [], [], [], []
    for x in split_speakers((d.get("fm") or {}).get("speakers", "")):
        m = re.match(r"^(.*?)\s*\((.*)\)\s*$", x)
        name, role = ((m.group(1), m.group(2)) if m else (x, ""))
        name = ALIAS.get(name.strip(), name.strip())
        if not name or HOST.search(role) or name in HOSTS:
            continue
        if SEC.search(role):
            sec.append(name)
        elif INV.search(role):
            inv.append(name)
        elif EXE.search(role):
            exe.append(name)
        else:
            oth.append(name)
    return inv, exe, sec, oth


def main(path, folder="General Transcripts"):
    m = json.load(open(path, encoding="utf-8"))
    alld = list(m["docs"].values())
    p = print
    p("# Transcript library: inventory numbers (%s)\n" % folder)
    p("Source: `_system/manifest.json` of the processed library (metadata only, no transcript text). Script: "
      "`tools/equity/library_stats.py`. Document kinds and the investor list are heuristics from the catalog's "
      "speaker and role fields; step E0.1 of the plan replaces them with a coded inventory.\n")
    p("## Whole library\n\n| Folder | Documents | Words (M) | Tokens (M) |\n|---|---|---|---|")
    f = collections.defaultdict(lambda: [0, 0, 0])
    for d in alld:
        k = d["src"].split("/")[0]
        f[k][0] += 1
        f[k][1] += d.get("words", 0)
        f[k][2] += d.get("tokens", 0)
    for k, (n, w, t) in sorted(f.items(), key=lambda kv: -kv[1][0]):
        p("| %s | %d | %.2f | %.2f |" % (k, n, w / 1e6, t / 1e6))
    p("| Total | %d | %.2f | %.2f |" % (len(alld), sum(v[1] for v in f.values()) / 1e6,
                                        sum(v[2] for v in f.values()) / 1e6))
    docs = [d for d in alld if d["src"].startswith(folder + "/")]
    sub = collections.Counter("/".join(d["src"].split("/")[1:-1]) or "(top level)" for d in docs)
    p("\n## %s: %d documents, %.2fM words, %.2fM tokens\n" % (folder, len(docs), sum(d["words"] for d in docs) / 1e6,
                                                             sum(d["tokens"] for d in docs) / 1e6))
    p("Subfolders: " + "; ".join("%s %d" % kv for kv in sub.most_common()) + ".")
    w = sorted(d["words"] for d in docs)
    p("Words per document: median %d, 10th percentile %d, 90th percentile %d." % (w[len(w) // 2], w[len(w) // 10],
                                                                                 w[9 * len(w) // 10]))
    yr = collections.Counter(((d.get("fm") or {}).get("date") or "unknown")[:4] for d in docs)
    p("\nBy year of the talk: " + "; ".join("%s %d" % kv for kv in sorted(yr.items())) + ".")
    recent = sum(n for y, n in yr.items() if y.isdigit() and int(y) >= 2022)
    p("Dated 2022 or later: %d of %d." % (recent, len(docs)))
    ch = collections.Counter((d.get("meta") or {}).get("channel", "") or "(none)" for d in docs)
    p("\nChannels (%d): " % len(ch) + "; ".join("%s %d" % kv for kv in ch.most_common(12)) + "; others %d."
      % sum(n for _, n in ch.most_common()[12:]))
    kinds = collections.Counter()
    by = collections.defaultdict(list)
    for i, d in enumerate(docs):
        inv, exe, sec, oth = parse(d)
        kinds["investor present" if inv else "host only, book or case study" if (sec and not exe and not oth)
              or not (exe or oth) else "company executive or founder" if exe else "author, academic or other guest"] += 1
        for n in inv:
            by[n].append(i)
    p("\n## Document kinds (heuristic)\n\n| Kind | Documents |\n|---|---|")
    for k, n in kinds.most_common():
        p("| %s | %d |" % (k, n))
    rank = sorted(by.items(), key=lambda kv: (-len(kv[1]), -sum(docs[i]["words"] for i in kv[1])))
    p("\n## Investors present (heuristic, a few aliases merged)\n")
    p("Distinct names: %d; appearing once: %d; twice or more: %d; three times or more: %d.\n"
      % (len(rank), sum(1 for _, L in rank if len(L) == 1), sum(1 for _, L in rank if len(L) >= 2),
         sum(1 for _, L in rank if len(L) >= 3)))
    p("| Investors taken (most documents first) | Documents covered | Words (M) | Tokens (M) |\n|---|---|---|---|")
    for n in (20, 40, 60, 100, len(rank)):
        ids = set(i for _, L in rank[:n] for i in L)
        p("| %d | %d | %.2f | %.2f |" % (n, len(ids), sum(docs[i]["words"] for i in ids) / 1e6,
                                         sum(docs[i]["tokens"] for i in ids) / 1e6))
    p("\nMost frequent: " + "; ".join("%s %d" % (n, len(L)) for n, L in rank[:40]) + ".")
    p("\n## Technique topics in the tags and one-line summaries (a document can count in several)\n\n"
      "Loose = any word match (also catches 'hedge fund', 'multiple times'); strict = whole phrases only.\n\n"
      "| Area | Documents (loose) | Documents (strict) |\n|---|---|---|")
    tc, ts, anyt, anys = collections.Counter(), collections.Counter(), 0, 0
    for d in docs:
        fm = d.get("fm") or {}
        txt = (fm.get("topics", "") + " " + fm.get("one_line", "")).lower()
        hit = hs = False
        for k in TECH:
            if re.search(TECH[k], txt):
                tc[k] += 1
                hit = True
            if re.search(STRICT[k], txt):
                ts[k] += 1
                hs = True
        anyt += hit
        anys += hs
    for k, n in tc.most_common():
        p("| %s | %d | %d |" % (k, n, ts[k]))
    p("| any of these | %d | %d |" % (anyt, anys))


if __name__ == "__main__":
    main(*sys.argv[1:3])
