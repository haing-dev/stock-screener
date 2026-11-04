---
source_id: MT190
title: "Trend Following Is Changing Faster Than Ever - Systematic Investor - Ep.409"
date: 2026-07-19
channel: "Top Traders Unplugged"
url: 
words: 12182
claims: 51
added_by_crosscheck: 12
corrections: 1
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Yoav Git (co-host, systematic CTA practitioner, caption 'Y of Git')", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Trend Following Is Changing Faster Than Ever - Systematic Investor - Ep.409

**Speakers:** Yoav Git (co-host, systematic CTA practitioner, caption 'Y of Git'); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** July 2026 Systematic Investor: single-stock futures and compute-power futures, blow-up risk ranking of strategies, July 2026 counter-trend conditions, and a listener question on contract choice for commodity trend signals. Main segments: CFM 'Seven degrees of market structure' (0DTE retail option selling gives market makers positive gamma, causing intraday mean reversion, low index vol and record dispersion), the CFM short-term trend demise paper (volatility-normalised tick size; autocorrelation arithmetic), thematic factors, narrative momentum and equity trend diversification.

**Approach:** trend following, market microstructure, 0DTE options gamma, single stock futures, commodity roll, thematic factors, narrative momentum, dispersion

**Cross-check completeness estimate of first read:** 0.85 - the first reader captured the CFM market-structure chain (0DTE gamma, dispersion, tick size), the commodity-contract answer and narrative momentum accurately; it missed secondary mechanisms and examples (maturity-specific ag risk, roll volatility adjustment, rational basis of underreaction, QIS human overlay, spread of short-dated options) and one unit mix-up.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 1 | intro; CME single-stock futures, Kalshi compute-power curves, tax practicalities |
| C02 | 2 | single-stock futures for shorting; retail risk; compute power as new risk factor |
| C03 | 4 | strategy blow-up risk ranking; IBM -25% day; AI capex and chip obsolescence |
| C04 | 3 | AI/job chat; July counter-trend; energy dispersion by speed; trend barometer 45 |
| C05 | 2 | July index numbers; listener question on commodity futures modelling start |
| C06 | 3 | front vs deferred contract participants and risk factors; why industry uses front contract |
| C07 | 2 | contract-specific volatility adjustments; carry/roll yield seasonality; CFM blog intro |
| C08 | 4 | seven degrees: retail, systematic, 0DTE options, dispersion, mean reversion |
| C09 | 2 | 0DTE gamma concentration, market maker hedging and anti-trend effect |
| C10 | 2 | implied dispersion all-time high; single-stock futures rationale; link to short-term trend paper |
| C11 | 2 | volatility-normalised tick size; equities have smaller normalised tick; blog mechanism |
| C12 | 3 | autocorrelation arithmetic: cost in Sharpe for short-term trend; open-close follow-through stat |
| C13 | 1 | thematic investing as missing factors: variance decomposition (index, industry, Barra, themes) |
| C14 | 2 | themes vs ETFs/QIS; narrative momentum paper setup |
| C15 | 2 | narrative momentum: slow-moving themes, underreaction, news beta |
| C16 | 3 | estimation issues; AI makes news incorporation instant; agentic news personalisation |
| C17 | 1 | building diversified equity trend: index, industry, factors, narrative; outro |
| C18 | 0 | outro and legal disclaimer, nothing actionable |

## Claims

### C01
- **Yoav Git** Practical issues such as tax treatment of dividends and price changes for single-stock futures (and Kalshi compute contracts) can block adoption even when the instruments are attractive.  #mech/structural_shift _(time-bound view)_
  > the tax implications or like various like uh uh practical implications of trading it.
  indicator: single-stock futures tax treatment · asset: equities · testable: no - practical not testable · confidence: medium
  ^MT190-C01-1
- **Yoav Git** Forward curves on the cost of AI compute power (priced off Nvidia chips) are a new commodity-like risk factor with no historical precedent, which a systematic manager can view as a diversifying exposure if its tax and operational treatment becomes clear.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > Kali is announcing uh forward curves for uh compute power for the cost of comput power. So that's a like a different uh a different type of uh of commodity which we've never seen before
  indicator: compute-power forward curve (Kalshi) · asset: commodities · conditions: needs clear tax status and adequate liquidity · testable: no - no price history exists yet · confidence: medium
  ^MT190-C01-X1
- **Niels Kaastrup-Larsen** Adoption of single-stock futures among CTAs is mixed: a minority strongly favour trading single names rather than only indices, while most CTAs still stick to index futures.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > there is definitely a little bit of a debate among um CTA practitioners um for sure and I don't know that that many of our colleagues have embraced them.
  indicator: single-stock futures adoption · asset: equities · testable: no - industry anecdote · confidence: medium
  ^MT190-C01-X2

### C02
- **Yoav Git** Single-stock futures make shorting easy because no borrow is needed, giving CTAs and others new diversifying risk factors.  #mech/structural_shift _(time-bound view)_
  > the ability to short specific stocks will be useful.
  indicator: single-stock futures · asset: equities · testable: no · confidence: medium
  ^MT190-C02-1
- **Niels Kaastrup-Larsen** Retail access to shorting via futures is dangerous because short losses are unlimited (takeover risk).  #mech/risk_management
  > being short a stock can be you know lethal because it's unlimited upside uh sorry unlimited downside if you're short
  asset: equities · testable: no · confidence: medium
  ^MT190-C02-2

### C03
- **Niels Kaastrup-Larsen** A Sins Capital ranking placed managed-futures CTAs 15th of 17 on blow-up risk, vol-targeted diversified macro second lowest and short-vol/short-gamma the worst.  #mech/risk_management
  > CTA Minus futures came in as number 15 out of 17 uh with a green collar lower
  indicator: blow-up / forced liquidation risk ranking · asset: multi · testable: no - single ranking · confidence: medium
  ^MT190-C03-1
- **Yoav Git** CTAs and vol-driven macro are defensive with upside bias in a blow-up, but not instantly protected, unlike short volatility which is dangerous.  #mech/risk_management
  > anybody who manages their risk so CTAs and volatilitydriven macros
  asset: multi · testable: partly · confidence: medium
  ^MT190-C03-2
- **Niels Kaastrup-Larsen** IBM fell about 25% in a day (from 332 to 213 in six weeks), showing single-stock gap risk.  #mech/risk_management _(time-bound view)_
  > IBM lost 69 billion of market value in one day and that's about 25%
  indicator: single stock gap · asset: equities · horizon: days · testable: no - anecdote · confidence: high
  ^MT190-C03-3
- **Yoav Git** AI capex goes to chips lasting 2-3 years, unlike 2001 fibre which served for 20-25 years, so if AI fails recovery value is near zero.  #mech/fiscal_debt _(time-bound view)_
  > these chips don't last forever, you know. I mean, in the in the in the boom and bust you mentioned 2001
  indicator: AI capex asset life · asset: equities · horizon: years · conditions: AI capex bust · testable: no · confidence: medium
  ^MT190-C03-4
- **Niels Kaastrup-Larsen** Long-only equity exposure is not low blow-up risk: a long-only Nasdaq position fell about 85% in the 2000-2002 bust, so a low blow-up ranking for long-only equity is questionable.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > if you were long only NASDAQ in 2001ish um you would have been down 85% at some point
  indicator: Nasdaq drawdown 2000-2002 · asset: equities · horizon: years · conditions: after a valuation bubble · testable: yes - historical drawdown · confidence: high
  ^MT190-C03-X1

### C04
- **Niels Kaastrup-Larsen** July 2026 saw geopolitical noise, ceasefire loss, oil reversal; managers split by speed on who was caught short energies.  #mech/slow_reaction _(time-bound view)_
  > July is uh one another month of a little bit of adaptation
  indicator: trend speed · asset: commodities · horizon: weeks · conditions: sudden reversal in oil · testable: partly · confidence: medium
  ^MT190-C04-1
- **Yoav Git** July 2026 was counter-trend in fixed income and FX (Japan bond and repatriation risk); dispersion in commodities by speed of trader.  #mech/slow_reaction _(time-bound view)_
  > I think July has been counter trend um in general both you know in fixed income certainly and then FX
  asset: multi · horizon: weeks · testable: partly · confidence: medium
  ^MT190-C04-2
- **Niels Kaastrup-Larsen** Trend barometer at 45 is neutral.  #mech/slow_reaction _(time-bound view)_
  > My trend barometer kind of reflects that it's it ended yesterday at 45.
  indicator: Trend barometer (45) · asset: multi · horizon: weeks · testable: yes · confidence: medium
  ^MT190-C04-3

### C05
- **Niels Kaastrup-Larsen** As of 14 Jul 2026: BTOP50 +8.5% YTD, SG CTA ~+9%, SG Trend +8.76%, SG Short-Term Traders +4% (down 1.12% in July), MSCI World +11.15%, S&P 500 +11.32%, US Agg +0.41%.  #mech/slow_reaction _(time-bound view)_
  > beta 50 down three basis points so pretty flat uh still up 8 and a half for the year.
  indicator: BTOP50, SG indices, MSCI World, S&P 500 · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT190-C05-1
- **Yoav Git** Commodity contract months are different assets linked only by storage/inventories, so risk factors differ by maturity (answer to listener question on modelling).  #mech/structural_shift
  > in commodities you consume the commodity and then like it's a new commodity a month later or a few months later which which like the only thing which is connecting potentially different different months is storage
  indicator: inventories across contract months · asset: commodities · horizon: months · testable: yes - compare contract-specific and front-contract signals · confidence: high
  ^MT190-C05-2

### C06
- **Yoav Git** Front contracts are populated by speculators; deferred contracts by physical hedgers, so price dynamics move from short-term flows to long-term supply, demand and cost of production.  #mech/crowding_positioning
  > in the front contract of oil you will see a lot of CTAs, a lot of market makers, a lot of retailers
  indicator: participant mix by contract maturity · asset: commodities · horizon: months · testable: partly · confidence: medium
  ^MT190-C06-1
- **Yoav Git** Trading the front contract captures most risk, with lowest cost and highest liquidity; most of the industry uses the front contract history as signal.  #mech/risk_management
  > let's capture 80% of the risk with just trading the front contract and it's very useful
  indicator: front-contract series · asset: commodities · testable: yes · confidence: high
  ^MT190-C06-2
- **Yoav Git** As a contract nears expiry its volatility converges to the front contract's, supporting use of front history; natural gas summer vs winter is an exception.  #mech/slow_reaction
  > as you approach expiry the the volatility of the uh of the June contract that maybe have been less volatile a month ago suddenly goes to match the current front contract.
  indicator: contract volatility convergence · asset: commodities · horizon: weeks · conditions: approaching expiry · testable: yes · confidence: medium
  ^MT190-C06-3
- **Yoav Git** In agricultural curves the front is driven by demand because the crop size is already largely known, while deferred contracts (new crop) are driven by supply risks such as weather and disease, so different maturities carry distinct risk factors and different diversification value.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > As you go to further out on the curve, suddenly you're moving to the new crop. You really don't know what is going to be the supply.
  indicator: agricultural futures curve by maturity · asset: commodities · horizon: months · conditions: applies to crops with a harvest cycle (cotton, wheat) · testable: yes - return correlation between front and deferred contracts · confidence: medium
  ^MT190-C06-X1

### C07
- **Yoav Git** The front contract explains 90-99% of risk in financial futures but less in commodities; trade deferred contracts only to capture different risk factors.  #mech/risk_management
  > in financial universe like 95 90 to 99% of the risk in commodities less so
  indicator: risk explained by front contract · asset: commodities · testable: yes · confidence: medium
  ^MT190-C07-1
- **Yoav Git** Roll yield and convenience yield in commodities must be contract-specific because seasonal contracts are unconnected, unlike trend signals.  #mech/seasonality
  > if you're trying to calculate a carry in natural gas between the June and the December contract good luck to you
  indicator: carry / roll yield · asset: commodities · horizon: months · conditions: seasonal commodities · testable: yes · confidence: medium
  ^MT190-C07-2
- **Yoav Git** Where adjacent contracts differ materially in volatility (natural gas summer versus winter), a trend manager can compute volatility for the specific contract or adjust position size at the roll, so risk stays constant across the roll; for most markets using the rolled front series is still valid and there is no single correct answer.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > natural gas is an example um you know for example we would calculate the volatility on a specific contract or we would make the adjustment to when you roll the position in order to manage the risk slightly better
  indicator: contract-specific volatility; roll adjustment · asset: commodities · horizon: weeks · conditions: natural gas and other seasonal contracts · testable: yes - compare realised portfolio volatility with and without roll adjustment · confidence: medium
  ^MT190-C07-X1

### C08
- **Yoav Git** CFM blog 'Seven Degrees of Market Structure': COVID-era retail inflows, API-based systematic retail, 0DTE options, rising dispersion and more mean reverting indices.  #mech/structural_shift
  > started flooding um started flooding the equity
  indicator: retail participation · asset: equities · horizon: years · testable: partly · confidence: medium
  ^MT190-C08-1
- **Yoav Git** 0DTE index options exploded since weekly expiries in 2012, driven by retail selling at-the-money straddles to harvest the variance risk premium.  #mech/structural_shift
  > a huge rise in the volumes of what's called zero day to expiry options in the index.
  indicator: 0DTE option volume · asset: equities · horizon: years · testable: yes · confidence: high
  ^MT190-C08-2
- **Yoav Git** Implied correlation/dispersion index shows single-stock variance far above index variance, globally at an all-time high.  #mech/structural_shift _(time-bound view)_
  > It's an correlation is at an all-time uh low i.e idiosyncratic risk is at an all-time high.
  indicator: implied correlation; dispersion index · asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT190-C08-3
- **Yoav Git** Buying dips was historically a mistake but over the last 10 years the index has become more mean reverting and dip-buying pays within a month.  #mech/structural_shift
  > Um but over the last um the over the last 10 years buying the deep actually works much better.
  indicator: index short-term mean reversion · asset: equities · direction: buy dips in indices · horizon: months · conditions: post-2015 regime · testable: yes · confidence: medium
  ^MT190-C08-4

### C09
- **Yoav Git** Retail selling of near-expiry ATM options gives market makers concentrated long gamma, whose delta hedging sells rallies and buys dips, creating an anti-trend flow every day.  #mech/liquidity_flows
  > retail has been selling options at the money near expiry. Okay, literally at expiry and that means that creates a very very strong positive gamma for the market makers
  indicator: gamma concentration at the money (0DTE) · asset: equities · direction: fade index moves intraday · horizon: days · conditions: near expiry, price near strike · testable: partly · confidence: medium
  ^MT190-C09-1
- **Yoav Git** The 0DTE gamma effect reduces index realised and implied volatility and has turned intraday and one-day equity autocorrelation negative; single stocks are less affected.  #mech/structural_shift
  > the autocorrelation of the intern like in intraday returns or one day returns in in equities have turned negative over time.
  indicator: one-day autocorrelation of equity returns · asset: equities · direction: index vol suppressed · horizon: days · testable: yes · confidence: medium
  ^MT190-C09-2

### C10
- **Yoav Git** Suppressed index volatility makes single-stock futures a better source of diversified risk for trend followers.  #mech/structural_shift
  > there's now more risk available there's in the uh in the single stock versus the the index than it ever has been because the index has been depressed in terms of the volatility.
  indicator: single-stock variance minus index variance · asset: equities · direction: trade single-stock futures · horizon: years · testable: yes · confidence: medium
  ^MT190-C10-1
- **Yoav Git** Demand for single-stock futures is mostly retail wanting to short expensive AI valuations, with limited effect on CTAs.  #mech/crowding_positioning _(time-bound view)_
  > I think what's driving the the single stock futures is more to do with the fact that retails want to short
  asset: equities · testable: no · confidence: low
  ^MT190-C10-2
- **Yoav Git** Launching single-stock futures should not reduce single-stock dispersion because the cause is the index options explosion (0DTE), not the ease of shorting; single-stock options are less liquid and the CME contracts cover only about 50 very liquid names.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > I think that mechanism that causes it is more the options.
  indicator: single-stock dispersion; implied correlation · asset: equities · direction: dispersion stays high · horizon: years · testable: partly - monitor dispersion after the single-stock futures launch · confidence: medium
  ^MT190-C10-X1
- **Yoav Git** Short-dated and weekly option expiries are spreading from equity indices to bond futures and oil, so the options-gamma mechanism that suppresses equity index trends could appear in other markets, with implications for short-term trend following there.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > we've seen a little bit in like in bond futures we've seen that um so we've seen again moving to weekly options at different days expiry um a little bit in oil and stuff like that.
  indicator: weekly option volumes in bond futures and oil · asset: multi · horizon: years · conditions: if option volume in those markets concentrates at-the-money near expiry · testable: yes - test autocorrelation changes as short-dated option volume grows · confidence: low
  ^MT190-C10-X2

### C11
- **Yoav Git** Volatility-adjusted tick size = tick divided by volatility; as the S&P rose from about 1000 (1995) to 7000 the equity vol-adjusted tick shrank, unlike bond futures which stay near 100.  #mech/liquidity_flows
  > the volatility adjusted tick size is basically the size of the tick divided by the volatility of the underlying price.
  indicator: volatility-normalised tick size · asset: equities · horizon: years · testable: yes · confidence: high
  ^MT190-C11-1
- **Yoav Git** The blog gives a mechanism (retail 0DTE selling) complementing the CFM order-book sparsity explanation of why short-term equity trend has declined.  #mech/structural_shift
  > the nature of the players that have entered the market and they are very much playing the anti-trend uh position
  asset: equities · horizon: years · testable: partly · confidence: medium
  ^MT190-C11-2
- **Yoav Git** The CFM tick-size result is driven mainly by cross-asset differences (equities now have a much smaller volatility-adjusted tick than bonds); within each asset class the relationship is more nuanced, so the equity index finding should not be generalised to every market.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > they look at within each asset class what is the variation. uh the picture there is actually a lot more nuanced I would say
  indicator: volatility-adjusted tick size by asset class · asset: multi · horizon: years · testable: yes - replicate the within-asset-class regressions · confidence: medium
  ^MT190-C11-X1

### C12
- **Yoav Git** A 1% fall in one-day autocorrelation costs a 1-day-signal trend follower about 0.16 Sharpe, but a 5/20-day crossover only about 3bp per market (about 6bp across equities), so a 3% fall costs about 0.2 Sharpe for fast traders and little for slower ones.  #mech/structural_shift
  > a 16 basis point sharp negative 16 basis point sharp on your on your uh on your performance right
  indicator: one-day autocorrelation; Sharpe cost · asset: equities · horizon: days · conditions: fast short-term trend followers · testable: yes - back-of-envelope with sqrt(252) · confidence: medium
  **Correction (cross-check):** Unit inconsistency: Git's 'basis points of Sharpe' mean hundredths of a Sharpe ratio (16bp = 0.16, 3bp = 0.03, 6bp = 0.06, about 20bp = 0.2). The first-reader text mixes '0.16 Sharpe' with '3bp' and '6bp', which reads as 0.0003 and 0.0006 Sharpe. → A 1% fall in one-day autocorrelation costs a trader using yesterday's price about 0.16 Sharpe (1% times about 16, the square root of roughly 256 trading days), but a 5/20-day crossover with roughly one-fifth weight on the one-day effect loses only about 0.03 Sharpe per market, or about 0.06 across a lightly diversified equity portfolio; a 3% fall therefore costs about 0.2 Sharpe for short-term traders and much less for slower (two-month) trend followers.
  ^MT190-C12-1
- **Yoav Git** Slower trend followers (2-month horizon) are insulated from intraday microstructure; alpha comes from long-term trends and macro events.  #mech/slow_reaction
  > trends are driven really by macroeconomic events more than just the order book structure.
  asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT190-C12-2
- **Niels Kaastrup-Larsen** Toby Crabel observed that open-to-close follow-through fell from about 58% to about 53-54%, a significant headwind for short-term managers.  #mech/structural_shift
  > markets that generally traded sort of higher at the open in the old days
  indicator: open-to-close follow-through frequency · asset: equities · horizon: days · conditions: short-term traders · testable: yes · confidence: medium
  ^MT190-C12-3
- **Yoav Git** One-day autocorrelation in equity returns has fallen by about three percentage points over roughly 20 years, enough to cost fast equity trend followers about 0.2 Sharpe while leaving slower, macro-driven trend followers largely unaffected.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > we have seen maybe a drop of 3% in autocorrelation in the equity market over over the last 20 years.
  indicator: one-day equity return autocorrelation · asset: equities · direction: short-term equity trend weakens · horizon: years · conditions: applies to short-lookback signals · testable: yes - rolling autocorrelation of index returns · confidence: medium
  ^MT190-C12-X1

### C13
- **Yoav Git** Index explains a shrinking share of single-stock variance (35% to 25-30%); industry plus Barra factors take it to about 50%; themes (news-driven, transient) explain about 5% more, leaving about 45% idiosyncratic.  #mech/structural_shift
  > in the good old days uh the index might have explained 35%. These days it might be explaining 30 or 25%
  indicator: variance decomposition: index, industry, factors, themes · asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT190-C13-1

### C14
- **Yoav Git** Thematic ETFs and bank QIS baskets are mostly exposed to industry, country or standard factors and fail to give pure theme exposure; build pure theme baskets yourself.  #mech/research_method
  > actually sometimes these do not actually capture the volatility.
  indicator: thematic ETFs/QIS orthogonal exposure · asset: equities · testable: yes - orthogonality of theme returns · confidence: medium
  ^MT190-C14-1
- **Yoav Git** Decide how much extra risk single-stock futures, further contracts or themes add before trying to predict returns.  #mech/research_method
  > it's less about prediction. It's really about risk about trying to identify where is the risk coming from
  indicator: risk decomposition · asset: multi · testable: partly · confidence: medium
  ^MT190-C14-2

### C15
- **Yoav Git** Narrative momentum (Satka et al., 13.3m articles, 2012-2023): slow-evolving themes show underreaction over about 6 months, and trend-following the news (stock beta to narrative) earns money distinct from price momentum.  #mech/slow_reaction
  > there is the underreaction like it takes time for uh for investors and we are very familiar with that.
  indicator: narrative / news theme exposure · asset: equities · direction: long stocks with rising narrative exposure · horizon: months · conditions: themes evolving slowly · testable: yes · confidence: medium
  ^MT190-C15-1
- **Yoav Git** Estimating stock-to-narrative beta is noisy when only about 5% of volatility is narrative-driven, so basket construction has large estimation error.  #mech/research_method
  > to understand what the beta or the correlation between uh a certain stock and a narrative. It's a much more difficult exercise
  indicator: narrative beta estimation · asset: equities · testable: yes · confidence: medium
  ^MT190-C15-2
- **Yoav Git** Narrative underreaction has a rational explanation: with incomplete information, investors infer value from price moves and from what others discuss, so slow-moving themes diffuse gradually; fast, obvious themes such as war are priced instantly and show no lag.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > in the absence of complete information in the market, the fact that the price has gone up or the fact that other people are talking about a theme actually makes you evaluate your own valuation
  indicator: news theme diffusion · asset: equities · direction: trend-follow slow-evolving narratives · horizon: months · conditions: slow-evolving themes only; instant for obvious shocks such as war · testable: yes - test underreaction by theme speed · confidence: medium
  ^MT190-C15-X1

### C16
- **Yoav Git** AI and machine learning now process news instantly, so the news underreaction/narrative momentum edge is likely to disappear quickly.  #mech/structural_shift _(time-bound view)_
  > with the rise of AI with the rise of our ability to harvest text and news
  asset: equities · horizon: years · testable: partly · confidence: medium
  ^MT190-C16-1
- **Niels Kaastrup-Larsen** Agentic AI personalises news, so narrative truth becomes individual and may bias trading.  #mech/behavioral _(time-bound view)_
  > it's actually being generated for each of us individually.
  asset: multi · horizon: years · testable: no · confidence: low
  ^MT190-C16-2
- **Yoav Git** Equity index futures cover only about 30% of harvestable equity risk; medium and long-term equity trend remains fine.  #mech/structural_shift
  > equity index futures uh that we understand now covers about 30% of the equity risk that is available to harvest.
  asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT190-C16-3
- **Yoav Git** Because statistical stock-to-narrative betas are noisy, one bank's QIS theme baskets add a human overlay (for example judging that Coca-Cola benefits from the World Cup even if it is not visible in price), which is sensible economically but non-quantitative and hard for a systematic manager to trade.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > I actually like the way that they do an uh a human overlay of the basket for the themes that they're doing.
  indicator: QIS thematic baskets · asset: equities · horizon: months · testable: partly - human-curated basket construction cannot be replicated systematically · confidence: medium
  ^MT190-C16-X1

### C17
- **Yoav Git** Equity trend diversification layers: index, industry (avoid double counting, e.g. semiconductors vs S&P), Barra-style factors, narrative; construction and normalisation are hard, but the result can be nearly uncorrelated to index trend.  #mech/risk_management
  > you don't want to double count right because you right. So like at the moment trading the semiconductors and the SMB you are basically trading the same thing.
  indicator: index, sector, factor and theme trend components · asset: equities · direction: build diversified equity trend with sector, factor and theme components · horizon: months · testable: yes · confidence: medium
  ^MT190-C17-1
- **Yoav Git** Narrative-based equity trend is harder than the other layers because the narrative covers only about 5% of variance and its identity keeps changing, so a manager has to track both the trend and which risk factor is currently live.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > you're not just catching up to trend you're also catching up to the risk factor which is trading right now.
  indicator: narrative risk factor · asset: equities · horizon: months · testable: partly - requires a point-in-time news dataset · confidence: medium
  ^MT190-C17-X1

