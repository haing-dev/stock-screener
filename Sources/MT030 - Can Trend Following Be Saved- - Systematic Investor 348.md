---
source_id: MT030
title: "Can Trend Following Be Saved- - Systematic Investor 348"
date: 2025-05-22
channel: "Top Traders Unplugged"
url: 
words: 14224
claims: 61
added_by_crosscheck: 7
corrections: 1
crosscheck: "opus cross-check"
speakers: ["Andrew Beer (DBi, replication ETF manager)", "Niels Kaastrup-Larsen (host, hedge fund manager)"]
tags: [source, layer0]
---
# Can Trend Following Be Saved- - Systematic Investor 348

**Speakers:** Andrew Beer (DBi, replication ETF manager); Niels Kaastrup-Larsen (host, hedge fund manager)

**Summary:** Top Traders Unplugged Systematic Investor 348 (May 2025): Andrew Beer and Niels on why trend following suffered its worst period in years, policy-driven whipsaws and short-term models, and how allocators should judge managers and fees. Conclusions: sentiment head fakes hurt short-term and innovation-heavy managers; medium-long trend has worked for 50 years; expect a 3% allocation and rebound after drawdowns.

**Approach:** trend following, CTA drawdowns, replication, allocator behaviour

**Cross-check completeness estimate of first read:** 0.89 - first reader captured nearly all arguments and numbers with correct speakers; missed some reasoning steps (price-as-information logic, timing luck), fee history and internalisation incentives.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | nothing actionable: intro and personal anecdote about a dog |
| C02 | 0 | nothing actionable: discussion of a book on Apple and China, background on China (no method content) |
| C03 | 2 | Apple reshoring and tariffs; sovereign wealth fund internalizing trend following |
| C04 | 0 | insourcing motivations; tangents (Trump comments, AI airline punctuality); no method claims |
| C05 | 4 | trend barometer and May 2025 performance; policy noise |
| C06 | 1 | Trump negotiation style story |
| C07 | 4 | short-term models gullible; five reversals since 2022; medium to long-term models |
| C08 | 5 | lookback test; managers' innovation drawdowns; index drawdown |
| C09 | 3 | central bank vs politician cycle; worst drawdowns; certainty of recovery |
| C10 | 3 | investor reaction, Buffett contrast, information vs sentiment |
| C11 | 4 | 2024 early success, Treasuries 2020, sentiment head fakes |
| C12 | 4 | market reversals, drawdown to volatility ratio, narratives |
| C13 | 1 | core beta commoditisation |
| C14 | 4 | flow-chasing, alternative markets evidence, ablation test, AQR |
| C15 | 3 | how to judge manager changes; fees vs replication |
| C16 | 3 | replicator track record and lag; fee-to-alpha rule; trading costs |
| C17 | 2 | past drawdowns then strong years; yields at 4.5% |
| C18 | 3 | alpha against slow investors; replication; static sizing |
| C19 | 4 | stacked products lag; buy in drawdowns; bonds failed; musical chairs |
| C20 | 4 | winners differ; stacked product demand; 3% allocation; narrative |
| C21 | 0 | nothing actionable: outro |

## Claims

### C03
- **Niels Kaastrup-Larsen** Apple built its supply chain in China (about $275bn pledged 2016-2021, engineers trained locally), so tariff-driven reshoring of production is unrealistic over the near term, which makes trade-war policy hard to trade on fundamentals.  #mech/structural_shift _(time-bound view)_
  > completely unrealistic that you can move pretty much any of the Apple production back to the US or any other country for that matter
  asset: multi · horizon: years · testable: no - industry anecdote from a book · confidence: medium
  ^MT030-C03-1
- **Niels Kaastrup-Larsen** A large sovereign wealth fund that hosted staff at trend followers redeemed from them around 2007 and built the capacity internally, an example of institutions internalizing trend following (also via QIS swaps).  #mech/liquidity_flows
  > around 20 2007 they simply started to uh redeem from all these external trend followers and built the whole capacity internally
  asset: multi · horizon: years · testable: no - anecdote · confidence: medium
  ^MT030-C03-2

### C04
- **Andrew Beer** Institutions bring trend following in-house (own teams or QIS swaps) not only for cost but because staff gain status by moving from allocating to external managers to running money themselves.  #mech/structural_shift _(added by opus cross-check)_
  > They they want to move from being somebody who just you know mails money to somebody else to having responsibility for it to moving from an analyst to a PM role.
  asset: multi · direction: flows away from external CTAs toward in-house and QIS · horizon: years · conditions: large institutions · testable: no - organisational incentive · confidence: medium
  ^MT030-C04-X1
- **Andrew Beer** Large seed investors historically demanded position transparency so they could copy and scale a manager's trades without paying fees on the copied capital, an early form of position-level replication.  #mech/new _(added by opus cross-check)_
  > you would have people who would give money to an equity long short manager with the expectation that they could see their positions and therefore double up or triple up on trade.
  asset: equities · horizon: years · testable: no - historical anecdote · confidence: medium
  ^MT030-C04-X2

### C05
- **Niels Kaastrup-Larsen** Niels's Trend Barometer at 25 in May 2025 is exceptionally weak, signalling a hostile environment for trend following.  #mech/cycle_persistence _(time-bound view)_
  > my own trend barometer finished yesterday at 25. That's exceptionally weak.
  indicator: Trend Barometer = 25 · asset: multi · direction: trend followers losing · horizon: weeks · testable: yes - barometer vs CTA returns · confidence: medium
  ^MT030-C05-1
- **Niels Kaastrup-Larsen** In May 2025 SG Trend was down about 3% (down 12% YTD), SG CTA down 8.69% YTD and BTOP50 down 5.25%, while short-term traders were roughly flat and equities were up 3-6% in May.  #mech/cycle_persistence _(time-bound view)_
  > Stocken trend down about uh 3% down 12% for the year
  indicator: SG Trend, SG CTA, BTOP50, SG Short-Term index, MSCI World, S&P 500 · asset: multi · horizon: months · testable: yes - public index data · confidence: high
  ^MT030-C05-2
- **Niels Kaastrup-Larsen** In 2025 up to May very few markets gave tradable trends; many reversed once or twice, and losses came mainly from fixed income and precious metals giving back gains.  #mech/cycle_persistence _(time-bound view)_
  > very very few markets that have given any kind of trends that can be traded
  indicator: number of trending markets, fixed income and precious metals P&L · asset: multi · horizon: months · conditions: repeated reversals · testable: yes - trend-breadth measure · confidence: medium
  ^MT030-C05-3
- **Andrew Beer** Policy announcements such as Liberation Day tariffs were chosen without analysis, so policy signals are noisy and macro views built on them are hard to trade.  #mech/policy_reaction _(time-bound view)_
  > one of the problems for allocators right now is it's very hard to distinguish the signal when sometimes the policy is about noise
  indicator: tariff policy announcements · asset: multi · horizon: weeks · testable: no - qualitative · confidence: medium
  ^MT030-C05-4

### C06
- **Andrew Beer** Trump's policy style treats negotiation as the goal with no need for consistency or do-no-harm, so announcements reverse and create whipsaws in markets.  #mech/policy_reaction _(time-bound view)_
  > unlike other areas of the business world that we're used to, the negotiation is often the point
  indicator: policy reversals · asset: multi · horizon: weeks · conditions: current US administration · testable: no - political characterization · confidence: medium
  ^MT030-C06-1

### C07
- **Andrew Beer** Short-term trend models take news-driven moves (e.g. a tweet) at face value, so they get whipsawed in headline-driven markets, whereas long-term models wait for confirmation.  #mech/cycle_persistence _(time-bound view)_
  > And the problem with short-term models is they're really gullible, right?
  indicator: short-term trend models · asset: multi · horizon: weeks · conditions: policy-news driven reversal environment · testable: yes - compare lookbacks in reversal regimes · confidence: medium
  ^MT030-C07-1
- **Andrew Beer** Since the 2022 peak there were five vicious reversals (inflation not falling, SVB, Powell pivot, growth fear plus yen carry unwind, Liberation Day), which created repeated drawdowns for trend followers.  #mech/cycle_persistence _(time-bound view)_
  > since the peak in 2022, we've had five vicious reversals, right?
  indicator: market reversals 2022-2025 · asset: multi · horizon: years · testable: yes - reversal counts and CTA drawdowns · confidence: medium
  ^MT030-C07-2
- **Andrew Beer** Short-term models enter trends early but get head-faked two or three times on the way, giving roughly zero Sharpe over time; they may hurt in policy-noise regimes like the 2016-2020 Long Winter.  #mech/cycle_persistence
  > you get head faked out two or three times on on on the way. So it's kind of a zero sharp ratio strategy over time
  indicator: short-term trend model Sharpe · asset: multi · direction: prefer medium/long-term models · horizon: years · conditions: regimes with repeated head fakes · testable: yes - Sharpe by lookback · confidence: medium
  ^MT030-C07-3
- **Andrew Beer** Medium to long-term trend models are the core that has worked for 50 years and may outperform the innovations (short-term models, vol controls, alt markets) added to protect against whipsaws.  #mech/cycle_persistence _(time-bound view)_
  > going back to what's really worked for 50 years which is is is is the medium to long-term trend models
  indicator: medium to long-term trend models · asset: multi · horizon: years · testable: yes - compare variants · confidence: medium
  ^MT030-C07-4

### C08
- **Niels Kaastrup-Larsen** In Niels's YTD 2025 test varying only lookback, the 20-day outperformed 60-day, which outperformed 260-day, and the 130-day was worst, so medium-term was not the safe haven.  #mech/cycle_persistence _(time-bound view)_
  > the worst time frame is actually the 130 days
  indicator: trend lookback test 20/60/130/260 days YTD 2025 · asset: multi · horizon: months · testable: yes - lookback comparison · confidence: medium
  ^MT030-C08-1
- **Niels Kaastrup-Larsen** Many CTAs favour medium-term models because of capacity, and some managers believe medium term is uniquely best.  #mech/crowding_positioning
  > a lot of people gravitated towards the medium-term because of size, right?
  indicator: medium-term trend capacity · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT030-C08-2
- **Niels Kaastrup-Larsen** Rather than speeding up models, whipsaw protection may come from improved risk management.  #mech/risk_management
  > not actually through speed of models but it could be through different ways of looking at risk management for example
  indicator: risk management vs model speed · asset: multi · testable: partly · confidence: low
  ^MT030-C08-3
- **Andrew Beer** The SG trend/CTA index was down 15% year over year to April 2025, matching its worst drawdown since 2000, and managers built on shorter models, vol controls, active position management and alternative markets had drawdowns worse than the space.  #mech/cycle_persistence _(time-bound view)_
  > the asen index is down 15% year-over-year um through the end of April that matches or slightly exceeds its largest historical draw down going back to 2000
  indicator: SG CTA/Trend index 12-month return · asset: multi · horizon: years · testable: yes - index data · confidence: high
  ^MT030-C08-4
- **Andrew Beer** Managers whose pitch was better risk controls and innovation (short models, vol controls, position management, alternative markets) suffered worse drawdowns than plain trend, suggesting those features failed in this environment.  #mech/cycle_persistence _(time-bound view)_
  > individual managers who um uh you know who had basically built their thesis around better risk management and risk controls
  indicator: innovation features vs drawdown · asset: multi · horizon: months · testable: yes - manager-level comparison · confidence: low
  ^MT030-C08-5
- **Andrew Beer** In the April 2025 reversals, results depended heavily on luck in rebalance timing and positioning just before policy headlines, so dispersion between managers in such periods says little about skill.  #mech/research_method _(added by opus cross-check, time-bound view)_
  > we rebalance on Mondays and a few there were a few times we're like oh thank god we rebalance on Monday
  indicator: rebalance-day sensitivity of returns · asset: multi · horizon: weeks · conditions: headline-driven reversal markets · testable: yes - simulate the same strategy with different rebalance weekdays · confidence: medium
  ^MT030-C08-X1

### C09
- **Niels Kaastrup-Larsen** A cycle exists between strong central banks with weak politicians and the reverse; after a period of Fed control, 2025 resembles strong politicians and weak central banks, where Trump rather than Powell moves markets.  #mech/policy_reaction _(time-bound view)_
  > at some point you have strong central banks and weak politicians and then at some point you have strong politicians and weak central banks
  indicator: central bank vs political dominance regime · asset: multi · horizon: years · testable: partly - regime classification needed · confidence: low
  ^MT030-C09-1
- **Niels Kaastrup-Larsen** Even managers with 20-40 year histories were hitting their worst drawdowns in 2025, consistent with longevity eventually producing a worst period.  #mech/cycle_persistence _(time-bound view)_
  > I have also observed that even managers who've been around for a long time, two, three, four decades, some of them are hitting their worst draw downs uh ever right now
  indicator: manager max drawdown · asset: multi · horizon: years · testable: yes - drawdown records · confidence: medium
  ^MT030-C09-2
- **Niels Kaastrup-Larsen** Niels expects trend following to make new highs again as models adjust and markets begin trending, with investor emotional reactions the main concern.  #mech/cycle_persistence _(time-bound view)_
  > I feel absolutely certain that we're going to go back and we're going to make new highs
  indicator: CTA index highs · asset: multi · horizon: years · testable: no - forecast · confidence: high
  ^MT030-C09-3

### C10
- **Niels Kaastrup-Larsen** Trend following is declared dead after drawdowns, and that is usually the best time to buy or add.  #mech/behavioral
  > people will at some point probably soon declare trend following dead once again and it's usually the best time to to buy or add uh to it
  indicator: CTA drawdown and subsequent returns · asset: multi · direction: add after deep drawdown · horizon: years · testable: yes - returns after drawdowns · confidence: medium
  ^MT030-C10-1
- **Andrew Beer** Unlike value investing (Buffett holding through 50% drawdowns), managed futures has no intrinsic-value anchor and cuts losers, so one cannot argue that cheaper means rebound; communication must rely on the information story.  #mech/behavioral
  > the whole point of managed futures is you sell your losers right you don't hold on to them you don't double down
  indicator: drawdown behaviour · asset: multi · testable: no - conceptual · confidence: medium
  ^MT030-C10-2
- **Andrew Beer** Price moves have two components, changing information and changing sentiment, which compete; managed futures profit when they detect true changes in information.  #mech/behavioral
  > The information is going to change between now and when you next measure it and the sentiment about that information is going to change as well.
  indicator: information versus sentiment · asset: multi · horizon: months · testable: partly - decomposition difficult · confidence: medium
  ^MT030-C10-3

### C11
- **Andrew Beer** In early 2024 CTAs picked up the post-election information shift early (long equities, dollar, gold, rate cuts priced out) before sentiment whipsaws began after April.  #mech/cycle_persistence _(time-bound view)_
  > the space was on fire in the beginning of 2024. Why? Because it picked up on the Trump trade early
  indicator: trend positioning early 2024 · asset: multi · direction: long equities, USD, gold · horizon: months · testable: partly · confidence: medium
  **Correction (cross-check):** Timing wrong: Andrew says CTAs picked up the Trump trade early in 2024, i.e. before the November election, not a post-election shift. → In early 2024 CTAs picked up the 'Trump trade' early, before the election (long equities, dollar, gold, fewer rate cuts priced), before sentiment whipsaws began after April 2024.
  ^MT030-C11-1
- **Andrew Beer** Trend picks up changes in information early: short Treasuries in September 2020 when yields rose from 0.50% to 0.70%, a contrarian move signalling inflation before consensus.  #mech/slow_reaction
  > we went short treasuries in September of 2020. Think about how early that was
  indicator: 10y Treasury yield move 0.50% to 0.70% · asset: rates · direction: short Treasuries · horizon: months · testable: yes - trend signal history in 2020 · confidence: medium
  ^MT030-C11-2
- **Andrew Beer** Since April 2024 information changed little but sentiment head fakes caused a 15% SG CTA drawdown in a series of 2-5% drops without time to recover, like the 2022-2023 drawdown.  #mech/cycle_persistence _(time-bound view)_
  > there are all these kind of sentiment head fakes
  indicator: sentiment head fakes, drawdown sequence · asset: multi · horizon: months · conditions: sentiment flips without lasting information change · testable: yes - drawdown decomposition · confidence: medium
  ^MT030-C11-3
- **Andrew Beer** Trend following works if real information changes eventually outweigh sentiment noise.  #mech/cycle_persistence
  > the bet that you have to make on the space is that the world is actually going to change and the change in information is going to drown out the change in in in sentiment
  asset: multi · horizon: years · testable: no - premise · confidence: medium
  ^MT030-C11-4
- **Andrew Beer** A sustained price move signals that informed participants know something, so trend following works by extracting early evidence of changing fundamentals from prices across many markets, and its alpha is contrarian, not late.  #mech/slow_reaction _(added by opus cross-check)_
  > what's the first question you ask who knows something what do they know that I don't know
  indicator: price momentum across markets · asset: multi · direction: follow the price move before consensus · horizon: months · conditions: works when information changes; fails when moves are sentiment noise · testable: partly - test whether trend signals lead fundamental revisions · confidence: medium
  ^MT030-C11-X1

### C12
- **Andrew Beer** Andrew expects big things to break (inflation up, confidence in the dollar lost) as policy risk-taking spirals, creating the money-making opportunity for managed futures.  #mech/fiscal_debt _(time-bound view)_
  > inflation's going to go the dollar is going to people are going to lose confidence in the dollar
  indicator: US dollar, inflation · asset: fx · direction: dollar weaker, inflation higher · horizon: years · testable: no - forecast · confidence: low
  ^MT030-C12-1
- **Niels Kaastrup-Larsen** Bonds had about five reversals in 12 months, equities a couple, and dollar and energies also reversed, tricking managers into flipping exposure (a perfect storm).  #mech/cycle_persistence _(time-bound view)_
  > bonds have essentially had something like five reversals in the last 12 months or so, which is a lot
  indicator: number of trend reversals by asset · asset: multi · horizon: months · testable: yes - count reversals · confidence: medium
  ^MT030-C12-2
- **Niels Kaastrup-Larsen** Measured as max drawdown relative to annualised volatility over 12 years, bonds have by far the worst ratio and equities are not better than many CTA managers, so current CTA drawdowns are not extreme in relative terms.  #mech/risk_management
  > what is the max draw down in relation to its annualized volatility and people will be surprised I think that
  indicator: max drawdown / annualised volatility · asset: multi · horizon: years · testable: yes - compute ratio · confidence: medium
  ^MT030-C12-3
- **Niels Kaastrup-Larsen** The alternative-markets-trend-better narrative worked for a couple of years then failed for three to four years, partly because momentum disappeared as people crowded into them.  #mech/crowding_positioning
  > oh these alternative markets they trend better
  indicator: alternative markets trend returns · asset: multi · horizon: years · testable: yes - alt vs core markets trend Sharpe over time · confidence: medium
  ^MT030-C12-4

### C13
- **Andrew Beer** The core trend beta was discovered decades ago; when banks offered QIS products and GSA a 50bp product in the early 2010s it was commoditised, pushing managers to differentiate through added features.  #mech/structural_shift
  > I think the core driver the core beta of managed futures was discovered 50 years ago.
  indicator: commoditized trend beta, QIS · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT030-C13-1
- **Andrew Beer** In the 1990s, retail managed-futures products (e.g. guaranteed notes) carried about 10 points of annual fees, including about 600 bp of contractual trading commissions; Niels notes the middlemen's packaging added this cost, not the managers.  #mech/new _(added by opus cross-check)_
  > they highlighted funds that had 10 points in them including 600 basis points of uh of contractual trading commissions
  asset: multi · horizon: years · testable: partly - historical fund documents · confidence: medium
  ^MT030-C13-X1

### C14
- **Andrew Beer** A trend fund with luckily positioned March 2020 and strong 2020-2021 grew to $5bn; narrative reinforced skill, assets flowed in, then it lagged, a recurring flow-chasing pattern.  #mech/behavioral
  > the narrative followed positioning luck because then after the money comes in, they have not
  indicator: fund flows after short-term outperformance · asset: multi · horizon: years · testable: yes - flows vs subsequent returns · confidence: medium
  ^MT030-C14-1
- **Andrew Beer** Smart researchers found no evidence that alternative markets trend more; they mainly provide diversification.  #mech/research_method
  > people that I think are very very smart and and respect have looked at that issue and have not found evidence of it
  indicator: alternative markets trend strength · asset: multi · horizon: years · testable: yes - statistical test · confidence: medium
  ^MT030-C14-2
- **Andrew Beer** Allocators should ask managers to backtest their announced enhancements (more markets, vol controls, short-term models) against the model of 3 and 6 years ago to see if complexity adds value.  #mech/research_method
  > Go back 3 years ago. Show me the model you had then and how it would have done and and have these things that you've done.
  indicator: ablation of model enhancements · asset: multi · horizon: years · testable: yes - ablation backtest · confidence: medium
  ^MT030-C14-3
- **Andrew Beer** Model overhauls can go either way: AQR rebuilt its models and is doing very well but from 2014 to 2020 underperformed the other 19 SG CTA constituents by 20%.  #mech/research_method
  > underperformed the other 19 guys in the stock CTA index by by by by 20%
  indicator: AQR relative performance to SG CTA constituents · asset: multi · horizon: years · testable: yes - relative performance · confidence: medium
  ^MT030-C14-4

### C15
- **Niels Kaastrup-Larsen** Managers should be judged on relative performance rather than asked to justify individual model changes, since changes are made believing they are better and hypothetical comparisons are impractical.  #mech/research_method
  > I think it's fair to judge pe judge firms which which we all get judged from from the performance from the relative performance
  asset: multi · testable: no - evaluation philosophy · confidence: medium
  ^MT030-C15-1
- **Andrew Beer** With cheap replication and bank trend products available as benchmarks, managers must justify higher fees relative to such alternatives.  #mech/risk_premium
  > the bonus is on the manager to to to explain why they why somebody should be be paying 170 basis points, not 85 basis points
  indicator: fees 170bp vs 85bp · asset: multi · testable: no - allocation standard · confidence: medium
  ^MT030-C15-2
- **Niels Kaastrup-Larsen** Replicators also over-promise: a 300-400bp outperformance claim ended as about 50bp after five years.  #mech/research_method
  > we can outperform three to 400 basis points to the index and then 5 years later you look at the numbers and they outperformed by 50 basis points
  indicator: replicator outperformance vs promise · asset: multi · horizon: years · testable: yes - realized vs promised · confidence: medium
  ^MT030-C15-3

### C16
- **Andrew Beer** The weekly replicator underperformed in 2023 because it was slow at SVB and the second Powell pivot; its track record still met promised numbers since 2016, and outcomes depend on the window used.  #mech/cycle_persistence
  > we were slow with SVB. We were slow with the second Powell pivot
  indicator: replicator lag at inflections · asset: multi · horizon: months · testable: yes - episode analysis · confidence: medium
  ^MT030-C16-1
- **Andrew Beer** Each additional 100bp of fees should require 300-400bp of added value because added complexity also raises trading costs.  #mech/risk_premium
  > what should be your expectation of to how much value they would add to warrant an additional 100 basis points? To me, it's three or 400 basis points
  indicator: fee premium vs required alpha · asset: multi · horizon: years · testable: yes - compare · confidence: medium
  ^MT030-C16-2
- **Andrew Beer** Trading only 10 super-liquid contracts gives about 8bp of trading costs, whereas a competitor trading many more markets shows about 200bp, so complex programs must beat cheap ones by a wide margin.  #mech/risk_management
  > our trading costs on in in in US land are eight basis points or something like that because we're just trading these 10 super liquid contracts
  indicator: trading cost 8bp vs 200bp · asset: multi · horizon: years · testable: yes - cost comparison · confidence: medium
  ^MT030-C16-3

### C17
- **Niels Kaastrup-Larsen** Long-established managers had their worst drawdowns in 2012-2013 in an under-the-radar period, followed by about five flat years and then among the best-ever years, suggesting drawdowns precede strong periods.  #mech/cycle_persistence
  > suddenly they had their worst draw down by some margin was actually 2012 12 or 2013
  indicator: manager drawdowns 2012-2013 then 2014 · asset: multi · horizon: years · testable: yes - drawdown then forward returns · confidence: medium
  ^MT030-C17-1
- **Niels Kaastrup-Larsen** The 10-year yield keeps returning to about 4.5% despite attempts to push it lower, and Niels suspects interest rates could be where markets break.  #mech/fiscal_debt _(time-bound view)_
  > it just keeps coming back to this 4 and a half% and we're a little bit above that
  indicator: 10-year Treasury yield about 4.5% · asset: rates · direction: yields stay high · horizon: months · testable: no - view · confidence: low
  ^MT030-C17-2
- **Andrew Beer** Many allocators choose trend managers on brand and legacy rather than testing whether complexity and higher fees add value over a cheap beta alternative.  #mech/behavioral _(added by opus cross-check)_
  > A lot of people are interested in, you know, my god, you know, they're they're they're legends
  asset: multi · horizon: years · testable: partly - flows vs brand age vs risk-adjusted returns · confidence: medium
  ^MT030-C17-X1
- **Andrew Beer (probable)** A US president with a personal economic interest in a dollar alternative (crypto) adds to the risk of lost confidence in the dollar, one of the 'things breaking' that could produce large trends.  #mech/policy_reaction _(added by opus cross-check, time-bound view)_
  > president of the United States who for the first time in history has an economic interest in an alternative to the dollar.
  asset: fx · direction: dollar down risk · horizon: years · testable: no - qualitative risk · confidence: low
  ^MT030-C17-X2

### C18
- **Andrew Beer** Managed futures alpha is not zero-sum between managers but earned against slow-moving 60/40 investors who are slow by design and constrained by their justification (e.g. inflation never returning), so even convinced allocators cannot change quickly.  #mech/slow_reaction
  > they are slow on purpose and and they have told they have told their end investors that you should not panic and you should not move fast
  indicator: allocator inertia · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT030-C18-1
- **Andrew Beer** Replication works because it captures managed futures trading against slow investors using a few instruments such as the 10-year Treasury; niche markets like palm oil add little for that edge.  #mech/structural_shift
  > you can get that in the 10-year Treasury you don't need that in 32 different different um uh instruments
  indicator: 10-year Treasury exposure of replicator · asset: multi · testable: yes - replicator vs index · confidence: medium
  ^MT030-C18-2
- **Niels Kaastrup-Larsen** Managers with few markets, bigger risk in smaller markets and static position sizing had top returns over five years but outsized losses now.  #mech/risk_management _(time-bound view)_
  > you can great outsized gains by having static position size, but you can have great outsized losses by having static position size as we're seeing now
  indicator: static vs dynamic position sizing, concentration · asset: multi · horizon: years · testable: yes - compare sizing approaches · confidence: medium
  ^MT030-C18-3

### C19
- **Niels Kaastrup-Larsen** Return-stacked managed futures plus equity products lag now that CTA alpha is negative and equity beta has recovered, behaving exactly as designed.  #mech/risk_management _(time-bound view)_
  > they're now obviously not able to keep up because the alpha is hurting, but the beta is back to where it was
  indicator: return-stacked product performance · asset: multi · horizon: months · testable: yes - decomposition · confidence: high
  ^MT030-C19-1
- **Niels Kaastrup-Larsen** Historically the best time to buy trend following has been in drawdowns because strategies subsequently made new highs.  #mech/cycle_persistence
  > if history is anything to go by the best time to buy this strategy is in the draw down
  indicator: CTA drawdown depth then forward return · asset: multi · direction: buy after drawdowns · horizon: years · testable: yes - conditional returns · confidence: medium
  ^MT030-C19-2
- **Andrew Beer** Bonds have failed since 2020 (inflation not transitory, high stock-bond correlation), which will drive trend into wealth-management portfolios; allocators avoid admitting the mistake of holding 40% in bonds.  #mech/structural_shift _(time-bound view)_
  > bonds have failed miserably right since since the end of 2000 I mean including this year by the way
  indicator: bond returns since 2020, stock-bond correlation · asset: rates · horizon: years · conditions: high stock-bond correlation · testable: yes - bond returns and correlation · confidence: high
  ^MT030-C19-3
- **Andrew Beer** After underperformance expect musical chairs: managers fired, some investors leave the space, and money flows to recent winners (AQR, Campbell, a CTA ETF), as in the late 2010s.  #mech/liquidity_flows _(time-bound view)_
  > people will fire managers who have done who have underperformed their expectations
  indicator: manager flows after drawdown · asset: multi · horizon: years · testable: yes - flows vs prior returns · confidence: medium
  ^MT030-C19-4

### C20
- **Andrew Beer** Recent winners are not highly correlated to the CTA index (not 90%) and differ materially, while others will seek cheaper beta-like exposure that suits replication.  #mech/structural_shift _(time-bound view)_
  > they're not 90% correlated to the CTA index, 80% correlated with with like a little bit of enhancements here or there
  indicator: correlation to SG CTA Index · asset: multi · horizon: years · testable: yes - correlation data · confidence: medium
  ^MT030-C20-1
- **Andrew Beer** April 2025's performance weakened demand for stacked managed futures plus equity products (e.g. a UCITS fund with a $200m weekly outflow), delaying adoption.  #mech/liquidity_flows _(time-bound view)_
  > April called into question whether you could rely on manage futures in a sharp inflection point
  indicator: flows into stacked products · asset: multi · horizon: months · testable: partly - flow data · confidence: medium
  ^MT030-C20-2
- **Andrew Beer** Managed futures should be about a 3% allocation: large enough to matter in a 2022-type event but small enough to hide in the tall grass in years like 2025.  #mech/risk_management
  > it needs to be big enough that in 2022, the next time there's a 2022, you can point to it and say, "Look, we've got this beacon of green and a sea of red."
  indicator: 3% allocation to managed futures · asset: multi · horizon: years · testable: yes - portfolio optimisation with behavioural constraint · confidence: medium
  ^MT030-C20-3
- **Andrew Beer** Selling trend to wealth managers requires a narrative that fits their constructs, not statistical obviousness aimed at institutional allocators.  #mech/behavioral
  > when you move into the wealth management space, the language needs to change
  asset: multi · testable: no - communication · confidence: medium
  ^MT030-C20-4

