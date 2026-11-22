# Independent check of playbook card 1.4 #5 (commodity balances: Pierre Andurand), brief of 2026-11-21

A Fable run wrote a playbook card from interview claims of Pierre Andurand:
/tmp/claude-0/-home-claude/a8a60852-162d-5d9b-8463-3f9415508c73/scratchpad/card_1.4_andurand/fable_work/CARD_1.4_commodity_balances.md. You are the independent checker (quant and risk officer). Do not defend it.
Verify it against the verbatim quotes and list exact corrections. "Cannot verify" is a valid result.

Work dir: /tmp/claude-0/-home-claude/a8a60852-162d-5d9b-8463-3f9415508c73/scratchpad/card_1.4_andurand (write only inside opus_work/; do not edit the card or the pack; do not read fable_work/ scratch files).
No code reading, no backtests, no web. Do not spawn agents.

## Inputs
1. The card and its author's brief (/tmp/claude-0/-home-claude/a8a60852-162d-5d9b-8463-3f9415508c73/scratchpad/card_1.4_andurand/BRIEF_FABLE.md).
2. The pack (/tmp/claude-0/-home-claude/a8a60852-162d-5d9b-8463-3f9415508c73/scratchpad/card_1.4_andurand/pack/): ground truth = the "quote" field of CLAIMS.json; everything else is machine-written.
3. Tools: /tmp/claude-0/-home-claude/a8a60852-162d-5d9b-8463-3f9415508c73/scratchpad/card_1.4_andurand/tools/lookup.py (use it for every id cited); /tmp/claude-0/-home-claude/a8a60852-162d-5d9b-8463-3f9415508c73/scratchpad/card_1.4_andurand/opus_work/apply_check.py.

## Checks
A. Numbers: every number in the card: in quote / summary only / contradicted / not found.
B. Causal chains and indicators: does the cited quote say it, by that man, at that date? Label justified? Are the two
   speakers, the firm framework and personal views kept apart?
C. Rules: for each rule, is every element (series, threshold, lookback, action, holding, lag) either in a quote or an
   explicit version grid with a reason; any hidden choice; any look-ahead; is the series really on the data sheet;
   does the cited quote support the direction of the trade?
D. Read ALL 201 quotes: list quotes that contradict the card, important ideas of either man the card omits, and any
   statement by one speaker attributed to another; rules duplicating cards 1-4 (pack/DIGEST.md sections D-G) or the commodity Trend / Carry pods; any rule needing data the sheet lacks; anything resting on MT115 without its identity flag.
E. Dating table: does each "documented before 2011" rest on words in the quote?
F. Rules of the shop: no decision handed to the user; versions averaged; every open choice is a version, a diagnostic
   with a fixed gate, or dropped; analyst questions answerable and scoreable; forecasts really open and dated.

## Output: /tmp/claude-0/-home-claude/a8a60852-162d-5d9b-8463-3f9415508c73/scratchpad/card_1.4_andurand/opus_work/CHECK_1.4_andurand.md
1. Verdict: PASS / PASS WITH CORRECTIONS / FAIL in five lines with counts.
2. Findings A to F.
3. Required corrections (heading exactly "## 3. Required corrections"): numbered 1., 2., ...; each item one line of
   description, then exactly these two lines, then a line starting "Reason:":
   - Find: `<words copied verbatim from the card, one line, occurring exactly once, no backticks>`
   - Replace: `<replacement, one line, no backticks>`
   Then run python3 /tmp/claude-0/-home-claude/a8a60852-162d-5d9b-8463-3f9415508c73/scratchpad/card_1.4_andurand/opus_work/apply_check.py until it prints ALL PAIRS APPLIED; read the changed passages in
   opus_work/note_corrected_preview.md.
4. Open judgement points (heading "## 4. Open judgement points"), one line each.
5. What you could not verify.
Reply with section 1, the number of corrections, the open judgement points, and the three most important findings of D.
