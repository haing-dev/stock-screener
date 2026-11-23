# Step 3.1: pod specs (WORKFLOW v2.1), brief of 2026-11-23

You are the quant and risk officer of a small systematic-macro shop run as pods. Step 1.5 produced ONE register of
every thesis (pack/THESIS_REGISTER_1.5.md). Step 3.1 turns each pod in it into a spec in a fixed form, so that step 3.2
(a fresh agent checks each spec), 3.3 (power check) and 3.4 (registration) can work from the specs alone. Three agents
write specs at the same time; your assignment is at the end. Write ONLY inside your own folder agent_<X>/.

Work dir: /tmp/claude-0/-home-claude/a8a60852-162d-5d9b-8463-3f9415508c73/scratchpad/spec_3.1. No backtests, no market data, never any 2011-2026 result.
No web. Do not spawn agents. The repo /home/claude/stock-screener is read-only (read gm/*.py freely, especially
config.py, panel.py, signals.py, book.py, vol.py, daily.py, protocol.py).

## Inputs (pack/)
- THESIS_REGISTER_1.5.md: the register (rows T01-T106, sections A-I). Its status block: preconditions D1 (doubled US
  2-year) and D2 (LOCK_v2.json) are RESOLVED (engine gm-1.2.2; gm_CHANGES.md has the entry). Read all of it.
- The notes and their checks (CHARTER_1.2, THESIS_1.3_rates / _xs / _method, CARD_1.4_* and each _check.md; F1, foundation/):
  the final text of a note is the note (corrections applied). Read in full every note your pods come from, and its check.
- WORKFLOW.md (rules 1-9, steps, test sheet section 5, budget section 6), TESTING_PROTOCOL.md (existing protocol,
  costs, eras), gm_CHANGES.md and gm_trials.csv (every engine change and every design trial already run, i.e. what has
  been seen), BOOK_FACTS_design_era.md (design-era results on record), DATA_DIGEST_from_CLAUDE_md.md and DATA_SHEET_card_*.md.
- Tool: tools/check_ids.py FILE (every claim id exists; every "words" (ID) phrase is in that id's quote).

## The spec form (one file per pod: agent_<X>/SPEC_<pod name>.md; headings exactly these, in this order)
0. Header: pod name; type (existing pod / new systematic pod / discretionary pod = rule layer + shadow analyst);
   register rows; source notes and sections; register status (batch, gating diagnostics); dating class (A/B/C/n/a,
   register column 8) and what rule 5 then allows.
1. Economic claim: who pays whom and why, in two or three sentences, as the notes state it after their checks; the
   evidence grade exactly as the note gives it, with the id or section.
2. What is predicted: the quantity (excess return of which instrument, over which horizon), its sign, and in which
   states it should be largest.
3. Signal: exact computation in numbered steps that a builder can code without a choice: inputs, transformations,
   windows, lags (publication lags of each economic series, as-of rule: only data public at the month-end), the
   rebalancing date, the mapping to a position. The SIGN is fixed here and cannot be flipped after results. For an
   existing pod, describe what the code does NOW (file and function), then any registered change the notes ask for.
4. Markets: the list (ids as in gm/panel.py where they exist), each with its earliest usable design month; markets
   that enter only through a gate (name the gate).
5. Sizing: volatility estimate, target, caps, how the pod's positions combine into the pod and the pod into the book
   (state what WORKFLOW 5.1 and config.py say; where they disagree, say so and name step 3.4).
6. Version grid: every version, as a table (knob values per version); versions are averaged with equal weight, never
   picked; total count; which versions exist only if a diagnostic opens them.
7. Sample: design window (fixed here; start = the first month every input of at least half the versions exists, or a
   reason for another start); eras as in TESTING_PROTOCOL; months excluded and why. Never 2011+.
8. Data: per input, history source and first date, live source and delay, licence status (free / LSEG on the user's
   PC, not registered as live / Bloomberg research only / none). Rule 7: a pod without a live source for every input
   cannot be Core: say whether this pod can.
9. Costs: per market class as in TESTING_PROTOCOL and the engine (file, constant); turnover expectation if the notes
   give one; the double-cost test applies.
10. What would prove it wrong: observable results on the design window that would reject the CLAIM (not just "fails
   the test"): e.g. return of the wrong sign in the states the mechanism names, profits coming from a different
   source than the mechanism says. Fixed now; numeric where the notes allow.
11. When it should stop working: conditions observable live that would end the mechanism (crowding, regime, rule
   change), as the notes state them; these become the live kill and review conditions.
12. Knobs that were tuned: every parameter in sections 3-6 with its origin: quote (id) / source paper / engine
   convention / chosen after seeing design results (cite the gm_trials.csv row or CHANGES entry) / grid. Count the
   knobs chosen after results: that count goes into the hindsight flag.
13. Gating diagnostics: each diagnostic that gates this pod or a version (register section A id), with its gate as
   fixed after the note's check, and what follows from pass and fail. Flag any that reads sealed months as written and
   state the fix the register proposes, as a proposal for 3.4.
14. Overlaps: every overlap the register (section C) or a note lists, re-checked against the code where it names an
   existing pod (cite gm/signals.py function and theme); what must be measured and at which step.
15. Open choices: each one closed as a version (in section 6), a rule written here with its reason, or left to a named
   step (3.2, 3.3, 3.4). Nothing is left to the user.
16. Builder must not change: a short list (sign, sample, grid, data sources, costs).

## Hard rules
- Take theses, grades, gates and versions from the notes and register only. Do not add, regrade or drop a thesis.
  Where register and note disagree, the note's final text wins; say so in section 15.
- Every claim id exactly as the notes cite it; any quoted claim words go as "words" (ID). Run tools/check_ids.py on
  each spec until ALL IDS AND QUOTES OK.
- Where the notes leave a computation open, close it in section 3 with the simplest form that matches the note's
  words and say "closed here: <reason>" so 3.2 can check it; or make it a version; never leave it open.
- Plain language, short sentences; tables where they help. No backticks in tables. Aim for 1-3 pages per spec.
- Nothing is registered or run. Do not write any number from the design-era results except as "already seen" in
  section 12 (and give where it was seen).

## Output
Your specs, plus agent_<X>/NOTES.md: (a) contradictions or gaps found between register, notes and code; (b) items
for 3.4 (with the spec and section); (c) check_ids result per spec. Reply with one line per spec (pod, versions, status,
gates, can it be Core) and the three most important items of NOTES.md.

## Assignments
- Agent A: the four existing pods: Trend (T01, with T09 breadth item and the T12 note on cross-sectional momentum),
  Economic trend (T02; state the four themes as coded and that there is no growth theme), Carry (T03, T04, T05, with
  T10 short-rate futures markets as a gated market set), Value (T06, T07). Code first: describe what runs now.
- Agent B: the two new systematic pods: Curve carry (T08) and Strip reversion (T11, gated by diagnostic R1; data
  precondition: daily dollar strip contracts 1-8, only 1, 2, 4, 8 in hand).
- Agent C: the five discretionary pods, one spec per card: card 1 policy and liquidity (T13-T19), card 2 regime and
  debt cycle (T20-T22), card 3 macro relative value and risk (T23-T27), card 4 flows and volatility (T28-T33), card 5
  commodity balances (T34-T36). Each card pod = its rule layer (each rule with its own sub-block for sections 3, 4, 6,
  10, 13) + its shadow analyst (questions, forecast set, live scoring; judged live only). Held-back rules (T18, T35):
  spec the release condition only. Re-check every "already held by pod X" statement against gm/signals.py.
