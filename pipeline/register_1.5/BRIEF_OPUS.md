# Step 1.5: thesis register (WORKFLOW v2.1), brief of 2026-11-22

You are the quant and risk officer of a small systematic-macro shop run as pods. Read pack/WORKFLOW.md sections 1-6
first (rules 1-9, the steps, the test sheet, the budget). Steps 1.2-1.4 are done: one charter, three thesis notes, five
playbook cards, each with an independent check whose corrections are already applied in the note. Your job is step 1.5:
ONE register of every thesis those notes put forward, so that steps 3.1-3.4 (specs, spec check, power check,
registration) can start from it without re-reading the notes.

Work dir: /tmp/claude-0/-home-claude/a8a60852-162d-5d9b-8463-3f9415508c73/scratchpad/register_1.5. Write only inside opus_work/. No backtests, no
market data, never any 2011-2026 result. Do not spawn agents. Do not edit anything outside opus_work/.

## Inputs
1. The notes, in pack/: CHARTER_1.2.md, THESIS_1.3_rates.md, THESIS_1.3_xs.md, THESIS_1.3_method.md,
   CARD_1.4_policy_liquidity.md, CARD_1.4_regime_debt_cycle.md, CARD_1.4_relative_value_risk.md,
   CARD_1.4_flows_volatility.md, CARD_1.4_commodity_balances.md, and each one's _check.md. The final text of a note is
   the note itself (corrections applied); the check is evidence about it (its section 4 lists open judgement points).
   Older inputs the charter consolidated: F1_economic_trend.md, F1_SPEC.md, foundation/U01-U07, AUDIT_1.1 (it says
   the numbers in U01-U07 are UNVERIFIED; the charter's check supersedes them). Read every note and check in full.
2. Rules: pack/WORKFLOW.md, pack/TESTING_PROTOCOL.md (the registered protocol for the existing book).
3. Data: pack/DATA_DIGEST_from_CLAUDE_md.md (what Bloomberg and LSEG returned, with start dates and failures),
   pack/DATA_SHEET_card_*.md (live series named for the cards). The existing book's markets and free-data sources: read
   /home/claude/stock-screener/gm/panel.py, gm/config.py, gm/signals.py (read only). Live data must be free or licensed
   for trading (rule 7); Bloomberg is research history only; LSEG is on the user's own PC (refreshable daily; WORKFLOW
   does not yet register it as a live source: say so where it matters).
4. Tool: tools/check_ids.py FILE (every claim id exists; every "quoted words" (ID) phrase is in that id's quote).

## What a row is
One thesis = one claimed way of making money that a note keeps (a pod, a version family inside a pod, a playbook
rule layer, an analyst-layer item) or explicitly drops. Every rule R1.. of every card is a row, held-back and dropped
ones included. Protocol items and diagnostics are not theses: list them in their own sections (below), not as rows.

## The register (the main table, one row per thesis; ids T01..)
Columns:
1. id; short name; source note(s) and section.
2. Thesis in one sentence (mechanism: who pays and why), as the note states it after its check.
3. Pod: existing pod (Trend, Economic trend, Carry, Value) / new systematic pod / rule layer of a discretionary pod /
   analyst layer only / not a pod (dropped, held back). Name duplicates: if the note or check says the rule is, or may
   be, the same as another pod or another card's rule, give that row id.
4. Rule sketch: signal, markets, direction, holding, sizing; number of versions as the note fixes them (and the count
   with any sizing version).
5. Data, history: series and source as the notes and the data digest show them, with the earliest usable date for the
   design window (1975-2010); "not on the sheet" or "unknown" where so.
6. Data, live: free source and delay, or "LSEG only (not registered as live)", or "none". A pod without a live source
   for every input cannot be Core (rule 7).
7. Evidence grade, exactly as the note states it after its check (strong / moderate / weak / none), with the id or
   section that carries it. Do not regrade; if note and check disagree, give both and say which text is final.
8. Dating (rule 5): documented before 2011 = a source dated before 2011 that states THIS mechanism and THIS rule form
   (not just the topic). Give the source as the notes cite it. Where a note's check names a candidate pre-2011 source
   from the checker's knowledge, you may confirm the bibliographic facts only (authors, title, journal, year) with
   WebSearch/WebFetch and give the URL; record whether the source states the same mechanism and rule form as far as
   its abstract or the notes show; if you cannot confirm, the row stays "hindsight-flagged (candidate: ...)". Every
   playbook rule layer is hindsight-flagged unless a pre-2011 document of that investor states the rule. Never infer a
   date from memory alone.
9. Status for testing, from the notes and WORKFLOW section 6: Batch A (hygiene) / B1 / B2 / B2 rule layer
   (Incubator at best) / gated by diagnostic Xn (name it) / held back (condition for release) / dropped (reason).
10. Open judgement points that touch this row, each with the step that closes it (from the note's last sections and
    the check's section 4).

## Further sections
A. Diagnostics: every zero-slot diagnostic across all notes (charter D1-D6, R1, X1, X2, M1, each card's D1/D2 ...),
   one row each: id, question, gate exactly as fixed in the note after its check, data, design months, which rows it
   gates, and anything in its definition that is still a hidden choice. Flag duplicates (two notes asking the same).
B. Protocol items: every item a note puts to step 3.4 (P1-P4 of 1.3c, pod process rules and sizing versions of the
   cards, the charter's version grids), one line each with the source and whether it changes a decisive test.
C. Overlaps and conflicts across notes: same rule in two cards; a card rule that is an existing pod; a card that
   contradicts another card or a thesis note; each with ids and what step 3.1-3.2 must decide.
D. Engine and data preconditions before any run (from the notes and the digest): e.g. the doubled US 2-year series,
   LOCK_v2.json not yet in the repo, data still missing per row (e.g. daily dollar strip contracts 3, 5, 6, 7),
   LSEG not registered as a source. One line each, with which rows it blocks.
E. Budget: count of candidate pods per batch against WORKFLOW's limit (at most 4 per B batch); what does not fit and
   the ordering rule the notes give (if they give none, say so; do not invent one).
F. The five conflicts between WORKFLOW and TESTING_PROTOCOL that 1.3c lists (error level per batch, era test, form of
   test 1, hygiene test, double costs) plus any further one you find; for each, the two texts verbatim and the step.
G. Counts: rows by pod type, by status, by dating; versions to register in total.
H. What you could not settle and why; pack problems (contradictions between notes, a check that a later note
   contradicts, ids cited by one note that another note reads differently).

## Hard rules
- No decisions for the user. Every open choice becomes a registered version, a diagnostic with a gate, a step that
  closes it, or is dropped with a reason. Nothing is claimed as registered or run.
- Do not add theses, rules or grades the notes do not contain. You may merge two rows only when a note or check says
  they are the same; otherwise list both and cross-reference.
- Quote the notes' own words for grades, gates and statuses (short). Cite claim ids exactly as the notes cite them;
  any quoted claim words go as "words" (ID) so the checker can verify them.
- Plain language, short sentences; explain a term a non-specialist would not know. No backticks inside table cells.
- Before you finish: run python3 tools/check_ids.py opus_work/THESIS_REGISTER_1.5.md until it prints ALL IDS AND
  QUOTES OK; check that every card rule (R1.. of all five cards), every pod of the charter and every new pod or
  version family of the three thesis notes has a row (write this as a checklist at the end, section I).

## Output: opus_work/THESIS_REGISTER_1.5.md
Order: 1. Summary in at most ten lines (counts; what can go to Batch A, B1, B2; what is blocked and by what; the
weakest point of the whole register). 2. The register table. 3. Sections A-I. Length as needed; tables preferred.
Reply with section 1, the counts of section G, and the three most important items of sections C-D.
