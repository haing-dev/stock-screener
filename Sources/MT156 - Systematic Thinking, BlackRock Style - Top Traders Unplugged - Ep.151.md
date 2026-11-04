---
source_id: MT156
title: "Systematic Thinking, BlackRock Style - Top Traders Unplugged - Ep.151"
date: 2025-12-15
channel: "Top Traders Unplugged"
url: 
words: 12658
claims: 68
added_by_crosscheck: 17
corrections: 1
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Jeff Rosenberg (Managing Director, BlackRock Systematic)", "Niels Kaastrup-Larsen (host, Top Traders Unplugged; caption spelling 'Neils Castro Larson')", "Alan Dunne (co-host)"]
tags: [source, layer0]
---
# Systematic Thinking, BlackRock Style - Top Traders Unplugged - Ep.151

**Speakers:** Jeff Rosenberg (Managing Director, BlackRock Systematic); Niels Kaastrup-Larsen (host, Top Traders Unplugged; caption spelling 'Neils Castro Larson'); Alan Dunne (co-host)

**Summary:** BlackRock Systematic's Jeff Rosenberg on the post-Covid inflation regime, weaker stock-bond diversification and the move toward liquid alternatives. Describes breadth-based trend ETFs, the defensive-alpha equity long/short built on a credit lens, and ETF wrapper constraints. Hosts worry that low-fee narrow trend ETFs hide breadth compromises.

**Approach:** trend following, systematic multi-strategy, defensive alpha, liquid alternatives, portfolio construction

**Cross-check completeness estimate of first read:** 0.79 - the first reader captured the main macro, systematic-framework, ETF and defensive-alpha ideas (64 claims) but skipped host/co-host points (unstable inflation, dual mandate, ETF fee economics, drawdown types), allocation-size reasoning and the AI/differentiation remarks

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro, sponsor and compliance read, host introduces guest |
| C02 | 2 | guest background; macro: post-Covid inflation, stock-bond correlation |
| C03 | 3 | divine coincidence, persistent not resurgent inflation, Fed credibility |
| C04 | 5 | term premium, wages, affordability, price adjustment; fixed income as income |
| C05 | 4 | history of fixed income and 60/40; diversifiers; debt and financial repression |
| C06 | 4 | financial repression modelling; systematic definitions start |
| C07 | 2 | meaning of systematic, return-source separation, AI |
| C08 | 2 | why big managers launch trend, engineering for outcomes |
| C09 | 1 | trend vs momentum/factors; 2025 timing of ISMF |
| C10 | 5 | 2025 reversals; law of active management; breadth in ETFs |
| C11 | 3 | cocoa 2024 and basket selection; no timing; defensive alpha intro |
| C12 | 7 | defensive alpha, convex profiles, combining strategies |
| C13 | 2 | multi-strat mix, implementation alpha, market impact |
| C14 | 1 | ETF wrapper sequencing and constraints |
| C15 | 3 | leverage constraints, contract choice, CalPERS total portfolio |
| C16 | 2 | alternatives growth, market concentration |
| C17 | 3 | 60/40 to 50/30/20, allocator views |
| C18 | 2 | ETF fee and breadth concerns, manager selection, outro |
| C19 | 0 | nothing actionable: outro and subscribe read |

## Claims

### C02
- **Jeff Rosenberg** The post-Covid shift from too little to too much (but gradually falling) inflation is a structural regime change that alters the structure of strategies and portfolios.  #mech/structural_shift
  > the precoid environment was one of too little inflation and the postcoid environment is an environment of too much inflation
  indicator: US inflation vs 2% target · asset: multi · horizon: years · conditions: Regime change from pre-Covid disinflation to post-Covid persistent inflation · testable: partly: regime can be dated, effect on strategies testable by sub-period · confidence: high
  ^MT156-C02-1
- **Jeff Rosenberg** Higher inflation challenges the stock-bond correlation, the key construct for portfolio construction, so bond diversification is less reliable.  #mech/structural_shift
  > the relationship between risky assets and safe assets. stock bond correlation
  indicator: stock-bond correlation · asset: multi · direction: stock-bond correlation rises (positive) · horizon: years · conditions: Post-Covid inflation regime · testable: yes: rolling stock-bond correlation vs inflation level · confidence: high
  ^MT156-C02-2

### C03
- **Jeff Rosenberg** With too little inflation the Fed has no conflict between its mandates (easing helps both), which made bonds powerful diversifiers; with too much inflation there is no riskless policy path and that diversification weakens.  #mech/policy_reaction
  > divine coincidence of monetary policy exists when you have too little inflation
  indicator: inflation level, Fed dual-mandate conflict · asset: rates · direction: bonds diversify equities when inflation is low and easing is costless; not when inflation is above target · horizon: years · conditions: Inflation near or below target vs persistently above target · testable: yes: bond hedge efficacy conditional on inflation regime · confidence: high
  ^MT156-C03-1
- **Jeff Rosenberg** The practical inflation risk is persistent above-target inflation (about 3%) rather than a return of Covid-level inflation.  #mech/structural_shift _(time-bound view)_
  > resurgent inflation really means first and foremost a lack of the continual collapse of inflation down to the 2% target
  indicator: US inflation near 3% · asset: multi · horizon: years · testable: partly: inflation persistence can be measured · confidence: high
  ^MT156-C03-2
- **Jeff Rosenberg** If the Fed tolerates about 3% inflation while saying its target is 2%, credibility suffers and investors may not be compensated for that inflation in long bonds (term premium).  #mech/policy_reaction _(time-bound view)_
  > So, there's a credibility problem.
  indicator: term premium, inflation vs target · asset: rates · direction: higher term premium needed on long bonds · horizon: years · conditions: Persistent above-target inflation · testable: partly: term premium is a model estimate · confidence: medium
  ^MT156-C03-3
- **Jeff Rosenberg** The persistent-inflation concern is concentrated in the US; outside the US the factors that could drive resurgent inflation are not present, so the weakened stock-bond diversification story is mainly a US one.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > Most of that inflation concern is really in the US. Outside the US, you don't really see the same, you know, sort of factors that might contribute to resurgent inflation
  indicator: US vs non-US inflation drivers · asset: rates · direction: inflation risk and weaker bond diversification mainly US · horizon: years · conditions: US fiscal stimulus and wage pressure · testable: yes - compare stock-bond correlation across regions · confidence: medium
  ^MT156-C03-X1

### C04
- **Jeff Rosenberg** Inflation uncertainty raises term premium and reduces the hedging efficacy of long-end versus front-end yields.  #mech/risk_premium
  > that's a big debate around term premium and the value of uh the hedging efficacy of back-end yields versus front-end yields
  indicator: term premium, long-end vs front-end yields · asset: rates · direction: long-end yields less effective hedge; term premium up · horizon: years · conditions: Inflation uncertainty regime · testable: yes: hedge beta by maturity over time · confidence: medium
  ^MT156-C04-1
- **Jeff Rosenberg** Wage inflation and real incomes are the main source of persistent inflation, so a stalling decline in wage growth is the indicator to watch.  #mech/cycle_persistence _(time-bound view)_
  > So, you got to kind of watch this kind of petering out of the decline in the wage inflation figures
  indicator: wage inflation figures, real income growth · asset: multi · direction: inflation stays elevated if wage growth stops falling · horizon: months · conditions: US, affordability backdrop · testable: yes: wage growth as inflation predictor · confidence: medium
  ^MT156-C04-2
- **Jeff Rosenberg** The affordability problem (real income lagging the price level) cannot be fixed by lower prices (deflationary spiral) so the political resolution needs nominal income growth, which is inflationary.  #mech/policy_reaction _(time-bound view)_
  > real income growth didn't keep up with the surge of inflation
  indicator: real income growth, nominal GDP · asset: multi · direction: nominal GDP and wages up · horizon: years · conditions: US post-Covid · testable: no: political narrative · confidence: medium
  ^MT156-C04-3
- **Jeff Rosenberg** After a long period of too little inflation in which firms feared adjusting prices, one inflation episode teaches firms that they can raise prices, so price adjustment is easier and inflation more persistent and less stable.  #mech/behavioral
  > Once you've gone through that process, then it's easier the next time to see the price increases.
  asset: multi · direction: inflation more persistent · horizon: years · conditions: After a large inflation shock · testable: partly: pricing-frequency surveys · confidence: medium
  ^MT156-C04-4
- **Jeff Rosenberg** With positive real yields and weaker diversification, investors use fixed income more for income than as a diversifier, opening room for alternative diversifiers.  #mech/structural_shift
  > income is is a more attractive source of use of fixed income in portfolios than diversification
  indicator: real yields · asset: rates · direction: fixed income used for income; alternatives take diversification role · horizon: years · conditions: Post-Covid positive real yields · testable: no: allocator behaviour claim · confidence: medium
  ^MT156-C04-5
- **Niels Kaastrup-Larsen** Beyond a higher level, post-Covid inflation is likely to be less stable, which makes planning harder and keeps inflation uncertainty (and the term premium) elevated.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > we used to have very stable inflation people could plan but postco I think going forward we'll continue to have kind of uh unstable inflation
  indicator: inflation volatility · asset: rates · direction: higher inflation uncertainty, higher term premium · horizon: years · conditions: post-Covid regime · testable: yes - rolling inflation volatility vs term premium · confidence: medium
  ^MT156-C04-X1

### C05
- **Jeff Rosenberg** Disinflation in the 1990s-2000s gave negative stock-bond correlation plus positive real yields, the golden period for 60/40 and risk parity.  #mech/structural_shift
  > negative stock bond correlation with high not great but at least for a while there positive real yields
  indicator: stock-bond correlation, real yields · asset: multi · direction: bonds hedged equity · horizon: years · conditions: Low-inflation disinflation regime · testable: yes: historical correlation · confidence: high
  ^MT156-C05-1
- **Jeff Rosenberg** Total-return bond investing worked because yields were in secular decline; at the zero bound that diversification argument reached its limit.  #mech/overshoot
  > thinking about bonds as total return in the after in the in an environment of secular declining interest rates that's a pretty good strategy
  indicator: bond yields trend · asset: rates · direction: long bonds up in secular decline, limited at zero rates · horizon: years · conditions: Secular falling yields; fails near zero lower bound · testable: yes: bond returns by rate regime · confidence: high
  ^MT156-C05-2
- **Jeff Rosenberg** Weaker bond diversification opens space for systematic trend and liquid alternatives as diversifiers.  #mech/structural_shift
  > opening the door if you will for other types of diversifying strategies to help fill the gap that is being created by the structural change
  asset: multi · direction: allocate to trend and liquid alternatives · horizon: years · conditions: When stock-bond correlation is less negative · testable: partly: portfolio diversification benefit testable · confidence: medium
  ^MT156-C05-3
- **Jeff Rosenberg** Post-Covid inflation plus accelerated government debt creates fiscal dominance and financial-repression tail risk for fixed income.  #mech/fiscal_debt
  > not only did we create inflation, we also created a tremendous amount of government debt along the way
  indicator: government debt levels · asset: rates · direction: long government bonds at risk · horizon: years · conditions: High debt developed markets · testable: partly: debt/GDP and term premium · confidence: high
  ^MT156-C05-4

### C06
- **Jeff Rosenberg** Inflation uncertainty reversed the long decline in term premium and real rates.  #mech/structural_shift
  > uncertainty sort of undid the secular decline in in in term premium and and uh real interest rates falling
  indicator: term premium, real rates · asset: rates · direction: term premium and real rates up · horizon: years · testable: partly · confidence: medium
  ^MT156-C06-1
- **Jeff Rosenberg** Systematic models built on fundamentals assume free price setting; under financial repression or Fed-Treasury coordination rates are set administratively, so models must account for it (e.g. 1942-51 pegged rates).  #mech/fiscal_debt
  > if prices are not free to be set by those signals, then you you got to recognize that.
  indicator: administered interest rates · asset: rates · horizon: years · conditions: Fiscal dominance / yield-curve control regimes · testable: partly: regime break in rates models · confidence: high
  **Correction (cross-check):** The '1942-51' date is not in the transcript. Rosenberg only refers to the pre-1951 Treasury-Fed accord regime (front end about 3/8%, long end about 2.5%, which he says someone should fact check). → Models built on fundamentals assume prices are free; under financial repression or Fed-Treasury coordination rates are set administratively, as in the US regime before the 1951 accord (fixed rates, long end about 2.5% per the speaker's uncertain recollection).
  ^MT156-C06-2
- **Jeff Rosenberg** Models should not rely only on growth and inflation indicators to explain interest rates because soft financial repression can set them.  #mech/fiscal_debt
  > there are soft forms of repression that you need to be aware of
  asset: rates · horizon: years · testable: partly · confidence: medium
  ^MT156-C06-3
- **Jeff Rosenberg** As a fiduciary, systematic managers can avoid repression by moving away from long government bonds when valuations are poor, since repression transfers wealth from investors.  #mech/risk_management
  > if you saw things like poor valuations in long-term government bonds, you might pivot away
  indicator: long-term government bond valuation · asset: rates · direction: underweight long government bonds · horizon: months · conditions: When valuation poor and repression likely · testable: yes: valuation-conditioned bond allocation · confidence: medium
  ^MT156-C06-4

### C07
- **Jeff Rosenberg** Separate beta, smart beta/risk premia and alpha explicitly because they need different data, skill and fee levels; market-neutral alpha is the hardest.  #mech/research_method
  > the different sources of returns have very different risk profiles
  asset: multi · testable: no: framing · confidence: high
  ^MT156-C07-1
- **Jeff Rosenberg** Market-beta-and-factor-neutral alpha measured by information ratio is the hardest return stream to deliver.  #mech/research_method
  > It is the hardest thing in our investing world to achieve market
  indicator: information ratio · asset: equities · testable: partly · confidence: high
  ^MT156-C07-2
- **Jeff Rosenberg** BlackRock Systematic's platform rests on Grinold and Kahn's active portfolio management: find an edge and put it into portfolios systematically (the framework behind the fundamental law).  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > how do you have edge and systematically put edge into portfolios and that's the kind of fundamental basis for for for our entire investment platform
  indicator: Grinold-Kahn fundamental law · asset: multi · testable: yes - IR decomposed into skill, breadth, transfer coefficient · confidence: high
  ^MT156-C07-X1
- **Jeff Rosenberg** Systematic firms have long used predictive AI (older machine learning) and now also generative AI; client demand now centers on generative AI, so the label hides which kind of model is doing the work.  #mech/research_method _(added by sonnet-xhigh cross-check, time-bound view)_
  > we've been doing artificial intelligence before artificial intelligence was cool
  indicator: predictive vs generative AI · asset: multi · testable: no - descriptive · confidence: medium
  ^MT156-C07-X2
- **Jeff Rosenberg** If every manager becomes 'systematic' the label stops differentiating and edge gets crowded; he nevertheless sees it as good for the industry because systematic investing brings outcome orientation and explicit separation of return sources.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check)_
  > there's this risk here that everybody's becoming systematic and then like nobody's systematic and we're losing the differentiation
  asset: multi · horizon: years · testable: no - qualitative · confidence: medium
  ^MT156-C07-X3

### C08
- **Jeff Rosenberg** Systematic funds are engineered to deliver a known return profile; trend has a specific profile that a well risk-budgeted implementation delivers, though not in all environments.  #mech/risk_management
  > we call it engineering for outcomes
  asset: multi · testable: partly · confidence: medium
  ^MT156-C08-1
- **Jeff Rosenberg** Trend is not good in all environments but is very diversifying in particular ones, so it should be held for diversification.  #mech/research_method
  > there are not all environments in which trend is a great strategy
  indicator: trend following · asset: multi · direction: trend good in crisis and strong markets · conditions: Fails in trendless or reversal markets · testable: yes: conditional performance · confidence: high
  ^MT156-C08-2
- **Niels Kaastrup-Larsen** Pure trend following was historically ignored by the very large asset managers, but big houses (BlackRock, Fidelity, Invesco) have launched trend products in the last year or two, a structural shift in who offers trend and in what wrapper.  #mech/structural_shift _(added by sonnet-xhigh cross-check, time-bound view)_
  > it was never popular. It was never uh a strategy talked much about or embraced much about uh embraced by by the very large asset managers frankly but that's changing
  indicator: launches of trend products by large managers · asset: multi · direction: more trend capacity from large managers · horizon: years · conditions: rising demand for diversifiers · testable: partly - launch counts and AUM are observable · confidence: high
  ^MT156-C08-X1

### C09
- **Jeff Rosenberg** Trend is the time-series cousin of price momentum, the equity factor literature's big factor, so trend, factor and ML approaches blend.  #mech/behavioral
  > trend on a broader context is is momentum a a and price momentum if
  indicator: price momentum · asset: multi · testable: yes · confidence: medium
  ^MT156-C09-1
- **Jeff Rosenberg** The pure trend ETF (ISMF) deliberately keeps a simple, expected trend profile, while the multi-strategy ETF (iAlt) is more ambitious and adds momentum and machine-learning elements to modify the payoff profile.  #mech/research_method _(added by sonnet-xhigh cross-check, time-bound view)_
  > just taking a very simple strategy and and and keeping it simple and and replicating what investors expect out of trend and trying to deliver a trend-like experience
  indicator: simple trend vs enhanced momentum/ML · asset: multi · testable: partly - needs fund track records · confidence: high
  ^MT156-C09-X1
- **Niels Kaastrup-Larsen** Managed futures has a dual mandate, long-run return uncorrelated to equities and crisis alpha at times of stress, and the balance between them shapes signal speed and risk allocation across markets.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > delivering a return stream that's uncorrelated to equities over the kind of long term, but also delivering crisis alpha or whatever you like to call it at times of stress
  indicator: trend speed vs crisis alpha · asset: multi · direction: faster systems for crisis alpha, slower for long-run return · horizon: years · conditions: trade-off between the two goals · testable: yes - speed-bucket backtest vs crisis-period returns · confidence: high
  ^MT156-C09-X2

### C10
- **Jeff Rosenberg** 2025 policy uncertainty created repeated reversals (inception 13 March 2025), which was very hard for trend; slower signals, multiple windows and breadth helped.  #mech/slow_reaction _(time-bound view)_
  > trend hates reversals and and and and the policy uncertainty of this world has been you know a reversal engine
  indicator: trend following, policy uncertainty · asset: multi · direction: trend loses in reversals · horizon: months · conditions: 2025 tariff / policy shock reversals · testable: yes: trend returns vs policy-uncertainty index · confidence: high
  ^MT156-C10-1
- **Jeff Rosenberg** Fundamental law: IR = skill x sqrt(breadth) x transfer coefficient; momentum has little skill so breadth and risk budgeting drive results.  #mech/research_method
  > the law of active management information ratio is is skill times the square root of breath times transfer coefficient
  indicator: information ratio, breadth · asset: multi · direction: more markets raises IR · conditions: Requires independent bets · testable: yes: IR vs number of markets · confidence: high
  ^MT156-C10-2
- **Jeff Rosenberg** Use the law of active management: with weak per-bet skill, win through breadth and transfer coefficient.  #mech/risk_management
  > The the key is breadth uh and then transfer coefficient like getting into your portfolios, managing the risk and and risk budgeting.
  asset: multi · testable: partly · confidence: high
  ^MT156-C10-3
- **Jeff Rosenberg** ETF structure caps breadth since the fund must scale, producing a trade-off between breadth, diversification and capacity.  #mech/liquidity_flows
  > how much breadth can you have is is sort of limited by by the structure because you need it to be able to scale
  indicator: number of contracts, capacity · asset: multi · conditions: ETF wrapper · testable: partly · confidence: high
  ^MT156-C10-4
- **Niels Kaastrup-Larsen** Narrow replicator trend ETFs may have outperformed by lucky market selection rather than by systematic edge; commodities add breadth.  #mech/research_method _(time-bound view)_
  > it was just basically because of fortuitous selection of a few markets
  asset: commodities · horizon: years · testable: yes: compare narrow vs broad basket · confidence: medium
  ^MT156-C10-5

### C11
- **Jeff Rosenberg** In 2024 trend funds were differentiated by whether they held cocoa futures, a small non-scalable contract, so BlackRock excluded it for scalability.  #mech/crowding_positioning _(time-bound view)_
  > the differentiator was did you have cocoa futures in your in your basket and the ones that did did great and the ones that didn't were underperformers
  indicator: cocoa futures · asset: commodities · horizon: months · conditions: 2024 · testable: yes: attribution · confidence: high
  ^MT156-C11-1
- **Jeff Rosenberg** Their trend ETF trades about 40+ liquid contracts across FX, rates, commodities and equities, chosen by testing lists for liquidity, diversification and capacity.  #mech/risk_management
  > We're about somewhere about over 40 uh individual contracts
  indicator: number of contracts · asset: multi · testable: partly · confidence: high
  ^MT156-C11-2
- **Jeff Rosenberg** It is hard to forecast which environment (tails or middle) is next, so hold trend for diversification not for timing.  #mech/risk_management
  > own these things from a portfolio diversification perspective and less from a timing perspective
  asset: multi · testable: partly · confidence: high
  ^MT156-C11-3
- **Jeff Rosenberg** Very concentrated trend baskets outperform when they happen to hold the right markets and miss other periods; the goal is consistency of delivering the intended outcome, not luck-driven outperformance.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > these very concentrated strategies, yeah, you're going to get some outperformance when when you're in the lucky right spot and then you're going to you're going to miss it in other days
  indicator: breadth of trend portfolio · asset: multi · direction: broad baskets give more consistent results · horizon: years · conditions: applies to ETFs limited by capacity · testable: yes - dispersion of narrow vs broad trend baskets · confidence: high
  ^MT156-C11-X1

### C12
- **Jeff Rosenberg** Because credit shorts are capacity constrained, credit insights (Merton) were used to trade equities long-short instead.  #mech/new
  > Credit is very capacity constrained on the short side.
  asset: equities · testable: partly · confidence: high
  ^MT156-C12-1
- **Jeff Rosenberg** Merton-style capital-structure signals link equity and debt value.  #mech/research_method
  > how can we take signals and inputs from the equity to value uh the debt
  indicator: Merton distance to default type signals · asset: credit · testable: yes · confidence: medium
  ^MT156-C12-2
- **Jeff Rosenberg** Limiting a market-neutral equity universe to ~500-600 firms with debt increases dispersion between winners and losers, especially in down markets, so alpha is stronger when diversification is needed.  #mech/behavioral
  > oh, what does debt do? It accelerates dispersion.
  asset: equities · direction: long/short debt-bearing firms · conditions: Defensive alpha strategy, market, beta and factor neutral · testable: yes: dispersion in debt vs non-debt firms · confidence: high
  ^MT156-C12-3
- **Jeff Rosenberg** In down markets analysts focus on balance sheet, liquidity and credit access rather than the income statement, so overweighting balance-sheet signals gives alpha concentrated in drawdowns.  #mech/behavioral
  > When things are really tough, you batten down the hatches.
  indicator: balance sheet, liquidity, cost of credit signals · asset: equities · conditions: Down markets · testable: yes: signal IC by market state · confidence: high
  ^MT156-C12-4
- **Jeff Rosenberg** Defensive alpha is strong in very down markets and okay in up markets (long-put-like payoff) while being beta-neutral.  #mech/risk_management
  > that profile kind of looks like a short sorry long put option profile but without the timing and without the directionality
  asset: equities · testable: yes · confidence: high
  ^MT156-C12-5
- **Jeff Rosenberg** Trend has a smile and defensive alpha a different convex shape; combine uncorrelated payoff profiles.  #mech/risk_management
  > Trend has a particular the CTA smile. It's good in really down markets. It's good in really strong up markets.
  asset: multi · testable: yes · confidence: high
  ^MT156-C12-6
- **Jeff Rosenberg** Their multi-strategy blends uncorrelated profiles with fixed-income-like volatility as a bond complement, while the ETF version is a higher-octane equity substitute.  #mech/risk_management
  > in systematic multi strategy we do it with a fixed income anchoring
  asset: multi · testable: partly · confidence: medium
  ^MT156-C12-7

### C13
- **Jeff Rosenberg** Implementation alpha is larger in less liquid asset classes (credit, EM, high yield, commodities); in liquid ones execution is about scale and avoiding market impact.  #mech/liquidity_flows
  > We we we call it implementation alpha.
  asset: multi · testable: partly · confidence: high
  ^MT156-C13-1
- **Jeff Rosenberg** Internal crossing of index, active and systematic flows reduces market impact and a systematic investor's footprint.  #mech/liquidity_flows
  > they all get traded together
  asset: multi · conditions: Large asset manager · testable: partly · confidence: medium
  ^MT156-C13-2
- **Alan Dunne** Combining several defensive strategies is motivated by different equity-drawdown types (short sharp sell-offs versus prolonged ones like 2022 or the dot-com unwind), since each strategy protects in a different kind of drawdown.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > because we'll have different types of equity drawdowns like you know short sharp ones more prolonged
  indicator: drawdown shape · asset: equities · direction: diversify defensive strategies across drawdown types · testable: yes - strategy returns by drawdown type · confidence: medium
  ^MT156-C13-X1

### C14
- **Jeff Rosenberg** ETF wrappers constrain liquidity, capacity and leverage versus Cayman hedge fund vehicles; so quant strategies must be adapted.  #mech/risk_management
  > Uh ETFs are a 40act rapper, but they just add some additional uh constraints
  asset: multi · testable: partly · confidence: high
  ^MT156-C14-1

### C15
- **Jeff Rosenberg** Leverage limits designed for beta exposure misfit long-short neutral strategies.  #mech/risk_management
  > leverage in an uncorrelated asset world means something very different than what leverage means in the beta world
  asset: multi · testable: no · confidence: high
  ^MT156-C15-1
- **Jeff Rosenberg** Low-volatility contracts need huge notional per unit of risk, so contract choice weighs risk per notional too.  #mech/risk_management
  > attract a huge amount of notional leverage to to you know deliver a similar level of risk
  indicator: notional per unit of risk · asset: rates · direction: exclude low-vol contracts in capped-leverage wrappers · testable: yes · confidence: high
  ^MT156-C15-2
- **Niels Kaastrup-Larsen** CalPERS moving to a total portfolio approach mid-2026 should raise allocations to uncorrelated strategies.  #mech/liquidity_flows _(time-bound view)_
  > they're going to move to a total portfolio approach where each investment actually has to be justified in terms of its contribution to the total portfolio
  asset: multi · direction: more allocation to uncorrelated strategies · horizon: years · testable: no · confidence: medium
  ^MT156-C15-3
- **Niels Kaastrup-Larsen** A Capgemini report (as recalled by the host, number not exact) sees alternative investments growing two to three times from about $5 trillion, one data point for rising allocator demand for alternatives.  #mech/liquidity_flows _(added by sonnet-xhigh cross-check, time-bound view)_
  > they saw a massive growth two threefold from the $5 trillion we see right now
  indicator: alternatives AUM forecast · asset: multi · direction: alternatives assets rise · horizon: years · conditions: source and exact figure not verified in the talk · testable: partly - forecast only · confidence: low
  ^MT156-C15-X1

### C16
- **Jeff Rosenberg** Record market-cap concentration (top 10 about 40% of S&P 500, tech and AI) makes market beta less diversified, increasing demand for uncorrelated liquid alternatives.  #mech/crowding_positioning _(time-bound view)_
  > 40% of the S&P 500 market cap is now in the top 10 names
  indicator: top-10 weight in S&P 500 · asset: equities · horizon: years · conditions: Late 2025 · testable: yes: concentration level · confidence: high
  ^MT156-C16-1
- **Jeff Rosenberg** Uncorrelated return streams matter more than crisis alpha alone in concentrated markets.  #mech/structural_shift
  > an uncorrelated return stream uh is very attractive in an environment where you've got a lot of concentration in your market betas
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT156-C16-2
- **Jeff Rosenberg** The shift to a whole-portfolio (total portfolio) lens, long used by institutions, is spreading to retail: products should be judged by their contribution in context, not in isolation, which favors uncorrelated strategies.  #mech/structural_shift _(added by sonnet-xhigh cross-check)_
  > bringing this whole portfolio perspective to a broader audience to a retail audience moving away from kind of a a specific product focus uh evaluating products in isolation as opposed to evaluating in in in the context
  indicator: contribution to total portfolio · asset: multi · direction: more allocation to diversifying strategies · horizon: years · testable: partly - allocation behavior · confidence: high
  ^MT156-C16-X1
- **Jeff Rosenberg** Liquid alternatives should be defined by strategy (long/short, momentum or trend as intellectual property) rather than by asset type; trend is an alternative strategy that can deliver uncorrelated return even when trading ordinary assets.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > Trend is an alternative strategy. It invests somewhat in alternative assets
  asset: multi · testable: no - classification · confidence: high
  ^MT156-C16-X2

### C17
- **Jeff Rosenberg** Rule of thumb: 50/30/20 with 20% alternatives replaces 60/40.  #mech/new
  > 50 30 20 is the new 6040 like 20% of your portfolio in alternatives
  asset: multi · testable: partly · confidence: medium
  ^MT156-C17-1
- **Alan Dunne** Allocators want to participate in the equity rally but with protection, via multi-strat, defensive alpha or trend.  #mech/behavioral _(time-bound view)_
  > are we 95 or 99? You know, this rally could go on for quite a while
  asset: equities · conditions: Late equity rally · testable: no · confidence: medium
  ^MT156-C17-2
- **Niels Kaastrup-Larsen** Institutions understand trend better but still doubt it when markets do not trend, as in 2025.  #mech/behavioral
  > equally uh uncomfortable uh with the strategy when uh things are not trending so to speak
  asset: multi · horizon: years · conditions: Trendless periods · testable: no · confidence: medium
  ^MT156-C17-3
- **Jeff Rosenberg** Small tilts around a concentrated market beta do not diversify enough; the answer is allocating a sizeable portion (the 20% of 50/30/20) to uncorrelated strategies.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > really get you away from that market beta enough. And this is where allocating a good portion of your portfolio
  indicator: allocation size to uncorrelated assets · asset: multi · direction: raise alternatives to around 20% · horizon: years · conditions: market-cap concentration high · testable: yes - portfolio simulation of tilt vs allocation size · confidence: medium
  ^MT156-C17-X1
- **Jeff Rosenberg** The 20% alternatives sleeve can mix illiquid assets (earning an illiquidity premium and showing smoother marks) with liquid alternatives (true diversification, daily marks); his own preference is all liquid.  #mech/risk_premium _(added by sonnet-xhigh cross-check)_
  > it may be a mixture between taking some ill liquidity premium for diversification um in terms of marktomarket risk liquid alternatives for diversification
  indicator: illiquidity premium vs liquid alternatives · asset: multi · direction: mix of illiquid and liquid alternatives · horizon: years · conditions: mark-to-market tolerance · testable: partly - premium net of smoothing is debated · confidence: medium
  ^MT156-C17-X2
- **Alan Dunne** From the allocator side, the shift in bond-equity correlation is a main driver of the case for hedge fund strategies, liquid alternatives and trend.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > bond equity correlation shift is a big driver for for allocators
  indicator: bond-equity correlation · asset: multi · direction: more allocations to alternatives as correlation turns positive · horizon: years · testable: yes - correlation vs alternatives flows · confidence: high
  ^MT156-C17-X3

### C18
- **Niels Kaastrup-Larsen** Cheap trend ETFs (85 bps) compromise market breadth for scalability and may fail to match traditional CTA performance in a stress event.  #mech/research_method _(time-bound view)_
  > I worry that that will come back to haunt the industry because at some point something is going to happen
  asset: multi · horizon: years · conditions: Narrow, low-fee replicators · testable: partly: compare replicator to CTA indices · confidence: medium
  ^MT156-C18-1
- **Jeff Rosenberg** In the uncorrelated space dispersion between products is large, so manager selection requires looking under the hood.  #mech/research_method
  > In the uncorrelated space there's much much more diversification.
  asset: multi · testable: yes: dispersion between trend products · confidence: high
  ^MT156-C18-2
- **Niels Kaastrup-Larsen** At ~85 bps flat fees an ETF needs about $10 billion to be a viable business, pushing sponsors to cut breadth for scalability (against full-fee CTAs at ~115 bps), which is the mechanism behind the narrow-basket risk.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check, time-bound view)_
  > the fees are so low that you need 10 billion to make it even a a a good business
  indicator: ETF fee vs required AUM · asset: multi · direction: narrower baskets in low-fee trend ETFs · horizon: years · conditions: fee-compression pressure · testable: yes - fee, AUM and breadth of trend ETFs · confidence: medium
  ^MT156-C18-X1

