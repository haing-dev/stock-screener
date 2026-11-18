"""Packs for phase A2 of the scorecard (E0.4): one block per investor with the roles the notes give and the
candidate filers and funds from the WRDS matching report. No return figure is in these packs.

    python3 tools/equity/match_pack.py INVENTORY_DIR PACK_DIR MATCH_REPORT OUT_DIR [n_packs=3]"""
import csv
import glob
import json
import os
import random
import re
import sys


def main(inv_dir, pack_dir, report, out, n=3):
    n = int(n)
    os.makedirs(out, exist_ok=True)
    people = [p for p in csv.DictReader(open(os.path.join(inv_dir, "investors.csv"), encoding="utf-8"))
              if p["ran_money"] == "yes"]
    front = {}
    for f in glob.glob(os.path.join(pack_dir, "pack_*.md")):
        for blk in re.split(r"(?m)^=== DOC ", open(f, encoding="utf-8").read())[1:]:
            d = int(blk.split(" ", 1)[0])
            sp = re.search(r"(?m)^speakers: (.*)$", blk)
            dt = re.search(r"(?m)^date: (.*)$", blk)
            front[d] = (sp.group(1) if sp else "", (dt.group(1) if dt else "")[:4])
    cand = {}
    for blk in re.split(r"(?m)^## (?=I\d{3} )", open(report, encoding="utf-8", errors="replace").read())[1:]:
        cand[blk[:4]] = "\n".join(l for l in blk.split("\n")[1:] if l.startswith("   "))
    blocks = []
    for p in people:
        sur = re.sub(r"[^a-z ]", "", p["name"].lower()).split()[-1]
        roles, years = [], []
        for d in map(int, p["doc_ids"].split()):
            sp, yr = front.get(d, ("", ""))
            for seg in re.split(r";\s*(?![^()]*\))", sp):
                if sur and sur in seg.lower() and seg.strip() not in roles:
                    roles.append(seg.strip())
            if yr.isdigit():
                years.append(yr)
        blocks.append("### %s | %s\nfirms in the notes: %s\nroles in the notes: %s\nyears of the talks: %s\n%s\n"
                      % (p["id"], p["name"], p["firms"], " || ".join(roles[:5]) or "(none found)",
                         ", ".join(sorted(set(years))), cand.get(p["id"], "   (no candidate block)")))
    for k in range(n):
        open(os.path.join(out, "match_pack_%d.md" % (k + 1)), "w", encoding="utf-8").write("\n".join(blocks[k::n]))
    ids = sorted(random.Random(20261117).sample(range(len(blocks)), max(1, round(len(blocks) / 10))))
    open(os.path.join(out, "match_recheck_pack.md"), "w", encoding="utf-8").write("\n".join(blocks[i] for i in ids))
    print("investors %d | packs %d | recheck %d | chars %d" % (len(blocks), n, len(ids), sum(map(len, blocks))))


if __name__ == "__main__":
    main(*sys.argv[1:6])
