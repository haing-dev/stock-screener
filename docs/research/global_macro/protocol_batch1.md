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
