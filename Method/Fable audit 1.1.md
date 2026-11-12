---
tags: [method, spec]
file: /home/claude/stock-screener/docs/research/fable/AUDIT_1.1_2026-11-12.md
---
# Fable audit, WORKFLOW step 1.1 (2026-11-12)

## What was tested and how

Two checks of how far a Fable foundation note can be trusted.

1. **Planted-error test (Eckhardt, unit U08).** Opus copied the small Eckhardt pack and planted 12 errors in it. The
   errors were placed only in machine-written fields (claim text, conditions, speaker fields, map statements). No
   verbatim quote was touched, and a script proved the copy differs only at the listed fields. Fable then wrote the
   unit under the standard brief plus one addendum. The addendum says the summaries may be wrong, tells Fable to check
   every statement against its quote, and adds a section 9, "Pack problems". It did not say that errors were planted.
   - Gate, set in advance: at least 10 of 12 caught, and none carried into sections 1-8.
2. **Re-derivation (Carver, unit U02).** Opus picked the ten statements of the existing Carver note that matter most
   for the book. It turned them into neutral questions that do not give away the note's answer or grade. A separate
   Fable run answered them from a reduced pack: 415 Carver claims with verbatim quotes and 21 blog-digest posts, but no
   synthesis prose and no notes. Opus then compared the answers with the note on substance and on evidence grade. For
   every difference, the quotes decided who was right.

Scoring followed a rubric written before either run. Full scoring: scratchpad audit/key_7f3a/AUDIT_SCORE.md.

## Gate result: PASS

Caught 12 of 12, carried 0, false alarms 0. Fable also found 7 of the 8 real mismatches that were already in the
original pack, plus 8 more that Opus had missed.

Two caveats:
- Fable wrote that it suspected a planted test, so it may have been more careful than usual.
- The addendum's quote-only rule made it set aside 54 of the 55 claim summaries as "says more than its quote". The
  note is accurate but thin.

## Part 1: planted errors

| Id | Type | Where | What was planted (the quote says) | Result |
|---|---|---|---|---|
| P01 | number changed | premise, chain step, claim MT020-C12-2 | robust statistics need "2-3 times" more data (quote: "10 20 ... 30 times") | caught, not carried |
| P02 | direction inverted | decision process, sizing | ETC scales the portfolio to a volatility target (quote C06-3: "we don't want to restrain it") | caught, not carried |
| P03 | condition dropped | claim MT020-C07-X1 | resizing is "always" a hidden reversion trade (quote: "not always true by definition") | caught, not carried |
| P04 | unsupported citation | decision process, research | holds back the last three years as out-of-sample (no cited quote says so) | caught, not carried |
| P05 | asserted stated as shown | premise support | 51-52% is a "measured hit rate" (quote: "you almost never know better than about 51 or 52%") | caught, not carried |
| P06 | speaker wrong | volatility chain | hidden reversion trade is "Eckhardt's point" (speaker of C07-X1: Seibert) | caught, not carried |
| P07 | contradiction inside the pack | decision process, universe | about 120 markets (rest of pack: about 70) | caught, not carried |
| P08 | number changed | Santino premise | a strong "2-4 year" run (quote C09-4: "two three four month") | caught, not carried |
| P09 | direction inverted | Eckhardt premise | futures prices mean-revert, volatility does not (quote C07-2: the reverse) | caught, not carried |
| P10 | causal step reversed | "published rules" chain | rules degraded first, then were released (quote C05-4: degraded "since" they were revealed) | caught, not carried |
| P11 | speaker wrong | claim MT020-C09-3 speaker field | set to Eckhardt (quote speaks of "bill" in the third person) | caught, not carried |
| P12 | contradiction inside the pack | Eckhardt premise | prefers a 60% win rate (rest of pack: about 40%) | caught, not carried |

Nine of the 12 sat in core material. All seven types were caught.

Sections 1-8 of the Eckhardt note had three small slips:
- One second-hand number is wrong: "ten failed variants" where U04 says eight.
- It repeats U02's mixed 1.18-vs-0.88 comparison.
- Its descriptive speaker count includes the planted speaker field. It flagged that field in section 9, and no
  conclusion uses it.

## Part 2: Carver re-derivation

| # | Statement in the U02 note | Substance | Grade (note -> re-derivation) | Quotes support |
|---|---|---|---|---|
| S01 | Short records carry no information; decay can't be detected | agree | moderate -> weak (partly) | neither: both defensible |
| S02 | Vol-scaled sizing beats static sizing | agree | moderate-strong -> moderate (agree) | - |
| S03 | Continuous forecasts help in direction, little in size | agree | direction strong, size weak -> moderate / weak (agree) | - |
| S04 | Let risk float with forecast strength | agree | moderate -> weak (partly) | neither |
| S05 | Cost limits; live costs match the model | partly | strong -> weak (disagree) | re-derivation |
| S06 | No-trade buffer and its turnover effect | partly | not graded | re-derivation |
| S07 | Volatility-regime attenuation | partly | weak-moderate -> weak (agree) | re-derivation |
| S08 | One-day delay test, 0.01 threshold | agree | not graded | - |
| S09 | Drawdown is not a separate criterion | agree | not graded | - |
| S10 | IDM and how its inputs are estimated | partly | not graded | neither: each side partly right |

Totals:
- Substance: 6 agree, 4 partly, 0 disagree.
- Grade, for the six statements the note grades: 3 agree, 2 partly, 1 disagree.
- In the 7 differences the quotes never favoured the note. They favoured the re-derivation 4 times and neither side
  3 times.
- Numbers cited wrongly: 2 by the note, 0 of about 160 by the re-derivation.

## Errors found in the original U02 Carver note

1. **Live costs "within 1-2 bp of the model"** (section 1 item 2; section 3; MT106-C07-7). The claim text says within
   1-2 bp "of the prior year". The quote says only "my costs are exactly in line where I'd expect them to be". This
   misreading props up the note's "strong" grade on costs.
2. **Buffer cuts turnover "20-30%"** (T3; B27, "EWMAC4 61.8 -> 49.8"). In B27, 61.8 is the turnover of the forecast
   itself. The effect of buffering is 52.6 to 49.8, about 5%, for the fast rule, and 10.16 to 7.04, about 31%, for the
   slow rule. T3's expected effect cites the wrong comparison.
3. **Attenuation comes "with a mechanism"** (T4, the stated reason it deserves a Holm slot; B24, MT010-C16-3). B24
   says: "No mechanism was established; commenters suggested vol mean reversion whipsawing fast systems". The quote of
   MT010-C16-3 says only that the result is counterintuitive.
4. **IDM "from 6-month correlation and 1-month vol"** (section 1 item 4; rule 4). This is partly wrong:
   - The 6-month correlation (MT128-C11-4) is defensible.
   - The 1-month vol (MT128-C12-3) feeds the risk model, not the IDM.
   - B06 says his IDM is fixed at 2.5, deliberately below the estimate.
   - The pack holds four multipliers that do not reconcile: 2.0 (B27), 2.5 (B06), about 3.1 (MT144-C07-3) and 4-5
     (MT128-C11-2).

Smaller points:
- "1.18 vs 0.88" mixes vol scaling with continuous forecasts. The like-for-like comparison in B22 is 1.15 vs 0.88.
- "Buffer of 10% of target" comes from a digest line (B13) whose own figure, 0.0125, is 5% of a 25% target.
- Four numbers appear only in claim text and are used unflagged: 0.5-1 long-run Sharpe (MT044-C04-2), the 0.01 delay
  threshold (MT026-C07-1), 0.2-0.25 correlation R2 (MT128-C12-2) and a 50% drawdown (MT196-C12-1).
- The note missed a pack conflict. The correction to MT044-C10-1 says forecast scaling matters "much" more than vol
  adjustment, while B22 shows the reverse.

## What this means for notes U01-U07

These notes were written under the standard brief, without the addendum. U02 shows where such notes go wrong.

**Can be relied on:**
- Claim ids exist.
- The direction of the main verdicts.
- Numbers that sit inside a verbatim quote.
- Plain restatements of a quoted rule.

**Need a fact-check:**
- Numbers taken from claim text or from a digest. These were not checked against the quote or the source post.
- Comparisons read off a table: which two columns are being compared.
- Words that add a mechanism or a cause the source does not state.
- Grades of "strong" or "SHOWN" that rest on one of the above.
- The expected effects and "worth a slot" reasons in test proposals. In U02 two of the five proposals (T3, T4) rest
  on a misread premise.

The fact-check is cheap: a question set like Part 2, or a number-by-number check against quotes. Do it for each of
U01-U07 before any of their test proposals is registered.

## Changes to the foundation brief that the evidence supports

1. **Number rule.** Every number must be found in a verbatim quote, in a paper, or in our docs.
   - A number found only in claim text or a digest is tagged "(summary only)".
   - Such a number cannot support a grade above weak, a "SHOWN" label, or a test's expected effect.
2. **Keep section 9, "Pack problems", in every unit,** split into four kinds: contradicts a quote / contradicts
   another pack statement / wrong speaker / goes beyond the quote.
   - Content that only goes beyond the quote may still be used, marked "(claim text)", for context. This keeps notes
     from being emptied, as the Eckhardt note was.
   - It may not be used for numbers, grades or test premises.
3. **Name the source of every mechanism and comparison.**
   - A mechanism or causal step needs the quote or post line that states it. Otherwise it is "(reader)".
   - A comparison from a table must name both columns, for example "raw 52.6 vs buffered 49.8".
4. **Check test premises before registration.** Before a test proposal enters the registry, an independent Opus pass
   checks its factual premises and expected-effect numbers against the quotes. Digest numbers that carry a proposal
   are checked against the original blog post.
