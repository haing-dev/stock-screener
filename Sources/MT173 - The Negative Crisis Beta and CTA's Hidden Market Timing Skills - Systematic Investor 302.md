---
source_id: MT173
title: "The Negative Crisis Beta and CTA's Hidden Market Timing Skills - Systematic Investor 302"
date: 2024-07-03
channel: "Top Traders Unplugged"
url: 
words: 12253
claims: 58
added_by_crosscheck: 20
corrections: 3
crosscheck: "sonnet-xhigh cross-check"
speakers: ["Nick Baltas (systematic macro quant researcher)", "Alan Dunne (host, sitting in for Niels Kaastrup-Larsen)"]
tags: [source, layer0]
---
# The Negative Crisis Beta and CTA's Hidden Market Timing Skills - Systematic Investor 302

**Speakers:** Nick Baltas (systematic macro quant researcher); Alan Dunne (host, sitting in for Niels Kaastrup-Larsen)

**Summary:** Top Traders Unplugged Systematic Investor 302 (June 2024): Baltas and Dunne cover trend performance, universe size and speed, volatility targeting, the Quantica paper on negative crisis beta (capping equities helps in downturns but costs more long-run), and the Resolve guide to futures carry.

**Approach:** trend following, carry, mean reversion, CTA research

**Cross-check completeness estimate of first read:** 0.78 - first reader caught the main arguments of both papers (Quantica crisis beta/alpha numbers, Resolve carry definitions, correlations, universe and complementarity) accurately; missed methodological detail and supporting points: quarter-bucketing method, regression caveat, short-only motivation, upside cost, what to do with freed risk when capping, beta neutralisation mechanics (AHL linear beta, equity beta in other markets), June 2024 attribution and vol-scaling, drawdown rule of thumb, horizon dependence of timing, and several carry design details

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 2 | intro, MXN carry loss, low vix, cheap options |
| C02 | 3 | trend index performance June 2024, reversion complement, skewness |
| C03 | 3 | questions: reversion cross-section, number of markets, market selection |
| C04 | 2 | number of markets, macro vs alternative markets |
| C05 | 2 | trend speed vs beta portfolio, equity cap |
| C06 | 2 | vol target question, risk aversion, liabilities |
| C07 | 2 | vol rules of thumb, leveraged ETF drawdown, intro to Quantica paper |
| C08 | 4 | Quantica paper motivation and equity contribution 2024 |
| C09 | 2 | worst quarters regression, three constrained variants |
| C10 | 2 | results of constraints, cost vs benefit numbers |
| C11 | 1 | implementation caveats, beta constraints |
| C12 | 1 | asymmetry of loss aversion |
| C13 | 2 | market timing and volatility clustering, momentum vs trend |
| C14 | 2 | crisis beta/alpha message, Resolve carry paper intro |
| C15 | 3 | carry definitions and z-score |
| C16 | 2 | portfolio construction, bond carry beta, universe |
| C17 | 2 | beta constraints and trend/carry complementarity |
| C18 | 1 | wrap-up, commodity carry skew |

## Claims

### C01
- **Nick Baltas** In June 2024 the carry space suffered a temporary loss driven by an unexpected Mexican peso move after elections, with part later recovered; an example of event risk hitting carry.  #mech/crowding_positioning _(time-bound view)_
  > the interesting move we saw recently was this um maybe temporary um loss in the carry space uh you know primarily driven by the Mexican peso unexpected move following those elections
  indicator: FX carry (MXN) · asset: fx · direction: carry loss · horizon: weeks · conditions: Election surprise · testable: partly - episode study · confidence: medium
  ^MT173-C01-1
- **Nick Baltas** With VIX near historical lows and rate vol moderating, options are cheap so adding hedges is attractive even though the environment is not anti-CTA.  #mech/risk_management _(time-bound view)_
  > optionality seems to be cheap at the moment
  indicator: implied vol / VIX level · asset: multi · direction: buy cheap optionality · horizon: weeks · conditions: Low vix and low rate vol · testable: partly - option cheapness vs realized vol testable · confidence: medium
  ^MT173-C01-2
- **Nick Baltas** Backdrop for first half 2024: a strong equity trend (mega caps +24% since April, Nasdaq +18% YTD, S&P +35% since October) with VIX near historic lows and interest-rate vol moderating, a benign environment for trend programs that carry equity exposure.  #mech/cycle_persistence _(added by sonnet-xhigh cross-check, time-bound view)_
  > since April for example Mega caps have been up for like 24% NASDAQ is going to be 18% for the full year and S&P is like 35% since October
  indicator: S&P 500, Nasdaq, mega-cap returns; VIX; rate volatility (June 2024) · asset: equities · direction: equities up, volatility low · horizon: months · conditions: As of the end of June 2024; a short-term sell-off had just occurred · testable: yes - index returns and VIX are public · confidence: high
  ^MT173-C01-X1

### C02
- **Alan Dunne** CTA indices turned choppy in late May-June 2024 (Trend index -2.84% in June, +8.5% YTD; CTA index -2.2%, +7.09% YTD) with reversals in fixed income, grains and metals after a strong start.  #mech/slow_reaction _(time-bound view)_
  > sub 10 Trend down 2.84% on the month uh up 88.5% year to date and sub CJ index extend 2.2% on the month still up a very good seven.09 on the year
  indicator: SG Trend Index; SG CTA Index · asset: multi · horizon: months · conditions: June 2024 · testable: yes - public indices · confidence: high
  ^MT173-C02-1
- **Nick Baltas** A mean-reversion component complemented trend in a month of reversals (reversion strategies up about 1-1.5% month-to-date, mainly in commodities), showing complementarity when trend underperforms.  #mech/slow_reaction _(time-bound view)_
  > obviously for those months that we see those reversals is it worth having reversion components in the strategy
  indicator: mean-reversion strategy returns vs trend returns · asset: multi · direction: add mean reversion alongside trend · horizon: weeks · conditions: Months with reversals across markets · testable: yes - blended strategy backtest · confidence: medium
  ^MT173-C02-2
- **Nick Baltas** Reversion signals use skewness: a trend accompanied by exaggerated, positively skewed up-moves flags a sell from the reversion standpoint, so the signal is an exacerbated trend rather than any positive trend.  #mech/overshoot
  > to the extent that this positive trend materializes as a high positive skewness then that Flags a cell signal from a reversion standpoint
  indicator: return skewness over a window · asset: multi · direction: short after high positive skewness · horizon: weeks · conditions: Applies where trend comes with extreme up moves · testable: yes - skewness-based reversion signal is testable · confidence: medium
  ^MT173-C02-3
- **Nick Baltas** Performance attribution for June 2024: market reversals across fixed income and other markets explained more than half of the month's trend underperformance, with commodities (grains, cocoa) the remaining part.  #mech/slow_reaction _(added by sonnet-xhigh cross-check, time-bound view)_
  > reversion that we've seen during the month has obviously um I think contributed maybe more than half of the under performance month today
  indicator: trend program month-to-date attribution by sector · asset: multi · direction: trend losses from reversals · horizon: weeks · conditions: Choppy second half of May and June 2024 after a strong start to the year · testable: yes - sector attribution of trend indices · confidence: medium
  ^MT173-C02-X1
- **Nick Baltas** Volatility targeting limits whipsaw losses: as cocoa volatility rose, trend programs had already cut its exposure, so after another big move it was only about the fifth-worst commodity contributor, costing roughly 20-30bp in a 15%-vol program.  #mech/risk_management _(added by sonnet-xhigh cross-check, time-bound view)_
  > the overall exposure to it has been moderated since earlier in the year
  indicator: cocoa position size; contribution to a 15% vol trend program (20-30bp) · asset: commodities · direction: exposure reduced as vol rises · horizon: weeks · conditions: Works when vol rises before the reversal; does not protect against gap moves · testable: yes - position sizing versus realised vol can be verified · confidence: medium
  ^MT173-C02-X2

### C03
- **Nick Baltas** Reversion built as a cross-sectional strategy and trend as time-series tap different principal components, adding diversification beyond the signal difference.  #mech/research_method
  > reversion as a crosssectional dynamic whereas we think about Trend as a Time series Dynamic so there's an additional complimentarity
  indicator: cross-sectional reversion vs time-series trend · asset: multi · horizon: weeks · testable: yes · confidence: medium
  ^MT173-C03-1
- **Nick Baltas** Adding markets to a trend program has diminishing diversification benefit (about square-root-of-N) while newer, niche markets cost more to trade.  #mech/risk_management
  > the more markets we have the more diversification we achieve but the marginal diversification benefit drops this kind of thing square root over n
  indicator: number of markets in trend program · asset: multi · testable: yes - breadth vs Sharpe/cost testable · confidence: high
  ^MT173-C03-2
- **Nick Baltas** Select markets for diversification and cost, not for past performance contribution, as that is data mining (cocoa was the worst contributor until it was not).  #mech/research_method
  > we would not want to choose markets on the basis of contributing performance or not contributing performance
  indicator: market-level performance attribution · asset: multi · testable: yes · confidence: high
  ^MT173-C03-3

### C04
- **Nick Baltas** Backtests of 40, 50, 100 or 150 markets look similar if vol target is held constant, as removing markets means grossing up the rest; a sensible universe is about 50-100 markets, with 10 markets more cautious.  #mech/risk_management
  > there is no right number at least to me uh and we do get I mean to your point we do get questions oh should I do it with like no 40 markets
  indicator: number of markets · asset: multi · conditions: Holding the target volatility constant · testable: yes - universe-size study · confidence: medium
  ^MT173-C04-1
- **Nick Baltas** Alternative commodity markets driven by producers and consumers have low cross-dependence and add more diversification than traditional speculative markets; macro markets however provide crisis alpha.  #mech/structural_shift
  > the less correlated the univers is the more diversification and benefits you get from the additional market
  indicator: market correlation structure · asset: commodities · direction: add less-correlated markets · testable: yes · confidence: medium
  ^MT173-C04-2
- **Nick Baltas** Trend return has two layers: capturing the common principal-component moves (net long equities, net long commodities, net short bonds at a given time) plus a fine adjustment from cross-sectional differences between markets; the diversification of a broad universe pays most at turning points.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > it gets performance from capturing principal component moves and net long equities I'm net long Commodities I'm net short bonds whatever that might be
  indicator: trend portfolio net exposures by asset class; cross-sectional spread of signals · asset: multi · horizon: months · conditions: Single-market or index-only implementations simplify but lose turning-point diversification · testable: yes - decompose trend returns into common component and cross-sectional residual · confidence: high
  ^MT173-C04-X1

### C05
- **Nick Baltas** Faster trend speeds reduce correlation to a 60/40 beta portfolio because they can flip with turning points; slow speeds look like net long the market. A reasonable range is about 3 to 12 months balancing reactivity, false positives and cost.  #mech/slow_reaction
  > the speed here all else being equal is going to reduce correlation to the beta portfolio
  indicator: trend lookback speed vs correlation to 60/40 · asset: multi · direction: faster speed for diversification · horizon: months · conditions: Excess turnover and false positives offset benefit at very fast speeds · testable: yes - speed vs correlation study · confidence: medium
  ^MT173-C05-1
- **Nick Baltas** Capping equity exposure on the upside decorrelates from the beta portfolio and may preserve capital in downturns, though not necessarily maximising returns (a gut feeling).  #mech/risk_management
  > some form of moderate Equity exposure on the upside will help with preservation of capital in a downt
  indicator: equity exposure cap in trend programs · asset: equities · direction: cap long equities · horizon: months · testable: yes · confidence: low
  **Correction (cross-check):** Baltas says moderate equity exposure on the upside may preserve capital in a downturn and so may not maximise the average (arithmetic) return, but he adds 'I think that geometric it would', i.e. it may improve the compounded return; the first reader drops the geometric point. → Capping equity exposure on the upside decorrelates from the beta portfolio; Baltas has a gut feeling that it preserves capital in downturns and may not maximise the average return but could maximise the geometric (compounded) return.
  ^MT173-C05-2

### C06
- **Nick Baltas** Liability-driven investors need a nominal return target so their volatility is implied by the required Sharpe ratio; target-date funds cut equity as retirement nears; mandates run at 5-15% vol.  #mech/risk_management
  > I would also say that sometimes when it comes to to to Investments and effectively when it comes to managing liabilities
  indicator: portfolio volatility target · asset: multi · horizon: years · conditions: Depends on risk aversion and liabilities · testable: no · confidence: medium
  ^MT173-C06-1
- **Nick Baltas** A 5% vol trend allocation alongside a 60/40 does little; leverage can scale it but then financing and leverage constraints dominate the choice.  #mech/risk_management
  > I don't think that a 5% Vol will move the needle
  indicator: trend program volatility level · asset: multi · testable: partly · confidence: medium
  ^MT173-C06-2
- **Nick Baltas** There is no universal safe volatility level: on the Markowitz frontier the right risk is set by the investor's risk aversion and, for asset owners, by the nominal return target they must meet, so Baltas declines to give a risk-of-ruin threshold.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > there is a frontier whereby you get rewarded in the maximal way for the level of risk you're happy to take and there's this concept of risk aversion
  indicator: target volatility versus required return · asset: multi · conditions: Depends on liabilities, horizon and tolerance for deep drawdowns · testable: no - depends on investor preferences · confidence: high
  ^MT173-C06-X1

### C07
- **Nick Baltas** A 10-15% vol is suitable for trend in isolation, and about 20% alongside a strategic allocation matches equity vol; a lot of trend programs run higher than 15%.  #mech/risk_management
  > the 20 alongside the SAA is pretty much matching the the Vol of equities
  indicator: volatility target · asset: multi · horizon: years · testable: partly · confidence: medium
  ^MT173-C07-1
- **Alan Dunne** A 2x leveraged equity ETF would have been wiped out in the 1929-32 crash, so leverage beyond matching equity vol is too aggressive.  #mech/risk_management
  > the equities fell 89% in in after the crash I think 1929 1930 so that would suggest that that that is too much
  indicator: leveraged equity drawdown · asset: equities · horizon: years · testable: yes · confidence: medium
  **Correction (cross-check):** Dunne raises the 1929-32 fall (about 89%) as showing a 2x leveraged equity ETF could be wiped out, but the conclusion that matching equity vol (about 15%) is as aggressive as one would go is Baltas's own view, explicitly labelled as reflecting his level of risk aversion and subjective, not Dunne's. → Dunne notes equities fell about 89% in 1929-32 so a 2x leveraged equity ETF would be wiped out; Baltas replies that for an overall portfolio, matching equity volatility (about 15%) is probably as aggressive as he would go, a subjective view reflecting his risk aversion.
  ^MT173-C07-2
- **Alan Dunne** Rule of thumb that expected drawdown is about twice the volatility (a 10%-vol program should expect around a 20% drawdown); Baltas says trend returns are not IID and are positively skewed over the medium term so the rule is only approximate, and he checks whether historical drawdowns stay below roughly twice vol while disliking drawdown as a measure.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > if you're running a 10 Vol program you should expect a 20% draw down over time
  indicator: maximum drawdown divided by volatility · asset: multi · horizon: years · conditions: Assumes roughly IID returns; trend deviates from that · testable: yes - drawdown-to-vol ratios from trend indices · confidence: medium
  ^MT173-C07-X1

### C08
- **Nick Baltas** In 2024 equities were the best contributor to trend programs and the dispersion between equity-constrained and unconstrained programs was the widest in years; without equities trend would be about flat.  #mech/slow_reaction _(time-bound view)_
  > year to date if I look into at least some of the TR following TRS we have um you equities is by far the best contributor
  indicator: equity contribution to trend returns · asset: equities · horizon: months · conditions: 2024 YTD · testable: yes · confidence: high
  ^MT173-C08-1
- **Nick Baltas** The rolling beta of SG Trend index to equities is about 0.4, near its highest in a while.  #mech/crowding_positioning _(time-bound view)_
  > the rolling beta of a trend following strategy in this particular case the stockchain trend index um is now at around point4
  indicator: rolling beta of SG Trend Index to S&P 500 · asset: equities · horizon: months · conditions: June 2024 · testable: yes · confidence: high
  ^MT173-C08-2
- **Nick Baltas** Quantica finds capping equity exposure helps in downturns but costs more in long-run upside, so run trend unconstrained.  #mech/research_method
  > their conclusion is yes capping the equity exposure can help you in a downturn but over the longer term the price to pay from this reduced participation on the upside is significantly higher
  indicator: capped vs unconstrained equity exposure in trend · asset: equities · direction: run unconstrained · horizon: years · testable: yes · confidence: medium
  ^MT173-C08-3
- **Nick Baltas** Trend following can earn good returns in rising markets by capturing equities, contrary to the idea that it pays only in bad times.  #mech/slow_reaction _(time-bound view)_
  > this concept of like Trend following only doing badly if things go south seems that this here is is is is an example that this is not actually the case
  indicator: trend returns in bull markets · asset: equities · horizon: months · testable: yes · confidence: medium
  ^MT173-C08-4

### C09
- **Nick Baltas** In the worst 16 quarters for the S&P since 2000, CTAs were positive in 12 and their equity beta was negative, with positive alpha from bonds, commodities and other classes: crisis beta plus crisis alpha.  #mech/risk_premium
  > 12 out of 16 CTS have had good performance as in positive performance which is primarily driven by this Alpha Factor
  indicator: CTA returns in worst S&P quarters · asset: multi · direction: long trend in equity downturns · horizon: months · conditions: Down quarters (below -1 sigma) · testable: yes - regression done in paper · confidence: high
  ^MT173-C09-1
- **Nick Baltas** Quantica tested three equity-constrained variants: no equities, equities short-only, and short S&P futures hedging ex-ante beta to zero.  #mech/research_method
  > number one take equities out if there is truly some Alpha from the rest you don't need equities at all
  indicator: equity constraint variants · asset: equities · horizon: months · testable: yes · confidence: high
  ^MT173-C09-2
- **Nick Baltas** Quantica's method splits the roughly 97 quarters since 2000 into the worst 16% (below minus one sigma), the best 16% (above plus one sigma) and the normal middle, then compares equity and trend returns in each regime.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > in more than one Sigma quarters the best quarters as in the above one Sigma and everything in in the middle
  indicator: quarterly S&P 500 returns split into sigma buckets (about 16 bad, 16 good quarters) · asset: equities · horizon: months · conditions: Conditioning on realised equity quarters is ex-post · testable: yes - replicable from index data · confidence: high
  ^MT173-C09-X1
- **Nick Baltas** Caveat on the crisis beta/alpha split: a quarterly regression assumes beta stays constant within the quarter, which is not true for a trend program that changes positions, so the split is descriptive rather than a precise attribution.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > running a regression at the end of a quarter assuming everything is static throughout the quarter is an assumption that things are staying kind of constant
  indicator: quarterly regression of trend returns on S&P 500 · asset: multi · horizon: months · conditions: Positions and betas vary within the quarter · testable: yes - rerun with daily or monthly rolling betas · confidence: high
  ^MT173-C09-X2
- **Nick Baltas** The short-only equity variant is motivated by not wanting to be long equities when a vol shock hits (the end of 2017 into the February 2018 VIX event), because the program would be long into the reversal before it can turn short.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > I don't want to be equities long at the end of 2018 sorry end of 2017 because vix is going to crash the markets and I'll be long markets
  indicator: long equity exposure of trend programs before the 2018 volatility shock · asset: equities · direction: avoid long equities into reversal · horizon: weeks · conditions: Costs upside in sustained rallies · testable: yes - compare short-only equity variant across episodes · confidence: medium
  ^MT173-C09-X3

### C10
- **Nick Baltas** In the worst 16 quarters, unconstrained trend averaged +4.1% versus S&P -9.5%; no equities gave 3.7% and capped equities gave 4.5-4.6%, but long-run returns fell from 5.9% to about 4%, so a roughly 50bp downside gain costs about 200bp long term.  #mech/risk_premium
  > the average quarter out of those worst 16 quarters was negative 99.5% for S&P versus an unconstrained trend of 4.1 having no equities reduces that to 3.7
  indicator: equity-capped trend variants · asset: equities · direction: unconstrained trend preferred · horizon: years · conditions: 24-year sample 2000-2024 · testable: yes · confidence: high
  ^MT173-C10-1
- **Nick Baltas** Neutralising beta with short S&P futures dilutes the trend profile since it shorts rising markets.  #mech/research_method
  > going short equities when the market is going maybe up and has a positive beta might dilute the trend profile because you no longer follow Trends here
  indicator: beta-neutral trend variant · asset: equities · horizon: months · testable: yes · confidence: medium
  ^MT173-C10-2
- **Nick Baltas** The cost of equity constraints shows up in bull regimes: in the best quarters the constrained variants give up roughly 100-140bp (the numbers are garbled in the captions), which is the mirror of the small downside benefit and part of why the long-run return falls.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > so you lose the participation on the upside because you're short equities or you're not allowed to go long equities
  indicator: trend return in best 16% of equity quarters, constrained versus unconstrained · asset: equities · direction: constrained variants lag in rising markets · horizon: months · conditions: Reading of captioned numbers is uncertain · testable: yes - from Quantica's paper tables · confidence: low
  ^MT173-C10-X1

### C11
- **Nick Baltas** Constraining portfolio beta can flip longs to shorts or increase negatively correlated bond longs, thus increasing exposure to a joint equity and bond selloff (inflation spike).  #mech/research_method
  > you might end up some end up having some position switching that dilutes quite substantially the trend nature of the program
  indicator: portfolio equity beta constraint · asset: multi · horizon: months · conditions: When stock-bond correlation turns positive · testable: yes · confidence: medium
  ^MT173-C11-1
- **Nick Baltas** Capping equity exposure forces a design decision the paper does not address: either redeploy the freed risk elsewhere (which can add concentration) or accept lower volatility; Dunne notes the capped variants might have been levered up to compensate, so part of their lower long-run return is simply lower risk.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > if you don't deploy Equity exposure on the upside what do you do with that risk do you still earn you know a particular V level
  indicator: realised volatility of constrained versus unconstrained trend variants · asset: multi · horizon: years · conditions: Comparison is only fair at equal volatility · testable: yes - rescale variants to equal vol and compare · confidence: medium
  ^MT173-C11-X1
- **Alan Dunne** Neutralising equity beta with S&P futures alone ignores the equity beta carried by non-equity positions (commodities, bonds and others), so the way beta is neutralised changes the results; Baltas agrees.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > you could have neutralized Equity beta in a different ways because obviously you're picking up Equity beta in other markets not just Equity
  indicator: portfolio beta to equities including non-equity markets · asset: multi · conditions: Betas are unstable and noisy for individual markets · testable: yes - compare futures-hedge versus full portfolio-beta neutralisation · confidence: medium
  ^MT173-C11-X2
- **Nick Baltas** A way to cap equity beta properly: estimate each market's beta to equities, note that portfolio beta is the position-weighted sum, and optimise the portfolio so that sum is capped at zero or another level; an AHL working paper (about 2016-17) did this, though the published version dropped the analysis.  #mech/risk_management _(added by sonnet-xhigh cross-check)_
  > because beta calculation and portfolio is a linear combination of the single betas the weighted beta is the portfolio beta
  indicator: per-market equity beta, weighted portfolio beta · asset: multi · direction: cap portfolio equity beta · horizon: months · conditions: Single-market betas are statistically noisy; Baltas recalls the AHL paper from memory · testable: yes - implementable with rolling betas and a constrained optimiser · confidence: medium
  ^MT173-C11-X3

### C12
- **Nick Baltas** Loss aversion justifies paying a long-term premium for downside protection (cap equity exposure) for investors with sensitive monthly P&L, even if the paper shows a high cost.  #mech/behavioral
  > because know investors are very all of us are very asymmetric to gains and losses right we're we're much more sensitive to losing than winning
  indicator: investor utility asymmetry · asset: multi · direction: cap equity exposure for risk-averse investors · conditions: Depends on investor utility horizon · testable: no · confidence: medium
  ^MT173-C12-1
- **Alan Dunne** Origin of the equity-cap debate: in 2017 trend programs were up to roughly 50% long equities on top of investors' existing equity holdings, creating stacked exposure and worry about a reversal, which is why investors ask for equity limits.  #mech/crowding_positioning _(added by sonnet-xhigh cross-check)_
  > equities were trending heavily higher and Trend followers were long and people were concerned you know in some cases you might have seen CG being hundreds 50% long equities
  indicator: net equity exposure of CTA programs relative to investors' core equity allocation · asset: equities · direction: double exposure to equity reversal · horizon: months · conditions: Late-stage equity uptrends when trend is fully long · testable: yes - CTA equity exposure estimates and subsequent drawdowns · confidence: medium
  ^MT173-C12-X1

### C13
- **Nick Baltas** Trend following can work even without return serial correlation if volatility clusters, because high-vol regimes produce big directional moves; positive skewness over 1-6 months is evidence of market-timing ability.  #mech/slow_reaction
  > the serial correlation of returns or even more so the clustering of volatility gives rise to predictability
  indicator: volatility clustering · asset: multi · horizon: months · conditions: Not obvious over very short horizons · testable: yes · confidence: medium
  ^MT173-C13-1
- **Nick Baltas** Goyal and Jegadeesh show time-series momentum is cross-sectional momentum plus time-varying net long investment, whereas a cross-sectional strategy is market-neutral.  #mech/research_method
  > time series tests of return predictability
  indicator: time-series vs cross-sectional momentum · asset: multi · horizon: months · testable: yes · confidence: high
  ^MT173-C13-2
- **Nick Baltas** Market timing only makes sense with a horizon: over one day it is a coin toss (about 50% hit rate), but over one to six months volatility clustering and serial correlation make direction partly predictable, which is the timing skill trend following shows.  #mech/slow_reaction _(added by sonnet-xhigh cross-check)_
  > timing the market in itself without a context of horizon is an incomplete statement
  indicator: hit rate of direction forecasts by horizon · asset: multi · horizon: months · conditions: Predictability appears at medium horizons and not in the very short term · testable: yes - hit rate and skew by horizon · confidence: high
  ^MT173-C13-X1

### C14
- **Alan Dunne** Allocating to CTAs systematically manages net equity exposure, giving crisis beta from timing and crisis alpha from multi-asset diversification.  #mech/risk_management
  > allocating to CJ they have that market timing mechanism so that you know we all we don't know when when's the right time to get out and scale back or equities
  indicator: CTA allocation as equity risk management · asset: multi · horizon: months · testable: partly · confidence: medium
  ^MT173-C14-1
- **Nick Baltas** Carry is the return from holding an asset if the price stays unchanged (yield minus financing); the risk is capital depreciation, which in a no-arbitrage world offsets it, but covered interest parity fails.  #mech/risk_premium
  > the difference between being 2% is your carry that's the return you get over the course of a year with a big if if the price stays at 100
  indicator: carry (yield minus funding) · asset: multi · direction: long high carry, short low carry · horizon: years · testable: yes · confidence: high
  ^MT173-C14-2

### C15
- **Nick Baltas** Carry returns across FX, bonds, equity dividends and commodity convenience yield compensate for risk such as short supply or crash risk.  #mech/risk_premium
  > is a source of return that has historically been associated with risk in this regards
  indicator: carry across asset classes · asset: multi · horizon: years · testable: yes · confidence: medium
  ^MT173-C15-1
- **Nick Baltas** Equity carry from the futures curve is a risk-neutral expectation of dividends, distinct from historical dividend yield which is more like value; commodity carry needs seasonality adjustment.  #mech/research_method
  > the latter is more like value whereas the former is more like the kind of risk neutral expectation of the dividend payment
  indicator: futures-implied dividend yield; curve slope; forward basis · asset: equities · testable: yes · confidence: medium
  ^MT173-C15-2
- **Nick Baltas** A carry z-score standardises today's carry against its own history (1-5 year mean and volatility), making carry relative to normal, like cheap versus its own past in equities.  #mech/research_method
  > they transform this 5% by deducting the average carry over the last let's say one year or three years or five years and divide by The Vault
  indicator: carry z-score · asset: multi · direction: long markets with carry high versus own history · horizon: years · testable: yes · confidence: medium
  ^MT173-C15-3
- **Nick Baltas** Standard carry measures: bonds use the slope of the curve and roll-down, commodities use neighbouring futures contracts (with seasonality considerations), currencies use the forward basis; these definitions are uncontroversial, so the design work is in the signal and portfolio construction.  #mech/risk_premium _(added by sonnet-xhigh cross-check)_
  > we would typically look into neighboring contracts maybe there are seasonality considerations here to be taken into account for currencies is the forward basis
  indicator: bond curve slope / roll-down, commodity front-to-next contract spread, FX forward basis · asset: multi · direction: long high carry, short low carry · horizon: months · conditions: Commodity carry needs seasonality adjustment · testable: yes - computable from futures and forwards · confidence: high
  ^MT173-C15-X1
- **Nick Baltas** Three carry implementations are compared: time-series (long positive carry, short negative), cross-sectional within each asset class (long the top half, short the bottom half, balanced to cut beta and principal-component exposure), and optimiser-based weights instead of inverse-volatility scaling across asset classes.  #mech/risk_premium _(added by sonnet-xhigh cross-check)_
  > they look into cross-sectional definitions which basically says top half bottom half I'm going to go long and short the top carry and I'm going to go short the worst carry but I'm going to be balanced between them
  indicator: carry rank within asset class; time-series sign of carry; optimiser weights · asset: multi · direction: long high carry, short low carry · horizon: months · conditions: Time-series implementations carry beta; cross-sectional ones are more neutral but need a large universe · testable: yes - implementable from futures data · confidence: high
  ^MT173-C15-X2

### C16
- **Nick Baltas** Time-series carry in bonds has a 67% correlation to bond beta because curves are mostly upward sloping; cross-sectional carry is more beta-neutral.  #mech/structural_shift
  > the time series implementation of curine bonds has a 67% correlation to bonds because historically you have upward sloping curves
  indicator: bond carry correlation to bond index · asset: rates · horizon: years · testable: yes · confidence: high
  ^MT173-C16-1
- **Nick Baltas** In the Resolve universe (5 currencies, 6 energies, 3 metals, 3 bonds, 7 equities) cross-sectional carry weakened over five to seven years while time-series carry did better; small universes constrain cross-sectional portfolios.  #mech/cycle_persistence
  > cross-sectional definitions have been losing steam based on those definitions based on those Universe for the last five six 7 years whereas the time series one seemed to favor a bit better
  indicator: cross-sectional vs time-series carry · asset: multi · direction: time-series carry preferred recently · horizon: years · conditions: Small universe · testable: yes · confidence: medium
  ^MT173-C16-2
- **Nick Baltas** The cross-sectional carry portfolio ranks on z-scores, a double comparison: which asset's carry is better than its own history relative to how the other assets' carry compares with their own histories.  #mech/overshoot _(added by sonnet-xhigh cross-check)_
  > which currency is caring today better versus its history when compared to all the others versus the respective history
  indicator: carry z-score ranked across currencies, energies, metals, bonds · asset: multi · direction: long assets whose carry is high versus own history · horizon: months · conditions: Needs enough markets per asset class to rank · testable: yes - compute z-scores with 1-5 year lookbacks · confidence: medium
  ^MT173-C16-X1

### C17
- **Nick Baltas** Optimised carry portfolios constrained to zero beta to equities and Treasuries combine carry and trend with Sharpe near one, although rolling correlations to equities and bonds vary over time.  #mech/risk_management
  > they add some constraints in the optimization that controls the beta to
  indicator: carry portfolio beta to equities and Treasuries · asset: multi · horizon: years · testable: yes · confidence: medium
  **Correction (cross-check):** The 'Sharpe close to one' belongs to the time-series carry portfolios after optimisation, which Baltas describes as having stable performance through time (stated before the beta-constraint discussion), not to the combined carry and trend portfolio; the combination is described only as complementary. → Optimised time-series carry portfolios reduce correlation to the beta markets and show a stable Sharpe ratio close to one, but their rolling correlations to equities and bonds vary over time; constraining beta to equities and Treasuries to zero controls this, and the paper concludes carry is a complementary strategy to trend (for example a 50/50 trend and carry mix on top of the S&P 500).
  ^MT173-C17-1
- **Nick Baltas** Time-series carry gets implicit benefit from trend rather than carry itself (e.g. oil in contango while falling), so carry should be designed to minimise spot contribution when run alongside trend.  #mech/research_method
  > benefiting because something is moving exactly yeah
  indicator: carry roll-down vs spot move contribution · asset: multi · testable: yes · confidence: medium
  ^MT173-C17-2
- **Nick Baltas** Beta-neutralising a time-series carry portfolio imports cross-sectional logic: if all bonds are long because of positive carry and beta to bonds must be zero, the optimiser shorts half of them, so the result is a mix of cross-sectional and time-series carry and can short assets with a positive signal.  #mech/research_method _(added by sonnet-xhigh cross-check)_
  > you want to control your beta to bonds equal to zero what do you do well you start shorting half of them
  indicator: carry portfolio beta to bonds and equities · asset: rates · direction: beta constraint forces shorts in positive-carry assets · horizon: months · conditions: Optimisation does not respect the sign of the signal, even without constraints · testable: yes - compare constrained and unconstrained carry portfolios · confidence: high
  ^MT173-C17-X1

### C18
- **Alan Dunne** FX carry is negatively skewed and blunts trend convexity but commodity carry is not, so commodity carry is a better complement to trend.  #mech/risk_premium
  > there's an assumption that they're all that they all operate like effect carry in terms of being negatively skewed and might enhance the sharp but will blunt the positive con convexity
  indicator: commodity carry skewness · asset: commodities · direction: add commodity carry to trend · horizon: years · testable: yes · confidence: medium
  ^MT173-C18-1
- **Nick Baltas** Trend captures directional (beta) moves while carry can add the return from rolling up and down the curves in a market-neutral way, which is why Baltas favours carry as an addition to trend.  #mech/risk_premium _(added by sonnet-xhigh cross-check)_
  > the trend following in itself captures beta moves K can further enhance that by adding to the extent possible in a neutral fashion
  indicator: roll-up and roll-down return of futures curves · asset: multi · direction: add neutral carry to directional trend · horizon: months · conditions: Implementation should minimise spot contribution so carry is not just a second trend · testable: yes - decompose carry return into roll and spot parts · confidence: high
  ^MT173-C18-X1

