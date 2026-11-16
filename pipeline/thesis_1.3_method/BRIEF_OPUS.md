# Independent check of the testing-method thesis note (WORKFLOW step 1.3), brief of 2026-11-15

A Fable run wrote a thesis note from one deck of teaching slides (QP13, Stine): <work dir>/fable_work/THESIS_1.3_method.md.
It judges our test sheet and adoption protocol against the slides and proposes protocol items and diagnostics. You are
the independent checker (quant and risk officer). You did not write it; do not defend it. Verify it against the slide
text and the verbatim quotes and list exact corrections. "Cannot verify" is a valid result; a guess is not.

Work dir: <work dir> (write only inside opus_work/; do not edit the note or the pack). No code reading, no backtests, no
market data, never 2011-2026 results. Do not spawn agents.

## Inputs
1. The note (read all of it first) and its author's brief: <work dir>/BRIEF_FABLE.md.
2. The pack the author had: <work dir>/pack/. Ground truth = QP13_slides_text.md (the slides themselves) and the
   "quote" field of each claim in QP13.json (a fragment of the slide text); every other field of QP13.json is a machine
   summary and may be wrong. Our own rules: WORKFLOW_sections_1-6.md, TESTING_PROTOCOL.md, BRIEF_V2_RULES.md (with the
   extension stated in the author's brief: a number on a slide but outside a quote is "on slide" and counts as in the
   source). CHARTER_DIGEST.md and BOOK_FACTS_design_era.md are repo extracts (design months only).
3. Tools: <work dir>/tools/lookup.py (claim id -> quote; --slide Cnn; --grep "words"). Use it for every id and slide
   cited. <work dir>/opus_work/apply_check.py (see Output 3).

## Checks
A. Numbers: every number in the note that comes from the slides, from the repo extracts, or from the note's own
   arithmetic. Verdict per number: in quote / on slide / summary only / repo result (matches the pack) / contradicted
   (give the source's words) / not found. Recompute every piece of arithmetic and give your result.
B. Statements and labels: every row of the "what the slides establish" table. Do the slides say it? Is SHOWN justified
   by a derivation, a constructed example or a result with numbers on the slides? Does the row state its limits
   honestly (assumptions, constructed against real data, number of cases)? Verdict: supported / partly / not supported
   / contradicted.
C. Element table: for each element, (i) does the note state our own rule correctly (compare with the pack's words in
   WORKFLOW and TESTING_PROTOCOL), and (ii) is its verdict (supports / contradicts / silent / adds a check) supported by
   the slides? Then read ALL 72 claims and the whole slide text and list everything in the slides that bears on our
   test sheet, protocol or sizing that the note does not mention, and everything that weakens a proposal of the note.
D. Proposals: for each protocol item and each diagnostic: is it precise enough to register or run without a hidden
   choice; free of look-ahead; is the gate fixed; does it say decisive or reported-only, the effect on the pass
   chance, and what the power check (step 3.3) must simulate; is it redundant with an existing test; does it respect
   the shop's rules (fixed budget, versions averaged, no new decisive test without the power check)?
E. Rules of the shop: no decision handed to the user; every proposal is exactly one of protocol item, zero-slot
   diagnostic with a fixed gate, or dropped with a reason; nothing claimed as registered or run; no 2011-2026 result;
   statements from the author's own knowledge are flagged and nothing is built on them; the two attributions in
   TESTING_PROTOCOL ("Stine 2009" for the tail test; "Foster-Stine value-add test") are judged against the slides.
   Add what you know with certainty about the cited paper (Foster, Stine, Young) and about the inequality the test
   rests on, marked "(checker's knowledge)".
F. The martingale-test section: are the assumptions those on the slides; is each open choice (what plays the market
   and beta, the scale at which returns are compounded, the data frequency, look-ahead in any estimate, the count for
   multiplicity) closed by a cited slide, closed by a rule with a reason, or reported as unanswered; is the
   detectable-effect arithmetic right; is the status the note gives the test consistent with that arithmetic and with
   the slides' own remarks on power and multiplicity?

## Output: <work dir>/opus_work/CHECK_1.3_method.md
1. Verdict: PASS / PASS WITH CORRECTIONS / FAIL in five lines with counts (numbers; statements; elements; proposals
   whose status you would change).
2. Tables A, B; findings C, D, E, F as lists.
3. Required corrections (the heading must read exactly "## 3. Required corrections"): numbered 1., 2., ...; each item
   is one line of description, then exactly these two lines, then a line starting "Reason:" with the claim id or slide
   and the quoted words:
   - Find: `<words copied verbatim from the note, on one line, occurring exactly once in the note, no backticks>`
   - Replace: `<the replacement text, on one line, no backticks>`
   Keep each Find as short as uniqueness allows. A correction that needs two places is two items. Then run
   python3 <work dir>/opus_work/apply_check.py: it must print ALL PAIRS APPLIED (fix the pairs until it does). It writes
   opus_work/note_corrected_preview.md; read the changed passages there once to confirm they read correctly.
4. Open judgement points (not corrections), one line each (heading "## 4. Open judgement points").
5. What you could not verify.
Reply with section 1, the number of required corrections, the open judgement points, and the three most important
findings from C.
