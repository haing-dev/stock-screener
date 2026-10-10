"""Add new transcripts.  python3 scripts/ingest.py <file-or-folder> [...] [--collection X] [--dry-run]
Accepts .docx / .txt / .md with the standard header (title line, Channel:, URL:, Upload date:, Transcript source:).
Folders: the Drive root ('Transcripts', with one subfolder per collection) or a single collection subfolder. The
collection comes from the subfolder name (collections.json 'folders'); collections in 'skip' (crypto, real estate)
are left out unless named with --collection. Skips anything already stored (same YouTube id, URL or title). New
items get the next id, notes = "pending" and category = "uncategorized"; fill those in when the Doc 1 entry is
written. Rebuilds search.db at the end."""
import argparse, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import ROOT, collection_of, collections, read_any, normalize_transcript, write_transcript, load_index, \
    save_index

EXT = (".docx", ".txt", ".md")


def guess_speakers(title):
    t = re.sub(r"^(#?\d+|Episode \d+|Ep\.? ?\d+)\s*[-–:]\s*", "", title, flags=re.I)
    for sep in [" - ", " – ", " — ", ": ", " | "]:
        if sep in t:
            return t.split(sep)[0].strip()
    return t.strip()[:60]


def gather(paths, only=None):
    cfg = collections()
    skip = set(cfg.get("skip", [])) - ({only} if only else set())
    out = []
    for p in paths:
        if os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs.sort()
                for f in sorted(files):
                    if not f.lower().endswith(EXT):
                        continue
                    full = os.path.join(root, f)
                    coll = only or collection_of(full) or "general"
                    if coll in skip:
                        continue
                    # files named only by a YouTube id are older copies of titled files
                    if re.fullmatch(r"[\w-]{11}\.docx", f):
                        continue
                    out.append((full, coll))
        else:
            out.append((p, only or collection_of(p) or "general"))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--collection", help="force a collection (general, healthcare, macro, ...)")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    files = gather(a.paths, a.collection)
    rows = load_index()
    have = {r.get("video_id") or r["url"]: r["id"] for r in rows}
    titles = {r["title"].lower(): r["id"] for r in rows}
    nxt = max([r["id"] for r in rows] or [0]) + 1
    added, skipped = [], []
    for f, coll in files:
        meta, body = normalize_transcript(read_any(f))
        key = meta.get("video_id") or meta.get("url")
        if not key:
            skipped.append((f, "no URL in header - add 'URL: ...' as line 3")); continue
        if key in have:
            skipped.append((f, f"already stored (id {have[key]})")); continue
        if meta["title"].lower() in titles:
            skipped.append((f, f"same title as id {titles[meta['title'].lower()]} - check")); continue
        meta.update(id=nxt, speakers=guess_speakers(meta["title"]), category="uncategorized", notes="pending",
                    collection=coll)
        if not a.dry_run:
            rel = write_transcript(meta, body)
            rows.append(dict(id=nxt, speakers=meta["speakers"], title=meta["title"], channel=meta.get("channel"),
                             date=meta.get("date"), url=meta["url"], video_id=meta.get("video_id"), collection=coll,
                             category="uncategorized", file=rel, notes="pending", words=len(body.split())))
        have[key] = nxt; added.append((nxt, coll, meta["speakers"], meta["title"])); nxt += 1
    if added and not a.dry_run:
        save_index(rows)
        subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "build_db.py")], check=True)
    for i, c, s, t in added:
        print(f"ADDED {i:03d} [{c}]  {s}  |  {t}")
    for f, why in skipped:
        print(f"SKIP  {os.path.basename(f)}: {why}")
    print(f"{len(added)} added, {len(skipped)} skipped" + (" (dry run)" if a.dry_run else ""))


if __name__ == "__main__":
    main()
