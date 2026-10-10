"""Shared helpers for the investor-research store (stdlib only; python-docx needed for .docx ingest)."""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "index.jsonl")
LINE_TARGET = 350   # reflow transcripts to ~350-char lines so grep hits give usable context + line refs
COLLECTIONS_FILE = os.path.join(ROOT, "collections.json")


def collections():
    """Drive subfolder -> collection, collections skipped by default, and which collections feed each screen."""
    return json.load(open(COLLECTIONS_FILE, encoding="utf-8"))


def collection_of(path):
    """Collection from the name of the Drive subfolder a file sits in (None if the folder isn't a known one)."""
    folders = collections()["folders"]
    for part in reversed(os.path.normpath(path).split(os.sep)[:-1]):
        if part in folders:
            return folders[part]
    return None


def slugify(s, n=60):
    return re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")[:n].rstrip("_")


def read_any(path):
    if path.lower().endswith(".docx"):
        import docx  # python-docx
        return "\n".join(p.text for p in docx.Document(path).paragraphs)
    return open(path, encoding="utf-8", errors="replace").read()


def normalize_transcript(raw):
    """Split the header (title, Channel:, URL:, Upload date:, Transcript source:) from the body and reflow it."""
    lines = raw.strip().splitlines()
    meta, i = {"title": lines[0].strip() if lines else ""}, 1
    keys = {"channel": "channel", "url": "url", "upload date": "date", "transcript source": "source"}
    while i < len(lines) and i < 8:
        m = re.match(r"\s*([A-Za-z ]+):\s*(.*)$", lines[i])
        if not m or m.group(1).strip().lower() not in keys:
            break
        meta[keys[m.group(1).strip().lower()]] = m.group(2).strip()
        i += 1
    v = re.search(r"(?:v=|youtu\.be/)([\w-]{11})", meta.get("url", ""))
    meta["video_id"] = v.group(1) if v else None
    text = re.sub(r"\s+", " ", " ".join(lines[i:])).strip()
    out, cur = [], ""
    for sent in re.split(r"(?<=[.?!])\s+", text):
        cur = f"{cur} {sent}".strip()
        if len(cur) >= LINE_TARGET:
            out.append(cur); cur = ""
    if cur:
        out.append(cur)
    # very long unpunctuated captions: hard-wrap at word boundaries
    body = []
    for ln in out:
        while len(ln) > 3 * LINE_TARGET:
            cut = ln.rfind(" ", 0, 2 * LINE_TARGET)
            cut = cut if cut > 0 else 2 * LINE_TARGET
            body.append(ln[:cut]); ln = ln[cut:].strip()
        body.append(ln)
    return meta, "\n".join(body) + "\n"


FRONT = ["id", "speakers", "title", "channel", "date", "url", "video_id", "collection", "category", "source", "notes",
         "doc1_heading"]


def write_transcript(meta, body):
    rel = f"transcripts/{meta['id']:03d}_{slugify(meta.get('speakers') or meta['title'], 40)}.md"
    with open(os.path.join(ROOT, rel), "w", encoding="utf-8") as fh:
        fh.write("---\n")
        for k in FRONT:
            if meta.get(k) is not None:
                fh.write(f"{k}: {json.dumps(meta[k], ensure_ascii=False)}\n")
        fh.write("---\n")
        fh.write(body)
    return rel


def load_index():
    if not os.path.exists(INDEX):
        return []
    return [json.loads(l) for l in open(INDEX, encoding="utf-8") if l.strip()]


def save_index(rows):
    rows = sorted(rows, key=lambda r: r["id"])
    with open(INDEX, "w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")


def split_doc1(text):
    """notes/doc1/NNN.md per entry (+ 000_index.md for the header and index table)."""
    d = os.path.join(ROOT, "notes", "doc1")
    os.makedirs(d, exist_ok=True)
    parts = re.split(r"(?m)^(?=### \d+\. |## )", text)
    open(os.path.join(d, "000_index.md"), "w").write(parts[0])
    n, section = 0, ""
    for p in parts[1:]:
        if p.startswith("## "):
            section = p.splitlines()[0][3:].strip()
            continue
        num = int(re.match(r"### (\d+)\.", p).group(1))
        open(os.path.join(d, f"{num:03d}.md"), "w").write(f"<!-- section: {section} -->\n" + p.rstrip() + "\n")
        n += 1
    return n


def split_doc2(text):
    d = os.path.join(ROOT, "notes", "doc2")
    os.makedirs(d, exist_ok=True)
    parts = re.split(r"(?m)^(?=## )", text)
    open(os.path.join(d, "00_intro.md"), "w").write(parts[0])
    for i, p in enumerate(parts[1:], 1):
        title = p.splitlines()[0][3:]
        open(os.path.join(d, f"{i:02d}_{slugify(title, 40)}.md"), "w").write(p.rstrip() + "\n")
    return len(parts) - 1
