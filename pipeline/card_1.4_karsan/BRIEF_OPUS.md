# Independent check of playbook card 1.4 #4 (flows and volatility: Cem Karsan), brief of 2026-11-21

A Fable run wrote a playbook card from interview claims of Cem Karsan:
<work dir>/fable_work/CARD_1.4_flows_volatility.md. You are the independent checker (quant and risk officer). Do not defend it.
Verify it against the verbatim quotes and list exact corrections. "Cannot verify" is a valid result.

Work dir: <work dir> (write only inside opus_work/; do not edit the card or the pack; do not read fable_work/ scratch files).
No code reading, no backtests, no web. Do not spawn agents.

## Inputs
1. The card and its author's brief (<work dir>/BRIEF_FABLE.md).
2. The pack (<work dir>/pack/): ground truth = the "quote" field of CLAIMS.json; everything else is machine-written.
3. Tools: <work dir>/tools/lookup.py (use it for every id cited); <work dir>/opus_work/apply_check.py.

## Checks
A. Numbers: every number in the card: in quote / summary only / contradicted / not found.
B. Causal chains and indicators: does the cited quote say it, by that man, at that date? Label justified? Are the two
   speakers, the firm framework and personal views kept apart?
C. Rules: for each rule, is every element (series, threshold, lookback, action, holding, lag) either in a quote or an
   explicit version grid with a reason; any hidden choice; any look-ahead; is the series really on the data sheet;
   does the cited quote support the direction of the trade?
D. Read ALL 785 quotes: list quotes that contradict the card, important ideas of either man the card omits, and any
   statement by one speaker attributed to another; rules duplicating cards 1-3 (pack/DIGEST.md sections C-E) or the systematic pods; any rule that needs options data the data sheet lacks.
E. Dating table: does each "documented before 2011" rest on words in the quote?
F. Rules of the shop: no decision handed to the user; versions averaged; every open choice is a version, a diagnostic
   with a fixed gate, or dropped; analyst questions answerable and scoreable; forecasts really open and dated.

## Output: <work dir>/opus_work/CHECK_1.4_karsan.md
1. Verdict: PASS / PASS WITH CORRECTIONS / FAIL in five lines with counts.
2. Findings A to F.
3. Required corrections (heading exactly "## 3. Required corrections"): numbered 1., 2., ...; each item one line of
   description, then exactly these two lines, then a line starting "Reason:":
   - Find: `<words copied verbatim from the card, one line, occurring exactly once, no backticks>`
   - Replace: `<replacement, one line, no backticks>`
   Then run python3 <work dir>/opus_work/apply_check.py until it prints ALL PAIRS APPLIED; read the changed passages in
   opus_work/note_corrected_preview.md.
4. Open judgement points (heading "## 4. Open judgement points"), one line each.
5. What you could not verify.
Reply with section 1, the number of corrections, the open judgement points, and the three most important findings of D.
