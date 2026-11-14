# Fable unit 1.3a: thesis note, rates and curve (WORKFLOW step 1.3), brief of 2026-11-14

You are the strategist of a small systematic-macro shop run as pods (read pack/WORKFLOW_sections_1-6.md first; step 1.3:
"per candidate pod: mechanism, rule family, version grid, data, when it stops working"). Three papers by one author
group propose trading the yield curve: QP06 (mean-reverting yield-curve strategies), QP07 (predicting short-term
Eurodollar futures), QP12 (modelling the yield curve, cash rates and commodity futures in one framework). Write ONE
thesis note that says which rates/curve pods, if any, the shop should spec, exactly enough for a builder to write the
spec, and what the papers do and do not establish. This is judgement on source logic only. Be meticulous and
self-checking; "the papers do not establish this" is a valid finding.

## Inputs (read all of pack/; work dir: <work dir>)
1. pack/WORKFLOW_sections_1-6.md: the shop's rules. Rule 2 (versions averaged, list fixed at registration, no picking),
   rule 5 (holdout verdict only for theses documented before 2011), rule 7 (live source for every input), sections 5-6
   (budget: new pods go to Batch B1/B2).
2. pack/BRIEF_V2_RULES.md: binding. Quotes are the ground truth; a number that appears only in a summary field cannot
   support a grade or a test premise.
3. pack/QP06.json, QP07.json, QP12.json: every claim with its VERBATIM "quote" (ground truth) plus machine summaries
   (claim, exact_rule, reported_result, mechanism: may be wrong) and a machine-written reasoning map. Read all claims.
4. pack/CHARTER_DIGEST.md: the systematic charter (existing pods Trend, Economic trend, Carry, Value; new Curve carry;
   open points). pack/DEFERRED_PROPOSALS.md: two proposals the charter sent to this note (short-rate futures as markets;
   a spread gate). Their numbers are unverified.
5. pack/DATA_AVAILABILITY.md: history and live sources in hand.
No code reading. No backtests, no data, never 2011-2026 results.

## Hard rules
- Verify every statement and number you rely on against the QUOTE of its claim id; cite claim ids. Label each
  statement SHOWN (the quote gives a test with numbers), ASSERTED (no test), or reader (your inference). If a number is
  only in a summary field, write "(summary only)" and do not build on it.
- One mechanism per pod: who is on the other side and why they keep paying. A statistical regularity without a
  stated counterparty is "pattern, no mechanism" and says so.
- Judge the evidence as a risk officer would: sample period, in-sample vs out-of-sample, transaction costs, whether
  payoffs are risk-adjusted, how many variants the authors tried, whether the trade is implementable with the
  instruments named, whether the authors' own caveats limit it. Say what would have to be true for it to be an artefact.
- No decisions or routes for the user. An open design choice becomes a version in the grid (averaged), a zero-slot
  diagnostic with a gate fixed now, or is dropped with a reason.
- Version dimensions need a stated reason for model uncertainty, not an expected gain. Keep grids small.
- Rule 5: state for each pod whether the thesis was documented before 2011, with the publication and its year as
  the pack gives it (date fields, quotes, sample end). If the pack does not date the paper, write "not dated in the
  pack" and give what the sample period implies; mark anything from your own knowledge "(author's knowledge)".
- Plain language, short sentences; explain any term a non-specialist would not know in a few words.

## Output: write <work dir>/fable_work/THESIS_1.3_rates.md (about 2,500-4,000 words)
1. Verdict in at most eight lines: which pods to spec, which not, the single weakest link.
2. What the three papers establish: one table, most important first (at most 20 rows): statement; label; claim ids;
   the quoted words or numbers that carry it; limits (sample, costs, in/out of sample).
3. Candidate pods. For each (include candidates you reject, with the reason): name; mechanism chain and the other side;
   evidence grade (strong / moderate / weak / none) with the reason; the rule family in one precise paragraph
   (instruments, signal, how the "normal" curve is estimated without look-ahead, entry and exit, holding period,
   weighting, risk scaling); version grid (dimension, levels, count; all averaged); what is fixed; data (history source
   and start, live source, what is missing); when it stops working; relation to existing pods (is it a version of
   Carry or Value on a new market set, or a separate mechanism?); rule 5 status; batch (B1, B2, or not now).
4. The two deferred proposals: for each, registered as what (markets added to an existing pod / a gate / dropped), with
   the reason from the papers' quotes.
5. Diagnostics: at most three zero-slot diagnostics on design months (question; computation in two sentences; data
   needed; the gate as a rule fixed now). None if none is justified.
6. Numbers used, each with claim id and status (in quote / summary only).
7. What the Opus check should look at first; what the papers leave unanswered.
8. Pack problems: contradictions inside the pack (paper vs paper, summary vs quote, pack vs charter, data sheet vs a
   paper's data need).
9. Self-check: the strongest argument against each pod you propose and against each rejection.
Write scratch files only inside <work dir>/fable_work. Do not spawn agents.
Reply with section 1, the pod list with grade and batch, the number of diagnostics, and the word count.
