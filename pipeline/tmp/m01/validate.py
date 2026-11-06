import json,sys,re
FP="""trend_following, carry, value_mean_reversion, macro_fundamental_topdown,
bottom_up_fundamental, liquidity_flows, positioning_crowding, volatility_options, dealer_hedging_flows,
crisis_alpha_convexity, diversification_risk_parity, position_sizing_vol_target, kelly_or_conviction_sizing,
debt_cycle_long_term, policy_reaction_central_banks, fiscal_dominance, valuation_contrarian, behavioral_sentiment,
market_internals_leading, regime_detection, nowcasting_data, research_robustness_overfitting, costs_execution,
replication_indexing, portfolio_construction_stacking, short_term_systematic, relative_value_arbitrage,
commodity_fundamentals, geopolitics, structural_themes, manager_selection_allocation"""
FP=set(x.strip() for x in FP.split(','))
sid=sys.argv[1]
m=json.load(open(f'maps/{sid}.json'))
led=json.load(open(f'ledger/{sid}.json'))
ids={c['claim_id'] for c in led['claims']}
doc=open(f'docs/{sid}.txt').read()
chunks={}
for mm in re.finditer(r'\[(C\d+)\]\n(.*?)(?=\n\[C\d+\]\n|\Z)',doc,re.S):
    chunks[mm.group(1)]=mm.group(2)
norm=lambda s:re.sub(r'\s+',' ',s.lower()).strip()
added=m.get('added_claims',[])
aids=set()
for a in added:
    aids.add(a['claim_id'])
    ch=a['claim_id'].split('-')[1]
    assert re.fullmatch(sid+r'-C\d\d-R\d+',a['claim_id']),a['claim_id']
    q=norm(a['quote'])
    assert q in norm(chunks[ch]),('QUOTE NOT FOUND',a['claim_id'],a['quote'])
    assert len(a['quote'].split())<=40,a['claim_id']
    assert a['chunk']==ch
    for k in ['speaker','claim','mechanism','asset_class','indicator','horizon','direction','conditions','testable','speaker_confidence','time_bound']:
        assert k in a,(a['claim_id'],k)
allids=ids|aids
cited=set()
def chk(lst,where):
    for i in lst:
        assert i in allids,('MISSING',i,where)
        cited.add(i)
n={'prem':0,'chain':0,'dec':0,'view':0}
for s in m['speakers']:
    assert set(s['fingerprint'])<=FP,set(s['fingerprint'])-FP
    assert 3<=len(s['fingerprint'])<=8
    for p in s['worldview_premises']:
        n['prem']+=1; chk(p['claim_ids'],'prem'); assert p['stated'] in('stated','implicit'); assert p['type'] in 'empirical theoretical behavioural institutional experience'.split()
        assert p['claim_ids'] or p['stated']=='implicit'
    for c in s['mechanism_chains']:
        n['chain']+=1; chk(c['claim_ids'],'chain')
        for st in c['steps']: chk(st['claim_ids'],'step')
    for d in s['decision_process']:
        n['dec']+=1; chk(d['claim_ids'],'dec'); assert d['element'] in 'signal universe sizing risk execution research portfolio other'.split()
    for v in s['current_views']:
        n['view']+=1; chk(v['claim_ids'],'view'); assert v['as_of']
for d in m['disagreements']:
    for p in d['positions']: chk(p['claim_ids'],'dis')
for g in m['gaps_and_conflicts']: chk(g['claim_ids'],'gap')
for k in ['source_id','episode_thesis','speakers','disagreements','gaps_and_conflicts','forward_looking_inputs','reader_inferences','added_claims']: assert k in m,k
print(sid,'OK speakers',len(m['speakers']),n,'disagreements',len(m['disagreements']),'added',len(added),'cited',len(cited&ids),'of',len(ids))
unc=sorted(ids-cited); print("uncited ledger claims:",unc)
