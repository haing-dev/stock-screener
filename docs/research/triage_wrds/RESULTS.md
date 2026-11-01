# Triage on WRDS: follow-up test results (job tri_research1, 2026-10-31)

Plan and pass test: PLAN.md (written before these results). Train = calls 2008-2015, test = 2016-2024.
Excess = one-year return minus the 10 most similar stocks (capped at +500%); t by month = clustered by call month.
Alpha = calendar-time FF5+UMD, Newey-West t. Statistics only (WRDS policy).

## Verdict: no test passes. No change to triage/rules.py.
| Test | Hidden Earnings | Emerging | Core |
|---|---|---|---|
| 0. Pre-registered Buy - Avoid, test years (alpha/yr, t) | -12.1% (-1.42) | -0.1% (-0.04) | +0.3% (0.15) |
| 2. Learned weights, top - bottom third (alpha/yr, t) | -6.0% (-0.63) | -1.0% (-0.28) | -2.3% (-0.79) |
| 3. Red-flag filter, clean - flagged (alpha/yr, t) | -4.9% (-0.61); flags fcf, roic, sales | -1.5% (-0.35); flags gm, dilution | no flags chosen |
| Pass needs t >= 2.0 | fail | fail | fail |

## What the numbers say
- Red flags pick losers in raw terms, out of sample: Hidden clean +1.5 median excess, 52% beat, 5% halve vs flagged
  -12.5, 41%, 21%; Emerging clean -2.7 vs flagged -12.9 (18% halve). Bottom third by learned score: Hidden -18.6,
  Emerging -11.6 median excess. Avoid calls over 3 years: Hidden -35.7 median excess, Emerging -24.7, Core -8.6.
- But all of that is the profitability factor (RMW loading +0.6 to +1.1 on every long-short): known, cheaply
  available, not new alpha. After FF5+UMD nothing is left.
- Estimate revisions cell (I/B/E/S, 97% coverage): no signal in any triage (green vs red within 1-3 pts). Hidden
  events with no analyst estimates are poor (-15.5 median excess, t -3.5; n 385).
- Learned weights did not hold out of sample (Core: bottom third beat top third).
- Core Buys: +1.0 median excess one year (t by month +3.1) and +1.3 over three years, but FF alpha +1.2%/yr (t 0.4).

## Implication
The triage works as a warning system (Avoid = high odds of large losses), not as a source of excess return. Any
practical use: treat Avoid/red flags as exclusions on an otherwise diversified quality-tilted portfolio.
