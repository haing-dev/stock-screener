---
source_id: MT200
title: "Trend Following- How much to Allocate- - Systematic Investor 316"
date: 2024-10-10
channel: "Top Traders Unplugged"
url: 
words: 12002
claims: 49
added_by_crosscheck: 10
corrections: 4
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Nick Baltas (quant researcher/trend follower; caption 'Nick Balter')", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Trend Following- How much to Allocate- - Systematic Investor 316

**Speakers:** Nick Baltas (quant researcher/trend follower; caption 'Nick Balter'); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** Nick Baltas and Niels review Aug-Oct 2024 for trend following, then discuss speed in the August V-shaped reversal, three papers on risk-based allocation and carry-optimised trend, and how much to allocate to trend following. Main conclusions: no speed sweet spot, longer lookbacks fare better in real crises, scale by volatility, and size trend by tracking error versus the policy benchmark.

**Approach:** trend following, allocation, risk parity, volatility targeting

**Cross-check completeness estimate of first read:** 0.85 - the first reader captured the speed/V-shape analysis, three allocation papers and the sizing framework; missed several secondary points (risk-budget reallocation before August, vol-scaling versus signal change, convexity not tested, zero expected return input, EMH discomfort) and made one speaker split error and small date and ranking slips.

## Argument map

**Episode thesis:** Baltas and Kaastrup-Larsen argue that the August 2024 V-shaped reversal is not a reason to change trend models: no speed is best across episodes (medium speeds did worst in the V, long lookbacks do best in long, meaningful equity crises), and short-term trend following is probably unprofitable in the long run. Recent risk-based allocation papers say to scale exposure by realised volatility (and correlation, if not too noisy) because risk is forecastable and returns are not. On how much to allocate to trend, Baltas argues that mean-variance and downside-risk optimisation give absurdly high numbers (about 70% and 52%), so size by scenario analysis against tracking error to the policy benchmark, ideally by moving trend into the strategic benchmark (5-20%).

### Nick Baltas (systematic macro quant researcher and trend follower; co-author of a 2019 paper on how much to allocate to trend following (caption 'Nick Balter'))
Fingerprint: #approach/trend_following #approach/position_sizing_vol_target #approach/diversification_risk_parity #approach/portfolio_construction_stacking #approach/research_robustness_overfitting #approach/regime_detection #approach/carry #approach/manager_selection_allocation
_Speaker note: Captions have no labels. Attribution uses first-person facts: client conversations after August, co-authorship of the 2019 sizing paper, a paper he wrote 'seven or eight years back' on return prediction. Kaastrup-Larsen's turns include his barometer and his own firm's research. The ledger correction to C17-1 splits it: the debt-level remark is the host's, the 60/40-as-a-carry-trade remark is Baltas agreeing._

**Worldview premises**
- Risk is forecastable but returns are not at short horizons: volatility clusters and today's volatility predicts tomorrow's volatility, but is unrelated to tomorrow's return; elevated risk after a fall implies positive returns only over 1-5 year horizons. _[empirical, stated; support: a Man Group paper ('Risky Business') on 100 years of US stock data, which he summarises]_ ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C09-2|C09-2]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C10-2|C10-2]])
- A 60/40 portfolio holds about 90% equity risk and 10% bond risk and in down markets risk rises without compensation, and the stock-bond correlation turned positive in 2022, so exposure should be scaled by realised volatility, and correlation incorporated if not too noisy. _[empirical, stated; support: the same paper and a risk-parity allocation paper; the 2022 experience]_ ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C09-3|C09-3]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C11-1|C11-1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C11-2|C11-2]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C12-1|C12-1]])
- Over long horizons static and dynamic exposure converge because volatility mean reverts, but scaling by volatility matters locally, around turning points, which is where money is managed. _[theoretical, stated; support: reasoning on volatility clustering and mean reversion; a 7-8 year old paper on constrained return forecasts]_ ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C10-2|C10-2]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C10-3|C10-3]])
- Return prediction models constrained to positive forecasts look better over the long run only because equity returns are positive by design; they may not keep an investor solvent when returns are negative. _[theoretical, stated; support: his earlier paper on equity return prediction (with a friend)]_ ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C10-3|C10-3]])
- Trend following pays in sustained equity or bond stress years, not in short-lived V shapes: the worst S&P years since 2000 were 2002, 2008 and 2022, the best CTA years were 2008, 2022 and (depending on index) 2002, with 2014 fourth; short moves of days or weeks are not trend's domain and need options. _[empirical, stated; support: calendar-year ranking from memory; the host's guesses are confirmed]_ ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C08-2|C08-2]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C07-3|C07-3]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C08-1|C08-1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C07-X1|C07-X1]])
- Speed is a trade-off with no sweet spot: slower means less reactivity and missed turns; faster means more false positives and higher costs, so speed needs strong cost control. _[theoretical, stated; support: type I and type II error framing; his firm's speed analysis]_ ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C06-2|C06-2]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C05-1|C05-1]])
- Conventional optimisation cannot size trend following: any expected return input is either zero (no ex ante basis, it should not work in theory) or the historical Sharpe, which makes mean-variance recommend about 70% in trend; minimising downside risk gives about 52% (1999-2019 data). Both are too high for institutions. _[empirical, stated; support: his November 2019 sizing paper; a similar recent paper by a large CTA reached the same conclusion]_ ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C14-2|C14-2]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C15-1|C15-1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C15-X1|C15-X1]])
- Institutions are judged against a benchmark (policy portfolio), so the size of an alternative is limited by tracking error and career risk, not by return maximisation; larger sizes improve tail, Sharpe and downside, and the horizon (1 versus 10 years) changes the value. _[institutional, stated; support: the 2019 paper's scenario analysis of 2%, 5%, 10% and 15% sleeves]_ ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C15-2|C15-2]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C16-1|C16-1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C16-R1|C16-R1]])
- Efficient-market premises make people uncomfortable with trend following (past returns should not predict future returns), yet the fact that they do cannot be ignored. _[behavioural, stated; support: attributed to Andrew Beer's recent remark]_ ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C15-X2|C15-X2]])
- Inflation regimes call for short bonds, short equities, long commodities, which means paying the equity risk premium, term premium and negative roll yield; trend following lets an investor be dynamic around these costs. _[theoretical, stated; support: his earlier discussions about 2022; the Longtail Alpha paper]_ ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C13-3|C13-3]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C13-1|C13-1]])

**Chain: August 2024: why trend lost on the equity reversal**
1. year-to-date equity rally and carry trades → trend portfolios piled into equities (the only market trading much): dynamic risk scaling and conviction overweighted the asset class ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C04-1|C04-1]])
2. short fixed-income trade reversed in Q2; positive equity-bond correlation → equity risk cut in May-June, then re-added before the August reversal as rates exposure was cut: a risk-budget rule can add to the position about to reverse ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C04-2|C04-2]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C04-X1|C04-X1]])
3. V-shaped reversal and yen/China/Indonesia carry unwind → losses in equities and currencies (FX the worst attribution in a trend program in 25 years): trends were fading before the shock and then reversed ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C04-1|C04-1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C04-3|C04-3]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C06-X2|C06-X2]])
- Evidence: Return attribution by asset class from his firm; the host's observations on risk scaling.
- Fails when: He says this is data mining, not a lesson: other V shapes would favour other choices.

**Chain: V-shape and speed: the middle gets caught**
1. fast signal (about 1-2 month) → goes short on the fall and long on the recovery: participates in both legs ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C05-1|C05-1]])
2. slow signal (12 month) → barely reacts, stays long through the rebound: little change in exposure by the trough ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C05-1|C05-1]])
3. medium signal (3-6 month) → flips short near the trough and misses the rebound: resonance-like timing mismatch ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C05-1|C05-1]])
- Evidence: His firm's analysis of speeds for August 2024; he did not expect the result.
- Fails when: Different episodes favour different speeds (Covid, a 3-4 week downturn, favoured faster than longest, and longer models still got short in time); a false positive, not a reason to change the model.

**Chain: Carry-optimised trend inside a risk-parity stock-bond portfolio**
1. risk parity stocks and bonds, both long → both fall when the stock-bond correlation turns positive (2022): no diversifier in a positive-correlation selloff ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C12-2|C12-2]])
2. adding trend following → helps, especially 2022; replacing bonds with trend gives a similar or worse portfolio over the long run: historically long bonds earned enough that shorting them cost carry ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C12-2|C12-2]])
3. carry filter: no shorts in positively carrying assets (upward-sloping bond curves) and no longs in negative-carry markets → avoids carry drag before 2022 while still benefiting in 2022; keeps commodities from lowering Sharpe: does not pay negative roll or term carry ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C13-1|C13-1]])
- Evidence: Longtail Alpha paper; sample 1998-2023.
- Fails when: He notes the host's objection: the sample coincides with the carry regime, so the enhancement may be overfit.

**Chain: Sizing trend by tracking error to the benchmark**
1. mean-variance with historical Sharpe, or minimum downside risk → about 70% or 52% in trend, unrealistic: trend's historical Sharpe exceeds a stock-bond portfolio's ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C15-1|C15-1]])
2. institutions are judged against a policy portfolio → the active-risk (tracking error) cost of a sleeve is the binding constraint: career and business risk ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C15-2|C15-2]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C16-1|C16-1]])
3. scenario analysis of 2%, 5%, 10%, 15% sleeves against tracking error → choose a size that balances tail benefit and tracking error; not too small to matter: bigger sleeves improve tail, Sharpe and downside ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C16-1|C16-1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C16-R1|C16-R1]])
4. put trend inside the strategic benchmark (5-20%) → the benchmark absorbs the tracking error and allows bigger sizes: tracking error is measured against the new benchmark ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C16-2|C16-2]])
- Evidence: 2019 paper (data 1999-2019); a similar recent paper by a large CTA.
- Fails when: A 1-year versus 10-year horizon changes the value.

**Decision process**
- [sizing] Scale exposure inversely to realised volatility (static to vol-targeted risk allocation with a top-level leverage adjustment), and incorporate correlations if not too noisy.. Why: you scale down before negative return realisations and up before positive ones; reduces vol of vol ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C09-3|C09-3]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C10-2|C10-2]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C11-1|C11-1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C11-2|C11-2]])
- [research] Do not change a trend model because of one episode; label such findings as data mining or false positives.. Why: other episodes would give the opposite answer (Covid versus August 2024) ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C05-1|C05-1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C07-1|C07-1]])
- [signal] Run a cloud of lookbacks with dynamic selection and filter trends that pay negative carry (carry-optimised trend).. Why: improvements over fixed lookbacks (host's firm) and over pre-2022 carry drag (paper) ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C06-1|C06-1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C13-1|C13-1]])
- [portfolio] Add trend following to the stock-bond portfolio rather than replacing bonds with it.. Why: replacement gives a similar or worse long-run portfolio ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C12-2|C12-2]])
- [portfolio] Size trend by scenario analysis of sleeves (2-15%) against tracking error to the policy portfolio; ideally include 5-20% trend in the strategic allocation.. Why: optimiser outputs are unusable; benchmark absorbs tracking error ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C16-1|C16-1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C16-2|C16-2]])
- [risk] For short-lived dips (days to weeks) use options protection rather than relying on trend.. Why: trend is not designed for these but options are more expensive ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C07-3|C07-3]])

**Evidence style:** Quant researcher: own backtests and attribution (speed, FX), published papers (his 2019 sizing paper, Man, Longtail Alpha), and careful labelling of what is data mining versus a robust result; uses physical analogies (resonance on a bridge).

**Views at the time**
- (2024-10-04) After August 2024 clients moved from carry-seeking to defensive; interest in trend following rose and no client unwound a trend allocation.. Reasoning: asset owners understand that sustained drawdowns, not V shapes, are where trend pays ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C01-1|C01-1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C08-1|C08-1]])
- (2024-10-04) China's September stimulus lifted Chinese equities and spilled into commodities such as iron ore; September was strong for commodities but not for systematic commodity strategies.. Reasoning: weather, energy and China drivers differed across commodities ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C02-2|C02-2]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C03-1|C03-1]])
- (2024-10-04) FX attribution in a trend program in 2024 is the worst of any calendar year in at least 25 years.. Reasoning: yen, China and Indonesia currency carry unwind in August ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C04-3|C04-3]])
- (2024-10-04) Asset owner interest in trend following and in challenging 60/40 has risen since 2022 as bond risk was realised; 60/40 worked as a carry trade plus falling yields, and it is open which of those can persist.. Reasoning: questions asked more than five years ago are now live ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C17-2|C17-2]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C17-1|C17-1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C17-R1|C17-R1]])

### Niels Kaastrup-Larsen (host, Top Traders Unplugged; long-term trend follower background)
Fingerprint: #approach/trend_following #approach/regime_detection #approach/research_robustness_overfitting #approach/short_term_systematic #approach/policy_reaction_central_banks #approach/debt_cycle_long_term #approach/behavioral_sentiment
_Speaker note: Host, who also argues positions on speed, sizing, carry-optimised trend and debt. The recording date is Friday 4 October 2024 (ledger correction): his trend barometer of 36 is for Thursday 3 October and the index numbers are as of Wednesday night 2 October. His memory of Roy Niedhoefer's 2014 paper is approximate._

**Worldview premises**
- Short-term trend following is probably not profitable even if short-term trading can be: in a 20-year simulation with fixed lookbacks from 20 to 260 days, 20 days was by far the worst, 60-130 days improved a lot, 260 days improved by a big factor, and dynamic parameter selection improved further. _[empirical, stated; support: his firm's simulation, with the usual simulation disclaimers; treatment of costs not stated]_ ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C06-1|C06-1]])
- In the very fast August 2024 reversal, models cut exposure mainly through volatility scaling (volatility expansion), not through signal changes; the result depended on how yen and Nikkei positions had been handled during the summer. _[experience, stated; support: his firm's models]_ ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C06-X1|C06-X1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C06-X2|C06-X2]])
- Longer lookbacks give more performance in meaningful, long equity crises; short dips are too quick for trend, which is the price of long-term compound growth, and overthinking models to remove bad periods ends badly. Speed performance depends on the episode (Covid's 3-4 week downturn was long enough for longer-term models). _[experience, stated; support: his research on lookbacks and crises; the Covid example]_ ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C07-2|C07-2]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C05-2|C05-2]])
- CTAs are first and foremost risk managers: returns cannot be forecast but risks can (Man Group paper). Reducing exposure in a vol spike implicitly plays a trend; early trend followers used static sizing but technology allows dynamic sizing. _[theoretical, stated; support: the Man paper and trend-following history]_ ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C09-1|C09-1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C09-4|C09-4]])
- Dynamic sizing is used by most bigger managers but long-run returns of static and dynamic managers are hard to tell apart, as is 500 versus 50 markets; the host does not buy that 500 markets are better than 50. _[experience, stated; support: observation of managers; no data]_ ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C10-1|C10-1]])
- Carry-optimised trend is based on 1998-2023, the carry regime, so the enhancement may be overfit; purity (no clever filters, no forecasting) is more robust in an unknowable future even if it costs something. Roy Niedhoefer's 2014 prediction that rising rates would hurt trend followers failed, showing nobody knows. _[experience, stated; support: sample-period argument; the 2014 paper and its aftermath]_ ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C13-2|C13-2]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C14-R1|C14-R1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C14-1|C14-1]])
- High government debt levels are part of why 40% in bonds may be too risky now. _[theoretical, stated; support: debt level data he saw in a newsletter; no government default so far]_ ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C17-1|C17-1]])
- Large wage settlements (dock workers 62% over six years, Boeing rejecting 30%) signal a shift in labour bargaining power that could spark inflation, with EU 45% EV tariffs and higher energy prices adding price pressure. _[empirical, stated; support: news items in the week of recording]_ ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C02-1|C02-1]])

**Chain: Why longer lookbacks do better in real crises**
1. a meaningful, long equity crisis → longer lookbacks are short equities and long bonds in time: the downturn lasts long enough for slow signals ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C07-2|C07-2]])
2. short-lived dips → too quick for trend following: signals react after the dip ends ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C07-2|C07-2]])
3. removing bad periods by overthinking the model → worse long-run outcome: price of compound growth ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C07-2|C07-2]])
- Evidence: Simulations of lookbacks across crises (not shown in detail).
- Fails when: Fast crises (Covid-type 3-4 weeks may favour faster speeds); different episodes give different winners.

**Decision process**
- [signal] Uses a cloud of lookbacks with dynamic selection rather than a fixed lookback; avoids very short (20-day) trend.. Why: 20-day was by far the worst in the 20-year simulation; dynamic selection improved results ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C06-1|C06-1]])
- [sizing] Dynamic position sizing, with correlation-based risk management that cut equity exposure over the summer when rates positions were reversing.. Why: risk management by volatility and correlation ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C04-2|C04-2]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C06-X1|C06-X1]])
- [other] Tracks his trend barometer (36 on 3 October 2024, weak) as an environment gauge.. Why: weak readings were reflected in October performance ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C03-2|C03-2]])

**Evidence style:** Practitioner: his firm's simulations, observation of managers, history of the industry and published papers; stresses purity and caution about overfitting.

**Views at the time**
- (2024-10-04) Early October 2024: BTOP50 -78bp (+3.34% YTD), SG CTA -92bp (+1.56%), SG Trend about -1%, short-term traders -63bp (-10bp YTD); MSCI World about -1.25% (+16%), S&P 500 about -1% (+19.5%).. Reasoning: index data as of Wednesday night; barometer 36 ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C03-2|C03-2]])
- (2024-10-04) Labour bargaining power is shifting, which with tariffs and energy prices could spark inflation.. Reasoning: wage settlements, EU tariffs on Chinese EVs, Middle East energy move ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C02-1|C02-1]])
- (2024-10-04) August 2024 was a non-event for allocators, but 2022 opened discussions, and more asset owners are now serious about trend strategies.. Reasoning: events like 2022 convert research into action ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C08-X1|C08-X1]])
- (2024-10-04) 40% in bonds may be too risky given government debt levels.. Reasoning: bond sell-off showed risk; debt accumulation ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C17-1|C17-1]])

### Disagreements
- **Is carry-optimised trend an improvement?**: Nick Baltas: Describes the paper's carry filter as sensible: it avoids carry drag and commodity Sharpe loss while keeping the 2022 benefit; he adds that it is a nice paper but not groundbreaking. ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C13-1|C13-1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C12-2|C12-2]]); Niels Kaastrup-Larsen: The 1998-2023 sample coincides with the carry regime, so it may be overfit; purity is more robust in an unknowable future. ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C13-2|C13-2]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C14-R1|C14-R1]])
- **Static versus dynamic position sizing**: Nick Baltas: Dynamic scaling matters locally at turning points; long-run results converge because volatility mean reverts; static sizing would have helped in August 2024 but that is data mining. ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C10-2|C10-2]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C07-1|C07-1]]); Niels Kaastrup-Larsen: Most big managers use dynamic sizing but the long-run returns of static and dynamic managers are hard to tell apart. ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C10-1|C10-1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C09-4|C09-4]])
- **Which speed is best and what does August 2024 teach**: Nick Baltas: Medium speeds (3-6 months) did worst in the V shape, faster or slower did better, but no change to the model is warranted. ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C05-1|C05-1]]); Niels Kaastrup-Larsen: Agrees no speed is best; someone convinced that a medium speed is the best would see it as the worst here; longer lookbacks are better in long crises, short-term trend following is not profitable long run. ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C05-2|C05-2]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C06-1|C06-1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C07-2|C07-2]])

### Gaps and conflicts
- The speed result for August 2024 is a single episode; Baltas himself calls it a typical false positive and data mining, so the 'medium speed does worst' finding has no out-of-sample support. ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C05-1|C05-1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C07-1|C07-1]])
- The 20-year lookback simulation's treatment of costs is not stated (ledger correction), so the conclusion that 20-day trend is by far the worst cannot be separated from cost effects; Baltas separately says cost impact grows with speed. ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C06-1|C06-1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C06-2|C06-2]])
- The calendar-year ranking of best CTA years depends on index variant: Baltas says 2002 is one of the top three depending on the index and 2014 fourth; this is recalled from memory. ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C08-2|C08-2]])
- The ledger records the sizing figures (70% mean-variance, 52% downside) from a 2019 paper using 1999-2019 data; the figures change with sample and Sharpe input, and Baltas says the exact Sharpe 'does not matter'. ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C15-1|C15-1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C15-X1|C15-X1]])
- The risk-budget explanation of August (equity risk re-added just before the reversal) is the host's and Baltas's reading of attribution, not shown with data, and conflicts in emphasis with the view that exposures simply followed trends. ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C04-X1|C04-X1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C04-1|C04-1]], [[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C04-2|C04-2]])
- Baltas's convexity point (August did not test the smile) is a claim that the month ended positive and the downturn was too short; no scatter plot is shown. ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C07-X1|C07-X1]])
- The host's claim that trading 500 markets is not better than 50 and that static and dynamic managers look alike is offered without evidence. ([[MT200 - Trend Following- How much to Allocate- - Systematic Investor 316#^MT200-C10-1|C10-1]])

### Forward-looking inputs (reader synthesis)
(reader) Observable inputs the speakers treat as leading outcomes: realised volatility (forecasts next volatility, not return) for exposure; the stock-bond correlation (positive correlation in 2022 raised overshoot risk); term structure carry of bonds and commodities for carry-optimised trend; tracking error to the policy benchmark for sizing; asset owner enquiries after bond losses; wage settlements, tariffs and energy prices as inflation drivers; government debt levels for bond risk. Horizons: 1-5 years for return after elevated risk, one versus ten years for sizing.

### Reader inferences (not stated by the speakers)
- Baltas's own sizing argument depends on the benchmark: the same trend sleeve is 'small' or 'large' depending on whether it sits inside the strategic allocation, so the answer to 'how much' is a governance choice as much as an optimisation result.
- The speed result (medium worst in a V shape) and the host's lookback simulation (longer lookbacks better over 20 years) are consistent only if the V shape is rare; a model combining speeds would hedge both.
- If risk is forecastable and returns are not, the volatility-scaling advice and the carry filter both aim to avoid cost without forecasting returns; neither speaker tests whether this holds out of the 1998-2023 sample.
- Both speakers treat allocator behaviour (no unwinding after August, rising interest since 2022) as a function of drawdown type: V shapes do not trigger redemptions, but sustained losses do.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | intro; clients defensive after August, less carry appetite |
| C02 | 2 | OpenAI, wage settlements, tariffs, China stimulus |
| C03 | 2 | commodities in Sept, trend barometer and index numbers, August reflections intro |
| C04 | 3 | August equity/currency reversals, risk scaling, FX attribution |
| C05 | 2 | speed analysis for V shape, medium speed worst |
| C06 | 2 | fixed lookback simulation 20-260 days, speed trade-off |
| C07 | 3 | static sizing, crisis protection, options |
| C08 | 2 | client behaviour after August; S&P/bond/CTA years |
| C09 | 4 | Man risk-not-returns paper, volatility predictability, 60/40 risk |
| C10 | 3 | dynamic vs static sizing, vol clustering, constrained forecasts |
| C11 | 2 | solvency of forecasts, correlation matters for vol target |
| C12 | 2 | risk allocation stages, Longtail trend and risk parity |
| C13 | 3 | carry-optimized trend, critique, inflation hedge |
| C14 | 2 | Niedhoefer 2014, sizing paper intro |
| C15 | 2 | mean-variance sizing, benchmark tracking error |
| C16 | 2 | scenario analysis sizing, strategic allocation |
| C17 | 2 | 60/40 questions, debt, outro |
| C18 | 0 | outro; nothing actionable |

## Claims

### C01
- **Nick Baltas** After August 2024 client appetite shifted from carry trades (dominant for about a year and a half) to a defensive mindset, raising interest in trend following.  #mech/behavioral _(time-bound view)_
  > post August we are seeing more and more and more of this defensive mindset coming back
  indicator: client risk appetite carry vs defensive · asset: multi · horizon: months · conditions: post August 2024 · testable: partly - investor flows · confidence: medium
  ^MT200-C01-1

### C02
- **Niels Kaastrup-Larsen** Large wage settlements (dock workers 62% over 6 years, Boeing rejecting 30%) signal a shift in labour bargaining power that could spark inflation; EU 45% EV tariffs and higher energy prices add to price pressure.  #mech/policy_reaction _(time-bound view)_
  > employers were uh at the wheel uh determining terms and now it seems that is changing
  indicator: wage settlements, tariffs, energy prices · asset: multi · horizon: months · conditions: Oct 2024 · testable: partly · confidence: medium
  ^MT200-C02-1
- **Nick Baltas** China's stimulus in Sept 2024 boosted Chinese equities and propagated into commodities such as iron ore after a year of falling prices.  #mech/policy_reaction _(time-bound view)_
  > this Chinese bazooka that has been uh Unleashed uh which have certainly had an impact on the markets
  indicator: Chinese stimulus, iron ore · asset: commodities · direction: long China equities and metals · horizon: weeks · conditions: Sept 2024 · testable: yes · confidence: medium
  ^MT200-C02-2

### C03
- **Nick Baltas** Commodities had a strong September 2024 for different reasons (weather, energy, China) but it was not a great month for systematic commodity strategies.  #mech/slow_reaction _(time-bound view)_
  > Commodities as a as a as a whole uh had a very strong um setember
  indicator: systematic commodity strategies · asset: commodities · horizon: weeks · conditions: Sept 2024 · testable: yes · confidence: medium
  ^MT200-C03-1
- **Niels Kaastrup-Larsen** Trend barometer 36 on 2 Oct 2024; BTOP50 -78bp in October (+3.34% YTD), SG CTA -92bp (+1.56%), SG Trend about -1% (garbled YTD), short-term traders -63bp (-10bp YTD), MSCI World -1.25% (+16%), global sovereign bonds -8bp (+2.34%), S&P 500 -1% (+19.5%).  #mech/slow_reaction _(time-bound view)_
  > my Trend barometer at the moment it finished at 36 yesterday so not uh you know not a great reading
  indicator: trend barometer, BTOP50, SG indices · asset: multi · horizon: weeks · conditions: Oct 2024 · testable: yes - public data · confidence: high
  **Correction (cross-check):** Date error: the recording was on Friday 4 October 2024 (the EU EV-tariff vote is reported as 'this morning'), so the barometer reading of 36 'yesterday' was for Thursday 3 October; only the CTA index numbers are 'as of Wednesday night' (2 October). → Niels' trend barometer finished at 36 on Thursday 3 October 2024 (weak); CTA indices as of Wednesday night 2 October: BTOP50 -78bp for October (+3.34% YTD), SG CTA -92bp (+1.56%), SG Trend about -1% for October (YTD garbled), short-term traders -63bp (-10bp YTD); MSCI World about -1.25% (+16% YTD), global sovereign bonds -8bp (+2.34%), S&P 500 about -1% (+19.5%).
  ^MT200-C03-2

### C04
- **Nick Baltas** August 2024 equity reversal and yen/China/Indonesia currency carry unwind hit trend followers who were piling into equity trends, as expected; only equities traded much so dynamic risk scaling overweighted the asset class.  #mech/slow_reaction _(time-bound view)_
  > it does exactly what it says on the team you have been piling on historical Trends year to date equities have been rallying
  indicator: trend exposure concentrated in equities · asset: equities · horizon: weeks · conditions: V-shaped reversal after long rally · testable: yes · confidence: high
  ^MT200-C04-1
- **Niels Kaastrup-Larsen** From Q2 2024 the reversal of the short fixed-income trade, plus correlation-based risk management, reduced equity exposure over the summer before the August reversal.  #mech/risk_management _(time-bound view)_
  > reversal of the short fixed income trade and for those who use correlations as part of their risk management that would actually lead to equ to the equity exposure being rever or reduced
  indicator: correlation-aware risk scaling · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT200-C04-2
- **Nick Baltas** FX attribution in a trend program in 2024 was the most negative of any calendar year across asset classes in at least 25 years.  #mech/cycle_persistence _(time-bound view)_
  > currencies including the August reversion have had so far I believe in 2024 the worst year of attribution in a trend program in their history
  indicator: FX trend attribution · asset: fx · horizon: years · conditions: 2024 YTD · testable: yes - trend FX attribution history · confidence: medium
  ^MT200-C04-3
- **Nick Baltas** Correlation-aware risk management cut equity risk in May-June while the short bond trade was reversing (two positively correlated longs), but as rates exposure was reduced approaching August the freed risk budget went back into equities just before the August reversal, so a risk-budget rule can add to the position that is about to reverse.  #mech/risk_management _(added by sonnet-xhigh cross-check, time-bound view)_
  > getting closer to August and reversion of those rates moves you ended up reducing the rates exposure and then just before the the reversion INE equities uh you ended up kind of allocating a bit more to equities
  indicator: correlation-based risk budgeting between equity and bond trend positions · asset: multi · direction: equity exposure cut May-June then raised before the August 2024 reversal · horizon: months · conditions: positive equity-bond correlation regime · testable: yes - replay the risk-budget path through June-August 2024 · confidence: medium
  ^MT200-C04-X1

### C05
- **Nick Baltas** In the August 2024 V shape a medium-speed trend (3-6 months) did worse than faster or slower speeds: fast speeds participate in fall and recovery, slow speeds barely react, but the middle gets reversed near the trough then misses the rebound. Not a reason to change the model (data mining, false positive).  #mech/slow_reaction _(time-bound view)_
  > having an average speed which is relatively I guess medium-term 3 to 6 months will get you worse off than being faster than that or slower than that
  indicator: trend lookback speed (1-12 months) · asset: equities · horizon: months · conditions: V-shaped sell-off and recovery · testable: yes - speed sweep on episodes · confidence: high
  ^MT200-C05-1
- **Niels Kaastrup-Larsen** In Covid, the 3-4 week downturn was long enough for longer-term models to be short equities and long bonds in time; speed performance depends on the episode, so one cannot conclude a best speed.  #mech/slow_reaction
  > it was actually um Co H and what I mean by that was that that downturn was just enough like three or four weeks
  indicator: trend speed in Covid vs August 2024 · asset: multi · horizon: weeks · testable: yes · confidence: medium
  ^MT200-C05-2

### C06
- **Niels Kaastrup-Larsen** In a 20-year simulation using fixed lookbacks from 20 to 260 days, 20-day trend following was by far the worst, 60-130 days improved a lot and similar, 260 days improved by a big factor; dynamic parameter selection (a cloud of lookbacks) improved further. Short-term trading can be profitable but short-term trend following probably is not.  #mech/slow_reaction
  > it not only is it by far the worst look back period
  indicator: 20-day to 260-day trend lookbacks · asset: multi · direction: longer lookbacks outperform · horizon: years · conditions: simulated, gross of full costs · testable: yes · confidence: high
  **Correction (cross-check):** The condition 'gross of full costs' is unsupported: Niels says only that the 20-year fixed-lookback result is a simulation subject to the usual disclaimers; costs are discussed afterwards as a general trade-off by Nick, not as a statement about this simulation. → Same claim, with condition 'simulated 20-year result, subject to simulation disclaimers; treatment of costs not stated'.
  ^MT200-C06-1
- **Nick Baltas** Choice of speed is a trade-off: slower means less reactivity (missing turning points), faster means more false positives and higher costs, and going faster requires strong cost control.  #mech/risk_management
  > the quicker you are then you have more false false positives
  indicator: speed vs cost trade-off · asset: multi · testable: yes · confidence: high
  ^MT200-C06-2
- **Niels Kaastrup-Larsen** In the very fast August 2024 reversal, trend models cut exposure mainly through volatility scaling (volatility expansion), not through the trend signal changing within those few days.  #mech/risk_management _(added by sonnet-xhigh cross-check, time-bound view)_
  > they reduced they reduced risk mainly because of vol expansion not so much about the signal making a change for those few days
  indicator: volatility-scaled position size versus trend signal · asset: equities · direction: positions reduced by vol expansion, not signal flips · horizon: days · conditions: very short sell-off with a V-shaped recovery · testable: yes - decompose exposure change into vol-scaling and signal components · confidence: high
  ^MT200-C06-X1
- **Niels Kaastrup-Larsen** Results in the August 2024 reversal depended on how the yen and Nikkei positions had been handled over the summer, since those trends were already being challenged and were weaker than earlier in the year.  #mech/slow_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > how you had handled the Yen the Nik over the summer months because there were signs of a change in direction or at least there were signs of those Trends being challenged
  indicator: yen and Nikkei trend strength, summer 2024 · asset: multi · horizon: months · conditions: trend fading before the reversal · testable: yes - attribute August 2024 P&L to yen and Nikkei positioning · confidence: medium
  ^MT200-C06-X2

### C07
- **Nick Baltas** Static position sizing would have helped in the August 2024 V shape because exposure would not be reduced into the trough, but this is data mining and not a lesson.  #mech/risk_management _(time-bound view)_
  > static position sizing would have helped because you wouldn't have reduced your Equity exposure throughout that vshape
  indicator: static vs volatility-scaled sizing · asset: equities · horizon: weeks · conditions: V shape · testable: yes · confidence: medium
  ^MT200-C07-1
- **Niels Kaastrup-Larsen** Longer lookbacks give more performance in meaningful, long equity crises; short-lived dips are too quick for trend following, which is the price of long-term compound growth, and overthinking models to remove bad periods ends badly.  #mech/risk_management
  > the longer you go um you actually get more performance during those uh periods where there is equity crisis
  indicator: trend lookback vs equity crisis protection · asset: equities · direction: longer lookback better in long crises · horizon: years · conditions: sustained drawdowns · testable: yes · confidence: medium
  ^MT200-C07-2
- **Nick Baltas** Short moves of a day, two days or two weeks are not trend following's domain; combining options protection with trend following is possible but more expensive.  #mech/risk_management
  > This is precisely the space that maybe require some contractual protection
  indicator: options plus trend following · asset: equities · direction: buy optionality · horizon: days · testable: partly · confidence: medium
  ^MT200-C07-3
- **Nick Baltas** August 2024 was not a test of trend following's convexity (the 'smile' scatter of trend returns against equity returns): the downturn was too short-lived and the month ended positive, so convexity would only have paid if the move had been contagious and a fast model had reacted.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > looking into August on a month that the market was positive doesn't even appear if you do your typical kind of Scar plot with a trend following smile
  indicator: trend-following smile (CTA returns vs equity returns) · asset: equities · horizon: months · conditions: convexity needs a sustained, contagious downturn · testable: yes - scatter of monthly CTA vs equity returns, label August 2024 · confidence: high
  ^MT200-C07-X1

### C08
- **Nick Baltas** After August 2024 no clients unwound their trend allocations; asset owners understand that long-term sustained drawdowns, not V shapes, are where trend following pays.  #mech/behavioral _(time-bound view)_
  > post August we've seen none of our um I guess um business activities or if you like discussions uh leading to any particular challenge
  indicator: client reaction to August · asset: multi · horizon: months · testable: no - anecdote · confidence: medium
  ^MT200-C08-1
- **Nick Baltas** The worst S&P years since 2000 were 2002, 2008 and 2022, the worst bond year was 2022, and the best CTA years were 2022, 2014, 2008 (2002 close), showing CTAs pay off in equity and bond stress years.  #mech/cycle_persistence
  > what are the three worst kalada years of S&P since 2000
  indicator: calendar-year S&P, bonds and CTA returns · asset: multi · horizon: years · conditions: equity and bond bear years · testable: yes - public data · confidence: high
  **Correction (cross-check):** Misstates the best CTA years. After Niels guessed 2022, 2014 and 2008, Nick says depending on the index variant 2002 is one of the top three and 2014 is the fourth ('those three plus one'). → Worst S&P years since 2000 were 2002, 2008 and 2022 (2022 also the worst bond year; GFC among the best bond years); the best CTA years were 2008, 2022 and (depending on index variant) 2002, with 2014 fourth.
  ^MT200-C08-2
- **Niels Kaastrup-Larsen** August 2024 was a non-event for allocators, but events like 2022 opened discussions, so more asset owners are now serious about trend strategies and willing to act on their research.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check, time-bound view)_
  > there are more people who are now serious and who want to dive deeper into these type of strategies
  indicator: allocator demand for trend following · asset: multi · direction: rising allocation interest after 2022 · horizon: years · testable: partly - flows into CTA / trend products · confidence: medium
  ^MT200-C08-X1

### C09
- **Niels Kaastrup-Larsen** Man Group paper 'Risky Business: why the smart money forecasts risk not returns': CTAs are first and foremost risk managers; returns cannot be forecast but risks can.  #mech/research_method
  > risky business why the smart money forecast risk not returns
  indicator: volatility forecast vs return forecast · asset: multi · testable: yes · confidence: high
  ^MT200-C09-1
- **Nick Baltas** In 100 years of stock data volatility clusters and persists, but today's volatility has no short-term forecasting power for returns while predicting tomorrow's volatility; high risk with down markets implies positive returns only over 1-5 year horizons.  #mech/risk_premium
  > there is no association between today's realization of volatility and tomorrow's returns
  indicator: realised volatility and subsequent returns · asset: equities · horizon: days · conditions: short horizon · testable: yes · confidence: high
  ^MT200-C09-2
- **Nick Baltas** A 60/40 portfolio carries about 90% equity risk and 10% bond risk, and in down markets risk rises without compensation, while the stock-bond correlation turned positive in 2022; hence scale exposure as a function of realised volatility.  #mech/risk_management
  > in a 640 portfolio it ends up being 90% Equity risk and 10% Bond risk
  indicator: 60/40 risk share, realised volatility · asset: multi · direction: scale down in vol spikes · horizon: years · conditions: stock-bond correlation positive · testable: yes · confidence: high
  ^MT200-C09-3
- **Niels Kaastrup-Larsen** Reducing exposure in a vol spike implicitly plays a trend; early trend followers used static sizing, but technology allows dynamic sizing.  #mech/risk_management
  > even by just reducing the exposure in a in in in a vol Spike you somehow implicitly play a trend
  indicator: volatility-scaled sizing · asset: multi · testable: yes · confidence: medium
  ^MT200-C09-4

### C10
- **Niels Kaastrup-Larsen** Most bigger managers use dynamic position sizing, but long-term returns of static and dynamic managers are hard to tell apart, as is 500 vs 50 markets; Niels does not buy that 500 markets is better than 50.  #mech/research_method
  > it is sometimes difficult to tell the difference once you zoom out a little bit between uh the two
  indicator: static vs dynamic sizing, number of markets · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT200-C10-1
- **Nick Baltas** Volatility clusters and mean reverts, so over long horizons static and dynamic exposure converge, but scaling by volatility matters locally around turning points; spikes have shown negative association with subsequent returns.  #mech/risk_management
  > volatility beyond the fact that it's clustering it's also mean revering
  indicator: volatility clustering and mean reversion · asset: multi · direction: scale down before negative returns · testable: yes · confidence: high
  ^MT200-C10-2
- **Nick Baltas** Return prediction models constrained to positive forecasts look better over the long run (equity returns are positive by design) but may not keep the investor solvent at the times returns are negative.  #mech/research_method
  > if you constrain your model to only predict positive numbers otherwise you should scrap your prediction
  indicator: constrained return forecasts · asset: equities · horizon: years · testable: yes · confidence: high
  ^MT200-C10-3

### C11
- **Nick Baltas** In a risk parity setup correlation only matters for top-level leverage under a vol target; when stocks and bonds correlate positively (2022) volatility overshoots, so incorporate correlation if it is not too noisy.  #mech/risk_management
  > in a risk parity World correlation only matters for the top level leverage if we have a vol Target
  indicator: correlation forecasting in vol targeting · asset: multi · conditions: vol target portfolio · testable: yes · confidence: high
  ^MT200-C11-1
- **Nick Baltas** The paper moves from nominal allocation to a vol-targeted risk allocation with a top-level leverage adjustment, reducing vol of vol.  #mech/risk_management
  > they say how about you have a vol Target which in itself allows you to scale the exposures inversely to V
  indicator: vol target with leverage adjustment · asset: multi · testable: yes · confidence: medium
  ^MT200-C11-2

### C12
- **Nick Baltas** Three stages: nominal allocation, static long-term risk allocation, then active risk allocation using realised volatilities and correlations, which performs best, similar to risk parity.  #mech/risk_management
  > nominal allocation long-term risk allocation as they call it static and then um active risk allocation
  indicator: nominal, static risk, active risk allocation · asset: multi · testable: yes · confidence: high
  ^MT200-C12-1
- **Nick Baltas** A Longtail Alpha paper shows adding trend following to a risk parity stock-bond portfolio helps, particularly in 2022, but replacing bonds with trend following over the long term gives a similar or worse portfolio.  #mech/risk_premium
  > hey Trend following can help you and they go into this journey of like adding Trend following
  indicator: trend following overlay on risk parity · asset: multi · direction: add trend, do not replace bonds · horizon: years · conditions: 2022 inflation regime · testable: yes · confidence: high
  ^MT200-C12-2

### C13
- **Nick Baltas** A carry-optimized trend program avoids shorting bonds with positive carry (upward term structure) and longing negative-carry markets, avoiding pre-2022 carry drag while still benefiting in 2022; adding commodities to stocks/bonds raises diversification but drops Sharpe unless carry filtered.  #mech/risk_premium
  > do not go long appreciating markets that have negative carry do not go short depreciating markets that have positive carry
  indicator: carry filter on trend signals · asset: multi · direction: skip trends that pay negative carry · horizon: years · conditions: carry regime · testable: yes · confidence: medium
  ^MT200-C13-1
- **Niels Kaastrup-Larsen** The carry-optimized trend benefit is based on 1998-2023, exactly when the carry regime started, so the enhancement may overfit; the next 20 years may differ (e.g. rates at 25%) and purity is more robust.  #mech/research_method
  > this is exactly what I mentioned earlier on trying to be too clever and adding stuff to a trend following model
  indicator: carry-optimized trend overfit risk · asset: multi · horizon: years · testable: yes - out of sample test · confidence: high
  ^MT200-C13-2
- **Nick Baltas** An inflation hedge is short bonds, short equities, long commodities, which means paying equity risk premium, term premium and negative roll yield; trend following lets you be dynamic around these.  #mech/risk_premium
  > one of the more successful inflation Hedges is to go short bonds you go short equities and you go long Commodities
  indicator: inflation hedge positioning · asset: multi · direction: short bonds, short equities, long commodities · horizon: years · conditions: inflation regimes · testable: yes · confidence: medium
  ^MT200-C13-3

### C14
- **Niels Kaastrup-Larsen** Roy Niedhoefer's 2014 paper argued trend followers would struggle when rates rise; instead shorting bonds became profitable, showing no one knows the future.  #mech/structural_shift
  > longer term Trend followers would not be able to make money when interest rate started to go up
  indicator: trend profits in rising rates · asset: rates · horizon: years · conditions: rising rates · testable: yes · confidence: medium
  ^MT200-C14-1
- **Nick Baltas** Conventional sizing (mean-variance optimisation) does not work for deciding how much to allocate to trend following; the 2019 paper and a recent large-CTA paper reach the same conclusion.  #mech/research_method
  > conventional ways of determining sizing do not work
  indicator: trend following allocation sizing · asset: multi · testable: yes · confidence: high
  ^MT200-C14-2
- **Niels Kaastrup-Larsen** Kaastrup-Larsen prefers a pure trend following approach without clever filters, forecasts or overfitting, accepting that it has a price, because it is more robust to an unknowable future.  #mech/research_method _(added by map cross-check)_
  > I like the purity of trend following not being too clever not trying to forecast not trying to overfit and yes you pay a price for it
  indicator: trend model purity · asset: multi · horizon: years · testable: partly - compare pure and filtered models out of sample · confidence: high
  ^MT200-C14-R1

### C15
- **Nick Baltas** Mean-variance analysis would put about 70% in trend following because its historical Sharpe is higher than a stock-bond portfolio; minimising downside risk gives about 52% (1999-2019 data), both too high for institutions.  #mech/risk_management
  > any minan variance analysis would tell you to do 70% Trend following 30% the remaining of your portfolio
  indicator: mean-variance optimisation allocation to trend following · asset: multi · testable: yes · confidence: high
  ^MT200-C15-1
- **Nick Baltas** Sizing must balance benchmark-relative active risk (tracking error to the policy portfolio) against benefits, since institutions are judged against a benchmark.  #mech/risk_management
  > anything you do away from it is an active risk decision
  indicator: benchmark tracking error · asset: multi · testable: yes · confidence: high
  ^MT200-C15-2
- **Nick Baltas** Asked what expected return to put into a mean-variance optimiser for trend following, Nick would say zero (no ex ante basis and it should not work in theory); yet using its historical Sharpe gives about 70% allocation, so optimiser inputs for trend are either unusable or absurd, which is why a different sizing method is needed.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > if you ask me I'm going to tell you zero because I have no clue and it shouldn't work in the first place
  indicator: expected return input for trend following in mean-variance optimisation · asset: multi · horizon: years · testable: partly - the optimiser output is a calculation; the zero input is a judgement · confidence: medium
  ^MT200-C15-X1
- **Nick Baltas** Citing Andrew's point: discomfort with trend following comes from the efficient-market premise that past returns should not predict future returns, but the empirical fact that they do cannot be ignored.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > people that don't feel comfortable about following is because it goes against their premises and their fundamental understanding of the market that you know past return should not predict future return
  indicator: time-series momentum / trend persistence · asset: multi · testable: yes - time-series momentum evidence · confidence: medium
  ^MT200-C15-X2

### C16
- **Nick Baltas** Assess scenario analysis for increments of trend allocation (2%, 5%, 10%, 15%) with tracking error against benchmark; larger sizes improve tail, Sharpe and downside but carry career risk, and the horizon (1 vs 10 years) changes the value.  #mech/risk_management
  > what you really have to assess is a scenario analysis and value ad of various increments of TR following allocation
  indicator: trend allocation increments and tracking error · asset: multi · direction: size 2-15% sleeves · horizon: years · testable: yes · confidence: high
  ^MT200-C16-1
- **Nick Baltas** Include trend following inside strategic asset allocation (5-20%) so the benchmark absorbs the tracking error.  #mech/structural_shift
  > maybe the Strat allocation should change and contain maybe five or 10% or 20% of trend following
  indicator: strategic allocation including managed futures · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT200-C16-2
- **Nick Baltas** Baltas says a trend allocation should not be too small because the impact would be tiny, but the larger it becomes the more conscious institutions must be about tracking error to their benchmark.  #mech/risk_management _(added by map cross-check)_
  > sizing it should not be too small because the impact would be tiny
  indicator: trend allocation size versus tracking error · asset: multi · horizon: years · conditions: institution judged against a benchmark · testable: yes - scenario analysis of sleeve sizes · confidence: medium
  ^MT200-C16-R1

### C17
- **Niels Kaastrup-Larsen** High government debt levels may make a 40% bond allocation too risky; the 60/40 was a carry trade plus yield reduction at a turning point.  #mech/fiscal_debt _(time-bound view)_
  > maybe 40% in bonds is way too risky today compared to what it was 20 years ago
  indicator: government debt levels, bond risk · asset: rates · horizon: years · testable: no · confidence: medium
  **Correction (cross-check):** Wrong speaker for part of the claim. Niels makes the debt-level point (40% in bonds may be too risky); the closing remark that 60/40 was a carry trade and a yield reduction at a turning point is Nick agreeing, and he asks which of those components can still exist. → Niels: high government debt levels should be part of why 40% in bonds is too risky today. Nick (agreeing): 60/40 worked as a carry trade plus falling yields at a turning point, and it is an open question which of those components can persist.
  ^MT200-C17-1
- **Nick Baltas** Asset owner interest in trend following and challenging 60/40 has risen since 2022 as bond risk was realised.  #mech/behavioral _(time-bound view)_
  > the fact that this report became again relevant for a good amount of our clients is precisely the consequence of those questions now being asked much more
  indicator: asset owner demand · asset: multi · horizon: years · conditions: post-2022 · testable: no · confidence: medium
  ^MT200-C17-2
- **Nick Baltas** Baltas says his 2019 sizing paper became relevant again for many clients because asset owners are asking more questions about 60/40 and trend than five years ago.  #mech/structural_shift _(added by map cross-check, time-bound view)_
  > the fact that this report became again relevant for a good amount of our clients is precisely the consequence of those questions now being asked much more than in the past
  indicator: asset owner interest in trend sizing · asset: multi · direction: rising interest in trend allocations · horizon: years · testable: partly - client enquiry and flow data · confidence: medium
  ^MT200-C17-R1

