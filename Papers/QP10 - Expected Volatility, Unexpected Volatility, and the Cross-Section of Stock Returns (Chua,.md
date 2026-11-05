---
source_id: QP10
title: "Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua, Goh, Zhang 2010)"
type: paper
claims: 127
opus_only: 14
tags: [paper, layer0]
---
# Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua, Goh, Zhang 2010)

**Authors:** Choong Tze Chua, Jeremy Goh, Zhe Zhang (Singapore Management University)

**Summary:** Question: why do studies disagree on whether idiosyncratic volatility predicts stock returns? Method: split Fama-French-3 daily residual variance into expected (AR(2) forecast, EIV) and unexpected (residual, UIV) parts, run Fama-MacBeth regressions 1963-2003 using UIV as a control for unexpected returns. Conclusion: EIV is insignificant alone but positive (about 0.26-0.43) once UIV is controlled; UIV is positively tied to same-month returns, more so for high-leverage firms (Merton option effect); UIV sorts are contemporaneous, not a trading strategy.

## Argument map

**Question:** Is expected idiosyncratic volatility priced in the cross-section of stock returns (Merton 1987 says yes, Ang et al. say high IV earns less), and why do studies disagree? For an investor: does a stock's forecastable idiosyncratic risk earn a premium?

**Thesis:** Once realized returns are cleaned of their unexpected part by controlling for unexpected idiosyncratic volatility (which rises with same-month returns through Merton's option effect), expected idiosyncratic volatility is positively and significantly related to expected returns. ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C02-5|C02-5]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C01-3|C01-3]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C08-3|C08-3]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C09-2|C09-2]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C18-1|C18-1]])

### Foundations (premises)
- Underdiversified investors demand a premium for expected idiosyncratic risk. _[theoretical, stated; support: citation Merton (1987)]_ ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C01-2|C01-2]])
- Monthly realized returns are dominated by unexpected returns, so they are noisy and possibly biased proxies for expected returns. _[empirical, stated; support: intuition plus Appendix algebra]_ ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C02-4|C02-4]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C02-5|C02-5]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C19-1b|C19-1b]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C19-1|C19-1]])
- UIV is not known at t-1 and so is unrelated to expected returns. _[assumed, stated; support: construction (one-step-ahead AR forecast error); not tested]_ ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C03-4|C03-4]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C08-5|C08-5]])
- Equity is a call option on firm assets, so unexpected rises in asset volatility raise equity value. _[theoretical, stated; support: citation Merton (1974); leverage test]_ ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C04-4|C04-4]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C04-6|C04-6]])
- Expected IV is already priced and does not affect contemporaneous return; only the unexpected part moves price. _[assumed, stated; support: assertion (fn 3)]_ ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C04-10|C04-10]])
- Stock idiosyncratic variance follows a forecastable AR(2) process. _[empirical, stated; support: AIC choice, median coefficients]_ ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C06-9|C06-9]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C07-2|C07-2]])

### Mechanism chain
- 1. Realized monthly return = expected + unexpected return → EIV slope from returns-on-EIV is noisy and biased if UR correlates with EIV in sample: UR dominates; sample correlation with EIV biases the slope (downward if negative) _[assertion]_ ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C02-5|C02-5]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C19-1|C19-1]])
- 2. Unexpected asset volatility shock → same-month positive unexpected return: option effect: call value rises with volatility _[test]_ ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C04-4|C04-4]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C08-3|C08-3]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C14-2|C14-2]])
- 3. UIV highly correlated with UR → UIV as a control removes UR noise and bias: control on the RHS absorbs UR, cutting error variance and correcting bias _[assertion]_ ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C02-7|C02-7]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C19-3b|C19-3b]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C20-1|C20-1]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C20-3|C20-3]])
- 4. EIV slope with UIV control → positive EIV-expected return relation: with UR absorbed, the EIV slope reflects expected returns _[test]_ ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C08-3|C08-3]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C08-5|C08-5]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C09-1|C09-1]])
- 5. Higher idiosyncratic volatility → higher firm-asset premium that outweighs lower equity beta: positive EIV coefficient contradicts constant-premium Merton/Johnson implication _[assertion]_ ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C05-11|C05-11]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C16-6b|C16-6b]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C16-4|C16-4]])

### Design rationale
- **Use expected (ex-ante) IV, not total IV**: pricing theory concerns expected risk (Fu 2009); FSS 1987 analogy. Alternatives: total IV, lagged realized IV (Ang et al.). Sensitivity: not shown directly ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C02-2|C02-2]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C02-3|C02-3]])
- **IV = sum of squared daily FF3 residuals within month**: consistency with Ang et al., Zhang, Wei-Zhang; daily data. Alternatives: EGARCH on monthly returns (Fu; Spiegel-Wang); lagged-factor residuals. Sensitivity: lagged factors: essentially unchanged (not shown) ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C03-1|C03-1]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C03-12|C03-12]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C05-9|C05-9]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C06-8|C06-8]])
- **AR(2) expanding-window forecast, min 36 months**: best AIC, removes autocorrelation. Alternatives: other AR lags. Sensitivity: qualitatively unaffected (not shown) ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C03-2|C03-2]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C06-2|C06-2]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C06-3|C06-3]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C06-9|C06-9]])
- **UIV as RHS control for unexpected returns**: highly correlated with UR, uncorrelated with ER; theory from option effect. Alternatives: direct ER/UR decomposition (not feasible). Sensitivity: not shown for other proxies ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C02-6|C02-6]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C04-3|C04-3]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C19-3b|C19-3b]])
- **Fama-MacBeth with Newey-West t-stats**: not given. Alternatives: none. Sensitivity: not shown ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C08-1|C08-1]])
- **Standardize UIV by firm SD for leverage test**: equal variance across quintiles makes slopes comparable. Alternatives: raw UIV. Sensitivity: not shown ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C15-4|C15-4]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C16-1|C16-1]])

### Evidence map
- EIV alone: -0.03 (t -0.66); with UIV: 0.26 (t 2.99), UIV 0.77 (t 7.52). Tests: steps 1-4. Rules out: that EIV has no partial relation with returns. Does not rule out: (reader) that the EIV coefficient is a mechanical artefact of conditioning on a same-month variable that is cross-sectionally correlated with EIV (UIV = IV - EIV), i.e. a 'bad control'; the unconditional ex-ante relation is still zero. Strength: moderate - large t on UIV, EIV t about 3, no simulation of the estimator ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C08-2|C08-2]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C08-3|C08-3]])
- Controls for size, B/M, momentum, small-cap and NASDAQ exclusion: EIV 0.36-0.43, UIV 1.01-1.11. Tests: that characteristics or microstructure drive step 4. Rules out: size/BM/momentum/smallest-stock explanations. Does not rule out: (reader) other omitted contemporaneous variables (earnings news) correlated with UIV. Strength: moderate ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C09-6|C09-6]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C09-5|C09-5]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C09-4|C09-4]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C10-2|C10-2]])
- Liquidity controls (annual and TAQ monthly) leave EIV/UIV significant. Tests: liquidity alternative. Rules out: illiquidity premium as driver. Does not rule out: (reader) other microstructure noise in daily residuals. Strength: moderate ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C12-2|C12-2]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C12-2b|C12-2b]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C13-1|C13-1]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C13-2|C13-2]])
- UIV-return slope rises monotonically with leverage (0.14 -> 0.21, diff t 6.92), in both sub-periods. Tests: step 2 option effect. Rules out: pure non-leverage explanations of UIV-return link. Does not rule out: (reader) leverage proxying for distress or size; news-driven volatility being larger for levered firms. Strength: moderate - monotone and significant, but contemporaneous ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C16-2|C16-2]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C16-3b|C16-3b]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C16-3|C16-3]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C17-1|C17-1]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C16-3|C16-3]])
- Down-market months: UIV 0.89, EIV 0.21 still significant. Tests: that UIV-return link is not a mechanical up-market artefact. Rules out: market-direction artefact. Does not rule out: (reader) stock-level skewness (positive jumps raise both IV and return). Strength: weak to moderate - only month filter ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C09-8|C09-8]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C09-3|C09-3]])
- UIV-sorted portfolios: H-L 0.58%/mo, FF3+MOM alpha 0.39%/mo. Tests: step 2. Rules out: . Does not rule out: (reader) everything; not tradable. Strength: weak as investment evidence - contemporaneous ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C14-2|C14-2]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C15-1|C15-1]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C14-4|C14-4]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C15-2|C15-2]])

### Regimes
- High financial leverage → UIV-return relation stronger (more option-like equity) ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C04-6|C04-6]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C16-2|C16-2]])
- 1963-1984 vs 1984/85-2003 → monotone leverage pattern holds in both; slopes and DIV larger in earlier half ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C16-3|C16-3]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C16-3|C16-3]])
- Down-market months → EIV and UIV coefficients remain significant ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C09-8|C09-8]])
- 1993-2003 TAQ sample → smaller EIV/UIV coefficients (about 0.28/0.55) ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C13-3|C13-3]])

### Gaps and conflicts
- [conflict] Intro reports EIV 0.17 / UIV 0.828 (5% level) while Table 2 shows 0.2591 / 0.7695 (EIV t 2.99, 1% claimed in text). ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C03-3|C03-3]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C08-3|C08-3]])
- [conflict] Text says size is negatively related to returns, but Table 3 size coefficients are positive (0.0007, t 2.19) in all samples. ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C09-7|C09-7]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C10-2|C10-2]])
- [conflict] Sub-period dates: text says second half starts Jan 1985, Table 6 Panel C says 1984:01 (overlap with Panel B to 1984:12). ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C16-3|C16-3]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C16-3|C16-3]])
- [conflict] UIV SD 0.114 in text vs 0.1231 in Table 1. ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C06-7|C06-7]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C07-1|C07-1]])
- [conflict] SIC codes swapped in Table 6 note vs Section II. ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C05-6|C05-6]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C17-2|C17-2]])
- [conflict] Text cites monthly-liquidity coefficients EIV 0.28 / UIV 0.55 'after controlling for both' lag and change, but that column shows 0.3218 / 0.5595; 0.2840 / 0.5438 is the lag-only column. ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C13-3|C13-3]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C12-2b|C12-2b]])
- [unspecified] EIV is described as one-step-ahead forecast (eq. 4) but Table 1 note calls it 'fitted values'; in-sample fitting would leak information. ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C06-2|C06-2]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C07-3b|C07-3b]])
- [unspecified] Newey-West lag length not stated; Table 2 note lists lagged EIV and ret-1 regressors with no values. ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C08-1|C08-1]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C08-5b|C08-5b]])
- [unspecified] Equal-weighted portfolio results claimed but not reported; conclusion says 'both types of portfolios'. ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C04-2|C04-2]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C18-3b|C18-3b]])
- [untested] No predictive / tradable test of EIV: EIV is known ex ante, yet no EIV-sorted portfolio, no transaction costs, and the EIV-only regression is zero. The positive EIV result exists only conditional on same-month UIV. ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C08-2|C08-2]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C14-4|C14-4]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C15-2|C15-2]])
- [untested] Identifying assumption that UIV is unrelated to expected returns is not tested; UIV = IV - EIV is mechanically correlated with EIV, and the claim that this moves the estimate closer to truth is asserted without proof or simulation. ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C03-4|C03-4]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C20-2|C20-2]])
- [conflict] Economic magnitude '1% increase in EIV (10% increase in SD)' mixes variance and SD units; leverage-test text says 'low-UIV to high-UIV' where it means low to high leverage. ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C09-1|C09-1]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C16-2|C16-2]])
- [data] Firm UIV standardization uses each firm's full-sample SD (look-ahead), harmless for a contemporaneous test but not usable in real time. ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C15-4|C15-4]])
- [unspecified] Robustness tests for lagged factors and other AR models are 'available upon request' only. ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C06-8|C06-8]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C06-9|C06-9]])

### Relations to other strategies
- Ang et al. (2006, 2009) low-idiosyncratic-volatility anomaly: **contradicts**. they find high lagged realized IV predicts low returns; authors argue realized measures are not expected values so results are not comparable ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C01-5|C01-5]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C04-1|C04-1]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C18-3|C18-3]])
- Fu (2009), Spiegel-Wang (2005) EGARCH expected IV premium: **complement**. same positive conclusion via different estimator ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C04-1|C04-1]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C18-3|C18-3]])
- Size effect: **substitute**. IV may partly explain the size effect (with sign conflict noted) ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C09-7|C09-7]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C10-2b|C10-2b]])
- Liquidity premium: **contradicts**. after volatility controls illiquidity coefficients are negative ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C13-2|C13-2]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C13-4|C13-4]])
- Market-level volatility feedback (FSS 1987): **special case**. firm-level version of expected/unexpected volatility decomposition ([[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C02-3|C02-3]], [[QP10 - Expected Volatility, Unexpected Volatility, and the Cross-Section of Stock Returns (Chua,#^QP10-C04-8|C04-8]])

### Forward-looking inputs (reader synthesis)
(reader) Only EIV is observable in advance (AR(2) forecast of next-month idiosyncratic variance from daily FF3 residuals). The paper implies a positive premium on EIV over one month, but only conditional on next month's UIV; unconditionally (Table 2 model 1) EIV does not predict returns, so a long-high-EIV sort would not be expected to pay on its own. UIV is contemporaneous and has no forecasting use. For a macro/multi-asset researcher the transferable point is methodological: test a risk-return relation with ex-ante risk and control for the contemporaneous risk surprise. It would stop working if the UIV-UR link (option effect) weakened or if the UIV-EIV cross-sectional correlation, not expected returns, drives the EIV slope.

### Reader inferences (not stated by the authors)
- (reader) The EIV slope in model 2 is a partial coefficient conditional on a same-month realization; an investor cannot harvest it without knowing UIV, and the unconditional EIV-return slope is about zero.
- (reader) Because UIV = IV - EIV, conditioning on UIV is close to conditioning on realized IV; the 'positive EIV' result may partly reflect that high-EIV stocks with a given realized IV had lower UIV, a possible bad-control problem.
- (reader) Positive return jumps (skewness) raise both realized IV and return, an alternative to the option effect for the UIV-return link that is not separately tested.
- (reader) Monthly IV autocorrelation is low (median phi1+phi2 about 0.35), so EIV is a weak forecast and mostly cross-sectional level differences.
- (reader) Asset class is US single stocks only; relevance to macro is the econometric control idea, not a signal.

## Claims

### C01 (page 1)
- Standard theory says idiosyncratic risk earns no premium, which is the benchmark the paper tests against. _(mechanism, premise)_ #mech/risk_premium
  > Standard asset pricing theory predicts that only systematic risks should be priced.
  ^QP10-C01-1
- If investors are underdiversified, expected idiosyncratic volatility can carry a premium (Merton 1987 incomplete-information model), giving a reason for EIV to predict returns positively. _(citation, mechanism_step)_ #mech/risk_premium
  > Merton (1987), however, argues that expected idiosyncratic volatility may explain expected stock returns if investors are underdiversified.
  ^QP10-C01-2
- Headline result: unexpected idiosyncratic volatility (UIV) co-moves positively with same-month unexpected returns. _(result, conclusion)_ #mech/research_method
  > We show strong evidence that unexpected idiosyncratic volatility is positively related to unexpected returns.
  exhibit: Abstract
  ^QP10-C01-3
- The positive EIV-return relation (with UIV as control) survives size, book-to-market, past-return, liquidity controls and subsamples. _(robustness, conclusion)_ #mech/research_method
  > This result holds after controlling for various firm characteristics, and it is robust across different sample periods.
  exhibit: Abstract
  ^QP10-C01-4
- Ang et al. found high realized idiosyncratic volatility portfolios earn low subsequent returns: the negative result this paper argues is not about expected volatility. _(citation, context)_ #mech/risk_premium
  > Ang et al. (2006, 2009) find that portfolios with high idiosyncratic volatility subsequently have low returns.
  exhibit: footnote 1
  ^QP10-C01-5
- Lehmann, Malkiel-Xu, Spiegel-Wang and Fu find idiosyncratic volatility positively related to cross-sectional expected returns, so the literature is split. _(citation, context)_ #mech/risk_premium
  > Lehmann (1990), Malkiel and Xu (2006), Spiegel and Wang (2005), and Fu (2009) find that
  exhibit: footnote 1
  ^QP10-C01-6
- Aggregate-level studies of average idiosyncratic volatility versus market return also give mixed results. _(citation, context)_ #mech/research_method
  > Goyal and Santa-Clara (2003), Bali et al. (2005), Jiang and Lee (2006), and Guo and Savickas (2006) study the relation between the average idiosyncratic volatility and stock market return, and the results are mixed.
  exhibit: footnote 1
  ^QP10-C01-7

### C02 (page 2)
- The UIV-return link is attributed to Merton's option effect: equity is a call on firm assets, so a vol shock raises equity value. _(mechanism, mechanism_step)_ #mech/risk_premium
  > unexpected idiosyncratic volatility is positively related to unexpected returns and that this relation is consistent with the option effect proposed by Merton (1974).
  ^QP10-C02-1
- Fu (2009) argues the theoretically relevant measure is expected (ex ante) idiosyncratic volatility, not realized total volatility, when testing if idiosyncratic risk is priced. _(citation, premise)_ #mech/research_method
  > because the objective is to examine whether idiosyncratic risk is priced in expected returns
  exhibit: intro
  ^QP10-C02-2
- French, Schwert and Stambaugh (1987) suggested splitting market volatility into expected and unexpected parts; the paper copies this at the firm level. _(citation, design_choice)_ #mech/research_method
  > They suggest decomposing total market volatility into expected and unexpected components.
  exhibit: intro
  ^QP10-C02-3
- Realized monthly return is a noisy and possibly biased proxy for expected return, so regressions of realized returns on EIV have low power. _(mechanism, premise)_ #mech/research_method
  > total realized returns are poor (and potentially biased) proxies for expected returns in finite sample.
  ^QP10-C02-4
- For monthly stock returns the unexpected component dominates, so sample correlation of EIV with unexpected returns can cloud the EIV-expected return relation. _(mechanism, premise)_ #mech/research_method
  > At the monthly horizon, the effects of unexpected returns often dominate those of expected returns
  ^QP10-C02-5
- Since returns cannot be split directly, the authors use a variable highly correlated with unexpected returns (UIV) as a control. _(construction, design_choice)_ #mech/research_method
  > Because there is no easy way to decompose total stock returns into expected and unexpected components
  exact_rule: include UIV on right-hand side as proxy control for unexpected return when regressing returns on EIV
  ^QP10-C02-6
- Controlling for UIV removes finite-sample bias on the EIV coefficient and shrinks its standard error. _(mechanism, mechanism_step)_ #mech/research_method
  > we document a strong correlation between UIV and unexpected returns, which allows the true relation between expected returns and idiosyncratic volatility to be better observed because the finite sample bias on the coefficient of EIV is mitigated
  ^QP10-C02-7

### C03 (page 3)
- Monthly idiosyncratic volatility IV is the sum over the month's trading days of squared residuals from a daily Fama-French three-factor regression. _(construction, design_choice)_ #mech/research_method
  > as the within-month sum of squared residuals from the daily regression of the Fama–French (1993) three-factor model
  exact_rule: for each stock and month, regress daily returns on MKT, SMB, HML; IV = sum over days in month of squared residuals · data_needed: CRSP daily returns, Fama-French daily factors (French library)
  ^QP10-C03-1
- Each stock's IV history is fitted with an AR(2); the prediction is EIV and the residual is UIV. _(construction, design_choice)_ #mech/research_method
  > The monthly predicted idiosyncratic volatility is labeled EIV, and the residual is labeled UIV
  exact_rule: AR(2) on each stock's monthly IV series, using data only to month m; EIV = fitted forecast, UIV = realized IV minus EIV
  ^QP10-C03-2
- Cross-sectional regression of returns on EIV alone gives a coefficient near zero and insignificant. _(result, evidence)_ #mech/risk_premium
  > We find that EIV alone cannot explain stock returns.
  reported_result: Table 2 model 1: EIV coefficient -0.0327, t -0.66, adj R2 0.016, 1963:07-2003:12 · exhibit: Table 2 · conditions: without UIV control
  ^QP10-C03-3
- Intro states joint regression coefficients of 0.17 (EIV) and 0.828 (UIV), both significant at 5%; these differ from Table 2 values (0.26, 0.77). _(result, evidence)_ #mech/risk_premium
  > The average coefficients for EIV and UIV are 0.17 and 0.828, respectively, both statistically significant at the 5% level.
  reported_result: EIV 0.17, UIV 0.828 (intro); Table 2 shows 0.2591 and 0.7695 · exhibit: introduction vs Table 2
  ^QP10-C03-4
- The joint EIV/UIV result survives characteristic and liquidity controls and exchange exclusions. _(robustness, evidence)_ #mech/research_method
  > The results are robust after controlling for size, book-to-market, past returns, stock exchange, and various liquidity measures.
  exhibit: Tables 3-4
  ^QP10-C03-5
- UIV is by construction not in investors' month t-1 information set, so it cannot be priced as expected return; its positive coefficient therefore proxies unexpected return. _(mechanism, mechanism_step)_ #mech/research_method
  > hence, by construction it should not be related to the expected stock returns.
  ^QP10-C03-6
- Authors infer UIV's coefficient reflects unexpected returns, so EIV's coefficient, conditional on UIV, reflects expected return. _(mechanism, mechanism_step)_ #mech/research_method
  > We deduce that the positive and significant coefficient for UIV is driven by its relation with unexpected returns.
  ^QP10-C03-7
- Without a control for unexpected return, the EIV-expected return relation is hidden in realized returns. _(mechanism, conclusion)_ #mech/research_method
  > using total returns as a proxy for expected returns clouds the true relation between expected returns and EIV
  ^QP10-C03-8
- The paper differs from Fu and Spiegel-Wang by using daily-return IV with AR(2) decomposition rather than monthly EGARCH, while reaching a similar positive sign. _(citation, context)_ #mech/research_method
  > Unlike Fu and Spiegel and Wang, who apply the EGARCH model on monthly returns to estimate expected volatility, we focus on decomposing
  exhibit: Section I
  ^QP10-C03-9
- Contrast with Ang et al.: they use lagged realized volatility and realized returns, a different object than expected volatility vs expected return. _(citation, context)_ #mech/risk_premium
  > Our result is different from that of Ang et al. (2006, 2009), who find a negative relation between realized returns and lagged realized volatility.
  ^QP10-C03-10
- No agreed model for single-stock idiosyncratic volatility; EGARCH on monthly data used by Fu/Spiegel-Wang. _(caveat, qualifier)_ #mech/research_method
  > There is no consensus on what constitutes the best model for idiosyncratic volatility at the individual stock level.
  exhibit: footnote 2
  ^QP10-C03-11
- Daily returns are used for the volatility estimate to match existing literature, as the novelty lies in the decomposition. _(construction, design_choice)_ #mech/research_method
  > Because the main focus and innovation of this article is the decomposition of volatility, we keep the volatility estimates consistent with most of the existing literature by using daily return data.
  data_needed: CRSP daily returns · exhibit: footnote 2
  ^QP10-C03-12

### C04 (page 4)
- Ang et al.'s results are about noisy realized measures, hence not directly comparable to the expected-return/expected-volatility test. _(caveat, qualifier)_ #mech/research_method
  > their results do not necessarily involve the relation between the expected returns and expected volatility
  ^QP10-C04-1
- EIV-stratified UIV-sorted portfolios show high-UIV returns and CAPM/FF3/FF3+MOM alphas above low-UIV, equal- and value-weighted. _(robustness, evidence)_ #mech/research_method
  > the returns and alphas of the high-UIV portfolio are always significantly higher
  reported_result: see Table 5 claims · exhibit: Table 5 (value-weighted)
  ^QP10-C04-2
- Criterion for the control variable: highly correlated with unexpected returns, uncorrelated with expected returns. _(construction, design_choice)_ #mech/research_method
  > The solution is to find a proxy that we can use as a control variable that is likely to be highly correlated with unexpected returns and uncorrelated with expected returns.
  ^QP10-C04-3
- Equity as a call option on firm assets (Merton 1974) is the theoretical basis for choosing UIV as control. _(citation, premise)_ #mech/risk_premium
  > Merton (1974) posits that we can view common stocks as call options on the assets of the firm.
  ^QP10-C04-4
- A positive volatility shock raises firm asset volatility and so the equity-call value, raising the contemporaneous price and unexpected return ('option effect'). _(mechanism, mechanism_step)_ #mech/risk_premium
  > that the call option (the common stock) should increase in value as well, hence, the increase in the contemporaneous stock price and the unexpected return
  ^QP10-C04-5
- Prediction: the UIV-return relation strengthens with leverage because levered equity is more option-like. _(mechanism, mechanism_step)_ #mech/risk_premium
  > The option effect also implies that the observed relation should be stronger for firms with higher financial leverage because the equity of these firms are more option-like.
  ^QP10-C04-6
- UIV coefficient is positive in all five leverage quintiles and rises monotonically with leverage. _(result, evidence)_ #mech/research_method
  > Our results show that the relation between UIV and returns is positive for firms in all five quintiles and the relation gets monotonically stronger as leverage increases.
  reported_result: Table 6 Panel A: UIVS coefficients 0.1402 -> 0.2096 across leverage quintiles · exhibit: Table 6
  ^QP10-C04-7
- French-Schwert-Stambaugh, Jiang-Lee and Ang et al. found aggregate volatility innovations informative for returns; this paper extends to firm-level UIV. _(citation, evidence)_ #mech/research_method
  > find that innovations in volatilities, albeit aggregated over all stocks, are useful in the study of stock returns.
  exhibit: Section I
  ^QP10-C04-8
- Duffee (1995) found the return-volatility link weakens with leverage, the opposite of the option effect; authors say UIV, not total volatility, is the right test variable. _(citation, qualifier)_ #mech/risk_premium
  > However, he finds that this relation is negatively related to the leverage ratio.
  exhibit: footnote 3
  ^QP10-C04-9
- Expected volatility is already priced, so only unexpected volatility should move contemporaneous prices. _(mechanism, mechanism_step)_ #mech/research_method
  > We contend that it is more appropriate to use unexpected volatility to test the option effect, because the expected volatility should have already been priced
  exhibit: footnote 3
  ^QP10-C04-10

### C05 (page 5)
- The monotonic leverage pattern of the UIV effect holds in every subperiod examined. _(robustness, evidence)_ #mech/research_method
  > document that this monotonic relation holds for all the subperiods we investigate.
  exhibit: Table 6 Panels B-C
  ^QP10-C05-1
- Universe: all CRSP common stocks (share codes 10, 11) on NYSE/AMEX/NASDAQ, January 1963 to December 2003 (regressions start 1963:07). _(construction, design_choice)_ #mech/research_method
  > The sample period is from January 1963 to December 2003. All common stocks (share codes 10 and 11) traded at NYSE, AMEX, and NASDAQ are included.
  exact_rule: universe: CRSP shrcd 10,11; NYSE/AMEX/NASDAQ · data_needed: CRSP daily and monthly stock files, Compustat annual
  ^QP10-C05-2
- Book-to-market recomputed monthly: prior fiscal year-end book equity (Compustat item 60) over current-month market cap. _(construction, design_choice)_ #mech/research_method
  > we define the book-to-market ratio every month as the ratio between the previous year’s ending book value of common equity (item 60) and the current month’s market capitalization.
  exact_rule: BM_t = book common equity (item 60) at previous year end / market cap at t · data_needed: Compustat annual item 60; CRSP market cap
  ^QP10-C05-3
- Leverage = total debt (item 181) / (debt + other equity + market equity), where debt + other equity = prior year-end total assets minus prior year-end common equity. _(construction, design_choice)_ #mech/research_method
  > Financial leverage is defined as the book value of total debt (item 181) divided by the sum of the book value of debt, other equity, and the market value of common equity
  exact_rule: lev = item181 / (item181 + other equity + current market cap); other equity = prior year-end assets (item 6) - common equity · data_needed: Compustat items 181, 6, 60; CRSP market cap
  ^QP10-C05-4
- Firms with negative book-to-market are excluded. _(construction, design_choice)_ #mech/research_method
  > We exclude firms with negative book-to-market ratio.
  exact_rule: drop BM<0
  ^QP10-C05-5
- Financials (SIC 6000-6999) and utilities (SIC 4900-4999) are dropped only in leverage analyses. _(construction, design_choice)_ #mech/research_method
  > Following the literature, we exclude financial firms (Standard Industrial Classification [SIC] codes 6000–6999) and utility firms (SIC codes 4900–4999) whenever we need leverage information.
  exact_rule: exclude SIC 6000-6999 and 4900-4999 in leverage regressions · data_needed: SIC codes
  ^QP10-C05-6
- Firms with leverage outside [0,1] are excluded. _(construction, design_choice)_ #mech/research_method
  > We also exclude firms whose leverage ratio is outside the range of [0,1].
  exact_rule: keep 0<=lev<=1
  ^QP10-C05-7
- Factor data and risk-free rate come from Kenneth French's data library. _(construction, context)_ #mech/research_method
  > We obtain the daily and monthly risk-free rate and Fama–French three-factor returns from 1963 to 2003 from Kenneth French’s Web site.
  data_needed: Fama-French daily/monthly MKT, SMB, HML, rf (French data library) · exhibit: footnote 5
  ^QP10-C05-8
- Each month a daily three-factor regression is run per stock, with alpha and betas constant within the month but allowed to vary across months (Eq 1). _(construction, design_choice)_ #mech/research_method
  > For each month, we first perform the Fama–French (1993) regression using daily returns:
  exact_rule: r_{i,d,m} = a_{i,m} + b_mkt MKT + b_smb SMB + b_hml HML + e_{i,d,m}, estimated within each month · data_needed: CRSP daily, FF daily factors · exhibit: Equation (1)
  ^QP10-C05-9
- The contemporaneous positive UIV-return link does not by itself imply lower future returns. _(caveat, qualifier)_ #mech/research_method
  > It is worth noting the positive contemporaneous relation between UIV and unexpected return does not necessarily lead to a negative predictive relation.
  exhibit: footnote 4
  ^QP10-C05-10
- In Merton's framework with a constant asset premium, higher volatility lowers equity beta and hence expected equity return (Johnson 2004). _(citation, mechanism_step)_ #mech/risk_premium
  > if the risk premium of the underlying asset (total firm value) remains constant, an increase in volatility will lead to lower equity beta, and consequently to lower expected future returns for the equity of the firm
  exhibit: footnote 4
  ^QP10-C05-11
- The positive EIV coefficient implies asset-level premium rises with volatility, outweighing the equity-beta effect. _(mechanism, conclusion)_ #mech/risk_premium
  > Instead, our evidence suggests that an increase in volatility leads to higher expected returns on the value of the underlying firm as well, and this effect dominates the negative effect of volatility on equity beta.
  exhibit: footnote 4
  ^QP10-C05-12
- Authors conclude the contemporaneous idiosyncratic risk-return relation is driven by the option effect. _(mechanism, conclusion)_ #mech/risk_premium
  > Thus, we find strong evidence suggesting the idiosyncratic risk and stock return relation is indeed driven by the option effect.
  ^QP10-C05-13

### C06 (page 6)
- IV for stock i in month m is the sum of squared daily residuals, following Ang et al. and Zhang. _(construction, design_choice)_ #mech/research_method
  > Similar to Ang et al. (2006) and Zhang (2004), we then define the
  exact_rule: IV_{i,m} = sum_{d=1}^{N_m} e_{i,d,m}^2 (Eq 2) · exhibit: Equation (2)
  ^QP10-C06-1
- AR(2) is re-estimated every month per stock using only data to that month (no look-ahead). _(construction, design_choice)_ #mech/research_method
  > Every month m, using data only up to that month, we perform the following time-series regression for each stock:
  exact_rule: IV_{i,m} = p0 + p1 IV_{i,m-1} + p2 IV_{i,m-2} + xi, expanding sample to m · exhibit: Equation (3)
  ^QP10-C06-2
- A stock needs at least 3 years of IV history to receive an AR(2) forecast. _(construction, design_choice)_ #mech/research_method
  > We require that a firm has at least three years of data to estimate equation (3).
  exact_rule: min 36 months of history · exhibit: Equation (3)
  ^QP10-C06-3
- EIV for month m+1 uses AR coefficients estimated through m applied to IV at m and m-1. _(construction, design_choice)_ #mech/research_method
  > (using coefficients estimated from date up to month m):
  exact_rule: EIV_{i,m+1} = p0 + p1 IV_{i,m} + p2 IV_{i,m-1} · exhibit: Equation (4)
  ^QP10-C06-4
- UIV is realized IV minus the prior-month forecast EIV. _(construction, design_choice)_ #mech/research_method
  > we then define the unexpected idiosyncratic volatility for stock i in month m+1 as the difference between IV and EIV for month m+1
  exact_rule: UIV_{i,m+1} = IV_{i,m+1} - EIV_{i,m+1} · exhibit: Equation (5)
  ^QP10-C06-5
- Descriptive scale of monthly IV: mean 0.028, sd 0.132, positively skewed, fat-tailed. _(result, context)_ #mech/research_method
  > The monthly mean and standard deviation of IV are 0.028 and 0.132, respectively;
  reported_result: IV mean 0.028, sd 0.132 (Table 1 Panel A: 0.0279, 0.1317) · exhibit: Table 1
  ^QP10-C06-6
- UIV has near-zero mean and sd comparable to IV. The text's 0.114 differs from Table 1's 0.1231. _(result, context)_ #mech/research_method
  > UIV has a close-to-zero mean but is as volatile as the IV ; the standard deviation is 0.114.
  reported_result: text: UIV sd 0.114; Table 1: 0.1231; EIV sd 0.049 · exhibit: Table 1
  ^QP10-C06-7
- Adding one-day lagged daily factors to the IV regression leaves results essentially unchanged (non-synchronous trading check). _(robustness, evidence)_ #mech/research_method
  > We also experimented with other IV measures by including one-day lagged daily Fama–French factors in equation (1).
  exhibit: footnote 6
  ^QP10-C06-8
- AR(2) chosen because it removes most autocorrelation and minimizes AIC among tested lag lengths. _(construction, design_choice)_ #mech/research_method
  > The AR(2) model eliminates most of the serial autocorrelation and is the best model based on the Akaike information criterion.
  reported_result: AIC-selected; no numbers shown · exhibit: footnote 7
  ^QP10-C06-9
- Alternative AR lag specifications give qualitatively the same main results. _(robustness, evidence)_ #mech/research_method
  > The main results of this article are qualitatively unaffected by the choice of time-series model.
  exhibit: footnote 7
  ^QP10-C06-10

### C07 (page 7)
- Table 1 sample: July 1963 to December 2003. IV mean 0.0279 / sd 0.1317; EIV mean 0.0244 / sd 0.0492; UIV mean 0.0035 / sd 0.1231; skewness 18.9, 11.7, 13.2; kurtosis 699, 267, 740. _(result, context)_ #mech/research_method
  > The sample is from 1963:07 to 2003:12.
  reported_result: Table 1 Panel A: IV 0.0279/0.1317/18.90/699.45; EIV 0.0244/0.0492/11.70/267.47; UIV 0.0035/0.1231/13.24/740.13 (mean/sd/skew/kurt) · exhibit: Table 1 (page image checked)
  ^QP10-C07-1
- AR(2) coefficient percentiles show wide dispersion; median phi0 0.0074, phi1 0.2233, phi2 0.1297 (10th pct phi2 is -0.0497, 90th phi1 0.4356). _(result, evidence)_ #mech/cycle_persistence
  > Although there are significant variations in the coefficients across time and stocks, the median AR(2) relation is
  reported_result: Table 1 Panel B percentiles 10/25/50/75/90: phi0 .0017/.0033/.0074/.0158/.0304; phi1 .0300/.1178/.2233/.3294/.4356; phi2 -.0497/.0307/.1297/.2265/.3149 · exhibit: Table 1 Panel B (page image checked)
  ^QP10-C07-2
- Baseline Fama-MacBeth step: monthly cross-sectional regression of returns on EIV alone (Eq 6). _(construction, design_choice)_ #mech/research_method
  > For each month, we perform the following cross-sectional regression:
  exact_rule: R_{i,m} = f0 + f1 EIV_{i,m} + eta; average over months with Newey-West t-stats · exhibit: Equation (6)
  ^QP10-C07-3
- Table 1 note describes EIV as the AR(2) fitted values and UIV as residuals (in-sample wording), unlike eq. (4) which is a one-step-ahead forecast. _(caveat, qualifier, Opus only)_ #mech/research_method
  > We define the fitted values as the expected IV (EIV ) and the residuals as the unexpected IV (UIV )
  ^QP10-C07-3b

### C08 (page 8)
- Fama-MacBeth: average monthly cross-sectional coefficients, Newey-West adjusted t-stats, average adjusted R2. _(construction, design_choice)_ #mech/research_method
  > We report the time-series averages of parameter estimates and Newey–West (1987) adjusted t-statistics.
  exact_rule: monthly cross-section OLS, time-series mean of coefficients, Newey-West t · exhibit: Table 2 note
  ^QP10-C08-1
- EIV alone has coefficient -0.0327 (t -0.66), adj R2 0.016, constant 0.0143 (t 5.33). _(result, evidence)_ #mech/risk_premium
  > The coefficient for EIV is slightly negative at −0.03, yet not statistically significant as the t-statistic is only −0.66.
  reported_result: Table 2 model 1, 1963:07-2003:12: const 0.0143 (5.33), EIV -0.0327 (-0.66), adj R2 0.016 · exhibit: Table 2
  ^QP10-C08-2
- Adding UIV raises the EIV coefficient from -0.03 to 0.26 and lifts adj R2 from 0.016 to 0.076. _(result, evidence)_ #mech/risk_premium
  > The average coefficient for UIV is 0.77. With the inclusion of UIV, the average coefficient for EIV increases from −0.03 to 0.26.
  reported_result: Table 2 model 2: const 0.0104 (4.16), EIV 0.2591 (t 2.99), UIV 0.7695 (7.52), adj R2 0.076; 1963:07-2003:12 · exhibit: Table 2
  ^QP10-C08-3
- Both components are needed: using total or expected volatility alone misses the EIV premium. _(mechanism, conclusion)_ #mech/risk_premium
  > These results suggest that the decomposition of idiosyncratic volatility into both expected and unexpected components is essential in explaining the cross-sectional returns.
  ^QP10-C08-4
- Because UIV should have little relation with expected returns, its coefficient is read as an unexpected-return effect, making UIV a control and EIV's coefficient an expected-return effect. _(mechanism, mechanism_step)_ #mech/research_method
  > This implies that the positive and significant coefficient for UIV must be largely driven by its relation with unexpected returns.
  ^QP10-C08-5
- UIV enters contemporaneously with the month's return; the note also lists one-month lagged EIV and ret-1, but no such rows have values in Table 2. _(construction, design_choice, Opus only)_ #mech/research_method
  > cross-sectional regressions of monthly stock returns on the contemporaneous unexpected volatility (UIV )
  exhibit: Table 2 note
  ^QP10-C08-5b

### C09 (page 9)
- Economic size: +1 percentage point of monthly EIV maps to +0.26 percentage point of expected monthly return. _(result, evidence)_ #mech/risk_premium
  > A 1% increase in EIV (or 10% increase in the expected idiosyncratic return standard deviation) leads to 0.26% increase in the expected stock return.
  reported_result: coefficient 0.26 from Table 2 model 2 (monthly returns) · exhibit: Table 2
  ^QP10-C09-1
- Previous studies omitting UIV may have missed the EIV premium. _(mechanism, conclusion)_ #mech/research_method
  > The key result here is that we need UIV to bring out the significance of the relation between EIV and expected returns—an issue that many previous studies may have overlooked.
  ^QP10-C09-2
- UIV is not mechanically positive with returns: a large negative return also raises realized IV; a priori the sign is open, so the positive coefficient is substantive. _(mechanism, evidence)_ #mech/research_method
  > In contrast, an unexpectedly low (negative) return will also generate a high UIV statistic.
  ^QP10-C09-3
- Adding size, BM, ret(-1), ret(-12..-2) controls: EIV 0.43, UIV 1.01 (both 1% significance); similar when dropping the smallest size quintile or NASDAQ stocks. _(result, evidence)_ #mech/risk_premium
  > For the full sample, the average coefficient estimates for EIV and UIV are 0.43 and 1.01, respectively, after controlling for other firm characteristics.
  reported_result: Table 3 full sample: EIV 0.4304 (4.69), UIV 1.0093 (8.30), adj R2 0.113 · exhibit: Table 3
  ^QP10-C09-4
- Robustness to microstructure/illiquid small stocks: drop bottom size quintile (prior-month market cap, re-sorted monthly) and, separately, drop NASDAQ. _(robustness, evidence)_ #mech/research_method
  > we conduct two additional robustness tests. In one test, for every month we sort all stocks in our sample into five size quintiles based on the previous month’s market capitalization and exclude the smallest quintile from the sample.
  exact_rule: monthly sort on lagged market cap, exclude smallest quintile; separately exclude NASDAQ stocks · exhibit: Table 3
  ^QP10-C09-5
- Momentum control is the return from t-12 to t-2 (skipping last month), plus ret(-1) as reversal control. _(construction, design_choice)_ #mech/research_method
  > We also add previous one-year return (returns from previous 12 to 2 months ago) to control for the momentum effect
  exact_rule: ret_{-2-12} = cumulative return months t-12 to t-2 · exhibit: Table 3
  ^QP10-C09-6
- After EIV/UIV controls the size coefficient is small (0.0007 at t 2.19 in the full sample, positive; text reads size as negatively related), authors suggest size effect partly absorbed by IV, left for future work. _(result, qualifier)_ #mech/research_method
  > Firm size is negatively related to returns after controlling for the volatility effects, suggesting that the size effect may be partially
  reported_result: Table 3 size coef 0.0007 (t 2.19) full sample; text says negative - inconsistent sign · exhibit: Table 3
  ^QP10-C09-7
- Excluding months with positive market excess return, UIV and EIV stay positive and significant, so UIV's link to returns holds in down markets too. _(robustness, evidence)_ #mech/research_method
  > This indicates that the positive, contemporaneous relation between UIV and returns is not mechanically driven by the construction of our variables
  reported_result: down-market months only: EIV 0.2085, UIV 0.8924, both significant at 5% · exhibit: footnote 8 · conditions: months with CRSP market excess return <= 0
  ^QP10-C09-8

### C10 (page 10)
- Table 3 columns: full sample, excluding smallest size quintile, excluding NASDAQ; regressors EIV, UIV, size (lagged log market cap), b/m, ret(-1), ret(-2..-12). _(construction, design_choice)_ #mech/research_method
  > In addition to using the full sample, we sort stocks into five quintiles based on the previous month’s market capitalization.
  exact_rule: Fama-MacBeth of R on EIV, UIV, lagged log size, BM, ret-1, ret-2-12; require positive book and market value · data_needed: CRSP, Compustat · exhibit: Table 3 note
  ^QP10-C10-1
- Table 3 coefficients: Full: EIV 0.4304 (4.69), UIV 1.0093 (8.30), size 0.0007, BM 0.0091 (12.95), ret-1 -0.0603 (-13.48), ret-2-12 0.0101 (7.14), R2 0.113. Excl. small: EIV 0.3567 (3.17), UIV 1.1143 (7.44), R2 0.097. Excl. NASDAQ: EIV 0.3639 (3.91), UIV 1.0510 (8.73), R2 0.109. _(result, evidence)_ #mech/risk_premium
  > TABLE 3. Cross-Sectional Regressions of Returns on EIV and UIV : Controlling for Firm Characteristics.
  reported_result: Table 3, 1963:07-2003:12, Fama-MacBeth, NW t · exhibit: Table 3
  ^QP10-C10-2
- Concern: high IV stocks may be illiquid and spuriously volatile (bid-ask), so the premium might be a liquidity premium; also unexpected liquidity shocks may bias UIV-return link. _(mechanism, premise)_ #mech/liquidity_flows
  > It may be possible that firms with high idiosyncratic volatility are less liquid
  ^QP10-C10-3
- The size effect may be partly explained by idiosyncratic volatility, consistent with Fu (2009); left to future work. _(citation, qualifier, Opus only)_ #mech/research_method
  > explained by the IV s. This result is consistent with Fu’s (2009) findings.
  ^QP10-C10-2b

### C11 (page 11)
- Annual liquidity controls: Amihud illiquidity, Pastor-Stambaugh gamma, Hasbrouck Gibbs effective cost (one-year lagged), 1963-2003. _(construction, design_choice)_ #mech/liquidity_flows
  > we use three annual measures of liquidity to control for the effects of liquidity: the Amihud (2002) illiquidity measure (illiq), the Pastor and Stambaugh (2003) reversal measure
  exact_rule: add lagged annual illiq, gamma, Gibbs as regressors · data_needed: Hasbrouck website liquidity estimates (Gibbs, Amihud, gamma) · exhibit: Table 4
  ^QP10-C11-1
- Monthly liquidity from TAQ, January 1993-December 2003: proportional effective spread and proportional quoted spread, with lag and change terms. _(construction, design_choice)_ #mech/liquidity_flows
  > we construct two additional monthly liquidity measures based on the Trades and Quotes (TAQ) database.
  exact_rule: PESPR = 2|Pt-PM|/PM; PQSPR = (PA-PB)/PM; daily average per stock, monthly average of daily; include lagged level and monthly change · data_needed: TAQ trades and quotes 1993-2003 · exhibit: equation (8), Table 4
  ^QP10-C11-2
- Same Fama-MacBeth specification with liquidity controls added. _(construction, design_choice)_ #mech/research_method
  > cross-sectional regressions, controlling for various liquidity measures.
  exhibit: Table 4
  ^QP10-C11-3
- Annual liquidity measures miss monthly variation and cannot give monthly liquidity shocks. _(caveat, qualifier, Opus only)_ #mech/research_method
  > relations among return, volatility, and liquidity, one drawback is that they do not capture the monthly variation in volatility and stock returns
  ^QP10-C11-3b

### C12 (page 12)
- Annual-liquidity columns span 1963:07-2003:12; estimates with fewer than 50 observations are dropped; TAQ columns span 01:1993-12:2003. _(construction, design_choice)_ #mech/research_method
  > The sample period is from 1963:07 to 2003:12 for regressions using these measures.
  exact_rule: drop liquidity estimates with <50 observations · exhibit: Table 4 note
  ^QP10-C12-1
- With annual liquidity controls EIV stays 0.38-0.47 and UIV 0.93-0.97 (Gibbs: EIV 0.4661, UIV 0.9336; illiq: 0.3951/0.9721; gamma: 0.3770/0.9747). Monthly TAQ columns: EIV 0.21-0.32, UIV 0.54-0.59 (adj R2 0.091-0.134). _(result, evidence)_ #mech/liquidity_flows
  > TABLE 4. Cross-Sectional Regressions of Returns on EIV and UIV : Controlling for Liquidity Effects.
  reported_result: Table 4 (page image checked), Gibbs adj R2 0.108, illiq 0.114, gamma 0.110, PESPR 0.091/0.093, PQSPR 0.132/0.134; liquidity-level coefficients: Gibbs -0.4561 (t -5.48), illiq -0.0017 (t -2.85), gamma 0.6010 (t 0.69), PESPR(-1) -0.1090 (t -6.55), PQSPR(-1) -0.1062 (t -7.62) · exhibit: Table 4
  ^QP10-C12-2
- Table 4 monthly TAQ spreads (1993-2003): EIV and UIV stay significant with lagged spread and spread-change controls. _(result, evidence, Opus only)_ #mech/research_method
  > They are constructed using transaction-level data from the Trades and Quotes (TAQ) database, for the sample period from 01:1993 to 12:2003.
  reported_result: PESPR lag only: EIV 0.2840 (4.66), UIV 0.5438 (6.91), R2 0.091; PESPR lag+change: EIV 0.3218 (5.24), UIV 0.5595 (7.03), d -0.1098 (-5.13), lag -0.1090 (-6.55), R2 0.093. PQSPR lag only: EIV 0.2143 (3.36), UIV 0.5691 (6.58), R2 0.132; lag+change: EIV 0.2588 (3.98), UIV 0.5881 (6.77), d -0.0993 (-5.59), lag -0.1062 (-7.62), R2 0.134 · exhibit: Table 4
  ^QP10-C12-2b

### C13 (page 13)
- After liquidity controls EIV and UIV coefficients remain close to Table 3 and significant at 1% in the annual-measure models. _(robustness, conclusion)_ #mech/liquidity_flows
  > the positive relations between EIV and UIV with stock returns are not driven by liquidity effects.
  exhibit: Table 4
  ^QP10-C13-1
- Illiquidity measures carry negative coefficients once volatility is controlled, opposite of a liquidity premium; only gamma positive and insignificant. _(result, evidence)_ #mech/liquidity_flows
  > Table 4, however, shows that the coefficients for Gibbs and illiq measures are both negative, and statistically significant.
  reported_result: Gibbs -0.4561 (t -5.48), illiq -0.0017 (t -2.85), gamma 0.6010 (t 0.69) · exhibit: Table 4 · conditions: 1963:07-2003:12
  ^QP10-C13-2
- With TAQ spreads, 1993-2003, EIV about 0.28 and UIV about 0.55, smaller than the full-sample estimates; attributed to the shorter period. _(result, evidence)_ #mech/research_method
  > The magnitudes are comparable to earlier results (EIV : 0.28, UIV : 0.55), where the difference could be mainly due to the different sample period used for this test
  reported_result: EIV 0.28, UIV 0.55, 1993:01-2003:12 (PESPR model) · exhibit: Table 4
  ^QP10-C13-3
- Change in effective spread has negative coefficient (liquidity fall lowers same-month price) but lagged spread level is also negative, which contradicts a positive liquidity premium. _(result, evidence)_ #mech/liquidity_flows
  > The average coefficient for PESPR is negative, which is consistent with the idea that a decrease in liquidity increases the liquidity premium and hence lowers the contemporaneous stock price.
  reported_result: dPESPR -0.1098 (t -5.13), PESPR(-1) -0.1090 (t -6.55) · exhibit: Table 4
  ^QP10-C13-4
- Two follow-up tests: UIV-sorted portfolios and leverage test of the option effect. _(construction, design_choice)_ #mech/research_method
  > First, we construct UIV -sorted portfolios and observe how returns and alphas vary across the different portfolios.
  exhibit: Section IV
  ^QP10-C13-5

### C14 (page 14)
- Portfolio construction: monthly EIV quintiles, then UIV quintiles within each, pooling same-UIV quintiles across EIV groups, value-weighted, rebalanced monthly. _(construction, design_choice)_ #mech/research_method
  > Each month, we first sort common stocks (share codes 10 and 11) traded on NYSE/AMEX/NASDAQ into five quintiles based on their EIV rankings.
  exact_rule: sort on EIV into 5; within each sort on UIV into 5; combine across EIV groups; value-weight; monthly rebalance · exhibit: Table 5 note
  ^QP10-C14-1
- Value-weighted excess returns rise from 0.19% per month (Low UIV) to 0.76% (High UIV); H-L 0.58% (t 3.14). _(result, evidence)_ #mech/research_method
  > excess returns increase from 0.19% per month for the low-UIV quintile to 0.76% for the high-UIV quintile
  reported_result: Table 5, 1963:07-2003:12, value-weighted: Low 0.0019 (0.98), Q2 0.0044 (2.13), Q3 0.0054 (2.53), Q4 0.0066 (2.81), High 0.0076 (2.62), H-L 0.0058 (3.14); gross, no costs · exhibit: Table 5
  ^QP10-C14-2
- Alphas rise with UIV: H-L CAPM alpha 0.39% per month (t 2.39), FF3 0.39% (t 2.33), FF3+MOM 0.39% (t 2.28); Low-UIV alphas are significantly negative (-0.20%, -0.26%, -0.22%). _(result, evidence)_ #mech/research_method
  > alphas also register significant increases across the UIV portfolios
  reported_result: Table 5 H-L alpha 0.0039 for CAPM (2.39), FF-3 (2.33), FF3+MOM (2.28); Low UIV alpha -0.0020 (-3.09), -0.0026 (-3.85), -0.0022 (-3.30); High UIV alpha 0.0019 (1.55), 0.0013 (1.07), 0.0016 (1.32) · exhibit: Table 5
  ^QP10-C14-3
- Sorting on same-month UIV uses information not available ex ante, so Table 5 is explanatory, not a tradable strategy. _(caveat, qualifier)_ #mech/research_method
  > Note that the portfolios are constructed after the realizations for UIV (and hence returns) are known. Therefore, one cannot construct a profitable trading strategy to exploit the results in this table.
  exhibit: Table 5 note · conditions: UIV known only after month ends
  ^QP10-C14-4
- Authors annualize the 0.58% monthly high-minus-low gap to roughly 7% per year. _(result, evidence)_ #mech/research_method
  > a difference of 0.58% per month, or around 7% a year.
  reported_result: 0.58%/month ~ 7%/year (excess return H-L) · exhibit: Table 5
  ^QP10-C14-5
- The five UIV portfolios hold different UIVs but similar EIV spread; measured by excess return and CAPM, FF3 and FF3+MOM alphas; rebalanced monthly. _(construction, design_choice, Opus only)_ #mech/research_method
  > Then, we aggregate all the stocks in the same UIV portfolio across all the five EIV quintiles.
  exhibit: Table 5
  ^QP10-C14-3b

### C15 (page 15)
- FF3+MOM alpha moves from -0.22% to +0.16% monthly across UIV quintiles, about 4.6% a year, significant at 5%. _(result, evidence)_ #mech/research_method
  > for the FF-3 + MOM model, the alphas increase from approximately −0.22% per month for the low-UIV portfolio to approximately 0.16% per month for the high-UIV portfolio, about a 4.6% difference in annual returns.
  reported_result: Table 5 FF3+MOM alpha -0.22% to 0.16% per month (~4.6%/yr), significant at 5% · exhibit: Table 5
  ^QP10-C15-1
- Authors stress UIV sorts do not imply a profitable strategy but show UIV is a suitable control for unexpected returns. _(caveat, qualifier)_ #mech/research_method
  > the portfolio sorting is based on contemporaneous information (UIV ), and therefore the observed pattern does not imply a profitable investment strategy.
  exhibit: Section IV
  ^QP10-C15-2
- Leverage test setup: firms sorted into five leverage quintiles (D1..D5) and UIV interacted with each dummy to compare strength of the UIV-return link. _(construction, design_choice)_ #mech/research_method
  > we first divide the firms into five quintile portfolios sorted by leverage and assign five dummy variables
  exact_rule: monthly sort on previous-month leverage into 5 groups; dummies D1..D5 · exhibit: Equation (10)
  ^QP10-C15-3
- UIV is standardized per firm by dividing monthly demeaned UIV by its own time-series standard deviation so coefficients are comparable across leverage quintiles; returns and EIV are standardized likewise. _(construction, design_choice)_ #mech/research_method
  > we standardize the UIV variable so that the variance of the UIV variable is equal across all quintiles.
  exact_rule: UIVS_{i,m} = UIV_{i,m} / SD(UIV_{i,.}), with UIV demeaned monthly; RS and EIVS standardized similarly · exhibit: Equation (9)
  ^QP10-C15-4

### C16 (page 16)
- Eq 10 regresses standardized return on EIVS, size, btm and UIVS interacted with the five leverage dummies; each coefficient is the return effect of a one-sd UIV shock in that leverage quintile. _(construction, design_choice)_ #mech/research_method
  > We interpret the coefficient ϕ j (j = 4, . . . , 8) as the effect on returns, of a 1 standard deviation realization in the UIV .
  exact_rule: RS = f0 + f1 EIVS + f2 Size + f3 btm + sum_{j=1..5} f_{3+j} D_j*UIVS + eta, monthly cross-section · exhibit: Equation (10)
  ^QP10-C16-1
- UIV effect rises from 0.14 (lowest leverage quintile) to 0.21 (highest); the high-minus-low difference is 0.0695 with Newey-West t 6.92. _(result, evidence)_ #mech/risk_premium
  > The means of the coefficients ϕ j increase monotonically from 0.14 to 0.21 as j increases from 4 to 8
  reported_result: Table 6 Panel A (1963:07-2003:12): UIVS1 0.1402 (8.74), UIVS2 0.1611, UIVS3 0.1878, UIVS4 0.1911, UIVS5 0.2096 (15.68), DIV 0.0695 (6.92), adj R2 0.095, EIVS 0.0467 (12.79) · exhibit: Table 6 (page image checked)
  ^QP10-C16-2
- Subperiod check addresses Campbell et al.'s rising idiosyncratic volatility trend; the monotonic leverage pattern holds in both halves. Table 6 labels Panel C as 1984:01-2003:12, inconsistent with the text's January 1985. _(robustness, evidence)_ #mech/research_method
  > we divide the sample into two subperiods: July 1963 to December 1984 and January 1985 to December 2003.
  reported_result: Panel B 1963:07-1984:12: UIVS 0.1685->0.2498, DIV 0.0813 (6.26), R2 0.115; Panel C: UIVS 0.1059->0.1596, DIV 0.0537 (3.76), R2 0.070 · exhibit: Table 6 Panels B and C · conditions: low-volatility early period and high-volatility later period
  ^QP10-C16-3
- Reconciliation: the option effect (price jump on UIV) does not imply a negative EIV-future return relation, since the asset-level premium rises with volatility. _(mechanism, conclusion)_ #mech/risk_premium
  > The significant positive coefficient for EIV suggests that idiosyncratic volatility has a positive effect on the premium of the firm’s total assets, and this effect dominates the negative effect of volatility on equity beta.
  ^QP10-C16-4
- High-minus-low leverage UIV slope difference is significant. _(result, evidence, Opus only)_ #mech/new
  > statistic of 6.92), implying that the relation for firms in the high-leverage quintile is
  reported_result: DIV 0.0695, NW t 6.92 (full sample) · exhibit: Table 6
  ^QP10-C16-3b
- Because idiosyncratic volatility trended up from 1962 to 1997 (Campbell et al. 2001), the leverage test is repeated in two sub-periods. _(citation, context, Opus only)_ #mech/research_method
  > Campbell et al. (2001) document a rising trend in individual stock
  ^QP10-C16-4b
- Johnson (2004): with a constant asset premium, higher volatility lowers equity beta and expected equity return. _(citation, premise, Opus only)_ #mech/risk_premium
  > it can be shown that an increase in current volatility of the firm leads to lower equity beta
  ^QP10-C16-6b

### C17 (page 17)
- Table 6 DIV is the UIVS5 minus UIVS1 coefficient with a test of equality: Panel A 0.0695 (t 6.92), Panel B 0.0813 (6.26), Panel C 0.0537 (3.76). Other coefficients Panel A: ret-1 -0.4365, ret-2-12 0.0463, btm 0.0526, size -0.0025. _(result, evidence)_ #mech/risk_premium
  > The column for DIV reports the difference between the coefficients of UIVS 5 and UIVS 1 and the result for the null hypothesis that both coefficients are equal.
  reported_result: Table 6: DIV 0.0695/0.0813/0.0537; UIVS1-5 in A 0.1402,0.1611,0.1878,0.1911,0.2096; B 0.1685,0.2042,0.2292,0.2313,0.2498; C 0.1059,0.1127,0.1393,0.1439,0.1596 · exhibit: Table 6 (page image checked)
  ^QP10-C17-1
- Table 6 note swaps the SIC ranges (financials labeled 4900-4999, utilities 6000-6999) relative to the data section, a labelling error. _(caveat, qualifier)_ #mech/research_method
  > We exclude financial firms (SIC codes 4900–4999) and utility firms (SIC codes 6000–6999).
  exhibit: Table 6 note
  ^QP10-C17-2
- Leverage quintiles use the previous month's leverage ranking. _(construction, design_choice, Opus only)_ #mech/research_method
  > into quintiles based on their financial leverage rankings from the previous month
  exact_rule: leverage quintile from LEV at m-1 · exhibit: Table 6 note
  ^QP10-C17-3b

### C18 (page 18)
- Omitting UIV leads to wrong inference on EIV: EIV is positively related to expected returns and UIV to unexpected returns. _(mechanism, conclusion)_ #mech/risk_premium
  > Excluding UIV from the analysis leads to incorrect conclusions about the role of expected idiosyncratic volatilities.
  ^QP10-C18-1
- Conclusion repeats that Ang et al.'s negative realized return result addresses a different relation. _(caveat, qualifier)_ #mech/research_method
  > Because Ang et al. do not test the relation between the expected return and expected volatility (Ang et al. 2009), their finding is not necessarily comparable to ours.
  exhibit: Section V
  ^QP10-C18-2
- The authors attribute the contrast with Ang et al. and consistency with Fu and Spiegel-Wang to the volatility decomposition, not the EGARCH choice. _(mechanism, conclusion)_ #mech/research_method
  > we argue that the difference comes from the decomposition of the idiosyncratic volatility (estimated from daily returns) into EIV and UIV, and then using UIV to control for unexpected returns.
  ^QP10-C18-3
- Leverage-monotonic UIV coefficients are taken as support that UIV matters through the option effect. _(result, conclusion)_ #mech/risk_premium
  > We group firms into five leverage quintiles. We then standardize UIV and show that the magnitude of the regression coefficients for the standardized UIV increases monotonically as leverage increases.
  reported_result: Table 6: 0.14 -> 0.21; high-low diff t 6.92 · exhibit: Table 6
  ^QP10-C18-4
- Conclusion claims monotone return/alpha increase from low to high UIV for both portfolio types (only value-weighted reported). _(result, evidence, Opus only)_ #mech/new
  > We show that for both types of portfolios, the average returns, as well as the Jensen’s alphas
  exhibit: Table 5
  ^QP10-C18-3b
- UIV's importance comes from the option effect (leverage-monotone slopes). _(result, conclusion, Opus only)_ #mech/new
  > this importance stems from the consequences of the option
  ^QP10-C18-4b

### C19 (page 19)
- Appendix: with realized return = expected + unexpected return and noise dominated by unexpected return, the EIV coefficient has huge standard error, and any sample correlation of EIV with unexpected return biases it (downward if negative). _(mechanism, mechanism_step)_ #mech/research_method
  > However, because the noise in UR i,m dominates ER i,m (these are monthly returns for individual stocks), the standard error for the estimate of ξ 1 is very large.
  exhibit: Appendix (A2)
  ^QP10-C19-1
- If a variable X is correlated with unexpected return, adding it (A3) absorbs the noise and corrects bias in the EIV coefficient. _(mechanism, mechanism_step)_ #mech/research_method
  > Suppose we can find a variable that is perfectly correlated with UR i,m (call this variable X i,m ).
  exact_rule: ER+UR = x0 + x1 EIV + x2 X + v, X proxy for unexpected return · exhibit: Appendix (A3)
  ^QP10-C19-2
- Final claim: decomposing idiosyncratic volatility reveals both components significantly related to returns in different ways. _(mechanism, conclusion)_ #mech/risk_premium
  > With this decomposition, we are able to show that both components are
  ^QP10-C19-3
- Expected returns are unobservable and no model estimates them well, so realized returns (ER + UR) are used as the dependent variable. _(mechanism, premise, Opus only)_ #mech/research_method
  > we cannot observe, nor is there a reasonably accurate model to derive
  ^QP10-C19-1b
- Fix: add a right-hand-side variable X correlated with UR (eq. A3). _(construction, design_choice, Opus only)_ #mech/research_method
  > we propose that a control variable be inserted into the right-hand side of the regression
  exact_rule: R = c + x1 EIV + x2 X + e, X highly correlated with UR · exhibit: Appendix eq. A3
  ^QP10-C19-3b

### C20 (page 20)
- Adding the control reduces bias in the EIV coefficient and cuts regression error variance, lowering its standard error. _(mechanism, mechanism_step)_ #mech/research_method
  > First, the effect of the sample correlation between UR i,m and EIV i,m is mitigated because UR i,m and X i,m now have a much stronger correlation.
  exhibit: Appendix
  ^QP10-C20-1
- UIV need not be orthogonal to EIV; the key requirement is high correlation with unexpected return, and nonzero UIV-EIV correlation is expected because unexpected return itself correlates with EIV. _(caveat, qualifier)_ #mech/research_method
  > It need not necessarily be orthogonal to EIV in the cross-section.
  exhibit: Appendix
  ^QP10-C20-2
- An imperfect proxy only partly corrects the bias; the validity of UIV as control relies on its correlation with unexpected return, which is never measured. _(caveat, qualifier)_ #mech/research_method
  > In the event that a perfectly correlated variable cannot be found, using X i,m , a variable possessing a high correlation with UR i,m can still alleviate the problem to a large extent.
  exhibit: Appendix
  ^QP10-C20-3

