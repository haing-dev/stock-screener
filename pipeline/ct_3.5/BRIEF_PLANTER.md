# Step 3.5 checker test: planter brief, 2026-11-24

You build the test cases that will measure whether our backtest checker can be trusted. Read SCORING_RULES.md and
BRIEF_CHECKER.md (the checker's instructions) first; do not change them.

Work dir: /tmp/claude-0/-home-claude/a8a60852-162d-5d9b-8463-3f9415508c73/scratchpad/ct35. Write cases ONLY into cases/ and your key and notes ONLY into planter/. No market
data at all (synthetic only), no web, do not spawn agents. You may read /home/claude/stock-screener/gm/*.py and the
specs in docs/research/specs/ to make the cases realistic (monthly futures-style excess returns, volatility-scaled
positions, costs per trade, eras 1975-1992 / 1993-2010, design window 1975-01..2010-12).

## Build
1. cases/_lib/synth.py: a deterministic synthetic panel generator (about 20-40 markets in 4 classes, monthly 1970-2015
   with some markets starting late, fat tails, a weak trend or carry effect in some markets so results are not all
   zero; optional daily series if a case needs it). Seeded; every case imports it.
2. 20 case folders cases/C01..C20 (ids assigned in a random order you record; no pattern by id). Each has:
   - SPEC.md: the registered spec in our spec style (claim, signal, markets, sample window, costs per class, versions,
     what is reported) - short, one page.
   - backtest.py: runs the spec on the synthetic panel in under a minute and prints the numbers the report uses.
   - REPORT.md: the author's result report (headline net Sharpe, mean, vol, worst drawdown, eras, cost line, any
     sensitivity), written from the code's actual output.
   Vary the pods (trend, carry, value, a rule layer with on/off months, a spread pod) and the code style so cases do not
   look alike.
3. Plant exactly one defect in each of 10 cases, 2 per type: look-ahead, sample, costs, period-selection, tuned-knob
   (definitions: BRIEF_CHECKER.md items 1-5). Make them REALISTIC: the kind of bug a careful builder makes (an
   off-by-one shift, a full-sample z-score, a cost on positions not trades, a start date moved to skip a bad year, a
   knob set to the best of a quick grid with the report silent about it, a report that leads with the best era). No
   comments, names or report wording that point to the defect. The report must still match what the code prints
   (except for period-selection, where the report's emphasis is the defect). The defect must change the headline result
   materially (at least 0.15 Sharpe or a clear sign/size change) so a careful checker can show it.
4. The other 10 must be genuinely clean: check each of them yourself line by line for any accidental look-ahead,
   sample, cost or knob problem, and fix it.
5. planter/KEY.json: {case_id: {"defect": true/false, "type": "...", "where": "file:line", "what": "...",
   "effect": "headline before/after fixing"}} and planter/NOTES.md (how each defect was built; how you verified the
   clean cases). Also planter/ASSIGN.json: two lists of 10 case ids for checker 1 and checker 2, each with 5 defective
   and 5 clean, mixed.
6. Run every backtest.py once and make sure each REPORT.md matches its output.

Reply with the case-type count, the two assignment lists (ids only), and any problem. Do NOT include which cases are
defective in your reply text.
