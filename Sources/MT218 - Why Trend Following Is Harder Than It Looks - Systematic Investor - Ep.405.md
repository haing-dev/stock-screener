---
source_id: MT218
title: "Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405"
date: 2026-06-21
channel: "Top Traders Unplugged"
url: 
words: 13905
claims: 53
added_by_crosscheck: 13
corrections: 4
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Niels Kaastrup-Larsen (host)", "Rob Carver (systematic trader and author)"]
tags: [source, layer0]
---
# Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405

**Speakers:** Niels Kaastrup-Larsen (host); Rob Carver (systematic trader and author)

**Summary:** Top Traders Unplugged Systematic Investor ep. 405 (June 2026): trend following conditions, why drawdown is a poor evaluation metric, perpetual futures, the Quantica paper on chasing sector trends (no value added), AI-assisted backtests and overfitting, and the Man paper on drawdowns.

**Approach:** trend following, portfolio optimization, backtest process, CTA

**Cross-check completeness estimate of first read:** 0.82 - the first reader caught the main arguments (drawdown vs Sharpe, skew buckets, trend sleeve neutrality, perpetual futures mechanics, Quantica findings, AI overfitting, Man drawdown paper) but missed the June performance table, the CTA convergent-strategy mix, the small-allocation rebuttal, the cocoa and AUM-incentive points, and the due-diligence process answer.

## Argument map

**Episode thesis:** Rob Carver argues that systematic portfolios should be judged and sized mainly on Sharpe and robust process, not on drawdown, path risk or recent sector performance: drawdowns carry no information beyond Sharpe and history length, sector leadership in trend following rotates by decade because of single-factor macro stories, and a continuous trend-strength signal already tilts toward whichever asset class is trending. Both speakers hold that true diversification (more commodities, fewer correlated financial markets) is the durable edge, that AI-generated strategy ideas are acceptable only if tested through a process that assumes the idea was conceived with hindsight, and that perpetual futures are a structural change that may hurt hedgers and price discovery.

### Rob Carver (Systematic trader, author, runs his own trend plus carry futures portfolio (ex-AHL head of fixed income))
Fingerprint: #approach/trend_following #approach/carry #approach/research_robustness_overfitting #approach/position_sizing_vol_target #approach/diversification_risk_parity #approach/portfolio_construction_stacking #approach/costs_execution #approach/nowcasting_data
_Speaker note: Captions carry no speaker labels. Turns were assigned from content: the speaker who mentions his books, his own 9% risk position, 40% non-trend allocation and AHL fixed income is Carver; the one who reads index numbers, the listener question and says 'at Dunn' is the host. The C03 'I did not watch the game' turn and the C13 remark about Yarra also fit the stated split._

**Worldview premises**
- Sharpe ratio is the right primary lens for adding, sizing or dropping a strategy; drawdown depth and duration add nothing beyond Sharpe and sample length. _[theoretical, stated; support: Statistical argument: ignoring autocorrelation drawdown grows with history and shrinks with Sharpe.]_ ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C05-1|C05-1]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C05-2|C05-2]])
- Per-strategy path-risk and loss-clustering analysis overcomplicates and invites overfitting; it is more sensible at whole-portfolio level. _[experience, stated; support: Preference for simplicity; no data.]_ ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C05-3|C05-3]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C05-R1|C05-R1]])
- Almost no CTA is a pure trend follower; the trend vs convergent (carry-like) mix is a design choice, constrained for others by client pools and allocator boxes. _[institutional, stated; support: Observation of industry practice and his own 40% allocation.]_ ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C05-X1|C05-X1]])
- Skew is a useful label for sorting strategies into trend-like and carry-like buckets, but skew estimates are too statistically unreliable to enter a formal utility function. _[empirical, stated; support: Examples: EM FX carry negative skew, developed bond carry mildly positive; robustness argument.]_ ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C05-4|C05-4]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C06-1|C06-1]])
- Hundreds of published factors reduce to a handful of independent drivers, so true diversification is less than the count of factors suggests. _[empirical, stated; support: Cites the Alpha Architect piece classifying the factor zoo.]_ ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C06-2|C06-2]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C06-X1|C06-X1]])
- Trend following in equities is on average net long, so part of its return is the equity risk premium rather than trend skill. _[empirical, stated; support: Cites the Beyond Passive Investing post; equities tend to go up.]_ ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C07-1|C07-1]])
- Return autocorrelation of trend strategies is too weak to time entry or exit after drawdowns. _[empirical, stated; support: His own research and a Winton study; no figures quoted.]_ ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C12-2|C12-2]])
- More data is always better; deliberately removing official statistics harms economies and systematic models alike. _[experience, stated; support: Economist view; no data.]_ ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C02-3|C02-3]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C03-1|C03-1]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C03-R1|C03-R1]])
- Backtest and fitting quality depends more on process than maths, and every idea is formed using future information, whether from AI, data mining or a junior researcher. _[experience, stated; support: Years of research and an upcoming book on backtesting.]_ ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C16-2|C16-2]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C17-1|C17-1]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C18-X1|C18-X1]])

**Chain: Why drawdown adds no information beyond Sharpe**
1. Longer history → deeper maximum drawdown: Excluding autocorrelation, drawdown scales with the length of the track record. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C05-2|C05-2]])
2. Higher Sharpe ratio → smaller drawdown: Better strategies draw down less for the same length. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C05-2|C05-2]])
3. Drawdown is a function of Sharpe and history → using it as a separate criterion duplicates Sharpe and adds overfitting risk: Per-component path risk is noisy and overcomplicates the allocation. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C05-1|C05-1]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C05-3|C05-3]])
- Evidence: Statistical reasoning only.
- Fails when: He concedes autocorrelation breaks the proportionality and that path risk may matter at whole-portfolio level.

**Chain: Sector dominance in trend following is one factor, not diversification**
1. Trend P&L by sector rotates by decade (2000-09 broad, 2010-19 fixed income, 2020-26 commodities) → one asset class dominates in each period: Quantica attribution. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C13-1|C13-1]])
2. One asset class dominates → a single macro story drives all its markets (predictable rate cuts then hikes): Markets in that class move together, so returns are not from diversification. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C14-1|C14-1]])
3. Single-factor story → shifting weights toward the hot sector lowers diversification: Concentrates risk in one driver. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C14-1|C14-1]])
4. Continuous trend-strength scaling → already overweights the trending asset class: Signals are larger where trends are stronger, so extra chasing is redundant. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C14-2|C14-2]])
- Evidence: Quantica paper (null result: tactical sector chasing does not add value).
- Fails when: Not stated; applies to a continuous-signal system, a binary trader may differ.

**Chain: Trend sleeve inside a 60/40 portfolio**
1. Trend portfolio is on average net long equities and bonds → part of its return is the equity risk premium: Markets tend to rise. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C07-1|C07-1]])
2. Sleeve is a small part of a portfolio already holding equity and bond premia → double-counting of premia: Premia already earned in the 60/40. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C07-2|C07-2]])
3. Make sleeve more neutral (long only when trends are strong) → better overall portfolio for a limited allocation: Lower average beta in the sleeve. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C07-2|C07-2]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C08-X1|C08-X1]])
- Evidence: Theoretical argument; secondhand from a Substack post he calls complex.
- Fails when: Not needed if the investor can simply enlarge the CTA bucket or hold only a small sleeve (host's point).

**Chain: Perpetual futures as daily-settled futures**
1. Variation margin already settles futures cash flows daily → a perpetual future is effectively a daily future with identical cash flows: Compress expiry to one day; a new daily bet opens automatically. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C09-1|C09-1]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C10-1|C10-1]])
2. Settlement each day → futures price tracks spot, interest, dividend and storage terms negligible, no rolls: No-arbitrage at each settlement. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C10-1|C10-1]])
3. Hedgers need dated contracts and liquidity splits across venues → wider spreads, price discovery and concentration in market-maker houses: Dated hedging demand may move to OTC swaps. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C11-2|C11-2]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C12-1|C12-1]])
- Evidence: Mechanical explanation and analogy to UK daily spread bets; the downside is opinion.
- Fails when: He does not say; he admits uncertainty about where hedgers will go.

**Chain: AI-assisted idea generation and overfitting**
1. AI or data mining generates a strategy idea → the idea is contaminated by future information: It is conceived using data from the whole sample. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C17-1|C17-1]])
2. Contaminated idea → must pass a robust backtest process away from the AI: Process matters more than maths; do not trust the AI's self-evaluation. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C16-2|C16-2]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C18-X1|C18-X1]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C16-X1|C16-X1]])
3. Process output → a probability the idea works, mapped into a portfolio weight: Not a yes/no: 10-15% for an outstanding idea, about 0.01% for a weak one. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C17-2|C17-2]])
- Evidence: Experience; cites the Wisdom Trading blog.
- Fails when: If the AI is a public model with unknown training data, or the process is flawed, all bets are off.

**Decision process**
- [signal] Continuous trend-strength signals rather than binary; weight scales with trend strength.. Why: Automatically leans toward trending asset classes without extra sector-timing. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C14-2|C14-2]])
- [portfolio] About 40% of the portfolio in convergent, non-trend (carry-like) strategies, higher than CTAs who hold 20-30%.. Why: No client pool or allocator box constraining the mix. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C05-X1|C05-X1]])
- [sizing] Weight a strategy by the probability it works: 10-15% for an outstanding idea, about 0.01% for a weak one, so nothing is ever entirely excluded.. Why: No idea has zero chance of working. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C17-2|C17-2]])
- [risk] Drop a strategy only on very strong statistical evidence of a structural break; evaluate on Sharpe, not drawdown.. Why: Avoid overfitting and noise. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C05-1|C05-1]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C05-2|C05-2]])
- [risk] Use skew to classify strategies into buckets and cap the negative-skew bucket (illustrated at 30%), not in a formal utility with Sharpe.. Why: Skew estimates are unreliable. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C05-4|C05-4]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C06-1|C06-1]])
- [research] Use AI only for ideas and snippets under 10 lines; test every idea in a process designed for hindsight contamination; ask about research steps, checks and out-of-sample design in due diligence.. Why: Checking AI code or backtests costs more than writing it. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C16-2|C16-2]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C16-X1|C16-X1]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C17-1|C17-1]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C18-1|C18-1]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C18-X1|C18-X1]])
- [research] When a pattern appears, ask why it happens first, then whether it is exploitable; test the null.. Why: Many patterns do not add return and null results are valuable. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C13-X1|C13-X1]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C14-3|C14-3]])
- [execution] Rolls futures at expiry (IMM dates); perpetuals would remove roll code.. Why: Operational convenience, though he views perpetuals as a net negative for markets. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C09-1|C09-1]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C12-1|C12-1]])
- [other] Investing into a fund below its high-water mark gets the first returns without performance fees, unless a separate share class has its own high-water mark (host's correction).. Why: Fee mechanics, separate from any return-timing signal. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C12-3|C12-3]])

**Evidence style:** Statistical first principles and economist reasoning, backed by his own research and secondhand published papers (Quantica, Man, Alpha Architect, Wisdom Trading); little data of his own quoted. Treats null results as informative and warns about low counts of episodes (10-20 drawdowns in 50 years).

**Views at the time**
- (2026-06 (mid-June)) His own trend portfolio runs a low 9% annualised risk, biggest position a long equity position (pro peace deal), flat energies, so he was not positioned for the oil move.. Reasoning: Trend signals are weak; world is waiting. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C03-3|C03-3]])
- (2026-06 (mid-June)) Peace deal in the Middle East has been priced in for weeks, so risk is buy the rumour, sell the fact, while oil supply shortages could keep normalisation slow.. Reasoning: Markets had priced the optimistic scenario already. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C04-1|C04-1]])
- (2026-06 (mid-June)) US statistical data quality is degrading, worrying for economic indicators used as forecasting inputs.. Reasoning: Cuts, secrecy and delayed releases after the shutdown. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C02-3|C02-3]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C03-1|C03-1]])
- (2026-06 (mid-June)) Perpetual futures are probably not a great development for futures markets generally.. Reasoning: Hedgers need dated contracts; liquidity may split across swaps and market-maker platforms. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C12-1|C12-1]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C11-2|C11-2]])
- (2026-06 (mid-June)) Index providers relaxing rules to admit SpaceX is not an entirely responsible move.. Reasoning: Previous profitability and free-float rules (Tesla example) are being torn up. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C01-1|C01-1]])

### Niels Kaastrup-Larsen (Host, Top Traders Unplugged; allocator and manager-selection background)
Fingerprint: #approach/trend_following #approach/diversification_risk_parity #approach/crisis_alpha_convexity #approach/manager_selection_allocation #approach/regime_detection #approach/portfolio_construction_stacking
_Speaker note: Host also states positions on index design and trend sleeve sizing; attribution from content (CTA index numbers, 'at Dunn', manager due diligence). Corrections applied: C11-2 split between host (CME lawsuit) and Rob (hedging); C15-1 is the host's conjecture, not a paper result._

**Worldview premises**
- Do not distort a trend program to fit the rest of the portfolio; adjust the other holdings instead, since sector tweaks change the interaction among all markets. _[experience, stated; support: Gut feel, admits he has not read the paper.]_ ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C08-1|C08-1]])
- Trend following adds access to markets investors cannot easily trade themselves and is unbiased on long or short, e.g. fully short equities in a prolonged crisis. _[theoretical, stated; support: Skimmed paper conclusion.]_ ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C08-2|C08-2]])
- The 2010-19 fixed-income-led decade (zero rates, suppressed inflation) was the odd one out; earlier decades and the 2020s are more diverse and commodity-heavy. _[experience, stated; support: Own recollection of the CTA-winter debate; he explicitly wished the paper covered the 1990s and 1980s.]_ ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C15-1|C15-1]])
- Commodities are the most consistent trend sector in crises, so the best portfolio holds many truly uncorrelated markets rather than a financial-heavy book. _[empirical, stated; support: Unnamed reputable study; philosophy shared by Dunn.]_ ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C15-2|C15-2]])
- Dropping markets that have not recently trended is dangerous: cocoa idled for 15 years and then produced its biggest trend ever. _[experience, stated; support: Cocoa anecdote.]_ ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C12-X1|C12-X1]])
- CTAs drifted toward liquid financial markets because capacity and asset-based fees reward it, not because it is the best portfolio. _[institutional, stated; support: Incentive reasoning.]_ ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C15-X2|C15-X2]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C15-X1|C15-X1]])

**Chain: Why financial-heavy CTA books persist**
1. Financial futures are more liquid → managers can run more assets: Capacity. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C15-X2|C15-X2]])
2. Managers are paid on assets managed → incentive to tilt toward financials: Fees scale with capacity. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C15-X2|C15-X2]])
3. Financial tilt → less true diversification and exposure to equities that have not paid trend followers over 20-25 years: Commodities are the most consistent crisis sector. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C15-2|C15-2]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C15-X1|C15-X1]])
- Evidence: Recollection of a reputable but unnamed study and data he saw.
- Fails when: Fixed income will sometimes dominate (he concedes).

**Chain: Perpetual futures and exchange economics**
1. Futures without expiry → no rolls, lower exchange volume: Rolling generates volume. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C11-2|C11-2]])
2. Volume loss → CME sues the CFTC, arguing perpetuals are swaps: Exchange revenue at stake. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C11-2|C11-2]])
- Evidence: News report he picked up that morning.
- Fails when: Outcome of the lawsuit not discussed.

**Decision process**
- [portfolio] Build portfolios with as many truly uncorrelated markets as possible, more commodities.. Why: Commodities are the most consistent crisis sector; diversification beats financial concentration. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C15-2|C15-2]])
- [portfolio] Keep the trend program intact and fix excess equity by selling equity elsewhere; if the sleeve is only 5% do not worry about its equity exposure.. Why: Distorting sectors disrupts interaction across markets. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C08-1|C08-1]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C08-X1|C08-X1]])
- [signal] Use a trend barometer as a conditions gauge (36 = weak).. Why: Ties to realised June CTA returns. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C03-2|C03-2]])
- [other] Do not rotate away from markets that have not trended recently.. Why: Biggest trends can follow long idle periods (cocoa). ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C12-X1|C12-X1]])

**Evidence style:** Industry knowledge and anecdote; relays CTA index data and paper conclusions; admits not having read some papers.

**Views at the time**
- (2026-06 (mid-June)) Trend conditions weak in June 2026: barometer 36, with weak equities and metals and grains, gains in short rates and the dollar after the hawkish Fed.. Reasoning: Matches the weak June numbers. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C03-2|C03-2]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C04-2|C04-2]])
- (2026-06 (mid-June)) CTA indices roughly -0.8% to -1.25% in June but about +9% YTD, matching equities year to date.. Reasoning: Index data read out. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C04-X1|C04-X1]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C04-2|C04-2]])
- (2026-06 (mid-June)) New Fed chair Warsh more hawkish than expected: smaller balance sheet, less forward guidance, little appetite for cuts amid inflation.. Reasoning: First FOMC press conference. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C02-1|C02-1]])
- (2026-06 (mid-June)) Reworking government survey data would hurt economic-trend and systematic macro strategies but not price-based trend followers.. Reasoning: Those strategies use economic releases as inputs. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C02-2|C02-2]])

### Disagreements
- **Should a trend sleeve be adjusted for the investor's other holdings?**: Rob Carver: For a small sleeve inside a 60/40, make it more neutral (long only on strong trends) to avoid double-counting equity and bond premia; best is a bigger CTA bucket if possible. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C07-2|C07-2]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C08-X1|C08-X1]]); Niels Kaastrup-Larsen: Do not distort the program; sell the excess equity elsewhere, and with only 5% in trend the sleeve's equity exposure is not worth worrying about. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C08-1|C08-1]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C08-X1|C08-X1]])
- **Is a trend program's long bias a defect or a feature?**: Rob Carver: Long bias is the equity risk premium, desirable only if trend is the whole portfolio. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C07-1|C07-1]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C07-2|C07-2]]); Niels Kaastrup-Larsen: The value is access to markets one cannot trade oneself and unbiased long/short exposure, including being fully short in a crisis. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C08-2|C08-2]])
- **How to respond to sector rotation in trend following**: Rob Carver: No tactical chasing; a continuous signal already tilts to the trending class, and shifting reduces diversification. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C14-1|C14-1]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C14-2|C14-2]]); Niels Kaastrup-Larsen: Do not drop idle markets and structurally favour commodities and many uncorrelated markets over financial-heavy books. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C12-X1|C12-X1]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C15-2|C15-2]])

### Gaps and conflicts
- Carver endorses diversification yet agrees with tilting the CTA sleeve toward commodities, which is itself a sector weighting call; no rule for how much is stated. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C08-3|C08-3]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C14-1|C14-1]])
- Carver says path risk is not worth analysing per component but later says the Man paper's joint drawdown analysis is a more rigorous crisis-alpha test; the distinction is portfolio level versus component level, not spelled out. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C05-3|C05-3]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C19-2|C19-2]])
- Niels's claim that the 1970s-90s looked like 2000-09 and 2020-26 is conjecture; Carver supplies only the 1970s as supporting data. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C15-1|C15-1]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C16-1|C16-1]])
- The unnamed 'reputable firm' study that commodities are the most consistent crisis sector is not cited or verified. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C15-2|C15-2]])
- Neither speaker has read the Beyond Passive Investing paper in detail, and Niels had not read it at all; the neutral-sleeve argument is secondhand. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C07-2|C07-2]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C08-1|C08-1]])
- The Man paper conclusions are described as statistically weak (10-20 drawdown episodes) yet used as a template for a better crisis-alpha test. ([[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C19-1|C19-1]], [[MT218 - Why Trend Following Is Harder Than It Looks - Systematic Investor - Ep.405#^MT218-C19-2|C19-2]])

### Forward-looking inputs (reader synthesis)
(reader) The speakers give no price predictors. Observable inputs they name: a trend barometer (36 = weak conditions), CTA index returns, strength of trend signals by asset class (continuous signal scaling), policy path (Fed chair Warsh hawkish, balance sheet shrinking), oil supply normalisation after the Hormuz deal, and availability of official economic data for macro-trend models. Horizon is months (monthly CTA returns) to decades (sector regimes), with emphasis on robustness over timing.

### Reader inferences (not stated by the speakers)
- (reader) Carver's rejection of drawdown and path-risk metrics implies allocation rules built on Sharpe and probability weights, so a vault feature for 'how this investor sizes a new strategy' should record weight as a function of confidence, not pass/fail.
- (reader) The single-factor story for sector dominance (rate cuts then hikes for fixed income, inflation for commodities in the 1970s and 2020s) suggests that sector leadership in trend following depends on macro regime, which links to a regime-detection test rather than performance chasing.
- (reader) Niels's incentive argument (assets-based fees favour liquid financials) is a testable proposition for CTA index composition.
- (reader) Both speakers treat null results (Quantica) as evidence quality signals, a marker for judging which published claims to weight.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | Intro; peace deal and SpaceX index inclusion |
| C02 | 3 | New Fed chair Warsh, statistical data quality |
| C03 | 3 | Third-party data nowcasts; football banter; trend barometer 36; Rob positioning |
| C04 | 2 | Oil, metals, equities June moves; CTA index returns; listener question on Sharpe vs path risk |
| C05 | 4 | Drawdown as statistic; structural breaks; skew for classification |
| C06 | 2 | Skew caution; Factor Zoo paper |
| C07 | 2 | Beyond Passive Investing post: equity beta in trend following |
| C08 | 3 | Trend sleeve neutrality debate; CFTC perpetual futures intro |
| C09 | 1 | Perpetual futures vs variation margin mechanics |
| C10 | 1 | Perpetual futures as daily futures; pricing |
| C11 | 2 | Why perpetuals; CME lawsuit; hedgers |
| C12 | 3 | Futures market impact; Quantica paper: timing after drawdowns |
| C13 | 1 | Quantica sector rotation by decade |
| C14 | 3 | Single-factor explanation, continuous signals, null results |
| C15 | 2 | 2010s as exception; commodity role in crises |
| C16 | 2 | 1970s commodities; AI backtesting overfitting |
| C17 | 2 | Backtest process, probability weights |
| C18 | 1 | AI due diligence questions; Man Don't Look Down intro |
| C19 | 2 | Man drawdown paper |
| C20 | 0 | Outro and disclaimers - nothing actionable |

## Claims

### C01
- **Rob Carver** Index providers are relaxing eligibility rules (profitability, free float) to admit SpaceX, which changes what index-based benchmarks and CTA indices represent.  #mech/structural_shift _(time-bound view)_
  > in the olden days, you you couldn't get into an index unless you were profitable and they made adjustments for things like the free float of your shares.
  indicator: index eligibility rules · asset: equities · testable: no - governance observation · confidence: medium
  ^MT218-C01-1

### C02
- **Niels Kaastrup-Larsen** The new Fed chair Warsh was more hawkish than expected at his first FOMC, wants less forward guidance and a smaller balance sheet, and with high inflation there is little appetite for cuts.  #mech/policy_reaction _(time-bound view)_
  > the tone was a lot more hawkish uh than what he uh has been um uh
  indicator: Fed communication / balance sheet · asset: rates · direction: short rates / hawkish · horizon: months · conditions: current inflation environment · testable: partly · confidence: medium
  ^MT218-C02-1
- **Niels Kaastrup-Larsen** Reworking or removing government survey data would hurt economic-trend and systematic global macro strategies that use economic releases, while pure price-based trend followers are unaffected.  #mech/structural_shift _(time-bound view)_
  > we do have strategies in our world um that has come more recently that are economic trend or we have systematic global macro. Now, they do rely on this kind of data
  indicator: government economic data quality · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT218-C02-2
- **Rob Carver** US statistical data quality has degraded (cuts, secrecy, delayed releases from the government shutdown), which weakens economic indicators used as forecasting inputs.  #mech/structural_shift _(time-bound view)_
  > already been quite a serious
  indicator: US official statistics quality · asset: multi · horizon: years · testable: partly - data revisions and delays measurable · confidence: medium
  ^MT218-C02-3

### C03
- **Rob Carver** Third-party nowcasting services can replace official statistics only if raw data remains available; deliberately removing data is dangerous for models trading on it.  #mech/structural_shift
  > there are third-party services that collect data and kind of forecast what the government statistics will be
  indicator: third-party nowcasts of government statistics · asset: multi · testable: partly · confidence: medium
  ^MT218-C03-1
- **Niels Kaastrup-Larsen** A trend barometer of 36 signals weak trend following conditions in June (weak equities, metals, grains; gains in short rates and the dollar).  #mech/slow_reaction _(time-bound view)_
  > My trend barometer finished at 36 yesterday.
  indicator: Trend Barometer · asset: multi · horizon: weeks · testable: yes - indicator defined · confidence: medium
  ^MT218-C03-2
- **Rob Carver** A trend follower running only 9% annualized risk was positioned long equities (pro-deal) and flat energies, i.e. the portfolio mostly reflects the market's recent priced-in optimism.  #mech/risk_management _(time-bound view)_
  > The the biggest risk I have actually is in equities. I've got
  indicator: portfolio risk by sector · asset: multi · direction: long equities, flat energy · horizon: weeks · testable: no · confidence: low
  **Correction (cross-check):** The interpretation that the portfolio 'mostly reflects the market's recent priced-in optimism' is not stated. Rob describes his own book: 9% annualised risk (low), biggest risk a long equity position which he labels 'pro deal', and flat energies; the priced-in remark is a separate comment about the peace deal. → Rob Carver's own trend portfolio was running a low 9% annualised risk, with its largest risk a long equity position (pro peace deal) and no position in energies, so he was not positioned for the oil move.
  ^MT218-C03-3
- **Rob Carver** Carver believes more data is always better, so deliberately ending collection of official statistics is dangerous for the economy and irritating for computers trading on it.  #mech/structural_shift _(added by map cross-check)_
  > of the general belief that more data is always better
  indicator: official statistics availability · asset: multi · testable: no - belief · confidence: high
  ^MT218-C03-R1

### C04
- **Rob Carver** A peace deal that markets had priced in for weeks may produce buy the rumor, sell the fact, while oil supply shortages could keep normalization slow.  #mech/overshoot _(time-bound view)_
  > maybe this is one of those classic cases of, you know, buy the rumor, sell the sell the fact.
  indicator: oil complex around Hormuz peace deal · asset: commodities · horizon: weeks · testable: partly - event study · confidence: low
  ^MT218-C04-1
- **Niels Kaastrup-Larsen** In June 2026 oil fell about 15%, silver and platinum about 9%, offset by equities, shaping CTA returns (SocGen CTA about -0.8% in June, +9.5% YTD).  #mech/cycle_persistence _(time-bound view)_
  > the big market move so far in June has really been in the oil complex where we've seen kind of 15% drops in price.
  indicator: oil, silver, platinum June moves; SocGen CTA index · asset: commodities · horizon: weeks · testable: no - descriptive · confidence: medium
  **Correction (cross-check):** 'offset by equities' misstates the market picture. The only equity gain cited is +7% for the Nifty (Indian equity future, which is Rob's biggest long); broad equities were down in June (S&P 500 -2%, MSCI World -1%), and the host earlier called equities weak. → In June 2026 oil fell about 15%, silver and platinum about 9% each, and these losses were partly offset only by a 7% gain in the Nifty future; broad equity indices were slightly down (S&P -2%, MSCI World -1%); SocGen CTA was about -0.8% in June and about +9.5% YTD.
  ^MT218-C04-2
- **Niels Kaastrup-Larsen** Mid-June 2026 performance data: BTOP50 -85bp in June (+8.76% YTD), SG CTA -81bp (about +9.5% YTD), SG Trend about -1.25% (+9% YTD), short-term traders -0.25% (+5% YTD), versus MSCI World about -1% (+9% YTD), US Aggregate bonds flat (+0.5% YTD) and S&P 500 -2% (+9% YTD), so CTA indices roughly matched equities year to date with a small June loss.  #mech/new _(added by sonnet-xhigh cross-check, time-bound view)_
  > the Beta 50 index as of Tuesday is down 85 basis points for the month, up 8.76% so far this this year
  indicator: BTOP50; SG CTA Index; SG Trend Index; SG Short-Term Traders Index; MSCI World; US Aggregate; S&P 500 · asset: multi · horizon: weeks · conditions: June 2026 to mid-month only · testable: yes - index data · confidence: high
  ^MT218-C04-X1

### C05
- **Rob Carver** Sharpe ratio is the main metric for adding, sizing or removing a strategy; drop one only on very strong statistical evidence of a structural break.  #mech/research_method
  > the answer is, to be honest, um I tend
  indicator: Sharpe ratio; structural break tests · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT218-C05-1
- **Rob Carver** Drawdown is a poor evaluation statistic: ignoring autocorrelation it grows with history length and falls with Sharpe, so it adds no information beyond Sharpe.  #mech/research_method
  > your drawdown's going to scale with the performance of your strategy and how long you've been running it for.
  indicator: maximum drawdown · asset: multi · testable: yes - simulate drawdown vs Sharpe and length · confidence: high
  ^MT218-C05-2
- **Rob Carver** Looking at path risk and loss clustering for each individual strategy component overcomplicates and risks overfitting; it can matter at the whole-portfolio level.  #mech/research_method
  > potentially even going down the route of overfitting as well.
  indicator: path risk, loss clustering · asset: multi · testable: partly · confidence: medium
  ^MT218-C05-3
- **Rob Carver** Skew is useful for classifying strategies into trend-like (positive skew) and carry-like (negative skew) buckets, because e.g. emerging-market FX carry has negative skew while developed bond carry is mildly positive.  #mech/risk_management
  > I think that the issue becomes more when you're combining trend following with other things like carry
  indicator: skewness by strategy · asset: multi · direction: limit negative-skew strategies to e.g. 30% of portfolio · testable: yes - skew estimates measurable · confidence: medium
  ^MT218-C05-4
- **Rob Carver** Almost no CTA is a pure trend follower: they typically hold 20-30% in convergent (non-trend, e.g. carry) strategies, while Rob Carver holds 40% because he has no client pool or allocator box to fit, so the trend/non-trend mix is a design choice constrained by clients.  #mech/new _(added by sonnet-xhigh cross-check)_
  > they'll have, you know, a 20 or a 30% allocation to what you might call divergent strategies.
  indicator: share of non-trend strategies in a CTA program · asset: multi · conditions: the speaker misspeaks 'divergent' and corrects himself to 'convergent' · testable: partly - mix of trend and carry can be backtested · confidence: medium
  ^MT218-C05-X1
- **Rob Carver** Carver prefers simple evaluation of strategy components and avoids adding path-risk and loss-clustering tests on each one for fear of overfitting.  #mech/new _(added by map cross-check)_
  > I'm a big fan of keeping things simple
  indicator: none · asset: multi · conditions: individual strategy components · testable: no - preference · confidence: high
  ^MT218-C05-R1

### C06
- **Rob Carver** Skew estimates are statistically unreliable, so use skew only as a classification device with a cap on the negative-skew bucket, not as a formal utility with Sharpe.  #mech/research_method
  > I'm wary of using skew in of itself as in sort of very constantative ways
  indicator: skewness estimation error · asset: multi · testable: yes · confidence: medium
  ^MT218-C06-1
- **Rob Carver** The factor zoo has hundreds of factors but only a handful of independent drivers, so true diversification is less than the number of factors suggests.  #mech/research_method
  > the more that these sort of the the fewer kind of real things that are driving the world the less help diversification's going to be for you.
  indicator: factor clustering · asset: multi · testable: yes · confidence: medium
  ^MT218-C06-2
- **Rob Carver** Cross-sectional momentum is a relative factor (winners against losers) whereas trend following is an absolute, time-series factor, so the two should not be treated as the same source of return when counting factors.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > momentum, which is different from a trend following cuz it's a relative factor, not an absolute factor
  indicator: cross-sectional momentum vs time-series trend · asset: multi · testable: yes - compare return series · confidence: high
  ^MT218-C06-X1

### C07
- **Rob Carver** Trend following in equities is on average net long, so part of its return is the equity risk premium plus extra return from sometimes being short.  #mech/risk_premium
  > if you say trend follow equities, you will be on average net long equities.
  indicator: average equity beta of trend following · asset: equities · horizon: years · testable: yes · confidence: high
  ^MT218-C07-1
- **Rob Carver** If trend following is a sleeve of a 60/40 portfolio, make it more neutral (long only when trend is strong) to avoid double-counting equity and bond premia.  #mech/risk_management
  > if your trend following portfolio is say 20% of a bigger portfolio and that bigger portfolio is say 60/40
  indicator: average beta of trend sleeve · asset: multi · direction: reduce average equity and bond exposure in trend sleeve · horizon: years · conditions: only if the sleeve is a small part of a portfolio already holding the premia · testable: partly · confidence: medium
  ^MT218-C07-2

### C08
- **Niels Kaastrup-Larsen** Do not distort a trend program to fit the rest of the portfolio; adjust the other holdings, because distorting sectors changes the interaction among all markets.  #mech/risk_management
  > I think if you feel you have too much equity, you sell the equity. You let the trend following program run
  asset: multi · testable: no · confidence: medium
  ^MT218-C08-1
- **Niels Kaastrup-Larsen** Trend following adds access to markets investors cannot easily trade themselves and is unbiased about long or short, e.g. fully short equities in a prolonged crisis.  #mech/structural_shift
  > it adds the market you don't trade yourself.
  asset: multi · testable: no · confidence: medium
  ^MT218-C08-2
- **Rob Carver** Within a CTA sleeve, tilt sector allocation away from financials (already held) toward commodities for better portfolio diversification.  #mech/risk_management
  > tilting your sector allocation within your CTA away from financials that most people already have exposure to and towards things like commodities
  indicator: sector weights in CTA · asset: commodities · direction: overweight commodities, underweight financials · horizon: years · conditions: limited allocation to the CTA sleeve · testable: partly · confidence: medium
  ^MT218-C08-3
- **Rob Carver** Rebuttal to the host: investors who can only allocate 5-20% to a CTA sleeve (not restructure their 60/40) get a better total portfolio if the sleeve carries less equity and bond beta; the ideal is a bigger CTA bucket, but that is often not an option. Niels counters that with only 5% in trend the sleeve's equity exposure is not worth worrying about.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > you'll get a better portfolio overall if that five or 10 or 15 or 20% has less exposure overall to equities and bonds than than otherwise
  indicator: equity and bond beta of the trend sleeve · asset: multi · direction: reduce average equity/bond exposure inside a small trend sleeve · conditions: small CTA allocation inside a 60/40 portfolio; disputed by the host · testable: yes - backtest neutralised vs standard trend sleeve in a 60/40 · confidence: medium
  ^MT218-C08-X1

### C09
- **Rob Carver** The CFTC approved the first perpetual futures contract (crypto), which is effectively a daily-settled future with no expiry.  #mech/structural_shift _(time-bound view)_
  > it's basically a futures contract that, unlike every futures contract so far that has an expiration date, has no expiration date.
  indicator: perpetual futures · asset: other · testable: no - market structure · confidence: high
  ^MT218-C09-1

### C10
- **Rob Carver** Perpetual futures are daily-settled futures whose cash flows equal variation margin, so futures price tracks spot (interest, dividend and storage costs are negligible) and no rolling is needed.  #mech/structural_shift
  > although these are called perpetual futures, what they really are in the sense is daily futures.
  indicator: futures-spot basis · asset: multi · horizon: days · testable: yes · confidence: high
  ^MT218-C10-1

### C11
- **Rob Carver** Daily-settled instruments are cheaper for day traders since they avoid overnight funding costs, while exchange trading means only bid-ask costs.  #mech/structural_shift
  > if you're day trading it's a lot it's cheaper to to do it with a bet that closes today
  indicator: overnight financing cost · asset: multi · horizon: days · testable: partly · confidence: medium
  ^MT218-C11-1
- **Niels Kaastrup-Larsen** Perpetual futures would cut volume (no rolls) for exchanges; CME sued the CFTC arguing they are swaps, and hedgers like farmers need dated futures for price discovery.  #mech/structural_shift _(time-bound view)_
  > clearly that has some massive implications for firms involved in the futures industry that rely on on volume
  indicator: futures volume · asset: multi · horizon: years · testable: no · confidence: medium
  **Correction (cross-check):** Two speakers are merged. The volume loss for exchanges and the CME lawsuit against the CFTC (swap classification) are the host's; the points that futures began as hedging tools, that farmers need dated futures, and that price discovery needs a venue for hedgers are Rob Carver's. → Niels: perpetual futures would cut exchange volume (no rolls) and the CME sued the CFTC over approval, arguing they are swaps. Rob (separate point): futures began as hedging instruments, so farmers need dated futures, and price discovery needs a venue where producers and consumers hedge even though most volume is speculative.
  ^MT218-C11-2

### C12
- **Rob Carver** If perpetuals shift hedging to OTC swaps liquidity and spreads worsen as capacity is split, and trading may concentrate in market-maker houses.  #mech/liquidity_flows _(time-bound view)_
  > I think sort of for the futures market generally, I'm not sure it's a a great development, to be honest.
  indicator: futures liquidity · asset: multi · horizon: years · testable: no · confidence: low
  ^MT218-C12-1
- **Rob Carver** Timing entry or exit of trend following by recent drawdowns does not work: return autocorrelation is too weak to predict returns after drawdowns.  #mech/research_method
  > So, I've done research and other people have done research on, for example, whether you should get out of trend following or get into trend following after drawdowns.
  indicator: autocorrelation of trend following returns after drawdowns · asset: multi · horizon: months · testable: yes - autocorrelation test · confidence: high
  ^MT218-C12-2
- **Rob Carver** An investor in a fund below its high-water mark gets the first returns without performance fees, unless in a separate share class with its own high-water mark.  #mech/risk_management
  > if you are paying performance fees, then you absolutely want to invest in a in a fund when it's in a drawdown
  indicator: high-water mark · asset: multi · conditions: pooled share class only · testable: yes · confidence: medium
  ^MT218-C12-3
- **Niels Kaastrup-Larsen** Dropping markets that have not trended recently is dangerous: cocoa was idle for 15 years and then produced its biggest trend ever, so rotating only into the best recent performers would have missed it.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > Let's leave cocoa out because it didn't perform for 15 years and bang, you missed the the biggest trend it's ever had.
  indicator: cocoa · asset: commodities · direction: keep all markets in the universe · horizon: years · testable: yes - compare full universe with performance-chasing allocation · confidence: medium
  ^MT218-C12-X1

### C13
- **Rob Carver** Quantica: trend following P&L by sector rotates across decades: 2000-09 split equities/currencies/commodities, 2010-19 almost all fixed income, 2020-26 mostly commodities with equities detracting.  #mech/cycle_persistence
  > if we look at the performance of trend following in different asset classes over time, we see some very interesting patterns.
  indicator: trend following P&L by asset class by decade · asset: multi · horizon: years · testable: yes - Quantica paper data · confidence: high
  ^MT218-C13-1
- **Rob Carver** Faced with a pattern such as sector leadership rotating by decade, a quant should first ask why it happens and whether other explanations fit, and only then ask whether it can be exploited (e.g. shifting weight to the hot asset class).  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > First of all, is there a reason why this is happening? Are there are there different explanations for why this is happening? And secondly, can I exploit this apparent predictability in some way?
  asset: multi · testable: no - research procedure · confidence: high
  ^MT218-C13-X1
- **Rob Carver** Quantica tests time-based predictability (after drawdowns) and cross-sectional predictability (which asset classes trend better) together, rather than one at a time.  #mech/new _(added by map cross-check)_
  > it takes both of those dimensions simultaneously
  indicator: sector trend performance by decade · asset: multi · horizon: decades · conditions: trend following 2000-2026 · testable: yes - paper replication · confidence: high
  ^MT218-C13-R1

### C14
- **Rob Carver** Dominance of one asset class in trend returns is a single-factor story (e.g. predictable rate cuts and hikes), not diversification, so shifting into the hot sector reduces diversification.  #mech/structural_shift
  > in these periods when one asset class is dominating, it's very much about a a sort of single factor that's driving everything.
  indicator: single-factor concentration of trend returns · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT218-C14-1
- **Rob Carver** A continuous (trend-strength scaled) signal already tilts toward asset classes with stronger trends, so extra performance chasing of asset classes is unnecessary and does not add return.  #mech/research_method
  > by allocating to things with stronger trends, which is what you do naturally if you've got a continuous system, that allocation is already happening.
  indicator: trend strength by asset class · asset: multi · horizon: years · testable: yes - Quantica result · confidence: high
  ^MT218-C14-2
- **Rob Carver** Publishing null results is a sign of good research; Quantica found tactical asset-class chasing does not add value.  #mech/research_method
  > It's just as valuable to find out that something isn't working as to find out that something is working.
  asset: multi · testable: no · confidence: high
  ^MT218-C14-3

### C15
- **Niels Kaastrup-Larsen** The 2010-19 fixed-income-driven trend period, with zero rates and central banks suppressing inflation, was the exception; earlier decades and the 2020s show more diverse contribution including commodities.  #mech/structural_shift
  > that decade was not the new norm it's the odd one out.
  indicator: trend following sector contribution · asset: multi · direction: favor diversified portfolios including commodities · horizon: years · testable: partly · confidence: medium
  **Correction (cross-check):** Stated as observed fact, but it is the host's conjecture. The Quantica paper covers only 2000-2026; Niels says he would have liked the 1990s and 1980s included and thinks they would look more like 2000-09 or the 2020s. → Niels Kaastrup-Larsen: the 2010-19 fixed-income-driven decade (zero rates, central banks suppressing inflation) was the odd one out, not the new norm; he expects (not shown in the paper) that the 1970s-90s looked more like 2000-09 and 2020-26 with commodities contributing strongly.
  ^MT218-C15-1
- **Niels Kaastrup-Larsen** A reputable study found commodities are the most consistent trend sector in crises, so a portfolio should include many truly uncorrelated markets rather than overweight liquid financial markets.  #mech/risk_management
  > the most consistent sector in a crisis is the commodity sector
  indicator: sector P&L in crises · asset: commodities · horizon: years · testable: yes · confidence: medium
  ^MT218-C15-2
- **Niels Kaastrup-Larsen** Over 20-25 years, even through the long equity bull market, equities have not been a strong contributor to trend following P&L, so the financial-sector bias of many CTAs has not been rewarded by equities.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > if you go back 20, 25 years, I mean, even through this bull market of equities
  indicator: equity sector share of trend P&L · asset: equities · horizon: years · conditions: uses data the speaker had access to, not shown · testable: yes - sector attribution of a trend index · confidence: medium
  ^MT218-C15-X1
- **Niels Kaastrup-Larsen** CTAs have drifted toward liquid financial markets because capacity lets them run more assets and managers are paid on assets managed, an incentive that works against the more diversified commodity-heavy portfolio the speaker favours.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > focus more and more of the portfolio towards financial markets because they're more liquid usually and therefore you can manage more money
  indicator: sector weights of CTA programs · asset: multi · direction: overweight financial futures · horizon: years · conditions: fee structure based on AUM · testable: partly - sector weights of CTA indices · confidence: medium
  ^MT218-C15-X2

### C16
- **Rob Carver** The 1970s inflation was excellent for commodity trend following.  #mech/cycle_persistence
  > the inflation of the 1970s was fantastic for commodities trend following.
  indicator: inflation regime · asset: commodities · direction: long commodity trends · horizon: years · conditions: inflation shock regimes · testable: yes · confidence: medium
  ^MT218-C16-1
- **Rob Carver** AI is fine for idea generation but ideas must be tested in a robust process away from the AI, because the process matters more than the maths.  #mech/research_method
  > it's fine to use AI essentially to generate ideas, to generate strategy ideas.
  indicator: backtest process · asset: multi · testable: no · confidence: high
  ^MT218-C16-2
- **Rob Carver** AI-written code and AI-run backtests cost more in checking and rewriting than they save, so AI is used for ideas and small snippets and never trusted to run a strategy backtest.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > I've never used it to write any you know more than about 10 lines of code cuz I just don't trust it enough and I spend more time checking and rewriting it.
  asset: other · testable: no - practitioner experience · confidence: high
  ^MT218-C16-X1

### C17
- **Rob Carver** Any idea, from AI or data mining, is conceived with hindsight, so a backtest process must handle look-ahead contamination robustly.  #mech/research_method
  > that idea will almost certainly have been conceptualized using future information that you wouldn't have had at the start of your back test.
  asset: multi · testable: yes · confidence: high
  ^MT218-C17-1
- **Rob Carver** The output of backtesting should be a probability that a strategy works translating into a portfolio weight (outstanding idea 10-15%, weak idea about 0.01%), not a yes/no decision.  #mech/research_method
  > It's going to be a a probability that it's good and that will translate then into a portfolio weight.
  indicator: strategy weights · asset: multi · testable: partly · confidence: medium
  ^MT218-C17-2

### C18
- **Rob Carver** Due diligence on AI-driven strategies should ask whether models are internal or external and whether trained before a date with a pure out-of-sample test; public AI models may contain forward information.  #mech/research_method
  > did you train it on, say, data before a certain date and then have a pure out-of-sample period?
  indicator: AI model training cutoffs · asset: multi · testable: yes · confidence: medium
  ^MT218-C18-1
- **Rob Carver** Due diligence on a CTA should focus on the research process from idea to live trading (steps, checks and balances, robustness, peer review), which is the same whether the idea came from an AI, a junior researcher or data mining, because every idea is formed with forward information and the AI's own evaluation of itself should not be trusted.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > tell me what happens from through that process, from idea to live trading. What are the steps in that process? What are the checks and balances?
  asset: other · conditions: AI-specific questions only needed when the process is flawed · testable: no - due-diligence method · confidence: high
  ^MT218-C18-X1

### C19
- **Rob Carver** Drawdown studies need a definition because strictly one is in drawdown almost always; across 50 years there are only 10-20 episodes, so conclusions across assets are statistically weak.  #mech/research_method
  > he does actually define drawdowns, which is which is quite useful.
  indicator: drawdown definition and count · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT218-C19-1
- **Rob Carver** Man paper: examine joint drawdown behaviour across assets as a more rigorous crisis-alpha test than cherry-picked stress periods (e.g. omitting COVID, when trend followers did less well).  #mech/risk_management
  > when these assets were in a drawdown what other assets tend to be in a drawdown or not in a drawdown.
  indicator: joint drawdown overlap · asset: multi · horizon: years · testable: yes - Man Group paper · confidence: medium
  ^MT218-C19-2

