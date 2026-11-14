import re, os, json
H = os.path.dirname(os.path.abspath(__file__))
note = open(os.path.join(H, '..', 'fable_work', 'THESIS_1.3_rates.md')).read()
chk = open(os.path.join(H, 'CHECK_1.3_rates.md')).read()
sec = chk.split('## 3. Required corrections')[1].split('## 4.')[0]
pairs = re.findall(r'- Find: `([^`]*)`\n\s*- Replace: `([^`]*)`', sec)
print(len(pairs), 'corrections parsed')
txt = note
for i, (f, r) in enumerate(pairs, 1):
    n0 = note.count(f); n = txt.count(f)
    print(i, 'orig count', n0, 'at apply', n)
    txt = txt.replace(f, r, 1)
open(os.path.join(H, 'note_corrected_preview.md'), 'w').write(txt)
# quote words cited in reasons/findings: check each "..." string of >=12 chars in CHECK against all quotes
Q = {}
for p in ('QP06','QP07','QP12'):
    for c in json.load(open(os.path.join(H,'..','pack',p+'.json')))['claims']:
        Q[c['claim_id']] = re.sub(r'\s+',' ',c['quote'])
bad = []
for m in re.finditer(r'"([^"]{12,})"', chk.replace('\n',' ')):
    s = re.sub(r'\s+',' ', m.group(1))
    parts = [p.strip() for p in s.split('...') if p.strip()]
    if not any(all(p in q for p in parts) for q in Q.values()):
        bad.append(s[:100])
print('quoted strings not found in any quote:'); [print('  ', b) for b in bad]
