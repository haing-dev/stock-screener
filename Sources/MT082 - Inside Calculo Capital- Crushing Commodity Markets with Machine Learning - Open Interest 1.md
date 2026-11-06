---
source_id: MT082
title: "Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 15"
date: 2025-04-27
channel: "Top Traders Unplugged"
url: 
words: 7343
claims: 51
added_by_crosscheck: 5
corrections: 2
crosscheck: "opus cross-check"
speakers: ["Philip Engel Carlson (founder, Calculo Capital)", "Ola Hansen (Saxo Bank commodity strategist, Calculo board member)", "Moritz Seibert (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 15

**Speakers:** Philip Engel Carlson (founder, Calculo Capital); Ola Hansen (Saxo Bank commodity strategist, Calculo board member); Moritz Seibert (host, Top Traders Unplugged)

**Summary:** Interview with Calculo Capital, a Copenhagen short-term (2 to 5 day) systematic commodity CTA. Classical breakout trend-following entries, machine learning used only for exits via pattern matching to historical trades; plus Saxo's commodity outlook for early 2025 (precious metals, tariffs, natural gas).

**Approach:** trend following, commodities, machine learning exits, short-term CTA

**Cross-check completeness estimate of first read:** 0.90 - Calculo's method and Ola's outlook are well covered; missed the China-tariff copper driver, ML-noise caveat, no-curve design point, index composition and broad backwardation, and misattributed the host's natural gas trade to Calculo

## Argument map

**Episode thesis:** Philip Engel Carlson runs Calculo Capital, a commodities-only CTA with 2-5 day holds: classical price-breakout trend entries, with machine learning used only after entry to flag exits by matching a trade's daily candlestick and momentum pattern to historical trades with known next-day outcomes, which smooths returns and keeps volatility low. Ola Hansen (Saxo commodity strategist and Calculo investor) adds a bullish long-term commodity case built on deglobalization, defense, energy transition, de-dollarisation and under-investment, plus early-2025 tariff dislocations in COMEX precious metals and copper.

### Philip Engel Carlson (Founder of Calculo Capital (Copenhagen), short-term systematic commodity CTA, founded 2018)
Fingerprint: #approach/trend_following #approach/short_term_systematic #approach/commodity_fundamentals #approach/research_robustness_overfitting #approach/position_sizing_vol_target #approach/costs_execution #approach/crisis_alpha_convexity
_Speaker note: Auto-captions render names as Philillip, Kalculo and similar. Ledger corrections: the two-year short Henry Hub trade and the contango roll-yield remark belong to host Moritz Seibert's own long-term fund, not Calculo; those claims are mapped to Seibert and Ola Hansen._

**Worldview premises**
- Supply and demand constraints in commodities (weather, regional events) create fear and price moves that trend following can capture, which is why the strategy works in commodities but not in equities or interest rates. _[theoretical, stated; support: Explanation of why he trades commodities only; no data.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C05-3|C05-3]])
- Predicting where a market goes is a guess; trends have strength, so entry should be a simple trend breakout and machine learning should not be used for price prediction. _[theoretical, stated; support: Personal belief; avoids the overfitting problem of price-prediction models.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C08-2|C08-2]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C08-3|C08-3]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C08-1|C08-1]])
- Capturing parts of a trend and avoiding counter-moves gives a smoother ride than classical long-horizon trend following, at the cost of not capturing the whole trend. _[theoretical, stated; support: Design rationale; reported return and volatility figures.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C07-4|C07-4]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C06-3|C06-3]])
- After a shock the market often moves sideways while participants wait for news (the hurricane path), and that limbo carries data that identify when to take profit and when to re-enter. _[behavioural, stated; support: Hurricane example.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C06-4|C06-4]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C06-5|C06-5]])
- Shorter-horizon trading needs liquid markets, so only the most liquid commodities are traded; this also lets the fund scale. _[institutional, stated; support: Contrast with slow trend followers trading illiquid markets such as orange juice.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C05-4|C05-4]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C06-1|C06-1]])
- A low-volatility, non-correlated, non-cyclical commodity return stream is an add-on for investors. _[experience, stated; support: Self-reported: equity-like returns at two-thirds of stock index volatility since inception.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C10-6|C10-6]])

**Chain: Shock, risk premium and machine learning exit**
1. A weather or regional supply event (hurricane threat) → Price jumps as risk premium is added: Fear about supply ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C06-4|C06-4]])
2. Market waits on the storm path → Prices stabilise or trade sideways; some traders take profit: Limbo while news is awaited ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C06-4|C06-4]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C06-5|C06-5]])
3. Daily pattern of the open trade (candlesticks, momentum angle) matches historical trade patterns → Model flags keep or eliminate using T+1 and T+2 outcomes of similar trades: Known historical outcomes of similar patterns ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C07-3|C07-3]])
4. Eliminate flag → Exit during liquid hours and look for a new entry in the same trend if it resumes: The flag is a warning, not a price forecast ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C09-1|C09-1]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C06-5|C06-5]])
- Evidence: Description of method only; no backtest statistics beyond the claim of equity-like returns at two-thirds volatility.
- Fails when: If the market resumes the trend, exiting early forgoes part of the move (he accepts this and re-enters); not otherwise stated.

**Decision process**
- [signal] Entries are classical CTA price breakouts, up or down, trend only, with no mean reversion; inputs are price only, no weather data and no manual override.. Why: Predicting direction is a guess; trends have strength. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C06-2|C06-2]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C08-1|C08-1]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C06-6|C06-6]])
- [signal] Machine learning exits: each day match the open trade's candlestick and momentum features to a database of historical trades with known T+1 and T+2 outcomes and classify as keep or eliminate; this handles about 75-80% of exits, the rest by stops and trailing stops.. Why: Takes profit during stabilisation and reduces volatility. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C07-3|C07-3]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C07-2|C07-2]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C05-2|C05-2]])
- [universe] Only the most liquid metals, agriculturals, softs and energies; no smaller markets such as orange juice.. Why: Short horizon makes the strategy liquidity sensitive; scalability. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C05-4|C05-4]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C06-1|C06-1]])
- [portfolio] Can be flat, partly long or partly short; no mandatory allocation to any market, sector or direction.. Why: Participate only in real alpha periods. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C07-1|C07-1]])
- [execution] Use advanced algos to enter and time machine learning exits to the most liquid US hours; stops are executed as they trigger.. Why: Flags are warnings, not firm predictions, so there is no need to exit at once. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C09-1|C09-1]])
- [research] Daily bars are the emphasis for the machine learning classification; holding period 1-10 days, typically 2-5.. Why: Fits his trend methodology. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C07-4|C07-4]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C05-2|C05-2]])
- [other] No use of forward-curve information (contango, backwardation, seasonality) as a signal and no calendar spreads; outright futures only.. Why: Price-pattern-only design. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C09-X1|C09-X1]])
- [risk] Aim for very low-volatility access to commodities and a smoother return profile through post-entry risk management.. Why: Commodities are volatile. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C06-2|C06-2]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C06-3|C06-3]])

**Evidence style:** Design rationale and self-reported performance; no statistics on the machine learning exit effect are given, and he does not show how overfitting of the pattern database is controlled beyond restricting it to exits.

### Ola Hansen (Saxo Bank commodity strategist (author of the Saxo weekly commodity update), Calculo board member since 2022 and investor)
Fingerprint: #approach/commodity_fundamentals #approach/structural_themes #approach/geopolitics #approach/fiscal_dominance #approach/positioning_crowding #approach/diversification_risk_parity #approach/manager_selection_allocation
_Speaker note: Date inferred as 20 February 2025 from the remark 'today is the 20th of February' (spoken in a turn whose speaker is uncertain; the content is the Henry Hub trade of Seibert's fund). Caption errors: 'terrorists' for tariffs. Hansen and Seibert turns alternate without clear markers._

**Worldview premises**
- Precious metals demand reflects an unbalanced, uncertain world: geopolitical risk, fiscal debt worries and central banks diversifying away from US dollar assets for three years. _[theoretical, stated; support: Price strength in 2024 and 2025 and observed central bank buying.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C02-2|C02-2]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C02-3|C02-3]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C02-4|C02-4]])
- A set of structural themes supports commodity demand: deglobalization, European defense spending, the energy transition (EVs, data centers, cooling), ageing populations spending savings and emerging-market urbanisation. _[theoretical, stated; support: Qualitative thematic reasoning.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C02-5|C02-5]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C02-6|C02-6]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C03-1|C03-1]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C03-2|C03-2]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C03-3|C03-3]])
- Long mining lead times and 10-12 year price guessing hold back supply investment and can cause metals shortfalls. _[institutional, stated; support: Industry knowledge.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C03-4|C03-4]])
- Softs are produced in small geographical areas and so are highly exposed to local weather. _[empirical, stated; support: Cocoa 2024 in West Africa, coffee 2025 in Brazil.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C03-5|C03-5]])
- Natural gas has a long-term bullish case from rising US exports, US domestic demand and European LNG demand. _[empirical, stated; support: Stated trends; 30% YTD rally in 2025.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C03-6|C03-6]])
- Tariff expectations create basis dislocations between COMEX and London prices that attract physical flows and cash-and-carry arbitrage, and unwind when spreads normalise. _[institutional, stated; support: Observed $1,000 premium spike and shipments of gold and silver to New York; basis about 10% annualised.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C04-1|C04-1]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C04-2|C04-2]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C04-3|C04-3]])
- Silver is more vulnerable to squeezes and tariff risk than gold because no lender of last resort exists and much supply comes from Mexico. _[institutional, stated; support: Gold shorts can borrow from the Bank of England; silver has no equivalent.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C04-6|C04-6]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C05-1|C05-1]])
- Long-only commodity indices suffer deep, long drawdowns, so a long/short, lower-volatility strategy delivering similar returns is preferable and diversifies equity risk. _[empirical, stated; support: BCOM 77-month 38% drawdown (2015-20) and 22% drop after 2022.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C09-2|C09-2]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C09-3|C09-3]])
- Commodity index construction drives results: size limits exclude markets such as cocoa, rebalances force sales of winners, and smart-roll ETFs have not outperformed. _[empirical, stated; support: Cocoa and natural gas examples.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C10-2|C10-2]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C10-3|C10-3]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C10-4|C10-4]])
- Roll yield has turned positive (backwardation) across most commodities, with US natural gas the main exception (contango). _[empirical, stated; support: Curve structures he observes.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C10-X2|C10-X2]])

**Chain: Tariffs to COMEX premium to physical flows**
1. Tariff worries on imported metals → COMEX futures trade above London spot for gold, silver, copper and platinum: Imports would face tariffs, hurting hedgers' calculations ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C04-1|C04-1]])
2. Premium of futures over spot → Arbitrageurs ship physical gold and silver to New York and sell futures: Locks in a cash-and-carry return of about 10% annualised ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C04-2|C04-2]])
3. Premium narrows or tariffs are not imposed → Physical gold stranded in US vaults with no end user is sold or hedged: No natural buyer ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C04-3|C04-3]])
- Evidence: Observed price premium and shipments.
- Fails when: Not stated beyond normalisation of spreads.

**Chain: Electrification to copper and grid equipment**
1. Data centers, EVs and power demand → More copper needed, including for transmission: Power must be moved as well as generated ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C03-1|C03-1]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C04-4|C04-4]])
2. AI and electrification boom → Grid builders such as Siemens Energy capture gains (shovel sellers): Gold-rush analogy ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C04-5|C04-5]])
- Evidence: Siemens Energy up about 300% in the year.
- Fails when: Not stated.

**Decision process**
- [portfolio] Prefers a long/short, low-volatility commodity strategy (Calculo) as a part of general commodity exposure rather than long-only index exposure.. Why: Low volatility and low correlation; positive months when equities are weak; avoids long drawdowns. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C09-2|C09-2]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C09-3|C09-3]])

**Evidence style:** Market observation, recent price moves, historical drawdown figures and thematic narrative; no systematic testing.

**Views at the time**
- (2025-02-20) Long-term bullish on commodities: deglobalization, defense, energy transition, de-dollarisation, fiscal risk, demographics and supply under-investment.. Reasoning: Structural demand themes meet constrained supply. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C02-5|C02-5]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C02-6|C02-6]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C03-1|C03-1]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C03-2|C03-2]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C03-3|C03-3]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C03-4|C03-4]])
- (2025-02-20) Early 2025 started strongly: BCOM up almost 10%, ahead of equities; gold up about 15%.. Reasoning: Broad sector gains and safe-haven demand. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C02-1|C02-1]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C02-2|C02-2]])
- (2025-02-20) Copper rallied about 15% because China had not yet been hit with US tariffs and COMEX pricing dislocations; China demand held up despite construction.. Reasoning: Tariff and data-center demand. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C04-X1|C04-X1]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C04-4|C04-4]])
- (2025-02-20) Softs: coffee (Brazil) is the 2025 theme after cocoa (West Africa) in 2024.. Reasoning: Weather exposure of small production areas. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C03-5|C03-5]])
- (2025-02-20) Natural gas is long-term bullish and rallied about 30% in 2025 on cold weather.. Reasoning: US exports, domestic demand and European LNG demand. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C03-6|C03-6]])
- (2025-02-20) Silver has higher tariff and squeeze risk than gold; the unwinding of the COMEX premium could be a small negative for gold.. Reasoning: No lender of last resort in silver; stranded physical gold in the US. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C05-1|C05-1]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C04-6|C04-6]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C04-3|C04-3]])

### Moritz Seibert (Host of the Open Interest series; runs his own long-term trend-following fund)
Fingerprint: #approach/trend_following #approach/research_robustness_overfitting #approach/commodity_fundamentals #approach/replication_indexing
_Speaker note: Host. Ledger corrections: the two-year short Henry Hub position and the contango roll-yield remark belong to Seibert's fund, not Calculo._

**Worldview premises**
- Calculo Capital is a Copenhagen systematic CTA that trades only commodities, holds 1 to 10 days and uses machine learning in its process (host's framing of why the guest is interesting). _[institutional, stated; support: Introduction of the guest.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C01-1|C01-1]])
- Commodities have no equity-like positive drift and should be traded long and short. _[theoretical, stated; support: Assertion.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C10-1|C10-1]])
- Machine learning applied to price prediction risks fitting noise and would probably rediscover buying breakouts. _[theoretical, stated; support: Joke / view; he disclaims machine learning experience.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C08-X1|C08-X1]])
- Long-only commodity index choice drives commodity beta returns: first-generation indices (BCOM) are concentrated and exclude small markets while newer variants diversify along the curve. _[empirical, stated; support: Index construction knowledge.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C10-X1|C10-X1]])
- Slow trend followers need little liquidity and hold positions for years, whereas short-horizon traders are much more sensitive to liquidity. _[experience, stated; support: Own fund's orange juice position held for more than two years.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C06-1|C06-1]])
- In contango a short position earns roll yield (natural gas); his long-term trend fund held a short Henry Hub for more than two years until the late-February 2025 rally ended it. _[experience, stated; support: Own fund result.]_ ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C03-7|C03-7]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C10-5|C10-5]])

**Evidence style:** Own fund experience and interviewer questions.

**Views at the time**
- (2025-02-20) His trend fund's short Henry Hub position (two-plus years) was closed by the late-February 2025 rally.. Reasoning: Colder weather outlook triggered a reversal. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C03-7|C03-7]])

### Disagreements
- **Machine learning in trading: entry prediction versus exit management**: Philip Engel Carlson: Never use machine learning for entry; use it only post-entry for exit/risk because price prediction is a guess; exits cut volatility and smooth returns. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C08-2|C08-2]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C08-3|C08-3]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C06-3|C06-3]]); Moritz Seibert: Worried a machine would learn noise and probably rediscover buying breakouts (becoming a trend follower). ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C08-X1|C08-X1]])
- **Holding horizon and use of curve information**: Philip Engel Carlson: 2-5 day holds; ignores forward curves, contango and spreads and trades outright futures on price patterns. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C05-2|C05-2]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C09-X1|C09-X1]]); Moritz Seibert: His fund holds trends for years (orange juice over two years, Henry Hub short over two years) and earns roll yield in contango. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C06-1|C06-1]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C03-7|C03-7]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C10-5|C10-5]])

### Gaps and conflicts
- Speaker/fund attribution: first-read ledger entries attributed Seibert's two-year short Henry Hub trade and the contango roll-yield benefit to Calculo; Calculo holds 2-5 days and does not roll monthly, so both belong to Seibert's fund (correction fields in the ledger). ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C03-7|C03-7]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C10-5|C10-5]])
- Calculo's performance claim (equity-like returns at two-thirds of stock index volatility, non-correlated) is self-reported with no period statistics, fees or drawdown given. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C10-6|C10-6]])
- The machine learning exit is described as removing noise and volatility, but no out-of-sample test, database size, or evidence that it adds value over plain trailing stops is given; the keep/eliminate flag is also not a forecast. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C07-3|C07-3]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C07-2|C07-2]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C06-3|C06-3]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C09-1|C09-1]])
- Smoother returns come at the cost of capturing only part of each trend; the cost is acknowledged but not quantified. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C07-4|C07-4]])
- Statement that a trend-following model works in commodities but not equities/rates is asserted without evidence, while the fund trades only the most liquid markets. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C05-3|C05-3]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C05-4|C05-4]])
- Hansen's thematic bull case on commodities is not connected to Calculo's signals, which use only price and 2-5 day horizons; he invests for low volatility rather than for the themes. ([[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C02-5|C02-5]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C03-4|C03-4]], [[MT082 - Inside Calculo Capital- Crushing Commodity Markets with Machine Learning - Open Interest 1#^MT082-C05-2|C05-2]])

### Forward-looking inputs (reader synthesis)
(reader) For Calculo: only price patterns (breakouts, then daily candlestick and momentum features of the open trade) matter, over 2-5 days; no fundamentals. For Hansen: central bank gold buying, fiscal debt trends, US tariff decisions and COMEX-London spreads, China copper demand, mining lead times, weather in West Africa and Brazil, and US gas exports and LNG demand; horizons from weeks (tariff basis) to years (structural themes).

### Reader inferences (not stated by the speakers)
- (reader) The method is trend following with a pattern-matching nearest-neighbour exit filter; it assumes similar daily patterns have similar next-day outcomes, which would be fragile if regimes change.
- (reader) Calculo's low volatility likely comes from short holding periods, being flat often, and cutting trades early, not from forecasting skill.
- (reader) The investor-side (Hansen) rationale is portfolio diversification: lower drawdowns than long-only BCOM at comparable returns.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | Teaser of ML matching, disclaimers, host intro of Calculo and fund profile |
| C02 | 6 | Commodity market review early 2025; precious metals; long-term themes (deglobalisation, defence) |
| C03 | 7 | Energy transition, demographics, mining supply, softs, natural gas, Calculo gas trade |
| C04 | 6 | Copper, COMEX tariff premium, physical flows, silver |
| C05 | 4 | Calculo focus on commodities, holding period, liquidity, supply shocks |
| C06 | 6 | Entry signals, ML risk management, hurricane example, price-only inputs |
| C07 | 4 | Flat positions, exit methodology, ML matching, daily bars |
| C08 | 3 | Trend-only entries, ML for exit only |
| C09 | 3 | Execution timing, why Ola invests, BCOM drawdowns |
| C10 | 6 | Index design, roll yield, track record |
| C11 | 0 | Domicile, growth plans, outro (nothing actionable) |

## Claims

### C01
- **Moritz Seibert** Calculo Capital is a Copenhagen systematic CTA that trades only commodities with 1 to 10 day holding periods and uses machine learning in its trading process.  #mech/slow_reaction
  > Third, because they are short-term withholding periods of 1 to 10 days per trade.
  asset: commodities · horizon: days · testable: partly - strategy description, not a testable claim itself · confidence: high
  ^MT082-C01-1

### C02
- **Ola Hansen** The Bloomberg Commodity Index was up almost 10% in the first weeks of 2025, ahead of equities, with all sectors posting gains.  #mech/cycle_persistence _(time-bound view)_
  > I watch something like the Bloomberg commodity index which uh which is broadly exposed to agricultural com metals and energy and it's up nearly 10%
  indicator: Bloomberg Commodity Index YTD · asset: commodities · direction: commodities up · horizon: weeks · testable: yes - index data · confidence: high
  ^MT082-C02-1
- **Ola Hansen** Strong demand for gold and other precious metals, which yield nothing and cost money to store, is a hedge against an uncertain, unbalanced world.  #mech/risk_premium _(time-bound view)_
  > that really is just an expression of an a world that is not in balance.
  indicator: gold and precious metals prices · asset: commodities · direction: precious metals up · horizon: months · conditions: When uncertainty is high · testable: partly - needs an uncertainty measure · confidence: medium
  ^MT082-C02-2
- **Ola Hansen** Central banks buying gold for three years to diversify away from US dollar assets (plus private investors) is a persistent source of gold demand.  #mech/liquidity_flows _(time-bound view)_
  > Not only central banks who have been buying for the past three years in order to diversify their
  indicator: central bank gold purchases · asset: commodities · direction: gold up · horizon: years · testable: yes - central bank gold purchases are published · confidence: high
  ^MT082-C02-3
- **Ola Hansen** Rising government debt burdens, especially in the US, push investors into precious metals as a fiscal-risk hedge.  #mech/fiscal_debt
  > the fiscal debt worries that uh that that basically comes with the the rising debt burdens we're seeing around the world
  indicator: government debt levels and gold · asset: commodities · direction: gold up · horizon: years · testable: partly - debt vs gold relationship · confidence: medium
  ^MT082-C02-4
- **Ola Hansen** Deglobalisation moves production closer to home, which needs a lot of commodities and could raise some prices.  #mech/structural_shift
  > we're seeing the the deglobalization where production is being moved closer to home.
  asset: commodities · direction: commodities up · horizon: years · testable: no - thematic · confidence: medium
  ^MT082-C02-5
- **Ola Hansen** Rising European defence spending requires steel and rare-earth minerals, supporting commodity demand.  #mech/fiscal_debt
  > We have the increased spending on defense coming through in Europe now in a in a big way.
  indicator: European defence budgets · asset: commodities · direction: steel and rare earths up · horizon: years · testable: partly - spending is public · confidence: medium
  ^MT082-C02-6

### C03
- **Ola Hansen** The energy transition raises power demand (EVs, data centers, cooling), so it supports copper, aluminium, lithium, cobalt, nickel and silver.  #mech/structural_shift
  > the energy transition is also a question of of we're moving towards increased use of power and it's not only towards electrical vehicles it's also towards data centers
  indicator: power demand and electrification metals · asset: commodities · direction: copper, aluminium, lithium, cobalt, nickel, silver up · horizon: years · testable: partly - demand forecasts · confidence: medium
  ^MT082-C03-1
- **Ola Hansen** An ageing population with accumulated savings will spend that money, adding to consumption and commodity demand.  #mech/structural_shift
  > the money that we are saved in over decades that's that will be spent
  asset: commodities · direction: consumption up · horizon: years · testable: no - thematic · confidence: low
  ^MT082-C03-2
- **Ola Hansen** Continuing urbanisation in emerging markets underpins commodity demand.  #mech/structural_shift
  > urbanization undergoing in especially in emerging markets that will also underpin the demand.
  asset: commodities · direction: commodity demand up · horizon: years · testable: no - thematic · confidence: medium
  ^MT082-C03-3
- **Ola Hansen** Mining projects take many years, so miners must guess prices 10 to 12 years ahead, which holds back investment and can cause future metal shortfalls.  #mech/structural_shift
  > mining companies they have to look 10 to 12 years out and try to gauge what the price would be out there.
  indicator: mining capex vs lead times · asset: commodities · direction: metal prices up from shortfall · horizon: years · testable: partly - capex data · confidence: medium
  ^MT082-C03-4
- **Ola Hansen** Softs are produced in small geographic areas, so weather in West Africa (cocoa) and Brazil (coffee) drives large price moves.  #mech/structural_shift _(time-bound view)_
  > making them much more exposed to any weather developments.
  indicator: weather in cocoa and coffee regions · asset: commodities · direction: cocoa and coffee spikes · horizon: months · testable: yes - weather and price data · confidence: high
  ^MT082-C03-5
- **Ola Hansen** Rising US gas exports, domestic demand and European LNG demand underpin a long-term bullish case for natural gas.  #mech/structural_shift _(time-bound view)_
  > US exports of gas is rising. US demand for gas as well is also rising and that will over time underpin prices.
  indicator: US natural gas exports and demand · asset: commodities · direction: natural gas up · horizon: years · testable: partly - fundamental data · confidence: medium
  ^MT082-C03-6
- **Philip Engel Carlson** Calculo's short Henry Hub natural gas trade, held more than two years, was exited by a rally on 20 February 2025 after a cold weather outlook, an example of a trend position ending only when the trend reverses.  #mech/cycle_persistence _(time-bound view)_
  > We got kicked out of a short Henry hop position which we've had on for more than two years.
  indicator: Henry Hub natural gas · asset: commodities · direction: short natural gas · horizon: years · testable: no - single trade · confidence: high
  **Correction (cross-check):** wrong speaker and fund: the two-year short Henry Hub trade belongs to host Moritz Seibert's long-term trend fund, not Calculo (whose holding period is 2 to 5 days) → Moritz Seibert: his trend-following fund's short Henry Hub position, held more than two years, was stopped out by the late-February 2025 rally on a colder weather outlook, an example of a long-held trend ending on reversal.
  ^MT082-C03-7

### C04
- **Ola Hansen** Tariff worries lifted US COMEX futures prices of gold, silver, copper and platinum above London spot prices because imported metal would face tariffs.  #mech/policy_reaction _(time-bound view)_
  > we're seeing right now that futures prices for gold, silver, copper, platinum, they have all been uh been
  indicator: COMEX vs London metal premium · asset: commodities · direction: COMEX premium up · horizon: weeks · conditions: While tariff threat on metals persists · testable: yes - COMEX-LME spreads · confidence: high
  ^MT082-C04-1
- **Ola Hansen** The COMEX-London premium made it profitable to ship physical gold and silver to New York and sell futures against it, drawing in large inventories; the cash and carry basis on gold was about 10% annualised.  #mech/liquidity_flows _(time-bound view)_
  > if you have access to physicals and you can sell the future against it, you are earning a handsome handsome return.
  indicator: COMEX cash-and-carry basis · asset: commodities · direction: metal stocks flow into US · horizon: weeks · conditions: Premium persists · testable: yes - basis and inventory data · confidence: high
  ^MT082-C04-2
- **Ola Hansen** When the premium narrows, physical gold in US vaults with no end user may be sold or hedged, a possible small negative for prices.  #mech/liquidity_flows _(time-bound view)_
  > then there's a lot of physical gold sitting in the US uh with no uh end user.
  indicator: COMEX gold inventories · asset: commodities · direction: gold down · horizon: months · conditions: Spread normalises · testable: partly - needs inventory data · confidence: low
  ^MT082-C04-3
- **Ola Hansen** Chinese copper demand has held up despite the construction downturn, and data centers and power transmission add demand beyond EVs.  #mech/structural_shift _(time-bound view)_
  > the de demand in China has held up phenomenally well even though the construction
  indicator: China copper demand · asset: commodities · direction: copper up · horizon: months · testable: partly - demand data · confidence: medium
  ^MT082-C04-4
- **Ola Hansen** In the gold rush the shovel supplier made the money, so power-grid builders such as Siemens Energy (up 300%) capture the AI and electrification boom, as Nvidia did.  #mech/structural_shift _(time-bound view)_
  > It was the guy who supplied the shovels.
  indicator: power infrastructure stocks · asset: equities · horizon: years · testable: no - analogy · confidence: medium
  ^MT082-C04-5
- **Ola Hansen** Gold shorts can borrow from the Bank of England but silver has no lender of last resort, so silver gets squeezed harder.  #mech/liquidity_flows _(time-bound view)_
  > because if you are if you have a if you're short gold in London market, you can go to the Bank of England and uh and and lease gold from uh from them.
  indicator: silver vs gold lending · asset: commodities · direction: silver squeezes · horizon: weeks · testable: partly - lease rates · confidence: medium
  ^MT082-C04-6
- **Ola Hansen** Copper's early-2025 rally (about 15%) is driven first by China not yet being hit with US tariffs, alongside tariff-driven dislocations in COMEX pricing.  #mech/policy_reaction _(added by opus cross-check, time-bound view)_
  > I think first of foremost the fact that uh that that China hasn't been slapped with terrorists just yet. Uh that's probably one thing
  indicator: US tariff decisions on China; copper price · asset: commodities · direction: copper up while China escapes tariffs · horizon: weeks · conditions: until tariffs on China are imposed · testable: partly - copper moves around China tariff announcements · confidence: medium
  ^MT082-C04-X1

### C05
- **Ola Hansen** Silver carries higher tariff risk than gold because gold is quasi-monetary and much silver comes from Mexico.  #mech/policy_reaction _(time-bound view)_
  > there's probably more higher risk that tariffs would be added to silver than to gold being a a monetary
  indicator: tariff exposure of silver · asset: commodities · direction: silver premium · horizon: weeks · testable: no - speculation · confidence: low
  ^MT082-C05-1
- **Philip Engel Carlson** Calculo holds trades 2 to 5 days: it captures the alpha move and uses AI to choose the exit.  #mech/slow_reaction
  > it's more like 2 to 5 days actually.
  asset: commodities · horizon: days · testable: partly - holding period stated · confidence: high
  ^MT082-C05-2
- **Philip Engel Carlson** Supply constraints from weather or regional events create fear and price moves, which trend following can capture; this works in commodities and not in equities or rates, which explains the commodities-only focus.  #mech/slow_reaction
  > This fear sparks price movements and these movements is actually what we uh want to capture in our trend following model.
  indicator: price breakouts after supply shocks · asset: commodities · direction: long after upward shock, short after downward · horizon: days · conditions: Works where supply and demand are physically constrained · testable: partly - compare trend returns by asset class · confidence: high
  ^MT082-C05-3
- **Philip Engel Carlson** Calculo trades only the most liquid metals, agriculturals, softs and energies, which also lets it scale.  #mech/risk_management
  > we only do trade the liquid stuff.
  indicator: market liquidity · asset: commodities · conditions: Excludes small markets such as orange juice · testable: partly - liquidity filter · confidence: high
  ^MT082-C05-4

### C06
- **Moritz Seibert** Shorter-horizon traders are much more sensitive to market liquidity than slow trend followers, who do not need to trade daily.  #mech/risk_management
  > with your trading frequency you're absolutely much more sensitive to that
  indicator: liquidity · asset: commodities · horizon: days · testable: partly - cost and capacity by horizon · confidence: medium
  ^MT082-C06-1
- **Philip Engel Carlson** Entries are classical CTA breakouts and the advanced part is the post-entry risk management, which aims at low-volatility access to commodities.  #mech/slow_reaction
  > Basically we use only uh price patterns as our entry.
  indicator: price breakouts · asset: commodities · direction: long breakout up, short breakout down · horizon: days · testable: yes - breakout rules are testable · confidence: high
  ^MT082-C06-2
- **Philip Engel Carlson** Machine learning applied to risk management reduces volatility and gives a smoother return profile than plain trend following.  #mech/risk_management
  > commodities can be volatile and and it through the use of AI, we can sort out a lot of the volatility and create a more linary return profile.
  indicator: machine-learning exit signal · asset: commodities · horizon: days · testable: partly - compare with and without ML exit · confidence: medium
  ^MT082-C06-3
- **Philip Engel Carlson** A hurricane threat first adds a risk premium (the price jump), then the market waits on the storm path; the system gets signals from price momentum and candlesticks during this limbo.  #mech/overshoot
  > after this initial risk premium being put into the market, the market will look at the hurricane development
  indicator: price patterns after weather shocks · asset: commodities · horizon: days · testable: partly - event study of weather shocks · confidence: medium
  ^MT082-C06-4
- **Philip Engel Carlson** After a shock move the market often goes sideways, which is enough for the model to take profit and then re-enter the trend if it resumes.  #mech/overshoot
  > So quite often we do participate in these movements where the market uh stabilizes a bit and trades sideways and this is often enough for us to exit the positions capturing the alpha
  indicator: sideways consolidation after a spike · asset: commodities · direction: exit after spike, re-enter on resumption · horizon: days · testable: partly - rule testable · confidence: medium
  ^MT082-C06-5
- **Philip Engel Carlson** The system uses price only, with no weather input and no manual override of signals.  #mech/research_method
  > there's no manual input in regards to selecting signals.
  indicator: price only · asset: commodities · testable: no - process statement · confidence: high
  ^MT082-C06-6

### C07
- **Philip Engel Carlson** The model can be flat, partly long or partly short, with no mandatory allocation to any market or sector.  #mech/risk_management
  > we only want to participate in in real alpha periods
  indicator: position flexibility · asset: commodities · testable: partly - compare to always-invested · confidence: high
  ^MT082-C07-1
- **Philip Engel Carlson** About 75 to 80% of trades are closed by machine learning exits and the rest by classical stops and trailing stops.  #mech/risk_management
  > 75 80% of our trades is handled via the machine learning exits.
  indicator: stops vs ML exits · asset: commodities · horizon: days · testable: partly - exit mix reportable · confidence: high
  ^MT082-C07-2
- **Philip Engel Carlson** Each day the open trade's candlestick and momentum features are matched to a database of historical trades with known T+1 and T+2 outcomes, then classified as keep or eliminate.  #mech/research_method
  > when we take this new data put into our database, it finds a match that is as close to something it has seen before.
  indicator: nearest-neighbour matching on candlestick and momentum features · asset: commodities · direction: exit when matched history shows adverse outcome · horizon: days · conditions: Needs a large trade history · testable: yes - algorithm described · confidence: high
  ^MT082-C07-3
- **Philip Engel Carlson** Capturing parts of trends and avoiding counter-moves gives a smoother ride but not the whole trend, as classical longer-term CTAs do; ML uses daily bars.  #mech/risk_management
  > we try to capture bits and pieces of these existing trends and trying to vet out any counter moves along the way.
  indicator: daily bars · asset: commodities · horizon: days · conditions: Trade-off: smoother returns but misses the tail of trends · testable: partly - compare to long-horizon trend · confidence: high
  ^MT082-C07-4

### C08
- **Philip Engel Carlson** Entries are trend only with no mean reversion.  #mech/slow_reaction
  > We use trend following strategies to enter the markets. Trend only.
  asset: commodities · horizon: days · testable: yes · confidence: high
  ^MT082-C08-1
- **Philip Engel Carlson** Machine learning is not used for entry because predicting where the market moves is a guess; it is used only for exits, where it avoids learning noise about direction.  #mech/research_method
  > I do believe that trends have strength.
  asset: commodities · horizon: days · testable: partly - compare ML-entry vs ML-exit · confidence: high
  ^MT082-C08-2
- **Philip Engel Carlson** Using ML only as a risk-off element avoids the overfitting problem of price prediction models.  #mech/research_method
  > we actually only use it as a riskoff element which changes the picture quite a bit compared to trying to build a fully AI model that tries to predict the price targets.
  asset: commodities · horizon: days · testable: partly · confidence: high
  ^MT082-C08-3
- **Moritz Seibert** Machine learning applied to market prediction risks fitting noise, and Seibert jokes that a clever machine would probably just rediscover buying breakouts, i.e. become a trend follower.  #mech/research_method _(added by opus cross-check)_
  > how do you prevent the machine to learn from the noise which is you know a prevalent factor in the markets.
  indicator: ML model trained on price data · asset: multi · conditions: noisy market data; ML used for direction prediction · testable: partly - compare ML entry rules with plain breakout rules out of sample · confidence: low
  ^MT082-C08-X1

### C09
- **Philip Engel Carlson** Machine learning exits are timed at the most liquid hours and are flags of possible correction, not firm predictions, so execution is done in liquid periods.  #mech/risk_management
  > timed towards the most liquid time in the US.
  indicator: time-of-day liquidity · asset: commodities · horizon: days · testable: partly - execution cost study · confidence: medium
  ^MT082-C09-1
- **Ola Hansen** The long-only Bloomberg Commodity Index had a 77-month, 38% drawdown from 2015 to 2020 and a further 22% drop after 2022, so a long/short strategy with similar returns and lower volatility is preferable.  #mech/risk_management
  > We had the two biggest one was a 77 months draw down between 15 and 20 where it fell 38%.
  indicator: Bloomberg Commodity Index drawdowns · asset: commodities · horizon: years · testable: yes - index history · confidence: high
  ^MT082-C09-2
- **Ola Hansen** Commodity strategy returns tend to be positive in bad equity months, lowering portfolio volatility.  #mech/risk_management
  > we had to have bad months for equities we quite often find that uh that there's actually some uh positive months coming in through the commodities.
  indicator: commodity strategy vs equity monthly returns · asset: multi · horizon: months · testable: yes - correlation in down months · confidence: low
  ^MT082-C09-3
- **Philip Engel Carlson** Calculo does not use forward-curve information (contango, backwardation, seasonality) as a signal and does not trade calendar spreads; only outright futures on price patterns.  #mech/research_method _(added by opus cross-check)_
  > Does this information trigger anything at Calculu or are you maybe even trading spreads uh which you know you can do in the commodity markets? is when we're not trading spreads as no.
  indicator: forward curve shape (not used) · asset: commodities · horizon: days · testable: no - design description · confidence: high
  ^MT082-C09-X1

### C10
- **Moritz Seibert** Commodities have no equity-like positive drift, so they should be traded both long and short.  #mech/risk_premium
  > commodities don't have the equity drift or anything like that.
  asset: commodities · direction: long and short · testable: partly - commodity risk premium debate · confidence: medium
  ^MT082-C10-1
- **Ola Hansen** Cocoa was not in the Bloomberg Commodity Index because of its size, so the index missed the cocoa rally, while natural gas, a member, dragged it down.  #mech/structural_shift _(time-bound view)_
  > because it's a relatively small market, is not a BCOM member.
  indicator: BCOM composition · asset: commodities · horizon: years · testable: yes - index membership · confidence: high
  ^MT082-C10-2
- **Ola Hansen** Index rebalancing in January forced sales of a winner whose weight had grown extreme (cocoa).  #mech/liquidity_flows _(time-bound view)_
  > there was a massive re rebalancing in in the when January came because the the percentage share of expos exposure to coco out of the total was uh had gone quite extreme
  indicator: index rebalancing · asset: commodities · horizon: weeks · testable: yes - rebalance data · confidence: medium
  ^MT082-C10-3
- **Ola Hansen** Smart-roll commodity ETFs have not outperformed the main total return indices.  #mech/research_method
  > I don't find them having been particularly successful uh they haven't really outperformed uh the uh the main uh total return in in the indices.
  indicator: smart-roll commodity ETFs · asset: commodities · horizon: years · testable: yes - ETF vs index returns · confidence: medium
  ^MT082-C10-4
- **Moritz Seibert** In contango, a short position earns roll yield (natural gas); Calculo benefited from the upward-sloping curve but does not roll monthly and is aware of seasonality.  #mech/risk_premium
  > you have been making money being short simply on the the role of the uh the role from a from a from a low to a high contract.
  indicator: commodity futures curve slope (contango) · asset: commodities · direction: short in contango · horizon: months · conditions: Applies in contango markets · testable: yes - roll yield is measurable · confidence: medium
  **Correction (cross-check):** wrong attribution: the natural gas short that earned contango roll yield is Seibert's fund, not Calculo; Ola raised the roll point and Seibert replied → Ola Hansen / Moritz Seibert: in contango a short natural gas position earned roll yield even through big rallies; Seibert's fund benefited from the upward-sloping curve, though it does not roll every month and watches seasonality.
  ^MT082-C10-5
- **Philip Engel Carlson** Calculo reports equity-like returns at two-thirds of stock index volatility since 2018, non-correlated and non-cyclical.  #mech/risk_management _(time-bound view)_
  > that we over the past seven years almost since inception has actually delivered equity-like returns at 2/3 of the volatility of uh the broad stock indices.
  indicator: fund track record · asset: commodities · horizon: years · conditions: Self-reported · testable: partly - track record claim, not verified · confidence: medium
  ^MT082-C10-6
- **Moritz Seibert** First-generation long-only commodity indices (e.g. BCOM) are concentrated (caption says equity; likely energy) and metals heavy and exclude small markets, while newer variants diversify more and spread exposure along the curve, so index choice drives commodity beta returns.  #mech/structural_shift _(added by opus cross-check)_
  > the first [L380] generation of these indices, they're equity and metals heavy. And then there's all the, you know, smart variations that um are more diversified and they distribute liquidity across the curve more.
  indicator: commodity index composition and curve placement · asset: commodities · horizon: years · testable: yes - compare first-generation vs diversified/curve-spread indices · confidence: medium
  ^MT082-C10-X1
- **Ola Hansen** Roll yield has turned positive (backwardation) across most commodity markets, with US natural gas the big exception where contango kept rewarding shorts even through price spikes.  #mech/risk_premium _(added by opus cross-check, time-bound view)_
  > we generally are starting to see a a positive royal coming into the markets except uh and the big exception is is obviously where you just have had your profitable short in natural gas
  indicator: futures curve slope / roll yield by commodity · asset: commodities · direction: long backwardated markets earn roll; short contango natural gas earns roll · horizon: months · conditions: backwardated curves (most markets) vs contango (natural gas) · testable: yes - curve slope and roll returns by market · confidence: medium
  ^MT082-C10-X2

