# Independent check of the rates and curve thesis note (WORKFLOW step 1.3), brief of 2026-11-14

A Fable run wrote a thesis note from three papers: <work dir>/fable_work/THESIS_1.3_rates.md. You are the independent checker
(quant and risk officer). You did not write it; do not defend it. Verify it against the verbatim quotes and list exact
corrections. "Cannot verify" is a valid result; a guess is not.

Work dir: <work dir> (write only inside opus_work/; do not edit the note or the pack). No code reading, no backtests, no market
data, never 2011-2026 results. Do not spawn agents.

## Inputs
1. The note (read all of it first) and its author's brief: <work dir>/BRIEF_FABLE.md.
2. The pack the author had: <work dir>/pack/ (QP06.json, QP07.json, QP12.json with every claim's verbatim "quote" = ground truth;
   the other fields are machine summaries and may be wrong; WORKFLOW sections 1-6; v2 rules; charter digest; deferred
   proposals; data sheet). Write a small lookup script in opus_work/ (claim id -> quote) and use it for every id cited.

## Checks
A. Numbers: every number in the note that comes from a paper. Verdict: in quote / summary only / contradicted (give the
   quote's words) / claim id not found / no claim id given.
B. Statements and labels: every row of the "what the papers establish" table and every mechanism chain. Do the quotes
   say it? Is SHOWN justified by a test with numbers in the quote? Verdict: supported / partly / not supported /
   contradicted.
C. Evidence judgement: for each pod grade, is it consistent with what the quotes show about sample period, in-sample vs
   out-of-sample, transaction costs, risk adjustment, number of variants tried and the authors' own caveats? Read ALL
   claims of the three papers and list every quote that weakens or contradicts a pod the note proposes and that the
   note does not mention.
D. Rule specification: is each rule family precise enough to build without a hidden choice, and free of look-ahead (how
   the "normal" curve or model parameters are estimated)? Is each gate of a diagnostic fixed and free of a hidden choice?
E. Rules of the shop: versions averaged, not picked; no decision handed to the user; one mechanism per pod; each version
   dimension has a stated model-uncertainty reason; data table agrees with pack/DATA_AVAILABILITY.md; every pod without a
   live source for an input is flagged as not Core-eligible; rule 5 dating is supported by the pack (or marked as the
   author's knowledge). For rule 5 add what you know with certainty about each paper's publication (journal, year),
   marked "(checker's knowledge)".
F. The two deferred proposals: is the fate the note gives each one supported by the quotes?

## Output: <work dir>/opus_work/CHECK_1.3_rates.md
1. Verdict: PASS / PASS WITH CORRECTIONS / FAIL in five lines with counts (numbers; statements; pods whose grade you
   would change).
2. Tables A, B; findings C, D, E, F as lists.
3. Required corrections: numbered; each gives the location (section and the exact words to find, copied verbatim from the
   note so a script can find them), the exact replacement text, and the reason with claim id and quoted words.
4. Open judgement points (not corrections), one line each.
5. What you could not verify.
Reply with section 1, the number of required corrections, the open judgement points, and the three most important
findings from C.
