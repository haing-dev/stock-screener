---
source_id: MT223
title: "Why Trend Thrives When Inflation Returns - Systematic Investor - Ep.373"
date: 2025-11-14
channel: "Top Traders Unplugged"
url: 
words: 11411
claims: 37
added_by_crosscheck: 10
corrections: 2
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Alan Dunne (host, guest-hosting)", "Yoav Git (CTA manager)"]
tags: [source, layer0]
---
# Why Trend Thrives When Inflation Returns - Systematic Investor - Ep.373

**Speakers:** Alan Dunne (host, guest-hosting); Yoav Git (CTA manager)

**Summary:** Top Traders Unplugged episode with three papers: the inelastic markets hypothesis ($1 inflow raises valuation $5, critiqued as trend-following reverse causality), Man AHL on the best strategies for inflationary times (trend and commodities do well), and backtest overfitting in alternative beta (average 60% Sharpe haircut). Conclusion: elasticity governs trend speed, inflation suits trend, and portfolio construction matters more than signal.

**Approach:** trend following, supply and demand elasticity, inflation, QIS, backtest overfitting

**Cross-check completeness estimate of first read:** 0.80 - the first reader captured the paper summaries, critiques, Man inflation findings and overfitting haircut well; it missed several secondary mechanisms (rebalancing spillover, price-impact versus volatility, trend-speed implication for commodities versus equities, option-like payoff of trend, wealth effect, money-market cash argument) and mis-framed the bond 'elasticity' number.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro; speaker's radar on UK maths education, no market content |
| C02 | 2 | SG CTA performance; inelastic markets hypothesis headline |
| C03 | 2 | supply-demand elasticity and trend |
| C04 | 1 | instrumental variable method, granular IV |
| C05 | 1 | market clearing debate, elasticity of bonds vs equities |
| C06 | 2 | intensity of buying pressure; critique, trend flows |
| C07 | 2 | data used, policy implications of QE |
| C08 | 2 | elasticity and trend speed, equity vs commodity adjustment |
| C09 | 2 | trading speeds, time series, stock-bond correlation |
| C10 | 2 | rebalancing spillover, takeaway; Man inflation paper intro |
| C11 | 2 | inflation and equities/bonds/trend |
| C12 | 2 | hit ratio, inflation mandates |
| C13 | 3 | commodities vs trend, TIPS, real estate |
| C14 | 1 | transition; QIS industry opacity |
| C15 | 2 | backtest overfitting haircut, portfolio construction |
| C16 | 1 | QIS vs CTA incentives, execution |
| C17 | 0 | outro |

## Claims

### C02
- **Alan Dunne (host)** As of early Nov 2025 SG CTA index was -1.9% YTD and SG Trend -1.44% YTD, after a recovery in recent months.  #mech/slow_reaction _(time-bound view)_
  > Stock gen CTA down 40 basis points monthto date and year to date still down uh 1.9% uh this year and stockgen trend down 56 basis points on the month and down 1.44% so far um this year.
  indicator: SG CTA index, SG Trend index · asset: multi · horizon: months · conditions: Nov 2025 · testable: no - performance data point · confidence: high
  ^MT223-C02-1
- **Yoav Git (CTA manager)** The inelastic markets hypothesis (Gabaix and Koijen) estimates that $1 of inflow into the US equity market raises aggregate valuation by about $5, implying flows drive valuations and a possible bubble.  #mech/liquidity_flows
  > whenever there's a $1 flowing into equity market that translates into a $5 increase in the overall valuation in the market.
  indicator: flow-to-price multiplier · asset: equities · direction: long equities while inflows persist; vulnerable if flows reverse · horizon: quarters · testable: yes - paper's instrumental-variable estimate · confidence: medium
  ^MT223-C02-2
- **Yoav Git** As of early November 2025 fixed income has been very difficult for trend following, with prices going up and down in a choppy range while the UK kept rates at 4%, making fixed income trend a hard market to trade.  #mech/slow_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > certainly fixed income has been very difficult. Um we've seen up and down and uh and round we go and of course the UK has kept interest rates at 4% as well.
  indicator: fixed income trend / UK policy rate 4% · asset: rates · direction: fixed income trend whipsawed · horizon: months · conditions: range-bound rates with policy on hold · testable: partly - trend returns in rates for 2025 measurable · confidence: medium
  ^MT223-C02-X1

### C03
- **Yoav Git (CTA manager)** Trend size depends on elasticity of supply and demand: inelastic markets (electricity, commodities) need a large price move to clear a shock, and delayed adjustment (cows must be grown) makes the trend persist.  #mech/slow_reaction
  > the more the more inelastic the market, the more response we need to get in price to really drive to change the supply and demand.
  indicator: elasticity of supply/demand; time to new equilibrium · asset: commodities · horizon: months · conditions: physical markets with slow supply response · testable: partly - elasticity hard to measure · confidence: high
  ^MT223-C03-1
- **Yoav Git (CTA manager)** Supply and demand elasticities are hard to estimate because shocks hit both curves, giving a biased estimate unless an instrument isolates one side.  #mech/research_method
  > every time there is a shock uh you get a shock in both the both to the supply and to the demand and the two are mixed up.
  indicator: instrumental variable · asset: multi · testable: yes - econometrics · confidence: high
  ^MT223-C03-2

### C04
- **Yoav Git (CTA manager)** Gabaix-Koijen granular instrumental variable uses shifts in each holder's share of demand (e.g. between pension funds, mutual funds, ETFs) as idiosyncratic shocks to identify market elasticity without bias.  #mech/research_method
  > if suddenly the US starts consuming more and the and Europe starts consuming less that is definitely idiosyncratic shock
  indicator: change in share of holdings across investor types · asset: equities · horizon: quarters · testable: yes - method · confidence: high
  ^MT223-C04-1

### C05
- **Yoav Git (CTA manager)** Fixed income is far more elastic than equities (elasticity about 0.25-0.75): $1 trillion of Fed buying in the GFC did not move bonds like equities because Treasury supply expands to meet demand, whereas equity supply (~$500bn issuance a year) is driven by the real economy and barely responds to price.  #mech/liquidity_flows
  > the balance balance sheet grows from 10 trillion to about 11 trillion. Okay. Um so there's a 1 trillion flowing into the market. Now, did we see bond prices going up by 50%.
  indicator: market elasticity by asset class; Fed balance sheet; issuance · asset: multi · direction: money moved from money-market funds to equities has large price effect · horizon: years · testable: partly - natural experiments · confidence: medium
  **Correction (cross-check):** The 0.25-0.75 figure is a price-impact multiplier, not an elasticity in the economist's sense: the speaker says fixed income 'elasticity' is 'much much lower' (0.25, 0.5, maybe 0.75, and later '25 cents' per dollar), meaning a dollar of buying moves bond prices far less than the equity multiplier of 5. The claim's wording 'far more elastic ... (elasticity about 0.25-0.75)' mixes the two meanings. → Fixed income reacts far less to flows than equities: $1 trillion of Fed buying in the GFC did not lift bond prices by 50%, the bond-market flow multiplier is about 0.25-0.75 per dollar versus 5 for equities, because Treasury supply expands to meet demand (US Treasuries grew from $10tn to about $25tn), whereas equity issuance (~$500bn a year) is constrained by the real economy.
  ^MT223-C05-1
- **Alan Dunne** Cash in money market funds is bullish for equities if the inelastic-markets result holds, because moving it into stocks would lift valuation by a multiple of the inflow; the objection is that the market always clears (every buyer has a seller), which Yoav answers with the mismatch in elasticity between money markets and equities.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check)_
  > if you're to believe this paper if if this money comes in it'll push it up by a magnitude of five
  indicator: money market fund assets · asset: equities · direction: equities up when cash moves from money market to equity · horizon: months · conditions: depends on equity price impact being much larger than money market price impact · testable: partly - flow-to-price relationship testable, subject to the causality critique · confidence: medium
  ^MT223-C05-X1

### C06
- **Yoav Git (CTA manager)** The regression is contemporaneous so the 5x multiplier confuses causality: rising equity prices attract trend-following flows (CTAs, closet trend followers, retail), so the true flow-impact multiple is probably lower (just above 1).  #mech/slow_reaction
  > I actually don't believe that's the correct number. and and let me tell you what uh my crit I mean the main criticism really is about what drives what.
  indicator: contemporaneous flow-price regression; trend-following flows · asset: equities · horizon: quarters · testable: yes - Granger-style lead-lag tests · confidence: medium
  ^MT223-C06-1
- **Yoav Git (CTA manager)** CTA assets of about $300bn would produce quarterly trend-driven flows into equity equal to roughly 0.2% of market value after a rise, a sizeable fraction of the 6% flow figure used in the paper.  #mech/crowding_positioning
  > 300 billion under management in CTAs, that kind of translates into a quarterly a quarterly flows into equity if equity prices go up of about 0.2% 2% of the value of the overall market
  indicator: CTA AUM times trend exposure · asset: equities · horizon: quarters · testable: yes - flow calculation · confidence: low
  **Correction (cross-check):** Number is ambiguous in the transcript ('about 0.2% 2% of the value of the overall market'); the speaker then calls it 'not far from the 6%', which fits about 2% (one third of 6%) better than 0.2% (a thirtieth), so '0.2% ... a sizeable fraction' is likely wrong or at least unsafe. → CTAs with about $300bn under management would produce quarterly trend-following flows into equities of roughly 0.2% or 2% of market value (transcript garbled, 2% more consistent with 'not far from the 6%'), so trend flows plus closet trend followers could explain a substantial part of the paper's 6% flow figure.
  ^MT223-C06-2
- **Alan Dunne** Although every buyer has a seller, prices move because of the intensity of buying and selling pressure (buyers bid up while sellers hold back offers), which reconciles the market-clearing objection to the inelastic-markets hypothesis and explains why 'more buyers than sellers' is a wrong explanation of price moves.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check)_
  > there is a seller, but it's the intensity of the buying and selling pressure.
  asset: multi · testable: no - conceptual framing · confidence: high
  ^MT223-C06-X1
- **Alan Dunne** Equities behave like Giffen goods because of the wealth effect and psychology: demand rises when prices rise, a positive-feedback channel that is already in the literature and amplifies flow-driven valuation changes.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > there's a wealth effect you know so psychology Gh people become more bullish when they see the price going up.
  asset: equities · direction: demand up as price rises · testable: no - already-known behavioural effect · confidence: low
  ^MT223-C06-X2

### C07
- **Yoav Git (CTA manager)** The paper uses slow quarterly data (flow of funds, Morningstar fund flows, 13F, roughly 2000-2021), so one quarter is the horizon and the multiplier cannot be estimated over time.  #mech/research_method
  > the data that they use is uh uh uh flows of funds. They look at morning star data about uh mutual fund flows and they use the 13F um filings.
  indicator: flow of funds, Morningstar, 13F · asset: equities · horizon: quarters · conditions: sample about 2000-2021 · testable: yes · confidence: high
  ^MT223-C07-1
- **Yoav Git (CTA manager)** If the 5x equity multiplier were right, a dollar of central bank buying is more effective in equities than bonds (25 cents), though with obvious moral hazard; QE's portfolio-rebalancing channel relies on this effect.  #mech/policy_reaction
  > you would think it would it might caution central bankers a bit so much QE.
  indicator: central bank asset purchases · asset: multi · horizon: years · testable: no - policy implication · confidence: medium
  ^MT223-C07-2

### C08
- **Yoav Git (CTA manager)** Equity markets have low elasticity but adjust quickly: ETF shares outstanding show strong negative autocorrelation weekly, whereas commodity prices become negatively autocorrelated only about a year out, because supply takes a year to respond.  #mech/slow_reaction
  > if I look at shares outstanding in ETF market you see a very strong negative autocorrelation on the weekly scale
  indicator: ETF shares outstanding autocorrelation; commodity price autocorrelation sign change · asset: multi · direction: trend speed should be slower in physical commodities than in equities · horizon: weeks · testable: yes - autocorrelation by horizon · confidence: medium
  ^MT223-C08-1
- **Yoav Git (CTA manager)** There is a trend lookback that falls in the mean-reversion zone of each market's adjustment process, and this varies with the physical nature of the market, especially in commodities.  #mech/slow_reaction
  > there is a frequency which is actually not a good frequency where you are sort of stuck in the mean reversion area of that of that process
  indicator: trend lookback by market · asset: multi · direction: avoid lookbacks in the mean-reversion window · horizon: months · conditions: strongest in commodities; complicated in equities · testable: yes - sharpe by lookback per market · confidence: medium
  ^MT223-C08-2
- **Yoav Git** More elastic markets have lower volatility because supply or demand absorbs shocks with small price moves; bond volatility is lower than equity volatility for this reason, so elasticity helps explain cross-market differences in trend size.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > if the market is is more elastic it will have lower volatility and we see that again in bonds versus equity the bond volatility is lower than than equity volatility
  indicator: market elasticity vs volatility · asset: multi · direction: more elastic market, lower volatility · testable: yes - volatility versus estimated elasticity testable across markets · confidence: medium
  ^MT223-C08-X1
- **Yoav Git** Because commodity supply takes about a year to respond (planting, mining), price must do the adjusting work over a year and the resulting prolonged trend should be harvested at a slow speed, whereas equities find a new equilibrium quickly, which is why intraday equity trend strategies exist.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > price will have to do the work over an entire year and that means that you are looking at a a sort of a prolonged trend and that's how you should harvest it.
  indicator: trend lookback by market type · asset: commodities · direction: slow trend in commodities, fast in equities · horizon: months · conditions: commodity supply lag of about a year · testable: yes - optimal lookback by market type testable · confidence: medium
  ^MT223-C08-X2

### C09
- **Yoav Git (CTA manager)** Markets are already traded at different speeds because costly-to-trade markets use slower signals; liquidity partly reflects the physical market, and a tilt toward a faster or slower lookback in a commodity may have genuine physical reasons.  #mech/slow_reaction
  > the speed at which you trade is uh is already a function of um it's already a function of of something in the market like the
  indicator: trading cost and trend speed per market · asset: commodities · direction: slower trend in expensive markets · horizon: months · testable: yes · confidence: medium
  ^MT223-C09-1
- **Yoav Git (CTA manager)** A 5x equity valuation multiplier during an inflationary asset process would spill over into bonds via rebalancing and show up as positive bond-equity correlation, which has appeared in the last two years and is a warning sign.  #mech/liquidity_flows _(time-bound view)_
  > I would have expected to see uh a positive bond equity correlation.
  indicator: stock-bond correlation · asset: multi · horizon: years · testable: partly - hypothesis · confidence: low
  ^MT223-C09-2
- **Yoav Git** If the 5x valuation multiplier is real, a reversal of flows would amplify a downturn in the same ratio (a roller coaster), but the data are quarterly from the early 2000s to 2021, so there are too few points to see whether the multiplier changes over time.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check)_
  > if things go start going south we are heading for a bit of a roller coaster ride right there's no question about that
  indicator: flow-to-valuation multiplier · asset: equities · direction: equities fall faster when flows reverse · horizon: months · conditions: assumes symmetric multiplier · testable: no - only one estimated number, no time variation · confidence: low
  ^MT223-C09-X1

### C10
- **Yoav Git (CTA manager)** His takeaway: multiplier probably nearer one than five, but the paper rightly replaces the efficient market view with buying and selling pressure that clears order books.  #mech/liquidity_flows
  > I suspect the number is actually lower. It may be a little bit above one
  indicator: price impact multiple · asset: equities · horizon: quarters · testable: partly · confidence: medium
  ^MT223-C10-1
- **Yoav Git (CTA manager)** Man AHL paper (Otto Van Hemert, May 2021, The Best Strategies for Inflationary Times) predicted inflation-period performance before 2022 spike and its backtest goes back to 1925.  #mech/research_method
  > this paper was was published in May 2021 before we saw inflation spiking to around 8% in the US um and it predicted exactly what it's like
  indicator: asset and strategy returns in high inflation · asset: multi · horizon: years · testable: yes - published out-of-sample 2022 · confidence: high
  ^MT223-C10-2
- **Yoav Git** Any rebalancing process spreads value from where money is put (one stock) to nearby stocks in the same industry and to other asset classes, so flows into equities can spill over into bonds and show up as a positive stock-bond correlation.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check)_
  > any rebalancing process uh spreads the the value from let's say from one stock if you're putting money into one stock into the other stocks
  indicator: rebalancing spillover / stock-bond correlation · asset: multi · horizon: months · conditions: flow-driven rather than inflation-driven valuation regime · testable: partly - cross-asset flow spillover testable · confidence: medium
  ^MT223-C10-X1

### C11
- **Yoav Git (CTA manager)** Rising inflation from a low level is good for equities, rising inflation from above-median level is bad; bonds always lose when inflation rises because yields rise.  #mech/policy_reaction
  > if inflation starts picking up from a low level that's actually quite good for equities.
  indicator: inflation level and change vs asset returns · asset: multi · direction: long equities if inflation rises from a low base; short bonds if inflation rises · horizon: months · conditions: depends on starting level of inflation · testable: yes - conditioned regressions · confidence: medium
  ^MT223-C11-1
- **Yoav Git (CTA manager)** In inflationary periods commodity trend and also fixed-income trend do well in the Man paper's backtest to 1925.  #mech/slow_reaction
  > what trend strategies are likely to do well and um and is looking at commodity trend which is not surprising right inflation and commodities are very much linked together
  indicator: trend by sector in rising inflation · asset: multi · direction: long commodity and fixed-income trend when inflation rises · horizon: years · testable: yes · confidence: medium
  ^MT223-C11-2

### C12
- **Yoav Git (CTA manager)** Trend following breaks even at about a 40% hit ratio of markets trending; the last couple of years had about 30% and 2021-22 about 60%, so returns come from the share of markets trending, not an absence of trends.  #mech/slow_reaction _(time-bound view)_
  > we just need about 40% heat ratio to sort of break even and start making money. And the last couple of years have been tough because we've had a heat ratio of 30% maybe.
  indicator: share of markets trending (hit ratio) · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT223-C12-1
- **Yoav Git (CTA manager)** Investors with inflation-plus mandates rarely use CTAs, yet active strategies such as CTAs with commodity exposure benefit from inflation volatility, unlike TIPS or real estate.  #mech/policy_reaction
  > a CTA with a high commodity allocation will do extremely well in periods of sort of rising and and falling inflation right so it's inflation volatility uh which is important to us
  indicator: inflation volatility · asset: commodities · direction: long commodity-heavy CTA for inflation protection · horizon: years · testable: partly · confidence: medium
  ^MT223-C12-2
- **Alan Dunne** The Man backtest showed trend following earning about 25% annualised in higher-inflation periods; this looked fanciful after a five-year tough spell for trend, but 2021-22 matched or exceeded it.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check)_
  > periods of higher inflation 25% uh annualized returns etc which seemed like uh
  indicator: trend following returns in high-inflation regimes · asset: multi · direction: long trend in high inflation · horizon: years · conditions: high inflation periods · testable: yes - conditional returns computable from history to 1925 · confidence: medium
  ^MT223-C12-X1
- **Yoav Git** Trend following bleeds a little money day by day like an option-buying strategy and then pays spectacularly when many markets trend (stairs down, elevator up, as in 2021-22 with 60% winners), so the right response is to trust and improve the process rather than abandon it.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > the way that we die is we die by thousand cuts. We we essentially bleed money because it is like an option buying strategy.
  indicator: hit ratio of trending markets · asset: multi · direction: small steady losses, large occasional gains · horizon: years · conditions: needs enough markets to trend (about 40% break-even) · testable: yes - payoff profile of trend index vs option replication · confidence: high
  ^MT223-C12-X2

### C13
- **Yoav Git (CTA manager)** Long-only commodities have negative carry (storage and financing) and large losses in other periods, so trend following gives inflation protection with lower downside than long-only.  #mech/risk_premium
  > holding just just being sort of long only a commodity may not be the solution for an inflation product
  indicator: long-only commodity index vs commodity trend · asset: commodities · direction: trend rather than long-only commodities · horizon: years · testable: yes · confidence: high
  ^MT223-C13-1
- **Yoav Git (CTA manager)** Inflation evolves slowly, matching the speed of trend following, whereas equity crises can happen in two days and give trend followers only a second-response hedge.  #mech/slow_reaction
  > inflation is a much more slowly evolving process. And that really plays very well with the speed at which CTAs trend.
  indicator: inflation as slow risk factor · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT223-C13-2
- **Yoav Git (CTA manager)** TIPS and long-dated bonds combine inflation and duration exposure which offset (higher inflation brings higher yields); housing suffers from higher mortgage rates, so real assets do not reliably hedge inflation in the episode.  #mech/policy_reaction
  > So if you have a long-term if you have a if you have a longdated bonds the there is it's they've got two risk factors built in.
  indicator: TIPS, REITs, residential real estate in inflation · asset: rates · horizon: months · conditions: when inflation accompanies higher rates · testable: yes · confidence: medium
  ^MT223-C13-3

### C14
- **Yoav Git (CTA manager)** QIS (bank quant index) market of $300-600bn is opaque, making it hard to assess; hedge fund managers must justify their added value against QIS trend products.  #mech/research_method
  > difficult for us to actually assess to make a like a a bird's eye assessment of that industry.
  indicator: QIS assets · asset: multi · testable: no · confidence: medium
  ^MT223-C14-1

### C15
- **Yoav Git (CTA manager)** A study of ~200 alternative-beta (QIS) products found an average 60% Sharpe haircut from pre-launch backtest to live, even for carry and trend, so a backtest Sharpe of 1 delivers about 0.4; a 50% haircut is appropriate before allocating.  #mech/research_method
  > the average haircut is around 60%. So um you you think your shop is one but actually the shop you're getting is point4.
  indicator: Sharpe haircut live vs backtest · asset: multi · horizon: years · conditions: backtest overfitting · testable: yes - published study (2017) · confidence: high
  ^MT223-C15-1
- **Yoav Git (CTA manager)** In trend following the signal is a commodity worth about 0.2 Sharpe per market; value comes from portfolio construction, risk management and execution.  #mech/research_method
  > the signal is actually going to be fairly well known and actually it doesn't really matter which particular signal you're looking at. Um that is going to give you let's say sharper point two per market.
  indicator: trend signal Sharpe per market · asset: multi · testable: partly · confidence: medium
  ^MT223-C15-2

### C16
- **Yoav Git (CTA manager)** Spiky returns of a QIS trend index signal weak risk management; QIS makes money from netting flows so their execution incentives differ from a fund, though they offer low fees, customisation and capital-efficient margining.  #mech/risk_management
  > if you look at the returns very spiky okay and that's to me is a sign that the risk management isn't necessarily like cutting edge
  indicator: return spikiness · asset: multi · testable: partly · confidence: medium
  ^MT223-C16-1

