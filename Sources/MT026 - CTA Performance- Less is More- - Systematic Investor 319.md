---
source_id: MT026
title: "CTA Performance- Less is More- - Systematic Investor 319"
date: 2024-11-01
channel: "Top Traders Unplugged"
url: 
words: 16236
claims: 85
added_by_crosscheck: 19
corrections: 1
crosscheck: "opus cross-check"
speakers: ["Rob Carver (systematic trader and author)", "Niels Kaastrup-Larsen (host, hedge fund manager)"]
tags: [source, layer0]
---
# CTA Performance- Less is More- - Systematic Investor 319

**Speakers:** Rob Carver (systematic trader and author); Niels Kaastrup-Larsen (host, hedge fund manager)

**Summary:** Top Traders Unplugged Systematic Investor 319: Rob Carver and Niels discuss CTA myths, bond/fiscal views, execution and rebalancing practice, and the diversification and replication papers. Conclusions: CTAs are too small to move markets; avoid selecting strategies on noisy backtests; fewer independent bets than markets; return-based CTA replication is flawed.

**Approach:** trend following, CTA replication, position sizing and cost-aware rebalancing, diversification

**Cross-check completeness estimate of first read:** 0.82 - first reader caught all main arguments (CTA blame, replication, buffering, correlations, factors); missed secondary reasoning steps, numbers (index YTD, correlation levels) and several caveats.

## Argument map

**Episode thesis:** Rob Carver argues that systematic evidence beats narrative: CTAs are too small to cause large price moves, backtest or one-month rankings of instruments, strategies or horizons are mostly noise and should not drive allocation, and adding hundreds of markets mainly adds exposure to a handful of latent macro factors (so more markets are different, not clearly better). He treats return-based CTA replication as flawed (in-sample, backward-looking, cannot give manager diversification) while position-level and simple bottom-up replication are valid, and he describes a low-maintenance, cost-aware execution practice (delay tests, dynamic optimisation, buffers, short-window instrument correlations). Host Niels Kaastrup-Larsen adds the October 2024 performance context, Paul Tudor Jones's fiscal warning that Carver rebuts with the Japan analogy, and the point that institutional allocators who select managers cannot rationally settle for a replicator.

### Rob Carver (systematic futures trader (about 300-instrument portfolio, ex-AHL fixed income), author of systematic trading books and blog; guest)
Fingerprint: #approach/trend_following #approach/research_robustness_overfitting #approach/costs_execution #approach/position_sizing_vol_target #approach/diversification_risk_parity #approach/replication_indexing #approach/volatility_options #approach/regime_detection
_Speaker note: Clear first-person speaker. He trades his own retail account at about 25% annual volatility target. He calls out his 'pet hates' (blaming CTAs, short samples, return-based replication)._

**Worldview premises**
- CTAs are too small relative to market size to cause big price moves such as oil or equity volatility; vol-targeted trend followers shrink positions as volatility expands, so rallies like cocoa 2024 coincide with CTA selling. _[empirical, stated; support: simple arithmetic on AUM and leverage; he runs a model of positions in oil and finds a small short; cocoa position cut]_ ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C01-1|C01-1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C02-1|C02-1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C02-3|C02-3]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C02-X1|C02-X1]])
- A single month of results says nothing about the right trend horizon. Short- and long-term trend followers are only moderately correlated and win in different path types; backtests need decades and many cycles. Only high-frequency strategies get enough independent observations in a month. _[theoretical, stated; support: statistical argument; his own practice (a one-month backtest would get an analyst fired)]_ ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C03-1|C03-1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C03-2|C03-2]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C03-3|C03-3]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C03-X1|C03-X1]])
- Selecting instruments or strategies by backtested performance is mostly fitting noise: when error bars are added, all 100 instruments' trend results overlap. Allocation should therefore ignore performance, and simple allocation works as well as sophisticated optimisation that overfits. _[empirical, stated; support: his chart of 100 ranked instruments with error bars (in his books); decades of backtests and 10 years live]_ ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C14-1|C14-1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C13-2|C13-2]])
- Trend following gives a long-option-like payoff (gains when markets trend, small losses whipsawing in ranges) without paying the volatility risk premium that explicit option buying pays. _[theoretical, stated; support: payoff reasoning; volatility risk premium: implied exceeds realised on average]_ ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C08-3|C08-3]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C09-1|C09-1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C09-2|C09-2]])
- A slow trend system is insensitive to intraday and overnight price movement between signal and execution because a small change in the last price barely changes the desired position. _[empirical, stated; support: delayed-fill test in backtests (if Sharpe change is under about 0.01, execution timing does not matter)]_ ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C07-1|C07-1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C07-2|C07-2]])
- CTA returns are driven by a few latent macro factors (four or five) that change over time (commodities, 2008 risk-off), so a 300-market portfolio really holds roughly 16-25 independent bets, of which only about half a dozen matter at any time; extra alternative markets add only one new factor. _[theoretical, stated; support: Yavin's article; his own observation that backtested performance rises about four to five times with more markets]_ ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C15-3|C15-3]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C16-1|C16-1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C16-2|C16-2]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C16-X1|C16-X1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C16-X2|C16-X2]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C19-3|C19-3]])
- Positive skew in a large trend portfolio comes from exposure to the underlying macro factors, because idiosyncratic left and right tails wash out; yet correlation understates diversification in trend following because returns are non-linear, so benefits continue beyond where correlations say they level off. _[theoretical, stated; support: argument built on the Kaminski skew discussion and his own research; no numbers]_ ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C17-2|C17-2]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C17-4|C17-4]])
- A country like the US that prints its own reserve currency can carry larger debt, as Japan did, and ageing populations raise bond demand, so a Minsky moment in US bonds is unlikely; fundamental short calls in bonds are widow-maker trades. _[experience, stated; support: Japanese government bonds 1990s-2013 (long position held about 3 years until a gap down in February 2013); personal AHL experience; he says he could be wrong]_ ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C05-2|C05-2]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C05-3|C05-3]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C05-4|C05-4]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C05-5|C05-5]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C05-R1|C05-R1]])
- Correlations between instrument returns jump to extreme levels in crises (flight to safety, simultaneous deleveraging); correlations between trading-strategy returns are lower and more stable. _[empirical, stated; support: Bund versus US 10-year about 0.5 on average, Bund versus Schatz about 0.9; US/German rate cycle alignment]_ ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C12-1|C12-1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C12-3|C12-3]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C11-X1|C11-X1]])
- Absent performance information, equal weights beat market-cap weights in long-only portfolios, and an allocator could hold a vanilla low-cost CTA as core beta plus a lower-correlation CTA for alpha; low-cost beta products cannibalise flagship funds because much of a flagship's return is the same beta. _[theoretical, stated; support: argument by analogy with equities and with past equity hedge-fund beta, plus the 15-years-ago AHL beta-fund episode]_ ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C15-2|C15-2]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C17-3|C17-3]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C17-X1|C17-X1]])
- Investors who cannot afford 10-15 CTA tickets face single-manager dispersion to the index by construction, so tracking error against the index is not unique to replicators; the choice depends on whether they believe few factors drive CTAs. _[institutional, stated; support: ticket-size arithmetic (5-10% CTA allocation split 10 ways is about 1% each)]_ ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C22-X1|C22-X1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C23-X1|C23-X1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C23-1|C23-1]])

**Chain: Why CTAs do not move markets, and the one case where they could**
1. Volatility expands in a market (cocoa 2024) → Vol-targeted trend followers cut position size, selling into the rally: position size is inverse to volatility ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C02-3|C02-3]])
2. A long smooth trend (low volatility) → Large positions and high leverage: volatility targeting sizes up in low-volatility trends ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C02-2|C02-2]])
3. Sharp reversal after such a smooth trend → CTAs deleverage and could amplify the move: stops and signal flips force selling at once ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C02-2|C02-2]])
- Evidence: Oil 2024: the price fell from 87 to 65 and models went long early, now flat to slightly short; his own crude position is a small short.
- Fails when: Illiquid speculative pockets where CTA size is large relative to commercial activity.

**Chain: Why trend following should not be replaced by explicit option strategies**
1. Explicit option buying → Pays the volatility risk premium (implied volatility above realised on average because buyers pay for insurance and certainty): insurance demand ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C09-1|C09-1]])
2. Call option delta rises with price → Automatic pyramiding like a trend follower: increasing exposure as price rises ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C09-2|C09-2]])
3. Trade futures or options depending on implied versus forecast volatility, and also sell options → A system short volatility with trend's positive skew and in theory a higher Sharpe than futures-only trend: collects the volatility premium and buys optionality when cheap ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C09-3|C09-3]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C09-4|C09-4]])
- Evidence: Reasoning only; no backtest quoted.
- Fails when: Operational cost: options need much more implementation, infrastructure and data work.

**Chain: Cost-aware rebalancing**
1. Zero transaction costs → Always rebalance to target: no downside to trading ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C10-1|C10-1]])
2. Higher costs → Wider tolerance around the target position (buffer wider for expensive instruments): moving costs more than the deviation is worth ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C10-1|C10-1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C11-1|C11-1]])
3. Whole-portfolio dynamic optimisation versus the zero-cost ideal → Trade only when worth the cost, in the cheapest correlated market, leaving expensive positions alone: cost-aware at portfolio level ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C08-1|C08-1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C10-2|C10-2]])
- Evidence: His own practice and costs: about 1% a year as retail at a 25% risk target (about 60bp for an institution).
- Fails when: The fixed 10% buffer is a simplification suited to retail single-lot trades.

**Chain: Why more markets give fewer independent bets**
1. Add more instruments to a portfolio → Less idiosyncratic risk and more exposure to common factors: idiosyncratic risk diversifies away ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C15-1|C15-1]])
2. Backtested performance rises four to five times with more markets → About 16-25 independent bets, of which half a dozen matter at any time: gain scales like the square root of independent bets ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C16-2|C16-2]])
3. 300 markets → Idiosyncratic markets like cocoa contribute little; macro trends drive performance: each small position barely changes results ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C16-1|C16-1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C17-2|C17-2]])
- Evidence: Yavin's article, his own backtest scaling, Niels's performance-database observation that 300-400-market CTAs do not beat <=100-market CTAs.
- Fails when: Non-linear returns mean correlation understates diversification, so Carver himself keeps 300 markets.

**Chain: Why return-based replication fails**
1. CTA positions change sign over months → Regression must use short windows to capture current positions: a 6-12 month regression would show positions that are no longer held ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C21-1|C21-1]])
2. Short windows with about 30 futures as regressors → Regression becomes infeasible, so lasso is used to pick about five: too few data points for too many regressors ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C21-1|C21-1]])
3. Results measured in-sample → Overstated tracking; out-of-sample refits always do worse: back-test overfitting ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C21-2|C21-2]])
4. Replicating an index backward-looking from returns → Cannot reproduce the diversification of the individual managers: no information on forward positions ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C22-3|C22-3]])
- Evidence: His reading of the New Found Research paper (random pseudo-CTA universe, about 30 factors, Sharpe-style cost-savings ratio near one at the ceiling and 0.23, about 150bp, for BTOP50).
- Fails when: Position-level and simple bottom-up replication (about 30 liquid futures across asset classes) do work and he endorses them; the factor spread must be varied (30 US bond futures would fail).

**Chain: Why trend followers avoid the widow-maker trade in bonds**
1. Fundamental case: deficit, debt and demographics imply higher yields → Short JGB trade loses for decades: prices kept rising and yields stayed near zero ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C05-2|C05-2]])
2. Trend followers follow price → Long JGBs for about three years until a gap down in February 2013: no fundamental view required ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C05-3|C05-3]])
- Evidence: Personal recollection from running the AHL fixed income book.
- Fails when: Not stated; he notes the position ended with a sharp gap.

**Decision process**
- [execution] Backtest on daily data and test the effect of delaying fills by one or two days; if the Sharpe change exceeds about 0.01 the system needs hourly data or slower trading; otherwise ignore intraday and overnight moves. He trades off the previous close and does not rerun the optimiser hourly.. Why: slow systems are insensitive to execution timing ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C07-1|C07-1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C07-2|C07-2]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C08-X1|C08-X1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C08-1|C08-1]])
- [execution] Dynamic optimisation versus the zero-cost ideal portfolio; the older version used a buffer of 10% of a standard vol-adjusted position unit and skipped trades below it.. Why: avoid trades not worth their cost; fixed buffer is a simplification ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C08-2|C08-2]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C08-1|C08-1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C11-1|C11-1]])
- [risk] Estimate instrument return correlations (for portfolio risk) with an exponentially weighted window of about 6 months; estimate correlations between trading strategies over 10+ years covering more than one cycle.. Why: balances responsiveness against noise; exponential weighting avoids sharp jumps when spikes roll off; strategy correlations are stable ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C11-2|C11-2]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C12-2|C12-2]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C12-3|C12-3]])
- [portfolio] Do not dynamically reallocate capital between strategies or instruments on past performance; use simple allocation.. Why: differences are rarely statistically significant over decades of backtest and 10 years live; sophisticated optimisation overfits ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C13-2|C13-2]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C14-1|C14-1]])
- [universe] Hold over 300 futures markets in the model portfolio but trade about 20 instruments that replicate it (position-level replication).. Why: small account cannot trade 300; keeps diversification at lower cost ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C18-1|C18-1]])
- [research] Test on randomly generated data (pseudo-CTAs and pseudo index) to avoid overfitting to the last 30 years of real trends; test replication out-of-sample by refitting weekly and holding for the next week.. Why: real data may be a fluke; out-of-sample always does worse than in-sample ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C19-2|C19-2]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C21-2|C21-2]])
- [other] Automate monitoring: a status web page refreshed every 10 minutes and nightly emails; automatic checks for missing prices, missing daily positions and broker-versus-system position differences.. Why: minimise human supervision ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C12-4|C12-4]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C13-1|C13-1]])

**Evidence style:** Mostly first principles and statistics (error bars, in- versus out-of-sample, sampling), simple arithmetic, simulation with random data, and his own trading experience; openly flags uncertainty ('I could be wrong').

**Views at the time**
- (late October 2024 (recorded Thursday; upload 2024-11-01)) Oil has not been a good market for CTAs in 2024; models went long early and are now roughly flat or slightly short; he has a small short in crude.. Reasoning: price fell from 87 to 65 and is now about 72 ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C02-1|C02-1]])
- (October 2024) His trend model is short German Bunds with no other fixed-income position, in line with Paul Tudor Jones's direction but not the US.. Reasoning: model output ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C06-2|C06-2]])
- (October 2024) The US will behave like Japan rather than face a Minsky moment because it prints its own reserve currency; ageing populations support bond demand.. Reasoning: Japan analogy and demographics; acknowledges possible error ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C05-4|C05-4]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C05-5|C05-5]])
- (October 2024) Return-based CTA replication is a bad idea; a cheap bottom-up ETF of about 30 markets at about 50bp is reasonable if one believes few factors drive CTAs.. Reasoning: in-sample bias, lack of manager diversification ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C23-1|C23-1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C22-1|C22-1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C20-2|C20-2]])

### Niels Kaastrup-Larsen (host, veteran hedge fund manager and trend follower)
Fingerprint: #approach/trend_following #approach/manager_selection_allocation #approach/replication_indexing #approach/policy_reaction_central_banks #approach/fiscal_dominance #approach/behavioral_sentiment #approach/diversification_risk_parity
_Speaker note: Reports Paul Tudor Jones's views and index data; his own opinions on market count, replication and allocators are stated explicitly. Ledger correction applied to C20-1 (the 'Sharpe near one' ceiling is the paper's figure presented by Rob)._

**Worldview premises**
- Past instrument performance is a poor guide to future contribution: cocoa made no money for 15 years then the most in 18 months. _[experience, stated; support: cocoa anecdote]_ ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C14-2|C14-2]])
- More markets are different, not necessarily better: adding markets also adds chances of ranging markets, and performance databases show no evidence that 300-400-market CTAs beat those trading about 100 or fewer. _[empirical, stated; support: his reading of performance databases (no numbers)]_ ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C16-3|C16-3]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C17-1|C17-1]])
- Tracking error is not the right metric for CTA replication because managers do not target a benchmark; live replicators show lower correlation than expected on daily data, and the paper's cost inputs look too high. _[experience, stated; support: recollection of paper and live replication products]_ ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C22-2|C22-2]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C20-1|C20-1]])
- Institutional allocators who select managers must believe in persistent manager skill, so settling for a replicator contradicts their role; replication ETFs and manager ETFs are good for smaller investors. _[behavioural, stated; support: argument from role of allocators]_ ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C23-2|C23-2]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C23-X2|C23-X2]])
- Strategies can rebound after long drawdowns (Paul Tudor Jones favoured trend after four to five weak years and a strong run followed). _[experience, stated; support: anecdote]_ ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C06-X1|C06-X1]])

**Chain: Why policy easing coincided with a bond selloff in autumn 2024**
1. Fed cut 50bp (more than expected), ECB cut to 3.25% (first back-to-back cut in 13 years) → Long-term yields rose instead of falling: implied by Niels's account: fiscal and inflation concerns outweighed easing (not argued explicitly) ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C04-1|C04-1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C04-X1|C04-X1]])
2. Rising yields → Trend followers' fixed income positions lost money even as long exposure was already shrinking: a reversal costs money while the trend signal is decaying ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C06-4|C06-4]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C06-X2|C06-X2]])
- Evidence: Index numbers for October 2024.
- Fails when: Causal explanation is implicit, not stated.

**Decision process**
- [portfolio] Track the trend barometer as a monthly gauge of expected trend performance (reading 32 = weak).. Why: his own indicator; weak reading suggests trend followers will lose money this month ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C06-3|C06-3]])

**Evidence style:** Cites performance data, anecdotes (cocoa, Paul Tudor Jones), investor conversations and databases rather than formal tests; says outright when he cannot back a claim academically.

**Views at the time**
- (2024-10-29 close (recording Thursday; data as of Tuesday)) The October 2024 bond selloff began when the Fed cut 50bp and long yields rose; trend followers lost mainly in fixed income, equity corrections and some currencies, while gold and silver were the only strong liquid markets; SocGen Trend about -3% for the month.. Reasoning: index data and attribution ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C04-1|C04-1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C06-4|C06-4]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C06-X3|C06-X3]])
- (2024-10 (CNBC interview reported by Niels)) Paul Tudor Jones expects a Minsky moment where bond vigilantes reject US fiscal plans (US debt $35tn, receipts about $5tn, deficit about $2tn, path to 200% of GDP in 30 years) and would own no fixed income and short the back end.. Reasoning: fiscal arithmetic cited by Jones ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C04-2|C04-2]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C04-3|C04-3]])
- (2024-10) Investor sentiment in late 2024 strongly favoured buying fixed income at 4-5% yields, the opposite of Jones's concern.. Reasoning: conversations with investors ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C06-1|C06-1]])
- (2024-10) Trend can profit from a sustained bond bear market, as in 2022.. Reasoning: 2022 experience ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C05-1|C05-1]])

### Disagreements
- **Whether more markets is better**: Rob Carver: Keeps over 300 markets: backtested performance rises four to five times with more markets, and non-linear benefits continue even where correlations say they level off; yet accepts that only about half a dozen independent bets matter at once. ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C16-2|C16-2]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C17-4|C17-4]]); Niels Kaastrup-Larsen: 50-100 markets is enough; adding markets is different but not clearly better and adds chances of ranging markets; no database evidence that 300-400 markets do better. ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C16-3|C16-3]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C17-1|C17-1]])
- **Whether Paul Tudor Jones's bond Minsky-moment warning is right**: Niels Kaastrup-Larsen (reporting Paul Tudor Jones): US debt dynamics risk a Minsky moment; own no fixed income and short the back end. ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C04-2|C04-2]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C04-3|C04-3]]); Rob Carver: The US is more likely to behave like Japan (can print the reserve currency, ageing raises bond demand); he does not want to make discretionary calls, though his model is short Bunds. ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C05-4|C05-4]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C05-5|C05-5]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C06-2|C06-2]])
- **Whether replication savings and the paper's cost inputs are reasonable**: Niels Kaastrup-Larsen: The cost inputs (200bp management, 110bp performance, 275bp unnetted) look too high and tracking error is the wrong metric. ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C20-1|C20-1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C22-2|C22-2]]); Rob Carver: The paper's figure is a ceiling; realistic savings are about 100-200bp minus the replicator's fees, and the paper's own BTOP50 result implies a 0.23 ratio. ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C20-2|C20-2]])

### Gaps and conflicts
- Carver warns against short samples and noisy rankings, yet his claim about August 2024 and the Risk magazine article rests on his reading of a graph he had not studied in detail; no data shown for his claim that one month is meaningless beyond statistical logic. ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C03-3|C03-3]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C03-X1|C03-X1]])
- Carver argues about 16-25 independent bets (from a fourfold to fivefold performance rise) but still holds 300 markets, partly because of non-linear diversification; the claim that correlation understates diversification is stated as his research result without numbers. ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C16-2|C16-2]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C17-4|C17-4]])
- The Sharpe-style 'ceiling' ratio near one and the later 0.23 (about 150bp) are given from memory; some paper details (daily versus monthly returns, tracking error of 6-8%) are uncertain in the speakers' recall. ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C20-1|C20-1]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C20-2|C20-2]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C22-2|C22-2]])
- Paul Tudor Jones's fiscal arithmetic is relayed second-hand from one clip and the 200% of GDP path is not independently checked. ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C04-2|C04-2]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C04-3|C04-3]])
- Niels's argument that allocators must believe in manager skill assumes persistent skill exists, which neither speaker tests; Carver's own premise that selection on past performance is noise sits uneasily with it. ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C23-2|C23-2]], [[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C14-1|C14-1]])
- Carver says options could raise the Sharpe ratio 'in theory' but gives no empirical test. ([[MT026 - CTA Performance- Less is More- - Systematic Investor 319#^MT026-C09-4|C09-4]])

### Forward-looking inputs (reader synthesis)
(reader) Carver names few forward-looking inputs because he distrusts forecasting: price trend and volatility (for positions), implied versus forecast volatility (for options versus futures), correlation regimes (rate-cycle alignment between US and Germany, flight-to-safety spikes), and the dispersion of CTA returns as a sign of how many macro factors dominate a year. Niels uses the trend barometer (32 in late October 2024) and sentiment (investor appetite for 4-5% bond yields). Horizons are months for trend, six months for correlations and 10+ years for strategy correlations and backtest evidence.

### Reader inferences (not stated by the speakers)
- (reader) Carver's position implies that the best evidence for any CTA design choice (horizon, instrument list, strategy weights) needs decades of data; month-level performance should not trigger changes, which also explains his hostility to commentary built on a single month.
- (reader) His replication views separate three ideas: position-level (valid), simple bottom-up (valid for small investors) and return-based (flawed). The deciding factor is whether the replicator knows forward positions, not how cheap it is.
- (reader) The 'few latent factors' premise cuts both ways: it supports cheap bottom-up replication and shrinks the benefit of extra markets, but Carver and Niels still disagree on market count, showing the premise alone does not fix the portfolio design.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | intro; CTAs too small to move markets (pet hate) |
| C02 | 3 | oil and cocoa CTA positioning; vol targeting reduces size when vol expands |
| C03 | 3 | short vs long term trend followers; one month is not evidence |
| C04 | 3 | Fed cut and bond selloff; Paul Tudor Jones fiscal view |
| C05 | 5 | JGB widow maker; Rob's counterargument on US debt |
| C06 | 4 | sentiment on bonds; Rob short Bunds; Oct 2024 CTA performance and trend barometer |
| C07 | 2 | daily data, delayed-fill test, intraday and gap risk |
| C08 | 3 | dynamic optimisation, buffer, options vs trend following |
| C09 | 4 | volatility risk premium, calls vs futures, combined skew |
| C10 | 3 | rebalancing and transaction costs |
| C11 | 2 | position inertia buffer, correlation window for instrument returns |
| C12 | 4 | exponential weighting, strategy-level correlation window |
| C13 | 2 | system monitoring; no performance-based strategy allocation |
| C14 | 2 | do not select strategies on backtests; error bars; Yavin article intro |
| C15 | 3 | Yavin factor argument, equal weights, CTA factors |
| C16 | 3 | effective bets, performance scaling with markets, 300 market debate |
| C17 | 4 | skew from factors, core-satellite allocation, non-linear diversification |
| C18 | 2 | New Found replication paper: three replication methods |
| C19 | 4 | random data testing, dispersion, 30 futures sufficient |
| C20 | 2 | replication savings and cost numbers |
| C21 | 2 | return-based regression window, lasso, in-sample critique |
| C22 | 3 | simple ETF alternative, tracking error, return-only replication flaw |
| C23 | 2 | manager selection options and skill; wrap-up |
| C24 | 0 | nothing actionable: outro |

## Claims

### C01
- **Rob Carver** CTAs are too small relative to market size to be the cause of big price moves such as oil volatility, because their AUM and leverage are limited, except possibly in illiquid speculative pockets.  #mech/crowding_positioning
  > we're actually quite quite small players and even even with a bit of leverage which obviously we use, we're not really big enough to to move things in in in markets
  asset: multi · testable: partly - could be tested by comparing estimated CTA position sizes with market volume · confidence: high
  ^MT026-C01-1

### C02
- **Rob Carver** Oil was a poor market for CTAs in 2024 because trend models went long early, were disappointed, and are now roughly flat or slightly short after the price fell from 87 to 65.  #mech/slow_reaction _(time-bound view)_
  > And actually I suspect that oil hasn't been a very good market for CTAs this year
  indicator: oil price trend (high $87 in April, $65, $72 recently) · asset: commodities · direction: trend followers flat/slightly short crude · horizon: months · testable: partly - CTA oil P&L could be checked in index data · confidence: medium
  ^MT026-C02-1
- **Rob Carver** Vol-targeted trend followers hold their largest positions in smooth, low-volatility trends, so a sharp reversal after such a trend is the case where CTA deleveraging could amplify a move.  #mech/crowding_positioning
  > you can sort of plausibly say if there'd been a really long smooth trend, which you'd expect CTAs to buy into with big positions because the trend is smooth, therefore volatility is low, therefore leverage should be high
  indicator: realized volatility, position size · asset: multi · direction: large positions build in smooth trends · conditions: matters only after a long smooth trend that sharply reverses; not the case in oil · testable: partly - position estimates from vol-scaled signals are replicable · confidence: medium
  ^MT026-C02-2
- **Niels Kaastrup-Larsen** Volatility-targeted trend followers cut position size as volatility expands, so a big rally such as cocoa in 2024 is accompanied by CTA selling of position size, the opposite of the claim that CTAs pushed the price up.  #mech/risk_management _(time-bound view)_
  > Well, in fact, we've sold about 90% of our cocoa into that rally because as you mentioned, when vol expands, we contract our position size
  indicator: cocoa price and volatility · asset: commodities · direction: position size falls when vol rises · horizon: months · testable: yes - inverse-vol scaling is mechanical · confidence: high
  ^MT026-C02-3
- **Rob Carver** CTA positioning in a market can be estimated by running a simple momentum plus volatility-scaled sizing model, which is how one can check claims that CTAs hold big positions (e.g. in oil).  #mech/crowding_positioning _(added by opus cross-check)_
  > if you do any kind of basic replication of position sizing and and behavior, and you you got to have understanding of how things like momentum and volatility drive our positioning.
  indicator: estimated CTA position from a simple trend + vol-targeting model · asset: multi · horizon: weeks · testable: yes - simple trend model positions can be computed from prices · confidence: high
  ^MT026-C02-X1

### C03
- **Rob Carver** Short-term and long-term trend followers have moderately positive but not high correlation because they pick up trends at different time scales.  #mech/cycle_persistence
  > you would expect the correlation between short-term trend followers and long-term trend trend followers to be probably not zero or negative, but it wouldn't it's not going to be especially especially high
  indicator: return correlation of short-term vs long-term trend CTA indices · asset: multi · horizon: months · testable: yes - compute correlation of short vs long lookback trend returns · confidence: medium
  ^MT026-C03-1
- **Rob Carver** Short-term trend followers do well when trends occur over short periods, which whipsaws long-term followers, while long-term followers do well in slow trends with jagged spikes that whipsaw short-term followers.  #mech/cycle_persistence
  > a short-term trend follower will be whipsawed because the market's kind of moving up slowly but in a series of sort of jagged pipes spikes
  indicator: trend lookback length · asset: multi · direction: short-term trend wins in short bursts, long-term wins in slow drift · horizon: weeks · conditions: depends on the time scale of the prevailing trend · testable: partly - regime classification of trend scale needed · confidence: medium
  ^MT026-C03-2
- **Rob Carver** One month of results (August 2024 short-term CTAs beating long-term) is not evidence for choosing a trend horizon; backtests need many years and economic cycles to avoid picking up temporary events.  #mech/research_method
  > if if I had somebody working for me and who came up with a backtest that was one month long, they'd be out the door
  asset: multi · horizon: years · testable: yes - sample-size and significance can be computed · confidence: high
  ^MT026-C03-3
- **Rob Carver** One month of data can only be statistically meaningful for high-frequency strategies, because only they generate enough independent observations in a month; for slow strategies it is noise.  #mech/research_method _(added by opus cross-check)_
  > the only place that might make sense is in the high frequency space where you can get enough data points with a month data to get a statistically significant result.
  asset: multi · conditions: holds for slow strategies; exception for high-frequency trading · testable: partly - follows from sample-size statistics · confidence: high
  ^MT026-C03-X1

### C04
- **Niels Kaastrup-Larsen** In autumn 2024 the bond selloff began when the Fed cut 50 bp, which led to higher long-term yields rather than lower, hurting trend followers' fixed-income positions.  #mech/policy_reaction _(time-bound view)_
  > it pretty much started when the Fed cut 50 basis points, and which as was actually probably more than most people would have expected
  indicator: US 10y yield after Fed 50bp cut (Sept 2024) · asset: rates · direction: long-end yields rose after a larger-than-expected cut · horizon: weeks · testable: partly - single episode · confidence: medium
  ^MT026-C04-1
- **Niels Kaastrup-Larsen** Paul Tudor Jones expects a point where bond vigilantes reject US fiscal plans, a Minsky moment, and said he would own no fixed income and would short the back end.  #mech/fiscal_debt _(time-bound view)_
  > may start to vote with their feet and give a vote of no confidence, not so much to the candidate, but actually to the budget plans that either of them really stands for
  indicator: US long-end Treasury yields, deficit path · asset: rates · direction: short long-end Treasuries · horizon: years · conditions: requires loss of confidence in US budget path · testable: no - timing of a loss-of-confidence event is not testable · confidence: high
  ^MT026-C04-2
- **Niels Kaastrup-Larsen** Paul Tudor Jones cites US debt of $35tn, tax receipts of about $5tn and a deficit of about $2tn a year, with a path toward 200% of GDP in 30 years, as the basis of his fiscal-risk argument.  #mech/fiscal_debt _(time-bound view)_
  > Right now, the US debt, according to this interview, is $35 trillion. But the income from tax receipts is only 5 trillion per year.
  indicator: US federal debt $35tn, receipts $5tn, deficit $2tn · asset: rates · horizon: years · testable: partly - data are public but the inference is a projection · confidence: medium
  ^MT026-C04-3
- **Niels Kaastrup-Larsen** In October 2024 the ECB cut to 3.25%, its first back-to-back cut in 13 years, while long bond yields were rising after the Fed's 50 bp cut, i.e. policy easing coincided with a bond selloff.  #mech/policy_reaction _(added by opus cross-check, time-bound view)_
  > ECB did it earlier this month as well. They're down to 3 and 1/4, I think, now. And it was the first back-to-back cut in 13 years
  indicator: ECB deposit rate; consecutive cuts · asset: rates · direction: policy rates down while long yields up · horizon: months · testable: partly - data point, no rule · confidence: medium
  ^MT026-C04-X1
- **Rob Carver** Carver notes that AI-labelled CTAs are now a tracked category in the dashboard in the Risk article and expects many to jump on that bandwagon, another of his pet hates.  #mech/new _(added by map cross-check, time-bound view)_
  > the AI CTAs are now being tracked on on this dashboard and and uh no doubt we will see lots of people jumping on that particular bandwagon
  indicator: AI CTA category · asset: multi · direction: n/a · horizon: n/a · conditions: none stated · testable: no · confidence: medium
  ^MT026-C04-R2

### C05
- **Niels Kaastrup-Larsen** Trend following can profit from a sustained bond bear market, as it did in 2022, unlike most strategies.  #mech/cycle_persistence
  > not that many strategies are able to profit from a long-term bear market in in bonds, but but trend following has actually proven that it can very recently
  indicator: trend-following returns in bonds · asset: rates · direction: short bonds when trend is down · horizon: years · testable: yes - CTA bond P&L in 2022 is observable · confidence: medium
  ^MT026-C05-1
- **Rob Carver** Shorting Japanese government bonds on deficit and demographic arguments was a widow-maker trade for decades because prices kept rising and yields stayed near zero.  #mech/overshoot
  > And you know one of the the great widow maker trades last 30 years was was shorting Japanese government bonds.
  indicator: JGB price trend · asset: rates · direction: long JGBs for trend followers, fundamental shorts lost · horizon: years · conditions: fundamental debt arguments can fail for decades in a country with its own currency · testable: partly - one historical episode · confidence: high
  ^MT026-C05-2
- **Rob Carver** Trend followers avoid widow-maker fundamental calls by following price, which let them stay long JGBs for about three years until a sharp gap down in February 2013 closed the position.  #mech/cycle_persistence
  > Um and one of the nice things, of course, about being you know, being trend followers is we could ignore all of that.
  indicator: JGB trend signal · asset: rates · direction: long JGBs while trend up; exit on gap down · horizon: years · testable: yes - JGB trend history is testable · confidence: high
  ^MT026-C05-3
- **Rob Carver** Rob Carver expects the US to behave like Japan rather than face a Minsky moment because it prints its own reserve currency and can carry larger debt.  #mech/fiscal_debt
  > there's no reason why the US as a country can't support quite a large federal debt
  asset: rates · direction: no forced US bond collapse · horizon: years · conditions: holds while the dollar remains the reserve currency and demand for US assets persists · testable: no - a regime view, not a rule · confidence: low
  ^MT026-C05-4
- **Rob Carver** Ageing populations shift savings into fixed income, increasing bond demand and keeping yields lower for longer.  #mech/structural_shift
  > one of the things that happens as you get an aging society is people do move more of their investments into fixed income
  indicator: demographics · asset: rates · direction: bond yields lower · horizon: years · testable: partly - demographics and yield link is testable but confounded · confidence: medium
  ^MT026-C05-5
- **Rob Carver** Carver says he does not want to make discretionary calls on the US bond market and regards it as a very difficult business, which is why he treats Paul Tudor Jones's call with caution and relies on his trend model.  #mech/new _(added by map cross-check)_
  > I'm glad I'm not in a position where I'm expected to make discretionary calls on the US bond market
  indicator: discretionary US bond call · asset: bonds · direction: n/a · horizon: n/a · conditions: none stated · testable: no · confidence: high
  ^MT026-C05-R1

### C06
- **Niels Kaastrup-Larsen** Investor sentiment in late 2024 was strongly in favour of buying fixed income at 4 to 5% yields, which is opposite to Paul Tudor Jones's bearish concern.  #mech/behavioral _(time-bound view)_
  > People are so excited and and they want to essentially just buy fixed income because now they can get four or five percent
  asset: rates · direction: investors buying bonds for yield · horizon: months · testable: no - anecdotal sentiment · confidence: medium
  ^MT026-C06-1
- **Rob Carver** Rob Carver's trend model was short German Bunds in October 2024 with no other fixed-income position, in line with Paul Tudor Jones's direction though not the US.  #mech/cycle_persistence _(time-bound view)_
  > I am short bunds.
  indicator: Bund trend signal · asset: rates · direction: short Bunds · horizon: months · testable: partly - a single position snapshot · confidence: medium
  ^MT026-C06-2
- **Niels Kaastrup-Larsen** Niels's trend barometer at 32 is on the weak side and suggests trend followers will lose money this month.  #mech/cycle_persistence _(time-bound view)_
  > My own trend barometer finished at 32 last night
  indicator: Trend Barometer (Top Traders Unplugged) = 32 · asset: multi · direction: trend followers lose money when barometer is low · horizon: weeks · conditions: barometer measures how favourable current conditions are to trend following · testable: yes - barometer vs monthly CTA index return can be regressed · confidence: medium
  ^MT026-C06-3
- **Niels Kaastrup-Larsen** In October 2024 trend followers were hurt mainly by fixed income and equity corrections and some currencies, while gold and silver were the only strong liquid markets; SocGen trend was down almost 3% for the month.  #mech/cycle_persistence _(time-bound view)_
  > SocGen trend down almost 3% this month now down 71 basis points for the year.
  indicator: SG Trend Index, SG CTA Index, BTOP50, S&P 500, MSCI World · asset: multi · direction: gold and silver positive; bonds, equities, FX negative · horizon: weeks · testable: yes - index data are public · confidence: high
  ^MT026-C06-4
- **Niels Kaastrup-Larsen** Paul Tudor Jones publicly favoured trend following after four to five weak years for the strategy, and a strong run followed soon after, an anecdote that strategy returns can rebound after long drawdowns.  #mech/behavioral _(added by opus cross-check, time-bound view)_
  > this is after four five years where trend following had not done so well, he wanted to put that in trend
  indicator: trend-following index trailing 4-5 year performance · asset: multi · direction: long trend following after multi-year underperformance · horizon: years · testable: partly - single anecdote; strategy-level reversal can be tested on CTA index · confidence: low
  ^MT026-C06-X1
- **Niels Kaastrup-Larsen** Trend followers lost most in bonds in October 2024 even though their long bond positions had already shrunk, showing that a reversal still costs money while the trend signal is decaying.  #mech/slow_reaction _(added by opus cross-check, time-bound view)_
  > that's probably where trend followers are hurting the most this month despite long exposure becoming smaller in bonds
  indicator: CTA bond exposure; SocGen Trend Index · asset: rates · direction: trend followers lose on bond selloff after long positions · horizon: weeks · conditions: trend reversal after a long bond rally · testable: partly - index attribution not public · confidence: medium
  ^MT026-C06-X2
- **Niels Kaastrup-Larsen** In October 2024 the SocGen short-term traders index was flat for the year (BTOP50 +2.88% YTD, SG CTA +0.63% YTD) while the S&P 500 was up about 21.5%, i.e. CTAs lagged equities sharply that year.  #mech/slow_reaction _(added by opus cross-check, time-bound view)_
  > The short-term traders index is down 62 basis points flat as a pancake this year.
  indicator: SG Short-Term Traders Index; BTOP50; SG CTA Index; S&P 500 YTD · asset: multi · horizon: months · testable: yes - index data · confidence: high
  ^MT026-C06-X3

### C07
- **Rob Carver** For slow trend following, test sensitivity by delaying fills by one or two days; if the Sharpe change is above about 0.01 the system is sensitive to delay and needs hourly data or slower trading, otherwise intraday moves and overnight gaps do not matter.  #mech/research_method
  > a really good test to do when you're doing your backtest on daily data is to see what effect has if you delay your fills by one one business day or even by two business days
  indicator: Sharpe ratio change when fills are delayed 1-2 days · asset: multi · horizon: days · conditions: slow trading systems; not high frequency · testable: yes - direct backtest comparison · confidence: high
  ^MT026-C07-1
- **Rob Carver** A slow system's desired position barely changes if the latest price moves, so intraday and overnight price movements between signal and execution can be ignored on average.  #mech/risk_management
  > if you're trading slowly enough, then moving one, you know, the last price in a whole series of prices by a by even a quite a large amount won't change the desired position that much
  asset: multi · horizon: days · conditions: trading slowly relative to daily price noise · testable: yes - delayed-fill test · confidence: high
  ^MT026-C07-2

### C08
- **Rob Carver** Dynamic optimisation compares current positions with the zero-cost ideal portfolio and trades only when moving is worth the cost, sometimes not trading at all or trading in cheaper markets.  #mech/risk_management
  > This is the portfolio I'd ideally want to have if I didn't have trading costs.
  indicator: current vs ideal portfolio, trading costs · asset: multi · direction: trade only if benefit exceeds cost · horizon: days · testable: yes - cost-aware rebalancing can be backtested · confidence: high
  ^MT026-C08-1
- **Rob Carver** A simple buffer skips a trade if the position changes by less than 10% of a standard vol-adjusted position unit.  #mech/risk_management
  > which is vol adjusted, then if it was less than 10%, I wouldn't bother trading
  indicator: 10% position buffer · asset: multi · direction: no trade inside buffer · horizon: days · testable: yes - buffer width is testable · confidence: high
  ^MT026-C08-2
- **Rob Carver** Trend following has a long-option-like payoff (gains when markets trend, small losses whipsawing in ranges), particularly at short horizons, without paying the explicit option premium.  #mech/risk_premium
  > So, we can actually treat trend following, particularly short-term trend following, as a bit like buying an option without buying an option.
  indicator: trend following payoff convexity · asset: multi · direction: long convexity · horizon: months · testable: yes - payoff vs straddle returns · confidence: high
  ^MT026-C08-3
- **Rob Carver** A dynamic-optimisation system could be rerun hourly to pick up new prices (handling stale prices in closed markets), but for a slow system trading off the prior close is good enough and Rob does not bother.  #mech/risk_management _(added by opus cross-check)_
  > in theory, I could actually run that system on an intraday basis and run it every every hour or so
  asset: multi · horizon: days · conditions: slow systems; markets with different trading hours give stale prices · testable: yes - compare daily vs hourly reruns in backtest · confidence: medium
  ^MT026-C08-X1
- **Rob Carver** The main cost of expressing directional forecasts with options instead of futures is operational: options need much more implementation, infrastructure and data work.  #mech/new _(added by opus cross-check)_
  > the main con is that options are more complicated than futures. So, from a kind of implementation and infrastructure and data perspective, you know, there's a lot of work to do.
  asset: multi · testable: no - operational judgement · confidence: high
  ^MT026-C08-X2

### C09
- **Rob Carver** Systematically buying options loses money because of the volatility risk premium: implied volatility exceeds realized volatility on average since investors pay for insurance and certainty.  #mech/risk_premium
  > So, buying options consistently is a money-losing strategy.
  indicator: implied minus realized volatility · asset: multi · direction: short options earns, long options pays premium · horizon: years · testable: yes - variance risk premium is well documented · confidence: high
  ^MT026-C09-1
- **Rob Carver** A long call automatically pyramids as price rises because delta increases, mimicking trend followers' increasing exposure.  #mech/risk_management
  > as the price goes up the delta of the option goes up, which means you've effectively got more exposure to the market
  indicator: option delta · asset: multi · direction: more exposure as price rises · testable: yes - option mechanics · confidence: high
  ^MT026-C09-2
- **Rob Carver** Choose between futures and options for a directional view by comparing implied vol with forecast vol: buy calls when implied is below forecast, use futures when implied is high.  #mech/risk_management
  > if implied volatility is currently really low um and actually below my forecast for historical volatility, it may make sense to buy the call option
  indicator: implied volatility vs forecast realized volatility · asset: multi · direction: long call when implied cheap; long future when implied expensive · horizon: weeks · testable: yes - backtestable with option data · confidence: medium
  ^MT026-C09-3
- **Rob Carver** A combined futures-trend plus option-selling system would be net short volatility yet keep trend following's positive skew, with a higher Sharpe than futures-only trend following in theory.  #mech/risk_premium
  > the positive skew properties of trend following combined with the negative skew properties of auction selling
  indicator: trend following plus short options · asset: multi · direction: long trend, short vol bias · conditions: theory only; adds implementation complexity · testable: partly - requires option data to test · confidence: medium
  ^MT026-C09-4

### C10
- **Rob Carver** With zero costs one should always rebalance; as transaction costs rise, the optimal tolerance for deviation from the target position widens.  #mech/risk_management
  > The more transaction costs are are are higher, the more tolerance you're going to have from being away from the position that you want
  indicator: transaction cost, position deviation · asset: multi · direction: wider no-trade band when costs higher · testable: yes - rebalancing theory is testable · confidence: high
  ^MT026-C10-1
- **Rob Carver** A portfolio-level cost-aware optimiser can express a required bond exposure through the cheapest-to-trade correlated market and leave expensive positions untouched.  #mech/risk_management
  > What I'm probably going to do is buy go long and buy more of bonds that are cheaper to trade
  indicator: relative trading cost across correlated instruments · asset: rates · direction: buy cheaper substitute · horizon: days · testable: yes - backtest with instrument-specific costs · confidence: high
  ^MT026-C10-2
- **Rob Carver** A retail trader with 25% risk target pays about 1% a year in costs (half commissions, half spreads); an institution would pay about 60 bp (50 bp spread, 10 bp commission).  #mech/risk_management
  > standard annual standard deviation target is about 25% and I pay about 1% in transaction costs
  indicator: annual transaction cost 1% at 25% vol target · asset: multi · horizon: years · testable: partly - single practitioner figure · confidence: high
  ^MT026-C10-3

### C11
- **Rob Carver** In theory the position-inertia buffer should be wider for expensive instruments and narrower for cheap ones; the fixed 10% is a simplification that suits retail single-lot trades.  #mech/risk_management
  > in theory, you should actually, yes, have a a wider buffer if an instrument's more expensive and a smaller buffer if it's cheaper
  indicator: position buffer width by instrument cost · asset: multi · testable: yes - cost-scaled buffer is testable · confidence: high
  ^MT026-C11-1
- **Rob Carver** For measuring current portfolio risk, estimate correlations between instrument returns with an exponentially weighted window of about 6 months, balancing responsiveness against noise.  #mech/risk_management
  > I actually use um roughly a 6-month window, and I do use an exponentially rolling method
  indicator: 6-month exponentially weighted correlation of instrument returns · asset: multi · horizon: months · testable: yes - window choice is testable · confidence: high
  ^MT026-C11-2
- **Rob Carver** Bund vs US 10-year correlation is about 0.5 on average (Bund vs Schatz about 0.9) and falls when the US and German rate cycles are misaligned, rising when they move in lockstep, so cross-market bond correlations are regime dependent.  #mech/cycle_persistence _(added by opus cross-check)_
  > there's going to be times when the US and German economies are in quite different things, and their rate cycles are going to be misaligned and the correlations will be lower.
  indicator: rolling correlation Bund vs UST 10y; Bund vs Schatz · asset: rates · direction: correlation lower when rate cycles diverge, higher in crises · horizon: months · conditions: rate-cycle alignment between US and Germany · testable: yes - rolling correlations vs policy-rate divergence · confidence: medium
  ^MT026-C11-X1

### C12
- **Rob Carver** Correlations between instruments move to extreme levels in crises because of flight to safety and simultaneous deleveraging, so safe-haven bond correlations rise.  #mech/liquidity_flows
  > correlations always move to dramatic levels when when there's a crisis
  indicator: correlation of Bunds and US 10y · asset: multi · direction: correlations rise · horizon: weeks · conditions: crisis periods · testable: yes - correlation by regime · confidence: high
  ^MT026-C12-1
- **Rob Carver** Exponential weighting avoids sharp jumps in estimated correlation when a spike leaves a fixed window, which matters most for short windows.  #mech/research_method
  > it will gradually dissipate out of your returns rather than jumping in in one go
  indicator: exponentially weighted vs fixed-window correlation · asset: multi · testable: yes - compare estimator stability · confidence: high
  ^MT026-C12-2
- **Rob Carver** Correlations between trading-strategy returns (e.g. trend on Bund vs trend on US 10y) are lower and more stable than between assets, so estimate them over 10 or more years covering more than one cycle; exponential weighting matters little with that window.  #mech/risk_management
  > And because it's more stable, I actually want to use as much data as possible, 10 years, you know.
  indicator: 10-year correlation of sub-strategy returns · asset: multi · horizon: years · testable: yes - compare strategy vs asset correlation stability · confidence: high
  ^MT026-C12-3
- **Rob Carver** Automated monitoring: a status web page refreshed every 10 minutes shows whether processes are running, crashed or stale, plus nightly emails confirming normal operation.  #mech/risk_management
  > publishes a web page every 10 minutes
  indicator: process heartbeat, last-updated timestamp · asset: multi · horizon: days · testable: no - operational practice · confidence: high
  ^MT026-C12-4

### C13
- **Rob Carver** Automated checks flag missing prices for several days, missing daily positions, and differences between broker and system positions (often from expired futures) so human supervision is minimal.  #mech/risk_management
  > here are the positions that that the broker thinks you have. Here are the positions I think you have
  indicator: position reconciliation, stale price alerts · asset: multi · horizon: days · testable: no - operational practice · confidence: high
  ^MT026-C13-1
- **Rob Carver** Do not dynamically reallocate capital between strategies or instruments on past performance because with decades of backtest and 10 years live data, differences are rarely statistically significant; simple allocation works as well as sophisticated optimisation which overfits.  #mech/research_method
  > I usually almost completely ignore the performance of of strategies and and instruments
  indicator: strategy track record · asset: multi · horizon: years · conditions: slow trading systems; high-frequency strategies have enough data · testable: yes - test performance-based reallocation out of sample · confidence: high
  ^MT026-C13-2

### C14
- **Rob Carver** Ranking about 100 instruments by backtested trend performance looks like a clear winner-loser spread, but with error bars all overlap, so selecting instruments or strategies by backtest results is mostly fitting noise.  #mech/research_method
  > all of the error bars overlap
  indicator: backtest Sharpe with confidence intervals across ~100 instruments · asset: multi · direction: do not drop instruments with poor backtests · horizon: years · conditions: slow trading strategies · testable: yes - bootstrap error bars · confidence: high
  ^MT026-C14-1
- **Niels Kaastrup-Larsen** Cocoa made no money for trend followers for 15 years then made the most in 18 months, illustrating that an instrument's past record is a poor guide to its future contribution.  #mech/research_method _(time-bound view)_
  > just think of the cocoa example where for 15 years it made no money and the last 18 months it's made all the money in the world for trend followers
  indicator: cocoa trend P&L · asset: commodities · horizon: years · testable: partly - single anecdote · confidence: medium
  ^MT026-C14-2

### C15
- **Rob Carver** Yavin's argument: adding more assets (even equal weighted) removes idiosyncratic risk and increases exposure to the common factor (e.g. S&P 500), so diversification benefits diminish.  #mech/structural_shift
  > mathematically you actually get less diversification because you end up with less idiosyncratic sort of stock risk
  indicator: portfolio factor exposure vs number of holdings · asset: equities · testable: yes - factor regression as holdings increase · confidence: medium
  ^MT026-C15-1
- **Rob Carver** Equal weights are preferable to market-cap weights in long-only portfolios absent performance information, because cap weighting bets on mega caps being worth 50 times the smallest; momentum makes cap weighting look better.  #mech/behavioral
  > in the absence of any information about stock performance you should have equal weights
  indicator: equal vs market-cap weighting · asset: equities · direction: equal weight · conditions: momentum raises weight of winners in cap-weighted portfolios · testable: yes - weight scheme comparison · confidence: medium
  ^MT026-C15-2
- **Rob Carver** CTA performance is driven by a handful of latent macro factors (e.g. commodity move, 2008 risk-off with stocks down and bonds up) that change over time.  #mech/structural_shift
  > there are probably four, maybe five factors out there that that potentially explain CTA performance
  indicator: latent factors in CTA returns · asset: multi · horizon: years · testable: yes - PCA of CTA returns · confidence: medium
  ^MT026-C15-3

### C16
- **Rob Carver** With 300 markets a trend portfolio really holds a few independent macro bets, so idiosyncratic markets like cocoa contribute little and macro trends drive performance.  #mech/structural_shift
  > well actually you've got five bets
  indicator: number of markets vs effective independent bets · asset: multi · testable: yes - effective bet count via PCA · confidence: medium
  ^MT026-C16-1
- **Rob Carver** Backtested trend performance rises about four to five times with more markets, implying roughly 16 to 25 independent bets of which only about half a dozen matter at any time.  #mech/research_method
  > the increase in performance in a back test of a trend following portfolio as I add markets to it it does increase by a factor of about four to five
  indicator: Sharpe vs number of markets · asset: multi · testable: yes - diversification multiplier from backtest · confidence: medium
  ^MT026-C16-2
- **Niels Kaastrup-Larsen** Adding many markets also adds many chances of ranging markets, so more markets are different, not necessarily better.  #mech/risk_management
  > you're also adding the chance of 200 markets being stuck in a range and you losing money of those
  indicator: number of markets · asset: multi · conditions: small position sizes in extra markets · testable: partly - compare 50-market vs 300-market programs · confidence: medium
  ^MT026-C16-3
- **Rob Carver** Adding alternative (non-traditional) futures markets to a trend portfolio adds only a little diversification, perhaps one new latent factor, because most markets load on the same few macro trends.  #mech/slow_reaction _(added by opus cross-check)_
  > even that's kind of only buys you a little bit more diversification. You might be introducing that one new risk factor
  asset: multi · horizon: years · testable: yes - factor analysis of trend returns with and without alternative markets · confidence: medium
  ^MT026-C16-X1
- **Rob Carver** Yavin's conclusion: a plain-vanilla trend CTA gains little from 300 markets; extra value comes from lower-correlation approaches, though Rob notes the author sells such a different CTA.  #mech/research_method _(added by opus cross-check)_
  > if you're just a plain vanilla trend following CTA, there's probably no point in having 300 markets.
  asset: multi · horizon: years · conditions: vanilla trend following · testable: yes - compare backtests by universe size · confidence: medium
  ^MT026-C16-X2

### C17
- **Niels Kaastrup-Larsen** Looking at performance databases, there is no evidence that CTAs trading 300 to 400 markets do better than those trading about 100 or fewer.  #mech/research_method
  > there is no evidence, in my opinion, that
  indicator: CTA performance vs number of markets · asset: multi · horizon: years · testable: yes - database comparison · confidence: medium
  ^MT026-C17-1
- **Rob Carver** Positive skew in a large trend portfolio comes from exposure to underlying macro factors, since idiosyncratic left and right tails wash out, so purer factor exposure gives better skew.  #mech/structural_shift
  > for the best skew, you want as pure an exposure to those factors as possible
  indicator: skew of trend portfolio · asset: multi · testable: yes - skew by number of markets · confidence: medium
  ^MT026-C17-2
- **Rob Carver** Allocators could hold a vanilla low-cost CTA as core beta and add a lower-correlation CTA for alpha, as in equities.  #mech/structural_shift
  > maybe people allocating to CTA should be thinking a little bit more like um people in in in stocks do, which is you have your kind of core beta allocation
  indicator: core-satellite CTA allocation · asset: multi · testable: partly - needs correlation and fee data · confidence: medium
  ^MT026-C17-3
- **Rob Carver** Because returns are non-linear, correlation understates diversification in trend following: benefits continue beyond where correlation analysis says they level off.  #mech/structural_shift
  > the correlations potentially probably understate the amount of diversification that's available as you add more assets, especially in trend following
  indicator: portfolio Sharpe vs correlation-implied diversification · asset: multi · testable: yes - compare realized vs correlation-implied gains · confidence: medium
  ^MT026-C17-4
- **Rob Carver** Low-cost beta trend products cannibalise high-fee flagship funds because much of a flagship's return is the same beta, as equity hedge funds once charged full fees on beta they would not unbundle.  #mech/new _(added by opus cross-check)_
  > there's a big risk this could outperform the flagship fund, and and people would be going, "Well, are we paying you guys, you know, two and 20 when there's this thing here for 50 basis points flat
  asset: multi · horizon: years · testable: partly - compare flagship vs beta product returns net of fees · confidence: medium
  ^MT026-C17-X1

### C18
- **Rob Carver** Three replication methods exist: position-level, bottom-up simple model, and return-based; position-level replication is fine and Rob uses it, trading about 20 instruments that replicate his 300-instrument portfolio.  #mech/structural_shift
  > Position-level replication, which is where you start, you know you know what the positions need to be, and then you form a series of positions that get as close to that portfolio as you possibly can.
  indicator: position-level replication · asset: multi · testable: yes - tracking error between replica and full portfolio · confidence: high
  ^MT026-C18-1
- **Rob Carver** Bottom-up replication builds a simple trend model on about 30 liquid futures: cheap and good for ETFs to reach investors who cannot meet minimums.  #mech/structural_shift
  > why don't I just build a really simple model that does that in, say, 30 liquid futures markets
  indicator: simple trend model on 30 liquid futures · asset: multi · testable: yes - backtest vs CTA index · confidence: high
  ^MT026-C18-2
- **Rob Carver** If CTA returns are driven by only four or five latent macro trend factors, replication should work: estimate those factors from data and hold a small portfolio that captures them without CTA fees.  #mech/slow_reaction _(added by opus cross-check)_
  > one reason why replication should work is if they really are just a small number of kind of macro trend factors out there
  asset: multi · horizon: years · conditions: holds only if few factors dominate · testable: yes - factor count from PCA of CTA returns · confidence: medium
  ^MT026-C18-X1

### C19
- **Rob Carver** Return-based replication, fitting positions to reproduce an index's returns, is the approach Rob objects to most.  #mech/research_method
  > the return-based application is the one I have a problem with
  indicator: regression of CTA index returns on futures · asset: multi · testable: yes - out-of-sample tracking test · confidence: high
  ^MT026-C19-1
- **Rob Carver** Testing replication on randomly generated pseudo-CTAs and a pseudo index avoids overfitting to the last 30 years of real trends and reproduces features such as yearly dispersion.  #mech/research_method
  > rather than using real data, it uses random data, randomly generated data. And this is a brilliant approach that I think quants should use more um because it reduces the chances of overfitting
  indicator: simulated CTA universe · asset: multi · testable: yes - Monte Carlo · confidence: high
  ^MT026-C19-2
- **Rob Carver** Low CTA dispersion years indicate one or two dominant factors; high dispersion years indicate varied market events where different weights and trades lead to different results.  #mech/structural_shift
  > in years with low dispersion, probably there were one or two big factors that, you know, everyone made their money out of.
  indicator: cross-sectional dispersion of CTA returns · asset: multi · horizon: years · testable: yes - dispersion vs factor concentration · confidence: medium
  ^MT026-C19-3
- **Rob Carver** In the simulated universe about 30 factors explain everything, so about 30 futures suffice if they are spread across asset classes and liquid; 30 US bond futures would not work.  #mech/structural_shift
  > you only need about, say, 30 futures as long as you choose your universe to have a reasonable amount of independence
  indicator: 30 diversified liquid futures · asset: multi · testable: yes - subset replication of index · confidence: medium
  ^MT026-C19-4

### C20
- **Niels Kaastrup-Larsen** The paper's saving estimate of 200bp management fee, 110bp performance fee and 275bp unnetted costs looks too high; it implies a ceiling Sharpe near one for replication savings over tracking error.  #mech/research_method
  > And then 275 basis points of unnetted transaction costs. And I'm kind of thinking compared to the cost we pay, compared to the cost you just mentioned, this seems high.
  indicator: CTA fee and cost assumptions · asset: multi · testable: yes - compare to realistic fees · confidence: medium
  **Correction (cross-check):** Mixes speakers: the 'Sharpe near one' ceiling is the paper's calculation as presented by Rob; Niels's own point is only that the cost inputs (200 bp management fee, 110 bp performance fee, 275 bp unnetted costs) look too high. → Niels says the paper's cost-saving inputs (200 bp management fee, 110 bp performance fee, 275 bp unnetted costs) look too high versus actual costs, so the paper's Sharpe-near-one ratio of cost savings to tracking error (as described by Rob) overstates the gain.
  ^MT026-C20-1
- **Rob Carver** Realistic replication savings are about 100 to 200 bp (paper's actual BTOP50 result implied a 0.23 ratio, about 150bp), minus the replicator's own fees.  #mech/risk_premium
  > it's probably not unreasonable to to be able to to make an extra 100, maybe 200 basis points through a combination of a little bit of transaction cost saving and a bit of a bit of fee saving
  indicator: replication fee and cost saving · asset: multi · horizon: years · testable: yes - compute net savings · confidence: medium
  ^MT026-C20-2
- **Rob Carver** Many independent managers each pay costs on trades that would offset each other; one combined book nets those trades, which is the 'unnetted transaction cost' saving claimed for replication.  #mech/new _(added by opus cross-check)_
  > If you had them under a single roof, you could actually get them to net off a lot of those trades
  asset: multi · testable: partly - needs manager-level trades · confidence: medium
  ^MT026-C20-X1

### C21
- **Rob Carver** Return-based regression needs short windows to capture sign changes in CTA positions, but short windows with many futures regressors make regression infeasible, so the paper uses lasso.  #mech/research_method
  > What you're trying to capture here is the effect of what happens when people's position changes sign.
  indicator: rolling regression window length, lasso · asset: multi · horizon: months · testable: yes - window sensitivity · confidence: medium
  ^MT026-C21-1
- **Rob Carver** The replication paper's results appear in-sample; a proper test would refit weekly, hold positions the next week and measure tracking out of sample, which always does worse than in-sample.  #mech/research_method
  > it still looks to me like they're doing an in-sample test
  indicator: out-of-sample tracking error of replicator · asset: multi · horizon: weeks · testable: yes - walk-forward test · confidence: medium
  ^MT026-C21-2

### C22
- **Rob Carver** A simple momentum model on 30 futures automatically captures sign changes and is a more sensible cheap trend product than regressing on a benchmark.  #mech/structural_shift
  > just do 30 futures in a very simple portfolio and just bung that into an ETF
  indicator: simple 30-futures trend ETF · asset: multi · testable: yes - backtest · confidence: high
  ^MT026-C22-1
- **Niels Kaastrup-Larsen** Tracking error is not the right metric for CTA replication because managers do not target a benchmark; live replication products show lower than expected correlation to the benchmark on daily data.  #mech/research_method
  > But of course, managers are not trying to meet a benchmark. So I think the concept of tracking error as such is not so relevant.
  indicator: tracking error and correlation of replicators vs BTOP50/SG index · asset: multi · testable: yes - measure live replicator correlation · confidence: medium
  ^MT026-C22-2
- **Rob Carver** Return-only backward-looking replication cannot reproduce a CTA index's diversification, so marketing it as benchmark less fees is flawed.  #mech/research_method
  > for me fundamentally it's not possible to to do a good replication job with a purely backward looking measure based only on returns
  asset: multi · testable: partly - out-of-sample tracking test · confidence: high
  ^MT026-C22-3
- **Rob Carver** Diversifying across 10 to 15 CTAs needs a large portfolio, because with a 5 to 10% CTA allocation each manager ticket is about 1% of assets and must meet minimums, so most investors cannot do it.  #mech/new _(added by opus cross-check)_
  > pick say 10 15 CTAs and dump, you know, a chunk of money into them. You'd need to be quite wealthy to do that
  asset: multi · testable: no - practical constraint · confidence: high
  ^MT026-C22-X1

### C23
- **Rob Carver** If investors believe a few risk factors drive CTAs and diversification across managers is limited, a cheap bottom-up ETF with about 30 markets at about 50bp is reasonable; return-based replication of an index of many managers is a bad move.  #mech/structural_shift
  > well, actually, something like a bottom-up replication done cheaply may make sense to you
  indicator: bottom-up 30-market trend ETF at 50bp · asset: multi · testable: partly - depends on factor concentration · confidence: medium
  ^MT026-C23-1
- **Niels Kaastrup-Larsen** Institutional allocators who select managers must believe in persistent manager skill, so settling for a replicator contradicts their role.  #mech/behavioral
  > because they must believe that within managers there is something called skill
  indicator: manager skill persistence · asset: multi · horizon: years · testable: partly - manager persistence studies · confidence: medium
  ^MT026-C23-2
- **Rob Carver** A single CTA manager, even one in the index, has dispersion to the CTA index by construction, so tracking error against the index is not unique to replicators.  #mech/research_method _(added by opus cross-check)_
  > they're going to have dispersion to it, you know, something like like just like the replication people can.
  indicator: manager tracking error vs SG CTA/BTOP50 index · asset: multi · horizon: years · testable: yes - manager vs index tracking error · confidence: medium
  ^MT026-C23-X1
- **Niels Kaastrup-Larsen** Replication ETFs opened trend following to smaller investors, and CTA managers now offer versions of their own strategies as ETFs, an alternative to replication.  #mech/structural_shift _(added by opus cross-check, time-bound view)_
  > some of the managers now are offering this or some version of their strategies in in ETF format
  asset: multi · horizon: years · testable: no - industry observation · confidence: medium
  ^MT026-C23-X2

