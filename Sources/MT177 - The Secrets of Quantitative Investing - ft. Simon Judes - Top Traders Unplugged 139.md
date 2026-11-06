---
source_id: MT177
title: "The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139"
date: 2023-03-21
channel: "Top Traders Unplugged"
url: 
words: 14098
claims: 62
added_by_crosscheck: 14
corrections: 1
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Simon Judes (co-CIO, Winton)", "Niels Kaastrup-Larsen (host)", "Alan Dunne (co-host)"]
tags: [source, layer0]
---
# The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139

**Speakers:** Simon Judes (co-CIO, Winton); Niels Kaastrup-Larsen (host); Alan Dunne (co-host)

**Summary:** Judes explains Winton's scientific research approach, three-quarters trend plus one-quarter other signals, why long-term trend Sharpe is about 0.5 and fast trends deteriorated most. Adds that more genuinely diversifying markets matter via effective number of markets, risk is not volatility, and trend is often contrarian. Conclusions: no regime-based speed switching, humans own key parameters, scenario stress tests from history and correlation shocks.

**Approach:** trend following, CTA, research method, risk management, market diversification, machine learning

**Cross-check completeness estimate of first read:** 0.82 - first reader's 46 claims cover the core Winton method, speed, markets, risk and contrarian-trend arguments; additions are secondary reasoning (allocator mechanism, research structure, correlation condition, caveats).

## Argument map

**Episode thesis:** Simon Judes, co-CIO of Winton (Top Traders Unplugged 139, uploaded 21 March 2023), argues that Winton's edge comes from empirical scientific research with strict data-mining controls, rejecting the efficient market hypothesis, and from hyper-vigilant risk management that goes beyond volatility. Long-term trend following Sharpe is about 0.5 (declining as the number of traders grew, with fast trend deteriorating most), so Winton runs a diversified CTA that is 75% trend and 25% other signals, adds genuinely diversifying alternative markets (effective number of markets, not raw count), lets humans own key parameters, refuses to switch trend speed on regime (that is an implicit call on the Fed), and sees trend as often contrarian to prevailing narratives. Kaastrup-Larsen pushes the portfolio-Sharpe framing and challenges the 'more markets' claim; Dunne adds that falling costs and fees partly offset the lower gross Sharpe.

### Simon Judes (Guest; co-CIO of Winton (joined July 2008; firm founded about 25 years earlier by David Harding, about 200 staff, USD 10bn AUM))
Fingerprint: #approach/trend_following #approach/research_robustness_overfitting #approach/portfolio_construction_stacking #approach/position_sizing_vol_target #approach/crisis_alpha_convexity #approach/carry #approach/regime_detection #approach/costs_execution
_Speaker note: Speaks for Winton as a firm. Statements about David Harding's 2018 comments are relayed. The 2023 market-position remarks (short bonds, long equities) describe Winton's trend book at the time of recording (about March 2023). The replication fee figure (about 95bp) is the host's, not his (ledger correction applied)._

**Worldview premises**
- The efficient market hypothesis is not the right foundation: with hard work and scientific analysis good predictions about markets are possible, so one approaches markets with an open mind rather than preconceived theories. _[experience, stated; support: Winton's founding experience; David Harding found EMH to be a headwind for years.]_ ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C02-2|C02-2]])
- Early market experiences (1987, 2008) shape how researchers and firms parametrise and organise trend strategies, a behavioural source of differences between trend followers. _[experience, stated; support: Own experience of joining in July 2008 and Harding's 1987 experience; observation of firms that started after 2008.]_ ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C02-1|C02-1]])
- Data-mining false positives are the central threat to research; they are avoided by shared statistical techniques for multiple and sequential hypothesis testing and by a process that stops researchers privately overfitting many ideas and presenting only the good subset. _[theoretical, stated; support: Describes hiring, training and process; no specific tests or thresholds quoted.]_ ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C02-3|C02-3]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C02-4|C02-4]])
- Confidence in a new signal comes from backtest statistics (Sharpe, correlation to existing strategies) plus, when available, an economic rationale with testable intermediate relationships; lack of rationale lowers confidence but does not kill the idea. The sources of alpha are a mixture of behavioural, structural and microstructure effects, so who is on the other side is hard to say. _[theoretical, stated; support: Winton practice.]_ ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C03-1|C03-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C03-2|C03-2]])
- Long-term trend following Sharpe is about 0.5, which is scarcely enough on its own to run a fund; other signals should be added to raise Sharpe. Trend performance has declined steadily since the 1970s (first seen in Winton research around 2007), not only after 2008. _[empirical, stated; support: Harding's 2018 statement and Winton long-horizon research on the strategies in use at the time.]_ ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C04-1|C04-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C04-2|C04-2]])
- The decline correlates strongly with growth in the number of traders of the strategy, so 0.5 is the expectation; long simulations show only that underlying markets trend, not what a crowded real strategy will earn. _[empirical, stated; support: Observed correlation over the last 50 years with industry growth; no figures given.]_ ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C19-1|C19-1]])
- Fast trend strategies deteriorated most since 1997 because everyone traded them; slow strategies started with lower Sharpe. Pure Sharpe maximisation favours very slow trend, but investors also want responsiveness at turning points like 2008 and 2022. _[empirical, stated; support: Winton analysis of speeds (paper on its website).]_ ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C08-1|C08-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C08-2|C08-2]])
- Trend cannot be timed and a good year does not predict a bad next year (good years come in sequences), but allocators bear personal risk if trend underperforms right after they allocate, so their concerns should be addressed (for example averaging in over months) rather than answered with statistics. _[experience, stated; support: Winton's pre-2008 record of good years; allocator conversations.]_ ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C06-3|C06-3]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C07-1|C07-1]])
- Allocators drop trend after long drawdowns not for lack of faith but because each line item must be justified to an investment committee; smoothing drawdowns has great value but adding non-trend signals necessarily reduces crisis effectiveness, so the type and weight of added signals matter. _[behavioural, stated; support: Allocator experience and Winton's own trade-off.]_ ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C05-1|C05-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C05-X1|C05-X1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C05-2|C05-2]])
- Liquidity, opportunism and no bias are necessary but not sufficient for crisis performance; trend works in extended trends and fails when equities rise steadily then reverse sharply (February 2018). Labels like 'crisis alpha' mislead, so describe the response in different environments instead. _[theoretical, stated; support: Historical record of trend in crises, February 2018 as counterexample.]_ ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C06-1|C06-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C06-2|C06-2]])
- Trend following is often contrarian to prevailing fundamental narratives (oil in 2014 when shale supply was underestimated against a peak-oil view; German yields falling into negative territory against the belief they could never go below zero), and trends extend in time precisely when a narrative says the market must go the other way. _[empirical, stated; support: Two named examples.]_ ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C19-2|C19-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C20-1|C20-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C19-R1|C19-R1]])
- Slow-horizon strategies have too few independent events for machine learning (one cannot rerun a crash; observational science), while fast intraday strategies have many observations and suit machine learning (experimental science). _[theoretical, stated; support: Winton paper on observational versus experimental science; astronomy versus particle-physics analogy.]_ ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C10-2|C10-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C11-1|C11-1]])
- Sharpe scales with the square root of the effective number of markets, not the count: 50-60 classical markets may be only 8-10 independent, so adding genuinely different markets adds a lot. Alternative markets outperformed major markets over the last decade, including the post-crisis period when mainstream trend struggled. _[theoretical, stated; support: Correlation arithmetic; European gas up tenfold as the largest trend he has seen; no performance table quoted.]_ ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C13-1|C13-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C13-2|C13-2]])
- Alternative markets earn extra return partly because barriers to entry (software, operations, middle office) keep trend followers from extending into them; many OTC alternatives can be cleared on exchange, reducing counterparty risk toward major-futures levels. _[institutional, stated; support: Winton's own build-out experience.]_ ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C15-1|C15-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C14-2|C14-2]])
- Risk is not volatility: volatility is easy to estimate but loss risk is hard (VIX at record lows in 2017 while valuations were rich), so use many risk measures and scenarios. _[theoretical, stated; support: The 2017 low-VIX / rich-valuation example.]_ ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C16-1|C16-1]])
- Claiming that a systematic process is fully automated hides that someone must still choose the parameters or the algorithm that picks them (an infinite regress); a firm must decide at which level humans take responsibility, and Winton pushes responsibility to humans fairly early (trend speed, asset allocation). _[theoretical, stated; support: Reasoning from first principles; not a result.]_ ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C11-X1|C11-X1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C12-1|C12-1]])

**Chain: Why switching trend speed with the regime is an implicit Fed call**
1. February-March 2020: markets fall for a month until the Fed intervenes → Fast trend beats slow trend (turn positions short within two weeks and profit as the fall continues; slow trend loses on the way down and again on the rebound): Short duration of the fall before policy intervention. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C09-2|C09-2]])
2. Two weeks into the fall with a slow trend long → Choosing to speed up is right only if the Fed steps in later, wrong if it steps in now, and about the same if it does not step in: The decision amounts to a bet on what the Fed will do and when. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C10-1|C10-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C10-R1|C10-R1]])
3. No evidence that fast trend's edge persisted → Slower trend did better again afterwards; no regime-based speed switching: Predicting policy is the job of discretionary macro managers, not systematic managers. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C09-2|C09-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C10-1|C10-1]])
- Evidence: The 2020 episode and subsequent performance; qualitative scenario reasoning.
- Fails when: Not stated; a systematic speed switch that does not rely on policy forecasts is not considered.

**Chain: Adding non-trend signals: smoothing versus convexity**
1. Long drawdowns in trend between 2008 and 2022 → Allocators drop trend because each line item must be justified: Investment-committee accountability. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C05-1|C05-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C05-X1|C05-X1]])
2. Add non-trend signals (carry, statistical, economic, faster technical) → Smoother drawdowns but less crisis effectiveness: Trade-off in type and weight; carry in equities would add long equity bias and reduce convexity, so carry is traded in commodities and fixed income as well as currencies, where small-gain/large-loss is mitigated. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C05-2|C05-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C07-2|C07-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C07-X1|C07-X1]])
3. Winton sets 75% trend / 25% other and fixes it → Trend profile retained with some drift, and investors know what they receive: Mix depends on opportunity set but is fixed deliberately. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C01-2|C01-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C07-3|C07-3]])
4. Lower expected trend Sharpe → Split into pure trend, diversified CTA and multi-strategy products: Offer choice rather than abandon trend. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C04-3|C04-3]])
- Evidence: Winton's product design and the 2008/2022 record.
- Fails when: If added signals are mostly slow and economically related they reduce convexity in crises.

**Chain: Why more genuinely different markets add return**
1. Correlations among 50-60 markets → Only about 8-10 independent markets: Equity indices, bond futures and many commodities are highly correlated. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C13-1|C13-1]])
2. Add Chinese futures, regional gas, power, freight, marine fuel (not equity sector ETFs or developed-market swaps) → Large diversification and large trends (gas up tenfold): Genuinely alternative and additive; barriers to entry keep others out. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C14-1|C14-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C15-1|C15-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C13-2|C13-2]])
3. Access via onshore, internationalised contracts, swaps and QFI; clearing on exchange where possible → Execution and counterparty risk contained: Operations and software built to absorb markets without large headcount growth. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C14-X2|C14-X2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C14-2|C14-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C15-1|C15-1]])
- Evidence: Correlation arithmetic and recent trends; no portfolio-level performance numbers given.
- Fails when: When added markets are correlated with vanilla ones or are easy for competitors to access.

**Chain: Scenario-based risk management and the 2013 taper tantrum**
1. Replay current positions through every historical environment (worst day/week), e.g. the 1990 Gulf War oil jump of 30% → Ask whether that loss is acceptable: By definition anything that happened is realistic. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C16-2|C16-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C17-R2|C17-R2]])
2. Before 2013 trend was long bonds and long stocks with negative correlation; scenario in which correlation turns positive → Loss judged unacceptable, volatility run lower: Stylised correlation-shock stress test. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C17-3|C17-3]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C18-1|C18-1]])
3. March 2023: short bonds, long equities, modestly positive stock-bond correlation because of the inflation dynamic → Main worry is a classic risk-off (bonds rally, equities fall) on disinflationary bad news; leverage may be held in a band: That scenario is worst for the current book. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C17-1|C17-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C17-X1|C17-X1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C17-2|C17-2]])
- Evidence: Historical replays and the 2013 outcome.
- Fails when: Judes concedes the worst case imaginable is everything to zero, so scenarios must be anchored in realism.

**Decision process**
- [research] Two research streams: finding new alpha sources (ideas or data), and maintaining existing ones (reviewing trend speed, signal construction and volatility models); do original research rather than rely on academic journals, including ideas found in Chinese commodity markets that work globally.. Why: Journals are not at the forefront of alpha research; large research department. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C09-X1|C09-X1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C08-3|C08-3]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C01-1|C01-1]])
- [research] Test many hypotheses with simultaneous and sequential multiple-testing techniques and a process that exposes all attempted ideas, not just the best backtests; hire and train for statistical competence.. Why: Avoid false positives. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C02-3|C02-3]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C02-4|C02-4]])
- [research] Update models after market events (February 2007 reversal that hit CTA positions led to volatility-model changes that helped in February 2018) but do not conclude a regime has changed from one episode (March 2020).. Why: Learning from new event types without overreacting to single occurrences. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C09-1|C09-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C09-2|C09-2]])
- [signal] Keep trend as the core (about 75% of the diversified CTA), add carry (not in equities), statistical, economic and faster technical signals; add new signals each year.. Why: Raise Sharpe while preserving the trend profile. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C01-2|C01-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C05-2|C05-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C07-2|C07-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C07-X1|C07-X1]])
- [signal] Parameters mostly universal across markets, adjusted for transaction costs, market impact, spreads and commissions; trend speed chosen with some faster component for turning points even at lower Sharpe; no regime-based speed switching.. Why: Investor objectives and implicit policy call. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C11-2|C11-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C08-2|C08-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C10-1|C10-1]])
- [universe] Prioritise effective number of markets: add Chinese futures, regional gas and power, freight, marine fuel; avoid equity sector ETFs and developed-market swaps correlated with existing exposure.. Why: Square-root-of-effective-markets argument. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C13-1|C13-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C14-1|C14-1]])
- [execution] Access Chinese futures onshore, through internationalised contracts, via swaps and via the QFI route; clear OTC alternative markets on exchange where possible; invest in software and automation to absorb markets.. Why: Reduce counterparty risk and operating burden. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C14-X2|C14-X2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C14-2|C14-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C15-1|C15-1]])
- [risk] Replay current positions through all historical environments, run stylised correlation-flip stress tests, look beyond volatility, and let leverage float with signal strength and correlation inside a band decided by the risk measures.. Why: Risk is not volatility; correlation flip tested in 2013. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C16-1|C16-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C16-2|C16-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C17-2|C17-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C17-3|C17-3]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C18-1|C18-1]])
- [portfolio] Fix the trend/non-trend mix; offer pure trend, diversified and multi-strategy products and bespoke programs (varying alternative-market or China exposure more than trend share); offer capped-equity-long trend as an option.. Why: Allocator drawdown tolerance and process vary; cap lowers long-term performance in proportion but helps the crisis profile. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C07-3|C07-3]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C15-2|C15-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C18-2|C18-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C04-3|C04-3]])
- [other] Humans own early design decisions (trend speed, asset allocation, overall strategy leverage, adding a signal) made with analysis; optimisers are used where they do not obscure understanding of the portfolio.. Why: Preserve understanding and responsibility; machine learning reserved for fast intraday strategies. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C12-1|C12-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C11-X1|C11-X1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C10-2|C10-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C11-1|C11-1]])
- [other] Single-manager risk is mitigated by fund of funds (with lost fee netting), not by regression-based replication, which is itself a single manager.. Why: Replication is another manager; using several trend managers trades fee netting for diversification. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C12-2|C12-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C18-3|C18-3]])

**Evidence style:** Scientific-method framing with emphasis on statistical controls against data-mining; historical event studies (1987, 2007, 2008, 2013, 2014, 2018, 2020, 2022); correlation arithmetic; scenario replays; few numerical results quoted.

**Views at the time**
- (2023-03 (upload 2023-03-21)) No reason to think 2023 will be bad because 2022 was good; averaging in over several months is a reasonable way to address timing concerns.. Reasoning: Good years come in sequences; 2008 followed good years. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C07-1|C07-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C06-3|C06-3]])
- (2023-03) Expected long-term trend Sharpe is about 0.5 and slower trend has done better again since 2020, so no change in the view that trend remains Winton's biggest source of return.. Reasoning: Industry growth correlates with decline; no evidence that faster trend's 2020 outperformance persisted. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C19-1|C19-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C09-2|C09-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C04-2|C04-2]])
- (2023-03) Current trend positions are short bonds and long equities, so the key scenario risk is a disinflationary risk-off with bonds rallying and equities falling; stock-bond correlation is modestly positive because of inflation.. Reasoning: Positioning of the book and recent correlation. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C17-1|C17-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C17-X1|C17-X1]])
- (2023-03) Alternative markets have outperformed major markets over the last decade (2022 was the first year not substantially true); European gas and power produced huge trends.. Reasoning: Low correlation and barriers to entry. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C13-2|C13-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C15-1|C15-1]])
- (2023-03) Winton's 2023 priorities are original research for new alpha sources and improving existing ones, and hyper-vigilant risk management monitoring many scenarios.. Reasoning: What matters is what can be controlled. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C01-1|C01-1]])

### Niels Kaastrup-Larsen (Host; veteran CTA manager)
Fingerprint: #approach/trend_following #approach/manager_selection_allocation #approach/crisis_alpha_convexity #approach/portfolio_construction_stacking #approach/behavioral_sentiment
_Speaker note: Most turns are questions, but he states views on Sharpe framing, investors' timing mindset and number of markets. His own firm offers a major-markets trend strategy (a conflict of interest in the 'more markets' debate)._

**Worldview premises**
- Trend following should be judged by the improvement in total-portfolio Sharpe it delivers, not by its stand-alone Sharpe or a 'crisis alpha' mandate, because Sharpe was not created for single-strategy evaluation. _[theoretical, stated; support: Reaction to the AQR paper on trend mandates.]_ ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C04-X1|C04-X1]])
- Crisis alpha originally meant three traits (liquid, opportunistic, unbiased long or short), as Kaminski explains: in 2020 the best trade was long bonds and short energy, in 2022 the opposite. _[experience, stated; support: Katie Kaminski interview on the same podcast.]_ ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C05-3|C05-3]])
- Potential investors treat trend following as a tactical trade and assume that after a strong 2022 it is too late or cannot repeat, a market-timing mindset that trend followers need to counter. _[experience, stated; support: Investor conversations while travelling.]_ ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C06-X1|C06-X1]])
- A 50-60 market classical portfolio already includes diversified commodities, and going from 100 to 200 markets mostly adds correlated financial markets unless the extras are genuinely alternative (such as Chinese futures); he sees no huge long-term performance difference between managers with different market counts. _[experience, stated; support: Observation of manager track records; no data quoted.]_ ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C14-X1|C14-X1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C13-R2|C13-R2]])

**Chain: Why investors mis-time trend following**
1. Strong 2022 for trend → Potential investors assume it is too late or cannot repeat: Treat trend as a trade to be timed. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C06-X1|C06-X1]])
- Evidence: Conversations with potential investors.
- Fails when: Judes replies that good years come in sequences.

**Decision process**
- [other] Frames the discussion around portfolio Sharpe improvement rather than stand-alone Sharpe or labels.. Why: Sharpe was designed for portfolios. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C04-X1|C04-X1]])

**Evidence style:** Anecdote, industry conversations and published papers (AQR, Kaminski).

**Views at the time**
- (2023-03) The investor mindset after 2022 that it is too late for trend is wrong and needs to be countered.. Reasoning: Market-timing notion applied to a strategy that adapts. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C06-X1|C06-X1]])
- (2023-03) Going from 100 to 200 markets mostly adds correlated financial markets unless genuinely alternative.. Reasoning: Classical portfolio of 50-60 already diversified. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C14-X1|C14-X1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C13-R2|C13-R2]])

### Alan Dunne (Co-host; macro and CTA analyst)
Fingerprint: #approach/trend_following #approach/costs_execution #approach/manager_selection_allocation
_Speaker note: Mostly asks questions; one stated view, mapped for completeness._

**Worldview premises**
- Lower trading costs and lower fees partly offset the decline in gross trend Sharpe, so the investor's net outlook is less negative than the 0.5 gross estimate suggests. _[empirical, stated; support: Reasoning from cost and fee trends; no numbers.]_ ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C19-X1|C19-X1]])

**Evidence style:** Asks structured questions drawn from other guests' research (100-200 year trend studies).

**Views at the time**
- (2023-03) Net-of-cost trend outlook is better than the gross 0.5 Sharpe suggests because costs and fees have fallen.. Reasoning: Lower trading costs and fees. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C19-X1|C19-X1]])

### Disagreements
- **Does trading more (alternative) markets improve long-term performance?**: Simon Judes: Yes: only 8-10 of 50-60 markets are independent, alternative markets outperformed major markets over the decade, and the markets added must be genuinely alternative. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C13-1|C13-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C13-2|C13-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C14-1|C14-1]]); Niels Kaastrup-Larsen: Sees no huge difference in long-term performance between managers; 50-60 classical markets already diversified; going from 100 to 200 mostly adds correlated financial markets. Judes largely agrees on that last point. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C13-R2|C13-R2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C14-X1|C14-X1]])
- **Outlook for trend Sharpe**: Simon Judes: Expectation is about 0.5 gross, because performance declines as more traders do the strategy; long simulations show only that markets trend. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C04-1|C04-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C19-1|C19-1]]); Alan Dunne: Lower trading costs and fees partly offset the lower gross Sharpe for investors. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C19-X1|C19-X1]]); Niels Kaastrup-Larsen: Judge trend by improvement in portfolio Sharpe, not stand-alone Sharpe. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C04-X1|C04-X1]])
- **Is trend following a herding strategy?**: Simon Judes: No: it is often contrarian to the prevailing narrative (oil 2014, German yields into negative territory). ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C19-2|C19-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C20-1|C20-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C19-R1|C19-R1]]); Critics (as characterised by Judes, not speakers): A dumb strategy of people following each other in herd behaviour. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C19-R1|C19-R1]])
- **Can regression-based CTA replication mitigate single-manager risk?**: Simon Judes: No: the replicator is itself a single manager; a fund of funds is the way to diversify manager risk, with its own pros and cons. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C12-2|C12-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C18-3|C18-3]]); Replication providers (as characterised by Judes, not speakers): Claim that replication mitigates single-manager risk. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C12-2|C12-2]])

### Gaps and conflicts
- The argument that switching speed is an implicit Fed call applies equally to choosing any fixed speed, and Winton does choose a mix of speeds partly for turning points (2008, 2022); the distinction between a static and a dynamic choice is asserted rather than argued. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C10-1|C10-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C08-2|C08-2]])
- The claim that trend decline correlates strongly with growth in the number of traders is stated without data or measure of trader count; alternative explanations (market structure, costs) are not discussed. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C19-1|C19-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C04-2|C04-2]])
- No Sharpe, return or drawdown numbers are given for Winton products, the 75/25 mix, the alternative markets or the capped-beta option; 'outperformed by a long way' is unquantified. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C13-2|C13-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C05-2|C05-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C18-2|C18-2]])
- Judes says Winton lowered volatility ahead of the 2013 taper tantrum due to a correlation scenario, which is a discretionary-looking risk call alongside a claim that trend should not be timed or regime-switched; the boundary between risk overlay and timing is not defined. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C17-3|C17-3]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C18-1|C18-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C10-1|C10-1]])
- Statement that Winton has not changed its view since Harding's 2018 comment coexists with the observation that trend Sharpe has declined steadily since the 1970s; the product split is presented as a response, not a contradiction. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C04-1|C04-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C04-3|C04-3]])
- Alternative-market outperformance and barriers to entry are given as the reasons for extra return, but the same crowding logic that explains trend's decline would predict erosion as more managers extend into these markets; not addressed. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C15-1|C15-1]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C13-2|C13-2]], [[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C19-1|C19-1]])
- The replication fee (about 95bp) is the host's figure, and Judes says he has not looked closely at replication products, so his rejection of the single-manager-risk claim rests on logic rather than study. ([[MT177 - The Secrets of Quantitative Investing - ft. Simon Judes - Top Traders Unplugged 139#^MT177-C12-2|C12-2]])

### Forward-looking inputs (reader synthesis)
(reader) Judes names few price-leading inputs: the stock-bond correlation (modestly positive due to inflation) and the direction of news (disinflationary and negative for growth) as the key scenario for a short-bond, long-equity trend book; central bank intervention timing is treated as unforecastable by systematic managers. Longer-term he treats the number of traders in trend following as the driver of expected trend Sharpe, with 0.5 as the planning figure, and the effective number of independent markets as the driver of diversification benefit. Horizons are scenario-based (days to weeks for stress tests) and multi-year for Sharpe.

### Reader inferences (not stated by the speakers)
- (reader) Winton's stance is built around process: scientific research controls, human responsibility for key parameters, a fixed product mix and scenario risk management, with the investor experience (drawdowns, committees) as an explicit design input.
- (reader) The 75/25 mix, the alternative-market expansion and the product split can be read as three responses to the same belief that stand-alone trend Sharpe is about 0.5 and falling.
- (reader) Judes separates what is knowable (long-run markets trend; crowding lowers Sharpe) from what is not (timing of trend, Fed behaviour), and builds rules around the second category by refusing to act on it.
- (reader) Kaastrup-Larsen's portfolio-Sharpe framing and Judes's investor-experience framing converge on the argument against evaluating trend on stand-alone Sharpe or crisis labels.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 2 | intro, Winton overview and product structure |
| C02 | 4 | history effect, scientific philosophy, avoiding data mining |
| C03 | 2 | confidence via backtest vs rationale, sources of alpha, Harding 2018 comment question |
| C04 | 3 | long-term trend Sharpe 0.5, performance decline, three products |
| C05 | 3 | investor experience, smoothing drawdowns, crisis alpha traits |
| C06 | 3 | crisis alpha is necessary-not-sufficient, labels, allocator timing worries |
| C07 | 3 | averaging in, carry in the mix, 75/25 level, speed question |
| C08 | 3 | speed deterioration, research sources |
| C09 | 2 | types of research, event-driven model changes, March 2020 |
| C10 | 2 | no regime speed switching, machine learning data limits |
| C11 | 2 | observational vs experimental, parameters across markets |
| C12 | 2 | human responsibility for parameters, CTA replication |
| C13 | 2 | number of markets, effective independent markets |
| C14 | 2 | genuinely alternative markets, counterparty risk |
| C15 | 2 | barriers to entry, portfolio role, customised programs |
| C16 | 2 | risk is not volatility, historical stress replay |
| C17 | 3 | current scenario risks, leverage, correlation shock 2013 |
| C18 | 3 | 2013 outcome, equity beta cap, number of managers |
| C19 | 2 | return expectations, crowding, contrarian view of trend |
| C20 | 1 | trend as contrarian: German yields, closing priorities |
| C21 | 0 | nothing actionable: outro and plugs |

## Claims

### C01
- **Simon Judes** Winton's priorities are original research for new alpha sources and improvement of existing ones, plus hyper-vigilant risk management that monitors many possible scenarios.  #mech/research_method
  > what matters is original research to find new Alpha sources and you know improve our existing ones and on risk management
  asset: multi · testable: no - process statement · confidence: high
  ^MT177-C01-1
- **Simon Judes** Winton runs a diversified CTA that is 75% trend following and 25% other systematic macro strategies, alongside pure trend and quant multi-strategy products.  #mech/risk_management
  > there's a diversified CTA which is three-quarters Trend following and a quarter other systematic microstrategies and then we have pure Trend products as well
  indicator: trend / non-trend allocation · asset: multi · testable: partly - mix is a design choice testable via backtest · confidence: high
  ^MT177-C01-2

### C02
- **Simon Judes** Researchers' and firms' early market experiences (1987, 2008) shape how they parametrise and organise trend strategies, a behavioural source of differences between trend followers.  #mech/behavioral
  > people have been very influenced by their initial experiences
  asset: multi · testable: no - observation · confidence: medium
  ^MT177-C02-1
- **Simon Judes** Winton's philosophy is to approach markets with an open mind and use empirical scientific research, rejecting the efficient market hypothesis as a foundation, because good predictions are possible with hard work.  #mech/research_method
  > you can discover and improve successful investment strategies by applying empirical scientific research methods
  asset: multi · testable: no - philosophy · confidence: high
  ^MT177-C02-2
- **Simon Judes** Avoiding data-mining false positives requires shared statistical techniques for testing many hypotheses simultaneously and sequentially, which also drives hiring and training.  #mech/research_method
  > help you in particular test multiple hypotheses at the same time and sometimes also sequentially one after the other
  indicator: multiple-testing procedures · asset: multi · testable: yes - apply multiple-testing corrections to trial counts · confidence: high
  ^MT177-C02-3
- **Simon Judes** Process must prevent researchers from privately overfitting many ideas and presenting only the subset that looked good in a backtest.  #mech/research_method
  > avoiding situations where researchers privately overfit ideas and day touring and then only show you
  indicator: research trial log · asset: multi · testable: yes - log all trials and count them · confidence: high
  ^MT177-C02-4

### C03
- **Simon Judes** Backtest statistics give confidence in Sharpe and low correlation, and an economic rationale with testable intermediate relationships adds confidence; absence of a rationale lowers confidence rather than killing the idea.  #mech/research_method
  > if there is for example an economic rationale behind a particular idea then you can use that you can test the intermediate economic relationships and that can add additional confidence
  indicator: backtest Sharpe, correlation to existing strategies · asset: multi · testable: yes - tiered evidence thresholds · confidence: high
  ^MT177-C03-1
- **Simon Judes** Winton's alpha comes from a mixture of behavioural, structural and microstructure sources depending on strategy, so it is hard to say who is on the other side of the trades.  #mech/structural_shift
  > extremely diverse collection of alpha sources
  asset: multi · testable: no - generalisation declined · confidence: medium
  ^MT177-C03-2

### C04
- **Simon Judes** Harding's 2018 view is that long-term trend following Sharpe is around 0.5, enough on its own to run a fund only marginally, so other signals should be added to raise Sharpe.  #mech/slow_reaction
  > the long-term sharp outlook for Trend following is perhaps around a half
  indicator: trend following Sharpe ratio · asset: multi · horizon: years · testable: yes - Sharpe of trend indices over time · confidence: high
  ^MT177-C04-1
- **Simon Judes** Over a long window from the 1970s trend performance declined steadily for the strategies in use; the decline was first seen in Winton research around 2007 and was not just a post-2008 story.  #mech/crowding_positioning
  > then you actually find a consistent decline in the performance of trend um of the kind of trend strategies that people were trading at the time
  indicator: trend strategy performance since 1970s · asset: multi · direction: trend Sharpe down over time · horizon: years · testable: yes - rolling Sharpe of trend · confidence: high
  ^MT177-C04-2
- **Simon Judes** Winton responded to lower trend Sharpe expectations by splitting into pure trend, diversified CTA and multi-strategy products rather than abandoning trend.  #mech/structural_shift
  > instead of having one product uh dominated by Trend following we now have three products
  asset: multi · testable: no - business response · confidence: high
  ^MT177-C04-3
- **Niels Kaastrup-Larsen** Trend following should be judged by the improvement in total-portfolio Sharpe it delivers, not by its stand-alone Sharpe or a 'crisis alpha' mandate, because Sharpe was not created for single-strategy evaluation (reacting to the AQR paper on trend mandates).  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > my opinion is we probably should change the conversation to talk about the Improvement of portfolio shop that these strategies provide
  indicator: portfolio Sharpe improvement · asset: multi · conditions: when trend is held alongside traditional assets · testable: yes - marginal contribution to portfolio Sharpe can be computed · confidence: medium
  ^MT177-C04-X1

### C05
- **Simon Judes** Trend gave diversification in 2008 and 2022, but the long drawdowns in between make allocators drop it; judging by investor experience beats focusing on Sharpe or mandate labels.  #mech/behavioral
  > I think we prefer to look at the investor experience you look at situations where investors really needed diversification in 2008 uh last year and trend has done very well there
  indicator: trend returns in equity crises · asset: multi · horizon: years · testable: yes - trend vs equity drawdown episodes · confidence: medium
  ^MT177-C05-1
- **Simon Judes** Adding non-trend signals smooths drawdowns but reduces crisis effectiveness, so type and weight of added signals matter; Winton chooses 75% trend as the level that keeps the trend profile with some drift.  #mech/risk_management
  > there's Great Value in adding signals which smooth out those drawdowns
  indicator: non-trend signal weight · asset: multi · direction: drawdowns down, crisis convexity down · horizon: years · conditions: depends on which signals are added and their weight · testable: yes - blend-weight sweep · confidence: high
  ^MT177-C05-2
- **Niels Kaastrup-Larsen** Kaminski's crisis alpha traits: liquid, opportunistic (can move to where the action is) and unbiased (long as easily as short); in 2020 the best trade was long bonds and short energy, in 2022 the opposite.  #mech/slow_reaction
  > it needs to have um you know it needs to be opportunistic so that you you don't you're not stuck in the same asset class or in the same Market you can move around
  indicator: trend following across markets · asset: multi · horizon: years · testable: partly - trade direction by year documented · confidence: medium
  ^MT177-C05-3
- **Simon Judes** Allocators abandon trend after long drawdowns not from lack of faith but because each line item must be justified to an investment committee, which is why smoothing the drawdowns has great value.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > the people who are making these allocation decisions have to justify each line item to their investment committees and it becomes very difficult
  indicator: allocator behaviour in drawdowns · asset: multi · horizon: years · conditions: when allocation decisions are scrutinised line by line · testable: partly - allocator flows can be studied · confidence: high
  ^MT177-C05-X1

### C06
- **Simon Judes** Liquidity, opportunism and no bias are necessary, not sufficient, for crisis performance; trend does well in extended trends but fails when equities rise steadily then reverse sharply (Feb 2018).  #mech/slow_reaction
  > those three characteristics that you mentioned are prerequisites for something to function in that way but they don't guarantee that it's going to work
  indicator: trend following in sharp reversals · asset: equities · direction: trend loses · horizon: weeks · conditions: after a steady equity rise followed by a sharp downturn · testable: yes - trend returns around Feb 2018 type reversals · confidence: high
  ^MT177-C06-1
- **Simon Judes** Labels like crisis alpha mislead because trend only sometimes works in crises; describe its response in different environments instead.  #mech/research_method
  > the best thing is to really try and describe the strategy how it's going to react what it's going to do in different environments
  asset: multi · testable: no - communication advice · confidence: high
  ^MT177-C06-2
- **Simon Judes** Trend cannot be timed, but allocators bear personal risk if it underperforms right after they allocate, so concerns should be addressed rather than answered with statistics.  #mech/behavioral
  > even if you um can't time Trend following even if we agree that you can't time when it's going to work there's still a risk for the allocator
  asset: multi · testable: no - behavioural · confidence: medium
  ^MT177-C06-3
- **Niels Kaastrup-Larsen** Potential investors treat trend following as a tactical trade and assume that after a strong 2022 it is too late or cannot repeat, a market-timing mindset that trend followers need to counter.  #mech/behavioral _(added by sonnet-xhigh cross-check, time-bound view)_
  > they kind of look at Trend following a little bit like a trade they try to time it and then also they have this notion that well it did so well in 2022 um it's either too late
  indicator: investor timing of trend allocation · asset: multi · horizon: months · conditions: after strong trend years · testable: partly - flows after good years can be checked · confidence: medium
  ^MT177-C06-X1

### C07
- **Simon Judes** A good year does not predict a bad next year: 2008 was good but all prior Winton years were also good, and good years come in sequences; investors can average in over months to ease timing worries.  #mech/cycle_persistence
  > there's no reason to think that next year will be um will be bad because last year was good
  indicator: trend annual returns · asset: multi · horizon: years · testable: yes - autocorrelation of annual CTA returns · confidence: medium
  ^MT177-C07-1
- **Simon Judes** Carry added to trend is not traded in equities because it adds long equity bias and reduces convexity; carry's currency-style small-gain/large-loss profile is mitigated by trading it in commodities and fixed income too.  #mech/risk_premium
  > we don't trade it on um equities um though because often that that does just add a long bias to your Equity portfolio
  indicator: carry signal across asset classes · asset: multi · direction: carry returns smoother across commodities and bonds than currencies · horizon: years · conditions: equities excluded because of long bias · testable: yes - carry by asset class · confidence: high
  ^MT177-C07-2
- **Simon Judes** The trend/non-trend mix depends on the opportunity set but is fixed so investors know what they receive.  #mech/risk_management
  > important to you know fix a level so that investors know what they're what they're going to get
  asset: multi · testable: no - governance choice · confidence: medium
  ^MT177-C07-3
- **Simon Judes** The non-trend quarter of the diversified CTA is a mixture of purely statistical signals, economic-rationale signals and non-trend technical signals, some faster than trend, with new signals added each year.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > some of them are purely statistical in nature some of them have economic rationales some of them are other technical signals like Trend following that are different from Trend following
  indicator: non-trend signals in Winton diversified program · asset: multi · testable: no - not specified · confidence: medium
  ^MT177-C07-X1

### C08
- **Simon Judes** Fast trend strategies deteriorated most since 1997 because everyone traded them; slow strategies started with lower Sharpe, so always choosing the best speed shows decline.  #mech/crowding_positioning
  > the largest deterioration is seen in the faster Trend strategies this is what everyone was trading
  indicator: trend speed (lookback) Sharpe · asset: multi · direction: fast trend Sharpe down, slow flat · horizon: years · testable: yes - speed-split Sharpe over time · confidence: high
  ^MT177-C08-1
- **Simon Judes** Maximising Sharpe alone favours very slow trend, but investors want responsiveness at turning points like 2008 and 2022, so some faster speed fits objectives even at lower Sharpe.  #mech/slow_reaction
  > if you're trying to purely maximize the the sharp ratio um then uh what our analysis has shown is that you really want to be very slow
  indicator: trend lookback choice · asset: multi · direction: slower speed gives higher Sharpe · horizon: years · conditions: investor objective is crisis responsiveness not Sharpe · testable: yes - speed-blend backtest · confidence: high
  ^MT177-C08-2
- **Simon Judes** Winton finds academic journals no longer at the forefront of alpha research and instead does original research, sometimes finding ideas from Chinese commodity markets that work globally.  #mech/research_method
  > one place we uh we haven't uh looked so much recently though is is in academic journals actually
  asset: multi · testable: no - process · confidence: medium
  ^MT177-C08-3

### C09
- **Simon Judes** Event-driven model adjustments: Feb 2007's reversal that hit CTA positions (crowding effect) led to volatility model changes that helped in Feb 2018.  #mech/crowding_positioning
  > often adjustments to our our volatility models for example have been prompted by new types of events
  indicator: CTA volatility models, Feb 2007 and Feb 2018 reversals · asset: multi · direction: CTA losses in sudden reversals after low-volatility equity rises · horizon: days · conditions: after rising equities on low volatility · testable: partly - two events · confidence: high
  ^MT177-C09-1
- **Simon Judes** Fast trend beat slow in Feb-Mar 2020 because the fall lasted one month before the Fed stepped in; Winton saw no evidence of a lasting change and slower trend has since done better again.  #mech/slow_reaction _(time-bound view)_
  > if on the other hand you took a month to turn around your positions then you lost all the way down and then you lost again on the way up
  indicator: fast vs slow trend in March 2020 · asset: equities · direction: fast trend gained in a one-month crash · horizon: weeks · conditions: short crash with sharp reversal · testable: partly - one episode · confidence: high
  ^MT177-C09-2
- **Simon Judes** Research has two streams: finding new alpha sources (new ideas or data inputs) and maintaining existing ones by reviewing trend speed, signal construction and volatility models.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > you've got your existing Alpha sources and you need to make sure you're doing them as well as you can and that involves reviewing things like the uh the speed of trend following
  asset: multi · testable: no - process description · confidence: high
  ^MT177-C09-X1

### C10
- **Simon Judes** Switching trend speed with the regime is an implicit call on policy (e.g. Fed intervention), which systematic managers should not make; discretionary macro managers do that.  #mech/research_method
  > you can see that this apparently technical statistical decision about which is the best speed at that moment amounts to just a call on what the FED is going to do and when
  indicator: regime-based speed switching · asset: multi · horizon: weeks · testable: partly - test regime-switching speed rules · confidence: high
  ^MT177-C10-1
- **Simon Judes** Machine learning lacks enough independent events for slow-trading strategies because few examples of crashes exist, but works for faster intraday strategies with many observations.  #mech/research_method
  > machine learning algorithms require a lot of data a lot of training data
  indicator: machine learning · asset: multi · conditions: slow time scales fail, fast time scales work · testable: yes - sample-size analysis · confidence: high
  ^MT177-C10-2
- **Simon Judes** Choosing a faster trend speed mid-selloff looks technical but is actually a bet on when the Fed will step in: right if intervention comes later, wrong if it comes at once, roughly neutral if it never comes.  #mech/new _(added by map cross-check)_
  > this apparently technical statistical decision about which is the best speed at that moment amounts to just a call on what the FED is going to do and when
  indicator: trend speed switch conditional on regime · asset: multi-asset · horizon: weeks · conditions: market falling for about two weeks while long equities · testable: partly - could be tested with regime-conditional speed rules, but argument is scenario logic · confidence: high
  ^MT177-C10-R1

### C11
- **Simon Judes** Slow-horizon research is an observational science (cannot rerun a crash) while fast execution research is experimental and can iterate, so machine learning suits the latter.  #mech/research_method
  > in financial markets if you're talking about what happens on slower time scales how you deal with events like a market crash well you can't just create a market crash on demand
  asset: multi · testable: no - methodology · confidence: high
  ^MT177-C11-1
- **Simon Judes** Parameters are mostly universal across markets but adjusted for transaction cost, market impact, spreads and commissions.  #mech/risk_management
  > we're fairly Universal but they're not not completely there are practical differences often between uh between markets
  indicator: market-specific cost parameters · asset: multi · testable: yes - cost-adjusted parameters · confidence: high
  ^MT177-C11-2
- **Simon Judes** Claiming that a systematic process is fully automated hides that someone must still choose the parameters or the algorithm that chooses them (an infinite regress), so firms should deliberately decide at which level humans take responsibility.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > there's a temptation as a um as a Quant to say everything's automated I didn't do anything the the whole thing's done by a computer that's definitely the wrong thing to do
  indicator: parameter selection process · asset: multi · testable: no - governance principle · confidence: high
  ^MT177-C11-X1

### C12
- **Simon Judes** Humans should own early design decisions such as trend speed and asset allocation (made with analysis) rather than defer to an optimizer, preserving understanding of the portfolio.  #mech/research_method
  > our point of view has generally been that we try to push responsibility on the human fairly early so things like the trend following speed
  indicator: trend speed, asset allocation · asset: multi · conditions: avoid black boxes · testable: no - governance philosophy · confidence: high
  ^MT177-C12-1
- **Simon Judes** Regression-based CTA replication (about 95bp fee) is still a single-manager risk; Winton disagrees that it mitigates manager risk.  #mech/research_method
  > I think they are a single manager if you want to mitigate a single manager risk then obviously the fund of funds approach is the way to go
  indicator: CTA replication · asset: multi · testable: no - opinion · confidence: medium
  **Correction (cross-check):** The fee figure was supplied by the host, not Judes: Judes asked how much replication products charge and the host answered 'just shy of one percent' (85bp plus about 10bp). Judes' own view is only that replication does not mitigate single-manager risk and that fund-of-funds is the real route. → Judes disagrees that regression-based CTA replication mitigates single-manager risk (the replicator is itself a single manager; fund of funds is the way to diversify manager risk); the host noted such products charge just under 1% (about 95bp).
  ^MT177-C12-2

### C13
- **Simon Judes** Sharpe scales with the square root of the effective number of markets given correlations; 50-60 markets might be only 8-10 independent, so adding genuinely different markets adds a lot.  #mech/structural_shift
  > the number that goes into that square root is not the number of markets you trade but the effective number of markets when you've taken account of all of the correlations
  indicator: effective number of markets · asset: multi · direction: Sharpe up with uncorrelated markets · horizon: years · conditions: adding highly correlated markets adds nothing · testable: yes - effective-N from correlations · confidence: high
  ^MT177-C13-1
- **Simon Judes** Alternative markets outperformed major markets over the last decade, including the post-crisis period when mainstream trend struggled; European gas and power gave huge trends (gas up tenfold).  #mech/structural_shift _(time-bound view)_
  > the alternative markets portfolio they did extremely well in that period
  indicator: alternative markets trend portfolio · asset: commodities · direction: alternative market trend returns above major markets · horizon: years · testable: yes - split portfolio returns · confidence: high
  ^MT177-C13-2
- **Niels Kaastrup-Larsen** Comparing managers that trade the 50-60 classical markets with those trading hundreds, the host sees different performance at different times but no huge difference in long-term performance.  #mech/new _(added by map cross-check)_
  > I don't really see a huge difference in long-term performance
  indicator: number of markets traded · asset: futures · horizon: long term · testable: yes - manager performance comparison · confidence: medium
  ^MT177-C13-R2

### C14
- **Simon Judes** Added markets should be truly diversifying (Chinese futures, regional gas, power, freight, marine fuel) rather than equity sector ETFs or developed-market swaps correlated with existing exposure.  #mech/risk_management
  > the markets that you add have to genuinely be alternative and additive
  indicator: correlation of added markets · asset: multi · horizon: years · testable: yes - marginal contribution analysis · confidence: high
  ^MT177-C14-1
- **Simon Judes** Many OTC-traded alternative markets can be cleared on exchange, reducing counterparty risk close to major futures levels.  #mech/risk_management
  > there's still markets that where you can clear your position uh on the exchange so you can um really reduce the counterparty risk
  asset: multi · conditions: not always possible · testable: no - operational · confidence: medium
  ^MT177-C14-2
- **Niels Kaastrup-Larsen** Counterpoint to the more-markets argument: a 50-60 market classical portfolio already includes diversified commodities, and going from 100 to 200 markets mostly adds correlated financial markets unless the extras are genuinely alternative (e.g. Chinese futures).  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > a lot of the additional markets you see often are as you say financial markets that may have correlations to other markets that you may already have
  indicator: number of markets in trend portfolios · asset: multi · direction: Sharpe gain from extra markets small beyond about 100 · conditions: when added markets are correlated financial instruments · testable: yes - Sharpe vs effective number of markets · confidence: medium
  ^MT177-C14-X1
- **Simon Judes** Chinese futures are accessed onshore, through internationalised exchange contracts, via swaps and via the QFI route, an execution method for reaching a diversifying market that others cannot easily trade.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > we trade them now um via the internationalized markets via swaps and by the qfi route you know for our Global Investors
  indicator: Chinese futures access · asset: commodities · testable: no - implementation detail · confidence: high
  ^MT177-C14-X2

### C15
- **Simon Judes** Alternative markets carry extra returns partly because barriers to entry (software, operations, middle office) keep trend followers from extending into them easily.  #mech/risk_premium
  > these markets are by definition have a barrier to entry and that's you know one of the reasons why they have extra offers
  asset: multi · horizon: years · testable: no - structural reason · confidence: medium
  ^MT177-C15-1
- **Simon Judes** Trend allocation size and form (pure, capped beta) depend on the investor's drawdown tolerance and process, so there is no fixed rule; customised programs often vary alternative-market or China exposure rather than trend share.  #mech/risk_management
  > the answers depend on what the investors objectives are what their tolerance is for for drawdowns in particular parts of their book
  indicator: trend allocation size · asset: multi · testable: no - depends on investor · confidence: medium
  ^MT177-C15-2

### C16
- **Simon Judes** Risk is not volatility: in 2017 the VIX was at record lows while valuations were rich, and estimating loss risk is harder than estimating volatility, so use many risk measures besides volatility.  #mech/risk_management
  > there's a strange confusion that affects the CTA industry particularly which is to equate risk with volatility
  indicator: volatility as risk measure · asset: multi · testable: partly - compare vol vs drawdown predictors · confidence: high
  ^MT177-C16-1
- **Simon Judes** Risk management by replaying current positions through all historical environments (worst day or week) and asking whether the loss is acceptable, e.g. the 1990 Gulf War oil jump of 30%.  #mech/risk_management
  > we look at our current positions and we see how they would have performed in all the previous Market environments that we have data for
  indicator: worst day/week of current exposures · asset: multi · testable: yes - historical stress replay · confidence: high
  ^MT177-C16-2

### C17
- **Simon Judes** In early 2023 trend positions were short bonds and long equities, so a risk-off move with bonds rallying and equities falling (disinflationary bad news) is the main scenario risk.  #mech/crowding_positioning _(time-bound view)_
  > most things are short bonds and long equities so obviously the um the situation that's really worrisome is a very classic risk-off move where bonds rally inequities um decline
  indicator: trend positioning, stock-bond correlation · asset: multi · direction: portfolio losses if bonds up, equities down · horizon: months · conditions: modest positive stock-bond correlation currently · testable: partly - positioning-based scenario test · confidence: high
  ^MT177-C17-1
- **Simon Judes** Leverage varies naturally with signal strength and correlations, and risk measures decide whether to hold it inside a band.  #mech/risk_management
  > the way that these strategies operate the leverage naturally fluctuates as the signal strength varies and the correlation between markets varies
  indicator: leverage, correlation · asset: multi · testable: yes - leverage bands · confidence: medium
  ^MT177-C17-2
- **Simon Judes** Stylised stress test of correlation flips: before the 2013 taper tantrum trend was long bonds and long stocks with negative correlation, and a positive correlation scenario looked unacceptable, so risk was cut.  #mech/risk_management
  > you look at things like what if all the correlations change in whatever way would be worse for you
  indicator: stock-bond correlation scenario · asset: multi · testable: yes - correlation-shock scenario · confidence: high
  ^MT177-C17-3
- **Simon Judes** Recently stock-bond correlation has been modestly positive because of the inflation dynamic, so bonds no longer rally reliably in risk-off episodes and trend portfolios that are short bonds and long equities face a different scenario map.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > we've been seeing sort of modest positive correlation between those asset classes and obviously the dynamic with with inflation has made that somewhat different from the usual situation
  indicator: stock-bond correlation · asset: multi · direction: bonds and equities fall together when inflation drives markets · horizon: months · conditions: when inflation, not growth, is the dominant shock · testable: yes - rolling correlation · confidence: medium
  ^MT177-C17-X1
- **Simon Judes** Stress scenarios drawn from history are realistic by definition, whereas 'the worst that could happen' (everything to zero) is not helpful; so Winton replays current positions through past environments.  #mech/new _(added by map cross-check)_
  > by definition anything that has happened is realistic because it did happen
  indicator: worst historical day/week for current positions · asset: multi-asset · testable: yes - replay of positions through history · confidence: high
  ^MT177-C17-R2

### C18
- **Simon Judes** Winton ran lower volatility ahead of the 2013 taper tantrum because of the correlation scenario, which helped that year.  #mech/risk_management _(time-bound view)_
  > we temporarily operated at a lower level of volatility and that really helped us actually in that year
  indicator: bond-stock correlation, volatility target · asset: rates · horizon: months · conditions: before bond/equity correlation turns positive · testable: partly - single year · confidence: high
  ^MT177-C18-1
- **Simon Judes** Capping equity long exposure in a trend program reduces long-term performance in proportion to the cap, helps crisis profile, and is offered as a bespoke option; neither is objectively better.  #mech/risk_management
  > you reduce the long-term performance to some extent depending on how big the you know how significant the cap is
  indicator: equity beta cap in trend · asset: equities · direction: long-run return down, equity beta down · horizon: years · testable: yes - capped vs uncapped backtest · confidence: high
  ^MT177-C18-2
- **Simon Judes** Using multiple trend managers cuts single-manager risk but loses fee netting; the investor chooses the trade-off.  #mech/risk_management
  > you can diversify and you reduce the single manager risk and on the other hand you don't and have fee netting
  indicator: number of trend managers · asset: multi · testable: partly - dispersion data · confidence: medium
  ^MT177-C18-3

### C19
- **Simon Judes** The decline in trend performance correlates strongly with growth in the number of traders, so 0.5 Sharpe is the expectation; long simulations only show underlying markets trend, not future Sharpe for a crowded strategy.  #mech/crowding_positioning
  > it's clear that that correlates very strongly to the growth of people trading the strategy
  indicator: trend Sharpe vs industry assets · asset: multi · direction: Sharpe down as trend AUM up · horizon: years · testable: yes - regress Sharpe on CTA AUM · confidence: medium
  ^MT177-C19-1
- **Simon Judes** Trend following is often contrarian to prevailing fundamental narratives, e.g. oil in 2014 when shale supply was underestimated against a peak-oil view.  #mech/behavioral
  > Trend following is most successful it's because it's actually a contrarian strategy
  indicator: oil price 2014 · asset: commodities · direction: trend short oil · horizon: months · conditions: when fundamental narrative opposes the move · testable: no - narrative-based single case · confidence: high
  ^MT177-C19-2
- **Alan Dunne** Lower trading costs and lower fees are partial offsets to the decline in gross trend Sharpe, so the investor's net outlook is less negative than the 0.5 gross estimate suggests.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > you've got lower trading costs now that you might have had in the past um which would be a positive and fees have probably come down for investors too
  indicator: trend net Sharpe after costs and fees · asset: multi · direction: net returns less depressed than gross · horizon: years · testable: partly - cost series available · confidence: low
  ^MT177-C19-X1
- **Simon Judes** The belief Winton most disagrees with about trend following is that it is a dumb herding strategy in which people follow each other.  #mech/new _(added by map cross-check)_
  > this idea that Trend following is a kind of dumb strategy that is just people following each other
  indicator: none · asset: multi-asset · testable: no - opinion · confidence: high
  ^MT177-C19-R1

### C20
- **Simon Judes** Trends extend in time because a prevailing narrative says the market must go the other way, as in German yields that kept falling into negative territory against the belief they could never go below zero.  #mech/slow_reaction
  > for that to be a trend the movement has to be extended in time and often it can be extended because it is contrarian because there's a narrative
  indicator: German bond yields 2014-2016 · asset: rates · direction: long bonds · horizon: months · conditions: when a widespread belief rejects the move · testable: no - historical examples · confidence: high
  ^MT177-C20-1

