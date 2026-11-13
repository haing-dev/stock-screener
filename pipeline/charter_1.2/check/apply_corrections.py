import re,sys
src,dst=sys.argv[1],sys.argv[2]
s=open(src).read(); n=0
def rep(find,repl,count=1):
    global s,n
    pat=r'\s+'.join(re.escape(x) for x in find.split())
    m=re.findall(pat,s)
    assert len(m)==count, (len(m),find[:70])
    s=re.sub(pat,lambda _:repl,s); n+=1
# 1
rep('SHOWN (described) in U03; summary only in U02; ASSERTED elsewhere','ASSERTED for the Sharpe gain (summary only: U02 B22); the U03 described study (Quantica) gives long-volatility correlation and volatility ratios, not Sharpe')
rep('All agree on Sharpe; only U03 weighs the lost capture.',"U04-U06 quotes assert the practice, not a Sharpe gain; only U03 weighs the lost capture (static: '40% or higher' long-vol correlation, MT195-C08-2).")
# 2
rep('"negative first" (U03, U05)',"\"negative first\" (U03; U05's MT205-C08-1 says 'negative skew there', claim text: day to day)")
# 3
rep('3-6 months (U04), 4-9 months (U03) (unverified).',"3-6 months (U04), 4-9 months (U03); the reversal link is MT042-C09-2 ('this extreme V-shaped move') (numbers in quote).")
# 4
rep('Yes: U02 MT026-C17-1, U06 MT158-C13-4. No: U05 MT205-C09-1.',"Yes: U02 MT026-C17-4 ('correlations ... probably understate the amount of diversification'), U06 MT158-C13-4. No: U05 MT205-C09-1; the host in MT026-C17-1 ('there is no evidence, in my opinion, that'). Carver also: alternatives 'only buys you a little bit more diversification' (MT026-C16-X1).")
# 5
rep('and no payoff in equity crises. |','and a weaker payoff in equity crises. |')
rep('SHOWN (described house study)',"ASSERTED (numbers hedged: 'maybe 8.9 sharp something like that')")
# 6
rep('Result SHOWN (paper: hypothetical, no t-statistics)',"Result summary only (Sharpe figures are chart reads in claim text; quotes: 'Hypothetical', 'gross of fees and transaction costs')")
rep('U01 C06-1, C07-2, C04-2..C04-5, C06-6;','U01 C06-1, C07-2 (summary only), C03-9 (1970-2022), C04-2..C04-5, C06-6;')
# 7
rep('a risk premium (U02 MT137-C01-1)',"a risk premium (claim text of U02 MT137-C01-1; quote: 'if anyone can do it then you haven't got an edge')")
rep('autocorrelation (returns that follow their own past) from market structure (U05 MT024-C14-2, MT029-C08-1)',"a 'sustained imbalance in the asset class' (U05 MT029-C08-1), which gives autocorrelation, returns that follow their own past (MT024-C14-2: it 'is really important')")
# 8
rep('SHOWN as simulation (U06, described); ASSERTED elsewhere',"ASSERTED (U06's 33% drawdown 'spent years in drawdown' is in quote; 'simulation' and its 0.6 Sharpe are claim text, MT083-C14-1)")
rep('U05 MT221-C08-X1, MT073-C03-3','U05 MT073-C03-3')
# 9
rep('no crowding in positions data (U05 MT073-C10-3)','no rise in the return loading on slow or mid-frequency trend (U05 MT073-C10-3)')
# 10
rep('lowers the crisis payoff (U03, U07)',"lowers the crisis payoff (U03 MT021-C13-2; U07's quote says only that signals which 'smooth out those drawdowns' have 'Great Value', the crisis cost is claim text)")
rep('hurts only in a full liquidity break (U06)',"has 'horrible left tails' in 'a full liquidity break, a dash for cash' (U06; 'only' and 'carry' are claim text)")
# 11
rep('investors bound by benchmarks and career risk (U04 MT087-C11-1, C12-1) adjust in steps (reader)',"investors digest information slowly (U04 MT116-C02-1 'slow digestion of information'; MT216-C12-1 'a journey that takes you from some valuation level to the new valuation level'); benchmark and career constraints are claim text of MT087-C11-1 only")
# 12
rep('(U01 C14-9)','(U01 C14-15b)')
rep('quiet macro data (C06-3)',"a weak 2010s (claim text of C06-3; its quote is the row label 'Jan. 2010 - Dec. 2019'; 'quiet macro data' is reader)")
# 13
rep('(U02 MT064-C19-1, C20-1)',"(U02 MT064-C20-2 'anything longer than a year is is when mean reversion kicks in'; MT044-C07-2 'In the very long run, it mean reverts')")
rep('(U04 MT116-C13-2)','(U04 MT116-C13-2) (claim text)')
# 14
rep('near contracts lose more on each roll, the move to the next contract, than far ones (reader)',"near contracts lose more on each roll, the move to the next contract, than far ones (ASSERTED: 'doing it on the front has a negative roll yield', MT167-C03-X2)")
rep('(a "risk-sharing" premium in U04\'s words, MT167-C02-X1; said to survive crowding, MT204-C14-3, C15-1)',"(a premium 'shared between consumers and and and producers', MT167-C02-X1)")
# 15
rep('"15 years live" (MT130-C08-X1) is summary only.',"'probably goes back 15 years' (MT130-C08-X1) is in the quote, but it dates the QIS-format design to about 2011; it is not a live record and does not establish pre-2011 documentation.")
rep('| 15 years | live record of curve carry (summary only) | U04 MT130-C08-X1 | rule 5 for Curve carry |','| 15 years | age of the QIS-format design (in quote, not a live record) | U04 MT130-C08-X1 | rule 5 for Curve carry |')
# 16
rep("Trend profit and loss per market at equal risk (book.py:60-76, 132). Principal components (common factors) of market returns over 60 months: the first factor's share of variance, each class's exposure to it, pod Sharpe over mean market Sharpe. Per candidate with a locked history: the share of its variance explained by the first three factors and by its nearest held market.",
    "Trend profit and loss per market at equal risk (book.py:60-76, 132) on the 61 distinct markets (st_us_2y dropped). Principal components (common factors) of monthly excess returns in each trailing 60-month design window, on markets with all 60 months; report, averaged over windows, the first factor's share of variance, each class's mean loading, and pod Sharpe over mean market Sharpe. Per candidate with a locked history: in the same windows, the share of its variance explained by the held markets' first three factors, and its R-squared on the single held market with the highest absolute correlation, each averaged over windows.")
rep('A candidate joins the breadth item only if both shares are under one half and it has 120 months (TESTING_PROTOCOL.md:12).','A candidate joins the breadth item only if both averaged shares are under one half, it has 120 months before 2011 (TESTING_PROTOCOL.md:12), and it is costed at the 8 bp charged for EM currencies (U06-T2).')
# 17
rep('If the non-signal share of turnover is at least 20% in both eras','If the non-signal share, 1 - (turnover with volatilities and all scalers held at last month\'s values) / (actual turnover), is at least 20% in both eras (1975-89, 1990-2010)')
rep('Its width must come from the source post, not from B13 (audit).',"Width: trade a market only if its target moves by more than 10% of its standard vol-adjusted position (MT026-C08-2: 'if it was less than 10%, I wouldn't bother trading'; 'standard position' is claim text), scaled by relative cost as in U02-T3 (MT026-C11-1: 'a wider buffer if an instrument's more expensive'); not B13's 10% of target.")
rep('turnover = sum of absolute position changes (book.py:212-216).','turnover = sum of absolute position changes (book.py:212-216). Cost drag per market (U02-T2 c) is reported.')
# 18
rep('If either split shows at least 2 points more realised volatility, with a 90% interval above zero','If either split shows realised forward 12-month volatility at least 2 points higher in the named state than in the other months, with the one-sided 90% bootstrap bound of that difference above zero (stationary bootstrap, mean block 12 months, because the forward windows overlap; seed as stats.py)')
rep("(U03-T3's form: 70% 12-month, 30% 36-month)","(U03-T3's form: 70% 12-month EWMA + 30% 36-month book volatility, floor 0.75 x the 36-month value)")
rep('MT021-C06-1; U04 MT087-C09-3 |',"MT021-C06-1; U04 MT087-C07-1 ('if your barometer is 90%. Then more likely than not you have a lot of directional exposures'), MT087-C09-3 (performance only) |")
# 19
rep('Sort design months by the fall of world equities (protocol.py:200) from their 24-month high',"Sort design months by the fall of the S&P 500 (eq_us_spx, compounded excess return; the source's base, MT194-C06-1) from its 24-month high; report the same table for the four-market average of protocol.py:200")
rep('lists "funding break" as its stop state; else dropped.','lists "funding break" as its stop state; else dropped. A cell with fewer than 6 months is reported, not used.')
# 20
rep('(standard errors as stats.py:165-182)','(one regression per era on year-level cross-market means: mean trend Sharpe on mean |market Sharpe|; Newey-West slope standard error, 2 lags, extending stats.py:165-182, which returns only the intercept t)')
# 21
rep('Not run; for the checker to confirm.','Confirmed by the Opus check (code reading: panel.py:477-480, 496, 502-503; daily.py:128-131; signals.py:36-39): identical in returns, volatility and every signal wherever DGS2 exists.')
rep('the doubled US 2-year note removed once the checker confirms it (section 9, item 2)',"st_us_2y removed (bd_us_2y's series is a superset: the same DGS2 months plus any stooq months before DGS2, panel.py:486-488, 496); registered as a design change before the run")
rep('16 commodities; panel.py:304-352).','16 commodities; panel.py:304-352; 61 distinct; plus cm_aqr_ew, trend only, to 2000 (panel.py:543-551; book.py:121-122)).')
# 22
rep('("we don\'t want to restrain it", MT020-C06-3)','("we don\'t want to restrain it", MT020-C06-3, speaker Rob Santino of ETC)')
# 23
rep('metals 1973; WTI 1983; Brent 1988','metals 1973; WTI 1983 (24 contracts only from 1995; when a 12-month contract starts is not on the sheet); Brent 1988')
# 24
rep("| U01 C06-1 | size of the Economic trend thesis |","| U01 C06-1 (summary only); 1970-2022 in quote C03-9 | size of the Economic trend thesis |")
rep("| U01 C07-2 | U01's reading of the mechanism |","| U01 C07-2 (summary only: chart reads) | U01's reading of the mechanism |")
rep("| U01 C03-7 and the paper's title | rule 5 for Economic trend |","| 2017 in quote C03-7; 2023 from TESTING_PROTOCOL.md:55 (not a quote) | rule 5 for Economic trend |")
rep("| U04-T3, MT130-C08-1 | the Curve carry rule |","| about 12 months: U04-T3's choice; the quote says 'the back end of the curve' | the Curve carry rule |")
open(dst,'w').write(s); print('replacements',n)
