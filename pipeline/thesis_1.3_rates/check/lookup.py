#!/usr/bin/env python3
"""claim id -> verbatim quote (and machine fields). Usage: lookup.py ID [ID...] | --dump PAPER | --grep REGEX"""
import json, sys, re, os
PACK = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'pack')
C = {}
for p in ('QP06', 'QP07', 'QP12'):
    d = json.load(open(os.path.join(PACK, p + '.json')))
    for c in d['claims']:
        C[c['claim_id']] = c
def show(c, full=False):
    s = f"{c['claim_id']}: QUOTE=\"{c['quote']}\""
    if full:
        for k in ('claim', 'reported_result', 'exact_rule', 'exhibit'):
            if c.get(k): s += f"\n    [{k}] {c[k]}"
    return s
a = sys.argv[1:]
if a and a[0] == '--dump':
    for k, c in C.items():
        if k.startswith(a[1]): print(show(c, True))
elif a and a[0] == '--grep':
    r = re.compile(a[1], re.I)
    for k, c in C.items():
        if r.search(c['quote']): print(show(c))
else:
    for i in a:
        print(show(C[i], True) if i in C else f"{i}: NOT FOUND")
