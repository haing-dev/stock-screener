# Descriptive re-run of the crash-triage backtest (2026-11-15)

Purpose: describe what the public crash-triage backtest shows (dispersion, medians, results against XBI, horizons,
fragility) for `BIOTECH_DESK_DESIGN_v0.1.md`, section 3.2. Description only: the triage rules were chosen on these
same episodes (2020-2026), so nothing here is a test.

Inputs: a clone of the public repo `haing-dev/crash-triage` at the commit in `crash_triage_commit.txt` (code and
data as committed; no network calls).

How to run (in this order; the second script reads the score files the first one writes into the clone):

    python3 analyse.py  <path to a copy of the crash-triage clone>   > analyse_out.txt
    python3 horizons.py <same path>                                  > horizons_out.txt

Definitions:
- Episodes with a full year of outcome; calls made on the entry day (later upgrades left out), as in the repo's
  own report.
- Return = total return from the entry-day close; a single return is capped at +500% (the repo's rule).
- "ex" = that return minus the XBI total return over the same days.
- `t_month` = t statistic of the monthly means (one value per entry month).
- `mean_ex_wo_top2pct` = mean excess without the best 2% of episodes.
- Labels in the code: overdone = Buy candidate, close = Watch, justified = Avoid.

Sample sizes needed (80% power, one-sided 2.5%, independent events), from the 12-month spreads in the output:
crash Buy at +15 points: about 410; at +10 points: about 930; crash Avoid at -58 points: about 25; slide Avoid at
-28 points: about 90.
