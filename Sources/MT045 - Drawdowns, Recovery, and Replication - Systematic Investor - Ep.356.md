---
source_id: MT045
title: "Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356"
date: 2025-07-17
channel: "Top Traders Unplugged"
url: 
words: 11233
claims: 55
added_by_opus: 3
corrections: 1
crosscheck: "opus cross-check"
speakers: ["Niels Kaastrup-Larsen (host, Top Traders Unplugged)", "Katy Kaminski (AlphaSimplex, trend following researcher; caption 'Katie Kaminsky')"]
tags: [source, layer0]
---
# Drawdowns, Recovery, and Replication - Systematic Investor - Ep.356

**Speakers:** Niels Kaastrup-Larsen (host, Top Traders Unplugged); Katy Kaminski (AlphaSimplex, trend following researcher; caption 'Katie Kaminsky')

**Summary:** Top Traders Unplugged Ep.356 (mid July 2025): Katy Kaminski on her paper about managed futures drawdowns and recovery, exogenous vs endogenous shocks, a non-parametric regime paper and CTA replication. Conclusions: drawdowns coincide with strong equities and recover fast in stress, rebalance rather than time trend, replicators outperformed due to slower speed and smaller sets.

**Approach:** trend following, drawdown recovery, regimes, replication, shocks

**Opus completeness estimate of first read:** 0.94 - first reader covered the drawdown paper, shock types, regime method and replication debate well; missed one disagreement (low rates vs Trump for 2015-19), the turbulence metric and the Denmark/euro aside, and misattributed one explanation.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | intro, CME floor traders lawsuit; nothing actionable |
| C02 | 1 | China-focused CTA programs in June, euro and Bulgaria, dollar weakness chat |
| C03 | 5 | COMEX copper surge on tariffs, metals trends, July positioning, asset classes trending |
| C04 | 5 | fixed income and energies in trend, equity sentiment shift, index numbers, intro to drawdown paper |
| C05 | 3 | why the paper, drawdown sizes, durations and equity state during drawdowns |
| C06 | 3 | recovery speed vs equity regime, portable alpha blend, bond vs equity momentum |
| C07 | 4 | fixed income regimes, trade-war drawdowns, fastest S&P recovery, Trump 2.0 vs 1.0 |
| C08 | 5 | rhetoric vs fundamentals, copper tariff, CTA winter, CTA vs equity drawdown size |
| C09 | 3 | rolling returns, rebalancing not timing, investor behaviour, alternatives to trend |
| C10 | 4 | trend as equity complement, exogenous vs endogenous shocks intro |
| C11 | 5 | shock types and trend, Covid vs Liberation Day, digestion speed |
| C12 | 3 | short vs long term in shocks, introduction of non-parametric regime paper |
| C13 | 2 | regime paper method: state variables, distance metric, historical filtering |
| C14 | 3 | overfitting, trend and recessionary regimes, replication outperformance question |
| C15 | 3 | replication tracking error, slower and smaller sets, regression vs mechanical |
| C16 | 3 | replication regimes and tracking error; outro |
| C17 | 0 | outro |

## Claims

### C02
- **Niels Kaastrup-Larsen** China-focused CTA programs underperformed traditional CTAs in June 2025, probably because Chinese futures are commodity heavy and geopolitical moves hit energies hard, while metals trended.  #mech/cycle_persistence _(time-bound view)_
  > CTA programs that are focused on China markets actually had somewhat of a different experience in June, doing somewhat worse than the traditional CTA programs
  indicator: China-focused CTA programs vs traditional CTAs · asset: commodities · horizon: weeks · conditions: June 2025 · testable: yes - index comparison · confidence: medium
  **Correction (Opus):** Attributes the explanation to Niels; Niels only reports that China-focused CTA programs did worse in June 2025 and says he does not know why. The commodity-heavy explanation is Kaminski's explicitly labelled first guess. → Niels: China-focused CTA programs did worse than traditional CTAs in June 2025. Kaminski (a guess): Chinese futures are commodity heavy, energies were shocked by geopolitics while some supply-chain metals trended, so results there differed from other markets.
  ^MT045-C02-1
- **Niels Kaastrup-Larsen** Staying outside the euro (Denmark) has worked better than joining because the country keeps control of its own interest rates, and the krone has stayed strong.  #mech/policy_reaction _(added by Opus)_
  > I actually think Denmark has done better than the Euro zone because they stand outside and can still determine their own interest rates
  indicator: Danish krone; Denmark vs euro-area growth · asset: fx · horizon: years · testable: partly - Denmark vs euro-area outcomes, though the krone is pegged to the euro · confidence: medium
  ^MT045-C02-X1

### C03
- **Niels Kaastrup-Larsen** COMEX copper rose about 13% in a day on tariff news (largest since 1968) while London and Chinese copper were unaffected, and CTAs were likely on the right side.  #mech/policy_reaction _(time-bound view)_
  > this is the largest single day price surge in records going back to 1968
  indicator: COMEX copper · asset: commodities · direction: Copper up · horizon: days · conditions: tariff announcement · testable: yes - price data · confidence: high
  ^MT045-C03-1
- **Katy Kaminski** Isolated tariff events can start trends: long signals in metals (copper, platinum) were building on trade tension and potential tariffs.  #mech/policy_reaction _(time-bound view)_
  > it shows how isolated incidents can actually directly link to trends that extend
  indicator: metals trend signals · asset: commodities · direction: Long metals · horizon: months · testable: partly · confidence: medium
  ^MT045-C03-2
- **Katy Kaminski** The commodity sector provides diversification that most investors do not hold directly, which CTAs supply.  #mech/risk_management
  > it just shows the diversification of the commodity sector that you know a lot of investors don't really have exposure to directly
  asset: commodities · testable: partly · confidence: medium
  ^MT045-C03-3
- **Niels Kaastrup-Larsen** In early July 2025 CTAs were long equities and metals and short US fixed income with some gains in livestock and grains; European fixed income was tricky.  #mech/cycle_persistence _(time-bound view)_
  > also some short exposure in fixed income, US fixed income I should say, probably doing okay for for managers
  indicator: CTA positioning · asset: multi · direction: Long equities, long metals, short US bonds · horizon: weeks · testable: partly · confidence: medium
  ^MT045-C03-4
- **Katy Kaminski** Equities and a weak dollar trended most in 2025, though the dollar had started to revert in July.  #mech/cycle_persistence _(time-bound view)_
  > the two asset classes that have actually trended the most this year has been equities recently
  asset: multi · direction: Long equities, short USD · horizon: months · testable: yes · confidence: high
  ^MT045-C03-5

### C04
- **Katy Kaminski** Fixed income was choppy (steepening and flattening, Fed back and forth) so trend signals gave it little weight.  #mech/cycle_persistence _(time-bound view)_
  > fixed income is definitely underweighted by trend falling signals
  asset: rates · horizon: months · testable: yes · confidence: high
  ^MT045-C04-1
- **Katy Kaminski** Energies spiked, reversed and rebounded in June-July 2025, which was hard for trend following, while metals tied to trade policy were more interesting.  #mech/overshoot _(time-bound view)_
  > energies were really tricky last month because they shocked big and then they came back down and now they're back up again
  indicator: energy prices · asset: commodities · horizon: weeks · testable: yes · confidence: high
  ^MT045-C04-2
- **Katy Kaminski** Discretionary investors who cut equities in April find it psychologically hard to buy back at record highs, while systematic managers are indifferent.  #mech/behavioral _(time-bound view)_
  > to now having to suddenly consider buying back at all-time highs I mean these are psychologically very difficult decisions to make
  asset: equities · horizon: months · testable: partly · confidence: medium
  ^MT045-C04-3
- **Katy Kaminski** Sentiment shifted in early July 2025 toward better growth with rotation into US small caps, a tentative environment for equities.  #mech/behavioral _(time-bound view)_
  > I've seen a pretty large shift in sentiment um in the last two weeks or so where the world is kind of saying actually growth looks a little better than we thought
  indicator: growth sentiment, small vs large cap · asset: equities · direction: Equities up · horizon: weeks · testable: partly · confidence: medium
  ^MT045-C04-4
- **Niels Kaastrup-Larsen** Mid-July 2025 CTA indices were down about 3% to 10% year to date while MSCI World was up 8.7% and S&P 500 up 5.85%.  #mech/cycle_persistence _(time-bound view)_
  > Stocken trend flat for the month so far, down 10% for the year
  indicator: CTA indices year to date · asset: multi · horizon: months · testable: yes - index data · confidence: high
  ^MT045-C04-5

### C05
- **Katy Kaminski** Among managed-futures drawdowns above 10%, the largest was 2015-2019 (Trump's first term era), and the paper plots drawdown depth, duration and recovery.  #mech/research_method
  > the largest draw down was actually between 2015 and 2019
  indicator: SG Trend Index drawdowns · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT045-C05-1
- **Katy Kaminski** Drawdown and recovery times vary a lot, so the current drawdown could recover fast or slowly.  #mech/cycle_persistence
  > that just shows that there's a lot of variation across different draw down periods
  indicator: drawdown duration and recovery · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT045-C05-2
- **Katy Kaminski** Trend drawdowns tend to occur while equities are doing very well (shown with equity returns during each SG Trend Index drawdown).  #mech/risk_premium
  > equities tend to be doing very well. Um, when things are difficult for us
  indicator: equity return during trend drawdown · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT045-C05-3

### C06
- **Katy Kaminski** Recoveries from trend drawdowns are faster when equities are stressed and slower when equities keep making new highs, so trend is useful in both.  #mech/cycle_persistence
  > it tends to be really challenging environments, recovery is a lot faster
  indicator: drawdown recovery time vs equity returns · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT045-C06-1
- **Niels Kaastrup-Larsen** A blend of trend following and the S&P 500 gives nearly the sum of both returns (portable alpha), explaining the stream of new overlay products.  #mech/risk_management
  > you almost get the sum of the two meaning both returns on top of each other
  indicator: trend plus equity blend · asset: multi · horizon: years · testable: yes - blend backtest · confidence: high
  ^MT045-C06-2
- **Niels Kaastrup-Larsen** Per Ilmanen's paper, bonds have more inbuilt momentum while equities revert (V-shapes), so fixed income gives the best trend profits.  #mech/behavioral
  > even though people think of say fixed income as more mean reverting, it actually has an more of an inbuilt momentum
  indicator: trend returns by asset class · asset: multi · direction: Bond trend > equity trend · horizon: years · testable: yes · confidence: medium
  ^MT045-C06-3

### C07
- **Katy Kaminski** Fixed-income trend depends on regime: strong in falling rates with a steep curve, strong short when the curve is inverted, mixed when flat as now.  #mech/cycle_persistence
  > trend has done very well in a falling rate environment especially when the curve is steep
  indicator: rate direction, yield curve slope · asset: rates · direction: Long bonds in falling rates with steep curve; short when inverted · horizon: years · testable: yes - regime study · confidence: high
  ^MT045-C07-1
- **Niels Kaastrup-Larsen** The two worst trend drawdown-recovery combinations coincided with Trump trade-war periods, 2018 and 2025.  #mech/policy_reaction
  > the worst two are really the uh the trade war number one which is Trump's first uh term and then now the liberation
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT045-C07-2
- **Niels Kaastrup-Larsen** The post-Liberation Day S&P recovery (57 days, no Fed support) was the fastest ever from a 20% drawdown, a V-shape that trend following is not built for.  #mech/overshoot _(time-bound view)_
  > the recovery that we've seen in the S&P 500 uh, since liberation day uh, of a 20% or more draw down is the quickest recovery on record
  indicator: S&P 500 recovery time · asset: equities · horizon: weeks · testable: yes - price data · confidence: high
  ^MT045-C07-3
- **Katy Kaminski** Trump 1.0 tweets did not create much trend, but Trump 2.0 coincides with larger global change in geopolitics and supply chains.  #mech/structural_shift _(time-bound view)_
  > we were doing a a study of Trump's tweets and we just didn't find that much trends that he could trump
  asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT045-C07-4
- **Katy Kaminski** Kaminski disputes that the 2015-2019 trend drawdown was mainly a Trump trade-war effect; the very low rate environment of that period was also a cause.  #mech/policy_reaction _(added by Opus)_
  > I don't necessarily think that the longest draw down was particularly just linked to that particular presidency. It was just a period with very low rates as well.
  indicator: policy rate level during trend drawdowns · asset: multi · direction: trend returns weaker when rates are pinned near zero · horizon: years · conditions: disagrees with Niels's Trump attribution · testable: yes - trend returns conditioned on rate level · confidence: medium
  ^MT045-C07-X1

### C08
- **Katy Kaminski** For trend, initial rhetoric-driven shocks are bad, but once fundamental data show the new direction (e.g. copper tariffs) trends emerge in asset classes.  #mech/slow_reaction
  > the initial shock is often bad because it's based on rhetoric and people realizing that change is coming
  asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT045-C08-1
- **Niels Kaastrup-Larsen** Tariff-driven positions (long copper) are fragile because tariffs can be reversed by the next statement.  #mech/policy_reaction _(time-bound view)_
  > I'm hoping for something a little bit more substantial than than a tariff
  asset: commodities · horizon: weeks · testable: no · confidence: medium
  ^MT045-C08-2
- **Niels Kaastrup-Larsen** Trend recoveries often follow a real narrative change in a broad range of markets, such as rates rising after the post-GFC period.  #mech/structural_shift
  > recoveries are often linked to kind of an real narrative change
  asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT045-C08-3
- **Katy Kaminski** The 'CTA winter' (2010-2014, second longest drawdown) came after the GFC when the world recovered and ended with the 2014 energy collapse.  #mech/cycle_persistence
  > that period before 2014 before energies um exploded
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT045-C08-4
- **Niels Kaastrup-Larsen** CTA index drawdowns of about 20% are small next to a 55% S&P 500 drawdown.  #mech/risk_management
  > CTA drawdowns are so much smaller than equity draw down
  indicator: drawdown comparison · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT045-C08-5

### C09
- **Niels Kaastrup-Larsen** The Man paper shows rolling 12-month CTA returns below -5% are very rare compared to returns above +15% (about 59 vs 2-4 instances).  #mech/research_method
  > the rolling 12 months return that are less than minus5% for the CTA index
  indicator: rolling 12-month CTA index return · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT045-C09-1
- **Katy Kaminski** Do not time trend following; the strategy mean-reverts at long horizons, so rebalance (buy after drawdowns, trim after gains).  #mech/cycle_persistence
  > the key is you shouldn't time, but you should, you know, rebalance
  asset: multi · horizon: years · testable: yes - rebalancing study · confidence: high
  ^MT045-C09-2
- **Niels Kaastrup-Larsen** Investors chase performance and rarely rebalance into trend after poor returns.  #mech/behavioral
  > I see people selling trend after it's done well. I rarely see people buying trend when it's done poorly
  asset: multi · horizon: years · testable: partly - flow data · confidence: medium
  ^MT045-C09-3

### C10
- **Katy Kaminski** Trend following is one of few robust equity complements that pays in distress; no better alternative has been found.  #mech/risk_premium
  > it's one of the few things that tends to on average um do well during periods of distress or challenging equity markets
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT045-C10-1
- **Katy Kaminski** Institutions build layered defensive portfolios of different diversifiers, trend as one layer.  #mech/risk_management
  > I have my you know my first responders, my second responders, my third responders
  asset: multi · testable: no · confidence: medium
  ^MT045-C10-2
- **Niels Kaastrup-Larsen** Evaluate trend by its portfolio effect, not stand-alone Sharpe.  #mech/risk_management
  > a lot of people like to look at individual line items rather than looking at what the effect on the portfolio is doing and they use sharp for something they should never use sharp for
  asset: multi · testable: yes · confidence: medium
  ^MT045-C10-3
- **Niels Kaastrup-Larsen** CFM's work separates exogenous shocks (Liberation Day tariffs) from endogenous ones (2022 rates positioning) for CTA performance.  #mech/research_method
  > exogenous shocks and impacts on CTO CTA performance versus indogenous so things that comes from inside the system and not from the outside
  asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT045-C10-4

### C11
- **Katy Kaminski** Exogenous shocks that reverse quickly (whipsaw) are the worst for trend, but those that extend can help.  #mech/overshoot
  > an exogenous shock that is not sustainable in shorter term that just is sort of a whipssaw those are the worst
  asset: multi · horizon: weeks · testable: yes · confidence: high
  ^MT045-C11-1
- **Katy Kaminski** Covid was less damaging than Liberation Day because supply chain trouble was anticipated and bonds rallied, giving trends outside equities.  #mech/slow_reaction
  > they started buying bonds so there were some interesting trends that actually leaked out in other asset classes in COVID
  asset: multi · direction: Long bonds, short energy · horizon: months · testable: partly · confidence: medium
  ^MT045-C11-2
- **Katy Kaminski** After Liberation Day, further shocks (copper tariffs) get smaller reactions; endogenous shocks (monetary policy, inflation) are more likely next.  #mech/behavioral _(time-bound view)_
  > the market is much more reticent to react because the change and the shock has already occurred
  asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT045-C11-3
- **Katy Kaminski** Endogenous shocks (policy, inflation) tend to help trend because they are fundamental valuation shifts.  #mech/structural_shift
  > endogenous shocks tend to be more positive for uh trend perhaps because it's it's really a fundamental based shift in sort of how people are valuing assets
  asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT045-C11-4
- **Niels Kaastrup-Larsen** Trend works because news is digested at different speeds; a tariff is understood instantly but Covid took time, leaving time to position short energy.  #mech/slow_reaction
  > we all get the news at the same time but we kind of digest it at different speeds
  asset: multi · horizon: weeks · testable: no · confidence: medium
  ^MT045-C11-5
- **Katy Kaminski** Turbulence metrics (magnitude-of-surprise measures across assets) can be used to identify and size exogenous shocks when studying their effect on trend following.  #mech/research_method _(added by Opus)_
  > we wrote a great paper a couple years ago on turbulence and actually that man paper mentioned the turbulence metrics
  indicator: market turbulence index (magnitude surprise) · asset: multi · horizon: days · testable: yes - turbulence index vs trend returns · confidence: medium
  ^MT045-C11-X1

### C12
- **Niels Kaastrup-Larsen** Short-term CTAs beat long-term in April 2025 but the order reversed in May-June.  #mech/cycle_persistence _(time-bound view)_
  > Short-term doing better like it should uh compared to long-term, but actually it's kind of completely reversed in the last uh couple of months
  indicator: short-term vs long-term CTA · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT045-C12-1
- **Katy Kaminski** A three-day shock followed by rebound is too short to detect statistically, unlike Covid, which lasted a month or two.  #mech/slow_reaction
  > in liberation day it was really just you know a three-day move two or three days
  asset: multi · horizon: days · testable: yes · confidence: high
  ^MT045-C12-2
- **Katy Kaminski** A non-parametric regime approach avoids pre-defining regimes (rising or falling rates), which creates bias; critics say the seven state variables were chosen with hindsight.  #mech/research_method
  > nonparametric means that you're not sort of defining parameters to define regimes
  asset: multi · testable: yes · confidence: high
  ^MT045-C12-3

### C13
- **Katy Kaminski** The Harvey et al. regime method standardises seven state variables (equities, yield curve shape, volatility, copper, etc.) and measures Euclidean distance of the current month to every past month.  #mech/research_method
  > what is known as a uklidian distance measure or a measure of similarity
  indicator: seven state variables; Euclidean distance · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT045-C13-1
- **Katy Kaminski** Strategies that did well in similar past months are expected to do well next month, so one overweights trend or value accordingly.  #mech/cycle_persistence
  > if it did well in all those past events, we assume that regimes are somewhat persistent
  indicator: regime similarity forecast · asset: multi · horizon: months · testable: yes - walk-forward test · confidence: medium
  ^MT045-C13-2

### C14
- **Katy Kaminski** Rule-based regime definitions overfit history, so tests must be walk-forward and account for how many variables were tried.  #mech/research_method
  > you come up with all these huge parameter space of decisions you're very likely to fit history
  asset: multi · testable: yes · confidence: high
  ^MT045-C14-1
- **Katy Kaminski** Trend likely connects to recessionary regimes (e.g. inverted curve in fixed income), which the non-parametric method could test.  #mech/cycle_persistence
  > I'm pretty certain um you're going to see some regime connection between trend um and certain sort of more recessionary regimes
  asset: multi · horizon: years · testable: yes - proposed · confidence: medium
  ^MT045-C14-2
- **Niels Kaastrup-Larsen** Replicators outperformed their benchmarks in 2025, implying either large tracking error or a separate alpha strategy.  #mech/research_method _(time-bound view)_
  > replication strategies have done quite a lot better uh than uh the benchmarks they're trying to replicate
  indicator: replicator vs benchmark return · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT045-C14-3

### C15
- **Katy Kaminski** Replicators are smaller in market set and slower, so they reacted less to Liberation Day shock and kept near average CTA returns.  #mech/slow_reaction _(time-bound view)_
  > most of the replicator strategies out there are, you know, a little smaller in asset set. They also, um, are tending to be more slow in terms of, you know, how they move
  asset: multi · horizon: months · testable: yes · confidence: high
  ^MT045-C15-1
- **Katy Kaminski** Replicator tracking error in 2025 is within expected range per the paper's methodology.  #mech/research_method _(time-bound view)_
  > tracking error is kind of within range uh for for what we expect
  indicator: tracking error · asset: multi · horizon: months · testable: yes · confidence: medium
  ^MT045-C15-2
- **Katy Kaminski** Regression-based replication is slowest; mechanical or hybrid replication can be faster to track CTA performance.  #mech/research_method
  > regression based is really sort of looking at the past and that is the slowest approach
  indicator: replication method speed · asset: multi · testable: yes · confidence: high
  ^MT045-C15-3

### C16
- **Katy Kaminski** Replicators miss markets outside their set (cocoa), so differences reflect market regimes not luck.  #mech/structural_shift
  > if you were trying to trade Coco two years ago like replication cannot pick that up
  asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT045-C16-1
- **Katy Kaminski** Tracking error depends on market set and implementation, so investors must understand inputs to measure it.  #mech/research_method
  > you're running an a replicated replication strategy that has no European debt and only trades US, you're going to see variation where you don't capture those European moves
  indicator: tracking error vs market set · asset: rates · testable: yes · confidence: high
  ^MT045-C16-2
- **Katy Kaminski** Replication can be a separate strategy combined with CTAs to reduce dispersion.  #mech/risk_management
  > it's just another strategy that can be combined with other CTAs that might smooth the overall dispersion
  asset: multi · testable: partly · confidence: medium
  ^MT045-C16-3

