"""Claim id -> verbatim quote lookup (reads only the claim JSON files; no market data).
Usage: python3 lookup.py ID [ID ...]        print unit, speaker, quote (and claim text, marked)
       python3 lookup.py --grep REGEX [UNIT]  search quotes
       python3 lookup.py --charter           every id cited in the charter, expanded, with its quote
"""
import json, glob, os, re, sys
W = "/tmp/claude-0/-home-claude/a8a60852-162d-5d9b-8463-3f9415508c73/scratchpad/charter_1.2"
DB = {}
for p in sorted(glob.glob(W + "/opus_sources/*.json")):
    u = os.path.basename(p)[:-5]
    d = json.load(open(p))
    for c in d["claims"]:
        DB.setdefault(c["claim_id"], []).append((u, c))

def show(i, claim=True):
    if i not in DB:
        print(f"== {i}: NOT FOUND"); return
    for u, c in DB[i]:
        print(f"== {i} [{u}] speaker={c.get('speaker')} qc={c.get('quote_check')}")
        print("   QUOTE:", c["quote"])
        if claim:
            print("   (claim text):", c.get("claim"))

TOK = re.compile(r'\b(?:((?:MT\d{3}|QP\d{2}))-(C\d{2}-[A-Za-z0-9]+)|(C\d{2}-[A-Za-z0-9]+)|(B\d{2})|(U0[1-8]))\b')
def expand(text):
    out = []; prefix = None
    for m in TOK.finditer(text):
        if m.group(5):
            if m.group(5) == "U01": prefix = "QP01"
            continue
        if m.group(4): out.append(m.group(4)); continue
        if m.group(1):
            prefix = m.group(1); out.append(prefix + "-" + m.group(2))
        else:
            out.append((prefix or "??") + "-" + m.group(3))
    return out

if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--grep":
        rx = re.compile(a[1], re.I); unit = a[2] if len(a) > 2 else None
        for i, lst in DB.items():
            for u, c in lst:
                if unit and u != unit: continue
                if rx.search(c["quote"]):
                    print(f"{i} [{u}] {c.get('speaker')}: {c['quote']}")
    elif a and a[0] == "--charter":
        ch = open(W + "/fable_work/CHARTER_1.2.md").read().split("\n")
        for n, line in enumerate(ch, 1):
            ids = expand(line)
            if not ids: continue
            print(f"\n######## charter line {n}: {line[:160]}")
            for i in ids:
                if i.startswith("B"): print(f"== {i}: blog digest (no quote in sources)"); continue
                show(i, claim=False)
    else:
        for i in a: show(i)
