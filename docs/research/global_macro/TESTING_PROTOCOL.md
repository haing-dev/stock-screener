# Global Macro Book: statistical adoption protocol (pre-registered 2026-11-01)

Replaces the rule "adopt a change only if it raises net Sharpe in both 1990-2010 and 1975-89". That rule is a
two-coin sign test: it ignores how large and how noisy a difference is, and it can never pass a change whose data
start after 1989. Code: `gm/protocol.py` (tests in `gm/stats.py`). Written and committed BEFORE any batch below is run.

## 1. What is compared
- **Incumbent:** the current candidate config (`gm/config.py`, CANDIDATE = gm-2.0 at batch 1).
- **Challenger:** the incumbent with exactly one pre-registered change.
- **Returns:** monthly net returns of the whole book (costs, rolls, borrow included), 10% vol target.
- **Window:** design months only (1975-01 .. 2010-12; the holdout never enters), restricted to months where the
  challenger's new input exists. A window shorter than 120 months = "insufficient data", not tested.

## 2. Tests (all must pass)
| # | Test | Statistic | Pass if |
|---|---|---|---|
| 1 | Superiority | Paired stationary bootstrap of the Sharpe difference (Politis-Romano; mean block 6 months; 10,000 resamples; seed 20261101). One-sided p for H0: dSR <= 0, from the centred bootstrap distribution | Holm-adjusted p < 0.05 across the batch |
| 2 | Economic size | Point estimate dSR (annualised) on the window | dSR >= 0.05 |
| 3 | Non-inferiority per era | For each era (1975-89, 1990-2010) with >= 60 months of challenger data: one-sided 95% lower bound of dSR from the same bootstrap. An era with no new data must give identical returns (max abs difference < 1e-10) and passes | lower bound > -0.10 |
| 4 | Cost robustness | dSR at twice the costs on the window | > 0 |
| 5 | Tail (no "many small gains, rare big loss" profile; Harding 2002, Stine 2009) | Maximum drawdown and worst month on the window (both books at the same vol target) | max fall not worse by more than 2 points and worst month not worse by more than 1 point |

Reported but not decisive: Newey-West (6 lags) alpha t-stat of the challenger-minus-incumbent return against the
incumbent (the Foster-Stine value-add test); skew; Lo (2002) autocorrelation-adjusted Sharpe; the five-state equity
"smile". The bootstrap resamples whole months (all markets together), never single markets, because the 62 markets
are dependent.

## 3. Multiple testing and the trial count
- A **batch** is the list of challengers registered in section 5 before it runs. Holm's step-down correction is
  applied over every challenger in the batch, including any that fail to build (p = 1).
- Every challenger is logged in `gm/trials.csv`, so the whole-book deflated Sharpe counts it.
- A rejected idea is not re-run with tweaks inside the same batch. A changed version needs a new batch entry.
- Winners of a batch are combined into one config and re-tested once against the incumbent (tests 2-5 only; no new
  multiplicity). If the combination fails, winners are added one at a time in order of p-value, keeping each only
  if the combination still passes.

## 4. Why these choices
- Paired bootstrap: incumbent and challenger share most positions, so their returns are highly correlated. Pairing
  uses that, and the block bootstrap keeps autocorrelation and volatility clusters (Ledoit and Wolf 2008).
- Holm: controls the chance of any false adoption in a batch at 5% without the overly strict Bonferroni.
- dSR >= 0.05: below this a gain is within cost-estimate error and not worth extra complexity.
- Non-inferiority margin 0.10: about a third of the bootstrap standard error of a 15-year book Sharpe; a change may
  be neutral in one era but must not clearly hurt it.
- Data that start after 1989 (short-rate futures, forecasts, data surprises) are tested on their own window; the
  earlier era is then identical by construction, so test 3 cannot block them, while tests 1-2 still must pass.

## 5. Batches
### Batch 0: re-test of the gm-2.0 adoptions under this protocol (incumbent gm-1.2)
- B0.1 hybrid volatility.
- B0.2 family shares trend 45 / carry 25 / value 15 / econ 15 (with hybrid volatility, vs hybrid alone).
Consistency rule: a change that fails is reverted in the incumbent before batch 1.

### Batch 1: free data (from the quant-papers review, project doc quant_papers_review_2026-11-01.md)
- E1 economic trend as theme x asset-class portfolios (each block scaled to unit vol, themes equal risk inside the
  family; AQR Economic Trend 2023), keeping the tanh(z/2) scores.
- S1 US 3-month short-rate market (synthetic: -0.25 x monthly change in the month-end 3-month Treasury bill rate,
  FRED DTB3), traded by trend and economic trend with the US short-bond signals; counted at 0.25/1.9 of its notional
  in the gross cap (2-year equivalent). Other countries wait for Bloomberg futures (monthly-average OECD rates would
  create false trends).
- V1 bond value composite: average of the cross-sectional ranks of the real yield and of the 5-year rise in the
  10-year yield (Asness, Moskowitz and Pedersen 2013, Table I Panel C).
- V2 currency value skipping the latest 12 months (real change from t-60 to t-12), so value does not lean against
  the trend window.
- C1 bond carry per unit of duration in the cross-sectional half (2y 1.9, 5y 4.6, 10y 8.5, 30y 18), so long bonds are
  not favoured by construction (Baz et al., Man Group).

Diagnostics run with batch 1 (no adoption decision; they audit the 1.63 design Sharpe):
- trend family alone vs AQR's published TSMOM factor, 1990-2010;
- Lo-adjusted Sharpe, Sortino, skew, worst month, compound growth; rolling 36-month volatility vs the 10% target;
- Sharpe with each of the five biggest-contributing markets removed, and without 2008;
- five-state smile vs world equities; 1987 crash by family and asset class.

Considered and not registered (six-paper review, 2026-11-01): yield-curve level and whole-curve slope mean reversion
(lose to plain bonds in Chua-Koh-Ramaswamy 2006; slope reversion is already carry); curvature mean reversion (decayed
after about 1990 in the same paper); Kalman forward-curve forecasts (no better than a random walk, Chua-Ramaswamy-Stine
2008).

### Batch 2: Bloomberg and zero-curve data (final list registered when the data arrive, before testing)
Planned: short-rate futures (contracts about 1 year forward) for US, UK, euro, Canada, Australia, Japan with trend,
economic trend and carry (implied minus spot 3m rate); bond carry with roll-down from zero curves (Fed GSW, Bank of
England, Bundesbank, Japan MoF; pre-1990 coverage allows both eras); commodity carry from the 2nd/3rd or 12-month slope
with same-calendar-month spreads for seasonal energy and grains; equity value composite; growth on first-release
data; bond futures returns vs yield-built returns (data audit).

## 6. Note on the holdout criteria
The standard error of an annual Sharpe estimated from 15 years is about 0.27 at a true Sharpe of 0.5 (Lo 2002). The
holdout pass mark (net Sharpe >= 0.3) is therefore about one standard error below a realistic live Sharpe: it screens
out a broken book, it does not prove skill.
