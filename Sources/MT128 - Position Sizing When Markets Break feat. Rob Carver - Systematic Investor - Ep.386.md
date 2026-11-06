---
source_id: MT128
title: "Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386"
date: 2026-02-10
channel: "Top Traders Unplugged"
url: 
words: 12725
claims: 77
added_by_crosscheck: 18
corrections: 1
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Rob Carver (systematic futures trader, author, ex-AHL/AQR)", "Niels Kaastrup-Larsen (host)"]
tags: [source, layer0]
---
# Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386

**Speakers:** Rob Carver (systematic futures trader, author, ex-AHL/AQR); Niels Kaastrup-Larsen (host)

**Summary:** Top Traders Unplugged Systematic Investor Ep.386 (Feb 2026): Rob Carver and Niels on the silver crash of 30 Jan 2026 (volatility-adjusted sizing, liquidity, Hunt 1979), a new Fed chair, trend update, listener questions on correlation/covariance estimation for vol targeting, a Man AHL paper on traditional vs alternative markets in trend portfolios, and an FT article on quant/AI convergence. Conclusions: vol-adjusted sizing and diversification protect in parabolic reversals; crisis-alpha seekers should favour traditional liquid futures.

**Approach:** trend following, position sizing / volatility targeting, risk management, market universe selection, correlation estimation, AI in quant finance

**Cross-check completeness estimate of first read:** 0.84 - first reader captured the silver crash mechanics, sizing and paper findings well; missed side mechanisms (binary versus continuous sizing, daily-rebalance gap, stop-loss gap risk, liquidity filter, Fed chair institutional points, TACO behaviour, correlation-turnover point)

## Argument map

**Episode thesis:** After the 30 January 2026 silver crash, Rob Carver argues that continuous volatility-adjusted position sizing plus diversification is what protects a trend follower in parabolic reversals (his loss was 3%, while unscaled leveraged CTAs swung by tens of points), that liquidity is not constant, and that crowded volatility-adjusters can amplify sell-offs. The Man AHL paper he summarises says an investor who wants trend as equity-crisis protection and a cash source should favour traditional liquid futures, while a pure Sharpe maximiser should trade more alternative markets. Niels adds the Hunt brothers 1979 leverage lesson and the view that positioning, not the Fed-chair nomination, drove the silver sell-off.

### Rob Carver (systematic futures trader and author, ex-AHL and AQR, trades a small dynamically optimised futures account)
Fingerprint: #approach/position_sizing_vol_target #approach/trend_following #approach/diversification_risk_parity #approach/crisis_alpha_convexity #approach/positioning_crowding #approach/costs_execution #approach/portfolio_construction_stacking #approach/research_robustness_overfitting
_Speaker note: Main speaker. Captions are clean in most places. The remark that a 3% one-day loss was in line with other CTAs at similar volatility is Niels's (ledger correction on C05-5), not Rob's._

**Worldview premises**
- A CTA's position is a function of trend strength (forecast) and instrument volatility, so rising volatility can cut exposure even while the trend signal strengthens. Systems differ: binary long/short, continuous forecast scaling, or volatility sizing only at entry. _[theoretical, stated; support: his own silver position history]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C02-1|C02-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C02-3|C02-3]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C02-X1|C02-X1]])
- A normal-speed trend signal stays long after even a record one-day drop. A daily-rebalanced system sizes from the prior close and cannot cut intraday, so protection comes from having already scaled down. _[theoretical, stated; support: his silver trades around 30 January 2026]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C03-2|C03-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C03-X1|C03-X1]])
- Risk management comes down to position sizing and diversification. Together they limited his loss to 3% on the crash day, while concentrated or unscaled, leveraged funds lose far more. _[experience, stated; support: his own 3% loss versus reported swings of a levered CTA (+72% to +27% on the month)]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C05-4|C05-4]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C03-4|C03-4]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C05-R1|C05-R1]])
- Liquidity is not a constant. After a run-up and pullback the buyers are gone, so liquidity vanishes in crises (more in less-liquid markets), and recent volume and open interest spikes from 'tourists' overstate it; look back one to two years. _[behavioural, stated; support: market-structure argument (cinema with one fire door)]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C05-1|C05-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C05-2|C05-2]])
- CTAs, risk parity and other quant strategies all cut exposure when volatility spikes, so crowding magnifies volatility-driven sell-offs. _[behavioural, stated; support: reasoning; no data]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C05-3|C05-3]])
- A stop widened with volatility needs a smaller position at the same time, or risk rises. A stop that does not widen shakes you out of trends early, and no reasonable stop avoids a 25% one-day gap. _[theoretical, stated; support: design reasoning; he does not use stops]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C04-1|C04-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C04-2|C04-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C04-X2|C04-X2]])
- With volatility-targeted instruments portfolio risk depends only on correlations, so diversification forces positions to be scaled up (about 4-5x; a 15% target would otherwise give about 3%). _[theoretical, stated; support: his own calculation]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C11-1|C11-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C11-2|C11-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C11-3|C11-3]])
- Volatility is more predictable than correlation (month-on-month R-squared about 0.35 versus 0.2-0.25), and means are noise. Estimate volatility (about 1 month) and correlation (about 6 months) separately, then combine. _[empirical, stated; support: his own regressions, 'off the top of my head', plus academic research]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C12-1|C12-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C12-2|C12-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C12-3|C12-3]])
- A large part of trend returns is a risk-on/risk-off factor (about 55% for traditional markets), while alternative and esoteric markets are about one third factor and two thirds idiosyncratic, which makes them diversifying. _[empirical, stated; support: Man AHL paper (PCA factor decomposition)]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C14-1|C14-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C14-2|C14-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C14-3|C14-3]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C13-1|C13-1]])
- Futures are cash efficient (about 20-30% of cash as margin) and this matters most when cash is needed, as in 2008 when investors drew on CTAs. _[experience, stated; support: his own account (30% margin use) and the paper; 2008 history]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C16-1|C16-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C16-3|C16-3]])
- Discretionary override of his system cost him: selling equities in the April 2025 tariff tantrum lost relative performance, and the systematic version did better. _[experience, stated; support: his own result]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C08-1|C08-1]])
- Markets have largely shrugged off the president's policy shocks since early 2025, partly through a 'TACO' pattern (he backs down), so his initial expectation of a bad market was wrong. _[experience, stated; support: admitted forecast error]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C08-X2|C08-X2]])
- Systematic finance has always used supervised machine learning (regression, optimisation). AI works best in tightly defined areas such as execution research with rich tick data, and much fund AI is marketing or blue-sky research. _[experience, stated; support: opinion; he describes himself as an AI skeptic]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C17-2|C17-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C18-1|C18-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C18-R3|C18-R3]])

**Chain: Silver parabolic run and crash for a continuously vol-scaled trend follower**
1. silver trend strengthens (bought 27 Nov and 3 Dec at $53 and $59) → position grows with forecast: position is trend strength times inverse volatility ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C03-1|C03-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C02-1|C02-1]])
2. volatility rises (sold at $71 on 31 Dec and $81 on Monday after the crash) → position shrinks even though trend is still long: volatility scaling ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C03-1|C03-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C03-X1|C03-X1]])
3. 30 January drop (biggest one-day fall in about 45-47 years) hits a smaller position → loss limited to 3% of account and the silver trades still profitable: daily rebalance cannot trade the gap, but exposure was already cut and the portfolio diversified ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C03-2|C03-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C03-3|C03-3]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C05-4|C05-4]])
- Evidence: His own trade records and prices ($53/$59 in, $71/$81 out; peak $110-120).
- Fails when: The profit is measured against entry prices, so it misses the peak; he is uncertain whether he would have been better without vol-scaling at the top. His dynamic optimisation means a strong forecast does not always give a position.

**Chain: Unscaled leveraged CTAs in a parabolic reversal**
1. no continuous volatility adjustment, high leverage → silver becomes a growing share of the portfolio during the run-up: position value rises with price and is never cut ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C03-4|C03-4]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C02-3|C02-3]])
2. one-day crash → very large loss (a levered CTA went from roughly +50% to +25% by Rob's estimate, +72% to +27% per Niels): concentrated unscaled exposure ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C03-4|C03-4]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C03-5|C03-5]])
- Evidence: January monthly returns for unnamed CTAs; numbers differ slightly between speakers.
- Fails when: Not stated.

**Chain: Liquidity illusion and crowded volatility selling**
1. hot market with surging volume and open interest, new 'tourist' participants → trader believes a large position can be built and exited: treats liquidity as constant ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C05-1|C05-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C05-2|C05-2]])
2. price moves against the position → everyone exits at once and the liquidity is not there: buyers are already in; liquidity disappears in crises, more in less-liquid markets ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C05-1|C05-1]])
3. CTAs, risk parity and quants all cut on volatility spikes → sell-off magnified: crowding of the same volatility rule ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C05-3|C05-3]])
- Evidence: Argument and analogy; no data.
- Fails when: Niels notes larger CTAs were selling silver through December and January, so they were a buffer during the run-up rather than a cause.

**Chain: Fed chair nomination as cause of the silver crash**
1. nominee seen as relatively sane, possibly hawkish on rates, less mainstream on QE and balance sheet → relief reaction in markets: market expected someone aligned with the president ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C08-X1|C08-X1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C08-3|C08-3]])
2. bond market reaction muted (no 50bp two-year move recalled) → nomination probably not the true cause of the silver sell-off: bonds are the most direct measure of the news ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C08-2|C08-2]])
3. chair appointed by a president demanding loyalty → independence is unknowable; Powell was also appointed by Trump and resisted, and chairs cannot be removed and care about legacy: precedent ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C08-3|C08-3]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C09-X1|C09-X1]])
- Evidence: Recollection of bond moves ('haven't got the figures to hand'), precedent of Powell.
- Fails when: He admits no one knows what happens when Powell's term ends in May.

**Chain: Diversification and the risk-target multiplier**
1. every instrument targeted to the same volatility → book risk depends only on correlations: volatility is equalised by construction ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C11-1|C11-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C12-4|C12-4]])
2. low correlation between instruments → book undershoots risk target unless positions are multiplied by about 4-5: diversification lowers book volatility ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C11-2|C11-2]])
3. need to estimate the book correlation → use P&L streams over a rolling window of about 6 months (optionally exponentially weighted), which captures asset and signal correlation: slow estimate adds negligible extra trading compared with signal-driven trading ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C11-4|C11-4]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C12-X1|C12-X1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C12-3|C12-3]])
- Evidence: His own calculation of the multiplier; academic estimation research.
- Fails when: The fixed 0.7 correlation from his book is a ratio of trend correlation to underlying correlation, not a book correlation, so misuse biases risk.

**Chain: Market universe for a trend portfolio (Man AHL paper)**
1. traditional markets mostly factor-driven; alternative and esoteric mostly idiosyncratic → an unconstrained Sharpe-maximising portfolio is about 30% traditional and 70% alternative (about 5% crypto): idiosyncratic returns diversify ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C14-3|C14-3]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C14-4|C14-4]])
2. optimising only over periods when equities fell → about 50% traditional markets: crisis payoff comes from the factor: short equities, long bonds; alternatives trade like risk-on assets and may be hard to short or illiquid ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C15-1|C15-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C15-2|C15-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C15-3|C15-3]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C15-4|C15-4]])
3. adding a cash-efficiency constraint → about 70% traditional and 30% alternative: alternative markets need more margin, some 100%; cash efficiency matters most when cash is needed (2008) ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C16-1|C16-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C16-2|C16-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C16-3|C16-3]])
- Evidence: Paper's optimisations (figures read out by Rob).
- Fails when: The 30/70 optimum is unconstrained, and large CTAs cannot do it because of capacity.

**Chain: Trend breadth and realised risk**
1. many markets trending strongly (high trend barometer) → forecast-scaled system carries more risk: positions scale with forecast strength ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C10-X1|C10-X1]])
- Evidence: His own account: risk 'a little bit higher than it has been for a while', which matches the barometer.
- Fails when: Not stated.

**Decision process**
- [sizing] Continuously adjust each position for changes in volatility as well as forecast strength (daily rebalance from the prior close).. Why: protects against parabolic reversals ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C02-1|C02-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C03-X1|C03-X1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C05-4|C05-4]])
- [universe] Trade a dynamically optimised subset of 250 futures matching an idealised large portfolio; skip instruments barred by regulation or too illiquid or expensive.. Why: small account, so may hold no position despite a strong forecast ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C02-2|C02-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C04-X4|C04-X4]])
- [risk] Do not use stop-losses. If using a volatility-based stop, widen it only together with a smaller position.. Why: stops do not remove gap risk; position size determines the loss ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C04-1|C04-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C04-2|C04-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C04-X2|C04-X2]])
- [risk] Judge liquidity over a one to two year history, not recent volume or open interest.. Why: tourists inflate volume in hot markets ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C05-2|C05-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C04-X4|C04-X4]])
- [portfolio] Scale all positions up by about 4-5x so the diversified book hits its risk target.. Why: low correlation means undershooting otherwise ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C11-2|C11-2]])
- [portfolio] Estimate book correlation from combined P&L (rolling six months, optionally exponentially weighted) and estimate volatility separately (about one month). With vol-targeted instruments, portfolio construction only needs correlations.. Why: different predictability and speed of change ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C11-4|C11-4]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C12-1|C12-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C12-3|C12-3]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C12-4|C12-4]])
- [signal] Scale positions with forecast strength in each market and accept that realised risk rises when many markets trend at once.. Why: forecast-scaled design ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C10-X1|C10-X1]])
- [other] Stay systematic and avoid discretionary overrides.. Why: his April 2025 equity sale cost relative performance ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C08-1|C08-1]])

**Evidence style:** Own trade records and calculations (silver prices, 3% loss, 4-5x multiplier, R-squared figures from memory), reading of papers (Man AHL, FT Alphaville article), history (2008, Hunt via Niels), and first-principles reasoning on liquidity and crowding. He admits forecast errors openly.

**Views at the time**
- (early February 2026) Silver crash lesson is risk management (position sizing and diversification). His own loss was 3%, and his trend signal in silver remained long but the position was sold on Monday as volatility rose.. Reasoning: vol-scaling cut exposure into the crash ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C05-4|C05-4]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C03-1|C03-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C03-2|C03-2]])
- (early February 2026) The Fed-chair nomination was probably not the real cause of the silver sell-off, and the new chair's independence is unknowable.. Reasoning: muted two-year yield reaction; Powell precedent ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C08-2|C08-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C08-3|C08-3]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C09-X1|C09-X1]])
- (early February 2026) His trend portfolio is coping with dislocations in quant equity factors, Bitcoin and AI stocks. Most CTAs trading Bitcoin were probably short after the sell-off, and it was his biggest short position.. Reasoning: trend positions already short ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C07-2|C07-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C10-3|C10-3]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C10-R2|C10-R2]])
- (early February 2026) January trend profits came from idiosyncratic sources (gold, silver, natural gas), not from the risk-on/risk-off factor (bonds flat, equities slightly up).. Reasoning: factor decomposition applied to January ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C14-X1|C14-X1]])
- (early February 2026) Markets have shrugged off the president's policies; his own bearish call a year earlier was wrong.. Reasoning: TACO pattern or nobody takes threats seriously ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C08-X2|C08-X2]])

### Niels Kaastrup-Larsen (host, Top Traders Unplugged, veteran hedge fund manager; builds the Trend barometer)
Fingerprint: #approach/trend_following #approach/manager_selection_allocation #approach/crisis_alpha_convexity #approach/positioning_crowding #approach/market_internals_leading #approach/behavioral_sentiment
_Speaker note: Host who states views on silver history, crowding, manager selection and AI. Listener questions he reads (Pedro) are not his views. The 3% crash-day loss being decent is his comment (ledger correction on C05-5)._

**Worldview premises**
- Larger CTAs reduce silver notional as volatility expands, so they dampen rather than cause parabolic moves. _[empirical, stated; support: recollection of how large CTAs behaved through December and January; cocoa episode as precedent]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C06-1|C06-1]])
- Leverage with borrowed money, pyramiding and exchange margin hikes force liquidation in parabolic moves; the same pattern recurs across eras (Hunt 1979, January 2026). _[experience, stated; support: Hunt brothers silver 1979 story ($6 to $50)]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C06-2|C06-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C06-3|C06-3]])
- Experienced managers avoid emotional attachment and manage risk systematically. _[experience, stated; support: decades of observing CTAs]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C06-4|C06-4]])
- Silver is not gold: only about 30% is mined as silver, so supply is less controllable and the market more volatile. Traders became complacent after the precious-metals rally. _[empirical, stated; support: 'I've heard stories' (second-hand)]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C07-1|C07-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C04-X3|C04-X3]])
- Commodities belong in a trend universe because they offer opportunities, often independent of equity risk-off events (natural gas up 60% then down 26% in a day). _[experience, stated; support: the natural gas example and years of advocacy on the show]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C07-3|C07-3]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C07-4|C07-4]])
- The silver sell-off was driven by crowded positioning (including Chinese retail), not by the Fed chair news. _[behavioural, stated; support: muted market reaction]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C09-1|C09-1]])
- Being a systematic diversified investor beats trying to interpret political and market events discretionarily. _[experience, stated; support: none beyond Rob's own discretionary example]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C09-2|C09-2]])
- A trend barometer reading shows how many tracked markets trend (64 = 64%), which indicates breadth supportive for CTAs. _[empirical, stated; support: his own indicator]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C10-1|C10-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C10-2|C10-2]])
- Differences between trend managers come mainly from the markets they trade, not better models or faster signals. _[empirical, stated; support: Man AHL paper]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C13-X1|C13-X1]])
- Manager choice depends on investor objective: maximise standalone Sharpe by trading more markets, but pick traditional liquid futures managers for equity-crisis protection and cash needs. _[theoretical, stated; support: paper's conclusions]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C16-4|C16-4]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C17-1|C17-1]])
- Alphabet doubling AI capex to $185 billion suggests a possible bubble, and however high markets go it could still end badly because of building risks (timing unknowable). _[behavioural, stated; support: FT headline, no analysis]_ ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C09-3|C09-3]])

**Chain: Hunt brothers 1979 and margin-driven liquidation**
1. conviction that the dollar would fail and silver is real money → buying physical silver with borrowed money: leverage rose with the position ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C06-2|C06-2]])
2. silver rising from $6 to about $50 → COMEX raises margins: exchange rule change in parabolic moves ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C06-2|C06-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C06-3|C06-3]])
3. margin calls on leveraged holders → forced liquidation and a catastrophic outcome: ran out of money; same pattern recurs (margin hikes in January 2026) ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C06-3|C06-3]])
- Evidence: Historical story told from memory ('I won't do this story justice').
- Fails when: Details of the Hunt outcome are unclear to him.

**Chain: Silver supply structure and volatility**
1. only about 30% of silver supply is mined as silver, the rest by-product of gold and copper → supply is less controllable and harder to predict: by-product economics ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C07-1|C07-1]])
2. less controllable supply → silver is more volatile and harder to trade than gold: stated as possible reason ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C07-1|C07-1]])
- Evidence: Second-hand information.
- Fails when: Presented as 'maybe'.

**Chain: Objective-driven choice of trend manager**
1. goal is standalone maximum long-term Sharpe → trade more markets, including alternatives: paper's unconstrained optimisation ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C16-4|C16-4]])
2. goal is protection when equities or bonds fall, or a source of cash in a crisis → choose managers focused on traditional liquid futures: cash efficiency and factor exposure matter more in a crisis ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C16-4|C16-4]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C17-1|C17-1]])
- Evidence: Man AHL paper and his experience with investors.
- Fails when: Not stated.

**Decision process**
- [universe] Include commodities in the trend universe.. Why: opportunities that are independent of equity risk-off events ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C07-4|C07-4]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C07-3|C07-3]])
- [portfolio] Pick the CTA by investor objective (tail protection and cash needs point to traditional liquid futures managers), narrowing to a smaller number of managers.. Why: returns are not the only criterion ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C17-1|C17-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C16-4|C16-4]])
- [risk] Do not become emotionally attached to positions and manage risk systematically; avoid pyramiding and uncontrolled leverage.. Why: Hunt precedent ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C06-4|C06-4]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C06-2|C06-2]])
- [signal] Track the share of markets trending (trend barometer, 64 = strong breadth) as the read on trend environment.. Why: breadth is supportive for CTAs ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C10-1|C10-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C10-2|C10-2]])

**Evidence style:** Industry observation (index returns, manager results), history (Hunt 1979), and the Man AHL paper. He cites fund numbers without names and relies on second-hand information for the silver supply and the rumoured bank cause.

**Views at the time**
- (early February 2026) Silver sell-off driven by crowded positioning (Chinese retail), not the Fed chair nomination. Large CTAs were selling into the rally and so acted as a buffer.. Reasoning: muted reaction in financial markets; CTAs cut notional as volatility rose ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C09-1|C09-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C06-1|C06-1]])
- (early February 2026) The Fed chair is one of 12 FOMC votes, so the real independence risk is the pending Supreme Court ruling on removal of governors.. Reasoning: institutional structure ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C09-X2|C09-X2]])
- (early February 2026) Kevin Warsh was named as nominee, a surprise to him and taken by many as the proximate cause of the metals sell-off, which he doubts.. Reasoning: market reaction too muted ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C07-X1|C07-X1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C09-1|C09-1]])
- (early February 2026 (figures as of Tuesday)) January was strong for managers and February began well, with a broad base (equities, currencies, some fixed income, natural gas, meats, grains). Trend barometer 64. BTOP50 +5.38% year to date, SG CTA +5%, SG Trend +5.25%, short-term traders +2.37%, MSCI World +1.76%, S&P 500 +0.63%.. Reasoning: index data and breadth ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C10-2|C10-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C10-1|C10-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C10-4|C10-4]])
- (early February 2026) Alphabet's $185 billion AI capex plan sounds like a bubble, and the equity market could still end badly; timing is unknowable.. Reasoning: doubling of AI spend ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C09-3|C09-3]])
- (early February 2026) A 3% crash-day loss for a trend manager at Rob's volatility was very decent and in line with managers he follows.. Reasoning: what he saw from managers he can follow ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C05-5|C05-5]])

### Disagreements
- **Whether volatility-adjusting CTAs dampen or amplify parabolic moves**: Niels Kaastrup-Larsen: Larger CTAs were reducing silver notional as volatility expanded, so they act as a buffer and limit parabolic moves rather than cause them. ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C06-1|C06-1]]); Rob Carver: CTAs, risk parity and other quant strategies all sell on volatility spikes, and the more of them in a market, the more it magnifies the sell-off. ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C05-3|C05-3]])
- **Whether a stop-loss rule would have helped in the silver reversal**: Niels Kaastrup-Larsen: A hard stop from a recent high, possibly volatility-linked, could have stopped a trader out on the crash day; it depends on the rule. ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C04-X1|C04-X1]]); Rob Carver: Even a volatility-widened stop would probably have been breached by a 25% fall. A tight stop would shake you out of trends early, and position size is what determines the loss. ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C04-X2|C04-X2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C04-2|C04-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C04-1|C04-1]])
- **Where the Fed-independence risk lies**: Rob Carver: The key unknown is whether the new chair will cut for the president or resist as Powell did; no one knows. ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C08-3|C08-3]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C09-X1|C09-X1]]); Niels Kaastrup-Larsen: The chair is one vote of 12; the real risk is a pending Supreme Court decision that may let the president remove governors and pack the board. ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C09-X2|C09-X2]])

### Gaps and conflicts
- Speaker correction applied: the 3% crash-day loss being 'in line with other CTAs at similar annual volatility' is Niels's comment, not Rob's. ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C05-5|C05-5]])
- Numbers for the unscaled CTA's January swing differ between speakers (Rob: about 50% to 25% up; Niels: 72% to 27%). Both are unnamed and unverified. ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C03-4|C03-4]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C03-5|C03-5]])
- Rob says the Fed-chair news was 'supposedly' the proximate cause yet gives only a recollection of the two-year yield move ('haven't got the figures to hand'); Niels has rumours of an investment-bank cause that he declines to repeat. ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C08-2|C08-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C09-1|C09-1]])
- Tension between claims on crowding: Rob says vol-adjusters amplify sell-offs, Niels says large CTAs sold through the run-up and dampen. Both can hold (rise versus crash phase) but neither gives data on position sizes in silver. ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C05-3|C05-3]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C06-1|C06-1]])
- Rob's profit claim on the silver trades compares entry and exit prices only and ignores the move to $110-120 in between and the effect of his dynamic optimisation. ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C03-3|C03-3]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C02-2|C02-2]])
- Man AHL percentages (55/45, 1/3-2/3, 30/70, 50, 70/30, 5% crypto) are relayed from a paper that neither speaker has in front of them; Rob says 'about half' then 'more like 45-55'. ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C14-2|C14-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C14-3|C14-3]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C14-4|C14-4]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C15-2|C15-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C16-2|C16-2]])
- Rob's regression figures (R-squared 0.35 for volatility, 0.2-0.25 for correlation) are given 'off the top of my head'. His guess that Pedro's 0.7 comes from his book is also flagged as a gut feeling. ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C12-2|C12-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C11-3|C11-3]])
- The silver supply fact (30% mined as silver) is second-hand ('I've heard stories'). ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C07-1|C07-1]])
- Rob says he is wary of the FT article's AI claims because the authors are talking their own book, yet accepts its convergence thesis in workflow and pay as interesting; he supplies no evidence on how much AI funds really use. ([[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C17-3|C17-3]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C18-1|C18-1]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C18-2|C18-2]], [[MT128 - Position Sizing When Markets Break feat. Rob Carver - Systematic Investor - Ep.386#^MT128-C18-R3|C18-R3]])

### Forward-looking inputs (reader synthesis)
(reader) Trend barometer and breadth (share of markets trending), which Rob links to his realised risk; margin requirements and exchange margin changes in parabolic markets; liquidity measured over one to two years; correlation between instrument P&L streams (about 6 months) and volatility (about 1 month) as risk inputs; two-year yield reaction as the cleanest read of Fed news; the Fed-chair path from May and the Supreme Court ruling on governor removal. Horizon: days to months for positions, with trend lookbacks implied but not stated.

### Reader inferences (not stated by the speakers)
- (reader) Rob's protection claim depends on volatility rising before the break; a gap that arrives with no preceding volatility rise would hit a vol-scaled book as hard as an unscaled one.
- (reader) The crisis-alpha recommendation (about 50% traditional in equity-down periods) implies that a diversified CTA with many alternatives has less equity-crisis payoff than headline Sharpe suggests.
- (reader) Both speakers treat positioning and leverage, not macro news, as the proximate cause of the metals crash, which implies margin and open-interest data as the observable lead input.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | nothing actionable: intro, small talk and a paper title about total portfolio approach |
| C02 | 3 | Silver Freaky Friday setup; CTA positions as function of trend and volatility; dynamic optimisation; vol-adjustment variants |
| C03 | 5 | Rob silver trades, buy/sell dates and prices; effect of vol adjustment vs non-adjusting CTAs |
| C04 | 2 | Stop losses and volatility; liquidity differences across metals |
| C05 | 5 | Liquidity disappears in crisis, crowded vol-adjusting strategies, position sizing and diversification as risk management |
| C06 | 4 | CTAs as buffer rather than cause; Hunt silver 1979 and margin hikes; systematic risk management |
| C07 | 4 | Silver supply structure; cross-market dislocations incl. natural gas; commodities in trend universe; new Fed chair introduction |
| C08 | 3 | Tariff tantrum behavioural mistake; Fed chair uncertainty and muted bond reaction |
| C09 | 3 | Silver sell-off positioning; systematic vs discretionary; Google capex bubble comment |
| C10 | 4 | Trend barometer 64, Feb breadth, Bitcoin shorts, index data; listener question starts |
| C11 | 4 | Pedro question: correlation scaling for vol target; 0.7 origin; estimation window |
| C12 | 4 | Estimating correlation vs vol separately, predictability R-squared, vol targeting removes need for vol estimate |
| C13 | 1 | Man AHL paper: three market categories |
| C14 | 4 | Factor vs idiosyncratic return decomposition; unconstrained optimisation 30% traditional |
| C15 | 4 | Standalone vs 60/40 add-on; crisis-conditional optimisation favours traditional markets |
| C16 | 4 | Cash efficiency and margin constraints; 2008 cash machine; summary of choice |
| C17 | 3 | Investor fit; FT Alphaville quant-AI convergence, machine learning in systematic finance |
| C18 | 2 | AI use in funds, execution research, talent pay |
| C19 | 0 | nothing actionable: outro |

## Claims

### C02
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** A CTA's position in an instrument is a function of trend strength (forecast) and the instrument's volatility, so rising volatility can reduce exposure even while the trend signal strengthens.  #mech/risk_management
  > positions that are function of two things. The strength of the trend and the volatility of the instrument you're trading.
  indicator: trend forecast and volatility · asset: commodities · direction: position down when volatility rises, up when forecast rises · horizon: weeks · conditions: applies to continuous-forecast, vol-scaled CTAs · testable: yes: position = forecast / volatility is a testable rule · confidence: high
  ^MT128-C02-1
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** A small account trades a dynamically optimised subset of 250 futures, matching an idealised large portfolio, so it may hold no position in an instrument despite a strong forecast.  #mech/research_method
  > I basically dynamically optimize my portfolio every day to match to get the best possible match I could do to a sort of abstract portfolio
  indicator: dynamic optimisation for small accounts · asset: multi · horizon: days · conditions: small portfolio constraints · testable: yes · confidence: high
  ^MT128-C02-2
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** CTAs differ: some adjust position continuously for volatility changes, some size on volatility only at entry, which drives very different outcomes in parabolic moves.  #mech/risk_management
  > Um and also of course, some CTAs take volatility into account when they initially buy a position, but they don't make any further adjustments to that position as volatility changes.
  indicator: vol adjustment of existing positions · asset: multi · horizon: weeks · testable: yes: compare continuous vs entry-only vol scaling · confidence: high
  ^MT128-C02-3
- **Rob Carver** CTAs differ in how position size follows the trend signal: some take binary full-long or full-short positions, while others scale continuously with forecast strength; binary systems get much less benefit from forecast scaling when a trend ends abruptly.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > some CTAs will take basically binary positions, so they'll you know, they'll they'll kind of go from fully short to fully long
  indicator: forecast scaling versus binary signals · asset: multi · conditions: Design choice that decides exposure in a parabolic move. · testable: yes - binary versus continuous forecast scaling can be backtested · confidence: high
  ^MT128-C02-X1

### C03
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Rob bought silver in late Nov/early Dec as the forecast grew, then sold contracts on 31 Dec and the following Monday because volatility rose, so the position shrank into the crash while the trend signal stayed long.  #mech/risk_management _(time-bound view)_
  > on the 31st of December, I sold a contract and that would have been inevitably because the volatility increased
  indicator: silver futures, vol-scaled position · asset: commodities · horizon: weeks · conditions: during parabolic rises · testable: yes: vol-scaled position history · confidence: high
  ^MT128-C03-1
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Silver fell by the most in one day in 45 to 47 years on 30 Jan 2026, but a normal-speed trend system's signal stays long after one negative day.  #mech/slow_reaction _(time-bound view)_
  > even a day like Friday where silver dropped by the most in one day since
  indicator: silver price · asset: commodities · horizon: days · conditions: unless the trend system is very fast · testable: yes: trend persistence after one-day extremes · confidence: high
  ^MT128-C03-2
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Rob's silver trades (bought at $53 and $59, sold at $71 and $81) were profitable even though the price peaked at $110-120 before the crash, because the crash returned silver to levels of weeks earlier.  #mech/risk_management _(time-bound view)_
  > So I bought I bought into my silver position um at levels of 53 and 59 dollars per ounce respectively.
  indicator: silver · asset: commodities · horizon: weeks · testable: yes: single-trade anecdote · confidence: high
  ^MT128-C03-3
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Without continuous vol adjustment, silver grew as a share of the portfolio during the run-up, so the one-day drop caused a very large loss for such CTAs.  #mech/risk_management _(time-bound view)_
  > because what they would have done is seen the value of the silver in their portfolio kind of get bigger and bigger and bigger.
  indicator: position weight drift · asset: commodities · horizon: weeks · conditions: non-vol-adjusting, highly levered CTAs · testable: yes · confidence: high
  ^MT128-C03-4
- **Niels Kaastrup-Larsen (host)** One highly levered CTA without vol adjustment went from +72% to +27% on the month in one day on Freaky Friday.  #mech/risk_management _(time-bound view)_
  > think about being up 72% on the Thursday and ending the month up 27%.
  indicator: leveraged CTA returns · asset: commodities · horizon: days · conditions: high leverage, no vol scaling · testable: partly: single anecdote · confidence: medium
  ^MT128-C03-5
- **Rob Carver** A daily-rebalanced system sizes positions from the prior close, so on a gap day such as 30 Jan 2026 it cannot reduce exposure intraday; the loss is limited only because volatility-scaling had already cut the position in the days before.  #mech/risk_management _(added by sonnet-xhigh cross-check, time-bound view)_
  > I have a daily rebalance, so I didn't do any trading in silver during Friday itself cuz my position was based on Thursday's close
  indicator: daily rebalance using previous close, silver · asset: commodities · direction: position cut ahead of the crash by earlier volatility rises · horizon: days · conditions: Gap risk remains for any end-of-day system; only earlier vol-scaling protects it. · testable: yes - execution lag and gap losses are measurable · confidence: high
  ^MT128-C03-X1

### C04
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** If a volatility-based stop is raised as volatility rises, position size should be reduced simultaneously, otherwise risk increases.  #mech/risk_management
  > if you do increase your stop with you also should reduce your position at the same time
  indicator: volatility-scaled stop · asset: multi · horizon: weeks · testable: yes · confidence: high
  ^MT128-C04-1
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** A stop that does not widen with volatility risks being shaken out of a trend too early.  #mech/risk_management
  > Um if you don't increase your stop level as volatility rises, then you you you risk basically being shaken out the position too early.
  indicator: stop level vs volatility · asset: multi · horizon: weeks · testable: yes · confidence: high
  ^MT128-C04-2
- **Niels Kaastrup-Larsen** A trader using a hard stop based on the recent high (possibly vol-linked) could have been stopped out on the crash day itself, so whether a stop-loss rule helps in a parabolic reversal depends on its exact definition.  #mech/risk_management _(added by sonnet-xhigh cross-check, time-bound view)_
  > I guess you could have also been stopped out on freaky Friday because the move was so big
  indicator: stop-loss defined from the recent high · asset: commodities · direction: stop triggers on a large one-day fall · horizon: days · conditions: Depends on the stop rule and its volatility multiple. · testable: partly - stop rules can be backtested for gap days · confidence: medium
  ^MT128-C04-X1
- **Rob Carver** Even a volatility-widened stop would probably have been breached by a 25% one-day fall, so stops do not remove gap risk; the size of the position, not the stop, determines the loss.  #mech/risk_management _(added by sonnet-xhigh cross-check, time-bound view)_
  > a 25% fall probably still would have breached any reasonable stop
  indicator: vol-widened stop versus a 25% gap · asset: commodities · direction: stop breached in a crash · horizon: days · conditions: Gap moves bypass stops, so sizing is the main protection. · testable: yes - gap size versus stop distance is measurable · confidence: medium
  ^MT128-C04-X2
- **Niels Kaastrup-Larsen** After a long rally in precious metals, traders can become complacent and assume silver and platinum are as liquid as gold, but they are different markets with different liquidity and crash risk.  #mech/behavioral _(added by sonnet-xhigh cross-check, time-bound view)_
  > maybe become a little bit complacent thinking that these are all the same to trade
  indicator: silver and platinum versus gold liquidity · asset: commodities · direction: liquidity risk underestimated in the less liquid metals · horizon: months · conditions: Applies to crowded, extended rallies. · testable: partly - liquidity differences across metals can be measured · confidence: medium
  ^MT128-C04-X3
- **Rob Carver** A small account can use a broader liquidity filter than large CTAs and so holds instruments that big CTAs avoid or hold small, which gives it extra markets but also more exposure to thin-market liquidity gaps.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > I might kind of have a fairly broad liquidity filter
  indicator: liquidity filter relative to account size · asset: multi · conditions: Small accounts only; capacity limits large CTAs. · testable: yes - liquidity filter thresholds can be set from volume and open interest · confidence: high
  ^MT128-C04-X4

### C05
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Liquidity is not constant: after a run-up and a pullback the buyers are gone, so liquidity vanishes in crises, and more so in less-liquid markets.  #mech/liquidity_flows
  > people treat liquidity as a constant number as a constant number of volume of contracts they can expect to trade, but of course it isn't, right?
  indicator: volume and open interest · asset: commodities · horizon: days · conditions: less liquid markets, momentum-chasing entrants · testable: partly · confidence: high
  ^MT128-C05-1
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Judge liquidity over a one to two year history, not recent volume/open-interest spikes caused by tourists.  #mech/risk_management
  > what you really need to do is go back a year or 2 years and say, "Well, over a longer period of time, what does liquidity look like?"
  indicator: volume and open interest over 1-2 years · asset: commodities · horizon: months · conditions: hot markets with recent volume spikes · testable: yes · confidence: high
  ^MT128-C05-2
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** CTAs, risk parity and other quant strategies all cut exposure when vol spikes, so crowding amplifies volatility-driven sell-offs.  #mech/crowding_positioning
  > Um so anyone who sells on the hint of volatility spiking, the the more people there are in a particular market like that, the more it'll magnify the move.
  indicator: volatility-spike selling by quant funds · asset: multi · horizon: days · conditions: when many funds vol-adjust the same market · testable: partly: amplification is hard to isolate · confidence: medium
  ^MT128-C05-3
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Position sizing by volatility and diversification limited Rob's loss to 3% of account on the silver crash day, versus much larger for concentrated or unscaled funds.  #mech/risk_management
  > Um and the two key things about risk management are position sizing um and diversification.
  indicator: position sizing, diversification · asset: multi · horizon: days · testable: yes · confidence: high
  ^MT128-C05-4
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** A 3% one-day loss was in line with other CTAs at similar annual vol.  #mech/risk_management _(time-bound view)_
  > Um so on Friday, I lost 3% of my total account value because I have a reasonably diversified portfolio.
  indicator: single-day loss · asset: commodities · horizon: days · testable: yes · confidence: high
  **Correction (cross-check):** Wrong speaker. The comment that a 3% one-day loss was in line with other CTAs at similar annual volatility is Niels's, based on what he saw from managers he follows; Rob only reported his own 3% loss. → Niels Kaastrup-Larsen: a 3% loss on the crash day was very decent for a trend manager at that annual volatility, matching what he saw from the managers he can follow.
  ^MT128-C05-5
- **Rob Carver** Rob says the lesson of the silver crash is risk management, and its two key elements are position sizing and diversification, rather than explaining why silver fell more than gold.  #mech/new _(added by map cross-check)_
  > the two key things about risk management are position sizing um and diversification
  indicator: position size, diversification · asset: commodities · testable: partly - loss on crash day by sizing method · confidence: high
  ^MT128-C05-R1

### C06
- **Niels Kaastrup-Larsen (host)** Larger CTAs were reducing silver notional as volatility expanded, so they dampen rather than cause parabolic moves.  #mech/risk_management _(time-bound view)_
  > the majority of the larger CTAs, they're they're the ones who've been selling silver all the way through January, as you rightly said
  indicator: CTA silver positions · asset: commodities · horizon: weeks · testable: partly: CTA positioning data · confidence: medium
  ^MT128-C06-1
- **Niels Kaastrup-Larsen (host)** Hunt brothers silver 1979: leveraged buying with borrowed money, exchange margin hikes and a rise from $6 to $50 ended in catastrophe; pyramiding and leverage repeat across eras.  #mech/risk_management
  > he kept buying now for borrowed money. So, the leverage of his position became, you know, quite high.
  indicator: silver margin requirements · asset: commodities · horizon: years · conditions: parabolic markets with leverage and rising margins · testable: no: historical anecdote · confidence: medium
  ^MT128-C06-2
- **Niels Kaastrup-Larsen (host)** Exchanges raise margins in parabolic moves, forcing leveraged holders to liquidate (seen in 1979 and again in Jan 2026).  #mech/liquidity_flows
  > So, COMEX started to change the rules on margins.
  indicator: exchange margin changes · asset: commodities · horizon: days · testable: partly: margin changes are public · confidence: medium
  ^MT128-C06-3
- **Niels Kaastrup-Larsen (host)** Managers with decades of experience avoid emotional attachment and manage risk systematically.  #mech/behavioral
  > We manage our risk in a systematic, dispassionate way.
  asset: multi · testable: no · confidence: medium
  ^MT128-C06-4

### C07
- **Niels Kaastrup-Larsen (host)** Only about 30% of silver supply is mined as silver, so supply is less controllable and the market more volatile than gold.  #mech/structural_shift
  > It's only like 30% of the production actually every year is specifically mined as silver. The rest comes from a byproduct of gold and copper.
  indicator: silver supply share · asset: commodities · direction: silver more volatile than gold · horizon: years · testable: partly: supply structure data · confidence: low
  ^MT128-C07-1
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** The 30 Jan week saw dislocations across markets: quant equity factors, Bitcoin and AI stocks, while Rob's trend portfolio coped.  #mech/crowding_positioning _(time-bound view)_
  > long short quant equity factors have gone a balmy
  indicator: equity factor returns · asset: multi · horizon: days · testable: partly · confidence: medium
  ^MT128-C07-2
- **Niels Kaastrup-Larsen (host)** March natural gas gained 60% then lost 26% in a day on weather, showing large reversals outside precious metals.  #mech/overshoot _(time-bound view)_
  > from the 9th of January to the 30th of January, it um was up something like 60%. And then on the 2nd of February, in 1 day, it lost 26%.
  indicator: natural gas futures · asset: commodities · horizon: days · conditions: weather events · testable: yes · confidence: high
  ^MT128-C07-3
- **Niels Kaastrup-Larsen (host)** Commodities in a trend universe provide opportunities often independent of equity risk-off events.  #mech/structural_shift
  > people need to realize how important it is to have the commodities as part of their trend following universe because this is where we sometimes see lots and lots of opportunities
  indicator: commodity trend returns · asset: commodities · direction: include commodities in trend universe · horizon: years · testable: yes · confidence: high
  ^MT128-C07-4
- **Niels Kaastrup-Larsen** Kevin Warsh was named as the nominee for Fed chair around the time of the 30 January 2026 silver crash, a surprise relative to expectations, and was taken by many as the proximate cause of the precious-metals sell-off.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > if confirmed, we will have a new Fed chair with the name of Kevin Walsh
  indicator: Fed chair nomination · asset: rates · direction: tighter policy narrative for precious metals · horizon: months · conditions: Time-bound event; the speakers doubt it was the real cause. · testable: no - single event · confidence: high
  ^MT128-C07-X1

### C08
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Rob discretionarily sold equities in the April 2025 tariff tantrum and lost relative performance; systematic Rob did better.  #mech/behavioral _(time-bound view)_
  > did something very silly and non systematic and sold all of my equities
  asset: equities · horizon: months · testable: partly: anecdote of discretionary override · confidence: high
  ^MT128-C08-1
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** The bond market reaction to the new Fed chair nomination was muted (no 50bp two-year move), so it was probably not the genuine cause of the silver crash.  #mech/policy_reaction _(time-bound view)_
  > which is what you would have expected if this genuinely was a like a a novel and interesting piece of information
  indicator: two-year yield on nomination day · asset: rates · horizon: days · testable: yes: event-day yield change · confidence: medium
  ^MT128-C08-2
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Whether the new Fed chair will cut rates for the president or act independently is unknowable, though he is seen as relatively sane and possibly hawkish.  #mech/policy_reaction _(time-bound view)_
  > No one really knows what's going to happen, uh, in May.
  indicator: Fed chair independence · asset: rates · horizon: months · testable: no · confidence: medium
  ^MT128-C08-3
- **Rob Carver** The Fed chair nominee holds less mainstream views on QE and the Fed balance sheet but is seen as conventional or even hawkish on interest-rate setting, so the policy mix could differ from what the president wants.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > he does he does have some opinions that are less mainstream around things like QE and the Fed balance sheet
  indicator: Fed balance sheet and QE policy · asset: rates · direction: policy uncertainty rather than clear direction · horizon: months · conditions: Depends on confirmation and how the board votes. · testable: no - forecast of future policy · confidence: medium
  ^MT128-C08-X1
- **Rob Carver** Markets have largely shrugged off the president's policy shocks since early 2025, partly because of a 'TACO' pattern (he backs down) and because many do not take threats seriously, so Rob's initial expectation of a bad market was wrong.  #mech/behavioral _(added by sonnet-xhigh cross-check, time-bound view)_
  > Trump always chickens out of the taco trade
  indicator: equity reaction to tariff and policy announcements · asset: equities · direction: dips on policy shocks recover · horizon: months · conditions: Observed over the first year; may not hold if a shock is not reversed. · testable: partly - post-announcement returns can be studied · confidence: medium
  ^MT128-C08-X2

### C09
- **Niels Kaastrup-Larsen (host)** The silver sell-off was driven by crowded positioning, including Chinese retail, rather than the Fed chair news.  #mech/crowding_positioning _(time-bound view)_
  > I think it had much more to do with positioning and how people had been piling into this
  indicator: silver positioning · asset: commodities · horizon: days · testable: partly · confidence: medium
  ^MT128-C09-1
- **Niels Kaastrup-Larsen (host)** Systematic diversification beats discretionary attempts to interpret political and market events.  #mech/behavioral
  > being a systematic diversified investor, I think is so much better than trying to make any sense of this from a discretionary point of view
  asset: multi · testable: partly: discretionary vs systematic comparisons · confidence: medium
  ^MT128-C09-2
- **Niels Kaastrup-Larsen (host)** Alphabet doubling AI capex to $185 billion suggests a possible bubble.  #mech/overshoot _(time-bound view)_
  > Google said that it's planning to double its CapEx this year to as much as $185 billion to really bet huge on AI.
  indicator: hyperscaler capex · asset: equities · horizon: years · testable: partly · confidence: low
  ^MT128-C09-3
- **Rob Carver** A president's appointment says little about a Fed chair's later independence: Powell was appointed by Trump and then resisted pressure, and once in office chairs cannot be removed and care about their legacy.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > let's not forget it was Trump who appointed Powell
  indicator: Fed chair independence · asset: rates · direction: appointee may act against the appointer's wishes · horizon: years · conditions: Depends on legal protection of the Fed from removal. · testable: no - qualitative political reasoning · confidence: medium
  ^MT128-C09-X1
- **Niels Kaastrup-Larsen** The Fed chair is one of 12 FOMC votes and cannot set rates alone; the real independence risk is a pending Supreme Court ruling that may let the president remove governors and pack the board.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > it's not like he can decide what interest rates are going to do
  indicator: FOMC voting structure, Supreme Court ruling on Fed removal · asset: rates · direction: independence risk if the ruling favours the president · horizon: months · conditions: Time-bound legal decision. · testable: no - depends on a court ruling · confidence: medium
  ^MT128-C09-X2

### C10
- **Niels Kaastrup-Larsen (host)** A trend barometer of 64 means 64% of tracked markets trend, indicating broad trend breadth that is supportive for CTAs.  #mech/slow_reaction _(time-bound view)_
  > there's a lot of breath because the percentage or 64 means that there are 64 of the market that in the portfolio it tracks that are quote-unquote trending
  indicator: trend barometer · asset: multi · horizon: weeks · testable: yes · confidence: high
  ^MT128-C10-1
- **Niels Kaastrup-Larsen (host)** February 2026 trend profits came from equities, currencies, fixed income, natural gas, meats and grains, a broad base.  #mech/slow_reaction _(time-bound view)_
  > the financial sectors like equities, a bit of currency, some of the fixed income markets even are supporting the um um P&L this month
  indicator: sector P&L contributions · asset: multi · horizon: weeks · testable: yes · confidence: medium
  ^MT128-C10-2
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Most CTAs trading Bitcoin futures were likely short after the sell-off.  #mech/crowding_positioning _(time-bound view)_
  > Um most CTAs who trade it would probably be short.
  indicator: Bitcoin futures trend · asset: other · direction: short Bitcoin · horizon: days · testable: partly · confidence: medium
  ^MT128-C10-3
- **Niels Kaastrup-Larsen (host)** Early Feb 2026: BTOP50 +5.38% YTD, SG CTA +5%, SG Trend +5.25%, short-term traders +2.37%, MSCI World +1.76%, S&P 500 +0.63% YTD.  #mech/slow_reaction _(time-bound view)_
  > Beta 50 up 33 basis points, up 5.38% so far this year, so very strong.
  indicator: BTOP50, SG indices, MSCI World, S&P 500 · asset: multi · horizon: months · testable: yes: public index data · confidence: high
  ^MT128-C10-4
- **Rob Carver** A system that scales positions with forecast strength runs higher realised risk when many markets trend strongly, so portfolio risk rises with trend breadth (the barometer).  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > my risk is a little bit higher than it has been for a while, so that kind of matches up with your trend barometer
  indicator: portfolio risk versus trend barometer · asset: multi · direction: risk rises when breadth of trends is high · horizon: weeks · conditions: Applies to continuous forecast-scaled systems. · testable: yes - realised vol versus trend breadth can be tested · confidence: medium
  ^MT128-C10-X1
- **Rob Carver** Bitcoin futures are Rob's biggest short position in early February 2026.  #mech/new _(added by map cross-check, time-bound view)_
  > that's especially my biggest short position at the moment
  indicator: trend signal on Bitcoin futures · asset: crypto · direction: short · horizon: months · testable: no · confidence: high
  ^MT128-C10-R2

### C11
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** With vol-targeted instruments, portfolio risk depends only on correlations; diversification means you must scale up positions to hit the book risk target.  #mech/risk_management
  > if you're targeting say a 15% risk target on each of them, you'll end up with a 15% risk target on the entire book cuz it's perfectly correlated.
  indicator: portfolio correlation, instrument diversification multiplier · asset: multi · testable: yes · confidence: high
  ^MT128-C11-1
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Compensating for diversification across instruments requires multiplying positions by about four to five; without it a 15% target gives about 3%.  #mech/risk_management
  > I get numbers of between four and five.
  indicator: diversification multiplier · asset: multi · testable: yes · confidence: high
  ^MT128-C11-2
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** The 0.7 figure in Rob's book is the ratio of trend-strategy correlation to underlying return correlation, not a fixed book correlation.  #mech/research_method
  > 0.7 is actually um roughly speaking the ratio between the correlation between the underlying instrument returns and the correlation between what happens if you trend follow those those instruments
  indicator: trend vs underlying correlation ratio · asset: multi · testable: yes · confidence: medium
  ^MT128-C11-3
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Estimate book correlation from the combined P&L streams over a rolling 6-month window, optionally exponentially weighted; this includes asset and signal correlation.  #mech/research_method
  > you can use you can get can just use a rolling estimation window of about 6 months works quite well
  indicator: rolling correlation window 6 months · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT128-C11-4

### C12
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Volatility and correlation have different predictability, so estimate them separately and combine them into the covariance matrix.  #mech/research_method
  > it's better to estimate them separately and then combine them together if that's what you want to do.
  indicator: volatility, correlation, covariance estimation · asset: multi · testable: yes · confidence: high
  ^MT128-C12-1
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Volatility is predictable (R-squared about 0.35 month-on-month), correlation less so (0.2-0.25), and means are unpredictable noise.  #mech/research_method
  > if you do a regression of next month's volatility on last month's volatility, you get an R squared of about 0.35.
  indicator: predictability R-squared of vol, correlation, mean · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT128-C12-2
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Use about a 6-month window for correlation and about 1 month for volatility, since correlation structure changes more slowly.  #mech/research_method
  > you probably only use something like about a 6-month rolling estimate versus about a 1-month rolling estimate for vol
  indicator: estimation windows · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT128-C12-3
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** When instruments are already vol-targeted, portfolio construction only needs correlations.  #mech/risk_management
  > the nice thing about doing things in a vol targeted way is you you don't need to estimate vols again.
  indicator: vol targeting · asset: multi · testable: yes · confidence: high
  ^MT128-C12-4
- **Rob Carver** Extra trading caused by updating a slow (six-month) correlation estimate is negligible compared with the trading caused by signals, so a time-varying estimate has little cost compared with a fixed assumption.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > as long as your correlation estimate's quite slow, like 6 months is pretty good, then that's going to be al- effectively irrelevant
  indicator: correlation estimate turnover · asset: multi · horizon: months · conditions: Slow estimation window of about six months. · testable: yes - turnover from estimate changes can be measured · confidence: medium
  ^MT128-C12-X1

### C13
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** The Man AHL paper classifies trend markets by liquidity and complexity into traditional, alternative and esoteric (China futures, physical crypto) and studies where returns come from.  #mech/structural_shift
  > we're going to divide um our market universe into three categories: traditional markets, alternative markets, and alternative esoteric markets.
  indicator: market universe categories · asset: multi · testable: yes · confidence: high
  ^MT128-C13-1
- **Niels Kaastrup-Larsen** The Man AHL paper argues that differences between trend managers come mainly from which markets they trade (the market universe), not from better models or faster signals.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > this is a paper about not really about better models or faster signals
  indicator: market universe versus model speed · asset: multi · conditions: Paper's central thesis; evidence in factor and idiosyncratic decomposition. · testable: yes - testable by comparing universe versus speed contributions · confidence: high
  ^MT128-C13-X1

### C14
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** A large part of trend returns is a risk-on/risk-off factor (as in 2008: bonds up, equities down), and the remainder is idiosyncratic.  #mech/risk_premium
  > following portfolio is actually coming from my kind of risk on risk off factor, which I'm trend following.
  indicator: PCA first principal component of trend returns · asset: multi · horizon: years · testable: yes: PCA decomposition · confidence: high
  ^MT128-C14-1
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Traditional CTA returns are about 55% factor and 45% idiosyncratic.  #mech/risk_premium
  > 45% idiosyncratic, 55% factors
  indicator: factor vs idiosyncratic share · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT128-C14-2
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Alternative and esoteric markets are about one third factor and two thirds idiosyncratic, so they add weird, diversifying sources of return.  #mech/risk_premium
  > in these unusual markets, these these alternative and these esoteric markets, it's more like 1/3 2/3
  indicator: idiosyncratic return share · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT128-C14-3
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** An unconstrained Sharpe-maximising optimisation puts about 30% in traditional markets and 70% in alternatives (about 5% in crypto), although large CTAs cannot do this because of capacity.  #mech/risk_management
  > only about 30% of their portfolio needs to should be going into these traditional markets
  indicator: unconstrained portfolio optimisation · asset: multi · horizon: years · conditions: liquidity and capacity constraints ignored · testable: yes · confidence: high
  ^MT128-C14-4
- **Rob Carver** January 2026 trend profits did not come from the risk-on/risk-off factor (bonds flat, equities slightly up) but from idiosyncratic sources such as gold, silver and natural gas, an example of returns from alternative-style markets.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > that kind of first principal component didn't contribute much
  indicator: first principal component of trend returns, January 2026 · asset: multi · direction: idiosyncratic metals and gas drove returns · horizon: months · conditions: Month-specific example. · testable: yes - PCA decomposition can be repeated on the index · confidence: medium
  ^MT128-C14-X1

### C15
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Optimising for periods when equities fell gives a different answer than the generic optimisation, because investors buy trend for tail protection.  #mech/risk_management
  > let's focus in on periods when equity markets fell.
  indicator: conditional optimisation in equity drawdowns · asset: multi · horizon: years · conditions: for investors using CTAs as crisis alpha · testable: yes · confidence: high
  ^MT128-C15-1
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** For crisis protection the optimal portfolio is about 50% traditional markets because their high factor share (short equities, long bonds) pays in crises.  #mech/risk_premium
  > You want to have 50% traditional markets
  indicator: traditional market weight in crisis-conditional portfolio · asset: multi · direction: long trend in traditional futures for crisis alpha · horizon: years · conditions: when diversifying a 60/40 portfolio · testable: yes · confidence: high
  ^MT128-C15-2
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** In a crisis a CTA needs large bets on short equities and long bonds, not exotic markets.  #mech/risk_premium
  > because in a crisis um you basically want to just make fairly big bets on going 2008, going short equities, long bonds.
  indicator: crisis trend positions · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT128-C15-3
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Many alternative markets trade like risk-on assets, and may be hard to short or illiquid in a crisis.  #mech/liquidity_flows
  > Um, because a lot of these things in a crisis you do want to go short, because a lot of them trade like risk-on assets.
  indicator: alternative market shortability · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT128-C15-4

### C16
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Futures trading uses only about 20-30% of cash as margin, making CTAs cash efficient; alternative markets need more margin.  #mech/structural_shift
  > Um, I'm only using 30% of my cash as margin. So, you know, a typical CTA, that number's 20%, and that's super cash efficient.
  indicator: margin to equity · asset: multi · testable: yes · confidence: high
  ^MT128-C16-1
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Adding cash efficiency as a constraint shifts the optimum to about 70% traditional futures and 30% alternatives.  #mech/risk_management
  > So, we end up with 70% in traditional markets and just just 30% in the the old the alternative markets.
  indicator: margin-constrained optimisation · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT128-C16-2
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Cash efficiency matters most when cash is needed: in 2008 investors drew on CTAs as a source of ready cash.  #mech/liquidity_flows
  > So, you know, in 2008, the fact that CTAs had plenty of cash, daily liquidity, no gating meant that many people used them as cash machines
  indicator: CTA redemptions in crises · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT128-C16-3
- **Niels Kaastrup-Larsen (host)** To maximise standalone long-term Sharpe, trade more (including alternative) markets; to get equity-crisis protection, choose managers focused on traditional liquid futures.  #mech/risk_management
  > you would go for a portfolio that probably trades more markets
  indicator: market universe choice · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT128-C16-4

### C17
- **Niels Kaastrup-Larsen (host)** Manager selection depends on investor objective: choose a traditional-futures manager for tail protection and cash needs.  #mech/research_method
  > what's the best manager fit for me in terms of what my objective is with investing with the CTA
  asset: multi · testable: no · confidence: medium
  ^MT128-C17-1
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** Systematic finance has always used supervised machine learning in the form of regression and optimisation, blending into unsupervised and neural-network methods.  #mech/research_method
  > all the systematic finance is machine learning
  asset: multi · testable: no: definitional · confidence: medium
  ^MT128-C17-2
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** FT Alphaville thesis: finance quants and AI labs converge in workflow, hiring and technology stack.  #mech/structural_shift
  > their sort of thesis is that that basically these people are becoming more and more like each other
  asset: other · horizon: years · testable: no · confidence: low
  ^MT128-C17-3

### C18
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** AI works best in tightly defined areas such as execution research, where tick data is rich and fits non-linear models; much of fund AI is marketing or blue-sky.  #mech/research_method
  > I think the people who are doing it best are ones who are using it in very tightly defined areas.
  indicator: execution research with tick data · asset: other · testable: partly · confidence: medium
  ^MT128-C18-1
- **Rob Carver (systematic futures trader, author, ex-AHL/AQR)** AI researchers now get non-competes, gardening leave and nine-figure offers, exceeding quant pay.  #mech/structural_shift _(time-bound view)_
  > many of the top AI researchers are making far more money than than any person quant in finance is
  asset: other · horizon: years · testable: no · confidence: medium
  ^MT128-C18-2
- **Rob Carver** Rob thinks the FT Alphaville article slightly overstates how much AI is used in quant finance, probably because its authors are talking their own book.  #mech/new _(added by map cross-check)_
  > this is probably cuz they're talking their own book
  indicator: AI use in systematic funds · asset: multi-asset · testable: no · confidence: medium
  ^MT128-C18-R3

