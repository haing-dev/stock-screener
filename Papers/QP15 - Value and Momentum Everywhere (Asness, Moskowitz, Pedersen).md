---
source_id: QP15
title: "Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)"
type: paper
claims: 283
opus_only: 102
tags: [paper, layer0]
---
# Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)

**Authors:** Clifford S. Asness (AQR Capital Management); Tobias J. Moskowitz (University of Chicago Booth, NBER, AQR consultant); Lasse Heje Pedersen (NYU Stern, CBS, AQR, CEPR, NBER)

**Summary:** Question: do value and momentum premia exist across eight markets/asset classes (US, UK, Europe, Japan stocks; country indices; currencies; bonds; commodities), how are they correlated, and what explains the common structure? Method: simple uniform value and 2-12 month momentum signals, tercile portfolios and rank-weighted long-short factors, 1972-2011, with factor, PCA, liquidity-risk, Fama-MacBeth and GRS tests. Conclusion: premia are positive everywhere, value-with-value and momentum-with-momentum correlations are positive across assets while value-momentum is negative, the 50/50 combination reaches Sharpe about 1.4-1.6, and funding liquidity risk (mainly post-1998) explains only part of it; a global three-factor model prices 48 test assets, Fama-French portfolios and hedge funds.

## Argument map

**Question:** Are value and momentum premia a U.S.-stock curiosity or a pervasive feature of all liquid markets, do they share common sources across asset classes, and what single parsimonious model could describe global multi-asset returns? For an investor this decides whether value and momentum can be diversified across asset classes, whether a value+momentum combination is a robust core allocation, and what risks (e.g., funding liquidity) the positions carry.

**Thesis:** Value and momentum earn positive premia in every major asset class, value co-moves with value and momentum with momentum across unrelated markets while the two are negatively correlated, and a global market+value+momentum model prices these portfolios, U.S. stock portfolios and hedge funds better than U.S. factors; funding liquidity risk explains part of the comovement (especially after 1998) but not the premia, and the 50/50 combination remains a large, liquidity-neutral puzzle. ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C01-1|C01-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C01-3|C01-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C01-4|C01-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C15-4|C15-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C21-3|C21-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C38-2|C38-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C46-1|C46-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C34-4|C34-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C53-4|C53-4]])

### Foundations (premises)
- A premium that appears with the same simple signal in many unrelated asset classes is unlikely to be a data-mining artifact; uniform simple measures are an out-of-sample test. _[assumed, stated; support: intuition; deliberate choice of standard signals; asserted that better signals would raise returns]_ ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C04-2|C04-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C08-1|C08-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C19-3|C19-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C49-3b|C49-3b]])
- Long-horizon past price declines (negative 5-year return, 5-year PPP change, 5-year yield rise) measure 'cheapness' in assets that have no book value, just like BE/ME in stocks. _[empirical, stated; support: DeBondt-Thaler, Fama-French 1996, Gerakos-Linnainmaa; own test: 0.83 (U.S.) and 0.86 (global) correlation between 5-year-return and BE/ME value factors]_ ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C09-6|C09-6]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C09-6|C09-6]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C10-1|C10-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C10-1|C10-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C08-4|C08-4]])
- Past 12-month return skipping the latest month captures momentum in every asset class; the skip month avoids a short-term reversal tied to liquidity/microstructure. _[empirical, stated; support: standard in literature (Jegadeesh-Titman, Asness, Goyal-Wahal), out-of-sample record]_ ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C08-5|C08-5]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C08-6|C08-6]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C09-1b|C09-1b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C09-11b|C09-11b]])
- Comovement of long-short, market-neutral strategies across markets with different investors and institutions points to a common global risk factor rather than market-specific behaviour. _[theoretical, stated; support: interpretation of correlation and PCA evidence; argued that behavioral models do not predict it]_ ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C03-10|C03-10]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C22-1|C22-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C22-2|C22-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C23-1|C23-1]])
- Equity-specific rational theories (firm investment, growth options) and individual-investor behavioral theories cannot generate correlated effects in currencies, bonds and commodities. _[theoretical, stated; support: argument, citations to the theories; no formal test]_ ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C04-1|C04-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C18-3|C18-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C53-3|C53-3]])
- Momentum trades are crowded (return chasing) while value trades are contrarian, so forced liquidations in funding shocks hit momentum harder. _[behavioural, stated; support: intuitive story (Pedersen 2009 'run for the exit'); crowding is not measured]_ ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C04-6|C04-6]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C04-8b|C04-8b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C04-7|C04-7]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C04-7|C04-7]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C34-3|C34-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C34-6b|C34-6b]])
- Liquidity risk carries a positive risk premium. _[empirical, stated; support: Fama-MacBeth liquidity-beta premium of 24 bp/month (t=3.05) among the 48 portfolios; earlier literature]_ ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C34-2|C34-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C43-1|C43-1]])
- Averaging strategies across many markets diversifies idiosyncratic noise so a weak common exposure becomes detectable. _[empirical, stated; support: Figure 4: average individual t-stats -0.95/1.81 vs -3.25/4.43 for the averaged series]_ ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C03-7|C03-7]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C36-1|C36-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C35-1|C35-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C36-1|C36-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C21-2|C21-2]])
- Large, liquid universes (top 90% of market cap; futures) give implementable and conservative estimates because premia are larger in small illiquid securities. _[empirical, stated; support: citations; earlier draft with broader universe had stronger returns]_ ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C05-4|C05-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C06-3|C06-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C06-3|C06-3]])

### Mechanism chain
- 1. investors chase recent winners and shun multi-year losers → momentum positions are crowded; value positions are contrarian and cheap: return chasing makes momentum the most popular trade; value buys assets after long price declines _[assertion]_ ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C04-6|C04-6]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C04-8b|C04-8b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C34-3|C34-3]])
- 2. funding liquidity shock (wider TED/LIBOR-repo/swap spreads, redemptions, risk limits) → simultaneous liquidations by leveraged arbitrageurs/funds: cash needs and risk management force selling at the same time ('run for the exit'); Brunnermeier-Pedersen funding constraints _[citation]_ ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C04-8|C04-8]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C04-7|C04-7]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C34-6b|C34-6b]])
- 3. liquidations → momentum falls and value holds up when funding worsens (and the reverse when funding eases): price pressure concentrates on crowded trades _[test]_ ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C33-1|C33-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C31-2b|C31-2b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C32-2|C32-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C51-4|C51-4]])
- 4. opposite funding-liquidity loadings → part of the negative value-momentum correlation: a common shock moves the two strategies in opposite directions _[test]_ ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C03-4|C03-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C33-1|C33-1]])
- 5. global capital flowing simultaneously across asset classes (delegated management, slow-moving capital) → value-with-value and momentum-with-momentum correlation across asset classes: same arbitrage capital and funding conditions span markets; Vayanos-Woolley flows create momentum then reversal _[citation]_ ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C05-1|C05-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C05-1|C05-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C51-5b|C51-5b]])
- 6. Aug 1998 LTCM funding crisis and growth of leveraged arbitrage → higher cross-market correlations and liquidity-dependent performance after 1998: funding risk became a more important driver after 1998 _[test]_ ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C03-6|C03-6]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C51-3|C51-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C51-4|C51-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C53-3b|C53-3b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C53-4b|C53-4b]])
- 7. momentum's positive liquidity beta x positive liquidity premium → part of momentum's premium is compensation for liquidity risk: standard risk-premium logic _[test]_ ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C34-2|C34-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C43-1|C43-1]])
- 8. value's negative liquidity beta and the combo's zero liquidity beta → value and combo premia remain unexplained by liquidity: a liquidity hedge should earn a lower, not higher, premium; a liquidity-neutral combo with large returns cannot be liquidity compensation _[test]_ ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C03-9|C03-9]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C03-9|C03-9]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C34-2|C34-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C34-4|C34-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C35-2b|C35-2b]])

### Design rationale
- **One simple, standard value and momentum signal per asset class (BE/ME or negative 5-year return/yield change; MOM2-12)**: uniformity across assets and minimal data snooping, not maximal predictive power. Alternatives: real yield, term spread, composite bond value; MOM7-12; better stock value measures; no skip month. Sensitivity: bond value improves from SR 0.18 to 0.73 (real yield), 0.55 (term spread), 0.91-1.10 (composite); no-skip momentum stronger in futures/FX; MOM7-12 asserted not to matter (not shown) ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C08-1|C08-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C08-3b|C08-3b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C16-2b|C16-2b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C16-1|C16-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C16-4b|C16-4b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C19-2|C19-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C19-2|C19-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C09-1|C09-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C09-12b|C09-12b]])
- **Book value lagged 6 months but divided by current market value**: data availability; the 1-year price lag issue is not critical for conclusions. Alternatives: Fama-French timing (lagged ME), ME lagged 1 year, negative 5-year return. Sensitivity: value-momentum correlation -0.53 (current ME) vs -0.28 (ME lagged 1y) vs -0.48 (5y return); value premium slightly lower with recent prices; combo pricing unchanged ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C08-2|C08-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C08-3|C08-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C08-7b|C08-7b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C22-4|C22-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C22-4|C22-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C22-4|C22-4]])
- **Value proxies from 4.5-5.5-year average past prices (commodities, FX with CPI adjustment) and 5-year 10y-yield change (bonds)**: no book value exists; long-term reversal literature and 0.83-0.86 correlation with BE/ME in stocks. Alternatives: real bond yield, term spread (Panel C). Sensitivity: bond value weak with baseline; strong with alternatives; other asset classes not tested with alternatives ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C09-3|C09-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C09-4|C09-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C09-5|C09-5]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C10-1|C10-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C10-1|C10-1]])
- **Rank-weighted, dollar-neutral ($1 long/$1 short) factors plus tercile P3-P1 portfolios**: ranks limit outliers; linear signal weights outperform coarse terciles and diversify better. Alternatives: raw-signal weights, deciles, terciles. Sensitivity: raw signals similar/slightly better; deciles similar; terciles weaker Sharpe ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C10-4|C10-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C10-4|C10-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C10-4|C10-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C11-2|C11-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C11-2|C11-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C49-2|C49-2]])
- **Value-weight stocks within portfolios; equal-weight non-stock assets; monthly rebalance**: liquidity/conservatism for stocks; market cap meaningless elsewhere. Alternatives: ex ante vol weights; annual rebalancing. Sensitivity: similar results ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C10-4b|C10-4b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C10-3|C10-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C48-4|C48-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C49-5b|C49-5b]])
- **Large-cap universe: stocks making up 90% of each market's cap**: implementability and conservative estimates comparable to liquid futures. Alternatives: broader universe in earlier draft. Sensitivity: broader universe gave significantly stronger returns ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C05-4|C05-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C06-3|C06-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C06-3|C06-3]])
- **Aggregate markets and asset classes with inverse full-sample volatility weights**: volatilities differ greatly (commodities ~4x bonds); equal risk contribution. Alternatives: cap or equal weights; ex ante rolling vol/cov; 2% ex ante vol target with 3-year daily vol. Sensitivity: all reported as similar; ex post weights embed look-ahead ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C12-1|C12-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C17-5|C17-5]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C17-8b|C17-8b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C18-1|C18-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C18-6|C18-6]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C49-3|C49-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C50-1|C50-1]])
- **50/50 value-momentum combination**: negative correlation and positive means put the combination near the efficient frontier and stabilize it across markets. Alternatives: value or momentum alone; static optimization (Japan). Sensitivity: combo Sharpe exceeds either component in every asset class ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C11-1|C11-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C04-3|C04-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C17-1|C17-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C17-6b|C17-6b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C15-4|C15-4]])
- **Correlations on quarterly returns of averaged series**: nonsynchronous trading; averaging diversifies noise. Alternatives: pairwise averages (Internet Appendix), P3-P1 portfolios. Sensitivity: pairwise correlations weaker but same pattern ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C20-1|C20-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C21-1|C21-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C21-2|C21-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C21-2|C21-2]])
- **Liquidity shocks as AR(2) residuals of sign-flipped spreads; PC indices from correlation matrices**: follow Moskowitz-Pedersen and Korajczyk-Sadka; correlation matrix because units differ. Alternatives: AR(1), AR(3), first differences; Sadka and Adrian-Shin measures. Sensitivity: similar results ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C30-1|C30-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C30-4b|C30-4b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C30-2|C30-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C30-3|C30-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C30-2|C30-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C30-4|C30-4]])
- **Two separate value and momentum factors rather than one**: both earn positive means while negatively correlated. Alternatives: single factor with time-varying betas/premia; Mkt+VAL or Mkt+MOM only. Sensitivity: dropping either factor worsens pricing considerably ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C03-2|C03-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C03-2|C03-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C46-8b|C46-8b]])

### Evidence map
- Positive value and momentum premia in all 8 asset classes; global all-asset value SR 0.72, momentum 0.74, combo 1.59 (factors), 1972-2011 gross. Tests: premise that premia are pervasive. Rules out: pure U.S.-stock data mining. Does not rule out: (reader) common backtest design choices, gross-of-cost overstatement, look-ahead in vol weights; several individual classes insignificant (bonds, Japan momentum, commodity value t=1.92, FX momentum t=1.77). Strength: strong in aggregate, moderate per asset class ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C15-4|C15-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C13-1|C13-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C13-3|C13-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C14-3|C14-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C15-1|C15-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C15-2|C15-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C17-2|C17-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C17-2|C17-2]])
- Value-value and momentum-momentum correlations positive across markets (0.68, 0.65 within stocks; 0.15, 0.37 stocks vs non-stocks), value-momentum negative everywhere (-0.53 to -0.13); PC1 long momentum/short value explains 54% (stocks) and 23% (all assets). Tests: common global factor premise. Rules out: explanation by passive asset-class correlation (strategies are market neutral). Does not rule out: (reader) mechanical overlap from shared global flows of a few large arbitrageurs; non-stock value diagonal only 0.07 (insignificant); bond value loads ~0 on PC1. Strength: strong for stocks, moderate for non-stock value ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C20-2|C20-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C22-1b|C22-1b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C22-2b|C22-2b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C22-4b|C22-4b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C22-2|C22-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C23-2b|C23-2b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C23-1|C23-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C24-1|C24-1]])
- Negative value-momentum correlation survives ME lagged one year (-0.28) and 5-year-return value (-0.48). Tests: that correlation is not a mechanical price-overlap artifact. Rules out: pure overlap of current price in BE/ME and momentum. Does not rule out: (reader) remaining overlap of the 5-year window with the 12-month window. Strength: moderate - magnitude halves when overlap removed ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C22-4|C22-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C22-4|C22-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C22-4|C22-4]])
- Macro variables (LRC growth, recession, GDP, TERM, DEF) explain little; momentum lower in recessions; DEF negative for momentum. Tests: macro-risk explanation. Rules out: simple unconditional macro-risk explanations. Does not rule out: (reader) conditional/time-varying macro exposures; intercepts not reported. Strength: moderate - low R2 (2-13%) but no alpha reported ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C28-2|C28-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C28-2|C28-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C28-3|C28-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C28-7b|C28-7b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C29-1b|C29-1b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C30-1b|C30-1b]])
- Global funding liquidity PC: value -0.0094 (t=-4.74), momentum +0.0112 (t=3.58), combo ~0 (t=0.58); market liquidity insignificant. Tests: mechanism steps 3-4 (opposite funding exposure). Rules out: market liquidity as main channel; risk-aversion proxy story (value and momentum move oppositely). Does not rule out: (reader) funding shocks proxying for other common shocks (e.g., equity crashes, rebounds such as 2009) driving momentum crashes; sample only 1987-2011. Strength: moderate - significant only for averaged series; individual t-stats weak ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C32-2|C32-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C33-1|C33-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C33-2|C33-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C33-1|C33-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C35-1|C35-1]])
- Liquidity beta priced (24 bp/month) cross-sectionally, but subsumed by VAL/MOM betas and insignificant once market beta is added; liquidity FP lowers |alpha| only from 35 to 31 bp. Tests: whether liquidity explains premia. Rules out: liquidity as a full explanation. Does not rule out: (reader) measurement error in liquidity proxies understating its role. Strength: moderate ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C42-1|C42-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C42-1|C42-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C43-1|C43-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C43-4b|C43-4b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C46-3b|C46-3b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C46-2|C46-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C46-5b|C46-5b]])
- Factors from other markets explain 55% of the cross-section of each market's portfolios (no security overlap); global 3-factor model R2 0.71-0.72, |alpha| 18 bp, beats CAPM and FF4/FF6; prices FF 25+25 U.S. portfolios (R2 0.64-0.68) and hedge fund indices better than FF. Tests: common factor structure and global three-factor model. Rules out: market-specific premia without common pricing. Does not rule out: (reader) that VAL/MOM factors 'price' VAL/MOM portfolios partly by construction; GRS rejects every model including AMP. Strength: moderate - good fit but formally rejected ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C37-1|C37-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C37-3b|C37-3b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C38-2|C38-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C38-4b|C38-4b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C39-1|C39-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C39-2b|C39-2b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C41-2b|C41-2b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C46-1|C46-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C47-1|C47-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C47-2|C47-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C47-3|C47-3]])
- Within-style correlations rose (value 0.31 to 0.71, momentum 0.46 to 0.77) and jumped after Aug 1998; liquidity-conditional performance only after 1998; combo Sharpe stable. Tests: step 6 (funding risk growing post-1998). Rules out: a smooth time trend as the driver (dummy subsumes trend). Does not rule out: (reader) other post-1998 changes (euro, decimalization, ETF/quant growth, 2000 and 2008-09 crises) in a short post-1998 sample. Strength: weak to moderate - one break date, few independent episodes ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C51-2|C51-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C51-3|C51-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C51-4|C51-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C51-4|C51-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C52-1|C52-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C53-3b|C53-3b]])

### Regimes
- Funding liquidity worsening (post-1998) → value strong (SR 0.85), momentum weak (SR 0.19); combo 0.88 ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C51-4|C51-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C51-3|C51-3]])
- Funding liquidity improving (post-1998) → value weak (SR 0.28), momentum strong (0.77 table / 0.99 text); combo 1.07 ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C51-4|C51-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C51-3|C51-3]])
- Before Aug 1998 → funding shocks have little effect on value or momentum; cross-market correlations low (value 0.16, momentum 0.43) ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C51-3|C51-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C51-4|C51-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C53-3b|C53-3b]])
- Recessions → momentum returns lower (esp. non-stock); cross-market correlations of momentum (and marginally value) rise ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C28-7b|C28-7b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C53-1|C53-1]])
- Japan stocks → momentum fails (t=0.57) while value is very strong; combo still SR 0.88 ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C13-3|C13-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C13-1|C13-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C17-3|C17-3]])
- Government bonds with price-based value → value and momentum insignificant; yield-level value measures work ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C15-1|C15-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C19-1b|C19-1b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C16-2b|C16-2b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C16-1|C16-1]])
- Tech bubble 1999-2000 → large value drawdown across stock markets offset by momentum gains (reader reading of Figure 2) ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C25-1|C25-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C25-4b|C25-4b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C27-1b|C27-1b]])

### Gaps and conflicts
- [conflict] Text says the three-factor model captures 84% of covariation of the 48 portfolios; Table VI shows 74%, and the macro/liquidity six-factor model shows 80% (higher than AMP on this metric). ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C46-1|C46-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C44-1|C44-1]])
- [conflict] Post-1998 momentum Sharpe in improving liquidity is 0.99 in the text but 0.77 in Table VII. ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C51-4|C51-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C51-3|C51-3]])
- [conflict] (reader) Table VII post-1998 combo Sharpe 1.39 exceeds both liquidity-split sub-period Sharpes (0.88, 1.07), and post-1998 momentum 0.72 is high relative to 0.19/0.77; arithmetically hard to reconcile if the splits partition the same period. ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C51-3|C51-3]])
- [unspecified] (reader) Table I combo 'Factor' column is not 0.5*(value+momentum) in several classes (e.g., commodities combo 17.1% with 22.2% vol vs 7.3% and 11.5% components; country indices 10.6%; global all 6.8% vs 5.0%) - the combo factor appears rescaled; scaling unstated. Sharpe ratios unaffected. ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C15-2|C15-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C14-2|C14-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C15-4|C15-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C11-1|C11-1]])
- [conflict] The '50/50 combination is immune to liquidity risk' claim holds for the global funding PC but U.S. TED (t=2.13), swap-T-bill (t=3.67) and Acharya-Pedersen (t=3.05) combo loadings are significant, and post-1998 combo Sharpe differs (0.88 vs 1.07) across liquidity regimes. ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C03-9|C03-9]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C34-4|C34-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C31-4b|C31-4b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C51-4|C51-4]])
- [conflict] Combo Sharpe across all assets: 1.45 in text vs 1.42 (P3-P1) and 1.59 (factor) in Table I/Figure 2. ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C18-4|C18-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C15-4|C15-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C27-1|C27-1]])
- [conflict] Dates: bond sample Jan 1982 vs Panel C Jan 1983; Figure 3 Jan 1987-Jun 2010 vs text Jul 2011; Table VII second half 1992-2010 vs text 2011; Table VI/VII captions cite Tables IV/III for objects defined in Tables V/IV. ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C16-1b|C16-1b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C33-2b|C33-2b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C52-2b|C52-2b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C44-3b|C44-3b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C52-4b|C52-4b]])
- [data] Cross-asset aggregation uses full-sample (ex post) volatility weights, a look-ahead; ex ante versions are only said to be 'similar' (Internet Appendix), no numbers. ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C17-5|C17-5]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C49-3|C49-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C18-6|C18-6]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C50-1|C50-1]])
- [untested] All results gross of transaction costs, no capacity/turnover numbers; monthly rebalancing ignores costs; implementability argued by citation only. ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C48-1|C48-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C48-3|C48-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C48-4|C48-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C18-5|C18-5]])
- [untested] Crowding/forced-liquidation mechanism is a story; crowding, fund flows and arbitrage capital are never measured. ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C04-7|C04-7]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C34-6b|C34-6b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C05-1|C05-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C51-5b|C51-5b]])
- [unspecified] Several robustness claims asserted without numbers: MOM7-12, beta-neutral hedging, decile sorts, ex ante vol, raw-signal weights, cap-weighted markets. ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C09-12b|C09-12b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C50-2|C50-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C49-2|C49-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C10-4|C10-4]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C17-8b|C17-8b]])
- [unspecified] Table V: liquidity premium becomes insignificant (t=0.56) once a market beta is added (row not discussed), and GDP-growth beta turns significant in the full model; text does not address these. ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C42-1|C42-1]])
- [unspecified] Table III intercepts not reported, so how much premium remains after macro controls is not shown; recession dummy coding (0=peak, 1=trough) is ambiguous. ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C29-1b|C29-1b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C29-2b|C29-2b]])
- [unspecified] Composite bond value averaging/standardization method and real-yield inflation-forecast horizon details not fully specified; estimation window for AR(2) shocks unspecified. ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C16-4b|C16-4b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C30-2|C30-2]])
- [untested] Every pricing model including the global three-factor model is rejected by GRS (p=0) on all test sets. ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C39-2b|C39-2b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C47-3|C47-3]])
- [data] Conflict of interest: authors affiliated with AQR, which runs value and momentum strategies. ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C01-5b|C01-5b]])

### Relations to other strategies
- time-series momentum (trend following): **complement**. TSMOM times each asset on its own past return; this paper is cross-sectional relative momentum, same 12-1 lookback family ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C04-4|C04-4]])
- carry: **complement**. cited as another global multi-asset premium (Koijen et al.); currency returns here implicitly include the interest differential ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C04-5|C04-5]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C07-3b|C07-3b]])
- betting against beta: **complement**. cited as another consistent global premium ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C04-5|C04-5]])
- long-term reversal (DeBondt-Thaler): **special case**. value in non-stock assets is defined as negative 5-year return, i.e., long-term reversal ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C09-6|C09-6]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C09-6|C09-6]])
- real yield / term spread as bond value (carry-like): **substitute**. yield-level bond value works better than price-based value and is uncorrelated or positively correlated with momentum ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C16-2b|C16-2b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C16-1|C16-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C16-1|C16-1]])
- Fama-French/Carhart U.S. factors: **substitute**. global VAL/MOM everywhere factors price global portfolios and hedge funds better and U.S. portfolios almost as well ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C38-3|C38-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C41-1|C41-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C47-1|C47-1]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C47-2|C47-2]])
- funding liquidity risk (Brunnermeier-Pedersen): **complement**. partly explains comovement and value-momentum negative correlation, not the premia ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C03-6|C03-6]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C34-2|C34-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C46-2|C46-2]])
- macro/consumption risk (long-run risk): **contradicts**. macro variables explain little of value/momentum returns except U.S. value's link to long-run consumption ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C03-3|C03-3]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C28-2|C28-2]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C28-3|C28-3]])
- hedge fund returns: **complement**. hedge fund indices load on global value and momentum, suggesting similar trades ([[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C47-4b|C47-4b]], [[QP15 - Value and Momentum Everywhere (Asness, Moskowitz, Pedersen)#^QP15-C51-1|C51-1]])

### Forward-looking inputs (reader synthesis)
(reader) Cross-sectional ranks of (a) multi-year cheapness - negative 5-year price/real exchange-rate change, 5-year rise in 10y yields or (better) real yield and term spread for bonds, BE/ME for stocks and country indices - and (b) 12-1 month relative returns are the inputs that lead returns over the next month (rebalanced monthly; effect horizon roughly months to a few years). They work through slow-moving capital/return chasing (momentum) and later overshoot correction (value), with risk compensation and funding constraints in the background. Funding liquidity shocks (TED, LIBOR-repo, swap-T-bill spreads; AR(2) residuals) are contemporaneous drivers, not predictors: worsening funding hurts momentum and helps value. What would make them stop working: arbitrage capital crowding raising correlations (seen post-1998), sharp liquidity rebounds that crash momentum (2009), and for value long bubbles (1999-2000); the 50/50 mix is the version least exposed to these regime swings.

### Reader inferences (not stated by the authors)
- (reader) The combo factor column in Table I appears rescaled (not a literal 0.5/0.5 average) for several asset classes; scaling not stated.
- (reader) Table VII post-1998 conditional Sharpe ratios look arithmetically inconsistent with the unconditional post-1998 row, and Table VII Sharpe levels match the P3-P1 tercile spreads rather than the rank factors.
- (reader) Large value drawdowns around 1999-2000 and a momentum drop around 2009 are visible in Figure 2 but not discussed in the text.
- (reader) Bond value (baseline measure) does not share the common factor (PC1 loading ~0) and has a deep 1980s-early 1990s drawdown, so bond results are fragile.
- (reader) Funding-liquidity regressions use contemporaneous shocks; they describe risk exposure, not a timing signal.
- (reader) Ex post volatility weights and full-sample normalisation mean the published Sharpe ratios are not exactly implementable; costs would lower stock strategies most.
- (reader) Part of the three-factor model's pricing success on the 48 portfolios is mechanical because VAL/MOM factors are built from the same securities (equation 5), which the authors acknowledge; the leave-one-out equation (4) R2 of 0.55 is the cleaner evidence.

## Claims

### C01 (page 1)
- Value and momentum earn significant premia in every one of eight markets/asset classes and their returns co-move strongly across asset classes, which challenges existing single-market theories. _(result, conclusion)_ #mech/risk_premium
  > We find significant return pre- mia to value and momentum in every asset class and strong comovement of their returns across asset classes,
  reported_result: Significant premia in all eight markets; strong cross-asset comovement (details Tables I-III) · exhibit: Introduction
  ^QP15-C01-1
- A three-factor model (global market, global value, global momentum) prices the 48 test assets, Fama-French US portfolios and hedge fund indices. _(result, conclusion)_ #mech/risk_premium
  > We provide a simple three-factor model that captures the global returns across asset classes, the Fama–French U.S. stock portfolios, and a set of hedge fund indices.
  ^QP15-C01-2
- Value and momentum are negatively correlated with each other within and across asset classes, though each is positively correlated with itself across asset classes. _(result, premise)_ #mech/risk_premium
  > value and momentum are negatively correlated with each other, both within and across asset classes
  ^QP15-C01-3
- Funding liquidity risk is only a partial source of the value/momentum patterns and shows up only when markets are examined jointly. _(result, conclusion)_ #mech/liquidity_flows
  > Global funding liquidity risk is a partial source of these patterns, which are identifiable only when examining value and momentum jointly across markets.
  ^QP15-C01-4
- Because the premia and their correlations appear in non-equity asset classes, theories built for U.S. stocks alone cannot fully explain them. _(mechanism, conclusion, Opus only)_ #mech/research_method
  > Our findings present a challenge to existing behavioral, institutional, and rational asset pricing theories that largely focus on U.S. equities.
  ^QP15-C01-4b
- Authors disclose a commercial interest: their employer/consultancy invests in value and momentum strategies. _(caveat, context, Opus only)_ #mech/research_method
  > AQR Capital invests in, among other things, value and momentum strategies.
  ^QP15-C01-5b

### C02 (page 2)
- Universe: eight markets - individual stocks in US, UK, continental Europe and Japan, country equity index futures, government bonds, currencies and commodity futures. _(construction, design_choice)_ #mech/research_method
  > We uncover unique evidence and features of value and mo- mentum by examining them jointly across eight different markets and asset classes
  exact_rule: Eight markets: US, UK, Europe ex-UK, Japan stocks; country equity index futures; government bonds; currencies; commodity futures · data_needed: see Section I.A
  ^QP15-C02-1
- Value and momentum premia exist in all markets studied, including novel evidence for momentum and value in government bonds and value in currencies and commodities. _(result, conclusion)_ #mech/risk_premium
  > We find consistent and ubiquitous evidence of value and momentum return premia across all the markets we study
  ^QP15-C02-2
- The multi-asset set of portfolios has larger dispersion in average returns than US-stock-only sets, making it a harder test for asset pricing models. _(result, evidence)_ #mech/research_method
  > Our broader set of portfolios generates much larger cross-sectional dispersion in average returns than those from U.S. stocks only
  ^QP15-C02-3
- Value is positively correlated with value across unrelated markets, and momentum with momentum, pointing to common global factors. _(result, premise)_ #mech/risk_premium
  > Value strategies are positively correlated with other value strategies across otherwise unrelated markets, and momentum strategies are positively correlated with other mo-
  ^QP15-C02-4
- A three-factor model of global market index plus zero-cost value and momentum strategies across all asset classes explains both comovement and average returns, globally and within asset classes. _(result, evidence)_ #mech/risk_premium
  > we capture the comovement and the cross section of average returns both globally across asset classes and locally within an asset class
  exact_rule: Factors: global market index; zero-cost value strategy across all asset classes; zero-cost momentum strategy across all assets
  ^QP15-C02-5
- Citations: value in US equities (Stattman 1980, Rosenberg-Reid-Lanstein 1985, Fama-French 1992) and momentum in US stocks (Jegadeesh-Titman 1993, Asness 1994) with high 6-12 month past returns outperforming. _(citation, context)_ #mech/risk_premium
  > Early evidence on U.S. equities finds that value stocks on average outperform growth stocks
  ^QP15-C02-6
- Prior evidence of momentum in country indices, currencies and commodities exists in separate studies (Asness-Liew-Stevens 1997, Bhojraj-Swaminathan 2006, Kho, LeBaron, Erb-Harvey, Gorton et al). _(citation, evidence)_ #mech/slow_reaction
  > Momentum is also found in currencies (Shleifer and Summers (1990), Kho (1996), LeBaron (1999)) and commodities (Erb and Harvey (2006), Gorton, Hayashi, and Rouwenhorst (2008)).
  ^QP15-C02-7

### C03 (page 3)
- The simple three-factor model is motivated by increasingly global finance and a wish for one model for all asset classes rather than specialised models. _(mechanism, design_choice)_ #mech/research_method
  > finance research and practice becoming increasingly global and the desire to have a single model that describes returns across asset classes
  ^QP15-C03-1
- Value and momentum need separate factors because both earn positive returns but are negatively correlated; a single factor would need time-varying betas or risk premia. _(result, design_choice)_ #mech/risk_premium
  > We show that separate factors for value and momentum best explain the data, rather than a single factor, since both strategies produce positive returns on average yet are negatively correlated.
  exhibit: footnote 2
  ^QP15-C03-2
- Value and momentum factor returns have only modest links to macro variables (business cycle, consumption, default risk). _(result, evidence)_ #mech/risk_premium
  > We find only modest links to macroeconomic variables such as the business cycle, con- sumption, and default risk.
  ^QP15-C03-3
- Liquidity risk is negatively related to value and positively related to momentum globally, so opposite-signed liquidity exposure explains part of the negative value-momentum correlation. _(result, mechanism_step)_ #mech/liquidity_flows
  > liquidity risk is negatively related to value and positively related to momentum globally across asset classes
  ^QP15-C03-4
- Pastor-Stambaugh (2003) and Sadka (2006) showed liquidity risk is positively related to momentum in US stocks; this paper extends the link to other markets and shows value is negatively related. _(citation, evidence)_ #mech/liquidity_flows
  > measures of liquidity risk are positively related to momentum in U.S. individ-
  ^QP15-C03-5
- Separating market from funding liquidity, funding liquidity risk is the primary link, and its importance has grown over time, especially since the 1998 funding crisis. _(result, mechanism_step)_ #mech/liquidity_flows
  > the primary link between value and momentum returns comes from funding risk, whose importance has increased over time, particularly af- ter the funding crisis of 1998.
  conditions: stronger after 1998
  ^QP15-C03-6
- Pooling across many markets gives the statistical power to detect the liquidity-risk exposures that are invisible in a single market. _(mechanism, qualifier)_ #mech/research_method
  > The statistical power gained by looking across many markets at once—a unique feature of our analysis—allows these factor exposures to be revealed.
  ^QP15-C03-7
- Liquidity risk explains only a small fraction of the premia and comovement; it may partly explain the momentum premium but makes the value premium a deeper puzzle. _(result, conclusion)_ #mech/liquidity_flows
  > liquidity risk can only explain a small fraction of value and momentum return premia and comovement
  conditions: value loads negatively on liquidity risk so cannot explain value premium
  ^QP15-C03-8
- A 50/50 value-momentum combination is immune to liquidity risk yet earns substantial abnormal returns. _(result, evidence)_ #mech/liquidity_flows
  > a simple equal- weighted combination of value and momentum is immune to liquidity risk and generates substantial abnormal returns.
  ^QP15-C03-9
- Strong cross-asset correlation structure of value/momentum is consistent with common global risk factors but is not predicted by existing behavioural models (Daniel et al 1998, Barberis et al 1998, Hong-Stein 1999). _(citation, evidence)_ #mech/behavioral
  > Conversely, such correlation structure is not a prediction of existing behavioral models
  ^QP15-C03-10
- The global three-factor model prices the Fama-French U.S. stock portfolios and hedge fund indices well. _(result, evidence, Opus only)_ #mech/risk_premium
  > three-factor model does a good job capturing the returns to the Fama and French U.S. stock portfolios as well as a set of hedge fund indices.
  ^QP15-C03-1b

### C04 (page 4)
- Rational theories based on firm investment risk or growth options (Gomes-Kogan-Zhang, Zhang, Berk-Green-Naik and others) are built for firm equity and cannot explain correlated value/momentum in currencies, bonds and commodities. _(mechanism, qualifier)_ #mech/risk_premium
  > These theories seem ill equipped to explain the same and correlated effects we find in currencies, government bonds, and commodities.
  ^QP15-C04-1
- Consistent premia across diverse asset classes help alleviate data-mining concerns. _(mechanism, evidence)_ #mech/research_method
  > the same and correlated effects we find in currencies, government bonds, and commodities
  ^QP15-C04-2
- Because value and momentum are negatively correlated with high expected returns, a simple combination is much closer to the efficient frontier and varies less across markets and time. _(mechanism, conclusion)_ #mech/risk_premium
  > a simple combination of the two is much closer to the efficient frontier than either strategy alone, and exhibits less variation across markets and over time
  ^QP15-C04-3
- Distinction: this paper studies cross-sectional momentum, not time-series momentum (Moskowitz, Ooi, Pedersen 2012), which times each asset on its own past return and covers only futures. _(citation, context)_ #mech/slow_reaction
  > Time- series momentum is a timing strategy using each asset’s own past returns, which is separate from the cross-sectional momentum strategies we study here.
  ^QP15-C04-4
- Related global multi-asset evidence: betting against beta (Frazzini-Pedersen 2010), carry (Koijen et al 2012), size/value/momentum in global equities (Fama-French 2012). _(citation, context)_ #mech/risk_premium
  > Frazzini and Pedersen (2010) find consistent returns to “betting against beta,” Koijen et al. (2012) document global “carry” returns
  ^QP15-C04-5
- Mechanism proposed: momentum is the popular, crowded trade (return chasing) while value is contrarian, so momentum loads positively and value negatively on liquidity risk. _(mechanism, mechanism_step)_ #mech/crowding_positioning
  > momentum represents the most popular trades, as investors chase returns and flock to the assets whose prices appreciated most recently
  ^QP15-C04-6
- In a liquidity shock, forced liquidators sell the crowded high-momentum positions hardest (Pedersen 2009), while less crowded value trades are less affected. _(mechanism, mechanism_step)_ #mech/crowding_positioning
  > investors engaged in liquidating sell-offs (due to cash needs and risk management) will put more price pressure on the most popular and crowded trades
  conditions: liquidity shocks / funding squeezes
  ^QP15-C04-7
- Funding constraints on global arbitrageurs (Brunnermeier-Pedersen 2009) may influence value and momentum returns. _(citation, mechanism_step)_ #mech/liquidity_flows
  > The link to funding liquidity risk may also be consistent with global arbitrage activity in the face of funding constraints influencing value and momentum returns
  ^QP15-C04-8
- Value positions are contrarian, hence less crowded. _(mechanism, mechanism_step, Opus only)_ #mech/crowding_positioning
  > Value, on the other hand, represents a contrarian view.
  ^QP15-C04-8b

### C05 (page 5)
- Vayanos-Woolley (2012): fund flows with slow-moving capital generate momentum, then push prices from fundamentals causing reversals (value); flows across asset classes could link correlations via funding liquidity. Matching the magnitude remains open. _(citation, mechanism_step)_ #mech/liquidity_flows
  > flows between investment funds can give rise to momentum effects from inertia due to slow moving capital, and eventually push prices away from fundamentals causing reversals or value effects
  conditions: magnitude match is an open question
  ^QP15-C05-1
- US stock universe: CRSP common equity (sharecodes 10, 11) with Compustat book value from the previous 6 months and at least 12 months of return history, January 1972 to July 2011. _(construction, design_choice)_ #mech/research_method
  > The U.S. stock universe consists of all common equity in CRSP (sharecodes 10 and 11) with a book value from Compustat in the previous 6 months
  exact_rule: US stocks: CRSP sharecodes 10/11; need Compustat BE within previous 6 months and >=12 months past returns; Jan 1972-Jul 2011 · data_needed: CRSP, Compustat
  ^QP15-C05-2
- Exclusions: ADRs, REITs, financials, closed-end funds, foreign shares, and stocks priced below $1 at month start. _(construction, design_choice)_ #mech/research_method
  > We exclude ADRs, REITs, financials, closed-end funds, foreign shares, and stocks with share prices less than $1 at the beginning of each month.
  exact_rule: Exclude ADRs, REITs, financials, closed-end funds, foreign shares, price < $1 at start of month
  ^QP15-C05-3
- Liquidity filter: each month rank stocks by market cap descending and keep those cumulatively making up 90% of total market cap (MSCI-style); this is the largest ~17% of US firms on average. _(construction, design_choice)_ #mech/research_method
  > include in our universe the number of stocks that account cumulatively for 90% of the total market capitalization
  exact_rule: Each month, sort by beginning-of-month market cap, keep top names that sum to 90% of total market cap in each market · reported_result: US universe = largest 17% of firms on average; 354 names in Jan 1972 to 676 in Jul 2011; larger and more liquid than Russell 1000 · exhibit: footnote 4
  ^QP15-C05-4
- Whether these flow/delegation models can match the empirical magnitudes is unresolved. _(caveat, qualifier, Opus only)_ #mech/research_method
  > However, matching the magnitude of our empirical findings remains an open question.
  ^QP15-C05-4b
- The 90%-of-cap U.S. universe averages the largest 17% of firms, an extremely liquid, tradeable set. _(construction, context, Opus only)_ #mech/research_method
  > this universe corresponds to the largest 17% of firms on average
  ^QP15-C05-8b

### C06 (page 6)
- US universe is 354 names in January 1972 growing to 676 in July 2011, significantly larger and more liquid than the Russell 1000. _(result, context)_ #mech/research_method
  > our sample of U.S. equities is significantly larger and more liquid than the Russell 1000
  reported_result: 354 largest firms (Jan 1972); 676 largest (Jul 2011)
  ^QP15-C06-1
- Non-US stocks: UK, continental Europe (ex-UK) and Japan use the same universe rule with Datastream prices/returns and Worldscope book values; universe is on average the largest 13%, 20% and 26% of firms respectively. _(construction, design_choice)_ #mech/research_method
  > For stocks outside of the United States, we use Datastream data from the United Kingdom, continental Europe
  exact_rule: Same 90%-of-market-cap filter in UK, Europe ex-UK, Japan · data_needed: Datastream (prices, returns), Worldscope (book values) · reported_result: Largest 13% (UK), 20% (Europe), 26% (Japan) of firms on average
  ^QP15-C06-2
- The liquid restricted universe (roughly the largest 20% of stocks) is deliberately conservative because value and momentum premia are larger in small, illiquid stocks in this sample; a previous paper version with a broader universe had significantly stronger returns. _(caveat, qualifier)_ #mech/risk_premium
  > Our results are conservative since value and momentum premia are larger among smaller, less liquid securities over the sample period we study.
  exhibit: footnote 5 · conditions: size effect not robust for momentum in other sample periods (Israel-Moskowitz 2012)
  ^QP15-C06-3
- Sample periods: US and UK stocks start Jan 1972, Europe and Japan stocks start Jan 1974, all series end July 2011 and are monthly. _(construction, context)_ #mech/research_method
  > The U.S. and U.K. stock samples begin in January 1972. The Europe and Japan stock samples begin in January 1974.
  reported_result: Average (minimum) number of stocks: US 724 (354), UK 147 (76), Europe 290 (96), Japan 471 (148)
  ^QP15-C06-4
- Country equity index universe: 18 developed markets (Australia, Austria, Belgium, Canada, Denmark, France, Germany, Hong Kong, Italy, Japan, Netherlands, Norway, Portugal, Spain, Sweden, Switzerland, UK, US); returns, prices and book values from MSCI and Bloomberg, January 1978 to July 2011. _(construction, design_choice)_ #mech/research_method
  > The universe of country equity index futures consists of the following 18 developed equity markets
  exact_rule: 18 developed equity index markets; min 8 indices, all 18 after 1980 · data_needed: MSCI, Bloomberg · reported_result: Sample Jan 1978-Jul 2011
  ^QP15-C06-5
- Five of the 18 country index series (Austria, Belgium, Denmark, Norway, Portugal) are built from equity index swap returns on MSCI local indices, not actual futures. _(construction, qualifier)_ #mech/research_method
  > Austria, Belgium, Denmark, Norway, and Portugal are not index futures but are constructed from the returns of an equity index swap instrument using the respective local market index from MSCI.
  data_needed: MSCI local indices · exhibit: footnote 6
  ^QP15-C06-6
- Country index returns, prices and book values come from MSCI and Bloomberg. _(construction, design_choice, Opus only)_ #mech/research_method
  > Returns and price data as well as book values are obtained from MSCI and Bloomberg.
  data_needed: MSCI, Bloomberg
  ^QP15-C06-8b
- Value and momentum are stronger in small stocks in this period (Hong-Lim-Stein, Grinblatt-Moskowitz, Fama-French 2012) but the size relation is not robust for momentum in other periods. _(citation, qualifier, Opus only)_ #mech/research_method
  > Israel and Moskowitz (2012) show this relation is not robust for momentum in other sample periods.
  exhibit: footnote 5 · conditions: size effect on momentum period-dependent
  ^QP15-C06-9b
- Prior work shows stronger value and momentum in less liquid emerging markets (Rouwenhorst 1998, Erb-Harvey 2006, Griffin-Ji-Martin 2003). _(citation, context, Opus only)_ #mech/research_method
  > Value and momentum returns have also been shown to be stronger in less liquid emerging markets
  exhibit: footnote 5
  ^QP15-C06-10b

### C07 (page 7)
- Index futures returns exclude collateral returns, so they are comparable to excess returns over the risk-free rate. _(construction, design_choice)_ #mech/research_method
  > The returns on the country equity index futures do not include any returns on collateral from transacting in futures contracts, hence these are comparable to returns in excess of the risk-free rate.
  ^QP15-C07-1
- Currency universe: 10 currencies (Australia, Canada, Germany spliced with the Euro, Japan, New Zealand, Norway, Sweden, Switzerland, UK, US), January 1979 to July 2011, min 7 currencies, all 10 after 1980; returns from forward contracts or MSCI spot plus Libor, USD-denominated, implicitly including the interest differential. _(construction, design_choice)_ #mech/research_method
  > We obtain spot exchange rates from Datastream covering the following 10 currencies
  exact_rule: 10 currencies; dollar-denominated returns from forwards (or spot + Libor) including interest differential · data_needed: Datastream spot rates, Libor, MSCI spot · reported_result: Jan 1979-Jul 2011
  ^QP15-C07-2
- Bond universe: 10 countries (Australia, Canada, Denmark, Germany, Japan, Norway, Sweden, Switzerland, UK, US), January 1982 to July 2011, min 5 countries, all 10 after 1990; index returns from Bloomberg and Morgan Markets, yields and short rates from Bloomberg, inflation forecasts from Consensus Economics. _(construction, design_choice)_ #mech/research_method
  > We obtain government bond data for the following 10 countries
  exact_rule: 10 country government bond index returns · data_needed: Bloomberg, Morgan Markets, Consensus Economics · reported_result: Jan 1982-Jul 2011
  ^QP15-C07-3
- Commodity universe: 27 futures (LME metals, ICE Brent and gas oil, CME livestock, CBOT grains, NYMEX energy, COMEX gold/silver, NYBOT softs, TOCOM platinum), January 1972 to July 2011, min 10 commodities, all 27 after 1995. _(construction, design_choice)_ #mech/research_method
  > We cover 27 different commodity futures obtained from several sources.
  exact_rule: 27 commodity futures · data_needed: LME, ICE, CME, CBOT, NYMEX, COMEX, NYBOT, TOCOM · reported_result: Jan 1972-Jul 2011
  ^QP15-C07-4
- Commodity returns: each day take the excess return of the most liquid contract (usually nearest or next-nearest to delivery), compound into a total return index, then take monthly returns; USD-denominated, excluding collateral return. _(construction, design_choice)_ #mech/research_method
  > Each day we com- pute the daily excess return of the most liquid futures contract,
  exact_rule: Daily excess return of most liquid contract -> compound daily to total return index -> monthly returns
  ^QP15-C07-5
- Currency universe: 10 currencies (AUD, CAD, DEM/EUR, JPY, NZD, NOK, SEK, CHF, GBP, USD) from Datastream spot rates, Jan 1979-Jul 2011, min 7. _(construction, design_choice, Opus only)_ #mech/research_method
  > The data cover the period January 1979 to July 2011, where the mini- mum number of currencies is 7 at any point in time and all 10 currencies are available after 1980.
  data_needed: Datastream spot FX
  ^QP15-C07-2b
- Currency returns are USD-denominated from forwards (or spot plus Libor differential), so they include carry. _(construction, design_choice, Opus only)_ #mech/research_method
  > We compute returns from currency forward contracts or MSCI spot price data and Libor rates, where currency returns are all dollar denominated and implicitly include the local interest rate differential.
  exact_rule: FX excess return = forward return or spot change + (foreign Libor - USD Libor) · data_needed: FX forwards, MSCI spot, Libor
  ^QP15-C07-3b
- Bond returns from Bloomberg and Morgan Markets; short rates and 10-year yields from Bloomberg. _(construction, design_choice, Opus only)_ #mech/research_method
  > Bond index returns come from Bloomberg and Morgan Markets, short rates and 10-year government bond yields are from Bloomberg
  data_needed: Bloomberg, Morgan Markets bond indices; 10y yields; short rates
  ^QP15-C07-4b
- Inflation forecasts come from Consensus Economics analyst surveys (used in the alternative real-yield bond value measure). _(construction, design_choice, Opus only)_ #mech/research_method
  > casts are obtained from investment bank analysts’ estimates as compiled by Consensus Economics.
  data_needed: Consensus Economics inflation forecasts
  ^QP15-C07-5b

### C08 (page 8)
- Design philosophy: use the simplest, most standard value and momentum measures uniformly across asset classes to minimise data snooping, so results may understate gross returns of better-chosen measures. _(construction, design_choice)_ #mech/research_method
  > We are not interested in coming up with the best predictors of returns in each asset class. Rather, our goal is to maintain a simple and fairly uniform approach
  conditions: results may understate true gross returns from more thoughtfully chosen measures
  ^QP15-C08-1
- Stock value signal is book-to-market (BE/ME); book values lagged 6 months, most recent market values used. _(construction, design_choice)_ #mech/risk_premium
  > we use the common value signal of the ratio of the book value of equity to market value of equity, or book-to-market ratio, BE/ME
  exact_rule: Value = BE/ME; book equity lagged 6 months; latest market value · data_needed: Compustat/Worldscope book equity, market cap
  ^QP15-C08-2
- Using contemporaneous prices in the value ratio makes the value/momentum correlation more negative and slightly lowers value's premium, but combination pricing results are nearly identical; Asness-Frazzini (2012) argue contemporaneous market values are better in the presence of momentum. _(robustness, qualifier)_ #mech/research_method
  > When using more recent prices in the value measure, the negative correlation between value and momentum is more negative and the value premium is slightly reduced
  ^QP15-C08-3
- Gerakos-Linnainmaa (2012): the market-value component of BE/ME drives most of its pricing information. _(citation, evidence)_ #mech/behavioral
  > Gerakos and Linnainmaa (2012) decompose value into book and market components and find that the market value of equity drives most of the relevant pricing information.
  ^QP15-C08-4
- Momentum signal: past 12-month cumulative raw return skipping the most recent month (MOM2-12), used for all asset classes. _(construction, design_choice)_ #mech/slow_reaction
  > we use the common measure of the past 12-month cumula- tive raw return on the asset
  exact_rule: MOM2-12 = cumulative raw return from t-12 to t-1 (skip most recent month), same for all eight markets · data_needed: asset total returns
  ^QP15-C08-5
- The most recent month is skipped to avoid 1-month reversal in stock returns (liquidity/microstructure effects). _(mechanism, design_choice)_ #mech/behavioral
  > We skip the most recent month, which is standard in the momentum literature, to avoid the 1-month reversal in stock returns, which may be related to liquidity or microstructure issues
  conditions: 1-month short-term reversal
  ^QP15-C08-6
- Footnote 8: Novy-Marx (2012) finds past 7-12 month return better than 2-6 in US stocks, yet MOM2-12 is used because the benefit is negligible (Novy-Marx), Goyal-Wahal find no difference in 35 of 36 countries, and MOM2-12 is the established signal; MOM7-12 should not alter conclusions. _(robustness, design_choice)_ #mech/slow_reaction
  > the past 7- to 12-month return is a better momentum predictor in U.S. stocks than the past 2- to 6-month return
  exhibit: footnote 8 · conditions: US is the exception among 36 countries
  ^QP15-C08-7
- Simple measures likely understate the returns available from better-designed value and momentum signals. _(caveat, qualifier, Opus only)_ #mech/research_method
  > our results may therefore understate the true gross returns to value and momentum available from more thoughtfully chosen measures.
  ^QP15-C08-3b
- The value+momentum combination's pricing results are insensitive to whether price is lagged in the value measure. _(robustness, evidence, Opus only)_ #mech/research_method
  > A combination of value and momentum—one of the themes in this paper—obtains nearly identical pricing results regardless of whether we lag price in the value measure.
  ^QP15-C08-7b
- Better stock value measures exist (Lakonishok-Shleifer-Vishny, Asness-Porter-Stevens, Piotroski) but BE/ME is kept for simplicity and consistency. _(caveat, qualifier, Opus only)_ #mech/research_method
  > While research has shown that other value measures are more powerful for predicting stock returns
  exhibit: footnote 7
  ^QP15-C08-12b

### C09 (page 9)
- For index futures, currencies and other liquid classes momentum is stronger if the last month is not skipped; skipping is kept for uniformity, so results are conservative. _(robustness, qualifier)_ #mech/slow_reaction
  > Momentum returns for these asset classes are in fact stronger when we don’t skip the most recent month, hence our results are conservative.
  ^QP15-C09-1
- Country index value signal: previous month BE/ME of the country's MSCI index. _(construction, design_choice)_ #mech/risk_premium
  > For country indices, we use the previous month’s BE/ME ratio for the MSCI index of the country.
  exact_rule: Value = prior month MSCI country index BE/ME · data_needed: MSCI index book-to-market
  ^QP15-C09-2
- Commodity value = log(average spot price from 4.5 to 5.5 years ago / latest spot price), i.e. minus the past 5-year spot return. _(construction, design_choice)_ #mech/overshoot
  > we define value as the log of the spot price 5 years ago (actually, the average spot price from 4.5 to 5.5 years ago), divided by the most recent spot price
  exact_rule: Value = ln(avg spot price over months t-66..t-54 / spot price now) · data_needed: commodity spot prices
  ^QP15-C09-3
- Currency value = minus the 5-year exchange rate return (log avg spot 4.5-5.5 years ago over spot today) minus the log difference in foreign vs US CPI change over the same period, i.e. the 5-year change in purchasing power parity. _(construction, design_choice)_ #mech/overshoot
  > for currencies, our value measure is the negative of the 5-year return on the exchange rate
  exact_rule: Value = ln(avg spot t-66..t-54 / spot now) - [ln change in foreign CPI - ln change in US CPI] over same 5 years (5-year change in PPP) · data_needed: spot FX, CPI (foreign and US)
  ^QP15-C09-4
- Bond value = 5-year change in the yield of 10-year government bonds (similar to minus the past 5-year return). _(construction, design_choice)_ #mech/overshoot
  > For bonds, we use the 5-year change in the yields of 10-year bonds as our value measure, which is similar to the negative of the past 5-year return.
  exact_rule: Value = yield(10y bond, now) - yield(10y bond, 5 years ago); long markets with largest yield rise · data_needed: 10-year government bond yields
  ^QP15-C09-5
- Long-term past returns as value proxy are motivated by DeBondt-Thaler (1985), Fama-French (1996: negative 5-yr return portfolios correlate highly with BE/ME), Gerakos-Linnainmaa (link of past returns and BE/ME), and models of Daniel et al, Barberis et al, Hong-Stein, Vayanos-Woolley. _(citation, mechanism_step)_ #mech/overshoot
  > These long-term past return measures of value are motivated by DeBondt and Thaler (1985), who use similar measures for individual stocks to identify “cheap” and “expensive” firms.
  ^QP15-C09-6
- The same MOM2-12 signal is used in every asset class. _(construction, design_choice, Opus only)_ #mech/research_method
  > Momentum is straightforward since we can use the same measure for all asset classes, namely, the return over the past 12 months skipping the most recent month.
  ^QP15-C09-1b
- Behavioral and flow theories (DHS, BSV, Hong-Stein, Vayanos-Woolley) predict a link between long-term returns and book-to-market. _(mechanism, premise, Opus only)_ #mech/overshoot
  > Theory also suggests a link between long-term returns and book-to-market value measures
  ^QP15-C09-9b
- Goyal-Wahal: across 36 countries, 7-12 vs 2-6 month returns differ significantly only in the U.S. _(citation, design_choice, Opus only)_ #mech/research_method
  > Goyal and Wahal (2012) examine the power of past 7- to 12-month versus past 2- to 6-month returns across 36 countries and find that there is no significant difference
  exhibit: footnote 8
  ^QP15-C09-10b
- MOM2-12 is kept because it is the established signal with out-of-sample success; MOM7-12 should not change conclusions. _(construction, design_choice, Opus only)_ #mech/research_method
  > is the established momentum signal that has worked well out of sample over time and across geography.
  exhibit: footnote 8
  ^QP15-C09-11b
- Authors assert alternative momentum windows (MOM7-12) would not change conclusions, without showing results. _(robustness, qualifier, Opus only)_ #mech/research_method
  > using other momentum signals, such as MOM7–12, should not alter any of our conclusions.
  exhibit: footnote 8
  ^QP15-C09-12b

### C10 (page 10)
- Negative-5-year-return value factor correlates 0.83 with BE/ME value in US stocks, similarly high in UK/Europe/Japan, and 0.86 for a global stock value factor, validating the 5-year-return value proxy. _(result, evidence)_ #mech/overshoot
  > among U.S. stocks the correlation between returns to a value factor formed from the negative of the past 5-year return and the returns formed from BE/ME sorts is 0.83
  reported_result: Correlation 0.83 (US), 0.86 (global stocks) between -5y-return value and BE/ME value (Internet Appendix) · exhibit: Internet Appendix
  ^QP15-C10-1
- Portfolio construction: rank securities within each asset class on value or momentum, split into three equal groups (low P1, middle P2, high P3); stocks value-weighted by beginning-of-month market cap, nonstock securities equal-weighted; 3 portfolios x 2 characteristics x 8 asset classes = 48 test assets. _(construction, design_choice)_ #mech/research_method
  > ranking securities within each asset class by value or momentum and sorting them into three equal groups
  exact_rule: Terciles on signal within each market; value weighting by beginning-of-month market cap for stocks; equal weight for non-stocks; monthly rebalance · reported_result: 48 test portfolios
  ^QP15-C10-2
- Footnote 10: weighting non-stock assets by ex ante volatility, or rebalancing to equal weights annually instead of monthly, gives similar results. _(robustness, qualifier)_ #mech/risk_management
  > Weighting the nonstock asset classes by their ex ante volatility gives similar results.
  exhibit: footnote 10
  ^QP15-C10-3
- Factor weights w_it = c_t (rank(S_it) - mean rank), dollar neutral, scaled to one dollar long and one dollar short; ranks mitigate outliers, raw-signal weights give similar, slightly better performance. _(construction, design_choice)_ #mech/research_method
  > we weight securities in proportion to their cross- sectional rank based on the signal minus the cross-sectional average rank of that signal.
  exact_rule: w_it^S = c_t*(rank(S_it) - sum_i rank(S_it)/N); sum of weights = 0; c_t scales to $1 long and $1 short; r_t^S = sum_i w_it^S r_it · data_needed: signal and returns within each asset class · exhibit: Equation (1)-(2)
  ^QP15-C10-4
- Stock tercile portfolios are value-weighted by beginning-of-month cap; non-stock portfolios are equal-weighted. _(construction, design_choice, Opus only)_ #mech/research_method
  > for individual stocks we value weight the returns in the portfolios by their beginning-of-month market capitalization, and for the nonstock asset classes we equal weight securities.
  ^QP15-C10-4b
- 3 terciles x 2 signals x 8 asset classes = 48 new test portfolios. _(construction, design_choice, Opus only)_ #mech/research_method
  > producing 3 × 2 × 8 = 48 test portfolios.
  ^QP15-C10-5b

### C11 (page 11)
- COMBO factor = 0.5 value factor + 0.5 momentum factor. _(construction, design_choice)_ #mech/risk_premium
  > We also construct a 50/50 equal combination (COMBO) factor of value and momentum
  exact_rule: r_COMBO = 0.5*r_VALUE + 0.5*r_MOM · exhibit: Equation (3)
  ^QP15-C11-1
- Rank-weighted factors outperform P3-P1 tercile spreads because weights scale with the signal and more securities get non-zero, less extreme weights (better diversified). _(mechanism, design_choice)_ #mech/research_method
  > the signal-weighted factor portfolios outperform simple portfolio sort spreads because security weights are a positive (linear) function of the signal
  ^QP15-C11-2
- Table I frames the main claim: value and momentum, alone and combined, work in every market, including new evidence for bonds (value and momentum) and value in currencies and commodities. _(result, conclusion)_ #mech/risk_premium
  > Our em- phasis, however, is on the power of applying value and momentum everywhere at once.
  exhibit: Table I
  ^QP15-C11-3
- Alphas in Table I come from time-series regressions on a market index: MSCI country index for stocks, MSCI World for index futures, equal-weighted basket of securities for currencies, bonds and commodities. _(construction, qualifier)_ #mech/research_method
  > The market index for the stock strategies is the MSCI equity index for each country
  exact_rule: Alpha = intercept of strategy returns regressed on asset-class market index · exhibit: Table I
  ^QP15-C11-4

### C12 (page 12)
- Table I global aggregates (Global stocks, Global other, Global all) average market series with equal-volatility weights to adjust for large volatility differences (e.g. bonds vs commodities); stats computed monthly and annualised. _(construction, design_choice)_ #mech/risk_management
  > where average return series are computed using equal volatility weights across the markets and asset classes to account for the large differences in volatility
  exact_rule: Aggregate across markets with weights inversely proportional to each market's volatility · exhibit: Table I notes
  ^QP15-C12-1
- Table I Panel C tests alternative bond value measures (real yield, term spread, composite). _(construction, context)_ #mech/risk_premium
  > Panel C also reports results for alternative measures of value for fixed income securities.
  exhibit: Table I Panel C
  ^QP15-C12-2
- US stocks 1972-2011: value earns 3.7% (P3-P1) and 3.9% (Factor) excess return with weak t-stats but significant alphas; momentum earns 5.4% (P3-P1) and 7.7% (Factor); value/momentum correlation is -0.53/-0.65 and the 50/50 combination Sharpe is 0.63/0.86, well above either alone. _(result, evidence)_ #mech/risk_premium
  > Panel A: Individual Stock Portfolios
  reported_result: US stocks 01/1972-07/2011. Value P1/P2/P3 mean 9.5%/10.6%/13.2% (t 3.31/4.33/5.19), Sharpe 0.53/0.69/0.83; P3-P1 3.7% (t 1.83) stdev 12.8% Sharpe 0.29 alpha 5.3% (2.66); Factor 3.9% (1.66) stdev 14.8% Sharpe 0.26 alpha 5.8% (2.49). Momentum P1/P2/P3 8.8%/9.7%/14.2% (t 2.96/4.14/4.82), Sharpe 0.47/0.66/0.77; P3-P1 5.4% (2.08) stdev 16.4% Sharpe 0.33 alpha 6.0% (2.30); Factor 7.7% (2.84) stdev 17.0% Sharpe 0.45 alpha 8.7% (3.22). 50/50 combo P3-P1 4.6% (3.98) stdev 7.2% Sharpe 0.63 alpha 5.7% (5.05); Factor 5.8% (5.40) stdev 6.8% Sharpe 0.86 alpha 7.2% (7.06). Corr(Val,Mom) -0.53 (P3-P1), -0.65 (Factor) · exhibit: Table I Panel A
  ^QP15-C12-3
- Table I returns are excess of the 1-month U.S. T-bill rate, with t-stats, stdev and Sharpe ratios, annualized from monthly series. _(construction, design_choice, Opus only)_ #mech/research_method
  > Reported are the average raw excess (of the 1-month U.S. T-bill rate) return
  exact_rule: excess return = return - 1m T-bill; annualize monthly stats · exhibit: Table I
  ^QP15-C12-1b
- Value-momentum correlations in Table I are computed on returns after removing the asset-class market (residuals). _(construction, design_choice, Opus only)_ #mech/research_method
  > the last row for each asset class reports the correlation between value and momentum zero cost residual returns from the benchmark in each market or asset class.
  exhibit: Table I
  ^QP15-C12-3b
- All statistics are annualized from monthly returns. _(construction, context, Opus only)_ #mech/research_method
  > Statistics are computed from monthly return series but are reported as annualized numbers.
  exhibit: Table I
  ^QP15-C12-4b

### C13 (page 13)
- UK stocks 1972-2011: value 4.5%/5.5%, momentum 6.0%/7.2% (P3-P1/Factor); combination Sharpe 0.77/1.07 with value-momentum correlation -0.43/-0.62. _(result, evidence)_ #mech/risk_premium
  > U.K. stocks
  reported_result: UK 01/1972-07/2011. Value P3-P1 4.5% (t 1.83) stdev 13.4% Sharpe 0.33 alpha 3.5% (1.47); Factor 5.5% (2.10) stdev 14.4% Sharpe 0.38 alpha 4.4% (1.74). Momentum P3-P1 6.0% (2.37) stdev 15.9% Sharpe 0.38 alpha 6.7% (2.66); Factor 7.2% (3.00) stdev 15.0% Sharpe 0.48 alpha 8.0% (3.36). 50/50 combo P3-P1 6.3% (4.23) stdev 8.1% Sharpe 0.77 alpha 6.0% (4.05); Factor 7.2% (5.85) stdev 6.7% Sharpe 1.07 alpha 7.2% (5.84). Corr(Val,Mom) -0.43, -0.62 · exhibit: Table I Panel A
  ^QP15-C13-1
- Europe stocks 1974-2011: value 4.8%/5.2%, momentum 8.1%/9.8% (strongest momentum of the stock markets); combination Sharpe 0.87/1.20, correlation -0.52/-0.55. _(result, evidence)_ #mech/risk_premium
  > Europe stocks
  reported_result: Europe 01/1974-07/2011. Value P3-P1 4.8% (t 2.32) stdev 11.5% Sharpe 0.42 alpha 3.5% (1.71); Factor 5.2% (2.95) stdev 9.7% Sharpe 0.54 alpha 4.0% (2.32). Momentum P3-P1 8.1% (3.37) stdev 14.7% Sharpe 0.55 alpha 9.1% (3.88); Factor 9.8% (4.59) stdev 13.1% Sharpe 0.75 alpha 10.7% (5.05). 50/50 combo P3-P1 5.9% (4.77) stdev 6.8% Sharpe 0.87 alpha 6.1% (4.88); Factor 6.9% (6.55) stdev 5.8% Sharpe 1.20 alpha 7.1% (6.77). Corr(Val,Mom) -0.52, -0.55 · exhibit: Table I Panel A
  ^QP15-C13-2
- Japan stocks 1974-2011: value is very strong (12.0%/10.2%, Sharpe 0.79/0.77) while momentum is weak and insignificant (1.7%/2.2%, t 0.57/0.81); combination Sharpe 0.78/0.88, correlation -0.60/-0.64. _(result, evidence)_ #mech/risk_premium
  > Japan stocks
  reported_result: Japan 01/1974-07/2011. Value P3-P1 12.0% (t 4.31) stdev 15.3% Sharpe 0.79 alpha 13.0% (4.71); Factor 10.2% (4.22) stdev 13.2% Sharpe 0.77 alpha 10.7% (4.47). Momentum P3-P1 1.7% (0.57) stdev 18.6% Sharpe 0.09 alpha 1.7% (0.54); Factor 2.2% (0.81) stdev 16.5% Sharpe 0.13 alpha 2.2% (0.84). 50/50 combo P3-P1 6.4% (4.28) stdev 8.1% Sharpe 0.78 alpha 6.8% (4.63); Factor 5.9% (4.80) stdev 6.7% Sharpe 0.88 alpha 6.1% (5.05). Corr(Val,Mom) -0.60, -0.64 · exhibit: Table I Panel A · conditions: momentum fails in Japan 1974-2011 while value excels
  ^QP15-C13-3

### C14 (page 14)
- Global stocks (inverse-vol weighted across four markets) 1972-2011: value 6.2%/5.8%, momentum 5.6%/7.1%, combination Sharpe 1.04/1.28 (Factor), correlation -0.52/-0.60. _(result, evidence)_ #mech/risk_premium
  > Global stocks
  reported_result: Global stocks 01/1972-07/2011. Value P3-P1 6.2% (t 3.60) stdev 10.9% Sharpe 0.57 alpha 6.6% (3.79); Factor 5.8% (3.18) stdev 11.4% Sharpe 0.51 alpha 6.1% (3.37). Momentum P3-P1 5.6% (2.94) stdev 12.0% Sharpe 0.47 alpha 6.4% (3.37); Factor 7.1% (3.73) stdev 12.0% Sharpe 0.59 alpha 8.1% (4.31). 50/50 combo P3-P1 6.3% (6.52) stdev 6.1% Sharpe 1.04 alpha 6.8% (7.09); Factor 6.8% (8.04) stdev 5.3% Sharpe 1.28 alpha 7.5% (8.98). Corr(Val,Mom) -0.52, -0.60 · exhibit: Table I Panel A
  ^QP15-C14-1
- Country equity indices 1978-2011: value 6.0%/5.7% and momentum 8.7%/7.4% (P3-P1/Factor), both significant; combination Sharpe 1.16/1.00; correlation -0.34/-0.37. _(result, evidence)_ #mech/risk_premium
  > Country indices
  reported_result: Country indices 01/1978-07/2011. Value P3-P1 6.0% (t 3.45) stdev 9.8% Sharpe 0.61 alpha 5.9% (3.45); Factor 5.7% (3.40) stdev 9.5% Sharpe 0.60 alpha 5.3% (3.24). Momentum P3-P1 8.7% (4.14) stdev 11.9% Sharpe 0.73 alpha 8.2% (4.00); Factor 7.4% (3.57) stdev 11.8% Sharpe 0.63 alpha 7.1% (3.47). 50/50 combo P3-P1 7.3% (6.62) stdev 6.3% Sharpe 1.16 alpha 7.1% (6.49); Factor 10.6% (5.72) stdev 10.6% Sharpe 1.00 alpha 10.0% (5.47). Corr(Val,Mom) -0.34, -0.37 · exhibit: Table I Panel B
  ^QP15-C14-2
- Currencies 1979-2011: value 3.3%/3.9% (t 1.89/2.47) and momentum 3.5%/3.0% (t 1.90/1.77) are modest, combination Sharpe 0.63/0.69; correlation -0.42/-0.43. _(result, evidence)_ #mech/risk_premium
  > Currencies
  reported_result: Currencies 01/1979-07/2011. Value P3-P1 3.3% (t 1.89) stdev 9.7% Sharpe 0.34 alpha 3.4% (2.04); Factor 3.9% (2.47) stdev 9.0% Sharpe 0.44 alpha 4.1% (2.63). Momentum P3-P1 3.5% (1.90) stdev 10.3% Sharpe 0.34 alpha 3.6% (1.99); Factor 3.0% (1.77) stdev 9.6% Sharpe 0.32 alpha 3.1% (1.84). 50/50 combo P3-P1 3.4% (3.51) stdev 5.4% Sharpe 0.63 alpha 3.5% (3.83); Factor 5.6% (3.89) stdev 8.0% Sharpe 0.69 alpha 5.7% (4.11). Corr(Val,Mom) -0.42, -0.43 · exhibit: Table I Panel B
  ^QP15-C14-3
- In non-stock asset classes portfolios are equal-weighted and the same tercile/rank-factor/combo construction is applied. _(construction, context, Opus only)_ #mech/research_method
  > Panel B: Other Asset Class Portfolios
  exhibit: Table I
  ^QP15-C14-4b

### C15 (page 15)
- Government bonds 1982-2011: value (5-year yield change) 1.1%/0.5% (t 0.97/0.39) and momentum 0.4%/1.0% are insignificant, Sharpe 0.18/0.07 and 0.06/0.17; combination remains weak (Sharpe 0.19/0.20); this is the weakest asset class. _(result, evidence)_ #mech/risk_premium
  > Fixed income
  reported_result: Fixed income 01/1982-07/2011. Value P3-P1 1.1% (t 0.97) stdev 6.3% Sharpe 0.18 alpha 1.9% (1.68); Factor 0.5% (0.39) stdev 6.4% Sharpe 0.07 alpha 1.4% (1.21). Momentum P3-P1 0.4% (0.35) stdev 6.0% Sharpe 0.06 alpha -0.3% (-0.29); Factor 1.0% (0.88) stdev 5.8% Sharpe 0.17 alpha 0.1% (0.08). 50/50 combo P3-P1 0.8% (1.03) stdev 4.0% Sharpe 0.19 alpha 0.8% (1.10); Factor 0.7% (1.08) stdev 3.5% Sharpe 0.20 alpha 0.7% (1.15). Corr(Val,Mom) -0.17, -0.35 · exhibit: Table I Panel B · conditions: weakest results are in bonds, statistically unreliable with the simple measures
  ^QP15-C15-1
- Commodities 1972-2011: value 6.3%/7.3% (t 1.61/1.92) and momentum 12.4%/11.5% (t 3.29/3.14), combination Sharpe 0.71/0.77 with high volatility; correlation -0.39/-0.46. _(result, evidence)_ #mech/risk_premium
  > Commodities
  reported_result: Commodities 01/1972-07/2011. Value P3-P1 6.3% (t 1.61) stdev 24.2% Sharpe 0.26 alpha 7.7% (2.02); Factor 7.3% (1.92) stdev 23.7% Sharpe 0.31 alpha 8.2% (2.19). Momentum P3-P1 12.4% (3.29) stdev 23.4% Sharpe 0.53 alpha 11.4% (3.06); Factor 11.5% (3.14) stdev 22.8% Sharpe 0.51 alpha 10.5% (2.89). 50/50 combo P3-P1 9.4% (4.42) stdev 13.1% Sharpe 0.71 alpha 9.5% (4.57); Factor 17.1% (4.78) stdev 22.2% Sharpe 0.77 alpha 17.1% (4.82). Corr(Val,Mom) -0.39, -0.46 · exhibit: Table I Panel B
  ^QP15-C15-2
- Global other asset classes (inverse-vol across index, currency, bond, commodity) 1972-2011: value 3.4%/3.6%, momentum 4.6%/4.4%, combination Sharpe 1.03/1.14; correlation -0.40/-0.49. _(result, evidence)_ #mech/risk_premium
  > Global other
  reported_result: Global other asset classes 01/1972-07/2011. Value P3-P1 3.4% (t 3.08) stdev 6.4% Sharpe 0.50 alpha 4.0% (3.67); Factor 3.6% (3.42) stdev 6.6% Sharpe 0.55 alpha 3.9% (3.71). Momentum P3-P1 4.6% (3.88) stdev 7.4% Sharpe 0.63 alpha 4.5% (3.80); Factor 4.4% (3.83) stdev 7.1% Sharpe 0.62 alpha 4.1% (3.62). 50/50 combo P3-P1 4.0% (6.39) stdev 3.9% Sharpe 1.03 alpha 4.2% (6.83); Factor 6.8% (7.03) stdev 6.0% Sharpe 1.14 alpha 6.8% (7.12). Corr(Val,Mom) -0.40, -0.49 · exhibit: Table I Panel B
  ^QP15-C15-3
- Global all asset classes 1972-2011: value 4.6%/4.6% (Sharpe 0.73/0.72), momentum 5.0%/5.4% (Sharpe 0.67/0.74), and the 50/50 combination reaches Sharpe 1.42 (P3-P1) and 1.59 (Factor), t-stat of alpha ~9-10; correlation -0.53/-0.60. _(result, evidence)_ #mech/risk_premium
  > Global all
  reported_result: Global all asset classes 01/1972-07/2011. Value P3-P1 4.6% (t 4.55) stdev 6.3% Sharpe 0.73 alpha 4.8% (4.81); Factor 4.6% (4.47) stdev 6.4% Sharpe 0.72 alpha 4.8% (4.69). Momentum P3-P1 5.0% (4.18) stdev 7.5% Sharpe 0.67 alpha 5.2% (4.34); Factor 5.4% (4.59) stdev 7.4% Sharpe 0.74 alpha 5.6% (4.76). 50/50 combo P3-P1 5.0% (8.77) stdev 3.5% Sharpe 1.42 alpha 5.0% (9.00); Factor 6.8% (9.83) stdev 4.3% Sharpe 1.59 alpha 6.9% (10.03). Corr(Val,Mom) -0.53, -0.60 · exhibit: Table I Panel B
  ^QP15-C15-4

### C16 (page 16)
- Alternative bond value measures (Table I Panel C) greatly improve bond results: real bond yield (10y yield minus 5-year inflation forecast) Sharpe 0.73 (P3-P1)/0.70 (Factor), alpha t 2.36/2.09; term spread (10y yield minus short rate) Sharpe 0.55/0.65, alpha t 2.78/3.31; composite of all three Sharpe 0.91/1.10, alpha t 4.40/5.48, versus 0.18/0.07 for the 5-year yield change. _(result, evidence)_ #mech/risk_premium
  > Panel C: Alternative Value Measures for Fixed Income
  reported_result: Fixed income 01/1983-07/2011 value measures (P3-P1 / Factor): 5-year yield change mean 1.1%/0.5% Sharpe 0.18/0.07 alpha 1.9% (1.68)/1.4% (1.21), corr with mom -0.17/-0.35; real yield mean 2.0%/1.9% (t 3.78/3.58) Sharpe 0.73/0.70 alpha 1.0% (2.36)/0.9% (2.09), corr -0.09/-0.03, 50/50 combo Sharpe 0.46/0.49; term spread mean 1.5%/1.7% (2.69/3.22) Sharpe 0.55/0.65 alpha 1.3% (2.78)/1.4% (3.31), corr 0.22/0.28, combo Sharpe 0.28/0.37; composite of all three mean 2.6%/2.9% (4.88/5.89) stdev 2.9%/2.6% Sharpe 0.91/1.10 alpha 2.3% (4.40)/2.6% (5.48), corr 0.03/0.04, combo Sharpe 0.59/0.81 (alpha t 2.55/3.66) · exhibit: Table I Panel C
  ^QP15-C16-1
- Panel C tests alternative bond value measures over Jan 1983-Jul 2011 (vs. Jan 1982 start given for the bond data). _(robustness, context, Opus only)_ #mech/research_method
  > Fixed income 01/1983 to 07/2011
  exhibit: Table I Panel C
  ^QP15-C16-1b
- Bond value as the real yield (10-year yield minus 5-year inflation forecast) works much better: P3-P1 2.0% (t=3.78, SR 0.73), factor 1.9% (t=3.58, SR 0.70); correlation with momentum near zero (-0.09/-0.03). _(robustness, evidence, Opus only)_ #mech/research_method
  > Value = real bond yield (10-year yield to 5-year inflation forecast)
  exact_rule: value = y10_t - expected inflation (5y, Consensus Economics) · data_needed: 10y yields, Consensus Economics inflation forecasts · reported_result: real-yield value factor SR 0.70 t3.58; corr with mom -0.03 · exhibit: Table I Panel C
  ^QP15-C16-2b
- A composite of the three bond value measures is strongest: P3-P1 2.6% (t=4.88, SR 0.91), factor 2.9% (t=5.89, SR 1.10, alpha 2.6% t=5.48); correlation with momentum ~0 (0.03/0.04); combo factor SR 0.81. _(robustness, evidence, Opus only)_ #mech/research_method
  > Value = composite average of all three measures
  exact_rule: value = composite average of the three measures (averaging/standardization not specified) · reported_result: composite value factor 2.9% SR1.10; combo factor SR0.81 · exhibit: Table I Panel C
  ^QP15-C16-4b

### C17 (page 17)
- In stock markets the value-momentum correlation averages about -0.60, so combining two positive-return strategies raises Sharpe ratios; in every market the combination beats either alone. _(result, evidence)_ #mech/risk_premium
  > the correlation between value and momentum returns is strongly negative, averaging about –0.60
  reported_result: Average value/momentum correlation about -0.60 across the four stock markets; combination outperforms value or momentum alone in every stock market · exhibit: Table I Panel A text
  ^QP15-C17-1
- Value premium is significant in every stock market (strongest in Japan); momentum premia are positive in every market, especially Europe, but statistically insignificant in Japan. _(result, evidence)_ #mech/risk_premium
  > there is a significant return premium for value in every stock market, with the strongest performance in Japan
  reported_result: Value significant in all four stock markets, strongest in Japan; momentum positive everywhere, strongest in Europe, insignificant in Japan · exhibit: Table I Panel A text
  ^QP15-C17-2
- Japan: rather than ask why momentum failed (Chui-Titman-Wei 2010 cultural explanation), one should ask why value did so well; correlation of -0.64 means a positive momentum weight still raises Sharpe above value alone, confirmed by static portfolio optimisation. _(result, mechanism_step)_ #mech/behavioral
  > it would be nearly equally appropriate to ask why value did so well
  reported_result: Japan value/momentum correlation -0.64; equal combination Sharpe higher than value alone · exhibit: Table I Panel A text · conditions: Japan 1974-2011
  ^QP15-C17-3
- Global value (and global momentum) Sharpe is barely above the average market Sharpe, indicating strong covariation among value strategies and among momentum strategies across markets; the combination is what diversifies. _(result, evidence)_ #mech/risk_premium
  > Value applied globally generates an annualized Sharpe ratio not much larger than the average of the Sharpe ratios across each market, indicating strong covariation among value strategies across markets.
  reported_result: Global stocks value Sharpe 0.57 (P3-P1) vs market Sharpes 0.29-0.79; momentum 0.47 vs 0.09-0.55 · exhibit: Table I Panel A text
  ^QP15-C17-4
- Footnote 11: global portfolios weight each market (all of its portfolios and factors) by the inverse of its passive benchmark's monthly volatility, rescaled to sum to one; cap-weighting or equal-weighting gives nearly identical results. _(construction, design_choice)_ #mech/risk_management
  > each market contributes an equal fraction to the total volatility of the portfolio, ignoring correlations
  exact_rule: w_market = (1/stdev of passive benchmark) / sum(1/stdev), same weight applied to all portfolios of that market; non-stock benchmark = equal-weighted average of securities · exhibit: footnote 11
  ^QP15-C17-5
- The combination's higher Sharpe ratio raises the bar for theories explaining value or momentum alone. _(mechanism, conclusion, Opus only)_ #mech/research_method
  > many theories attempting to explain the ob- served Sharpe ratio for value or momentum have a higher hurdle to meet if considering a simple linear combination of the two.
  ^QP15-C17-4b
- Even in Japan a positive momentum weight improves the efficient frontier (confirmed by static portfolio optimization). _(implementation, evidence, Opus only)_ #mech/risk_management
  > an equal combination of value and momentum in Japan realizes an even higher Sharpe ratio than value alone suggesting that a positive weight on momentum in Japan improves the efficient frontier
  exhibit: Table I Panel A · conditions: Japan
  ^QP15-C17-6b
- Cap-weighting or equal-weighting markets gives nearly identical results; equal-vol is used for consistency with non-equity classes where market cap has no meaning. _(robustness, design_choice, Opus only)_ #mech/research_method
  > Weighting by total market cap or equal weighting produces nearly identical results
  exhibit: footnote 11
  ^QP15-C17-8b

### C18 (page 18)
- In non-stock asset classes premia vary but the value/momentum combination is robust due to consistently negative correlation averaging -0.49; the diversified portfolio weights each class by inverse volatility (commodity strategies have about four times the vol of bond strategies). _(result, evidence)_ #mech/risk_premium
  > the combination of value and momentum is quite robust due to a consistent negative correlation between value and momentum within each asset class that averages –0.49
  exact_rule: Weight each asset class by inverse ex post sample volatility · reported_result: Average within-class value/momentum correlation -0.49 for non-stock assets; commodity vol about 4x bond vol · exhibit: Table I Panel B text
  ^QP15-C18-1
- Diversifying value or momentum across asset classes improves Sharpe only slightly, which means value strategies (and momentum strategies) are correlated across classes. _(result, evidence)_ #mech/risk_premium
  > The diversified portfolio across all asset classes yields small improvements in Sharpe ratios, which suggests the presence of correlation structure
  reported_result: Small Sharpe improvement from diversifying value (or momentum) across asset classes · exhibit: Table I text
  ^QP15-C18-2
- Production/investment-based theories (Berk-Green-Naik, Zhang, etc.) and individual-investor behavioural theories built around equities cannot easily explain similar and correlated value/momentum effects in other asset classes. _(mechanism, qualifier)_ #mech/risk_premium
  > may not easily apply to other asset classes, yet we find similar value and mo- mentum effects that are correlated to those found in equities,
  ^QP15-C18-3
- Combining global stock strategies and global other-asset-class strategies (weighted by inverse in-sample volatility of each average) gives a 50/50 value-momentum Sharpe of 1.45, about three times the US equity premium Sharpe, raising the hurdle for pricing models. _(result, conclusion)_ #mech/risk_premium
  > The 50/50 value and momentum combina- tion portfolio produces an annual Sharpe ratio of 1.45,
  exact_rule: Combine global stock strategy and global non-stock strategy, each weighted by inverse in-sample volatility of the average stock/non-stock strategy · reported_result: Annual Sharpe ratio 1.45 for 50/50 combination across all stocks and other asset classes, about three times the US equity premium Sharpe · exhibit: Section II.A text
  ^QP15-C18-4
- Footnote 12: non-stock asset class returns are weaker, but trading costs are higher for individual stocks than for futures, so net of costs the non-stock strategies would look relatively better; discussed in Section V. _(implementation, qualifier)_ #mech/research_method
  > net-of-trading-cost returns would elevate the relative importance of the nonstock strategies
  exhibit: footnote 12
  ^QP15-C18-5
- Footnote 13: using ex ante rolling volatility and covariance estimates instead of ex post for the global weights yields similar results. _(robustness, qualifier)_ #mech/risk_management
  > Using ex ante rolling measures of volatility and covariances yields similar results.
  exhibit: footnote 13
  ^QP15-C18-6
- Applying value and momentum jointly across asset classes sets an asset-pricing hurdle several times larger than U.S. equity data. _(mechanism, conclusion, Opus only)_ #mech/research_method
  > the Sharpe ratio hurdle that these pricing models need to explain is several times larger than those found in U.S. equity data alone.
  ^QP15-C18-6b

### C19 (page 19)
- Single uniform signal per style across eight markets minimises data mining; results are positive in every class but bonds are statistically insignificant. _(caveat, qualifier)_ #mech/research_method
  > We choose the most studied or simplest measure in each case and attempt to maintain uniformity across asset classes to minimize the potential for data mining.
  exhibit: Section II.B · conditions: weakest results in bonds
  ^QP15-C19-1
- The simple bond value signal gives Sharpe 0.18 and alpha 1.9% (t 1.68) but more thoughtful signals (real yield, term spread) raise Sharpe to 0.73 and 0.55 with alpha t-stats 2.36 and 2.78; a composite of all three reaches Sharpe 0.91 and 1.10 with alpha t 4.40 and 5.48. _(robustness, design_choice)_ #mech/risk_premium
  > Using our current measure of value, the 5-year change in yields of 10-year maturity bonds, we are only able to produce a Sharpe ratio of 0.18
  reported_result: Bond value Sharpe: 5y yield change 0.18 (alpha 1.9%, t 1.68); real yield 0.73 (t 2.36); term spread 0.55 (t 2.78); composite 0.91 and 1.10 (t 4.40, 5.48) · exhibit: Table I Panel C
  ^QP15-C19-2
- Simple uniform measures likely understate true returns; the authors keep them to be conservative and avoid data mining even though bond results are insignificant; 50/50 combinations also improve with the alternative bond value measures. _(caveat, qualifier)_ #mech/research_method
  > our use of single, simple, and uniform value and momentum mea- sures may understate the true returns to these strategies in each asset class.
  ^QP15-C19-3
- Table II examines cross-asset-class correlation of value and momentum returns; the strength of comovement can support or challenge theoretical explanations. _(mechanism, context)_ #mech/risk_premium
  > Table II reports the correlations of value and momentum returns across diverse asset classes to identify their common movements.
  exhibit: Table II
  ^QP15-C19-4
- Footnote 14: Israel-Moskowitz (2012) show other measures improve stability of value and momentum returns among individual equities. _(citation, evidence)_ #mech/research_method
  > Israel and Moskowitz (2012) show how other measures of value and momentum can improve the stability of returns to these styles among individual equities.
  exhibit: footnote 14
  ^QP15-C19-5
- Bonds are the weakest asset class: baseline value and momentum premia are not statistically reliable. _(result, qualifier, Opus only)_ #mech/research_method
  > our weakest results pertain to bonds, which do not produce statistically reliable premia.
  exhibit: Table I
  ^QP15-C19-1b
- Averaging several value measures diversifies measurement error and gives more reliable premia (Israel-Moskowitz 2012 for stocks). _(mechanism, design_choice, Opus only)_ #mech/research_method
  > we are able to produce even more reliable risk premia when using multiple measures of value simultaneously that diversify away measurement error and noise across the variables.
  ^QP15-C19-4b

### C20 (page 20)
- Table II correlations use quarterly returns to mitigate nonsynchronous trading; Panel A correlates average value/momentum return series (stocks vs nonstocks); diagonal entries are each market's correlation with the average of all other markets, averaged; F-tests give joint significance at 5%. _(construction, design_choice)_ #mech/research_method
  > Correlations are computed from quarterly returns to mitigate the influence of nonsynchronous trading across markets.
  exact_rule: Quarterly returns; group average series first (inverse-vol weighted), then correlate; diagonal = average correlation of each market with average of others · exhibit: Table II caption
  ^QP15-C20-1
- Table II Panel A: stock value correlates 0.68 with value in other stock markets (diagonal) and 0.15 with nonstock value; stock momentum 0.65 with other stock momentum and 0.37 with nonstock momentum; stock value vs stock momentum -0.53, stock value vs nonstock momentum -0.26, nonstock value vs stock momentum -0.16, nonstock value vs nonstock momentum -0.13. _(result, evidence)_ #mech/risk_premium
  > Panel A: Correlation of Average Return Series
  reported_result: Panel A: Stock value-Stock value 0.68*, Stock value-Nonstock value 0.15*, Stock value-Stock mom -0.53*, Stock value-Nonstock mom -0.26*; Nonstock value diag 0.07, Nonstock value-Stock mom -0.16*, Nonstock value-Nonstock mom -0.13*; Stock mom diag 0.65*, Stock mom-Nonstock mom 0.37*; Nonstock mom diag 0.21* (* = F-test significant at 5%) · exhibit: Table II Panel A
  ^QP15-C20-2
- Table II Panel B: global stock value correlates positively with country index value 0.27* and currency value 0.13*, ~0 with bond value -0.03 and commodity value 0.01, negatively with momentum in indices -0.28*, currencies -0.20*, commodities -0.17*, bonds -0.01; global stock momentum correlates 0.40* (index), 0.28* (currency), 0.09 (bond), 0.20* (commodity) with nonstock momentum and negatively with nonstock value (-0.19*, -0.12*, -0.05, -0.06). _(result, evidence)_ #mech/risk_premium
  > Panel B breaks down the correlations of the individual stock value and momentum strategies series with each of the nonstock value and momentum strategies.
  reported_result: Global stock value vs nonstock value: index 0.27*, currency 0.13*, bond -0.03, commodity 0.01; vs nonstock momentum: index -0.28*, currency -0.20*, bond -0.01, commodity -0.17*. Global stock momentum vs nonstock value: -0.19*, -0.12*, -0.05, -0.06; vs nonstock momentum: 0.40*, 0.28*, 0.09, 0.20* · exhibit: Table II Panel B
  ^QP15-C20-3
- Table II diagonals are the average correlation of each market's strategy with the average of the same strategy in all other markets (leave-one-out). _(construction, design_choice, Opus only)_ #mech/research_method
  > The diagonal elements in Panel A are computed as the average correlation between each market’s return series and the average of all other return series in other markets, excluding the market itself.
  exhibit: Table II
  ^QP15-C20-2b
- An F-test checks joint significance; * marks 5% significance. _(construction, context, Opus only)_ #mech/research_method
  > An F-test for the joint significance of the individual correlations within each group is performed
  exhibit: Table II
  ^QP15-C20-3b

### C21 (page 21)
- Table II correlations use the signal-weighted zero-cost factors (equation 2), with similar results from P3-P1 portfolios. _(robustness, qualifier)_ #mech/research_method
  > results are similar using the top third minus bottom third P3-P1 portfolio returns
  exhibit: Section II.C
  ^QP15-C21-1
- Correlating averages first gives stronger results than averaging individual pairwise correlations because averaging diversifies away market-specific noise; the individual pairwise correlations (Internet Appendix) are weaker but show the same comovement. _(mechanism, qualifier)_ #mech/research_method
  > we obtain more powerful statistical findings when looking at the correlations of the average return series rather than the average of individual correlations
  exhibit: footnote 15 · conditions: individual pairwise correlations consistently weaker
  ^QP15-C21-2
- Panel A pattern: value correlates positively with value elsewhere, momentum with momentum elsewhere, and value with momentum negatively everywhere across markets and asset classes. _(result, evidence)_ #mech/risk_premium
  > value in one market or asset class is positively correlated with value elsewhere, momentum in one market or asset class is positively correlated with momentum elsewhere
  reported_result: See Table II Panel A signs: +value/value, +mom/mom, -value/mom · exhibit: Table II Panel A
  ^QP15-C21-3

### C22 (page 22)
- The cross-asset correlation structure arises despite different investors, institutions and information environments, which points to common global factors rather than local behavioural stories. _(mechanism, mechanism_step)_ #mech/risk_premium
  > since these asset classes have different types of investors, institutional and market structures
  ^QP15-C22-1
- The comovement of long-short value and momentum strategies across asset classes is stronger than the correlation of passive asset-class exposures, so it cannot be explained by common market exposure. _(result, evidence)_ #mech/risk_premium
  > The value and momentum strategies we examine are long–short and market neutral with respect to each asset class, and yet exhibit stronger correlation across asset classes than do passive exposures to these asset classes.
  reported_result: Cross-class value/value 0.15 and mom/mom 0.37 (stock vs nonstock) vs weaker passive correlations (as stated in text) · exhibit: Section II.C
  ^QP15-C22-2
- In Panel B nearly all value strategies are positively correlated across asset classes, all momentum strategies positively correlated, all value/momentum correlations negative, and most are statistically significant. _(result, evidence)_ #mech/risk_premium
  > Nearly all of the value strategies across asset classes are consistently positively correlated, all of the momentum strategies are consistently positively correlated
  exhibit: Table II Panel B
  ^QP15-C22-3
- Robustness: the value/momentum correlation of -0.53 (BE/ME with latest price) is still -0.28 when ME is lagged 1 year to avoid overlap with the momentum window, and -0.48 when value is the negative 5-year past return; so the negative correlation is not an artefact of the value measure. _(robustness, evidence)_ #mech/risk_premium
  > still produces a negative correlation between value and momentum of –0.28
  reported_result: Value/momentum correlation: -0.53 (BE/ME, latest price), -0.28 (BE/ME with ME lagged 1 year), -0.48 (negative of 5-year past return) · exhibit: Internet Appendix; Table II Panel A
  ^QP15-C22-4
- Average stock value strategy correlates 0.68 with value in other stock markets and 0.15 with non-stock value. _(result, evidence, Opus only)_ #mech/research_method
  > 0.68 with the average value strategy in other stock markets, and of 0.15 with the average nonstock value strategy.
  reported_result: 0.68, 0.15 · exhibit: Table II Panel A
  ^QP15-C22-1b
- Average stock momentum correlates 0.65 with momentum in other stock markets and 0.37 with non-stock momentum. _(result, evidence, Opus only)_ #mech/research_method
  > strategy has a correlation of 0.65 with the average momentum strategy in other stock markets and a correlation of 0.37 with the average nonstock momentum strategy.
  reported_result: 0.65, 0.37 · exhibit: Table II Panel A
  ^QP15-C22-2b
- Value in one stock market correlates -0.53 with momentum in other stock markets; stock value vs non-stock momentum -0.26; non-stock value vs stock momentum -0.16; non-stock value vs non-stock momentum -0.13. _(result, evidence, Opus only)_ #mech/research_method
  > The correlation between a value strategy in one stock market and a portfolio of momentum strategies in other stock markets is –0.53.
  reported_result: -0.53, -0.26, -0.16, -0.13 · exhibit: Table II Panel A
  ^QP15-C22-4b

### C23 (page 23)
- First principal component loads one direction on all value strategies and the opposite on all momentum strategies (long momentum/short value in every asset class); explains 54% of the covariance matrix of individual-stock strategies and 23% across all asset classes, indicating a common global factor structure. _(result, evidence)_ #mech/risk_premium
  > The first principal component, which is essentially long momentum and short value (or vice versa) in every asset class, accounts for 54% of the individual stock strategies’ covariance matrix and 23% of the all- asset-class covariance matrix.
  reported_result: PC1 explains 53.6% (four stock markets) and 22.7% (all five groups: global stocks, indices, currencies, bonds, commodities). Approx eigenvector weights (read from chart): stock markets value about -0.37 (US), -0.37 (UK), -0.37 (Europe), -0.27 (Japan), momentum about +0.39, +0.39, +0.36, +0.28; all classes value about -0.45 (stocks), -0.28 (indices), -0.25 (currencies), ~0 (bonds), -0.22 (commodities), momentum about +0.48, +0.40, +0.30, +0.16, +0.28 · exhibit: Figure 1
  ^QP15-C23-1
- Cross-market correlations of the 50/50 combination are lower than for value or momentum alone (Internet Appendix), so value and momentum load oppositely on some common sources of risk. _(result, mechanism_step)_ #mech/risk_premium
  > correlations across markets and asset classes for the value/momentum combination strategies are lower than they are for value or momentum alone
  reported_result: Direction only; numbers not in main text · exhibit: Internet Appendix
  ^QP15-C23-2
- Figure 2 shows consistent positive cumulative returns to value, momentum and the combination in all eight markets and aggregates; all series scaled to 10% annual volatility; each panel reports Sharpe ratios and the value-momentum correlation. _(result, evidence)_ #mech/risk_premium
  > plotting the cumulative returns to value, momen- tum, and their combination in each asset market and across all asset markets.
  reported_result: Figure 2 factor Sharpe ratios (value/momentum/combo) and correlation: US 0.26/0.45/0.86 (-0.65); UK 0.38/0.48/1.07 (-0.62); Europe 0.54/0.75/1.20 (-0.55); Japan 0.77/0.13/0.88 (-0.64); global stocks 0.51/0.59/1.28 (-0.60); country indices 0.60/0.63/1.00 (-0.37); currencies 0.44/0.32/0.69 (-0.43); commodities 0.31/0.51/0.77 (-0.46); bonds 0.07/0.17/0.20 (-0.35); global other 0.55/0.62/1.14 (-0.49); global all 0.72/0.74/1.59 (-0.60) · exhibit: Figure 2
  ^QP15-C23-3
- Macro exposure test: regress value and momentum returns (US stocks, global stocks, nonstock, all assets) on macro variables (Table III). _(construction, context)_ #mech/risk_premium
  > Table III reports results from time-series regressions of value and momentum returns for U.S. stocks, global stocks, nonstock asset classes, and all asset classes combined on various measures of macroeconomic risks.
  exact_rule: Time-series regressions of strategy returns on macro variables · exhibit: Table III
  ^QP15-C23-4
- Footnote 16: Chordia-Shivakumar (2002) claim macro risks explain US momentum, but Griffin-Ji-Martin (2003) show neither unconditional nor conditional macro models explain momentum across 40 countries; this paper tests across asset classes. _(citation, evidence)_ #mech/risk_premium
  > Chordia and Shivakumar (2002) claim that a conditional forecasting model of macroeconomic risks can explain momentum profits in U.S. stocks
  exhibit: footnote 16
  ^QP15-C23-5
- The first principal component loads with one sign on every value strategy and the opposite sign on every momentum strategy. _(result, evidence, Opus only)_ #mech/risk_premium
  > the first principal component loads in one direction on all value strategies and loads in exactly the opposite direction on all momentum strategies
  exhibit: Figure 1
  ^QP15-C23-2b

### C24 (page 24)
- Figure 1: the first principal component of the four stock markets' value and momentum strategies loads about -0.27 to -0.37 on value and +0.28 to +0.39 on momentum and explains 53.6% of the covariance matrix; for the five asset-class groups it explains 22.7%, with value negative everywhere (bonds about zero) and momentum positive everywhere (read from chart). _(result, evidence)_ #mech/risk_premium
  > Percentage of covariance matrix explained = 53.6%
  reported_result: PC1 share 53.6% (stocks) and 22.7% (all asset classes); approx weights value/momentum: US -0.37/0.39, UK -0.37/0.39, Europe -0.37/0.36, Japan -0.27/0.28; stocks -0.45/0.48, indices -0.28/0.40, currencies -0.25/0.30, bonds ~0/0.16, commodities -0.22/0.28 · exhibit: Figure 1 · conditions: weights read from chart, approximate
  ^QP15-C24-1

### C25 (page 25)
- Figure 2 plots cumulative sum-of-log returns of rank-weighted value, momentum and 50/50 combo factors in each of eight markets and three global aggregates (equal-volatility weighted), all scaled to 10% annual vol; Sharpe ratios on the chart match Table I Factor columns for US, UK, Europe and Japan stocks. _(result, evidence)_ #mech/risk_premium
  > Figure 2. Cumulative returns to value and momentum strategies across markets and asset classes.
  reported_result: US stocks Sharpe 0.26/0.45/0.86; UK 0.38/0.48/1.07; Europe 0.54/0.75/1.20; Japan 0.77/0.13/0.88 (value/momentum/combo); correlations -0.65, -0.62, -0.55, -0.64. Combo cumulative line rises steadily; Japan momentum is flat and Japan value surges, with a visible value drawdown around 2000 · exhibit: Figure 2 · conditions: charts low resolution; Japan value/momentum swings around 2000 read from chart
  ^QP15-C25-1
- U.K. stocks: Sharpe 0.38/0.48/1.07, corr -0.62; Europe stocks: 0.54/0.75/1.20, corr -0.55; both show the 1999-2000 value drawdown offset by momentum, and a momentum fall around 2009. _(result, evidence, Opus only)_ #mech/research_method
  > U.K. Stocks
  reported_result: UK 0.38/0.48/1.07; Europe 0.54/0.75/1.20 · exhibit: Figure 2
  ^QP15-C25-3b
- Japan stocks: Sharpe value 0.77, momentum 0.13, combo 0.88, corr -0.64; momentum is roughly flat over 1972-2011 while value rises strongly, with a value drawdown around 1999-2000 coinciding with a momentum spike. _(result, evidence, Opus only)_ #mech/research_method
  > Japan Stocks
  reported_result: Japan 0.77/0.13/0.88; corr -0.64 · exhibit: Figure 2 · conditions: Japan momentum flat
  ^QP15-C25-4b

### C26 (page 26)
- Figure 2 continued (country indices, currencies, commodities, bonds): factor Sharpe ratios value/momentum/combo and value-momentum correlation: country indices 0.60/0.63/1.00 (-0.37), currencies 0.44/0.32/0.69 (-0.43), commodities 0.31/0.51/0.77 (-0.46), bonds 0.07/0.17/0.20 (-0.35); cumulative combo lines rise more steadily than value or momentum alone. _(result, evidence)_ #mech/risk_premium
  > Figure 2. Continued.
  reported_result: Sharpe (V/M/Combo) and corr: indices 0.60/0.63/1.00 (-0.37); currencies 0.44/0.32/0.69 (-0.43); commodities 0.31/0.51/0.77 (-0.46); bonds 0.07/0.17/0.20 (-0.35) · exhibit: Figure 2 (continued)
  ^QP15-C26-1
- Fixed income (Figure 2): Sharpe value 0.07, momentum 0.17, combo 0.20, corr -0.35; bond value has a deep cumulative loss from the mid-1980s to the early-mid 1990s and ends near zero, so bond results are fragile and period-dependent. _(result, qualifier, Opus only)_ #mech/research_method
  > Fixed Income
  reported_result: 0.07/0.17/0.20; corr -0.35 (path read from chart) · exhibit: Figure 2 · conditions: bond value lost through 1980s-early 1990s
  ^QP15-C26-3b

### C27 (page 27)
- Figure 2 continued (global aggregates): global stocks Sharpe 0.51/0.59/1.28 (corr -0.60), global other assets 0.55/0.62/1.14 (-0.49), global all assets 0.72/0.74/1.59 (-0.60); combination line rises almost monotonically to a cumulative log return of about 3 on the 10%-vol scale, while value and momentum lines end near 1.2-1.5 (read from chart). _(result, evidence)_ #mech/risk_premium
  > Global Other Assets
  reported_result: Sharpe (V/M/Combo): global stocks 0.51/0.59/1.28; global other 0.55/0.62/1.14; global all 0.72/0.74/1.59; value stalls around 1998-2000 and momentum around 2008-2009 (read from chart) · exhibit: Figure 2 (continued) · conditions: chart low resolution; cumulative levels approximate
  ^QP15-C27-1
- Global stocks (Figure 2): Sharpe value 0.51, momentum 0.59, combo 1.28, corr -0.60; value's 1999-2000 drawdown is visible even in the global aggregate. _(result, evidence, Opus only)_ #mech/research_method
  > Global Stocks
  reported_result: 0.51/0.59/1.28; corr -0.60 · exhibit: Figure 2
  ^QP15-C27-1b

### C28 (page 28)
- Macro variables: long-run consumption growth (sum of 12 quarters ahead log nondurable-and-services per capita consumption growth), recession dummy (NBER peak=0, trough=1, ex post), GDP growth, market excess return, and Fama-French TERM and DEF. _(construction, design_choice)_ #mech/risk_premium
  > long-run consumption growth is the future 3-year growth rate in consumption, measured as the sum of log quarterly consumption growth 12 quarters ahead
  exact_rule: Regress strategy returns on: 12-quarter-ahead consumption growth; NBER recession dummy; GDP growth; market excess return; TERM; DEF · data_needed: NIPA, NBER, ECRI (global), MSCI World, Fama-French TERM/DEF · exhibit: Table III
  ^QP15-C28-1
- US value is positively related to long-run consumption growth (coefficient 0.0004, t 2.06), momentum is not; value and momentum are slightly negatively related to recessions and GDP growth but insignificantly; TERM and DEF positively related to value, DEF negatively to momentum. _(result, evidence)_ #mech/risk_premium
  > U.S. stock value strategies are positively related to long- run consumption growth in U.S. data,
  reported_result: US stocks: value long-run consumption growth 0.0004 (t 2.06), momentum 0.0001 (0.33); recession dummy -0.0068 (-1.06) / -0.0056 (-0.73); GDP growth -0.0050 (-1.75) / 0.0019 (0.57); market -0.3435 (-7.46) / 0.0219 (0.40); TERM 0.2038 (2.64) / -0.0234 (-0.25); DEF 0.7439 (5.25) / -0.7733 (-4.57); R2 13.1% / 5.9% · exhibit: Table III
  ^QP15-C28-2
- Globally macro variables mostly do not explain value or momentum; exceptions: momentum is significantly negatively related to recessions (esp. nonstock), DEF is positive for global stock value and consistently negative for momentum in all asset classes. _(result, evidence)_ #mech/risk_premium
  > the global macroeconomic variables are generally not significantly related to value and momentum returns, with a couple of excep- tions.
  reported_result: Global stocks: recession 0.0037 (0.66)/-0.0044 (-0.75), DEF 0.2650 (2.86)/-0.3752 (-3.87), R2 2.3%/6.4%. Nonstock: recession 0.0045 (1.48)/-0.0081 (-2.44), GDP -0.0005/-0.0034 (-2.08), TERM -0.0885 (-3.30), DEF -0.0510 (-1.03)/-0.0787 (-1.44), R2 3.4%/2.9%. All assets: recession 0.0043 (1.55)/-0.0072 (-2.26), TERM -0.0551 (-2.23)/0.0316 (1.11), DEF 0.0240 (0.53)/-0.1490 (-2.84), R2 2.9%/4.7%. Long-run consumption growth 0.0001 (insignificant) everywhere · exhibit: Table III · conditions: momentum weaker in recessions; momentum loses when default spread widens
  ^QP15-C28-3
- Global macro regressors are GDP-weighted averages across US, UK, Europe, Japan using ECRI data and recession dates; market is MSCI World excess return; TERM and DEF are U.S. versions only. _(construction, design_choice, Opus only)_ #mech/cycle_persistence
  > we use global long-run consumption growth, which is a GDP-weighted average of 12-quarter-ahead nondurable and service per capita consumption growth in the United States, the United Kingdom, Europe, and Japan.
  data_needed: ECRI production/consumption/business cycle dates (~50 countries), MSCI World, U.S. TERM/DEF · exhibit: Table III
  ^QP15-C28-5b
- Momentum does worse in recessions, especially outside stocks (nonstock momentum recession coef -0.0081, t=-2.44; all-asset -0.0072, t=-2.26). _(result, evidence, Opus only)_ #mech/cycle_persistence
  > Momentum is significantly negatively related to recessions, especially among nonstock asset classes.
  reported_result: nonstock mom recession -0.0081 (-2.44); all mom -0.0072 (-2.26) · exhibit: Table III · conditions: recessions
  ^QP15-C28-7b
- DEF loads positively on global stock value (0.265, t=2.86) but insignificantly negatively on non-stock value. _(result, evidence, Opus only)_ #mech/research_method
  > The default spread is positively related to global stock value
  reported_result: global stock value DEF 0.2650 (2.86); nonstock value -0.0510 (-1.03) · exhibit: Table III
  ^QP15-C28-8b
- Griffin-Ji-Martin (2003) show macro risk models cannot explain momentum across 40 countries. _(citation, context, Opus only)_ #mech/cycle_persistence
  > in equities globally across 40 countries, including the United States.
  exhibit: footnote 16
  ^QP15-C28-9b

### C29 (page 29)
- Global macro regressors are GDP-weighted averages across countries; macro variables explain very little of value/momentum returns (R2 2-6% outside US stocks). _(result, evidence)_ #mech/risk_premium
  > For the global, nonstock, and all-asset-class return regressions, the macroeconomic variables are averaged across all countries, weighting each country in proportion to its GDP.
  reported_result: R2 between 2.3% and 6.4% for global, nonstock and all-asset regressions; 13.1% (value) and 5.9% (momentum) for US stocks · exhibit: Table III
  ^QP15-C29-1
- Table III does not report intercepts, so how much of the premia macro variables absorb is not shown. _(caveat, qualifier, Opus only)_ #mech/research_method
  > The intercepts from the regressions are not reported for brevity.
  exhibit: Table III
  ^QP15-C29-1b
- Recession dummy is defined from NBER (U.S.) or ECRI (other countries) peak/trough dates, coded 0 = peak and 1 = trough. _(construction, design_choice, Opus only)_ #mech/cycle_persistence
  > a recession dummy (0 = peak, 1 = trough)
  data_needed: NBER, ECRI business cycle dates · exhibit: Table III
  ^QP15-C29-2b
- Table III global columns: global stock momentum DEF -0.375 (t=-3.87); nonstock value TERM -0.0885 (t=-3.30); all-asset value TERM -0.0551 (t=-2.23), all-asset momentum DEF -0.149 (t=-2.84); market betas small and insignificant; R2 2.3-6.4%. _(result, evidence, Opus only)_ #mech/research_method
  > Global Stocks
  reported_result: see claim · exhibit: Table III
  ^QP15-C29-3b

### C30 (page 30)
- Liquidity shock definition: funding liquidity (TED spread, LIBOR minus term repo, swap minus T-bill in each of four markets) and market liquidity variables, each signed so higher = more liquidity, taking shocks as AR(2) residuals (Korajczyk-Sadka 2008; Moskowitz-Pedersen 2012). _(construction, design_choice)_ #mech/liquidity_flows
  > We follow Moskowitz and Pedersen (2012) to define our liquidity shocks.
  exact_rule: Funding: -(3m LIBOR - 3m govt rate) [TED], -(LIBOR - term repo), -(swap - T-bill); Market: -(on-the-run minus off-the-run 10y spread), Pastor-Stambaugh innovations, -(Acharya-Pedersen illiquidity); shock = AR(2) residual · data_needed: Local 3m interbank/LIBOR, 3m govt rates, repo, swaps, on/off-the-run 10y yields (US, UK, Japan, Germany for Europe), CRSP and stock data in other markets · reported_result: Funding series available Jan 1987-Jul 2011 · exhibit: Section III.B.1
  ^QP15-C30-1
- AR(2) shocks are not special; AR(3), AR(1) and first differences give similar results. _(robustness, qualifier)_ #mech/research_method
  > There is no special or theoretical reason to use an AR(2). An AR(3), AR(1), and first differences model yield similar results.
  exhibit: footnote 17
  ^QP15-C30-2
- Liquidity indices: first principal component of the correlation matrix (not covariance, because variables differ in units and volatility) of funding shocks, market shocks, and all shocks. _(construction, design_choice)_ #mech/liquidity_flows
  > In addition, we take the first principal component of the correlation matrix of all funding liquidity shocks, all market liquidity shocks, and all liquidity shocks and construct an index of shocks for funding, market, and all liquidity.
  exact_rule: PC1 of correlation matrix of liquidity shocks -> funding, market and all-liquidity indices
  ^QP15-C30-3
- Footnote 18: Sadka and Adrian-Shin measures were dropped because their data (tick data, prime broker balance sheets) are unavailable outside US equities; earlier results were similar. _(robustness, qualifier)_ #mech/liquidity_flows
  > A previous version of this paper also included the liquidity measures of Sadka (2006) and Adrian and Shin (2010) and found similar results.
  exhibit: footnote 18
  ^QP15-C30-4
- The Fama-French DEF factor return loads negatively on momentum in every asset group. _(result, evidence, Opus only)_ #mech/liquidity_flows
  > DEF is consistently negatively related to momentum returns in all asset classes.
  reported_result: DEF on momentum: US -0.77, global stocks -0.38, nonstock -0.08, all -0.15 · exhibit: Table III
  ^QP15-C30-1b
- All spreads are sign-flipped so that higher values mean more liquidity. _(construction, design_choice, Opus only)_ #mech/liquidity_flows
  > we take the negative of the TED spread and the other spreads so that they capture liquidity, since a wider spread represents worse liquidity.
  ^QP15-C30-4b
- Liquidity regressions cover Jan 1987-Jul 2011 only (shorter than the 1972 return sample). _(caveat, qualifier, Opus only)_ #mech/liquidity_flows
  > The funding series are available for the common period January 1987 to July 2011.
  ^QP15-C30-5b

### C31 (page 31)
- Table IV Panel A (US liquidity measures, with Table III macro controls): funding liquidity shocks load negatively on value and positively on momentum. TED spread: value -0.0052 (t -1.44), momentum 0.0129 (3.07), combo 0.0061 (2.13), value-minus-momentum -0.0180 (-2.62); funding PC: value -0.0111 (-2.89), momentum 0.0153 (3.31), combo 0.0042 (1.49), Val-Mom -0.0264 (-3.41); All PC: value -0.0154 (-2.84), momentum 0.0195 (2.96), combo 0.0043 (1.09), Val-Mom -0.0349 (-3.17). Market liquidity measures are weak. _(result, evidence)_ #mech/liquidity_flows
  > Panel A: U.S. Liquidity Risk Measures
  reported_result: Panel A US liquidity shocks, coefficient (t): TED spread V -0.0052 (-1.44), M 0.0129 (3.07), 50/50 0.0061 (2.13), V-M -0.0180 (-2.62); LIBOR-term repo V -0.0137 (-2.15), M 0.0087 (1.11), 50/50 -0.0058 (-1.26), V-M -0.0223 (-1.71); Swap-T-bill V -0.0002 (-0.05), M 0.0141 (3.34), 50/50 0.0104 (3.67), V-M -0.0143 (-2.04); Funding PC V -0.0111 (-2.89), M 0.0153 (3.31), 50/50 0.0042 (1.49), V-M -0.0264 (-3.41); On-the-run-off-the-run V 0.0063 (0.53), M -0.0053 (-0.38), 50/50 -0.0043 (-0.50), V-M 0.0115 (0.49); Pastor-Stambaugh V 0.0034 (0.32), M 0.0107 (0.89), 50/50 0.0159 (1.93), V-M -0.0074 (-0.37); Acharya-Pedersen V 0.0010 (2.02), M 0.0005 (1.44), 50/50 0.0013 (3.05), V-M 0.0004 (0.70); Market liquidity PC V -0.0080 (-0.44), M 0.0222 (0.94), 50/50 0.0200 (1.06), V-M -0.0302 (-0.97); All PC V -0.0154 (-2.84), M 0.0195 (2.96), 50/50 0.0043 (1.09), V-M -0.0349 (-3.17) · exhibit: Table IV Panel A · conditions: dependent variables are the all-asset value/momentum 'everywhere' factors; macro controls included
  ^QP15-C31-1
- Global liquidity measures average the four countries' measures with weights from each country's first-principal-component contribution; all regressions control for Table III macro variables. _(construction, design_choice, Opus only)_ #mech/liquidity_flows
  > the global liquidity risks are estimated by taking the average of all the liquidity measures across countries—the United States, the United Kingdom, Europe, and Japan—weighted by the principal component
  exhibit: Table IV
  ^QP15-C31-1b
- U.S. funding liquidity PC: value -0.0111 (t=-2.89), momentum +0.0153 (t=3.31), Val-Mom -0.0264 (t=-3.41); TED: value -0.0052 (-1.44), momentum 0.0129 (3.07); all-liquidity PC: value -0.0154 (-2.84), momentum 0.0195 (2.96). _(result, evidence, Opus only)_ #mech/liquidity_flows
  > Funding liquidity PC
  reported_result: value -0.0111(-2.89), mom 0.0153(3.31), V-M -0.0264(-3.41); All PC value -0.0154(-2.84), mom 0.0195(2.96) · exhibit: Table IV Panel A
  ^QP15-C31-2b
- U.S. market liquidity shocks (on/off-the-run, Pastor-Stambaugh, market PC) are insignificant for value and momentum; only Acharya-Pedersen is marginal (value 0.0010, t=2.02). _(result, evidence, Opus only)_ #mech/liquidity_flows
  > Market liquidity PC
  reported_result: market liquidity PC value -0.0080(-0.44), mom 0.0222(0.94) · exhibit: Table IV Panel A
  ^QP15-C31-3b
- With U.S. measures the 50/50 combo is not fully liquidity-neutral: it loads positively on TED (0.0061, t=2.13), swap-T-bill (0.0104, t=3.67) and Acharya-Pedersen (0.0013, t=3.05), though not on the funding PC (t=1.49) or all PC (t=1.09). _(result, qualifier, Opus only)_ #mech/liquidity_flows
  > Swap-T-bill
  reported_result: combo TED 0.0061(2.13), Swap-T-bill 0.0104(3.67), AP 0.0013(3.05); funding PC 0.0042(1.49); All PC 0.0043(1.09) · exhibit: Table IV Panel A
  ^QP15-C31-4b

### C32 (page 32)
- Figure 3's global liquidity shock index (Jan 1987 on) picks up about a dozen big liquidity events (1987 crash, Gulf War, decimalization, 9/11, LTCM, quant meltdown of August 2007, Bear Stearns, Lehman), validating the measure. _(result, evidence)_ #mech/liquidity_flows
  > capture a dozen of the largest known liquidity events in global markets over the last 25 years
  reported_result: Global liquidity shocks series residual from AR(2) of the global liquidity index, flagged events 1987 crash through Lehman · exhibit: Figure 3
  ^QP15-C32-1
- Table IV Panel B (global liquidity measures): global funding liquidity again loads negatively on value and positively on momentum with higher significance; funding PC value -0.0094 (t -4.74), momentum 0.0112 (3.58), Val-Mom -0.0206 (-4.67), combo 0.0013 (0.58); All PC value -0.0079 (-3.25), momentum 0.0093 (4.43), Val-Mom -0.0172 (-4.63), combo 0.0016 (0.82); market liquidity effects weak. _(result, evidence)_ #mech/liquidity_flows
  > Panel B: Global Liquidity Risk Measures
  reported_result: Panel B global: TED V -0.0067 (-1.69), M 0.0094 (2.00), V-M -0.0161 (-2.05), 50/50 0.0023 (0.74); LIBOR-repo V -0.0177 (-2.87), M 0.0139 (1.66), V-M -0.0316 (-2.36), 50/50 -0.0005 (-0.08); Swap-T-bill V -0.0076 (-2.15), M 0.0055 (1.31), V-M -0.0131 (-1.86), 50/50 -0.0012 (-0.46); Funding PC V -0.0094 (-4.74), M 0.0112 (3.58), V-M -0.0206 (-4.67), 50/50 0.0013 (0.58); On/off-the-run V 0.0108 (0.68), M -0.0001 (-0.01), V-M 0.0109 (0.34), 50/50 0.0037 (0.32); Pastor-Stambaugh V 0.0010 (1.06), M -0.0002 (-0.15), V-M 0.0011 (0.61), 50/50 0.0003 (0.43); Acharya-Pedersen V 0.0009 (0.39), M 0.0008 (0.28), V-M 0.0001 (0.02), 50/50 0.0020 (1.30); Market PC V -0.0009 (-0.74), M 0.0016 (1.21), V-M -0.0025 (-1.45), 50/50 0.0012 (1.00); All PC V -0.0079 (-3.25), M 0.0093 (4.43), V-M -0.0172 (-4.63), 50/50 0.0016 (0.82) · exhibit: Table IV Panel B
  ^QP15-C32-2
- Global LIBOR-term repo: value -0.0177 (t=-2.87), momentum 0.0139 (t=1.66); global swap-T-bill value -0.0076 (t=-2.15); global TED value -0.0067 (-1.69), momentum 0.0094 (2.00). _(result, evidence, Opus only)_ #mech/liquidity_flows
  > LIBOR-term repo
  exhibit: Table IV Panel B
  ^QP15-C32-2b
- Each liquidity shock enters a separate regression (with macro controls); dependent variables are global value and momentum everywhere factors, the 50/50 combo and value minus momentum. _(construction, design_choice, Opus only)_ #mech/liquidity_flows
  > We examine each liquidity shock in iso- lation in separate regressions.
  exhibit: Table IV
  ^QP15-C32-4b
- Adding liquidity shocks barely changes macro coefficients. _(result, context, Opus only)_ #mech/research_method
  > the coefficient estimates on the macro variables do not change much with the addition of the liquidity variables.
  exhibit: Table IV
  ^QP15-C32-5b
- Some liquidity measures need tick data or prime-broker balance sheets unavailable outside the U.S., limiting the global liquidity proxies. _(caveat, qualifier, Opus only)_ #mech/liquidity_flows
  > data and balance sheet information from prime brokers, we cannot compute them internationally and hence omit them.
  exhibit: footnote 18
  ^QP15-C32-6b

### C33 (page 33)
- Value does poorly when funding liquidity improves (borrowing easier) while momentum does well; the opposite exposure partly explains the negative value-momentum correlation. Market liquidity shocks (US) show little relation; Acharya-Pedersen marginally negative for value, positive for momentum. _(result, mechanism_step)_ #mech/liquidity_flows
  > The first four rows of Panel A of Table IV show that funding liquidity risk is consistently negatively related to value returns and significantly positively related to mo-
  reported_result: Funding liquidity: negative for value, positive for momentum in all four US funding measures (Table IV Panel A) · exhibit: Table IV Panel A · conditions: market liquidity shocks weakly related
  ^QP15-C33-1
- Footnote 19: funding shocks might proxy for risk aversion or risk premia, but then both value and momentum should fall with wider spreads whereas they move in opposite directions; market and macro controls also absorb risk-premium changes. _(mechanism, qualifier)_ #mech/liquidity_flows
  > Another interpretation of these funding shocks is that they proxy for changes in risk aversion or risk premia.
  exhibit: footnote 19
  ^QP15-C33-2
- Figure 3 plots the global liquidity shock index (AR(2) residual of PC-weighted average of all market and funding liquidity variables across US, UK, Europe, Japan) with labelled episodes: 1987 crash, Gulf War, Euro, decimalization, LTCM, Sept. 11, Bear Stearns, FAS 157, quant meltdown, Lehman. Caption says Jan 1987 to June 2010 while the text says Jan 1987 to July 2011. _(result, evidence)_ #mech/liquidity_flows
  > Time-Series of Global Liquidity Shocks
  reported_result: Series range about -0.30 to +0.15; largest negative shocks at the 1987 crash and Lehman (read from chart) · exhibit: Figure 3 · conditions: inconsistency between caption end date (June 2010) and text (July 2011)
  ^QP15-C33-3
- Figure 3 caption gives Jan 1987-Jun 2010, while the text says the index is plotted Jan 1987-Jul 2011 (internal inconsistency). _(caveat, qualifier, Opus only)_ #mech/research_method
  > plotted from January 1987 to June 2010
  exhibit: Figure 3
  ^QP15-C33-2b
- Market liquidity shocks show little relation to value and momentum returns. _(result, evidence, Opus only)_ #mech/liquidity_flows
  > we find little relation between market liquidity shocks and value and momen- tum returns.
  exhibit: Table IV
  ^QP15-C33-4b

### C34 (page 34)
- Momentum has the same sign as in Pastor-Stambaugh for market liquidity but is insignificant here; the authors use PS's factor, not the mimicking portfolio, which PS themselves show has a weak relation to momentum. _(result, evidence)_ #mech/liquidity_flows
  > for our global momentum returns across asset classes over our sample period, but do not detect a significant relation.
  reported_result: Market liquidity insignificant for global momentum · exhibit: Table IV · conditions: uses Pastor-Stambaugh innovations factor rather than factor-mimicking portfolio
  ^QP15-C34-1
- Opposite-signed liquidity loadings can explain the negative correlation but not why both earn positive premia: momentum's premium may compensate liquidity risk, while value loads negatively, which deepens the value puzzle. _(mechanism, qualifier)_ #mech/risk_premium
  > the opposite signed loadings on a single factor, such as liquidity risk, cannot explain why both value and momentum earn positive risk pre- mia.
  conditions: unless liquidity betas or the liquidity risk premium vary substantially over time
  ^QP15-C34-2
- Proposed (untested) story: momentum is crowded and popular, value contrarian; in liquidation episodes crowded high-momentum positions suffer more price pressure (Pedersen 2009). Further investigation is left for future research. _(mechanism, mechanism_step)_ #mech/crowding_positioning
  > momentum captures the most popular trades, being long the assets whose prices have recently appre- ciated as fickle investors flocked to these assets.
  conditions: liquidity shocks, forced liquidations
  ^QP15-C34-3
- Because of opposite-signed funding liquidity exposure the 50/50 value-momentum combination is essentially immune to funding shocks yet earns large returns, so liquidity risk cannot explain the combination premium. _(result, conclusion)_ #mech/liquidity_flows
  > the 50/50 equal combination of value and momentum is essentially immune to funding shocks, and yet, as we have shown, generates huge positive returns
  reported_result: 50/50 combination coefficients on funding liquidity PC: 0.0042 (t 1.49) US, 0.0013 (0.58) global · exhibit: Table IV
  ^QP15-C34-4
- Forced liquidations from cash needs, redemptions and risk management hit crowded momentum trades harder than value trades; further investigation is left for future work. _(mechanism, mechanism_step, Opus only)_ #mech/crowding_positioning
  > These liquidations may affect crowded high momentum securities more than the less popular contrarian/value securities.
  conditions: liquidity shocks
  ^QP15-C34-6b

### C35 (page 35)
- Individual market liquidity betas are weak (average t -0.95 for value and 1.81 for momentum), but regressing the average value and average momentum series across all markets on global liquidity shocks gives t -3.25 and 4.43; averaging removes market-specific noise and reveals the common factor exposure. _(result, evidence)_ #mech/liquidity_flows
  > The average t-statistic of the liquidity betas for value is –0.95 and for momentum is 1.81—hardly con- vincing.
  reported_result: Average of individual t-stats: value -0.95, momentum 1.81; t of average return series on global liquidity shocks: value -3.25, momentum 4.43. Approx individual t-stats read from chart (value / momentum): US stocks -0.8/2.3, UK -2.1/2.5, Europe -1.2/3.5, Japan +1.4/-0.7, country index +0.8/1.8, currencies -1.8/2.7, fixed income -0.6/1.0, commodities -3.1/1.4 · exhibit: Figure 4 · conditions: Japan is the exception with the opposite sign for both
  ^QP15-C35-1
- Liquidity risk can only partially explain the cross-section of returns because it cannot explain the combo's profitability. _(mechanism, conclusion, Opus only)_ #mech/liquidity_flows
  > so profitable, and hence can only partially explain part of the cross-sectional variation in returns.
  ^QP15-C35-2b

### C36 (page 36)
- Averaging across all markets mitigates idiosyncratic regional or asset-specific noise, so common liquidity exposure only appears in the cross-market average, not in individual strategies. _(mechanism, qualifier)_ #mech/research_method
  > The scope and uniformity of studying value and momentum everywhere at once is what allows these patterns to be identified.
  ^QP15-C36-1
- Equation (4): each of the 48 test portfolios is regressed on MSCI World excess return plus equal-volatility-weighted average value and momentum factors from all OTHER markets (excluding the own market), so no securities overlap between left and right sides. _(construction, design_choice)_ #mech/risk_premium
  > regressed on the excess returns of the market portfolio MKT (proxied by the MSCI World Index) and the returns to value and momentum factors in all other markets and asset classes.
  exact_rule: R_it^p - r_f = alpha + beta*MKT + v*sum_{j!=i} w_j VAL_jt + m*sum_{j!=i} w_j MOM_jt + eps; MKT = MSCI World; w_j equal-volatility weights · data_needed: 48 value/momentum tercile portfolios; value and momentum factors by market · exhibit: Equation (4); Figure 5
  ^QP15-C36-2
- Equation (4) is estimated separately for each of the 8 markets on its 6 tercile portfolios (48 test assets). _(construction, design_choice, Opus only)_ #mech/research_method
  > We estimate equation (4) for each market and asset class separately.
  exhibit: Equation (4)
  ^QP15-C36-4b

### C37 (page 37)
- Value and momentum in one market are well explained by value and momentum in other markets: cross-sectional R2 0.55 and average absolute alpha 22.6 bp per month, with no overlap in securities, supporting a common global factor structure. _(result, evidence)_ #mech/risk_premium
  > The cross-sectional R 2 is 0.55 and the average absolute value of the pricing errors (alpha) is 22.6 basis points per month.
  reported_result: Cross-sectional R2 0.55, average |alpha| 22.6 bp/month (0.00226); no formal GRS test possible · exhibit: Figure 5
  ^QP15-C37-1
- This 'other markets' test has no security overlap between test assets and factors, avoiding the usual mechanical link in single-market asset pricing tests. _(mechanism, qualifier)_ #mech/research_method
  > The dependent variable contains securities from a completely separate market or asset class from those used
  ^QP15-C37-2
- No joint test of pricing errors is possible for equation (4) because regressors differ by market. _(caveat, qualifier, Opus only)_ #mech/research_method
  > A formal statistical test of the joint significance of the pricing errors is not possible since the independent variables change across test assets
  exhibit: Figure 5
  ^QP15-C37-2b
- Because test assets and factors share no securities, the fit evidences genuine common global factor structure. _(mechanism, evidence, Opus only)_ #mech/research_method
  > there is no overlap of securities between the test assets used as the dependent variable and the factors used as regressors.
  ^QP15-C37-3b
- Figure 5 scatter: most test assets lie near the 45-degree line; the largest misses include low-return commodity value and bond momentum portfolios below the line. _(result, evidence, Opus only)_ #mech/research_method
  > AMP 3-Factor Model (only using factors from other markets)
  reported_result: read from chart (approx.) · exhibit: Figure 5
  ^QP15-C37-4b

### C38 (page 38)
- Equation (5): for each of the 48 portfolios regress excess return on MSCI World excess return plus global VAL-everywhere and MOM-everywhere factors (equal-volatility-weighted across asset classes), similar in spirit to Fama-French (1993) and Carhart (1997). _(construction, design_choice)_ #mech/risk_premium
  > we construct a three-factor model similar to equation (4), but where the regressors are the same for every asset
  exact_rule: R_it^p - r_f = alpha + beta*MKT + v*VAL_everywhere + m*MOM_everywhere + eps; factors = equal-volatility-weighted average across asset classes of rank-weighted factors · data_needed: 48 test portfolios, MSCI World, global value and momentum factors · exhibit: Equation (5)
  ^QP15-C38-1
- Global three-factor model: cross-sectional R2 0.71 and average absolute alpha 18 bp for the 48 test assets, slightly better than the other-markets regression (0.55, 22.6 bp) partly because securities overlap. _(result, evidence)_ #mech/risk_premium
  > The cross-sectional R 2 is 0.71 and the average absolute value of the alpha is 18 basis points
  reported_result: AMP 3-factor: average |alpha| 0.00182, GRS F-stat 2.657, p 0, cross-sectional R2 0.707 · exhibit: Figure 6 Panel A
  ^QP15-C38-2
- Alternative models fit worse on the 48 assets: global CAPM, Fama-French four-factor (US RMRF, SMB, HML, UMD) and six-factor (adding DEF, TERM) generate about twice the pricing errors and lower R2 than the global three-factor model. _(result, evidence)_ #mech/risk_premium
  > the global CAPM does not do a very good job fitting the cross section of value and momentum returns across markets and asset classes, producing the largest absolute pricing errors and smallest R 2 .
  reported_result: Panel A (48 assets): CAPM |alpha| 0.00389, GRS 6.586, R2 0.449; FF 4-factor 0.00352, GRS 6.702, R2 0.554; FF 6-factor 0.00349, GRS 7.113, R2 0.601; AMP 3-factor 0.00182, GRS 2.657, R2 0.707 · exhibit: Figure 6 Panel A
  ^QP15-C38-3
- Cross-market explanatory power shows the common variation is economically meaningful, capturing much of the cross-section of average returns. _(result, conclusion, Opus only)_ #mech/research_method
  > the evidence in Figure 5 makes a compelling case for common global factor struc- ture in value and momentum returns
  exhibit: Figure 5
  ^QP15-C38-1b
- The three-factor fit is mechanically helped by overlap between test assets and factors, unlike equation (4). _(caveat, qualifier, Opus only)_ #mech/research_method
  > equation (5) contains some of the same securities on the left- and right-hand side of the regression.
  exhibit: Equation (5)
  ^QP15-C38-4b

### C39 (page 39)
- Figure 6 Panel A (48 assets): scatter of actual vs predicted average returns; AMP 3-factor |alpha| 0.00182, GRS 2.657, R2 0.707; CAPM 0.00389, 6.586, 0.449; FF4 0.00352, 6.702, 0.554; FF6 0.00349, 7.113, 0.601; GRS p-value 0 for all (read from image). _(result, evidence)_ #mech/risk_premium
  > Fama-French 6-Factor Model
  reported_result: Average |alpha| / GRS F / cross-sectional R2: AMP3 0.00182/2.657/0.707; CAPM 0.00389/6.586/0.449; FF4 0.00352/6.702/0.554; FF6 0.00349/7.113/0.601; p-values 0 · exhibit: Figure 6 Panel A
  ^QP15-C39-1
- Even the best (AMP) model is rejected by the GRS test (p = 0) on the 48 portfolios; remaining misfits include low-return momentum and value portfolios in bonds, currencies and commodities (read from chart). _(caveat, qualifier, Opus only)_ #mech/research_method
  > GRS F-stat = 2.657
  reported_result: GRS 2.657, p-value 0 · exhibit: Figure 6 Panel A
  ^QP15-C39-2b

### C40 (page 40)
- Figure 6 Panel B (50 US size-value/momentum portfolios): AMP 3-factor |alpha| 0.00181, GRS 3.296, R2 0.642; CAPM 0.00319, 4.245, R2 -0.316; FF4 0.00113, 3.28, 0.772; FF6 0.00113, 3.345, 0.766; GRS rejects all (read from image). _(result, evidence)_ #mech/risk_premium
  > Fama-French 6-Factor Model
  reported_result: Average |alpha| / GRS F / cross-sectional R2: AMP3 0.00181/3.296/0.642; CAPM 0.00319/4.245/-0.316; FF4 0.00113/3.28/0.772; FF6 0.00113/3.345/0.766 · exhibit: Figure 6 Panel B
  ^QP15-C40-1
- In Figure 6 each model must also price the equity premium; the AMP model's value/momentum factors are inverse in-sample-volatility weighted across the eight asset classes. _(construction, design_choice, Opus only)_ #mech/research_method
  > where each model is forced to also price the equity premium.
  exact_rule: VAL/MOM everywhere = sum_k (1/sigma_k in-sample) factor_k, normalized · exhibit: Figure 6
  ^QP15-C40-2b

### C41 (page 41)
- Fama-French factors produce twice the pricing error of the global three-factor model on the 48 assets with much lower R2. _(result, evidence)_ #mech/risk_premium
  > generate twice the absolute magnitude of pricing errors as the three-factor global model and have much lower R 2 s.
  reported_result: See Figure 6 Panel A · exhibit: Figure 6
  ^QP15-C41-1
- On the Fama-French 25 size-value and 25 size-momentum US portfolios the global three-factor model has R2 0.64 and average absolute alpha 18 bp; FF factors do slightly better, and excluding the two smallest size quintiles the global model does as well as FF (it has no size factor). _(result, evidence)_ #mech/risk_premium
  > Our three- factor model derived from other markets and asset classes does a reasonable job explaining the returns to these 50 U.S. equity portfolios.
  reported_result: Panel B (50 US portfolios): AMP 3-factor |alpha| 0.00181, GRS 3.296, R2 0.642; CAPM 0.00319, GRS 4.245, R2 -0.316; FF 4-factor 0.00113, GRS 3.28, R2 0.772; FF 6-factor 0.00113, GRS 3.345, R2 0.766 · exhibit: Figure 6 Panel B · conditions: worse in small-cap quintiles because no size factor
  ^QP15-C41-2
- Global multi-asset value and momentum portfolios explain US value/momentum nearly as well as US factors, but US factors do not explain global ones, suggesting the global factors are closer to the efficient frontier and a more robust set of pricing factors. _(result, conclusion)_ #mech/risk_premium
  > global value and momentum portfolios across markets and asset classes are closer to the efficient frontier than U.S. stock-only value and momentum portfolios
  ^QP15-C41-3
- Table V: monthly Fama-MacBeth regressions of the 48 portfolios' returns on univariate betas (rolling 60-month windows) to funding liquidity risk, GDP growth, long-run consumption growth, TERM, DEF, market (Dimson-corrected with 2 lags), value-everywhere and momentum-everywhere. _(construction, design_choice)_ #mech/risk_premium
  > Regressions are run in the style of Fama and MacBeth (1973), where the cross section of monthly returns are regressed on the betas (estimated univariately using rolling windows of the past 60 months of returns) each month
  exact_rule: Each month: cross-sectional regression of 48 portfolio returns on univariate betas from the prior 60 months; report time-series mean and t-stat of coefficients; market beta = sum of contemporaneous plus 2 lagged coefficients (Dimson) · data_needed: 48 portfolios; liquidity PC, GDP growth, LRCG, TERM, DEF, MSCI World, VAL/MOM everywhere · exhibit: Table V
  ^QP15-C41-4
- Global factors built mostly from other markets explain the 50 Fama-French U.S. size-value and size-momentum portfolios with R2 0.64 and 18 bp mean absolute alpha. _(result, evidence, Opus only)_ #mech/research_method
  > The cross-sectional R 2 is 0.64 and the average absolute pricing error is only 18 basis points.
  reported_result: R2 0.64; |alpha| 18bp/month · exhibit: Figure 6 Panel B
  ^QP15-C41-2b

### C42 (page 42)
- Table V Fama-MacBeth results: liquidity beta premium 0.0024 (t 3.05); TERM 0.0021 (2.19) and DEF 0.0023 (2.18) priced alone, GDP and LRCG not; with liquidity beta added liquidity 0.0023 (2.29) and TERM/DEF lose significance; adding market, value and momentum factors, liquidity falls to 0.0016 (1.38) while value 0.0031 (3.96) and momentum 0.003 (3.53) are priced; funding-only liquidity 0.0022 (2.06) priced, market-only liquidity 0.0001 (0.07) not. _(result, evidence)_ #mech/liquidity_flows
  > Table V
  reported_result: Rows (coef, t): liquidity 0.0024 (3.05); GDP 0.0003 (0.43), LRCG 0.0005 (0.42), TERM 0.0021 (2.19), DEF 0.0023 (2.18); liquidity 0.0023 (2.29), GDP -0.0001 (-0.13), LRCG 0.0012 (1.01), TERM 0.0014 (1.59), DEF 0.0001 (0.11); liquidity 0.0005 (0.56), TERM 0.0015 (1.75), DEF 0.0020 (2.22), Mkt 0.0029 (2.58); full model liquidity 0.0016 (1.38), GDP 0.0018 (2.87), LRCG -0.0001 (-0.03), TERM 0.0033 (2.87), DEF 0.0014 (1.12), Mkt -0.0006 (-0.38), Value 0.0031 (3.96), Momentum 0.003 (3.53); funding only: liquidity 0.0022 (2.06), TERM 0.0011 (1.05), DEF 0.0015 (1.30), then full model liquidity 0.0012 (1.80), GDP 0.0019 (3.28), Value 0.0034 (4.40), Momentum 0.0031 (3.50); market liquidity only: 0.0001 (0.07), then full model -0.0013 (-0.88), GDP 0.0019 (3.19), TERM 0.0045 (5.05), Value 0.0038 (5.94), Momentum 0.0040 (5.82) · exhibit: Table V
  ^QP15-C42-1
- Market beta uses the Dimson correction (contemporaneous plus 1- and 2-month lagged market) to handle nonsynchronous trading. _(construction, design_choice, Opus only)_ #mech/research_method
  > For the market, a Dimson correction is used to account for possible nonsynchronous trading effects
  exhibit: Table V
  ^QP15-C42-1b

### C43 (page 43)
- The cross-sectional liquidity risk premium among the 48 assets is 24 bp per month (about 3% per year); the time series of Fama-MacBeth coefficients is a factor-mimicking portfolio (FP liq risk) with unit exposure, used later in time-series tests. _(result, evidence)_ #mech/liquidity_flows
  > which is 24 basis points per month or about 3% per year
  exact_rule: Factor-mimicking portfolio = monthly Fama-MacBeth coefficient series for each beta · reported_result: Liquidity risk premium 24 bp/month (~3%/year), t 3.05; TERM 21 bp and DEF 23 bp per month · exhibit: Table V
  ^QP15-C43-1
- TERM and DEF are priced alone but subsumed by liquidity beta; value and momentum betas subsume part of liquidity's explanatory power; only funding liquidity (not market liquidity) is priced in the cross section. _(result, evidence)_ #mech/liquidity_flows
  > only funding liquidity risk appears to be priced in the cross section of our global assets
  reported_result: Funding-only liquidity premium 0.0022 (t 2.06); market-only 0.0001 (0.07) · exhibit: Table V · conditions: value/momentum common factors capture part of funding liquidity exposure
  ^QP15-C43-2
- Table VI time-series pricing tests regress the 48 portfolios (plus 25+25 US portfolios and 13 hedge fund indices) on factor-mimicking portfolios from Table V and on global/US factor sets, reporting GRS, average |alpha|, cross-sectional R2, average time-series R2 and Eig% (Moskowitz 2003). _(construction, design_choice)_ #mech/research_method
  > we regress each of the 48 portfolios’ time series of monthly returns on the factor mimicking portfolio returns for liquidity risk, GDP growth, and long-run consumption growth, as well as TERM, DEF, and the value and momentum everywhere factors.
  exact_rule: Time-series regressions of each test asset on factor sets; GRS F-test of joint alphas; Eig% = sum of eigenvalues of model-implied covariance divided by sample covariance · data_needed: Fama-French 25 size-BE/ME and 25 size-momentum portfolios; DJCS and HFRI hedge fund indices · exhibit: Table VI
  ^QP15-C43-3
- TERM and DEF betas carry 21 and 23 bp/month premia, but are subsumed when liquidity betas are added; GDP and LRCG betas are not priced. _(result, evidence, Opus only)_ #mech/risk_premium
  > TERM and DEF do, exhibiting a risk premium of 21 and 23 basis points, respectively.
  reported_result: TERM 0.0021 (2.19), DEF 0.0023 (2.18) · exhibit: Table V
  ^QP15-C43-3b
- VAL and MOM everywhere betas capture average returns and subsume much of liquidity risk's explanatory power. _(result, evidence, Opus only)_ #mech/risk_premium
  > betas with respect to value and momentum factors capture average returns to value and momentum portfolios and that they subsume a significant portion of the explanatory power of other factors such as liquidity risk.
  exhibit: Table V
  ^QP15-C43-4b
- Using factor-mimicking portfolios makes the macro/liquidity factors traded returns so GRS time-series tests are valid. _(construction, design_choice, Opus only)_ #mech/research_method
  > Because we use factor mimicking portfolios as regressors, both the dependent and independent variables are measured in returns, and hence we can conduct formal pricing tests.
  exhibit: Table VI
  ^QP15-C43-6b

### C44 (page 44)
- Table VI Panel A (48 assets): global CAPM GRS 6.02, |alpha| 35 bp, time-series R2 0.40, cross-sectional R2 0.52, covariance captured 57%; adding liquidity factor GRS 5.02, |alpha| 31 bp, R2 0.48, 0.54, 64%; adding liquidity, GDP, LRCG, TERM, DEF GRS 4.09, 27 bp, 0.59, 0.56, 80%; AMP three-factor GRS 2.66, 18 bp, 0.68, 0.72, 74%; market+value only 3.72, 28 bp; market+momentum only 3.80, 22 bp; US models worse (US CAPM 6.59, 39 bp; FF3 7.18, 36 bp; FF4 6.70, 35 bp; FF6 7.11, 35 bp). _(result, evidence)_ #mech/risk_premium
  > Table VI
  reported_result: Panel A: Mkt (global CAPM) GRS 6.02, p 0.000, |alpha| 0.0035, avg TS R2 0.40, CS R2 0.52, 57% of covariances; Mkt+FPliq 5.02, 0.0031, 0.48, 0.54, 64%; Mkt+FPliq,GDPg,LRCG,TERM,DEF 4.09, 0.0027, 0.59, 0.56, 80%; Mkt+VAL+MOM everywhere 2.66, 0.0018, 0.68, 0.72, 74%; Mkt+VAL 3.72, 0.0028, 0.42, 0.43, 68%; Mkt+MOM 3.80, 0.0022, 0.42, 0.57, 70%; US CAPM 6.59, 0.0039, 0.30, 0.44, 47%; FF3 7.18, 0.0036, 0.31, 0.50, 53%; FF4 6.70, 0.0035, 0.33, 0.55, 63%; FF6 7.11, 0.0035, 0.39, 0.62, 64% · exhibit: Table VI Panel A · conditions: text says 84% of covariation captured by three-factor model while table shows 74%
  ^QP15-C44-1
- Table VI caption says factor-mimicking portfolios come from cross-sectional coefficients in Table IV, but the text and Table V show they come from the Fama-MacBeth regressions in Table V (labelling inconsistency). _(caveat, qualifier, Opus only)_ #mech/research_method
  > (each estimated from the cross-sectional regression coefficients in Table IV)
  exhibit: Table VI
  ^QP15-C44-3b

### C45 (page 45)
- Table VI Panels B and C: on the 50 US size-value/momentum portfolios the three-factor model has |alpha| 19 bp, CS R2 0.68, 66% of covariances (vs FF3 23 bp, 0.30, 93%; FF4/FF6 11 bp, 0.77, 97%); on 13 hedge fund indices it has the smallest alphas (18 bp vs 21-26 bp for FF models) and highest cross-sectional R2 (0.47 vs 0.36 max for FF); all models rejected by GRS. _(result, evidence)_ #mech/risk_premium
  > Panel C: 13 Hedge Fund Indexes
  reported_result: Panel B (50 US portfolios) in order global CAPM, +liq, +liq/macro, AMP 3F, US CAPM, FF3, FF4, FF6: |alpha| 0.0030/0.0030/0.0035/0.0019/0.0032/0.0023/0.0011/0.0011; GRS 4.09/4.12/4.76/3.22/4.25/3.81/3.28/3.35; CS R2 0.20/0.20/0.38/0.68/0.17/0.30/0.77/0.77; TS R2 0.41/0.42/0.57/0.70/0.73/0.87/0.91/0.91; covariances 48%/49%/61%/66%/82%/93%/97%/97%. Panel C (13 hedge fund indices): |alpha| 0.0032/0.0025/0.0022/0.0018/0.0028/0.0026/0.0022/0.0021; GRS 12.14/12.36/11.86/7.26/12.14/12.64/13.03/12.25; CS R2 0.20/0.30/0.17/0.47/0.18/0.19/0.36/0.36; TS R2 0.30/0.34/0.46/0.41/0.30/0.35/0.37/0.44; covariances 43%/47%/53%/54%/43%/47%/49%/51% · exhibit: Table VI Panels B and C · conditions: row order inferred from the text of the page; page image not tabulated clearly for these panels
  ^QP15-C45-1

### C46 (page 46)
- Global CAPM alone gives average |alpha| 35 bp per month and explains 57% of covariation; adding the liquidity factor lowers |alpha| to 31 bp; macro factors lower errors further; the three-factor model fits best (|alpha| 18 bp, cross-sectional R2 72%). _(result, evidence)_ #mech/risk_premium
  > the market portfolio alone (global CAPM) generates substantial pricing errors
  reported_result: Global CAPM |alpha| 35 bp, 57% covariation; with liquidity 31 bp; three-factor 18 bp, CS R2 72%, '84%' of covariation (text) vs 74% in table · exhibit: Table VI Panel A
  ^QP15-C46-1
- Liquidity risk captures only a small fraction of return premia and covariation; the authors treat this as a starting point for theory, acknowledge measurement error in liquidity risk, and note a single liquidity factor cannot explain both value and momentum without time-varying betas. _(caveat, conclusion)_ #mech/liquidity_flows
  > only a small fraction of the return premia and covariation is captured by our
  ^QP15-C46-2
- Models with only value or only momentum increase pricing errors and reduce fit, underscoring that one factor cannot explain both. _(result, evidence)_ #mech/risk_premium
  > The next two rows further show that having both value and momentum in the model is important
  reported_result: Market+VAL only GRS 3.72, |alpha| 28 bp, CS R2 0.43; Market+MOM only GRS 3.80, 22 bp, 0.57; both 2.66, 18 bp, 0.72 · exhibit: Table VI Panel A
  ^QP15-C46-3
- US factor models (US CAPM, FF3, FF4, FF6) leave larger pricing errors and lower R2 on the global 48 value/momentum portfolios. _(result, evidence)_ #mech/risk_premium
  > As Table VI shows, the U.S. factors do not do a great job of describing the global value and momentum portfolio returns
  reported_result: US models |alpha| 35-39 bp vs 18 bp for global three-factor; CS R2 0.44-0.62 vs 0.72 · exhibit: Table VI Panel A
  ^QP15-C46-4
- Eig% = sum of eigenvalues of model-implied covariance / sum of eigenvalues of sample covariance (share of covariance captured). _(construction, design_choice, Opus only)_ #mech/research_method
  > the Eig% metric from Moskowitz (2003), which is the sum of eigenvalues from the covariance matrix of the test assets implied by the model divided by the sum of eigenvalues of the sample covariance matrix.
  exact_rule: Eig% = tr(B Sigma_f B') / tr(Sigma_sample) · exhibit: Table VI
  ^QP15-C46-1b
- Adding the liquidity factor-mimicking portfolio cuts mean absolute alpha to 31 bp and raises fit, but GRS still rejects. _(result, evidence, Opus only)_ #mech/liquidity_flows
  > the average absolute alpha declines to 31 basis points, the cross-sectional R 2 increases, and the amount of covaria- tion captured increases.
  reported_result: |alpha| 31bp; Eig 64% · exhibit: Table VI Panel A
  ^QP15-C46-3b
- Measurement error in liquidity proxies may understate liquidity's explanatory power. _(caveat, qualifier, Opus only)_ #mech/liquidity_flows
  > We also recognize that measurement error in liquidity risk may limit what we can explain.
  ^QP15-C46-5b
- One liquidity factor cannot price both negatively correlated positive-premium strategies unless betas/premia vary strongly over time. _(mechanism, qualifier, Opus only)_ #mech/liquidity_flows
  > a single liquidity risk factor alone cannot explain value and momentum since they are negatively correlated with each other but both produce positive returns, unless there is substantial time variation in liquidity risk betas
  ^QP15-C46-6b
- Dropping either VAL or MOM from the model worsens fit considerably, showing both factors are needed. _(result, evidence, Opus only)_ #mech/research_method
  > having only value or momentum by itself increases pricing errors and decreases the fit considerably.
  reported_result: Mkt+VAL |a| 0.0028 CS R2 0.43; Mkt+MOM 0.0022, 0.57 · exhibit: Table VI Panel A
  ^QP15-C46-8b

### C47 (page 47)
- Global value and momentum factors (mostly non-US equities and other asset classes) explain the 50 US size-value/momentum portfolios with |alpha| 19 bp, CS R2 68% and 66% of covariation, better than FF3 and slightly worse than FF4/FF6. _(result, evidence)_ #mech/risk_premium
  > the global value and momentum everywhere factors, which consist primarily of non-U.S. equities and other asset classes, also do a good job explaining the
  reported_result: |alpha| 19 bp, CS R2 68%, 66% of covariation (Table VI Panel B) · exhibit: Table VI Panel B
  ^QP15-C47-1
- Value and momentum everywhere capture a sizeable fraction of the returns to 13 hedge fund indices (DJCS and HFRI), better than Fama-French US factors, consistent with Boyson-Stahel-Stulz (2010), Sadka (2012), Bali-Brown-Caglayan (2011, 2012); suggests hedge funds run similar or correlated strategies. _(result, evidence)_ #mech/crowding_positioning
  > the global three-factor model has smaller pricing errors than the Fama–French model and its extensions with the momentum, TERM, and DEF factors
  reported_result: Hedge funds |alpha| 18 bp (global 3-factor) vs 21-26 bp (FF models); CS R2 0.47 vs 0.18-0.36 · exhibit: Table VI Panel C
  ^QP15-C47-2
- The three-factor model is rejected by the GRS test for every set of test assets, so it is incomplete. _(caveat, qualifier)_ #mech/research_method
  > the GRS test still rejects our model in all cases, suggesting that more work needs to be done to fully describe the cross section of returns
  exhibit: Table VI
  ^QP15-C47-3
- Hedge fund returns load on global value and momentum, implying these factors are a natural benchmark for hedge fund performance. _(implementation, conclusion, Opus only)_ #mech/risk_premium
  > simple value and momentum factors applied globally across asset classes do appear to capture a sizeable fraction of the returns to hedge funds.
  exhibit: Table VI Panel C
  ^QP15-C47-4b

### C48 (page 48)
- All reported results are gross of transaction costs, which overstate real profits; momentum has higher turnover and its capacity has been questioned (Korajczyk-Sadka 2004, Lesmond-Schill-Zhou 2003). _(caveat, qualifier)_ #mech/research_method
  > Like most academic studies, we focus on gross returns, which are most suit-
  exhibit: Section V.A · conditions: gross returns only; no cost model in this paper
  ^QP15-C48-1
- Frazzini-Israel-Moskowitz (2012) use live trading data and find real trading costs of value, momentum and the combination are orders of magnitude lower for a large institution than calibrated models imply, so the strategies can be scaled considerably and still earn strong net returns. _(citation, evidence)_ #mech/liquidity_flows
  > Using live trading data, Frazzini, Israel, and Moskowitz (2012) challenge these results
  conditions: large institution; live trading data
  ^QP15-C48-2
- Costs are lower for futures-based markets, so although equity strategies beat non-equity ones gross, net-of-cost returns are likely much closer; the liquid universe (about the largest 17% of firms) also minimises price impact and capacity constraints. _(implementation, evidence)_ #mech/liquidity_flows
  > half of the markets that we examine are implemented with futures contracts, which typically have much lower trading costs than stocks
  reported_result: No net-of-cost numbers reported
  ^QP15-C48-3
- Strategies are naively rebalanced monthly; varying rebalance frequency, optimising for expected trading costs (Garleanu-Pedersen 2012) and extending or contracting the trade horizon can improve net returns, at some cost in gross returns (style drift). _(implementation, design_choice)_ #mech/liquidity_flows
  > the strategies we study here are all naively rebalanced exactly monthly no matter what the expected gain per amount traded
  exact_rule: Monthly rebalance regardless of expected gain per trade · conditions: cost-aware rebalancing could improve net performance
  ^QP15-C48-4
- Some studies find equity momentum's net returns and capacity much lower than paper returns. _(citation, qualifier, Opus only)_ #mech/risk_management
  > Korajczyk and Sadka (2004) and Lesmond, Schill, and Zhou (2003) argue that the real world returns and capacity of equity momentum strategies are considerably lower than the theoretical results would imply.
  ^QP15-C48-2b
- Shorting is costless-symmetric in futures but costly in stocks, a potential implementation concern. _(caveat, qualifier, Opus only)_ #mech/risk_management
  > While going long versus short is symmetric for futures, shorting involves special costs in stock markets.
  ^QP15-C48-6b

### C49 (page 49)
- Israel-Moskowitz (2012): returns come roughly equally from long and short sides, and long-only value and momentum portfolios still produce abnormal returns, so the strategies work even if shorting is restricted; Frazzini et al. (2012) find stock shorting costs for large institutions not materially different from long-side trading costs. _(citation, evidence)_ #mech/liquidity_flows
  > Israel and Moskowitz (2012) provide evidence that the return contributions of both value and momentum strategies across the same asset classes we study here are roughly equal from the long and short sides of the portfolio
  ^QP15-C49-1
- Decile sorts (80 decile portfolios across four equity markets, Internet Appendix) give very similar results and the three-factor model prices them well; value weighting vs other weighting schemes yields similar results. _(robustness, qualifier)_ #mech/research_method
  > we also explore more extreme sorts of securities into deciles and find that doing so does not materially affect the results
  reported_result: Similar results for 80 decile portfolios; numbers not in main text · exhibit: Internet Appendix
  ^QP15-C49-2
- Cross-asset aggregation scales each asset class by inverse full-sample realised volatility (look-ahead); real-world portfolios need ex ante volatility estimates. _(caveat, qualifier)_ #mech/risk_management
  > we scale each asset class by the inverse of its realized volatility over the full sample
  exact_rule: Weight each asset class by 1/(full-sample realised vol) · conditions: uses full-sample information, not ex ante
  ^QP15-C49-3
- Frazzini-Israel-Moskowitz find institutional shorting costs similar to buying/selling and not prohibitive. _(citation, evidence, Opus only)_ #mech/risk_management
  > the trading costs of shorting stocks are not materially different from the costs of buying or selling stocks
  ^QP15-C49-2b
- The paper is framed as an out-of-sample test of U.S. stock anomalies in other asset classes, hence deliberately simple choices. _(construction, premise, Opus only)_ #mech/research_method
  > one of the paper’s objectives is to provide a robust out-of-sample test of ideas that have been largely tested in individual, particularly U.S., stocks and extend them to other asset classes.
  ^QP15-C49-3b
- Alternative weighting schemes give similar results; trading costs unlikely to change much given the liquid universe. _(robustness, qualifier, Opus only)_ #mech/research_method
  > other weighting schemes yield similar results
  ^QP15-C49-5b

### C50 (page 50)
- Robustness: scaling every strategy to the same ex ante volatility using a rolling 3-year estimate from daily returns gives very similar Sharpe ratios and correlations and identical conclusions. _(robustness, design_choice)_ #mech/risk_management
  > scaled to the same ex ante volatility of 2% per annum using a rolling 3-year estimate of each portfolio’s volatility from daily returns
  exact_rule: Scale each strategy to constant ex ante vol (text says 2% per annum) using rolling 3-year daily-return volatility · reported_result: Sharpe ratios and correlations 'very similar'; not tabulated · exhibit: Internet Appendix
  ^QP15-C50-1
- Constructing strategies to be ex ante beta neutral rather than dollar neutral does not affect alpha inferences. _(robustness, qualifier)_ #mech/risk_management
  > We find that our inferences based on the strategies’ alpha from factor regressions are not affected by market hedging.
  reported_result: Not tabulated · exhibit: Section V.E
  ^QP15-C50-2
- Practical implementations use multiple value and momentum measures to diversify measurement error; bond results improve with composite measures (Table I Panel C); the simple measures likely understate true returns. _(implementation, design_choice)_ #mech/research_method
  > Most practical implementations use a variety of measures for a given style.
  ^QP15-C50-3
- Bonds remain the weakest asset class with the uniform measures; composite measures (Table I Panel C) improve them markedly. _(caveat, qualifier, Opus only)_ #mech/research_method
  > our weakest results using the current measures of value and momentum pertain to bonds, which do not produce statistically significant premia.
  exhibit: Table I Panel C
  ^QP15-C50-4b
- Authors judge the effects applicable to real portfolios, citing the hedge-fund pricing evidence. _(implementation, conclusion, Opus only)_ #mech/research_method
  > current evidence, research, and practical experience point to the effects we study being highly applicable to real world portfolios.
  ^QP15-C50-5b

### C51 (page 51)
- The factors' ability to capture hedge fund returns suggests hedge funds engage in similar or highly correlated strategies globally. _(mechanism, evidence)_ #mech/crowding_positioning
  > fraction of the returns to hedge fund indices, which suggests that hedge funds are engaged in similar or highly correlated strategies globally.
  ^QP15-C51-1
- Over 1972-1991 vs 1992-2011, value and momentum Sharpe ratios declined slightly, cross-market correlation among value strategies rose 0.31 to 0.71 and among momentum 0.46 to 0.77, while value/momentum correlation fell from -0.44 to -0.63, so the combination Sharpe was little changed; consistent with more arbitrageur participation. _(result, evidence)_ #mech/crowding_positioning
  > the average correlation among value strategies has risen from 0.31 to 0.71 and among momentum strategies has risen from 0.46 to 0.77
  reported_result: Value Sharpe 0.78 -> 0.68, momentum 0.90 -> 0.71, 50/50 combination 1.40 -> 1.43; rho(Val,Val) 0.31 -> 0.71; rho(Mom,Mom) 0.46 -> 0.77; rho(Val,Mom) -0.44 -> -0.63 · exhibit: Table VII Panel A · conditions: splits 1972-1991 and 1992-2010/2011 (text says 2011, table label says 2010)
  ^QP15-C51-2
- Splitting at August 1998 (LTCM funding crisis), cross-market correlations jump: value 0.16 -> 0.64 and momentum 0.43 -> 0.71. _(result, evidence)_ #mech/liquidity_flows
  > The correlation among value strategies is much higher after August 1998 (0.16 pre-1998 vs. 0.64 post-1998), and the correlation among momentum strategies is also higher after 1998 (0.43 vs. 0.71).
  reported_result: Pre-08/1998 Sharpe value 0.68, momentum 1.02, combo 1.49; post-08/1998 value 0.75, momentum 0.72, combo 1.39; rho(Val,Val) 0.16 -> 0.64; rho(Mom,Mom) 0.43 -> 0.71; rho(Val,Mom) -0.51 -> -0.55 · exhibit: Table VII Panel A
  ^QP15-C51-3
- Funding liquidity effects appear only after 1998: post-1998 value Sharpe is 0.85 when liquidity worsens vs 0.28 when it improves, momentum 0.19 when it worsens vs 0.99 when it improves (text) while pre-1998 liquidity shocks have little impact; the 50/50 combination is immune even post-1998. _(result, evidence)_ #mech/liquidity_flows
  > value strategies do worse when liquidity improves and momentum strategies do worse when liquidity declines, but these patterns appear only after 1998
  reported_result: Table VII Panel A: worsening liquidity pre-1998 value 1.10, momentum 1.00, combo 1.76; improving pre-1998 1.09, 1.27, 2.04; worsening post-1998 value 0.85, momentum 0.19, combo 0.88; improving post-1998 0.28, 0.77, 1.07 (text quotes 0.99 for post-1998 improving momentum, table shows 0.77); all-sample worsening 0.95/0.57/1.36, improving 0.59/0.87/1.45 · exhibit: Table VII Panel A · conditions: post-1998 only; liquidity shocks = negative/positive funding liquidity shocks (text) or top/bottom half of global index (table caption)
  ^QP15-C51-4
- Dynamic correlation proxy: the time-t correlation among strategies is estimated as the average across asset classes of cross products of monthly returns, regressed on a time trend, recession indicator and liquidity shocks (Table VII Panel B). _(construction, design_choice)_ #mech/research_method
  > We estimate the time t correlation among value strategies globally, ρ(Val,Val) t , as
  exact_rule: rho(Val,Val)_t = average across asset classes of r_i,t * r_k,t for value strategies; likewise rho(Mom,Mom)_t, rho(Val,Mom)_t; regress on time trend, global recession dummy, liquidity shocks, post-Aug-1998 dummy and interaction · exhibit: Table VII Panel B
  ^QP15-C51-5
- Value-momentum correlation became more negative (-0.44 to -0.63), offsetting higher within-style correlations so the combo Sharpe was stable. _(robustness, evidence, Opus only)_ #mech/risk_management
  > the correlation between value and momentum has declined from –0.44 to –0.63
  reported_result: -0.44 -> -0.63 · exhibit: Table VII Panel A
  ^QP15-C51-4b
- Rising correlations may reflect growing arbitrageur participation in global value/momentum. _(mechanism, mechanism_step, Opus only)_ #mech/crowding_positioning
  > These results may be consistent with increased participation of arbitrageurs driving up correlations among value and momentum strategies globally.
  ^QP15-C51-5b

### C52 (page 52)
- Table VII Panel B: correlation among value and among momentum strategies trend up over time and value/momentum correlation trends more negative; recessions increase value and momentum cross-correlations; liquidity shocks increase momentum correlation; with a post-Aug-1998 dummy the time trend vanishes and the dummy and liquidity interaction (momentum) drive the changes. _(result, evidence)_ #mech/crowding_positioning
  > Panel B: Dynamics of Value and Momentum Correlations
  reported_result: Cols 1-3 (coef, t): time trend rho(Val,Val) 0.0067 (2.21), rho(Mom,Mom) 0.0181 (3.26), rho(Val,Mom) -0.0320 (-4.22); recession 0.0828 (1.88), 0.0971 (2.31), 0.0195 (0.31); liquidity shocks 0.0131 (0.98), 0.0519 (2.58), -0.0303 (-1.62). Cols 4-6 with post-1998: time trend -0.0011 (0.20), 0.0045 (0.52), -0.0197 (-1.37); recession 0.0823 (2.05), 0.0938 (2.30), 0.0206 (0.34); liquidity 0.0458 (1.80), -0.0048 (-0.11), -0.0717 (-1.64); post-08/1998 0.1212 (1.70), 0.2136 (1.82), -0.1928 (-0.99); liquidity x post 1998 -0.0379 (-1.20), 0.0929 (2.11), 0.0161 (0.34) · exhibit: Table VII Panel B
  ^QP15-C52-1
- Table VII labels the second half 1992-2010 while the text says 1992-2011; Sharpe levels (combo 1.40/1.43) match Table I P3-P1 (1.42) rather than the rank factors (1.59), so the portfolio type is unstated. _(caveat, qualifier, Opus only)_ #mech/research_method
  > 2nd half—1992 to 2010
  exhibit: Table VII
  ^QP15-C52-2b
- Improving/worsening liquidity regimes are the top/bottom half of global liquidity shock observations (caption cites Table III though shocks are defined with Table IV). _(construction, design_choice, Opus only)_ #mech/liquidity_flows
  > for the top and bottom half of observations based on our global index of liquidity shocks from Table III
  exact_rule: regime = above/below median global liquidity shock · exhibit: Table VII
  ^QP15-C52-4b

### C53 (page 53)
- Recessions raise cross-market correlations of both value and momentum; liquidity shocks raise momentum correlations; rather than a time trend, the post-1998 dummy drives correlation changes and the liquidity effect is exclusively post-1998, pointing to leveraged arbitrageurs and funding constraints rather than slow growth in popularity. _(result, conclusion)_ #mech/crowding_positioning
  > Recessions increase the correlation among both value and momentum strategies globally, controlling for the time trend.
  conditions: post-1998 regime
  ^QP15-C53-1
- Footnote 20: Israel-Moskowitz (2012) find little evidence that returns to size, value and momentum vary with aggregate trading costs or institutional investment over time. _(citation, evidence)_ #mech/crowding_positioning
  > examine the relation between size, value, and momentum
  exhibit: footnote 20
  ^QP15-C53-2
- Conclusion: the cross-asset correlation structure is hard to reconcile with behavioural theories, and the large Sharpe ratio of a global diversified value and momentum portfolio is an even bigger hurdle for rational models; a more general framework is needed since effects exist across assets with different investors and structures. _(result, conclusion)_ #mech/risk_premium
  > The strong correlation structure among value and momentum strategies across such diverse asset classes is difficult to reconcile under existing behavioral theories
  ^QP15-C53-3
- Funding liquidity risk partially explains the correlation structure, especially after 1998, but leaves much unexplained. _(result, conclusion)_ #mech/liquidity_flows
  > exposure to funding liquidity risk provides a partial explanation for this correlation structure, especially following the funding crisis of 1998, but leaves much to be explained
  conditions: post-1998
  ^QP15-C53-4
- Correlations within value and within momentum rose significantly over time, and value-momentum correlation became more negative. _(robustness, evidence, Opus only)_ #mech/research_method
  > the average correlation among value and momentum strategies across markets and asset classes has been significantly increasing over time and the correlation between value and momentum is significantly more negative over time.
  exhibit: Table VII Panel B
  ^QP15-C53-1b
- The correlation increase is a post-1998 regime shift rather than a gradual trend, and liquidity effects on correlations exist only after 1998. _(robustness, evidence, Opus only)_ #mech/liquidity_flows
  > Rather than a time trend, the post-1998 dummy seems to be driving any correlation changes, and the impact of liquidity shocks on correlations also appears to be exclusively a post-1998 phenomenon.
  exhibit: Table VII Panel B · conditions: post-Aug 1998 regime
  ^QP15-C53-3b
- Funding liquidity and limits to arbitrage may be increasingly important drivers of value/momentum after 1998, more than growing popularity per se. _(mechanism, conclusion, Opus only)_ #mech/liquidity_flows
  > funding liquidity risk and limits to arbitrage activity may be a progressively more crucial feature of these strategies
  ^QP15-C53-4b

### C54 (page 54)
- Limited arbitrage (funding constraints) may contribute to the prevalence and dynamics of value and momentum; left to future theory. _(mechanism, conclusion)_ #mech/crowding_positioning
  > limited arbitrage activity may contribute to the prevalence and dynamics of these phenomena
  ^QP15-C54-1
- Final claim: a simple global three-factor model (market, value everywhere, momentum everywhere) describes 48 multi-asset test assets, Fama-French portfolios and hedge fund indices, a framework for pricing global assets. _(result, conclusion)_ #mech/risk_premium
  > we provide a simple global three-factor model that describes a new set of 48 global across-asset-class test assets, the Fama–French portfolios, and a variety of hedge fund indices
  exhibit: Conclusion
  ^QP15-C54-2

