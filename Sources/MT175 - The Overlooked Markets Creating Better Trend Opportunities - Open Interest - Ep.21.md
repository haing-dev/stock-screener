---
source_id: MT175
title: "The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21"
date: 2026-04-09
channel: "Top Traders Unplugged"
url: 
words: 8440
claims: 40
added_by_crosscheck: 12
corrections: 1
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Tom Babbage (chief scientist, Gresham Quant)", "Moritz Seibert (host, Open Interest series)"]
tags: [source, layer0]
---
# The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21

**Speakers:** Tom Babbage (chief scientist, Gresham Quant); Moritz Seibert (host, Open Interest series)

**Summary:** Open Interest Ep.21 (Apr 2026): Babbage explains Gresham Quant's commodity-only alternative-markets trend program: structural market selection, capacity discipline, trend quality (autocorrelation) and execution with a risk-budgeted desk that waits passively.

**Approach:** trend following, alternative commodities, execution, capacity

**Cross-check completeness estimate of first read:** 0.82 - first reader captured the full argument chain (structural market selection, alternativeness, trend quality, curve position, capacity, execution framework and costs, client positioning) accurately; missed supporting reasoning and caveats: fundamental versus measured diversification, capacity scaling with commodity volatility, the factor themes accessible, furnace-type clusters, long/short symmetry exceptions, Liberation Day insulation, the non-discretionary clarification, the multi-year drawdown, the CPI-goods inflation mechanism and the client top-up use

## Argument map

**Episode thesis:** Tom Babbage argues that a commodity-only alternative-markets trend program earns its place through structural market selection, not backtest selection: physically distinct, little-speculated commodities have more independent risk, better trend drift and better trend autocorrelation because supply and demand are inelastic and hedgers dominate, provided capacity stays small enough to allocate meaningfully to niche markets. He adds that execution is a second source of edge: giving the trading desk a tracking-error budget to wait passively behaves like an anti-trend buffer, cuts slippage close to zero relative to prior years and permits faster signals.

### Tom Babbage (Chief scientist, Gresham Investment Management; runs the AQA alternative-commodity trend program (ex-Winton researcher, astrophysics PhD))
Fingerprint: #approach/trend_following #approach/commodity_fundamentals #approach/diversification_risk_parity #approach/costs_execution #approach/research_robustness_overfitting #approach/structural_themes #approach/portfolio_construction_stacking #approach/position_sizing_vol_target
_Speaker note: Single guest; host Moritz Seibert asks questions and is not mapped as a speaker (his one stated characterisation, that the desk is a discretionary alpha generator, is recorded under disagreements). Caption slip: the program is named 'AQR' once in C09, it is AQA. Ledger claim C09-3 corrected as noted._

**Worldview premises**
- Diversification comes from effective degrees of freedom, not market count; beyond a few hundred markets the next one has a tiny allocation and changes nothing, and related instruments (2-, 5-, 10-year Treasuries) are one market. _[theoretical, stated; support: Allocation arithmetic and structural reasoning.]_ ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C02-1|C02-1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C02-X1|C02-X1]])
- Financialized markets (FX, indices, fixed income) collapse to one in macro shocks, whereas less financialized commodities with distinct regional, consumer and producer drivers stay independent and resilient. _[empirical, stated; support: Structural description plus examples (sunflower seeds, US East Coast power, Chinese bitumen); not quantified in the talk.]_ ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C02-2|C02-2]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C02-X1|C02-X1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C10-X1|C10-X1]])
- Commodity trends have a structural cause: inelastic supply and demand, long permitting, shipping and storage frictions mean imbalances clear only via large persistent price moves. _[theoretical, stated; support: Coal mine example; no tests shown.]_ ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C06-1|C06-1]])
- Trend splits into drift (quantity) and autocorrelation (quality), and both are better in low-speculation alternative commodities than mainstream ones over about 30 years. _[empirical, stated; support: Internal paper 'You Trend, I'll Follow'; a measured gap over 30 years.]_ ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C05-1|C05-1]])
- Deferred contracts (about 5 years out) are dominated by hedgers and trend more smoothly than the speculative, news-driven front. _[theoretical, stated; support: Analogy of news and weather vs climate.]_ ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C05-2|C05-2]])
- Selecting markets by backtest Sharpe is data mining and the key to future misery; selection should rest on market structure. _[experience, stated; support: Claims it is classic systematic finance failure since parameter search is cheap; example of carbon.]_ ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C04-2|C04-2]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C06-2|C06-2]])
- Alternativeness means low correlation to mainstream commodities and few speculators, not low liquidity or access barriers. _[experience, stated; support: A low-liquidity oil spread correlated with crude is just costly crude exposure.]_ ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C04-3|C04-3]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C04-4|C04-4]])
- Capacity discipline is what keeps a commodity book diversified: at billions, allocation concentrates in crude, gold and gas and niche markets cease to matter. _[theoretical, stated; support: Capacity arithmetic; half-closed around 1bn.]_ ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C03-1|C03-1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C03-X1|C03-X1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C03-X2|C03-X2]])
- Execution risk is a small share of portfolio variance, so cost savings from passive execution dominate any risk it adds. _[empirical, stated; support: At 15% annual risk, trades are about 5% of daily variance and uncorrelated across markets.]_ ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C08-3|C08-3]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C08-2|C08-2]])
- Commodity prices and inflation are two sides of the same coin, so commodity trend is convex to both inflation and deflation regimes. _[theoretical, stated; support: Goods are commodities; cites the firm's 'Eras Tour' paper adding commodity trend to 60/40.]_ ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C12-2|C12-2]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C12-X2|C12-X2]])
- Signals with clear structural drivers survive long drawdowns, while opaque machine-learning signals are pulled after three weak years. _[behavioural, stated; support: Client behaviour observed by the firm.]_ ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C12-1|C12-1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C12-X1|C12-X1]])

**Chain: Why less-speculated commodities trend better**
1. Supply cannot flex (coal mines take decades to permit and keep running at a loss) → price must move far to clear the imbalance: Shipping and storage frictions add to inelasticity. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C06-1|C06-1]])
2. Few speculators and hedger-dominated deferred contracts → smoother, higher-autocorrelation trends: Fewer noisy speculative flows. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C05-1|C05-1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C05-2|C05-2]])
3. Speculators enter (CTAs attend the same conferences, show up in COT) → market becomes financialized and less interesting: Trend quality and independence erode. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C04-4|C04-4]])
- Evidence: 30-year drift and autocorrelation comparison from an internal paper; European carbon example.
- Fails when: When the market becomes financialized; also price floors cap short trends (California carbon).

**Chain: Capacity discipline preserves diversification**
1. Billions in assets → allocation concentrates in crude, gold, gas: Position limits must allow exit within about a week in stress. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C03-1|C03-1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C07-1|C07-1]])
2. Concentration → niche markets have negligible effect and the book looks like a standard commodity allocation: Tiny weights contribute nothing. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C02-1|C02-1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C03-X2|C03-X2]])
3. Soft-close near 1bn with headroom (top-line capacity of a couple of billion) → existing clients can benefit from organic growth over several years and the book keeps distinct risk factors: Trend needs a multi-year horizon. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C03-2|C03-2]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C03-X1|C03-X1]])
- Evidence: Capacity measured in dollar risk; COVID paper capacity 4-5bn, not assumed to persist.
- Fails when: Not stated.

**Chain: Passive, risk-budgeted execution lowers cost and adds diversification**
1. Splitting orders over the day looks fine against TWAP/VWAP → hidden autocorrelated cost; slippage rises as CTAs grow: Slices are benchmarked individually. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C08-2|C08-2]])
2. Desk given a tracking-error budget to wait over several days → does not cross the spread about half the time: Prices are near 50/50 each day; spreads can reach 100bp in freight. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C09-1|C09-1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C09-2|C09-2]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C10-2|C10-2]])
3. Model changes target before the order completes → invisible savings, slippage close to zero relative to earlier years: Smaller trade needed after a day. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C09-3|C09-3]])
4. Waiting is an anti-trend component → more diversification, so the risk scale can be raised and signals can be faster: Faster signals look better before costs; patient execution preserves them after costs. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C10-1|C10-1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C09-2|C09-2]])
- Evidence: Just over a year live on AQA; earlier use in the sister financial program; April 2025 propane example.
- Fails when: Market runs away: slippage variance rises and the desk is forced to trade at the limit.

**Chain: Commodity trend as inflation and 60/40 protection**
1. Inflation measures goods prices and goods are commodities → commodity prices and inflation move together: Two sides of the same coin. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C12-X2|C12-X2]])
2. Trend follows the commodity move in either direction → positive convexity in inflation and deflation regimes: Long and short symmetric. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C12-2|C12-2]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C06-X1|C06-X1]])
- Evidence: Firm's 'Eras Tour' paper (60/40 with basic commodity trend).
- Fails when: Not stated.

**Decision process**
- [universe] Trade about 150 markets, rotating roughly a quarter per year (44 dropped, 31 added in 2025), chosen on market structure: who trades, where on the curve, correlation to mainstream commodities, speculator share (COT, open interest to delivery, broker queries, conference attendance).. Why: Backtest selection is data mining. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C04-1|C04-1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C04-2|C04-2]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C04-3|C04-3]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C04-4|C04-4]])
- [universe] Cluster markets by shared physical drivers (a furnace cluster of iron ore, flat glass, coking coal) to manage correlation and risk.. Why: Real supply-chain linkages, not only statistical estimates. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C04-X1|C04-X1]])
- [universe] Avoid markets that have become financialized (cocoa) and avoid the front of the oil curve; accept an asset without a prior trend record (EU carbon with negative 8-year trend Sharpe was included in 2016 and became a top performer).. Why: Selection on structure rather than backtest. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C01-1|C01-1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C06-2|C06-2]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C06-X1|C06-X1]])
- [signal] Treat long and short symmetrically, but override the model to stop adding to shorts near a price floor (California carbon auction floor).. Why: Floor caps downside trend. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C06-3|C06-3]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C06-X1|C06-X1]])
- [sizing] Position proportional to signal strength (several trend horizons) and inversely proportional to volatility; largest position set so it can be exited in about a week in stress; new markets start small until real fills confirm costs.. Why: Liquidity and diversification determine top-line capacity. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C07-1|C07-1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C10-X1|C10-X1]])
- [risk] Soft-close capacity (half-closed around 1bn; top line a couple of billion), leaving headroom after a 15-20% year.. Why: Multi-year trend horizon; protect existing clients. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C03-1|C03-1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C03-2|C03-2]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C03-X1|C03-X1]])
- [execution] Give the desk a tracking-error budget to work orders passively over several days within bounds; never trade against the model or on own views; fall back to normal trading when the limit is hit.. Why: Avoid crossing the spread, anti-correlated buffer, faster signals possible. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C09-1|C09-1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C09-2|C09-2]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C09-3|C09-3]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C10-1|C10-1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C10-2|C10-2]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C11-X1|C11-X1]])
- [execution] Use a wide network of specialist brokers and dealers by phone quotes; onboard new brokers when adding markets; access Chinese futures via swaps with margin held by a third party; all others are exchange-cleared futures.. Why: Niche markets cannot be plugged electronically; competition on pricing. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C07-2|C07-2]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C08-1|C08-1]])
- [portfolio] Position the program as a diversifying addition (20-25% correlation to the SG CTA index) beside cheap liquid core trend, not as the equity-shock convexity core.. Why: Core trend with equity-shock convexity should come from cheap liquid trend. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C11-1|C11-1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C12-X3|C12-X3]])

**Evidence style:** Structural first principles and market microstructure (who trades, where on the curve), supported by internal papers (drift/autocorrelation, Eras Tour, The Waiting Game) and a year of live execution results; explicitly rejects backtest Sharpe as a selection criterion. Examples are single cases (EU carbon, cocoa, propane).

**Views at the time**
- (2026-04) Alternative-commodity trend has been through a multi-year drawdown, which he attributes to sampling the weaker side of a long-run positive Sharpe distribution.. Reasoning: Structural logic (inelastic supply, concrete diversification) lets investors hold through it. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C12-X1|C12-X1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C12-1|C12-1]])
- (2025-04 (recounted 2026-04)) The book was up in April 2025 around the Liberation Day shock, confirming that niche commodities follow their own drivers rather than risk-on/risk-off.. Reasoning: Insulation from the financial risk factor. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C10-X1|C10-X1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C10-3|C10-3]])
- (2026-04) Macro themes the book taps through capacity discipline: biofuels and green transition, uranium for AI data-centre power, freight routes and onshoring, tariff wars.. Reasoning: Different regions' supply, demand and logistics are diverging. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C03-X2|C03-X2]])
- (2026-04) Cocoa 2024 was the biggest commodity trend after 20 years without a trend, yet too financialized to trade.. Reasoning: Illustrates trend appearing without prior history and the financialization screen. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C01-1|C01-1]])

### Disagreements
- **Is waiting-desk execution discretionary?**: Moritz Seibert (host): It is fair to summarise the setup as a systematic engine with a discretionary alpha generator in execution. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C11-R1|C11-R1]]); Tom Babbage: Not discretionary: the desk never trades against the model or on its own views, only times within bounds, and the rule could be written as an execution algorithm. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C11-X1|C11-X1]])
- **More markets as the route to diversification**: Quant-finance convention (as described by Babbage): Free lunch is diversification: if you have 100 markets try 200, then 400. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C02-R1|C02-R1]]); Tom Babbage: Beyond a few hundred markets another changes nothing; what matters is real independence and capacity discipline. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C02-1|C02-1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C03-1|C03-1]])

### Gaps and conflicts
- Claims of better drift and autocorrelation in alternative commodities rest on an internal paper; no magnitudes or out-of-sample test are given, and the market classification was made by the firm (selection risk). ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C05-1|C05-1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C04-4|C04-4]])
- Argues backtest-based market selection is data mining, but market selection by 'alternativeness' also uses long history to document the drift and autocorrelation gap; EU carbon is a single post-hoc success example. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C04-2|C04-2]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C06-2|C06-2]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C05-1|C05-1]])
- Reports near-zero slippage over just over one year, with admitted higher slippage variance and anecdotal propane evidence; the gain relative to prior years is not quantified and may be luck or regime. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C09-3|C09-3]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C10-2|C10-2]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C10-3|C10-3]])
- Says a 10bn book would look like a standard commodity allocation while also saying 4-5bn capacity was possible on paper during COVID; the capacity ceiling depends on volatility and prices and is judgemental. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C03-X1|C03-X1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C03-X2|C03-X2]])
- Avoids cocoa as too financialized despite the biggest commodity trend in 2024, which tests the financialization screen against its opportunity cost. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C01-1|C01-1]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C04-4|C04-4]])
- Inflation convexity claim relies on a firm paper; the instruments and period of the 60/40 test are not described. ([[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C12-2|C12-2]], [[MT175 - The Overlooked Markets Creating Better Trend Opportunities - Open Interest - Ep.21#^MT175-C12-X2|C12-X2]])

### Forward-looking inputs (reader synthesis)
(reader) Inputs named that lead future trend opportunities: speculator participation in a market (COT, share of open interest delivered, entry of other CTAs), position on the curve (deferred contracts), supply inelasticity, physical clusters (furnace chain), structural themes (biofuels, uranium, freight, onshoring, tariffs) and regime of high commodity volatility (raises dollar-risk capacity). Horizon is multi-year; he does not offer a price forecast.

### Reader inferences (not stated by the speakers)
- (reader) The financialization screen implies that alternative-market edge decays as more CTAs enter, so Babbage's own program is exposed to crowding of the markets he identifies as alternative.
- (reader) Capacity measured in dollar risk means that the same assets under management can be fully invested or oversized depending on the commodity volatility regime; a model of CTA capacity should include volatility.
- (reader) Passive execution converts part of the execution budget into an implicit short-horizon mean-reversion position, which is why he can speak of raising the risk scale; the same logic would fail in trending, gapping markets.
- (reader) The claim that commodity trend is convex to both inflation and deflation is an interpretation of goods prices as commodity prices and is testable against CPI components.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | teaser, intro and guest background |
| C02 | 2 | why commodities only, diversification and financialization |
| C03 | 2 | capacity discipline, factor diversity, capacity numbers |
| C04 | 4 | market turnover and selection criteria |
| C05 | 2 | alternativeness metrics, speculators, trend quality vs quantity, curve position |
| C06 | 3 | inelastic supply, carbon examples, long/short symmetry |
| C07 | 2 | risk allocation, liquidity limits, broker network |
| C08 | 3 | clearing and swaps, execution costs and variance |
| C09 | 3 | discretionary-looking execution risk budget, passive fills |
| C10 | 3 | anti-correlated execution, vol-scaled positions, unfilled orders |
| C11 | 1 | liberation day, execution is systematic, client positioning |
| C12 | 2 | why clients allocate, inflation convexity |
| C13 | 0 | sign-off |

## Claims

### C01
- **Tom Babbage** Cocoa in 2024 delivered the biggest commodity trend after twenty years without one, but Gresham avoids it as too financialized, illustrating that trend can appear in markets without a prior trend record.  #mech/structural_shift _(time-bound view)_
  > after 20 years of no trend that was probably the biggest commodity trend there was
  indicator: cocoa price trend · asset: commodities · horizon: years · testable: no - anecdote · confidence: medium
  ^MT175-C01-1

### C02
- **Tom Babbage** Beyond a few hundred markets, adding another changes nothing because allocation to it is tiny and the effective degrees of freedom matter more than the count (2-, 5- and 10-year Treasuries are essentially one market).  #mech/risk_management
  > One is just incrementally adding one market to your, you know, your 301st market really makes no difference to diversification.
  indicator: number of independent markets · asset: multi · testable: yes - effective-N or marginal Sharpe tests · confidence: high
  ^MT175-C02-1
- **Tom Babbage** Financialized markets (FX, indices, fixed income) collapse to one in macro shocks, while less financialized commodities with structural differences stay resilient and diversifying.  #mech/structural_shift
  > you're kind of side-stepping that whole collapse to one effect.
  indicator: cross-market correlation in risk-on/risk-off shocks · asset: commodities · direction: include alternative commodities · conditions: Macro shock regimes · testable: yes - conditional correlation tests · confidence: high
  ^MT175-C02-2
- **Tom Babbage** Judge diversification by fundamental independence (different regions, consumers, producers, logistics) rather than by correlations measured over short windows: South African sunflower seeds, US East Coast power and Chinese bitumen are different markets whatever a one- or two-month correlation says.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > Maybe in a month or two period you might mathematically measure a high correlation or a low correlation. I almost that almost doesn't matter because you know fundamentally they're entirely different
  indicator: structural independence of commodity markets versus short-window measured correlation · asset: commodities · conditions: Holds for physically distinct commodities; financialized markets collapse to one in macro shocks · testable: partly - correlation stability in stress for structurally distinct versus financial markets can be tested · confidence: high
  ^MT175-C02-X1
- **Tom Babbage** Babbage describes the quant-finance convention that the only free lunch is diversification, so a manager with 100 markets should try 200 and then 400 in an arms race on market-list length.  #mech/new _(added by map cross-check)_
  > the only free lunch is diversification. If you've got 100
  indicator: number of markets traded · asset: multi · conditions: industry convention · testable: no - convention · confidence: medium
  ^MT175-C02-R1

### C03
- **Tom Babbage** Alternative commodity diversification requires capacity discipline: with billions, allocation concentrates in crude, gold and gas so niche markets matter little. Gresham sees capacity around 1-2bn and soft-closed at about 1bn (half closed during COVID's high commodity volatility).  #mech/risk_management
  > unless you have a real strong capacity discipline, your portfolio won't look diversified.
  indicator: capacity · asset: commodities · horizon: years · conditions: Small AUM relative to market liquidity · testable: yes · confidence: high
  ^MT175-C03-1
- **Tom Babbage** Trend investors need a horizon of several years, so leave headroom so existing clients can benefit from organic growth instead of closing after a 15-20% year.  #mech/risk_management
  > the investment horizon that we think is is relevant for a trend strategy is not months or even a year, it's several years.
  indicator: investment horizon for trend · asset: multi · horizon: years · testable: no · confidence: medium
  ^MT175-C03-2
- **Tom Babbage** Capacity in commodity trend is measured in units of dollar risk, so it expands when prices and volatility are high (during COVID paper capacity was 4-5bn); Gresham did not assume that level would persist, so it half-closed at about 1bn and sets top-line capacity around a couple of billion through the cycle.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > On paper, capacity in our markets could have been 4 5 billion and it wouldn't have compromised diversification.
  indicator: dollar risk capacity versus commodity price level and volatility · asset: commodities · horizon: years · conditions: Capacity set on through-the-cycle volatility, not peak volatility · testable: yes - capacity estimates scale with price and vol levels · confidence: high
  ^MT175-C03-X1
- **Tom Babbage** With capacity discipline an alternative-commodity book taps distinct macro risk factors (biofuels and the green transition, uranium and nuclear power for AI data centres, freight routes and onshoring, tariff wars), whereas a manager with about 10bn would look like a standard commodity allocation inside a broader portfolio.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > you're tapping into the green transition, you're tapping into um, nuclear power resurgence and how you power AI data centers
  indicator: biofuels, uranium, freight routes · asset: commodities · horizon: years · conditions: Requires small enough assets to give niche markets meaningful weight · testable: no - qualitative thematic exposure argument · confidence: high
  ^MT175-C03-X2

### C04
- **Tom Babbage** Gresham trades about 150 markets and turned over roughly a quarter of the list in 2025 (44 dropped, 31 added), selecting on market structure rather than backtests.  #mech/research_method _(time-bound view)_
  > last year we dropped 44 markets and we added 31.
  indicator: market list turnover · asset: commodities · horizon: years · testable: no · confidence: high
  ^MT175-C04-1
- **Tom Babbage** Choosing markets by backtest Sharpe is data mining and 'the key to future misery'; instead evaluate who trades the market, where on the curve, and its correlation to mainstream commodities.  #mech/research_method
  > So, the first thing I would say it's not based on the back test, right?
  indicator: market selection criteria · asset: commodities · testable: yes · confidence: high
  ^MT175-C04-2
- **Tom Babbage** 'Alternativeness' means low correlation to mainstream commodities (for example the Bloomberg Commodity Index), not low liquidity or barriers to entry; a low-liquidity oil spread correlated with crude is just costly crude exposure.  #mech/research_method
  > you know, if there's an expensive oil spread that looks alternative from a low liquidity perspective, that that's not interesting to us if it's going to be highly correlated to mainstream crude.
  indicator: correlation to Bloomberg Commodity Index · asset: commodities · direction: include low-correlation alternative commodities · testable: yes · confidence: high
  ^MT175-C04-3
- **Tom Babbage** Speculator participation (Commitments of Traders, share of open interest going to delivery vs recycled, broker queries, conference attendance) identifies alternative markets; when CTAs enter, the market is becoming financialized and less interesting.  #mech/crowding_positioning
  > For us it's how many speculators are in this market? So, you can look at commit to the trader data.
  indicator: COT data; open interest to delivery · asset: commodities · direction: avoid markets crowded with speculators · testable: yes · confidence: high
  ^MT175-C04-4
- **Tom Babbage** Group markets into clusters by shared physical drivers (a 'furnace' cluster of iron ore, flat glass and coking coal), so correlation and risk are managed through real supply-chain linkages rather than only statistical estimates.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > iron ore would cluster somewhat with things like flat glass panels and and coking coal. And that's because they're all kind of related to this sort of furnace concept
  indicator: physical linkage clusters among commodity markets · asset: commodities · conditions: Cluster membership is judged from the physical process · testable: partly - cluster correlations can be checked against the fundamental grouping · confidence: medium
  ^MT175-C04-X1

### C05
- **Tom Babbage** Trend splits into drift (quantity) and autocorrelation (quality); both are better in alternative commodities than mainstream ones over 30 years, linked to low speculative activity.  #mech/slow_reaction
  > There's a drift component, which I'd call kind of like the quantity of trend, how far a market moves. And there's an auto correlation component, which I would label as the quality of the trend.
  indicator: trend drift and return autocorrelation · asset: commodities · direction: favour alternative commodity trend · horizon: years · conditions: Persistent over decades · testable: yes - published decomposition · confidence: high
  ^MT175-C05-1
- **Tom Babbage** Further along a commodity curve (about 5 years out) hedgers dominate, giving smoother, higher-autocorrelation trends than the noisy speculative front; trading deferred contracts improves trend quality.  #mech/slow_reaction
  > the front of that curve is a financialized speculator dominated kind of noise news driven market.
  indicator: curve position of trend (front vs far) · asset: commodities · direction: trade further out the curve · horizon: years · testable: yes · confidence: high
  ^MT175-C05-2

### C06
- **Tom Babbage** Inelastic supply (coal mines take decades to permit and keep running at a loss) and demand, plus shipping and storage frictions, mean imbalances clear only through large persistent price moves, a structural reason for trends in commodities.  #mech/slow_reaction
  > there's an inelasticity in these sort of markets between supply and demand.
  indicator: supply elasticity in niche commodities · asset: commodities · direction: trend following in inelastic commodities · horizon: years · testable: partly - elasticity proxies could be used · confidence: high
  ^MT175-C06-1
- **Tom Babbage** European carbon had negative trend Sharpe over its 8 years of history in 2016 but was added on structural criteria and became one of the best performers, an example of selecting on structure not backtest.  #mech/research_method
  > we were looking at European carbon, which is at the time really the only carbon market around with any liquidity.
  indicator: EU carbon trend · asset: commodities · horizon: years · testable: no - single example · confidence: medium
  ^MT175-C06-2
- **Tom Babbage** In markets with a price floor (California carbon auction floor) the short trend is capped, so the model must be overridden to prevent adding to shorts near the floor.  #mech/risk_management
  > Californian carbon scheme, there's an effective auction floor price each set each year.
  indicator: Californian carbon futures vs auction floor · asset: commodities · horizon: weeks · conditions: Near administrative floor prices · testable: yes · confidence: high
  ^MT175-C06-3
- **Tom Babbage** Long and short positions are treated symmetrically in futures, with real-world boundary exceptions: Gresham avoids the front of the oil curve (prices went negative in COVID) and overrides shorts near price floors.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > In terms of longs and shorts in in futures land, yeah, we would view that as a symmetric problem.
  indicator: price floors; front-month oil contract · asset: commodities · direction: long and short symmetric except at boundaries · conditions: Boundary cases arise in markets with floors or physical constraints · testable: yes - compare long and short trend performance and boundary episodes · confidence: high
  ^MT175-C06-X1

### C07
- **Tom Babbage** Position limits are set so the largest position can be exited in about a week in stress; liquidity plus diversification determine top-line capacity, and new markets start with small weights until real fills confirm costs.  #mech/risk_management
  > we want to be able to get out of a max conviction long or short within, say, a week or so in a stress scenario.
  indicator: liquidity-based position limit · asset: commodities · direction: small initial weights in new markets · horizon: weeks · testable: yes · confidence: high
  ^MT175-C07-1
- **Tom Babbage** Niche commodity execution relies on a wide network of specialist brokers and dealers via phone quotes, which creates price competition and requires onboarding brokers when adding markets.  #mech/liquidity_flows
  > you cannot plug a computer into the exchange and just electronically trade. You have to do it through getting quotes
  indicator: execution via broker network · asset: commodities · testable: no · confidence: high
  ^MT175-C07-2

### C08
- **Tom Babbage** Chinese commodity futures are accessed through swaps with margin held by a third party to limit counterparty risk; all other markets are exchange-cleared futures.  #mech/risk_management
  > Chinese commodity futures, we do via swap, but that that money is all kept offshore.
  indicator: swap counterparty exposure · asset: commodities · testable: no · confidence: high
  ^MT175-C08-1
- **Tom Babbage** Large CTAs lose roughly 0.7-1% a year to slippage, and splitting orders across the day benchmarks well against TWAP/VWAP but hides the autocorrelated cost.  #mech/risk_management
  > a typical liquid CTA, maybe they're spending, I don't know, say, 70 basis points a year. Maybe maybe even a percent on on slippage transaction costs.
  indicator: slippage cost per year · asset: multi · horizon: years · conditions: Multi-billion CTA scale · testable: yes · confidence: medium
  ^MT175-C08-2
- **Tom Babbage** At 15% annual risk (about 1% daily variance), trades account for only about 5% of daily variance and are uncorrelated across markets, so execution risk is a small fraction of portfolio risk.  #mech/risk_management
  > nearly all of that is just the positions you're holding. It's not the trades you're doing on a day
  indicator: share of daily variance from trading · asset: multi · horizon: days · testable: yes - variance decomposition · confidence: high
  ^MT175-C08-3

### C09
- **Tom Babbage** Gresham gives the trading desk a risk budget (tracking error to model) and lets it work orders passively over several days with bounds, so the desk acts as an anti-correlated buffer and trend signals can be faster for the same cost.  #mech/risk_management
  > we're going to give the desk a higher level of effective risk allocation, if you like.
  indicator: execution desk tracking-error budget · asset: commodities · horizon: days · conditions: Needs risk controls on tracking · testable: yes - slippage with and without patience · confidence: high
  ^MT175-C09-1
- **Tom Babbage** Faster signals look better before costs, but patient passive execution (avoiding crossing the spread, which in freight can be 100bp) preserves them after costs.  #mech/risk_management
  > normally fast signals are better before cost, right?
  indicator: bid-offer spread; passive fills · asset: commodities · direction: passive limit orders in wide-spread markets · horizon: days · conditions: Largest benefit in wide-spread markets such as freight · testable: yes · confidence: high
  ^MT175-C09-2
- **Tom Babbage** Passive execution cut slippage close to zero over the first year, partly via invisible savings when the model changes its target before the order is done.  #mech/risk_management _(time-bound view)_
  > Our slippage bill last year was effectively close to zero compared to previous years in in a relative sense.
  indicator: realized slippage · asset: commodities · horizon: years · conditions: 2025, one year of evidence · testable: yes · confidence: medium
  **Correction (cross-check):** Babbage qualifies the result: slippage was 'effectively close to zero compared to previous years in a relative sense' after running the method for just over a year, not zero in absolute terms; he also notes the approach was first used on the sister financial-instruments strategy several years earlier with great success and rolled out to the alternative commodity program at the start of last year. → After just over a year of passive, risk-budgeted execution, last year's slippage bill was much lower than in earlier years ('effectively close to zero' in a relative sense), helped by not crossing the spread and by invisible savings when the model changes its target before the order is done; the method was proven first on the sister financial strategy and rolled out to AQA at the start of last year.
  ^MT175-C09-3

### C10
- **Tom Babbage** Passive waiting behaves as an anti-trend (mean-reverting) component, adding diversification so the strategy risk scale can be raised.  #mech/risk_management
  > You can kind of view it as the trading desk being an anti-correlated strategy to trend.
  indicator: execution as anti-correlated return stream · asset: commodities · horizon: days · testable: yes · confidence: medium
  ^MT175-C10-1
- **Tom Babbage** If the market moves away, the unfilled trade accumulates tracking variance until the limit forces a trade, so slippage variance rises while the average cost falls; market near 50/50 each day gives savings about half the time.  #mech/risk_management
  > So, yes, it went from 100 lots, nothing was done, and 120 lots, nothing was done.
  indicator: unfilled order tracking error · asset: commodities · horizon: days · conditions: Bounded risk allocation · testable: yes · confidence: high
  ^MT175-C10-2
- **Tom Babbage** In April 2025 big propane moves, the passive method of cutting positions saved slippage versus an aggressive exit that would have hit a move-away-and-back.  #mech/risk_management _(time-bound view)_
  > liberation day wasn't really an event.
  indicator: propane April 2025 · asset: commodities · horizon: days · conditions: Anecdotal · testable: no - anecdote · confidence: low
  ^MT175-C10-3
- **Tom Babbage** Alternative-commodity trend was insulated from the April 2025 Liberation Day macro shock: the book was up for the month, consistent with niche commodities following their own supply-demand drivers rather than the financial risk-on/risk-off factor.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > for us liberation day wasn't really an event. Um we were up up for the month
  indicator: Gresham AQA return, April 2025 · asset: commodities · horizon: months · conditions: One episode; very large propane moves occurred in the same month · testable: yes - compare alternative-commodity trend with equity-shock months · confidence: medium
  ^MT175-C10-X1

### C11
- **Tom Babbage** Core trend with equity-shock convexity should come from cheap liquid trend; alternative-commodity trend is a diversifying addition with only 20-25% correlation to the SG CTA index.  #mech/risk_premium
  > You should go and find a cheap management fee only liquid trend that will go up when stock markets go down and won't cost you much, right?
  indicator: correlation to SG CTA Index · asset: multi · direction: add alternative commodity trend as a satellite · horizon: years · testable: yes · confidence: high
  ^MT175-C11-1
- **Tom Babbage** The budgeted, passive execution is not discretionary alpha: the desk never trades against the model or on its own views, it only chooses timing within bounds as the market moves towards or away, and the rule could be written as an execution algorithm.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > it's not really discretionary in in what I would call a capital D. It's it's still part of our systematic framework
  indicator: tracking error of executed positions versus model positions · asset: commodities · horizon: days · conditions: Requires clear controls and monitoring of how long the desk may wait · testable: yes - the passive rule can be coded and simulated · confidence: high
  ^MT175-C11-X1
- **Moritz Seibert** Host Moritz Seibert suggests the setup is a systematic trade engine with a non-systematic discretionary alpha generator in execution.  #mech/new _(added by map cross-check)_
  > Probably fair to summarize this as you you have the systematic trade engine and then a non-systematic discretionary alpha generator
  indicator: execution desk discretion · asset: commodities · conditions: Gresham passive execution · testable: no - characterisation · confidence: medium
  ^MT175-C11-R1

### C12
- **Tom Babbage** Signals with clear structural drivers (inelastic commodity supply) let investors keep faith through multi-year drawdowns, whereas opaque machine-learning signals get pulled after three years of weak results.  #mech/behavioral
  > it shortcuts a lot of the kind of faith aspect you almost have to put into any any system or any signal
  indicator: structural rationale vs opaque signal · asset: commodities · horizon: years · testable: no · confidence: high
  ^MT175-C12-1
- **Tom Babbage** Commodity trend protects a 60/40 portfolio in rising, high and low inflation periods, so adding even basic commodity trend improves results across inflation regimes (the 'Eras Tour' paper).  #mech/risk_management
  > there's a very strong and clear positive convexity for commodity trend and inflation and deflation.
  indicator: commodity trend returns vs inflation regime · asset: commodities · direction: add commodity trend to 60/40 · horizon: years · conditions: Inflation regimes · testable: yes · confidence: high
  ^MT175-C12-2
- **Tom Babbage** Alternative-commodity trend has just been through a drawdown lasting several years (as of April 2026); Babbage says the pain of trend is a modest Sharpe with long drawdowns and that structural logic is what lets investors hold through them.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > certainly, you know, recently we've been in a in a drawdown of several years.
  indicator: Gresham AQA multi-year drawdown · asset: commodities · horizon: years · conditions: Self-reported by the manager; depth and length not given · testable: partly - needs the program's return series · confidence: medium
  ^MT175-C12-X1
- **Tom Babbage** Why commodity trend hedges inflation: inflation is measured as goods prices and goods are commodities, so commodity prices and inflation are two sides of the same coin, which gives commodity trend positive convexity to both inflation and deflation regimes.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > when you measure inflation, you're measuring prices of goods and goods are commodities.
  indicator: CPI goods component versus commodity trend returns · asset: commodities · direction: commodity trend gains when inflation rises, falls sharply, or is high · horizon: years · conditions: Mechanism is a stylised argument; the Eras Tour paper provides the empirical test · testable: yes - trend returns conditional on inflation regime · confidence: high
  ^MT175-C12-X2
- **Tom Babbage** Many allocators already hold an alternative-markets CTA but find the commodity share underweighted because of capacity limits, so a commodity-only program is bought as a top-up to that sleeve.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check, time-bound view)_
  > they kind of feel that the commodity aspect is underweighted and that might be because of a capacity question around how much
  indicator: allocator commodity-trend weight within alternative-markets CTA allocation · asset: commodities · direction: demand for commodity-only trend · horizon: years · conditions: Manager's account of client conversations · testable: no - anecdotal client behaviour · confidence: medium
  ^MT175-C12-X3

