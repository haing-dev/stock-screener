"""Ground-truth lookup for QP13.
  python3 lookup.py QP13-C39-3 [QP13-C44-1 ...] [--full]   claim id -> verbatim quote (--full adds the machine fields)
  python3 lookup.py --slide C39 [C44 ...]                    the text of a slide
  python3 lookup.py --grep "exceed 20"                       slides whose text contains the words (whitespace-normalised)
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.join(HERE, '..', 'pack')
DB = {c['claim_id']: c for c in json.load(open(os.path.join(PACK, 'QP13.json'), encoding='utf-8'))['claims']}
TEXT = open(os.path.join(PACK, 'QP13_slides_text.md'), encoding='utf-8').read()
SLIDES = {m.group(1): m.group(2).strip() for m in re.finditer(r'\[(C\d\d)\]\n(.*?)(?=\n\[C\d\d\]\n|\Z)', TEXT, flags=re.S)}
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
if __name__ == '__main__':
    a = sys.argv[1:]
    if '--slide' in a:
        for s in [x for x in a if re.fullmatch(r'C\d\d', x)]:
            print(f'[{s}]\n{SLIDES.get(s, "NOT FOUND")}\n')
    elif '--grep' in a:
        q = norm(a[a.index('--grep') + 1]).lower()
        hits = [s for s, t in SLIDES.items() if q in norm(t).lower()]
        print('found on:', ', '.join(hits) if hits else 'NO SLIDE')
    else:
        full = '--full' in a
        for cid in [x for x in a if not x.startswith('--')]:
            c = DB.get(cid)
            if c is None:
                print(f'{cid}: NOT FOUND'); continue
            print(f'{cid} | QUOTE: {c["quote"]}')
            if full:
                for k in ('claim', 'exact_rule', 'reported_result', 'exhibit', 'conditions'):
                    if c.get(k): print(f'   {k}: {c[k]}')
