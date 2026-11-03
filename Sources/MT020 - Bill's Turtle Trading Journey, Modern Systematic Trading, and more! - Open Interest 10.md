---
source_id: MT020
title: "Bill's Turtle Trading Journey, Modern Systematic Trading, and more!  - Open Interest 10"
date: 2024-10-26
channel: "Top Traders Unplugged"
url: 
words: 9987
claims: 52
added_by_opus: 6
corrections: 1
crosscheck: "opus cross-check"
speakers: ["Bill Eckhardt (guest, co-creator of the Turtle system, Eckhardt Trading Company)", "Rob Santino (guest, president and COO, Eckhardt Trading Company)", "Moritz Seibert (host, Open Interest series)"]
tags: [source, layer0]
---
# Bill's Turtle Trading Journey, Modern Systematic Trading, and more!  - Open Interest 10

**Speakers:** Bill Eckhardt (guest, co-creator of the Turtle system, Eckhardt Trading Company); Rob Santino (guest, president and COO, Eckhardt Trading Company); Moritz Seibert (host, Open Interest series)

**Summary:** Eckhardt and Santino discuss the Turtle origins and how ETC evolved from published breakout rules: risk control first (utility theory), avoiding overfitting and underfitting, the E-score and Gauntlet testing process. Key views: futures returns are heavy-tailed so use robust statistics and long samples; reject high win-rate strategies; keep position sizes constant, no vol targeting; diversify to ~70 liquid markets; avoid stocks and CTA replication.

**Approach:** trend following, risk control and utility theory, overfitting and robust statistics, diversification, Turtle trading history

**Opus completeness estimate of first read:** 0.90 - first reader caught the core risk-control, fitting and statistics claims; missed several host elaborations (hidden mean reversion, SD vs normality, Mandelbrot evidence, long-term robustness) and Santino's replication call; one speaker error.

## Coverage

| Chunk | Claims | Note |
|---|---|---|
| C01 | 2 | intro; many-to-few principle; Eckhardt's role in Turtles |
| C02 | 2 | Eckhardt-Dennis background, mechanization, theory-building |
| C03 | 2 | ballistics analogy, ETC as research lab, risk aversion and prediction futility |
| C04 | 4 | risk control first, utility theory, risk-loving utilities |
| C05 | 5 | risk aversion; trade horizons; Turtle rule degradation; death of trend following |
| C06 | 4 | Red Queen; volatility use; no vol targeting; constant sizing |
| C07 | 3 | stop-loss optionality; vol mean-reverts; non-trend 20%; summary statistics |
| C08 | 3 | structure vs summary statistics, moving averages, overfitting and underfitting |
| C09 | 4 | underfitting, E-score, Gauntlet |
| C10 | 3 | Gauntlet tests code; alternative markets, diversification, liquidity and slippage |
| C11 | 4 | alternative markets slippage; stocks vs futures; replication; non-normality |
| C12 | 3 | robust statistics and data needs; LTCM; Mandelbrot |
| C13 | 4 | replication and stops; fat left tail; high win-rate systems; prediction vs risk control |
| C14 | 2 | human biases, cut losses, pain arbitrage; Turtle selection |
| C15 | 1 | Turtles drop-outs; outro |

## Claims

### C01
- **Bill Eckhardt** Money flows from the many to the few, so normal human reflexes put you among the many and losing; successful trading feels unpleasant and requires suffering and not following inclinations.  #mech/behavioral
  > the structure of the market is that the money flows from the many to the few so you have to be among the few not among the many
  asset: multi · testable: no - behavioral principle · confidence: high
  ^MT020-C01-1
- **Bill Eckhardt** Trading success needs more than entry rules: risk management and attitudes toward profit and loss; Dennis ran the Turtles' risk control while Eckhardt developed rules.  #mech/risk_management
  > there's more to trading than Simply Having rules you have risk management
  asset: multi · testable: no - qualitative · confidence: medium
  ^MT020-C01-2

### C02
- **Bill Eckhardt** Eckhardt thought mechanizing trading (versus Dennis' 'weighted rules' view) was much harder than it seemed.  #mech/research_method
  > it was much harder to mechanize what is needed for trading
  asset: multi · testable: no - opinion · confidence: medium
  ^MT020-C02-1
- **Bill Eckhardt** His approach was to build a theory of trading from the philosophy of science, formalizing pieces rigorously rather than a complete theory.  #mech/research_method
  > I have formalized certain parts of trading in a mathematically rigorous fashion
  asset: multi · horizon: years · testable: no - method statement · confidence: medium
  ^MT020-C02-2

### C03
- **Bill Eckhardt** Like ballistics, a trading theory starts oversimplified (few factors) and improves as research adds relevant factors.  #mech/research_method
  > because you have to oversimplify a problem sometimes in the beginning
  asset: multi · horizon: years · testable: no - analogy · confidence: medium
  ^MT020-C03-1
- **Bill Eckhardt** Markets are not random but too close to random for simple predictions, so focus should be on risk control, which one can know and control, rather than prediction.  #mech/risk_management
  > we can't be very successful about predicting where the Market's going to go it's too close
  indicator: market predictability · asset: multi · direction: focus on risk control not prediction · testable: partly - low predictability is testable · confidence: high
  ^MT020-C03-2

### C04
- **Bill Eckhardt** Do not predict the market; decide what to do wherever it goes: risk control first, with profitability following from correct risk control.  #mech/risk_management
  > instead you have to focus on risk control because that's something you you can know your risk you can change your risk you can control your risk
  asset: multi · testable: no - principle · confidence: high
  ^MT020-C04-1
- **Bill Eckhardt** Utility theory: marginal utility of money diminishes, so losses weigh more than gains and risk aversion is a rigorous concept; ETC uses a small class of utility functions suited to commodity trading and client circumstances.  #mech/risk_management
  > every dollar every new dollar that you make is a little smaller than the last one and more importantly every dollar that you lose is the little bigger than the last
  indicator: expected utility / risk aversion · asset: multi · testable: partly - utility-based sizing can be tested · confidence: high
  ^MT020-C04-2
- **Bill Eckhardt** Most traders build a profitable system first and graft risk control on afterwards; ETC brings expected utility in at the ground floor of research and judges every idea by its effect on expected utility.  #mech/risk_management
  > they graft risk control almost as an afterthought on their system on their profitability system
  asset: multi · testable: partly - design philosophy · confidence: medium
  ^MT020-C04-3
- **Bill Eckhardt** Risk-neutral and risk-loving utility functions lead to ruin (the St Petersburg paradox shows absurd infinite expected value bets).  #mech/risk_management
  > the risk loving ones to be died these are utility functions for somebody who wants to keep betting the ranch and eventually I think they're financially suicidal
  asset: multi · testable: no - theoretical argument · confidence: high
  ^MT020-C04-4

### C05
- **Bill Eckhardt** In futures trading with leverage, risk aversion is primary since risk-loving traders repeatedly lose all their money.  #mech/risk_management
  > one has to be risk averse that's the only thing that can that can work in this business
  asset: multi · testable: no - principle · confidence: high
  ^MT020-C05-1
- **Bill Eckhardt** ETC runs short, medium and long-term systems with average trade lengths from 4-5 days to 50-60 days.  #mech/slow_reaction
  > we have shortterm we have medium we have long-term systems but you know we have trades that that have a a four or five day average length
  indicator: trade horizon mix · asset: multi · horizon: weeks · testable: no - description · confidence: medium
  ^MT020-C05-2
- **Moritz Seibert** Many Turtle students moved to longer holding periods because of alpha decay in short-term systems.  #mech/slow_reaction
  > they have moved over to longer term hold periods because of the Alpha DK that we could deserve observe in the shorter term systems
  indicator: short-term trend alpha decay · asset: multi · direction: longer holding periods · horizon: years · testable: partly - trend returns by horizon over time · confidence: medium
  ^MT020-C05-3
- **Bill Eckhardt** Turtle rules (breakout systems) were widely published so their edge was degraded by competition; Eckhardt moved to different trend-following systems even before they were released.  #mech/crowding_positioning
  > they've been heavily degraded since we let the turtles go and all all this information got revealed
  indicator: published breakout rules · asset: multi · horizon: years · testable: partly - performance of published rules · confidence: high
  ^MT020-C05-4
- **Bill Eckhardt** Trend following has been declared dead every few years; the majority of ETC's work is still trend following with a small non-trend part.  #mech/cycle_persistence
  > the death of trend following has been highly exaggerated
  indicator: trend following · asset: multi · direction: long trend following · horizon: years · testable: yes - long history of trend returns · confidence: high
  ^MT020-C05-5
- **Moritz Seibert** While short-term trend systems show alpha decay, longer-term trend systems (around 200-day look-backs) still work and remain robust, with drawdowns.  #mech/slow_reaction _(added by Opus)_
  > the longer term systems you know two and a day time frames things like that to the present day they continue to work and they go up and down and they're robust
  indicator: trend look-back length (about 200 days) · asset: multi · direction: favour long look-back trend systems · horizon: months · testable: yes - compare short vs long look-back trend returns over time · confidence: medium
  ^MT020-C05-X1

### C06
- **Bill Eckhardt** Red Queen effect: with more competition and technical analysis knowledge, a commodity trader must improve as fast as possible just to hold his own.  #mech/crowding_positioning
  > one has to keep researching to stay ahead of it
  asset: multi · horizon: years · testable: no - qualitative · confidence: high
  ^MT020-C06-1
- **Rob Santino** Volatility enters ETC's systems in five or six ways (position sizing, measuring price change, risk control) alongside price, so the systems are based on both.  #mech/risk_management
  > volatility enters into our trading system in several different ways and about five or six different ways
  indicator: volatility · asset: multi · testable: no - proprietary · confidence: medium
  ^MT020-C06-2
- **Rob Santino** ETC does not target portfolio volatility because higher volatility often helps trend systems and they do not want to juice up when volatility is low; they track individual futures' volatility for risk.  #mech/risk_management
  > in a lot of situations um increased volatility often helps us we don't want to restrain it
  indicator: portfolio volatility targeting · asset: multi · direction: no vol targeting · testable: yes - compare vol-targeted vs unscaled · confidence: medium
  ^MT020-C06-3
- **Rob Santino** Position sizes are kept roughly constant from entry to exit: readjusting to rising volatility would cut the position along with the trend, which they found counterproductive.  #mech/risk_management
  > since um volatility often increases with a trend we have found that and if we were readjusting to volatility we would
  indicator: post-entry volatility readjustment · asset: multi · horizon: weeks · testable: yes - test dynamic vs constant size · confidence: medium
  ^MT020-C06-4

### C07
- **Moritz Seibert** Constant sizing with a stop-loss gives controlled risk and a synthetic long-optionality (volatility-seeking) profile.  #mech/risk_management
  > which means controlled risk and therefore a sythetic long optionality profile if you will
  indicator: stop-loss · asset: multi · direction: long volatility profile · horizon: weeks · testable: partly · confidence: medium
  ^MT020-C07-1
- **Bill Eckhardt** ETC's non-trend methods (about 20% of work) are not mean reversion because futures prices do not mean revert while volatility does.  #mech/cycle_persistence
  > it's volatility that mean reverts uh price doesn't doesn't mean revert at least Futures prices
  indicator: futures prices vs volatility · asset: multi · testable: yes - autocorrelation tests · confidence: medium
  ^MT020-C07-2
- **Bill Eckhardt** Summary statistics of signals (e.g. a moving average) throw away structure; keeping the 20-day high and low gives more information (position within the range).  #mech/research_method
  > instead of boiling all the structure down into one number you're keeping some of the structure
  indicator: moving average vs high/low channel · asset: multi · horizon: days · testable: yes - signal comparison · confidence: medium
  ^MT020-C07-3
- **Moritz Seibert** Resizing an open trend position to rising volatility amounts to a hidden mean-reversion trade against the trend, because volatility usually rises as the trend extends.  #mech/risk_management _(added by Opus)_
  > essentially executing a hidden Mar reversion trade against the direction of the trend that is not always true by definition but uh it is true in my experience more often than not
  indicator: post-entry volatility resizing · asset: multi · direction: do not cut trend positions as volatility rises · horizon: weeks · conditions: when volatility rises with the trend (usual but not always) · testable: yes - backtest constant vs vol-resized position sizing · confidence: medium
  ^MT020-C07-X1

### C08
- **Bill Eckhardt** Keeping all price-history structure is combinatorially impossible, so research must eliminate structure but keep what is important.  #mech/research_method
  > what you have to do is you have to find out you have to eliminate a lot of the structure but you have to keep enough of it
  asset: multi · testable: no - research problem · confidence: medium
  ^MT020-C08-1
- **Bill Eckhardt** Volatility is a moving-average process, so moving averages suit volatility, but price is non-stationary and not an MA process, so moving averages and crossovers on price are counterproductive.  #mech/research_method
  > it's appropriate to estimate volatility using moving averages
  indicator: moving average on price vs volatility · asset: multi · testable: yes - MA crossover vs breakout · confidence: medium
  ^MT020-C08-2
- **Bill Eckhardt** Fitting should capture permanent features and ignore transitory ones; some overfitting is inevitable, so ETC uses in-house techniques to estimate and minimize overfit.  #mech/research_method
  > to try to fit to the permanent features of the time series whereas you want to ignore the transitory features
  indicator: overfitting estimate · asset: multi · testable: yes - overfit estimators · confidence: high
  ^MT020-C08-3

### C09
- **Bill Eckhardt** Underfitting is also bad because it ignores worthwhile market information; some good traders lost all their money from overfitting.  #mech/research_method
  > if you're afraid of overfitting one way is to underfit
  asset: multi · testable: partly · confidence: high
  ^MT020-C09-1
- **Bill Eckhardt** The E-score combines many performance measures (a 'Super Value') and discounts systems that earned most profit in a short span (e.g. 2 of 20 years), guarding against false impressions of quality.  #mech/research_method
  > a system might make too much of its money over too short a period of time well we have elements of the escore which which will test for that
  indicator: E-score · asset: multi · horizon: years · testable: yes - concentration of profits test · confidence: medium
  ^MT020-C09-2
- **Rob Santino** The Gauntlet is a barrage of tests designed to tear a system apart, showing where it fails, which is as important as knowing why it works, and removes emotion.  #mech/research_method
  > bill has spent as much time uh tearing systems apart as we do putting them together
  indicator: The Gauntlet · asset: multi · testable: partly - proprietary · confidence: medium
  ^MT020-C09-3
- **Rob Santino** Systems can have a strong 2-4 month run then go flat, so scientific testing and emotion removal are needed.  #mech/research_method
  > you could have systems that they might have a two three four month really strong run and then they just go flat or degrade
  asset: multi · horizon: months · testable: no - observation · confidence: low
  ^MT020-C09-4

### C10
- **Bill Eckhardt** The Gauntlet also tests the program code and finds subtle glitches that would otherwise be nearly impossible to find.  #mech/research_method
  > it actually tests the program too it can find very subtle glitches in the program
  indicator: The Gauntlet · asset: multi · testable: no - proprietary · confidence: medium
  ^MT020-C10-1
- **Moritz Seibert** More markets give more independent bets and less noise in any run, though smaller portfolios can outperform for periods because of concentration.  #mech/risk_management
  > the more markets we trade the more independent bets we can place um the better we can crystallize our Edge over time
  indicator: number of markets traded · asset: multi · direction: maximize diversification · horizon: years · testable: yes - performance vs number of markets · confidence: medium
  ^MT020-C10-2
- **Bill Eckhardt** ETC trades about 70 markets, believes in diversification as the greatest financial idea of the 20th century, but avoids markets with too much slippage or too little liquidity.  #mech/risk_management
  > we measure the liquidity and the trade slippage for all markets that we trade whether we're considering trading
  indicator: liquidity, slippage · asset: multi · direction: avoid illiquid markets · testable: yes - cost-adjusted market selection · confidence: high
  ^MT020-C10-3
- **Bill Eckhardt** Many traders undercut diversification by concentrating on whichever few markets are currently hot, which is anti-diversification despite its proven value.  #mech/behavioral _(added by Opus)_
  > I still think a lot of Traders just like to jump on the latest bandwagon you know the latest few things that are hot and avoid everything else you know they're they're anti- diversifying
  indicator: market concentration of trader portfolios · asset: multi · testable: partly - compare concentrated hot-market portfolios vs broad ones · confidence: medium
  ^MT020-C10-X1

### C11
- **Bill Eckhardt** Alternative markets look better in backtests but slippage and exit difficulty in a hurry make them worse in practice.  #mech/risk_management
  > on paper these Alternatives markets might appear better but in practice I I think they're actually worse
  indicator: alternative market slippage · asset: multi · testable: yes - backtest with realistic costs · confidence: medium
  ^MT020-C11-1
- **Bill Eckhardt** Single stocks have a weaker trend component than futures (splits, dividends, long-dominated), so ETC specialises in futures where it has relative advantage.  #mech/structural_shift
  > stocks don't really have the kind of robust Trend component that Futures tend to have in other words our systems don't apply very well to stocks
  indicator: trend strength in stocks vs futures · asset: equities · testable: yes - compare trend returns by asset · confidence: medium
  ^MT020-C11-2
- **Bill Eckhardt** Futures are balanced (one long per short) while stock markets are dominated by longs, so they are different processes.  #mech/structural_shift
  > whereas in the Futures Market there is exactly one long for every short and vice versa it's completely balanced
  asset: multi · testable: no - structural fact · confidence: high
  ^MT020-C11-3
- **Bill Eckhardt** Replicating CTA indices by regression 'sounds like an invitation to really overfit'; futures price changes and trade results are radically non-normal.  #mech/research_method
  > here's a fundamental fact and that is that the distribution the probability distribution of price change and also of trades in a Futures Trading System are not normally distributed
  indicator: CTA replication by regression · asset: multi · testable: yes - replication out-of-sample tests · confidence: medium
  ^MT020-C11-4

### C12
- **Bill Eckhardt** Use robust, distribution-free statistics because futures returns are heavy tailed (Mandelbrot: possibly no variance); small-sample normal statistics give wrong answers, standard deviation and least-squares correlation are unreliable.  #mech/research_method
  > you need to avoid normal techniques and you need to use what statisticians call robust or distribution free statistics
  indicator: robust statistics · asset: multi · testable: yes - compare robust vs normal estimates · confidence: high
  ^MT020-C12-1
- **Bill Eckhardt** Robust statistics need 10-30 times more data, so ETC needs 10-20 years of data and cannot conclude anything from two or three years (that is overfitting).  #mech/research_method
  > the drawback of such robust statistics is that they're kind of data Hogs you need 10 20 time 30 times as much data to make a reliable inference
  indicator: sample length · asset: multi · horizon: years · testable: yes · confidence: high
  ^MT020-C12-2
- **Bill Eckhardt** LTCM failed because it relied on normal distribution theory despite fat tails.  #mech/risk_management
  > busted out spectacularly and it really was because they were using normal distribution Theory
  indicator: LTCM · asset: multi · horizon: years · testable: yes - historical case · confidence: medium
  ^MT020-C12-3
- **Rob Santino** Regression-based CTA-index replication products are likely to end badly.  #mech/research_method _(added by Opus, time-bound view)_
  > I think on the replication question that's probably not going to have a good ending
  indicator: CTA replication ETFs · asset: multi · direction: negative outlook for replication strategies · horizon: years · testable: yes - replication ETF performance vs CTA indices over time · confidence: medium
  ^MT020-C12-X1
- **Moritz Seibert** Evidence cited from Mandelbrot's cotton-price work: futures returns are fat-tailed on both sides and jump-prone, possibly a stable Paretian distribution without a defined variance.  #mech/research_method _(added by Opus)_
  > it is definitely tailed in both directions it is prone to jumps
  indicator: cotton price return distribution · asset: commodities · testable: yes - tail-index estimation on futures returns · confidence: medium
  ^MT020-C12-X2
- **Moritz Seibert** Computing volatility as a standard deviation for sizing reintroduces normal-distribution assumptions and their drawbacks; range-based measures like ATR are not standard deviations.  #mech/risk_management _(added by Opus)_
  > many people would calculate volatility as a function of standard deviation under the assumption of normal distribution there you go again you're back
  indicator: standard deviation vs ATR volatility · asset: multi · direction: prefer robust volatility measures · conditions: heavy-tailed returns · testable: yes - compare sizing with SD vs ATR/robust estimators · confidence: medium
  ^MT020-C12-X3

### C13
- **Rob Santino** Replication portfolios lack predefined exits, exposing them to discontinuity and gap events; stops and exit rules keeping losses small are essential.  #mech/risk_management
  > keeping these losses small is what keeps you in business
  indicator: stop-loss exit rules · asset: multi · testable: partly · confidence: medium
  **Correction (Opus):** Wrong speaker: the point that replication portfolios lack predefined exits and that keeping losses small keeps you in business is made by host Moritz Seibert (he opens 'and Rob maybe to your point'); Eckhardt then agrees. → Moritz Seibert: regression-based replication portfolios lack predefined exits, exposing them to discontinuity and gap events; stops and exit rules that keep losses small are essential.
  ^MT020-C13-1
- **Bill Eckhardt** All futures markets have heavy left tails (leptokurtosis), so trading rules must intervene to control the left tail via risk management.  #mech/risk_management
  > the left hand tail the one that represents losses is very heavy
  indicator: kurtosis, left tail · asset: multi · testable: yes - tail statistics · confidence: high
  ^MT020-C13-2
- **Bill Eckhardt** High win-rate strategies (selling cheap options) periodically bust out because they exploit the bulk of the distribution; ETC rejects any new system with 70-80% success and prefers a ~40% success rate with larger winners.  #mech/risk_premium
  > they make money 70 80 90% of the time but then they're subject to large freakish losses
  indicator: trade success rate · asset: multi · direction: avoid high-win-rate short-tail strategies · testable: yes - win rate vs tail loss · confidence: high
  ^MT020-C13-3
- **Bill Eckhardt** Predictive accuracy is about 51-52%, so put ten times as much emphasis on risk control as on prediction.  #mech/risk_management
  > you almost never know better than about 51 or 52% which way the Market's going
  indicator: hit rate · asset: multi · testable: yes - hit rate measurement · confidence: high
  ^MT020-C13-4

### C14
- **Bill Eckhardt** Normal human attitudes (hold losers) are dead wrong; traders must cut losses and let profits run.  #mech/behavioral
  > you have to get out of your losses you have to let your profits run
  asset: multi · direction: cut losses, run profits · testable: yes - disposition effect · confidence: high
  ^MT020-C14-1
- **Moritz Seibert** The trend follower's edge is a pain arbitrage: enduring bad periods while keeping individual losses small.  #mech/behavioral
  > this pain Arbitrage of sticking to your system during bad times when the going gets tough and nobody enjoys it
  asset: multi · horizon: years · testable: no - behavioral · confidence: medium
  ^MT020-C14-2

### C15
- **Bill Eckhardt** Some Turtle trainees dropped out or could not get along, which showed they lacked the right emotional makeup.  #mech/behavioral
  > there were some who dropped out you know fairly soon and that that indicated that they didn't have the right emotional makeup
  asset: multi · testable: no - anecdote · confidence: low
  ^MT020-C15-1

