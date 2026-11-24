# Step 3.5 checker test: scoring rules, fixed 2026-11-24 BEFORE any case is built or checked

Cases: 20 synthetic backtests, 10 with one planted defect (2 each of: look-ahead, sample, costs, period-selection,
tuned-knob) and 10 clean, in random order. Two fresh checker agents (brief BRIEF_CHECKER.md v1) check 10 cases each;
neither sees the key or the other's cases.

A defective case is CAUGHT when the checker's verdict is DEFECT and its evidence points to the planted defect (the
listed type matches, or the evidence names the planted line or its effect). DEFECT with the wrong reason = MISSED
(scored separately as "flagged for another reason"). A clean case is a FALSE ALARM when the verdict is DEFECT; the
coordinator then reads the evidence: if it shows a real, unplanted defect in that case, it is recorded as an
"unplanted defect found" (the case is repaired and the key updated; it is not a false alarm).

Pass bar for relying on the checker (Kinlay's critic: 20 of 25 caught, 4 false alarms on 25 clean):
- catch rate >= 8 of 10 (80%), with every defect type caught at least once;
- false alarms <= 2 of 10.
If the bar is missed: the checker brief is revised (v2) from the misses only, and the test is repeated with NEW cases
built by a fresh planter (never re-run on the same cases). Results go on record either way. Whatever the score, no
single check is trusted alone (WORKFLOW s7 item 5): step 4 keeps the script checks (truncation test, reproduction) as
well.
