"""prep_heldout.py CODE "Investor name" HELDOUT_DOC DATE -> scratch H_CODE/ with CARD.md, heldout_claims.json, brief"""
import json, os, shutil, sys
B = '/tmp/claude-0/-home-claude/c6d39485-a0af-5a90-b220-a415744a715e/scratchpad/pilot3'
P = '/home/claude/stock-screener/docs/research/equity/pilot'
code, name, held, date = sys.argv[1:5]
H = '%s/H_%s' % (B, code); os.makedirs(H, exist_ok=True)
shutil.copy('%s/C_%s/CARD.md' % (B, code), H + '/CARD.md')
c = json.load(open('%s/batch2/%s/verified/%s.verified.json' % (P, code, held)))
r = [{k: x.get(k, '') for k in ['id', 'quote', 'kind', 'part', 'measure', 'value', 'direction', 'strength', 'computable_final', 'note', 'rule_status']} for x in c if x['rule_status'] != 'no']
o = [{k: x.get(k, '') for k in ['id', 'quote', 'kind', 'part', 'note']} for x in c if x['rule_status'] == 'no']
json.dump({'rules': r, 'other_claims': o}, open(H + '/heldout_claims.json', 'w'), ensure_ascii=False, indent=1)
b = open(P + '/heldout/BRIEF_HELDOUT.md').read()
b = b.replace('CARD.md is an investor card for Dev Kantesaria built from four interviews.', 'CARD.md is an investor card for %s.' % name)
b = b.replace('a fifth interview (2023-05-29, a breakdown of FICO)', 'one more document (%s, %s)' % (held, date))
assert 'Kantesaria' not in b and 'FICO' not in b
open(H + '/BRIEF_HELDOUT.md', 'w').write(b)
print(code, 'held-out rules', len(r), 'other', len(o))
