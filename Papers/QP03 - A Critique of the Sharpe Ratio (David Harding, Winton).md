---
source_id: QP03
title: "A Critique of the Sharpe Ratio (David Harding, Winton)"
type: paper
claims: 23
opus_only: 6
tags: [paper, layer0]
---
# A Critique of the Sharpe Ratio (David Harding, Winton)

**Authors:** David Harding (Winton Capital Management)

**Summary:** Question: why should the Sharpe ratio not be used as the universal measure of strategy quality. Method: conceptual critique (stationarity, parametricity, perverse incentives, examples), no data. Conclusion: use Sharpe cautiously, check stationarity, prefer semi-variance and long-term return under a risk constraint.

## Argument map

**Question:** Is the Sharpe ratio a valid universal measure of strategy quality, and what goes wrong when investors and managers optimise to it?

**Thesis:** The Sharpe ratio is only meaningful for stationary, parametric return processes and even then penalises upside and rewards tiny consistent returns; its indiscriminate use leads managers to game it, so investors should use several measures, semi-variance and long-term return under a risk constraint. ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-4|C01-4]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-2|C01-2]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-3|C02-3]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-5|C02-5]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-8|C02-8]])

### Foundations (premises)
- Return is observable; risk is not directly observable. _[theoretical, stated; support: argument]_ ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-3|C01-3]])
- Standard deviation measures risk only for stationary, parametric return processes. _[theoretical, stated; support: statistical reasoning; Cauchy example]_ ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-4|C01-4]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-8|C01-8]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-11b|C01-11b]])
- Managers respond to what investors reward. _[behavioural, stated; support: practitioner experience; Goetzmann et al.]_ ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-2|C01-2]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-7|C02-7]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-9|C01-9]])

### Mechanism chain
- 1. investors rank managers by Sharpe and overvalue short-run consistency → managers maximise Sharpe: incentives _[assertion]_ ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-2|C01-2]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-7|C02-7]])
- 2. Sharpe maximisation → negative-skew, smoothed or option-like return streams: short-option payoffs, illiquid marking and take-profit/run-loss rules raise measured Sharpe _[citation]_ ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-9|C01-9]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-9|C01-9]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-1b|C02-1b]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-2|C02-2]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-1|C02-1]])
- 3. non-stationary / non-parametric returns → misleading Sharpe ratios and hidden tail risk: sd no longer describes the risk _[assertion]_ ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-4|C01-4]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-5|C01-5]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-7b|C01-7b]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-8|C01-8]])
- 4. symmetric sd → upside-volatile dynamic strategies are penalised: large gains counted as risk _[example]_ ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-3|C02-3]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-3|C02-3]])

### Design rationale
- **Use downside semi-deviation (Sortino) instead of sd**: does not penalise large positive returns. Alternatives: Sharpe ratio. Sensitivity: not shown; still needs stationarity ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-4|C02-4]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-7b|C02-7b]])
- **Rolling sd / mean diagnostics before computing statistics**: reveal non-stationarity from style or leverage changes. Alternatives: . Sensitivity: window not given ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-6|C01-6]])
- **Long-term return subject to a risk constraint as a quality statistic**: Sharpe can favour tiny riskless returns over meaningful returns. Alternatives: Sharpe, Sortino. Sensitivity: not shown ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-6|C02-6]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-8|C02-8]])

### Evidence map
- Removing the highest returns can raise Sharpe. Tests: step 4. Rules out: Sharpe as a universal quality metric. Does not rule out: . Strength: strong - mathematical ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-3|C02-3]])
- Serial correlation overstates Sharpe in illiquid strategies (Asness et al.; Lo). Tests: step 2. Rules out: . Does not rule out: . Strength: moderate - cited, no own data ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-1|C02-1]])
- Option-like strategies engineer high Sharpe without skill (Goetzmann et al.). Tests: step 2. Rules out: . Does not rule out: . Strength: moderate - cited ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-9|C01-9]])

### Regimes
- Before a tail event in negative-skew strategies → Sharpe looks high; after the event it collapses ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-9|C01-9]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-1b|C02-1b]])
- Manager AUM growth → strategy changes and early record is unrepresentative ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-6b|C01-6b]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-7b|C01-7b]])

### Gaps and conflicts
- [unspecified] No empirical data, no thresholds for "reasonable stationarity", no rolling window length ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-6|C01-6]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-7|C01-7]])
- [unspecified] Recommended "long-term return subject to some risk constraint" is not defined ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-8|C02-8]])
- [untested] Sortino has the same stationarity requirement, so the fix is partial by the author's own logic ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-7b|C02-7b]])

### Relations to other strategies
- trend following (positively skewed): **complement**. (reader) trend has upside volatility that Sharpe penalises, the opposite of take-profit/run-loss strategies ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-2|C02-2]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-3|C02-3]])
- carry / short-volatility strategies: **contradicts**. negative-skew strategies show high Sharpe until the crash ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C01-9|C01-9]], [[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-1b|C02-1b]])
- Lo (2002) autocorrelation-adjusted Sharpe: **complement**. corrects for smoothing ([[QP03 - A Critique of the Sharpe Ratio (David Harding, Winton)#^QP03-C02-1|C02-1]])

### Forward-looking inputs (reader synthesis)
(reader) Not a signal paper. For evaluating any macro backtest it implies: check rolling volatility/mean for stationarity, return autocorrelation (smoothing), skewness and tail losses, and upside vs downside deviation; a high Sharpe from a negatively skewed or smoothed series should be discounted. This stops mattering only if returns are close to i.i.d. normal.

### Reader inferences (not stated by the authors)
- (reader) The critique implicitly favours positively skewed strategies such as trend following (Winton is a trend follower), which the Sharpe ratio understates.
- (reader) Practical adoption rule for a macro book: report Sortino, skew, max drawdown and autocorrelation-adjusted Sharpe alongside Sharpe.
- (reader) The 1%-mean/1%-sd example has a monthly Sharpe of 1, so it is the infinite-Sharpe riskless case that the Sharpe ratio would prefer.

## Claims

### C01 (page 1)
- The Sharpe ratio (mean excess return over standard deviation, devised 1966 for mutual funds) has some value as a quality measure but crucial limitations. _(caveat, premise)_ #mech/research_method
  > it undoubtedly has some value as a measure of strategy “quality”, but it also has several crucial limitations
  exact_rule: Sharpe = average period return in excess of the risk-free rate / standard deviation of returns
  ^QP03-C01-1
- Indiscriminate use of Sharpe as the quality measure distorts priorities because firms manipulate strategies and data to maximise it. _(mechanism, premise)_ #mech/behavioral
  > its widespread and often indiscriminate adoption as a quality measure is leading to distortion of proper investment priorities, as investment firms manipulate strategies and data to maximise it.
  conditions: Incentive effect when Sharpe is the target metric
  ^QP03-C01-2
- Core objection: return is observable but risk is not; standard deviation can be computed on any series but does not mean the same thing across series. _(mechanism, premise)_ #mech/research_method
  > whilst return is a definite and meaningful quantity (an “observable”), risk is not.
  ^QP03-C01-3
- Standard deviation is only a meaningful risk statistic if the return process is stationary (constant variance, skew, kurtosis) and parametric (a distribution with parameters of known meaning). _(mechanism, premise)_ #mech/research_method
  > the return time series must be generated from a process that is both stationary and parametric.
  exact_rule: precondition: stationary AND parametric return process
  ^QP03-C01-4
- Track records are commonly non-stationary because style or leverage changes, early records on small assets (exploiting anomalies, 'swinging for the bleachers') differ from later ones, and growing AUM forces strategy change. _(mechanism, mechanism_step)_ #mech/structural_shift
  > A common violation of this in track records occurs when a manager’s style or leverage changes over the course of their history.
  conditions: Small-AUM early record vs large-AUM later record
  ^QP03-C01-5
- Proposed check: rolling standard deviation (or rolling average period change) through time reveals non-stationarity. _(implementation, design_choice)_ #mech/research_method
  > A simple test of rolling standard deviation through time (or even average period change) may be sufficient to uncover the manifestations of the resulting non-stationarity.
  exact_rule: compute rolling standard deviation and rolling mean of period changes over the track record; look for drift · data_needed: manager or strategy return series · conditions: Window length not specified
  ^QP03-C01-6
- Zero style drift is too demanding; the standard is reasonable stationarity before computing statistics. _(caveat, qualifier)_ #mech/structural_shift
  > It is probably too demanding to ask that a manager’s record show no style drift at all; markets are dynamic things and some change over time is unavoidable.
  ^QP03-C01-7
- Non-stationary distributions are non-parameterisable, so standard deviation conveys no information; Cauchy-Paretian distributions have infinite variance and would not be assessed well by Sharpe. _(mechanism, mechanism_step)_ #mech/research_method
  > In a non-parameterisable distribution, it conveys no information about anything. Non-stationary distributions are non-parameterisable.
  ^QP03-C01-8
- Strategies with many small gains and rare large losses (short-volatility style, merger arbitrage, LTCM) look excellent on Sharpe until the loss arrives; footnote 1 cites Goetzmann et al. 2002 on option-like strategies engineering high Sharpe without skill. _(mechanism, mechanism_step)_ #mech/risk_premium
  > some will produce many small profits and the occasional large loss - before the loss has appeared such strategies will have a high Sharpe ratio!
  exhibit: footnote 1 · conditions: Before the tail loss appears; short-sample track records
  ^QP03-C01-9
- Early track records often differ from later ones because a small manager can exploit a good anomaly or take big risks with little to lose. _(mechanism, mechanism_step, Opus only)_ #mech/new
  > It is common for a manager’s early track record to differ significantly from later performance
  ^QP03-C01-6b
- Asset growth constrains capacity and almost inevitably changes the strategy, making the return process non-stationary. _(implementation, mechanism_step, Opus only)_ #mech/new
  > An increase in assets under management can enforce constraints on such opportunities, leading almost inevitably to a change in investment strategy.
  ^QP03-C01-7b
- Fat-tailed (Cauchy-Paretian) return processes have infinite variance, so the Sharpe ratio cannot assess them. _(caveat, qualifier, Opus only)_ #mech/research_method
  > Cauchy-Paretian distributions have infinite variance
  ^QP03-C01-11b

### C02 (page 2)
- Serial correlation in monthly returns of illiquid strategies (e.g. convertible arbitrage) substantially overstates Sharpe ratios (Asness, Krail, Liew 2001; Lo 2001). _(citation, mechanism_step)_ #mech/liquidity_flows
  > while the serial correlation of monthly returns common in the more illiquid hedge fund strategies (e.g. convertible arbitrage) can lead to a substantial overstatement of Sharpe ratios (Asness et al. 2001; Lo 2001).
  conditions: Illiquid, smoothed-return strategies
  ^QP03-C02-1
- Strategies that take profits quickly and let losses run (negative skew) flatter Sharpe. _(mechanism, mechanism_step)_ #mech/behavioral
  > Some trading approaches which are swift to take profit but run losses may also twist the statistics to their advantage
  ^QP03-C02-2
- Standard deviation penalises large positive returns, so removing a strategy's best returns can raise its Sharpe ratio, which Harding calls a reductio ad absurdum, and which matters for positively skewed (trend-like) dynamic strategies. _(mechanism, mechanism_step)_ #mech/research_method
  > large positive returns increase the perception of risk as though they could as easily be negative, which for a dynamic investment strategy may not be the case.
  conditions: Positively skewed dynamic strategies
  ^QP03-C02-3
- Replacing standard deviation by negative semi-standard deviation (Sortino) is a partial fix, still requiring stationarity and parametricity. _(implementation, design_choice)_ #mech/research_method
  > We might suggest an improvement by considering only the negative semi-standard deviation for the denominator, a measure known as the Sortino ratio.
  exact_rule: Sortino-type ratio: excess return / downside (negative) semi-standard deviation · conditions: Semi-deviation must come from a well-understood stationary distribution
  ^QP03-C02-4
- Very small but consistent profits (e.g. AAA commercial paper slightly above risk-free) give a very high Sharpe with little return and say nothing about skill; this may not be caught by other tests even in a long sample. _(mechanism, mechanism_step)_ #mech/research_method
  > a string of very small but consistent profits which will produce a very high Sharpe ratio with very little return.
  conditions: Low-volatility, low-return instruments
  ^QP03-C02-5
- Illustration: 0.01% per month over risk-free would have a far higher Sharpe than 1% with 1% standard deviation, yet few would prefer it, so raw return still matters. _(result, evidence)_ #mech/research_method
  > Who would prefer to make 0.01% over risk-free each month rather than 1% with a standard deviation of 1%?
  reported_result: Hypothetical: 1% monthly return with 1% sd (monthly Sharpe 1.0) vs 0.01% per month over risk-free (no sd given); no empirical numbers · conditions: Hypothetical, no empirical data
  ^QP03-C02-6
- Author asserts the Sharpe distortions are practical, reflected in investors overvaluing short-run consistent returns and biased return-generating processes. _(mechanism, evidence)_ #mech/behavioral
  > They are all mirrored in the (faulty) decision-making processes of investors who overvalue short run consistent returns and biased return-generating processes.
  ^QP03-C02-7
- Recommended remedies: check stationarity and parametricity, use flexibly designed quality statistics, prefer semi-variance to variance as the risk measure, and revive long-term return subject to a risk constraint as the quality statistic. _(implementation, conclusion)_ #mech/research_method
  > Suggested solutions include paying more attention to stationarity and parametricity in making estimates of future return and risk from manager track records;
  exact_rule: evaluate strategies by long-term return subject to a risk constraint; use semi-variance; test stationarity/parametricity · conditions: No numeric thresholds or backtests given
  ^QP03-C02-8
- Merger arbitrage and similar strategies have short-option-like return distributions exposed to rare cataclysms, as LTCM showed. _(mechanism, evidence, Opus only)_ #mech/risk_premium
  > sorts of distribution, vulnerable, like LTCM, to a major cataclysm.
  ^QP03-C02-1b
- The Sortino ratio still requires a stationary, well-understood distribution to be meaningful. _(caveat, qualifier, Opus only)_ #mech/research_method
  > it still remains vital that the semi-standard deviation used is meaningful
  ^QP03-C02-7b
- No single statistic should be relied on to judge risky strategies. _(caveat, conclusion, Opus only)_ #mech/research_method
  > the danger of relying slavishly on any single measure for assessing product quality for risky investments.
  ^QP03-C02-11b

