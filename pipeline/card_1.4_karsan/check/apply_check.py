"""Parse the Find/Replace pairs of section 3 of CHECK_1.4_karsan.md, confirm each Find occurs exactly once in the note,
apply them in order and write note_corrected_preview.md. Exit code 1 if any pair fails."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
check = open(os.path.join(HERE, 'CHECK_1.4_karsan.md'), encoding='utf-8').read()
note = open(os.path.join(HERE, '..', 'fable_work', 'CARD_1.4_flows_volatility.md'), encoding='utf-8').read()
sec = check.split('## 3. Required corrections', 1)[1].split('\n## 4.', 1)[0]
pairs = re.findall(r'^- Find: `([^`\n]+)`\n- Replace: `([^`\n]+)`$', sec, flags=re.M)
items = len(re.findall(r'^\d+\. ', sec, flags=re.M))
print(f'numbered items: {items}; Find/Replace pairs parsed: {len(pairs)}')
ok = len(pairs) == items
for k, (f, r) in enumerate(pairs, 1):
    n = note.count(f)
    if n != 1:
        print(f'  pair {k}: FAIL, Find occurs {n} times: {f[:80]}'); ok = False; continue
    note = note.replace(f, r, 1)
    print(f'  pair {k}: applied')
open(os.path.join(HERE, 'note_corrected_preview.md'), 'w', encoding='utf-8').write(note)
print('ALL PAIRS APPLIED' if ok else 'SOME PAIRS FAILED')
sys.exit(0 if ok else 1)
