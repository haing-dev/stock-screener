---
source_id: MT083
title: "Inside Q1’s Chaos - Systematic Investor - Ep.394"
date: 2026-04-06
channel: "Top Traders Unplugged"
url: 
words: 13158
claims: 67
added_by_crosscheck: 2
corrections: 0
crosscheck: "opus cross-check"
speakers: ["Niels Kaastrup-Larsen (host, Top Traders Unplugged)", "Katie Kaminski (Alpha Simplex, trend following researcher)", "Harry Moore (partner and senior client portfolio manager, Man AHL)"]
tags: [source, layer0]
---
# Inside Q1’s Chaos - Systematic Investor - Ep.394

**Speakers:** Niels Kaastrup-Larsen (host, Top Traders Unplugged); Katie Kaminski (Alpha Simplex, trend following researcher); Harry Moore (partner and senior client portfolio manager, Man AHL)

**Summary:** Systematic Investor episode on Q1 2026 trend following performance (March pivot to inflation and energy) and four papers: optimal market mix for trend, portable alpha, trend drawdowns, assessing alpha in macro strategies. Conclusions: trend diversified in March; traditional liquid markets give crisis alpha; drawdowns are normal.

**Approach:** trend following, portable alpha, crisis alpha, managed futures research

**Cross-check completeness estimate of first read:** 0.96 - first reader captured nearly every claim with correct speakers and numbers; only the move-size-driven manager dispersion point and the portable-alpha research gap (buffers, tail co-dependence) were missing

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 0 | Intro and small talk; nothing actionable |
| C02 | 2 | Small talk; Q1 2026 headlines; trend vs equities |
| C03 | 4 | Q1 2026 trend review: pivot to inflation, YTD numbers |
| C04 | 5 | March dispersion; speed; pure trend vs mixed |
| C05 | 7 | Differentiators; March positioning; carry; index results |
| C06 | 5 | March index returns; optimal market mix paper intro |
| C07 | 4 | Market mix paper: macro factors, crisis vs long-run Sharpe, cash efficiency |
| C08 | 4 | 900 markets and 60 factors; objective functions |
| C09 | 3 | Trend and macro themes; crisis alpha criteria |
| C10 | 4 | Portable alpha paper |
| C11 | 4 | Portable alpha caveats |
| C12 | 3 | Cash buffers; trend margin in crisis |
| C13 | 3 | Trend drawdowns paper, June 2025 setting |
| C14 | 4 | Simulation of 0.6 Sharpe drawdown; Liberation Day shock |
| C15 | 4 | Drawdowns self-correct; change; probability of drawdowns |
| C16 | 3 | Crowding; macro alpha paper |
| C17 | 3 | Macro paper: fees and survivorship |
| C18 | 3 | Geopolitical risk, future topics, allocations |
| C19 | 0 | Outro and disclaimers; nothing actionable |

## Claims

### C02
- **Niels Kaastrup-Larsen** In March 2026 the S&P had its worst quarter since 2022, gold its steepest monthly drop since autumn 2008 and the 60/40 portfolio was stress-tested, a regime in which stocks, bonds and gold fell together.  #mech/crowding_positioning _(time-bound view)_
  > gold the the deepest or the steepest drop on a monthly basis, I think, since the autumn of 2008.
  indicator: S&P 500, gold monthly return, 60/40 · asset: multi · horizon: months · conditions: March 2026 sample · testable: yes - index returns · confidence: high
  ^MT083-C02-1
- **Niels Kaastrup-Larsen** Trend following (SocGen Trend Index) has outperformed MSCI World for six or seven consecutive months into March 2026.  #mech/cycle_persistence _(time-bound view)_
  > this is the sixth or seventh month in a row where trend following uh measured by the SocGen Trend Index has outperformed the MSCI World Index.
  indicator: SocGen Trend Index vs MSCI World · asset: multi · direction: trend outperforms equities · horizon: months · testable: yes - index data · confidence: medium
  ^MT083-C02-2

### C03
- **Katie Kaminski** In Q1 2026 trend followers profited in January and February from continuing themes (weaker dollar, strong equities); in March the themes flipped (inflation, huge energy move), and new trends offset reversals of old ones.  #mech/slow_reaction _(time-bound view)_
  > you kind of found that new trends were building as other trends were pivoting.
  indicator: trend positioning across asset classes · asset: multi · direction: long energy, short bonds in March; long equities and short dollar before · horizon: months · conditions: Works when new trends form quickly enough to offset reversals · testable: yes - trend index returns by sector · confidence: high
  ^MT083-C03-1
- **Katie Kaminski** Energy and short fixed-income/rate positions profited from inflation worries and offset equity losses, showing the diversification value of trend.  #mech/risk_management _(time-bound view)_
  > that diversification that energies and other asset classes, like some of the short rate positions or short positions in fixed income, that profited from the inflation concerns
  indicator: energy and short bond trend positions · asset: multi · direction: long energy and short bonds in inflation shocks · horizon: months · testable: yes - trend sector P&L · confidence: high
  ^MT083-C03-2
- **Harry Moore** Most trend index formulations were up roughly 3 to 7% year to date at end of Q1 2026, a good result against equities, bonds and 60/40.  #mech/cycle_persistence _(time-bound view)_
  > between 3 and kind of 7% on a year-to-date basis
  indicator: trend indices YTD · asset: multi · horizon: months · testable: yes - index data · confidence: high
  ^MT083-C03-3
- **Harry Moore** If inflation returns or escalation continues, neither equities, bonds, gold (wobbling) nor private markets help; trend is a candidate defensive allocation.  #mech/risk_management _(time-bound view)_
  > And it doesn't seem to be equities. It certainly doesn't seem to be bonds.
  indicator: trend vs equities, bonds, gold in inflationary stress · asset: multi · direction: trend as diversifier · horizon: months · conditions: Applies to an inflationary or escalation scenario · testable: partly - scenario argument · confidence: medium
  ^MT083-C03-4

### C04
- **Katie Kaminski** March 2026 dispersion among trend managers came mostly from energy exposure (the first principal component) and from avoiding positions that were selling off.  #mech/crowding_positioning _(time-bound view)_
  > how much energy you had was sort of PCA one, right? So, the more energy you had, the better things were.
  indicator: energy exposure as PC1 of March dispersion · asset: commodities · direction: long energy better · horizon: months · conditions: March 2026 only · testable: yes - attribute manager returns · confidence: medium
  ^MT083-C04-1
- **Katie Kaminski** Faster trend models did better in March 2026 because they could pivot out of reversing trends.  #mech/slow_reaction _(time-bound view)_
  > speed was helpful. So, being able to pivot out of some of these you know, reversing trends also helped.
  indicator: trend speed · asset: multi · direction: faster trend wins at reversals · horizon: months · conditions: At trend reversals · testable: yes - compare speeds · confidence: medium
  ^MT083-C04-2
- **Niels Kaastrup-Larsen** Large CTAs are not pure trend any more; carry and value sub-strategies may explain a good March, so trend should be compared like for like.  #mech/research_method _(time-bound view)_
  > I certainly get the suspicion that certainly not all of them are pure trend anymore.
  indicator: trend share of manager returns · asset: multi · horizon: months · testable: partly - decompose manager returns · confidence: low
  ^MT083-C04-3
- **Harry Moore** Below 70 to 80% trend content, a manager has other return drivers, so a dedicated trend mandate should be judged for how its non-trend part behaves.  #mech/research_method
  > I think once you go below 80, 70% trend following, right? You're starting to introduce different return drivers.
  indicator: trend share of portfolio · asset: multi · testable: partly - decomposition · confidence: medium
  ^MT083-C04-4
- **Harry Moore** Trend following should be a divergent strategy, continuing to bet on what is happening, as opposed to convergent strategies.  #mech/research_method
  > if I'm looking at something that I I would call trend following, I want that to be a divergent strategy.
  asset: multi · testable: no - definition · confidence: high
  ^MT083-C04-5
- **Katie Kaminski** Dispersion between trend managers rises in months with very large moves because small design choices (weights, speed, markets) get amplified; the largest managers stay in a narrow band while mid-sized ones diverge, so one month's ranking says little about skill.  #mech/research_method _(added by opus cross-check)_
  > in a big move, you're always going to see a little bit more dispersion, but that's it's kind of typical given sort of how large the size of the moves are.
  indicator: cross-sectional dispersion of CTA monthly returns vs size of market moves · asset: multi · direction: dispersion up when moves are large · horizon: months · conditions: months with big trend moves or reversals · testable: yes - regress manager return dispersion on absolute market move size · confidence: high
  ^MT083-C04-X1

### C05
- **Harry Moore** Carry, value and similar strategies may do well in a mid-distribution equity unwind but can show horrible left tails in a full liquidity break.  #mech/risk_management
  > if there's a kind of full liquidity break, a dash for cash, sometimes they have these these kind of horrible left tails.
  indicator: carry and value in liquidity crises · asset: multi · horizon: days · conditions: In a dash for cash · testable: yes - tail studies exist · confidence: medium
  ^MT083-C05-1
- **Katie Kaminski** Manager performance differences come from speed, market set and trend vs non-trend share.  #mech/research_method
  > I often just point to the three key differentiators. One is speed, one is market set, third is like trend or non-trend, so how much non-trend.
  indicator: speed, market mix, trend share · asset: multi · testable: yes - attribution · confidence: high
  ^MT083-C05-2
- **Harry Moore** Positioning into March: long oil helped, bonds were mixed because fast models were long then switched short, and most were long equities then scaled down as momentum flipped.  #mech/slow_reaction _(time-bound view)_
  > if you were already long oil coming into March, then you should have done had some some good offsetting profits there.
  indicator: trend positions into March 2026 · asset: multi · horizon: months · conditions: March 2026 only · testable: yes - positions vs returns · confidence: medium
  ^MT083-C05-3
- **Katie Kaminski** In March 2026 energy carry and FX carry worked while bond carry did not.  #mech/cycle_persistence _(time-bound view)_
  > energy carry worked very well. Um FX carry worked well. Bond carry didn't work so well.
  indicator: carry by asset class · asset: multi · horizon: months · conditions: March 2026 only · testable: yes · confidence: medium
  ^MT083-C05-4
- **Katie Kaminski** Faster trend worked in March except in fixed income, which has been a headache for over a year because pivots keep failing.  #mech/slow_reaction _(time-bound view)_
  > we did see that faster was good except for maybe in fixed income.
  indicator: speed of trend in fixed income · asset: rates · horizon: months · conditions: Fixed income reversals false-start · testable: yes · confidence: medium
  ^MT083-C05-5
- **Katie Kaminski** Market-set weights matter when one sector makes a huge move (50% in energy): 10% vs 20% energy weight changes results greatly.  #mech/risk_management _(time-bound view)_
  > when you have the key strongest trend and you have a 50% move in energy, like every different, you know, if you're 10% or if you're 20%, like that makes a huge difference.
  indicator: energy weight in trend portfolio · asset: commodities · horizon: months · conditions: When one sector dominates · testable: yes · confidence: medium
  ^MT083-C05-6
- **Niels Kaastrup-Larsen** Trend indices (Beta 50, SocGen CTA, SocGen Trend) fell only about 0.7 to 1.5% in March 2026 and were up 7% or more YTD.  #mech/cycle_persistence _(time-bound view)_
  > The Beta 50 Index looks to be down only 1.44% still up 7.15% for the year.
  indicator: Beta 50, SocGen CTA and Trend indices · asset: multi · horizon: months · testable: yes - index data · confidence: high
  ^MT083-C05-7

### C06
- **Niels Kaastrup-Larsen** Against the S&P (down about 4.3% YTD), MSCI World and world government bonds, trend did well in March, answering critics who said there was no crisis alpha; the short-term traders index did best (+56 bp).  #mech/risk_management _(time-bound view)_
  > And the S&P 500 Total Return Index down almost 5% in March, down 4.33% so relatively speaking
  indicator: trend indices vs S&P, MSCI World, bonds · asset: multi · horizon: months · conditions: March 2026 · testable: yes · confidence: high
  ^MT083-C06-1
- **Harry Moore** Faster trend trading gives more crisis alpha while slower trading gives a slightly higher Sharpe.  #mech/risk_premium
  > if you trade more quickly you tend to have more crisis alpha if you tend if you trade more a little bit slower you tend to have a slightly higher sharp.
  indicator: trend speed · asset: multi · direction: fast for crisis alpha, slow for Sharpe · horizon: months · testable: yes - Man AHL research · confidence: high
  ^MT083-C06-2
- **Harry Moore** The market universe can be widened from traditional cleared futures (crude, gold) to alternative markets (Nordic hydropower, iron ore, Chinese bitumen and glass) and synthetic markets (equity factors) with different return drivers.  #mech/structural_shift
  > things like Nordic hydropower it might be iron ore.
  indicator: universe of traded markets · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT083-C06-3
- **Harry Moore** The paper builds portfolios with maximum diversification so no market dominates.  #mech/research_method
  > using essentially a maximum diversification so you're you're you're not putting too much weight into into any individual market
  indicator: maximum diversification weights · asset: multi · testable: yes · confidence: high
  ^MT083-C06-4
- **Harry Moore** Traditional markets gave the best Sharpe in crises while alternative markets gave a higher long-run Sharpe.  #mech/risk_premium
  > you say hey well the traditional markets they tended to give me my best sharp in the crisis periods whereas my alternative markets have tended to give me a higher sharp ratio over the long run.
  indicator: Sharpe by market group · asset: multi · horizon: years · testable: yes - Man AHL results · confidence: high
  ^MT083-C06-5

### C07
- **Harry Moore** Traditional markets load more on macro factors (risk on/off, growth, inflation, monetary policy) while alternative markets have more idiosyncratic drivers.  #mech/structural_shift
  > the traditional markets tend to pick up more of those macro factors. And the alternative markets tend to pick up less and so they have more idiosyncratic return drivers.
  indicator: macro factor loadings by market · asset: multi · horizon: years · testable: yes - factor regression · confidence: high
  ^MT083-C07-1
- **Harry Moore** In sell-offs macro factors explain more variance (principal components), so traditional markets do better then.  #mech/liquidity_flows
  > in these in these sell-offs things like risk on risk off or inflation they explain more and therefore the traditional markets do better.
  indicator: macro factor variance share in sell-offs · asset: multi · horizon: days · conditions: In crises · testable: yes - PCA · confidence: high
  ^MT083-C07-2
- **Harry Moore** Maximum crisis-Sharpe portfolio overweights gold, crude and dollar-vs-pound; maximum long-run-Sharpe portfolio overweights alternative markets (hydropower, iron ore, China commodities).  #mech/risk_management
  > that maximum crisis sharp overweights traditional markets.
  indicator: portfolio weights · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT083-C07-3
- **Harry Moore** Traditional markets give maximum cash efficiency, so for portable alpha a trend allocation needs little cash.  #mech/risk_management
  > traditional markets are great for that that cash efficiency.
  indicator: margin per unit of risk · asset: multi · testable: yes · confidence: high
  ^MT083-C07-4

### C08
- **Harry Moore** About 60 equity factors come from roughly 15 style factors times four regions, since regional versions are imperfectly correlated and count as separate markets (about 900 markets overall).  #mech/research_method
  > if I trade value in the US and I trade value in Japan and I trade value in Europe like those aren't perfectly correlated.
  indicator: regional equity factors · asset: equities · testable: yes · confidence: medium
  ^MT083-C08-1
- **Harry Moore** Number of markets is a poor measure of diversification: 30 stock indices are highly correlated while 30 commodities are not.  #mech/research_method
  > If I trade 30 commodity markets cocoa gold crude right? They're they're they're less correlated.
  indicator: market count vs correlation · asset: multi · testable: yes - correlation structure · confidence: high
  ^MT083-C08-2
- **Katie Kaminski** Optimal market mix depends on the objective: max standalone Sharpe vs a defensive crisis-alpha add-on.  #mech/research_method
  > given the markets that we can trade, what are the different objective functions and what should investors do given those different objective functions?
  indicator: objective functions · asset: multi · testable: no - framing · confidence: high
  ^MT083-C08-3
- **Katie Kaminski** The crisis-alpha portfolio and cash-efficient portfolio are similar, so risk mitigators also get cash efficiency.  #mech/risk_management
  > for those investors out there looking at risk mitigation, they're actually sort of close to their cash optimal portfolio as well.
  indicator: portfolio overlap · asset: multi · testable: yes · confidence: medium
  ^MT083-C08-4

### C09
- **Katie Kaminski** Trend gives exposure to macro themes without needing a forecast of which theme or when.  #mech/slow_reaction
  > with trend, you actually are following a lot of the big macro themes and capturing them with a process that's diligent and sort of systematic as opposed to trying to predict which macro theme is going to occur and when.
  indicator: trend · asset: multi · testable: partly · confidence: high
  ^MT083-C09-1
- **Katie Kaminski** Crisis alpha needs a strategy to be unbiased, liquid and adaptable.  #mech/risk_management
  > it's a few key things. One, being unbiased. You know, two, being liquid. Three, being adaptable.
  asset: multi · horizon: days · testable: partly · confidence: medium
  ^MT083-C09-2
- **Katie Kaminski** In a crisis the liquid markets move with macro themes, so liquid traditional markets provide the offsetting returns for a crisis allocation.  #mech/liquidity_flows
  > it's the things that are liquid that move with the macro themes that have the potential to find opportunities if you can adapt with them quickly enough in markets that are tradeable enough
  indicator: liquid futures in crises · asset: multi · horizon: days · conditions: In crises · testable: partly · confidence: medium
  ^MT083-C09-3

### C10
- **Harry Moore** Alpha evaporation in active equities shifted investors to passive, so portable alpha splits the decision: own the index via swap or future and separately find a repeatable alpha.  #mech/structural_shift
  > the kind of evaporation of alpha in active equities.
  asset: equities · horizon: years · testable: partly · confidence: medium
  ^MT083-C10-1
- **Harry Moore** Portable alpha replicates the index with swaps or futures and layers a separate alpha on top.  #mech/research_method
  > I'm going to decouple my investment choice. So, the index is hard to beat. Well, why don't I just go and replicate the index?
  asset: equities · horizon: years · testable: yes · confidence: high
  ^MT083-C10-2
- **Harry Moore** Trend uses little cash ($25 to $30 per $100 of exposure), leaving cash to hold the beta index.  #mech/risk_management
  > I don't need $100 to get $100 of trend exposure. I might only need $25 or $30.
  indicator: margin usage · asset: multi · testable: yes · confidence: high
  ^MT083-C10-3
- **Harry Moore** Historically, trend on top of beta outperformed with more consistency than a multi-strategy alpha.  #mech/research_method
  > you are able to to outperform with more consistency.
  indicator: trend overlay on equity index · asset: equities · horizon: years · testable: yes - paper backtest · confidence: medium
  ^MT083-C10-4

### C11
- **Katie Kaminski** Trend as portable alpha had better drawdown characteristics than equity-focused or hedge fund alpha.  #mech/risk_management
  > adding trend with um as sort of your portable alpha strategy did have the better drawdown characteristic compared to say more equity focused or hedge funds
  indicator: drawdown of overlay strategies · asset: equities · horizon: years · testable: yes · confidence: medium
  ^MT083-C11-1
- **Katie Kaminski** Alpha and beta are never fully separated; in March 2026 equities and trend were in drawdown at the same time, as in return-stacked ETFs.  #mech/crowding_positioning _(time-bound view)_
  > alpha and beta are never 100% separated.
  indicator: correlation of alpha and beta in drawdowns · asset: equities · horizon: months · conditions: March 2026 · testable: yes · confidence: medium
  ^MT083-C11-2
- **Harry Moore** Coincident alpha and beta drawdowns (COVID, GFC) could hurt portable alpha, so structures need due diligence.  #mech/risk_management
  > those risks from 2008 that caused so many issues, they haven't gone away.
  asset: multi · testable: partly · confidence: medium
  ^MT083-C11-3
- **Niels Kaastrup-Larsen** Some trend styles (liquid markets, certain speeds) may suit portable alpha better; untested.  #mech/research_method
  > I imagine that there are certain kinds of trend following that probably are better suited for this uh particular uh thing.
  asset: multi · testable: yes - future test · confidence: low
  ^MT083-C11-4

### C12
- **Harry Moore** With 10% margin on S&P futures, an 8 to 10% fall exhausts margin, so keep large cash buffers (e.g. $40 per $100 rather than $10) instead of investing the rest.  #mech/risk_management
  > if the S&P draws down 8, 9, especially if it draws down 10, right? All of your margin is going to be exhausted.
  indicator: futures margin buffer · asset: equities · testable: yes · confidence: high
  ^MT083-C12-1
- **Harry Moore** An illiquid alpha cannot meet margin calls, forcing closure of the beta, so use liquid alpha such as trend.  #mech/risk_management
  > if your alpha isn't liquid, you're not going to be able to source that from your alpha and you'll get closed out of your of your beta.
  indicator: alpha liquidity · asset: multi · horizon: days · testable: yes · confidence: high
  ^MT083-C12-2
- **Harry Moore** Trend manages to risk, so in a crisis its exposure and margin fall, reducing funding needs.  #mech/risk_management
  > our margin requirements actually go down in the crisis.
  indicator: trend margin usage in stress · asset: multi · horizon: days · conditions: In volatility spikes · testable: yes · confidence: high
  ^MT083-C12-3

### C13
- **Niels Kaastrup-Larsen** By June 2025, after five months of drawdown, SocGen Trend neared its historical maximum drawdown (about 22%) amid the tariff reversals and headlines that trend was too slow for social-media-driven news; a strong recovery followed.  #mech/cycle_persistence _(time-bound view)_
  > the industry were in the fifth consecutive months of drawdowns.
  indicator: SocGen Trend Index drawdown · asset: multi · horizon: months · conditions: Mid-2025 · testable: yes - index · confidence: high
  ^MT083-C13-1
- **Harry Moore** If an asset's drawdown does not change your belief it no longer works, rebalance into it rather than dropping it.  #mech/behavioral
  > then what you should actually do is rebalance in that time.
  asset: multi · testable: partly · confidence: high
  ^MT083-C13-2
- **Niels Kaastrup-Larsen** The narrative that trend is too slow for social-media news was refuted by later recovery.  #mech/slow_reaction _(time-bound view)_
  > trend following for sure would be too slow to deal with a world where political news were communicated through social media
  asset: multi · testable: partly · confidence: medium
  ^MT083-C13-3

### C14
- **Harry Moore** Simulation: a 0.6 Sharpe strategy at 15% vol (vs equities about 0.4 Sharpe) still had a 33% drawdown lasting years, so a long drawdown does not show a broken strategy.  #mech/research_method
  > Now, that strategy spent years in drawdown. It had a drawdown of 33%.
  indicator: simulated drawdown of 0.6 Sharpe strategy · asset: multi · horizon: years · testable: yes - simulation · confidence: high
  ^MT083-C14-1
- **Harry Moore** Rules that deallocate from strategies in drawdown underperform holding.  #mech/behavioral
  > what about if you set drawdown rules such that you deallocate from strategies um when they have drawdowns, and and again you find um that underperforms.
  indicator: drawdown-based deallocation · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT083-C14-2
- **Harry Moore** Human behavioural biases explain why trend works over the long run.  #mech/behavioral
  > There's a lot of well-documented biases from humans psychology that explain um why trend following works over the long run.
  asset: multi · horizon: years · testable: partly · confidence: high
  ^MT083-C14-3
- **Katie Kaminski** A sudden shock such as Liberation Day is hard for trend because there is no trend yet, only confusion about the macro meaning.  #mech/overshoot
  > that type of shock is very difficult for trend because there's no actual trend yet.
  asset: multi · horizon: days · conditions: Right after a shock · testable: partly · confidence: medium
  ^MT083-C14-4

### C15
- **Katie Kaminski** Realisation of macro change takes time (tariffs to prices), and trends return afterwards.  #mech/slow_reaction
  > of macro change takes time. It takes time for tariffs to affect prices.
  asset: multi · direction: trend profits after shock · horizon: months · testable: partly · confidence: medium
  ^MT083-C15-1
- **Katie Kaminski** Trend drawdowns are cyclical and self-correcting, as in the 2013 CTA winter and the second-largest drawdown since 2000.  #mech/cycle_persistence
  > over time the strategy is sort of self-correcting, just like most strategies
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT083-C15-2
- **Niels Kaastrup-Larsen** Change hurts convergent strategies while divergent strategies such as trend are designed for it.  #mech/structural_shift
  > Change will hit all strategies that have a conversion profile because they don't like change.
  asset: multi · testable: partly · confidence: medium
  ^MT083-C15-3
- **Niels Kaastrup-Larsen** The probability of a two-standard-deviation drawdown is about 21% after five years but almost 80% over 25 years for a 0.5 Sharpe, 10% vol strategy, so a short clean record is weak evidence.  #mech/research_method
  > But if you've been around for 25 years, like some of us have, that number goes to almost 80%.
  indicator: probability of 2 SD drawdown · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT083-C15-4

### C16
- **Niels Kaastrup-Larsen** CTA AUM fell from almost 30% of hedge fund AUM to 5% and to about 2% of futures volume, so crowding is not a credible reason for trend to fail.  #mech/crowding_positioning
  > dropping from somewhere almost 30% back in the late '90s to now it's just 5% of the total hedge fund universe
  indicator: CTA AUM share of hedge funds and futures volume · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT083-C16-1
- **Niels Kaastrup-Larsen** Trends form because human behaviour does not change; the world changing does not break trend.  #mech/behavioral
  > I think the real question is did people change?
  asset: multi · horizon: years · testable: no · confidence: medium
  ^MT083-C16-2
- **Katie Kaminski** Remove equity and trend exposures from macro managers' returns to measure idiosyncratic alpha.  #mech/research_method
  > we kind of showed mathematically how you can tease out sort of take out the equity and trend exposure and understand the idiosyncratic alpha that you have in a particular manager.
  indicator: macro manager alpha vs equity and trend · asset: multi · testable: yes · confidence: high
  ^MT083-C16-3

### C17
- **Harry Moore** Across macro managers, higher fees are only very weakly related to higher net returns.  #mech/research_method
  > Now, there's a very very weak positive correlation between higher fee and higher net of returns from the paper, but it's very weak.
  indicator: fee vs net return · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT083-C17-1
- **Harry Moore** Survivorship bias makes current manager indices look better; analysis should account for it.  #mech/research_method
  > Uh but the 10 that did badly don't exist anymore. So my data set is very biased towards the the better performers.
  indicator: survivorship bias · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT083-C17-2
- **Harry Moore** Decompose macro managers against equities and trend (and bonds) and judge the alpha above cheap trend and equity exposure.  #mech/research_method
  > if I can go and access trend via a low cost route and I can access equities through a low cost route. Like what is the actual alpha on top of that.
  asset: multi · horizon: years · testable: yes · confidence: high
  ^MT083-C17-3

### C18
- **Katie Kaminski** Oil shocks weaken the consumer and create inflation shocks, so geopolitical risk transmits to managed futures through energy.  #mech/structural_shift _(time-bound view)_
  > oil shocks cause a weak in consumer, they also cause inflation shocks.
  indicator: oil price shocks · asset: commodities · horizon: months · testable: partly · confidence: medium
  ^MT083-C18-1
- **Harry Moore** If the inflation theme continues, trend will be long oil and short bonds.  #mech/slow_reaction _(time-bound view)_
  > if we continue to see the inflation theme, I think we'll see yeah, a bit more bit more oil in there. We'll see short bonds.
  indicator: inflation theme · asset: multi · direction: long oil, short bonds · horizon: months · conditions: If inflation persists · testable: partly · confidence: medium
  ^MT083-C18-2
- **Niels Kaastrup-Larsen** Allocations to trend and non-correlated strategies are too small for the risks in 2026 (recovery or deeper crisis).  #mech/structural_shift _(time-bound view)_
  > I'm not so sure that there is enough people who are well prepared for whatever comes because I still think that the allocation to our space is way too small
  asset: multi · testable: no · confidence: medium
  ^MT083-C18-3
- **Harry Moore** Portable alpha research has covered what it is and how to build it, but sizing of cash buffers and structuring around tail co-dependence between the alpha and the beta remain under-researched and are the key open design questions.  #mech/research_method _(added by opus cross-check)_
  > I think less literature so far on things like the cash buffer question, tail code dependent structuring.
  indicator: tail dependence between overlay alpha and equity beta; cash buffer size · asset: multi · conditions: portable alpha / return-stacked structures · testable: yes - simulate buffers and tail co-drawdowns historically · confidence: medium
  ^MT083-C18-X1

