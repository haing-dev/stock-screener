"""Add new transcripts.  python3 scripts/ingest.py <file-or-folder> [...] [--dry-run]
Accepts .docx / .txt / .md with the standard header (title line, Channel:, URL:, Upload date:, Transcript source:).
Skips anything already stored (same YouTube id or URL). New items get the next id, notes = "pending" and
category = "uncategorized"; fill those in when the Doc 1 entry is written. Rebuilds search.db at the end."""
import argparse, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import ROOT, read_any, normalize_transcript, write_transcript, load_index, save_index


def guess_speakers(title):
    t = re.sub(r"^#?\d+\s*[-–:]\s*", "", title)
    for sep in [" - ", " – ", " — ", ": ", " | "]:
        if sep in t:
            return t.split(sep)[0].strip()
    return t.strip()[:60]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    files = []
    for p in a.paths:
        if os.path.isdir(p):
            files += [os.path.join(p, f) for f in sorted(os.listdir(p)) if f.lower().endswith((".docx", ".txt", ".md"))]
        else:
            files.append(p)
    rows = load_index()
    have = {r.get("video_id") or r["url"] for r in rows}
    titles = {r["title"].lower(): r["id"] for r in rows}
    nxt = max([r["id"] for r in rows] or [0]) + 1
    added, skipped = [], []
    for f in files:
        meta, body = normalize_transcript(read_any(f))
        key = meta.get("video_id") or meta.get("url")
        if not key:
            skipped.append((f, "no URL in header - add 'URL: ...' as line 3")); continue
        if key in have:
            skipped.append((f, "already stored")); continue
        if meta["title"].lower() in titles:
            skipped.append((f, f"same title as id {titles[meta['title'].lower()]} - check")); continue
        meta.update(id=nxt, speakers=guess_speakers(meta["title"]), category="uncategorized", notes="pending")
        if not a.dry_run:
            rel = write_transcript(meta, body)
            rows.append(dict(id=nxt, speakers=meta["speakers"], title=meta["title"], channel=meta.get("channel"),
                             date=meta.get("date"), url=meta["url"], video_id=meta.get("video_id"),
                             category="uncategorized", file=rel, notes="pending", words=len(body.split())))
        have.add(key); added.append((nxt, meta["speakers"], meta["title"])); nxt += 1
    if added and not a.dry_run:
        save_index(rows)
        subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "build_db.py")], check=True)
    for i, s, t in added:
        print(f"ADDED {i:03d}  {s}  |  {t}")
    for f, why in skipped:
        print(f"SKIP  {os.path.basename(f)}: {why}")
    print(f"{len(added)} added, {len(skipped)} skipped" + (" (dry run)" if a.dry_run else ""))


if __name__ == "__main__":
    main()
