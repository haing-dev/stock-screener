# Validation protocol (pre-registered 2026-10-20)

Goal: find out, with evidence that doesn't depend on the owner or on an AI assistant, whether each of the 14 screens
picks better stocks, and keep, fix, replace or drop each one. This file is fixed before any backtest is run. A
change to it, or to the rules it freezes, is logged in `validation/CHANGES.md` and restarts the forward clock.

## 1. What is frozen
- The screens as of version 2.8.0: every gate, threshold and rule-bearing config value.
- `validation/freeze.json` holds two fingerprints (`python -m qs.freeze`):
  - **rules**: canonical JSON of every gate and its threshold;
  - **behavior**: each screen's class for the 38 real SEC samples in `tests/real_samples`.
- Every validation run prints `python -m qs.freeze --check`. Results computed with code that doesn't match are
  labelled **MODIFIED** and don't count as evidence for the frozen screens.
- A rule change is tested as a *variant*: logged in `CHANGES.md` with its own fingerprints and evaluated on months
  after it was logged. The frozen version stays the reference.
- The tag `prereg-2026-10-20` marks the commit. The validation workflow also records an external OpenTimestamps
  proof of `freeze.json` (`validation/freeze.json.ots`).

## 2. Data (point in time)
- **Fundamentals.** SEC XBRL companyfacts (nightly bulk file) for every company the price universe maps to,
  including companies that have since delisted.
  - A fact is used at date *d* only if its filing date is before *d*.
  - When a period was restated, the value known at *d* is used (the latest filed before *d*).
  - Quarterly (10-Q) facts are kept from 2009 on.
- **Filing events** (Form 10, S-1/F-1/424B4, 8-K items) come from the full submissions history (bulk file,
  including the older pages), filtered to filings before *d*.
- **Prices.** Massive grouped daily bars, unadjusted (as printed), for the last trading day of each month and the
  first trading day of the next.
  - Corporate actions come from Massive's split and dividend lists.
  - Ticker to CIK is mapped through Massive's ticker reference, including inactive tickers. A ticker that was
    reused is resolved by its delisting date.
  - History length depends on the Massive plan: Basic 2 years, Starter 5, Developer 10, Advanced 20+.
- **Factors.** Kenneth French data library, monthly: Fama-French 5 factors and momentum (UMD).
- **Known limits.**
  - XBRL covers about 2009-11 onward, so screens needing 8-10 years of history can pass only from about 2015-17.
  - The 2021-23 margin-change inputs and the recession tests use fixed calendar windows. Before those years they
    count as missing data, and the rate of missing data per gate is reported.
  - FX uses the static config rates.
  - 13F, insider and summary data play no part in the rules, so they are not reconstructed.

## 3. Formation, holding, costs
- **Formation.** Day *d* is the last trading day of each month. Information is filings before *d*; price rules use
  the close on *d* and, as live, the 12-month high from month-end closes. Evaluation runs the live code
  (`metrics_for`, `build_ctx`, industry cycle, `valuation.value`, `Screen.evaluate`) unchanged.
- **Universe.** NYSE and Nasdaq common stocks and ADRs with a price on *d* and a CIK with XBRL facts. Each
  screen's own industry universe applies on top, exactly as live.
- **Entry and exit.** Entry is the open of the next trading day (*d*+1, the first trading day of the next month).
  The exit is the open of the following month's first trading day.
  - Returns include dividends with an ex-date inside the holding period, and are adjusted for splits.
  - Holding horizons: 1 month (rebalanced monthly, the primary test), plus 3 and 12 months as overlapping cohorts
    (Jegadeesh-Titman).
- **Delisting.** A holding with no exit price takes the last daily close from Massive's per-ticker bars.
  - If that is unavailable, it takes the last grid price minus 30% (Shumway 1997).
  - A sensitivity run uses 0%.
- **Costs.** 50 bp per side on turnover.
- **Portfolios per screen.**
  - **P1 (primary):** PASS, including starred passes, equal-weighted.
  - **P2:** PASS excluding starred passes.
  - **P3:** value-weighted P1.
  - **P4:** near misses (NEAR).
  - A month with fewer than 5 names holds the screen's own universe for that month, which counts as zero excess
    return. The share of such months is reported.

## 4. Benchmarks and baselines
- **Own universe.** Every company the screen evaluated at *d*, equal- and value-weighted.
- **Characteristic-matched** (Daniel-Grinblatt-Titman-Wermers style). Each stock's return is taken minus the
  equal-weighted return of its size × book-to-market × 12-1 momentum tercile cell (3×3×3) in the full universe.
- **Simple baselines** in the screen's own universe, holding the same number of names as the screen that month
  (top-ranked):
  - Piotroski F-score (2000);
  - Magic Formula (Greenblatt), the combined rank of EBIT/EV and EBIT/tangible capital;
  - gross profitability, gross profit / assets (Novy-Marx 2013).
- **Placebo.** 10,000 random portfolios per screen and month. Each holds the same number of names, drawn from the
  same size tercile × SIC division cells as the actual picks.

## 5. Statistics
- **Alpha.** Monthly excess return over the risk-free rate, regressed on FF5 + UMD. Newey-West t-statistic with
  lag floor(4(T/100)^(2/9)). Also reported: the long-short against the own universe, and against the
  characteristic-matched benchmark.
- **IC.** Each month, the Spearman correlation between the share of rules met and the next-month return, within
  the screen's universe. Mean IC and its t-statistic over the months.
- **Overfitting.**
  - Deflated Sharpe Ratio (Bailey & López de Prado 2014), with N = every portfolio variant evaluated.
  - PBO by CSCV over the threshold grid, 16 blocks (Bailey et al. 2017).
  - White's Reality Check and Hansen's SPA across the 14 screens: P1 minus own universe, stationary bootstrap
    with 2,000 draws and mean block length 6.
- **Robustness.**
  - Threshold grid s ∈ {−0.3, −0.2, −0.1, 0, +0.1, +0.2, +0.3}, applied to every numeric threshold (looser to
    stricter).
  - Leave-one-gate-out: each gate's marginal contribution to the alpha.
  - Results for the first and second halves of the sample.
- **Red Flags.** AUC of membership, and of the number of flags, for a bad outcome within 12 months: a fall of 50%
  or more from the formation price at a later grid date, or a delisting at a loss. Compared with Altman Z''
  (lower = worse) and Beneish M (higher = worse) on the same companies.

## 6. Verdicts (mechanical, per screen)
| Verdict | Condition |
| --- | --- |
| **too little history** | fewer than 36 monthly observations, or fewer than 5 names in more than half the months. |
| **edge** | P1 FF5+UMD alpha t ≥ 3.0 (Harvey-Liu-Zhu 2016); same sign in both halves; DSR ≥ 0.95; PBO ≤ 0.20; above the 95th placebo percentile; alpha above every baseline with difference t ≥ 2 (paired monthly returns). |
| **promising** | alpha t ≥ 2.0 and above the 90th placebo percentile, but not every *edge* condition. |
| **replace with baseline** | a baseline's alpha is higher with difference t ≥ 2. |
| **harmful** | alpha t ≤ −2.0. |
| **no evidence** | anything else. |
| **Red Flags: works** | P1 alpha t ≤ −2.0, AUC ≥ 0.70, and AUC above both Altman Z'' and Beneish M. |

The thresholds are the proposals of the 16 Oct 2026 independent assessment, except Harvey-Liu-Zhu's t ≥ 3.

## 7. Forward record (the true out-of-sample test)
- From 2026-10-20, every Screen and Daily run appends its lists to the append-only branch `history`. Each entry
  carries the date, code SHA, config hash, the freeze check, and the PASS / starred / NEAR CIKs and tickers per
  screen.
- The monthly validation run scores the forward record with the same rules as section 6, using only months after
  2026-10-20. With an information ratio of 0.5, t = 2 needs about 16 years. Until 36 forward months exist, the
  forward record serves to catch implementation errors and gross failure (monthly IC, t ≥ 2 over 36 months or more).

## 8. Independent checks
| Check | Method | Pass |
| --- | --- | --- |
| Data reconciliation | 300 random firm-years, stratified by screen. Our revenue, operating income, operating cash flow, capex, total debt and diluted shares, against SEC Financial Statement Data Sets for the same filing (CSV with filing links, for a third party to recheck). | ≥ 95% of values within 2%; ≥ 98% of gate outcomes agree in the human recheck |
| Star audit | 50 starred passes, blinded (CSV); a reviewer checks the missing inputs in the filing. | ≥ 90% still pass with full data; otherwise stars become CHECK (the owner decides) |
| Re-implementation | An agent that never saw the code implements one screen from the written rules and raw companyfacts. | Jaccard of the pass lists ≥ 0.9, with every difference explained |
| Style fidelity | The quoted managers' latest 13F holdings, run through "their" screens. | PASS + NEAR rate ≥ 3 × the screen's universe rate |

## 9. Outputs
- The validation workflow writes `validation/out/` to the branch `validation`:
  - per-month lists and returns (CSV.gz);
  - `stats.json`;
  - `report.md`, with each verdict next to the numbers behind it;
  - the audit CSVs.
- Raw outputs are committed so anyone can recompute every number.
