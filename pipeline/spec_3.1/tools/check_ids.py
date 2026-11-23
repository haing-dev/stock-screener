"""Id and quote check for the thesis register (step 1.5).
  python3 check_ids.py FILE.md
Checks: (1) every claim id (MTnnn-Cnn-n / QPnn-Cnn-n, X ids too) exists in the ledger;
(2) every phrase written as "words" (ID[, ID]) occurs (normalised) in the quote of one of those ids.
Prints counts and every failure; last line ALL IDS AND QUOTES OK or FAILURES n."""
import json, glob, os, re, sys
V = '/tmp/claude-0/-home-claude/a8a60852-162d-5d9b-8463-3f9415508c73/scratchpad/vault_wt'
Q = {}
for f in glob.glob(V + '/ledger/MT*.json') + glob.glob(V + '/papers/merged/QP[0-9][0-9].json'):
    for c in json.load(open(f, encoding='utf-8')).get('claims', []):
        Q[c['claim_id']] = c.get('quote', '')
norm = lambda s: re.sub(r'[^a-z0-9%$.]+', ' ', s.lower().replace('’', "'")).strip()
ID = re.compile(r'\b(?:MT\d{3}|QP\d{2})-C\d+-X?\d+\b')
t = open(sys.argv[1], encoding='utf-8').read()
ids = set(ID.findall(t)); bad = sorted(i for i in ids if i not in Q)
fails = [f'missing id {i}' for i in bad]
nq = 0
for m in re.finditer(r'"([^"\n]{3,300})"\s*\(([^)\n]*)\)', t):
    cited = ID.findall(m.group(2))
    if not cited: continue
    nq += 1
    raw = m.group(1).replace('\u2026', '...')
    p = norm(raw)
    parts = [norm(x) for x in raw.split('...') if norm(x)]
    if not any(all(x in norm(Q.get(i, '')) for x in [p]) or all(x in norm(Q.get(i, '')) for x in parts) for i in cited):
        fails.append(f'quote not in cited ids: "{m.group(1)}" ({", ".join(cited)})')
print(f'ids cited: {len(ids)}; missing: {len(bad)}; quoted phrases checked: {nq}')
for f in fails: print('  ' + f)
print('ALL IDS AND QUOTES OK' if not fails else f'FAILURES {len(fails)}')
