"""Apply the Find/Replace corrections of a step 3.2 check to copies of the specs.
  python3 apply_check.py CHECK.md SPEC_DIR OUT_DIR
Section "## 3. Required corrections" holds sub-headings "### SPEC_<name>.md" with numbered items, each with exactly one
line "- Find: `...`" and one line "- Replace: `...`". Each Find must occur exactly once in that spec (as it stands after
the earlier pairs for the same file). Writes corrected copies to OUT_DIR; last line ALL PAIRS APPLIED or FAILURES n."""
import os, re, sys
chk, sdir, out = sys.argv[1:4]
t = open(chk, encoding='utf-8').read()
m = re.search(r'^## 3\. Required corrections\s*$(.*?)(?=^## 4\.)', t, re.S | re.M)
if not m: sys.exit('no "## 3. Required corrections" ... "## 4." section')
body = m.group(1)
blocks = re.split(r'^### (SPEC_[^\s]+\.md)\s*$', body, flags=re.M)
os.makedirs(out, exist_ok=True)
fails, n = [], 0
for i in range(1, len(blocks), 2):
    name, txt = blocks[i], blocks[i + 1]
    src = os.path.join(sdir, name)
    if not os.path.exists(src): fails.append(f'{name}: spec not found'); continue
    s = open(src, encoding='utf-8').read()
    pairs = re.findall(r'^- Find: `(.*)`\s*\n- Replace: `(.*)`\s*$', txt, re.M)
    nitems = len(re.findall(r'^\d+\.', txt, re.M))
    if nitems != len(pairs): fails.append(f'{name}: {nitems} numbered items but {len(pairs)} Find/Replace pairs')
    for k, (a, b) in enumerate(pairs, 1):
        c = s.count(a)
        if c != 1: fails.append(f'{name} pair {k}: Find occurs {c} times: {a[:80]}'); continue
        s = s.replace(a, b); n += 1
    open(os.path.join(out, name), 'w', encoding='utf-8').write(s)
print(f'pairs applied: {n}')
for f in fails: print('  ' + f)
print('ALL PAIRS APPLIED' if not fails else f'FAILURES {len(fails)}')
