"""Stage 2 prep: download the latest annual report for shortlisted companies and build an
'evidence pack' for qualitative moat scoring (by Claude, another LLM, or you).

Design choices (from the interviews):
  * Blind by default (Perlmutter's blind analysis): company name and ticker are replaced by
    [COMPANY] and files are coded C01, C02...; the key is in a separate file. No prices included.
  * Verifiable: the full cleaned text is saved next to each evidence pack so every quote the
    reviewer uses can be checked word-for-word (see quotes.py).
"""
import gzip
import json
import os
import re
import shutil
import zipfile
from datetime import date

from .config import CACHE_DIR, OUTPUT_DIR, ROOT
from .sec import NotFound, doc_url

INLINE_TAGS = {"span", "a", "b", "i", "u", "em", "strong", "font", "sup", "sub", "small", "big", "s", "strike"}

SECTION_ITEMS = {
    "10-K": {"business": "1", "risk": "1A", "mdna": "7"},
    "20-F": {"business": "4", "risk": "3", "mdna": "5"},
}
ITEM_RE = re.compile(r"^\s*item\s*(\d{1,2})([a-d])?(?![a-z0-9])\s*[\.\:\-\u2013\u2014]?\s*(.{0,120})$", re.I)

KEYWORDS = [
    r"pric(e|es|ing|ed)", r"market share", r"compet(e|es|ition|itor|itors|itive)", r"switching",
    r"renewal|retention|recurring|subscription", r"long-term (contract|agreement)s?", r"patent|intellectual property|proprietary",
    r"network effect|network", r"scale|largest|leading|market leader|number one|no\. 1", r"barrier", r"regulat",
    r"installed base|aftermarket|mission[- ]critical", r"substitut|disrupt|obsolete", r"artificial intelligence|\bai\b",
    r"customer concentration|largest customer", r"exclusive|sole source|only (provider|supplier|company)",
    r"duopoly|oligopoly|two (major|large) (competitors|players)", r"brand", r"cost advantage|low[- ]cost",
]
KW = [re.compile(k, re.I) for k in KEYWORDS]
BUDGET = {"business": 6000, "risk": 1500, "mdna": 2000}


def html_to_text(html):
    from bs4 import BeautifulSoup
    try:
        soup = BeautifulSoup(html, "lxml")
    except Exception:  # noqa: BLE001
        soup = BeautifulSoup(html, "html.parser")
    for t in soup.find_all(["script", "style", "head", "title"]):
        t.decompose()
    for t in soup.find_all(lambda tag: tag.name and tag.name.lower() in ("ix:header", "ix:hidden")):
        t.decompose()
    for t in soup.find_all(style=re.compile(r"display\s*:\s*none", re.I)):
        t.decompose()
    for t in soup.find_all("table"):
        t.decompose()
    for br in soup.find_all("br"):
        br.replace_with("\n")
    for t in soup.find_all(lambda tag: tag.name and (tag.name.lower() in INLINE_TAGS or tag.name.lower().startswith("ix:"))):
        t.unwrap()
    soup.smooth()
    raw = soup.get_text("\n")
    lines = []
    for line in raw.split("\n"):
        line = re.sub(r"[ \t\u00a0\u2009\u200b\u202f]+", " ", line).strip()
        if line:
            lines.append(line)
    return "\n".join(lines)


def find_sections(text, form):
    lines = text.split("\n")
    heads = []
    for i, line in enumerate(lines):
        if len(line) > 160:
            continue
        m = ITEM_RE.match(line)
        if m:
            heads.append((i, (m.group(1) + (m.group(2) or "")).upper()))
    items = SECTION_ITEMS.get(form.split("/")[0], SECTION_ITEMS["10-K"])
    out = {}
    for name, key in items.items():
        best = None
        for j, (i, k) in enumerate(heads):
            if k != key:
                continue
            nxt = next((i2 for i2, k2 in heads[j + 1:] if k2 != key), len(lines))
            length = sum(len(x) for x in lines[i:nxt])
            if best is None or length > best[0]:
                best = (length, i, nxt)
        if best and best[0] > 2000:
            out[name] = "\n".join(lines[best[1]:best[2]])
    return out


def _words(s):
    return len(s.split())


def take_words(text, n):
    out, count = [], 0
    for para in text.split("\n"):
        w = _words(para)
        if count + w > n:
            break
        out.append(para)
        count += w
    return "\n".join(out)


def select_paragraphs(text, budget):
    paras = [p for p in text.split("\n") if _words(p) >= 20]
    scored = []
    for idx, p in enumerate(paras):
        hits = sum(1 for k in KW if k.search(p))
        if hits >= 2:
            scored.append((hits, idx, p))
    scored.sort(key=lambda x: (-x[0], x[1]))
    chosen, count = [], 0
    for hits, idx, p in scored:
        w = _words(p)
        if count + w > budget:
            continue
        chosen.append((idx, p))
        count += w
    return "\n\n".join(p for _, p in sorted(chosen))


def core_name(name):
    n = re.sub(r"\s*/.*$", "", name or "")          # drop SEC suffixes like /DE/ or /NEW/
    n = re.sub(r"[,\.]", " ", n)
    n = re.sub(r"\b(inc|incorporated|corp|corporation|co|company|ltd|limited|plc|holdings?|group|n ?v|s ?a|"
               r"ag|se|sa|nv|the|class [a-c]|/de/|/new/|de)\b", " ", n, flags=re.I)
    n = re.sub(r"\s+", " ", n).strip()
    return n


def _word_re(w):
    w = re.escape(w)
    if len(w) > 3 and w.lower().endswith("s"):
        w = w[:-1] + "[\'\u2019]?s"   # MOODYS -> Moody's
    return w


SUFFIX_RE = (r"(?:[\s,]+(?:inc|incorporated|corp|corporation|co|company|ltd|limited|plc|n\.?v|s\.?a|ag|se|"
             r"holdings?|group)\b\.?)*")


def redact(text, name, tickers):
    """Replace the company's name (with legal suffixes, possessive) and ticker by [COMPANY]."""
    out = text
    cn = core_name(name)
    if len(cn) >= 3:
        pattern = r"\b" + r"\s+".join(_word_re(w) for w in cn.split()) + SUFFIX_RE + r"(?:[\'\u2019]s\b)?"
        out = re.sub(pattern, "[COMPANY]", out, flags=re.I)
    for t in tickers:
        if t and len(t) >= 2:
            out = re.sub(r"\b" + re.escape(t) + r"\b", "[COMPANY]", out)
    return out


def _download_doc(client, cik, accn, doc):
    path = os.path.join(CACHE_DIR, "docs", f"{cik}_{accn}.html.gz")
    if os.path.exists(path):
        with gzip.open(path, "rb") as f:
            return f.read()
    data = client.get_bytes(doc_url(cik, accn, doc))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wb") as f:
        f.write(data)
    return data


def _fmt(v, pct=True):
    if v is None:
        return "n/a"
    return f"{v:.1%}" if pct else f"{v:.1f}"


def _snapshot(it):
    skip = {"rank", "ticker", "name", "cik", "industry", "sic", "list", "why", "flags", "latest_annual_form",
            "latest_annual_accn", "latest_annual_doc", "latest_annual_filed", "event_filing_url", "market_cap_usd",
            "adv_usd", "price", "ev_usd"}
    parts = []
    for k, v in it.items():
        if k in skip or v is None or isinstance(v, (list, dict)):
            continue
        if isinstance(v, float):
            parts.append(f"{k} {v:.3g}")
        else:
            parts.append(f"{k} {v}")
    return ", ".join(parts)


def build_pack(client, screen="core", top=30, near=0, blind=True, results_path=None):
    results_path = results_path or os.path.join(OUTPUT_DIR, "latest_results.json")
    if not os.path.exists(results_path):
        raise SystemExit("No results yet - run the screen first (2_RUN_ALL_SCREENS.bat).")
    with open(results_path, encoding="utf-8") as f:
        res = json.load(f)
    sc = (res.get("screens") or {}).get(screen)
    if sc is None:
        raise SystemExit(f"The latest results don't include the '{screen}' screen.")
    items = sc["pass"][:top] + sc["watch"][:near]
    if not items:
        raise SystemExit(f"The latest '{screen}' results have no companies.")
    stamp = date.today().isoformat()
    pack = os.path.join(OUTPUT_DIR, f"ai_pack_{screen}_{stamp}")
    if os.path.exists(pack):
        shutil.rmtree(pack)
    os.makedirs(pack)
    key, manifest = [], []
    print(f"Building AI review pack for {len(items)} companies (blind={'yes' if blind else 'no'})")
    for n, it in enumerate(items, 1):
        code = f"C{n:02d}" if blind else it["ticker"]
        accn, doc, form = it.get("latest_annual_accn"), it.get("latest_annual_doc"), it.get("latest_annual_form") or "10-K"
        entry = {"code": code, "form": form, "status": "ok"}
        try:
            if not (accn and doc):
                raise NotFound("no annual report on file")
            html = _download_doc(client, it["cik"], accn, doc)
            text = html_to_text(html)
        except Exception as e:  # noqa: BLE001
            entry["status"] = f"download failed: {e}"
            manifest.append(entry)
            key.append({**entry, "ticker": it["ticker"], "name": it["name"], "cik": it["cik"]})
            print(f"  {code}: {entry['status']}")
            continue
        tickers = [it["ticker"]]
        if blind:
            text = redact(text, it["name"], tickers)
        secs = find_sections(text, form)
        entry["sections_found"] = sorted(secs)
        business = secs.get("business") or take_words("\n".join(text.split("\n")[len(text.split("\n")) // 40:]), BUDGET["business"])
        parts = [
            f"COMPANY CODE: {code}",
            f"Industry (SEC SIC): {it.get('industry')}  |  Report: {form} filed {it.get('latest_annual_filed')}",
            f"Screen: {sc['title']} ({'watch list: ' + str(it.get('why')) if it.get('list') not in (None, 'PASS') else 'passed every rule'})",
            "Quant snapshot (no prices on purpose): " + _snapshot(it),
            "",
            f"=== BUSINESS SECTION ({'found' if 'business' in secs else 'NOT FOUND - opening text used'}; "
            f"first {BUDGET['business']} words) ===",
            take_words(business, BUDGET["business"]),
        ]
        for sec, label in (("risk", "RISK FACTORS"), ("mdna", "MANAGEMENT DISCUSSION & ANALYSIS")):
            if sec in secs:
                parts += ["", f"=== SELECTED PARAGRAPHS FROM {label} (keyword-ranked: pricing, competition, "
                              "share, switching, contracts, disruption...) ===",
                          select_paragraphs(secs[sec], BUDGET[sec])]
        ev = "\n".join(parts)
        with open(os.path.join(pack, f"{code}_evidence.txt"), "w", encoding="utf-8") as f:
            f.write(ev)
        with open(os.path.join(pack, f"{code}_fulltext.txt"), "w", encoding="utf-8") as f:
            f.write(text)
        entry["evidence_words"] = _words(ev)
        entry["fulltext_words"] = _words(text)
        manifest.append(entry)
        key.append({**entry, "ticker": it["ticker"], "name": it["name"], "cik": it["cik"],
                    "accession": accn, "url": doc_url(it["cik"], accn, doc)})
        print(f"  {code}: {entry['evidence_words']} words of evidence, sections: {', '.join(sorted(secs)) or 'none'}")
    with open(os.path.join(pack, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump({"created": stamp, "blind": blind, "companies": manifest}, f, indent=1)
    with open(os.path.join(pack, "KEY_open_after_scoring.json"), "w", encoding="utf-8") as f:
        json.dump(key, f, indent=1)
    shutil.copy(os.path.join(ROOT, "moat_rubric.md"), os.path.join(pack, "moat_rubric.md"))
    with open(os.path.join(pack, "screen_focus.md"), "w", encoding="utf-8") as f:
        f.write(f"# What to look for in this screen: {sc['title']}\n\n{sc['rubric']}\n\n"
                "Answer these in each company's 'unknowns' and 'bear_case' fields, with quotes like every other "
                "trait.\n")
    zpath = pack + ".zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for fn in sorted(os.listdir(pack)):
            z.write(os.path.join(pack, fn), arcname=os.path.join(os.path.basename(pack), fn))
    print(f"\nPack saved: {zpath}\nUpload this zip to Claude for the moat review.")
    return zpath
