"""Score the step 3.5 checker test (rules: SCORING_RULES.md). python3 score.py KEY.json VERDICTS_1.md VERDICTS_2.md
Automatic part: verdict and listed type vs the key. A DEFECT verdict whose listed types miss the planted type is
printed for a manual read of the evidence (the rules let evidence naming the planted line or effect count)."""
import json, re, sys
key = json.load(open(sys.argv[1]))
TYPES = ['look-ahead', 'sample', 'costs', 'period-selection', 'tuned-knob', 'report-mismatch', 'other']
ver = {}
for f in sys.argv[2:]:
    for blk in re.split(r'\n(?=\S*\s*\**(?:case\s*)?C\d\d\b)', open(f).read(), flags=re.I):
        m = re.search(r'\b(C\d\d)\b', blk)
        if not m: continue
        cid = m.group(1)
        v = 'DEFECT' if re.search(r'\bDEFECT\b', blk) else ('CLEAN' if re.search(r'\bCLEAN\b', blk) else None)
        if v is None or cid in ver: continue
        types = [t for t in TYPES if re.search(re.escape(t), blk, re.I)]
        ver[cid] = (v, types, blk.strip()[:400])
caught = missed = fa = 0; bytype = {}; manual = []
for cid, k in sorted(key.items()):
    v, types, txt = ver.get(cid, (None, [], ''))
    if k['defect']:
        t = k['type']; bytype.setdefault(t, [0, 0]); bytype[t][1] += 1
        if v == 'DEFECT' and t in types: caught += 1; bytype[t][0] += 1; res = 'CAUGHT'
        elif v == 'DEFECT': res = 'DEFECT, other type (read evidence)'; manual.append(cid)
        else: missed += 1; res = 'MISSED'
        print(f'{cid} planted {t:16s} -> {v} {types} : {res}')
    else:
        if v == 'DEFECT': fa += 1; manual.append(cid); res = 'FALSE ALARM? (read evidence)'
        else: res = 'ok'
        print(f'{cid} clean                  -> {v} {types} : {res}')
missing = [c for c in key if c not in ver]
print(f'\nautomatic: caught {caught} of 10; missed {missed}; DEFECT with other type {len([m for m in manual if key[m]["defect"]])}; '
      f'clean flagged {fa} of 10; by type {bytype}; verdicts missing {missing}')
print('manual reads needed:', manual)
