---
source_id: MT196
title: "Trend Following in Crisis- - Systematic Investor 346"
date: 2025-05-08
channel: "Top Traders Unplugged"
url: 
words: 13575
claims: 68
added_by_crosscheck: 13
corrections: 2
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Rob Carver (systematic trader, author)", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Trend Following in Crisis- - Systematic Investor 346

**Speakers:** Rob Carver (systematic trader, author); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** Rob Carver and Niels review April 2025 for trend followers after Liberation Day and Rob's own 2024-25 drawdown year. Discussion of stops vs continuous sizing, drawdown maths, costs, a single-EMA trend paper, industry history and leveraged ETFs. Conclusion: bad years are normal for trend, process discipline matters, leveraged ETFs are toxic.

**Approach:** trend following, CTA, risk management, position sizing

**Cross-check completeness estimate of first read:** 0.85 - the first reader caught the main mechanisms, numbers and Rob's method points; missed a few secondary ideas (sector headwinds, speed vs capture split, GDP distortion, symmetric review, diversification response) and slightly misattributed two items.

## Argument map

**Episode thesis:** Rob Carver argues that bad years are a normal, mathematically expected part of trend following, that how a system sizes and exits positions (continuous volatility-scaled sizing versus stops) matters as much as signal speed in a V-shaped shock like April 2025, and that the right response to a drawdown is process discipline (check costs, compare to expected drawdown, keep diversification) rather than redesign. He also holds a bearish discretionary view on the US economy after tariffs and argues leveraged ETFs are toxic. Niels frames April 2025 as a stress test in which Treasuries and the dollar failed as safe havens, trend followers were wrong-footed in equities and FX but helped by commodities, and risk-management systems mostly worked as designed.

### Rob Carver (Co-host; independent systematic futures trader, author on systematic trading; ex-AHL, trades his own money)
Fingerprint: #approach/trend_following #approach/position_sizing_vol_target #approach/kelly_or_conviction_sizing #approach/costs_execution #approach/research_robustness_overfitting #approach/diversification_risk_parity #approach/portfolio_construction_stacking #approach/regime_detection
_Speaker note: Transcript spells him 'Rob Carver'. Corrections applied from the ledger: MT196-C09-2 is the 2024-25 tax year (about -15%, roughly a one-in-10-year event), with his previous worst year being April 2014 to April 2015; MT196-C18-3 is Niels describing the leveraged Nasdaq tweet, with Rob only saying it is not remotely a good idea. The 'Sebastian Valerie' paper is 'Breaking the Trend: How to Avoid Cherrypicked Signals'._

**Worldview premises**
- Bad years happen to well-diversified trend portfolios because everything goes wrong at once in a trendless year, not because of concentration in one market; a 2024-25 loss of about -15% was roughly a one-in-10-year event for him. _[experience, stated; support: His own P&L by asset class for the year: losses in equities, energies, FX, metals and bonds, with gains only in the S&P; natural gas worst. Worst previous year April 2014 to April 2015.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C09-2|C09-2]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C10-1|C10-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C10-2|C10-2]])
- The longer a strategy runs, the larger its expected worst drawdown, so veteran funds hitting new worst drawdowns is mathematically unsurprising. _[theoretical, stated; support: Drawdowns grow over time in expectation (he is unsure if the growth follows the square root of time).]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C11-2|C11-2]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C12-1|C12-1]])
- Because trend signals have a modest Sharpe ratio, it takes a very long time to tell statistically that a system has stopped working, so continuing is a matter of faith; systematic traders should in theory do nothing when the strategy underperforms, though in practice that is hard. _[theoretical, stated; support: Reasoning from Sharpe-ratio statistics; no calculation shown.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C12-2|C12-2]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C12-3|C12-3]])
- Variable position sizing (daily risk adjustment) makes the return distribution closer to normal with fewer outliers, while stop-based systems create larger outliers both ways; stops can close at the wrong moment, and outsized positions in a market that has run up (cocoa) are a source of downside outliers. _[theoretical, stated; support: Described by himself as a handwaving academic argument.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C06-4|C06-4]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C07-1|C07-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C06-3|C06-3]])
- Capturing a V-shaped reversal such as April 2025 needs extremely fast trading; slightly too slow trading is whipsawed, a very wide stop simply holds, and a tight stop is triggered near the low. _[theoretical, stated; support: Walk-through of the S&P path around April 8-9, 2025.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C06-1|C06-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C06-2|C06-2]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C06-X1|C06-X1]])
- Few quantitative variables predict when trend following will do well or badly, so meta-timing is not productive; the best answer to a client's worry is visibility into historical analogues. _[experience, stated; support: His own attempts at quantitative conditioning.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C13-1|C13-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C12-4|C12-4]])
- Costs are predictable while P&L is nearly random, so an annual cost check (commissions plus slippage versus mid) is the most reliable review; his costs were about 100 bp, in line with the backtest, and passive limit orders beat the conservative half-spread assumption. _[experience, stated; support: His own annual review.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C13-2|C13-2]])
- Different trend indicators are highly correlated, so no single one is uniquely best, but once automated, extra signals cost nothing; a single calibrated EMA (112 days) can represent the trend universe. _[empirical, stated; support: Comparison of his own five or six indicators across speeds; the Breaking the Trend paper's mathematical link between exponential and simple moving averages.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C15-3|C15-3]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C15-4|C15-4]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C16-1|C16-1]])
- Relative (cross-sectional) signals and style diversification held up in the 2024-25 trendless regime: of about 50 forecasting variables, only fast relative momentum, relative carry and relative value skew made money. _[empirical, stated; support: His own attribution by indicator; even carry (especially slowest) lost.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C11-1|C11-1]])
- US Treasuries may no longer be the default safe haven: US policy seems designed to create stagflation so the normal central bank reaction (cutting rates) may not apply, and traditional buyers (China) may avoid Treasuries in a crisis born in the US; breakdown of institutional rules is bad for US assets. _[theoretical, stated; support: Two competing explanations he calls policy-reaction and flows; the FT 'Giffen good' article framing.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C01-1|C01-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C02-1|C02-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C02-4|C02-4]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C03-1|C03-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C03-2|C03-2]])
- Tariffs lag in the data: Q1 GDP was not affected by them, CEOs avoid honest forward earnings guidance, and the real-economy effect and earnings downgrades come later, producing a deep technical recession. _[theoretical, stated; support: FT articles (Martin Wolf's Road Runner analogy), Bezos tariff example, noted distortion of Q1 GDP by gold flows and import front-running.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C14-1|C14-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C14-X1|C14-X1]])
- Funds that can make 100% in good years can lose 30-60% in bad years; whether that is Kelly-optimal matters less than whether investors can stomach it, and fixed 2-4x leverage on already risky assets is far beyond Kelly sizing. _[theoretical, stated; support: Brief reasoning on Kelly; leveraged ETF example.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C07-3|C07-3]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C19-2|C19-2]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C19-X1|C19-X1]])
- Leveraged ETFs reset daily so compounding makes adverse, choppy moves devastating (a 4x S&P ETF down 52% year to date versus S&P about -4.5%) and carry high expense ratios (about 295 bp). _[empirical, stated; support: His own data download for his new book; quoted year-to-date figures.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C19-1|C19-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C19-2|C19-2]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C18-3|C18-3]])
- Practical market-structure knowledge (contract quotation, settlement, data cleaning) is essential in systematic futures work. _[experience, stated; support: Career experience; advice to a young quant.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C08-X1|C08-X1]])
- In extreme stress liquidity can vanish: in the first days after Liberation Day some positions had no bid and could not be sold. _[experience, stated; support: His own attempt to sell positions.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C15-2|C15-2]])
- Trend followers form a family tree with distinct lineages (US pit-trading wing, British quantitative wing, Scandinavian), which explains differences of opinion about sizing and position changes. _[experience, stated; support: Substack article on industry history; his AHL background.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C16-3|C16-3]])

**Chain: Why April 2025 hurt different trend followers differently**
1. Liberation Day shock drives a sharp equity sell-off (S&P about 20% off its high) → Trend followers cut or reverse equity and FX positions, some via stops: Trend and risk rules react to drawdown and volatility ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C06-2|C06-2]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-1|C04-1]])
2. Equity market V-reverses within days (bottom April 8-9) → Tight-stop systems are flat with a loss booked; wide-stop systems hold; continuous sizing systems are down then sideways at one third of normal risk: Position-capture method determines participation after the reversal ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C06-1|C06-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C06-2|C06-2]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C06-3|C06-3]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-6|C04-6]])
3. Fastest models catch part of the initial bounce → Later whipsaw erases it; moves too fast for even fast models (overnight gaps): Reversals were too quick ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C05-2|C05-2]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-8|C04-8]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C06-1|C06-1]])
4. Treasuries and the dollar sold off with equities → Traditional hedge legs failed; gains came from commodities (energies, grains) and short rates: Safe-haven status shifted when the crisis originated in the US ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-2|C04-2]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-7|C04-7]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-5|C04-5]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-X1|C04-X1]])
- Evidence: April 2025 index results: BTOP50 -3.49%, SG CTA -4.47%, SG Trend -4.98% (-9.41% YTD), short-term traders -0.86%, Bridge flat-fee trend -6.24%; Rob's own -5.5%; large trend followers -1% to -10%.
- Fails when: Depends on speed and the path; in a slower, trending sell-off, stops and sizing would behave differently. Rob notes he has not looked at individual market P&L.

**Chain: Why Treasuries failed as a safe haven in the tariff shock**
1. US policy seen as stagflationary (stagnation plus tariff inflation) → Central bank reaction function (cut rates when growth weakens) may not apply: Supply shock raises inflation while growth falls ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C02-4|C02-4]])
2. Crisis born in the US and breakdown of institutional rules → Traditional foreign buyers (China) avoid Treasuries: Flows-based explanation: the US is hurt most ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C03-1|C03-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C03-2|C03-2]])
3. Treasuries sell off with equities → Bonds hedge less; Swiss franc retains haven behaviour (Niels): Recency bias from a 40-year falling-rate cycle may be ending (Niels) ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C02-1|C02-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C02-2|C02-2]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C02-3|C02-3]])
- Evidence: April 2025 price action; the Giffen-good analogy of the FT article.
- Fails when: Both explanations are stated as competing; neither is tested, and bonds partly recovered later in the month (Niels).

**Chain: From tariffs to a US recession (Rob's discretionary view)**
1. Tariffs hit goods in transit and stockpiles run down → Real-economy data and earnings deteriorate with a lag: Q1 GDP unaffected by tariffs; CEOs avoid honest forward guidance ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C14-1|C14-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C14-X1|C14-X1]])
2. Two negative GDP quarters → Technical recession deep enough that the equity market cannot stay where it is: Expected earnings downgrades and demand destruction ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C14-1|C14-1]])
3. Cash earning about 4% against equity expected return of maybe 4% with large downside → Stay in cash in the long-only portfolio: Risk-reward ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C15-1|C15-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C13-3|C13-3]])
- Evidence: FT commentary (Wolf, Bezos), Q1 GDP quirks (gold, import spike).
- Fails when: Rob admits the call looks wrong so far because the market rebounded, and that he would be long equities in his systematic portfolio if equities rise.

**Chain: Why leveraged ETFs destroy value**
1. Daily reset of 2-4x leverage on volatile assets → Compounding losses in choppy markets (4x S&P ETF -52% versus S&P -4.5%): Volatility drag and path dependence ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C19-1|C19-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C19-X1|C19-X1]])
2. High expense ratio (about 295 bp) → Toxic as a holding instrument: Product designed for short-term exposure management ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C19-2|C19-2]])
- Evidence: Rob's own ETF data.
- Fails when: Short holding periods in trending markets (not discussed).

**Decision process**
- [sizing] Adjust positions daily to risk (variable position sizing), which automatically cut risk to about a third of normal as the trend became unclear (less in equities).. Why: Avoids both the stop-out and the oversized exposure outliers. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C06-3|C06-3]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C06-4|C06-4]])
- [signal] Run about 50 forecasting variables (several trend indicators at multiple speeds, carry, relative momentum, value skew) and keep adding signals because additional automated signals cost nothing.. Why: Diversification across styles; relative signals held up in 2024-25. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C11-1|C11-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C15-3|C15-3]])
- [universe] Dynamically select positions from a larger instrument universe even though year-to-year return differences are noisy.. Why: Better risk targeting. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C10-3|C10-3]])
- [portfolio] Keep about 50-60% in trend and add non-trend systems only when confident in them.. Why: More diversified than many peers; trend remains the core. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C12-X1|C12-X1]])
- [research] Annual review includes a cost check (commissions plus slippage versus mid price at order time), which should match the backtest (just under 100 bp).. Why: Costs are predictable, P&L is almost random. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C13-2|C13-2]])
- [research] Do not redesign after a bad year: the same review should be asked after an exceptional year and changes made only if evidence is clear. Compare the current drawdown with the probability of such a drawdown in a comparable period (about 30% over 12 years) and with backtest drawdowns.. Why: Single-year performance is mostly noise. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C10-X1|C10-X1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C12-1|C12-1]])
- [risk] Treat a 50% drawdown (far beyond the backtest and expectation) as a real concern; otherwise follow the process.. Why: Statistical bound from backtest and simulation. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C12-1|C12-1]])
- [execution] Use passive limit orders first and switch to market orders if necessary; conservative backtest assumes paying half the spread.. Why: Lower realised slippage than the backtest assumption. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C13-2|C13-2]])
- [portfolio] Raised the allocation to trend at the end of the previous tax year after trend's best quarter in 25 years, which meant the later losses hit a larger capital base.. Why: Not a deliberate timing call; the outcome illustrates the give-back risk of adding capital after a strong run. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C09-X1|C09-X1]])
- [portfolio] In the discretionary long-only portfolio he sold all remaining US stocks around Liberation Day and went to cash, calling it his biggest discretionary decision ever.. Why: Bearish US economy view; cash at 4%. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C13-3|C13-3]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C15-1|C15-1]])

**Evidence style:** Mostly own track record and own data (P&L by market and indicator, cost analysis), plus simple mathematics of drawdowns and Sharpe ratios; first-principles reasoning on position-sizing; sceptical of meta-timing. Discretionary macro views rely on FT commentary and reasoning about lags; he is open about his call looking wrong so far.

**Views at the time**
- (2025-05-02) Bearish on the US economy: expects a deep technical recession and equity weakness; prefers cash (about 4%) in his long-only portfolio over equities.. Reasoning: Tariffs lag; earnings downgrades to come; Q1 GDP distorted by gold and import front-running; institutional breakdown is bad for US assets. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C14-1|C14-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C14-X1|C14-X1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C15-1|C15-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C03-2|C03-2]])
- (2025-05-02) US Treasuries may not be the go-to safe asset in this crisis; the normal central bank reaction function may not apply if policy produces stagflation.. Reasoning: Stagflation policy mix and flows away from US assets. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C02-1|C02-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C02-4|C02-4]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C03-1|C03-1]])
- (2025-05-02) His own April 2025 return was -5.5%, roughly in line with the industry, and the 2024-25 tax year about -15%, a one-in-10-year event; the strategy is not broken.. Reasoning: Industry comparison: SG CTA about -10% versus his about -14.7% at higher volatility; probability of such a drawdown in 12 years about 30%. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C05-2|C05-2]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C09-2|C09-2]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C10-2|C10-2]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C12-1|C12-1]])
- (2025-05-02) Leveraged ETFs are toxic and the proliferation of 3-4x products is alarming.. Reasoning: Daily reset compounding, cost, Kelly-exceeding leverage. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C19-1|C19-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C19-2|C19-2]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C19-X1|C19-X1]])
- (2025-05-02) Pure trend is open to question after a long weak stretch (most firms diversified into other strategies), but he accepts that trend-is-dead worries have recurred and the industry survived.. Reasoning: Winton and Aspect history from the Substack article read aloud. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C17-X1|C17-X1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C18-1|C18-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C11-1|C11-1]])

### Niels Kaastrup-Larsen (Host, Top Traders Unplugged; trend-following allocator and industry observer)
Fingerprint: #approach/trend_following #approach/manager_selection_allocation #approach/crisis_alpha_convexity #approach/behavioral_sentiment #approach/positioning_crowding #approach/diversification_risk_parity
_Speaker note: Transcript spells him 'Neils Castro Larson'. He reports index numbers as of April 30/May 1, 2025, early manager indications, and describes the leveraged Nasdaq tweet (ledger correction for MT196-C18-3). 'Bill Dunn' comment is his: he says he worked for Bill Dunn._

**Worldview premises**
- Safe-haven assets are changing: bonds' safe-haven status may be recency bias from a 40-year falling-rate cycle; the Swiss franc still seems to retain safe-haven behaviour. _[behavioural, stated; support: Observation of April 2025; admits he may be talking his book (Swiss resident) but denies it.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C02-2|C02-2]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C02-3|C02-3]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-2|C04-2]])
- In stress months commodities again delivered trend-following gains, while equities and currencies were headwinds in April 2025. _[empirical, stated; support: Early manager indications; no precise attribution.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-7|C04-7]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-X1|C04-X1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-5|C04-5]])
- Dispersion between trend followers is usual and comes from speed, risk management and markets traded; hard-stop versus continuous-signal systems may differ materially in a V-shaped reversal. _[empirical, stated; support: CFM research on dispersion; reasoning.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-4|C04-4]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-6|C04-6]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C05-3|C05-3]])
- Funds with large open profits (high flyers) risk big give-backs, so investors entering after a hot streak face outsized drawdown risk. _[behavioural, stated; support: A fund he noted being hit hard in April 2025.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C07-2|C07-2]])
- Risk management systems worked as designed in April 2025, so a down month for managers who followed process is normal and not evidence of strategy failure; investors should not redeem on a bad month (November 2021 example). _[experience, stated; support: Early data; November 2021 was a bad day followed by one of the best 12 months for many managers.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C07-X1|C07-X1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C12-4|C12-4]])
- Portable alpha products (trend overlay on equity beta) looked bad in April 2025 with negative alpha and flat beta even though they did what they are designed to do. _[empirical, stated; support: Imagined from index moves, not from reported results.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C05-1|C05-1]])
- Trend following had its best quarter in about 25 years in Q1 2024, then became much more challenging from April 2024. _[empirical, stated; support: Index history.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C09-1|C09-1]])
- The industry has survived the recurrent 'is trend following dead' question; Winton diversified away from trend, did poorly when CTAs did well, and has since rebuilt its trend allocation, while Aspect stuck to trend. _[experience, stated; support: Substack article read aloud; his industry knowledge.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C17-1|C17-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C18-2|C18-2]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C17-R1|C17-R1]])
- There is a fine balance between simplicity and over-complication in trend systems and it makes a big difference. _[experience, stated; support: Past podcast discussions.]_ ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C16-2|C16-2]])

**Chain: Stop-out versus continuous participation in a V reversal**
1. A stop-based follower is stopped out in the sell-off → Cannot re-enter until a new signal, missing the bounce: Rule requires a fresh signal ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C05-3|C05-3]])
2. Continuous-signal system keeps participating → Different April P&L from stop systems: Position adjusts with the signal rather than switching off ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-6|C04-6]])
- Evidence: Observed performance differences among managers he can see online.
- Fails when: Rob adds that the real difference is the speed and capture method combined; a V reversal is extreme.

**Decision process**
- [research] Track a trend barometer (52 at end of April 2025, a short-term measure) plus BTOP50, SG CTA, SG Trend, SG Short-Term Traders and Bridge flat-fee trend indices against MSCI World, S&P 500 and bonds.. Why: Weekly health check of the category. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C03-3|C03-3]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C07-4|C07-4]])
- [portfolio] When evaluating managers, look at speed, risk management and markets traded as sources of dispersion, and consider open-profit levels of funds.. Why: Dispersion is usual; give-back risk for new entrants. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-4|C04-4]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C07-2|C07-2]])

**Evidence style:** Index tables, early manager reports, news and anecdote; relies on guests for mechanics. Acknowledges the limit of early data.

**Views at the time**
- (2025-05-02) April 2025 was a stress test: CTAs lost on the V-reversal in equities and FX, Treasuries and the dollar failed as hedges, commodities and short-term rates helped; the largest trend followers lost 1-10% in April and were between slightly up and -15-18% YTD.. Reasoning: Early manager reports and index results. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-1|C04-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-2|C04-2]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-3|C04-3]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-7|C04-7]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-X1|C04-X1]])
- (2025-05-02) Short-term models did better in the first half of April, but later reversals erased most of it; the fast models were still too slow for some moves.. Reasoning: Observed performance by speed. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-8|C04-8]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C07-4|C07-4]])
- (2025-05-02) Risk management systems held up and a down month is within normal range; no sign that trend following is broken.. Reasoning: Early indications only. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C07-X1|C07-X1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C17-1|C17-1]])
- (2025-05-02) Bonds may stop providing cover if rates trend higher after a 40-year falling-rate cycle.. Reasoning: Recency bias argument. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C02-3|C02-3]])

### Disagreements
- **Stops versus continuous signals as the explanation for April dispersion**: Niels Kaastrup-Larsen: April may differ materially between hard-stop systems and continuous-signal systems because a stopped-out system cannot re-enter before a new signal. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C04-6|C04-6]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C05-3|C05-3]]); Rob Carver: Two separate drivers: signal speed and position-capture method; capturing the bounce needed extremely fast trading, wide stops simply held, and continuous sizing was down then flat. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C06-X1|C06-X1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C06-1|C06-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C06-2|C06-2]])
- **Explanation of the Treasury selloff**: Niels Kaastrup-Larsen: Bond safe-haven status may be recency bias from a 40-year falling-rate cycle. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C02-3|C02-3]]); Rob Carver: Two competing explanations: stagflationary policy that breaks the central bank reaction function, and flows (traditional buyers such as China avoid Treasuries in a crisis born in the US). ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C02-4|C02-4]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C03-1|C03-1]])
- **Should a veteran trend system react to a long drawdown**: Rob Carver: Do nothing in theory; only a drawdown well beyond backtest (for example 50%) is a real concern; avoid redesign and keep trend as 50-60% of the book while adding confident non-trend systems. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C12-3|C12-3]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C12-1|C12-1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C10-X1|C10-X1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C12-X1|C12-X1]]); Niels Kaastrup-Larsen: Surprised that managers with 30 years of experience hit their worst-ever drawdown, and notes investors will want to redeem; asks how to keep them from projecting. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C12-4|C12-4]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C11-2|C11-2]])

### Gaps and conflicts
- Ledger correction: Rob's -15% is the April 2024 to April 2025 tax year, not his worst-ever year (April 2014 to April 2015); the later figure is -14.7%. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C09-2|C09-2]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C10-2|C10-2]])
- Ledger correction: Niels, not Rob, describes the leveraged Nasdaq tweet (7% a year becomes 21% with 3x); Rob's daily-reset explanation comes later. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C18-3|C18-3]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C19-1|C19-1]])
- Index figures are early and partial (as of April 30/May 1), the ledger line for April omits the SG CTA YTD (-6.88%) and BTOP50 YTD (-3.54%) given in the transcript, and the trend barometer of 52 is a short-term measure Niels does not define. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C07-4|C07-4]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C03-3|C03-3]])
- Rob has not looked at individual market P&L for April; his claim about the fastest models is an expectation of whipsaw afterwards, not a measured result. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C05-2|C05-2]])
- The statement that worst drawdown grows with time is mathematical in expectation but Rob is unsure about the growth rate; the 30% probability over 12 years is quoted without the model. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C11-2|C11-2]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C12-1|C12-1]])
- Rob's bearish call (cash over equities) conflicted with the market rebound he admits; his systematic portfolio remains long if equities rise. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C14-R1|C14-R1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C15-1|C15-1]])
- Niels says portable alpha did badly from imagination rather than reported results. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C05-1|C05-1]])
- Rob says even the slowest carry signal lost money in 2024-25, contradicting the usual diversifier role of carry; he does not explain why. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C11-1|C11-1]])
- Rob's costs claim (about 100 bp, in line with backtest) is one number without breakdown; passive-order slippage advantage is asserted. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C13-2|C13-2]])
- Rob raised trend allocation at the end of the tax year before the drawdown, which conflicts with his own advice against adding after strong runs. ([[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C09-X1|C09-X1]], [[MT196 - Trend Following in Crisis- - Systematic Investor 346#^MT196-C07-2|C07-2]])

### Forward-looking inputs (reader synthesis)
(reader) Inputs these speakers treat as leading: tariff pass-through (goods in transit, stockpiles) to Q2-Q3 US GDP and earnings guidance; direction of Treasury yields and whether Treasuries rally on bad news (central bank reaction function); dollar and Swiss franc behaviour in stress; trend barometer; speed and position-capture method of trend models in V-shaped markets; commodity trends (energies, grains). Horizon: months for the tariff-recession call; the trend drawdown question is statistical and multi-year.

### Reader inferences (not stated by the speakers)
- (reader) Rob's account implies that variable position sizing behaves like an automatic reduction of exposure when signals become unclear, which gives a flat P&L after a shock instead of a clear stop-out; it protects against whipsaw but forfeits recoveries.
- (reader) The 2024-25 pattern (only relative signals making money, every outright trend and even carry lost) suggests the loss was a trendless regime for outright trend rather than a failure of any one market, consistent with his diversified-portfolio argument.
- (reader) Niels's and Rob's views on safe-haven change point to the same observable: whether Treasuries rally on bad US news. Neither provides a test beyond April 2025.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | intro, sponsor, Treasuries as Giffen good safe haven |
| C02 | 4 | Treasuries not safe haven, CHF, recency bias, stagflation reaction function |
| C03 | 3 | flows explanation, institutions, trend barometer |
| C04 | 8 | April 2025 CTA performance, dispersion, markets, speed, stops, portable alpha start |
| C05 | 3 | portable alpha, Rob April result, stop-out vs bounce |
| C06 | 4 | speed vs stops, variable sizing returns distribution |
| C07 | 4 | stops outliers, open profit give-back, index returns |
| C08 | 0 | career advice for young quant; nothing actionable |
| C09 | 2 | book list, annual review, 2024 Q1 strength, worst year |
| C10 | 3 | benchmark comparison, bad year attribution, dynamic selection |
| C11 | 2 | forecast variables that worked, worst drawdown maths |
| C12 | 4 | drawdown probability, faith, investor behaviour |
| C13 | 3 | meta-timing, costs review, slippage, Rob moves to cash |
| C14 | 1 | US economy bearish view |
| C15 | 4 | cash decision, liquidity, trend indicator correlation, single indicator paper |
| C16 | 3 | 112-day EMA, simplicity balance, family tree |
| C17 | 1 | history of industry, is trend dead |
| C18 | 3 | Winton/Aspect, leveraged ETF tweet |
| C19 | 2 | leveraged ETFs 4x performance and cost |
| C20 | 0 | outro and sponsor; nothing actionable |

## Claims

### C01
- **Rob Carver** US Treasuries have traditionally behaved like a Giffen good for markets: demand rises when risk and fear rise, making them the default safe haven.  #mech/risk_premium
  > the TR US Treasury bond is a little bit like the the GI and good for the financial markets
  indicator: US Treasury bond demand in stress · asset: rates · direction: buy Treasuries when risk rises (traditional) · conditions: traditional pattern; questioned in April 2025 · testable: partly - safe-haven behaviour of Treasuries in equity sell-offs can be tested · confidence: medium
  ^MT196-C01-1

### C02
- **Rob Carver** In the April 2025 tariff shock Treasuries sold off alongside equities instead of acting as the go-to safe asset, unlike earlier crises.  #mech/liquidity_flows _(time-bound view)_
  > people temporarily at least didn't seem that keen on owning US Treasury bonds
  indicator: Treasury yield vs equity moves in the Liberation Day sell-off · asset: rates · direction: Treasuries sold, no flight to safety · horizon: weeks · conditions: crisis originating in the US / US policy uncertainty · testable: yes - stock-bond correlation in stress episodes · confidence: medium
  ^MT196-C02-1
- **Niels Kaastrup-Larsen** The Swiss franc still seems to retain safe-haven behaviour when Treasuries and the dollar do not.  #mech/risk_premium
  > something like a Swiss Franks uh seems to still be be um having that um uh ability
  indicator: CHF as safe haven · asset: fx · direction: long CHF in stress · testable: yes - CHF return in equity drawdowns · confidence: low
  ^MT196-C02-2
- **Niels Kaastrup-Larsen** Bonds' safe-haven reputation may be recency bias from a 40-year falling-rate cycle, and may not hold if rates trend higher.  #mech/structural_shift
  > we are again just using kind of recency bias, meaning that we think about bonds as a safe haven because we've been in a 40-year cycle where interest rates just went down
  indicator: bond-equity hedge across rate regimes · asset: rates · direction: bonds less protective in a rising-rate era · horizon: years · conditions: rising-rate regime · testable: yes - stock-bond correlation by rate regime · confidence: low
  ^MT196-C02-3
- **Rob Carver** If policy produces stagflation (stagnation plus tariff inflation), the normal central bank reaction of cutting rates when growth weakens may not apply, so bonds hedge less.  #mech/policy_reaction _(time-bound view)_
  > the policies of the US government seem deliberately designed to create stagflation
  indicator: central bank reaction function under stagflation · asset: rates · direction: bonds weaker hedge · horizon: months · conditions: supply-shock / stagflation regime · testable: partly - need regime classification · confidence: medium
  ^MT196-C02-4

### C03
- **Rob Carver** Traditional Treasury buyers (e.g. China) may deliberately avoid Treasuries, and a crisis born in the US may make Treasuries a poor safe haven, a flows-based explanation.  #mech/liquidity_flows _(time-bound view)_
  > maybe it's the Chinese and they want to actually punish the US government
  indicator: foreign official demand for Treasuries · asset: rates · direction: Treasury selling · conditions: crisis originating in the US · testable: partly - TIC flow data · confidence: low
  ^MT196-C03-1
- **Rob Carver** Breakdown of institutional rules and frameworks is bad for US assets and markets.  #mech/structural_shift _(time-bound view)_
  > I think the breakdown in kind of institutional frameworks and
  asset: multi · horizon: years · testable: no - qualitative · confidence: medium
  ^MT196-C03-2
- **Niels Kaastrup-Larsen** Niels' CTA trend barometer reading of 52 at end of April 2025 coincided with a decent 10-day CTA recovery, though it is a short-term measure.  #mech/slow_reaction _(time-bound view)_
  > my trend barometer yesterday finished at 52, which actually is a good reading
  indicator: Top Traders trend barometer · asset: multi · horizon: days · conditions: short-term measure, April still negative · testable: partly - barometer is a CTA-index derived gauge · confidence: medium
  ^MT196-C03-3

### C04
- **Niels Kaastrup-Larsen** April 2025 was a roller coaster: MSCI World fell 11% peak to trough yet ended the month positive, so CTAs caught on the wrong side of reversals after Liberation Day lost money.  #mech/overshoot _(time-bound view)_
  > MEI world index for example dropped 11% peak to trough and still it managed to end the month of April positive
  indicator: MSCI World, CTA indices · asset: equities · direction: trend followers lose on sharp V reversals · horizon: weeks · conditions: sharp reversal after announcement shock · testable: yes - trend returns around V-shaped reversals · confidence: high
  ^MT196-C04-1
- **Niels Kaastrup-Larsen** Safe-haven assets (dollar, bonds) sold off in the shock, so dollar and Treasury trend positions were ineffective hedges in April 2025.  #mech/liquidity_flows _(time-bound view)_
  > more safe haven assets selling off like the dollar. uh we saw bonds got sold quite hard initially
  indicator: USD, Treasuries · asset: multi · direction: dollar and Treasuries fell with equities · horizon: weeks · testable: partly · confidence: medium
  ^MT196-C04-2
- **Niels Kaastrup-Larsen** The largest trend followers lost from about 1% to 10% in April 2025, leaving year-to-date results between slightly up and down 15-18%.  #mech/risk_management _(time-bound view)_
  > returns in the range of say minus one or flat to about down 10% uh for the month
  indicator: large CTA monthly returns · asset: multi · horizon: months · conditions: dispersion by speed, risk management and markets traded · testable: yes - CTA index data · confidence: medium
  ^MT196-C04-3
- **Niels Kaastrup-Larsen** Dispersion of returns across trend followers is not unusual historically (CFM research); speed, risk management and markets traded are the usual sources of differentiation.  #mech/research_method
  > they're not unusual once you sort of uh look at it in historical perspective at least according to CFM
  indicator: cross-manager return dispersion · asset: multi · horizon: years · testable: yes - compare manager dispersion over time · confidence: medium
  ^MT196-C04-4
- **Niels Kaastrup-Larsen** Single markets such as JGBs, copper and silver were specifically tricky for trend followers in April 2025, while short-term interest rates, softs and meats gave relief.  #mech/slow_reaction _(time-bound view)_
  > Japanese government bonds uh copper silver those were actually specifically tricky markets
  indicator: JGB, copper, silver, short-term interest rates, softs, meats · asset: commodities · horizon: weeks · conditions: April 2025 reversal · testable: partly · confidence: low
  ^MT196-C04-5
- **Niels Kaastrup-Larsen** April 2025 outcomes may differ materially between hard-stop trend systems and continuous-signal systems.  #mech/risk_management _(time-bound view)_
  > I thought this month particular could be quite different from whether you use a stop hard stop uh system or whether you use continuous signals
  indicator: stop-loss vs continuous trend signals · asset: multi · horizon: weeks · conditions: sharp drop then V bounce · testable: yes - simulate both rule types on the episode · confidence: medium
  ^MT196-C04-6
- **Niels Kaastrup-Larsen** Commodities (energies, grains) again delivered the trend-following gains in April, as in past stress periods.  #mech/cycle_persistence _(time-bound view)_
  > commodities really won the day again uh in April
  indicator: energy and grain trends · asset: commodities · direction: long/short commodity trends profited · horizon: weeks · conditions: stress months · testable: partly · confidence: medium
  ^MT196-C04-7
- **Niels Kaastrup-Larsen** Short-term models gained more in the first half of April 2025 than long-term models, but later reversals erased much of that benefit and moves were sometimes too fast (overnight gaps) even for fast models.  #mech/slow_reaction _(time-bound view)_
  > short-term models, certainly enjoyed uh the first half of the month better than the longerterm models
  indicator: trend speed · asset: multi · direction: faster models better initially · horizon: weeks · conditions: V-shaped crash and reversal · testable: yes - speed-split trend returns · confidence: medium
  ^MT196-C04-8
- **Niels Kaastrup-Larsen** In April 2025 trend followers as a group faced headwinds in equity and currency positions (the sharp V-reversal after the tariff announcement), while commodities and short-term rates were where gains or relief came from.  #mech/slow_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > we all face some headwinds in equities for sure. Um currencies most likely as well.
  indicator: CTA sector P&L attribution (equities, FX vs commodities, short rates), April 2025 · asset: multi · direction: trend-following long/short positions in equities and FX lost · horizon: weeks · conditions: sharp reversal after a policy-announcement shock · testable: yes - sector-level P&L attribution of CTA indices · confidence: medium
  ^MT196-C04-X1

### C05
- **Niels Kaastrup-Larsen** Portable alpha products (trend overlay on equity beta) had negative alpha and flat beta in April 2025, so looked bad though doing what they are designed to do.  #mech/research_method _(time-bound view)_
  > most people would have had um negative alpha from the portable side and and maybe the beta side actually ended up pretty flat
  indicator: portable alpha CTA overlay · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT196-C05-1
- **Rob Carver** Rob's own April 2025 return was -5.5%, roughly in line with the industry; the very fastest models made a little money on the initial bounce but whipsawed afterwards.  #mech/slow_reaction _(time-bound view)_
  > I was down five and a half% maybe in line with the industry actually.
  indicator: Rob Carver fund track record · asset: multi · horizon: weeks · testable: no - anecdote · confidence: high
  ^MT196-C05-2
- **Niels Kaastrup-Larsen** A stop-based trend follower who is stopped out cannot re-enter until a new signal, so can miss the bounce, while a continuous-signal approach keeps participating.  #mech/risk_management
  > if you get stopped out and then you get this bounce and sometimes, you know, it's great to have, you know, a a simple trigger um and you're out and sometimes it works against you
  indicator: stop-out and re-entry rule · asset: multi · horizon: weeks · conditions: V reversals · testable: yes · confidence: medium
  ^MT196-C05-3
- **Rob Carver** Rob says November 2021 was a worse single-month return for him than April 2025, but it hurt less in context because he was at a high-water mark and the following months recovered; the current drawdown has lasted longer since his high-water mark of May 2024.  #mech/new _(added by map cross-check, time-bound view)_
  > that was actually a worse single month return for me
  indicator: own monthly returns · asset: multi · direction: n/a · horizon: months · testable: no: anecdote · confidence: medium
  ^MT196-C05-R1

### C06
- **Rob Carver** Capturing the April 2025 V-shaped bounce would require extremely fast trading; trading only slightly too slowly gets whipsawed, while a very wide stop simply holds through.  #mech/slow_reaction _(time-bound view)_
  > the only way that would have been trading fast and also very, very fast indeed
  indicator: S&P 500 trend speed · asset: equities · horizon: days · conditions: extreme V reversal · testable: yes · confidence: medium
  ^MT196-C06-1
- **Rob Carver** A tight stop gets triggered near the lows, booking a loss and leaving a flat position, producing a sharp drop then flat P&L curve.  #mech/risk_management
  > if let's say you were running a stop loss trend following system but your stop was a bit tighter
  indicator: stop-loss trend system · asset: equities · horizon: weeks · conditions: tight stop with a ~18-20% drawdown trigger · testable: yes · confidence: medium
  ^MT196-C06-2
- **Rob Carver** Variable position sizing that adjusts positions daily to risk automatically cut Rob's risk to about a third of normal (less in equities) as the trend became unclear, so his P&L dropped then went sideways.  #mech/risk_management _(time-bound view)_
  > I'm running currently something like a third of my normal risk levels
  indicator: volatility-scaled position sizing · asset: multi · direction: reduce risk when trend unclear · horizon: days · testable: yes - compare dynamic sizing vs stops · confidence: medium
  ^MT196-C06-3
- **Rob Carver** Variable position sizing makes return distributions closer to normal with fewer extreme outliers, while stops make outliers (both big winners and big losers) more likely.  #mech/risk_management
  > running um with with variable position sizing essentially makes your distribution returns closer to a normal distribution to a nice bell curve without extreme outliers
  indicator: stops vs variable position sizing · asset: multi · testable: yes - compare skew and kurtosis · confidence: medium
  ^MT196-C06-4
- **Rob Carver** Dispersion among trend followers in a V-shaped reversal has two separate drivers that should not be conflated: signal speed, and the position-capture method (hard or wide stops versus continuously risk-adjusted sizing).  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > the sort of conflation here are two things, which is speed and kind of the the way, as you say, the way you kind of capture your positions.
  indicator: signal speed (lookback) and stop-based vs continuous position sizing · asset: multi · horizon: weeks · conditions: sharp V-shaped reversals · testable: yes - run speed and stop/continuous variants independently through the April 2025 episode · confidence: high
  ^MT196-C06-X1

### C07
- **Rob Carver** Stop-based systems give larger outliers; the upside outliers are desired for positive skew but downside outliers occur when closing at the wrong moment or when an oversized position (e.g. cocoa) moves against you.  #mech/risk_management
  > you know, makes you more likely that you'll have a, you know, bigger outliers.
  indicator: stop-loss, position concentration (cocoa) · asset: commodities · conditions: oversized exposure to a market that has run up · testable: partly · confidence: medium
  ^MT196-C07-1
- **Niels Kaastrup-Larsen** Funds with large open profits after a big run (high flyers) risk large give-back, so new investors entering at that time face outsized drawdown risk, as seen in April 2025.  #mech/crowding_positioning
  > when you build up a lot of open profit which of course is great for the investors who are in the fund
  indicator: open profit / prior outperformance · asset: multi · horizon: months · conditions: new investor entering after a hot streak · testable: yes - performance chasing in CTAs · confidence: medium
  ^MT196-C07-2
- **Rob Carver** Funds that can make 100%+ in good years can lose 30-60% in bad years; whether that is Kelly-optimal matters less than whether investors can stomach it.  #mech/risk_management
  > in the bad years, you could be down 30 40 50 60% potentially
  indicator: fund leverage level · asset: multi · horizon: years · testable: yes - Kelly sizing analysis · confidence: medium
  ^MT196-C07-3
- **Niels Kaastrup-Larsen** April 2025 index results: Barclay BTOP50 -3.49%, SG CTA -4.47%, SG Trend -4.98% (-9.41% YTD), SG short-term traders -0.86%, Bridge flat-fee trend -6.24% (-10.58% YTD), MSCI World +0.74%, S&P 500 -0.68%, US aggregate bonds +0.36%.  #mech/slow_reaction _(time-bound view)_
  > SG trend down 4.98% um and down 9.41% for the year
  indicator: BTOP50, SG CTA, SG Trend, SG Short-Term Traders, Bridge alternatives index · asset: multi · direction: short-term traders outperformed trend · horizon: months · conditions: April 2025 · testable: yes - public index data · confidence: high
  ^MT196-C07-4
- **Niels Kaastrup-Larsen** Early April 2025 data suggested most trend managers' risk-management systems worked as designed, so a down month for those who followed their process is within the normal range and not evidence that the strategy has broken.  #mech/risk_management _(added by sonnet-xhigh cross-check, time-bound view)_
  > for the most part actually managers did well and risk management systems held up as they
  indicator: CTA index monthly returns, April 2025 · asset: multi · horizon: months · conditions: early indications only, before full numbers were in · testable: partly - compare April 2025 loss with the historical distribution of monthly CTA returns · confidence: medium
  ^MT196-C07-X1

### C08
- **Rob Carver** Implementing systematic futures strategies needs practical market-structure knowledge (quoting conventions such as US bonds in 32nds/64ths, how futures trade and settle), and early-career quant work is mostly data cleaning and inspecting numbers; ignoring contract mechanics causes data and execution errors.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > that US bonds trade um on on 30 seconds or 64th rather than on decimal fractions
  indicator: contract quoting and tick conventions · asset: rates · testable: no - practitioner advice · confidence: medium
  ^MT196-C08-X1

### C09
- **Niels Kaastrup-Larsen** Trend following had its best quarter in about 25 years in Q1 2024, then became much more challenging from April 2024.  #mech/cycle_persistence _(time-bound view)_
  > The first quarter was so strong, the best I think it had was probably the best quarter in in the last 25 years.
  indicator: CTA quarterly returns · asset: multi · horizon: months · testable: yes - CTA index history · confidence: medium
  ^MT196-C09-1
- **Rob Carver** Rob's worst year in his own trading was about -15%, a roughly one-in-10-year event; the 2024-25 tax year drawdown was driven by a few short sharp legs (about 12% over 3 weeks tied to the yen), not by a steady bleed.  #mech/risk_management _(time-bound view)_
  > My worst my worst ever year of of since I started doing this with my own money which is my first full year was um April 2014 to April 2015.
  indicator: Rob Carver track record, yen · asset: multi · horizon: months · testable: no - anecdote · confidence: high
  **Correction (cross-check):** Conflates the previous worst year with the current one: Rob says his worst ever year (his first full year trading his own money) was April 2014 to April 2015; the April 2024 to April 2025 year (about -15%, per the later -14.7% figure) is described as roughly a one-in-10-year event. The leg of about 12% over about 3 weeks was mostly the yen (July), and there was also a May to mid-June leg, followed by drift to October and sideways. → Rob's 2024-25 tax year was about -15%, the worst since his previous worst year (April 2014 to April 2015), which he calls roughly a one-in-10-year event; the loss came from a few sharp legs (May to June, and about 12% over 3 weeks in July tied mainly to the yen) then a gentle drift to October and a sideways path.
  ^MT196-C09-2
- **Rob Carver** Rob raised his trend allocation at the end of the previous tax year, after trend's best quarter in 25 years, so the 2024-25 losses hit a larger capital base: adding capital after a strong run carries the same give-back risk he flags for investors entering at high open profit.  #mech/behavioral _(added by sonnet-xhigh cross-check, time-bound view)_
  > the money I've lost the last tax year was with a larger amount of capital than I had before.
  asset: multi · direction: increased allocation to trend before a drawdown · horizon: years · conditions: allocation increase after a very strong period · testable: partly - evaluate allocation-timing rules after strong trend quarters · confidence: medium
  ^MT196-C09-X1

### C10
- **Rob Carver** In a well-diversified multi-asset, multi-speed portfolio a bad year occurs because everything goes wrong at once, not because of concentration in one market; Rob lost money in equities, energies, FX, metals and bonds (but made money in S&P), with natural gas the worst.  #mech/cycle_persistence _(time-bound view)_
  > It's rarely because you're overexposed to one individual market
  indicator: sector P&L attribution · asset: multi · horizon: years · conditions: diversified trend portfolio in a trendless year · testable: yes - P&L attribution · confidence: medium
  ^MT196-C10-1
- **Rob Carver** Over the year to end-March/April 2025 the SG CTA index was about -10% versus Rob at about -14.7% on much higher volatility, so vol-adjusted his performance was acceptable.  #mech/risk_management _(time-bound view)_
  > the SGCTA index for for the period I looked at which was um end of March to end of March sorry it was down 10%
  indicator: SG CTA Index · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT196-C10-2
- **Rob Carver** Selecting positions dynamically from a larger instrument universe shows noisy return differences year to year versus the earlier set, but gives better risk targeting, which is a reason to keep it.  #mech/research_method
  > I think the dynamic is better at risk targeting so even if it doesn't give me extra return I'll probably stick with it
  indicator: dynamic instrument selection · asset: multi · horizon: years · testable: yes - compare risk-target accuracy · confidence: medium
  ^MT196-C10-3
- **Rob Carver** Redesigning a system after a bad year is a dangerous path (it fits recent noise); the post-year design review should be symmetric and be asked after an exceptional year too, with changes only if the evidence is clear.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > it's the obvious question you get asked if you've had a bad year, right? And um well, you should also ask yourself if you have an exceptional year
  asset: multi · horizon: years · conditions: single-year performance is mostly noise · testable: no - process discipline · confidence: high
  ^MT196-C10-X1

### C11
- **Rob Carver** Of about 50 forecasting variables, nearly all lost money over the year except fast relative momentum, relative carry and relative value skew; relative (cross-sectional) signals held up, and even carry (especially the slowest) lost, so style diversification helped.  #mech/cycle_persistence _(time-bound view)_
  > pretty much all of them uh lost money um apart from three which was um fast relative momentum relative car carry and relative value skew
  indicator: fast relative momentum, relative carry, skew value · asset: multi · direction: relative signals worked while outright trend failed · horizon: years · conditions: 2024-25 trendless regime · testable: yes · confidence: high
  ^MT196-C11-1
- **Rob Carver** The longer a strategy runs, the larger its worst drawdown is expected to be, since expected worst drawdown grows with time, so veteran funds hitting new worst drawdowns is mathematically unsurprising.  #mech/research_method
  > mathematically um the the longer you run any trading strategy the worse the bigger your worst draw down will get over time
  indicator: maximum drawdown vs track-record length · asset: multi · horizon: years · testable: yes - extreme value statistics · confidence: high
  ^MT196-C11-2

### C12
- **Rob Carver** Compare the current drawdown to the probability of such a drawdown in a comparable period (about 30% over 12 years) rather than just to the backtest max; a 50% drawdown would be well beyond the backtest and expectation and be a real concern.  #mech/research_method
  > what's the probability of getting a draw down this size in say a 12 year trading period and it'll tell you that you know it's about a 30% chance
  indicator: drawdown probability simulation · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT196-C12-1
- **Rob Carver** Because trend signals have a modest Sharpe ratio, it takes a very long time to statistically tell that a strategy has stopped working, so continuing is largely a matter of faith.  #mech/research_method
  > the sort of um efficacy of of of particularly trend following signals is quite low. The sharp ratio is not that high
  indicator: trend following Sharpe ratio · asset: multi · horizon: years · testable: yes - power analysis of Sharpe tests · confidence: high
  ^MT196-C12-2
- **Rob Carver** Systematic traders should in theory do nothing when a strategy underperforms; both managers and investors find this hard, and investors tend to redeem after bad months.  #mech/behavioral
  > if things start to go against you as a systematic trader, in theory, you should do nothing, but in practice it's very hard not to
  asset: multi · testable: partly · confidence: high
  ^MT196-C12-3
- **Niels Kaastrup-Larsen** November 2021 was one of the worst single days for many trend managers yet was followed by one of their best 12-month periods, so redeeming after a bad month can be wrong.  #mech/behavioral _(time-bound view)_
  > it was also the beginning of one of the best 12 months returns that they've ever had
  indicator: trend follower returns after sharp drawdown days · asset: multi · horizon: months · testable: yes - forward returns after drawdowns · confidence: medium
  ^MT196-C12-4
- **Rob Carver** Rob's answer to trend underperformance is to keep trend (about 50-60% of his portfolio) and add non-trend systems he is confident in for diversification, rather than abandoning trend or tinkering with it.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > I'm happy to include it in my portfolio. Um, you know, if I'm confident in that it's, you know, I'm happy to have more diversification.
  indicator: trend share of portfolio (about 50-60%) · asset: multi · direction: diversify across systematic styles · horizon: years · conditions: only systems he is confident in · testable: partly - portfolio of trend plus other styles versus pure trend · confidence: medium
  ^MT196-C12-X1

### C13
- **Rob Carver** Attempts to meta-time trend following with quantitative conditioning variables found very few useful predictors; best response is providing visibility by showing historical analogues where trend did fine.  #mech/research_method
  > whenever I've tried to do that in a quantitative way I found very few things that that sort of tell you whether a trend fun is going to do well or badly
  indicator: trend fund meta-timing · asset: multi · testable: yes · confidence: medium
  ^MT196-C13-1
- **Rob Carver** Rob checks commissions plus slippage annually (about 100 bp, in line with backtest) because costs are predictable while P&L is nearly random; slippage is the fill price versus mid at order time, and passive limit orders then switching give lower costs than the conservative half-spread backtest.  #mech/research_method
  > I was just under um 100 basis points which is kind of in line with with what I expect in my back test
  indicator: trading cost and slippage vs mid · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT196-C13-2
- **Rob Carver** Rob, already underweight US stocks, sold remaining US stock exposure before Liberation Day and went to cash in his long-only portfolio, his biggest discretionary decision ever, outside his systematic portfolio.  #mech/policy_reaction _(time-bound view)_
  > I actually sold all my remaining US stock exposure
  indicator: US equities · asset: equities · direction: sold US equities, held cash · horizon: months · testable: no - discretionary view · confidence: medium
  ^MT196-C13-3

### C14
- **Rob Carver** Rob expects a deep technical US recession as tariffs hit goods already in transit; Q1 GDP was unaffected by tariffs, and CEOs are reluctant to give honest forward earnings, so the real-economy effect and earnings downgrades come later and the market should not stay where it is.  #mech/policy_reaction _(time-bound view)_
  > it feels like the US economy has kind of run out and it's just not realizing that there's there's nothing below it and it's just going to crash
  indicator: US GDP, corporate earnings guidance, tariffs · asset: equities · direction: bearish US equities · horizon: months · conditions: lags between tariffs and real-economy data · testable: no - view · confidence: medium
  ^MT196-C14-1
- **Rob Carver** The negative Q1 2025 US GDP print was distorted by gold flows and a pre-tariff import surge (imports subtract from GDP), so it is a noisy signal of tariff damage; the real tariff effect should show in later quarters' hard data and earnings.  #mech/new _(added by sonnet-xhigh cross-check, time-bound view)_
  > there's gold which messed things up and and and then there's the the sort of the spike of imports prior to the tariffs
  indicator: US real GDP Q1 2025, net imports, gold flows · asset: equities · direction: bearish US growth expected in later quarters · horizon: months · conditions: tariff-driven front-running of imports · testable: yes - GDP components and subsequent quarters · confidence: medium
  ^MT196-C14-X1
- **Rob Carver** Rob concedes that his sale of all US stocks and move to cash is looking wrong so far because the market rebounded after the April low; he regrets not going to cash earlier, as Warren Buffett did.  #mech/new _(added by map cross-check, time-bound view)_
  > right now that decision is looking looking bad because the market has rebounded since then
  indicator: own discretionary US equity exit · asset: equities · direction: cash decision lost to rebound · horizon: weeks · conditions: After the April 2025 rebound · testable: no: anecdote · confidence: high
  ^MT196-C14-R1

### C15
- **Rob Carver** Staying in cash at about 4% is preferred to equities whose expected return may only be about 4% given large downside risk; his systematic portfolio still follows trends, so he would partly benefit if equities rally.  #mech/risk_premium _(time-bound view)_
  > I'm now my money's in cash it's earning you know four 4% or something a year. Do I think the market's going to be 4% higher? I mean, maybe. But the risk is just astonishing.
  indicator: cash yield vs equity risk · asset: equities · direction: cash over equities · horizon: months · testable: no - discretionary · confidence: medium
  ^MT196-C15-1
- **Rob Carver** In the first days after Liberation Day some positions could not be sold because there was no bid, illustrating liquidity risk in stress.  #mech/liquidity_flows _(time-bound view)_
  > there were some positions I couldn't sell. There was no bid in the
  indicator: bid liquidity · asset: equities · horizon: days · conditions: extreme stress · testable: partly · confidence: high
  ^MT196-C15-2
- **Rob Carver** Different trend indicators are highly correlated, so no one is uniquely best, but once automated the cost of adding another signal is zero, so you might as well include several.  #mech/research_method
  > the cost of having an additional signal in there is zero
  indicator: multiple trend indicators and speeds · asset: multi · testable: yes - correlation of trend filters · confidence: high
  ^MT196-C15-3
- **Rob Carver** A single calibrated exponential moving average can summarise the whole universe of trend indicators (a representative filter), using the mathematical link between exponential and simple moving averages.  #mech/research_method
  > what if we were to just pick up one single indicator
  indicator: single EMA representing trend universe · asset: multi · testable: yes · confidence: medium
  ^MT196-C15-4

### C16
- **Rob Carver** The paper reports an exponential moving average with a 112-day parameter is optimal at capturing trends; Rob would not replace his multi-indicator system but values it as first-principles thinking.  #mech/research_method
  > if you use um a just an explanatory moving average with 112 days as the parameter that's optimal at capturing trends
  indicator: 112-day EMA · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT196-C16-1
- **Niels Kaastrup-Larsen** There is a fine balance between simplicity and over-complication in trend systems and it makes a big difference.  #mech/research_method
  > there is a very fine balance between simplicity in your trend system and over complication and it's really about getting that balance right
  asset: multi · testable: partly · confidence: medium
  ^MT196-C16-2
- **Rob Carver** Trend followers form a family tree with distinct lineages (US pit-trading wing, British quantitative wing, Scandinavian), which explains differences of opinion about sizing and position changes.  #mech/structural_shift
  > there's almost two or maybe even three sort of original parents or grandparents in this family tree
  indicator: trend follower lineage · asset: multi · testable: no - history · confidence: medium
  ^MT196-C16-3

### C17
- **Niels Kaastrup-Larsen** The question whether trend following is dead has recurred many times and the industry survived each time.  #mech/cycle_persistence
  > Of course, we've survived many of those uh in the past. I'm not worried about
  asset: multi · horizon: years · testable: no - historical · confidence: medium
  ^MT196-C17-1
- **Rob Carver** After a long stretch of weak trend returns, most trend-following firms diversified into other systematic strategies, either inside the flagship fund or as separate funds, which leaves open the question whether pure trend still works.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > obviously most people have done diversified to a degree into other systematic strategies either within the fund or launching a separate funds
  asset: multi · horizon: years · testable: partly - correlation of diversified CTA funds with equities versus pure trend · confidence: medium
  ^MT196-C17-X1
- **Niels Kaastrup-Larsen** Niels adds that the early trend-following pioneers in the US were people such as Keith Campbell and Bill Dunn (from the mid-1970s), not the Turtles' teacher Richard Dennis and John Henry.  #mech/new _(added by map cross-check)_
  > frankly Richard Dennis and um uh John Henry were not the pioneers right
  indicator: none · asset: multi · direction: n/a · horizon: n/a · testable: no: history · confidence: high
  ^MT196-C17-R1

### C18
- **Rob Carver** Winton diversified away from pure trend following into other quant strategies, did poorly when CTAs did well and was more correlated to equities, with AUM falling from above $30bn to $7.5bn, while Aspect stuck to trend and returned 40% in 2020.  #mech/crowding_positioning _(time-bound view)_
  > By 2020, only a small part of Winton's flagship fund was in traditional trend following.
  indicator: Winton and Aspect strategy drift · asset: multi · horizon: years · testable: partly - manager case studies · confidence: medium
  ^MT196-C18-1
- **Niels Kaastrup-Larsen** Winton has rebuilt its trend-following allocation and again manages a lot of money there.  #mech/structural_shift _(time-bound view)_
  > Winon has really done a great job in rebuilding the trend side
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT196-C18-2
- **Rob Carver** A tweet claims 3x leveraged Nasdaq turns 7% a year into 21%, which ignores that leveraged ETFs reset daily and are not a remotely good idea.  #mech/behavioral
  > he talks about the NASDAQ being up 7% every year, and if you have a 3x leveraged NASDAQ, um, ticker, you can make 21%
  indicator: 3x leveraged Nasdaq ETF · asset: equities · testable: yes - simulate leveraged ETF compounding · confidence: high
  **Correction (cross-check):** Wrong speaker and an over-read: it is Niels who describes the tweet (Nasdaq up 7% a year, 3x gives 21%); Rob's reply here only says it is not remotely a good idea and worries that people may take it seriously. The daily-reset explanation comes later (C19). → Niels reports a tweet claiming a 3x leveraged Nasdaq ETF turns a 7% annual Nasdaq return into 21%; Rob replies that it is not remotely a good idea and that Twitter posts like this can mislead people.
  ^MT196-C18-3

### C19
- **Rob Carver** The one quadruple-leveraged S&P 500 ETF was down 52% year to date versus S&P down about 4.5%, because daily reset compounding makes adverse moves devastating.  #mech/risk_management _(time-bound view)_
  > So, it's lost over half its value.
  indicator: 4x leveraged S&P 500 ETF · asset: equities · horizon: months · conditions: volatile choppy market · testable: yes - volatility drag formula · confidence: high
  ^MT196-C19-1
- **Rob Carver** Leveraged ETFs carry high expense ratios (about 295bp) and are toxic as holding instruments; multiples of 2-4x on already risky assets exceed Kelly-criterion sizing.  #mech/risk_management
  > the expense ratio on that is a incredibly is 295 basis points
  indicator: leveraged ETF expense ratio, Kelly criterion · asset: equities · horizon: years · testable: yes · confidence: high
  ^MT196-C19-2
- **Rob Carver** Leveraged ETFs stack fixed 2x-4x multiples (long and inverse) on already very volatile assets such as Bitcoin, semiconductors, South Korea and single stocks, the opposite of volatility-scaled sizing; with daily reset they compound the leverage and lose heavily in volatile, choppy markets.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > you can also get um triple leverage shorts so you can get triple leveraged shorts NASDAQ um you know Bitcoin you name it
  indicator: leveraged ETF product universe and daily reset · asset: multi · direction: avoid holding leveraged ETFs · conditions: choppy, volatile markets · testable: yes - simulate daily-reset leveraged returns · confidence: high
  ^MT196-C19-X1

