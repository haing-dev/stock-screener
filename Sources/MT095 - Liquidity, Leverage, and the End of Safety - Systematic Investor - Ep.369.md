---
source_id: MT095
title: "Liquidity, Leverage, and the End of Safety - Systematic Investor - Ep.369"
date: 2025-10-18
channel: "Top Traders Unplugged"
url: 
words: 12669
claims: 63
added_by_crosscheck: 13
corrections: 1
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Mark Rzepczynski (co-host, transcript spelling Mark Ramsinski)", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Liquidity, Leverage, and the End of Safety - Systematic Investor - Ep.369

**Speakers:** Mark Rzepczynski (co-host, transcript spelling Mark Ramsinski); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** Systematic Investor episode on gold and the changing meaning of safe assets, Fed operating targets, retail and inelastic markets, First Brands trade finance, CTA performance and market impact, and a network view of markets. Conclusion: safety is relative, flows move prices, and CTA footprint and execution are the key constraints.

**Approach:** trend following, CTA, gold, market microstructure, complex systems

**Cross-check completeness estimate of first read:** 0.85 - first reader (66 claims) captured the main arguments on gold, safe assets, Fed plumbing, inelastic markets, CTA market impact and network ideas; misses are supporting reasoning steps, a speaker disagreement on trend speed, and some data points.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | intro; safe asset question |
| C02 | 4 | gold: central banks, COT positioning, safety, history |
| C03 | 4 | gold fundamentals unstable; structural changes |
| C04 | 3 | ETFs anecdote; metals rally, spillover to satellites |
| C05 | 3 | safe strategies, good-friend analogy, Logan speech |
| C06 | 2 | Fed operating target and repo |
| C07 | 1 | SEP dispersion, IMF survey |
| C08 | 3 | fiscal literacy survey, retail options, noise |
| C09 | 3 | prediction markets, inelastic markets |
| C10 | 3 | composition and flows; First Brands trade finance |
| C11 | 3 | trade finance collateral, futures MTM, Q4 |
| C12 | 2 | gold September, CTA/market numbers |
| C13 | 4 | Quantica alternative vs core markets, market impact |
| C14 | 3 | market footprint, CTA trackers |
| C15 | 3 | CTA flow data, execution |
| C16 | 4 | trend speed, diversification, causal inference |
| C17 | 3 | network of markets, pushback |
| C18 | 1 | cointegration, causal optimisation, sign-off |
| C19 | 0 | disclaimer only |

## Claims

### C01
- **Mark Rzepczynski** Safe-asset status is relative and changing: French, UK and even US Treasury debt (shutdown, high debt/GDP) are no longer clearly safe, which is relevant to gold at $4,000.  #mech/structural_shift _(time-bound view)_
  > in some sense there's no such thing as an absolute safe asset. It's all relative.
  indicator: sovereign debt safety · asset: rates · direction: safe-asset premium shifting away from sovereigns · horizon: years · testable: no: conceptual · confidence: medium
  ^MT095-C01-1

### C02
- **Mark Rzepczynski** Central banks are buying gold to diversify reserves out of traditional safe assets, the reverse of their 1990s gold selling.  #mech/liquidity_flows _(time-bound view)_
  > They're actually buying up a lot of gold right now to increase their reserves in their in their foreign uh uh foreign currency reserves.
  indicator: central bank gold purchases · asset: commodities · direction: gold up · horizon: years · conditions: Price-insensitive official buying · testable: yes: central bank gold reserve data · confidence: high
  ^MT095-C02-1
- **Mark Rzepczynski** Large speculators' gold longs in the CFTC commitment of traders have been declining, so the rally is not driven by large speculative excess.  #mech/crowding_positioning _(time-bound view)_
  > this speculative exposure in the commodity uh commitment of traders from large speculators their long positions have actually been declining over this period
  indicator: CFTC COT large speculator gold longs · asset: commodities · horizon: months · testable: yes: COT data · confidence: high
  ^MT095-C02-2
- **Mark Rzepczynski** Gold behaves like a safe asset: uncorrelated with risk assets, better in crises, an inflation hedge and as liquid as Treasuries at times.  #mech/risk_management
  > it's uncorrelated with risky assets and you know that does better in a crisis to some degree
  indicator: gold correlation to risk assets · asset: commodities · direction: gold up in crises · testable: yes: correlation and crisis returns · confidence: medium
  ^MT095-C02-3
- **Niels Kaastrup-Larsen** Past gold rallies (1978-80, 2007-11) were followed by large drawdowns (to about 500 after the 1970s peak), the latter coinciding with central bank selling.  #mech/overshoot
  > which is of course around the time when the central banks were selling gold interestingly enough
  indicator: gold price history · asset: commodities · direction: gold down after surges · horizon: years · testable: yes: gold price history · confidence: medium
  **Correction (cross-check):** Wrong chronology: central-bank selling coincided with the fall of gold to about 500 after the 1970s peak (the 1990s sales Mark mentioned), not with the decline after 2011; Niels's price levels (600 to 3,500, 2,500-2,600 at the GFC) are loosely recalled and do not match nominal prices. → Niels notes three gold rallies (1978-80, GFC to about 2011, and now); after the 1970s surge prices fell sharply to roughly 500, around the time central banks were selling gold, and after the GFC-era peak they fell again less dramatically; his price levels are approximate or recalled loosely.
  ^MT095-C02-4
- **Mark Rzepczynski** The 2025 gold rally cannot be explained by inflation, which is lower than two years earlier, so central-bank reserve diversification away from traditional safe assets is the better explanation than inflation hedging or speculation.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > gold shouldn't be going up because inflation seems to be uh tamed relative to what it was two years ago
  indicator: gold versus inflation · asset: commodities · direction: gold up despite lower inflation · horizon: years · conditions: Reserve diversification demand · testable: partly - compare gold with inflation and central-bank purchases · confidence: medium
  ^MT095-C02-X1

### C03
- **Mark Rzepczynski** Gold's fundamentals are unstable: real rates, inflation and uncertainty (VIX) each link to gold only loosely and the drivers are in flux.  #mech/structural_shift
  > you expect if real rates are higher gold price should should go down. Okay that works sometimes but not always.
  indicator: real rates, inflation, VIX vs gold · asset: commodities · direction: gold vs real rates inverse (unreliable) · horizon: years · testable: yes: regression of gold on real rates · confidence: medium
  ^MT095-C03-1
- **Mark Rzepczynski** A 20% move in a couple of weeks is abnormal, but whether it is a bubble or a new era is hard to call.  #mech/overshoot _(time-bound view)_
  > You know, 20% move in in let's say last couple of weeks is seems truly abnormal.
  indicator: gold price · asset: commodities · horizon: weeks · testable: partly: historical analogs · confidence: medium
  ^MT095-C03-2
- **Mark Rzepczynski** Structural changes in gold: price-insensitive central bank buyers; geopolitical buyers (Russia, China) who cannot hold Treasuries at the New York Fed.  #mech/liquidity_flows
  > central banks are are are are sort of not price sensitive
  indicator: central bank demand · asset: commodities · direction: gold up · horizon: years · conditions: Geopolitical divide · testable: yes · confidence: high
  ^MT095-C03-3
- **Mark Rzepczynski** Gold ETFs and CME acceptance of gold as margin collateral financialize gold and give it safe-asset characteristics.  #mech/structural_shift
  > you can use that as as collateral, which is key to being a safe asset
  indicator: gold ETF assets, collateral eligibility · asset: commodities · direction: gold demand up · horizon: years · testable: yes · confidence: medium
  ^MT095-C03-4

### C04
- **Niels Kaastrup-Larsen** Gold up 46% in 2025 alongside platinum 77%, palladium 63%, silver 59% and copper 22%, raising the question of a broader metals or commodity super cycle.  #mech/slow_reaction _(time-bound view)_
  > Then you look at platinum up 77%. Palladium up 63%. Silver up 59%.
  indicator: metals YTD returns · asset: commodities · direction: long metals · horizon: months · testable: yes: price data · confidence: high
  ^MT095-C04-1
- **Mark Rzepczynski** Markets form a network where a shock in a core market (gold) pulls satellites (platinum, palladium, silver) via substitution.  #mech/liquidity_flows
  > you could have one is your core market and then you have satellites around the core that that get pulled along by the behavior of one
  indicator: gold-silver-platinum co-movement · asset: commodities · direction: satellites follow core · horizon: weeks · testable: yes: lead-lag tests · confidence: medium
  ^MT095-C04-2
- **Mark Rzepczynski** Spillovers are larger in less liquid satellite markets because flows matter more when trading volume is low.  #mech/liquidity_flows
  > if those other markets are less liquid the pull effect could be much greater
  indicator: market liquidity · asset: commodities · direction: larger moves in illiquid markets · horizon: weeks · conditions: Thin volume · testable: yes · confidence: medium
  ^MT095-C04-3

### C05
- **Niels Kaastrup-Larsen** Safety may come from strategies that are adaptive, diversified and liquid (trend following) rather than from long-only safe assets.  #mech/risk_management
  > instead of safe assets, should we think about safe strategies
  asset: multi · conditions: Admitted bias as a trend follower · testable: partly: crisis performance · confidence: medium
  ^MT095-C05-1
- **Mark Rzepczynski** Safe assets can be fickle like friends, so diversify across multiple safe assets and strategies.  #mech/risk_management
  > a safe asset is like a good friend. They're going to be there when you need them.
  asset: multi · testable: no: analogy · confidence: medium
  ^MT095-C05-2
- **Mark Rzepczynski** Dallas Fed's Logan says the Fed needs a new operating target beyond Fed funds because ample reserves mean the market has shrunk and no longer represents money market rates.  #mech/policy_reaction _(time-bound view)_
  > we're probably going to be in need for new operating targets beyond Fed funds
  indicator: Fed funds, SOFR, tri-party repo · asset: rates · horizon: years · conditions: Ample reserves regime · testable: yes: volumes observable · confidence: medium
  ^MT095-C05-3
- **Niels Kaastrup-Larsen** Uncertainty about Fed independence is one of the reasons offered for the gold rally, by lowering confidence in dollar and Treasury safety.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > why some people say gold is going up is for example the uncertainty about you know Fed independence
  indicator: Fed independence uncertainty · asset: commodities · direction: gold up · horizon: months · conditions: Fed credibility questioned · testable: no - qualitative · confidence: medium
  ^MT095-C05-X1

### C06
- **Mark Rzepczynski** The Fed funds market trades only about 100bn a day while tri-party repo trades in trillions, so repo or SOFR is a candidate target.  #mech/policy_reaction
  > it only trades about hundred billion dollars, you know, a day and it doesn't represent the true money market rates that people are paying
  indicator: Fed funds volume vs tri-party repo volume · asset: rates · horizon: years · testable: yes · confidence: medium
  ^MT095-C06-1
- **Mark Rzepczynski** A repo-based target is more volatile but deeper and clearer, so it should reduce uncertainty; the target drives margin and collateral costs across markets.  #mech/policy_reaction
  > the uh triparty repo is is probably more volatile than uh than Fed funds rate
  indicator: tri-party repo volatility · asset: rates · horizon: years · testable: yes · confidence: medium
  ^MT095-C06-2
- **Mark Rzepczynski** With ample reserves and interest paid on reserves, banks no longer need to borrow reserves, so the Fed funds market has shrunk to foreign-bank buyers and Federal Home Loan Bank providers and no longer represents true money-market funding rates.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > they get paid interest on their reserves that they hold in the Fed
  indicator: Fed funds volume; interest on reserves · asset: rates · horizon: years · conditions: Ample-reserve regime · testable: yes - volumes and rates are observable · confidence: high
  ^MT095-C06-X1

### C07
- **Mark Rzepczynski** The September SEP dots were dispersed, showing the Fed has no clear view, which raises buyer-seller disagreement and trading volume.  #mech/behavioral _(time-bound view)_
  > the Fed forecast of what interest rates are going to be over the next year are all over the map
  indicator: FOMC SEP dispersion · asset: rates · direction: volume and volatility up · horizon: months · conditions: When projections are widely dispersed · testable: yes: dot dispersion vs volume · confidence: medium
  ^MT095-C07-1

### C08
- **Mark Rzepczynski** An IMF survey of 27,000 respondents found just over half knew that higher spending raises deficits, so public ignorance of fiscal links raises credit-crisis risk.  #mech/fiscal_debt
  > just over 50% of the people got this right
  indicator: IMF perceptions of public debt survey · asset: credit · direction: credit crisis risk up · horizon: years · testable: yes: survey results · confidence: medium
  ^MT095-C08-1
- **Mark Rzepczynski** Very short-dated option volume rose from about 20 million to over 60 million contracts per day and ETF flows are large and can reverse quickly, adding market impact.  #mech/liquidity_flows _(time-bound view)_
  > before 2020 there was daily volume of about you know 20 million contracts. Now it's it's it's well over 60 plus uh million
  indicator: short-dated option volume, ETF flows · asset: equities · direction: flow-driven volatility · horizon: years · conditions: Retail-driven flow · testable: yes: OCC volume · confidence: high
  ^MT095-C08-2
- **Mark Rzepczynski** More retail (noise trader) activity distorts price signals, so models relying on price must adjust.  #mech/research_method
  > if you use prices as signals of value, but if noise increases, then those signals are going to get distorted
  indicator: retail noise · asset: equities · horizon: years · testable: partly: noise measures · confidence: medium
  ^MT095-C08-3

### C09
- **Mark Rzepczynski** CME and FanDuel/Robinhood push prediction markets and retail into futures; financial innovation can have unintended consequences.  #mech/structural_shift _(time-bound view)_
  > this intersection between uh we'll call it betting markets, prediction markets and traditional futures markets uh that they're getting more closely aligned
  asset: other · horizon: years · testable: no · confidence: low
  ^MT095-C09-1
- **Mark Rzepczynski** Inelastic markets hypothesis: markets are not perfectly efficient because large flows relative to normal volume move prices, and different participants have different elasticities.  #mech/liquidity_flows
  > market uh can be inelastic or the elasticity changes across markets because of the volume that you trade or the flows that you trade have an impact on price
  indicator: market elasticity to flows · asset: multi · horizon: days · conditions: Large flows vs usual volume · testable: yes: flow-price impact · confidence: medium
  ^MT095-C09-2
- **Mark Rzepczynski** Participants' mandates limit their ability to provide capital, so market composition matters and flows affect prices away from efficient value.  #mech/liquidity_flows
  > if you take a mutual fund that has a a focus in stocks, if they have flows that come in, they're going to have to invest in stocks
  indicator: fund flows · asset: equities · direction: price up with inflows · horizon: days · conditions: Mandate-constrained buyers · testable: yes · confidence: medium
  ^MT095-C09-3
- **Niels Kaastrup-Larsen** In Denmark almost half of TV advertising is now from betting firms, an anecdotal gauge of how widespread retail speculation and betting products have become, which adds noise to markets.  #mech/behavioral _(added by sonnet-xhigh cross-check, time-bound view)_
  > about almost half the advertising on television is purely from betting firms
  indicator: betting advertising share · asset: multi · direction: retail speculation up · testable: no - anecdote · confidence: low
  ^MT095-C09-X1
- **Niels Kaastrup-Larsen** The chairman of CFM (a large systematic manager) is cited as a leading proponent of the inelastic markets hypothesis, an example of practitioner interest in flow-driven price impact.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check)_
  > the chairman of CFM who had become a very or has become a very uh big proponent as I understand it of this inelastic market hypothesis
  indicator: inelastic market hypothesis · asset: multi · direction: flows move prices · testable: partly - hypothesis is testable with flow data · confidence: medium
  ^MT095-C09-X2

### C10
- **Mark Rzepczynski** Because composition of the market is determined by flows, flows move prices; retail flow timing and beliefs can push price from the efficient value.  #mech/liquidity_flows
  > the market matters and because the composition is affected by the flow flow matters and flow will then affect prices
  indicator: flows · asset: equities · horizon: days · testable: yes · confidence: medium
  ^MT095-C10-1
- **Niels Kaastrup-Larsen** First Brands' bankruptcy hit trade-finance funds (a UBS fund had 30% exposure) marketed as low-risk steady double-digit returns, showing packaging narratives can hide risk.  #mech/risk_management _(time-bound view)_
  > there was a UBS fund that turned out to have 30% of its portfolio tied to the failed first brand group
  indicator: trade finance funds · asset: credit · direction: private credit losses · horizon: weeks · conditions: Opaque collateral · testable: partly: single event · confidence: medium
  ^MT095-C10-2
- **Niels Kaastrup-Larsen** Trend following shows daily volatility but rarely any really bad surprises in 35 years.  #mech/risk_management
  > really bad surprises. I I can't really think of any in the last 35 years that I've been part of this where something happened that you wouldn't expect.
  asset: multi · horizon: years · testable: partly: track record · confidence: medium
  ^MT095-C10-3

### C11
- **Mark Rzepczynski** Trade finance is intensive credit work requiring physical inventory checks (counting windshield wipers); you need many good loans to cover one bad loan.  #mech/risk_management
  > is that my collateral or is you use that collateral for five other different loans
  indicator: collateral verification · asset: credit · testable: no: practitioner knowledge · confidence: medium
  ^MT095-C11-1
- **Mark Rzepczynski** Daily mark-to-market and margining in futures makes lending against collateral safer than opaque lending, though fraud like nickel and the salad-oil case happened in futures markets.  #mech/risk_management
  > what is the tremendous innovation that's been associated with futures markets since its inception with daily marktomarket
  indicator: daily margin · asset: multi · testable: no · confidence: medium
  ^MT095-C11-2
- **Niels Kaastrup-Larsen** Q4 tends to be a decent quarter for trend following, though Niels notes he has no data to base it on.  #mech/seasonality
  > which I'm always thinking of Q4 as not a bad quarter for trend following
  indicator: trend following Q4 returns · asset: multi · direction: trend up in Q4 · horizon: months · testable: yes: seasonal test · confidence: low
  ^MT095-C11-3
- **Mark Rzepczynski** Lending against inventory carries a double-pledging risk: the same collateral may back several loans, so lenders must verify inventory physically (windshield wipers in First Brands' warehouses).  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > is that my collateral or is you use that collateral for five other different loans
  indicator: collateral verification in trade finance · asset: credit · direction: private credit losses when collateral is pledged repeatedly · conditions: Opaque inventory lending · testable: partly - detectable only through collateral audits · confidence: high
  ^MT095-C11-X1

### C12
- **Niels Kaastrup-Larsen** Gold rose 10.2% in September 2025, its largest monthly move since futures began in 1974, a great opportunity for old-school trend following despite AI-disruption talk.  #mech/slow_reaction _(time-bound view)_
  > But then you see gold up 10% 10.2% I think it was in September.
  indicator: gold monthly return · asset: commodities · direction: long gold trend · horizon: months · conditions: Strong trending moves · testable: yes: data · confidence: high
  ^MT095-C12-1
- **Niels Kaastrup-Larsen** October 2025 early numbers: Beta 50 +1.22% month, +1.68% YTD; CTA index -1.54% YTD; versus MSCI World +19.1%, S&P 500 TR +15.98% YTD.  #mech/slow_reaction _(time-bound view)_
  > After so many months of uh having negative um numbers uh year to date, we're now for the Btop 50 at least into positive territory.
  indicator: BTOP50, SG CTA, MSCI World, S&P 500 TR · asset: multi · horizon: months · testable: yes: index data · confidence: high
  ^MT095-C12-2
- **Niels Kaastrup-Larsen** Early-October 2025 trend data: SG Trend about +1.6% in the month and -0.71% YTD, the short-term traders index +73bp in October and about -4.42% YTD, and a very strong CTA day the day before, so managed futures were roughly flat YTD after a long negative stretch.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > Stocken trend up another 1.6% up only sorry down only 71 basis points uh as of Tuesday.
  indicator: SG Trend index; short-term traders index · asset: multi · direction: trend recovering · horizon: months · conditions: Gold and equity trends continuing · testable: yes - public index data · confidence: high
  ^MT095-C12-X1
- **Niels Kaastrup-Larsen** Traditional assets kept gaining: the S&P US aggregate bond index was up 20bp in early October and 4.5% YTD, with MSCI World up 1.1% in the month, so trend lagged a 60/40 portfolio.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > S&P US aggregate bond index up 20 basis points in October um and up 4 and a.5% so far this year
  indicator: S&P US aggregate bond index · asset: rates · direction: bonds modestly up · horizon: months · testable: yes - public index data · confidence: high
  ^MT095-C12-X2

### C13
- **Mark Rzepczynski** Quantica research: for about 10 years alternative (smaller, esoteric) futures markets added value with high Sharpe and low correlation, but recently their performance fell behind core markets.  #mech/slow_reaction
  > these alternatives for a good 10 years was adding a significant amount of uh value uh value added to the portfolio that they had high sharp ratios and that they were uh uh low correlated
  indicator: alternative vs core market trend returns · asset: multi · horizon: years · testable: yes: core vs alternative returns · confidence: medium
  ^MT095-C13-1
- **Mark Rzepczynski** Adding alternative markets recently hurt trend followers, raising the question of the optimal number of markets.  #mech/slow_reaction
  > it's been more of a headwind that having more diversification we're adding these alternative markets has had a negative impact
  indicator: number of markets · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT095-C13-2
- **Mark Rzepczynski** As CTAs piled into less liquid alternative markets their flows changed behaviour and reduced profitability, an inelastic-market market-impact effect that grows with AUM.  #mech/crowding_positioning
  > more and more CTAs entering in these less liquid markets, these alternative markets, by definition, is is that their flows are going to impact the the behavior of those markets
  indicator: CTA flows in illiquid futures · asset: multi · direction: trend profits down · horizon: years · conditions: Large AUM in thin markets · testable: yes: capacity studies · confidence: medium
  ^MT095-C13-3
- **Mark Rzepczynski** Market footprint (notional far above cash) not bid-ask cost drives CTA performance, so backtests must include impact.  #mech/research_method
  > it's not the cost of the bid ask spread it's not the trading cost it's the market footprint or impact that really drives performance
  indicator: market impact · asset: multi · horizon: years · conditions: Large CTAs · testable: yes · confidence: medium
  ^MT095-C13-4
- **Mark Rzepczynski** Two schools exist on market breadth for trend followers: stay with a core of the most liquid markets, or add many smaller 'alternative' markets for hidden opportunities; the Quantica study tests which has paid.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > Let's stick to a core group, keep the most liquid markets. That's all you need to do to, uh, to be a good CTA trend follower.
  indicator: number of markets traded · asset: multi · horizon: years · conditions: Depends on AUM and market liquidity · testable: yes - compare core versus extended universes · confidence: medium
  ^MT095-C13-X1

### C14
- **Mark Rzepczynski** The key research battle for a CTA is lowering market impact while growing AUM; signal identification is largely solved.  #mech/research_method
  > how can uh they reduce their market impact their market footprint while still adding more assets under management
  indicator: market impact vs AUM · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT095-C14-1
- **Mark Rzepczynski** Banks run CTA trackers (trend models plus flow analysis) to anticipate CTA flows and trade with or against them, a form of front-running pressure on CTAs.  #mech/crowding_positioning
  > a number of large brokerage firms, you know, some of the French banks, uh, for example, have now CTA trackers
  indicator: CTA tracker models · asset: multi · horizon: days · conditions: Large CTA flows · testable: partly: flows observable · confidence: medium
  ^MT095-C14-2
- **Mark Rzepczynski** There is too much money following similar CTA strategies; knowing when large CTAs are coming lets others step off the track.  #mech/crowding_positioning
  > I could say yes, there is too much money following it with, uh, with similar strategies.
  indicator: CTA assets · asset: multi · direction: trend returns down · horizon: years · conditions: On average; very strong trends overcome impact · testable: partly · confidence: medium
  ^MT095-C14-3
- **Mark Rzepczynski** Brokers offer CTAs cheap execution partly to see their order flow, because knowing a large CTA's orders are coming lets the broker step aside or trade ahead, so cheap commissions can hide information leakage costs.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check)_
  > why are they willing to do this at just such low prices
  indicator: broker visibility of CTA order flow · asset: multi · direction: CTA execution costs hidden · horizon: days · conditions: Large CTA orders executed through few brokers · testable: no - motive is inferred from an anecdote · confidence: medium
  ^MT095-C14-X1

### C15
- **Niels Kaastrup-Larsen** Brokers publish estimated CTA flows tied to price triggers and sell audit data, making CTA flows widely known and a crowding risk.  #mech/crowding_positioning
  > if the S&P does this then CTAs will have to sell you know 80 million worth of equities
  indicator: estimated CTA equity flows · asset: equities · horizon: days · testable: partly · confidence: medium
  ^MT095-C15-1
- **Mark Rzepczynski** Execution is short-term trading: cutting market impact costs by 1-2% can be a significant share of annual returns, and market-on-close still has impact.  #mech/risk_management
  > every CTA is a short-term trader. And what I mean by that is is that how you actually execute your orders
  indicator: execution costs · asset: multi · horizon: days · testable: yes: transaction cost analysis · confidence: high
  ^MT095-C15-2
- **Mark Rzepczynski** Trading at the close, first 10 minutes or VWAP all have microstructure impact even for long-term trend followers.  #mech/risk_management
  > market on close still has a market impact because you know it it is a market clearing price
  indicator: execution timing · asset: multi · horizon: days · testable: yes · confidence: medium
  ^MT095-C15-3
- **Mark Rzepczynski** Mark states that the common view is that intermediate-term trends (a couple of weeks) are the sweet spot, long-term is also good and short-term is poor, which Niels then disputes with his own research.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check)_
  > the sweet spot for most trend followers is sort of intermediate trend you know a couple weeks
  indicator: trend speed · asset: multi · direction: medium-speed trend best · horizon: weeks · testable: yes - compare speeds historically · confidence: medium
  ^MT095-C15-X1
- **Niels Kaastrup-Larsen** Niels dislikes brokers publicising estimated CTA flows despite Chinese walls, because it exposes CTA positioning and creates conflict-of-interest and crowding risk for the managers who trade through them.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check)_
  > I'm not a great fan of of the um of the of the shops that we place our trades with, whether or not there are Chinese walls or not
  indicator: broker-published CTA flow estimates · asset: multi · horizon: days · conditions: Broker research on CTA flows · testable: no - qualitative · confidence: medium
  ^MT095-C15-X2

### C16
- **Niels Kaastrup-Larsen** In Niels's research longer-term trend following is most profitable (with more volatility and drawdowns) while short-term has not made money for a long time, contrary to the 'medium-term sweet spot' view.  #mech/slow_reaction
  > longerterm uh trend following and yes it's been the most profitable in in our research
  indicator: trend speed returns · asset: multi · direction: long-term trend profitable · horizon: years · conditions: Higher vol and drawdowns · testable: yes: speed-segmented returns · confidence: medium
  ^MT095-C16-1
- **Niels Kaastrup-Larsen** Medium-term trend following has been the hardest hit in the last two to three years, so adaptive speed matters and investors should not choose managers set on one time frame.  #mech/slow_reaction _(time-bound view)_
  > the last two or three years, probably medium-term has been the hardest hit of of these kind of different speeds of trend following
  indicator: medium-term trend returns · asset: multi · horizon: years · conditions: Recent 2-3 years · testable: yes · confidence: medium
  ^MT095-C16-2
- **Mark Rzepczynski** Diversify across style, time horizon and markets because nothing works all the time.  #mech/risk_management
  > a three-dimensional uh diversification is style timing and markets
  asset: multi · testable: partly · confidence: medium
  ^MT095-C16-3
- **Mark Rzepczynski** Trend following isolates each market's price signal and discards fundamentals and cross-market information, which is both its strength and a limitation.  #mech/research_method
  > A trend follower says I'm not interested in causal inference.
  asset: multi · testable: no: conceptual · confidence: medium
  ^MT095-C16-4

### C17
- **Mark Rzepczynski** Treat markets as a network where one market's flows, behaviour and volatility influence another (e.g. dollar trend informing gold).  #mech/liquidity_flows
  > Flows out of the dollar may flow into the gold market.
  indicator: dollar flows vs gold · asset: multi · horizon: weeks · testable: yes: lead-lag models · confidence: low
  ^MT095-C17-1
- **Mark Rzepczynski** Cross-market connections are nonlinear and episodic, requiring lots of data, computing power and machine learning; an edge could exist but is hard to find.  #mech/research_method
  > if you could sort of find those connections and realize that they're nonlinear, they're episodic
  indicator: cross-market connectedness · asset: multi · testable: yes: ML network models · confidence: low
  ^MT095-C17-2
- **Niels Kaastrup-Larsen** Cross-market ideas are not new (cross-sectional momentum, PCA), and relationships change, so the challenge is knowing when connectedness breaks down.  #mech/research_method
  > They will do cross-sectional momentum analysis or whatever we define it as.
  indicator: cross-sectional momentum, PCA · asset: multi · testable: yes · confidence: medium
  ^MT095-C17-3

### C18
- **Mark Rzepczynski** Portfolio construction should use causal relationships rather than correlation and integrate prediction with optimization; decision-focused learning optimizes and predicts together instead of sequentially.  #mech/research_method
  > think in terms of not correlation but causal relationships and also you want to think about how you integrate predictions with the optimization
  indicator: correlation vs causal links, decision-focused learning · asset: multi · testable: yes: research agenda · confidence: low
  ^MT095-C18-1
- **Mark Rzepczynski** Current CTA practice relies on correlation, hierarchical clustering or PCA across markets and cointegration tests to decide which markets to hold, which treats connectedness only as a diversification input, not a causal or predictive one.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > most CTAs will spend a lot of time looking at what is the correlation across markets and do I need to have both of those markets in the portfolio
  indicator: cross-market correlation, clustering, cointegration · asset: multi · conditions: Portfolio construction stage · testable: yes - standard methods · confidence: high
  ^MT095-C18-X1

