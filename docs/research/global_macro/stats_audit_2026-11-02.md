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
