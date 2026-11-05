---
source_id: QP13
title: "Valuing Investments: A Statistical Perspective (slides: Bob Stine, Wharton 2009)"
type: paper
claims: 72
opus_only: 4
tags: [paper, layer0]
---
# Valuing Investments: A Statistical Perspective (slides: Bob Stine, Wharton 2009)

**Authors:** Bob Stine (Wharton, Department of Statistics, University of Pennsylvania)

**Summary:** Question: how should an investor judge an investment record and decide how much and which assets to hold, given fat tails, correlation and hidden volatility? Method: teaching slides using a dice game, CAPM regressions on Exxon, Berkshire, 'Bob' and TEAM monthly returns 1980-2009, and the martingale CERT test of alpha (Foster, Stine, Young 2008). Conclusion: look at returns not cumulative value, remove market beta, test alpha with a robust martingale test and adjust for multiplicity; only Berkshire passes CERT and then only before a Bonferroni adjustment.

## Argument map

**Question:** How should an investor judge whether an investment's past outperformance reflects genuine skill (alpha) that will persist, and how much to invest in it, when returns are fat-tailed, dependent, and many candidates are examined?

**Thesis:** Judge investments on returns, not cumulative value; size by long-run growth (E - Var/2, Kelly); remove market exposure with CAPM; and test alpha with a martingale (CERT) test that needs compounded residual returns to exceed 1/alpha (20 at 5%), adjusted by Bonferroni for the number of candidates. On this test only Berkshire's 1980-2009 alpha survives, and even it is marginal after multiplicity. ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C04-1|C04-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C20-1|C20-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C25-1|C25-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C30-1|C30-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C39-3|C39-3]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C39-4|C39-4]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C41-1|C41-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C45-1|C45-1]])

### Foundations (premises)
- Returns over time are nearly independent (close to iid), though correlated across assets. _[empirical, stated; support: S&P 500 monthly return chart since 1950]_ ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C08-1|C08-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C10-1|C10-1]])
- Returns are fat-tailed, especially at daily frequency, and CAPM residuals are non-Gaussian and dependent (ARCH). _[empirical, stated; support: normal quantile plots, residual plots]_ ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C09-1|C09-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C09-2|C09-2]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C32-1|C32-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C38-1|C38-1]])
- Long-run wealth compounds, so the relevant return is the geometric (E - Var/2), not the arithmetic mean. _[theoretical, stated; support: approximation plus dice simulation]_ ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C20-1|C20-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C19-1|C19-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C22-2|C22-2]])
- The market portfolio is the tangent portfolio; skill is only what remains after removing market exposure. _[theoretical, stated; support: CAPM / efficient frontier]_ ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C29-1|C29-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C30-1|C30-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C27-2|C27-2]])
- Strategies can hide rare large losses (peso problem) that a finite sample never shows. _[theoretical, stated; support: Bob Fund construction]_ ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C04-3|C04-3]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C44-1b|C44-1b]])
- Investors search over many candidates, so the best observed alpha is inflated (multiplicity). _[institutional, stated; support: assertion, mutual-fund example]_ ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C04-4|C04-4]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C43-2|C43-2]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C28-2|C28-2]])

### Mechanism chain
- 1. high-variance asset → low or negative long-run growth despite high mean: volatility drag: growth ~ E - Var/2 _[example]_ ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C20-1|C20-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C18-1|C18-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C19-1|C19-1]])
- 2. rebalanced mixing of assets → higher long-run growth: variance falls faster than mean (by 4 vs 2 for a 50/50 mix) _[example]_ ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C21-1|C21-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C22-2|C22-2]])
- 3. growth objective → position size p = (mu - rf)/sigma^2: maximising E - Var/2 over the fraction invested _[assertion]_ ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C25-1|C25-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C25-3|C25-3]])
- 4. asset return → specific return after removing market beta: market exposure is available cheaply via the index _[assertion]_ ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C30-1|C30-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C30-2|C30-2]])
- 5. specific returns with zero conditional mean (no alpha) → compounded specific return is a non-negative martingale: product of (1+w) with E(w|past)=0 _[assertion]_ ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C39-1|C39-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C39-3|C39-3]])
- 6. martingale property → valid p-value 1/max C_t regardless of tails or dependence: Doob's maximal inequality _[test]_ ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C39-3|C39-3]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C39-4|C39-4]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C44-2|C44-2]])
- 7. p-value per candidate → family-wise valid conclusion: Bonferroni multiply by number of candidates _[assertion]_ ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C43-2|C43-2]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C45-2b|C45-2b]])

### Design rationale
- **Use returns rather than cumulative value/prices**: cumulative charts deceive; returns are close to iid. Alternatives: cumulative value charts. Sensitivity: not shown ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C04-1|C04-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C07-1|C07-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C08-1|C08-1]])
- **Kelly fraction p = (mu - rf)/sigma^2**: maximises long-run wealth. Alternatives: implied: more risk-averse fractions. Sensitivity: market history gives 1.75x leverage, which the author considers too aggressive ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C25-1|C25-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C25-2|C25-2]])
- **CAPM regression to remove market risk**: market can be bought directly; leverage looked like skill. Alternatives: raw returns. Sensitivity: not shown ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C04-2|C04-2]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C30-1|C30-1]])
- **Martingale (CERT) test instead of t-test**: t-test unreliable with fat tails, dependence, ARCH; CERT assumes only zero conditional mean. Alternatives: standard t-test. Sensitivity: t-test rejects for all four; CERT only for Berkshire ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C38-1|C38-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C39-1|C39-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C36-1|C36-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C41-1|C41-1]])
- **Estimate beta from finely spaced data**: CERT bound does not depend on n. Alternatives: monthly beta. Sensitivity: requires constant beta ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C40-1|C40-1]])
- **Bonferroni multiplicity adjustment**: simple; number of alternatives is hard to count anyway. Alternatives: none mentioned. Sensitivity: not shown ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C43-2|C43-2]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C45-2b|C45-2b]])

### Evidence map
- Dice game: Red (mean 71%) loses almost surely; 50/50 Red/White mix grows at 0.14. Tests: steps 1-2 (volatility drag, diversification). Rules out: judging by arithmetic mean. Does not rule out: (reader) real assets are correlated and parameters unknown, as the author notes. Strength: strong - mathematical, but stylised ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C19-1|C19-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C20-1|C20-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C21-1|C21-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C23-1b|C23-1b]])
- t-tests find significant alpha for Exxon, Berkshire, Bob and (negative) TEAM; CERT rejects only for Berkshire. Tests: steps 5-6: robust test is stricter. Rules out: that the Exxon/Bob/TEAM alphas are robust. Does not rule out: (reader) Berkshire's alpha may be a factor exposure (value, quality, low-beta) or survivorship-selected; after Bonferroni over many candidates it may also fail. Strength: moderate - four assets, one period ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C35-1|C35-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C36-1|C36-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C41-1|C41-1]])
- Bob Fund with hidden total-loss risk exceeds 20 with probability exactly 1/20. Tests: step 6: test keeps size against peso-type strategies. Rules out: smooth-return strategies passing at a rate above test size. Does not rule out: (reader) low power for genuine small alphas over short samples. Strength: strong - analytical ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C44-1b|C44-1b]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C44-2|C44-2]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C43-3|C43-3]])
- Mutual fund 1993-on-1992 slope -0.49, t -11.6, but sign flips across years. Tests: premise that cross-sectional dependence inflates significance. Rules out: naive pooled t-tests of persistence. Does not rule out: (reader) genuine time-varying reversal from style rotation. Strength: moderate - single illustration ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C28-1|C28-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C28-2|C28-2]])

### Regimes
- leverage in rising markets (until 2008) → leveraged market exposure looks like skill until a crash ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C04-2|C04-2]])
- market crashes (Oct 1987, Aug 1998, Oct 2008) → outliers dominate tails; peso-type risks materialise ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C08-1|C08-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C04-3|C04-3]])
- short horizons → a poor long-run investment can look very attractive ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C22-2|C22-2]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C18-1|C18-1]])
- real-world dependence and changing parameters → dice-game sizing lessons weaken ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C23-1b|C23-1b]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C27-1|C27-1]])

### Gaps and conflicts
- [conflict] Kelly example prints p = 0.075/0.040 = 1.75; the arithmetic gives 1.875 ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C25-2|C25-2]])
- [unspecified] Identity and construction of 'Bob' and 'TEAM' series are not explained on the slides ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C11-2|C11-2]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C32-1|C32-1]])
- [unspecified] Market proxy (excess.vw), risk-free series and beta-estimation frequency for the CERT results are not fully stated ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C30-1|C30-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C40-1|C40-1]])
- [untested] Power of the martingale test (how large/long an alpha is needed to reach 20) is not quantified ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C43-3|C43-3]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C39-4|C39-4]])
- [untested] CERT assumes constant beta; time-varying beta would leak market returns into w_t ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C40-1|C40-1]])
- [unspecified] 'Special' series on slide 7 is not defined ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C07-1|C07-1]])

### Relations to other strategies
- volatility targeting / Kelly sizing: **complement**. both size positions by expected return over variance ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C25-1|C25-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C20-1|C20-1]])
- multiple-testing adjustments for backtests (Holm, deflated Sharpe): **complement**. Bonferroni on CERT p-values addresses the same data-mining risk ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C43-2|C43-2]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C45-2b|C45-2b]])
- Sharpe ratio / t-stat based strategy evaluation: **substitute**. CERT replaces the t-test where tails and dependence make t unreliable ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C38-1|C38-1]], [[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C39-3|C39-3]])
- short-volatility / carry strategies: **special case**. (reader) the Bob Fund is a stylised short-tail-risk strategy with smooth returns and rare crashes ([[QP13 - Valuing Investments A Statistical Perspective (slides Bob Stine, Wharton 2009)#^QP13-C44-1b|C44-1b]])

### Forward-looking inputs (reader synthesis)
(reader) No market-timing input is proposed; the forward-looking content is a filter: an alpha is credible going forward only if compounded market-neutral returns exceeded m/alpha-level (m = number of candidates) in-sample (step 6-7), and the size of any holding should follow (mu - rf)/sigma^2 shrunk for estimation error (step 3). The filter stops being reliable if beta drifts over time, if the candidate count is understated, or if the search horizon is too short to reach the threshold.

### Reader inferences (not stated by the authors)
- (reader) For the Global Macro Book, the CERT test is a usable non-parametric check on strategy alpha: compound the residual (beta-hedged) returns and require max cumulative value above m/0.05.
- (reader) The Bob Fund maps onto short-volatility or carry strategies whose smooth returns hide crash risk; Sharpe-based tests overstate their significance.
- (reader) Bob's residual plot (two levels) and steady CERT path suggest a constructed series with a fixed small excess and rare jumps, but the slides do not say so.
- (reader) Berkshire's CERT success may reflect known factor exposures; with a multi-factor model it might not reject.
- (reader) The Kelly 1.75 figure appears to be an arithmetic slip (1.875), not a different formula.

## Claims

### C02 (page 2)
- Four record paths are shown for a $1 stake invested in 1980 (Exxon, Berkshire, Bob, TEAM; log scale); the question posed is whether any of these records is convincing going forward. _(result, premise)_ #mech/research_method
  > Value of $1 initially invested in 1980 and reinvested
  reported_result: Ending value of $1 (1980 to about mid-2009, read from chart, approximate): Berkshire ~55 (peak ~85 around 2008), Exxon ~15, Bob ~6.5, TEAM ~1.5 · exhibit: slide 2 chart
  ^QP13-C02-1
- The author's point is that a good cumulative record alone does not show that the manager or asset has skill that will continue. _(mechanism, premise)_ #mech/research_method
  > Convincing going forward?
  ^QP13-C02-2

### C03 (page 3)
- A fund that 'guarantees' 2% annual excess return over any benchmark is offered as a lure and is later shown (slide 44) to be a hidden-volatility scheme that looks perfect until it busts. _(mechanism, premise)_ #mech/risk_management
  > Guarantees 2% excess annual returns above any benchmark you want. Guaranteed.
  conditions: works only until the rare large loss occurs
  ^QP13-C03-1

### C04 (page 4)
- Evaluate investments on period returns, not cumulative value or prices, because one good year does not mean continuing success and cumulative paths mislead. _(mechanism, premise)_ #mech/research_method
  > Focus on returns, not cumulative value or prices
  exact_rule: Analyse R_t = (P_t - P_{t-1})/P_{t-1} series, not cumulative value
  ^QP13-C04-1
- Remove market performance by regressing excess returns on the market (CAPM), because leverage on the market looked like skill 'until lately'. _(mechanism, premise)_ #mech/risk_premium
  > Remove market performance (CAPM)
  exact_rule: Regress asset excess return on market excess return and judge the intercept (alpha)
  ^QP13-C04-2
- Past records can hide rare large losses (peso problem): the absence of an event in the sample does not make it impossible. _(mechanism, premise)_ #mech/risk_management
  > Watch for unseen volatility (Peso problem)
  ^QP13-C04-3
- When many managers or assets are examined, the best-looking result must be adjusted for the number of alternatives considered; the author jokes about E-trade ads reappearing after the rebound. _(mechanism, premise)_ #mech/research_method
  > Adjust for multiplicity
  exact_rule: Adjust p-values for the number of assets or strategies considered
  ^QP13-C04-4

### C06 (page 6)
- Market data are S&P 500 monthly values from Yahoo Finance, January 1950 to February 2009 (710 months). _(construction, design_choice)_ #mech/research_method
  > Data: Yahoo finance, Jan 1950 - Feb 2009, 710 months
  data_needed: S&P 500 monthly index/return series, Yahoo Finance, Jan 1950-Feb 2009 · exhibit: slide 6
  ^QP13-C06-1
- $1 invested in the S&P 500 on 1 January 1950 grew about 7% a year, reaching roughly 49 by February 2009 after peaks near 89 (2000) and 91 (2007). _(result, evidence)_ #mech/risk_premium
  > 7% Annual growth
  reported_result: S&P 500 $1 from Jan 1950: about 7% annual growth; value ~49 at Feb 2009; peaks ~88-90 in 2000 and ~91 in 2007 (chart reading); chart is annotated 'Log Scale' but the plotted axis appears linear · exhibit: slide 6 chart · conditions: sample ends at the 2008 crash
  ^QP13-C06-2

### C07 (page 7)
- A 'Special' cumulative curve ends about twice as high as the market curve (about 100 vs 49 in 2009, with peak ~180 vs ~90) and looks impressive although the slide's moral is that cumulative plots make performance easy to misread. _(result, evidence)_ #mech/research_method
  > Too easy to be deceived...
  reported_result: 'Special' vs Market cumulative value, 1950-2009: Special ~97 at 2009, peaks ~178 (2000) and ~182 (2007); Market ~49, ~90, ~91 (chart reading) · exhibit: slide 7 chart
  ^QP13-C07-1
- Therefore analysis should be done on returns rather than cumulative value. _(mechanism, conclusion)_ #mech/research_method
  > Moral: Stick to returns...
  ^QP13-C07-2

### C08 (page 8)
- Monthly S&P returns, unlike cumulative value, have a much simpler structure and are almost independent and identically distributed; the largest monthly drops are in October 1987 (Black Monday), August 1998 (Long Term Capital) and October 2008 (banking crisis). _(result, evidence)_ #mech/risk_management
  > Much simpler structure, almost iid...
  reported_result: Monthly S&P returns 1950-2009 range from about -0.22 (Oct 1987) to about +0.15; labelled outliers: Oct 1987, Aug 1998, Oct 2008 · exhibit: slide 8 chart · conditions: extreme months cluster in crisis episodes
  ^QP13-C08-1

### C09 (page 9)
- Monthly S&P 500 returns 1950-Feb 2009 have mean 0.0064, SD 0.0415 and variance 0.0017. _(result, evidence)_ #mech/risk_premium
  > mean = 0.0064, s = 0.0415, s 2 = 0.0017
  reported_result: Monthly returns: mean 0.0064, s 0.0415, s^2 0.0017 (Jan 1950-Feb 2009, 710 months) · exhibit: slide 9
  ^QP13-C09-1
- The normal quantile plot shows fat tails (extreme returns well beyond the normal line) in monthly data, and more so in daily data (mean 0.0003, SD 0.0095, variance 0.0001). _(result, evidence)_ #mech/risk_management
  > Fat tails more apparent in daily data.
  reported_result: Daily returns: mean 0.0003, s 0.0095, s^2 0.0001; monthly worst point about -0.20 where a normal would give about -0.12 · exhibit: slide 9 chart · conditions: tails fatter at higher frequency
  ^QP13-C09-2

### C10 (page 10)
- Each asset's period returns look like a sequence of nearly independent bets, but returns across assets remain correlated, so risk cannot be assessed asset by asset. _(mechanism, premise)_ #mech/risk_management
  > Sequence of “bets” that appear nearly independent, but correlation remains between assets.
  exact_rule: R_t = (P_t - P_{t-1})/P_{t-1}; risk defined as variation in returns
  ^QP13-C10-1

### C11 (page 11)
- Monthly return means and SDs for 1980-2009 for the four assets show Berkshire with the highest mean and risk and TEAM with the lowest. _(result, evidence)_ #mech/risk_premium
  > Monthly returns, 1980-2009
  reported_result: Mean/SD monthly: Exxon 0.0089/0.0503; Berkshire 0.0137/0.0701; Bob 0.0064/0.0467; TEAM 0.0014/0.0217 (1980-2009) · exhibit: slide 11 table
  ^QP13-C11-1
- The slide asks whether return should be traded for risk, setting up the long-run return formula E(r) - Var(r)/2. _(mechanism, context)_ #mech/risk_management
  > Trade off return for risk?
  ^QP13-C11-2

### C12 (page 12)
- Portfolio design splits into two questions: how much wealth to invest and which assets to hold, beginning with the whole-market index and asking what else to add to it. _(mechanism, context)_ #mech/research_method
  > How much of my wealth should I invest to meet my financial goals?
  ^QP13-C12-1

### C15 (page 15)
- Three hypothetical investments: Green (mean 7.5%, SD 20% a year), Red (71%, 132%) and White (0%, 6%); the audience must choose between return and risk. _(result, premise)_ #mech/risk_management
  > Which of these do you like, if any?
  reported_result: Average / SD annual return: Green 7.5% / 20%; Red 71% / 132%; White 0% / 6% · exhibit: slide 15 table
  ^QP13-C15-1

### C16 (page 16)
- Each round wealth is multiplied by a table result from a die roll: Green 0.8/0.9/1.05/1.1/1.2/1.4, Red 0.06/0.2/1/3/3/3, White 0.9/1/1/1/1/1.1 for outcomes 1-6, so W_t = result * W_{t-1}. _(construction, design_choice)_ #mech/risk_management
  > 3 dice determine outcomes:
  exact_rule: W_t = (table result)*W_{t-1}; Green 0.8,0.9,1.05,1.1,1.2,1.4; Red 0.06,0.2,1,3,3,3; White 0.9,1,1,1,1,1.1 · exhibit: slide 16 table
  ^QP13-C16-1
- The dice game is taken from the author's 'Being Warren Buffett' article in The American Statistician (2006). _(citation, context)_ #mech/research_method
  > “Being Warren Buffett”, Amer Statistician, 2006
  ^QP13-C16-2

### C17 (page 17)
- In a typical 20-round run Red swings wildly and ends near zero, Green grows steadily to about 10,000-12,000 (from 1,000) and White stays near 1,000. _(result, evidence)_ #mech/risk_management
  > Red is “exciting” but generally loses value.
  reported_result: Typical run, 20 rounds, start 1,000: Green ends ~10,200 (peak ~11,800), White ~950, Red falls to ~0 after reaching ~4,900 at rounds 7-9 · exhibit: slide 17 chart
  ^QP13-C17-1
- Green is calibrated to the annual excess returns of the US stock market, White to Treasury bill returns, and Red is invented (an extreme high-mean, high-variance asset). _(construction, design_choice)_ #mech/research_method
  > We made up Red!
  exact_rule: Green ~ US stock market excess return (mean 7.5%, SD 20%); White ~ T-bills; Red fictional
  ^QP13-C17-2

### C18 (page 18)
- Red's expected terminal wealth after 20 rounds is 1.71^20, about 45,700 times the start, and in rare runs it does soar (to over 10 million times in the plotted run), although most runs lose. _(result, evidence)_ #mech/risk_management
  > In 20 rounds, the expected value of Red is
  reported_result: E[Red at 20 rounds] = 1.71^20 = 45,700x initial; plotted rare run peaks about 100,000,000 (log axis, from 1,000) near round 12 · exhibit: slide 18 chart · conditions: arithmetic mean is dominated by a few rare winners
  ^QP13-C18-1

### C19 (page 19)
- Despite its 71% expected return, Red loses with probability one in the long run, because its compound growth is negative; a few simulations end fabulously rich (the 'Warren Buffetts' of the class) but most lose most of their value. _(mechanism, mechanism_step)_ #mech/risk_management
  > In the long run, Red will lose (w.p. 1)
  conditions: independent repeated bets with high variance
  ^QP13-C19-1
- The open questions are how to recognise a losing high-variance investment without waiting for the loss and how to still exploit a mixed use of Red (answered by diversification, slide 21). _(mechanism, context)_ #mech/research_method
  > How can I recognize that Red will lose without waiting for it to happen?
  ^QP13-C19-2

### C20 (page 20)
- With independent period returns, long-run wealth grows like W_0*(1 + E(r) - Var(r)/2)^t, so variance subtracts from growth (volatility drag). _(mechanism, mechanism_step)_ #mech/risk_management
  > If the r t are independent over time, then
  exact_rule: Long-run growth rate g = E(r_t) - Var(r_t)/2 for independent returns; W_t ~ W_0 (1+g)^t
  ^QP13-C20-1
- Applying g = E - Var/2: Green 0.075 - 0.04/2 = 0.055 (positive, 'can buy this one'), Red 0.71 - 1.74/2 = -0.16, White 0 - 0.003/2 = -0.002. _(result, evidence)_ #mech/risk_management
  > Can buy this one
  reported_result: E(r)-Var(r)/2: Green 0.055; Red -0.16 (Var 1.74); White -0.002 (Var 0.003) · exhibit: slide 20 table
  ^QP13-C20-2

### C21 (page 21)
- A 50/50 mix of Red and White ('Pink') gives up half of Red's expected return (0.355) but cuts variance by four (0.435), so its long-run value E - Var/2 is positive (0.14) although neither component has positive long-run growth. _(result, evidence)_ #mech/risk_management
  > Mix investments rather than leaving everything in one.
  exact_rule: Portfolio 0.5*Red + 0.5*White: E = E(Red)/2, Var = Var(Red)/4; long-run growth = E - Var/2 · reported_result: Pink: E = 0.355, Var = 0.435, long-run E - Var/2 = 0.14 (slide arithmetic ignores White variance, 0.003) · exhibit: slide 21 · conditions: variance falls with the square of the weight, return only linearly; requires independence between the mixed bets
  ^QP13-C21-1

### C22 (page 22)
- Lesson: long-run return equals E(return) - (1/2)Var(return), so portfolios succeed by trading expected return for variance reduction. _(mechanism, conclusion)_ #mech/risk_management
  > Long-run return given by
  exact_rule: Maximise E(r) - 0.5*Var(r) (long-run growth)
  ^QP13-C22-1
- Over short horizons a bad long-term investment (such as Red) can look very attractive, so short records cannot validate a high-variance strategy. _(mechanism, conclusion)_ #mech/risk_management
  > Over short horizons, a poor long-term investment might appear very attractive.
  conditions: short samples
  ^QP13-C22-2

### C23 (page 23)
- The dice game assumes independent assets, so real investments with correlation (Red unaffected by Green) behave differently from the game. _(caveat, qualifier)_ #mech/risk_management
  > The dice fluctuate independently of one another.
  conditions: assets are correlated in reality
  ^QP13-C23-1
- Stability: the dice's odds never change, whereas real return distributions drift. _(caveat, qualifier)_ #mech/structural_shift
  > The properties of the dice stay the same throughout the simulation.
  conditions: parameters change over time
  ^QP13-C23-2
- Parameters are known in the game but must be estimated in practice, which adds estimation risk. _(caveat, qualifier)_ #mech/research_method
  > We know the properties of the random processes in the dice game.
  conditions: mean and variance unknown in real data
  ^QP13-C23-3
- Unlike the dice, real investments are not independent of each other, their properties change over time, and their parameters are unknown. _(caveat, qualifier, Opus only)_ #mech/research_method
  > Real investments lack some properties of the investments in the dice simulation
  conditions: dependence, instability and estimation error weaken the dice lessons
  ^QP13-C23-1b

### C24 (page 24)
- Applying long-run return = mean - SD^2/2 to monthly 1980-2009 data gives Exxon 0.0076, Berkshire 0.0113, Bob 0.0053 and TEAM 0.0012 per month. _(result, evidence)_ #mech/risk_management
  > Challenge: Summary Stats
  exact_rule: long-run return = mean - s^2/2 on monthly returns · reported_result: Long-run monthly return (mean/SD): Exxon 0.0076 (0.0089/0.0503); Berkshire 0.0113 (0.0137/0.0701); Bob 0.0053 (0.0064/0.0467); TEAM 0.0012 (0.0014/0.0217), 1980-2009 · exhibit: slide 24 table
  ^QP13-C24-1

### C25 (page 25)
- If the objective is maximum long-run wealth, the fraction of wealth to invest in an asset is p = (mu - r_f)/sigma^2 (Kelly-type sizing), with r_f the risk-free rate. _(construction, design_choice)_ #mech/risk_management
  > If we accept the objective to maximize long- run wealth, then the proportion of our wealth p to put in an investment is
  exact_rule: p = (mu - r_f) / sigma^2, mu and sigma for the asset, r_f risk-free rate; short if mu < r_f · data_needed: Asset mean and variance, risk-free rate
  ^QP13-C25-1
- For the whole US market with mu = 0.075 and sigma^2 = 0.040 the formula gives p = 0.075/0.040 = 1.75 times wealth, which the author says is more than people actually want (people are more risk averse than the objective). _(result, evidence)_ #mech/risk_management
  > Example suggests we’re more risk averse…
  reported_result: p = 0.075/0.040 = 1.75 times wealth for the stock market (annual mu - r_f = 7.5%, variance 0.04) · exhibit: slide 25 · conditions: assumes mu and sigma known and fixed; highly sensitive to the estimated mu
  ^QP13-C25-2
- Any asset with a known nonzero expected excess return deserves some position, long if positive and short if negative. _(mechanism, conclusion)_ #mech/risk_premium
  > Nonetheless, we ought to invest some fraction of our wealth in any asset for which we know μ ≠ 0 (short it if μ < 0).
  ^QP13-C25-3

### C27 (page 27)
- Choosing among many correlated assets requires forecasting future correlations, which is the messy part of portfolio analysis. _(caveat, qualifier)_ #mech/risk_management
  > Messy problem of portfolio analysis is to anticipate correlations going forward.
  ^QP13-C27-1
- Finance theory advises investing first in the whole market and then considering other assets only for what they add beyond it. _(mechanism, premise)_ #mech/risk_premium
  > Invest first in the market as a whole
  exact_rule: Start from the market portfolio; test other assets for alpha relative to it
  ^QP13-C27-2

### C28 (page 28)
- Regressing 1993 returns on 1992 returns for about 1,500 mutual funds gives a 'statistically significant' slope of -0.49 (t = -11.57, intercept 18.63), but the sign changes in other years, because the 1,500 observations are dependent (common market shock), not independent. _(result, evidence)_ #mech/research_method
  > Regress growth in current year on prior growth
  exact_rule: Cross-sectional regression: Return_{1993} = a + b*Return_{1992} across ~1,500 funds · reported_result: Intercept 18.634 (SE 0.468, t 39.83); Return 92 slope -0.49079 (SE 0.04243, t -11.57); the slide notes 'But the sign changes!' · exhibit: slide 28 table and scatter · conditions: cross-sectional t-statistics overstate evidence when fund returns share a common year effect
  ^QP13-C28-1
- The apparent significance is spurious because the funds' returns in a year are correlated, so 1,500 funds behave like far fewer independent observations. _(mechanism, conclusion)_ #mech/research_method
  > Explanation: 1,500 dependent observations...
  ^QP13-C28-2

### C29 (page 29)
- In mean-SD space of random portfolios the efficient frontier is traced by the best portfolios; the tangent portfolio from the risk-free rate r_f is the market portfolio, and mixing it with cash (lend) or leveraging it (borrow) beats any other mix. _(mechanism, premise)_ #mech/risk_premium
  > Plot average return on SD of return for a collection of randomly formed portfolios
  exact_rule: Hold market (tangent) portfolio plus cash or borrowing to set risk · reported_result: Chart: tangent portfolio at SD ~0.10, return ~0.035; r_f ~0.01; borrowing line extends above frontier points at SD 0.13 and 0.22 · exhibit: slide 29 chart · conditions: holds if the market portfolio is mean-variance efficient
  ^QP13-C29-1

### C30 (page 30)
- CAPM: R_t - r_f = alpha + beta*(M_t - r_f) + eps_t, with beta = Cov(R-r_f, M-r_f)/Var(M-r_f) and alpha = 0 in the theory, so risk splits into market and specific parts. _(construction, design_choice)_ #mech/risk_premium
  > Excess returns on an asset are related to those on whole market by a linear equation
  exact_rule: R_t - r_f = alpha + beta (M_t - r_f) + eps_t; beta = Cov/Var; specific return w_t = (R_t - r_f) - beta (M_t - r_f) = alpha + eps_t · data_needed: Asset returns, market (value-weighted) returns, risk-free rate
  ^QP13-C30-1
- If alpha is not zero the asset's specific return has a non-zero mean and one should buy (alpha>0) or sell (alpha<0) some amount of it. _(mechanism, conclusion)_ #mech/risk_premium
  > Intrinsic variation in asset has non-zero mean
  ^QP13-C30-2

### C31 (page 31)
- All four assets (Exxon, Berkshire, Bob, TEAM) are strongly correlated with the market excess return; Bob and TEAM lie almost exactly on a line with the market, Exxon and Berkshire are diffuse. _(result, evidence)_ #mech/risk_premium
  > All have substantial correlation with the returns on the whole market (market risk)
  reported_result: Slide 31 scatters of asset vs market monthly excess returns; Bob and TEAM nearly collinear with market; text on slide: alpha = 0.006, t = 2.68 (Exxon) and alpha = 0.01, t = 3.12 (Berkshire) · exhibit: slide 31 charts
  ^QP13-C31-1
- Berkshire's alpha is about 0.01 per month with t = 3.12 in the CAPM regression (Exxon 0.006, t 2.68). _(result, evidence)_ #mech/risk_premium
  > alpha= 0.01 with t= 3.12
  reported_result: Berkshire alpha ~0.01, t 3.12; Exxon alpha 0.006, t 2.68 (monthly, 1980-2009) · exhibit: slide 31
  ^QP13-C31-2

### C32 (page 32)
- CAPM residuals violate regression assumptions: Berkshire and Exxon show volatility clustering with the market level, Bob's residuals lie on two near-deterministic curves of size under 0.02, and TEAM's residuals form a bow-tie shape. _(result, evidence)_ #mech/risk_management
  > Residuals often deviate from the usual assumptions of simple regression.
  reported_result: Residuals vs market excess return (monthly): Exxon within about +-0.15, Berkshire within about -0.15 to +0.25, Bob residuals 0 to 0.015 along curves, TEAM within +-0.02 in a bow-tie · exhibit: slide 32 charts · conditions: non-constant variance and dependence mean the t-distribution p-value is unreliable
  ^QP13-C32-1

### C34 (page 34)
- TEAM's residuals are a nonlinear, bow-tie function of the market (negative residual when the market is up by 3-10%, positive when down by 5%), which is not additive noise and is typical of a payoff with hidden option-like exposure. _(result, evidence)_ #mech/risk_management
  > Residuals often deviate from the usual
  reported_result: TEAM residuals about +-0.02 (outliers +0.034 and -0.02), bow-tie pattern against market excess return · exhibit: slide 34 chart · conditions: a linear CAPM fit misses nonlinearity; the option-like reading is the reader interpretation, not stated on the slide
  ^QP13-C34-1

### C35 (page 35)
- For Exxon the CAPM regression gives alpha 0.0062 (SE 0.0023, t 2.68, p 0.0077) and beta 0.5623 (SE 0.0500, t 11.25); the standard test uses the t-distribution for the p-value. _(result, evidence)_ #mech/risk_premium
  > Regress out market risk, obtaining estimates of α and β.
  exact_rule: OLS of Exxon excess return on market excess return; H0: alpha = 0, t-test · reported_result: Exxon: alpha 0.0062, SE 0.0023, t 2.68, p 0.0077; beta 0.5623, SE 0.0500, t 11.25 · exhibit: slide 35 table
  ^QP13-C35-1

### C36 (page 36)
- The standard t-test finds all four alphas 'significant': Exxon 0.0062 (t 2.7, p 0.008), Berkshire 0.0103 (3.1, 0.002), Bob 0.0016 (5.5, 0.000) and TEAM -0.0008 (-2.6, 0.009); the author asks the audience whether they believe them. _(result, evidence)_ #mech/research_method
  > Do you believe these results?
  reported_result: Alpha / t / p: Exxon 0.0062/2.7/0.008; Berkshire 0.0103/3.1/0.002; Bob 0.0016/5.5/0.000; TEAM -0.0008/-2.6/0.009 (monthly, 1980-2009) · exhibit: slide 36 table · conditions: t-test assumes Gaussian independent errors, which slides 32-34 contradict
  ^QP13-C36-1

### C38 (page 38)
- The usual alpha t-test is doubtful because returns have fat tails and outliers, so the distribution of the t-statistic is unknown. _(mechanism, premise)_ #mech/risk_management
  > Some investments produce returns that are far from Gaussian, with large outliers (fat tails)
  conditions: non-Gaussian returns
  ^QP13-C38-1
- CAPM residuals are not independent (ARCH-type processes), yet a p-value is still wanted, which motivates a test that does not need independence. _(mechanism, premise)_ #mech/risk_management
  > Evident lack of independence in CAPM residuals
  conditions: ARCH / volatility clustering
  ^QP13-C38-2
- Despite model risk, an investor still needs a valid p-value for alpha. _(mechanism, premise, Opus only)_ #mech/research_method
  > Nonetheless want a p-value
  ^QP13-C38-2b

### C39 (page 39)
- CERT tests H0: alpha = 0 on specific returns w_t = (R_t - r_f) - beta*(M_t - r_f), assuming only that w_t has zero conditional mean given its past (a martingale difference), not iid. _(construction, design_choice)_ #mech/research_method
  > Assume only that E(w t |w t-1 ,w t-2 ,…) = 0 (not nec. iid)
  exact_rule: w_t = (R_t - r_f) - beta (M_t - r_f); H0: E(w_t | w_{t-1}, w_{t-2}, ...) = 0 · data_needed: Asset and market excess returns, beta estimate
  ^QP13-C39-1
- Under H0 the compounded specific returns C_t = (1+w_1)(1+w_2)...(1+w_t) form a non-negative martingale starting at 1, so Doob's inequality bounds how high C can go by chance. _(construction, mechanism_step)_ #mech/research_method
  > Compound returns are non-negative martingale
  exact_rule: C_t = prod_{i<=t}(1+w_i), t = 1..n
  ^QP13-C39-2
- The CERT p-value is from Doob's inequality P(max(C_1..C_n) >= gamma) <= 1/gamma, so the p-value is 1 over the maximum compounded residual return. _(construction, design_choice)_ #mech/research_method
  > CERT p-value from Doob’s inequality
  exact_rule: p-value = 1 / max_t C_t (capped at 1); reject H0 when max C_t >= 1/level
  ^QP13-C39-3
- To reject at the 0.05 level the compounded residual return must exceed 20 at some point during the observed period. _(result, evidence)_ #mech/research_method
  > have to exceed 20 during observed period
  exact_rule: Threshold: max C_t > 20 for 5% level (1/0.05) · reported_result: 5% rejection threshold C > 20 · exhibit: slide 39 · conditions: the bound is conservative for Gaussian-like returns
  ^QP13-C39-4

### C40 (page 40)
- Since the martingale test does not depend on the number of observations n, one can use finely spaced (e.g. daily) data to pin down beta, provided beta is constant. _(implementation, design_choice)_ #mech/research_method
  > we can use finely spaced data that essentially reveal β (if you believe it’s fixed!)
  exact_rule: Estimate beta from high-frequency data; compound w_t at the same frequency; test p = 1/max C · conditions: requires a fixed beta
  ^QP13-C40-1
- Exxon's CERT compounded residual return rises from 1 in 1980 to about 8 by 2009 (jump after 2004), well below the 20 threshold. _(result, evidence)_ #mech/research_method
  > Since the martingale test does not depend on n
  reported_result: Exxon CERT path: ~2 in 1990, ~3.5 in 2000, peak ~7.8 in 2009 (chart reading) · exhibit: slide 40 chart
  ^QP13-C40-2

### C41 (page 41)
- Only Berkshire's compounded residual return exceeds 20, so only Berkshire rejects alpha = 0; Exxon peaks near 8, Bob ends near 1.75 and TEAM near 1.3, all below threshold. _(result, conclusion)_ #mech/research_method
  > Only Berkshire Hathaway rejects the null, and then we have to consider multiplicity.
  reported_result: Maximum CERT value, 1980-2009: Berkshire ~25 (crosses 20 first around 1998-99; ends ~21); Exxon ~7.8; Bob ~1.75; TEAM ~1.35 (chart reading) · exhibit: slide 41 charts · conditions: single-asset rejection before multiplicity adjustment
  ^QP13-C41-1
- The robust test reverses the t-test for Bob (t 5.5 versus CERT 1.75, no rejection) and TEAM (t -2.6, CERT path above 1), showing how smooth hidden-risk payoffs can look statistically significant under the t-test. _(result, evidence)_ #mech/risk_management
  > Only Berkshire Hathaway rejects the null, and then we have to consider multiplicity.
  reported_result: Standard t-test rejects for all four (slide 36); CERT rejects for Berkshire only (slide 41) · exhibit: slides 36 and 41 · conditions: Bob and TEAM returns are nearly exact functions of the market
  ^QP13-C41-2

### C43 (page 43)
- A p-value around 0.05 does not survive adjustment for multiplicity when many assets have been considered. _(mechanism, conclusion)_ #mech/research_method
  > A p-value of 1/20 does not overcome adjustments for multiplicity.
  conditions: more assets considered than the four shown
  ^QP13-C43-1
- Bonferroni adjustment: multiply the CERT p-value by the number of assets considered; the author bets the audience considered more than four. _(construction, design_choice)_ #mech/research_method
  > Multiply the p-value from martingale test by number of assets considered.
  exact_rule: adjusted p = min(1, m * p_CERT), m = number of assets or strategies examined
  ^QP13-C43-2
- The martingale test is 'tight': there are processes an investor would not want to hold for which the bound is exactly right (shown in the Bob Fund example). _(robustness, qualifier)_ #mech/research_method
  > The test is “tight” in the sense that there are processes you would not want to consider for which it gets the right answer,
  ^QP13-C43-3

### C44 (page 44)
- The Bob Fund 'guarantee' is built from a bet with return 1/k with probability k/(k+1) and -1 (total loss) with probability 1/(k+1), expected return zero, so it earns steady small gains until the rare wipe-out ('busted'). _(construction, evidence)_ #mech/risk_management
  > Unobserved volatility
  exact_rule: r_t = +1/k w.p. k/(k+1); r_t = -1 w.p. 1/(k+1); E(r_t)=0 · reported_result: k = 19: the slide states returns a bit more than 2% growth; smaller k give more exciting performance · exhibit: slide 44 · conditions: looks like positive alpha until the rare loss; the slide figure of about 2% for k=19 is not derived there (1/k = 5.3% per win)
  ^QP13-C44-1
- For any k the probability that the Bob Fund's compounded value ever exceeds 20 is exactly 1/20, so the CERT test controls the false-positive rate against this hidden-volatility strategy. _(result, conclusion)_ #mech/risk_management
  > Martingale test protects against the “until it happens” unobserved volatility
  exact_rule: P(C_t of Bob Fund > 20) = 1/20 for any k · reported_result: P(C > 20) = 1/20 for every k · exhibit: slide 44
  ^QP13-C44-2
- The 'Bob Fund' delivers smooth excess returns by earning 1/k each period with probability k/(k+1) and losing everything with probability 1/(k+1), so its expected excess return is zero; with k=19 it shows a bit over 2% growth until it busts. _(mechanism, evidence, Opus only)_ #mech/new
  > How do you guarantee those 2% above benchmark returns?
  exact_rule: r_t = 1/k w.p. k/(k+1); r_t = -1 w.p. 1/(k+1); E(r_t) = 0; example k = 19 · conditions: looks good until the rare loss happens (peso problem)
  ^QP13-C44-1b

### C45 (page 45)
- Summary of method: use returns not cumulative value, remove market with CAPM, test with the martingale test (CERT) for unseen volatility, and use Bonferroni for multiplicity, which does fine since it is hard to count the alternatives considered. _(construction, conclusion)_ #mech/research_method
  > Watch for unseen volatility using robust test
  exact_rule: 1) work with returns; 2) regress out market (CAPM); 3) CERT p = 1/max C; 4) Bonferroni by number of alternatives
  ^QP13-C45-1
- The CERT test comes from Foster, Stine and Young (2008), 'A martingale test for alpha'. _(citation, context)_ #mech/research_method
  > Foster, Stine, Young (2008) “A martingale test for alpha”
  ^QP13-C45-2
- Bonferroni is adequate because the true number of alternatives considered is hard to count anyway. _(caveat, qualifier, Opus only)_ #mech/research_method
  > Bonferroni does fine, particularly since it’s hard to “count” the considered alternatives
  ^QP13-C45-2b

