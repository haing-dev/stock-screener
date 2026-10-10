"""Build search.db: SQLite FTS5 over transcript passages and notes. Rebuild after any change (~2 s)."""
import glob, os, re, sqlite3, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import ROOT, load_index

DB = os.path.join(ROOT, "search.db")


def front(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    return (m.end(), text[:m.end()].count("\n")) if m else (0, 0)


def chunks(lines, start_line, size=3):
    for i in range(0, len(lines), size):
        part = " ".join(l.strip() for l in lines[i:i + size] if l.strip())
        if part:
            yield start_line + i, part


def main():
    if os.path.exists(DB):
        os.remove(DB)
    con = sqlite3.connect(DB)
    con.execute("CREATE VIRTUAL TABLE p USING fts5(text, speakers, kind UNINDEXED, path UNINDEXED, line UNINDEXED, "
                "doc_id UNINDEXED, collection UNINDEXED, tokenize='porter unicode61')")
    rows = []
    idx = load_index()
    for r in idx:
        t = open(os.path.join(ROOT, r["file"]), encoding="utf-8").read()
        off, nl = front(t)
        for ln, txt in chunks(t[off:].splitlines(), nl + 1):
            rows.append((txt, r["speakers"], "transcript", r["file"], ln, r["id"], r.get("collection") or ""))
    spk = {r["id"]: r["speakers"] for r in idx}
    col = {r["id"]: r.get("collection") or "" for r in idx}
    for path in sorted(glob.glob(os.path.join(ROOT, "notes", "doc1", "*.md")) +
                       glob.glob(os.path.join(ROOT, "notes", "doc2", "*.md"))):
        rel = os.path.relpath(path, ROOT)
        m = re.search(r"doc1/(\d+)\.md$", rel)
        did = int(m.group(1)) if m else None
        lines = open(path, encoding="utf-8").read().splitlines()
        for ln, txt in chunks(lines, 1, size=1):     # notes: one bullet / paragraph per passage
            rows.append((txt, spk.get(did, ""), "notes", rel, ln, did, col.get(did, "")))
    con.executemany("INSERT INTO p VALUES (?,?,?,?,?,?,?)", rows)
    con.commit()
    print(f"search.db: {len(rows)} passages")


if __name__ == "__main__":
    main()
