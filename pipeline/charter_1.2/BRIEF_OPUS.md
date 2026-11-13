# Independent check of the systematic charter (WORKFLOW step 1.2), brief of 2026-11-13

A Fable run consolidated seven foundation notes into a charter: <work dir>/fable_work/CHARTER_1.2.md.
You are the independent checker (quant and risk officer). You did not write it; do not defend it. Your job is to
verify it against the verbatim quotes and our code, read two sources the charter's author never saw, and list exact
corrections. Be meticulous; "cannot verify" is a valid result, a guess is not.

Work dir: <work dir> (write only inside opus_work/; do not edit the charter, the pack or the repo).

## Inputs
1. The charter (read all of it first), and the brief its author had: <work dir>/BRIEF_FABLE.md.
2. The author's pack: <work dir>/pack/ (WORKFLOW sections 1-6, v2 rules, AUDIT_1.1, the seven notes, QUEUED_TESTS,
   VARIANTS, engine change log, data sheet).
3. The verbatim quotes, which the author did NOT have: <work dir>/opus_sources/U02.json .. U07.json (per unit: "claims" = list
   of {claim_id, speaker, quote, claim, ...}; the "quote" field is the ground truth, script-checked against the
   transcripts; "claim" and other fields are machine summaries and may be wrong), QP01.json (the AQR Economic Trend paper
   behind note U01; same claim layout). Write a small lookup script in opus_work/ (claim id -> quote) and use it for
   every id; do not rely on the summary fields.
4. Two sources outside the charter: <work dir>/opus_sources/U08.json (Eckhardt, transcript MT020, 55 claims with quotes) and
   <work dir>/opus_sources/QP09.json (Fung and Hsieh, "The Risk in Hedge Fund Strategies: Theory and Evidence from Trend
   Followers", 149 claims with quotes, plus "reasoning").
5. Our code, read only: /home/claude/stock-screener/gm/ and docs/research/global_macro/TESTING_PROTOCOL.md.

## Hard rules
- No backtests, no code that loads returns or prices, never the 2011-2026 holdout. Reading code, docs and the JSON
  claim files is fine.
- Quotes are the ground truth. A number that appears only in a summary field, not in the quote, is "summary only".
- Do not spawn other agents.

## Checks
A. Numbers. For every number the charter keeps from the notes (its section 7, plus any number elsewhere in the text
   that comes from a source): find the claim id's quote. Verdict per number: in quote / summary only / contradicted
   (give the quote's words) / claim id not found / no claim id given. Numbers from our code or docs: open the file:line
   and confirm.
B. Statements. For every row of the established-vs-asserted table and every pod mechanism chain: do the cited quotes
   say it? Is the label right (SHOWN needs a test with numbers in the quote; interviews are mostly ASSERTED)? Verdict
   per row: supported / partly (say what is missing) / not supported / contradicted.
C. Diagnostic premises. For every diagnostic kept: is the premise supported by the quotes of the claim ids named? Does
   the code at each file:line exist and do what the charter says, so the computation is possible without new data? Is
   the gating rule fixed and free of a hidden choice? A premise that fails goes on a "must not be registered as
   written" list with the reason.
D. Pre-2011 documentation. For each pod's claim that its thesis was documented before 2011: is there a dated,
   published source named? Mark each: established (name the publication and year) / plausible but not shown in our
   material / wrong. Use only what the pack, the quotes and your own certain knowledge of the published literature
   support; mark the last kind "(checker's knowledge)".
E. Completeness and rules. All 34 queued proposals accounted for (kept, merged, dropped, deferred)? Every VARIANTS
   dimension and level mapped? Any decision handed to the user? Any place where versions are picked, not averaged?
   Any pod with more than one mechanism blended? Does the data table agree with pack/DATA_AVAILABILITY.md, and is every
   pod without a live source for an input flagged as not Core-eligible? Any error of the Carver note (AUDIT_1.1) carried?
F. Eckhardt (MT020) and Fung and Hsieh (QP09). Read both in full (quotes). List every point where either contradicts,
   qualifies or sharpens a charter statement, pod mechanism, version grid or diagnostic; cite claim ids and the quoted
   words. Say also what they add that the charter lacks (at most five points each), each labelled SHOWN / ASSERTED.
   For Fung and Hsieh pay attention to: the option-like (lookback straddle) payoff of trend followers, what that
   implies for judging a trend pod by Sharpe, for the "crisis" behaviour, and for which factors a trend pod should be
   compared with.

## Output: <work dir>/opus_work/CHECK_1.2.md
1. Verdict: PASS / PASS WITH CORRECTIONS / FAIL, in five lines, with counts (numbers checked: in quote / summary only /
   contradicted / not found; statements: supported / partly / not supported / contradicted; premises: ok / must not be
   registered as written).
2. Table A (numbers), Table B (statements), Table C (diagnostic premises and code references), Table D (pre-2011).
3. E findings as a list.
4. F: contradictions and additions from Eckhardt and from Fung and Hsieh.
5. Required corrections: a numbered list; each gives the charter location (section and the words to find), the exact
   replacement text, and the reason with the claim id and quoted words. Keep judgement changes (a pod should not exist,
   a grid should change) separate under "Open judgement points", not as corrections.
6. What you could not verify and why.
Reply with section 1, the number of required corrections, the open judgement points in one line each, and the three
most important findings from F.
