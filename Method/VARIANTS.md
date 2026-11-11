---
tags: [method, spec]
file: /home/claude/stock-screener/docs/research/fable/foundation/VARIANTS.md
---
# Strategy variant registry and selection procedure (draft, 2026-11-09)

User rule (2026-11-09): the foundation notes do not hand "decisions" to the user (cost route, risk route, breadth route,
how to read a 2022 fail). Each open choice becomes levels of a strategy dimension. The choices are then made by data,
on the Bloomberg design-era panel, through ONE pre-registered selection procedure. Status: DRAFT. Register it in
TESTING_PROTOCOL.md (Batch 2) before any run, once the Bloomberg files are in.

## Why not one test per idea
Each foundation idea promises a small gain (+0.02 to +0.04 dSR, U02 section 1). Under the per-change bar (dSR >= 0.05,
Holm) none can pass alone. Picking winners one by one on the same data would also inflate the selection
(stats_audit_2026-11-02). The fix is to test the selection procedure, not the ideas: the procedure picks levels using only
past data, and its out-of-sample result is judged once against the live book.

## Dimensions and levels (level 0 = live BASE gm-1.2 / CANDIDATE gm-2.0)
| Dim | Choice | Levels | Source |
|---|---|---|---|
| A | Universe | 0 current 62 markets; 1 + alternative commodities (30% cap, PC1-beta gate); 2 = 1 + wider EM FX (file 3) | U05-T1, U06-T2 |
| B | Market weights | 0 equal risk per class; 1 scaled by effective breadth (first-factor beta) | U05-T1 |
| C | Vol sizing | 0 hybrid 70/30 (live); 1 m36; 2 slow only; 3 static at entry | U03-T1 |
| D | Book scaler | 0 36-month realised; 1 6-month correlation x 1-month vol | U02 row 22, U03-T3 |
| E | Trend signal | 0 sign 1/3/12; 1 continuous, scaled to avg 10, cap 20; 2 = 0 + vol-regime attenuation | U02-T4/T5 |
| F | Execution | 0 monthly, day 1; 1 day 3 (skip the turn); 2 weekly re-read; 3 = 0 + cost-scaled no-trade buffer | U04-T1, U06-T3, U02-T3 |
| G | Commodity carry | 0 current; 1 calendar spread (12m vs front, off in backwardation) | U04-T3 |
| H | Econ themes | 0 current; 1 forecast-based growth/inflation (first release + consensus) | U01-T3 |
| S | Selection statistic (procedure) | 0 shrunk net Sharpe; 1 shrunk net downside ratio with a concavity bar (chosen by the U07-T1 shape audit rule, fixed before the run) | U07-T1 |
| P | Holdout form (procedure) | 0 frozen picks at end of design era; 1 annual re-selection continued through the holdout | U07-T3 |

Fixed (not dimensions): family shares 45/25/15/15, costs model, the 30% alternative cap, rules per market identical.
Excluded until their diagnostic says otherwise: carry-tercile structure tilt (U05-T3), geopolitical-risk theme (U03-T4),
spread trading (U05-T5 vol gate).

## Selection procedure (the one thing tested)
1. Design era only (holdout 2011-2026 never touched). Monthly panel from Bloomberg files 1-7 + free data.
2. Main effects: for each dimension, each level vs level 0 with every other dimension at 0 (21 runs). Report dSR,
   max fall, 2022-type windows (1994, 2008), turnover, cost. Diagnostics only, no adoption.
3. Walk-forward selection: from year 10 of the sample, each January pick per dimension the level with the best
   shrunk net Sharpe on data up to that date (shrinkage 0.5 toward level 0, Carver B29); a level must also not worsen
   max fall by > 2 points. Hold the picks for the year. The chained out-of-sample returns = the PROCEDURE.
4. Test: PROCEDURE vs BASE under TESTING_PROTOCOL tests 1-5 (paired bootstrap dSR >= 0.05, non-inferiority per era).
   One Holm slot for the whole registry.
5. If it passes: freeze the levels the procedure picks on the full design era; that book goes to the one holdout run.
   If it fails: BASE stays; the main-effects table guides the next registry.

## Holdout reading (pre-committed, replaces the "decisions" in U02/U03)
- Criteria stay as registered (SR >= 0.3, worst fall > -25%, corr S&P <= 0.3, 2022 positive).
- Each criterion's pass probability at the frozen book's design-era Sharpe is stated before the run (stats_audit table).
- A fail is decomposed with the zero-slot diagnostics (U03-T1 vol speed, U05-T2 winner share); no redesign on holdout data.

## Zero-slot diagnostics to run first (inform priors, do not adopt)
U01-T1/T2, U02-T1/T2, U03-T1/T2/T3, U04-T1/T2, U05-T1/T2/T4, U06-T1.
