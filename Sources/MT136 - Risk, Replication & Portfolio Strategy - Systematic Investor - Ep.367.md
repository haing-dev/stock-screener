---
source_id: MT136
title: "Risk, Replication & Portfolio Strategy - Systematic Investor - Ep.367"
date: 2025-10-06
channel: "Top Traders Unplugged"
url: 
words: 12772
claims: 63
added_by_crosscheck: 13
corrections: 5
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Neils Kaastrup-Larsen (host, Top Traders Unplugged)", "Andrew Beer (co-founder DBi, managed-futures replication ETF DBMF)"]
tags: [source, layer0]
---
# Risk, Replication & Portfolio Strategy - Systematic Investor - Ep.367

**Speakers:** Neils Kaastrup-Larsen (host, Top Traders Unplugged); Andrew Beer (co-founder DBi, managed-futures replication ETF DBMF)

**Summary:** Systematic Investor weekly with Beer and Kaastrup-Larsen (Sept 2025). Topics: inelastic market hypothesis and breaking 60/40 paradigm, Sept 2025 CTA performance and the 'let it run hot' trade, why replication outperformed large single-manager CTAs in 2024-25 (implementability, liquidity, whipsaw), and why multistrategy pod hedge funds deliver consistent returns. Main conclusions: flows and paradigm shifts matter, cost/liquidity limit broad universes, multistrats work via talent plus structure but face capacity risk.

**Approach:** trend following, managed futures replication, multi-strategy hedge funds, portfolio construction, market microstructure/implementation costs, inelastic markets

**Cross-check completeness estimate of first read:** 0.80 - first reader caught the main themes and most numbers across all 19 chunks; missed attributed views (Mike Green, Pivotal Path data quality), the CalPERS bucket closure, CTA index dispersion, the 2022 incentive-fee point and several caveats (dead-money risk, lookback hypothesis).

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | intro; resilience of markets despite shocks |
| C02 | 1 | inelastic market hypothesis; Danish drones aside |
| C03 | 3 | talent vs efficient markets; paradigm stickiness; flows |
| C04 | 3 | 60/40 paradigm failure; passive impact on strategies |
| C05 | 4 | allocator slowness and 2022 CTA alpha; CalPERS total portfolio approach; model assumptions |
| C06 | 3 | capital market assumption extrapolation; bond bubble; wealth managers' diversifying bucket |
| C07 | 4 | CTA index performance Sept 2025; BTFD and trend detection |
| C08 | 3 | let it run hot trade; replication vs single-manager pair trade question |
| C09 | 2 | when replication under/outperforms: missed idiosyncratic trades, inflection points |
| C10 | 4 | inflection de-risking; why single managers drew down: reversals in financials |
| C11 | 2 | ETFs vs funds; complexity, liquidity and vol controls in many markets |
| C12 | 3 | microstructure stress costs; trend in all markets debate |
| C13 | 4 | implementation costs, slippage, capacity, worst-day evaluation |
| C14 | 2 | recovery driven by liquidity; multistrat returns |
| C15 | 2 | multistrat index data; Pinnacle manager-selection story |
| C16 | 3 | multistrats as prop desks; compensation; efficiency of markets |
| C17 | 4 | multistrat capacity risk and why it works; liquid alt multi-strategy failure |
| C18 | 2 | pod PM incentives; fees vs Sharpe |
| C19 | 0 | nothing actionable: outro and sponsor reads |

## Claims

### C01
- **Andrew Beer** Despite a long list of political, war and tariff shocks over ~2 years, equities rallied about 55%, showing the system's resilience, though Beer thinks repeated shocks cannot be ignored forever.  #mech/behavioral _(time-bound view)_
  > the um equities are up 55% over that period of time and uh and and and nothing's broken
  asset: equities · horizon: years · conditions: after repeated shocks without a market break; Beer expects fragility eventually · testable: no - narrative observation · confidence: medium
  ^MT136-C01-1

### C02
- **Neils Kaastrup-Larsen** Under the inelastic market hypothesis (Bouchaud/CFM), each dollar flowing into equities moves price by a multiple of that dollar because few participants absorb flow, so flows rather than fundamentals can dominate returns.  #mech/liquidity_flows
  > inelastic market hypothesis um where essentially it's a theory that um contemplates that $1 into equities just it doesn't just notch the price higher
  indicator: net equity fund flows / price impact multiplier · asset: equities · direction: equity prices rise with inflows, fall with outflows · conditions: when passive/price-insensitive flows dominate · testable: yes - price impact of flows can be estimated · confidence: medium
  **Correction (cross-check):** The 'because few participants absorb flow' reason is not stated; the host only says a dollar into equities multiplies rather than notches the price (and that this is the Bouchaud/Wigglesworth FT lunch article). → Under the inelastic market hypothesis (Bouchaud, CFM, as described by the host from an FT article), a dollar flowing into equities multiplies the price effect rather than moving it by one dollar's worth, so flows can dominate returns.
  ^MT136-C02-1

### C03
- **Andrew Beer** Skill is only monetised where the opportunity set is favourable; talent cannot overcome a structurally declining or efficient area, so market efficiency varies by segment.  #mech/structural_shift
  > if you are the very best executive in America running a steel company going through a 30-year structural decline, you're going to have a really hard time
  asset: other · horizon: years · conditions: depends on the market segment's opportunity · testable: no - anecdotal · confidence: medium
  ^MT136-C03-1
- **Andrew Beer** Investment paradigms (e.g. efficient markets, Black-Litterman allocation) persist until contradicting evidence reaches critical mass, because practitioners' identity is tied to them, so paradigm change is slow then abrupt.  #mech/behavioral
  > when you have an existing paradigm, it it's very sticky because you have tons and tons of people who are trained in that paradigm
  asset: multi · horizon: years · testable: no - conceptual · confidence: medium
  ^MT136-C03-2
- **Neils Kaastrup-Larsen** If market outcomes are driven mainly by flows, a reversal of passive inflows could produce a very different market regime from the post-GFC rally.  #mech/liquidity_flows
  > what determines more uh what goes on in markets are the flows, right?
  indicator: passive fund flows · asset: equities · conditions: when passive inflows reverse · testable: partly - flow data exist but regime shift is a prediction · confidence: low
  ^MT136-C03-3
- **Neils Kaastrup-Larsen** Mike Green's view, cited by the host, is that the growth of passive investing distorts equity prices because flows rather than valuation information set the price.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check)_
  > clearly people like Mike Green thinks that this is really distorting the markets
  indicator: passive share of equity flows · asset: equities · direction: passive inflows push equity prices away from fundamentals · horizon: years · conditions: attributed view; unclear whether it holds once flows reverse · testable: partly - passive-flow share and flow-price impact can be measured but no spec given · confidence: medium
  ^MT136-C03-X1

### C04
- **Andrew Beer** 60/40 worked because of the stock-bond correlation regime of the long bond bull market (zero/negative correlation); it reinforced itself as a paradigm and would not have looked the same starting in 1990.  #mech/structural_shift
  > if you'd done it in 1990, um then you wouldn't have seen the same negative correlation or zero correlation of stocks and bonds
  indicator: stock-bond correlation · asset: multi · horizon: years · conditions: depends on stock-bond correlation regime · testable: yes - rolling correlation and 60/40 results by start date · confidence: medium
  ^MT136-C04-1
- **Andrew Beer** This decade bonds became highly correlated with equities (around 0.8 in his words, vol doubled or tripled) and fell with stocks in the inflation shock, breaking the diversification premise of 60/40.  #mech/structural_shift _(time-bound view)_
  > bonds have 80 80% correlation to equities and they went down in 2020 when they were supposed to protect
  indicator: stock-bond correlation · asset: multi · direction: bonds fail to hedge equities in an inflation regime · horizon: years · conditions: inflationary regime / rising rates · testable: yes - rolling stock-bond correlation · confidence: high
  ^MT136-C04-2
- **Andrew Beer** Passive investing may have impaired some active strategies such as equity long/short, while others such as managed futures are affected differently, so the impact is uneven.  #mech/crowding_positioning
  > equity long short was everyone's favorite hedge fund strategy in the 2000s. by the end of the 2010s it had faced years and years and years of underperformance
  asset: equities · horizon: years · testable: partly - attribution to passive is hard · confidence: medium
  ^MT136-C04-3
- **Neils Kaastrup-Larsen** Strategies and allocation models validated on the post-GFC flow-driven period may behave differently over a longer sample, so evidence from a unique era is a fragile basis for allocation.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > they're kind of built on a unique time period where markets were behaving somewhat differently that they may do over a longer period of time
  asset: multi · horizon: years · conditions: applies to alternative-strategy track records built in one regime · testable: partly - split-sample or regime tests would show it · confidence: low
  ^MT136-C04-X1

### C05
- **Andrew Beer** Allocators who deliberately do not change their minds quickly were slow to react when inflation returned, so fast trend followers made about a decade of alpha in 2022.  #mech/slow_reaction _(time-bound view)_
  > it presented an opportunity for CTAs to make a decade of alpha in one year
  asset: multi · direction: long managed futures/trend when inflation regime shifts · horizon: months · conditions: when allocators and portfolios are slow to adapt to a regime change · testable: yes - CTA 2022 returns documented · confidence: high
  ^MT136-C05-1
- **Neils Kaastrup-Larsen** If passive funds see outflows and a long bear market arrives, allocator demand for dedicated short sellers would reverse from nil to high.  #mech/liquidity_flows _(time-bound view)_
  > If if money starts to flow out of passive funds and we get a 10-year bare market, everyone's gonna love short sellers again.
  indicator: passive fund flows · asset: equities · direction: long short sellers · horizon: years · conditions: in a prolonged bear market with passive outflows · testable: no - conditional prediction · confidence: low
  ^MT136-C05-2
- **Neils Kaastrup-Larsen** Under CalPERS' total portfolio approach, assets are judged by contribution to total portfolio goals, which would favour diversifiers such as trend following that look unappealing on a standalone basis.  #mech/risk_management
  > every investment is judged by its contribution ution to the entire portfolio goals, not just its own asset class
  asset: multi · direction: more allocation to diversifying strategies like managed futures · horizon: years · conditions: if institutions follow through; may take years to trickle down · testable: partly - portfolio contribution can be tested · confidence: medium
  ^MT136-C05-3
- **Andrew Beer** Capital market assumption and asset allocation models fit historical premia (e.g. size factor with data issues in 2000) and extrapolate them, so results are overfit and judgement is layered on top.  #mech/research_method
  > they torture the data until they get the the answer that they want
  asset: multi · horizon: years · testable: yes - out-of-sample test of extrapolated assumptions · confidence: high
  ^MT136-C05-4
- **Andrew Beer** Allocators' weight in managed futures is far below what its diversification statistics (low correlation to other strategies) would justify, so a portfolio-contribution lens would raise it.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > the allocation to manage futures relative to all these other hedge fund strategies is is preposterously small
  indicator: allocation weights by hedge fund strategy · asset: multi · direction: higher managed-futures allocation · horizon: years · conditions: needs allocators to judge by portfolio contribution rather than standalone return · testable: partly - mean-variance contribution can be computed, allocation data are needed · confidence: high
  ^MT136-C05-X1

### C06
- **Andrew Beer** Institutional allocators haircut recent winners (e.g. Nasdaq) and assume mean reversion for others, so they are structurally unlikely to give large allocations to whatever has recently worked.  #mech/behavioral
  > they kind of haircut assumptions for things that look too good recently and they and they kind of assume mean reversion on other assets
  asset: multi · horizon: years · testable: partly - allocator behaviour observable · confidence: medium
  ^MT136-C06-1
- **Andrew Beer** Holding a large bond allocation at the peak of the bond bubble (2021 yields) mathematically limited future returns, a mistake of the 60/40 paradigm.  #mech/risk_premium
  > we basically decided in the beginning of 2021 that a very meaningful portion of your portfolio would be in something that mathematically was going to diff have difficulty earning a return over time
  indicator: starting bond yield · asset: rates · direction: bonds' expected return low when yields are low · horizon: years · conditions: at very low starting yields · testable: yes - starting yield predicts bond returns · confidence: high
  ^MT136-C06-2
- **Andrew Beer** US wealth managers moved from 60/40 to 60/20/20 with a 20% diversifying bucket because bonds had correlation to equities of about 0.8, vol up 2-3x and returned less than cash.  #mech/structural_shift _(time-bound view)_
  > a lot of people who um who who sold or built their business on 60/40 have now introduced a 20% % diversifying bucket
  asset: multi · direction: more allocation to diversifiers (trend/alternatives) · horizon: years · testable: partly · confidence: medium
  ^MT136-C06-3
- **Andrew Beer** CalPERS shut its $4bn absolute-return bucket because a 4% return on about 1-2% of the fund could not move total results, so a diversifier sized too small to matter gets cut despite its portfolio benefit.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > they used to have a $4 billion absolute return bucket but making 4% on 1% of your two you know 2% of your portfolios didn't mean anything
  indicator: CalPERS absolute return allocation · asset: multi · direction: diversifiers need meaningful size to survive allocator reviews · horizon: years · conditions: institutional allocators judging on total-fund impact · testable: no - anecdote, but the sizing logic is checkable · confidence: medium
  ^MT136-C06-X1

### C07
- **Neils Kaastrup-Larsen** In September 2025 trend following profits came from equities and precious metals, while fixed income was quiet despite the Fed pivot.  #mech/slow_reaction _(time-bound view)_
  > It's the equities and it's the precious metals in particular uh that are helping with a few supporting acts from the commodity side
  indicator: CTA sector P&L attribution · asset: multi · direction: long equities, long precious metals · horizon: weeks · conditions: Sept 2025 · testable: yes - attribution data · confidence: medium
  ^MT136-C07-1
- **Neils Kaastrup-Larsen** As of late September 2025 the trend index was up almost 5% for the month but down 3% YTD, while MSCI World was up about 17% and S&P 500 about 14%.  #mech/slow_reaction _(time-bound view)_
  > The trend index is up almost 5% for the month um as of Tuesday, I should say. Um down 3% for the year.
  indicator: SG Trend Index; SG CTA Index; BUP 50; short-term traders index · asset: multi · horizon: months · conditions: 2025 year to date · testable: yes - index data · confidence: high
  ^MT136-C07-2
- **Neils Kaastrup-Larsen** Kaastrup-Larsen's trend barometer read 36 (weak) despite good performance data; a fourth positive month for SG Trend would be the first since Jan-Apr 2024.  #mech/slow_reaction _(time-bound view)_
  > my own trend barometer finished at 36 yesterday
  indicator: Trend barometer (Niels' own) · asset: multi · horizon: weeks · conditions: Sept 2025 · testable: partly - barometer definition not given · confidence: low
  ^MT136-C07-3
- **Andrew Beer** Beer advised a client near the lows to buy the dip because trend following has a known pattern of being rattled and then turning around and pivoting.  #mech/slow_reaction _(time-bound view)_
  > BTFD
  asset: multi · direction: long trend following after drawdown · horizon: weeks · conditions: after sharp drawdown · testable: no - anecdote · confidence: medium
  ^MT136-C07-4
- **Neils Kaastrup-Larsen** Through late September 2025 CTA indices were still weak: BTOP50 (transcribed 'BUP 50') +2.81% in the month and about flat YTD after months negative, SG CTA +3.5% and -3% YTD, SG Trend about +5% and -3% YTD, SG Short-Term Traders +1.5% and -5% YTD, so the short-term sub-style lagged trend.  #mech/research_method _(added by sonnet-xhigh cross-check, time-bound view)_
  > short-term traders index is also up one and a half% uh is uh but still down 5% so far this year
  indicator: BTOP50, SG CTA, SG Trend, SG Short-Term Traders indices · asset: multi · direction: short-term CTA style lags longer-term trend in 2025 · horizon: months · testable: yes - index data · confidence: high
  ^MT136-C07-X1

### C08
- **Andrew Beer** After the April 2025 Liberation Day whipsaw, trend models detected the let-it-run-hot trade early (long equities/gold/crypto) even when it felt reckless in June.  #mech/slow_reaction _(time-bound view)_
  > what I think it detected early was the let it run hot trade
  asset: multi · direction: long equities, gold, crypto; short USD · horizon: months · conditions: after head-fake inflections · testable: no - narrative · confidence: medium
  ^MT136-C08-1
- **Andrew Beer** Let-it-run-hot view: political pressure keeps rates lower than warranted, lifting equity valuations and gold/crypto, with a bond tantrum later rather than sooner; the president is also structurally short the dollar.  #mech/policy_reaction _(time-bound view)_
  > Fed is Trump is going to jawbone the Fed or they're going to then keep rates lower than they should that's going to you drive up equity valuations.
  asset: multi · direction: long equities, gold, crypto; bond tantrum later · horizon: months · conditions: while Fed is pressured to stay easy · testable: no - political thesis · confidence: medium
  ^MT136-C08-2
- **Andrew Beer** Pair trading replication against single managers is costly because replication has historically had about a 300 bps annual cost advantage over hedge fund CTAs, so the short side bleeds, and timing relative outperformance is unpredictable.  #mech/research_method
  > we have about a 300 basis point efficiency advantage
  indicator: replication vs CTA index spread · asset: multi · horizon: years · testable: yes - historical spread measurable · confidence: high
  **Correction (cross-check):** Beer calls the 300 bps an 'efficiency advantage' and 'outperformance' of the replication product versus single managers over 10 years, not a cost advantage. → Pairing against replication is costly because DBMF has outperformed single managers by about 300 bps a year over 10 years (more for investable mutual fund or UCITS peers), so the short leg bleeds and timing the swings is unpredictable.
  ^MT136-C08-3

### C09
- **Andrew Beer** Hedging or pairing against replication loses at least 300 bps per year on average; for investable mutual fund or UCITS managed futures the gap is greater than 300 bps.  #mech/risk_management
  > you could buy five well-known mutual funds in the US and short DBMF against it and you'd lose 300 basis points on average
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT136-C09-1
- **Andrew Beer** Replication underperforms when many idiosyncratic non-core trades (Mexican peso, Canada front end, Nikkei, softs in early 2023) work at the same time, which is hard to forecast.  #mech/slow_reaction _(time-bound view)_
  > we didn't have the Mexican peso, we didn't have the front end of the Canadian interest rate curve, we didn't have the Nikkay, we didn't have softs
  asset: multi · horizon: months · conditions: when a broad set of niche markets trend together · testable: yes - attribute replication tracking error to markets absent · confidence: high
  ^MT136-C09-2
- **Andrew Beer** The replication ETF outperformed single-manager CTAs by roughly 600-800 bps at the 2022 peak, partly because it charges no incentive fee, then gave much of that back when markets reversed in 2023, so relative performance versus managers swings widely.  #mech/risk_management _(added by sonnet-xhigh cross-check, time-bound view)_
  > by by the peak in 2022 we were outperforming in part because of absence of incentive fees
  indicator: DBMF versus CTA peers · asset: multi · direction: fee structure (no incentive fee) adds to relative gain when trends pay · horizon: years · testable: yes - fee-drag decomposition · confidence: high
  ^MT136-C09-X1

### C10
- **Andrew Beer** At sharp inflection points like SVB (March 2023), replication loses a few hundred bps at most when a sharp reversal persists and gets de-risked faster than actual funds, but recovers if it was a head fake.  #mech/slow_reaction
  > when it keeps going we will be de-risking that position faster than actual funds
  asset: rates · horizon: weeks · conditions: at sharp inflection points · testable: yes - episode analysis · confidence: medium
  ^MT136-C10-1
- **Andrew Beer** Replication outperforms when the extra non-core trades or the risk management overlays of single-manager CTAs backfire.  #mech/risk_management
  > the periods when we tend to outperform are periods when those non-core trades backfire or risk management backfire
  asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT136-C10-2
- **Neils Kaastrup-Larsen** Large CTAs tilted to financials suffered because equities, fixed income and currencies each had 2-3 large reversals within about 14 months, forcing long/short flips (whipsaw).  #mech/new _(time-bound view)_
  > I would argue that there have been you know two three big reversals in all of those sectors within the last 14 months
  asset: multi · horizon: months · conditions: when all financial sectors reverse together · testable: yes - trend returns vs reversal frequency · confidence: medium
  ^MT136-C10-3
- **Neils Kaastrup-Larsen** Managers with broader diversification including commodities mitigated losses from financial sector reversals.  #mech/risk_management _(time-bound view)_
  > those that are more diversified where smaller market contributions or where smaller markets like you know the commodities have been able to mitigate um some of those losses
  asset: commodities · horizon: months · conditions: when financial markets whipsaw · testable: partly · confidence: medium
  ^MT136-C10-4

### C11
- **Andrew Beer** In 2024-2025 the large majority of simple ETF replication products beat the average mutual fund/hedge fund managed futures peer, which should not happen and suggests a structural reason.  #mech/research_method _(time-bound view)_
  > 80 to 90% of ETFs are outperforming um the average mutual fund hedge fund in 2024 and 2025 by a lot
  asset: multi · horizon: years · conditions: 2024-2025 · testable: yes - fund return comparison · confidence: medium
  **Correction (cross-check):** Beer says '80 to 90% of ETFs' beat the average mutual fund/hedge fund in 2024-25 (his HedgeNordic article); the scope is ETFs versus fund peers, not specifically simple replication products versus managed futures peers. → In 2024 and 2025 about 80-90% of ETFs beat the average mutual fund or hedge fund peer by a lot, which Beer calls statistically awkward and takes as a hint of a structural cause (cost, liquidity, simplicity).
  ^MT136-C11-1
- **Andrew Beer** Large multi-hundred-instrument CTAs with vol controls and short-term models must trade many positions in thin markets after shocks, incurring large impact costs and whipsaw.  #mech/liquidity_flows
  > in a four or five day period of time, you may be selling a hundred different positions or buying back a 100 different positions in markets where there's thin liquidity
  asset: multi · horizon: days · conditions: after shocks when liquidity vanishes in large footprint · testable: yes - transaction cost analysis · confidence: medium
  ^MT136-C11-2
- **Andrew Beer** Entering 2025 a chaotic, noisy year should have favoured complex multi-hundred-instrument single-manager funds with vol controls and short-term models over a slower replication model, and about $100bn of professional money was positioned that way, yet the simple model did better.  #mech/behavioral _(added by sonnet-xhigh cross-check, time-bound view)_
  > there is a hundred billion dollars of professional money that has had would have made a bet on on the latter not the former and it hasn't happened right
  indicator: single-manager CTAs versus replication, 2025 · asset: multi · direction: simple slower replication outperformed complex CTAs · horizon: months · testable: partly - compare complexity buckets of CTAs · confidence: high
  ^MT136-C11-X1
- **Andrew Beer** CTA losses in 2024-25 have no single clear narrative (unlike stock pickers, who can state which thesis failed); they came from many small timing, rebalancing and model-speed costs adding up, which makes the shortfall hard to diagnose and fix.  #mech/risk_management _(added by sonnet-xhigh cross-check, time-bound view)_
  > it's a lot of little paper cuts that resulted in a in in a fairly deep wound across the industry
  indicator: single-manager CTA P&L attribution · asset: multi · horizon: months · testable: partly - attribution of cost versus signal loss · confidence: medium
  ^MT136-C11-X2

### C12
- **Andrew Beer** CTAs exiting positions in stressed illiquid markets trade against prop desks that anticipate forced flows, adding to cost.  #mech/crowding_positioning
  > you're also trading with prop desks, right? Who can who can smell blood in the water.
  asset: multi · horizon: days · conditions: during forced selling in thin markets · testable: partly · confidence: medium
  ^MT136-C12-1
- **Andrew Beer** Before adding a marginal market to a CTA portfolio, test whether a stress-day execution loss (e.g. 200 bps) would have justified inclusion; liquidity under stress should be a market-selection criterion.  #mech/risk_management
  > would you five years ago when you thought about in including position number 298 would you have included in your portfolio knowing there could be a day where you lost 200 basis points just trading it
  indicator: stress-day liquidity cost · asset: multi · testable: yes - stress-liquidity test · confidence: medium
  ^MT136-C12-2
- **Neils Kaastrup-Larsen** Every market can trend but not simultaneously, so broad diversification will sometimes lag a narrower longer-timeframe replication, yet the 2024-25 snapshot is not conclusive evidence of a permanent change.  #mech/cycle_persistence
  > all markets has the ability to trend. They obviously don't trend at the same time
  asset: multi · horizon: years · conditions: periods where niche markets do not trend · testable: partly · confidence: medium
  ^MT136-C12-3
- **Neils Kaastrup-Larsen** Dispersion among CTAs in 2024-25 can come from model lookback choice (a wrong lookback for that regime) or from many markets in the book simply not trending, rather than from a permanent structural change.  #mech/slow_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > you could have a different, you know, the the kind of quote unquote the wrong look back period for your models
  indicator: trend lookback length · asset: multi · horizon: months · conditions: regime dependent: lookback fit and number of non-trending markets · testable: yes - lookback sensitivity test · confidence: medium
  ^MT136-C12-X1

### C13
- **Andrew Beer** A trend only has value if transaction costs allow capture (Copenhagen housing example): trendfollowing needs low costs.  #mech/risk_management
  > If getting in and out costs you 10 to 15%. brokerage commissions and everything else, there may be a trend, you still don't want to try to do it from an investment perspective.
  asset: other · conditions: when round-trip costs are high · testable: yes - net of cost trend returns · confidence: high
  ^MT136-C13-1
- **Andrew Beer** Strategies like high-frequency trading earned huge returns on a few million dollars but alpha disappeared at 30-50 million, so capacity and implementation limit what backtests suggest.  #mech/risk_management
  > the returns disappeared at 30 or 50 million
  indicator: capacity · asset: multi · conditions: at larger AUM · testable: yes - capacity test · confidence: medium
  ^MT136-C13-2
- **Andrew Beer** Slippage measured on simple 70-market liquid portfolios may not hold when trading 300 instruments; quants once boasted of cutting slippage from 400 to 200 bps.  #mech/risk_management
  > what do you think about trading 300 instruments, not 70?
  indicator: slippage in bps · asset: multi · conditions: wider, less liquid universes · testable: yes · confidence: medium
  ^MT136-C13-3
- **Andrew Beer** Allocators judge strategies by worst-day outcomes, e.g. private credit risk lies in defaults and markdowns, so execution and liquidity must be evaluated for stress scenarios.  #mech/risk_management
  > everybody evaluates these things on the very worst day that it can happen.
  asset: multi · testable: partly · confidence: medium
  ^MT136-C13-4

### C14
- **Andrew Beer** The rebound in managers after April 2025 may reflect a liquidity influx (YOLO, FOMO, let it run hot) rather than durable expected returns.  #mech/liquidity_flows _(time-bound view)_
  > that recovery is not necessarily a sign of long-term high expected returns
  asset: multi · horizon: months · conditions: in strongly liquidity-driven rallies · testable: no - interpretation · confidence: medium
  ^MT136-C14-1
- **Andrew Beer** Multistrategy hedge funds had a worst month of -6% in March 2020 (about -1% at 5x unleveraged equivalent) while delivering consistent returns.  #mech/risk_management
  > the worst month I've been able to find was down 6% in March
  indicator: multistrategy hedge fund index · asset: multi · horizon: months · testable: yes · confidence: high
  **Correction (cross-check):** Garbled: the -6% March 2020 loss is the multistrat fund NAV; Beer says with about 5x leverage that equals only about -1% across the underlying unlevered portfolio. → Multistrategy hedge funds had a worst month of about -6% (March 2020, per Beer), equal to roughly -1% on the underlying unlevered book at 5x leverage, so the engine was very resilient to the COVID crash.
  ^MT136-C14-2
- **Neils Kaastrup-Larsen** Trading liquid exchange-listed futures is a structural advantage over off-exchange or illiquid instruments because exit costs and valuations stay transparent in stress, so liquidity should be stressed as a selection criterion.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > trading liquid futures on exchange relative to off exchange and illquid stuff
  asset: multi · testable: partly - bid-ask and impact comparison · confidence: high
  ^MT136-C14-X1

### C15
- **Andrew Beer** Pivotal Path Multistrategy index returns: 2020 13%, 2021 9%, 2022 2%, 2023 6%, 2024 11%, 2025 YTD 8%, very steady, with total fees possibly 1000 bps before clients are paid.  #mech/risk_premium _(time-bound view)_
  > 2% in 2022 up 6% in 23 up 11% 24 and up 8% year-to- date.
  indicator: Pivotal Path Multistrategy Hedge Fund Index · asset: multi · horizon: years · conditions: 2020-2025 · testable: yes - index data from CalPERS-type institutions · confidence: high
  ^MT136-C15-1
- **Andrew Beer** Giving an exceptional specialist manager seed capital with capacity caps and full fees yields about 30% a year for the first three years, because new talented managers outperform before size grows.  #mech/new
  > He's going to do 30 a year for his first three years.
  asset: commodities · horizon: years · conditions: provided AUM growth is capped and managed accounts give transparency · testable: partly - manager-level performance data · confidence: medium
  ^MT136-C15-2
- **Andrew Beer** Pivotal Path's multistrategy index is built from data supplied by institutions that actually invest in the funds, which Beer says makes it the most accurate record of what investors earned, better than manager-reported databases.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > he gets his hedge fund index data from the institutions like Kalpers that actually invest in hedge funds
  indicator: Pivotal Path Multistrategy Hedge Fund Index · asset: multi · testable: partly - compare index against self-reported databases · confidence: medium
  ^MT136-C15-X1
- **Andrew Beer** Beer had expected multistrat risk to be dead money after fees over time rather than blow-up, was wrong over the last 24 months, but notes equities up 55% and bonds about 8% a year make this a poor test.  #mech/risk_premium _(added by sonnet-xhigh cross-check, time-bound view)_
  > the risk of the space was not that they're going to blow up but that they are but the risk is basically dead money over time
  indicator: multistrategy hedge fund net return after fees · asset: multi · horizon: years · conditions: depends on market backdrop; weak test in a strong equity and bond period · testable: partly - needs a longer sample · confidence: medium
  ^MT136-C15-X2

### C16
- **Andrew Beer** Multistrat funds act like bank proprietary desks with better information, financing and pay-out around 55% of revenue as compensation.  #mech/structural_shift
  > Banks used to pay 55% of revenue
  asset: multi · testable: no · confidence: medium
  ^MT136-C16-1
- **Andrew Beer** Markets are efficient in segments like US large cap stocks, so fees of 100 bps are not recouped, but esoteric segments remain inefficient where talent can earn alpha.  #mech/structural_shift
  > picking uh large cap stocks in the US and getting paid 100 basis points for it, your clients are probably not you're probably not going to do better than 100 basis points over time statistically
  asset: equities · horizon: years · testable: partly · confidence: medium
  ^MT136-C16-2
- **Andrew Beer** Multistrats bet that putting top PMs in a structure removing distractions with high payouts (e.g. $200m of $500m profit) leaves clients, firm and PM better off.  #mech/behavioral
  > we can take that guy and give him an incentive structure where he is not sleeping for the next five years
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT136-C16-3

### C17
- **Neils Kaastrup-Larsen** Multistrats allocate capital to pods mainly by past P&L, which risks capacity dilution and hidden leverage as inflows grow, as in private equity.  #mech/crowding_positioning
  > the risk management teams that are allocating the money to these uh sub uh parts to a large extent they're buying P&L curves
  asset: multi · horizon: years · conditions: as assets grow and leverage increases · testable: partly · confidence: low
  ^MT136-C17-1
- **Andrew Beer** Marginal pods are logically less attractive than earlier ones, so capacity dilution is a risk for multistrats, although leaders like Citadel have so far disproved it.  #mech/crowding_positioning
  > is is pod number 300 right by definition less attractive than pod number 20
  asset: multi · horizon: years · conditions: as pod count rises · testable: yes · confidence: medium
  ^MT136-C17-2
- **Andrew Beer** Despite 5x leverage on $50bn and major regime shifts since 2020, no multistrat blew up or had a catastrophic drawdown, which suggests the pod structure with hedge fund format works.  #mech/risk_management _(time-bound view)_
  > not a single one of these funds had not only not blown up, but not had a anything approaching what would be deemed to be a catastrophic draw down
  indicator: drawdown · asset: multi · horizon: years · conditions: needs hedge fund structure with lockups · testable: yes · confidence: high
  ^MT136-C17-3
- **Andrew Beer** Liquid-alt multi-strategy mutual funds, the plug-and-play versions, returned under 3% a year over 10 years after about 200 bps of fees, and cannot replicate hedge fund multistrats with quarterly liquidity.  #mech/risk_premium
  > has been an embarrassing failure. the the entire space has done less than 3% peranom after about a 200 basis points in in in expenses over the past 10 years
  asset: multi · horizon: years · conditions: needs hedge fund structure with limited withdrawals · testable: yes · confidence: high
  **Correction (cross-check):** The ending is ambiguous: Beer says the multistrat model cannot be run outside a hedge fund structure or when clients can redeem every quarter, not that it cannot be 'replicated with quarterly liquidity'. → Liquid-alt multi-strategy mutual funds returned under 3% a year over 10 years after about 200 bps fees (an embarrassing failure), and Beer says multistrat returns need the hedge-fund structure and capital that clients cannot pull every quarter.
  ^MT136-C17-4
- **Andrew Beer** Investors in liquid-alt multi-strategy mutual funds chase whichever fund is working, rotating among them, which adds to poor realised investor returns on top of the category's under-3% fund return.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > there's this kind of musical chairs of people kind of like going from one fund that's working well to another fund
  asset: multi · horizon: years · testable: yes - flow versus return studies · confidence: medium
  ^MT136-C17-X1

### C18
- **Andrew Beer** Pod managers face harsh drawdown limits, a down 3% year can mean dismissal, which drives risk discipline and hunger.  #mech/risk_management
  > being down 3% one year and, you know, he goes back to his office and the fact his, you know, he's he's all his stuff is sitting in boxes
  indicator: pod drawdown limit · asset: multi · horizon: years · testable: no - anecdote · confidence: low
  ^MT136-C18-1
- **Andrew Beer** Paying 1000 bps in fees is acceptable if the pod structure generates a Sharpe near 4 and half is paid out, but 200 bps for a 3% multi-strategy mutual fund return is excessive.  #mech/risk_premium
  > generate a four sharp ratio, take two of the sharp ratio to pay everybody
  indicator: Sharpe ratio net of fees · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT136-C18-2

