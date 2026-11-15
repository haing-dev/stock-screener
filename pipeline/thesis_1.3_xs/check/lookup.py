"""Claim id -> verbatim quote (and summary fields) from the pack. Usage: python3 lookup.py ID [ID ...] [--full]
Short ids like C17-1 need a prefix: QP08-C17-1."""
import json, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.join(HERE, '..', 'pack')
DB = {}
for f in ('QP15.json', 'QP08.json'):
    for c in json.load(open(os.path.join(PACK, f)))['claims']:
        DB[c['claim_id']] = c
def get(cid):
    return DB.get(cid)
if __name__ == '__main__':
    full = '--full' in sys.argv
    for cid in [a for a in sys.argv[1:] if not a.startswith('--')]:
        c = DB.get(cid)
        if c is None:
            print(f'{cid}: NOT FOUND'); continue
        print(f'{cid} | QUOTE: {c["quote"]}')
        if full:
            for k in ('claim', 'exact_rule', 'reported_result', 'exhibit', 'conditions'):
                if c.get(k): print(f'   {k}: {c[k]}')
