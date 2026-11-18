"""Build the reading packs for step E0.1 (inventory and typing) from the notes of the processed library.

    python3 tools/equity/inventory_pack.py MANIFEST.json NOTES_DIR OUT_DIR [per_pack=70] [seed=20261117]

NOTES_DIR holds the .note.md files with the folder layout of 'General Transcripts'. Writes OUT_DIR/docs.csv (doc
number, file), OUT_DIR/pack_NN.md (front matter, Summary, Topics covered, Quotes of each note) and
OUT_DIR/recode_pack.md (a seeded random tenth, for the blind second coder). No transcript text is read."""
import csv
import json
import os
import random
import re
import sys

KEEP = ("## Summary", "## Topics covered", "## Quotes")


def trim(note):
    fm, body = "", note
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", note, re.S)
    if m:
        fm, body = m.group(1), m.group(2)
    parts = re.split(r"(?m)^(?=## )", body)
    keep = [p.strip() for p in parts if p.startswith(KEEP)]
    fm = "\n".join(l for l in fm.split("\n") if not l.startswith(("source:",)))
    return fm.strip() + "\n\n" + "\n\n".join(keep)


def main(manifest, notes, out, per=70, seed=20261117):
    m = json.load(open(manifest, encoding="utf-8"))
    docs = sorted(d["txt"] for d in m["docs"].values() if d["src"].startswith("General Transcripts/"))
    os.makedirs(out, exist_ok=True)
    rows, texts, missing = [], {}, 0
    for i, txt in enumerate(docs, 1):
        rel = txt[len("General Transcripts/"):-4] + ".note.md"
        p = os.path.join(notes, rel)
        if not os.path.exists(p):
            missing += 1
            continue
        texts[i] = "=== DOC %d | %s ===\n%s\n" % (i, rel[:-8], trim(open(p, encoding="utf-8").read()))
        rows.append((i, rel[:-8]))
    csv.writer(open(os.path.join(out, "docs.csv"), "w", newline="", encoding="utf-8")).writerows([("doc", "file")] + rows)
    ids = [i for i, _ in rows]
    rnd = random.Random(seed)
    shuffled = ids[:]
    rnd.shuffle(shuffled)                      # packs are random mixes, so no coder gets one channel only
    n = 0
    for k in range(0, len(shuffled), per):
        n += 1
        part = sorted(shuffled[k:k + per])
        open(os.path.join(out, "pack_%02d.md" % n), "w", encoding="utf-8").write("\n".join(texts[i] for i in part))
    rec = sorted(random.Random(seed + 1).sample(ids, max(1, round(len(ids) / 10))))
    open(os.path.join(out, "recode_pack.md"), "w", encoding="utf-8").write("\n".join(texts[i] for i in rec))
    json.dump(rec, open(os.path.join(out, "recode_ids.json"), "w"))
    words = sum(len(t.split()) for t in texts.values())
    print("documents %d (notes missing %d) | packs %d of up to %d | recode %d | words in packs %d"
          % (len(rows), missing, n, per, len(rec), words))


if __name__ == "__main__":
    a = sys.argv[1:]
    main(a[0], a[1], a[2], *[int(x) for x in a[3:5]])
