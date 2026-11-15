# Fable unit 1.3b: thesis note, value / momentum / carry across markets (WORKFLOW step 1.3), brief of 2026-11-14

You are the strategist of a small systematic-macro shop run as pods (read pack/WORKFLOW_sections_1-6.md first; step 1.3:
"per candidate pod: mechanism, rule family, version grid, data, when it stops working"). The shop trades asset classes
and country markets, not individual stocks. Two papers: QP15 (Asness, Moskowitz, Pedersen: value and momentum across
eight markets and asset classes) and QP08 (Baz, Granger, Harvey, Le Roux, Rattray: carry, momentum and value, as
directional or cross-asset implementations). The systematic charter (pack/CHARTER_DIGEST.md) found that its seven
source notes give NO thesis for the existing Carry and Value pods. Write ONE thesis note that (a) supplies or refuses a
thesis for Carry and for Value from these two papers, (b) says whether cross-sectional momentum (ranking markets
against each other) is a version of the Trend pod or a separate mechanism, and (c) says which implementation
(directional, i.e. each market against its own past, or cross-asset, i.e. markets ranked against each other) each
pod should register as versions. This is judgement on source logic only. Be meticulous and self-checking; "the papers
do not establish this" is a valid finding.

## Inputs (read all of pack/; work dir: <work dir>)
1. pack/WORKFLOW_sections_1-6.md: the shop's rules. Rule 2 (versions averaged, list fixed at registration, no picking),
   rule 5 (holdout verdict only for theses documented before 2011), rule 7 (live source for every input), sections 5-6.
2. pack/BRIEF_V2_RULES.md: binding. Quotes are the ground truth; a number that appears only in a summary field cannot
   support a grade or a test premise.
3. pack/QP15.json, QP08.json: every claim with its VERBATIM "quote" (ground truth) plus machine summaries (claim,
   exact_rule, reported_result, mechanism: may be wrong) and a machine-written reasoning map. Read all claims.
4. pack/CHARTER_DIGEST.md: the charter's verdict, pods, version grids and open points, and the verdict of thesis note
   1.3a (rates and curve). Its numbers are not ground truth for this note.
5. pack/DATA_AVAILABILITY.md: history and live sources in hand.
No code reading. No backtests, no data, never 2011-2026 results.

## Hard rules
- Verify every statement and number you rely on against the QUOTE of its claim id; cite claim ids. Label each
  statement SHOWN (the quote gives a test with numbers), SHOWN (words) (the quote reports a test's outcome, its numbers
  are summary only), ASSERTED (no test), or reader (your inference). A number only in a summary field is written
  "(summary only)" and nothing is built on it.
- One mechanism per pod: who is on the other side and why they keep paying. Where the papers offer several rival
  explanations (risk, behaviour, funding liquidity), state them as rivals and say what each predicts differently; do
  not blend. A regularity without a stated counterparty is "pattern, no mechanism".
- Judge the evidence as a risk officer would: sample period, in-sample vs out-of-sample, transaction costs, whether
  results are for individual stocks or for the asset classes this shop trades (keep the two apart in every row),
  how many variants were tried, the authors' own caveats, and that both author groups work for firms that sell these
  strategies.
- No decisions or routes for the user. An open design choice becomes a version in the grid (averaged), a zero-slot
  diagnostic with a gate fixed now, or is dropped with a reason.
- Version dimensions need a stated reason for model uncertainty, not an expected gain. Keep grids small. The charter
  already gives Carry 2 versions and Value 1: say exactly what changes, if anything, and why.
- Rule 5: state for each pod whether the thesis was documented before 2011, with the publication and its year as the
  pack gives it (quotes, sample end, coverage notes). If the pack does not date a paper, write "not dated in the pack"
  and give what the sample period implies; mark anything from your own knowledge "(author's knowledge)".
- Plain language, short sentences; explain any term a non-specialist would not know in a few words.

## Output: write <work dir>/fable_work/THESIS_1.3_xs.md (about 3,000-4,000 words)
1. Verdict in at most eight lines: the thesis for Carry, the thesis for Value, the answer on cross-sectional momentum,
   what changes in the charter's pods or grids, the single weakest link.
2. What the two papers establish: one table, most important first (at most 22 rows): statement; label; claim ids; the
   quoted words or numbers that carry it; asset classes it covers (stocks / country indexes / currencies / bonds /
   commodities); limits (sample, costs, in or out of sample).
3. Pods. For each of Carry, Value, cross-sectional momentum, and any other candidate the papers support (include
   candidates you reject, with the reason): the mechanism chain and the other side, with rival explanations kept apart;
   evidence grade (strong / moderate / weak / none) with the reason; the rule family in one precise paragraph
   (markets, signal definition per asset class, directional vs cross-asset form, ranking and weighting, rebalance,
   risk scaling); version grid (dimension, levels, count; all averaged) and what is fixed; data (history source and
   start, live source, what is missing: check each signal's inputs against the data sheet); when it stops working;
   relation to the other pods (including the negative correlation of value and momentum, if the quotes show it, and
   what that implies for how the book is tested); rule 5 status; batch (existing book, A, B1, B2, or not now).
4. The directional vs cross-asset question: what QP08 shows per style, and the resulting registration per pod.
5. Diagnostics: at most three zero-slot diagnostics on design months (question; computation in two sentences; data;
   the gate as a rule fixed now, free of hidden choices). None if none is justified.
6. Numbers used, each with claim id and status (in quote / summary only).
7. What the Opus check should look at first; what the papers leave unanswered.
8. Pack problems: contradictions inside the pack (paper vs paper, summary vs quote, pack vs charter digest, data sheet
   vs a paper's data need).
9. Self-check: the strongest argument against each thesis you supply and against each rejection.
Write scratch files only inside <work dir>/fable_work. Do not spawn agents.
Reply with section 1, the pod list with grade and batch, the number of diagnostics, and the word count.
