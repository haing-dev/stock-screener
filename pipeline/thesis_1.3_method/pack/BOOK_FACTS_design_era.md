# Book facts, design months 1975-2010 only (verbatim from repo result files; written by the orchestrator, 2026-11-15)

Nothing here uses 2011-2026 data. Section 4 of the statistical audit is a simulation: design-era returns, block-bootstrapped, rescaled to an assumed true Sharpe and cut to the holdout's length (189 months); the correlation criterion is assumed met. The book: about 61 distinct markets (equity indexes, government bonds, short rates, currencies, commodities), monthly, four signal families (trend, carry, value, economic trend), 10% volatility target on the whole book (trailing 36-month realised volatility of the unscaled book, lagged), 5x cap on total face value, per-market cap. BASE = gm-1.2.1 (live). CANDIDATE = gm-2.0.1 (hybrid volatility + family shares 45/25/15/15), not frozen. These numbers are repo results, not ground truth about QP13; cite them as '(repo result, design era)'.

## 1. docs/research/global_macro/protocol_batch0.md

# Protocol results: batch0 (2026-11-01 20:25 UTC)

Rules: TESTING_PROTOCOL.md. Window = design months 1975-01..2010-12 where the challenger has data. Sharpe = annualised, net of costs. dSR = challenger minus incumbent.

| Challenger | Window | SR inc | SR cha | dSR | boot SE | p | Holm p | dSR 2x cost | max fall inc / cha | 1975-89 dSR (95% LB) | 1990-2010 dSR (95% LB) | alpha t | Adopt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B0.1 hybrid volatility | 1975-01..2010-12 | 1.24 | 1.35 | +0.118 | 0.039 | 0.0018 | 0.0036 | +0.100 | -20.5% / -20.3% | +0.13 (+0.03) | +0.10 (+0.01) | 3.8 | YES |
| B0.2 family shares 45/25/15/15 | 1975-01..2010-12 | 1.35 | 1.46 | +0.111 | 0.063 | 0.0367 | 0.0367 | +0.109 | -20.3% / -16.8% | +0.17 (+0.02) | +0.05 (-0.09) | 3.1 | YES |

Failed checks:
- B0.1 hybrid volatility: none
- B0.2 family shares 45/25/15/15: none

## 2. docs/research/global_macro/protocol_batch1.md

# Protocol results: batch1 (2026-11-01 20:26 UTC)

Rules: TESTING_PROTOCOL.md. Window = design months 1975-01..2010-12 where the challenger has data. Sharpe = annualised, net of costs. dSR = challenger minus incumbent.

| Challenger | Window | SR inc | SR cha | dSR | boot SE | p | Holm p | dSR 2x cost | max fall inc / cha | 1975-89 dSR (95% LB) | 1990-2010 dSR (95% LB) | alpha t | Adopt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E1 econ theme blocks | 1975-01..2010-12 | 1.46 | 1.45 | -0.009 | 0.036 | 0.6168 | 1.0000 | -0.009 | -16.8% / -19.5% | +0.02 (-0.05) | -0.04 (-0.12) | 0.3 | no |
| S1 US 3m short-rate market | 1975-01..2010-12 | 1.46 | 1.45 | -0.015 | 0.013 | 0.8880 | 1.0000 | -0.037 | -16.8% / -17.1% | -0.05 (-0.09) | +0.01 (-0.01) | -0.9 | no |
| V1 bond value composite | 1975-01..2010-12 | 1.46 | 1.47 | +0.003 | 0.014 | 0.4308 | 1.0000 | +0.002 | -16.8% / -16.6% | -0.00 (-0.05) | +0.01 (-0.02) | 0.5 | no |
| V2 FX value skip 12m | 1975-01..2010-12 | 1.46 | 1.48 | +0.014 | 0.015 | 0.1734 | 0.8669 | +0.014 | -16.8% / -17.1% | +0.03 (-0.00) | +0.00 (-0.03) | 1.2 | no |
| C1 bond carry per duration | 1975-01..2010-12 | 1.46 | 1.47 | +0.005 | 0.014 | 0.3760 | 1.0000 | +0.002 | -16.8% / -16.9% | +0.03 (-0.02) | -0.02 (-0.04) | 0.6 | no |

Failed checks:
- E1 econ theme blocks: 1 superiority (Holm p<0.05), 2 size (dSR>=0.05), 3 non-inferior in each era, 4 dSR>0 at 2x costs, 5 tail: max fall not >2pt, worst month not >1pt worse
- S1 US 3m short-rate market: 1 superiority (Holm p<0.05), 2 size (dSR>=0.05), 4 dSR>0 at 2x costs
- V1 bond value composite: 1 superiority (Holm p<0.05), 2 size (dSR>=0.05)
- V2 FX value skip 12m: 1 superiority (Holm p<0.05), 2 size (dSR>=0.05)
- C1 bond carry per duration: 1 superiority (Holm p<0.05), 2 size (dSR>=0.05)

## 3. docs/research/global_macro/protocol_diagnostics.md

# Diagnostics for the gm-2.0 candidate (design periods only)

- 1975..1989: SR 1.22, Lo-adjusted SR 1.32, skew -0.65, first-order autocorrelation 0.09
  Sortino 2.07, worst month -14.7%, compound growth 11.6%/yr, rolling 36m vol min/median/max 4.9/10.3/13.3%
- 1990..2010: SR 1.63, Lo-adjusted SR 1.49, skew 0.26, first-order autocorrelation 0.12
  Sortino 3.54, worst month -9.8%, compound growth 17.1%/yr, rolling 36m vol min/median/max 6.1/9.5/14.2%

Sharpe 1975-2010 (net) with a top-contributing market removed (positions zeroed, costs kept):
- full book: 1.46; without 2008: 1.44
- without fx_krw (contributed 42% of capital in total): 1.35
- without st_jp_2y (contributed 35% of capital in total): 1.37
- without cm_wti (contributed 28% of capital in total): 1.40
- without bd_us_30y (contributed 28% of capital in total): 1.48
- without cm_aqr_ew (contributed 25% of capital in total): 1.46

Trend family (unit-vol blocks, equal class weight, gross) vs AQR TSMOM factor, 1990-2010 (252 months): our SR 1.22, AQR SR 1.34, correlation 0.66
- smile 1975..1989 (book return by world-equity quintile, %/yr): {1: -1.0, 2: 7.5, 3: 18.0, 4: 8.8, 5: 24.2}
- smile 1990..2010 (book return by world-equity quintile, %/yr): {1: 18.1, 2: 9.5, 3: 14.7, 4: 25.0, 5: 14.4}

1987 crash (Oct-Nov), gross contribution by family x class (percent of capital):
- trend: {'EQ': -6.38, 'FI': -2.06, 'FX': 0.71, 'CM': 1.18}
- econ: {'EQ': -1.58, 'FI': -1.71, 'FX': -1.04, 'CM': -0.39}
- carry: {'EQ': 0.0, 'FI': 0.92, 'FX': -0.05, 'CM': -0.29}
- value: {'EQ': -0.71, 'FI': -0.02, 'FX': -1.04, 'CM': 0.0}

## 4. docs/research/global_macro/stats_audit_2026-11-02.md

# Statistical audit of the Global Macro Book build (design months 1975-2010 only)

## 1. Bootstrap block length

| Mean block (months) | gm-2.0 SR 90% interval 1975-2010 | B0.1 hybrid vol dSR p (lb95) | B0.2 shares dSR p (lb95) |
|---|---|---|---|
| 3 | 1.17 - 1.79 | +0.118 p 0.0022 (+0.053) | +0.111 p 0.0340 (+0.009) |
| 6 | 1.17 - 1.79 | +0.118 p 0.0012 (+0.058) | +0.111 p 0.0397 (+0.008) |
| 12 | 1.18 - 1.76 | +0.118 p 0.0012 (+0.058) | +0.111 p 0.0340 (+0.011) |
| 24 | 1.22 - 1.74 | +0.118 p 0.0005 (+0.062) | +0.111 p 0.0377 (+0.009) |

Analytic standard error of the 1975-2010 Sharpe (Lo 2002, iid): 0.24 (SR 1.46 over 36 years).

## 2. Selection inflation and trial count

Logged 1990-2010 Sharpe ratios of 32 book variants: mean 1.45, sd 0.11, best 1.63.
- if 32 variants had been tried: expected best Sharpe from luck alone = mean + 2.10 x sd = selection inflation about 0.23
- if 100 variants had been tried: expected best Sharpe from luck alone = mean + 2.53 x sd = selection inflation about 0.28
- if 300 variants had been tried: expected best Sharpe from luck alone = mean + 2.90 x sd = selection inflation about 0.31
- deflated Sharpe probability at N = 32 (trial variance from the log): 1.000
- deflated Sharpe probability at N = 100 (trial variance from the log): 1.000
- deflated Sharpe probability at N = 300 (trial variance from the log): 1.000

## 3. Probability of backtest overfitting (CSCV)

20 rebuildable variants, 432 months, 16 blocks, 12870 in/out splits: PBO 0.04; median in-sample Sharpe of the in-sample winner 1.50, its median out-of-sample Sharpe 1.45.
Variants: base gm-1.2, trend cont, vol hybrid, cont + hybrid, cluster weights, trend spot-only, scenario limit 3%, weights expert, candidate, candidate slow 6/12, cand2 hybrid+expert, cand2 slow 6/12, cand2 slow 12, cand2 + scenario 5%, cand2 + scenario 3%, E1 econ theme blocks, S1 US 3m short-rate market, V1 bond value composite, V2 FX value skip 12m, C1 bond carry per duration.

## 4. Power of the one-shot holdout (189 months, 2011-01..2026-09)

| True Sharpe | P(SR >= 0.3) | P(max fall > -25%) | P(2022 > 0) | P(pass all) |
|---|---|---|---|---|
| 0.0 | 0.13 | 0.13 | 0.46 | 0.04 |
| 0.3 | 0.50 | 0.40 | 0.58 | 0.22 |
| 0.5 | 0.78 | 0.61 | 0.67 | 0.41 |
| 0.8 | 0.97 | 0.84 | 0.77 | 0.66 |

## 5. Emerging markets before 2000

- 1975..1989: gm-2.0 SR 1.22; without EM currencies and equities before 2000: 1.30
- 1990..2010: gm-2.0 SR 1.63; without EM currencies and equities before 2000: 1.51
- 1975..2010: gm-2.0 SR 1.46; without EM currencies and equities before 2000: 1.43

## 5. gm/CHANGES.md, extracts (engine change log)

Lines 34-39:
| Config | Period | Sharpe | Mean %/yr | Vol %/yr | Worst drawdown % |
|---|---|---|---|---|---|
| BASE gm-1.2.0 -> gm-1.2.1 | 1975-2010 | 1.235 -> 1.236 | 12.48 -> 12.49 | 10.10 -> 10.11 | -20.5 -> -20.5 |
| BASE gm-1.2.0 -> gm-1.2.1 | 1990-2010 | 1.475 -> 1.474 | 14.40 -> 14.41 | 9.77 -> 9.77 | -12.3 -> -12.3 |
| CANDIDATE gm-2.0 -> gm-2.0.1 | 1975-2010 | 1.464 -> 1.464 | 14.32 -> 14.33 | 9.78 -> 9.78 | -16.8 -> -16.8 |
| CANDIDATE gm-2.0 -> gm-2.0.1 | 1990-2010 | 1.630 -> 1.629 | 16.34 -> 16.34 | 10.03 -> 10.03 | -16.8 -> -16.8 |

Lines 45-66:
Framework rebuilt to be config-driven and statistics-driven: gm/config.py (every rule), gm/vol.py, gm/daily.py,
gm/timing.py, gm/stats.py (decade table, bootstrap, deflated Sharpe, marginal alpha), gm/trials.py (every trial
logged to gm/trials.csv with its config hash), gm/bloomberg.py (adapter; synthetic smoke test passes).
Decision rule fixed before the tests: adopt a component only if it raises net Sharpe in BOTH 1990-2010 and 1975-89.
| Trial (logged) | SR 1990-2010 | SR 1975-89 | Verdict |
|---|---|---|---|
| gm-1.2 base | 1.48 | 0.93 | reference |
| continuous vol-normalised trend | 1.43 | 0.76 | rejected |
| hybrid volatility (daily EWMA 35d + 10y, floor) | 1.58 | 1.06 | ADOPTED |
| cluster weights within class | 1.48 | 0.94 | rejected (no gain, deeper drawdown) |
| trend on spot moves only | 1.39 | 0.92 | rejected (carry inside trend helps) |
| scenario limit 3% | 1.32 | 0.93 | rejected as a rule; diagnostic |
| family shares 45/25/15/15 (trend/carry/value/econ) | 1.56 | 1.09 | ADOPTED |
| hybrid + shares = candidate | 1.63 | 1.22 | candidate |
| candidate with slow trend 6/12 / 12 | 1.43 / 1.40 | 1.03 / 1.10 | rejected |
| candidate + scenario limit 5% / 3% | 1.56 / 1.41 | 1.22 / 1.20 | rejected (drawdown/vol 1.55 vs 1.68 only) |
| risk theme credit-only (removes trend overlap) | 1.57 | 1.20 | rejected |
Trade timing (daily, price moves only, 1990-2010): 1/3/12 trend Sharpe 0.95 at k=0, 0.85 at 1 day late, 0.64 at 5,
0.61 at 10; slow 6/12 0.57 / 0.52 / 0.42 / 0.42. The fast blend beats the slow one at every delay. Rule: trade on the
first trading day after month end.
Candidate statistics 1990-2010: net SR 1.63, bootstrap 90% interval 1.26-2.02, deflated-Sharpe probability ~1.00
with 32 logged book trials (expected best of unskilled trials 0.21); every family adds (marginal alpha t: carry 4.9,

Lines 136-147:

## 2026-11-02: statistical audit (gm/audit.py -> docs/research/global_macro/stats_audit_2026-11-02.md)
- Bootstrap: gm-2.0 1975-2010 SR 1.46, 90% interval 1.17-1.79, stable for mean blocks 3-24 months; batch-0 p-values
  stable across block lengths.
- Selection inflation among 32 logged variants (sd 0.11): about 0.23 Sharpe (0.28-0.31 if 100-300 variants).
  Deflated Sharpe is 1.000 at every trial count, so it is uninformative here and is no longer cited as evidence.
- CSCV over 20 rebuildable variants: PBO 0.04 (in-sample winner 1.50 -> 1.45 out of sample).
- Holdout power (block bootstrap, 189 months): pass-all probability 0.04 if true SR 0, 0.22 at 0.3, 0.41 at 0.5,
  0.66 at 0.8; the -25% max-fall criterion is the binding one (61% at SR 0.5).
- EM currencies and equities removed before 2000: 1990-2010 SR 1.63 -> 1.51; 1975-2010 1.46 -> 1.43.
- Trial log fix: batch rows had the pooled 1975-2010 SR in the 1990-2010 column and signal-only challengers
  shared the incumbent's hash; corrected (era columns recomputed, fingerprint includes the challenger name).