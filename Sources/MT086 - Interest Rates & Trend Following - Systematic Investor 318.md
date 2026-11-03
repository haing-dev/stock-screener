---
source_id: MT086
title: "Interest Rates & Trend Following - Systematic Investor 318"
date: 2024-10-23
channel: "Top Traders Unplugged"
url: 
words: 10955
claims: 56
added_by_opus: 5
corrections: 0
crosscheck: "opus cross-check"
speakers: ["Katy Kaminski (chief research strategist, AlphaSimplex)", "Niels Kaastrup-Larsen (host, Top Traders Unplugged)"]
tags: [source, layer0]
---
# Interest Rates & Trend Following - Systematic Investor 318

**Speakers:** Katy Kaminski (chief research strategist, AlphaSimplex); Niels Kaastrup-Larsen (host, Top Traders Unplugged)

**Summary:** Systematic Investor 318: Kaminski and Kaastrup-Larsen review 2024 trend-following performance and dispersion, her defensive-rotation paper (bonds long/short helps in every crisis) and Quantica's high vs low cash rate study. Conclusions: inflation drives stock-bond correlation, trend diversifies 60/40 more when rates are high (about 15-20% allocation), and allocate to trend in drawdowns.

**Approach:** trend following, managed futures, crisis alpha, stock-bond correlation, interest rate regimes, allocation

**Opus completeness estimate of first read:** 0.89 - first reader caught nearly all performance numbers, paper findings and allocation numbers; missed a few interpretive/method points (positioning delta as recession signal, falling-rate dependence of 60/40, long-history backtest limits, rate level vs inflation).

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro, disclaimer, MIT Nobel small talk |
| C02 | 2 | Danish energy trader wellness anecdote; trader physiology |
| C03 | 6 | Oct 2024 index performance; difficult environment; themes |
| C04 | 5 | 2024 attribution by sector; monetary policy pivot drove noise |
| C05 | 3 | low to high rate regime, inflation view, Fed plan |
| C06 | 5 | new paper: defensive rotation, crisis positioning, bonds in crises |
| C07 | 4 | energy long/short in crises; bonds behaving badly; stock-bond correlation |
| C08 | 3 | commodities in crises; correlation drivers |
| C09 | 4 | inflation and stock-bond correlation; manager dispersion: speed, asset class |
| C10 | 3 | non-trend/carry influence; SG Trend factor paper |
| C11 | 2 | trend timing futility, divergent regimes; Turtle teaser |
| C12 | 2 | upcoming risks: inflation; election; Quantica intro |
| C13 | 6 | Quantica paper on high vs low cash rates |
| C14 | 3 | allocation conclusions 55/35/10 vs 55/25/20; investor demand |
| C15 | 3 | allocate in drawdown; signals even; research |
| C16 | 0 | outro, predictions small talk |

## Claims

### C02
- **Niels Kaastrup-Larsen** A Danish power and energy trading firm trades systematically at very high frequency, an example of a high-turnover commodity shop that made large profits when energy prices exploded in 2022.  #mech/new _(time-bound view)_
  > they do on average like 30,000 trades per day and on a busy day like 100,000 trades
  asset: commodities · horizon: days · testable: no: anecdote about one firm · confidence: low
  ^MT086-C02-1
- **Katy Kaminski** Risk taking has a physiological component: neuro-finance studies show trader cortisol correlates with the VIX, so discretionary traders are affected by stress.  #mech/behavioral
  > they were studying sort of the physiological response of traders to the market and it is true it's their point was that it's really a physical activity so taking risk is a physical activity
  indicator: VIX; cortisol · asset: other · testable: no: not a market signal · confidence: medium
  ^MT086-C02-2

### C03
- **Katy Kaminski** Trend following is a medium to long horizon strategy, so it needs less intense trader stress management than high-frequency trading.  #mech/structural_shift
  > Trend following is is a little bit less energy uh it's it's a medium to long strategy
  asset: multi · horizon: months · testable: no: descriptive · confidence: medium
  ^MT086-C03-1
- **Niels Kaastrup-Larsen** In October 2024 (to Tuesday) trend indices were down for the month: BTOP 50 -1.5% (+2.6% YTD), SG CTA about -2.1% (flat YTD), SG Trend -3.25% (about -1% YTD), short-term traders -0.67%.  #mech/cycle_persistence _(time-bound view)_
  > BTO 50 index down 1.5% for the month still up 2.6% for the year
  indicator: BTOP50; SG CTA; SG Trend; SG Short-Term Traders · asset: multi · horizon: months · testable: yes: published index returns · confidence: high
  ^MT086-C03-2
- **Niels Kaastrup-Larsen** Traditional markets in Oct 2024 were up: MSCI World +0.33% for the month and +17.86% YTD; global sovereign bonds -0.47%; S&P 500 +1.39% for the month and about +22.5% YTD, so trend lagged stocks.  #mech/new _(time-bound view)_
  > S&P 500 as I mentioned on a tear up another 1.39% this month up 225% so far this year
  indicator: MSCI World; S&P 500; S&P Global Developed Sovereign Bond index · asset: equities · horizon: months · testable: yes: index data · confidence: high
  ^MT086-C03-3
- **Niels Kaastrup-Larsen** CTA replicators showed large tracking error against the CTA indices they benchmark in 2024.  #mech/research_method _(time-bound view)_
  > tracking error is how I describe it between CTA replicator and the indices that they're trying to to Benchmark against
  indicator: CTA replicators vs SG indices · asset: multi · horizon: months · testable: yes: tracking error measurable · confidence: medium
  ^MT086-C03-4
- **Niels Kaastrup-Larsen** October 2024 trend losses came from currency reversals (GBP, AUD, NZD) and fixed income corrections, with bright spots in grains, gold and US equities.  #mech/overshoot _(time-bound view)_
  > we've seen some corrections in the currency sector showing up um markets that you know like British pounds and some of the commodity uh currencies Aussie and kiwi dollar for sure
  asset: multi · horizon: months · testable: no: period description · confidence: medium
  ^MT086-C03-5
- **Katy Kaminski** Trend following results depend on whether markets have a persistent macro theme; in 2024 several markets were driven by volatility and uncertainty without one, hurting trend.  #mech/cycle_persistence
  > what were the trends and What markets were sort of driven by volatility and uncertainty where there wasn't really a sort of a key macros theme
  asset: multi · horizon: months · conditions: works with persistent macro themes; fails in theme-less, uncertainty-driven markets · testable: partly: needs a measure of theme persistence · confidence: medium
  ^MT086-C03-6

### C04
- **Katy Kaminski** In 2024 CTA P&L was positive in equities, mixed in commodities, and weak in currencies and fixed income.  #mech/cycle_persistence _(time-bound view)_
  > it has been pre predominantly positive for equities um Commodities has been mixed and positive in certain Pockets but really the The Thorn and the side has been currencies and fixed income
  indicator: CTA sector P&L · asset: multi · horizon: months · testable: yes: sector attribution · confidence: high
  ^MT086-C04-1
- **Katy Kaminski** Trend following needs extreme, disruptive, consistent moves; when monetary-policy expectations ebb and flow (yes/no/maybe data), rates and FX trend signals whipsaw.  #mech/policy_reaction
  > once you look back at it from a from more sort of a policy perspective because really in the trend world we like things to be extreme disruptive consistent
  asset: multi · horizon: months · conditions: fails when policy expectations oscillate without a clear direction (2024) versus clear 2022 direction · testable: partly: define signal stability or whipsaw measure · confidence: high
  ^MT086-C04-2
- **Katy Kaminski** Over summer 2024 the market focus shifted from inflation to slowdown, and trend positions rotated defensively (commodities down, bonds up).  #mech/policy_reaction _(time-bound view)_
  > we saw a pivot from a focus on inflation for uh monetary policy to economic slowdown and potential for demand destruction and as you saw that um Trends did a rotation into a more defensive posture
  asset: multi · horizon: months · testable: no: narrative of one period · confidence: medium
  ^MT086-C04-3
- **Katy Kaminski** In October 2024 markets had priced in aggressive Fed cuts and then repriced, reversing trend positions in rates and currencies.  #mech/overshoot _(time-bound view)_
  > people were too far ahead of themselves and expecting that fed policy would be aggressive
  indicator: Fed rate expectations · asset: rates · horizon: weeks · testable: no: one episode · confidence: medium
  ^MT086-C04-4
- **Katy Kaminski** Sentiment swung between fear and optimism within weeks in autumn 2024, showing the market was grasping for direction, a transition phase in which trends do not stabilise.  #mech/behavioral _(time-bound view)_
  > whenever you ask anybody what's going to happen everyone goes back and forth I mean this is what I'm noticing in sentiment you go from the first half of September being like everything's terrible to the second half
  asset: multi · horizon: weeks · testable: no: anecdotal · confidence: low
  ^MT086-C04-5

### C05
- **Katy Kaminski** Investors hoping for a return to low rates magnify sentiment swings, which adds noise to trend signals during the regime transition.  #mech/behavioral
  > we have a large number of people that are still holding on to this idea aidea that you know we're going to go back to normal
  asset: multi · horizon: years · conditions: during regime transitions · testable: no: not measurable directly · confidence: medium
  ^MT086-C05-1
- **Katy Kaminski** Kaminski's macro view: inflation matters more now, the post-2008 low-rate regime was historically abnormal and the baseline of rates may stay higher with more inflation volatility.  #mech/structural_shift _(time-bound view)_
  > we've moved into a regime where inflation is much more important um and that we are probably not going to go back to the regime post 2008 this you know golden period of low interest rates
  asset: rates · direction: higher baseline rates, higher inflation volatility · horizon: years · testable: no: macro opinion · confidence: medium
  ^MT086-C05-2
- **Niels Kaastrup-Larsen** The Fed's expected plan is a 12-18 month cutting cycle down to about 3-3.5%, still much higher than the previous low.  #mech/policy_reaction _(time-bound view)_
  > the plan probably is that we have 12 18 months of a cutting cycle it comes down to three three and a half%
  indicator: Fed funds path · asset: rates · horizon: months · testable: yes: later checkable · confidence: low
  ^MT086-C05-3

### C06
- **Katy Kaminski** In summer 2024 trend followers' aggregate positioning pivoted defensive: from short to long bonds and from long to short energy and commodities.  #mech/crowding_positioning _(time-bound view)_
  > you saw positions go from being short fixed income to Long fixed income um you saw um energy positions and commodity positions that were generally long moving to short
  indicator: CTA positioning in bonds, energy, commodities · asset: multi · direction: long bonds, short energy/commodities · horizon: months · testable: partly: positioning data needed · confidence: medium
  ^MT086-C06-1
- **Katy Kaminski** The 2024 defensive trend positioning resembled early 2020 (bought bonds to hedge equity, sold energy and commodities), raising the question of what such positioning does in a later equity drawdown.  #mech/crowding_positioning _(time-bound view)_
  > it actually started to rhyme with the positioning we saw preco which made me a little nervous because that's exactly what you saw at the beginning of uh 2020
  indicator: trend positioning pattern · asset: multi · horizon: months · testable: partly: only a few analog episodes · confidence: medium
  ^MT086-C06-2
- **Katy Kaminski** Her paper finds fixed income was a positive contributor to trend-following returns in every equity crisis/drawdown period studied, because the bond market reacts early and trend can be long or short bonds.  #mech/risk_premium
  > fixed income in every crisis period was a positive contributor for Trend falling
  indicator: trend-following fixed income P&L conditional on equity drawdowns · asset: rates · direction: long or short bonds following trend · horizon: months · conditions: equity drawdown / crisis periods · testable: yes: crisis-conditional attribution · confidence: high
  ^MT086-C06-3
- **Katy Kaminski** A dynamic long/short trend exposure to fixed income is a good diversifier in a world with higher cash rates and inflation risk, not just long bonds.  #mech/risk_management
  > a dynamic trendall exposure to fixed income seems to work well in crisis
  indicator: bond trend signal · asset: rates · direction: long/short bonds by trend · horizon: months · conditions: higher cash rate and inflation · testable: yes · confidence: medium
  ^MT086-C06-4
- **Katy Kaminski** Currency and energy trend contributions in crises are environment dependent: long USD worked in some events; energy can contribute a lot but direction varies.  #mech/cycle_persistence
  > being long the dollar has worked sometimes in certain events um and if you look across energies it can also be a big contributor but it really depends on the environment
  indicator: USD and energy trend P&L in crises · asset: multi · horizon: months · conditions: depends on the crisis type · testable: partly: small sample of crises · confidence: medium
  ^MT086-C06-5
- **Katy Kaminski** A shift (delta) in aggregate trend-follower positioning toward long bonds and short commodities is itself a market signal that recession expectations are being repriced and economic weakness is possible.  #mech/cycle_persistence _(added by Opus)_
  > more buying of bonds and sort of selling off of Commodities that's a relatively uh defensive position it sort of shows some potential for economic weakness potentially repricing of recession expectations
  indicator: change in aggregate CTA positioning (bonds long, commodities short) · asset: multi · direction: defensive pivot -> higher odds of economic weakness / equity drawdown · horizon: months · testable: yes - estimate CTA positioning from trend signals and relate defensive pivots to later growth data and equity drawdowns · confidence: medium
  ^MT086-C06-X1

### C07
- **Katy Kaminski** In COVID trend was short energy and in 2022 long energy: trend profits in crises come from the ability to move with whichever trend prevails, not from a fixed hedge direction (crisis alpha).  #mech/cycle_persistence
  > Co it was being shorten energy uh in 2022 it was being long energy
  indicator: energy trend · asset: commodities · direction: short energy 2020, long energy 2022 · horizon: months · conditions: disruptive events · testable: yes: historical · confidence: high
  ^MT086-C07-1
- **Katy Kaminski** Over long histories, higher inflation brings higher bond volatility and more positive stock-bond correlation (paper: Bonds Behaving Badly).  #mech/fiscal_debt
  > as you look over longer Horizons for fixed income whenever you have higher inflation um you tend to have higher volatility for bonds and you also tend to have more positive correlation between stocks and bonds
  indicator: bond volatility; stock-bond correlation; inflation · asset: rates · horizon: years · conditions: high-inflation regimes · testable: yes: long-history data, back to 1970s · confidence: high
  ^MT086-C07-2
- **Katy Kaminski** Trend following in bonds (long or short) yields strongly negative correlation to stocks even when static bonds correlate positively, so it fixes the 60/40 diversification loss.  #mech/risk_management
  > by having a dynamic long short being able to be long or short and following Trends in those asset classes you actually can get strong negative correlation uh from that Dynamic strategy
  indicator: bond trend returns vs stocks · asset: rates · horizon: years · conditions: higher inflation / rate regimes · testable: yes · confidence: high
  ^MT086-C07-3
- **Katy Kaminski** Static bonds are a less reliable diversifier in higher rate/inflation environments, so 60/40 needs more long/short exposure to improve correlation properties.  #mech/risk_management
  > bonds are much more volatile and less predictable uh as a diversifier in an environment with higher rates Andor inflation as a Potential Threat for bonds
  indicator: 60/40 portfolio · asset: multi · direction: add long/short trend exposure · horizon: years · conditions: higher rates or inflation · testable: yes · confidence: medium
  ^MT086-C07-4
- **Niels Kaastrup-Larsen** The protection 60/40 investors got from negative stock-bond correlation depended, largely unknowingly, on a secular falling-rate cycle, so it need not persist once that cycle ends.  #mech/structural_shift _(added by Opus)_
  > if you have a 60/40 portfolio people will have relied on the negative correlation uh and and probably without knowing it the fact that we were in a in an interest rate cycle that just kept going down
  indicator: stock-bond correlation; rate cycle direction · asset: multi · horizon: years · conditions: holds while rates trend down; weakens when the rate cycle ends · testable: yes - stock-bond correlation and 60/40 drawdowns split by falling vs rising rate eras · confidence: medium
  ^MT086-C07-X1
- **Katy Kaminski** Very long trend-following backtests are only credible for single-asset-class signals (e.g. bonds), because extending a full multi-asset futures portfolio back in time requires many assumptions about market infrastructure.  #mech/research_method _(added by Opus)_
  > unless you stick to just Trend falling signals in one asset class because you know obviously like the infrastructure the Futures markets they you know you have to make a lot of assumptions
  asset: multi · conditions: pre-futures-era history · testable: partly - compare single-asset long-history trend results with modern multi-asset results over the overlap · confidence: high
  ^MT086-C07-X2

### C08
- **Katy Kaminski** In crisis periods fixed income and commodities provide the most interesting trend profits; the paper focuses on energy as a proxy for global demand shocks; currencies are tricky.  #mech/cycle_persistence
  > I think Commodities come in second in our paper we focused on energies
  indicator: energy trend returns in crises · asset: commodities · horizon: months · testable: yes · confidence: medium
  ^MT086-C08-1
- **Katy Kaminski** Testing trend performance conditional on positive stock-bond correlation is hard because the post-1990 sample has few such periods; longer data back to the 1970s is needed.  #mech/research_method
  > there's been very few periods of time where um stock Bond correlation is positive um so it does become an empirically challenging task
  indicator: stock-bond correlation sign · asset: multi · horizon: years · testable: partly: limited sample · confidence: high
  ^MT086-C08-2
- **Katy Kaminski** Positive stock-bond correlation is driven by inflation, because inflation devalues fixed long-term bond cash flows and erodes their safe-haven property.  #mech/fiscal_debt
  > a core driver can be um inflation and we've seen that so if you think about bonds from the perspective of of they are basically fixed on long-term cash flows
  indicator: stock-bond correlation; inflation expectations · asset: rates · horizon: years · conditions: when inflation expectations are non-negligible · testable: yes · confidence: high
  ^MT086-C08-3

### C09
- **Katy Kaminski** With inflation near 2-2.5% (2024) stock-bond correlation returned to the classic risk-off pattern (stocks down, bonds up), versus 2022-23 when both fell.  #mech/new _(time-bound view)_
  > without inflation bonds are sort of a pure more of a pure Safe Haven trade because they're fixed cash flows they're safe
  indicator: stock-bond correlation · asset: rates · horizon: years · testable: yes · confidence: high
  ^MT086-C09-1
- **Niels Kaastrup-Larsen** Niels doubts stock-bond correlation will revert to the persistent negative correlation of the first decades of this century.  #mech/structural_shift _(time-bound view)_
  > I actually don't think necessarily we're going to see it also just go back to this negative correlation that we saw for these decades
  indicator: stock-bond correlation · asset: multi · horizon: years · testable: partly: future correlation · confidence: low
  ^MT086-C09-2
- **Katy Kaminski** Manager dispersion in 2024: slower (medium to long term) trend signals did better because they did not chase the many undulations, versus faster crisis-alpha signals.  #mech/slow_reaction _(time-bound view)_
  > slower I think has tended to be a little bit better this year because there were a lot of undulations
  indicator: trend signal speed · asset: multi · horizon: months · conditions: choppy markets with reversals favour slower signals · testable: yes: test by lookback · confidence: medium
  ^MT086-C09-3
- **Katy Kaminski** Dispersion also came from asset-class risk allocation: managers with more risk in equities and commodities beat those with more in bonds and FX in 2024.  #mech/risk_management _(time-bound view)_
  > basic Trend signals suggests that equities and commodities were the two areas where there were key themes uh whereas fixed income and um currencies were challenging
  asset: multi · horizon: months · testable: yes: sector attribution · confidence: medium
  ^MT086-C09-4

### C10
- **Katy Kaminski** A third source of dispersion was non-trend signals such as FX carry/relative value, exposed to the August 2024 yen carry unwind; even small carry allocations create large relative gaps.  #mech/crowding_positioning _(time-bound view)_
  > how much other non- Trend signals did you have that were exposed to some of these rather violent moves um for example the carry trade in August
  indicator: FX carry; yen carry trade · asset: fx · horizon: weeks · conditions: August 2024 carry unwind · testable: yes · confidence: medium
  ^MT086-C10-1
- **Katy Kaminski** Her 2018 factor analysis of the SG Trend index showed that over time index constituents slowed down and picked up non-trend premia exposure (value, carry, cross-sectional momentum), especially post-2008.  #mech/structural_shift
  > the increase of influence of non- trend strategies within the index across different factors like value carry across different asset classes um crosssectional momentum exposure
  indicator: SG Trend index factor decomposition · asset: multi · horizon: years · conditions: post-2008 · testable: yes: factor regression · confidence: medium
  ^MT086-C10-2
- **Katy Kaminski** In a higher-rate regime pure momentum has become more desirable, so the index may drift back toward faster, purer trend.  #mech/structural_shift _(time-bound view)_
  > the macro shifts have been made sort of pure momentum a lot more desirable in a higher interest rate
  asset: multi · horizon: years · testable: partly: needs updating the factor study · confidence: low
  ^MT086-C10-3

### C11
- **Katy Kaminski** Investors should hold managed futures as a reactive strategy rather than try to time which trend will come; big regime changes are only recognised after the fact.  #mech/research_method
  > it's not about really what trend they think is going to work that they need managed Futures as something that reacts to those Trends um because timing these things it's just it's it's a Fool's game
  asset: multi · horizon: years · testable: no: philosophy · confidence: high
  ^MT086-C11-1
- **Katy Kaminski** Trend followers do better in divergent environments (large, one-directional macro moves like 2022) than in convergent, consolidating ones.  #mech/cycle_persistence
  > we tend to do better in those Divergent environments versus a convergent environment where things are kind of consolidating and if you really think about it 2022 was very Divergent
  asset: multi · horizon: years · conditions: divergent regime works; convergent fails · testable: partly: needs a divergence measure · confidence: high
  ^MT086-C11-2

### C12
- **Katy Kaminski** Kaminski's market view (Oct 2024): the bigger risk to a soft-landing consensus is renewed inflation (CPI uptick, commodities rebounding, China stimulus, port closures), with rates paused and higher for longer, which could drive next year's trends.  #mech/policy_reaction _(time-bound view)_
  > for us the bigger risk on the medium to longterm are more an uptick in inflation and sort of what does that mean
  indicator: CPI; commodities · asset: multi · horizon: years · testable: no: macro opinion · confidence: medium
  ^MT086-C12-1
- **Niels Kaastrup-Larsen** Niels expects China trade policy to continue whoever wins the 2024 US election, limiting election impact.  #mech/policy_reaction _(time-bound view)_
  > a lot of the policies that uh Trump installed Visa China they have continued under the current regime and probably will continue whoever wins
  asset: multi · horizon: months · testable: no · confidence: low
  ^MT086-C12-2
- **Katy Kaminski** A trend follower's way to anticipate the next big trend is to ask what investors are underestimating or overly hopeful about (in 2024 the soft-landing consensus), since the unpriced outcome drives the next large move.  #mech/behavioral _(added by Opus)_
  > as a trender I'm always thinking about what are the things that investors are underestimating particularly what are they being overly hopeful about that may be a little unlikely
  asset: multi · horizon: months · testable: partly - compare surveyed consensus expectations with later realised moves · confidence: medium
  ^MT086-C12-X1

### C13
- **Niels Kaastrup-Larsen** A common objection to trend following at high cash rates is that bonds yield 5%, but a trend portfolio also earns the cash yield (collateral) plus trend returns and diversification.  #mech/risk_premium
  > why do I need Trend following because now I can just buy bonds at 5% and I think this you know it's a fair statement but it also shows that maybe they don't don't fully understand the benefit
  indicator: cash rate on futures collateral · asset: multi · horizon: years · conditions: high cash rates · testable: yes · confidence: medium
  ^MT086-C13-1
- **Katy Kaminski** Quantica's Q3 2024 paper splits history into high and low cash-rate regimes and finds stock-bond correlation is much higher when cash rates are high, so 60/40 diversifies less.  #mech/new
  > Bond correlations um change significantly U between stocks and bonds when cash rates are higher
  indicator: cash rate regime; stock-bond correlation · asset: multi · horizon: years · conditions: high cash rate · testable: yes: data since 1990 · confidence: high
  ^MT086-C13-2
- **Katy Kaminski** Quantica finds trend following correlates negatively with bonds in high cash-rate periods and slightly positively in low cash-rate periods.  #mech/new
  > Trend falling is negatively correlated with bonds
  indicator: trend index vs bonds, split by cash rate · asset: multi · horizon: years · conditions: high cash rate regime · testable: yes · confidence: high
  ^MT086-C13-3
- **Katy Kaminski** Trend following has higher volatility and a wider return range in high cash-rate regimes.  #mech/new
  > Trend falling has a little bit more volatility in return during higher cash rate environments um and then also um expected return range were higher
  indicator: trend return volatility by cash regime · asset: multi · horizon: years · conditions: high cash rate · testable: yes · confidence: medium
  ^MT086-C13-4
- **Katy Kaminski** With higher cash rates, adding trend following to a 60/40 portfolio helps more because bonds lose diversification while trend keeps return and negative correlation.  #mech/risk_management
  > as cash rates are higher you actually better off adding Trend because of the negative correlation to your portfolio
  indicator: portfolio allocation to trend · asset: multi · horizon: years · conditions: high cash rate · testable: yes: mean-variance on data · confidence: medium
  ^MT086-C13-5
- **Katy Kaminski** The limitation of the Quantica study: its data start in 1990, a period of mostly low cash rates, so evidence for long high-rate or high-inflation periods is thin.  #mech/research_method
  > the data starts in 1990 so you know that data period is definitely one where cash rates are much much lower
  asset: multi · horizon: years · testable: no: sample caveat · confidence: high
  ^MT086-C13-6
- **Katy Kaminski** Splitting regimes by the level of cash rates (Quantica) and by inflation (Bonds Behaving Badly) are related but distinct conditioning variables, so results from one need not carry over to the other.  #mech/research_method _(added by Opus)_
  > they didn't focus on inflation but they focused on the level of rates which is somewhat corelated but not the same thing
  indicator: cash rate level vs inflation regime · asset: multi · horizon: years · testable: yes - run the same regime study conditioning on rate level and on inflation and compare · confidence: medium
  ^MT086-C13-X1

### C14
- **Niels Kaastrup-Larsen** Quantica's optimal mixes: in low cash-rate regimes 55/35/10 (stocks/bonds/trend) beats 60/40; in high cash-rate regimes 55/25/20.  #mech/risk_management
  > in low cach environments a 55 3510 with 10 being trend uh would be uh more optimal uh than 60/40 uh and in higher cash rate environments it's actually TW 55 25 and 20 to Trend
  indicator: portfolio weights stocks/bonds/trend · asset: multi · direction: raise trend weight from 10% to 20% when cash rates are high · horizon: years · conditions: high cash rate · testable: yes · confidence: medium
  ^MT086-C14-1
- **Niels Kaastrup-Larsen** Rule of thumb: if you cannot judge the rate regime, hold about 15% in trend as core allocation; 2-3% allocations are too small to help in a crisis.  #mech/risk_management
  > they should just simply pick 15 as the core allocation to Trend which in an odd way is is not necessarily a bad number
  indicator: trend allocation size · asset: multi · direction: 15% allocation to trend · horizon: years · testable: partly: sizing study · confidence: medium
  ^MT086-C14-2
- **Katy Kaminski** Investor interest in managed futures and liquid alternatives has risen because 2022 showed the 60/40 diversification can vanish.  #mech/behavioral _(time-bound view)_
  > that 2022 kind of woke people up to that um just when the diversification was gone between bonds and stocks
  indicator: fund flows · asset: multi · horizon: years · testable: partly: flows data · confidence: medium
  ^MT086-C14-3

### C15
- **Niels Kaastrup-Larsen** Niels notes risk (leverage) had come out of trend portfolios in late 2024 because of changed correlations, making a lower-risk entry point even in a drawdown.  #mech/risk_management _(time-bound view)_
  > risk has generally come off come out of trend falling portfolios or with the CH because of the changes in correlation and and Expos in in in the equity and bond relationship
  indicator: trend portfolio risk level · asset: multi · horizon: months · testable: partly · confidence: low
  ^MT086-C15-1
- **Katy Kaminski** Allocate to trend after drawdowns rather than after strong gains: consolidation periods often precede new trends, so chasing trend-following performance is worse.  #mech/cycle_persistence
  > it's usually better to allocate the trend in a draw down than it is to kind of trend fall Trend falling or Trend falling squared
  indicator: manager performance · asset: multi · direction: allocate to trend after drawdown · horizon: years · testable: yes: allocation timing backtest on trend indices · confidence: medium
  ^MT086-C15-2
- **Katy Kaminski** In Oct 2024 trend signals across asset classes were balanced with no standout, which she reads as an inflection point before the next big trend, possibly after the election or Fed meetings.  #mech/cycle_persistence _(time-bound view)_
  > Trend signals across different asset classes are pretty even so there's nothing that's really sticking out at this point
  indicator: cross-asset trend signal strength · asset: multi · horizon: months · testable: partly: signal dispersion measure · confidence: low
  ^MT086-C15-3

