# Step 3.2: spec check (WORKFLOW v2.1), brief of 2026-11-23

You are an independent checker (quant and risk officer). Step 3.1 wrote pod specs; you did not write them and must not
defend them. WORKFLOW 3.2 asks three things of each spec: is it faithful to the card / note and its claims? can it
fail? is the hindsight flag right? Add three more: is the signal fully specified (a builder needs no choice) and free
of look-ahead? is what it says about the existing code true? are its data and live-source statements true?
"Cannot verify" is a valid result; a guess is not.

Work dir: /tmp/claude-0/-home-claude/a8a60852-162d-5d9b-8463-3f9415508c73/scratchpad/spec_3.1. Your specs: the folder named in your assignment (read only).
Write ONLY inside your check folder check_<X>/. No backtests, no market data, never any 2011-2026 result, no web, do
not spawn agents. Repo /home/claude/stock-screener read-only (gm/*.py, tools/bbgq/engine_ref.json metadata only).

## Inputs
- The specs of your assignment and the writer's NOTES.md (read them first, in full).
- The spec form and the writer's rules: BRIEF_OPUS.md (sections 0-16 and hard rules).
- pack/: THESIS_REGISTER_1.5.md; the notes and checks the specs come from (CHARTER_1.2, THESIS_1.3_*, CARD_1.4_* and
  *_check.md, F1, foundation/); WORKFLOW.md; TESTING_PROTOCOL.md; gm_CHANGES.md; gm_trials.csv; BOOK_FACTS_design_era.md;
  DATA_DIGEST_from_CLAUDE_md.md; DATA_SHEET_card_*.md. Ground truth for claims = the "quote" field of the ledger
  (tools/check_ids.py and the lookup used by it); for the engine = the code; for rules = WORKFLOW and TESTING_PROTOCOL.
- Tools: tools/check_ids.py FILE; tools/apply_check.py CHECK.md SPEC_DIR OUT_DIR.

## Checks, per spec
A. Faithful: every thesis, grade, gate, version count and status matches the note's final text and the register (cite
   both). Nothing added, regraded or dropped. Every quoted claim is in its quote and supports what the spec uses it for.
B. Can it fail: section 10 names results on the design window that would reject the claim; they are fixed, numeric
   where the notes allow, and not satisfied by construction. Section 11 kill conditions are observable live.
C. Hindsight: section 12 lists every knob in sections 3-6 with its origin; each "chosen after results" is right and
   complete (check gm_trials.csv and gm_CHANGES.md for knobs already tested, and BOOK_FACTS for results already seen);
   the dating class and its rule 5 consequence match the register.
D. Specified and point in time: walk section 3 as a builder. List every place a choice remains, every input used
   before it was public (publication lags, revisions, as-of rule), every window that reaches past 2010-12 (including
   holding periods and next-day trades). Judge each "closed here" choice: accept, or correct with a reason.
E. Code: for existing pods and every "already held" / overlap statement: is it what gm/config.py, panel.py,
   signals.py, book.py, vol.py, daily.py actually do (cite file and line or function)?
F. Data and costs: history starts, live sources, licence status and cost classes against the data digest, data sheet,
   engine_ref.json design-month counts and the engine's cost constants. Rule 7 conclusion right?
G. Rules of the shop: versions averaged, not picked; no decision for the user; sign fixed; sample fixed by the spec,
   not the builder; nothing claimed as registered or run; no 2011+ number.

## Output: check_<X>/CHECK_3.2_<X>.md
1. Verdict per spec: APPROVED / APPROVED WITH CORRECTIONS / REJECTED (rejected = a defect that corrections cannot fix,
   e.g. a rule that cannot be specified without a new thesis), with counts per check A-G, in a table.
2. Findings per spec, by check A-G (lists).
3. Required corrections (the heading must read exactly "## 3. Required corrections"). Under it one sub-heading per
   spec file, exactly "### SPEC_<name>.md"; under each, numbered items 1., 2., ...: one line of description, then
   exactly these two lines, then a line starting "Reason:" with the id / file:line / section and the words:
   - Find: `<words copied verbatim from the spec, on one line, occurring exactly once in it, no backticks>`
   - Replace: `<the replacement, on one line, no backticks>`
   Keep each Find short but unique. Then run: python3 tools/apply_check.py check_<X>/CHECK_3.2_<X>.md <spec folder>
   check_<X>/corrected  until it prints ALL PAIRS APPLIED; run tools/check_ids.py on every corrected spec (ALL OK);
   read the changed passages once.
4. Items for step 3.4 (one line each: spec, section, what 3.4 must fix and why). Include anything shared across specs.
5. What you could not verify.
Reply with section 1, the number of corrections per spec, and the three most important findings.

## Assignments
- Checker A: agent_A/ (SPEC_Trend, SPEC_Economic_trend, SPEC_Carry, SPEC_Value). Code-heavy: check E closely.
- Checker B: agent_B/ (SPEC_Curve_carry, SPEC_Strip_reversion). Check the sizing / cap closure and the cost closure.
- Checker C: agent_C/ (SPEC_Card1..5). Check every rule against its card's quotes and every "already held" against code.
