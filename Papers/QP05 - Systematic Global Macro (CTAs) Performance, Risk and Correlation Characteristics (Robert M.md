---
source_id: QP05
title: "Systematic Global Macro (CTAs): Performance, Risk and Correlation Characteristics (Robert Murray, Graham Capital Management)"
type: paper
claims: 24
opus_only: 2
tags: [paper, layer0]
---
# Systematic Global Macro (CTAs): Performance, Risk and Correlation Characteristics (Robert Murray, Graham Capital Management)

**Authors:** Robert E. Murray (Graham Capital Management)

**Summary:** Question: do systematic global macro programs (CTAs) diversify traditional and hedge fund portfolios. Method: Jan 1994-Dec 2008 monthly Barclay Systematic Traders Index vs S&P/EAFE/T-bond and CSFB/Tremont indices: correlations, conditional correlations, stress months, skew/kurtosis, autocorrelation, optimized portfolios. Conclusion: CTAs show low or negative correlation, positive convexity and no smoothing bias, so they improve portfolio ratios.

## Argument map

**Question:** Why should a hedge fund or traditional portfolio allocate to systematic global macro (CTAs), and do standard statistics capture their benefit?

**Thesis:** CTAs (BSTI) have low or negative correlation to equities and hedge fund styles, positive returns in crisis months, positive skew and no return smoothing; once autocorrelation is accounted for, their risk-adjusted return is better and other styles worse, so optimised hedge fund portfolios should hold CTAs at the maximum weight. ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C02-2|C02-2]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C04-1|C04-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C06-1|C06-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C08-1|C08-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C11-1|C11-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C12-2|C12-2]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C13-1|C13-1]])

### Foundations (premises)
- Smoothed (autocorrelated) monthly returns understate true volatility; correcting for it is needed for fair comparison. _[theoretical, stated; support: statistical identity]_ ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C09-1|C09-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C09-1|C09-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C09-2|C09-2]])
- Investors value diversification most in down markets, so conditional (down-month) correlation and stress returns matter. _[assumed, implicit; support: shown through conditional tables]_ ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C04-1|C04-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C05-1|C05-1]])
- Negative skew and fat tails are undesirable risks hidden by mean-variance statistics. _[theoretical, implicit; support: definitions plus table]_ ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C07-1|C07-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C07-1|C07-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C08-1|C08-1]])
- BSTI is a fair proxy for systematic global macro. _[assumed, implicit; support: none]_ ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C04-1|C04-1]])

### Mechanism chain
- 1. CTAs trade liquid futures marked daily → no return smoothing (autocorrelation ~0): (reader) liquid pricing; authors only show the statistic _[test]_ ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C10-1|C10-1]])
- 2. illiquid hedge fund styles → smoothed returns, understated vol, overstated IR: positive autocorrelation raises annual vol _[test]_ ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C09-1|C09-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C10-1|C10-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C11-1|C11-1]])
- 3. equity / liquidity crises → other styles fall together, CTAs gain or are flat: (reader) trends develop in crises; authors show outcomes only _[test]_ ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C04-1|C04-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C05-1|C05-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C06-1|C06-1]])
- 4. adjusted statistics → optimiser assigns maximum weight to CTAs: diversification and better adjusted IR _[test]_ ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C12-1|C12-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C12-2|C12-2]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C13-1|C13-1]])

### Design rationale
- **Adjust IR for statistically significant monthly autocorrelation**: needed to measure annual volatility accurately. Alternatives: naive sqrt(12) scaling. Sensitivity: changes IR by -0.56 to +0.21; changes optimal weights ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C09-2|C09-2]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C11-1|C11-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C12-2|C12-2]])
- **Conditional up/down-month correlations**: not given (implied: diversification matters in down markets). Alternatives: unconditional correlation. Sensitivity: BSTI -0.15 all vs -0.31 down ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C04-1|C04-1]])
- **Optimise with several objectives (IR, adjusted IR, Calmar, Sortino) and weight bounds**: different risk/return ratios. Alternatives: four objectives compared. Sensitivity: BSTI weight 14-20%; others shift ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C12-1|C12-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C13-1|C13-1]])

### Evidence map
- BSTI corr -0.15 with S&P, -0.31 in down months. Tests: diversification premise. Rules out: CTAs as hidden equity beta in 1994-2008. Does not rule out: (reader) sample dominated by 2000-02 and 2008 bear markets where trend was short equities; results could differ in V-shaped crashes. Strength: moderate - 15 years, one index ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C03-1|C03-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C04-1|C04-1]])
- Positive BSTI in 15 of 19 S&P stress months and in worst HF months. Tests: crisis alpha. Rules out: . Does not rule out: (reader) selection of stress months not defined; small sample. Strength: moderate ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C05-1|C05-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C06-1|C06-1]])
- BSTI skew +0.22, kurtosis 0.18 vs arbitrage strategies strongly negative skew. Tests: tail-risk premise. Rules out: . Does not rule out: (reader) EMN -12 skew driven by one month (Nov 2008, likely index-specific event). Strength: moderate ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C08-1|C08-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C08-1|C08-1]])
- Autocorrelation adjustment lifts BSTI IR 0.72 to 0.93 and cuts others. Tests: smoothing premise. Rules out: . Does not rule out: (reader) the BSTI lift with lag-1 rho -0.01 must come from other lags; lags/significance rule not given. Strength: moderate ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C11-1|C11-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C10-1|C10-1]])
- Optimised portfolios put 14-20% in BSTI. Tests: allocation conclusion. Rules out: . Does not rule out: (reader) entirely in-sample optimisation with bounds; no out-of-sample test. Strength: weak - in-sample ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C12-2|C12-2]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C13-1|C13-1]])

### Regimes
- S&P 500 down months → CTA correlation turns more negative; other styles more positive ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C04-1|C04-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C04-2b|C04-2b]])
- Liquidity crises (Aug/Oct 1998, Oct/Nov 2008) → CTAs positive or flat while arbitrage styles lose 10-40% ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C06-1|C06-1]])
- Some stress months (Aug 1997, Sep 2000, Feb 2001, Apr 2002, Oct 1998) → CTAs also lost, modestly ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C05-1|C05-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C06-1|C06-1]])

### Gaps and conflicts
- [conflict] BSTI lag-1 autocorrelation is -0.01 yet its IR rises by 0.21 after adjustment; which lags and significance test were used is not stated ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C10-1|C10-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C11-1|C11-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C09-2|C09-2]])
- [unspecified] Stress-month selection rule for slide 5 not defined ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C05-1|C05-1]])
- [unspecified] Optimiser constraints (apparent 4%-20% bounds), return/risk inputs and benchmark for IR not stated; Multi-Strategy appears only in the optimisation ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C12-1|C12-1]])
- [data] "Positive annual returns for more than 20 years" has no index or data shown ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C02-1|C02-1]])
- [data] Hedge fund indices have survivorship/backfill biases; deck is marketing material from a CTA ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C01-1|C01-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C04-1|C04-1]])

### Relations to other strategies
- hedge fund arbitrage styles (carry-like, short-volatility): **complement**. CTAs positively skewed and uncorrelated; arbitrage styles negatively skewed ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C08-1|C08-1]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C03-2|C03-2]])
- Sharpe ratio critique (serial correlation, skew): **complement**. applies the autocorrelation and skew corrections to strategy comparison ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C09-2|C09-2]], [[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C11-1|C11-1]])
- discretionary global macro: **complement**. only 0.37 correlation with BSTI ([[QP05 - Systematic Global Macro (CTAs) Performance, Risk and Correlation Characteristics (Robert M#^QP05-C03-2|C03-2]])

### Forward-looking inputs (reader synthesis)
(reader) No forecasting signal. The deck implies conditioning allocation on equity drawdowns is unnecessary because CTAs are naturally convex; for evaluating a macro book, measure down-month correlation, skew and autocorrelation-adjusted IR. The diversification would weaken in sharp V-shaped reversals or if CTA crowding raised correlation with equities.

### Reader inferences (not stated by the authors)
- (reader) The CTA crisis returns come from trend following (short equities / long bonds in prolonged bear markets), not stated in the deck.
- (reader) Weight bounds of 4%-20% are inferred from the weight table.
- (reader) The EMN Nov 2008 -40% is a single-index event that drives its -12 skew.
- (reader) Up/down months are presumably defined by the sign of the S&P 500 monthly return.

## Claims

### C01 (page 1)
- Title slide: Graham Capital marketing brochure, exempt from CFTC filing; CFTC has not reviewed the program; past performance not necessarily indicative of future results. _(caveat, qualifier)_ #mech/research_method
  > PAST PERFORMANCE IS NOT NECESSARILY INDICATIVE OF FUTUR
  conditions: Marketing document by an asset manager; claims are not independently audited
  ^QP05-C01-1

### C02 (page 2)
- Claimed benefit: positive annual returns for more than 20 years for systematic global macro (CTAs); stated without data and not matched to the 1994-2008 sample used in the exhibits. _(result, conclusion)_ #mech/slow_reaction
  > Positive annual returns for more than 20 years
  reported_result: Claim: positive annual returns for more than 20 years; no numbers · conditions: Unsupported on the slide; exhibits cover Jan 1994-Dec 2008
  ^QP05-C02-1
- Claimed benefit: low to negative correlation of systematic global macro to other asset classes and hedge fund strategies. _(result, conclusion)_ #mech/slow_reaction
  > Low to negative correlations to most other asset classes and hedge fund strategies
  exhibit: slide 2 summary; evidence on slides 3-4
  ^QP05-C02-2
- Claimed benefit: strong historical performance in crisis periods (evidence on slides 5-6); also managed accounts give more transparency. _(result, conclusion)_ #mech/slow_reaction
  > Strong historical performance during crisis periods
  exhibit: slide 2 summary; evidence on slides 5-6 · conditions: Managed accounts lead to increased transparency (a structural, not performance, claim)
  ^QP05-C02-3
- CTAs can be accessed via managed accounts, giving investors more transparency. _(implementation, context, Opus only)_ #mech/risk_management
  > Managed accounts lead to increased transparency
  ^QP05-C02-3b

### C03 (page 3)
- Barclay Systematic Traders Index (BSTI) has low or negative correlation with traditional assets: S&P 500 -0.15, MSCI EAFE -0.10, Lehman Brothers T-Bond Index 0.28 (S&P-EAFE 0.79, S&P-T-Bond -0.09, EAFE-T-Bond -0.12). _(result, evidence)_ #mech/slow_reaction
  > Low Correlation to Other Asset Classes VS. TRADITIONAL ASSET CLASSES Barclay Systematic Traders Index ("BSTI") S&P 500
  exact_rule: pairwise correlation of monthly returns, BSTI vs S&P 500, MSCI EAFE, Lehman T-Bond · data_needed: Barclay Systematic Traders Index; S&P 500; MSCI EAFE; Lehman Brothers T-Bond Index · reported_result: Jan 1994-Dec 2008 monthly, BSTI correlation with S&P 500 -0.15, MSCI EAFE -0.10, Lehman T-Bond 0.28; S&P 500 vs EAFE 0.79; S&P vs T-Bond -0.09; EAFE vs T-Bond -0.12 · exhibit: Exhibit slide 3 (Low Correlation to Other Asset Classes)
  ^QP05-C03-1
- BSTI correlation with CSFB/Tremont hedge fund indices is near zero for most (equity market neutral 0.01, fixed income arb -0.03, event driven -0.08, long/short 0.05, convertible arb -0.05, dedicated short 0.09, emerging markets -0.06) and 0.37 with global macro. _(result, evidence)_ #mech/slow_reaction
  > VS. ALTERNATIVE ASSET CLASSES Barclay Systematic Traders Index Barclay Systematic Traders Index ("BSTI") 1. 00 CSFB/Tremont Global M acro 0. 37
  exact_rule: pairwise correlation of monthly returns, BSTI vs eight CSFB/Tremont indices · data_needed: Barclay Systematic Traders Index; CSFB/Tremont hedge fund sub-indices · reported_result: Jan 1994-Dec 2008 monthly, BSTI vs Global Macro 0.37, Equity Market Neutral 0.01, Fixed Income Arbitrage -0.03, Event Driven -0.08, Long/Short Equity 0.05, Convertible Arbitrage -0.05, Dedicated Short Bias 0.09, Emerging Markets -0.06 · exhibit: Exhibit slide 3 (lower matrix) · conditions: Highest link is with discretionary global macro
  ^QP05-C03-2
- Among the hedge fund indices themselves correlations are high (event driven vs long/short 0.72, convertible arb vs fixed income arb 0.78, event driven vs emerging markets 0.70), while dedicated short bias is negative to most (long/short -0.68, convertible arb -0.23, emerging markets -0.53); BSTI is the least correlated of the group. _(result, evidence)_ #mech/crowding_positioning
  > CSFB/ Tremont Event Driven -0. 08 CSFB/ Tremont Long/Short Equity 0. 05
  reported_result: Jan 1994-Dec 2008 monthly, Event Driven-Long/Short 0.72; Convertible Arb-Fixed Income Arb 0.78; Event Driven-Emerging Markets 0.70; Long/Short-Emerging Markets 0.64; Dedicated Short Bias vs Long/Short -0.68, vs Event Driven -0.57, vs Emerging Markets -0.53; Global Macro vs Event Driven 0.42, vs Long/Short 0.47 · exhibit: Exhibit slide 3 (lower matrix) · conditions: Equity-beta-like hedge fund strategies cluster together
  ^QP05-C03-3

### C04 (page 4)
- BSTI correlation with the S&P 500 is -0.02 in up months, -0.31 in down months and -0.15 overall, i.e. it hedges more in equity down months, while most hedge fund strategies correlate more strongly with the S&P 500 in down months. _(result, evidence)_ #mech/slow_reaction
  > Conditional Correlations January 1994 – December 2008 Up Down All Months Months Months
  exact_rule: correlation of monthly BSTI (and each hedge fund index) with S&P 500 within S&P up months, down months, all months · data_needed: BSTI, CSFB/Tremont indices, S&P 500 monthly returns · reported_result: Jan 1994-Dec 2008 monthly, BSTI -0.02 (up), -0.31 (down), -0.15 (all); Global Macro 0.17/0.38/0.26; Equity Market Neutral 0.51/0.22/0.24; Fixed Income Arb 0.12/0.44/0.33; Event Driven 0.49/0.68/0.61; Convertible Arb 0.28/0.41/0.37; Long/Short 0.54/0.71/0.63; Dedicated Short -0.73/-0.74/-0.73; Emerging Markets 0.35/0.70/0.52 · exhibit: Exhibit slide 4 (Conditional Correlations) · conditions: Conditioning on the sign of the S&P month; hedge fund indices show correlation rising in down months
  ^QP05-C04-1
- Hedge fund styles such as event driven, long/short equity and emerging markets lose diversification when equities fall (down-month correlations 0.68-0.71). _(robustness, evidence, Opus only)_ #mech/risk_management
  > Correlation with S&P 500 Index
  reported_result: Down-month correlations: Event Driven 0.68, L/S Equity 0.71, EM 0.70, FI Arb 0.44 (vs up-month 0.49, 0.54, 0.35, 0.12) · exhibit: slide 4 · conditions: equity down months
  ^QP05-C04-2b

### C05 (page 5)
- In 19 listed S&P 500 stress months (S&P between about -5% and -17%, Aug 1997-Nov 2008), BSTI was positive in 15 and negative in 4 (Aug-97 about -4.7%, Sep-00 about -2.4%, Feb-01 about -0.5%, Apr-02 about -1.0%); large gains in Aug-98 (about +7.5%), Jun-02 (about +7.2%), Mar-01 (about +5.7%), Dec-02 (about +5.7%), Oct-08 (about +4.6%). _(result, evidence)_ #mech/slow_reaction
  > Performance During Stress Periods for S&P 500
  exact_rule: stress period = individual months of large S&P 500 loss (selection criterion not stated) · data_needed: S&P 500 total return; BSTI monthly returns · reported_result: 19 months labelled Aug-97, Aug-98, Jan-00, Sep-00, Nov-00, Feb-01, Mar-01, Aug-01, Sep-01, Apr-02, Jun-02, Jul-02, Sep-02, Dec-02, Jan-08, Jun-08, Sep-08, Oct-08, Nov-08; S&P 500 worst about -16.8% (Oct-08), -14.5% (Aug-98); BSTI Oct-08 about +4.6%, Aug-98 about +7.5%; values read from bar chart (approximate); BSTI positive in 15 of 19 · exhibit: Exhibit slide 5 (Performance During Stress Periods for S&P 500) · conditions: Months chosen by the author (rule undisclosed, appear to be S&P months below about -5%); not a full-sample test; 4 of 19 months were losses
  ^QP05-C05-1

### C06 (page 6)
- Aug 1998: Systematic Traders +7.51% while CSFB/Tremont Emerging Markets -23.03%, Event Driven -11.77%, Long/Short Equity -11.43%. _(result, evidence)_ #mech/slow_reaction
  > Performance during Stress Periods for Hedge Fund Strategies AUGUST 1998 15.00% Systematic Traders 7.51%
  reported_result: Aug 1998: Systematic Traders +7.51%; Emerging Markets -23.03%; Event Driven -11.77%; Long/Short Equity -11.43% (values read from chart labels) · exhibit: Exhibit slide 6 (Performance during Stress Periods for Hedge Fund Strategies) · conditions: Single selected stress month per strategy group
  ^QP05-C06-1
- Other stress months chosen per strategy: Oct 1998 Systematic Traders -1.01% vs Global Macro -11.55% and Dedicated Short Bias -8.69%; Oct 2008 +4.56% vs Fixed Income Arb -14.04% and Convertible Arb -12.59%; Nov 2008 +2.06% vs Equity Market Neutral -40.45%. _(result, evidence)_ #mech/slow_reaction
  > NOVEMBER 2008 OCTOBER 1998 OCTOBER 2008 Systematic Traders 4.56% Systematic Traders 2.06% Systematic Traders -1.01%
  reported_result: Oct 1998: ST -1.01%, Global Macro -11.55%, Dedicated Short Bias -8.69%; Oct 2008: ST +4.56%, Fixed Income Arb -14.04%, Convertible Arb -12.59%; Nov 2008: ST +2.06%, Equity Market Neutral -40.45% · exhibit: Exhibit slide 6 · conditions: The comparison month differs per hedge fund strategy, chosen to show each strategy's worst episode (selection effect)
  ^QP05-C06-2

### C07 (page 7)
- Definitions used for the later tail statistics: skew measures asymmetry (negative skew = thicker left tail); excess kurtosis measures tail thickness relative to a normal distribution (zero = normal tail frequency). _(construction, design_choice)_ #mech/research_method
  > Skew of zero indicates the distribution is symmetric; negative skew distributions have thicker left tails than right, with positive skew distributions having thinner left tails than right tails.
  exact_rule: skew and excess kurtosis of monthly return distribution · exhibit: Exhibit slide 7 (Skew & Kurtosis definitions) · conditions: Definitions only; no numbers
  ^QP05-C07-1

### C08 (page 8)
- BSTI return distribution is nearly symmetric and thin-tailed (skew 0.22, excess kurtosis 0.18) while hedge fund indices are negatively skewed and fat-tailed: Global Macro -0.03/3.04, Emerging Markets -0.74/4.64, Event Driven -2.70/14.79, Convertible Arb -3.56/19.58, Fixed Income Arb -4.63/29.96, Equity Market Neutral -12.02/155.46; Dedicated Short Bias 0.78/1.73, Long/Short 0.02/3.53. _(result, evidence)_ #mech/risk_premium
  > Skew & Kurtosis of Hedge Fund Strategies Standard Deviation from Mean (z-score)
  exact_rule: histogram of monthly returns in z-score buckets of width 2; skew and excess kurtosis · data_needed: Monthly returns of BSTI and eight CSFB/Tremont indices · reported_result: Jan 1994-Dec 2008 monthly, BSTI skew 0.22, excess kurtosis 0.18; Dedicated Short Bias 0.78/1.73; Global Macro -0.03/3.04; Long/Short 0.02/3.53; Emerging Markets -0.74/4.64; Event Driven -2.70/14.79; Convertible Arb -3.56/19.58; Fixed Income Arb -4.63/29.96; Equity Market Neutral -12.02/155.46 · exhibit: Exhibit slide 8 (Skew & Kurtosis of Hedge Fund Strategies)
  ^QP05-C08-1
- BSTI z-score histogram (180 months): 3 months in -4 to -2, 89 in -2 to 0, 80 in 0 to 2, 8 in 2 to 4, with none below -4; Equity Market Neutral has one month at -14 to -12 standard deviations, Fixed Income Arb one month at -10 to -8. _(result, evidence)_ #mech/risk_premium
  > 3 89 80 8 0.22 0.18
  reported_result: BSTI counts: 3, 89, 80, 8 across buckets (-4,-2),(-2,0),(0,2),(2,4); Equity Market Neutral 1 month at -14 to -12 z; Fixed Income Arbitrage 1 at -10 to -8, 2 at -6 to -4; Convertible Arb 2 at -8 to -6; Event Driven 1 at -8 to -6 · exhibit: Exhibit slide 8 (histogram cells) · conditions: Counts read from the exhibit; hedge fund index tails reflect single crisis months (1998, 2008)
  ^QP05-C08-2

### C09 (page 9)
- Positive monthly autocorrelation raises annual volatility above the root-12 scaling of monthly volatility and negative autocorrelation lowers it, so autocorrelation must be incorporated to measure annual volatility and risk-adjusted performance. _(mechanism, mechanism_step)_ #mech/research_method
  > Positive autocorrelation of monthly returns leads to an increased volatility of annual returns. Negative autocorrelation of monthly returns leads to a decreased volatility of annual returns.
  exact_rule: annual volatility adjusted for statistically significant monthly return autocorrelations (annualisation not specified) · exhibit: Exhibit slide 9
  ^QP05-C09-1
- Annual volatility should be measured with statistically significant monthly autocorrelations included, otherwise risk (and risk-adjusted ratios) of illiquid strategies is understated. _(construction, design_choice)_ #mech/research_method
  > Incorporating statistically significant autocorrelations of monthly returns is important to accurately measure annual volatility.
  exact_rule: include statistically significant autocorrelation terms when scaling monthly volatility to annual · exhibit: Exhibit slide 9
  ^QP05-C09-2

### C10 (page 10)
- BSTI has essentially zero one-month autocorrelation (-0.01) while most CSFB/Tremont hedge fund indices are positively autocorrelated (Convertible Arb 0.57, Fixed Income Arb 0.51, Event Driven 0.39, Emerging Markets 0.32, Long/Short 0.22, Global Macro 0.10, Dedicated Short 0.09, Equity Market Neutral 0.08). _(result, evidence)_ #mech/liquidity_flows
  > One Month Lag Autocorrelation January 1994 – December 2008 One Month Lag Autocorrelation: The correlation between one month’s return and the previous month’s return.
  exact_rule: lag-1 autocorrelation of monthly returns · data_needed: monthly returns of BSTI and eight CSFB/Tremont indices · reported_result: Jan 1994-Dec 2008 monthly, BSTI -0.01; Global Macro 0.10; Equity Market Neutral 0.08; Fixed Income Arb 0.51; Event Driven 0.39; Convertible Arb 0.57; Long/Short 0.22; Dedicated Short Bias 0.09; Emerging Markets 0.32 · exhibit: Exhibit slide 10 (One Month Lag Autocorrelation) · conditions: Positive autocorrelation in illiquid strategies (smoothing); read from table order, last two values assigned to Dedicated Short Bias and Emerging Markets
  ^QP05-C10-1

### C11 (page 11)
- Adjusting for autocorrelation raises the BSTI information ratio from 0.72 to 0.93 (+0.21) but lowers every hedge fund index's ratio: Global Macro 1.18 to 0.98, Event Driven 1.57 to 1.02, Convertible Arb 0.80 to 0.43, Fixed Income Arb 0.58 to 0.35, Long/Short 0.95 to 0.74. _(result, evidence)_ #mech/research_method
  > Autocorrelation & Volatility January 1994 – December 2008 Information Ratio Information Ratio Information disregarding incorporating Ratio Autocorrelation Autocorrelation Difference
  exact_rule: information ratio computed with and without autocorrelation-adjusted annual volatility · data_needed: monthly returns of BSTI and eight CSFB/Tremont indices · reported_result: Jan 1994-Dec 2008 monthly, BSTI 0.72 -> 0.93 (+0.21); Global Macro 1.18 -> 0.98 (-0.20); Equity Market Neutral 0.51 -> 0.43 (-0.08); Fixed Income Arb 0.58 -> 0.35 (-0.23); Event Driven 1.57 -> 1.02 (-0.56); Convertible Arb 0.80 -> 0.43 (-0.37); Long/Short 0.95 -> 0.74 (-0.21); Dedicated Short Bias -0.05 -> -0.05 (-0.01); Emerging Markets 0.42 -> 0.33 (-0.10) · exhibit: Exhibit slide 11 (Autocorrelation & Volatility) · conditions: Information ratio defined without stated benchmark or risk-free rate; ratio ranking reverses after adjustment (BSTI best vs Event Driven first on unadjusted basis)
  ^QP05-C11-1

### C12 (page 12)
- Four sample portfolios of BSTI plus nine CSFB/Tremont strategies were optimized in sample over Jan 1994-Dec 2008 for four objectives (max information ratio ignoring autocorrelation, max information ratio including autocorrelation, max Calmar, max Sortino). _(construction, design_choice)_ #mech/risk_management
  > Sample Portfolio Construction January 1994 – December 2008 The weightings for each portfolio listed below have been optimized for different risk/return ratios.
  exact_rule: portfolio optimization over BSTI + 9 CSFB/Tremont indices (Global Macro, Equity Market Neutral, Multi-Strategy, Fixed Income Arb, Event Driven, Convertible Arb, Long/Short, Dedicated Short Bias, Emerging Markets); weights lie between 4% and 20%; objectives: IR (A), IR with autocorrelation (B), Calmar (C), Sortino (D) · data_needed: monthly returns of BSTI and CSFB/Tremont indices · reported_result: Weights as read from table (BSTI / GM / EMN / MS / FIA / ED / CA / L/S / DSB / EM): A 14/4/4/20/4/20/4/13/13/4; B 20/4/4/4/4/18/4/18/20/4; C 20/20/4/4/4/16/4/4/20/4; D 20/6/4/14/4/20/4/13/11/4 · exhibit: Exhibit slide 12 (Sample Portfolio Construction) · conditions: Weights are in-sample optimal over the same 15 years, so they overfit; 4% floor and 20% cap are visible but not stated as constraints
  ^QP05-C12-1
- BSTI receives the maximum 20% weight in three of four optimal portfolios (14% in A) and dedicated short bias 11-20% in B, C and D, while global macro gets 20% only in the Calmar-optimal portfolio C; event driven 16-20% in all. _(result, evidence)_ #mech/risk_management
  > PORTFOLIO A: PORTFOLIO B: PORTFOLIO C: PORTFOLIO Maximum D: Sortino Ratio Portfolio Weight
  reported_result: BSTI weight: A 14%, B 20%, C 20%, D 20%; Dedicated Short Bias: A 13%, B 20%, C 20%, D 11%; Event Driven 20/18/16/20%; Multi-Strategy 20/4/4/14% · exhibit: Exhibit slide 12 · conditions: In-sample, hits upper bound of 20%; weights very unstable across objectives
  ^QP05-C12-2

### C13 (page 13)
- Each optimal portfolio wins its own metric in sample: IR ignoring autocorrelation A 1.82; IR including autocorrelation B 1.29; Calmar C 0.69; Sortino D 2.35. _(result, evidence)_ #mech/risk_management
  > Comparison of Optimal Portfolios Information Ratio (disregarding Autocorrelation) Information Ratio (including Autocorrelation) Calmar Ratio Sortino Ratio January 1994 – December 2008
  reported_result: Jan 1994-Dec 2008 monthly, IR (disregarding autocorrelation): A 1.82, B 1.68, C 1.48, D 1.78; IR (including autocorrelation): A 1.13, B 1.29, C 1.19, D 1.21; Calmar: A 0.48, B 0.59, C 0.69, D 0.54; Sortino: A 2.30, B 2.20, C 2.00, D 2.35 · exhibit: Exhibit slide 13 (Comparison of Optimal Portfolios) · conditions: In-sample, no out-of-sample test; ratios are on portfolios blended with BSTI; unadjusted IR overstates by 0.5-0.7 (A 1.82 vs 1.13)
  ^QP05-C13-1
- Slide 13 shows the choice of optimization objective matters more than the portfolio mix, and the Sharpe-type ratio is substantially lower once autocorrelation is included (A: 1.82 to 1.13); the exhibit does not report returns, volatility or drawdown levels themselves. _(caveat, qualifier)_ #mech/research_method
  > Weight Maximum Sortino Ratio Portfolio Weight 1.82 1.68 1.48 1.78 1.29 1.13 1.19 1.21 0.69 2.00 0.48 2.30 0.59 2.20 0.54 2.35
  reported_result: Exhibit reports ratios only; no annual return, volatility or max drawdown values for the portfolios · exhibit: Exhibit slide 13 · conditions: No costs, no fees, hedge fund index returns assumed investable
  ^QP05-C13-2

