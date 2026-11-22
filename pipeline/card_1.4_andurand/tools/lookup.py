"""Ground-truth lookup for the card pack.
  python3 lookup.py MT148-C01-1 [more ids] [--full]   claim id -> source date, speaker, verbatim quote (--full adds machine fields)
  python3 lookup.py --grep "words"                     claims whose QUOTE contains the words (case-insensitive)
  python3 lookup.py --source MT148                     all claim ids and quotes of one source
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
DB = {c['claim_id']: c for c in json.load(open(os.path.join(HERE, '..', 'pack', 'CLAIMS.json'), encoding='utf-8'))['claims']}
norm = lambda s: re.sub(r'\s+', ' ', s).strip().lower()
if __name__ == '__main__':
    a = sys.argv[1:]
    if '--grep' in a:
        q = norm(a[a.index('--grep') + 1])
        for k, c in DB.items():
            if q in norm(c['quote']): print(f"{k} [{c['source_date']}] {c['speaker']}: {c['quote']}")
    elif '--source' in a:
        s = a[a.index('--source') + 1]
        for k, c in DB.items():
            if k.startswith(s + '-'): print(f"{k}: {c['quote']}")
    else:
        for cid in [x for x in a if not x.startswith('--')]:
            c = DB.get(cid)
            if c is None: print(f'{cid}: NOT FOUND'); continue
            print(f"{cid} [{c['source_date']}] {c['speaker']} | QUOTE: {c['quote']}")
            if '--full' in a:
                for k in ('claim', 'mechanism', 'indicator', 'direction', 'conditions', 'horizon'):
                    if c.get(k): print(f'   {k}: {c[k]}')
