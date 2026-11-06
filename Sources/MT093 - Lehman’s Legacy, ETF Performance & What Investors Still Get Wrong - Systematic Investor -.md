---
source_id: MT093
title: "Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor - Ep.366"
date: 2025-09-27
channel: "Top Traders Unplugged"
url: 
words: 11562
claims: 66
added_by_crosscheck: 16
corrections: 2
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Rob Carver (systematic trader, author)", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor - Ep.366

**Speakers:** Rob Carver (systematic trader, author); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** Systematic Investor episode on institutional entry into managed futures, position sizing without leverage, why not to currency-convert prices, and the gap between fund and investor returns (YieldMax, Morningstar). Main conclusion: do not time in and out of strategies; use all data rather than a recent window, and hold trend following despite weak recent results.

**Approach:** trend following, CTA, position sizing, investor behavior, research method

**Cross-check completeness estimate of first read:** 0.85 - first reader (80 claims) captured nearly all of the methodological content (sizing, FX conversion, window length, investor returns); misses are supporting data points, a few reasoning links, and one hosts' view on bond risk premia.

## Argument map

**Episode thesis:** Rob Carver argues that systematic discipline means testing claims rather than telling stories: investors systematically earn less than the funds they hold because they chase returns (YieldMax ETF, Morningstar 1.7% gap), instrument-by-instrument claims about trend lack significance, and 'the world has changed' stories about weak CTA returns cannot be backtested, so the default is to use the full history and buy and hold strategies. Niels Kaastrup-Larsen adds the industry view that trend survives by adapting, that lower index volatility explains lower returns, and that large asset managers' entry signals interest; the episode also answers listener questions on cash-only sizing and currency conversion.

### Rob Carver (Independent systematic trader, author (position sizing, trading without leverage), consultant to a crypto hedge fund)
Fingerprint: #approach/research_robustness_overfitting #approach/position_sizing_vol_target #approach/trend_following #approach/behavioral_sentiment #approach/portfolio_construction_stacking #approach/manager_selection_allocation #approach/diversification_risk_parity
_Speaker note: Rob Carver (UK). Ledger C02-2 (allocators giving money after losses) has Rob stating the hedge-fund half while Niels adds that CTA allocation behaves oppositely. Ledger C02-1 corrected: the Morgan Stanley note details are Niels's; Rob only mentions the sell-side Lehman note via the FT Alphaville article. C05-X3 (gilt yields 27-year high, UK vs EU inflation) is ambiguous between Rob and Niels in captions; assigned to Rob in the first part of that exchange (Rob continues "it can't just be a debt story, it must be an inflation story")._

**Worldview premises**
- Statistical evidence is the arbiter: claims that trend works better on some instruments than others usually fail significance tests, and testing 250 instruments will find a few that look significant by chance. _[empirical, stated; support: Own testing practice: overlay return distributions and run a test.]_ ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C08-3|C08-3]])
- Cash (dollar-weighted) investor returns trail fund returns because investors pile in before losses and leave before gains; the gap is larger for strongly skewed funds and worst in sector equity funds. _[empirical, stated; support: YieldMax coin option income ETF (42% fund gain, investors lost about 35.5m on 2.5bn net inflows) plus Morningstar average gap of 1.7% a year over 10 years and 4.4% for sector equity funds.]_ ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C09-2|C09-2]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C10-1|C10-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C10-2|C10-2]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C11-1|C11-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C11-2|C11-2]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C11-3|C11-3]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C12-1|C12-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C12-2|C12-2]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C12-3|C12-3]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C10-R1|C10-R1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C10-X1|C10-X1]])
- Persistence and autocorrelation of strategy returns are weak, so there is no reliable conditioning variable to forecast CTA performance over the next 12 months; people are poor at timing in and out of funds. _[empirical, stated; support: Review of persistence evidence; the persistence-scorecard debate is unsettled.]_ ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C13-1|C13-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C13-X1|C13-X1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C15-1|C15-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C12-3|C12-3]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C16-5|C16-5]])
- Out-of-sample performance degrades as the fitting window shrinks, nonlinearly: 50 years is good, 20-40 almost as good, 2-3 much worse. _[empirical, stated; support: General statistics of optimisation; extreme 10-day example.]_ ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C15-2|C15-2]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C15-3|C15-3]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C15-X1|C15-X1]])
- "The world has changed" stories for weak CTA returns (Trump policy, more algorithmic trading, efficient markets) are narratives indistinguishable from bad luck unless a testable, backtestable method exists. _[theoretical, stated; support: Using only the last 2-3 years of data smuggles in future information.]_ ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C14-2|C14-2]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C14-X1|C14-X1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C13-2|C13-2]])
- Even if rolling trend returns look degraded, the difference is not statistically significant, and for a low-Sharpe strategy it could take another 50 years to know. _[empirical, stated; support: Statistical power argument.]_ ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C16-4|C16-4]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C16-3|C16-3]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C16-5|C16-5]])
- The default should be to buy and hold assets, funds, strategies or factors unless one can convincingly show that timing adds value. _[theoretical, stated; support: All evidence he has seen shows investors time badly.]_ ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C16-6|C16-6]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C12-3|C12-3]])
- Developed-market bond sell-offs on debt worries are the dog that has never barked; UK yields above Italy's with worse Italian debt/GDP show UK weakness is inflation, not debt alone. _[empirical, stated; support: Truss exception; UK vs Italy yield comparison.]_ ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-4|C05-4]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C06-1|C06-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-X3|C05-X3]])
- A model-driven systematic book can contradict the trader's gut views and cost money if the gut is right; he is comfortable with that. _[experience, stated; support: His own long bond position versus bearish discretionary view on Fed independence.]_ ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-2|C05-2]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-5|C05-5]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-X2|C05-X2]])
- Passive has largely won the passive-versus-active debate. _[empirical, stated; support: Persistent long-term rise in the share of assets in passive strategies.]_ ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C12-X1|C12-X1]])
- Trend following works well on cryptocurrencies, with no guarantee for the future. _[experience, stated; support: His testing and a crypto hedge fund he advises.]_ ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C09-1|C09-1]])

**Chain: Why fund returns exceed investor returns**
1. Fund shows persistent gains (negative-skew strategy, e.g. option income) → Flows chase it: Investors buy after persistent gains ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C11-3|C11-3]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C10-2|C10-2]])
2. Large flows arrive just before the big loss (and leave before gains in positively skewed funds) → Aggregate cash return is far below the percentage return: Dollar-weighting: more money present when losses occur ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C10-2|C10-2]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C10-1|C10-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C11-1|C11-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C10-X1|C10-X1]])
3. Gap summed over a decade → Investor return trails fund return by 1.7% a year across US funds and 4.4% in sector equity funds: News and emotion (e.g. AI theme) drive buying after rallies ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C12-1|C12-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C12-2|C12-2]])
- Evidence: Stylised 51-week example; YieldMax net flows and loss; Morningstar study of all US funds over 10 years.
- Fails when: Funds where investors beat the fund are probably lucky; effect smaller for lower-skew funds and in buy-and-hold with no flows.

**Chain: Should an allocator give up on trend because the world has changed**
1. Allocator uses the full 50-year history with equal weight → Blend of trend with 60/40 improves mean, volatility, drawdown and Sharpe: Equal treatment assumes no structural change ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C14-1|C14-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C03-2|C03-2]])
2. Allocator instead fits only the last 2-3 years → Trend allocation falls towards zero: Misses 2022; choice of window cannot have been made in advance, so it is polluted by future information ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C14-2|C14-2]])
3. Rule-based shorter windows (10, 5, 3 years) → Worse out-of-sample results: Optimisation needs data; noise dominates ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C15-2|C15-2]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C15-3|C15-3]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C15-X1|C15-X1]])
4. Persistence and autocorrelation are weak → No testable conditioning variable: So default remains buy and hold ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C15-1|C15-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C16-6|C16-6]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C13-1|C13-1]])
- Evidence: Own 50-year backtest back to 1970; backfilled trend indexes by replication; general statistics.
- Fails when: If a backtestable, genuinely out-of-sample timing signal existed he would reconsider; none found.

**Chain: Currency conversion before trend following**
1. Convert foreign price to home currency → Signal blends asset trend and FX trend: Falling pound makes US ETF look stronger ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C08-X1|C08-X1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C08-2|C08-2]])
2. Blend plus separate FX trade → Diversification lost and correlation to FX trade rises: One instrument in place of two ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C08-2|C08-2]])
3. Futures only convert margin → FX exposure is a fraction of notional and can be traded separately: Margin of roughly 20-25% ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C08-4|C08-4]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C08-1|C08-1]])
- Evidence: Reasoning; admits he has not tested the performance difference.
- Fails when: Works only if trend works better on the combined series than on the two separately, which he doubts.

**Chain: Cash-only position sizing with forecast scaling**
1. Forecast-scaled positions sum above 100% of capital → Either halve every position or cap forecasts at the average (10) instead of 20: Halving gives average 50% invested ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C06-2|C06-2]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C07-1|C07-1]])
2. Halving applied to a liquid S&P 500 portfolio → Risk target falls from about 25% to 12.5%, probably too low: Fine for 50%-vol emerging-market stocks (25% target) ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C06-3|C06-3]])
3. Capping at 10 → Weak forecasts shrink positions and cash creeps back; stronger-than-average cannot add: Reallocating cash is optimal in theory but rarely worth the complexity ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C07-1|C07-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C07-2|C07-2]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C06-X1|C06-X1]])
- Evidence: Own sizing framework; details deferred to forthcoming book.
- Fails when: Where cash constraints force less information from forecast strength.

**Decision process**
- [sizing] Position size scales with forecast strength (average forecast 10, cap 20); in cash-only accounts cap at 10 or halve all positions depending on the volatility of the instruments.. Why: Preserves risk target when leverage is unavailable. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C06-2|C06-2]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C06-3|C06-3]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C07-1|C07-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C07-2|C07-2]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C06-X1|C06-X1]])
- [signal] Trend-follow the local-currency price and trade FX as a separate instrument; do not convert price series into home currency first.. Why: Retains diversification between asset and currency trends. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C08-1|C08-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C08-2|C08-2]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C08-X1|C08-X1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C08-4|C08-4]])
- [universe] Do not drop or favour instruments because trend "works better" on them unless a significance test says so.. Why: With 250 instruments some look significant by chance. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C08-3|C08-3]])
- [research] Treat anecdotes as hypotheses to test for generality; do not extrapolate.. Why: Quant discipline. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C11-4|C11-4]])
- [portfolio] Allocator default: use full-history (since 1970) equal-weight evidence for blending trend with 60/40; build a backfill trend index by replication if needed.. Why: Avoids hindsight windows. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C14-1|C14-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C14-2|C14-2]])
- [risk] Currently running about 50-60% of typical risk because clear trends are lacking; long equities, FX, bonds, short energy and Bitcoin.. Why: Model-dictated risk when trends are weak. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-1|C05-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-2|C05-2]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-X2|C05-X2]])
- [portfolio] Buy and hold funds, strategies and factors; do not time in and out unless timing is convincingly proven.. Why: Evidence that investors time badly. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C16-6|C16-6]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C12-3|C12-3]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C13-1|C13-1]])

**Evidence style:** Statistical testing and first principles; stylised numerical examples; published studies (Morningstar investor-return gaps); explicit humility about macro views and about untested claims.

**Views at the time**
- (2025-09-26) Long equities, FX and bonds and short energy and Bitcoin in his systematic book at about 50-60% of typical risk; no very clear trends yet.. Reasoning: Model output as of the show. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-1|C05-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-X2|C05-X2]])
- (2025-09-26) Rates markets underprice bad news such as threats to Fed independence, yet his systematic book stays long bonds and will lose if his gut is right.. Reasoning: Discretionary gut versus model. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-2|C05-2]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-5|C05-5]])
- (2025-09-26) Big asset managers (BlackRock, Fidelity) entering trend products will likely allocate model-portfolio flows to their own trend products; the timing may be dip-buying after weak trend years.. Reasoning: Curiosity about why they did not launch 10-15 years ago. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C03-3|C03-3]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C04-1|C04-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C03-2|C03-2]])
- (2025-09-26) UK bond weakness is an inflation story, not only debt (gilts above Italy), and gilt yields hit 27-year highs.. Reasoning: UK vs Italy yield comparison. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C06-1|C06-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-X3|C05-X3]])
- (2025-09-26) Trend following on crypto works fine; he is writing a book on trading without leverage.. Reasoning: Own testing. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C09-1|C09-1]])
- (2025-09-26) Whether trend has stopped working cannot be settled statistically; belief matters, and the default is buy and hold.. Reasoning: Low-Sharpe strategy needs decades of data. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C16-4|C16-4]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C16-5|C16-5]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C16-6|C16-6]])

### Niels Kaastrup-Larsen (Host of Top Traders Unplugged; veteran CTA/hedge fund investor, works with Dawn Capital)
Fingerprint: #approach/trend_following #approach/manager_selection_allocation #approach/policy_reaction_central_banks #approach/fiscal_dominance #approach/behavioral_sentiment #approach/regime_detection
_Speaker note: Host who also states views (trend barometer, performance data, Fed commentary, bond risk premium, adaptability of trend). Ledger C02-1 corrected: the Morgan Stanley note details are his. C04-3 corrected: the 50-60% risk is Rob's._

**Worldview premises**
- Trend following survives structural change because it adapts through continuous research, though 1970s rules should not be applied unchanged. _[experience, stated; support: 51 years of trend following at the firm he works with and the Barclay CTA index volatility history.]_ ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C16-1|C16-1]])
- Lower CTA index returns reflect lower index volatility (above 25% in the 1970s-80s, below 5% now), so lower returns are expected. _[empirical, stated; support: Rolling volatility of the Barclay CTA index in the Dawn paper.]_ ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C16-2|C16-2]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C16-3|C16-3]])
- With large fiscal deficits and rising debt almost everywhere, many government bond markets should carry a higher risk premium. _[theoretical, stated; support: Debt trajectories; UK gilt yield highs.]_ ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-X1|C05-X1]])
- Divergence in CTA bond positioning arises because carry matters more for bonds than for equities, so the carry weight changes positions relative to trend. _[theoretical, stated; support: Observed daily moves across ETFs and mutual funds.]_ ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-3|C05-3]])
- Large-manager entry into trend products signals growing institutional interest; the standard case for managed futures is diversification and crisis protection without outperforming in every environment. _[experience, stated; support: Reads the Fidelity paper conclusion.]_ ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C02-4|C02-4]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C03-1|C03-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C04-2|C04-2]])
- CTA allocation behaves oppositely to hedge-fund allocation: investors do not add to CTAs after losses. _[experience, stated; support: Industry experience.]_ ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C02-R1|C02-R1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C02-2|C02-2]])

**Decision process**
- [research] Tracks a trend barometer (41, improving but weak) and index performance to gauge the trend environment.. Why: Gives a read on how strong trends are. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C04-3|C04-3]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C04-4|C04-4]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C04-5|C04-5]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C04-X1|C04-X1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C04-X2|C04-X2]])

**Evidence style:** Industry data and published papers; track record of long-lived trend firms; read-outs of index numbers.

**Views at the time**
- (2025-09-18) Fed cut 25bp in September 2025 with Miran dissenting for 50 and Waller (a contender for chair) not dissenting; Powell did not signal capitulation to many cuts.. Reasoning: Dissent pattern and press conference. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C02-3|C02-3]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C02-X1|C02-X1]])
- (2025-09-26) Trend barometer at 41, improving over 10 days but still weak; CTA gains from equity and gold trends; CTA indices still negative YTD (CTA -3.62%, SG Trend about -4%, Beta 50 -0.45%) versus MSCI World +16.6% and S&P 500 TR +13.29%, with bonds +6.25%.. Reasoning: Index data. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C04-3|C04-3]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C04-4|C04-4]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C04-5|C04-5]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C04-X1|C04-X1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C04-X2|C04-X2]])
- (2025-09-26) Many government bond markets should carry a higher risk premium given global fiscal deficits.. Reasoning: Debt and deficits. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-X1|C05-X1]])

### Disagreements
- **Whether to explain weak CTA returns by structural change**: Rob Carver: Stories of change are untestable narratives; evidence of degradation is not significant and may need 50 more years to confirm; use full history. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C14-X1|C14-X1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C14-2|C14-2]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C16-4|C16-4]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C16-5|C16-5]]); Niels Kaastrup-Larsen: The world always changes, yet trend adapts and has worked 51 years; lower returns reflect much lower index volatility. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C16-1|C16-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C16-2|C16-2]])
- **Why large managers launch trend products now**: Rob Carver: Possibly dip-buying after weak performance; curious why not 10-15 years ago (or personnel driven). ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C04-1|C04-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C03-3|C03-3]]); Niels Kaastrup-Larsen: Treats it as a sign of growing institutional interest and legitimacy. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C02-4|C02-4]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C03-1|C03-1]])
- **Bond risk premium and debt**: Niels Kaastrup-Larsen: Many bond markets should carry a higher risk premium given deficits. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-X1|C05-X1]]); Rob Carver: Debt-driven sell-offs are the dog that has never barked; UK weakness is inflation-led. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-4|C05-4]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C06-1|C06-1]])

### Gaps and conflicts
- Rob's systematic book is long bonds while his stated gut view is that Fed-independence risk is under-priced; he accepts the conflict but gives no rule on when to override the model. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-2|C05-2]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-5|C05-5]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-X2|C05-X2]])
- The claim that investors lose from bad timing relies on one anecdotal fund plus the Morningstar average; the YieldMax figure (35.5m loss on 2.5bn inflows) is second-hand from an article. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C11-1|C11-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C09-2|C09-2]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C12-1|C12-1]])
- Rob has not tested the currency-conversion claim and says so; the dismissal of instrument-level differences is a statistical prior, not a result. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C08-3|C08-3]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C08-1|C08-1]])
- Two speakers disagree on whether visible degradation of trend returns exists; Rob concedes "looks degraded" but not significant, Niels attributes it to volatility, and no test of the degradation is shown on air. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C16-2|C16-2]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C16-3|C16-3]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C16-4|C16-4]])
- Rob says the full-history default means treating 2025 like 1975, but also says the 1970s early results had fewer markets, which complicates the same comparison. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C14-1|C14-1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C16-3|C16-3]])
- Lehman anecdote: no explicit lesson drawn by the speakers; the ledger's reader inference that buy ratings are poor risk signals is not stated. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C02-1|C02-1]])
- CTA positioning/risk figures: Niels's read-out is as of Tuesday and some numbers (Beta 50, SG Trend) are quoted from memory; Rob gives no P&L because his computer is broken. ([[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C04-5|C04-5]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C04-X1|C04-X1]], [[MT093 - Lehman’s Legacy, ETF Performance & What Investors Still Get Wrong - Systematic Investor -#^MT093-C05-1|C05-1]])

### Forward-looking inputs (reader synthesis)
(reader) No explicit price forecasts. Observable inputs named: strength of the trend barometer, equity and gold trends driving CTA P&L, bond positioning divergence (carry weight), Fed independence and the pace of cuts, UK inflation versus EU. The main forward claim is that trend allocations should not be conditioned on recent performance because persistence is weak.

### Reader inferences (not stated by the speakers)
- (reader) Rob's 'default is buy and hold unless proven otherwise' treats the burden of proof as lying on the timer; combined with weak autocorrelation it implies allocators should not redeem or add after drawdowns, which clashes with the observed behaviour he describes.
- (reader) His investor-return argument implies that for skewed products the realised client experience, not the fund track record, is the relevant risk measure for product design.
- (reader) Niels's volatility argument and Rob's market-count argument both imply raw return comparisons across eras are not like for like; neither provides a normalised comparison on the show.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro, Lehman anniversary (no content) |
| C02 | 4 | Lehman analyst anecdote, Fed cut, institutions entering CTA |
| C03 | 3 | Fidelity managed futures paper, classic CTA deck |
| C04 | 5 | institutions timing, trend barometer and CTA/market numbers |
| C05 | 5 | positioning, bonds divergence, debt and Fed independence |
| C06 | 3 | UK vs Italy yields, cash-only position sizing question |
| C07 | 2 | forecast cap, currency-converted trend question |
| C08 | 4 | do not currency convert, instrument significance, futures margin |
| C09 | 2 | crypto trend following, YieldMax article intro |
| C10 | 2 | percentage vs cash return example |
| C11 | 4 | YieldMax flows, skewness, Morningstar study |
| C12 | 3 | investor underperformance numbers, active vs passive intro |
| C13 | 2 | manager persistence, CTA doubt discussion |
| C14 | 2 | allocation using all data vs recent window |
| C15 | 3 | look-ahead, short-window degradation |
| C16 | 6 | Has the world changed? vol, significance, buy-and-hold default |
| C17 | 0 | sign-off, nothing actionable |

## Claims

### C02
- **Rob Carver** A sell-side overweight initiation on Lehman (reiterated until about 10 days before it failed) shows analyst buy ratings are poor risk signals near failures.  #mech/behavioral
  > initiates coverage of Lehman Brothers with an overweight recommendation that is iterated apparently on July 14th and August 27th
  indicator: sell-side recommendation · asset: equities · horizon: weeks · conditions: Single anecdote · testable: no: anecdote · confidence: medium
  **Correction (cross-check):** The precise details of the Morgan Stanley note (initiated 30 June, reiterated 14 July and 27 August) are given by Niels after he looked them up, not Rob; the lesson 'analyst buy ratings are poor risk signals near failures' is the first reader's inference, as the speakers only remark on the irony and the analyst's later career. → Niels notes that a Morgan Stanley note initiating Lehman at overweight on 30 June was reiterated on 14 July and 27 August, shortly before the September failure; the hosts treat it as an ironic anecdote, with no explicit methodological conclusion.
  ^MT093-C02-1
- **Rob Carver** Allocators often give money to managers after large losses, opposite to how CTA allocation behaves, raising the question of whether to allocate after losses.  #mech/behavioral
  > if you're a hedge fund manager and you've lost a lot of money then then actually people are desperate to give you money
  asset: multi · testable: no: anecdotal · confidence: low
  ^MT093-C02-2
- **Niels Kaastrup-Larsen** At the September 2025 25bp Fed cut, new governor Miran dissented for 50bp but contender Waller did not, and Powell dodged a question about Fed independence.  #mech/policy_reaction _(time-bound view)_
  > Christopher Waller who I think is one of the contenders to be the next Fed chair he did not descend
  indicator: FOMC dissents · asset: rates · horizon: days · testable: yes: FOMC votes · confidence: high
  ^MT093-C02-3
- **Niels Kaastrup-Larsen** Large managers such as BlackRock and Fidelity have entered trend-following products lately, suggesting growing institutional interest.  #mech/liquidity_flows _(time-bound view)_
  > some of these large institutions the black rocks the Fidelities have entered the CTA trend following space lately
  asset: multi · direction: trend following inflows · horizon: years · testable: partly: product launches observable · confidence: medium
  ^MT093-C02-4
- **Niels Kaastrup-Larsen** After the 25bp September cut, Waller (a contender for Fed chair) did not dissent and Powell did not signal capitulation to a run of cuts, which the administration would not have wanted to see; the Fed is not pre-committed to many cuts.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > it didn't sound like from what I've read that PAL was lining up um you know complete um surrender and lots of rate cuts coming uh our way
  indicator: FOMC votes and dissents · asset: rates · direction: fewer cuts than the administration wants · horizon: months · conditions: Fed independence under pressure · testable: partly - FOMC votes and guidance are observable · confidence: medium
  ^MT093-C02-X1
- **Niels Kaastrup-Larsen** Niels says that unlike hedge funds that attract money after large losses, CTAs do not get new allocations after losing money.  #mech/new _(added by map cross-check)_
  > it doesn't work in our in funny enough in the CTA world, it doesn't seem to be the way the work things work
  asset: CTA · testable: no: qualitative · confidence: medium
  ^MT093-C02-R1

### C03
- **Niels Kaastrup-Larsen** The Fidelity paper argues managed futures dynamically follow trends, keep low correlation to traditional assets and protect capital in crises, though not outperforming in every environment.  #mech/structural_shift
  > managed future strategies represent one of the most time-tested researchbacked and structurally unique investment approaches available today
  indicator: managed futures correlation to equities/bonds/60-40 · asset: multi · direction: adds portfolio resilience · horizon: years · testable: yes: standard diversification statistics · confidence: medium
  ^MT093-C03-1
- **Rob Carver** The classic managed-futures case shows crisis episodes (GFC, 2022, 2000) and that adding 10% trend to a 60/40 portfolio improves mean, standard deviation, drawdown and Sharpe ratio.  #mech/risk_management
  > when you put 10% of a 60/40 portfolio into into um trend it does better
  indicator: 60/40 plus 10% trend · asset: multi · direction: trend improves 60/40 · horizon: years · conditions: Selected crises; depends on sample · testable: yes: portfolio backtest · confidence: medium
  ^MT093-C03-2
- **Rob Carver** Big asset managers that run model portfolios will likely use their own trend products, creating new allocation flows to trend followers.  #mech/liquidity_flows _(time-bound view)_
  > gatekeepers of huge model portfolios where um most likely they're going to be using their own products to give people exposure to trends
  asset: multi · direction: trend following inflows · horizon: years · testable: no: speculation · confidence: medium
  ^MT093-C03-3

### C04
- **Rob Carver** The timing of institutional launches after weak trend performance may be dip-buying; Rob notes it is curious they did not launch 10-15 years ago.  #mech/behavioral _(time-bound view)_
  > It may be because you know trend hasn't done so well recently and who knows maybe this is buying the dip
  asset: multi · testable: no: speculation · confidence: low
  ^MT093-C04-1
- **Niels Kaastrup-Larsen** Dawn Capital's paper compares evidence for trend following versus all major hedge fund strategies.  #mech/research_method
  > we compared it to all the major hedge fund strategies um because we hadn't seen that being done before
  indicator: trend vs hedge fund strategies · asset: multi · horizon: years · testable: yes: strategy index comparison · confidence: medium
  ^MT093-C04-2
- **Niels Kaastrup-Larsen** His trend barometer was at 41, an improvement over the previous 10 days but still not strong, with positions about 50-60% of typical risk.  #mech/slow_reaction _(time-bound view)_
  > my own trend barometer finished yesterday at 41. So that's an improvement.
  indicator: Niels trend barometer · asset: multi · direction: trend signal weak · horizon: weeks · testable: partly: barometer is proprietary · confidence: medium
  **Correction (cross-check):** The 50-60% of typical risk is Rob's own stated risk level (said in C05, 'equivalent numbers to you really'); Niels did not state a risk level in the transcript. → Niels' trend barometer was at 41, an improvement over about 10 days but still not strong; separately Rob says his own risk is about 50-60% of typical.
  ^MT093-C04-3
- **Niels Kaastrup-Larsen** CTA gains in recent months came from equity and gold trends.  #mech/slow_reaction _(time-bound view)_
  > such as equity, such as gold um have been really pulling uh the performance forward
  indicator: CTA sector P&L · asset: multi · direction: long equity, long gold · horizon: months · testable: yes: sector attribution · confidence: medium
  ^MT093-C04-4
- **Niels Kaastrup-Larsen** September 2025 CTA numbers: Beta 50 +2.43% in month, -0.45% YTD; CTA index +2.85% in month, -3.62% YTD; versus MSCI World +16.6% and S&P 500 TR +13.29% YTD.  #mech/slow_reaction _(time-bound view)_
  > So CT index up 2.85 for the month, down only 3.62% for the year.
  indicator: CTA indexes, MSCI World, S&P 500 TR · asset: multi · horizon: months · testable: yes: index data · confidence: high
  ^MT093-C04-5
- **Niels Kaastrup-Larsen** September 2025 trend-index data beyond the CTA index: SG Trend up almost 4% in the month and down just over 4% YTD, and the short-term traders index up 2.13% in the month and down 4.37% YTD, i.e. managed futures recovering but still negative for the year.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > the short-term traders index actually a good improvement 2.13% uh for the month down uh just 4.37% so far this year
  indicator: SG Trend index; short-term traders index · asset: multi · direction: CTA performance recovering · horizon: months · conditions: Late 2025 rebound led by equities and gold trends · testable: yes - index series are public · confidence: high
  ^MT093-C04-X1
- **Niels Kaastrup-Larsen** Traditional assets kept delivering in 2025: the S&P US aggregate bond index was up 1.25% in September and 6.25% YTD, alongside equities, so a 60/40 benchmark outran trend indices.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > the US aggregate bond index from S&P is up one and a quarter for the month, up 6 and a quarter for the year
  indicator: S&P US aggregate bond index · asset: rates · direction: bonds up · horizon: months · testable: yes - index series are public · confidence: high
  ^MT093-C04-X2

### C05
- **Rob Carver** Rob runs about 50-60% of his typical risk because clear trends are lacking, with long equities, FX, bonds and short energy and Bitcoin.  #mech/risk_management _(time-bound view)_
  > it would be about 50 or 60% of my kind of typical kind of risk level
  indicator: trend signal strength scaling risk · asset: multi · direction: long equities, FX, bonds; short energy, Bitcoin · horizon: weeks · conditions: When trends are unclear · testable: yes: forecast-scaled sizing · confidence: medium
  ^MT093-C05-1
- **Rob Carver** Rob thinks rates markets underprice bad news such as Fed independence threats, yet his systematic book stays long bonds.  #mech/risk_premium _(time-bound view)_
  > there's an awful lot of bad news out there that isn't to me priced in
  asset: rates · horizon: months · testable: no: opinion · confidence: low
  ^MT093-C05-2
- **Niels Kaastrup-Larsen** CTA bond positioning diverges because carry matters more for bonds than equities, so carry weight changes positions relative to trend.  #mech/slow_reaction
  > carry is a much more significant factor in bond price movements than it is in equities
  indicator: carry vs trend in bonds · asset: rates · horizon: months · conditions: Managers differ on carry weight · testable: partly: carry-trend blend backtest · confidence: medium
  ^MT093-C05-3
- **Rob Carver** Bond market sell-offs on debt worries are the dog that has never barked; developed-market politicians get away with high debt (Truss was the exception).  #mech/fiscal_debt
  > politicians in in in developed markets generally speaking get away with levels of debt that a few years ago people thought would be inconceivable
  indicator: developed market government debt · asset: rates · horizon: years · testable: partly: yield response to debt · confidence: medium
  ^MT093-C05-4
- **Rob Carver** If discretionary views (Trump bad for bonds and equities) were right, a systematic long-bond portfolio would lose money, showing model and gut views can conflict.  #mech/risk_management
  > at least in my systematic portfolio, I'm going to lose money
  asset: multi · testable: no: reflection · confidence: low
  ^MT093-C05-5
- **Niels Kaastrup-Larsen** Niels argues that, given large fiscal deficits and rising debt almost everywhere, many government bond markets should carry a higher risk premium than they currently do.  #mech/fiscal_debt _(added by sonnet-xhigh cross-check, time-bound view)_
  > everybody getting into massive amount of debt, I think you could probably argue that many bond markets might uh you know probably should have a higher risk premier
  indicator: bond term/risk premium versus debt levels · asset: rates · direction: long-end yields should be higher · horizon: years · conditions: Rising debt supply · testable: partly - term premium estimates exist but timing is not specified · confidence: medium
  ^MT093-C05-X1
- **Rob Carver** Rob's trend system holds a modest but persistent long bond position (BTPs, US 30-year, Canadian 10-year) with risk about half that on equities, so a bond sell-off driven by Fed-independence or inflation fears would cost his systematic book money.  #mech/risk_management _(added by sonnet-xhigh cross-check, time-bound view)_
  > I'm long bonds, but my risk is about half what is in equities
  indicator: bond trend signal (with carry) and risk allocation · asset: rates · direction: long BTPs, US 30-year, Canada 10-year · horizon: months · conditions: Trend and carry signals still long · testable: yes - positions follow a rules-based system · confidence: high
  ^MT093-C05-X2
- **unclear (Rob Carver or Niels Kaastrup-Larsen)** UK gilt yields recently reached 27-year highs, above the Truss-crisis peak, together with inflation that stayed high since 2022 while EU inflation mean-reverted, a case where bond markets have priced debt and inflation concerns.  #mech/fiscal_debt _(added by sonnet-xhigh cross-check, time-bound view)_
  > in the UK we did hit 27year high yields uh only a couple of weeks ago higher than windless trust
  indicator: UK gilt yields · asset: rates · direction: UK yields higher · horizon: weeks · conditions: Persistent UK inflation versus EU · testable: yes - gilt yield history is public · confidence: high
  ^MT093-C05-X3

### C06
- **Rob Carver** UK yields are above Italy's even though Italian debt/GDP is worse, so UK bond weakness reflects persistent inflation rather than debt alone.  #mech/fiscal_debt _(time-bound view)_
  > So it can't just be a debt story. It must be an inflation story.
  indicator: gilt vs BTP vs Bund spreads · asset: rates · direction: UK yields higher · horizon: months · conditions: UK inflation persistently higher than EU · testable: partly: spread vs inflation · confidence: medium
  ^MT093-C06-1
- **Rob Carver** For cash-only (unlevered) portfolios where forecast-scaled positions exceed 100%, one option is to halve all positions so average exposure is 50% and maximum is 100%.  #mech/risk_management
  > So one is to kind of just effectively cut everything in half.
  indicator: forecast-scaled position size · asset: multi · conditions: Cash-only portfolios; no leverage · testable: yes: backtest unlevered sizing · confidence: high
  ^MT093-C06-2
- **Rob Carver** Halving works for high-volatility assets (e.g. EM stocks at 50% vol, giving a 25% target) but gives a risk target too low for liquid S&P 500 stocks.  #mech/risk_management
  > you're going to be going down from some say 25 to 12 a.5% which is a very low risk target
  indicator: annualised volatility of instruments · asset: equities · conditions: Depends on asset volatility · testable: yes: risk target comparison · confidence: high
  ^MT093-C06-3
- **Rob Carver** In an unlevered account forecast scaling is asymmetric: weak forecasts can shrink positions but stronger-than-average ones cannot raise them, so the fraction of the forecast-strength information that is used falls.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > So if my forecasts become really weak, then yes, I will cut my position, but if they get stronger than average, then I can't really do anything about it.
  indicator: forecast-scaled position sizing · asset: multi · conditions: Cash-only portfolios with a 100% notional cap · testable: yes - compare capped versus uncapped forecasts in a backtest · confidence: high
  ^MT093-C06-X1

### C07
- **Rob Carver** Alternative: cap forecasts at the average (10) instead of twice average (20), so weak forecasts shrink positions and cash creeps back in.  #mech/risk_management
  > if you had instruments you were holding where you had less than the um, average forecast, then you'd have a smaller position in them
  indicator: forecast cap at 10 versus 20 · asset: multi · conditions: Cash-only portfolios · testable: yes: backtest · confidence: medium
  ^MT093-C07-1
- **Rob Carver** Reallocating freed-up cash to other positions is theoretically optimal but usually not worth the complexity.  #mech/risk_management
  > So in theory, yes, in practice, unless it was a big effect, I probably wouldn't bother because it would get get a bit too complicated.
  asset: multi · testable: partly: depends on effect size · confidence: medium
  ^MT093-C07-2

### C08
- **Rob Carver** Do not currency-convert price series before trend following; trade the local-currency price and the FX rate as separate instruments.  #mech/risk_management
  > I would not combine those two things together. I tra trade them separately.
  indicator: GBPUSD and local price series · asset: fx · conditions: Applies to cash instruments and futures · testable: yes: compare converted vs separate · confidence: medium
  ^MT093-C08-1
- **Rob Carver** Combining the price and FX rate into one series removes diversification and increases correlation with a separate currency trade.  #mech/risk_management
  > removing the the potential for diversifying across two instruments, a currency and a stock market index
  asset: multi · testable: yes · confidence: medium
  ^MT093-C08-2
- **Rob Carver** Claims that trend following works better on some instruments than others usually lack statistical significance; checking 250 instruments will find a few significant by chance.  #mech/research_method
  > it's quite hard to pick out statistically significant differences in performance of trend following of different instruments
  indicator: trend return by instrument · asset: multi · testable: yes: statistical tests across instruments · confidence: high
  ^MT093-C08-3
- **Rob Carver** With futures only margin is converted, so FX exposure is a fraction of notional and the currency can be traded separately.  #mech/risk_management
  > I just have to convert enough for the margin.
  indicator: futures margin · asset: fx · conditions: Futures not cash instruments · testable: yes · confidence: medium
  ^MT093-C08-4
- **Rob Carver** Converting a foreign asset's price into home currency before trend following adds the exchange-rate trend to the asset's trend (e.g. a falling pound makes a US ETF look stronger), so the signal becomes a blend of two instruments rather than a clean trend in either.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > Because it would have had a sort of systematic drift added to it, which is the depre depreciation of the currency effect on top of it.
  indicator: home-currency price of a foreign-listed asset · asset: multi · direction: trend signal inflated when home currency depreciates · conditions: Non-home-currency instruments · testable: yes - compare signals on converted versus local price series · confidence: high
  ^MT093-C08-X1

### C09
- **Rob Carver** Trend following works well on cryptocurrencies by Rob's testing and by a crypto hedge fund he advises, with no guarantee for the future.  #mech/slow_reaction
  > So um trend following on cryptocurrencies seems to work pretty well.
  indicator: crypto trend following · asset: other · testable: yes: backtest · confidence: medium
  ^MT093-C09-1
- **Rob Carver** The YieldMax coin option income ETF earned 42% yet its investors lost money because of investor timing around its returns.  #mech/behavioral
  > An ETF gains 42% a year, its investors still lose money.
  indicator: fund percentage return vs investor cash return · asset: equities · horizon: years · testable: yes: flows-weighted returns · confidence: high
  ^MT093-C09-2

### C10
- **Rob Carver** Investor (cash/dollar-weighted) returns differ from fund (percentage) returns unless the investor buys and holds with no flows.  #mech/research_method
  > it's going to be impossible for any individual um investor to actually earn the returns of a fund unless they literally buy and hold
  indicator: dollar-weighted vs time-weighted returns · asset: multi · horizon: years · testable: yes: compute from net flows · confidence: high
  ^MT093-C10-1
- **Rob Carver** Investors pile in just before losses and leave before gains, so net flows turn a 42% fund return into a loss.  #mech/behavioral
  > lot of pe a lot more people are putting money in just before the thing goes down that are putting money in um when it's about to go
  indicator: net fund flows · asset: multi · horizon: months · conditions: Spiky/skewed funds · testable: yes: flows data · confidence: high
  ^MT093-C10-2
- **Rob Carver** Investor (cash/dollar-weighted) return for a fund can be estimated from its annual reports and net flows in and out, then compared with the headline percentage return; the flow-weighted aggregate is what investors actually earned.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > he looks at the the um the annual reports and the kind of cash movements um and looks at the the net flows in and out
  indicator: fund net flows; investor return minus fund return · asset: multi · horizon: years · conditions: Needs fund-level flow and NAV data · testable: yes - Morningstar-type calculation on fund flows · confidence: high
  ^MT093-C10-X1
- **Rob Carver** Using a stylised fund that loses 1% for 51 weeks and gains 200% on the last day, Rob shows that only a buy-and-hold investor with no flows earns the fund's percentage return; any timing yields a very different cash return.  #mech/new _(added by map cross-check)_
  > it's going to be impossible for any individual um investor to actually earn the returns of a fund unless they literally buy and hold
  asset: funds · horizon: annual · conditions: fund returns concentrated in a few days (skewed) · testable: yes: dollar-weighted vs time-weighted return · confidence: high
  ^MT093-C10-R1

### C11
- **Rob Carver** For the YieldMax fund, 2.5bn of net inflows and investors lost a combined 35.5m (about 1.5%) against a 42% fund gain.  #mech/behavioral
  > $2.5 billion were coming in in net inflows. Yeah. But the investors lost a combined $ 35.5 million over the very same period
  indicator: fund net flows · asset: equities · horizon: years · testable: yes: reported · confidence: high
  ^MT093-C11-1
- **Rob Carver** The return gap between fund and investor is larger for funds with strong positive or negative skew.  #mech/behavioral
  > this is going to be more problematic in in funds whose returns are very let's say patchy or spiky
  indicator: skewness of fund returns · asset: multi · horizon: years · conditions: Spiky or skewed returns · testable: yes: gap vs skew · confidence: medium
  ^MT093-C11-2
- **Rob Carver** Trend following is positively skewed, option selling negatively skewed; flow-chasers buying after persistent gains in negative-skew strategies suffer the large losses.  #mech/behavioral
  > But if you buying before one of those big losses you're going to on the back of what probably look like persistent gains in the past you're going to do very badly.
  asset: multi · horizon: years · conditions: Negative skew strategies · testable: partly · confidence: medium
  ^MT093-C11-3
- **Rob Carver** When faced with an anecdote a quant should test whether it is generally true rather than extrapolate.  #mech/research_method
  > as a quant if you like you should say well this is generally true or is this just you know are the investors in this particular fund just uniquely stupid
  asset: multi · testable: yes · confidence: high
  ^MT093-C11-4
- **Rob Carver** In the few funds where investors beat the fund's own return, the cause is probably luck rather than timing skill, given so many funds; the industry average gap is negative.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > There's probably no skill here. It probably just that by luck, you know, there are so many funds out there that
  indicator: investor return gap by fund · asset: multi · horizon: years · conditions: Large cross-section of funds · testable: yes - test cross-sectional dispersion against chance · confidence: medium
  ^MT093-C11-X1

### C12
- **Rob Carver** Morningstar finds investor returns trail fund returns by 1.7% a year across all US funds over 10 years, substantial over a decade.  #mech/behavioral
  > if you look at the the whole universe of funds the underperformance is 1.7% a year
  indicator: Morningstar investor return minus fund return · asset: equities · direction: investor return gap · horizon: years · testable: yes: Morningstar study · confidence: high
  ^MT093-C12-1
- **Rob Carver** The gap is worst in sector equity funds at 4.4% a year, likely because news and emotion (e.g. AI themes) drive buying after rallies.  #mech/behavioral
  > there the underperformance is 4.4% 4% a year
  indicator: sector fund investor return gap · asset: equities · direction: investor return gap · horizon: years · conditions: Thematic funds after strong runs · testable: yes · confidence: high
  ^MT093-C12-2
- **Rob Carver** Investors are poor at predicting the future and at timing entry into and exit from funds.  #mech/behavioral
  > they're pretty poor at very poor at timing when to invest in things and when to take money out of things
  asset: multi · horizon: years · testable: yes: flow studies · confidence: high
  ^MT093-C12-3
- **Rob Carver** The share of assets in passive or index strategies has risen persistently over a long period, so the passive-versus-active debate is largely won by passive.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > the percentage of of um assets that are passively managed or in managed by indices has just just kind of gone up um persistently over quite long period of time now
  indicator: share of assets passively managed · asset: equities · direction: passive share up · horizon: years · testable: yes - industry asset-share data · confidence: medium
  ^MT093-C12-X1

### C13
- **Rob Carver** Manager skill persistence can be tested through return autocorrelation: positive means good managers stay good, negative means mean reversion.  #mech/research_method
  > one is that good managers continue to do well the other is that good managers is mean revert
  indicator: return autocorrelation · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT093-C13-1
- **Rob Carver** Every strategy (CTAs, equity value) has long underperformance spells that provoke the 'has everything changed' question.  #mech/research_method
  > any strategy that will go through long periods of underperformance or negative performance inevitably at some point people are going to be asking that question
  asset: multi · horizon: years · testable: no: framing · confidence: high
  ^MT093-C13-2
- **Rob Carver** Evidence on whether active-manager performance persists (the persistence scorecard debate) is unsettled; a critique of the scorecard analysis does not settle the question either way.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > the FT sort of said well this is a very poor analysis but actually ultimately um it doesn't really kind of settle the argument one way or the other
  indicator: active manager performance persistence · asset: equities · horizon: years · testable: partly - persistence tests exist but results are disputed · confidence: medium
  ^MT093-C13-X1

### C14
- **Rob Carver** The default allocator approach for blending trend with 60/40 is to use the full history (Rob's backtest runs back to 1970) with equal weight; a backfill trend index can be built by replication using futures prices.  #mech/research_method
  > I want to use as much data as I possibly can. So, I'm just going to use all of my data and I'm going to treat it all equally.
  indicator: full-sample portfolio optimization · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT093-C14-1
- **Rob Carver** Choosing to use only the last 2-3 years because trend did badly cannot be backtested; it smuggles in future information and would drive trend allocations to near zero.  #mech/research_method
  > you've done something that is not back testable because you have essentially created a an arbitrary point
  indicator: recent-window optimization · asset: multi · horizon: years · testable: yes: can show look-ahead bias · confidence: high
  ^MT093-C14-2
- **Rob Carver** Plausible 'the world has changed' stories for weak CTA returns (Trump policy, more algorithmic trading, markets becoming more efficient so less alpha) are narratives that cannot be separated from bad luck without a testable method.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > just over time markets get more efficient and therefore there's less alpha to be collected
  indicator: trend following alpha over time · asset: multi · direction: trend returns lower · horizon: years · testable: partly - test for structural break in trend returns · confidence: low
  ^MT093-C14-X1

### C15
- **Rob Carver** Persistence and autocorrelation of strategy returns are weak, so there is no reliable conditioning variable to forecast CTA performance over the next 12 months.  #mech/research_method
  > if you do look at things like persistence and autocorrelation of things like that, generally speaking, um the the effects aren't especially strong
  indicator: strategy return autocorrelation · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT093-C15-1
- **Rob Carver** Fitting on only 10, 5 or 3 years degrades out-of-sample results, nonlinearly: 50 years is good, 20-40 makes little difference, 2-3 is much worse.  #mech/research_method
  > there's a degradation of of out of sample performance as you reduce the size of the data you have available to you
  indicator: lookback length · asset: multi · horizon: years · conditions: Short windows · testable: yes: out-of-sample optimization comparison · confidence: high
  ^MT093-C15-2
- **Rob Carver** Using 20-40 years of data performs about as well as 50, so the loss only appears with very short samples.  #mech/research_method
  > It doesn't make a lot of difference if you use 40 or even 30 years of data or even 20 years of data
  asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT093-C15-3
- **Rob Carver** An allocation optimised on a very short window (e.g. the last 10 days) is mostly noise and would also cause constant switching and trading costs, showing that out-of-sample quality degrades as the fit window shrinks.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > Even ignoring trading costs, you know, you're just going to have mostly noise.
  indicator: optimisation window length · asset: multi · horizon: days · conditions: Very short windows · testable: yes - compare out-of-sample results by window length · confidence: high
  ^MT093-C15-X1

### C16
- **Niels Kaastrup-Larsen** Trend following has survived 51 years of change because it adapts through research, though 1970s rules should not be applied unchanged.  #mech/structural_shift
  > the world is always changing. And if you look at say the company that I work with, you know, we've been doing trend following for 51 years.
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT093-C16-1
- **Niels Kaastrup-Larsen** Lower CTA index returns reflect lower index volatility, from over 25% in the 1970s-80s to under 5% now, so returns should be lower.  #mech/research_method
  > back in the 70s and the 80s it was you know more than 25% annual volatility. Today that index is less than 5% annualized volatility.
  indicator: Barclay CTA index rolling volatility · asset: multi · horizon: years · testable: yes: rolling vol · confidence: high
  ^MT093-C16-2
- **Rob Carver** Early trend-following results had fewer markets and less diversification, which complicates volatility-adjusted comparisons over time.  #mech/structural_shift
  > in the earlier days when when there were fewer markets there was less diversification
  indicator: number of markets traded · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT093-C16-3
- **Rob Carver** Even if rolling trend returns degraded, the difference is not statistically significant, and with a low Sharpe strategy it could take another 50 years to know.  #mech/research_method
  > you still don't see a statistically significant difference in returns
  indicator: rolling trend performance · asset: multi · horizon: years · conditions: Low Sharpe strategy · testable: yes · confidence: high
  ^MT093-C16-4
- **Rob Carver** Statistics cannot settle whether trend following has stopped working, so belief matters; the evidence on timing in and out of strategies is poor.  #mech/research_method
  > you're at the point where statistics can't really help you
  asset: multi · horizon: years · testable: no: argument about power · confidence: medium
  ^MT093-C16-5
- **Rob Carver** The default should be buy and hold of assets, funds, strategies or factors unless one can convincingly show timing adds value.  #mech/research_method
  > you should be buying and holding those funds or or strategies or risk factors unless you can prove very convincingly that you can do better
  asset: multi · horizon: years · testable: yes: timing evidence · confidence: high
  ^MT093-C16-6

