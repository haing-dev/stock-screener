# Step 3.4: registration (WORKFLOW v2.1), brief of 2026-11-23

You are the quant and risk officer. WORKFLOW 3.4: "Registration: batches, pods, grids, tests, error budget, freeze rule,
holdout consequences, live checkpoints written into TESTING_PROTOCOL.md and committed before any run." Everything
needed is decided in earlier steps or left to 3.4 by name. Your job: write the registration text, settle every item
left to 3.4 with a reason, and a one-page summary for the user. A fresh agent checks your draft before it is committed.

Work dir: /tmp/claude-0/-home-claude/a8a60852-162d-5d9b-8463-3f9415508c73/scratchpad/reg_3.4 (write only here). Repo /home/claude/stock-screener read-only. No backtests,
no market data, never any 2011-2026 result, no web, do not spawn agents.

## Inputs (read all)
- docs/research/WORKFLOW.md (whole), docs/research/global_macro/TESTING_PROTOCOL.md (whole; the new section is added
  to it, existing batches 0-1 stay as history).
- docs/research/THESIS_REGISTER_1.5.md (rows, sections A-I), docs/research/specs/ (11 approved specs; README;
  NOTES_3.1_agent_*.md; checks/CHECK_3.2_*.md, especially section 4 = items for 3.4), docs/research/power/POWER_3.3.md
  (section 4 = proposal for 3.4, section 5 = limits).
- docs/research/fable/THESIS_1.3_method.md (P1-P4, M1, conflicts), CHARTER_1.2.md (D1-D6, grids), the CARD_1.4_* notes
  only where a spec points to them; gm/CHANGES.md and gm/trials.csv (what exists, what was already seen); gm/config.py.

## What the registration must contain (as text ready to paste into TESTING_PROTOCOL.md as a new section 7)
1. Scope and precedence: which document wins where WORKFLOW and TESTING_PROTOCOL differ after this section (settle all
   five 1.3c conflicts plus any found in specs/checks: error level per batch, era test, form of test 1, hygiene test,
   double costs for a pod; deflated Sharpe as reported; 5.1 equal risk vs family shares). Quote both texts, rule, reason.
2. Rule 5 reading: what "documented before 2011" requires (mechanism and rule form? dating classes A/B/C of the
   register) and what each class may earn (Core / Incubator), with the reason. Use the power check and register G7.
3. Trade timing: k=0 (engine) vs k=1 (WORKFLOW one-day delay): which is decisive, which reported; the cut of every
   holding at the 2010-12-31 close; the weekly-tranche calendar.
4. Pre-run engine and data changes (each needs its own gm/CHANGES.md entry before code, like C1-C4 and gm-1.2.2):
   Bloomberg switches OFF by default + gm/bloomberg.py:52 map fix; CPI release-date rule; k=1 form; holding cut;
   strip-vector caps; anything else the specs/checks list. One line each: what, why, which runs it blocks.
5. Diagnostics (zero slots, design months only): the full list with gates as fixed in specs/register, the sealed-month
   fixes (end dates), duplicates merged with one threshold rule where specs leave it to 3.4 (e.g. "already held"
   thresholds: settle one rule or keep each note's, with reason), order of running, and what each pass/fail does.
6. Batches: A1 (data swap), A2 (grids, tranches, averaging; the Value v2 already-seen leg), B1, B2: exact contents,
   version grids (counts per pod), what enters only through a gate, whether card rule layers count against "at most 4
   per B batch" (settle), ordering rule if over budget, minimum on-months / episodes for a rule layer (power check).
7. Tests and thresholds: the decisive statistic and threshold of each decisive test, the batch error level and Holm
   count, Incubator rule, hygiene rule, reported lines (P4, M1, eras, one-period delay, fragility...), the measured
   false-adoption rate to state (power check), and the expected pass rates per pod shape (one small table).
8. Trial count and hindsight: how trials are counted (gm/trials.csv rows; already-seen legs such as Value v2's bond
   leg and the S1 trial), the deflated Sharpe as a reported line or dropped (with reason).
9. Freeze rule (config id + lock id), holdout: criteria as registered, which pods get a verdict (rule 5), consequences
   of pass and fail (already in WORKFLOW s6: restate exactly), the power of the criteria (power check holdout table).
10. Live: checkpoints and promotion rules for Incubator pods, kill/review conditions from spec section 11, the live
    sources needed (GB/euro 3-month rate gap before 2027-01; LSEG not registered as a live source: what registering
    it requires), forecast ledger and analyst layers (descriptive).
11. What is NOT registered yet and why (e.g. pods blocked by LSEG history), and what would change the registration
    (a new version number and entry, never silently).

## Rules
- No decision for the user: every open item is settled here with a reason, or named as blocked with what unblocks it.
- Take numbers from the specs, register and power check; cite file and section. Do not invent thresholds without a
  reason from those sources.
- The text must be precise enough that a builder runs it without a choice; plain language; tables where they help.
- Nothing is run. No 2011+ number.

## Output
- reg_3.4/REGISTRATION_3.4.md: (a) the new TESTING_PROTOCOL section 7 text, ready to paste; (b) a table of every item
  left to 3.4 by the register, specs, checks and power check, each with "settled in 7.x" or "blocked by ...";
  (c) the list of gm/CHANGES.md entries to write before the first run.
- reg_3.4/SUMMARY_FOR_USER.md: at most one page, plain language: what will be tested, in what order, what can and
  cannot pass, what is blocked, what happens at the holdout.
Reply with the summary and the count of items settled / blocked.
