---
source_id: MT144
title: "Should You Just Buy a CTA Index- - Systematic Investor 312"
date: 2024-09-11
channel: "Top Traders Unplugged"
url: 
words: 15211
claims: 64
added_by_crosscheck: 14
corrections: 1
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Niels Kaastrup-Larsen (host, Top Traders Unplugged)", "Rob Carver (independent systematic futures trader, author)"]
tags: [source, layer0]
---
# Should You Just Buy a CTA Index- - Systematic Investor 312

**Speakers:** Niels Kaastrup-Larsen (host, Top Traders Unplugged); Rob Carver (independent systematic futures trader, author)

**Summary:** Systematic Investor 312 (Sept 2024) with Rob Carver answering listener questions on macro momentum, diversification multipliers, ATR stop losses and small accounts, then discussing a US strategic Bitcoin reserve, what ETFs really are (creation/redemption, leveraged ETP risk) and whether to just buy a CTA index (Transtrend paper; new investable SG CTA index based on a replication engine).

**Approach:** trend following, portfolio construction, position sizing, stop losses, ETF mechanics, CTA index replication, Bitcoin, systematic discipline

**Cross-check completeness estimate of first read:** 0.80 - first reader captured the main Carver method points (correlation over Sharpe, IDM/FDM, stop-loss decoupling, ETF mechanics, Transtrend debate) and the dated views (about 53 of roughly 67 ideas); missed supporting numbers, the host-guest disagreement on breadth, retail-leverage ETP logic, ETF fund-structure mechanics and the backtest-as-index precedent

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 2 | intro, Carver's current positions and low risk in drawdown |
| C02 | 1 | leaving the system untouched during a drawdown |
| C03 | 1 | detachment from news, why systematic suits most people |
| C04 | 4 | US unemployment/Fed view, Sept 2024 trend sector moves, three reasons to cut risk |
| C05 | 3 | drawdown-based risk scaling, trend index stats, macro momentum question and latent factors |
| C06 | 4 | asset-class momentum share of P&L, adding a lower-Sharpe strategy: use correlation |
| C07 | 3 | correlation rules for adding strategies, diversification multipliers (IDM/FDM) |
| C08 | 2 | hierarchical portfolio construction, stop-loss dual role problem start |
| C09 | 3 | separate position size from holding period; ATR stops and holding times |
| C10 | 3 | small accounts need $100k, Bitcoin strategic reserve effects |
| C11 | 2 | Fed balance sheet and Bitcoin flows, taxes and why Bitcoin cannot be money |
| C12 | 1 | US dollar advantage opinion, Bitcoin ETF holder data, gold, active ETFs intro |
| C13 | 2 | active ETF size, ETF as regulated wrapper, open vs closed fund structure |
| C14 | 0 | open-end mechanics, closed-end funds, ETF as hybrid |
| C15 | 2 | authorized participants, creation/redemption, ETF can hold anything |
| C16 | 2 | MicroStrategy 3x ETP, ETF due diligence, new CTA index introduced |
| C17 | 2 | Transtrend paper: stock index vs CTA index as factor exposure, pick winners vs index |
| C18 | 3 | CTA manager diversification, limits of stock-index analogy |
| C19 | 4 | more markets, nonlinearity, SG CTA index breadth, purposes of an index |
| C20 | 4 | ETFs for retail, bottom-up replication, fewer than 20 markets cannot deliver index |
| C21 | 1 | back-test as public track record risk |
| C22 | 1 | bottom line: understand what is inside any ETF; outro |

## Claims

### C01
- **Rob Carver** Sept 2024 snapshot of Carver's trend system after a poor few months: long equities and bonds (a risk-parity-like stance) and short gas and agricultural markets.  #mech/cycle_persistence _(time-bound view)_
  > I'm currently long equities long bonds um and short um some sort of gas and agricultural markets
  indicator: own system positions · asset: multi · direction: long equities and bonds, short gas and ags · horizon: months · testable: no - one-off snapshot · confidence: high
  ^MT144-C01-1
- **Rob Carver** In a drawdown models find weak forecasts and many markets have low volatility, so a volatility-targeted trend system runs low risk.  #mech/risk_management
  > running quite low risk at the moment is what we'd expect in the middle of a draw down
  asset: multi · horizon: weeks · conditions: during drawdowns · testable: yes - risk level vs drawdown can be tested · confidence: high
  ^MT144-C01-2

### C02
- **Rob Carver** Leaving the system alone is easier when away; the main temptation in a drawdown is to fiddle with the system.  #mech/behavioral
  > the big Temptation when you're losing money is to change your system and change your strategy and Fiddle with things
  asset: multi · conditions: during drawdowns · testable: no - behavioural discipline · confidence: high
  ^MT144-C02-1
- **Rob Carver** Confidence to leave a system running through a drawdown (his current one roughly equals his worst in ten years) comes from having written and understood the code, and from it being his own money with no fiduciary duty; the longer he trades the less attention he pays to daily market noise.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > I have enough trust in I mean it helps that it's my code I've written it it's my trading strategy I understand everything that's going into it
  asset: multi · conditions: own code, own capital · testable: no - psychological · confidence: high
  ^MT144-C02-X1

### C03
- **Rob Carver** Systematic trading suits most people because detached emotion is very hard for discretionary traders.  #mech/behavioral
  > systematic trading suits me and probably most people out there um better than than discretionary
  asset: multi · testable: no · confidence: medium
  ^MT144-C03-1
- **Rob Carver** Sept 2024 datum: the US yield curve had just dis-inverted, with 10-year yields back above 2-year yields.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > the US yield curve is just dis inverted so 10 year yields now above two-year yields which is the kind of quote unquote correct way around
  indicator: US 10y minus 2y yield curve · asset: rates · horizon: months · testable: yes - public series · confidence: high
  ^MT144-C03-X1

### C04
- **Niels Kaastrup-Larsen** Sept 2024 view: US unemployment data (due that day) would set the Fed path; soft data since April; he expected 25bp cuts at each of the three remaining meetings.  #mech/policy_reaction _(time-bound view)_
  > I wouldn't be surprised if they just do 25 basis points at each of the next three meetings
  indicator: US unemployment report, Fed funds · asset: rates · horizon: months · testable: no - market view · confidence: low
  ^MT144-C04-1
- **Niels Kaastrup-Larsen** First week of Sept 2024: falling equities hurt long-biased trend followers while rising bonds helped, and a grain correction hurt short positions.  #mech/cycle_persistence _(time-bound view)_
  > equities uh are down in price but they're also hurting Trend followers
  indicator: trend follower sector exposure · asset: multi · horizon: weeks · testable: no - episode description · confidence: medium
  ^MT144-C04-2
- **Niels Kaastrup-Larsen** Direction flips in major sectors in August 2024 changed correlations and triggered broad risk reduction in CTA portfolios.  #mech/crowding_positioning _(time-bound view)_
  > August may have been the month that tricked a lot of risk reduction overall in CTA portfolios
  indicator: CTA risk reduction, correlations · asset: multi · horizon: months · conditions: when sectors flip together · testable: partly - CTA risk levels observable · confidence: medium
  ^MT144-C04-3
- **Rob Carver** A trend system reduces risk for three reasons: trends turn against you (continuous forecast or stop loss), volatility rises (for vol-targeted systems), and you are losing money.  #mech/risk_management
  > you basically reduce risk for two reasons one one reason being that you you know the trends turn against you
  indicator: forecast strength, volatility, equity drawdown · asset: multi · direction: reduce positions · horizon: weeks · testable: yes - mechanical rules · confidence: high
  ^MT144-C04-4

### C05
- **Rob Carver** Scale positions with account value: after a 10% loss cut positions by 10% (open or closed trade equity).  #mech/risk_management
  > if you lose 10% of your of you know of your account value then you should reduce your positions by 10% even if nothing else has changed
  indicator: account equity · asset: multi · direction: reduce positions proportionally to equity loss · horizon: days · testable: yes - equity-based risk scaling is backtestable · confidence: high
  ^MT144-C05-1
- **Niels Kaastrup-Larsen** Trend barometer 50 on 5 Sept 2024 with SG indices up about 1-2.5% YTD; MSCI World +12.6%, S&P 500 +15.4%.  #mech/cycle_persistence _(time-bound view)_
  > it finished at 50 yesterday so that's actually a pretty good number
  indicator: Trend barometer, SG CTA/Trend/Short-term Traders indices · asset: multi · horizon: months · testable: no - snapshot · confidence: medium
  ^MT144-C05-2
- **Rob Carver** Theory behind macro momentum: unobservable latent factors form trends and momentum on individual markets is a window onto them; AQR proposes trending macro factors directly.  #mech/structural_shift
  > the there's a bunch of latent factors in the world that you can't see and when we do momentum all we're doing really is is doing momentum on individual markets
  indicator: latent factors; AQR A Half Century of Macro Momentum · asset: multi · horizon: years · testable: partly - macro vs price momentum can be tested · confidence: medium
  ^MT144-C05-3
- **Niels Kaastrup-Larsen** Listener test (read out by the host): macro-momentum signals for growth, inflation, policy, risk sentiment and trade applied to about 100 futures markets reproduced AQR's published results, yet adding them to price trend plus carry lowered the total Sharpe ratio, despite much more complexity and harder data.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > found that the total sh ratio was worse than the original system with just price trend plus carry
  indicator: AQR macro momentum (A Half Century of Macro Momentum) on top of trend plus carry · asset: multi · horizon: years · conditions: retail data access, about 100 markets · testable: yes - a stated backtest that can be rerun · confidence: medium
  ^MT144-C05-X1

### C06
- **Rob Carver** Evidence for latent factors: asset-class-level momentum (synthetic index per asset class) captures about 80-85% of the P&L of trading individual markets, the remainder being relative momentum.  #mech/cycle_persistence
  > that actually captures about 80 to 85% of the p&l of trading the individual markets
  indicator: asset-class momentum vs individual market momentum · asset: multi · horizon: years · testable: yes - decomposition testable · confidence: high
  ^MT144-C06-1
- **Rob Carver** Macro momentum is probably quite correlated with price trend because both rest on the same latent factors, so adding it probably improves Sharpe only modestly.  #mech/research_method
  > my suspicion is that macr momentum is quite correlated with um price trend
  indicator: macro momentum vs price trend correlation · asset: multi · horizon: years · testable: yes · confidence: low
  **Correction (cross-check):** Likely sign error from caption: the caption reads 'probably adding this strategy in would have improved the Sharpe ratio', but in context (the listener's backtest Sharpe fell, Carver is explaining why) the point is that a non-zero correlation to price trend means adding macro momentum would not improve Sharpe much; the claim 'probably improves Sharpe only modestly' contradicts the listener's result. → Carver suspects macro momentum is quite correlated with price trend (same latent-factor idea, correlation not near zero), which explains why adding it did not raise the listener's Sharpe; he would still add a small allocation if the correlation were low enough (caption on the direction is ambiguous).
  ^MT144-C06-2
- **Rob Carver** Portfolio Sharpe rises by adding either a higher-Sharpe stream or a lower-Sharpe stream with very low or negative correlation; a fall from 1.3 to 1.2 is not a deal-breaker.  #mech/research_method
  > something that has a lower Shar ratio but has got a lot of very low correl or even negative correlation
  indicator: Sharpe ratio, correlation · asset: multi · testable: yes - arithmetic · confidence: high
  ^MT144-C06-3
- **Rob Carver** When adding strategies look at correlation rather than Sharpe, because Sharpe ratios are noisier and more dispersed in backtests than correlations.  #mech/research_method
  > sharp ratios are a lot more variable and harder to forecast
  indicator: backtest Sharpe vs correlation stability · asset: multi · testable: yes - estimation error is measurable · confidence: high
  ^MT144-C06-4
- **Rob Carver** From running a global macro system at AHL: collecting and analysing macro data is more expensive and time-consuming than price-based trend following and brings its own data problems, which weighs against adding macro signals.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > I did Implement a global macro system so I have experience of collecting macro data analyzing it and it's obviously more expensive and timec consuming
  indicator: macro data · asset: multi · testable: no - experience statement · confidence: high
  ^MT144-C06-X1

### C07
- **Rob Carver** If correlation to existing strategy is around 0.4, allocate 5-10% even if the backtested Sharpe falls, trusting diversification more than Sharpe.  #mech/risk_management
  > probably think that's worth adding 5 10% to this even if it does reduce the back tested sh ratio
  indicator: correlation between strategies · asset: multi · direction: small allocation to low-correlation strategy · conditions: correlation ~0.4 · testable: partly - rule of thumb · confidence: medium
  ^MT144-C07-1
- **Rob Carver** If correlation is about 0.89 the extra work is not worth it for an individual, although a big fund with staff may still benefit.  #mech/research_method
  > if on the other hand the correlation is like 8.9 between say macro momentum and price momentum
  indicator: correlation 0.89 · asset: multi · direction: shelve the strategy · conditions: for an individual with limited resources · testable: no - cost-benefit judgment · confidence: medium
  ^MT144-C07-2
- **Rob Carver** Instrument and forecast diversification multipliers (IDM/FDM) rescale combined streams back to the target standard deviation: with 150-200 markets portfolio volatility falls from 25% to about 8% without them.  #mech/risk_management
  > I'll find that my volatility drops from 25% to about 8%
  indicator: IDM, FDM multipliers · asset: multi · direction: scale up positions to target vol · testable: yes - multipliers computable from correlations · confidence: high
  ^MT144-C07-3

### C08
- **Rob Carver** Hierarchical construction: instead of extra multipliers at each level, give higher risk weight to groups with more internal diversification (e.g. more momentum signals than carry signals).  #mech/research_method
  > I do my portfolio Construction in a hierarchical way
  indicator: hierarchical risk weights · asset: multi · testable: yes - risk-weighting scheme is testable · confidence: high
  ^MT144-C08-1
- **Rob Carver** A stop loss both sets risk per trade and the holding period, creating a false choice between large risk with long holding and tight risk with premature exits.  #mech/research_method
  > is faecally doing two jobs for you
  indicator: ATR stop loss · asset: multi · testable: yes · confidence: high
  ^MT144-C08-2

### C09
- **Rob Carver** Separate position size (risk) from holding period (speed of trading) instead of tying both to stops.  #mech/risk_management
  > want to do is completely separate out these two decisions so one decision is how big should my positions be and the second decision is how long should I hold my positions for
  indicator: position size, holding period · asset: multi · testable: yes · confidence: high
  ^MT144-C09-1
- **Rob Carver** A 4 ATR stop gives about a month's holding, typical CTA futures; 8 ATR gives about three months; much tighter makes you a short-term trend trader.  #mech/cycle_persistence
  > I think 4 atrs would give you a holding period of about a month
  indicator: ATR stop width vs holding period · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT144-C09-2
- **Rob Carver** A wider ATR stop means more risk per trade but fewer trades, so overall risk is similar or lower than a tight stop with 2% per trade, which trades often and has bigger volatility and drawdowns.  #mech/risk_management
  > you do take more risk per trade but because you're taking fewer trades your actual overall risk stays the same
  indicator: ATR stop · asset: multi · testable: yes · confidence: high
  ^MT144-C09-3
- **Rob Carver** Trading speed should follow instrument cost: his retail-oriented book system uses a slow 8 ATR stop (about three-month holds) because the instruments are expensive to trade, whereas futures can be traded somewhat faster.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > the books aimed at retail traders who are often trading instruments that are quite expensive to trade so maybe if it wouldn't Futures probably you can you could trade a bit quicker
  indicator: ATR stop width; holding period; transaction cost · asset: multi · direction: slower systems for costly instruments · horizon: months · conditions: high cost per trade · testable: yes - speed versus cost is testable · confidence: high
  ^MT144-C09-X1

### C10
- **Rob Carver** Below roughly $100,000 even micros and minis give a portfolio dominated by equity indices and agriculturals; smaller investors are better off with a CTA ETF or fund.  #mech/structural_shift
  > you probably should be looking at least $100,000 to trade a diversified portfolio Futures
  indicator: account size for futures diversification · asset: multi · direction: use CTA ETF until account grows · conditions: small accounts · testable: partly · confidence: medium
  ^MT144-C10-1
- **Rob Carver** Sept 2024: floating a US strategic Bitcoin reserve (US buying lifts price) makes Bitcoin a proxy for Trump's election chances.  #mech/liquidity_flows _(time-bound view)_
  > be quietly High correlated to Trump's chances of winning
  indicator: Bitcoin vs Trump election odds · asset: other · direction: long Bitcoin if Trump favoured · horizon: months · testable: partly - correlation with polls could be tested · confidence: medium
  ^MT144-C10-2
- **Rob Carver** Bitcoin has lost its original claim as money and is viewed as a speculative asset.  #mech/structural_shift
  > I think most people agree now it's just a purely speculative asset
  asset: other · testable: no · confidence: medium
  ^MT144-C10-3

### C11
- **Rob Carver** A small central bank Bitcoin allocation would barely change a balance sheet but would move Bitcoin's price through the size of the flow.  #mech/liquidity_flows _(time-bound view)_
  > it's not going to change the fed's balance sheet very much but it may potentially change bitcoin's price quite a lot because it would be quite a big flow of money
  indicator: central bank reserve purchases · asset: other · direction: long Bitcoin · conditions: if a strategic reserve is created · testable: no · confidence: medium
  ^MT144-C11-1
- **Rob Carver** Currencies derive value from tax acceptance and government creation; governments will not accept an asset they do not control for taxes, so Bitcoin cannot be money.  #mech/structural_shift
  > there's no way any government would be crazy enough to say oh yeah well you can pay your taxes in this other thing that we don't control
  asset: other · testable: no - conceptual · confidence: high
  ^MT144-C11-2

### C12
- **Niels Kaastrup-Larsen** Despite Trump odds, Bitcoin and ether fell (ether -22% in August) and gold made new highs, though 54% of institutional filers raised Bitcoin ETF positions in Q2.  #mech/liquidity_flows _(time-bound view)_
  > most institutional investors who allocate in q1 either held or bought more shares this spring
  indicator: 13F Bitcoin ETF holdings, Bitcoin, ether, gold · asset: other · horizon: months · testable: partly · confidence: medium
  ^MT144-C12-1
- **Rob Carver** The dollar's status as the global reserve and trade-settlement currency is a huge advantage for the US (though hegemony is weaker than before), so officially adding Bitcoin to the monetary system risks frittering it away.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > the fact that it's the world's Global Reserve asset the fact the fact that everyone has to kind of use it for for trade and transfer
  indicator: USD reserve currency status · asset: fx · horizon: years · testable: no - opinion · confidence: medium
  ^MT144-C12-X1
- **Niels Kaastrup-Larsen** Scale check: Bitcoin's market cap of about $1.1tn is small relative to a roughly $7tn Fed balance sheet (down from about $9tn), so a US government purchase is feasible in size, which is why a reserve announcement can move the price.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check, time-bound view)_
  > the market capitalization is only about 1.1 trillion so you know they can just add a trillion to the def to to the to the balance sheet
  indicator: Bitcoin market cap versus Fed balance sheet · asset: other · direction: US buying lifts Bitcoin · testable: yes - sizes are public · confidence: low
  ^MT144-C12-X2

### C13
- **Rob Carver** Active ETFs reached $1tn but only about 10-15% of the ETF universe, which is still mostly passive.  #mech/structural_shift _(time-bound view)_
  > the actively managed ETFs have now hit apparently a trillion dollars
  indicator: active ETF assets · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT144-C13-1
- **Rob Carver** The ETF wrapper acts as a regulatory stamp that lets institutions that cannot hold crypto or futures buy exposure, widening demand.  #mech/liquidity_flows
  > there are a huge number of Institutions that cannot legally buy crypto outright or do not want to buy crypto outright
  indicator: crypto ETFs · asset: other · testable: partly · confidence: medium
  ^MT144-C13-2

### C14
- **Rob Carver** Fund structure drives liquidity: open-ended funds issue and redeem at a daily NAV and must hold cash or sell holdings to meet redemptions, closed-end funds have a static pool traded at a secondary-market price (can deviate from NAV, may use leverage), and an ETF behaves like a closed-end fund for small buyers.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check)_
  > so you know once a day I'd say this is how much my fund is worth and this is what you're buying in at I take your $500
  indicator: NAV versus market price · asset: multi · testable: no - structural description · confidence: high
  ^MT144-C14-X1

### C15
- **Rob Carver** Authorized participants create and redeem ETF shares in kind, so price stays close to NAV, unlike closed-end funds that can trade at large discounts or premiums.  #mech/liquidity_flows
  > take advantage of that with creation Redemption and that keeps the price honest
  indicator: ETF NAV vs price, creation/redemption · asset: multi · horizon: days · testable: yes · confidence: high
  ^MT144-C15-1
- **Rob Carver** The ETF is just a legal wrapper, not a safety label; it can hold single shares triple-leveraged.  #mech/risk_management
  > because you can literally put anything into this thing anything
  indicator: leveraged single-stock ETP · asset: equities · testable: no · confidence: high
  ^MT144-C15-2
- **Rob Carver** Creation and redemption by authorised participants requires the ETF's constituents to be known, a transparency constraint for active managers who do not want to disclose positions (partly avoidable).  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > the constituents of an ETF need to be known to do this authorized participant thing
  indicator: ETF holdings disclosure · asset: multi · conditions: active ETFs wanting to hide positions · testable: no - structural · confidence: medium
  ^MT144-C15-X1

### C16
- **Niels Kaastrup-Larsen** A 3x leveraged daily ETP on MicroStrategy (LMI3) lost about 82% while MicroStrategy rose over 100%, showing the compounding damage of leveraged ETFs.  #mech/risk_management _(time-bound view)_
  > while micro strategy itself is higher by more than 100% this year LMI 3 has dropped nearly 82%
  indicator: 3x MicroStrategy daily ETP · asset: equities · horizon: months · conditions: leveraged daily ETFs in volatile assets · testable: yes - daily-reset compounding is measurable · confidence: high
  ^MT144-C16-1
- **Niels Kaastrup-Larsen** ETF buyers do little due diligence compared with hedge fund allocators.  #mech/behavioral
  > with ETFs people don't do I I think don't do much due diligence
  asset: multi · testable: no · confidence: medium
  ^MT144-C16-2
- **Rob Carver** Leveraged single-stock/Bitcoin-proxy ETPs let retail investors take leverage they could not legally or practically obtain via options or futures, so buyers skew to less-informed retail and the issuers earn high fees while the SEC wrapper gives false comfort.  #mech/behavioral _(added by sonnet-xhigh cross-check)_
  > there are people out there who want to make this absolute crazy leverage bit on bitcoin but do not have um the access or the the capability to to do it with auctions or futures or whatever
  indicator: 3x leveraged MicroStrategy ETP · asset: other · conditions: retail buyers lacking options/futures access · testable: partly - flows and fees are observable · confidence: medium
  ^MT144-C16-X1

### C17
- **Rob Carver** Transtrend paper argument: a stock index is indirect exposure to factors such as yen and metals, and a CTA index is likewise exposure to factors via many CTAs.  #mech/structural_shift
  > by buying a stock index what you're actually buying is effectively One Step removed a exposure to a whole bunch of factors
  indicator: Transtrend 'Can't we just buy the index' · asset: multi · testable: partly · confidence: medium
  ^MT144-C17-1
- **Rob Carver** If you can pick winning CTAs, do so rather than index; the index is for those who cannot.  #mech/research_method
  > if you think you're good at picking winners if you think you can pick good ctas either based on their past performance or based on due diligence then you should probably do that rather than buy an index
  indicator: CTA manager selection · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT144-C17-2
- **Niels Kaastrup-Larsen** Sept 2024: a new investable SG CTA index (from a different part of SocGen than the usual SG CTA index publisher) is powered by the DBMF replication engine, which prompted the Transtrend paper 'Can't we just buy the index'.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > it is uh engined by Andrews uh dbmf uh replication model
  indicator: SG investable CTA index; DBMF replication model · asset: multi · testable: no - market development · confidence: medium
  ^MT144-C17-X1

### C18
- **Rob Carver** With 30-50 million, pick around 10 CTA managers since they are correlated.  #mech/risk_management
  > because CT managers are quite correlated you don't need that many of them to give you a kind of reasonable divers
  indicator: number of CTA managers · asset: multi · testable: yes · confidence: medium
  ^MT144-C18-1
- **Rob Carver** Weakness in the stock-index analogy: firms hedge FX and commodity exposures.  #mech/structural_shift
  > most companies do hedge out their exposure to their principal risk
  asset: multi · testable: partly · confidence: medium
  ^MT144-C18-2
- **Rob Carver** CTA factor exposure is dynamic and not linear or one-directional, unlike a company's.  #mech/structural_shift
  > CTS change their exposure dynamically sometimes they're long sometimes they're short
  asset: multi · testable: partly · confidence: medium
  ^MT144-C18-3

### C19
- **Rob Carver** More markets are better than fewer, so replicating with a small number of futures is not ideal.  #mech/structural_shift
  > in the much more in the more is better Camp
  indicator: number of markets · asset: multi · testable: yes · confidence: medium
  ^MT144-C19-1
- **Rob Carver** High correlation between CTAs does not prevent outliers; picking your own CTAs can miss an exploding manager, like missing Nvidia in a picked stock portfolio.  #mech/risk_management
  > correlations to poor poor judge of of anything that isn't linear
  indicator: correlation, idiosyncratic risk · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT144-C19-2
- **Rob Carver** The SG CTA index has only 20 managers, so it can be undiversified if it misses a big winner.  #mech/research_method
  > even 20 is not a big number for an index
  indicator: SG CTA index breadth · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT144-C19-3
- **Rob Carver** An index serves for benchmarking and as long-history proxy in asset allocation, which is institutional thinking.  #mech/research_method
  > I'm going to use this index for 20 years of history as a proxy for the CTA universe
  indicator: CTA index history · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT144-C19-4
- **Niels Kaastrup-Larsen** Disagreement on breadth: the host (inferred from Carver's reply 'one of your things') sees no evidence that trading 250 markets beats 50, whereas Carver is in the more-is-better camp and therefore dislikes replicating with few futures markets.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > I don't see the evidence that having say 250 rather than 50 markets is better
  indicator: number of markets traded (50 vs 250) · asset: multi · horizon: years · testable: yes - Sharpe versus breadth can be backtested · confidence: medium
  ^MT144-C19-X1

### C20
- **Rob Carver** Prefers bottom-up replication (replicate positions) over top-down (replicate an index) for statistical reasons.  #mech/research_method
  > I'm more of a fan of doing bottomup replication the top down
  indicator: replication method · asset: multi · testable: yes · confidence: medium
  ^MT144-C20-1
- **Rob Carver** Carver's own implementation generates positions in about 250 futures (60 untradeable) and replicates them in a small account.  #mech/risk_management
  > every day I try and replicate that big portfolio with my smaller portfolio
  indicator: own system replication · asset: multi · horizon: days · testable: no · confidence: high
  ^MT144-C20-2
- **Niels Kaastrup-Larsen** An ETF with fewer than 20 markets may be correlated with the CTA index but lacks its diversification and carries single-manager risk (Transtrend).  #mech/structural_shift
  > how can an ETF that trades in fewer than 20 markets deliver CTA index Returns the answer is simple it cannot
  indicator: ETF with fewer than 20 markets · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT144-C20-3
- **Rob Carver** ETFs give retail access to alternative risk premia and trend following that would otherwise be unavailable.  #mech/structural_shift
  > ETFs are a good thing for retail investors
  asset: multi · testable: no · confidence: high
  ^MT144-C20-4
- **Rob Carver** For non-institutional buyers who just want trend exposure, matching a CTA index closely is not important; an ETF with a trend-following style and reasonable fees serves them, since benchmarking is an institutional preoccupation.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > dogmatically matching an index just because that's what the the kind of institutional industry is obsessed with is necessarily for you know for most people who are just buying want to get exposure to trend is necessarily that important
  indicator: CTA index tracking · asset: multi · conditions: retail investors rather than institutions · testable: no - opinion · confidence: medium
  ^MT144-C20-X1

### C21
- **Niels Kaastrup-Larsen** Labelling a backtest as an index makes it a public track record, which could mislead since managers cannot sell on backtests.  #mech/research_method
  > however now that it's labeled an index and people think okay well I can now go and buy that index a back test becomes quote unquote a public track record
  indicator: backtested index · asset: multi · testable: no · confidence: medium
  ^MT144-C21-1
- **Rob Carver** Back-tested indices underlying ETFs are not new (smart-beta indices such as FX carry); the risk is disclosure that sets an index backtest next to the live track record so that it misleads, and he is unsure whether prospectuses show the backtest.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > there are what I call Smart beta indices that do things like for for example simple FX carry strategies
  indicator: index backtest versus live record · asset: multi · conditions: when marketing material shows both · testable: no - disclosure practice · confidence: medium
  ^MT144-C21-X1

### C22
- **Rob Carver** Understand what is inside any ETF; the new investable CTA index is more trustworthy than a triple-leveraged Bitcoin ETP.  #mech/risk_management
  > as with any ETF product don't just buy it and think it's safe because it says ETF on the outside
  asset: multi · testable: no · confidence: high
  ^MT144-C22-1

