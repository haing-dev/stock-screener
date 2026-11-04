---
source_id: MT216
title: "Why Smart Investors Are Switching to Trend Following - Systematic Investor 334"
date: 2025-02-14
channel: "Top Traders Unplugged"
url: 
words: 10727
claims: 52
added_by_crosscheck: 9
corrections: 2
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Niels Kastrup-Larsen (host, Top Traders Unplugged)", "Nick Baltas (co-host, systematic researcher)"]
tags: [source, layer0]
---
# Why Smart Investors Are Switching to Trend Following - Systematic Investor 334

**Speakers:** Niels Kastrup-Larsen (host, Top Traders Unplugged); Nick Baltas (co-host, systematic researcher)

**Summary:** Top Traders Unplugged weekly: early-2025 trend following conditions (flat January, weak February), crypto liquidation and crowding, safe-equities-as-bond-alternative paper, price vs narrative, and the Harvey et al rebalancing cost paper. Conclusion: combine contractual hedges, trend and carry; avoid calendar rebalancing; trend following suits a narrative-driven market.

**Approach:** trend following, cross-sectional carry/reversion, risk mitigation, rebalancing

**Cross-check completeness estimate of first read:** 0.85 - the first reader caught the main topics (crypto/crowding, trend conditions, hedging mix, safe equities, narrative vs price, rebalancing paper) and missed the performance index data, the valuation-definition argument, trend from forced liquidations, and the rebalancing/front-running points.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | Intro, disclaimers; DeepSeek / AI banter - nothing actionable |
| C02 | 2 | DeepSeek volatility; Vanguard fees; crypto liquidation and exit liquidity |
| C03 | 4 | Fire-sale contagion, crowding, conservative design |
| C04 | 4 | MicroStrategy buying, crowding measure, crypto supply dynamics |
| C05 | 6 | Bitcoin vs inflation, Bessent bonds, trend follower conditions early 2025, performance |
| C06 | 2 | Coffee streak; index performance figures; carry and skew cross-sectional trades |
| C07 | 3 | Uncertainty, defensive demand, trend as strategic allocation |
| C08 | 3 | Contractual vs statistical hedges, commodity curve carry |
| C09 | 4 | Trend and put hedges, stock-bond correlation, Safe Equities paper |
| C10 | 3 | Safe equities critique, diversification only absolute return |
| C11 | 3 | Disguised equity, price vs value breakdown, efficiency |
| C12 | 2 | Valuation definition, themes, narratives |
| C13 | 3 | No risk premium in themes, uncertainty creates trends, Fed put |
| C14 | 1 | Price vs narrative, rebalancing cost paper (Harvey) |
| C15 | 3 | Rebalancing paper details, avoiding calendar rebalancing |
| C16 | 0 | Outro, next week preview - nothing actionable |

## Claims

### C02
- **Niels Kastrup-Larsen** A forced liquidation of about $10bn of leveraged crypto longs (ETH -20% in a day) shows crypto lacks exit liquidity, so a systematic futures trader should require that a market cannot gap 20%+ in a day before trading it.  #mech/liquidity_flows _(time-bound view)_
  > we may have seen the largest crypto Liquidation in history uh it's estimated from from the news channels that I uh noticed it from that about 10 billion or so of Leverage Longs were stopped out
  indicator: crypto leveraged long liquidations · asset: other · horizon: days · conditions: applies to markets not trading 24/7 on futures exchanges · testable: partly - exit-liquidity screens can be defined · confidence: medium
  ^MT216-C02-1
- **Niels Kastrup-Larsen** Fee cuts at Vanguard continue the race to the bottom in ETF fees, which pressures CTA ETFs, some of which have in fact raised fees.  #mech/structural_shift
  > Vanguard slashed the fees on uh lots of their mutual funds and exchange traded funds ETFs which is interesting
  indicator: ETF fee levels · asset: multi · horizon: years · testable: no - industry observation · confidence: medium
  ^MT216-C02-2
- **Nick Baltas** DeepSeek-style cheaper model training does not remove the need for GPUs, but it may open AI development to a broader set of players, so the implication for the AI hardware trade is unclear.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > my personal view is that we will still be using gpus to train those models and maybe it's become now cheaper but maybe it's now more open to a broader set of of players
  asset: equities · testable: no - speculative technology view · confidence: low
  ^MT216-C02-X1

### C03
- **Nick Baltas** Large levered positions across seemingly unrelated themes are dangerous because an unrelated shock causes synchronous fire sales and contagion between them.  #mech/crowding_positioning
  > the primary danger of building big positions leved positions um across seemingly other related themes or strategies or or or or Investments
  asset: multi · horizon: days · testable: partly - correlation in stress can be measured · confidence: high
  ^MT216-C03-1
- **Nick Baltas** Investors with similar portfolios and utility functions (e.g. pension funds) react synchronously to a macro shock, creating a vicious circle of fire sales and indirect contagion.  #mech/crowding_positioning
  > investors that are perhaps having similar utility function let's call it in the pension Community um that have similar portfolios but then act in a synchronous manner to a macro shock can create a spillover effect
  asset: multi · horizon: weeks · testable: partly - academic evidence exists · confidence: medium
  ^MT216-C03-2
- **Nick Baltas** Systematic strategy design should be more conservative than historical data suggest because externalities such as who else trades the same signal with the same parameters cannot be quantified.  #mech/risk_management
  > we always try to erir in the I guess in the side of caution um and try to be even more conservative than what historical data suggest
  asset: multi · testable: no - design principle · confidence: high
  ^MT216-C03-3
- **Nick Baltas** For crowded systematic trades the larger risk is a forced liquidation event, not ordinary execution slippage.  #mech/crowding_positioning
  > I think the biggest problem would be in a in in a force liquidation event I think that's the bigger danger here uh which is more systemic
  asset: multi · horizon: days · testable: partly · confidence: medium
  ^MT216-C03-4

### C04
- **Niels Kastrup-Larsen** A single price-insensitive buyer (MicroStrategy added about $20bn of Bitcoin in Q4) supports price, so when the buying stops Bitcoin loses its continuous bid.  #mech/liquidity_flows _(time-bound view)_
  > they had basically doubled the number of Bitcoins they own uh in the fourth quarter to about 471 th000 Bitcoins
  indicator: MicroStrategy Bitcoin holdings · asset: other · direction: downside risk to Bitcoin when buyer stops · horizon: months · testable: partly - holdings are public · confidence: medium
  ^MT216-C04-1
- **Nick Baltas** Crowding measured by number of owners has different implications than crowding measured by position size, because many small holders can act synchronously.  #mech/crowding_positioning
  > it's more important to see how many uh investors own a specific stock or a specific I don't know Bitcoin in that case um instead of looking into the size of the
  indicator: number of owners vs position size · asset: multi · testable: yes - ownership counts measurable · confidence: low
  ^MT216-C04-2
- **Niels Kastrup-Larsen** Equities have shrinking share supply through buybacks while crypto supply of coins expands without limit, so a capped Bitcoin supply does not make crypto broadly scarce or an inflation hedge.  #mech/structural_shift
  > in the equity space for example you've seen many many large companies actually buy back shares so essentially there are much fewer shares to buy today than there were 10 years ago in the crypto space the completely opposite
  indicator: share count vs coin count · asset: other · horizon: years · testable: partly · confidence: medium
  ^MT216-C04-3
- **Niels Kastrup-Larsen** Bitcoin is a narrative-driven asset rather than an inflation hedge: it doubled while inflation fell and did not hedge in 2022.  #mech/behavioral
  > I don't really see that there is a strong relation between Bitcoin and inflation because uh the most recent rally of course has happened at a time
  indicator: Bitcoin vs inflation · asset: other · horizon: years · testable: yes - correlation with inflation measurable · confidence: medium
  ^MT216-C04-4

### C05
- **Niels Kastrup-Larsen** The Treasury Secretary's focus on lowering bond yields signals a policy aim of lower yields, which coincided with a drop in US yields, though the move may instead reflect risk aversion.  #mech/policy_reaction _(time-bound view)_
  > first comments we're getting from the new treasury secretary AR Scott bessent when he talked about bonds that actually they should be more focused on the yield on bonds getting that down
  indicator: US Treasury yields · asset: rates · horizon: weeks · testable: no - policy intent unclear · confidence: low
  ^MT216-C05-1
- **Nick Baltas** Bonds have underperformed for about 5 years, and trend followers have not profited because there has been no sustained bond trend.  #mech/cycle_persistence
  > bonds have disappointed now for a prolonger period of time
  indicator: bond trend · asset: rates · horizon: years · testable: yes · confidence: medium
  ^MT216-C05-2
- **Nick Baltas** Over the last year the price pattern hit 90 to 120 day trend horizons hard, as long signals at that speed reversed repeatedly.  #mech/slow_reaction _(time-bound view)_
  > every time you get a long signal around that that time frame which a lot of our peers would get the markets turn and it flips and so it's it's been difficult
  indicator: 90-120 day trend signal · asset: multi · horizon: months · conditions: medium-speed trend following suffered in 2024-25 · testable: yes - speed-specific backtest · confidence: medium
  **Correction (cross-check):** Speaker likely wrong. The comment that the last year's price pattern hit 90 to 120 day horizons hard comes from the host (Niels), who goes straight on to the year-to-date performance review and his own trend barometer; Nick's contribution in this passage is the bond underperformance remark. → Niels Kastrup-Larsen: over the last year or so price moves have hit roughly 90 to 120 day trend horizons hard, so long signals at that speed (which many peers share) kept reversing; he adds that trend followers have not timed bond shifts because there has been no real bond trend.
  ^MT216-C05-3
- **Niels Kastrup-Larsen** In early 2025 a bond rebound, soft European equities and a weaker dollar after a post-election rally together hurt trend followers (January flat, February down).  #mech/slow_reaction _(time-bound view)_
  > the dollar has weakened a bit that's Al also been a difficult combination for for Trend followers
  indicator: SG CTA / trend index returns · asset: multi · horizon: weeks · testable: partly - descriptive · confidence: medium
  ^MT216-C05-4
- **Niels Kastrup-Larsen** A trend barometer reading of 30 indicates trend followers are performing weakly.  #mech/slow_reaction _(time-bound view)_
  > my own Trend barometer finished uh yesterday at 30 so that's definitely uh suggesting a weak start to February
  indicator: Trend Barometer · asset: multi · horizon: weeks · testable: yes - indicator defined · confidence: medium
  ^MT216-C05-5
- **Niels Kastrup-Larsen** Coffee had its longest winning streak since 1970 (up 112% in 12 months), an outlier trend in soft commodities that helps trend followers.  #mech/cycle_persistence _(time-bound view)_
  > it's actually making uh I think it's the 11th consecutive rise yesterday which is the longest winning streak since 1970
  indicator: coffee futures · asset: commodities · direction: long coffee · horizon: months · testable: yes · confidence: medium
  ^MT216-C05-6
- **Nick Baltas** The recent drop in US yields reflected investor risk aversion, but if tariffs and other Trump policies play out they could push inflation and yields up instead, so the yield direction is open.  #mech/policy_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > somebody could argue that you know there's more of an inflationary
  indicator: US Treasury yields · asset: rates · direction: yields down on risk aversion; yields up if tariffs are inflationary · horizon: months · conditions: depends on whether tariffs are implemented · testable: no - open scenario view · confidence: low
  ^MT216-C05-X1

### C06
- **Nick Baltas** Cross-sectional carry in commodities, especially strong backwardation, gave a very strong start to the year and diversified trend following.  #mech/risk_premium _(time-bound view)_
  > more cross-sectional trades that actually play out quite nicely um and in this particular way looking into some car Dynamic specifically in the commodity sector
  indicator: cross-sectional commodity carry / backwardation · asset: commodities · direction: long backwardated, short contango commodities · horizon: months · testable: yes · confidence: medium
  ^MT216-C06-1
- **Nick Baltas** Cross-sectional reversion signals based on realized skewness in futures performed very strongly early in the year and diversify trend following.  #mech/overshoot _(time-bound view)_
  > we've discussed about you know realized skewness and some of those measures that try to build crosssectional reversion Dynamics within the universe of of of Futures
  indicator: realized skewness cross-sectional reversion · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT216-C06-2
- **Niels Kastrup-Larsen** Early-2025 data point: SG CTA about -91bp in February (-30bp YTD), SG Trend -92bp (-77bp YTD), short-term traders -1.19% (-1.15% YTD) and BTOP50 -35bp (+59bp YTD), while MSCI World was +3.8%, long Treasuries +3% and the S&P 500 total return +3.15% YTD, so CTA indices lagged both stocks and bonds in the first five weeks.  #mech/new _(added by sonnet-xhigh cross-check, time-bound view)_
  > the trend index almost the same down 92 basis points so far in February down 77 basis points so far this year and the short-term Traders index down 1.19% and down 1.15% so far uh this year
  indicator: SG CTA Index; SG Trend Index; SG Short-Term Traders Index; BTOP50; MSCI World; US 20y+ Treasury index; S&P 500 TR · asset: multi · horizon: weeks · conditions: January to early February 2025 only · testable: yes - index data · confidence: high
  ^MT216-C06-X1

### C07
- **Nick Baltas** Policy uncertainty (tariffs, AI frenzy reversals) shifts allocators from carry trades toward defensive positioning, increasing interest in trend following.  #mech/behavioral _(time-bound view)_
  > this uncertainty um builds up a bit of risk aversion
  asset: multi · horizon: months · testable: no · confidence: low
  ^MT216-C07-1
- **Nick Baltas** Trend following cannot be timed; the case for it is as a permanent component.  #mech/research_method
  > is it the time to do trend is one of the questions and classically the answer is you cannot time it
  asset: multi · testable: yes - market timing of trend can be tested · confidence: medium
  ^MT216-C07-2
- **Nick Baltas** Investors are moving from using trend following only as a defensive overlay to a strategic allocation because bonds disappointed and the equity-bond correlation may not fall if inflation tensions persist.  #mech/structural_shift _(time-bound view)_
  > Trend following could be seen now as a component of a strategic allocation it starts becoming a reality
  indicator: equity-bond correlation · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT216-C07-3

### C08
- **Nick Baltas** Contractual hedges such as long-volatility or option structures cover sharp corrections but not an equity-bond correlation shock or prolonged drawdowns, where trend following helps.  #mech/risk_management
  > more contractual Hedges cannot necessarily help in prolonged drawdowns
  asset: multi · direction: options for flash corrections, trend following for correlation shocks · horizon: years · testable: partly · confidence: high
  ^MT216-C08-1
- **Nick Baltas** A defensive overlay should combine contractual hedges (short delta, long vol), dispersion, trend following and carry or market-neutral components, since each covers a different drawdown type.  #mech/risk_management
  > that does address the need for a Sharp correction but it does not address the need for an equity Bond correlation shock and this is now when Trend Following comes into play
  asset: multi · testable: partly · confidence: high
  ^MT216-C08-2
- **Nick Baltas** Holding the back of commodity curves and shorting the front earns long-run carry while avoiding negative roll yield, and helps in drawdowns without an inflationary recession shock.  #mech/risk_premium
  > this classical way of allocating into Commodities on the back end of commodity curves and then shortening the front to avoid having the negative Ro yield
  indicator: commodity curve carry (long back, short front) · asset: commodities · direction: long back / short front of commodity curve · horizon: years · conditions: helps in equity drawdowns not driven by an inflationary shock · testable: yes · confidence: medium
  ^MT216-C08-3

### C09
- **Nick Baltas** Trend following is a transparent defensive tool: it cuts equity exposure in downtrends in a rule-based way, which makes it easy to explain to investors.  #mech/slow_reaction
  > if you really want it to be more defensive cut down your Equity exposure in up moves it's pretty clear
  indicator: price trend · asset: equities · direction: reduce equity exposure on down moves · horizon: months · testable: yes · confidence: high
  ^MT216-C09-1
- **Nick Baltas** Put hedging requires implementation choices (frequency, splitting notional over days, strike, financing with another option) and becomes complex once multiple components need sizing against the portfolio.  #mech/risk_management
  > how should you buy this SP option and you know in what frequency and can you do this thing every single day and split your National
  indicator: S&P put options · asset: equities · testable: yes · confidence: medium
  ^MT216-C09-2
- **Niels Kastrup-Larsen** The 2000-2020 negative stock-bond correlation was the exception; historically the correlation is mostly positive, so a return to positive correlation is normal.  #mech/structural_shift
  > stocks and bonds are actually more often positively correlated than negatively correlated
  indicator: stock-bond correlation · asset: multi · horizon: years · testable: yes - long history of stock-bond correlation · confidence: high
  ^MT216-C09-3
- **Nick Baltas** Equities plus bonds worked because they hold the equity and term premia and diversified each other in equity drawdowns.  #mech/risk_premium
  > you are exposed to the two most fundamental uh risk premium out there the equity risk premium and the
  indicator: equity risk premium, term premium · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT216-C09-4

### C10
- **Nick Baltas** Stock-bond correlation turns positive mainly in inflation shocks when both fall, which destroys the diversification that justified a 60/40.  #mech/policy_reaction
  > positive correlation is more when they both go down primarily driven by inflation shocks
  indicator: stock-bond correlation, inflation · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT216-C10-1
- **Nick Baltas** Safe equities (top 30% by safety) fell far less than the market in the 2000-02 bear market (-1.7% vs about -14.7%), but still lost money so they are not a bond replacement.  #mech/risk_management
  > the average annual Market return was minus 14
  indicator: low-beta / high-quality 'safe equities' factor · asset: equities · direction: tilt equity sleeve to safe stocks but not as absolute defense · horizon: years · testable: yes - Penman and Zhu paper · confidence: medium
  **Correction (cross-check):** The figures are garbled in the transcript ('a down Market of 2202', 'minus 14 4.73') and the claim states them as fact: the period could be 2002 or 2000-02 and the market return -14.73% or -4.73% per year. → Safe equities (top 30% by a safety measure) lost only about 1.7% a year in the early-2000s equity bear market versus a larger average market loss (transcript reads 'minus 14 4.73', exact figure and period uncertain), but they still lost money in absolute terms.
  ^MT216-C10-2
- **Nick Baltas** A true defensive allocation should produce absolute positive returns in a down market, which safe equities with beta around 0.8 do not.  #mech/risk_management
  > a defensive strategy should actually add an absolute positive return
  indicator: safe equities beta · asset: equities · horizon: years · testable: yes · confidence: high
  ^MT216-C10-3

### C11
- **Niels Kastrup-Larsen** Portfolios believed to be diversified are 85-90% equity risk in disguise (long-short equity, private equity), so true diversification needs other asset classes.  #mech/risk_management
  > 85 to 90% of it is actually short wall it's just it just called different things
  indicator: equity beta share of risk · asset: multi · testable: yes - decompose risk into equity beta · confidence: medium
  ^MT216-C11-1
- **Niels Kastrup-Larsen** Prices are now driven more by narrative and speculation than value, so price-only strategies like trend following are more relevant than valuation analyses calibrated on history.  #mech/behavioral
  > prices are much more driven by narratives by speculation by manipulation for that matter
  asset: multi · direction: favour trend following over value · horizon: years · testable: partly - value signal decay testable · confidence: medium
  ^MT216-C11-2
- **Nick Baltas** Trend following working at all is a soft rejection of market efficiency: past prices contain information about future prices.  #mech/slow_reaction
  > by having historical price movements giving us a bit of a hint as to where the price will go is in itself a soft I guess negation of
  indicator: price trend · asset: multi · testable: yes · confidence: medium
  ^MT216-C11-3

### C12
- **Nick Baltas** Thematic trends are a journey from one valuation level to another that takes time because information diffuses gradually, which is the source of price trends.  #mech/slow_reaction
  > temporary out performance which is precisely what TR following tries to achieve by the way right is just a journey that takes you from some valuation level to the new valuation level
  asset: equities · horizon: months · testable: partly · confidence: medium
  ^MT216-C12-1
- **Nick Baltas** Themes (AI, ageing) reduce dimensionality like old factors (value, momentum) but carry no risk premium; they cause overconfidence and overreaction followed by correction, as with the DeepSeek hit to Nvidia.  #mech/overshoot _(time-bound view)_
  > I do see from your perspective I guess the way that you kind of did the preamp in the conversation that narratives seem to be having having a bigger role
  indicator: thematic investing · asset: equities · horizon: weeks · testable: partly · confidence: medium
  ^MT216-C12-2
- **Nick Baltas** If value signals stop working it may be the definition of value that is outdated (intangibles, brand, a different type of measure) rather than valuation itself being uninformative, so the response is to update the measure before dropping the idea.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > is it that valuation itself is not informative of price movements or we should take a step back and challenge our own definition valuation
  indicator: valuation measures incl. intangibles-adjusted value · asset: equities · horizon: years · conditions: equity markets over roughly the last decade · testable: partly - alternative value definitions can be backtested · confidence: medium
  ^MT216-C12-X1
- **Nick Baltas** A narrative can lift a price only while demand lasts, and demand exists only if investors anticipate future performance, so narrative-driven prices are still tied to expected fundamentals and drop when that anticipation fades.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > unless there is enough demand for it the price will naturally drop and demand will only be there if there is some form of anticipation of our performance going forward
  asset: equities · testable: no - theoretical argument · confidence: medium
  ^MT216-C12-X2

### C13
- **Nick Baltas** Themes offer short-term predictable price movement, not a risk premium, because information is digested gradually.  #mech/slow_reaction
  > there is no risk Prem associated with the with the themes but what there is is shortterm price movement
  asset: equities · horizon: months · testable: partly · confidence: medium
  ^MT216-C13-1
- **Nick Baltas** Broad uncertainty about valuation makes prices informative so investors learn continuously, creating trends; when certainty is high, as during the Fed put period up to 2020, trend followers did worse in rising equity markets.  #mech/policy_reaction
  > broader uncertainty about outcomes is the one that creates Trends because because broad uncertainty about how something should be valued suggest that price movements contain information
  asset: multi · horizon: years · conditions: trend following weaker when a central bank put anchors expectations · testable: partly · confidence: medium
  ^MT216-C13-2
- **Niels Kastrup-Larsen** Trend following does not need to explain price, so it does not depend on trustworthy news or valuation narratives and may do relatively well in a speculation-driven market.  #mech/slow_reaction
  > we don't need to know what made the price go to this level we just need to know that that's what it did
  asset: multi · testable: no · confidence: medium
  ^MT216-C13-3
- **Niels Kastrup-Larsen** Large price swings without a clear change in the business (Novo Nordisk at about half its price of six months earlier, the long Tesla valuation debate) are cited as evidence that price is subjective, which favours a strategy that follows price without justifying it.  #mech/behavioral _(added by sonnet-xhigh cross-check, time-bound view)_
  > I can be surprised when I see someone like a Danish company like Nova nordis which has obviously had very much success and six months ago the price was like twice the price now
  asset: equities · horizon: months · conditions: single-stock examples from early 2025 · testable: no - anecdotal examples · confidence: medium
  ^MT216-C13-X1

### C14
- **Nick Baltas** Scheduled rebalancing of fixed-weight portfolios (60/40) is predictable and front-run by fast money, costing pension funds roughly 8bp a year on $20tn, about $16bn (Harvey et al).  #mech/liquidity_flows
  > there is a cost for um investors who do rebalancing uh of their portfolios and just to read what was on Bloomberg it says now a group of academics claim
  indicator: month-end / quarter-end rebalancing flows · asset: multi · horizon: weeks · testable: yes - paper estimates cost · confidence: medium
  ^MT216-C14-1
- **Nick Baltas** Besides slow digestion of news, trends can be generated endogenously by forced liquidations and stop-loss rules, which is a price-based mechanism that links trend following to the rebalancing and fire-sale discussion.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check)_
  > liquidation events or can be seen by stoploss rules playing out um so there are those Dynamics which are more like no price based uh or more I guess endogenous in the in the investment process
  asset: multi · direction: trends extend when forced selling or stops cluster · horizon: days · conditions: liquidation events · testable: partly - hard to isolate forced flows · confidence: medium
  ^MT216-C14-X1
- **Nick Baltas** Rebalancing a fixed-weight portfolio such as 60/40 is mechanically contrarian (sell what rose, buy what fell), equivalent to a value trade and the opposite of trend following.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check)_
  > when you follow a fixed weight portfolio and clearly the best example is a 6040 mhm you end up selling when something goes up and we end up buying when something Falls
  indicator: 60/40 portfolio weights vs target · asset: multi · direction: sell winners, buy losers at rebalance dates · horizon: months · conditions: fixed-weight portfolios on a calendar · testable: yes - portfolio arithmetic · confidence: high
  ^MT216-C14-X2

### C15
- **Nick Baltas** Before rebalancing a 60/40 back to target, check the trend and do not buy falling equities while the negative trend continues (Harvey et al with Man Group).  #mech/slow_reaction
  > if your equities are falling as in the 60 yeah becomes 50 then don't yet buy if that negative Trend continues
  indicator: trend signal for rebalancing · asset: equities · direction: delay buying equities in downtrend · horizon: months · testable: yes · confidence: medium
  ^MT216-C15-1
- **Nick Baltas** Systematic managers should avoid month-end and quarter-end rebalancing schedules: rebalance frequently, consider where liquidity sits and partially rebalance using thresholds.  #mech/risk_management
  > we try to be more frequent we try to be more thoughtful of where liquidity sits and maybe at times we only partially rebalance the portfolio rather than the whole lot
  asset: multi · testable: yes · confidence: medium
  ^MT216-C15-2
- **Nick Baltas** Trend following acts systematically and off the calendar, so it can run alongside slow, committee-driven asset-allocation portfolios and avoid front-running.  #mech/risk_management
  > Trend following strategies can also operate alongside as location portfolios because they act typically at no motion
  asset: multi · testable: no · confidence: low
  ^MT216-C15-3
- **Nick Baltas** Any product with scheduled rebalancing, including ETFs, is exposed to front-running by fast money; the paper finds no easy way around this and treats it as the price of the rebalancing rule, which makes it a regulatory concern.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check)_
  > we can think about ETFs for instance that have a very scheduled rebalancing activity they can be exposed to front running and I think this is an important consideration also for Regulators
  asset: multi · direction: front-runners profit at the expense of the rebalancer · horizon: days · conditions: predictable rebalancing dates · testable: partly - front-running cost estimated in the paper · confidence: medium
  ^MT216-C15-X1

