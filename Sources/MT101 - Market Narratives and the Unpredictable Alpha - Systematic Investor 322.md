---
source_id: MT101
title: "Market Narratives and the Unpredictable Alpha - Systematic Investor 322"
date: 2024-11-23
channel: "Top Traders Unplugged"
url: 
words: 11821
claims: 45
added_by_opus: 0
corrections: 0
crosscheck: "pending"
speakers: ["Mark (guest, systematic trend-following researcher)", "Alan Dunne (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Market Narratives and the Unpredictable Alpha - Systematic Investor 322

**Speakers:** Mark (guest, systematic trend-following researcher); Alan Dunne (host, Top Traders Unplugged)

**Summary:** Systematic Investor 322 (Nov 2024, post-US election): Mark discusses equity risk premium, bond term premium, risk cycle/leverage, why trend followers use prices not narratives, and research on analysts, narratives and trend-following allocation. Trend following is observational not causal; position sizing matters more than forecasting; economic trends beget price trends. Views: bond yields can keep rising, equity ERP falling means lower forward stock returns, credit spreads too tight.

**Approach:** trend following, macro, valuation, risk management, narrative

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 2 | intro; equity risk premium turned negative (earnings yield minus 10y) |
| C02 | 4 | ERP measures, analysts backward looking, CTA index performance Nov 2024 |
| C03 | 4 | VIX decline, term structure, small caps, Fed cuts vs rising long yields |
| C04 | 3 | average inflation targeting dropped, policy uncertainty, bond vigilantes, surprise indices |
| C05 | 4 | economic trends beget price trends, nowcast, dollar confirms bond move |
| C06 | 3 | term premium turning positive, QT, deficits, bond bearish case, swap spreads |
| C07 | 2 | safe asset shortage, bond volatility, SVB; crypto trend following question |
| C08 | 2 | allocators and crypto trend following; liquidity limits; risk cycle intro |
| C09 | 4 | low volatility breeds leverage; tight credit spreads vs weak consumer |
| C10 | 3 | leverage buildup, fixed rate mortgages, China balance sheet recession; info and rationality intro |
| C11 | 1 | perfect information experiment; information vs reaction uncertainty; trend follower focus on price |
| C12 | 2 | kind vs wicked learning environments; causal vs observational; ML |
| C13 | 3 | unstable causal relations; position sizing beats forecasting; analyst research intro |
| C14 | 1 | analysts use trailing PE and are backward looking, post-earnings drift |
| C15 | 2 | narrative aggregation via LLMs shows underreaction; anchoring |
| C16 | 3 | post-election themes; narrative plus fundamentals; unpredictable alpha vs dynamic beta |
| C17 | 2 | trend following in high rate regimes; trend beta replication and dispersion |

## Claims

### C01
- **Mark** S&P earnings yield minus 10-year Treasury yield has turned negative, signalling weaker long-term equity returns despite post-election euphoria.  #mech/risk_premium _(time-bound view)_
  > the equity risk premium has now turn negative so if you think that the stock market is going to continue to go higher over the next couple of years
  indicator: S&P 500 earnings yield minus 10y yield · asset: equities · direction: lower forward stock returns · horizon: years · conditions: one chart only; use an ensemble of valuation measures · testable: yes - simple series, test forward 1-5y returns · confidence: medium
  ^MT101-C01-1
- **Mark** A declining equity risk premium is followed on average by lower stock returns over 1, 2 and 5 years, a probabilistic not certain relation.  #mech/risk_premium
  > then you look at what is the uh forward behavior of stocks over one two five years it's usually lower
  indicator: equity risk premium · asset: equities · direction: lower equity returns · horizon: years · conditions: probabilistic, not always · testable: yes - regress forward returns on ERP · confidence: medium
  ^MT101-C01-2

### C02
- **Alan** The simple inverse-P/E equity risk premium ignores earnings growth, so growth-adjusted ERP measures differ in level though similar in direction.  #mech/research_method
  > it doesn't account for earnings growth so it's just taking the current uh earnings uh dividing it
  indicator: earnings yield based ERP vs growth-adjusted ERP · asset: equities · testable: partly - needs alternate ERP definition · confidence: medium
  ^MT101-C02-1
- **Alan** Expectations of equity returns are high while forward returns implied by valuation look poor, a gap last seen around 2000.  #mech/overshoot _(time-bound view)_
  > the gap between kind of what it was was pointing to and people's expectations
  indicator: ERP vs investor return expectations · asset: equities · direction: lower forward returns · horizon: years · testable: partly - expectations survey data needed · confidence: medium
  ^MT101-C02-2
- **Mark** Despite MBA training in discounting forward earnings, evidence shows analysts anchor on past earnings.  #mech/behavioral
  > there's still a preponderance of evidence to show that analysts you know look back in time as opposed to try to forecast in the future
  indicator: analyst valuation method · asset: equities · testable: partly · confidence: medium
  ^MT101-C02-3
- **Alan** SG CTA index up 1.6% mid-November 2024 (YTD +0.9%), trend index +2.7% (YTD +0.55%): equity and bond trends and a dollar spike helped trend followers.  #mech/slow_reaction _(time-bound view)_
  > the sck Gen CTA index up 1.6% month to date bringing the year to date figure to plus 0.9%
  indicator: SG CTA Index, SG Trend Index · asset: multi · direction: long equities, short bonds, long dollar helped · horizon: weeks · conditions: gold reversed and grains choppy · testable: yes - index data · confidence: high
  ^MT101-C02-4

### C03
- **Mark** VIX fell about 20 to 15 and began falling before the election as uncertainty resolved; SPX vol term structure moved from backwardation back to contango.  #mech/risk_premium _(time-bound view)_
  > people were were starting to be uh less uncertain about the outcome before the actual election occurred
  indicator: VIX, SPX volatility term structure · asset: equities · direction: lower volatility · horizon: weeks · testable: yes · confidence: high
  ^MT101-C03-1
- **Mark** Lower taxes or lighter regulation favour small caps over large caps because fixed regulatory costs weigh more on small firms; Russell 2000 outperformed after the election.  #mech/policy_reaction _(time-bound view)_
  > if there is a uh looser tax policy or expectation of lower taxes or lower regulation that's usually better for small cap stocks versus large cap stocks
  indicator: Russell 2000 vs large caps · asset: equities · direction: long small caps vs large caps · horizon: months · conditions: when deregulation or tax cuts are expected · testable: yes - event study of policy regimes · confidence: medium
  ^MT101-C03-2
- **Mark** Fed cut 25bp but long yields kept rising, breaking the classic easing-lowers-yields relation; long end trend continued.  #mech/policy_reaction _(time-bound view)_
  > the long end of the bond market is saying is is that well we're not buying what you're selling
  indicator: Fed funds vs 10y yield · asset: rates · direction: long-end yields up · horizon: weeks · testable: partly · confidence: high
  ^MT101-C03-3
- **Mark** The Fed's average inflation targeting framework has effectively been abandoned.  #mech/policy_reaction _(time-bound view)_
  > they were going to have the average inflation rate policy
  indicator: Fed framework · asset: rates · testable: no - qualitative · confidence: medium
  ^MT101-C03-4

### C04
- **Mark** High policy uncertainty (Bloom news and policy uncertainty indices) raises term premia in long bonds and can create divergence between what the Fed wants and market pricing.  #mech/risk_premium
  > if there is a lot of policy uncertainty and even from the comments from Paul thought what what will happen then what you see is is that there should be a greater uh risk premium or term premium in bonds
  indicator: Baker-Bloom economic policy uncertainty index · asset: rates · direction: higher long yields · horizon: months · conditions: index noisy and bounces around · testable: yes · confidence: medium
  ^MT101-C04-1
- **Alan** Rising TIPS breakevens can influence the Fed, so the bond market constrains the Fed as well as fiscal policy.  #mech/policy_reaction
  > if um if inflation break evens Rise sufficiently um you know that that that that very much influences uh the Fed
  indicator: TIPS breakeven inflation · asset: rates · horizon: months · conditions: when breakevens rise sufficiently · testable: partly · confidence: medium
  ^MT101-C04-2
- **Mark** Rising economic surprise indices and loose financial conditions are good trend signals supporting higher yields.  #mech/cycle_persistence _(time-bound view)_
  > when the surprise index moves higher that that tells you
  indicator: Citi/Bloomberg economic surprise index; financial conditions index; inflation surprise index · asset: rates · direction: higher yields · horizon: months · testable: yes · confidence: medium
  ^MT101-C04-3

### C05
- **Mark** As a macro trend follower, trends in economic data translate into price trends, so fundamental trends reinforce price trends.  #mech/cycle_persistence
  > economic Trends begets price trends if you see the trends in economics are all moving higher then that's going to actually then translate into the price
  indicator: macro data trends · asset: multi · direction: price trends follow economic trends · horizon: months · testable: yes · confidence: high
  ^MT101-C05-1
- **Mark** Trend confidence falls if fundamentals disagree: slowing growth, tightening financial conditions or negative surprise index while yields trend up.  #mech/risk_management
  > you're more wary if the fundamental data is at odds with what the trend we're seeing
  indicator: growth nowcast, financial conditions, surprise index · asset: rates · direction: reduce trend exposure when fundamentals conflict · horizon: months · testable: yes - filter test · confidence: medium
  ^MT101-C05-2
- **Mark** GDPNow near 3% and rising surprise indices reinforce the bond yield uptrend, so it could last longer.  #mech/cycle_persistence _(time-bound view)_
  > look at the Atlantic fed nowcast their GDP let showing up close to 3%
  indicator: Atlanta Fed GDPNow · asset: rates · direction: higher yields · horizon: months · testable: yes · confidence: medium
  ^MT101-C05-3
- **Mark** In a fiscal-crisis bond vigilante scenario yields would rise with a falling dollar; a rising dollar with rising yields says growth is driving it instead.  #mech/fiscal_debt _(time-bound view)_
  > rates would go higher but the dollar would go lower so that people didn't want to buy the safe assets
  indicator: US yields vs dollar direction · asset: multi · direction: dollar up with yields up = growth · horizon: months · testable: partly · confidence: medium
  ^MT101-C05-4

### C06
- **Mark** Term premia are turning positive across the curve, a trend that points to higher yields because deficits, QT and global financing needs demand compensation.  #mech/risk_premium _(time-bound view)_
  > the term premium across the board is starting to move from negative to positive
  indicator: term premium (ACM-type) · asset: rates · direction: higher long-end yields; bearish bonds · horizon: months · testable: yes · confidence: medium
  ^MT101-C06-1
- **Mark** China's balance sheet recession means firms use cash to pay down debt, so its fiscal stimulus does not boost spending as much.  #mech/structural_shift _(time-bound view)_
  > China That's while they have new fiscal policy that they're fa facing what we call a balance sheet recession
  indicator: Chinese corporate deleveraging · asset: multi · horizon: years · testable: no - qualitative · confidence: medium
  ^MT101-C06-2
- **Alan** Swap spreads falling reflect expectations that Treasuries get lighter bank capital treatment (supplementary leverage ratio relief) to support demand for bonds.  #mech/policy_reaction _(time-bound view)_
  > swap spreads have been trading lower relative to bond yields of late
  indicator: swap spreads · asset: rates · horizon: months · testable: partly · confidence: low
  ^MT101-C06-3

### C07
- **Mark** A shortage of Treasuries as collateral, plus FX risk for foreign buyers and higher rate volatility (MOVE above VIX), makes Treasuries riskier than before.  #mech/liquidity_flows
  > do we have a shortage of safe assets
  indicator: MOVE index · asset: rates · horizon: years · testable: partly · confidence: medium
  ^MT101-C07-1
- **Mark** Trend following models work in cryptocurrencies.  #mech/slow_reaction
  > I've done some analysis on this i s of say that uh Trend following models do work in
  indicator: crypto trend following · asset: other · direction: long and short crypto trends · testable: yes · confidence: high
  ^MT101-C07-2

### C08
- **Mark** The risk cycle (volatility, leverage, risk appetite) is distinct from the business cycle and should be monitored separately; volatility has been low apart from August 2024.  #mech/risk_premium
  > what is the risk cycle which is different than the business cycle
  indicator: VIX, MOVE · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT101-C08-1
- **Mark** Allocators are cautious on crypto-only trend programs because of operational issues (prime broker, no cross margining) and thin liquidity that caps capacity and raises costs beyond the top coins.  #mech/risk_management
  > you don't get the cross margining that you would like
  indicator: crypto liquidity and costs · asset: other · conditions: beyond top few coins · testable: partly · confidence: medium
  ^MT101-C08-2

### C09
- **Mark** The risk cycle differs from the business cycle: persistent low volatility, especially low downside volatility, invites leverage and risk-taking that plant the seeds of a later shock.  #mech/risk_premium
  > is is that low uh volatility actually be gets uh more leverage
  indicator: VIX, MOVE · asset: multi · horizon: years · conditions: low-volatility regimes · testable: partly · confidence: high
  ^MT101-C09-1
- **Mark** Harm from a volatility spike depends on prior low volatility and the leverage of players like hedge funds and CTAs, so watch how volatility propagates through leverage.  #mech/crowding_positioning
  > you have to look at what happened prior to the spike in the vix rise
  indicator: VIX; leverage of hedge funds and CTAs · asset: multi · testable: partly · confidence: medium
  ^MT101-C09-2
- **Mark** Credit spreads are extremely tight even as card and auto delinquencies rise and small-cap earnings are poor, suggesting equilibrium spreads should be higher.  #mech/overshoot _(time-bound view)_
  > credit spreads are extreme extremely tight
  indicator: credit spreads vs delinquencies · asset: credit · direction: wider spreads · horizon: months · testable: yes · confidence: medium
  ^MT101-C09-3
- **Alan** Credit spread spikes in 2022 and 2020 may have blunted leverage buildup compared with the uninterrupted late-1990s low spreads.  #mech/cycle_persistence
  > we had obviously you know a blip in 2022
  indicator: credit spreads 1995-2000 · asset: credit · horizon: years · testable: partly · confidence: low
  ^MT101-C09-4

### C10
- **Mark** US consumers hold fixed low-rate mortgages (housing gridlock), while floating-rate countries outside the US are more exposed to higher rates.  #mech/structural_shift
  > a lot of them all refinance to fixed rate mortgages in the US at at low rates
  indicator: mortgage rate structure · asset: other · horizon: years · testable: no · confidence: medium
  ^MT101-C10-1
- **Mark** Leverage uses assets as collateral, so a shock lowers collateral value; embedded leverage raises sensitivity to the shock.  #mech/behavioral
  > you are going to have spikes that's not the issue the issue is is that when you have low periods of low volatility
  indicator: collateral values and leverage · asset: multi · conditions: after long low volatility · testable: partly · confidence: medium
  ^MT101-C10-2
- **Mark** A trend follower should look first at prices while treating other information as supplementary.  #mech/research_method
  > prices are Primal so prices are the most important thing to look at first
  indicator: price · asset: multi · testable: no · confidence: high
  ^MT101-C10-3

### C11
- **Mark** Even perfect next-day headlines gave marginal returns in the Elm Capitalist experiment: knowing news does not tell you the market reaction, so a trend follower focuses on price.  #mech/behavioral
  > you can resolve information uncertainty I give you the headlines but you can't resolve or uh reaction or behavioral uncertainty
  indicator: next-day headline experiment · asset: multi · horizon: days · testable: partly · confidence: high
  ^MT101-C11-1

### C12
- **Mark** Kind learning environments have clear cause-effect feedback; markets are wicked (inconsistent relationships), so experience can mislead (Hogarth).  #mech/research_method
  > a kind environment would be is is that there's a good link between you know the action and then the response
  asset: multi · conditions: wicked: relation between inflation and bonds not one-for-one · testable: no - conceptual · confidence: medium
  ^MT101-C12-1
- **Mark** Trend following avoids hard causal inference in macro and relies on observed price persistence; machine-learning approaches suffer when learned relationships break down.  #mech/research_method
  > Trend following is more observational as opposed to causal in how they build the models
  indicator: price trend · asset: multi · conditions: when relationships are unstable ML fails more · testable: partly · confidence: high
  ^MT101-C12-2

### C13
- **Alan** Causal macro relations flip over time (bad news is good news, then good news is good news).  #mech/structural_shift
  > the Cal relationships themselves are are are not not necessarily consistent
  indicator: news-return relation · asset: multi · testable: partly · confidence: medium
  ^MT101-C13-1
- **Mark** Good position sizing and risk management matter as much as forecast skill: average forecasters survive with sizing, great forecasters with poor sizing still go bankrupt (55/45 accuracy is good).  #mech/risk_management
  > you can be an average forecaster but if you're very good at position sizing and risk management you can survive and still make money
  indicator: position sizing · asset: multi · testable: yes · confidence: high
  ^MT101-C13-2
- **Mark** FINRA-required analyst model disclosures show most analysts value stocks with trailing P/E multiples then tweak it, not discounted forward earnings.  #mech/behavioral
  > most of these models are actually EX look at trailing PE though
  indicator: trailing P/E in analyst models · asset: equities · testable: partly · confidence: medium
  ^MT101-C13-3

### C14
- **Mark** Backward-looking analysts adjust valuations slowly as new earnings arrive, explaining post-earnings drift and stock trends.  #mech/slow_reaction
  > we find we have post earnings drift and we as have Trend following some stocks
  indicator: post-earnings announcement drift · asset: equities · direction: stocks drift in direction of surprise · horizon: months · testable: yes · confidence: medium
  ^MT101-C14-1

### C15
- **Mark** LLM-aggregated news narrative trends (State Street product) predict stock returns because of underreaction and slow information diffusion; trends in news lead trends in prices.  #mech/slow_reaction
  > there's actually an underreaction in stocks
  indicator: aggregated news narrative sentiment · asset: equities · direction: trade in the direction of news sentiment trend · horizon: months · conditions: high barriers: data and processing · testable: yes · confidence: medium
  ^MT101-C15-1
- **Alan** Anchoring means investors underreact to news early in a trend and overreact later, one base of trend-following profit.  #mech/behavioral
  > investors do underreact to uh news early on in the trend and later on over overreact
  asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT101-C15-2

### C16
- **Mark** Post-election themes (tax cuts, deregulation, deficits) combined with trending fundamentals suggest trends continue as long as price action confirms; stop out otherwise.  #mech/cycle_persistence _(time-bound view)_
  > as long as the price action is behaving the same it says yes I'm going to continue to follow that
  indicator: post-election trends · asset: multi · direction: stay with trends · horizon: months · testable: partly · confidence: medium
  ^MT101-C16-1
- **Mark** Trend following is dynamic beta (positive, negative or zero) rather than crisis alpha or unpredictable alpha.  #mech/structural_shift
  > I've always sort of think of this as more Dynamic uh beta
  indicator: trend following beta · asset: multi · testable: partly · confidence: medium
  ^MT101-C16-2
- **Mark** Quantica research: increase allocation to trend following in high-rate regimes: more dispersion and volatility, and lower correlation to bonds and equities.  #mech/cycle_persistence
  > you should probably increase your allocation a trend following a high interest rate environment
  indicator: trend following vs interest rate level · asset: multi · direction: overweight trend following when rates are high · horizon: years · testable: yes · confidence: medium
  ^MT101-C16-3

### C17
- **Mark** In high-rate regimes CTA correlation to bonds and equities falls, making trend following a better diversifier than clipping bond coupons.  #mech/risk_premium
  > the correlation between ctas and bonds gets lower and the correlation is slightly slower for equities
  indicator: CTA-bond correlation · asset: multi · horizon: years · conditions: high rate environments · testable: yes · confidence: medium
  ^MT101-C17-1
- **Mark** Corey Hoffstein-type replication can mimic the BTOP 50 by bundling strategies, but dispersion among trend followers makes replicating skill hard; interest from swap providers and allocators.  #mech/research_method
  > certain techniques um that you can be able to bundle a set of strategies and come up with a replication strategy
  indicator: BTOP 50 replication · asset: multi · conditions: dispersion across managers · testable: yes · confidence: medium
  ^MT101-C17-2

