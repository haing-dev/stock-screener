"""post_verify.py CODE "Investor name" step   (step = score | merge)
score: copy the verifier's tags into the repo, score them, write the third-reading folder T_CODE.
merge: after T_CODE/third.json exists, merge into batch2/CODE/verified/.
"""
import json, os, shutil, subprocess, sys
B = '/tmp/claude-0/-home-claude/c6d39485-a0af-5a90-b220-a415744a715e/scratchpad/pilot3'
P = '/home/claude/stock-screener/docs/research/equity/pilot'
code, name, step = sys.argv[1:4]
R = '%s/batch2/%s' % (P, code)
V = R + '/verify'
if step == 'score':
    shutil.copy('%s/V_%s/tags.json' % (B, code), V + '/tags_opus.json')
    subprocess.run(['python3', P + '/tools/score_verify.py', V + '/verify_key.json', V + '/tags_opus.json', V + '/SCORE.md'], check=True,
                   stdout=subprocess.DEVNULL)
    print(open(V + '/SCORE.md').read().split('## Planted')[0])
    k = {x['vid']: x for x in json.load(open(V + '/verify_key.json'))}
    t = {x['vid']: x for x in json.load(open(V + '/tags_opus.json'))}
    it = {x['vid']: x for x in json.load(open(V + '/verify_items.json'))}
    rl = lambda s: s in ('rule', 'threshold')
    d = [v for v in k if not k[v]['planted'] and rl(k[v]['kind']) != rl(t[v]['kind'])]
    T = '%s/T_%s' % (B, code); os.makedirs(T, exist_ok=True)
    json.dump([{'tid': 'T%02d' % i, 'quote': it[v]['quote'], 'context': it[v]['context']} for i, v in enumerate(d, 1)],
              open(T + '/third_items.json', 'w'), ensure_ascii=False, indent=1)
    json.dump({'T%02d' % i: v for i, v in enumerate(d, 1)}, open(V + '/third_map.json', 'w'))
    b = open(P + '/verify_v1.1/BRIEF_THIRD.md').read().replace('Dev Kantesaria (Valley Forge Capital)', name)
    b = b.replace('he or his fund follows', 'the investor or the fund follows')
    assert 'Kantesaria' not in b
    open(T + '/BRIEF_THIRD.md', 'w').write(b)
    print('disputes for third reading:', len(d))
else:
    shutil.copy('%s/T_%s/third.json' % (B, code), V + '/third.json')
    os.makedirs(R + '/verified', exist_ok=True)
    claims = sorted(os.path.join(R + '/claims', f) for f in os.listdir(R + '/claims'))
    subprocess.run(['python3', P + '/tools/merge_verified.py', V + '/verify_key.json', V + '/tags_opus.json', V + '/third.json',
                    V + '/third_map.json', R + '/verified'] + claims, check=True)
