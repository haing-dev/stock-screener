---
source_id: QP08
title: "Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harvey, Le Roux, Rattray)"
type: paper
claims: 142
opus_only: 16
tags: [paper, layer0]
---
# Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harvey, Le Roux, Rattray)

**Authors:** Jamil Baz (Man Group); Nick Granger (Man AHL); Campbell R. Harvey (Duke University; Man Group); Nicolas Le Roux (Man Group); Sandy Rattray (Man AHL)

**Summary:** Do carry, momentum and value work better as directional (time-series) or cross-asset implementations? Daily backtest 1990-Apr 2015 of 87 futures/forwards/swaps across equity, rates, FX and commodities, with theory review for each style. Value is a cross-sectional style, momentum a time-series style, carry works in both; combining styles and implementations reaches Sharpe about 1.6 gross of costs.

## Argument map

**Question:** Should carry, momentum and value be traded directionally (time series) or cross-asset (long-short), and which market conditions decide? It matters because the choice changes net market exposure, which factor risks are hedged and how much of each signal's information is kept.

**Thesis:** Value works best cross-sectionally, momentum best directionally and carry in both; a cross-sectional book is a time-series book with the global factor hedged out, so the right choice depends on whether the global factor trends or mean-reverts and on how correlated signals are relative to assets. All versions combined give high but selection-biased, gross-of-cost Sharpe ratios. ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C21-3|C21-3]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C21-4|C21-4]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C22-1|C22-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C22-5|C22-5]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C27-3|C27-3]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C27-2|C27-2]])

### Foundations (premises)
- Forward prices are biased predictors of future spot (Jensen; CAPM forward bias), so a carry premium can exist; with a dividend/value factor the bias is tied to carry. _[theoretical, stated; support: derivation (eqs 1-9)]_ ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C03-3|C03-3]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C04-2|C04-2]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C04-3|C04-3]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C04-4|C04-4]])
- Carry premia compensate non-diversifiable risks (crash/peso risk in FX, recession and volatility risk) or hedging pressure and inventories in commodities and term premia in rates. _[theoretical, stated; support: citations (Lustig-Verdelhan, Koijen et al., Keynes, theory of storage)]_ ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C04-5|C04-5]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C05-1|C05-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C05-2|C05-2]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C05-7|C05-7]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C05-8|C05-8]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C05-9|C05-9]])
- Returns persist at 6-12 months and reverse at very short and multi-year horizons; momentum comes from underreaction, flow inertia or disposition effects (or risk exposure). _[behavioural, stated; support: citations and Grinblatt-Han model]_ ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C05-11|C05-11]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C06-3|C06-3]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C06-5|C06-5]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C06-6|C06-6]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C06-1|C06-1]])
- Asset prices revert toward fundamental anchors (real rate ~ growth, dividend yield ~ ERP, PPP, production cost), slowly, after overshooting. _[theoretical, stated; support: consumption model, Gordon model, PPP, Dornbusch]_ ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C06-8|C06-8]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C07-1|C07-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C07-3|C07-3]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C08-1|C08-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C08-4|C08-4]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C08-5|C08-5]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C08-6|C08-6]])
- Within an asset class there is a dominant global (market) factor; a market-neutral long-short book hedges it out. _[empirical, stated; support: PCA intuition; algebra for linear signals]_ ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C02-1b|C02-1b]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C21-4|C21-4]])
- Few investors can sit through multi-year underperformance, so simple premia are not arbitraged away. _[behavioural, stated; support: anecdote (1999 value, 2008 carry, 2011-13 momentum)]_ ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C26-6|C26-6]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C27-1|C27-1]])

### Mechanism chain
- 1. Signal applied directionally (TS) → Book holds net exposure to the asset class global factor: 1/N signed positions are all long when signals agree _[assertion]_ ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C12-6|C12-6]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C17-2b|C17-2b]])
- 2. Cross-sectional transformation → Global factor removed (w_CS = w_TS - mean): linear signals: CS weights are TS weights minus their average _[assertion]_ ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C21-4|C21-4]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C02-1b|C02-1b]])
- 3. Global factor trending → TS momentum beats CS momentum; reversion-based TS value loses: TS momentum harvests the factor trend which CS hedges away; value bets against it _[test]_ ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C02-2|C02-2]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C22-1|C22-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C17-1|C17-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C18-1|C18-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C22-4|C22-4]])
- 4. Signals more correlated than assets (momentum in equities/bonds) → CS hedges out signal alpha rather than market noise: the common part of the signals is the informative part _[test]_ ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C22-5|C22-5]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C23-1|C23-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C23-1|C23-1]])
- 5. Weak global factor (FX, commodities) → Small CS vs TS difference: less to hedge out _[test]_ ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C22-3|C22-3]])
- 6. Low correlations across styles, asset classes and implementations → Combined Sharpe 1.37-1.61: near-zero average pairwise correlation diversifies _[test]_ ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C14-2|C14-2]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C15-2|C15-2]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C19-2|C19-2]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C23-3|C23-3]])

### Design rationale
- **Single CTA EWMA-crossover momentum (3 speeds, vol-normalised, response function) for all asset classes**: not given beyond being a standard CTA signal; momentum works at medium frequencies. Alternatives: linear signals tested (similar). Sensitivity: not shown for speeds ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C10-5|C10-5]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C11-1|C11-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C11-2b|C11-2b]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C26-3|C26-3]])
- **Long-horizon value anchors (expanding-window real price, PPP mean, DY level, 10Y minus GDP)**: value is a long-term game. Alternatives: 10Y minus CPI for rates (similar). Sensitivity: only rates variant shown as 'quite similar' ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C11-3|C11-3]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C11-4|C11-4]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C11-5|C11-5]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C12-1|C12-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C12-2|C12-2]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C26-3|C26-3]])
- **Seasonality-adjusted equity carry; commodity carry from front vs 1-year-out contract**: remove dividend and harvest seasonality. Alternatives: none shown. Sensitivity: not shown ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C10-2|C10-2]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C10-3|C10-3]])
- **Rates carry includes roll-down; rates value uses lagged GDP growth**: carry meant as carry + roll; 3-month lag for release delay. Alternatives: CPI version. Sensitivity: similar ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C10-4|C10-4]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C12-2b|C12-2b]])
- **CS: top/bottom 3 equal-weight, binary, daily rebalance; TS: sign x 1/N**: simplicity; risk not tied to signal size. Alternatives: other numbers of extreme assets; monthly and linear. Sensitivity: 'comparable'/'broadly consistent', no numbers ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C12-3|C12-3]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C12-4|C12-4]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C21-1|C21-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C12-6|C12-6]])
- **FX carry and value in 252 daily tranches held one year**: FX mean reversion slower. Alternatives: none shown. Sensitivity: not shown ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C13-1|C13-1]])
- **Scale each portfolio to 15% ex-ante vol across asset classes; equal weight across styles**: volatility comes mostly from asset class. Alternatives: none. Sensitivity: not shown ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C12-5|C12-5]])

### Evidence map
- Momentum Sharpe 0.96 TS vs 0.42 CS; value 0.28 TS vs 0.75 CS; carry ~1.25 both. Tests: step 3 (global factor trend favours TS momentum and hurts TS value). Rules out: that implementation is irrelevant for momentum and value. Does not rule out: (reader) one 25-year sample with a secular bond and equity rally; the TS value zero point (raw DY, price ratio) may embed a structural long/short bias rather than a mean-reversion bet. Strength: moderate - large gaps but single sample, no significance tests, gross of costs ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C17-1|C17-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C18-3|C18-3]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C21-3|C21-3]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C18-2|C18-2]])
- Signal correlations exceed asset correlations for momentum in equities (66% vs 51%) and rates (51% vs 19%). Tests: step 4. Rules out: . Does not rule out: (reader) value signals are also more correlated than assets in FX/rates (48% vs 24%, 36% vs 19%) yet value works in CS, so signal correlation alone does not explain the ranking. Strength: weak - descriptive, no formal link to performance gap ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C23-1|C23-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C23-1|C23-1]])
- CS-TS gap smaller in FX and commodities than in equities and rates. Tests: step 5. Rules out: . Does not rule out: (reader) FX momentum CS 0.74 vs TS 0.72 fits, but commodity value 0.07 CS vs 0.22 TS goes the other way. Strength: weak - four asset classes only ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C22-3|C22-3]])
- Combined Sharpe 1.40 (CS), 1.37 (TS), 1.61 (CS+TS); rolling 3Y Sharpe never negative. Tests: step 6 diversification. Rules out: . Does not rule out: (reader) selection bias, survivorship, no costs, hindsight on parameters, and the TS book's 2008 jump driving results. Strength: moderate - stable over time but gross and selected ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C16-2|C16-2]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C16-3|C16-3]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C19-2|C19-2]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C23-3|C23-3]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C26-1|C26-1]])
- TS equity value and carry betas negative; FX carry beta +36-39%. Tests: foundation that carry is risk compensation (FX) and that equity carry/value are contrarian. Rules out: . Does not rule out: (reader) betas reflect daily S&P co-movement, not crash-state exposure. Strength: strong - high t-stats ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C15-1|C15-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C19-1|C19-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C18-4b|C18-4b]])

### Regimes
- Global factor trending (e.g. policy-supported rallies 1990-2015) → TS momentum outperforms; TS value underperforms ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C22-1|C22-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C22-4|C22-4]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C18-1|C18-1]])
- Global factor returns negatively autocorrelated → TS value should beat CS value ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C22-1|C22-1]])
- Low asset correlation within class (FX, commodities) → CS and TS converge ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C22-3|C22-3]])
- Equity sell-offs → FX carry loses (pro-cyclical); equity/rates carry gain (countercyclical) ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C14-5|C14-5]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C15-1|C15-1]])
- Tight commodity inventories → commodity carry and momentum both positive and correlated; value opposite ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C14-3|C14-3]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C14-4|C14-4]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C05-8|C05-8]])
- Late 1990s equity bubble; 2011-13 → value (TS) rolling Sharpe deeply negative; momentum weak after 2010 ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C20-2|C20-2]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C15-4|C15-4]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C26-6|C26-6]])

### Gaps and conflicts
- [conflict] Section 5 claims Sharpe 'close to 2' and eight-fold growth at 15% vol, but the best reported figure is 1.61 (Figure 11 ~7x at unstated vol). ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C26-1|C26-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C25-1|C25-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C23-3|C23-3]])
- [conflict] 'We tried our hand at six possible explanations' but only five are listed. ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C26-2|C26-2]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C26-3|C26-3]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C26-4|C26-4]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C26-5|C26-5]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C26-6|C26-6]])
- [data] Text says 26 equity indices, but the bullet list names 35 (Russell2000, Germany-Tech, Italy, Sweden, Austria, Sensex, Russia, Poland... missing from the start-date table); 'Russia included' in Section 5 yet not in the table. ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C30-1|C30-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C26-4|C26-4]])
- [data] FX list has 31 entries including USD itself although all are 'versus the USD'; 31 'pairs' vs 30 non-USD currencies. ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C29-1|C29-1]])
- [conflict] Commodity carry formula as printed (F_{T1+1y} - F_{T1})/F_{T1+1y} is positive in contango, the opposite sign of the equity and FX carry definitions; probably a typo. ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C10-3|C10-3]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C10-1|C10-1]])
- [unspecified] Trade sign for value signals not stated (FX PPP deviation, commodity price ratio); TS 'long if signal positive' undefined for always-positive signals (dividend yield, price ratio around 1) - centring not specified. ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C11-3|C11-3]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C11-4|C11-4]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C11-5|C11-5]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C12-6|C12-6]])
- [unspecified] FX value averaging window (overline mean) not defined; EWMA crossover applied to price or total return not explicit (C18 implies total return). ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C11-3|C11-3]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C18-4|C18-4]])
- [untested] All results gross of transaction costs; costs 'discussed later' but never quantified; daily rebalancing with binary signals implies high turnover. ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C09-6|C09-6]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C16-2|C16-2]])
- [untested] No t-stats or significance tests for Sharpe differences between CS and TS; robustness claims (other configurations, monthly/linear, CPI rates value) given without numbers. ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C12-2|C12-2]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C12-4|C12-4]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C21-1|C21-1]])
- [data] Universe expands over time (many EM series start 1997-2001; S&P value only from 2000), so early-sample results rest on few assets; survivorship admitted. ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C29-1|C29-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C30-1|C30-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C26-4|C26-4]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C26-5|C26-5]])
- [untested] The 'drivers' (asset vs signal correlation) are proposed but the ex-ante framework is not built or tested; explanation 1 does not explain why value beats momentum cross-sectionally. ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C02-5|C02-5]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C27-3|C27-3]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C22-3|C22-3]])
- [data] Hansen-Heaton-Li dated 1998 in text but 2008 in references; Table 12 IR carry t-stat printed '(10.1)' with negative beta. ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C09-2|C09-2]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C24-1|C24-1]])

### Relations to other strategies
- Time-series momentum (Moskowitz et al. 2012): **complement**. confirms TS momentum beats CS momentum in a multi-asset futures set ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C02-3|C02-3]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C17-1|C17-1]])
- Value and momentum everywhere (Asness et al. 2013): **complement**. CS value/momentum negatively correlated as in AMP ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C13-3|C13-3]])
- Carry (Koijen et al. 2013): **complement**. carry strongest standalone style in both implementations ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C05-1|C05-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C13-2|C13-2]])
- Value vs carry in FX and commodities: **substitute**. strong negative correlations (FX -68% TS, commodities -48% CS) and Dornbusch neutralisation link the two ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C14-4|C14-4]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C19-1|C19-1]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C09-1|C09-1]])
- Equity carry vs equity value: **substitute**. 51% correlation; both contrarian on index level ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C18-5b|C18-5b]], [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C18-4b|C18-4b]])
- Momentum vs carry: **complement**. momentum on total returns partly re-captures carry ([[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C18-4|C18-4]])

### Forward-looking inputs (reader synthesis)
(reader) Observable inputs: (1) carry (forward premium, futures slope, swap carry+roll) leads returns over months via risk-premium/forward-bias step; (2) EWMA-crossover trend leads over weeks-months via slow reaction; (3) value anchors (PPP gap, DY, real price vs history, 10Y minus nominal GDP) lead over years via mean reversion. For the CS vs TS choice: the autocorrelation/trend of the asset-class average return and the ratio of average signal correlation to average asset correlation should predict which implementation wins. These stop working if the global factor flips from trending to mean-reverting (hurting TS momentum, helping TS value), if crowding removes the patience premium, or if costs from daily binary rebalancing eat the gross edge.

### Reader inferences (not stated by the authors)
- (reader) The TS value result likely depends on how the always-positive value signals were centred, which the paper does not state; a demeaned or z-scored version could behave differently.
- (reader) The 2015 sample includes a 30-year bond rally and equity bull market, so the TS momentum vs value gap may be regime-specific rather than structural.
- (reader) The commodity carry sign as printed would invert the trade; real implementation must have used backwardation-positive carry given the positive commodity carry Sharpe.
- (reader) The 'close to 2' Sharpe in Section 5 is probably rhetorical or from an unreported variant; 1.61 is the documented figure.
- (reader) Since CS+TS = TS minus half the global mean, a continuous hedge ratio on the global factor (0 to 1) chosen by the global factor's autocorrelation is the natural generalisation the paper points to.

## Claims

### C01 (page 1)
- The paper compares carry, momentum and value implemented directionally (time series) versus across assets (cross section) to learn which market conditions favour which setting. _(mechanism, premise)_ #mech/research_method
  > we offer some insights on the market conditions that favor the application of a particular setting
  ^QP08-C01-1

### C02 (page 2)
- Practice differs: cash equity momentum is traded cross-sectionally, futures momentum directionally; the authors ask why and test both implementations. _(mechanism, premise)_ #mech/research_method
  > momentum is almost always traded across assets (relative value) whereas in futures trading, momentum is typically applied directionally. Why?
  ^QP08-C02-1
- If the dominant market factor is trending, time-series (directional) momentum should beat cross-sectional momentum, because a market-neutral cross-sectional book hedges out that factor. _(mechanism, mechanism_step)_ #mech/cycle_persistence
  > if the market factor is trending, then it is more likely time-series momentum will be profitable than cross-sectional momentum
  conditions: works when the first principal component (market/global factor) trends; if predictability sits in the other factors the cross-sectional form is preferred
  ^QP08-C02-2
- Scope: carry, value and momentum tested both ways in four asset classes (equity, fixed income, currency, commodity), plus combined time-series and cross-sectional information. _(construction, design_choice)_ #mech/research_method
  > We fill this gap by providing an analysis of both the time- series and cross-section using a broad number of asset classes: equity, fixed income, currencies and commodities.
  data_needed: equity index futures, rate swaps, FX, commodity futures
  ^QP08-C02-3
- The three styles were selected because they are known to have worked, so positive average returns are partly a selection effect; the aim is to understand conditions, not to find the most profitable strategy. _(caveat, qualifier)_ #mech/research_method
  > we are testing three strategies that are select - they are popular because they have worked.
  ^QP08-C02-4
- The difference between directional and cross-asset performance is driven by correlation of asset returns, correlation of the underlying (partly unobservable) information, and correlation of trading signals; to be explored in a future paper. _(mechanism, mechanism_step)_ #mech/research_method
  > Important drivers are the correlation of asset returns, the correlation of the information that drives markets
  ^QP08-C02-5
- Headline: the three styles are largely profitable and the combination of styles performs best. _(result, conclusion)_ #mech/research_method
  > these strategies are largely profitable over our sample - and the best performance is when these strategies are combined
  reported_result: qualitative; see Tables 1-12
  ^QP08-C02-6
- A market-neutral cross-asset portfolio removes the dominant first principal component (the market), so it only harvests predictability in the remaining factors. _(mechanism, premise, Opus only)_ #mech/research_method
  > In a cross-asset strategy that is market neutral, the dominant factor is effectively hedged out.
  exact_rule: Cross-sectional (market-neutral) portfolio = directional portfolio minus exposure to first PC/market factor
  ^QP08-C02-1b

### C03 (page 3)
- Carry is spot minus forward, i.e. the profit on a long forward position if prices do not change. _(construction, premise)_ #mech/research_method
  > We define carry as the difference between the spot and the forward price of an asset
  exact_rule: carry = spot - forward (profit on a long forward if spot unchanged)
  ^QP08-C03-1
- Simple carry trade: go long the forward when carry is positive, short when negative. _(construction, design_choice)_ #mech/research_method
  > buying the asset forward if the carry is positive or selling it forward if the carry is negative
  exact_rule: position sign = sign(carry); long forward if carry>0, short if carry<0
  ^QP08-C03-2
- By Jensen's inequality (F=E(S) for A per B and for B per A cannot both hold), forwards cannot be unbiased predictors of future spot, so a systematic forward bias must exist in all asset classes; for FX this means uncovered interest parity cannot hold. _(mechanism, premise)_ #mech/risk_premium
  > This means that forward prices cannot be unbiased predictors of future spot prices.
  ^QP08-C03-3
- Forward = spot * exp((r-d)(T-t)), so carry on a dividend-paying asset is positive when the risk-free rate exceeds the dividend yield. _(construction, mechanism_step)_ #mech/research_method
  > By standard arbitrage, the forward price is equal to the spot price compounded at the risk-free rate minus the dividend yield
  exact_rule: F(t,T)=S(t)*exp((r-d)(T-t)); eq. (4) · exhibit: Equation 4
  ^QP08-C03-4
- Footnote 1: forwards and futures are treated as equivalent in the theory section (ignores marking-to-market differences). _(caveat, qualifier, Opus only)_ #mech/research_method
  > For practical purposes, readers can think of forwards and futures as equivalent in this section.
  exhibit: footnote 1
  ^QP08-C03-4b

### C04 (page 4)
- Sign of carry = sign(r - d). _(construction, mechanism_step)_ #mech/research_method
  > Note that the carry is positive (negative) if the interest rate is greater (smaller) than the dividend yield.
  ^QP08-C04-1
- Under CAPM, E(S_T)=S_t exp((r+beta*pi-d)(T-t)); for positive-beta assets the forward is below expected spot, so a long forward earns expected P&L S_t e^{(r-d)(T-t)}[e^{beta*pi(T-t)}-1] > 0 (systematic forward bias). _(mechanism, mechanism_step)_ #mech/risk_premium
  > If the asset beta is positive as is generally the case, the forward price is lower than the expected spot price
  exhibit: Equations 5-7
  ^QP08-C04-2
- In plain CAPM the forward bias depends on beta*pi, not on r-d, so carry as a signal has no explanation from the market factor alone. _(mechanism, mechanism_step)_ #mech/risk_premium
  > The sign of the forward bias is independent of carry
  ^QP08-C04-3
- With a dividend (value-proxy) factor in expected returns, forward bias correlates with carry: higher yield means higher carry and a more profitable carry trade. _(mechanism, mechanism_step)_ #mech/risk_premium
  > The higher the dividend yield, the higher the carry, the lower the forward compared to the expected spot price, the more profitable the carry trade.
  exhibit: Equations 8-9 · conditions: requires an asset pricing model richer than CAPM (dividend factor loading gamma)
  ^QP08-C04-4
- Citation (Lustig and Verdelhan 2007): low-yielding currencies hedge low domestic consumption states and so carry lower expected returns than high yielders, a risk-based reason for FX carry. _(citation, evidence)_ #mech/risk_premium
  > high-yielding currencies tend to depreciate whereas low-yielding currencies hold their own in low domestic consumption states
  ^QP08-C04-5
- Breeden (1986) is cited for equilibrium links between interest rates and growth, used later to define rates value. _(citation, context, Opus only)_ #mech/risk_premium
  > Breeden (1986) derives equilibrium relationships between interest rates, growth and other parameters from optimal consumption and production models
  ^QP08-C04-5b

### C05 (page 5)
- Citation (Koijen, Moskowitz, Pedersen, Vrugt 2013): carry across asset classes is relatively uncorrelated with value and momentum but partly explained by recession and volatility risk. _(citation, evidence)_ #mech/risk_premium
  > find the strategy is rela- tively uncorrelated with factors such as value and momentum but is partially explained by recession and volatility risk
  ^QP08-C05-1
- FX carry (buy high-yield, sell low-yield currency) is compensation for non-diversifiable risks (political turmoil, weak property rights, persistent inflation). _(mechanism, mechanism_step)_ #mech/risk_premium
  > This trade can be profitable because high-yields are associated with non-diversifiable risk factors such as political turmoil or wavering property rights
  ^QP08-C05-2
- The yield differential can pay for peso-problem jump risk that has not materialised in the sample, so realised carry returns may overstate safety. _(mechanism, qualifier)_ #mech/risk_premium
  > the yield differential can remunerate a so-called peso effect, meaning that jump risk can be very real even though it has not materialized
  ^QP08-C05-3
- Alternative reading: a high yield can reflect a central bank about to (re)establish anti-inflation credibility that will make the currency more desirable. _(mechanism, mechanism_step)_ #mech/policy_reaction
  > a high yield on a currency can reflect a central bank just about to gain or regain anti-inflation
  ^QP08-C05-4
- Normal backwardation (Keynes): producers sell futures for insurance, creating structural excess futures supply so curves are backwardated and futures roll up to spot. _(mechanism, mechanism_step)_ #mech/risk_premium
  > was interpreted by Keynes as the result of producers selling futures to insure themselves against price falls
  ^QP08-C05-5
- Empirically commodity curves are often not backwardated, so the Keynesian insurance story is incomplete. _(caveat, qualifier)_ #mech/research_method
  > But as observed empirically, backwardation is not the norm, particularly today.
  ^QP08-C05-6
- Hedgers can be on either side (airlines are naturally long futures), so contango can pay speculators to be short; speculators earn carry by buying backwardation and selling contango. _(mechanism, mechanism_step)_ #mech/liquidity_flows
  > speculators are incented by hedgers to sell contangoed futures and buy backwardated futures
  ^QP08-C05-7
- Theory of storage (Working 1933, Kaldor 1939, Schwartz 1997): low inventories give a high convenience yield, hence backwardation; inventories rebuild slowly so carry profits can persist. _(mechanism, mechanism_step)_ #mech/cycle_persistence
  > the theory of storage links backwardation to tight inventories
  ^QP08-C05-8
- Fixed income carry is roll-down on an upward-sloping curve (liquidity premium / preferred habitat explanations), giving excess returns. _(mechanism, mechanism_step)_ #mech/risk_premium
  > Rates tend to roll down the curve: this translates into excess returns for fixed income investors.
  ^QP08-C05-9
- Conventional momentum: buy past 12-month winners, sell losers. _(construction, context)_ #mech/research_method
  > The conventional trade (at least for academic purposes) is to buy assets that outperformed and sell assets that underperformed over the previous year.
  exact_rule: long assets with high prior-12m return, short low
  ^QP08-C05-10
- Returns show negative autocorrelation below one month and above three years; positive autocorrelation (momentum sweet spot) is at 6-12 months. _(mechanism, premise)_ #mech/cycle_persistence
  > the sweet spot for momentum, or positively auto-correlated, strategies is around 6-12 months
  ^QP08-C05-11
- Momentum explanations are split between risk-based (sensitivity to macro factors) and behavioural (underreaction/overreaction). _(mechanism, premise)_ #mech/slow_reaction
  > Theories of momentum range from the risk-based to the behavioral.
  ^QP08-C05-12

### C06 (page 6)
- Risk story: high-momentum assets are more sensitive to macro factors such as industrial production growth (Liu and Zhang 2008). _(citation, evidence)_ #mech/risk_premium
  > growth rate of industrial production (Liu and Zhang, 2008)
  ^QP08-C06-1
- Conrad and Kaul (1988): when realised and expected returns are highly correlated, past winners have higher expected returns and outperform past losers. _(citation, evidence)_ #mech/risk_premium
  > a cross-section of past winners with high realized returns has higher expected returns and ends up outperforming a cross-section of past losers
  ^QP08-C06-2
- Behavioural: underreaction from conservatism (Barberis, Shleifer, Vishny 1998) or asynchronous information receipt (Hong and Stein 1999) produces momentum. _(citation, evidence)_ #mech/slow_reaction
  > investors underreact to news either because they display conservatism bias and are slow updating their beliefs
  ^QP08-C06-3
- Alternative: prices overreact and feed on themselves via noise traders, deepening mispricing until a reversal. _(mechanism, mechanism_step)_ #mech/overshoot
  > prices can overreact to news and feed upon themselves with noise traders deepening the mis-pricing
  ^QP08-C06-4
- Vayanos and Woolley (2013): fund-flow inertia and under-reaction to expected flows generate persistence until a large deviation from fundamentals triggers reversal. _(citation, evidence)_ #mech/liquidity_flows
  > behavioral biases can generate momentum when fund flows exhibit inertia and the market under-reacts to expected future flows
  ^QP08-C06-5
- Disposition effect (Grinblatt and Han 2002): with rational fraction mu and disposition fraction 1-mu, equilibrium price P_t = w F_t + (1-w) P_{t-1} with w=1/(1+mu*alpha), so price is positively correlated with yesterday's price and only partially reflects fundamentals. _(citation, evidence)_ #mech/slow_reaction
  > Investors tend to sell their winning stocks too early while holding on to their losers.
  exact_rule: P_t = w*F_t + (1-w)*P_{t-1}, w = 1/(1+mu*alpha) · exhibit: Equations 10-12
  ^QP08-C06-6
- Authors' view (AHL/MSS board): unprecedented policy (negative rates, QE, wealth-effect focus) makes investors rely on heuristics and anchoring, which together with liquid markets favours persistence of slow momentum; 'qualified yes' that momentum is behavioural in today's markets. _(mechanism, mechanism_step)_ #mech/behavioral
  > Behavioral biases, combined with more liquid markets and more efficient information diffusion, tend to favor persistence of slow momentum.
  ^QP08-C06-7
- Value = fundamental price minus market price; the paper discusses fundamental measures for rates, stocks, currencies and commodities. _(construction, premise)_ #mech/research_method
  > Value can be defined as the difference between a fundamental asset price and its prevailing market price.
  ^QP08-C06-8

### C07 (page 7)
- Value for rates: with log utility and lognormal consumption the equilibrium real rate is r = g + rho - sigma^2 (deterministic r = g), so real rates are anchored by consumption growth. _(mechanism, mechanism_step)_ #mech/structural_shift
  > we can solve for the equilibrium real interest rate
  exact_rule: r = g + rho - sigma^2 (log utility); r = g (deterministic); CRRA: r = gamma*g + rho - gamma^2 sigma^2/2 per footnote 2 · exhibit: Equations 13-15, footnote 2
  ^QP08-C07-1
- Value for rates can also be the domestic-foreign real-rate differential: higher domestic real rates create excess demand for domestic bonds. _(mechanism, mechanism_step)_ #mech/liquidity_flows
  > When capital is free to move across countries, there is evidently a tendency for real rates of return to converge.
  ^QP08-C07-2
- Gordon: P = D/(R-g_d); implied equity yield R = g + D/P; implied ERP = g - r + D/P, which with r=g reduces to ERP = D/P, justifying the dividend yield as equity value measure. _(construction, mechanism_step)_ #mech/research_method
  > the equity yield is the sum of the dividend growth and the dividend yield
  exact_rule: R = g + D/P; ERP = R - r = g - r + D/P; if r=g then ERP = D/P · exhibit: Equations 16-19
  ^QP08-C07-3

### C08 (page 8)
- Equity index value measure = dividend yield (high yield = cheap versus bonds). _(construction, design_choice)_ #mech/research_method
  > Dividend yields can therefore be used as a measure of value for broad equity markets.
  ^QP08-C08-1
- Caveat: dividend yield is time-varying and, when rates are below growth, understates the equity risk premium; leverage may also mean the ERP is less than it looks. _(caveat, qualifier)_ #mech/research_method
  > Of course the dividend yield can be time-varying and thus not necessarily a measure of value.
  ^QP08-C08-2
- Alternative equity value measures: price-to-book and Tobin's Q (market cap over replacement cost; Q>1 means expensive). _(construction, context)_ #mech/research_method
  > high price-to-book ratios are a presumption of expensiveness.
  ^QP08-C08-3
- Commodity value works because high prices stimulate supply and low prices reduce it, and competitive prices gravitate to production cost; value is a bet on long mean-reversion cycles. _(mechanism, mechanism_step)_ #mech/overshoot
  > high (low) commodity prices incentivise producers to boost (reduce) supply which in turn results in downward (upward) pressure on prices
  ^QP08-C08-4
- Currency value = deviation of real exchange rate from PPP; frictions (transport, tariffs, sticky prices, capital flows, policy) cause deviations; the authors call PPP 'more a tautology than a theory'. _(mechanism, mechanism_step)_ #mech/overshoot
  > purchasing power parity (PPP) has the most intuitive appeal
  ^QP08-C08-5
- Dornbusch overshooting: with sticky goods prices, flexible asset prices, UIP and PPP long run, an unanticipated money supply increase lowers the domestic rate so the currency must depreciate beyond PPP, then appreciates back. _(citation, evidence)_ #mech/overshoot
  > Dornbusch's overshooting model (1976) is an example of a rational story that explains large deviations from PPP.
  exhibit: Equations 20 · conditions: rational-expectations, sticky price assumption
  ^QP08-C08-6
- The value premium has rational and behavioural explanations, as momentum does. _(mechanism, context, Opus only)_ #mech/research_method
  > Much like theories of momentum, theories of value can be based on rational or behavioral stories.
  ^QP08-C08-5b

### C09 (page 9)
- In the Dornbusch model value premium is offset by carry (no free lunch), but overshooting still creates value opportunities in assets that adjust slowly (e.g. euro real estate after the euro depreciation). _(mechanism, qualifier)_ #mech/overshoot
  > While this model is arbitrage free - the value premium is perfectly neutralized by the carry
  ^QP08-C09-1
- Citation (Hansen, Heaton, Li): value outperformance reflects higher long-run consumption risk exposure (risk-based story). _(citation, evidence)_ #mech/risk_premium
  > attribute the out-performance of value portfolios (relative to growth portfolios) to a higher long term exposure to consumption risk
  ^QP08-C09-2
- Behavioural value stories: extrapolation of past history (Lakonishok, Shleifer, Vishny 1994); prospect-theory/myopic loss aversion (Benartzi and Thaler); ambiguity aversion (Maenhout 1999) partly explaining the equity premium. _(citation, evidence)_ #mech/behavioral
  > value strategies outperform glamour strategies because investors put excessive weight on past history
  ^QP08-C09-3
- Sample Jan 1990 - Apr 2015; sources Bloomberg, Global Financial Data, Man-AHL proprietary database. _(construction, design_choice)_ #mech/research_method
  > The sample period starts in January 1990 and ends in April 2015.
  data_needed: Bloomberg, Global Financial Data, Man-AHL database
  ^QP08-C09-4
- Universe: 26 equity futures, 14 interest-rate swaps, 31 currency pairs (versus USD), 16 commodity futures; all prices in USD. _(construction, design_choice)_ #mech/research_method
  > We study 26 equity futures markets, 14 interest rate swap contracts, 31 currency pairs, and 16 commodity futures.
  exact_rule: universe 26 EQ / 14 IR swaps / 31 FX / 16 commodities; USD prices
  ^QP08-C09-5
- All results use mid prices with no trading costs, so reported Sharpe ratios are gross of costs (daily rebalancing makes this material). _(caveat, qualifier)_ #mech/research_method
  > We used mid-market prices and do not therefore account for trading costs
  conditions: gross of transaction costs
  ^QP08-C09-6
- FX carry = 4 x (Spot/Fwd_3M - 1), annualised from the 3-month forward. _(construction, design_choice)_ #mech/research_method
  > We used the 3 month FX-forward to imply the carry
  exact_rule: Carry_t = 4*(Spot_t / Fwd3M_t - 1) · data_needed: spot and 3M forward FX · exhibit: Equation 21
  ^QP08-C09-7
- The recent euro fall after surprise ECB easing illustrates overshooting; such moves create value opportunities in slow-adjusting assets such as euro-denominated real estate, which stayed sticky. _(mechanism, evidence, Opus only)_ #mech/overshoot
  > This mechanism is reminiscent of the euro sudden depreciation in response to the unanticipated loosening of monetary policy in Europe recently.
  ^QP08-C09-1b

### C10 (page 10)
- Equity carry raw signal = (Fut_T1 - Fut_T2)/Fut_T2 * 1/(T2-T1) from the first two index futures. _(construction, design_choice)_ #mech/research_method
  > We used the first two futures of each index and computed a raw carry signal as follows
  exact_rule: RawCarry_t = [1/(T2-T1)] * (Fut_{t,T1} - Fut_{t,T2}) / Fut_{t,T2} · data_needed: first and second index futures prices and expiries · exhibit: Equation 22
  ^QP08-C10-1
- Equity carry is seasonally adjusted: subtract, for each calendar month m, the average (to date) of raw carry minus its 1Y moving average over all past days in month m (dividend seasonality). _(construction, design_choice)_ #mech/research_method
  > For every month m, we compute a seasonality adjustment which is the average difference between the raw carry and its 1Y moving average
  exact_rule: Adj_t = average over past days in same calendar month of [RawCarry - 1Y MA(RawCarry)]; Carry_t = RawCarry_t - Adj_t · exhibit: Equations 23-24 · conditions: expanding sample: only data up to t
  ^QP08-C10-2
- Commodity carry uses the first future against the contract expiring exactly one year later to remove seasonality: Carry = (Fut_{T1+1y} - Fut_{T1})/Fut_{T1+1y}. _(construction, design_choice)_ #mech/research_method
  > we used the first future and the contract exactly expiring one year later
  exact_rule: Carry_t = (Fut_{t,T1+1} - Fut_{t,T1}) / Fut_{t,T1+1}, T1+1 = one year after T1 · exhibit: Equation 25
  ^QP08-C10-3
- Swap carry = (S10Y - Fixing)/Duration + (S10Y - S7Y)/3 i.e. carry plus roll-down, with modified duration (1-(1+S10Y)^-10)/S10Y. _(construction, design_choice)_ #mech/research_method
  > Carry is meant as ”carry + roll down”.
  exact_rule: Carry_t = (S_10Y,t - Fixing_t)/Duration_t + (S_10Y,t - S_7Y,t)/3; Duration_t = (1-(1+S_10Y,t)^-10)/S_10Y,t · data_needed: 10Y and 7Y swap rates, short-rate fixing · exhibit: Equations 26-27
  ^QP08-C10-4
- Momentum for every asset class is a CTA-style multi-speed EWMA crossover signal; speeds S_k=(8,16,32) and L_k=(24,48,96), each n converted to lambda=(n-1)/n, half-life log(0.5)/log(1-1/n). _(construction, design_choice)_ #mech/research_method
  > For all asset classes, we used a CTA-momentum signal, based on the cross over of exponentially weighted moving averages.
  exact_rule: three pairs EWMA(P|S_k)-EWMA(P|L_k), S=(8,16,32), L=(24,48,96); lambda=(n-1)/n; HL=log0.5/log(1-1/n) · exhibit: Equation 28
  ^QP08-C10-5

### C11 (page 11)
- Each crossover x_k is divided by 63-day running standard deviation of price, then standardised again by the running 252-day standard deviation of y_k. _(construction, design_choice)_ #mech/research_method
  > We normalize with a moving standard deviation as a measure of the realized 3-months normal volatility (PW=63)
  exact_rule: x_k=EWMA(P|S_k)-EWMA(P|L_k); y_k=x_k/RunStDev(P,63); z_k=y_k/RunStDev(y_k,252) · exhibit: Equations 29-31
  ^QP08-C11-1
- Response function R(x)=x*exp(-x^2/4)/0.89 dampens extreme signals; u_k=R(z_k); final signal is equal-weighted (1/3) sum of u_k. _(construction, design_choice)_ #mech/research_method
  > The final CTA momentum signal is the weighted sum of the intermediate signals
  exact_rule: u_k=R(z_k), R(x)=x*exp(-x^2/4)/0.89; S_CTA = (1/3)*sum_k u_k · exhibit: Equations 32-33 · conditions: response function caps position as signal grows; reduces exposure to extreme trends
  ^QP08-C11-2
- FX value = log of CPI-adjusted real spot minus its long-run (historical) mean; real spot = spot x CPI_1/CPI_2. _(construction, design_choice)_ #mech/research_method
  > We used relative PPP (purchasing power parity) as value indicator
  exact_rule: Value_t = log(SpotReal_t) - mean(log(SpotReal)); SpotReal = Spot_CCY1/CCY2 * CPI_CCY1/CPI_CCY2 · data_needed: FX spot, national CPIs · exhibit: Equation 34
  ^QP08-C11-3
- Equity value signal = index dividend yield. _(construction, design_choice)_ #mech/research_method
  > We used dividend yield as value indicator
  exact_rule: Value_t = DivYield_t · exhibit: Equation 35
  ^QP08-C11-4
- Commodity value = US-CPI-deflated price divided by the deflated expanding-window average of all prices; sign is long when ratio is low. _(construction, design_choice)_ #mech/research_method
  > Value is defined as today’s deflated price divided by the deflated historical average price
  exact_rule: Value_t = AdjPrice_t / mean(AdjPrice over expanding window); AdjPrice=Price/US_CPI · data_needed: commodity futures prices, US CPI · exhibit: Equation 36
  ^QP08-C11-5
- Each normalised crossover passes through R(z) = z*exp(-z^2/4)/0.89, which peaks near |z| = 1.4 and fades for extreme values; the final signal is the equal-weight (1/3) average over the three speeds. _(construction, design_choice, Opus only)_ #mech/slow_reaction
  > We calculate an intermediate signal for each k=1,2,3 via a response function R
  exact_rule: u_k = z_k * exp(-z_k^2/4) / 0.89; S_CTA = (u_1 + u_2 + u_3)/3 · conditions: response function cuts exposure to very stretched trends
  ^QP08-C11-2b

### C12 (page 12)
- Rates value = 10Y swap rate minus latest nominal GDP growth (quarterly, lagged 3 months); results with CPI inflation instead were quite similar. _(construction, design_choice)_ #mech/research_method
  > We defined value, in the rate space, as the difference between the 10Y swap rate and the most recent nominal GDP growth rate
  exact_rule: Value_t = S_10Y,t - NominalGDPgrowth_t (3-month lag) · data_needed: 10Y swap rates, nominal GDP growth · exhibit: Equation 37, footnote 4
  ^QP08-C12-1
- Replacing nominal GDP growth with y/y CPI inflation in rates value gave similar results; GDP version is used throughout. _(robustness, evidence)_ #mech/research_method
  > We tested both definitions and the results were quite similar.
  reported_result: 'quite similar' (numbers not shown) · exhibit: Section 3.2
  ^QP08-C12-2
- Cross-sectional portfolio: per style and asset class, rank assets by signal, long top 3 and short bottom 3, equal risk weights regardless of signal size, rebalanced every trading day. _(construction, design_choice)_ #mech/research_method
  > we ranked all the assets according to the magnitude of the signal and took long/short positions on the six most extreme assets (three on each side)
  exact_rule: rank by signal; long 3 highest, short 3 lowest; equal risk per position; daily rebalance · exhibit: Section 3.3
  ^QP08-C12-3
- Using other numbers of extreme assets than six gave comparable results (footnote 5). _(robustness, evidence)_ #mech/research_method
  > Afterwards, we tested for other configurations and the results were compa- rable
  reported_result: 'comparable' (numbers not shown) · exhibit: footnote 5
  ^QP08-C12-4
- Aggregating asset classes: each portfolio is scaled ex ante to 15% annualised vol; aggregating styles uses equal weights because vol comes mostly from asset class choice. _(construction, design_choice)_ #mech/research_method
  > we computed the ex-ante volatility of each of the portfolios and scaled their allocations for an annualized volatility of 15% per portfolio
  exact_rule: scale each asset-class portfolio to 15% ex-ante annual vol; equal weight across styles · exhibit: Section 3.3
  ^QP08-C12-5
- Time-series portfolio: use the same signals; each of N assets in an asset class gets 1/N weight, long or short by the sign of the signal, so positions can all be long or all short. _(construction, design_choice)_ #mech/research_method
  > we consider the universe of N assets and take positions equivalent to N 1 .
  exact_rule: weight_i = sign(signal_i)/N within each asset class; same rebalance as CS · exhibit: Section 3.3
  ^QP08-C12-6
- Footnote 4: GDP growth enters with a three-month lag to approximate publication delay. _(construction, design_choice, Opus only)_ #mech/research_method
  > We used a three month lag for the GDP growth rate.
  exact_rule: GDP growth lagged 3 months · exhibit: footnote 4
  ^QP08-C12-2b
- Example: equity value is long the three highest-yield indices and short the three lowest, held one business day. _(construction, design_choice, Opus only)_ #mech/research_method
  > we ranked all indices by dividend yield, and took long positions on the three highest dividend paying indices and short positions on the three lowest dividend paying indices.
  exact_rule: daily: long 3 highest DY indices, short 3 lowest DY
  ^QP08-C12-6b

### C13 (page 13)
- FX carry and FX value are rebalanced slowly (1/252 of the book each day, positions held one year) because FX mean reversion is slower; all other portfolios are fully rebalanced daily. _(construction, design_choice)_ #mech/research_method
  > {“FX”, “carry”} and {“FX”, “value”} are two exceptions here because mean reversion in FX is slower than in equity and commodities.
  exact_rule: each day open 1/252 of FX carry/value positions and close those from one year earlier; others rebalance 100% daily
  ^QP08-C13-1
- Cross-sectional single-style Sharpe ratios: by style All Asset Value 0.75, Carry 1.27, Momentum 0.42; carry is the most profitable standalone style; all pairs positive except IR momentum -0.31. _(result, evidence)_ #mech/research_method
  > With one exception, all the Sharpe ratios are positive with an average of 0.40 per asset class.
  reported_result: Table 1A (CS, 1990-Apr 2015, gross): FX V/C/M 0.42/0.67/0.74; EQ 0.39/0.33/0.01; Commo 0.07/0.77/0.45; IR 0.56/0.76/-0.31; style averages 0.36/0.63/0.22; All Asset 0.75/1.27/0.42; asset-class averages FX 0.61, EQ 0.24, Commo 0.43, IR 0.34 · exhibit: Table 1 Panel A
  ^QP08-C13-2
- Cross-sectional max drawdown/vol by style across all assets is -1.8 (value), -3.1 (carry), -2.6 (momentum); skew positive for value and momentum, negative for carry. _(result, evidence)_ #mech/research_method
  > maximum drawdowns per style are of order 1.8 to 3.1 times the volatility
  reported_result: Table 1B All Asset DD/vol: Value -1.8, Carry -3.1, Mom -2.6; by class avg FX -3.0, EQ -3.7, Commo -2.2, IR -4.2; IR momentum -9.1 · exhibit: Table 1 Panel B
  ^QP08-C13-3

### C14 (page 14)
- Value is negatively correlated with carry and momentum in cross section (V-C -9.0%, V-M -9.2%, C-M +15.0%), the 'fundamental versus technical traders' battle. _(result, evidence)_ #mech/research_method
  > Looking at broad correlations, value is negatively correlated with both carry and momentum.
  reported_result: Table 2A (CS): V-C -9.0%, V-M -9.2%, C-M 15.0% · exhibit: Table 2 Panel A
  ^QP08-C14-1
- Cross-sectional correlations among style x asset-class pairs range -50% to +50% but cluster within +/-10%, average near zero; the largest are commodity value-carry -48%, commodity carry-momentum +51% and commodity value-momentum -32%. _(result, evidence)_ #mech/research_method
  > The average correlation, as evidenced from Table 2 Panel B, is close to zero, indicating great scope for diversification within a broad portfolio.
  reported_result: Table 2B: CO value vs CO carry -48%; CO carry vs CO momentum 51%; CO value vs CO momentum -32%; IR value vs IR momentum 15%; FX carry vs EQ carry -11%; most other pairs between -12% and +16% · exhibit: Table 2 Panel B
  ^QP08-C14-2
- Carry and momentum positively correlated mainly in commodities because low inventories cause both high carry and strong momentum (Erb and Harvey 2006). _(mechanism, mechanism_step)_ #mech/cycle_persistence
  > This is mostly due to the high correlation between commodity carry and commodity momentum as both a high carry and a strong momentum are caused by low inventory levels
  reported_result: CO carry-momentum corr 51% (Table 2B) · exhibit: Table 2 Panel B
  ^QP08-C14-3
- Commodity value and carry are strongly negatively correlated (-48%): both caused by high inventory (low spot price = deep value, low convenience yield = higher carry). _(mechanism, mechanism_step)_ #mech/cycle_persistence
  > a low spot price (revealing deep value) goes hand in hand with a lower convenience yield (or higher carry
  reported_result: CO value vs CO carry corr -48%; CO value vs CO momentum -32% (Table 2B) · exhibit: Table 2 Panel B; footnote 6
  ^QP08-C14-4
- Strategies are scaled to 15% vol and show low S&P betas, except FX carry which is pro-cyclical. _(result, evidence)_ #mech/research_method
  > most strategy pairs - each scaled for 15% volatility (in line with the S&P historical volatility) - are showing low S&P beta estimates
  reported_result: Table 3A S&P betas (see next page chunk for values) · exhibit: Table 3
  ^QP08-C14-5
- Footnote 6: commodity carry relation F/S = exp((r + s - c)(T - t)), with s storage cost and c convenience yield. _(construction, context, Opus only)_ #mech/research_method
  > where s and c are the storage cost and convenience yield respectively
  exact_rule: F/S = exp((r + s - c)(T - t)) · exhibit: footnote 6
  ^QP08-C14-5b

### C15 (page 15)
- Equity and rate carry are countercyclical; FX carry is pro-cyclical (S&P beta +36%, t=30.0), equity value -15%, equity carry -17%, IR carry -11%. _(result, evidence)_ #mech/research_method
  > Table 3: Assessing the Market Risk of Cross Sectional Strategies
  reported_result: Table 3A (CS) betas (t): FX V -1%(-1.2), C 36%(30.0), M -8%(-7.13); EQ V -15%(-12.3), C -17%(-14.7), M 1%(0.5); Commo V -1%, C -3%(-2.3), M -3%(-2.6); IR V 3%(1.9), C -11%(-8.8), M -5%(-3.4); All Asset V -4%(-5.9), C 2%(2.6), M -4%(-6.1) · exhibit: Table 3 Panel A
  ^QP08-C15-1
- Combining styles in the cross section roughly doubles Sharpe: All Asset V+C 1.49, V+M 0.86, C+M 1.08, V+C+M 1.40; asset-class V+C+M FX 1.07, EQ 0.42, Commo 0.83, IR 0.54. _(result, evidence)_ #mech/research_method
  > In panel A, the Sharpe ratios of all three styles are greatly enhanced when styles are aggregated across styles.
  reported_result: Table 4A (CS, gross): V+C+M All Asset 1.40; V+C 1.49; V+M 0.86; C+M 1.08; class avg of V+C+M: FX 1.07, EQ 0.42, Commo 0.83, IR 0.54; Avg of pairs 0.75/0.42/0.57 · exhibit: Table 4 Panel A
  ^QP08-C15-2
- Max drawdown/vol and skew of combined cross-sectional styles: All Asset V+C+M DD/vol -1.7, skew 0.20; V+C -1.3 (skew -0.14). _(result, evidence)_ #mech/research_method
  > Table 4: Combining the Cross Sectional Signals
  reported_result: Table 4B All Asset DD/vol: V+C -1.3, V+M -1.5, C+M -3.6, V+C+M -1.7; Table 4C skew: V+C -0.14, V+M 0.19, C+M 0.14, V+C+M 0.20 · exhibit: Table 4 Panels B-C
  ^QP08-C15-3
- Rolling 3Y Sharpe (Fig 1): value consistently positive, carry positive except mid-1990s, cross-sectional momentum has suffered in recent years. _(robustness, evidence)_ #mech/research_method
  > Remarkably, performance is consistently positive for value.
  reported_result: Figure 1 read from chart: carry 3Y Sharpe peaks about 2.5-2.8 in 2005-07; momentum fades towards 0-0.5 by 2014-15; value about 0.5-1.5 · exhibit: Figure 1
  ^QP08-C15-4

### C16 (page 16)
- 1Y rolling style correlations are unstable: value-carry ranges about -0.55 to +0.5; carry-momentum from about -0.3 to +0.6; value-momentum mostly between -0.5 and +0.25. _(robustness, evidence)_ #mech/research_method
  > In figure 2, it can be seen that correlations across styles are highly unstable, with value showing at times strong negative correlation with both carry and momentum.
  reported_result: Figure 2 read from chart: V-C from about -0.55 (1991, 2007) to +0.52 (2003); C-M up to 0.6 (1992-93) · exhibit: Figure 2
  ^QP08-C16-1
- All-asset all-style cross-sectional portfolio: Sharpe 1.40, return 6.88%, vol 4.92%, no transaction costs. _(result, evidence)_ #mech/research_method
  > The overall Sharpe ratio is 1.40, with corresponding return and volatility of 6.88% and 4.92% respectively.
  reported_result: CS V+C+M All Asset (1990-Apr 2015): Sharpe 1.40; return 6.88%; vol 4.92%; gross of costs · exhibit: Figures 3-4, text
  ^QP08-C16-2
- CS combined: 3Y rolling Sharpe between 0 and 2.30 and about 1.35 recently; never negative on 3Y rolling basis. _(robustness, evidence)_ #mech/research_method
  > Figure 4 shows that the portfolio was never in the red on a 3yr rolling basis with a Sharpe ratio moving between 0 and 2.30 and hovering around 1.35 recently.
  reported_result: 3Y rolling Sharpe range 0 to 2.30; ~1.35 recently; Fig 3 compounded P&L reaches about 550 from 100 (1990-2015) · exhibit: Figures 3, 4
  ^QP08-C16-3

### C17 (page 17)
- Time series: momentum Sharpe more than doubles vs cross section (0.42 to 0.96) and has the lowest drawdown/vol of the styles; value and momentum positively skewed, carry negatively. _(result, evidence)_ #mech/research_method
  > momentum more than doubles its Sharpe ratio from 0.42 to 0.96
  reported_result: Table 5A All Asset TS: Value 0.28, Carry 1.25, Mom 0.96 (vs CS 0.75/1.27/0.42); drawdown/vol Mom -2.4 · exhibit: Table 5; text
  ^QP08-C17-1
- Interpretation: TS momentum captures market directionality (including reversals) better than CS momentum; value is vastly worse in time series than cross section because equity value fell (stocks trended up for 25 years). _(mechanism, mechanism_step)_ #mech/cycle_persistence
  > One can surmise that momentum in a time series portfolio will capture more clearly market directionality, including reversals
  ^QP08-C17-2
- Fig. 3 CS V+C+M compounded P&L rises smoothly from 100 to roughly 550 over 1990-2015, Sharpe 1.4. _(result, evidence)_ #mech/research_method
  > Figure 3. Cross Sectional: Value+Carry+Momentum Compounded P&L
  reported_result: Figure 3: P&L index 100 to about 550; Sharpe 1.4. Figure 4: 3Y rolling Sharpe mostly 1.0-2.3, trough near 0 in 1996-97; distribution peaks 1.4 · exhibit: Figures 3, 4
  ^QP08-C17-3
- Unlike the CS book, the time-series book can carry net directional exposure to an asset class when signals agree. _(construction, mechanism_step, Opus only)_ #mech/research_method
  > Therefore, if the signal is uniformly positive across an asset class, the portfolio position will be directionally positive in all assets.
  exact_rule: position = sign(signal)/N; net exposure = average sign
  ^QP08-C17-2b

### C18 (page 18)
- Equity value in time series had negative Sharpe (-0.13) since stocks trended up 25 years and mean-reversion value underperforms in a trend; drawdown/vol -6.6. _(result, evidence)_ #mech/overshoot
  > 25 years, the value factor, which relies largely on mean reversion, was bound to underperform.
  reported_result: Table 5A TS EQ Value Sharpe -0.13; Carry 0.23; Mom 0.41; EQ value DD/vol -6.6 (Table 5B) · exhibit: Table 5 Panels A-B · conditions: fails when the directional factor trends for decades
  ^QP08-C18-1
- Time-series single-style results: FX 0.27/0.55/0.72, EQ -0.13/0.23/0.41, Commo 0.22/0.64/0.45, IR 0.48/0.83/0.77 (V/C/M); style averages 0.21/0.56/0.58; All Asset 0.28/1.25/0.96; max drawdown/vol and skew shown. _(result, evidence)_ #mech/research_method
  > Table 5: Time Series Strategies using Individual Signals
  reported_result: Table 5A Sharpe (TS, gross); 5B All Asset DD/vol V -4.4, C -2.5, M -2.4; 5C All Asset skew V 0.69, C -0.42, M 0.47; FX carry skew -1.20 · exhibit: Table 5
  ^QP08-C18-2
- Time-series S&P betas are more negative and more significant; equity value and equity carry boil down to buying dips and selling tops (negative beta) and are 51% correlated. _(result, evidence)_ #mech/overshoot
  > betas are more, yet weakly, negative and more significant in time series than in cross section
  reported_result: Table 6B EQ value vs EQ carry corr 51%; Table 7A (below) · exhibit: Table 6 Panel B; Table 7
  ^QP08-C18-3
- Carry and momentum correlate in time series because momentum is computed on total return series, which accumulates carry; longer momentum lookbacks raise the signal correlation. _(mechanism, mechanism_step)_ #mech/cycle_persistence
  > If a market exhibits a persistent carry premium this will accumulate though the total return and produce a momentum effect.
  ^QP08-C18-4
- Average time series style/asset correlations are near zero, so diversification is large. _(result, evidence)_ #mech/research_method
  > As in the cross sectional case, the average correlation in time series is close to zero
  reported_result: Table 6A overall TS: V-C -3.1%, V-M -10.2%, C-M +23.6% · exhibit: Table 6 Panel A
  ^QP08-C18-5
- Directional equity carry and value both buy after falls and sell after rallies, hence negative equity betas; FX carry stays pro-cyclical. _(mechanism, mechanism_step, Opus only)_ #mech/overshoot
  > equity carry, like equity value, boils down to buying market dips and selling market tops and will hence show a negative beta.
  ^QP08-C18-4b
- TS equity value and equity carry correlate 51%, i.e. they are largely the same trade. _(result, evidence, Opus only)_ #mech/research_method
  > From Table 6 Panel B, equity value and equity carry correlation is 51%, confirming that both strategies are similar in nature.
  reported_result: Table 6B TS EQ value vs EQ carry 51% · exhibit: Table 6 Panel B
  ^QP08-C18-5b

### C19 (page 19)
- TS S&P betas (t): FX V -29%(-25.1), C 37%(35.7), M -13%(-10.9); EQ V -31%(-24.9), C -23%(-27.7), M -20%(-18.1); Commo V 2%, C -18%(-14.4), M -10%(-8.1); IR V 7%(8.5), C -9%, M -9%; All Asset V -13%, C -3%, M -13%. _(result, evidence)_ #mech/research_method
  > Table 7: Assessing the Market Risk of Time Series Strategies
  reported_result: Table 7A TS betas to S&P as listed; All Asset V -13%(-25.3), C -3%(-6.5), M -13%(-18.5) · exhibit: Table 7 Panel A
  ^QP08-C19-1
- TS V+C+M All Asset Sharpe 1.37, 3Y rolling Sharpe between 0.1 and 2.7 over 21 years; styles combined: V+C 1.05, V+M 0.99, C+M 1.35; class V+C+M FX 1.14, EQ 0.31, Commo 0.79, IR 1.04. _(result, evidence)_ #mech/research_method
  > the time series Sharpe is high at 1.37, while the 3Y rolling Sharpe ratio for a combined carry, momentum and value portfolio was always positive
  reported_result: Table 8A (TS, gross): All Asset V+C 1.05, V+M 0.99, C+M 1.35, V+C+M 1.37; classes FX 1.14, EQ 0.31, Commo 0.79, IR 1.04 · exhibit: Table 8 Panel A; text
  ^QP08-C19-2
- Combined TS and CS Sharpe ratios are similar (1.37 vs 1.40) though individual style performance differs a lot (CS strong in value, TS strong in momentum). _(result, evidence)_ #mech/research_method
  > Combining signals, Sharpe ratios for time series are broadly in line with those for the cross sec- tion
  reported_result: TS V+C+M 1.37 vs CS 1.40 · exhibit: Tables 4, 8
  ^QP08-C19-3

### C20 (page 20)
- TS combined drawdown/vol and skew: All Asset V+C+M DD/vol -1.9, skew 0.91 (commodity skew 1.87); EQ drawdown/vol -5.4. _(result, evidence)_ #mech/research_method
  > Panel B: Maximum Drawdowns divided by Volatility
  reported_result: Table 8B All Asset DD/vol V+C -2.5, V+M -1.9, C+M -1.8, V+C+M -1.9; EQ V+C+M -5.4; Table 8C All Asset skew 0.18/1.25/0.34/0.91 · exhibit: Table 8 Panels B-C
  ^QP08-C20-1
- Fig 5: TS rolling 3Y Sharpe: carry highest in the 2000s, value dips negative around 1999 and 2007-09, momentum falls toward zero by 2014; Fig 6: TS 1Y rolling style correlations swing between about -0.8 and +0.8 (V-M reaching -0.8 in 2011). _(robustness, evidence)_ #mech/research_method
  > Figure 5. Time Series: 3Y Rolling Sharpe per Asset Class (left) and per Invest- ment Style (right)
  reported_result: Figure 5/6 read from chart: V-M corr about -0.8 near 2011-12; C-M up to about 0.8 in 1992 · exhibit: Figures 5, 6
  ^QP08-C20-2

### C21 (page 21)
- Robustness: monthly rebalancing with linear (non-binary) signals gives broadly consistent results with daily binary signals. _(robustness, evidence)_ #mech/research_method
  > we also tested all of the above strategies using monthly rebalancing and linear signals. The monthly results are broadly consistent with the daily results.
  reported_result: 'broadly consistent' (numbers not shown) · exhibit: Section 4.2
  ^QP08-C21-1
- Fig 7-8: TS V+C+M compounded P&L rises from 100 to about 540, Sharpe 1.37; 3Y rolling Sharpe from about 0.2 (1999) to 2.6 (1996); distribution peaks 1.4-1.6. _(result, evidence)_ #mech/research_method
  > Figure 7. Time Series: Value+Carry+Momentum Compounded P&L
  reported_result: Figure 7: ~100 to ~540; Sharpe 1.37; Figure 8 3Y rolling Sharpe range about 0.2-2.7, one jump up in 2008 · exhibit: Figures 7, 8
  ^QP08-C21-2
- Core finding: value is a cross-sectional style (0.75 vs 0.28), carry works in both (1.27 vs 1.25), momentum is a time-series style (0.96 vs 0.42). _(result, conclusion)_ #mech/research_method
  > value works well in the cross section, poorly in time series; carry works about equally well in both cross section and time series and momentum works well in time series, but poorly in the cross section.
  reported_result: Table 1A vs Table 5A All Asset Sharpe: V 0.75 vs 0.28; C 1.27 vs 1.25; M 0.42 vs 0.96 · exhibit: Tables 1, 5
  ^QP08-C21-3
- With linear signals CS weights = TS weights minus the cross-sectional average, so a CS portfolio is a TS portfolio hedged for the global factor. _(mechanism, mechanism_step)_ #mech/research_method
  > cross sectional portfolio weights are equal to time series weights minus the cross sectional average
  exact_rule: w_CS,i = w_TS,i - mean_j(w_TS,j)
  ^QP08-C21-4
- TS V+C+M 3-year rolling Sharpe falls to about 0.1 around 1999-2000 and peaks about 2.6 in 1997 and ~2.4 in 2003. _(robustness, evidence, Opus only)_ #mech/research_method
  > Figure 8. Time Series: 3Y Rolling Sharpe (left) and its Distribution (right) for
  reported_result: Figure 8 (read from chart): min ~0.1 around 2000; max ~2.6 (1997) · exhibit: Figure 8
  ^QP08-C21-2b

### C22 (page 22)
- TS momentum beats CS momentum to the extent the global factor trends; TS value beats CS value when global factor returns are negatively autocorrelated. _(mechanism, mechanism_step)_ #mech/cycle_persistence
  > time series momentum will outperform cross sectional mo- mentum to the extent that the global factor is trending
  conditions: TS momentum advantage scales with global factor trendiness; TS value advantage with global factor mean reversion
  ^QP08-C22-1
- Explanation 1: momentum uses price itself so assimilates novel information about the global factor that a valuation model omits; strongest in correlated asset classes (equities, bonds). _(mechanism, mechanism_step)_ #mech/slow_reaction
  > momentum, unlike value, takes the price movements themselves as being informative and, as in such, may be better placed to assimilate any truly novel information
  ^QP08-C22-2
- Where the global factor explains little (FX, commodities) there is less to hedge out and CS/TS differences are small; consistent with observed results. _(robustness, evidence)_ #mech/research_method
  > In FX and commodities where a global factor is much less apparent the performance differences between the cross section and time series is much less.
  reported_result: e.g. commodity Sharpe: CS V/C/M 0.07/0.77/0.45 vs TS 0.22/0.64/0.45 · exhibit: Tables 1, 5
  ^QP08-C22-3
- Explanation 2: strong trends in global factors (policy-boosted stock and bond rallies) hurt reversion-based value in time series and favoured momentum. _(mechanism, mechanism_step)_ #mech/policy_reaction
  > major global factors have exhibited very strong trends which have by definition hurt reversion based value predictors
  conditions: policy-driven asset price rallies 1990-2015
  ^QP08-C22-4
- Explanation 3: CS gains most when asset correlations are high and signal correlations low; if signals are also highly correlated CS hedges out signal too. Equity/bond momentum signals are more correlated than value signals, so CS hurts momentum there. _(mechanism, mechanism_step)_ #mech/research_method
  > a cross sectional approach has more to gain when asset correlations are very high
  conditions: CS better if asset corr high and signal corr low; TS better if signal corr >= asset corr
  ^QP08-C22-5

### C23 (page 23)
- Average signal correlations vs asset correlations: Value 39%, Carry 20%, Momentum 44% versus asset 25%; EQ asset 51% vs momentum signal 66%, value 44%; IR asset 19% vs momentum 51%, value 36%. _(result, evidence)_ #mech/research_method
  > Table 9: Signal and Asset Average Correlations
  reported_result: Table 9A: FX V/C/M/Asset 48/23/40/24%; EQ 44/23/66/51%; Commo 30/3/19/7%; IR 36/30/51/19%; Avg 39/20/44/25% · exhibit: Table 9
  ^QP08-C23-1
- Conclusion of 4.3: practice (value cross-sectional, momentum time-series) matches results; 'traders have generally come to the correct conclusions'. _(result, conclusion)_ #mech/research_method
  > value is tradi- tionally traded in the cross section while momentum is traded in time series
  ^QP08-C23-2
- Combining CS and TS: correlation between CS and TS portfolios 43%; same-style correlations 39% value, 49% carry, 51% momentum; combined Sharpe 1.61, 3Y rolling Sharpe 0.5-2.7 since 1994. _(result, evidence)_ #mech/research_method
  > The overall correlation between the two portfolios is 43%.
  reported_result: CS-TS correlation 43%; value 39%, carry 49%, momentum 51%; combined V+C+M Sharpe 1.61; 3Y rolling 0.5-2.7 since 1994 · exhibit: Table 11 Panel A; Figures 11-12
  ^QP08-C23-3
- Caveat: the CS+TS combination is, in a simple set-up, equal to the TS portfolio with half the cross-sectional mean hedged, so diversification benefit should not be overstated. _(caveat, qualifier)_ #mech/research_method
  > the combined portfolio is just the time series portfolio with half of the cross sectional mean hedged out
  ^QP08-C23-4
- Combined CS+TS Sharpe by style (All Asset): V 0.71, C 1.41, M 0.73; V+C 1.59, V+M 1.06, C+M 1.33, V+C+M 1.61; class V+C+M FX 1.21, EQ 0.47, Commo 0.92, IR 0.80; DD/vol All Asset V+C+M -1.7. _(result, evidence)_ #mech/research_method
  > Table 10: Combining the Cross Sectional and Time Series Signals
  reported_result: Table 10A (CS+TS, gross): All Asset V 0.71, C 1.41, M 0.73, V+C 1.59, V+M 1.06, C+M 1.33, V+C+M 1.61; Table 10B All Asset DD/vol V -2.8, C -3.0, M -2.3, V+C+M -1.7; EQ V+C+M -5.0 · exhibit: Table 10 Panels A-B
  ^QP08-C23-5

### C24 (page 24)
- Combined CS+TS S&P betas: All Asset V -7%(-13.2), C -1%(-2.0), M -8%(-12.4); EQ V -25%, C -25%; FX carry 39%(34.1); skew All Asset V+C+M 0.19. _(result, evidence)_ #mech/research_method
  > Table 12: Assessing the Market Risk of Cross Sectional Combined with Time Series
  reported_result: Table 11A CS-TS correlations V 39%, C 49%, M 51%, cross terms -20% (CS value vs TS carry); Table 10C All Asset skew V+C+M 0.19; Table 12A as listed · exhibit: Tables 10C, 11, 12
  ^QP08-C24-1
- Fig 9: combined CS+TS 3Y rolling Sharpe by style: carry mostly positive and strong in 2003-08, momentum falls to about 0 by 2013-15, value dips below zero 2006-09 and 2012. _(robustness, evidence)_ #mech/research_method
  > Figure 9. CS+TS: 3Y Rolling Sharpe per Asset Class (left) and per Investment Style (right)
  reported_result: Figure 9 read from chart · exhibit: Figure 9
  ^QP08-C24-2

### C25 (page 25)
- Fig 10-11: CS+TS 1Y rolling correlations still unstable; compounded P&L of combined V+C+M grows from 100 to about 700, Sharpe 1.61. _(result, evidence)_ #mech/research_method
  > Figure 11. CS+TS: Value+Carry+Momentum Compounded P&L
  reported_result: Figure 11: P&L index 100 to ~700 (1990-2015), Sharpe 1.61; Figure 10 V-C corr -0.55 to +0.55 · exhibit: Figures 10, 11
  ^QP08-C25-1
- CS+TS style correlations also swing (carry-momentum up to ~0.75 around 1992; value-carry down to ~-0.55). _(robustness, evidence, Opus only)_ #mech/research_method
  > Figure 10. CS+TS: 1Y Rolling Correlations
  reported_result: Figure 10 (read from chart): C-M ~0.75 max (1992); V-C ~-0.55 min (1992, 2007-08) · exhibit: Figure 10
  ^QP08-C25-1b

### C26 (page 26)
- Combined CS+TS portfolio over 25 years: Sharpe near 2 (reported 1.61), about eight-fold growth on a hypothetical 15% vol investment; considered genuine because funding costs are low (hypothetical, no transaction costs). _(result, conclusion)_ #mech/research_method
  > returning an approximately eight-fold increase on a hypothetical 15% volatility investment
  reported_result: Sharpe ~1.6 (text says 'close to 2'); about 8x on 15% vol; gross of costs · exhibit: Section 5; Figure 12
  ^QP08-C26-1
- Too-good-to-be-true check 1: selection bias (styles chosen because they worked), but few styles apply across diverse asset classes so the selection pool is small. _(caveat, qualifier)_ #mech/research_method
  > Selection bias is a partial answer.
  ^QP08-C26-2
- Check 2: no parameter fitting, but experience matters (value looks back much further than momentum because momentum works at medium frequencies and value is a long-term game). _(caveat, qualifier)_ #mech/research_method
  > There was no fitting in this exercise, although some po- tentially creeps in from experience.
  ^QP08-C26-3
- Check 3: survivorship; Argentina excluded but Russia, Greece, Indonesia included; removing turmoil markets likely biases value and carry upward. _(caveat, qualifier)_ #mech/research_method
  > This kind of bias will likely favor value and carry through the removal of markets where turmoil has caused major assets to exit.
  ^QP08-C26-4
- Check 4: markets that were small in 1990 and are big now have often trended up, adding a positive bias to momentum predictors. _(caveat, qualifier)_ #mech/research_method
  > we likely give a positive bias to momentum predictors
  ^QP08-C26-5
- Check 5: behavioural/institutional reason persistence - few firms tolerate multi-year losses; value was declared dead in 1999, carry toxic in 2008, momentum finished in 2011-13. _(mechanism, mechanism_step)_ #mech/behavioral
  > few firms have the appetite and patience to trade something so simple
  ^QP08-C26-6
- CS+TS 3-year rolling Sharpe ranges about 0.55 (around 1999-2000) to 2.6 (1997). _(robustness, evidence, Opus only)_ #mech/research_method
  > Figure 12. CS+TS: 3Y Rolling Sharpe (left) and Monthly Return Distribution
  reported_result: Figure 12 (read from chart): min ~0.55 around 2000; max ~2.6 · exhibit: Figure 12
  ^QP08-C26-1b

### C27 (page 27)
- Each style has had negative performance for at least three years at some point (Figures 1, 5, 9), hard to stick with. _(robustness, qualifier)_ #mech/research_method
  > with each style experiencing negative performances for at least three years
  reported_result: drawdown spells of 3+ years in each style (Figs 1, 5, 9) · exhibit: Figures 1, 5, 9
  ^QP08-C27-1
- Conclusion: positive average returns are no surprise since the styles were selected for past success; the paper's contribution is when to implement cross-sectionally versus in the time series. _(caveat, conclusion)_ #mech/research_method
  > There is a reason that carry, value and momentum are popular. They have worked well in the past.
  ^QP08-C27-2
- Suggested ex-ante framework: relative TS vs CS performance depends on correlation of asset returns and correlation of trading signals; left to ongoing research. _(mechanism, conclusion)_ #mech/research_method
  > Our results are suggestive of a framework that may help identify, ex ante, the likelihood that a directional will outperform a cross-asset implementation
  ^QP08-C27-3

### C28 (page 28)
- Reference list: Asness-Moskowitz-Pedersen (2013) value and momentum everywhere; Moskowitz-Ooi-Pedersen (2012) time series momentum; Koijen et al. (2013) Carry; Harvey-Liu-Zhu factor proliferation; Erb-Harvey (2006) commodities. _(citation, context)_ #mech/research_method
  > Moskowitz, T., Hua Ooi, Y., and Pedersen, L.H. (2012). “Time Series Momentum.”
  ^QP08-C28-1

### C29 (page 29)
- FX universe of 31 currencies versus USD (G10, EM Asia, Latam, CEEMEA, South Africa); signal start dates vary per series (value from 1974-1990s, carry 1983-2008, momentum 1972-2000). _(construction, design_choice)_ #mech/research_method
  > We considered 31 currencies, all expressed versus the USD, to avoid information redundancies.
  data_needed: 31 USD crosses; value/carry/momentum series start dates in Appendix · exhibit: Appendix 8.1 FX table
  ^QP08-C29-1

### C30 (page 30)
- Equity universe: 26 indices (US S&P, Dow, Nasdaq, Midcap, Russell 2000; Europe; Japan Nikkei/Topix; UK; Switzerland; Latin America, Asia, CEEMEA; Australia); start dates by index and signal given (carry from 1983-2003, momentum from 1983-2001). _(construction, design_choice)_ #mech/research_method
  > The equity sample covers 26 indices across several geographic regions.
  data_needed: 26 equity index series; dividend yield history from 1954-1977 for some · exhibit: Appendix 8.1 Equity table
  ^QP08-C30-1

### C31 (page 31)
- Commodity universe: 16 futures (gold, silver, platinum, palladium, copper, nickel, aluminium, crude, natgas, corn, wheat, soybean, coffee, cocoa, sugar, cotton); rates universe: 14 10Y swaps (10 G10 and HUF, PLN, ZAR, PHP) with start dates 1988-2003. _(construction, design_choice)_ #mech/research_method
  > We used a mix of commodity futures (16 in total).
  data_needed: 16 commodity futures; 14 10Y swap series · exhibit: Appendix 8.1 commodities and rates tables
  ^QP08-C31-1
- Rates universe: 10Y swaps for EUR, GBP, JPY, USD, NZD, AUD, CHF, CAD, NOK, SEK, HUF, PLN, ZAR, PHP (Bloomberg tickers like USSWAP10), starting 1988-2001. _(construction, design_choice, Opus only)_ #mech/research_method
  > We used swap data (14 in total). Here is the complete list:
  data_needed: 10Y swap rates (Bloomberg <ccy>SW10 tickers), 7Y swaps, fixings, GDP, CPI
  ^QP08-C31-2b

