"""prep_recipe.py CODE "Investor name" "eq_prof name or -" CARD_PATH LABELS -> scratch R_CODE/ with inputs + brief"""
import os, shutil, sys
S = '/tmp/claude-0/-home-claude/c6d39485-a0af-5a90-b220-a415744a715e/scratchpad'
E = '/home/claude/stock-screener/docs/research/equity'
code, name, prof, card, labels = sys.argv[1:6]
R = '%s/pilot3/R_%s' % (S, code); os.makedirs(R, exist_ok=True)
shutil.copy(card, R + '/CARD.md')
for f in ('field_dictionary_v0.1.csv', 'FIELD_DICTIONARY_v1.0.md'):
    shutil.copy('%s/%s' % (E, f), R)
lines = open(E + '/eq_prof_v1_report.txt', encoding='utf-8-sig').read().splitlines()
hdr = [l for l in lines if l.startswith('columns:')]
row = [l for l in lines if prof != '-' and l.startswith(prof + ' |')]
open(R + '/construction_13F.txt', 'w').write('\n'.join(hdr + row) if row else 'No 13F construction profile for this investor (not in the eq_conv panel).')
b = open('%s/recipe1/BRIEF_RECIPE.md' % S).read()
b = b.replace('# Brief: recipe for Dev Kantesaria (gate G6)', '# Brief: recipe for %s (gate G6)' % name)
b = b.replace('CARD_v1.1.md (his card; label: held-out test FAILED, K174 merged)', 'CARD.md (the card; labels: %s)' % labels)
b = b.replace('his 13F construction aggregates', 'the 13F construction aggregates')
assert 'Kantesaria' not in b
open(R + '/BRIEF_RECIPE.md', 'w').write(b)
print(code, 'ok', 'profile' if row else 'no profile')
