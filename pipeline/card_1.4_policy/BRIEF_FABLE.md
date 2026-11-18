# Fable unit 1.4, card 1: playbook card "policy and liquidity" (Druckenmiller, Bessent), brief of 2026-11-17

You are the strategist of a small systematic-macro shop run as pods (read pack/WORKFLOW_sections_1-6.md first; step 1.4
defines a playbook card: causal model, indicators with exact series, if-then rules, dated forecasts, what would prove it
wrong). A card feeds a discretionary pod with two layers: a RULE layer (coded, backtested, flagged for hindsight) and an
ANALYST layer (a weekly agent answering fixed questions, judged on its live record only). Write ONE card from what
Stanley Druckenmiller and Scott Bessent actually say in the pack. Be meticulous and self-checking. "They do not say
this" and "this cannot be coded" are valid findings.

## Inputs (work dir: <work dir>; read all of pack/)
1. pack/WORKFLOW_sections_1-6.md: rules of the shop (rule 5: holdout verdict only for theses documented before 2011).
2. pack/BRIEF_V2_RULES.md: binding.
3. pack/CLAIMS.json: 590 claims by the two men from 11 recordings (2018-2026), each with its VERBATIM quote, source
   date and machine summaries (may be wrong). Read every claim. pack/SOURCES.md lists the recordings.
4. pack/FORECASTS.csv: their dated views as coded for the forecast ledger (machine-coded; scored columns descriptive).
5. pack/DIGEST.md: verdicts of the charter and thesis notes 1.3a-c; scorecard lines. Not ground truth.
6. pack/DATA_SHEET.md: the only series the live cycle can observe today.
7. Tool: <work dir>/tools/lookup.py (claim id -> quote; --grep "words"; --source MTnnn). Check every id and quoted phrase.
No code reading, no backtests, no web, no results of our own book.

## Hard rules
- Quotes are ground truth. Label statements SHOWN (the speaker gives numbers or a worked case in the quote), SHOWN
  (words), ASSERTED, or reader (your inference). Numbers: "in quote" or "summary only" (cannot carry a rule).
- These are interviews by two famous investors recalling their wins. Judge them as a risk officer: a recalled trade
  shows that something happened once, not how often; nobody reports the trades that failed unless he says so.
- Keep the two men apart, and each man by period, wherever they differ. Bessent's 2026 recording is a Treasury
  Secretary speaking: treat policy statements there as an official's, not an investor's.
- A rule-layer rule must be codable without a hidden choice: exact series id from the data sheet (or it is not a
  rule), threshold, lookback, action (which markets, which direction), holding rule, release lag. A threshold must
  come from a quote; where the men give only a direction, the threshold is a small version grid you fix now with a
  reason, all versions averaged. If a rule cannot be made exact from the pack, it goes to the analyst layer as a
  question, or is dropped with a reason.
- No decisions for the user. Open choices become versions, a zero-slot diagnostic with a gate fixed now (design
  months to 2010-12), or are dropped with a reason.
- Dating (rule 5): the recordings are from 2018 to 2026. For each thesis say whether the QUOTE itself documents that
  the man held it before 2011 (he describes acting on it then). Otherwise flag hindsight.
- Plain language, short sentences. No backticks in the card.

## Output: write <work dir>/fable_work/CARD_1.4_policy_liquidity.md (about 3,000-4,000 words)
1. Verdict in at most eight lines: what the playbook is; how much of it can be coded; the strongest and the weakest
   link; number of rules, analyst questions, open forecasts, diagnostics.
2. Causal model: at most eight chains (cause -> ... -> market effect), each with who is on the other side, the man
   and period, claim ids, label, limits.
3. Indicators: one table (indicator; who uses it and how, with claim ids; exact series from the data sheet or "no
   live series"; release lag).
4. Rule layer: at most six rules, numbered R1.., each fully specified as above, with claim ids, the version grid,
   what it trades, hindsight flag, and the reason it is not already in the systematic pods (trend, carry, value,
   economic trend).
5. Analyst layer: at most ten fixed weekly questions (answerable from public information, each with the answer
   format and how it will be scored).
6. Process rules that are not signals (sizing, concentration, when to cut, time horizon): what they say, labels, and
   whether each is a registered rule for the pod, a version, or dropped.
7. Dated forecasts still open (for the forecast ledger): statement, date made, horizon, how it resolves, claim ids.
8. What would prove the playbook wrong; when it should stop working; where the two men disagree with each other or
   with their own earlier statements.
9. Dating table for rule 5.
10. Diagnostics (zero slots), at most two, with gates fixed now. None if none is justified.
11. Dropped ideas, one line each with the reason.
12. Numbers used with status; pack problems; what the Opus check should look at first.
13. Self-check: the strongest argument against each rule.
Write scratch files only inside fable_work/. Do not spawn agents.
Reply with section 1, one line per rule, and the word count.
