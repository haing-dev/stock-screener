# Step 3.5 checker test: result, 2026-11-24

**PASS. Caught 10 of 10 planted defects (every type 2 of 2); 0 false alarms on 10 clean cases.** Pass bar (fixed in
SCORING_RULES.md and pushed to the vault before any case was built): >= 8 of 10 caught with every type caught at least
once, and <= 2 false alarms. Answer key SHA-256 0796468d0b77...764c pushed before checking; re-verified identical
after scoring.

Set-up: one Opus 5.5 planter (effort high, ~0.30M tokens) built 20 synthetic backtests (spec + code + report each;
shared generator cases/_lib/synth.py; no market data): 10 with one planted defect, 2 each of look-ahead, sample, costs,
period-selection, tuned-knob, each moving the headline net Sharpe by >= 0.17 when fixed; 10 clean. Two fresh Opus
checkers (brief BRIEF_CHECKER.md v1; ~0.16M and ~0.15M tokens) got 10 cases each (5 + 5, one of each type), saw
neither the key nor the other's cases. Scoring by score.py (score_output.txt).

| Case | Planted | Checker verdict | Result |
|---|---|---|---|
| C01 | sample (22 extreme months dropped) | DEFECT: sample; net 0.87 -> 0.62 on all 432 months | caught |
| C05 | period-selection (report leads with a market subset) | DEFECT: period-selection; registered headline 0.22 | caught |
| C08 | look-ahead (CPI publication lag) | DEFECT: look-ahead; 0.23 -> -0.18 | caught |
| C09 | costs (charged on pair units, not leg notional) | DEFECT: costs; 1.09 -> 0.92 | caught |
| C10 | costs (one-way cost 0.1 bp vs 1 bp) | DEFECT: costs; 0.41 -> 0.11 | caught |
| C12 | look-ahead (full-sample z-score) | DEFECT: look-ahead; 0.74 -> 0.20 | caught |
| C14 | period-selection (leads with 1993-2010) | DEFECT: period-selection; registered 0.43 | caught |
| C15 | tuned-knob (isolated peak 6/1) | DEFECT: tuned-knob; neighbours <= 0.27 | caught |
| C19 | sample (dropna cuts to 1990) | DEFECT: sample; 0.94 -> 0.39 | caught |
| C20 | tuned-knob (best look-back of a grid) | DEFECT: tuned-knob; neighbours 0.10 / 0.24 | caught |
| C02, C03, C04, C06, C07, C11, C13, C16, C17, C18 | clean | CLEAN (all 10) | no false alarm |

Limits (why this is a floor, not proof): the cases are small (one file, under a second to run) while real batch runs
go through the full engine; every planted defect was sized to move Sharpe by >= 0.17, so subtler defects were not
tested; the planter read the checker brief; 20 cases give a wide interval (10 of 10 is consistent with a true catch
rate as low as about 74% at 95% confidence). So, as WORKFLOW s7 item 5 says, no single check is trusted alone: the
script checks (truncation test, reproduction, trial log) stay in force at step 4. Re-run with new cases whenever the
checker brief changes.
