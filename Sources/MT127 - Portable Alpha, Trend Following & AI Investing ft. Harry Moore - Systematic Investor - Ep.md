---
source_id: MT127
title: "Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep.412"
date: 2026-08-09
channel: "Top Traders Unplugged"
url: 
words: 13945
claims: 78
added_by_crosscheck: 12
corrections: 6
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Harry Moore (Man Group, systematic/trend researcher)", "Niels Kaastrup-Larsen (host; caption 'Neils')"]
tags: [source, layer0]
---
# Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep.412

**Speakers:** Harry Moore (Man Group, systematic/trend researcher); Niels Kaastrup-Larsen (host; caption "Neils")

**Summary:** Top Traders Unplugged Systematic Investor Ep.412 (Aug 2026): Harry Moore (Man Group) and Niels discuss July/August 2026 trend-following dispersion (speed, market universe, yen intervention, AI-trade unwind), AI productivity in quant research, and two papers. Main points: trend is a cash-efficient, left-tail-uncorrelated alpha for portable alpha (needs about 40% cash, rebalancing/swap vs futures choices), and the Turtle rules map to volatility sizing, Kelly and drawdown-control mathematics.

**Approach:** trend following, portable alpha, risk management/position sizing, AI in quant research, diversification and tail correlation

**Cross-check completeness estimate of first read:** 0.88 - first reader captured nearly all data, mechanisms and paper findings; main weaknesses are six speaker attributions in C03-C05 and a few design details of the portable alpha paper (structure definition, drift, callable capital, path-based rebalancing choice)

## Argument map

**Episode thesis:** Harry Moore (Man Group) argues that in a possible AI-capex bubble (he stays balanced: it could also be right for ten years) a portfolio that looks diversified in normal times may all fall together in a 30-40% equity crash, and trend following is the one holding that is zero or negatively correlated in that left tail while using only about $20-25 of cash per $100 of exposure. His portable-alpha paper concludes that a futures/swap structure needs about 40% cash (10% margin plus 30% unencumbered) to avoid forced beta selling more than once in 100-200 years, that rebalancing rules matter little on average but a lot in 2008-type paths (tolerance bands around 10% are the compromise), and that the alpha ported must be uncorrelated in the left tail. A second paper maps the Turtle rules onto volatility-based sizing, fractional Kelly and drawdown-control mathematics.

### Harry Moore (Man Group) (guest; systematic/trend researcher at Man Group, based in New York, former actuary; co-author of the portable alpha paper 'Portable Alpha: Ask the Hard Questions')
Fingerprint: #approach/trend_following #approach/crisis_alpha_convexity #approach/portfolio_construction_stacking #approach/diversification_risk_parity #approach/position_sizing_vol_target #approach/kelly_or_conviction_sizing #approach/costs_execution #approach/research_robustness_overfitting
_Speaker note: Recorded Thursday 6 August 2026 (index data as of Tuesday night; episode uploaded 9 August). Ledger corrections applied: the remarks that humans panic on intervention rumours while rules-based systems hold the yen short, and that sizing must stop a single position hurting too much, are his; the 20/60/130/260-day speed comparison and the estimate of CTA positioning are the host's; the point that slow models won because no persistent turning point let fast speeds shine, and 'keep some dynamism', are his. Views are his own research views as an employee of Man Group, not necessarily the firm's._

**Worldview premises**
- Being right on a theme does not prevent trouble: a hedge fund that was dollar or market neutral on paper was concentrated in one theme (the other side of the AI trade), so a July 2026 theme reversal caused a large loss; compounding on one idea is dangerous. _[experience, stated; support: The reported hedge fund loss (about two thirds of 45 billion); media reports he cautions may not be fully accurate.]_ ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C02-1|C02-1]])
- Authorities intervene when a move has run so far for so long that natural market forces are not reversing it; such interventions are hard to simulate (a 10-sigma yen move) so sizing must limit damage from any one position. _[institutional, stated; support: Yen intervention at end of July 2026; Swiss franc precedent raised by the host.]_ ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C03-4|C03-4]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C03-2|C03-2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C03-3|C03-3]])
- In trend following the short in the yen is uncomfortable and carries intervention rumours; humans panic and exit while rules-based systems do not. _[behavioural, stated; support: General experience; one intervention did produce a sharp bump.]_ ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C03-1|C03-1]])
- Dispersion among trend managers comes from asset-class risk weights, market inclusion choices and model speed, and from thematic positions (long tech hardware/semis, short software) that were hurt in July; alternative markets (Nordic and Italian power) were more rangebound than crude and heating oil. _[empirical, stated; support: July-August 2026 model behaviour; no numbers.]_ ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C03-6|C03-6]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C04-1|C04-1]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C05-4|C05-4]])
- Fixed income has been difficult for trend for years because opposing forces (political pressure for rate cuts versus inflation and deficits) produce choppy reversals, more so in smaller markets such as Polish swaps; cross-sectional sector and factor trend models were profitable in 2026 but differently from index trend, with quality struggling. _[empirical, stated; support: Observations in his own research; no figures.]_ ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C06-1|C06-1]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C06-2|C06-2]])
- Slower trend did better in 2026 because persistent shorts in bonds, longs in energy and long stocks were held throughout and no turning point lasted long enough for faster speeds to shine, echoing recent years; his view is still to keep some faster, dynamic models to capture turning points. _[empirical, stated; support: Intuition from model holdings (he agrees with the host's speed table).]_ ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C05-2|C05-2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C05-3|C05-3]])
- AI is compared with railroads and dotcom cable building as a likely capex bubble with the usual hallmarks (capex surge, mania) that end badly for markets even if useful infrastructure remains, yet it could also be right for ten years, so one should be prepared for both and not predict. _[theoretical, stated; support: Historical analogy; Man Group's own productivity gains from AI.]_ ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C06-3|C06-3]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C07-1|C07-1]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C07-2|C07-2]])
- A portfolio of equities, bonds, commodities and private assets looks diversified in normal times but may fall together in a 30-40% S&P crash: private assets mark down slowly and return capital slowly (paper protection only), and bonds and gold sold off together earlier in the year; inflation above target for many years may stop the Fed from cutting to rescue markets. _[theoretical, stated; support: Scenario reasoning and recent bond/gold correlation; no scenario numbers.]_ ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C07-3|C07-3]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C07-4|C07-4]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C07-5|C07-5]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C08-1|C08-1]])
- Trend has no long-term view and follows prices across assets (short bonds and equities or long commodities as narratives change), can even short the AI theme, and in a left-tail shock is zero or negatively correlated to equities while other correlations rise, making it a covariance-matrix diversifier. _[theoretical, stated; support: How trend rules work; historical low-to-negative correlation to equities in the worst periods.]_ ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C08-2|C08-2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C08-3|C08-3]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C08-4|C08-4]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C20-1|C20-1]])
- AI summarises existing knowledge but cannot easily produce new alpha ideas, shifting quant research time from implementation toward ideas (from about 50/50 to 90/10) and squeezing junior implementation roles; skill atrophy from one-click answers is the risk, so test researchers by having them critique AI output. _[experience, stated; support: Own experience at Man (hundreds of Python hours now 'useless'); no evidence about hiring outcomes.]_ ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C09-1|C09-1]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C09-2|C09-2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C09-3|C09-3]])
- Trend on futures needs only about $20-25 of capital per $100 of exposure, so allocators can add trend without selling existing holdings, and freed cash can fund extra alphas (cross-sectional trend or carry) that have lower correlation, positive Sharpe and add value; this suits investors whose private assets are not returning capital quickly. _[institutional, stated; support: Futures margin arithmetic; paper they discussed on cross-sectional trend versus carry.]_ ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C10-1|C10-1]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C10-2|C10-2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C11-1|C11-1]])
- Portable alpha structures failed in 2008 from insufficient liquidity and alpha-beta correlation, and those risks still exist; resilient designs must survive the GFC, the dotcom bust and COVID; liquid alphas such as trend allow quick recapitalisation. _[empirical, stated; support: History of 2008; paper's stress tests using SG Trend (internal analysis on other alphas reported to agree).]_ ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C12-1|C12-1]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C14-2|C14-2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C12-X1|C12-X1]])
- Futures- or swap-based beta needs unencumbered cash beyond margin because a 10% fall exhausts 10% margin and counterparties call for more; swap financing cost (about 40bp) is implicit in futures, so swaps versus futures is an operational choice (futures carry no counterparty risk), not a performance edge. _[institutional, stated; support: No-arbitrage reasoning, checked in their analysis.]_ ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C13-1|C13-1]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C15-2|C15-2]])
- Only one historical path exists, so Monte Carlo is used to simulate drawdowns beyond history; most investors want the manager to bear the operational and cash-flow complexity rather than hold callable capital. _[theoretical, stated; support: Standard limitation of history; client meetings.]_ ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C13-5|C13-5]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C14-1|C14-1]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C14-X1|C14-X1]])
- Leverage is a portfolio-construction tool, not inherently risky: a 50/50 portfolio holds roughly 85% of its risk in equities, so leverage on bonds improves risk balance and Sharpe; what matters is the alpha ported. _[theoretical, stated; support: Risk-share arithmetic; he calls three-times leveraged ETFs scary because of asymmetric returns.]_ ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C19-1|C19-1]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C19-2|C19-2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C19-R1|C19-R1]])
- The Turtle rules were hand-calculable approximations of later decision and probability theory (Parkinson range estimator, Kelly criterion, Grossman-Zhou drawdown control). _[theoretical, stated; support: Polson and Sirkul paper on the mathematics of turtle trading; his reading.]_ ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C16-1|C16-1]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C16-2|C16-2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C16-3|C16-3]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C17-1|C17-1]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C17-2|C17-2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C17-3|C17-3]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C18-1|C18-1]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C18-2|C18-2]])

**Chain: Why trend protects in a left-tail shock when other diversifiers fail**
1. AI trade or capex cycle breaks (S&P down 30-40%) → Equities fall; private assets mark down slowly and return capital slowly (paper protection only): Illiquid marks lag, and capital returns slow down. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C07-3|C07-3]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C07-4|C07-4]])
2. Inflation above target for years → Bonds and gold may sell off together; the Fed may lack tools to cut: Earlier in 2026 both sold off in a correlated manner. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C07-5|C07-5]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C08-1|C08-1]])
3. Prices change narrative over weeks and months → Trend goes short equities and bonds, long commodities in an inflation shock, even short semis and hardware: No long-term view; follows prices across assets. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C08-2|C08-2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C08-3|C08-3]])
4. Left-tail covariance matrix → Trend is zero or negatively correlated while other correlations rise: Trend is a covariance-matrix diversifier. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C08-4|C08-4]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C20-1|C20-1]])
- Evidence: Scenario reasoning and historical negative correlation in the worst equity periods; no numbers for the current episode.
- Fails when: Trend gets some turns wrong and costs pain from time to time; inflationary shock with whipsaws.

**Chain: Cash buffer needed in a portable alpha structure**
1. S&P exposure through a future or swap uses as little as 10% margin → A 10% equity fall exhausts margin and counterparties demand more: Margin calls are immediate. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C13-1|C13-1]])
2. A 20% unencumbered buffer on S&P plus trend → Fully drawn down in the GFC, dotcom and COVID, forcing beta sales: Large equity drawdowns exhaust it three times in 26-27 years. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C13-2|C13-2]])
3. Forced selling at the lows → Misses the rebound (about 30% in 2009) and creates large tracking error versus the benchmark: Equities tend to rebound after crises; benchmark was 100% long. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C13-3|C13-3]])
4. About 40% cash (10% margin plus 30% unencumbered) → Forced degearing only about once in 100-200 years: Monte Carlo beyond the single historical path. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C13-4|C13-4]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C13-5|C13-5]])
- Evidence: SG Trend as alpha in the S&P plus trend historical simulation; Monte Carlo; internal tests on other alphas.
- Fails when: Some investors with callable capital or credit facilities can hold less cash; one-in-100-200 years is approximate.

**Chain: Rebalancing the beta and alpha sleeves**
1. Periodic rebalancing of beta → No longer replicates the index (tracking error at year end): An index compounds on itself; selling after gains breaks compounding. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C14-3|C14-3]])
2. Buy and hold tracks best → Mix drifts and new investors cannot enter at NAV with the intended mix, so tolerance bands (rebalance beyond about 10% drift) are preferred: Compromise between tracking and mix control. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C14-X2|C14-X2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C14-4|C14-4]])
3. 2008 path: equities fall while trend rises → Rebalancing back to target loses money; only buy and hold did better: Buys falling equities and sells rising trend. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C14-5|C14-5]])
4. Long-run averages → Rebalancing rule makes little difference over the long run, but matters in 2008 and COVID: Choose by worst paths, not average performance. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C15-1|C15-1]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C15-X1|C15-X1]])
- Evidence: Simulation with S&P and SG Trend over the long run and specific episodes.
- Fails when: Different rebalancing rules suit different investor constraints; no single right answer, per Harry.

**Chain: Choosing the alpha to port (left-tail uncorrelated)**
1. 100% beta already held → The alpha layer should not add beta: Extra beta in the same direction raises volatility and left-tail loss. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C19-X1|C19-X1]])
2. Liquidity-provision alphas (short vol, merger arbitrage, basis trade) → Look good normally but have big left tails: Liquidity dries up in shocks; deals break. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C19-3|C19-3]])
3. Test alpha against the worst 5% of beta returns → Trend has low to negative correlation in those periods and scales down with volatility, so needs less margin: Position sizes fall as volatility rises at turning points. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C20-1|C20-1]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C20-2|C20-2]])
- Evidence: Historical correlations in the worst equity periods; vol-scaling mechanics.
- Fails when: History has limited crises; the alpha's tail behaviour could change.

**Chain: Turtle rules as sizing, Kelly and drawdown mathematics**
1. Range-based volatility N with half-life about 14 days (consistent with Parkinson) → Units equalise risk across markets (one unit of crude equals one unit of Treasuries): Volatility-based sizing. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C16-2|C16-2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C16-3|C16-3]])
2. Stop at 2N → A loss of 2% of equity per position, a fractional-Kelly size on the left of the optimum: Gives up some growth for much lower ruin risk. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C17-2|C17-2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C17-1|C17-1]])
3. Correlation between markets → Handled with position-size caps rather than covariance inversion: Pen and paper rules. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C17-3|C17-3]])
4. Managers run other people's money → Drawdown rule: cut equity used for sizing by 20% after a 10% loss (formalised by Grossman and Zhou): Allocators cannot stomach an 80% drawdown. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C18-1|C18-1]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C18-2|C18-2]])
- Evidence: Polson and Sirkul paper linking the 1980s rules to published theory.
- Fails when: He defers to the host as the history expert; the paper's test with its own data is only mentioned.

**Decision process**
- [sizing] Size so that no single position (such as the yen) can hurt the book too much if an intervention reverses it; scale positions inversely with volatility so margin falls as stress rises.. Why: Policy gaps are hard to simulate; vol scaling reduces margin needs. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C03-2|C03-2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C20-2|C20-2]])
- [signal] Keep some faster, dynamic models alongside slow ones to capture turning points.. Why: Slow models won in 2026 but only persist as long as trends do. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C05-3|C05-3]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C05-2|C05-2]])
- [portfolio] Fund portable alpha with about 40% cash (10% margin plus 30% unencumbered) against the beta, and hold liquid alphas that can be recapitalised quickly.. Why: Avoid forced degearing more than once in 100-200 years. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C13-4|C13-4]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C14-2|C14-2]])
- [portfolio] Rebalance sleeves only when the S&P and trend sleeves drift about 10% out of balance; check the worst historical paths when choosing a rule.. Why: Tracks the index closely while limiting drift; rebalancing rule matters in 2008-type paths. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C14-4|C14-4]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C15-X1|C15-X1]])
- [portfolio] Pick an alpha uncorrelated in the left tail; test it against the worst 5% of beta returns.. Why: Liquidity-provision alphas fail when it matters. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C19-3|C19-3]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C20-1|C20-1]])
- [execution] Choose swap versus futures by operational preference and counterparty risk, not performance.. Why: Financing costs wash out (about 40bp implicit in futures). ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C15-2|C15-2]])
- [research] Use Monte Carlo to simulate severe drawdowns beyond the single historical path; ask providers what happens in a 20% drawdown month (how margin is met, whether beta is sold, tracking error).. Why: Only one path of history exists; stress behaviour must be known before investing. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C13-5|C13-5]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C15-X2|C15-X2]])

**Evidence style:** Scenario reasoning and analogy for the macro view; simulation on historical data plus Monte Carlo for portable alpha; links practical rules to published theory (Kelly, Parkinson, Grossman-Zhou); stays balanced on AI and defers to the host on history.

**Views at the time**
- (2026-08-06) July 2026 trend dispersion came from the AI-trade reversal and rallying energy markets: trend models were long oil and long stocks, and asset-class risk weights, market choices and speed created dispersion.. Reasoning: Three-month moving-average-like models held longs in the oil complex and stocks. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C03-6|C03-6]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C04-1|C04-1]])
- (2026-08-06) The AI trade may be a bubble or may be right for ten years; the right response is a portfolio that survives either outcome with trend as the left-tail diversifier.. Reasoning: Cannot predict; capex bubble analogies versus productivity gains inside Man Group. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C06-3|C06-3]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C07-1|C07-1]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C07-2|C07-2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C08-4|C08-4]])
- (2026-08-06) Fixed income remains difficult for trend because of competing political and inflation forces, especially in smaller markets.. Reasoning: Choppy reversals as pressure for rate cuts collides with inflation and deficits. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C06-1|C06-1]])
- (2026-08-06) A year in which slower trend did better; no persistent turning point yet.. Reasoning: Persistent short bonds, long energy and long stocks held across the year. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C05-2|C05-2]])

### Niels Kaastrup-Larsen (host; caption 'Neils') (host, Top Traders Unplugged; CTA industry commentator (Dunn), runs a trend barometer)
Fingerprint: #approach/trend_following #approach/market_internals_leading #approach/portfolio_construction_stacking #approach/crisis_alpha_convexity #approach/manager_selection_allocation #approach/geopolitics
_Speaker note: Captions spell him 'Neils Castro Blaston'. Ledger corrections moved the yen-intervention rules remark, sizing point and slow-speed discussion to Harry, and moved the 20/60/130/260 speed table and the CTA-positioning estimate to Niels._

**Worldview premises**
- Concentration and leverage on one idea are dangerous and diversification matters (a 45 billion fund losing about two thirds in weeks; a 2x levered ETF lost over 40% while the underlying stock round-tripped to flat). _[experience, stated; support: Press stories and a guest's example (SK Hynix-type stock); volatility decay.]_ ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C02-2|C02-2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C04-2|C04-2]])
- The yen kept weakening after the BOJ began raising rates, so the rate-differential story failed to hold; joint intervention hit trend followers short yen, though earlier interventions did not last; the intervention was about a 10-sigma move, and the 2015 Swiss franc depeg (20-30 sigma) is the precedent for policy-driven gaps, the main tail risk for trend followers. _[institutional, stated; support: Historical precedent; his own recollection.]_ ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C02-3|C02-3]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C02-X1|C02-X1]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C03-3|C03-3]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C03-X1|C03-X1]])
- Combining trend and equities in portable alpha yields roughly the sum of both return streams rather than the average; other stacked combinations may look great in backtests but hide risks not exposed in recent decades, partly through correlations. _[empirical, stated; support: A slide he has shown for years; no data given here.]_ ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C11-2|C11-2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C15-3|C15-3]])
- The Turtles' edge was risk management and scaling, not the breakout entry; clear rules were mistaken for simplicity; trend followers are risk managers first, controlling risk not returns, with small losses and intelligent scaling to survive until outsized moves arrive. _[experience, stated; support: Industry experience over decades; the Turtles' fame came from books and narrative.]_ ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C18-3|C18-3]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C18-4|C18-4]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C18-X1|C18-X1]])
- AI code generation will change due-diligence answers about researchers writing and reviewing their own code, shifting control to review of AI-written code. _[institutional, stated; support: Due-diligence meetings he attends.]_ ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C10-X1|C10-X1]])

**Evidence style:** Industry data (barometer, indices), anecdote and history; asks the guest for mechanics and reports investor objections (leverage worry).

**Views at the time**
- (2026-08-06) Trend barometer at 27 is a very low reading, implying a soft start to August; July had more dispersion among managers than normal.. Reasoning: Barometer measures aggregate trend strength. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C03-5|C03-5]])
- (2026-08-04) Early August 2026 numbers (as of Tuesday): SG CTA about -0.9% for the month, +7.15% YTD; BTOP50 +7.17% YTD; trend index +6.89%; short-term traders +3.3%; MSCI World +12.5% and S&P 500 +12.8% YTD.. Reasoning: Index data. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C04-3|C04-3]])
- (2026-08-06) CTAs are probably still long equities, metals, energies and the dollar and most likely short fixed income, with little directional change but different commitment levels.. Reasoning: His estimate, not Man Group positioning data. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C04-4|C04-4]])
- (2026-08-06) In a standard trend model in 2026 the 20-day lookback was negative, 60-day less negative, 130-day slightly positive and 260-day best, so slower speeds did better.. Reasoning: Own look at a traditional model. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C05-1|C05-1]])

### Disagreements
- **Whether the leverage in portable alpha should worry investors**: Niels Kaastrup-Larsen: Investors worry that stacking trend on beta is leverage (more than $100 in total, replacing two unlevered holdings); he relays the objection and asks why they should be less concerned. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C15-3|C15-3]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C11-2|C11-2]]); Harry Moore: Leverage is a portfolio-construction tool that can reduce risk by raising diversification, provided the ported alpha is uncorrelated in the left tail and cash efficient, so margin needs fall in stress. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C19-1|C19-1]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C19-2|C19-2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C19-3|C19-3]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C20-2|C20-2]])
- **Emphasis on trend speed**: Niels Kaastrup-Larsen: Speed table shows slower lookbacks did better in 2026 (he and his firm trade the most liquid futures). ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C05-1|C05-1]]); Harry Moore: Agrees slower did better but wants some faster, dynamic models to capture turning points. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C05-2|C05-2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C05-3|C05-3]])

### Gaps and conflicts
- The hedge fund loss story (45 billion, losing two thirds in weeks) is from headlines both speakers say should not be fully believed; no verification. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C02-1|C02-1]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C02-2|C02-2]])
- The 40% cash buffer result rests on SG Trend as the alpha and on simple S&P plus trend simulation; the claim that conclusions hold for other alphas is asserted without figures. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C13-4|C13-4]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C12-X1|C12-X1]])
- 'About once every 100-200 years' depends on Monte Carlo assumptions not described in the conversation; the 20% buffer 'drawn down three times in 26-27 years' relies on history with only a few crises. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C13-2|C13-2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C13-4|C13-4]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C13-5|C13-5]])
- Harry argues both a bubble and a ten-year-right scenario without assigning probabilities; trend is offered as a hedge without evidence about the specific AI-theme drawdown mechanics. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C07-1|C07-1]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C07-2|C07-2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C08-3|C08-3]])
- Statement that private assets give only paper protection is argued by analogy and press reports (FT) rather than data. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C07-4|C07-4]])
- The 'sum of the two return streams' claim for trend plus equities is a visual from the host's slide deck; no data in the conversation and it ignores leverage costs. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C11-2|C11-2]])
- AI productivity claims (50/50 to 90/10 research time) are an estimate by Harry with no measurement; effects on hiring are admitted to be unsettled. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C09-2|C09-2]])
- Turtle mathematics: Harry says the paper shows a test with their own data later on but does not give the result; the half-life and Kelly claims are summaries of the paper. ([[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C16-2|C16-2]], [[MT127 - Portable Alpha, Trend Following & AI Investing ft. Harry Moore - Systematic Investor - Ep#^MT127-C17-1|C17-1]])

### Forward-looking inputs (reader synthesis)
(reader) Inputs the speakers name: the trend barometer (27, weak), persistence of long energy, long stocks and short bond positions as against reversals, and whether a turning point persists long enough to reward faster speeds; for the left tail, correlation of alphas with the worst 5% of equity returns, margin usage and volatility scaling at turning points, and inflation staying above target (limiting Fed rescue). Horizons: weeks to months for trend dispersion; multi-decade simulations for portable alpha buffers.

### Reader inferences (not stated by the speakers)
- (reader) Harry's argument is a covariance argument: the case for trend rests on its correlation in the left tail, not on its average return, so the same logic would apply to any alpha tested against the worst 5% of beta returns.
- (reader) The 40% cash rule is a risk-management choice trading a smaller alpha layer for a very low probability of forced beta selling; it follows from valuing tracking error and missing rebounds more than extra alpha.
- (reader) The Turtle paper and the portable alpha paper share one logic: size so that ruin or forced liquidation is a far tail event, accepting lower growth, which Harry presents as the prudent left side of the Kelly hill.
- (reader) The speakers' separate remarks on fixed income and the yen imply that dispersion in 2026 trend results came less from signal quality than from universe and risk-weight choices.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | nothing actionable: greetings, books and old phones small talk |
| C02 | 3 | Situational Awareness fund blow-up (theme concentration), BOJ/Fed yen intervention |
| C03 | 6 | Intervention vs rules-based trend, position sizing, 10-sigma move; trend barometer; July dispersion drivers |
| C04 | 4 | Themes (semis/software) dispersion, levered ETF decay, index performance data, CTA positioning, trend speed comparison starts |
| C05 | 4 | Speed results (20/60/130/260 day), slow outperformance, market-universe dispersion in energies |
| C06 | 3 | Fixed income dispersion, cross-sectional equity sector models, quality factor; AI trade bubble vs upside framing |
| C07 | 5 | AI bubble vs upside scenario, productivity gains, illusion of diversification in a 30-40% drawdown |
| C08 | 4 | Bonds also selling off, trend as left-tail diversifier, AI generation junior skills |
| C09 | 3 | AI changes quant researcher time split, hiring and testing |
| C10 | 2 | Humans reviewing code; cash efficiency of trend, freeing cash for cross-sectional/carry alphas |
| C11 | 3 | Cash-efficient access when private capital is illiquid; portable alpha construction; stacking returns |
| C12 | 1 | Portable alpha paper motivation, 2008 failure causes, cash buffer setup |
| C13 | 5 | Margin and cash buffers: 20% vs 40%, Monte Carlo, forced de-risking cost |
| C14 | 5 | Operational preference for no margin calls, liquid alpha, rebalancing replicates index issue |
| C15 | 3 | Rebalancing rule effects, swaps vs futures, caution on back-tested combinations; Turtle paper introduced |
| C16 | 3 | Turtle paper: range volatility estimate, Parkinson, volatility-based position sizing |
| C17 | 3 | Kelly criterion, Thorp, 2N stop equals 2% equity, correlation caps |
| C18 | 4 | Turtle drawdown rules and Grossman-Zhou, risk management is the edge |
| C19 | 3 | Leverage as tool, risk-balance of 50/50, choosing alpha uncorrelated in left tail |
| C20 | 2 | Check alpha vs worst 5% beta periods, trend negative correlation, volatility scaling lowers margin; outro |

## Claims

### C02
- **Harry Moore (Man Group, systematic/trend researcher)** A hedge fund that is dollar or market neutral on paper can still be concentrated in one theme (the other side of the AI trade), so a theme reversal caused a large loss; being right does not prevent trouble.  #mech/crowding_positioning _(time-bound view)_
  > even if on paper you look somewhat like dollar neutral or market neutral
  indicator: theme exposure (AI) · asset: equities · horizon: weeks · conditions: when a book is built around a single theme despite neutral beta · testable: partly: factor/theme concentration can be measured · confidence: high
  ^MT127-C02-1
- **Niels Kaastrup-Larsen (host; caption "Neils")** A 45 billion fund losing about two thirds in weeks shows that concentration and leverage on one idea are dangerous and diversification matters.  #mech/risk_management _(time-bound view)_
  > that diversification uh really does uh u matter
  asset: equities · horizon: weeks · testable: partly: concentration-loss anecdote · confidence: high
  ^MT127-C02-2
- **Niels Kaastrup-Larsen (host; caption "Neils")** Joint central-bank intervention in the yen hit trend followers who were short yen, though past interventions did not last long.  #mech/policy_reaction _(time-bound view)_
  > intervening uh in the Japanese yen only a couple of days before month end which you know it did have an effect
  indicator: USDJPY · asset: fx · direction: yen up, trend short-yen positions hurt · horizon: days · conditions: when intervention follows a long one-way yen move · testable: yes: intervention dates and trend returns are public · confidence: high
  ^MT127-C02-3
- **Niels Kaastrup-Larsen** The yen kept weakening even after the Bank of Japan began raising rates following 30 years of near-zero rates, so the rate-differential story failed to hold the currency; authorities then intervened, as they had a couple of times in the last two to three years without lasting effect.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > the BOJ started to raise rates for the first time in in ages and of course interest rates has continued to move higher despite uh and and the yen has despite actually continued to move lower
  indicator: USDJPY, BOJ policy rate · asset: fx · direction: yen weakness persisted despite BOJ hikes · horizon: years · conditions: Late-stage one-way trend where fundamentals no longer restrain the move. · testable: partly - intervention episodes and their durability can be listed from history · confidence: medium
  ^MT127-C02-X1

### C03
- **Niels Kaastrup-Larsen (host; caption "Neils")** Rules-based systems hold uncomfortable positions through intervention rumours while humans panic and exit.  #mech/behavioral
  > Humans start to panic. The rulesbased systems don't.
  asset: multi · horizon: days · testable: partly: systematic vs discretionary reaction can be compared · confidence: medium
  **Correction (cross-check):** Wrong speaker. The remark that humans panic on intervention rumours while rules-based systems hold the uncomfortable short is Harry Moore's reply to Niels, not Niels's. → Harry Moore: in trend following the yen short is uncomfortable and carries intervention rumours; humans panic and exit, rules-based systems do not.
  ^MT127-C03-1
- **Niels Kaastrup-Larsen (host; caption "Neils")** Position sizing must be set so that a single position (such as the yen) cannot hurt the portfolio too much when an intervention reverses it.  #mech/risk_management
  > it's the importance of stizing and and making sure that that one position um can't can't hit you too much
  indicator: position size limit · asset: multi · testable: yes: size caps vs loss can be tested · confidence: high
  **Correction (cross-check):** Wrong speaker. Harry Moore makes the point about sizing so that one position cannot hurt too much (Niels then finishes with 'make something turn around'). → Harry Moore: position sizing must ensure that a single position (the yen) cannot hurt the book too much when an intervention reverses it.
  ^MT127-C03-2
- **Niels Kaastrup-Larsen (host; caption "Neils")** The yen intervention produced a roughly 10 standard deviation move, rare and hard to simulate in market data, though such events exist.  #mech/risk_management _(time-bound view)_
  > I think it was like a 10 standard deviation move
  indicator: yen daily move · asset: fx · horizon: days · testable: partly: tail events are rare in samples · confidence: medium
  ^MT127-C03-3
- **Harry Moore (Man Group, systematic/trend researcher)** Authorities intervene when a move has run so far for so long that natural market forces are not reversing it.  #mech/policy_reaction
  > when you've when you've had a move go so far for for so long
  indicator: extended one-way FX moves · asset: fx · direction: reversal after extended move · horizon: months · conditions: after very long trends · testable: partly: intervention after extremes is testable · confidence: medium
  ^MT127-C03-4
- **Niels Kaastrup-Larsen (host; caption "Neils")** A trend barometer reading of 27 is a weak signal, implying a soft start to August for trend followers.  #mech/slow_reaction _(time-bound view)_
  > my trend barometer finished yesterday at 27. And that's a very low reading actually.
  indicator: trend barometer · asset: multi · horizon: weeks · testable: partly: barometer definition proprietary · confidence: medium
  ^MT127-C03-5
- **Harry Moore (Man Group, systematic/trend researcher)** July dispersion among trend managers came from asset-class risk weights, market inclusion choices and model speed, with long oil and long stocks positions diverging in outcome.  #mech/research_method _(time-bound view)_
  > choices of whether to exclude certain markets or whole asset classes would have created a lot a lot of dispersion in in July
  indicator: trend manager return dispersion · asset: multi · horizon: months · testable: yes: dispersion across indices is public · confidence: high
  ^MT127-C03-6
- **Niels Kaastrup-Larsen** The 2015 Swiss franc depeg was a 20 to 30 standard deviation move, a precedent showing that policy-driven gaps far larger than the 10 sigma yen intervention move exist and are the main tail risk for trend followers holding trending positions.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > when the Swiss Frank um you know got deep depicted from from the euro I think it was like 20 or 30 standard deviations
  indicator: Swiss franc 2015 de-peg, daily move in standard deviations · asset: fx · direction: policy-driven gap against a crowded trend position · horizon: days · conditions: Positions in managed or pegged currencies are most exposed. · testable: yes - gap sizes in sigma terms can be measured · confidence: medium
  ^MT127-C03-X1

### C04
- **Harry Moore (Man Group, systematic/trend researcher)** Thematic trend positions (long tech hardware/semis, short software) were hurt in July, accounting for dispersion among managers.  #mech/crowding_positioning _(time-bound view)_
  > if you were trend following themes and you were you were long let's say u tech hardware companies you're long semiconductors and you were um uh short kind of software like that would have would have hurt
  indicator: semis vs software · asset: equities · horizon: months · testable: partly: theme baskets can be backtested · confidence: medium
  ^MT127-C04-1
- **Niels Kaastrup-Larsen (host; caption "Neils")** A 2x levered ETF lost over 40% while the underlying stock round-tripped to flat, showing volatility decay in levered retail products.  #mech/risk_management
  > the stock had gone up like 120% and then down to flat for over a 3 months period but the 2x levered uh ETF was down like 40 plus% for that period
  indicator: 2x levered single-stock ETF · asset: equities · horizon: months · conditions: in volatile round trips · testable: yes: path-dependence of levered ETFs is mathematically testable · confidence: high
  ^MT127-C04-2
- **Niels Kaastrup-Larsen (host; caption "Neils")** Early August 2026 trend index data: SG CTA index about -0.9% for the month, +7.15% YTD, BTOP50 +7.17% YTD, trend index +6.89%, short-term traders +3.3% YTD, MSCI World +12.5% YTD, S&P 500 +12.8% YTD.  #mech/slow_reaction _(time-bound view)_
  > The sock gen CG index is down 88 basis points up 7.15% so far this year.
  indicator: SG CTA, SG Trend, BTOP50, S&P 500 · asset: multi · horizon: months · testable: yes: public index data · confidence: high
  ^MT127-C04-3
- **Harry Moore (Man Group, systematic/trend researcher)** Estimated CTA positioning in Aug 2026: long equities, metals, energies and dollar; short fixed income.  #mech/crowding_positioning _(time-bound view)_
  > CTAs are still long equities probably long metals probably as you said long energies um probably long the dollar I would imagine and then still most likely short fixed income
  indicator: CTA positioning estimate · asset: multi · direction: long equities, metals, energies, dollar; short bonds · horizon: weeks · testable: partly: replication of positioning from trend signals possible · confidence: medium
  **Correction (cross-check):** Speaker is most likely Niels, not Harry: the passage continues Niels's reading of index data and says 'as you said long energies' and 'I would imagine', and then invites Harry to comment. It is an estimate, not Man Group positioning data. → Niels Kaastrup-Larsen (estimate): CTAs are probably still long equities, metals, energies and the dollar, and most likely short fixed income, with little directional change but different commitment levels.
  ^MT127-C04-4

### C05
- **Harry Moore (Man Group, systematic/trend researcher)** In 2026 YTD a standard trend model was negative at a 20-day lookback, less negative at 60, slightly positive at 130 and best at 260 days, so slower speeds did better.  #mech/slow_reaction _(time-bound view)_
  > if you had chosen a 20-day look back, again, this is just from this specific model, um, you would actually have been down uh, this year
  indicator: trend look-back (20/60/130/260 days) · asset: multi · direction: slower trend better · horizon: months · conditions: in a year without persistent turning points · testable: yes: speed-sorted trend returns can be computed · confidence: high
  **Correction (cross-check):** Wrong speaker. The comparison of 20/60/130/260-day speeds is Niels's own look at a standard trend model ('you mentioned speed could have been a determinant'), and Harry then comments. → Niels Kaastrup-Larsen: in a standard trend model in 2026 the 20-day lookback was negative, 60-day less negative, 130-day slightly positive and 260-day best.
  ^MT127-C05-1
- **Niels Kaastrup-Larsen (host; caption "Neils")** Faster trend speeds win only after turning points that persist; absent those, slow models (short bonds, long energy, long stocks held throughout) outperform, echoing recent years.  #mech/slow_reaction _(time-bound view)_
  > we haven't had a a a turning point that that's that's persisted for long enough for for for the faster speeds to to kind of shine
  indicator: trend speed · asset: multi · direction: slow trend over fast trend · horizon: years · conditions: when reversals do not persist · testable: yes: speed vs regime test · confidence: high
  **Correction (cross-check):** Wrong speaker. The point that slow models won because no persistent turning point let fast speeds shine is Harry Moore's reply; Niels only agrees afterwards. → Harry Moore: slower trend systems held persistent short bonds, long energy and long stocks and did better, and no turning point has lasted long enough for faster speeds to shine, echoing recent years.
  ^MT127-C05-2
- **Niels Kaastrup-Larsen (host; caption "Neils")** Blend some faster speeds with slow models to capture turning points.  #mech/slow_reaction
  > my my view is always to have some dynamism there that you can you can still capture some of those turning points
  indicator: trend speed mix · asset: multi · testable: yes: speed-blend backtest · confidence: medium
  **Correction (cross-check):** Wrong speaker. 'My view is always to have some dynamism there' is Harry Moore. → Harry Moore: keep some faster, more dynamic models alongside slow ones to capture turning points.
  ^MT127-C05-3
- **Harry Moore (Man Group, systematic/trend researcher)** Alternative markets (Nordic and Italian power) were more rangebound than crude and heating oil in 2026, so market universe drives trend performance dispersion.  #mech/structural_shift _(time-bound view)_
  > markets have have just tended to be a little bit more rangebound than we've seen in the more traditional energy markets this year
  indicator: market universe, power vs oil · asset: commodities · direction: trend profits in liquid oil · horizon: months · testable: yes: universe-sorted trend returns · confidence: high
  ^MT127-C05-4

### C06
- **Harry Moore (Man Group, systematic/trend researcher)** Fixed income has been difficult for trend for years because opposing forces (political pressure for rate cuts vs inflation and deficits) produce choppy reversals, more so in smaller markets such as Polish swaps.  #mech/cycle_persistence _(time-bound view)_
  > you've got the administrator administration shouting for uh rate cuts rate cuts you have markets follow that occasionally then you look at the inflation you look at rising deficits
  indicator: fixed income trend returns · asset: rates · horizon: years · conditions: when policy and fundamentals pull in opposite directions · testable: partly: trend returns in bonds are testable · confidence: medium
  ^MT127-C06-1
- **Harry Moore (Man Group, systematic/trend researcher)** Cross-sectional sector and factor trend models (semis vs software, value, momentum, quality) were profitable in 2026 but differently from index trend; quality struggled.  #mech/slow_reaction _(time-bound view)_
  > These cross-sectional models, I mean, from a from a high level have also been profitable just in a very very different way
  indicator: cross-sectional equity sector/factor trend · asset: equities · horizon: months · testable: yes: factor and sector series · confidence: medium
  ^MT127-C06-2
- **Harry Moore (Man Group, systematic/trend researcher)** AI is compared to railroads and dotcom cable building as a likely capex bubble.  #mech/overshoot
  > all of these comparisons back to the railroads back to laying cable in the.com bust
  indicator: AI capex · asset: equities · horizon: years · testable: partly: capex booms and subsequent returns can be studied · confidence: medium
  ^MT127-C06-3

### C07
- **Harry Moore (Man Group, systematic/trend researcher)** Bear case: AI shares the hallmarks of past bubbles (capex surge, mania) that end badly for markets even if useful infrastructure remains.  #mech/overshoot
  > It's got all the hallmarks of these prior periods where capex went through the roof.
  indicator: AI capex, equity valuations · asset: equities · horizon: years · testable: partly: analogy based · confidence: medium
  ^MT127-C07-1
- **Harry Moore (Man Group, systematic/trend researcher)** Stay balanced: the AI trade could also be right for 10 years, so one cannot predict and portfolios should be built for either outcome.  #mech/risk_management
  > Maybe there is this huge upside scenario where um the trade that we saw go wrong last month is the right trade and it works over over the next 10 years.
  asset: equities · horizon: years · testable: no: uncertainty argument · confidence: medium
  ^MT127-C07-2
- **Harry Moore (Man Group, systematic/trend researcher)** A portfolio of equities, bonds, commodities and private assets appears diversified in normal times but may all fall together in a 30-40% S&P crash.  #mech/risk_management
  > Now on paper, you look diversified, right? These assets they seem to have kind of in normal times somewhat low correlations with each other.
  indicator: cross-asset correlation in drawdown · asset: multi · horizon: months · conditions: in left-tail equity shocks · testable: yes: conditional correlations in drawdowns · confidence: high
  ^MT127-C07-3
- **Harry Moore (Man Group, systematic/trend researcher)** Private assets mark down slowly and return capital slowly, so they give only paper protection in a crash.  #mech/risk_management
  > they may mark down more slowly but at some point you're going to take hits there
  indicator: private asset marks · asset: other · horizon: years · testable: partly: smoothed returns understate drawdowns · confidence: medium
  ^MT127-C07-4
- **Harry Moore (Man Group, systematic/trend researcher)** Bonds and gold have sold off together, so they were not a reliable hedge for equity drawdowns in an inflationary environment.  #mech/cycle_persistence _(time-bound view)_
  > Then in bonds and gold like earlier in the year we saw again both of those sell off in a in a fairly correlated manner.
  indicator: bond and gold correlation · asset: multi · horizon: months · conditions: inflation above target for years · testable: yes: correlation series · confidence: high
  ^MT127-C07-5

### C08
- **Harry Moore (Man Group, systematic/trend researcher)** With inflation above target for many years, the Fed may not be able to cut rates to rescue markets, leaving bonds also vulnerable to a hard sell-off.  #mech/policy_reaction _(time-bound view)_
  > do they have the tools to really cut rates uh like we've seen in in the past to to kind of boy markets
  indicator: Fed funds, inflation · asset: rates · direction: bonds down alongside equities · horizon: years · conditions: when inflation stays above target · testable: partly: Fed reaction function · confidence: medium
  ^MT127-C08-1
- **Harry Moore (Man Group, systematic/trend researcher)** Trend follows prices across assets, going short bonds and equities or long commodities as narratives change, with no long-term view.  #mech/slow_reaction
  > trend doesn't have a long-term view on any of these markets right it trades them all
  indicator: trend following · asset: multi · direction: short bonds and equities in inflation shock; long commodities · horizon: months · testable: yes · confidence: high
  ^MT127-C08-2
- **Harry Moore (Man Group, systematic/trend researcher)** Trend following can short equities and even the AI theme (semis and hardware) in a break, offering something different from other holdings.  #mech/slow_reaction
  > It might even go short the AI theme
  indicator: trend short positions · asset: equities · direction: short equities/semis · horizon: months · conditions: in a left-tail break · testable: yes · confidence: medium
  ^MT127-C08-3
- **Harry Moore (Man Group, systematic/trend researcher)** In a left-tail shock, trend following is zero or negatively correlated to equities while other asset class correlations rise, making it a covariance-matrix diversifier.  #mech/risk_management
  > typically it's it's trend following that is that is zero or or kind of negatively correlated and other asset classes uh of correlations typically typically pick up
  indicator: trend vs equity correlation in stress · asset: multi · direction: long trend in portfolio for tail protection · horizon: months · conditions: in the left tail · testable: yes: conditional correlation tests · confidence: high
  ^MT127-C08-4

### C09
- **Harry Moore (Man Group, systematic/trend researcher)** AI summarises existing knowledge but cannot easily produce new alpha ideas, so it frees researchers to be creative rather than write Python.  #mech/research_method
  > very very difficult to come up with brand new kind of quantitative high alpha ideas
  asset: other · testable: partly: productivity claim · confidence: medium
  ^MT127-C09-1
- **Harry Moore (Man Group, systematic/trend researcher)** AI shifts quant research time from implementation (Python, backtest setup) toward ideas, from about 50/50 to 90/10, squeezing junior implementation roles.  #mech/research_method
  > if you could split that 50/50 and make it more like 9010 so that your top researchers have plenty more time to think and be creative
  asset: other · testable: partly: productivity measurable · confidence: medium
  ^MT127-C09-2
- **Harry Moore (Man Group, systematic/trend researcher)** Test researchers by having them critique an AI-generated piece, since AI use is unavoidable; the risk is skill atrophy from one-click answers.  #mech/research_method
  > give someone an AI generated piece, get them to get them to go and critically analyze it
  asset: other · testable: no: hiring practice · confidence: medium
  ^MT127-C09-3

### C10
- **Harry Moore (Man Group, systematic/trend researcher)** Trend on futures needs only about $20-25 of capital per $100 exposure, so allocators can add trend without selling existing holdings.  #mech/structural_shift
  > if I only need to use $20 or $25 to get my $100 of trend following gives me a few new levers
  indicator: futures margin/cash efficiency · asset: multi · testable: yes: margin-to-notional · confidence: high
  ^MT127-C10-1
- **Harry Moore (Man Group, systematic/trend researcher)** Freed cash can fund extra alphas such as cross-sectional trend or carry, which have lower correlation, positive Sharpe and add value.  #mech/risk_premium
  > It had lower correlation. It still had positive sharp. It was still additive
  indicator: cross-sectional trend, carry · asset: multi · testable: yes: add-on alpha backtests · confidence: medium
  ^MT127-C10-2
- **Niels Kaastrup-Larsen** Quant firms have told due-diligence questioners that researchers write their own code and review each other's code; AI code generation will change that answer and shift the control to review of AI-written code.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > they need to review each other's code and all of that stuff
  asset: multi · conditions: Applies to quant due diligence on process controls. · testable: no - an operational control, not a testable signal · confidence: medium
  ^MT127-C10-X1

### C11
- **Harry Moore (Man Group, systematic/trend researcher)** Cash-efficient trend allows an allocation even when private assets are not returning capital quickly.  #mech/liquidity_flows
  > Imagine again, you're not getting your cash flows back as as fast as you want from from your private allocations.
  indicator: private asset distributions · asset: multi · horizon: years · testable: no: situational · confidence: medium
  ^MT127-C11-1
- **Niels Kaastrup-Larsen (host; caption "Neils")** Combining trend and equities in portable alpha yields roughly the sum of both return streams rather than the average.  #mech/risk_premium
  > actually you get almost the sum of the two return stream
  indicator: S&P 500 plus SG Trend stack · asset: multi · horizon: years · testable: yes: stacked return series · confidence: high
  ^MT127-C11-2
- **Harry Moore (Man Group, systematic/trend researcher)** Second-order portable-alpha design questions (rebalancing rule, cash buffer) are under-researched, motivating the paper.  #mech/research_method
  > how should I rebalance portable alpha or how much cash should I hold in a portable alpha structure like you don't find great answers
  asset: multi · testable: partly · confidence: high
  ^MT127-C11-3
- **Harry Moore** The portable alpha structure examined sells no equity exposure: part of a passive S&P holding is held synthetically through a future or swap, and the freed cash is used to buy trend (or another alpha) on top, so the investor keeps the beta and adds the alpha.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > I'm going to take a portion of my equities. Let's say I own some passive S&P and I'm going to hold that via a future or a swap.
  indicator: S&P 500 future or swap plus trend sleeve · asset: equities · direction: long equity beta plus alpha overlay · conditions: Needs cash for margin and buffers (see the cash-buffer findings). · testable: yes - the structure can be backtested with S&P and SG Trend returns · confidence: high
  ^MT127-C11-X1

### C12
- **Harry Moore (Man Group, systematic/trend researcher)** Portable alpha structures failed in 2008 due to insufficient liquidity and alpha-beta correlation; resilient designs must survive the GFC, the dotcom bust and COVID.  #mech/risk_management
  > in 2008 many of these structures failed right and the lines down which those structures failed those risks still exist
  indicator: alpha-beta correlation, liquidity · asset: multi · horizon: years · conditions: in stress events · testable: yes: stress-period simulation · confidence: high
  ^MT127-C12-1
- **Harry Moore** The paper's results use SG Trend as the alpha, but the same analysis was run internally on other alphas (such as multi-strategy), with the claim that the cash-buffer and rebalancing conclusions do not depend on trend alone.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > we've used trend in the analysis, but we yeah internally we've done this analysis across many different um alpha alpha structures
  indicator: SG Trend as alpha in S&P plus alpha stack · asset: multi · conditions: Robustness claim by the authors; results for other alphas not shown in the podcast. · testable: partly - could be checked against the paper · confidence: medium
  ^MT127-C12-X1

### C13
- **Harry Moore (Man Group, systematic/trend researcher)** A futures- or swap-based beta needs unencumbered cash beyond margin, because a 10% fall exhausts 10% margin and counterparties call for more.  #mech/risk_management
  > if you've only supported your S&P with $10 of capital and the S&P falls by 10%. All of your margin is gone, right?
  indicator: margin and cash buffer · asset: equities · horizon: days · conditions: in sharp equity declines · testable: yes: margin simulation · confidence: high
  ^MT127-C13-1
- **Harry Moore (Man Group, systematic/trend researcher)** A 20% unencumbered cash buffer on S&P plus trend would have been fully drawn down in the GFC, dotcom and COVID, forcing beta sales.  #mech/risk_management
  > you get fully drawn down um in the GFC in the dotcom and in co
  indicator: S&P 500 plus SG Trend backtest 26-27 years · asset: equities · horizon: years · conditions: in major crashes · testable: yes: backtest · confidence: high
  ^MT127-C13-2
- **Harry Moore (Man Group, systematic/trend researcher)** Forced beta selling at the lows loses the rebound (about 30% in 2009) and produces large tracking error against the benchmark.  #mech/risk_management
  > if you were were selling in the early part of 2009 at a at a low in your equity component and you're knocked out that position, you miss kind of 29 30% of of upside.
  indicator: tracking error vs S&P · asset: equities · horizon: months · conditions: after forced deleveraging near lows · testable: yes · confidence: high
  ^MT127-C13-3
- **Harry Moore (Man Group, systematic/trend researcher)** About 40% cash (10% margin plus 30% unencumbered) means a forced degearing only once in 100-200 years, per Monte Carlo and real data.  #mech/risk_management
  > about once in every 1 to 200 years
  indicator: cash buffer 40% · asset: equities · horizon: years · testable: yes: Monte Carlo simulation · confidence: medium
  ^MT127-C13-4
- **Harry Moore (Man Group, systematic/trend researcher)** Only one historical path exists, so Monte Carlo is used to simulate severe drawdowns beyond the history.  #mech/research_method
  > you've only had one one path of of the truth that actually happened
  asset: multi · testable: yes · confidence: high
  ^MT127-C13-5

### C14
- **Harry Moore (Man Group, systematic/trend researcher)** Most investors want the manager to bear operational and cash-flow complexity, so a larger buffer is preferred over callable capital.  #mech/risk_management
  > They do not want to be getting margin calls um on a Monday.
  asset: multi · testable: no: client preference · confidence: medium
  ^MT127-C14-1
- **Harry Moore (Man Group, systematic/trend researcher)** Liquid alphas such as trend allow quick recapitalisation, making them good candidates for portable alpha.  #mech/liquidity_flows
  > If you if you have something that's like weekly dealing or monthly dealing, you can recapitalize quickly.
  asset: multi · testable: partly · confidence: medium
  ^MT127-C14-2
- **Harry Moore (Man Group, systematic/trend researcher)** Rebalancing the beta component periodically causes tracking error versus the index; to track closely, buy and hold or use tolerance bands.  #mech/research_method
  > as soon as you select a monthly rebalance, you no longer replicate the S&P.
  indicator: rebalance frequency · asset: equities · horizon: years · testable: yes: simulate rebalancing rules · confidence: high
  ^MT127-C14-3
- **Harry Moore (Man Group, systematic/trend researcher)** Recommended compromise: rebalance only when the S&P and trend sleeves drift more than about 10% out of balance.  #mech/risk_management
  > if my S&P and SG trend goes more than 10% out of whack, I will rebalance.
  indicator: tolerance band · asset: multi · testable: yes · confidence: medium
  ^MT127-C14-4
- **Harry Moore (Man Group, systematic/trend researcher)** In 2008 rebalancing back to target lost money because equities kept falling while trend rose; only buy and hold did better.  #mech/behavioral
  > Every time you rebalance you reby you increase your equity allocation into a continually falling equity market.
  indicator: rebalancing in 2008 · asset: equities · horizon: months · conditions: in persistent crashes · testable: yes · confidence: high
  ^MT127-C14-5
- **Harry Moore** Some investors can accept a smaller cash buffer because they hold callable capital or a credit facility and can post margin at short notice, but most clients want the manager to carry the operational complexity.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > They might have callable capital available. They might have a credit facility.
  indicator: cash buffer alternatives · asset: multi · direction: smaller buffer with callable capital · conditions: Only for investors with operational capacity to meet margin calls. · testable: no - an operational choice · confidence: high
  ^MT127-C14-X1
- **Harry Moore** Pure buy and hold replicates the index best but causes the equity and alpha mix to drift, and makes it hard to bring new investors in at NAV with the intended mix, so the authors prefer a tolerance-band rebalance.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > you're going to slowly get this drift. you might own too much equities or too little. If other investors come in, well, how do you get them to the nav
  indicator: drift of alpha and beta weights · asset: multi · conditions: Applies to pooled portable alpha vehicles with inflows. · testable: partly - drift can be simulated · confidence: medium
  ^MT127-C14-X2

### C15
- **Harry Moore (Man Group, systematic/trend researcher)** Over the long run rebalancing frequency (monthly, quarterly, annual, 5-10% bands) makes little performance difference, but it matters in episodes such as 2008 and COVID.  #mech/research_method
  > over the long run, we found that in performance terms it kind of doesn't matter.
  indicator: rebalancing rule · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT127-C15-1
- **Harry Moore (Man Group, systematic/trend researcher)** Swap financing cost (about 40bp) is implicit in futures, so swaps vs futures give no structural performance advantage; the choice is operational, with futures lacking counterparty risk.  #mech/risk_premium
  > if you run this over time, it washes out, right? The you don't get a a a structural performance advantage
  indicator: futures vs swap cost · asset: multi · horizon: years · testable: yes: cost comparison · confidence: high
  ^MT127-C15-2
- **Niels Kaastrup-Larsen (host; caption "Neils")** Other popular stacked combinations may look great in backtests but hide risks not exposed in recent decades, partly through correlations.  #mech/research_method
  > we have seen uh some other combinations that may look great in a back test
  asset: multi · testable: partly · confidence: medium
  ^MT127-C15-3
- **Harry Moore** Because long-run results are the same across rebalancing rules, choose the rule by looking at the worst historical paths and picking the one that avoids outcomes the investor could not accept, rather than by average performance.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > have a look at the paths. Are there any paths that you really wouldn't like in there um and therefore that might push you towards a um a a certain rebalancing rule.
  indicator: rebalancing rule path analysis · asset: multi · conditions: When performance is similar on average, path dependence decides the choice. · testable: yes - path-wise comparison across rules is testable · confidence: medium
  ^MT127-C15-X1
- **Harry Moore** Investors in portable alpha should ask providers up front what happens in a stress month (for example a 20% drawdown): how margin is met, whether beta is sold, and what the tracking error would be.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > You should understand kind of what will happen if you you draw down 20% in a month.
  indicator: stress scenario of 20% monthly drawdown · asset: multi · horizon: months · conditions: Pre-trade operational due diligence. · testable: partly - the scenario can be simulated by the provider · confidence: high
  ^MT127-C15-X2

### C16
- **Harry Moore (Man Group, systematic/trend researcher)** The Turtle rules were hand-calculable approximations of later decision and probability theory.  #mech/research_method
  > rules of thumb hand calculable pen and paper easy to do in a in a few minutes uh approximations of later decision theory mathematics
  indicator: Turtle trading rules · asset: multi · testable: yes · confidence: high
  ^MT127-C16-1
- **Harry Moore (Man Group, systematic/trend researcher)** The Turtles estimated volatility N with a range-based exponential estimator (half-life about 14 days), consistent with Parkinson's efficient range estimator.  #mech/risk_management
  > they use a rangebased estimate estimator very simple to update each day
  indicator: range-based volatility, Parkinson · asset: multi · horizon: days · testable: yes · confidence: high
  ^MT127-C16-2
- **Harry Moore (Man Group, systematic/trend researcher)** Turtle units equalise risk across markets (one unit of crude equals one unit of Treasuries in risk), i.e. volatility-based position sizing.  #mech/risk_management
  > really what this is is this is volatility based um position sizing, right?
  indicator: N-based unit · asset: multi · testable: yes · confidence: high
  ^MT127-C16-3

### C17
- **Harry Moore (Man Group, systematic/trend researcher)** The Turtles' 2% equity per 2N stop corresponds to a fractional-Kelly size on the left of the optimum, giving up some growth for much lower ruin risk.  #mech/risk_management
  > Now any prudent manager will be on the left side of that hill, right? You are taking a little bit of less of the the upside for a much lower probability of of ruin.
  indicator: Kelly fraction, 2N stop · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT127-C17-1
- **Harry Moore (Man Group, systematic/trend researcher)** A stop at 2N equals a loss of 2% of equity per position.  #mech/risk_management
  > this equate this 2n equates to 2% of your total equity in your book
  indicator: 2N stop · asset: multi · testable: yes · confidence: high
  ^MT127-C17-2
- **Harry Moore (Man Group, systematic/trend researcher)** Turtles managed correlation with position-size caps on correlated markets instead of covariance inversion.  #mech/risk_management
  > the way they dealt with correlations was not in the actual construction but it was on position size caps.
  indicator: correlation caps · asset: multi · testable: yes · confidence: high
  ^MT127-C17-3

### C18
- **Harry Moore (Man Group, systematic/trend researcher)** Because managers run others' money, drawdown-control rules are needed; the Turtles cut equity 20% after a 10% loss, later formalised by Grossman and Zhou.  #mech/risk_management
  > like you cannot stomach an 80% draw down
  indicator: drawdown control rule · asset: multi · testable: yes: simulate drawdown rules · confidence: high
  ^MT127-C18-1
- **Harry Moore (Man Group, systematic/trend researcher)** Turtle drawdown rule: after losing 10% reduce book equity used for sizing by 20%.  #mech/risk_management
  > they lost 10% um in the market then they would cut their equity by 20%
  indicator: drawdown rule · asset: multi · testable: yes · confidence: medium
  ^MT127-C18-2
- **Niels Kaastrup-Larsen (host; caption "Neils")** The Turtles' edge was risk management and scaling rather than the breakout entry.  #mech/risk_management
  > the genius was not so much in buying a 100 day breakout
  asset: multi · testable: partly · confidence: high
  ^MT127-C18-3
- **Niels Kaastrup-Larsen (host; caption "Neils")** Trend followers control risk, not returns: small losses, intelligent scaling and surviving to catch outsized moves.  #mech/risk_management
  > we are probably risk managers first and foremost
  asset: multi · testable: partly · confidence: high
  ^MT127-C18-4
- **Niels Kaastrup-Larsen** The Turtles were not the first trend followers, but their fame came from books and narrative, which led people to mistake clear rules for simplicity and to credit the 100-day breakout rather than the risk management.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > they became the most known in a sense because of the books that was written about them and and the narrative
  asset: multi · conditions: Applies to how strategies are judged from stories rather than evidence. · testable: no - a statement about narrative bias · confidence: medium
  ^MT127-C18-X1

### C19
- **Harry Moore (Man Group, systematic/trend researcher)** A 50/50 portfolio holds roughly 85% of its risk in equities, so leverage on bonds improves risk balance and Sharpe versus a $100 capital constraint.  #mech/risk_management
  > 85% of the risk is equities, 15% is bonds, even though on paper it says 50/50
  indicator: risk contribution · asset: multi · testable: yes · confidence: high
  ^MT127-C19-1
- **Harry Moore (Man Group, systematic/trend researcher)** Leverage is a portfolio-construction tool that can raise Sharpe when assets are risk-balanced.  #mech/risk_management
  > you get a higher sharp um than you would by by by having the $100 constraint
  indicator: leverage · asset: multi · testable: yes · confidence: high
  ^MT127-C19-2
- **Harry Moore (Man Group, systematic/trend researcher)** Choose a portable alpha that is uncorrelated in the left tail; liquidity-provision strategies (short vol, merger arbitrage, basis trade) look good normally but have big left tails.  #mech/risk_management
  > What you also need to really investigate is not just that it's uncorrelated, but that it's uncorrelated in the left tail.
  indicator: alpha left-tail correlation · asset: multi · conditions: avoid liquidity-provision alphas · testable: yes · confidence: high
  ^MT127-C19-3
- **Harry Moore** The alpha layer in portable alpha should not add beta, because extra beta in the same direction as the 100% equity holding raises volatility and the left-tail loss; the alpha must be uncorrelated, especially in the tail.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > You almost certainly don't want to be introducing more beta, right? That's a risk in the same direction.
  indicator: alpha sleeve beta to equities · asset: multi · direction: pick low-beta, tail-uncorrelated alpha · conditions: Applies when the beta sleeve is already 100% long equities. · testable: yes - beta and tail correlation of the alpha sleeve are measurable · confidence: high
  ^MT127-C19-X1
- **Harry Moore** With leverage allowed, an investor can hold risk-balanced bonds (about 70%) and still keep 50-70% in equities, getting a higher Sharpe than under the $100 capital constraint, which is why leverage is a portfolio-construction tool.  #mech/new _(added by map cross-check)_
  > if you allow leverage in that portfolio, maybe you hold your 70 bonds, you're still able to hold 50 60 70% of of equities.
  indicator: risk share of equities in 50/50 portfolio (about 85%) · asset: multi · conditions: leverage permitted, assets risk-balanced · testable: yes - Sharpe of risk-balanced portfolio · confidence: high
  ^MT127-C19-R1

### C20
- **Harry Moore (Man Group, systematic/trend researcher)** Test alpha vs the worst 5% of beta returns; trend historically has low to negative correlation to equities in the worst periods.  #mech/research_method
  > like the worst 5% of beta returns, like the worst equity periods, and check that you still have no correlation
  indicator: trend vs equity correlation in worst 5% · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT127-C20-1
- **Harry Moore (Man Group, systematic/trend researcher)** Trend scales positions inversely with volatility, so it needs less margin in turning-point stress, unlike liquidity-provision strategies.  #mech/risk_management
  > Trend is actually reducing positions. It needs less margin to ride.
  indicator: volatility-scaled positions · asset: multi · horizon: days · testable: yes · confidence: high
  ^MT127-C20-2

