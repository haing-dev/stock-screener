"""prep_card.py CODE "Investor name" [HELDOUT_DOC]  -> scratch C_CODE/ with claims_for_card.json + BRIEF_CARD.md"""
import json, os, sys
B = '/tmp/claude-0/-home-claude/c6d39485-a0af-5a90-b220-a415744a715e/scratchpad/pilot3'
P = '/home/claude/stock-screener/docs/research/equity/pilot'
code, name = sys.argv[1:3]; held = sys.argv[3] if len(sys.argv) > 3 else None
docs = {d['doc']: d for d in json.load(open(P + '/batch2/docs.json')) if d['doc'].startswith(code)}
keep = ['id', 'line_found', 'quote', 'speaker', 'kind', 'part', 'scope', 'period_meant', 'computable_final', 'measure', 'value',
        'direction', 'strength', 'note', 'rule_status', 'second_kind', 'second_value']
out = []
for d in sorted(docs):
    if d == held:
        continue
    for c in json.load(open('%s/batch2/%s/verified/%s.verified.json' % (P, code, d))):
        r = {k: c.get(k, '') for k in keep}; r['date_said'] = docs[d]['date']; out.append(r)
C = '%s/C_%s' % (B, code); os.makedirs(C, exist_ok=True)
json.dump(out, open(C + '/claims_for_card.json', 'w'), ensure_ascii=False, indent=1)
used = [d for d in sorted(docs) if d != held]
b = open(P + '/BRIEF_CARD.md').read()
b = b.replace('Investor: Dev Kantesaria (Valley Forge Capital). Input: verified claims of four documents (K065 2021-10-22, K105\n2022-10-27, K189 2024-11-20, K290 2024-12-05)',
              'Investor: %s. Input: verified claims of %d documents (%s)' % (name, len(used), ', '.join('%s %s' % (d, docs[d]['date']) for d in used)))
b = b.replace('One document is held out and is NOT\nin your input; do not look for it.',
              ('One document is held out and is NOT in your input; do not look for it.' if held else 'No document is held out.'))
b = b.replace('no general knowledge about him or Valley Forge', 'no general knowledge about the investor or the fund')
b = b.replace('/tmp/claude-0/-home-claude/c6d39485-a0af-5a90-b220-a415744a715e/scratchpad/card1', C)
b += '\nLabel at the top of CARD.md: "File THIN (below the material bar, A13 item 8)" if fewer than 3 documents of 5,000+ words were read.\n'
assert 'Kantesaria' not in b and 'Valley Forge' not in b, b[:600]
open(C + '/BRIEF_CARD.md', 'w').write(b)
print(code, 'claims', len(out), 'rules', sum(c['rule_status'] != 'no' for c in out), 'docs', used)
