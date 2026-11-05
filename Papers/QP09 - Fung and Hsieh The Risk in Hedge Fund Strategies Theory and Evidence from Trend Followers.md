---
source_id: QP09
title: "Fung and Hsieh: The Risk in Hedge Fund Strategies: Theory and Evidence from Trend Followers"
type: paper
claims: 149
opus_only: 19
tags: [paper, layer0]
---
# Fung and Hsieh: The Risk in Hedge Fund Strategies: Theory and Evidence from Trend Followers

**Authors:** William Fung (PI Asset Management, LLC); David A. Hsieh (Duke University)

**Summary:** Can trend-following hedge fund returns be explained by option-like risk? Primitive trend-following strategy modelled as three-month lookback straddles on 26 futures markets, replicated by rolling standard straddles; compared with 407 CTA funds, 1985-1997 monthly data. Lookback straddle portfolios explain trend-follower returns (adjusted R2 47.9%) while standard asset benchmarks do not (about 1-8%); trend followers are long a convex, crisis-like payoff concentrated in currencies, bonds and commodities.

## Argument map

**Question:** How can investors see the systematic risk of hedge fund strategies whose returns are nonlinear, using trend-following CTAs as the case? It matters because linear factor models make such funds look riskless and uncorrelated, which misleads risk budgeting and benchmarking.

**Thesis:** A primitive trend follower has the payoff of a lookback straddle (long the realised range), so trend-following returns behave like long volatility / market-event-risk options; portfolios of lookback straddles on 26 futures markets explain about half of CTA index variance and the extreme-month payoffs, where asset-class benchmarks explain almost none. ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C01-2|C01-2]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C04-4|C04-4]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C15-3|C15-3]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C25-4|C25-4]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C25-5|C25-5]])

### Foundations (premises)
- Dynamic trading strategies generate option-like (nonlinear) returns, which linear regressions on asset benchmarks miss or misstate. _[theoretical, stated; support: citations (Merton 1981, Glosten-Jagannathan 1994, Grinblatt-Titman, Lehman-Modest)]_ ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C02-1|C02-1]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C02-3|C02-3]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C02-7|C02-7]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C05-5|C05-5]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C03-4|C03-4]])
- CTA returns are dominated by one common style, trend following. _[empirical, stated; support: PCA in Fung-Hsieh 1997b, updated on TASS]_ ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C03-1|C03-1]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C14-5|C14-5]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C12-1|C12-1]])
- Trend followers enter after a move (breakouts) and aim to capture the range between high and low, whose ideal payoff is S_max - S_min. _[institutional, stated; support: definition and industry usage]_ ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C06-1|C06-1]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C06-2|C06-2]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C06-6|C06-6]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C07-5|C07-5]])
- The fair cost of perfect trend following equals the lookback straddle premium, observable via exchange-traded options. _[assumed, stated; support: assumption (costs of real traders unknown)]_ ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C07-2|C07-2]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C25-2|C25-2]])
- Extreme market moves stem from common macro shocks that hit all financial markets together. _[empirical, stated; support: example (1990 Gulf War); Table 4]_ ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C17-7b|C17-7b]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C19-1|C19-1]])
- Whether markets actually trend is not asserted. _[assumed, stated; support: explicitly left open]_ ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C06-4|C06-4]])

### Mechanism chain
- 1. Trend-following rule (buy breakouts, sell breakdowns) → Path-dependent payoff ~ realised range S_max - S_min: rolling straddles to new highs/lows reproduces breakout trading; lookback delta is long near highs and short near lows _[assertion]_ ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C09-4|C09-4]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C26-5|C26-5]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C28-1|C28-1]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C04-4|C04-4]])
- 2. Long range/lookback straddle → Convex payoff: gains in large moves either way, premium bleed in quiet periods: option payoff; PTFS means insignificant but strongly skewed _[test]_ ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C04-5|C04-5]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C11-1|C11-1]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C21-1b|C21-1b]])
- 3. Extreme world equity months → Large moves in bonds, rates, currencies: common macro shocks _[example]_ ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C17-7b|C17-7b]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C19-1|C19-1]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C17-4|C17-4]])
- 4. Large cross-market moves → Trend followers profit in both equity tails (state-dependent beta): they are long range in the markets that move _[test]_ ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C03-2|C03-2]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C03-3|C03-3]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C17-1|C17-1]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C21-1b|C21-1b]])
- 5. Convex exposure averaging to ~zero linear beta → Linear models report no systematic risk; PTFS factors reveal it: nonlinearity hidden in average beta _[test]_ ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C16-1|C16-1]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C16-3b|C16-3b]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C14-3b|C14-3b]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C25-5|C25-5]])

### Design rationale
- **Model trend following as long lookback straddle rather than a specific technical rule**: captures the whole family's payoff; rules are proprietary and heterogeneous. Alternatives: standard straddle (market timer); technical rules (Alexander 1961). Sensitivity: standard straddles give similar monthly results (corr 0.83-0.92) ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C05-1|C05-1]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C03-6b|C03-6b]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C04-2|C04-2]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C19-3|C19-3]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C20-2|C20-2]])
- **Replicate lookbacks by rolling two exchange-traded straddles, daily at settlement**: lookbacks not traded; delta hedging needs assumed vol and costs more; tick data impractical. Alternatives: delta hedging; continuous rolls. Sensitivity: not shown ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C09-5|C09-5]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C09-7|C09-7]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C10-7|C10-7]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C10-5|C10-5]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C10-1|C10-1]])
- **Three-month horizon, quarterly expiries, nearest-to-money strikes**: liquidity and data availability; consistency across markets. Alternatives: longer options (unreliable data). Sensitivity: authors note 3 months may be too short to separate lookback from standard ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C08-3b|C08-3b]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C10-4|C10-4]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C10-3|C10-3]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C14-2|C14-2]])
- **Equal-weight PTFS portfolios per asset group; CTA index = EW of 407 PC1-correlated funds incl. defunct**: survivorship control; one dominant style. Alternatives: six largest funds (Figure 1). Sensitivity: not shown ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C10-6|C10-6]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C12-1|C12-1]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C14-6|C14-6]])
- **Five equity states by MSCI World return quintile**: show option-like behaviour vs world equity. Alternatives: none. Sensitivity: not shown ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C03-2|C03-2]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C17-3|C17-3]])

### Evidence map
- Adj R2 47.9% on five PTFS portfolios vs 1.0% on eight asset classes and <=7.5% on other indices. Tests: step 5 and the thesis. Rules out: that CTA returns have no systematic market-related risk. Does not rule out: (reader) any convex long-vol factor (e.g. standard straddles, which fit equally) or simple time-series momentum futures returns could explain the same variance; the test does not isolate the lookback feature. Strength: strong - large R2 gap, F-test decisive ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C15-3|C15-3]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C16-1|C16-1]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C16-3b|C16-3b]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C22-4|C22-4]])
- Funds and stock/bond/FX/rate PTFSs gain in both extreme equity states; funds +13% and +10% in 1987 and 1990 crashes. Tests: steps 3-4. Rules out: . Does not rule out: (reader) only two crash episodes and 30-month states in a 1985-97 sample with a falling-rate bond trend. Strength: moderate - consistent but few independent events ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C17-1|C17-1]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C20-1|C20-1]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C21-1b|C21-1b]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C04-1|C04-1]])
- Lookback vs standard straddle correlation 0.86 monthly (yen), 0.83 (CHF), 0.92 (Aus BA). Tests: whether the lookback feature matters empirically. Rules out: . Does not rule out: (reader) a plain market-timing straddle model explains CTAs as well; lookback preference is theoretical. Strength: strong - shows the distinction is not identified at monthly frequency ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C14-1|C14-1]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C19-3|C19-3]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C20-2|C20-2]])
- Individual funds: PTFS avg adj R2 24% vs 11% buy-and-hold; 18 of 21 currency-named funds load only on currency PTFS. Tests: PTFS as attribution/benchmark tool. Rules out: . Does not rule out: (reader) fund names and loadings both reflect the same mandate; still leaves 76% unexplained on average. Strength: moderate ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C23-3|C23-3]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C23-4|C23-4]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C24-3|C24-3]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C24-4|C24-4]])
- Extreme-state regression R2 60.7% on selected PTFSs. Tests: preferred habitat. Rules out: . Does not rule out: (reader) overfitting from pre-selected regressors, acknowledged by authors. Strength: weak - data-mined ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C21-1|C21-1]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C21-2|C21-2]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C22-2|C22-2]])

### Regimes
- Extreme equity months (best or worst 30) → PTFS and trend followers earn large positive returns ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C21-1b|C21-1b]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C17-4|C17-4]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C25-3|C25-3]])
- Middle equity state / quiet markets → PTFSs lose (premium decay); funds still slightly positive ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C21-1b|C21-1b]])
- Steady one-way trend → lookback and standard straddles coincide ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C26-4|C26-4]])
- Trend followed by reversal within the horizon → only the lookback (trend follower) profits ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C26-6|C26-6]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C12-4|C12-4]])
- Short (3-month) horizons, monthly data → lookback vs standard difference largely disappears ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C08-2|C08-2]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C14-1|C14-1]])
- Commodities → no option-like behaviour vs world equities (one outlier) ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C17-5b|C17-5b]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C17-5|C17-5]])

### Gaps and conflicts
- [conflict] The significant 'implicit alpha' (constant ~1.2%/month, t~3.7 in Table 5B; fund mean 1.37% vs insignificant PTFS means) is said to be analysed in Section 4, but Section 4 never returns to it. ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C15-1|C15-1]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C22-4|C22-4]])
- [conflict] State sizes: text says State 3 has 34 months and State 5 the best 30; Table 4 notes say State 5 = best 34 and State 3 = remaining 30. ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C17-3|C17-3]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C21-1b|C21-1b]])
- [conflict] Table 6 does not match text: buy-and-hold R2 said to range -9% to 58% but the table has 3 funds in (-0.2,-0.1) and none above 0.5. ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C23-3|C23-3]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C24-4|C24-4]])
- [conflict] Conclusion lists Japanese yen, Eurodollar and Short Sterling among PTFSs explaining extreme-period returns, while Section 3.4 names only US bonds, DEM, wheat and silver as significant; in Table 5A yen and Eurodollar coefficients are below 1.4 standard errors. ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C25-5b|C25-5b]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C21-1|C21-1]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C22-2|C22-2]])
- [conflict] Table 5C 'statistically significant' set keeps bonds (t~1.4) but drops stocks whose Table 5B coefficient is negative with t~-2.05. ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C22-4|C22-4]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C22-5|C22-5]])
- [data] Figure 1 caption cites Fung and Hsieh (1997a) while the text says it reproduces Exhibit 2 of Fung and Hsieh (1997b); footnote 6 quotes '17 advisors ... 46 of them' above 10%, numerically inconsistent. ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C04-1|C04-1]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C03-6|C03-6]])
- [data] Sample periods differ: Table 1F and Table 5 use 1989-1997, Table 4 Mar 1985-Dec 1997; market histories start 1982-1992 so early PTFS portfolios contain fewer markets. ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C12-2|C12-2]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C17-3|C17-3]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C28-3|C28-3]])
- [untested] PTFS returns ignore bid-offer and roll transaction costs, use American options (downward bias) and nearest strikes; daily (not continuous) rolls approximate the lookback. ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C10-2|C10-2]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C10-3|C10-3]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C10-5|C10-5]])
- [untested] The model is contemporaneous attribution, not a forecast; whether markets trend is explicitly not asserted, and the lookback model is not distinguishable from a standard straddle at monthly frequency. ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C06-4|C06-4]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C14-1|C14-1]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C08-5b|C08-5b]])
- [unspecified] Breakout lookback length and real traders' multiple entries are not modelled. ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C07-5|C07-5]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C04-6|C04-6]])

### Relations to other strategies
- Merton (1981) market timing / standard straddle: **substitute**. market timer = bills + standard straddle; empirically nearly indistinguishable from the lookback model at monthly frequency ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C05-5|C05-5]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C14-1|C14-1]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C20-2|C20-2]])
- Linear style analysis (Sharpe 1992): **contradicts**. linear asset-class regressions explain ~1% and imply no systematic risk ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C02-1|C02-1]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C16-1|C16-1]])
- Mount Lucas/BARRA trend index: **substitute**. rule-based trend index explains only 7.5% vs 47.9% for PTFS ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C16-2|C16-2]])
- Equity crash hedging / long volatility: **complement**. trend followers pay off in extreme equity downturns, reducing portfolio volatility ([[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C25-6|C25-6]], [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C25-4|C25-4]])

### Forward-looking inputs (reader synthesis)
(reader) The paper's factor is contemporaneous, so it does not itself forecast. Its logic implies trend-following P&L ~ realised range (max - min over ~3 months) in currencies, bonds/short rates and commodities minus the option-implied premium for that range. Hence the observable inputs that should lead trend-following returns over the next quarter are (a) the gap between expected realised range/volatility and option-implied volatility in FX, rates and commodities, and (b) the probability of common macro shocks that move many financial markets together. The edge fades when implied vol is rich relative to subsequent realised range, when markets are range-bound or reverse quickly within the window, or when equity tail events are not accompanied by large cross-asset moves.

### Reader inferences (not stated by the authors)
- (reader) Because standard and lookback straddles fit equally at monthly frequency, the evidence supports 'trend followers are long volatility' more than the specific lookback mechanism.
- (reader) The persistent ~1.2%/month constant suggests funds capture the range more cheaply than the option premium (or harvest a trend premium) - an untested source of return.
- (reader) The 1985-97 sample includes the 1987 crash, 1990 Gulf War and a long bond rally, which favour trend followers; results may be sample-specific.
- (reader) PTFS factors can be rebuilt today from listed options (or straddle approximations) to benchmark CTA allocations and to size them as crisis hedges.

## Claims

### C01 (page 1)
- Hedge fund returns are typically option-like, so linear factor models on benchmark asset indices fit them poorly. _(mechanism, premise)_ #mech/research_method
  > Hedge fund strategies typically generate option-like returns.
  ^QP09-C01-1
- Trend-following fund returns are modelled as returns on lookback straddles, which explain them better than standard asset indices. _(construction, design_choice)_ #mech/research_method
  > We use lookback straddles to model trend-following strategies
  exact_rule: trend-following return = T-bill + long three-month lookback straddles on each market (details Section 2)
  ^QP09-C01-2
- Standard straddles give similar empirical results to lookback straddles; lookback straddles are chosen for theoretical closeness to trend following. _(robustness, qualifier)_ #mech/research_method
  > Though standard straddles lead to similar empirical results, lookback straddles are theoretically closer to the concept of trend following.
  reported_result: monthly lookback vs standard straddle correlation 0.86 for yen (Section 2); 0.834 for Swiss franc (Section 3.3) · exhibit: abstract; Section 3.3
  ^QP09-C01-3
- Disclosure: research was supported by a managed-futures foundation and by John W. Henry & Company, a large trend-following CTA, a potential conflict to bear in mind. _(caveat, qualifier)_ #mech/research_method
  > This article received research support from the Foundation for Managed Derivatives Research and John W. Henry & Company.
  ^QP09-C01-4
- The lookback-straddle model is offered as a basis for trend-following fund benchmarks. _(implementation, conclusion, Opus only)_ #mech/research_method
  > Our model should be useful in the design of performance benchmarks for trend-following funds.
  ^QP09-C01-3b
- Hedge funds do not disclose their activities and LTCM (1998) raised concern about their hidden risk, motivating a model of strategy risk. _(caveat, context, Opus only)_ #mech/research_method
  > The near bankruptcy of Long-Term Capital Management (LTCM) in 1998 has further heightened attention on hedge fund risk.
  ^QP09-C01-4b

### C02 (page 2)
- Sharpe-type linear style regressions on asset benchmarks cannot capture the nonlinear (option-like) return features of hedge funds. _(mechanism, premise)_ #mech/research_method
  > Linear-factor models of investment styles using standard asset benchmarks, as in Sharpe (1992), are not designed to capture the nonlinear return features commonly found among hedge funds.
  ^QP09-C02-1
- Linear models can make hedge funds look as if they have no systematic risk, because the risk is nonlinear. _(mechanism, premise)_ #mech/risk_management
  > This may lead investors to conclude erroneously that there are no systematic risks.
  ^QP09-C02-2
- Glosten and Jagannathan (1994): use benchmark indices with embedded option-like features to evaluate funds with nonlinear payoffs. _(citation, evidence)_ #mech/research_method
  > A remedy is in Glosten and Jagannathan (1994), where they suggested using benchmark-style indices that have embedded option-like features.
  ^QP09-C02-3
- Fung and Hsieh (1997a) extracted hedge fund style factors that capture option-like features and are uncorrelated with standard benchmarks, but linking them to markets is hard because funds do not disclose positions. _(citation, evidence)_ #mech/research_method
  > By construction, these style factors captured much of the option-like features while preserving the general lack of correlation with standard asset benchmarks.
  ^QP09-C02-4
- Hedge funds dynamically allocate across strategies with different nonlinear risks, so pooled samples blur risk; the authors instead study one identifiable strategy (trend following, CTA funds). _(mechanism, design_choice)_ #mech/research_method
  > greatly limits the value of analyzing a general sample of many hedge funds
  ^QP09-C02-5
- Trend following is the self-described strategy of most CTAs (Billingsley and Chance 1996), so CTA funds are used as the sample. _(citation, evidence)_ #mech/research_method
  > Trend following is a self-described strategy for the major- ity of commodity trading advisors (CTAs)
  ^QP09-C02-6
- Footnote 3 evidence: linear alpha regressions mislead when payoffs are nonlinear (selling calls gives positive Jensen alpha; Merton 1981 market timing gives option-like returns; Treynor-Mazuy and Henriksson-Merton add nonlinear terms). _(citation, evidence)_ #mech/research_method
  > Grinblatt and Titman (1989) showed that a manager can generate positive Jensen’s alphas by selling call options
  exhibit: footnote 3
  ^QP09-C02-7
- Because funds dynamically mix several nonlinear strategies, studying a general hedge fund sample is of limited value; one should model a single strategy that many funds follow. _(construction, design_choice, Opus only)_ #mech/research_method
  > From a modeling perspective, it is useful to concentrate on a
  ^QP09-C02-3b
- Footnote 3: option-like return features are found even among mutual funds (Lehman and Modest 1987). _(citation, evidence, Opus only)_ #mech/research_method
  > Empirically, Lehman and Modest (1987) found that a number of mutual funds exhibited option-like return features.
  exhibit: footnote 3
  ^QP09-C02-5b

### C03 (page 3)
- Principal component analysis of CTA funds shows one dominant style factor, interpreted as trend following; the model targets that factor and also helps explain other hedge funds that use trend following. _(citation, premise)_ #mech/research_method
  > Fung and Hsieh (1997b) showed that the returns of CTA funds have one dominant style factor.
  ^QP09-C03-1
- Figure 1 (from Fung and Hsieh 1997b): sorting monthly MS World Equity returns into five states, six large trend-following funds earn positive returns in the worst and best states (about +4% in state 1 when world equities average about -9.5%; about +4.5% in state 5 when equities gain about +10%) and little in the middle. _(result, evidence)_ #mech/risk_premium
  > State 1 consists of the worst months, and State 5 the best months.
  reported_result: Figure 1 read from chart: world equities by state about -9.5%, -2%, +1.3%, +4.4%, +10%; six trend followers about +4%, +2%, +1.3%, +2.8%, +4.5% monthly · exhibit: Figure 1 · conditions: sample ends 1997
  ^QP09-C03-2
- Trend followers have low average beta to equities but beta is positive in up markets and negative in down markets, i.e. a convex, option-like payoff. _(mechanism, mechanism_step)_ #mech/research_method
  > the state-dependent beta estimates tend to be positive in up markets and nega- tive in down markets
  exhibit: Figure 1
  ^QP09-C03-3
- Contingent-claim-like returns mean trend followers must bear systematic risk, which linear betas can understate or overstate (the LTCM case). _(mechanism, mechanism_step)_ #mech/risk_premium
  > must therefore have systematic risk, albeit in a nonlinear manner
  ^QP09-C03-4
- Caveat: trading rules are proprietary, so the model is a theoretical proxy, not a replication of any manager. _(caveat, qualifier)_ #mech/research_method
  > We can therefore only theorize what trend followers do.
  ^QP09-C03-5
- Out-of-sample support (footnote 6): in August 1998 the S&P 500 fell 14.5% while commodity funds generally gained; per Barron's, 82% of 17 CTAs reporting to MAR were positive and 46 posted more than 10%. _(result, evidence)_ #mech/risk_management
  > While the S&P 500 lost 14.5% of its value, commodity funds generally had positive returns.
  reported_result: Aug 1998: S&P 500 -14.5%; 82% of CTAs positive · exhibit: footnote 6
  ^QP09-C03-6
- Trading rules are proprietary, so the authors can only theorise what trend followers do rather than estimate risk directly. _(caveat, qualifier, Opus only)_ #mech/research_method
  > traders regard their trading systems to be proprietary and are reluctant to disclose them.
  ^QP09-C03-6b
- Footnote 5: CTAs are CFTC-registered advisors (via NFA membership) who trade mainly futures for clients. _(construction, context, Opus only)_ #mech/research_method
  > who trade primarily futures contracts on behalf of a customer.
  exhibit: footnote 5
  ^QP09-C03-8b

### C04 (page 4)
- Figure 1 caption: average monthly returns of six large trend-following funds in five MS world equity market states; source Fung and Hsieh (1997a). _(result, evidence)_ #mech/risk_premium
  > Average monthly returns of six large trend-following funds in
  reported_result: see Figure 1 claim · exhibit: Figure 1
  ^QP09-C04-1
- Individual trend followers differ in entry and exit rules, so a stylised aggregate strategy is needed to capture the common payoff while avoiding idiosyncrasies. _(mechanism, design_choice)_ #mech/research_method
  > Trend followers can converge onto the same “trend” for different reasons and have very different “entry and exit” points.
  ^QP09-C04-2
- Primitive trend-following strategy (PTFS) is posited to have the same payout as a lookback straddle: long lookback call (buy at lowest price over life) plus lookback put (sell at highest price), paying the ex post maximum price range of the underlying. _(construction, mechanism_step)_ #mech/research_method
  > has the same payout as a structured option known as the “lookback straddle.”
  exact_rule: PTFS payout = S_max - S_min over the option life; cost = lookback straddle premium
  ^QP09-C04-3
- The lookback straddle gives the ex post maximum payout of any trend-following strategy, i.e. the perfect-foresight upper bound. _(mechanism, mechanism_step)_ #mech/research_method
  > which delivers the ex post maximum payout of any trend-following strategy
  ^QP09-C04-4
- Prediction: trend-follower returns resemble bills plus a portfolio of lookback straddles. _(mechanism, premise)_ #mech/research_method
  > trend followers should deliver returns resembling those of a portfolio of bills and lookback straddles
  ^QP09-C04-5
- Footnote 7: the model excludes multiple entries and exits within the horizon that real trend followers make when volatility around a trend is high. _(caveat, qualifier)_ #mech/research_method
  > trend followers often make multiple entry and exit decisions over a
  exhibit: footnote 7 · conditions: simplification: single trade per interval
  ^QP09-C04-6

### C05 (page 5)
- The option strategy is not tuned to replicate a specific trading rule (unlike earlier technical-rule studies) but to capture the general features of all trend-following strategies. _(construction, design_choice)_ #mech/research_method
  > Rather, it is designed to capture the general characteristics of the entire family of trend-following strategies.
  ^QP09-C05-1
- The key empirical link: lookback straddle returns resemble trend-following fund returns, connecting funds to standard asset markets. _(mechanism, mechanism_step)_ #mech/research_method
  > This provides the key link between the returns of trend-following funds and standard asset markets.
  ^QP09-C05-2
- Theory (Section 1, Appendix A): a lookback straddle captures trend following better than a standard straddle, which captures market timing. _(mechanism, mechanism_step)_ #mech/research_method
  > Given any asset, we show that the lookback straddle is better suited to capture the essence of trend-following strategies than a simple straddle.
  ^QP09-C05-3
- Merton (1981): with short-sale constraints a perfect market timer earns R + max{0, Z-R}, i.e. bills plus a call on stocks. _(citation, evidence)_ #mech/research_method
  > which is the return of a portfolio of bills and a call option on stocks
  exact_rule: R(t)+Max{0,Z(t)-R(t)}
  ^QP09-C05-4
- Without short-sale constraints a perfect market timer earns R + max{0,Z-R} + max{0,R-Z}, bills plus a straddle on stocks (Merton 1981). _(citation, evidence)_ #mech/research_method
  > which is the return of a portfolio of bills and a straddle on stocks.
  exact_rule: R(t)+Max{0,Z(t)-R(t)}+Max{0,R(t)-Z(t)}
  ^QP09-C05-5
- Trend followers allocate capital dynamically across markets in ways peculiar to their skill and technology, which complicates benchmarking. _(caveat, qualifier)_ #mech/research_method
  > Here we note the opportunistic nature of trend followers.
  ^QP09-C05-6
- The convex pattern in Figure 1 resembles a straddle payout on the underlying asset. _(mechanism, mechanism_step, Opus only)_ #mech/new
  > The convex return pattern observed in Figure 1 resembles the payout
  ^QP09-C05-2b

### C06 (page 6)
- Trend defined as persistent one-directional price movement with positive serial correlation of price changes; a trend follower trades in the direction of a developing pattern. _(construction, premise)_ #mech/cycle_persistence
  > A trend is a series of asset prices that move persistently in one direction over a given time interval, where price changes exhibit posi- tive serial correlation.
  ^QP09-C06-1
- PMTS (market timer) payout is |S'-S| (initial vs end price); PTFS payout is S_max - S_min (largest movement inside the interval), so PTFS adds trades at the max and min. _(construction, design_choice)_ #mech/research_method
  > The PTFS, on the other hand, attempts to capture the largest price movement during the time interval.
  exact_rule: PMTS payout = |S_end - S_start|; PTFS payout = S_max - S_min; one trade per interval
  ^QP09-C06-2
- Both primitive strategies complete a single trade per interval, following Merton (1981). _(construction, design_choice)_ #mech/research_method
  > Consistent with the Merton (1981) framework, we restrict our strategies to complete a single trade over the given time interval.
  exact_rule: one trade per interval
  ^QP09-C06-3
- Key caveat (footnote 9): the paper does not claim markets trend; it only models and risk-characterises trend-following funds, leaving the profitability or serial correlation of trends untested. _(caveat, qualifier)_ #mech/research_method
  > Note that we are not advocating that markets trend. That is an empirical issue best deferred to another occasion.
  exhibit: footnote 9
  ^QP09-C06-4
- Capital is split between the primitive strategy and the risk-free asset by comparing payout to the risk-free return (option premium vs bills); footnote 11 says the split also depends on risk preference. _(construction, design_choice)_ #mech/research_method
  > Capital allocation to the PMTS or PTFS is determined by comparing the payout of the respective strategy to the return of the risk-free asset.
  exhibit: footnote 11
  ^QP09-C06-5
- Market timers trade in anticipation of a move; trend followers trade only after observing certain price movements within the period (buying breakouts, selling breakdowns). _(mechanism, mechanism_step)_ #mech/slow_reaction
  > Generally, market timers enter into a trade in anticipa- tion of a price move over a given time period, whereas trend followers trade
  ^QP09-C06-6
- Footnote 10: under strict Merton assumptions PTFS and PMTS payouts coincide; the difference arises from path dependence. _(caveat, qualifier)_ #mech/research_method
  > if Merton’s (1981) assumptions were strictly imposed, the payout of the PTFS must equal that of the PMTS.
  exhibit: footnote 10
  ^QP09-C06-7

### C07 (page 7)
- Trend followers buy breakouts (price above recent high) and sell breakdowns (price below recent low). _(construction, design_choice)_ #mech/cycle_persistence
  > The terms buying breakouts and selling breakdowns are often used to describe trend followers.
  exact_rule: long when price breaks above recent high; short when below recent low (footnote 12) · exhibit: footnote 12
  ^QP09-C07-1
- Costs of capturing the optimal payout cannot be estimated without the strategies, so the PMTS cost is assumed to be an at-the-money standard straddle and the PTFS cost a lookback straddle. _(construction, design_choice)_ #mech/research_method
  > we assume that the ex ante cost of the PMTS is the value of an at-the-money standard straddle
  exact_rule: PMTS = long ATM straddle; PTFS = long lookback straddle
  ^QP09-C07-2
- PTFS returns are built from lookback straddles on 26 markets. _(construction, design_choice)_ #mech/research_method
  > In the next section, we will empirically create returns of the PTFS using lookback straddles on 26 different markets.
  exhibit: Table 1
  ^QP09-C07-3
- Black-Scholes deltas: standard straddle delta = 2N(a1)-1; lookback straddle delta is path dependent through the running minimum Q and maximum M (Equations 1-12); a derivation is available on request. _(construction, mechanism_step)_ #mech/research_method
  > In comparison, the delta of the lookback straddle is given by
  exact_rule: delta_std = 2N(a1)-1, a1=[ln(S/X)+(r+0.5 sigma^2)T]/(sigma sqrt T); delta_LB per Eq. 3 with Q=min, M=max since inception · exhibit: Equations 1-12
  ^QP09-C07-4
- Footnote 12: definitions of breakout and breakdown. _(construction, context)_ #mech/cycle_persistence
  > Breakout means that the price of an asset moves above a recent high, and buying breakouts refers to the strategy of going long when a breakout happens.
  exhibit: footnote 12
  ^QP09-C07-5

### C08 (page 8)
- Lookback delta uses Q = minimum and M = maximum price since inception; the key difference from a standard straddle is path dependency. _(construction, mechanism_step)_ #mech/research_method
  > Here Q and M denote the minimum and maximum prices, respectively, of the asset since the inception of the lookback straddle.
  exhibit: Equations 3-12
  ^QP09-C08-1
- PMTS and PTFS payouts are equal only if S_max and S_min occur at the start and end; they converge as the horizon shrinks and diverge as it lengthens. _(mechanism, mechanism_step)_ #mech/research_method
  > Consequently, as the investment horizon shrinks, the payouts of the two strategies converge.
  conditions: horizon: short -> same payout; long -> differ
  ^QP09-C08-2
- Three-month options are used because they are the most liquid, although this horizon may be too short to separate lookback from standard straddles. _(construction, design_choice, Opus only)_ #mech/research_method
  > In the empirical implementation, we use three-month options, which tend to be the most liquid options
  exact_rule: option horizon = 3 months
  ^QP09-C08-3b
- The goal is only to show that one bills-plus-lookback-straddle portfolio behaves like trend followers; other option portfolios might replicate better. _(caveat, qualifier, Opus only)_ #mech/research_method
  > We do not attempt to answer the question of which option portfolio best describes the returns of trend- following funds.
  ^QP09-C08-5b

### C09 (page 9)
- Universe, financial markets: 5 stock index futures (S&P 500, Nikkei 225, FTSE 100, DAX 30, Australian All Ordinary), 5 bond futures (US 30y, UK Gilt, Bund, French 10y, Australian 10y), 4 currency futures (GBP, DEM, JPY, CHF), 6 three-month rate futures. _(construction, design_choice)_ #mech/research_method
  > For stock indices, we used the futures contracts on the S&P 500 (CME), Nikkei 225 (Osaka), FTSE 100 (LIFFE), DAX 30 (DTB),
  exact_rule: stocks 5, bonds 5, currencies 4, 3-month rates 6 (26 markets total incl. commodities) · data_needed: futures and options on CME, Osaka, LIFFE, DTB, SFE, MATIF, TIFFE, CBOT · exhibit: Section 2; Appendix B
  ^QP09-C09-1
- Universe, commodities: soybean, wheat, corn (CBOT), gold, silver, crude oil (NYMEX). _(construction, design_choice)_ #mech/research_method
  > For commodities, we used the futures contracts on soybean, wheat, and corn futures traded on the CBOT and gold, silver, and crude oil
  exhibit: Section 2
  ^QP09-C09-2
- Data: exchange-supplied or purchased futures and options settlement data plus Datastream futures (Appendix B). _(construction, design_choice)_ #mech/research_method
  > Futures and option data on the DTB, MATIF, and Osaka were purchased from the Futures Industry Institute (FII).
  data_needed: exchange futures and option settlement prices
  ^QP09-C09-3
- Lookback options are not traded, so their payout is replicated by rolling a pair of standard straddles (Goldman, Sosin, Gatto 1979). _(construction, design_choice)_ #mech/research_method
  > First, lookback options are not exchange-traded contracts, so we can- not directly observe their prices.
  ^QP09-C09-4
- Replication rule, high straddle: roll to a higher strike whenever the underlying exceeds the current strike so the final strike equals the running maximum. _(construction, design_choice)_ #mech/research_method
  > We use one strad- dle to lock in the high price of the underlying asset by rolling this straddle to a higher strike whenever the price of the underlying asset moves above the current strike.
  exact_rule: buy 2 ATM straddles at inception; straddle 1 rolled up whenever price > current strike
  ^QP09-C09-5
- Replication rule, low straddle: roll to a lower strike whenever the underlying falls below the current strike so the final strike equals the running minimum; the pair pays max minus min. _(construction, design_choice)_ #mech/research_method
  > We use the other straddle to lock in the lowest price of the underlying asset by rolling the straddle to a lower strike whenever
  exact_rule: straddle 2 rolled down whenever price < current strike; combined payout = S_max - S_min
  ^QP09-C09-6
- Footnote 14: delta hedging is an alternative but needs implied volatility of an untraded option. _(construction, context)_ #mech/research_method
  > An alternative replication strategy is a delta-hedging strategy using the underlying asset.
  exhibit: footnote 14
  ^QP09-C09-7
- Data: futures and options from the Futures Industry Institute (DTB, MATIF, Osaka, CME options), the exchanges (LIFFE, SFE, TIFFE; CBOT/NYMEX options) and Datastream (CBOT, CME, NYMEX futures). _(construction, context, Opus only)_ #mech/research_method
  > Futures data on the CBOT, CME, and NYMEX came from Datastream.
  data_needed: FII, LIFFE, SFE, TIFFE, CBOT, NYMEX, CME, Datastream
  ^QP09-C09-2b

### C10 (page 10)
- Straddle rolls create extra cash flows that a true lookback straddle does not have; these are included in returns. _(caveat, qualifier)_ #mech/research_method
  > Second, though the strategy of rolling standard straddles can replicate the payout of the lookback straddle, it may not perfectly replicate all the cash
  conditions: cash flows from strike rolls included
  ^QP09-C10-1
- Most US-exchange options are American style and cost more than European, biasing PTFS returns downward; LIFFE options are futures-style so unaffected. _(caveat, qualifier)_ #mech/research_method
  > This biases downward the returns of the PTFS.
  ^QP09-C10-2
- Nearest-to-the-money options substitute for at-the-money (discrete strikes); authors judge the error small. _(caveat, qualifier)_ #mech/research_method
  > we use the nearest-to-the- money options to approximate at-the-money options. The error is likely to be small.
  ^QP09-C10-3
- Horizon: three-month lookback straddles, set as close to quarter-end as possible, because financial options expire quarterly and commodity options mostly in Mar/Jun/Sep/Dec. _(construction, design_choice)_ #mech/research_method
  > we used lookback straddles with three months to expiration as close to the end of a quarter as possible to maintain consistency.
  exact_rule: three-month lookback straddle initiated near quarter-end; horizon dictated by option liquidity
  ^QP09-C10-4
- Rolling is done daily at settlement prices, not continuously (tick data costly and asynchronous), then daily returns compound to monthly. _(construction, design_choice)_ #mech/research_method
  > In practice, we rolled the straddles only at the end of each trading day using the settlement prices of the options and the underlying assets.
  exact_rule: roll straddles at daily settlement; aggregate daily returns to monthly · conditions: approximation to continuous rolling
  ^QP09-C10-5
- Five PTFS portfolios (stocks, bonds, three-month rates, currencies, commodities) formed as equally weighted PTFSs. _(construction, design_choice)_ #mech/research_method
  > one each for stocks, bonds, three-month interest rates, currencies, and commodities.
  exact_rule: five equal-weighted portfolios of market PTFSs · exhibit: Table 1; Panel G
  ^QP09-C10-6
- Footnote 14: delta hedging would incur substantial transaction costs; straddle rolling needs far fewer transactions. _(caveat, design_choice)_ #mech/research_method
  > a delta-hedging strategy can incur substantial transaction costs, as it requires dynamically changing the amount of the underlying asset every time its price changes.
  exhibit: footnote 14
  ^QP09-C10-7

### C11 (page 11)
- Table 1A-E: monthly PTFS means are mostly small and insignificant and often negative (S&P -1.6%, Nikkei -4.7%, gold -5.4% a, silver -5.0% b, crude +4.6% b, Swiss franc +5.0% a, Euro-Yen +7.5% c); monthly SD about 16-48%. _(result, evidence)_ #mech/research_method
  > Statistical properties of primitive trend-following strategy (PTFS) returns for 26 markets and
  reported_result: Table 1 (monthly PTFS, sample varies by market, ends Dec 1997): means S&P -0.0161, FTSE -0.0177, DAX 0.0437c, Nikkei -0.0470, Aus All Ord -0.0304c; US30Y 0.0136, Gilt 0.0097, Bund 0.0321c, French 10Y 0.0157, Aus 10Y 0.0189; Euro$ 0.0170, Sterling 0.0449c, Euro-DM -0.0375, Euro-Yen 0.0750c, ABA 0.0453, PIBOR 0.0513c; GBP 0.0174, DM 0.0232, JPY 0.0455c, CHF 0.0496a; corn -0.0135, wheat 0.0435c, soybean -0.0355c, crude 0.0455b, gold -0.0539a, silver -0.0502b · exhibit: Table 1 Panels A-E
  ^QP09-C11-1
- Every individual PTFS is strongly positively skewed (skewness 0.71 to 3.83, all significant at 1%); share of positive months only 30-50%. _(result, evidence)_ #mech/risk_premium
  > Before proceeding to compare the PTFS returns to trend-following funds’
  reported_result: Table 1A-E skewness: S&P 3.83, FTSE 0.71, DAX 1.19, Nikkei 1.72, Aus 0.88; US30Y 1.55 ... Euro-DM 3.20, Euro-Yen 2.38; GBP 1.73, JPY 1.67; crude 2.93; % positive 30-50; monthly SD 0.1627 (Aus All Ord) to 0.4780 (ABA); max up to 2.5, min about -0.77 · exhibit: Table 1 Panels A-E
  ^QP09-C11-2

### C12 (page 12)
- Trend-following fund return series = equal-weighted portfolio of 407 defunct and live CTA funds significantly correlated with the first principal component of 1,304 funds. _(construction, design_choice)_ #mech/research_method
  > are based on an equally weighted portfolio of 407 defunct and operating commodity funds that had
  exact_rule: equal-weight 407 of 1304 CTA funds with significant correlation to PC1 · data_needed: Tass CTA database as of March 1998 · exhibit: Table 1 note
  ^QP09-C12-1
- Table 1F (1989-97): trend-following funds mean +1.37% a month (significant at 1%), SD 4.91%, skew 0.79; PTFS portfolios have much larger SD and insignificant means (stock -1.93%, bond 1.81%, rates 1.95%, currency 1.77%, commodity -0.72%). _(result, evidence)_ #mech/risk_premium
  > are equally weighted portfolios of the PTFSs in the
  reported_result: Table 1F: TF funds mean 0.0137a, SD 0.0491, max 0.1837, min -0.0820, skew 0.79a; Stock PTFS -0.0193/0.2094/skew 2.62a; Bond 0.0181/0.1573/1.07a; Interest rate 0.0195/0.1867/1.46a; Currency 0.0177/0.2305/1.68a; Commodity -0.0072/0.1310/1.19a · exhibit: Table 1 Panel F
  ^QP09-C12-2
- Correlations among the five PTFS portfolios are low to moderate: stock-bond 0.37, stock-commodity 0.37, bond-rate 0.32, rate-currency 0.36, others 0.06-0.21. _(result, evidence)_ #mech/research_method
  > Panel G: Correlation matrix of the
  reported_result: Table 1G: Stock-Bond 0.37, Stock-IR 0.06, Stock-Currency 0.16, Stock-Commodity 0.37, Bond-IR 0.32, Bond-Currency 0.21, Bond-Commodity 0.12, IR-Currency 0.36, IR-Commodity 0.07, Currency-Commodity 0.18 · exhibit: Table 1 Panel G
  ^QP09-C12-3
- Yen March 1994 example (Figure 2): futures 0.9199 on 30 Nov 1993, low 0.8878 early Jan, high 0.9780 mid-Feb, end 0.9459; lookback straddle pays 0.0902 vs standard straddle 0.0260 because min and max occurred mid-period. _(result, evidence)_ #mech/research_method
  > the payout of the lookback straddle (0.0902) was substantially greater than that of the standard straddle (0.0260).
  reported_result: lookback payout 0.0902 vs standard 0.0260 (Mar 1994 JY futures) · exhibit: Figure 2
  ^QP09-C12-4
- Yen September 1990 example (Figure 3): futures 0.6591 on end May, low 0.6444 end June, high 0.7147 at expiry; lookback 0.0703 vs standard 0.0556 since min and max were near start and end. _(result, evidence)_ #mech/research_method
  > the payout of the lookback straddle (0.0703) was much closer to that of the standard straddle (0.0556).
  reported_result: lookback payout 0.0703 vs standard 0.0556 (Sep 1990 JY futures) · exhibit: Figure 3
  ^QP09-C12-5

### C13 (page 13)
- Figures 2-3 chart: in March 1994 yen the lookback straddle rises steadily from 100 to about 165 while the standard straddle ends near 60 after a spike; in September 1990 both finish near 190-210. _(result, evidence)_ #mech/research_method
  > Standardized cumulative returns of the lookback straddle and the standard straddle on the March 1994
  reported_result: Figure 2 read from chart: lookback about 165, standard about 60 (base 100 on 11/30/93); Figure 3: lookback about 190, standard about 210 (base 100 on 5/31/90) · exhibit: Figures 2, 3
  ^QP09-C13-1
- Figure 3 (read from chart): with a steady rise into expiry both straddles end at similar levels (about 220-230 from 100). _(result, evidence, Opus only)_ #mech/research_method
  > 1990 Japanese yen futures contract
  reported_result: Figure 3 (chart): both straddles ~100 -> ~220-230 (May-Sep 1990) · exhibit: Figure 3
  ^QP09-C13-2b

### C14 (page 14)
- Yen, March 1986 to December 1997: daily correlation of lookback and standard straddle returns 0.39 but monthly correlation 0.86, so at the monthly interval the PMTS and PTFS are hard to distinguish. _(result, evidence)_ #mech/research_method
  > The daily returns of the two types of straddles on the Japanese yen had a correlation of 0.39, and their monthly returns had a correlation of 0.86.
  reported_result: Japanese yen straddles: daily corr 0.39, monthly corr 0.86 (Mar 1986-Dec 1997) · exhibit: Section 2 text
  ^QP09-C14-1
- Constraints: quarterly options (longer-dated data unreliable) and monthly fund returns (higher frequency fund data scarce) make standard and lookback straddles empirically similar. _(caveat, qualifier)_ #mech/research_method
  > We are empirically constrained to use quarterly options because data for longer-dated options are generally unreliable and, in most cases, unavailable.
  conditions: may not hold at other return intervals
  ^QP09-C14-2
- Lookback straddle is used in all empirical tests, chosen on theory rather than empirical superiority. _(construction, design_choice)_ #mech/research_method
  > Consequently, we apply the lookback straddle in our empirical tests given its superior theoretical properties.
  ^QP09-C14-3
- PCA on defunct and operating CTA funds yields one dominant style (trend following); the study updates this with the Tass CTA database as of March 1998. _(citation, evidence)_ #mech/research_method
  > Applying principal components analysis on all defunct and operating CTA funds, Fung and Hsieh (1997b) found a single dominant trading style.
  data_needed: Tass CTA database (March 1998)
  ^QP09-C14-4
- Of 1,304 funds, 407 are strongly correlated with the first principal component and form the representative trend-follower return series. _(construction, design_choice)_ #mech/research_method
  > Out of 1304 defunct and operating CTA funds, 407 are strongly corre- lated to the
  reported_result: 407 of 1304 CTA funds · exhibit: Section 3.1
  ^QP09-C14-5
- Footnote 15: defunct funds are included to avoid survivorship bias, which would otherwise bias fund returns upward. _(caveat, qualifier)_ #mech/research_method
  > This is likely to result in an upward bias, because the omitted defunct funds generally have poorer performance than surviving funds.
  exhibit: footnote 15
  ^QP09-C14-6
- Trend-following fund returns correlate strongly with PTFS returns, which means they carry systematic risk that linear models on asset indices miss. _(mechanism, conclusion, Opus only)_ #mech/new
  > This is consistent with the notion that trend-following funds have systematic risks, contrary to the prediction of linear-factor models applied to standard asset benchmarks.
  ^QP09-C14-3b

### C15 (page 15)
- Funds and PTFS share strong positive skewness, but funds have a significant positive mean (+1.37% monthly) while PTFS portfolios and most PTFSs do not; funds beat PTFS means except for the Swiss franc. _(result, evidence)_ #mech/risk_premium
  > mean, whereas the PTFS portfolios and most of the individual PTFSs do not.
  reported_result: Table 1F: TF funds mean +1.37%/month vs PTFS portfolios -1.93% to +1.95% · exhibit: Table 1
  ^QP09-C15-1
- The authors flag a positive implicit alpha in trend-following funds relative to PTFS, deferring analysis (Section 4 does not actually quantify it). _(caveat, qualifier)_ #mech/research_method
  > We defer further analysis of this implicit alpha in trend-following funds’ returns until Section 4.
  ^QP09-C15-2
- Table 2: adjusted R-squared of trend-follower returns on standard sets is near zero. _(result, evidence)_ #mech/research_method
  > Next, we document the apparent lack of systematic risk in trend-following funds’ returns in standard linear-factor models in Table 2.
  reported_result: Table 2 adjusted R2: eight asset classes 1.0%; five stock indices -2.1%; five bond markets 7.5%; six 3m rate markets 1.5%; four currencies -1.1%; six commodities -3.2%; GSCI -0.7%; CRB -0.8%; Mount Lucas/BARRA trend index 7.5%; five PTFS portfolios 47.9% · exhibit: Table 2
  ^QP09-C15-3
- Funds' mean exceeds nearly every individual PTFS mean with greater statistical significance. _(result, evidence)_ #mech/research_method
  > With the exception of the PTFS for the Swiss franc, trend-following funds’ returns
  exhibit: Table 1
  ^QP09-C15-4

### C16 (page 16)
- Adjusted R-squared of trend-follower returns on standard benchmarks: eight asset classes 1.0%, five stock markets -2.1%, five bond markets 7.5%, six 3m rates 1.5%, four currencies -1.1%, six commodities -3.2%. _(result, evidence)_ #mech/research_method
  > An investor using a linear-factor model on stan- dard asset benchmarks would have concluded that trend followers had no systematic risk.
  reported_result: Table 2 sets 1-6 adjusted R2: 1.0, -2.1, 7.5, 1.5, -1.1, -3.2 (%) · exhibit: Table 2
  ^QP09-C16-1
- GSCI Total Return adjusted R2 -0.7%, CRB -0.8% (both insignificant), Mount Lucas/BARRA Trend-Following Index 7.5% (significant but small). _(result, evidence)_ #mech/research_method
  > Other indices frequently associated with commodity traders and trend fol- lowers produced similarly poor results.
  reported_result: Table 2 sets 7-9: -0.7, -0.8, 7.5 (%) · exhibit: Table 2
  ^QP09-C16-2
- Regression of trend-following funds on the five PTFS portfolios gives adjusted R2 of 47.9%, with currency and commodity PTFS largest; the F-test rejects no relation. _(result, evidence)_ #mech/research_method
  > is rejected at any conventional
  reported_result: Table 2 set 10: adjusted R2 47.9% (five PTFS portfolios) vs 1.0% for eight asset classes · exhibit: Table 2; Table 5 Panel B
  ^QP09-C16-3
- Interpretation: trend followers have systematic risk that linear models on standard benchmarks miss but PTFS capture. _(mechanism, conclusion)_ #mech/risk_premium
  > This indicates that trend followers do have systematic risks.
  ^QP09-C16-4
- Figure 4 scatter plots: stock PTFS shows no apparent relation to funds; currency and commodity PTFS show the strongest relation, currency approximately linear; residual plots show no remaining nonlinearity. _(robustness, evidence)_ #mech/research_method
  > the relationship between the currency PTFS returns and the trend-following funds’ returns appear reasonably linear.
  reported_result: Figure 4 read from charts: currency PTFS up to about 100% when funds gain about 17%; commodity PTFS up to about 65%; stock PTFS flat · exhibit: Figure 4
  ^QP09-C16-5
- Residual diagnostics show no remaining nonlinearity (plots not shown). _(robustness, evidence)_ #mech/research_method
  > Plots of the residuals of the regression against the explanatory variables (available from the authors on request) do not show any remaining nonlinear relationships.
  reported_result: not shown
  ^QP09-C16-6
- The five PTFS portfolios explain 47.9% of trend-following returns, mostly via currencies and commodities; the joint F-test of no relation is rejected decisively. _(result, evidence, Opus only)_ #mech/new
  > The F -test that none of the PTFS portfolios is correlated with the trend-following funds’ returns is rejected at any conventional
  reported_result: 5 PTFS portfolios adj R2 47.9%; currencies and commodities most explanatory; F-test rejects at any level · exhibit: Table 2; Table 5 Panel B
  ^QP09-C16-3b

### C17 (page 17)
- Trend followers gained 13.0% in Sep-Nov 1987 (MS World -20.4%) and 10.2% in Aug-Sep 1990 (MS World -18.9%); stock PTFS positive, and bond, currency and commodity PTFS mostly positive; fewer than half of 3m rate PTFS profitable. _(result, evidence)_ #mech/risk_management
  > Trend-following funds recorded large positive returns of 13.0% and 10.2% during these two periods, respectively.
  reported_result: Table 3A: MS World -0.2036 / -0.1889; trend-following funds +0.1299 / +0.1019 (8709-8711, 9008-9009) · exhibit: Table 3
  ^QP09-C17-1
- In the two equity crashes the bond, currency and commodity PTFS mostly earned positive returns, not just stocks. _(result, evidence)_ #mech/risk_management
  > The less obvious results were the positive returns from the PTFSs for most of the government bonds, currencies, and commodities.
  reported_result: Table 3: Bond PTFS 0.2725 / 0.3557; Currency PTFS 0.7758 / 0.1832; Commodity PTFS 0.0220 / 0.8525; Stock PTFS 2.1060 / 0.7744; IR PTFS 0.8194 / -0.1372 · exhibit: Table 3
  ^QP09-C17-2
- State sort, March 1985-December 1997: five states from MS World Equity monthly returns (worst 30 months averaged -4.60%, next 30 -0.59%, best 30 +6.74%, next best +3.36%, remaining 34 months in the middle). _(construction, design_choice)_ #mech/research_method
  > Here we divided the longer time series for which there were data for all PTFSs (March 1985 to December 1997) into
  exact_rule: sort months by MS World Equity return into five states (30/30/34/30/30); average PTFS returns by state · data_needed: MS World Equity Index, PTFS returns · exhibit: Table 4
  ^QP09-C17-3
- Stock, bond, 3m-rate and currency PTFS have high average returns in extreme equity states 1 and 5 (convex, option-like); commodity PTFS does not. _(result, evidence)_ #mech/risk_management
  > the returns of the PTFSs tended to be high during extreme states 1 and 5 for stocks
  reported_result: Table 4 state 1/state 5 mean PTFS: stock 0.1281/0.0941; bond 0.0591/0.1017; currency 0.0827/0.0821; rate 0.0832/0.0560; commodity 0.0121/-0.0245; state 3: stock -0.0553, bond -0.0518, currency -0.0058, rate -0.0108, commodity -0.0188 · exhibit: Table 4
  ^QP09-C17-4
- Footnote 16: commodity PTFS missed the state-1 pattern mainly because of one outlier. _(caveat, qualifier)_ #mech/research_method
  > The low average return for the commodity PTFS in state 1 was primarily due to one outlier.
  exhibit: footnote 16
  ^QP09-C17-5
- In those crash periods stock PTFSs paid off as expected, and so did most bond, currency and commodity PTFSs, but fewer than half of the short-rate PTFSs. _(result, evidence, Opus only)_ #mech/research_method
  > However, less than half of the PTFSs for three-month interest rates were
  exhibit: Table 3
  ^QP09-C17-2b
- Commodity PTFSs do not show the option-like pattern versus world equities. _(result, evidence, Opus only)_ #mech/research_method
  > However, the PTFSs on commodities did not exhibit this option-like behavior.
  exhibit: Table 4
  ^QP09-C17-5b
- Financial assets (stocks, bonds, short rates, currencies) react to the same macro events, so extreme equity moves coincide with large moves, and trend profits, in the other financial markets. _(mechanism, mechanism_step, Opus only)_ #mech/new
  > month interest rates, and currencies) should respond to the same set of
  conditions: common macro shocks
  ^QP09-C17-7b

### C18 (page 18)
- Figure 4 (first panels): stock PTFS shows no relation to trend-following funds; bond and 3m-rate PTFS show diffuse positive relation. _(robustness, evidence)_ #mech/research_method
  > Scatter plots of monthly trend-following funds’ returns versus
  reported_result: read from chart: stock PTFS range about -50% to +130%, flat relation; bond PTFS up to about 45%; 3m rate PTFS up to about 80% · exhibit: Figure 4
  ^QP09-C18-1

### C19 (page 19)
- Mechanism: financial assets respond to the same macro events, and extreme moves have come from common shocks (e.g. the 1990 Gulf War oil shock) moving all markets in concert, so trend followers profit across markets in crises. _(mechanism, mechanism_step)_ #mech/risk_management
  > macroeconomic events. Historically, extreme moves tended to be caused by a common set of dramatic events
  ^QP09-C19-1
- Standard straddle check on Swiss franc (highest correlation) and Sydney bankers acceptance (lowest): lookback vs standard correlations 0.834 (CHF) and 0.924 (ABA). _(robustness, evidence)_ #mech/research_method
  > We investigated this for two markets: the Swiss franc futures contract because its PTFS returns were most highly correlated to trend-following funds’ returns
  reported_result: CHF lookback vs standard straddle corr 0.834; ABA 0.924 · exhibit: Section 3.3
  ^QP09-C19-2
- Figure 4 (continued): currency and commodity PTFS scatter plots against funds are the most striking positive relationships. _(robustness, evidence)_ #mech/research_method
  > For the Swiss franc, lookback straddle returns had a correlation of 0.834 with those of standard straddles.
  reported_result: read from chart: commodity PTFS up to about 65%, currency PTFS up to about 100% for fund returns up to 17% · exhibit: Figure 4 (continued)
  ^QP09-C19-3

### C20 (page 20)
- Table 3 detail: crash-period PTFS returns by market, e.g. crude oil PTFS +544% in Aug-Sep 1990 (Gulf War), Eurodollar +82% and S&P PTFS +211% in Sep-Nov 1987, British pound +134% (1987); wheat and silver missing for 1987. _(result, evidence)_ #mech/risk_management
  > Large PTFS returns during the two worst periods for world equities
  reported_result: Table 3 (period 8709-8711 / 9008-9009): S&P 500 2.1060 / 0.7744; US30Y 0.3187 / 0.3670; UK Gilt 0.0753 / -0.0513; Bund n.a. / 0.1257; French10Y n.a. / 1.0377; Euro-Dollar 0.8194 / -0.0052; Sterling n.a. / -0.0898; Euro-DM n.a. / -0.3145; PIBOR n.a. / 0.4268; GBP 1.3368 / 0.1887; DM 0.5401 / -0.0599; JPY 0.3842 / 0.0882; CHF 0.7448 / 0.5165; corn 0.1494 / 0.4336; wheat n.a. / 0.2040; soybean 0.8344 / -0.2891; crude -0.3871 / 5.4406; gold -0.3937 / 0.9578; silver n.a. / 0.1719 · exhibit: Table 3 Panels B-F
  ^QP09-C20-1
- Correlation of PTFS with funds: Swiss franc lookback 0.444 vs standard 0.433 (both significant); Sydney bankers acceptance lookback -0.006 vs standard 0.010 (neither significant); standard and lookback straddles are interchangeable at this frequency. _(robustness, evidence)_ #mech/research_method
  > These results indicate that, for quarterly expirations, standard straddles are similar to look- back straddles for the purpose of replicating monthly trend-following funds’ returns.
  reported_result: CHF: 0.444 (lookback), 0.433 (standard); ABA: -0.006, 0.010 · exhibit: Section 3.3
  ^QP09-C20-2
- Preferred-habitat test: regress funds on PTFSs in states 1 and 5 only, to see which markets explain performance in equity extremes. _(construction, design_choice)_ #mech/research_method
  > we regressed the trend-following funds’ returns on the PTFSs’ returns during the extreme states 1 and 5.
  exact_rule: OLS of trend-following fund return on market PTFS returns, states 1 and 5 only · exhibit: Section 3.4
  ^QP09-C20-3

### C21 (page 21)
- Group regressions in states 1 and 5: adjusted R2 stock PTFS 9.4% (none significant), bond 10.1% (US bonds), 3m rate 21.5% (Eurodollar, Short Sterling), currency 39.5% (DM, JPY), commodity 30.5% (wheat, silver); combined significant PTFS (US bonds, DM, wheat, silver) adjusted R2 60.7%. _(result, evidence)_ #mech/risk_management
  > These are the markets that, ex post, can account for trend followers’ performance during extreme equity market moves.
  reported_result: adjusted R2 9.4%, 10.1%, 21.5%, 39.5%, 30.5%; final 60.7% · exhibit: Table 5 Panel A; Section 3.4 · conditions: ex post selection of regressors
  ^QP09-C21-1
- Caveat: the final regression uses regressors chosen from earlier regressions (data mining), so inference is unreliable; it is ex post attribution. _(caveat, qualifier)_ #mech/research_method
  > As the regressors were selected based on previous regressions, statistical inference is not reliable.
  ^QP09-C21-2
- Table 4 note: state sizes differ from the text (note says state 5 has the best 34 months and state 3 the remaining 30; text says best 30 and remaining 34), an inconsistency in the table notes. _(caveat, qualifier)_ #mech/research_method
  > State 1 consists of the worst 30 months of the MS World Equity Index.
  exhibit: Table 4 notes vs text
  ^QP09-C21-3
- Table 4 numbers: by state 1-5 trend-following funds earn +2.03%, +1.12%, +1.32%, +0.10%, +5.69% a month versus MS World -4.60%, -0.59%, +1.56%, +3.36%, +6.74%. _(result, evidence)_ #mech/risk_management
  > Table 4
  reported_result: Table 4 trend-following funds mean by state (se): 0.0203 (0.0114), 0.0112 (0.0130), 0.0132 (0.0098), 0.0010 (0.0076), 0.0569 (0.0149); MS World -0.0460, -0.0059, 0.0156, 0.0336, 0.0674; Mar 1985-Dec 1997 · exhibit: Table 4
  ^QP09-C21-4
- Citation (Billingsley and Chance 1996): among specialised CTAs 41.2% trade bonds and 3m rates, 30.9% currencies, 15.5% commodities, 12.4% stock index futures; consistent with trend followers using currencies most and stocks least. _(citation, evidence)_ #mech/research_method
  > 41.2% trade bonds and three- month interest rate futures, 30.9% trade currencies, 15.5% trade commodi- ties, and 12.4% trade stock index futures.
  reported_result: 41.2% / 30.9% / 15.5% / 12.4%
  ^QP09-C21-5
- Table 4: in the worst equity state stock PTFS +12.8%, bond +5.9%, currency +8.3%, short-rate +8.3%, commodity +1.2%, funds +2.0%; in the best state +9.4%, +10.2%, +8.2%, +5.6%, -2.5%, funds +5.7%; in the middle state most PTFSs lose about 1-5.5%. _(result, evidence, Opus only)_ #mech/new
  > Option-like behavior of PTFS returns during
  reported_result: Table 4 (Mar85-Dec97) monthly means: state1 stock .1281 bond .0591 FX .0827 IR .0832 comm .0121 TF .0203 MSW -.0460; state3 stock -.0553 bond -.0518 FX -.0068 IR -.0108 comm -.0188 TF .0132 MSW .0156; state5 stock .0941 bond .1017 FX .0821 IR .0560 comm -.0245 TF .0569 MSW .0674 · exhibit: Table 4 · conditions: pays in extreme equity states, bleeds in calm states
  ^QP09-C21-1b

### C22 (page 22)
- Preferred habitat: both the qualitative CTA survey and the regressions say trend followers favour currencies and bonds and use stock indices least. _(result, conclusion)_ #mech/liquidity_flows
  > Currencies appeared to be the instrument of choice, and stock indices attracted the least trend-following
  ^QP09-C22-1
- Table 5A (states 1 and 5, Jan 1989-Dec 1997): coefficients US bond 0.0478, Euro-$ 0.0336, Short sterling 0.0234, DM 0.0544, JY 0.0194, wheat 0.0513, silver 0.0540; R2 0.674, adjusted 0.607; constant 0.0166. _(result, evidence)_ #mech/research_method
  > Estimating trend-following funds’ preferred habitat: January 1989–December 1997
  reported_result: Table 5A: const 0.0166 (se 0.0052); US bond 0.0478 (0.0204); Euro-$ 0.0336 (0.0259); Short sterling 0.0234 (0.0123); DM 0.0544 (0.0255); JY 0.0194 (0.0180); wheat 0.0513 (0.0169); silver 0.0540 (0.0128); R2 0.674; adj R2 0.607 · exhibit: Table 5 Panel A · conditions: regressors selected ex post
  ^QP09-C22-2
- Interpretation: currency is the most popular trend-following market and stocks the least. _(mechanism, conclusion)_ #mech/liquidity_flows
  > the lion’s share of available risk capital, whereas the equity market is the least popular.
  ^QP09-C22-3
- Table 5B (full sample, five PTFS portfolios): constant +1.155% a month (se 0.312), stock PTFS -0.035, bond 0.052, currency 0.110, rates -0.021, commodity 0.150; R2 0.5032, adjusted 0.4788, DW 2.31, chi2(5) 163.44. _(result, evidence)_ #mech/research_method
  > See the note for Table 1 for the deﬁnition of PTFS.
  reported_result: Table 5B: const 0.01155 (0.00312); stocks -0.03517 (0.01713); bonds 0.05164 (0.02495); currencies 0.10994 (0.01594); interest rates -0.02096 (0.02413); commodities 0.14999 (0.02468); R2 0.5032; adj 0.4788; DW 2.31; chi2(5) 163.44 p=0.0000 (Jan 1989-Dec 1997) · exhibit: Table 5 Panel B
  ^QP09-C22-4
- Table 5C (three significant PTFS): constant +1.229% (se 0.332), bond 0.029, currency 0.103, commodity 0.139; R2 0.4816, adjusted 0.4666; DW 2.28; chi2(3) 123.50. Currency and commodity PTFS carry most of the explanatory power. _(result, evidence)_ #mech/research_method
  > See the note for Table 2 for the deﬁnition of markets.
  reported_result: Table 5C: const 0.01229 (0.00332); bonds 0.02933 (0.02077); currencies 0.10308 (0.01575); commodities 0.13913 (0.02657); R2 0.4816; adj 0.4666; DW 2.28; chi2(3) 123.50 · exhibit: Table 5 Panel C
  ^QP09-C22-5
- To compare with survey data the authors assume the 41.2% bonds/short-rate share splits evenly. _(caveat, qualifier, Opus only)_ #mech/research_method
  > we assume that the group is evenly divided between the two instruments.
  ^QP09-C22-5b

### C23 (page 23)
- Figure 5: fitted PTFS replication portfolio plotted against trend-following fund returns shows a clear positive relation; funds range about -8% to +18% and replication about -7% to +15% monthly. _(result, evidence)_ #mech/research_method
  > Scatter plots of monthly trend-following fund’s returns versus PTFS replication portfolio returns
  reported_result: read from chart: strong positive scatter, outliers near fund +17% / replication +13%; replication about 4% at fund +18% · exhibit: Figure 5
  ^QP09-C23-1
- Individual-fund test sample: 163 trend-following funds with at least 24 months of returns to end-1997, regressed on five buy-and-hold portfolios and on the five PTFS portfolios. _(construction, design_choice)_ #mech/research_method
  > First, we focus on 163 trend-following funds with at least 24 months of return information through the end of 1997.
  exact_rule: per fund OLS on 5 buy-and-hold market portfolios vs on 5 PTFS portfolios · exhibit: Section 4; Table 6
  ^QP09-C23-2
- Individual funds on buy-and-hold benchmarks: R2 ranges -9% to 58% with average 11%; 86 funds with no coefficient significant at 1%; 72 with one (2 stocks, 1 currency, 7 bonds, 62 commodities); 5 with two. _(result, evidence)_ #mech/research_method
  > Eighty-six funds had no regression
  reported_result: adj R2 -9% to 58%, mean 11%; 86/72/5 funds with 0/1/2 significant coefficients · exhibit: Table 6; Section 4
  ^QP09-C23-3
- Individual funds on PTFS portfolios: R2 ranges -2% to 64% with average 24% (about double the 11% for buy-and-hold); 39 funds with no significant coefficient; 96 with one (12 bond PTFS, 33 currency PTFS, 51 commodity PTFS). _(result, evidence)_ #mech/research_method
  > Thirty-nine funds had no regression
  reported_result: adj R2 -2% to 64%, mean 24%; 39 / 96 funds with 0 / 1 significant coefficient · exhibit: Table 6; Section 4
  ^QP09-C23-4

### C24 (page 24)
- No individual fund had significant exposure to the stock PTFS; 27 funds had two significant coefficients (5 bond+currency, 11 bond+commodity, 10 currency+commodity, 1 currency+3m rate) and one fund had three. _(result, evidence)_ #mech/liquidity_flows
  > It is worth noting that no fund had any
  reported_result: no fund with significant stock PTFS exposure; 27 two-factor funds · exhibit: Section 4
  ^QP09-C24-1
- Significant PTFS exposures across funds: bond 4% to 65% (average 20%), currency 3% to 44% (16%), commodity 9% to 87% (26%), 3m rate 18% to 22% (20%). _(result, evidence)_ #mech/research_method
  > The commodity PTFS exposure ranged from 9% to 87%, averaging 26%.
  reported_result: exposure ranges: bond 4-65% avg 20%; currency 3-44% avg 16%; commodity 9-87% avg 26%; 3m rate 18-22% avg 20% · exhibit: Section 4
  ^QP09-C24-2
- Habitat validation: of 21 currency-only funds, 18 had significant exposure to the currency PTFS only, 2 had currency plus another, 1 none, supporting PTFS as habitat detectors. _(result, evidence)_ #mech/research_method
  > We examined 21 trend-following funds whose names imply they trade only currencies.
  reported_result: 21 funds: 18 / 2 / 1 · exhibit: Section 4
  ^QP09-C24-3
- PTFS beat buy-and-hold benchmarks fund by fund; Table 6 distribution of R2 for 163 funds shows most PTFS R2 between 0.0 and 0.4 (modal 0.2-0.3, 44 funds) vs buy-and-hold mostly 0.0-0.2 (modal 0.0-0.1, 53 funds). _(result, evidence)_ #mech/research_method
  > These results indicate that the PTFS returns (particularly bond, currency, and commodity) had much higher explanatory power than the benchmark asset returns even at the level of individual trend-following funds.
  reported_result: Table 6 R2 distribution (163 funds): PTFS bins -0.1-0:3, 0-0.1:21, 0.1-0.2:43, 0.2-0.3:44, 0.3-0.4:26, 0.4-0.5:17, 0.5-0.6:7, 0.6-0.7:2; buy-and-hold -0.2--0.1:3, -0.1-0:26, 0-0.1:53, 0.1-0.2:44, 0.2-0.3:28, 0.3-0.4:8, 0.4-0.5:1 · exhibit: Table 6
  ^QP09-C24-4

### C25 (page 25)
- Because funds differ in preferred habitat it is hard to find a single benchmark; fund-specific benchmarks may be needed, though PTFS capture nonlinear dynamics. _(caveat, qualifier)_ #mech/research_method
  > Glosten and Jagannathan (1994) recommended extensive discussions with each fund man- ager to understand how he or she operates
  ^QP09-C25-1
- Conclusion: the lookback straddle yields the payout of a perfect-foresight trend follower and its cost is observable from exchange-traded option prices. _(construction, conclusion)_ #mech/research_method
  > This strategy delivers the performance of a perfect foresight trend follower.
  exact_rule: PTFS cost from observable option prices
  ^QP09-C25-2
- Feature 1: PTFS and funds share strong positive skewness and positive returns in extreme up and down equity moves. _(result, conclusion)_ #mech/risk_management
  > They both have strong positive skewness.
  reported_result: Tables 1, 3, 4 · exhibit: Tables 1, 3, 4
  ^QP09-C25-3
- Interpretation: trend followers behave as if long volatility and market-event risk, delivering positive performance in extreme market environments. _(mechanism, conclusion)_ #mech/risk_premium
  > trend followers tend to perform as if they are long
  ^QP09-C25-4
- Implication 1: trend-following funds do have systematic risk invisible to linear models on buy-and-hold benchmarks. _(mechanism, conclusion)_ #mech/risk_premium
  > trend-following funds do have systematic risk. However, this risk cannot be observed in the context of a linear-factor model applied to standard asset benchmarks.
  ^QP09-C25-5
- Implication 2: a portfolio of lookback straddles on currencies, bonds and commodities (or trend followers) can reduce stock-bond portfolio volatility in extreme downturns; supported out of sample by Q3 1998. _(implementation, conclusion)_ #mech/risk_management
  > can reduce the volatility of a typical stock and bond portfolio during extreme market downturns.
  conditions: shown over 1985-97 plus Q3 1998
  ^QP09-C25-6
- Out-of-sample support: in Q3 1998 the S&P declined more than 10% while the vast majority of trend-following funds made large gains. _(result, evidence)_ #mech/risk_management
  > This view is corroborated by the out-of-sample events in the third quarter of 1998, when the S&P declined more than 10% and the
  reported_result: Q3 1998 S&P -10%+; majority of trend followers large gains (not tabulated) · exhibit: Conclusion
  ^QP09-C25-7
- Feature 2: extreme-period fund returns are explained by PTFSs on DEM and JPY, wheat and silver, Eurodollar and Short Sterling, and US bonds, but not stock indices; PTFSs beat buy-and-hold and industry benchmarks. _(result, conclusion, Opus only)_ #mech/research_method
  > Second, trend-following funds’ returns during extreme market moves can be explained by a combination of PTFSs on currencies (deutschemark and Japanese yen)
  ^QP09-C25-5b

### C26 (page 26)
- Q3 1998 out-of-sample: most trend-following funds made large gains during the S&P decline. _(result, evidence)_ #mech/risk_management
  > vast majority of trend-following funds made large gains.
  reported_result: not quantified · exhibit: Conclusion
  ^QP09-C26-1
- Implication 3: PTFS are building blocks for trend-follower performance benchmarks; but since strategies differ, no single benchmark fits all, and manager-specific operations may need to be included (Glosten and Jagannathan). _(implementation, conclusion)_ #mech/research_method
  > the PTFSs are key building blocks for the construction of a performance benchmark for trend-following funds
  ^QP09-C26-2
- Appendix A set-up: underlying volatility 20%, interest rate 6%, price 100, 60 days to expiry, both straddles ATM at 100; deltas compared across four price paths. _(construction, context)_ #mech/research_method
  > The interest rate, r, is 6%.
  exact_rule: sigma=20%, r=6%, S0=100, K=100, T=60 days · exhibit: Appendix A; Figure 6
  ^QP09-C26-3
- Scenarios A (price 100 to 160) and C (100 to 40): deltas similar and payouts identical, so in strongly trending markets lookback and standard straddles are the same. _(result, evidence)_ #mech/cycle_persistence
  > These two cases show that, in strongly trending markets, the two straddles are virtually identical.
  exhibit: Appendix A, Figure 6 scenarios A and C · conditions: strongly trending markets
  ^QP09-C26-4
- Scenario B (rise to 130, fall to 110, rise to 150): lookback delta falls and turns negative on the pullback (like selling a breakdown), then turns strongly positive again (like buying a breakout), unlike the standard straddle whose delta stays positive. _(result, evidence)_ #mech/cycle_persistence
  > the delta of the lookback straddle declines sharply and actually turns negative, resembling a trend follower selling breakdown.
  exhibit: Appendix A, Figure 6 scenario B
  ^QP09-C26-5
- Scenario D (rise to 130, fall back to 100): standard straddle pays 0, lookback straddle pays 30 and its delta turns negative on the way back; this is where trend-following differs from market timing. _(result, evidence)_ #mech/cycle_persistence
  > while the lookback straddle pays out 30
  reported_result: standard payout 0 vs lookback payout 30 · exhibit: Appendix A, Figure 6 scenario D · conditions: reversal after a trend: lookback gains, market timer loses
  ^QP09-C26-6

### C27 (page 27)
- Figure 6 shows the four price paths and the delta of each straddle (rotated page, only coarsely readable: in A and C deltas converge to about +1 and -1; in B and D the lookback delta drops toward or below zero on the pullback while the standard delta stays positive). _(result, evidence)_ #mech/cycle_persistence
  > Deltas of the standard straddle and lookback straddle in scenarios A, B, C, and D of the underlying asset’s price path
  reported_result: coarse reading from rotated chart; details taken from Appendix A text · exhibit: Figure 6
  ^QP09-C27-1

### C28 (page 28)
- Lookback straddle delta mimics a trader positioned by the current price relative to the running maximum and minimum since inception (long near the max, short near the min), while a standard straddle delta mimics a market timer positioned by price vs the inception price. _(mechanism, mechanism_step)_ #mech/cycle_persistence
  > The trader is long (short) when the current price is near the maximum (minimum) price. This is what a trend follower would do.
  exact_rule: trend follower: long when price near running max, short near running min; market timer: long if price > inception price, short otherwise
  ^QP09-C28-1
- Standard straddle delta equals a market timer who compares the current price only to the starting price. _(mechanism, mechanism_step)_ #mech/research_method
  > The trader is long if the current price is above the inception price and short otherwise.
  ^QP09-C28-2
- Appendix B: option data start dates range from 1982 (S&P 500 1983, 30y bond Oct 1982, gold Oct 1982) to 1992 (FTSE, DAX, Aus bills, Australian All Ordinary); options observations 45,785 to 626,348 per market; all samples end 31 Dec 1997. _(construction, design_choice)_ #mech/research_method
  > Futures and option data on the DTB, MATIF, and Osaka were purchased from the Futures Industry Institute (FII).
  data_needed: exchange option and futures data per Appendix B · reported_result: Appendix B: start dates S&P 83/01/28, FTSE 92/03/13, DAX 92/01/02, Nikkei 89/06/12, US 30Y 82/10/04, Euro-$ 85/03/21, GBP 85/03/01, DM 84/01/24, JPY 86/03/06, CHF 85/02/25, corn 85/02/27, wheat 88/01/04, soybean 84/10/31, crude 86/11/14, gold 82/10/04, silver 88/01/04 · exhibit: Appendix B
  ^QP09-C28-3
- Data gaps (Appendix B footnotes): Nikkei and Euro-Yen data missing from many dates; portions missing in 1993 for DM and CHF, and in 1987-88 for yen. _(caveat, qualifier)_ #mech/research_method
  > Data missing from many dates.
  exhibit: Appendix B footnotes b-d
  ^QP09-C28-4

### C29 (page 29)
- Reference list: Fung and Hsieh (1997a,b), Glosten and Jagannathan (1994), Goldman-Sosin-Gatto (1979), Merton (1981), Billingsley and Chance (1996); no new evidence. _(citation, context)_ #mech/research_method
  > Fung, W., and D. A. Hsieh, 1997b, “Survivorship Bias and Investment Style in the Returns of CTAs,”
  ^QP09-C29-1

