---
tags: [source, blog, carver]
---
# Carver blog digest (qoppac.blogspot.com)

31 posts. **Model-written extracts of the pages (WebFetch), not raw text: numbers and quotes are likely but unverified.** B12 has numbers Carver later corrected (B13). Used by [[U02 Rob Carver]].

## B01 How much risk should we take?
[2020-03-05](https://qoppac.blogspot.com/2020/03/how-much-risk-should-we-take.html) · 2020-03-05 · topic: position sizing; risk target; Kelly

**Rules:**
- Position exposure = (1/N) x C x (T/V) x (F/10): C capital, T risk target (annualised stdev), V instrument risk (annualised stdev), F forecast with average absolute value 10 on a -20..+20 scale, N expected number of concurrent positions
- Rule of thumb: annualised stdev is roughly 14 x daily ATR
- Risk target = the most conservative of four limits: personal loss tolerance, broker leverage cap, 'safe leverage' limit (max leverage = tolerable loss / worst plausible one-day crash), and half-Kelly (target = half the expected Sharpe ratio)
- Suggested starting target for a single-rule, single-instrument system: 12%; professional managers typically 10-30%; his own live target is 25%
**Numbers:**
- Half-Kelly: expected SR 0.5 implies a 25% risk target
- Safe-leverage example: 23% one-day crash and 50% tolerable loss gives max leverage 2.17; with 15% instrument risk that caps the target at 32.6%
- Worked example of the four limits: tolerance 25%, broker 50%, safe-leverage 32.6%, Kelly 12% -> chosen target 12%
- Sharpe benchmarks quoted: average retail trader -1.0; simple single-indicator mechanical system 0.24; diversified systematic retail trader about 1.0; top hedge funds 2-4
**Caveats:**
- Stdev is an imperfect risk measure; fat-tail crashes (e.g. 1987) can exceed what it implies
- Sharpe figures are illustrative benchmarks, not measured for a specific strategy
- Reader comments: a 25-day vol lookback can give huge positions after quiet spells; author says his own system uses a vol floor and a forecast-based V matched to holding period, and prefers simple over log returns

**Reasoning:** Size is proportional to capital and target risk and inversely proportional to instrument risk, so volatile instruments get smaller positions and total risk stays near target. Forecast strength scales exposure linearly. Kelly logic ties the affordable risk target to the true edge, and because the edge is uncertain and full Kelly is too aggressive, half-Kelly is the practical cap.

> The better your trading system is, the more risk you can take.
^B01

## B02 How fast should we trade?
[2020-04-02](https://qoppac.blogspot.com/2020/04/how-fast-should-we-trade.html) · 2020-04-02 · topic: costs; speed limit; trading speed

**Rules:**
- Total annual cost = holding (roll) cost + trading cost x number of trades; express costs in Sharpe-ratio units by dividing by annualised instrument stdev
- Speed limit: spend no more than one third of expected pre-cost SR on costs
- Max trades per year = ((expected SR / 3) - holding cost) / cost per trade
- Small trader with market orders pays about half the spread; he reports about a quarter of the spread with a simple execution algo
- Keep at least three trading-rule variations for diversification but drop the fastest ones that breach the speed limit
**Numbers:**
- Eurodollar example: execution cost 0.0058 SR per trade, roll cost 0.026 SR per year; with expected SR 0.24 the cost budget is 0.08, giving max about 9.3 trades per year
- Stop distance (fraction of annual vol) maps to trades per year: 0.3 -> 11.9, 0.4 -> 7.8, 0.5 -> 5.4
- EWMAC 64,256 averages SR about 0.28 and trades about 1.1 times a year; the Law of Active Management would predict SR 1.68 for EWMAC 2,8 but actual is about 0.07
- Net of Eurodollar costs the fastest rules lose money; EWMAC 8 only just passes the limit
- If costs rise 50% when volume doubles, speeding up stops helping around EWMAC 16
**Caveats:**
- Law of Active Management is an idealised upper bound that fast rules usually miss
- Cost assumptions are snapshot values (COVID-era spreads were wide); very fast trading changes costs via market impact
- Comparing average pre-cost SR across instruments against Eurodollar costs is a deliberate simplification
- Smoothing and buffering change turnover and should be tested in the backtest

**Reasoning:** Costs grow roughly linearly with the number of trades whereas the gross edge from trading faster grows more slowly (at best like the square root of trade count, by the Law of Active Management, which is an upper bound). Net return therefore peaks at some speed, and the one-third cost budget is a heuristic to locate it.

> SPEED LIMIT: DO NOT SPEND MORE THAN ONE THIRD OF YOUR EXPECTED PRE-COST RETURNS ON COSTS
^B02

## B03 Should I run my trading system at a fixed expected volatility target?
[2020-10-06](https://qoppac.blogspot.com/2020/10/should-i-run-my-trading-system-at-fixed.html) · 2020-10-06 · topic: vol targeting; forecast strength and realised risk

**Rules:**
- Baseline: expected risk = target risk x relative aggregate forecast strength x relative correlation factor (RCF); i.e. portfolio risk is deliberately allowed to float with aggregate forecast strength
- Fixed-risk variant: multiply all positions by target / ex-ante portfolio risk; forecast-adjusted variant multiplies by (forecast strength x target / ex-ante risk), which reduces to 1/RCF
- Aggregate forecast strength = instrument-weighted sum of absolute forecasts divided by the average absolute forecast (10)
- Risk multiplier capped at 3.0
**Numbers:**
- Sharpe: original 0.93; fixed-risk 0.64; forecast-adjusted (remove only RCF) 0.87
- Aggregate forecast strength varied from below 0.2 to above 1.3 once all 20 instruments were in (about sixfold)
- Fixed-risk made skew more negative at daily/weekly/monthly horizons and worsened the 1% daily tail, though kurtosis improved
**Caveats:**
- Skew and kurtosis estimates carry large sampling error
- Scaling positions by a constant ignores the extra trading each variant would cause, so costs are approximate
- Correlations break down in crises so realised risk can still exceed expected
- Author would not implement the forecast-adjusted version in his own system because of complexity and no clear gain

**Reasoning:** Aggregate forecast strength predicts future risk-adjusted returns (ex-post returns slope upward with it), so forcing constant risk throws that information away and cuts Sharpe. The RCF varies with current positions and correlations without any link to expected return, so removing only that term keeps most of the performance.

> it throws away the information provided by aggregate forecast strength
^B03

## B04 Do non-binary forecasts work?
[2020-07-03](https://qoppac.blogspot.com/2020/07/do-non-binary-forecasts-work.html) · 2020-07-03 · topic: forecast scaling and capping; linearity of forecast response

**Rules:**
- Forecast = calibrated estimate of future risk-adjusted return, scaled to average absolute value 10; cap at +/-20 (twice the target average)
- Holding period = 256 / annual turnover (EWMAC 16,64 on Eurodollar is about 17 business days)
- Normalised return = N-day price change divided by daily vol x sqrt(N)
- Test design: bucket forecasts by sign and quantile (bin size 2 gives four buckets) and t-test adjacent buckets for positive slope, plus first versus last bucket
- Decided not to add an intercept to correct the long bias in returns, since that would add a parameter and a built-in long bias
**Numbers:**
- Eurodollar, uncapped, sign only: mean normalised return 0.21 for positive forecasts vs 0.02 for negative (t = 7.6); positive forecasts about 2x as frequent
- Pooled over all instruments, capped, four buckets: adjacent-bucket t-stats 10.4, 13.5, 16.0; first-to-last t-stat 35.7
- Every EWMAC variant (2_8, 4_16, 8_32, 32_128, 64_256) passed pooled; ewmac2_8 weakest at about t = 3.6
- Carry pooled first-to-last t-stat about 40.9
- On Eurodollar alone the segment t-stats were marginal (1.8-4.2); 8 instruments in the dataset would fail the test for this rule
**Caveats:**
- Eurodollar was chosen to illustrate interesting behaviour; strong results come from pooling
- Without capping, slow rules show reversion in the tails
- Non-linear response functions invite overfitting; non-binary sizing needs more capital
- Digest note (not from the post): overlapping N-day returns are autocorrelated so the p-values are probably overstated

**Reasoning:** Stronger forecasts are followed by larger risk-adjusted returns across the whole range, so scaling position size with forecast strength (non-binary) is supported over binary +/-1 positions. At the extremes uncapped returns flatten or revert (trend exhaustion; very quiet markets giving huge forecasts and then reversing), which capping largely neutralises.

> the stronger your forecast, the larger your position should be.
^B04

## B05 Forecast linearity and forecasting mean reverting volatility
[2020-09-01](https://qoppac.blogspot.com/2020/09/forecast-linearity-and-forecasting-mean.html) · 2020-09-01 · topic: volatility estimation; vol mean reversion; forecast scaling

**Rules:**
- Risk-adjusted forecast = expected return / recent vol, with recent vol an exponentially weighted estimate of roughly one-month half-life
- Blended vol forecast = (1 - p) x current vol + p x slow vol, where slow vol = long-run average of vol (EWM span 2500 days, about 10 years); eyeballed p about 0.33, regression gave about 0.98 x current + 0.41 x (slow - current)
- Untested proposal: double slow-momentum forecasts then cap at 10 (instead of 20) to avoid the tail reversion
**Numbers:**
- Test rule ewmac64_256 pooled: at extreme forecasts realised vol ran 10-20% above the current-vol forecast, overstating expected risk-adjusted returns by a similar amount
- Blended vol cut the uncapped vol error to under 5% and removed about two-thirds of the bias
- Vol-forecast R-squared on S&P 500: 0.884 blended vs 0.84 for current vol alone
**Caveats:**
- Motivating chart used one market (S&P 500)
- Blend weight fitted in-sample (author argues it is stable)
- Regression residuals have heavy autocorrelation (Durbin-Watson about 0.03) and fat tails so fit statistics are fragile
- Did not test whether better vol forecasts actually raise returns; warns of overfitting a non-linear fix

**Reasoning:** Large forecasts mostly occur when recent vol is unusually low; low vol tends to revert upward, often just as the trend turns, so realised vol exceeds the forecast and realised risk-adjusted returns fall short. Blending in long-run vol removes most of that bias; the remainder is attributed to trend exhaustion.

> trends tend to get exhausted after a while, so a very strong trend is due a reversal.
^B05

## B06 My trading system (as of December 2021)
[2021-12-02](https://qoppac.blogspot.com/2021/12/my-trading-system.html) · 2021-12-02 · topic: full system spec: rules, forecast weights, IDM, instrument selection, dynamic optimisation

**Rules:**
- Rule families: EWMAC at 4,8,16,32,64; assettrend and normmom at 2-64; breakout 10-320; relative momentum 10-80; acceleration 16,32,64; carry spans 10,30,60,125; relative carry; skew (abs and relative, 180 and 365); slow mean reversion in asset class (mrinasset160); mean reversion in the wings (mrwrings4)
- Handcrafted forecast weights: trendy group 0.6 / other 0.4. Within trendy: assettrend 0.15, relmomentum 0.12, breakout 0.12, momentum 0.10, normmom 0.11. Within other: carry 0.18, relcarry 0.08, accel 0.06, skew 0.04, mean reversion 0.04
- Asset-class weights: equity 0.22, bonds and STIR 0.19, ags 0.15, FX 0.13, metals and crypto 0.13, oil/gas 0.13, vol 0.05
- IDM set at 2.5, deliberately below the estimated value
- Vol estimate = 70% recent vol + 30% ten-year average vol; momentum-style forecasts attenuated when vol is above its historic level
- Cost filter: skip an instrument for a rule if cost exceeds 0.01 SR per trade (speed limit); instruments sampled for spreads before inclusion
- Positions set by dynamic optimisation (minimum tracking error to the unrounded optimal portfolio, integer contracts) plus buffering
**Numbers:**
- 146 instruments, 109 with positive Sharpe, median Sharpe 0.27, average correlation of subsystem returns 0.05
- Equal-weighted rule Sharpes: carry 0.90-0.95; momentum64 0.73; normmom32 0.82; mrwrings4 -0.94; mrinasset160 -0.63
- Backtest (daily): Sharpe 1.31, mean 30.1%, stdev 23.0%, Sortino 1.81, Calmar 0.70; monthly Sharpe 1.14; hit rate 62.6%
**Caveats:**
- Backtest is heavily in-sample and calibrated, so overstates achievable performance
- Live weights are manual whereas backtests use automated handcrafting
- Rule Sharpes are crude averages across instruments
- Risk target, forecast cap and EWMAC scalars are not stated in the post

**Reasoning:** Trend following is the core and carry is the single most valuable rule. Mean-reversion rules lose money alone but are strongly negatively correlated with trend rules so handcrafting still gives them a small weight because backtest Sharpes are uncertain. Vol attenuation addresses the observed deterioration of momentum when vol is high.

> the biggest change to my system this year has been the introduction of a dynamic optimisation system
^B06

## B07 Year to date and historic performance by trading rule (April 2022)
[2022-05-11](https://qoppac.blogspot.com/2022/05/historic-and-recent-performance-by.html) · 2022-05-11 · topic: trading rules: divergent vs convergent performance and diversification

**Rules:**
- Rules are grouped as divergent (acceleration, assettrend, normalised momentum, EWMAC, breakout, relative momentum) and convergent (carry, relative carry, mean reversion in asset class, mean reversion in the wings, skew absolute and relative)
- Live trading has used the dynamic-optimisation strategy only since November 2021, so live-vs-backtest comparisons before that are not like for like
**Numbers:**
- Instrument count over history from a reader reply: about 17 (1970s), 27 (1980s), 36 (1990s), 57 (2000s), 102 over the full backtest
- No numeric Sharpes are readable in the text (they are in chart images); YTD to 4 April 2022 divergent rules were very good, skew excellent, carry and other convergent rules poor
**Caveats:**
- Static-portfolio proxy ignoring contract rounding, buffering and path dependency
- Short YTD Sharpe is unstable; data stop 4 April so later losses are excluded
- Early-March result partly execution luck
- Early backtest years have far fewer instruments

**Reasoning:** Divergent rules profit when prices keep moving one way so do well in trending markets; convergent rules assume reversion and suffer when trends persist. Most divergent variants are very similar to each other, so combining them gives little diversification beyond the first. Carry may have underperformed partly because agricultural markets were about half of the 1970s portfolio.

> With the exception of relative momentum, all very good, but also all very similar so not much diversification there.
^B07

## B08 Portfolio construction through handcrafting: The method
[2018-12-07](https://qoppac.blogspot.com/2018/12/portfolio-construction-through_7.html) · 2018-12-07 · topic: handcrafting; diversification multiplier; portfolio weights

**Rules:**
- Start from equal weights; for assets with different risk use inverse-volatility weights (weight proportional to 1/sigma, normalised) and convert to cash weights by dividing by sigma and renormalising; skip this step for trading strategies that already target a common risk
- Group assets hierarchically: equal vol weights across groups, then within groups, multiplying weights down the tree
- Diversification multiplier for a group = group risk / single-asset risk; multiply the group's raw weight by it and renormalise
- Risk targeting with leverage: scale by target risk / natural risk of the portfolio. Without leverage: if target < natural risk hold cash = (natural - target)/natural
- Original method matched correlations to seven candidate matrices (0, 0.5, 0.9) and applied conditional Sharpe multipliers; he later replaced both (see B09, B10)
**Numbers:**
- S&P 500 (16% vol) and US 2y bonds (2% vol): inverse-vol cash weights 11.1% / 88.9%; natural portfolio risk 2.5-3.5%
- 10% target at correlation 0.5 needs leverage about 3.2; with no leverage 59.8% S&P / 40.1% cash-bonds
- DM example: A,B correlated 0.5 with C uncorrelated, equal vol 10%: DM of group AB 1.155, final weights 26.8% A, 26.8% B, 46.4% C
- Correlation estimate uncertainty with 100 observations: 95% interval -0.2 to +0.2 for rho = 0 and 0.34 to 0.63 for rho = 0.5
**Caveats:**
- Assumes equal Sharpe ratios unless conditioned; designed for long-only weights
- Candidate-matrix and Sharpe-adjustment steps superseded by the author's later posts
- Human vs machine groupings can differ

**Reasoning:** Standard deviations are the most stable estimates so inverse-vol is a sound base. Grouping stops a cluster of similar assets taking most of the risk budget just because it has many members, and the diversification multiplier gives correlated groups more capital because their combined risk is lower than the raw weight implies.

> Equal weights should be the starting point for any portfolio allocation.
^B08

## B09 Handcrafting follow up: adjusting portfolio weights for Sharpe Ratios
[2019-12-10](https://qoppac.blogspot.com/2019/12/new-and-improved-sharpe-ratio.html) · 2019-12-10 · topic: handcrafting; Sharpe ratio uncertainty; forecast weights

**Rules:**
- Old heuristic: scale each weight by a factor depending on its SR relative to the group average, bounded 0.6 to 1.4, then renormalise
- New method: treat the SR difference as a distribution. Standard error of the difference between two assets = sqrt(2 x (sigma/sqrt(N))^2 x (1 - rho)), N years of data, rho average correlation
- Optimise weights at evenly spaced confidence points of that distribution (step 0.01 is enough) and average the weights; then express as a ratio to 1/N and renormalise
- pysystemtrade uses the minimum years of data across assets
**Numbers:**
- SR difference 0.2, rho 0.3, 10 years: median weights [0.653, 0.347]; at the 10% confidence point [0.14, 0.86]; at the 90% point [0.874, 0.126]
- Optimising raw with means 0.05 vs 0.06 at rho 0.9 gives roughly [0, 1], the instability the heuristic avoids
- With rho 0.5 and 2 years of data the lowest weight is about 0.5 of 1/N; with 30+ years it approaches zero
- VIX example, five rules incl. always-long: always-long weight fell from about 0.41 to 0.11 after adjustment as its performance faded
**Caveats:**
- Assumes Gaussian sampling error, equal stdevs and average SR 0.5
- Only mean uncertainty modelled here; correlation uncertainty is handled by the earlier heuristic and vol assumed stable
- Weight response is not symmetric (1.2 and 0.8 do not pair)
- Extra computation time

**Reasoning:** The mean (Sharpe) has the largest sampling error among return moments. Averaging optimised weights over the plausible range of the SR difference gives bigger tilts when histories are long and strategies are highly correlated (so small differences are informative) and tiny tilts when data are short.

> the mean (or equivalently Sharpe Ratio) is the moment of the distribution with the largest sampling error
^B09

## B10 Handcrafting follow up: a better method for dealing with correlation uncertainty
[2020-11-03](https://qoppac.blogspot.com/2020/11/improving-use-of-correlations-in.html) · 2020-11-03 · topic: handcrafting; correlation estimation and lookback; weights floor

**Rules:**
- For each three-asset group compute Fisher-transform confidence points for each correlation, optimise at each combination, and average the weights; pysystemtrade uses a step of 0.25 (9 optimisations per matrix)
- Inflate the Fisher standard error by a fixed factor of 4 as a proxy for real forecasting error
- Apply a minimum weight floor of 0.1 then renormalise to 1 (example [0.5,0.5,0] becomes [0.4545,0.0909,0.4545])
- Correlation lookback for handcrafting: about 10 years (about 500 weekly points)
**Numbers:**
- Coverage test: nominal 95% correlation intervals for S&P vs US10 were breached in 15 of 18 years, US5 vs US10 in 14 of 18; true uncertainty is roughly 4x the sampling-error intervals
- Out-of-sample R-squared lookback study: underlying returns best near 100 weeks; subsystem returns at least about 2 years; trading rules at least about 5 years, perhaps 10+
- Weights for AB=0.9, AC=0, BC=0.9: raw 0.5/0/0.5; original handcrafted 0.39/0.22/0.39; revised (100 points) 0.498/0.003/0.498
**Caveats:**
- Factor 4 and the 0.1 floor are heuristics; the right factor should depend on the correlation level
- Assumes stationary correlations and Gaussian returns
- With long lookbacks the method yields zero weights; author concludes zero weights are hard to justify for non-stationary data
- SR and correlation uncertainty not treated jointly

**Reasoning:** Sampling error in correlations feeds straight into portfolio weights, so averaging optimal weights over the plausible range of correlations gives robust allocations. Because past correlations are poor guides to future ones, intervals are widened by a fixed fudge factor, and a floor keeps every asset in.

> We're not really interested in the uncertainty of *past* correlations.
^B10

## B11 Fit forecast weights by instrument, by group, or pool everything; or a blend?
[2021-05-27](https://qoppac.blogspot.com/2021/05/fit-forecast-weights-by-instrument-by.html) · 2021-05-27 · topic: fitting forecast weights; pooling; overfitting; cost speed limit

**Rules:**
- Compare weights fitted per instrument, per k-means cluster of instruments (4 clusters), pooled over all instruments (gross returns pooled, costs per instrument), and a simple average (blend) of the three
- Speed limit: zero a rule for an instrument if its cost exceeds 0.13 SR
- Test universe 14 instruments, 12 rules (EWMAC 4/16 and 64/256, carry, breakouts, mean reversion, relative momentum, assettrend, normmom, relcarry, skew, kurtosis) not cherry-picked for profitability
**Numbers:**
- Net Sharpe (all rules / with speed limit): individual 0.602 / 0.545; groups 0.656 / 0.546; everything 0.651 / 0.587; blend 0.656 / 0.587; equal weights 0.657 / 0.726
- Cost drag in SR (all rules / with limit): individual 0.120 / 0.083; groups 0.109 / 0.085; everything 0.096 / 0.079; blend 0.090 / 0.083; equal weights 0.178 / 0.074
**Caveats:**
- Sharpe differences are small; one 14-instrument subset, one rule set, one period
- Four clusters is arbitrary
- Equal weights winning with the speed limit would not hold for a less curated rule set
- Speed limit lowers net Sharpe for most schemes, so its benefit is mixed

**Reasoning:** Per-instrument fitting uses little data and gives noisy weights; pooling brings more data and more robust weights, and grouping similar instruments also groups similar cost levels. Averaging fitting schemes usually improves out-of-sample behaviour. Differences between schemes are small and equal weights are competitive.

> Having said that a clearly stupid thing to do is to fit weights for each instrument individually
^B11

## B12 Optimising my way out of a small fund (part five): dynamic optimisation with greedy algo (Mr Greedy, part one)
[2021-10-01](https://qoppac.blogspot.com/2021/10/mr-greedy-and-tale-of-minimum-tracking.html) · 2021-10-01 · topic: dynamic optimisation; instrument selection for small accounts

**Rules:**
- Objective: minimise the stdev of the tracking-error portfolio (current integer positions minus unrounded optimal positions) using the instrument covariance matrix, plus trading costs
- Cost penalty = per-instrument cost x abs trade size x a shadow-cost multiplier (default 10 in this version)
- Greedy search: start at zero, each step add or remove one contract in the direction of the sign of the optimal position, take the single best improving step, repeat until none improves
- Constraints supported: reduce-only, do-not-trade, min and max positions
**Numbers:**
- 45 instruments, $100K: Sharpe unrounded 1.17, rounded 1.06, optimised 1.19; costs about 0.13 SR in all cases
- Return correlation with the unrounded portfolio: optimised 0.94, rounded 0.97
- Held 6 positions on average out of 45 (max 18)
- At $50K: optimised Sharpe about 0.1 above rounded but about 0.2 below unrounded
**Caveats:**
- Author later said the method did not work as well as hoped: his cost calculations were wrong for sparse positions and turnover was understated (see B13 for the corrected version)
- Greedy search can stop at local optima
- In-sample backtest with fixed shadow cost

**Reasoning:** Many near-equivalent integer portfolios exist, and minimising tracking-error variance gives a more stable target than maximising utility. A greedy one-directional search is usually good enough and scales far better than grid search; risk of untradeable markets is substituted into correlated tradeable ones.

> It didn't work, at least not as well as I'd hoped.
^B12

## B13 Optimising my way out of a small fund (part six): greedy algo part two
[2021-11-19](https://qoppac.blogspot.com/2021/11/mr-greedy-and-tale-of-minimum-tracking.html) · 2021-11-19 · topic: dynamic optimisation; buffering; costs; turnover

**Rules:**
- Shadow cost raised to 250, reasoned from an assumed Sharpe of 1.0 (not grid-searched)
- Portfolio-level buffer using tracking error as utility: if tracking error between current and unrounded optimal positions is below the buffer, do nothing; otherwise optimise, then trade only the share (x - b)/x of the required trades, where x is current-vs-optimised tracking error and b the buffer
- Buffer size 0.0125 (1.25% annualised risk), i.e. 10% of a 25% average risk target
- Costs measured in dollars per historic trade, deflated by changes in price vol; roll costs assume rolling the pre-roll position
- Shrink the correlation matrix to keep it positive semi-definite
**Numbers:**
- Dynamic 114-instrument portfolio, $500K: gross SR 1.336, net 1.287, cost about 5bp SR per year, turnover 51 times a year, return correlation with unrounded portfolio 0.986, holds a quarter to a third of instruments
- Static 34-instrument benchmark: gross SR 1.322, net 1.275, turnover 37.5 times a year
- Unrounded 114-instrument portfolio SR 1.359, so the integer constraint costs only a few bp of SR
**Caveats:**
- Author states the previous post's results were wrong, mainly from understated turnover and costs
- Shadow cost and buffer come from assumptions, not formal calibration
- Forecast weights fitted in-sample; benchmark depends on the chosen 34 instruments; static backtest has under 15 instruments before 2000
- No clean general fix for non-PSD pandas correlation matrices beyond shrinkage

**Reasoning:** The greedy algorithm always takes the sign of the optimal position, so every sign flip forces a trade regardless of shadow cost, which sets a turnover floor. A portfolio-level buffer that trades only the excess tracking error over the buffer fixes that and replaces instrument-by-instrument buffering.

> every time the underlying forecast changes sign, we'll definitely trade regardless of the size of the shadow cost.
^B13

## B14 An exogenous risk overlay
[2020 (about May; exact date not shown in the fetched text)](https://qoppac.blogspot.com/2020/05/when-endogenous-risk-management-isnt.html) · 2020 (about May; exact date not shown in the fetched text) · topic: risk management; position scaling in crises

**Rules:**
- Overlay gives a multiplier between 0 and 1 applied to all positions; it is the minimum of three components
- Maximum expected risk: min(1, 2 x target risk / current expected risk)
- Correlation risk: set all correlations to 1 (absolute weights): min(1, 4 x target / expected risk under that matrix)
- Stdev risk: replace each instrument's vol with its 99th percentile estimate over about 10 years (2,500-day rolling quantile): min(1, 6 x target / expected risk under those vols)
- Inputs: 30-day EWMA stdev, 120-day EWMA correlation; config keys max_risk_fraction_normal_risk 2.0, _correlation_risk 4.0, _stdev_risk 6.0
**Numbers:**
- Backtest realised risk 23.7% against 25% target; 6-month rolling risk ranged from about 10% to above 40%
- Overlay cut annual return and risk by roughly 3% each; Sharpe about 0.94 with vs 0.956 without (text is ambiguous which is which)
- Slightly less positive skew, lower kurtosis, better 1% quantile, slightly shallower drawdowns
**Caveats:**
- Thresholds 2, 4, 6 are calibrated choices not derived theory; warns against tuning them for performance (overfitting)
- Core risk model is Gaussian; some large outliers remain unpredicted (possibly bad data)
- Backtest on a subset of instruments with price data still being cleaned

**Reasoning:** The core system's inverse-vol scaling and Kelly-style sizing assume roughly Gaussian returns with predictable vol and correlation. When correlations or vols spike against open positions, expected risk can jump far above target; the overlay caps exposure in those states without touching the signals.

> The vast bulk of the risk management load is being carried by the core system.
^B14

## B15 Skew and expected returns
[2019-10-21](https://qoppac.blogspot.com/2019/10/skew-and-expected-returns.html) · 2019-10-21 · topic: skew as a predictor; skew premium

**Rules:**
- Rolling skew windows of 7, 14, 30, 90, 180, 365 days compared with the next period's annualised Sharpe (16 x mean/stdev); split at the median into high and low skew
- Drop false outliers with |vol-normalised return| > 10
- Demeaning variants: own 10-year average, cross-sectional median, asset-class median
- 1,000-sample bootstrap for skew sampling uncertainty
**Numbers:**
- Full-sample annualised mean returns: high-skew -6.6% vs low-skew +1.8% (mostly driven by VIX and V2X)
- Excluding VIX and V2X, bootstrapped Sharpe means 0.37 (high skew) vs 0.24 (low) so the risk-adjusted cross-sectional result reverses
- Time series: low-skew leads high-skew by about 0.1-0.4 SR for windows of one month or longer; high-skew assets made basically no money over 3-12 months
- Cross-sectional demeaning keeps the effect (about 0.4 SR best around 6 months); asset-class demeaning kills it (about 0.1 SR, insignificant)
**Caveats:**
- Few individual skew estimates are statistically significant; confidence intervals are wide for fat-tailed assets
- Raw return effect largely comes from vol markets
- Most realistic variant (asset-class demeaning) is weak and insignificant
- Window and cutoff choices made with full-sample visibility; no costs; analysis not a tradable backtest

**Reasoning:** Negatively skewed assets give frequent small gains and rare large losses, so investors are paid extra to hold them. The idea is a risk premium for skew, not short-term overreaction to losses. Demeaning matters because skew differs structurally by asset class.

> The most overlooked characteristic of a strategy is the expected skew of it's returns, i.e. how symmetrical they are
^B15

## B16 Trend following and skew
[2019-02-28](https://qoppac.blogspot.com/2019/02/skew-and-trend-following.html) · 2019-02-28 · topic: trend rules and skew by speed; skew timing

**Rules:**
- Universe about 40 futures in pysystemtrade; EWMAC pairs 2/8 up to 64/256; skew measured in 5-year windows at daily, weekly, monthly, annual horizons
- Separate test: trailing 3-month skew of daily returns versus next 3-month annualised Sharpe
**Numbers:**
- Median daily skew by rule: 2_8 -0.04, 4_16 -0.07, 8_32 -0.51, 16_64 -0.73, 32_128 -0.94, 64_256 -0.82
- Skew becomes more positive at slower measurement horizons; fastest rules peak at a monthly horizon
- After negative trailing skew next-period Sharpe averaged +0.33, after positive skew -0.016 (p = 0.01)
- Drawdown illustration (SR 0.5, 25% vol): 10%-probability drawdown about 9.3% at zero skew, 11% at +1 skew, 3.7% at -2 skew
**Caveats:**
- One dataset, 5-year windows, wide skew uncertainty
- No costs
- Faster-rule explanation is speculative; the claimed negative correlation of a skew rule with momentum was not verified
- Warns adding skew rules risks overfitting and does not change EWMAC rules based on this

**Reasoning:** Slow trend rules hold positions for months so their return skew reflects the skew of the underlying assets they are holding; they are often long negatively skewed assets (collecting a skew premium), so daily return skew is negative. Fast rules are short after sell-offs, and skew mean-reverts, so they end up short assets whose skew later improves. Positive skew only shows at the right horizon.

> Trend following rules do indeed have the positive skew you'd expect... but only at the right time horizon.
^B16

## B17 How much should we get paid for skew risk? Not as much as you think!
[2025-02-06](https://qoppac.blogspot.com/2025/02/how-much-should-we-get-paid-for-skew.html) · 2025-02-06 · topic: skew; geometric return; leverage and Kelly

**Rules:**
- Choose leverage to maximise geometric return at a chosen point of the outcome distribution: the median (full Kelly) or the 10% quantile (conservative)
- Build returns by mixing Gaussians to get series with the same Sharpe but different skew and left-tail fatness, bootstrap at each leverage level, and read the price of skew off indifference curves of equal geometric mean
**Numbers:**
- Kelly investor: going from skew -3 to +3 is worth at most about 4bp of SR; 10%-quantile investor at most a couple of bp
- Left-tail fatness worth at most about 5bp (Kelly) or 3bp (10% investor)
- Kelly optimal leverage rises from about 2.7 to 3.7 (lowest SR) or 4.2 to 5.6 (highest SR) going from most negative to most positive skew
- Headline: about 6bp of SR per 5 units of skew at best, so a 0.5 skew difference should cost under 1bp; the market price implied by a 0.30 SR drop is roughly 50x too high
**Caveats:**
- Brute-force bootstrapping gives noisy clouds, some non-monotonic curves
- Assumes freely available leverage; interaction of leverage with the Kelly point not fully analysed
- Depends on chosen quantile and bootstrapped returns; blog exploration not peer-reviewed
- Negatively skewed strategies can still be dangerous with leverage

**Reasoning:** Skew mainly bites when leverage is high because a fat left tail is punished by compounding; conservative investors who use less leverage are barely affected. Sharpe ratio drives most of the geometric return, so skew is second order and should earn only a small premium.

> Sure, get it if it's free, but don't pay much for it otherwise.
^B17

## B18 Testing skew and kurtosis as a trading rule
[2020-01-13](https://qoppac.blogspot.com/2020/01/skew-and-kurtosis-as-trading-rules.html) · 2020-01-13 · topic: skew and kurtosis trading rules

**Rules:**
- Three factors: skew, skew conditioned on kurtosis sign (skewK), kurtosis conditioned on skew sign (kurtS); four demeaning options (abs, ts, cs, rv within asset class); lookbacks 7, 14, 30, 90, 180, 365 days
- Signal = factor / its robust vol, optionally times conditioning sign, EWMA-smoothed with span = lookback/10
- Pruning: drop 7-day rules (cost above 0.13 SR), drop ts/cs variants (correlation 0.95-0.997 with abs), drop skewK (correlated 0.82-0.84 with kurtS) -> 20 rules: skew and kurtS, each in abs and rv form, at 14/30/90/180/365 days
**Numbers:**
- S&P 500 only: best vanilla skew rule skew_abs_365 SR 0.33; slowest skew_rv rules about 0.35; faster skew rules worse; carry and most EWMAC around 0.9 or higher
- Adding the skew rules raised the standard backtest SR by only about 7bp
- Adjacent-lookback skew_abs correlations low (about 0.53 between 14 and 30 days)
**Caveats:**
- Tested on a single market (S&P 500)
- Rules pruned after seeing results (implicit fitting); 365-day window matches an academic paper
- Estimators not exponentially weighted and sensitive to single extreme returns
- 7bp gain is small against estimation uncertainty; author would prefer not to use the kurtosis rules

**Reasoning:** Recent realised skew and kurtosis are known at decision time and may predict returns; slow skew signals may be negatively correlated with momentum and so diversify, though in testing the correlation was roughly zero.

> I would prefer not to use the kurtosis rules
^B18

## B19 Kelly versus Classical portfolio theory, and the two kinds of uncertainty premium
[2018-06-08](https://qoppac.blogspot.com/2018/06/kelly-versus-classical-portfolio-theory.html) · 2018-06-08 · topic: Kelly; leverage; Sharpe uncertainty

**Rules:**
- Kelly: optimal leverage f* = r/s^2 and optimal risk target s* = r/s (r arithmetic expected excess return, s unlevered stdev, risk-free zero)
- Utilitarian: risk target = maximum risk tolerance s_max; proposed compromise s* = min(r/s, s_max)
- SR sampling variance approx (1 + 0.5 SR^2)/N (Lo 2002) under i.i.d.; use a conservative percentile of the SR distribution to set leverage (uncertainty appetite)
**Numbers:**
- SR 0.5, 10 years monthly data (N = 120): median optimal risk 50% and leverage 5; half-Kelly 2.5
- Confidence that leverage is not too high -> risk target: 10% -> 9.2%; 25% -> about 17%; 50% -> 50%; 75% confidence (25th percentile) -> SR about 0.29, risk 29%, leverage 2.9
- Half-Kelly corresponds to roughly 22% confidence in this example
- Case SR 0.2 long-only: Kelly target 20% (leverage 2); case SR 1.0 equity-neutral: full Kelly 100% risk (leverage 20) versus practical 15% risk appetite
**Caveats:**
- Stdev treated as known; Gaussian i.i.d. returns assumed (no skew, autocorrelation, instability)
- Uncertainty-appetite framework is the author's own proposal not established theory
- Commenters objected that a single vol figure ignores SR; author replied that short-term leverage risk dominates

**Reasoning:** Kelly leverage depends on the true Sharpe ratio which is poorly estimated, so size using a conservative point in its sampling distribution. Greater uncertainty aversion lowers the risk target, so an external risk-appetite cap rarely binds; uncertainty aversion and risk aversion are hard to separate in practice.

> Frankly this is a bit of a cop-out by the Kelly people
^B19

## B20 Portfolio optimisation, leverage, allocation and uncertainty
[2023-12-12](https://qoppac.blogspot.com/2023/12/portfolio-optimisation-uncertainty.html) · 2023-12-12 · topic: leverage; bootstrap; Kelly with uncertainty; asset allocation

**Rules:**
- Daily bootstrap with replacement, series the same length as the data, repeated many times; choose leverage and allocation to maximise a chosen percentile (10th, 25th, median, 75th, 90th) of geometric return rather than the mean
- Inputs: S&P and 10-year bond futures since 1982 with means and vols reset to forward-looking values (bonds 3.5% at 5% vol, equities 5.75% at 17% vol, 2.5% risk-free, zero correlation)
**Numbers:**
- 60/40: vol about 10.4%, SR 0.226, closed-form Kelly leverage about 2.17
- Bootstrapped geometric mean at 1x leverage about 4.1% vs 4.31% Gaussian; at 2x about 4.8% vs 5.04%
- Optimal leverage by tolerance: median about 2.1; 25th percentile about 1.75; 10th about 1; 90th over 3
- Joint optimum (median): 30% equities at 4.5x leverage (5.8% geometric); suggested robust choice about 20% equities at 3x (stdev 15.75%); 25th percentile about 20% equities at leverage near 2
**Caveats:**
- Forward-looking inputs are illustrative; zero correlation assumed
- Bootstrap noise requires reading the optimum off a smoothed curve
- Daily resampling destroys autocorrelation, which matters for momentum strategies
- Parameter-estimation uncertainty not in the main analysis; leverage should be adjusted to current risk

**Reasoning:** Real returns are left-skewed with fat tails, so the geometric mean and optimal leverage are lower than Gaussian Kelly implies. The geometric mean falls steeply above the optimum, so picking a point below the peak is more robust, and the bootstrap lets the leverage reflect how much outcome dispersion the investor accepts.

> Each point on this histogram represents a single bootstrapped set of data, the same length as the original.
^B20

## B21 Dynamic trend following
[2020-12-04](https://qoppac.blogspot.com/2020/12/dynamic-trend-following.html) · 2020-12-04 · topic: trend rules; vol-scaled positions; dynamic stops; skew trade-off

**Rules:**
- Base: EWMAC 16/64 binary forecast with stop gap 0.5 x annualised stdev (X-factor 8 on daily vol)
- Dynamic vol control: position = (initial vol / current vol) x initial position, with stop gap scaling with current vol
- Dynamic stop: X-factor 2 when vol-normalised P&L <= 0, rising linearly to 8 at P&L of 8, capped at 8; cutoffs chosen by eye from Eurodollar
**Numbers:**
- Instrument-level gross Sharpe: neither 0.19; dynamic vol 0.25; dynamic stop 0.05; both 0.07
- Trade skew: 1.95 / 1.87 / 3.07 / 4.00; monthly return skew: 0.73 / 0.08 / 0.77 / 0.05
**Caveats:**
- Gross of costs (buffering would curb the extra trading from vol scaling)
- Stop parameters not optimised, tuned by eye on one instrument
- Trade-level and return-level skew differ a lot, so conclusions depend on measurement frequency

**Reasoning:** Vol scaling shrinks positions in high vol, which trims exposure to big trending winners, lowering skew but raising Sharpe. Dynamic stops cut losers fast and lift trade skew but close positions early and sharply lower Sharpe. The effects roughly offset when combined, a no-free-lunch trade-off.

> the market does not know what my position is or has been, or how much profit I've made.
^B21

## B22 Vol targeting: a CAgR race
[2022-06-27](https://qoppac.blogspot.com/2022/06/vol-targeting-cagr-race.html) · 2022-06-27 · topic: vol targeting vs fixed-size trend following; compounding and skew

**Rules:**
- Compare fixed-size one-entry-one-stop (1E1S), fixed-size reverse-on-signal (1E1E), binary vol-targeted with buffering (BV) and continuous-forecast vol-targeted with buffering (FV, 20% stdev target) on about 100 futures, EWMAC 8,32 / 16,64 / 32,128 / 64,256 and an equal-weighted combination, at the CAGR-maximising leverage rather than equal Sharpe
- No fitting
**Numbers:**
- At leverage 1 (combined EWMAC): CAGR FV 25.8%, BV 19.7%, 1E1E 19.3%, 1E1S 11.3%; Sharpe FV 1.18, BV 1.15, 1E1S and 1E1E 0.88; monthly skew FV 1.41, BV 0.78, 1E1S 1.98
- CAGR-optimal leverage is about 5x (FV), 7x (BV), 6x (1E1S), 3x (1E1E), implying 60-120% annualised vol, not practical
- At a 30% vol target: FV 36.0%, BV 35.2%, 1E1S 25.7%, 1E1E 25.1%
- Slow rule EWMAC512 CAGR: FV 7.1%, BV 8.2%, 1E1S 3.6%, 1E1E -1.4%
**Caveats:**
- Backtests with assumed costs (costs would need to be about 8x higher to reverse the result)
- Depends on author's rules and instruments
- Skew is unstable, especially for 1E1E; slow rules have few independent observations
- At 6x leverage 1E1S has a 100%+ loss day (ruin risk)

**Reasoning:** CAGR depends on mean and variance; positive skew helps and negative skew hurts compounding at high leverage. Vol targeting's Sharpe advantage outweighs its modest skew disadvantage across sensible risk levels, and only reverses at extreme leverage.
^B22

## B23 Risk targeting and dynamic asset allocation: absolute or relative momentum?
[2019-03-27](https://qoppac.blogspot.com/2019/03/risk-targeting-and-dynamic-asset.html) · 2019-03-27 · topic: asset-allocation momentum; absolute vs relative; risk targeting

**Rules:**
- Strategic risk weights 75:25 US equities:US bonds (about 60:40 cash weights), vol from trailing 12 months of monthly returns
- Relative momentum: tilt weights toward the asset with the higher trailing 12-month risk-adjusted return, tilt capped at 148% and floored at 60% of strategic weight, always fully invested
- Absolute momentum: tilt each asset on its own trailing 12-month risk-adjusted return, can be under-invested (min 60%, average 93%)
- Monthly rebalancing, Jan 1954 to Mar 2016, excess returns
**Numbers:**
- Arithmetic mean / stdev / Sharpe: fixed 8.37% / 8.14% / 1.03; relative 9.26% / 8.62% / 1.07; absolute 8.93% / 7.96% / 1.12
- Average equity cash weight 61% fixed, 67% absolute, 70% relative
- For about 8% stdev the needed strategic equity risk weights are roughly 75% (fixed), 68% (absolute), 40% (relative)
**Caveats:**
- The extra risk in relative momentum comes from past data and may not persist (least robust finding)
- Sharpe differences may not be significant; single backtest
- Tail drawdowns not analysed; author considers drawdown a poor risk measure under parameter uncertainty

**Reasoning:** Both tilt exposure toward recent risk-adjusted winners. Absolute momentum can hold less than full exposure when trends are weak, lowering vol; relative momentum stays fully invested, and its higher return partly reflects an implicit tilt that raises risk (more equity), so risk-target before comparing.

> Absolute momentum is a super popular asset allocation methodology, because people like the 'downside protection'
^B23

## B24 Should we trade momentum differently when vol changes?
[2021-03-04](https://qoppac.blogspot.com/2021/03/does-it-make-sense-to-change-your.html) · 2021-03-04 · topic: forecast attenuation by volatility regime; trend rule performance

**Rules:**
- Normalised vol = current EW daily % vol (about one month) divided by its own 10-year (2,500-day) rolling mean, lagged one day; regimes by backward-looking quantiles (bottom 25% low, middle 50% medium, top 25% high)
- Attenuate forecasts by multiplier L = 2 - 1.5Q, Q = vol percentile (0 to 1), smoothed with 10-day EWMA, forecasts capped at +/-20
- Applied to EWMAC 2_8 to 64_256 and carry
**Numbers:**
- In high vol, fast momentum underperforms slow more than usual and returns of all rules fall; Medium vs High difference p about 0.00 for every EWMAC, carry p = 0.32
- Net Sharpe before -> after attenuation: 2_8 0.43->0.52; 4_16 0.78->0.83; 8_32 0.96->1.00; 16_64 1.01->1.07; 32_128 1.02->1.07; 64_256 0.96->1.00; carry 1.07->1.11
- Paired t-test p: 2_8 0.00002; 4_16 0.014; 8_32 0.059; 16_64 0.018; 32_128 0.040; 64_256 0.086; carry 0.176
- With a 3-day lag the Medium-vs-High p-values rise to about 0.01-0.14 (Low-vs-High stays 0.00)
**Caveats:**
- Regime cutoffs and smoothing chosen by judgement
- Effect weakens with a realistic 3-day lag; gains modest and not significant for 64_256 and carry
- t-tests treat pooled daily observations as independent despite overlap and autocorrelation
- Backtest of author's own data, motivated by the 2020 crisis

**Reasoning:** Momentum and carry degrade when vol is high, more so for faster rules. The pattern persists without costs so it is not just a cost story. No mechanism was established; commenters suggested vol mean reversion whipsawing fast systems.

> To return to the original question: yes we should change our trading behaviour as vol changes.
^B24

## B25 Is the degradation of trend following a cohort, instrument or environment effect?
[2025-10](https://qoppac.blogspot.com/2025/10/is-degradation-of-trend-following.html) · 2025-10 · topic: trend decay

**Rules:**
- Group instruments by data start decade; compare rolling 5y average SR per cohort, EWMAC 2,8 to 64,256 and carry, pre-cost
**Numbers:**
- Strategy nine non-compounded return >500% in 1970s, >200% each next three decades, average return roughly halved since 2010
- 1972 start with 11 instruments; ~100 instruments in test list
- 1991 cohort 7 instruments
**Caveats:**
- Pre-cost
- Small cohorts
- Pre-1990 cost adjustment uncertain; fast trend may never have worked as well as backtests suggested

**Reasoning:** No cohort effect (old instruments not better); weak instrument decay in 1991 cohort; decline across all speeds looks environmental, so restricting to older/newer instruments cannot fix it. Carry shows slightly more instrument decay.

> Overall though, this does look an enviroment effect with noise.
^B25

## B26 Scream if you want to go faster (costs vs optimal momentum speed)
[2023-01-05](https://qoppac.blogspot.com/2023/01/scream-if-you-want-to-go-faster.html) · 2023-01-05 · topic: trading speed / costs

**Rules:**
- Slow down as instruments get more expensive: pre-cost optimal speed is flat across costs
- Speed limit: annual cost (turnover x SR cost per trade) <= 0.13 SR units
- Cost ceiling ~0.007-0.01 SR units per trade to trade at all
**Numbers:**
- 160 instruments, EWMAC2-64
- Turnover approx EWMAC2 42, 4 20, 8 9, 16 3.8, 32 2.3, 64 2.1
- All six rules need cost <0.00283; EWMAC64 alone <0.021
- Optimal speed net ~3.5 cheapest vs ~5 costliest (scale 1-6)
- Gross SR vs cost R2 0.075 fastest rule
**Caveats:**
- Low R2, noisy
- Roll turnover ignored
- Optimal-speed heuristic

**Reasoning:** No-free-lunch is wrong: gross performance does not rise enough with cost; post-cost, expensive instruments do worse even traded slowly, so penalise their weights.

> Broadly speaking it is correct that pre-cost optimal speed is flat, and therefore we should slow down as instruments get more expensive to trade.
^B26

## B27 Fast but not furious: smuggling in fast rules via buffering and dynamic optimisation
[2023-02](https://qoppac.blogspot.com/2023/02/fast-but-not-furious-do-fast-trading.html) · 2023-02 · topic: trading speed / costs / execution

**Rules:**
- Use fast rules only conditionally (cheap instruments); bar expensive instruments from trading under DO; buffering + cost penalty cut turnover
**Numbers:**
- S&P500 turnover forecast/raw/buffered: EWMAC4 61.8/52.6/49.8, EWMAC64 7.46/10.16/7.04
- DO cuts turnover roughly half to two-thirds
- Conditional approach costs ~1bp more than slow system; all-rules-everywhere ~50% more than conditional
- Slow vs fast benchmark correlation ~0.80
- Speed limit 0.13 SR; IDM ~2.0
**Caveats:**
- Constant capital backtests
- Omits vol attenuation and risk overlay
- Fast/slow regression labels possibly swapped in source

**Reasoning:** Buffering and DO give headroom under the speed limit; simply adding more fast momentum does not diversify much.

> Good news: all of this is a confirmation that what I'm currently doing* is probably pretty optimal!
^B27

## B28 Three kinds of overfitting
[2015-11](https://qoppac.blogspot.com/2015/11/the-three-kinds-of-overfitting.html) · 2015-11 · topic: research method / overfitting

**Rules:**
- Explicit fitting: restrict degrees of freedom (A<B, B=4A, powers of two, pooled parameters), expanding/rolling out-of-sample, robust tilts not wholesale reallocation
- Implicit fitting: record every idea tested; correct significance for trials
- Tacit fitting (hindsight priors) is hard: widen parameter space
**Numbers:**
- Free A,B in 1-256 gives 65,280 combinations per instrument
- Eurodollar 30y: optimum A=10,B=20; Mexican peso: few years, optimum indistinguishable
**Caveats:**
- SR used as illustrative metric

**Reasoning:** Incentives push toward overfitting; explicit fitting can be done properly, implicit and tacit are the real dangers.

> The good news about explicit fitting is that it's possible to do it properly.
^B28

## B29 Optimisation with costs (2026 series #11)
[2026-11-04](https://qoppac.blogspot.com/2026/11/optimisation-with-costs-oh-please.html) · 2026-11-04 · topic: forecast and instrument weights / costs

**Rules:**
- Cap SR cost at 0.01 in optimisation; exclude instruments above 0.01 SR cost from DO trading
- Pool gross returns (instrument, asset class, global), net off each instrument's own costs
- Shrink SR 0.5 and correlations 0.75 (more if <5y data); cluster size 6; 30y expanding then rolling window
**Numbers:**
- S&P500 0.00025, Cheese 0.008, Sugar#16 0.09 SR per trade
- 40y EMA ~ 28y SMA
**Caveats:**
- No backtest in post (design discussion)
- 0.01 cliff edge acknowledged as distasteful

**Reasoning:** Gold standard: rolling out-of-sample wrapper -> pooled gross returns -> clustering -> shrinkage with cost deduction. DO alone does not fully slow expensive instruments, so costs belong in the weight optimisation.

> But my previous research found that DO isn't completely effective at reducing the trading speed of expensive instruments.
^B29

## B30 Very slow mean reversion and trading horizons
[2025-03](https://qoppac.blogspot.com/2025/03/very-slow-mean-reversion-and-some.html) · 2025-03 · topic: horizons / mean reversion

**Rules:**
- Horizon map: >2y relative/value mean reversion works; 1-2y avoid; 3m-1y slow trend; 3w-3m best trend SR; days-3w cheap instruments only; hours-days avoid
**Numbers:**
- Slow absolute mean reversion (3y price change, vol scaled, EWM64): portfolio SR -0.48, median instrument -0.06 (data mostly 2013+)
- Trend optimal holding ~3 weeks, median instrument SR ~0.30
- Predictability ~6.5% at 3w vs ~1.8% at 2d
- Median future cost ~20x cheapest -> needs ~2 week holding for speed limit
- AFTS mean-reversion backtest SR >2 was an error; corrected ~no significant return
**Caveats:**
- Hourly data at best
- Single construction, short sample
- Own backtest error shows fragility of fast tests

**Reasoning:** Markets trend and mean-revert at different frequencies; absolute slow mean reversion failed in his test.

> The golden thread connecting them is the idea that markets trend and mean revert at different frequencies.
^B30

## B31 Vol targeting and trend following
[2018-07](https://qoppac.blogspot.com/2018/07/vol-targeting-and-trend-following.html) · 2018-07 · topic: vol targeting / skew

**Rules:**
- Keep vol targeting: removing it raises skew but costs about a third of SR
**Numbers:**
- 37 futures, after costs, monthly: with VT skew +1.08, SR 0.92, kurtosis 5.28; without VT skew +2.46, SR 0.569, kurtosis 33.0
- From 1981: SR 0.78 vs 0.52, skew 0.45 vs 0.64
- t-stat on SR difference 3.59
**Caveats:**
- Skew driven by 1979-80 outliers
- Backfilled slow vol has look-ahead early
- One system

**Reasoning:** Vol targeting removes some positive skew, but the Sharpe cost is large; cheaper skew sources exist (OTM straddles).

> But the cost is terribly high: about a third of our Sharpe Ratio!
^B31

