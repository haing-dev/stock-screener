# Triage on WRDS: follow-up tests (written 2026-10-31, before any result of these tests was seen)

Baseline (job tri_run2, rules v1.0.0): calls sort on profitability (RMW); no triage shows a significant FF5+UMD alpha.
These tests decide what, if anything, changes in triage/rules.py. Code: tools/wrdsq/tri_wrds_adapter.py `research()`.
Same events, cells and outcomes as tri_run2 (one-year return minus the 10 most similar stocks; each return capped at
+500%). Train = calls 2008-2015, test = calls 2016-2024; nothing is fitted on test years.

0. The pre-registered calls on the test years only (Buy / Watch / Avoid), as the benchmark.
1. New research cell, Estimate revisions (I/B/E/S summary, next fiscal year EPS): (ups - downs) / estimates summed
   over the 3 months up to the scan; green >= +10%, red <= -10%, no estimates = N/A. Evidence per colour, all years.
2. Learned weights: OLS of excess return (train, winsorised 1/99%) on each cell's colour (+1 green, -1 red, 0 neutral
   or N/A; insider excluded, revisions included). Test events split into thirds by fitted score.
3. Avoid filter: cells whose red colour trails the other events by 5+ points (median, train, n >= 100) become red
   flags; test events with any red flag vs none.
4. Three-year horizon: own vs similar stocks' 36-month return per call (events 2008-2022).

Pass test for adopting a change (2 or 3): on the test years, the top-minus-bottom (or no-flag-minus-flag) calendar-time
FF5+UMD alpha has t >= 2.0 AND the monthly-clustered excess-return t of the top (or clean) group is positive.
Anything else stays research; triage/rules.py is changed only through triage/CHANGES.md with a new version.
