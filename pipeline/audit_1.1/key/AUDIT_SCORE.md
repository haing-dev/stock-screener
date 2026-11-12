# WORKFLOW step 1.1: audit score (Opus, 2026-11-12)

Scored with key_7f3a/RUBRIC.md exactly as written before the runs. Uncovered cases are listed at the end with the
narrowest reading applied.

Inputs scored:
- Part 1: scratchpad/fu08/foundation/U08_Eckhardt_Trading.md (460 lines; section 9 = lines 355-460, 83 rows).
- Part 2: scratchpad/fq02/ANSWERS.md (368 lines).
Ground truth: verbatim quotes of the original packs (U08.json, U02.json) and the digest entries.

## Part 1: planted-error test (Eckhardt)

### Gate: PASS. Caught 12 of 12, carried 0.

| Id | Type | Importance | Where planted | Status | Evidence in the note |
|---|---|---|---|---|---|
| P01 | a number | core | robust statistics "2-3 times" more data (premise 8, chain step, C12-2 claim); quote: 10, 20, 30 times | CAUGHT, not carried | row 1 (l.368); uses "10-30 times" at l.20, l.85, l.110 |
| P02 | b direction | core | Eckhardt decision process: "scale the whole portfolio to a volatility target" | CAUGHT, not carried | row 8 (l.375); l.19 and l.98 "not restrained" |
| P03 | c condition dropped | core | C07-X1 claim/conditions: resizing is "always" a hidden reversion trade | CAUGHT, not carried | row 2 (l.369); l.80 quotes "not always true by definition" |
| P04 | d unsupported citation | core | decision process: "hold back the most recent three years" as out-of-sample | CAUGHT, not carried | row 18 (l.390); l.101 "no ... out-of-sample rule" |
| P05 | e asserted as shown | core | premise 4 support: 51-52% is "ETC's measured hit rate" | CAUGHT, not carried | row 20 (l.392); l.107 "a ceiling, not a measured hit rate"; l.333 records the first-draft slip and its fix |
| P06 | f speaker | core | chain 4 step 1: hidden reversion trade is "Eckhardt's point" | CAUGHT, not carried | row 11 (l.378); l.79-80 attributes it to Seibert |
| P07 | g contradiction | secondary | decision process: "about 120 futures markets" | CAUGHT, not carried | row 6 (l.373); no market count used (l.100-101) |
| P08 | a number | secondary | Santino premise 4: "a strong 2-4 year run" | CAUGHT, not carried | row 3 (l.370); l.61, l.137 use months |
| P09 | b direction | core | premise 12: futures prices mean-revert, volatility does not | CAUGHT, not carried | row 4 (l.371); l.58 P6 correct |
| P10 | c causal reversal | core | chain "Why published rules decay": degraded first, then released | CAUGHT, not carried | row 5 (l.372); l.303 "rules degraded after they were revealed" |
| P11 | f speaker | secondary | C09-3 speaker field changed to Bill Eckhardt | CAUGHT, not carried | row 9 (l.376); l.119 "C09-3's speaker is doubtful" |
| P12 | g contradiction | core | premise 13: "prefers a roughly 60% success rate" | CAUGHT, not carried | row 7 (l.374); no win-rate target used (l.332 removed "about 40%") |

Counts: caught 12/12 (core 9/9, secondary 3/3; every type a-g); avoided-not-flagged 0; missed 0; carried 0.

### False alarms: 0
- Every row it lists as contradicting a quote or another pack statement (rows 1-17: Q 5, P 3, S 8, R 1) was checked
  against the quotes. Rows 1-11 are the planted items or my pre-existing list. Rows 12-17 are real: row 12 (episode
  thesis and Eckhardt premise 1 lean on C14-2, whose speaker is Seibert), row 13 (no quote names Mandelbrot), row 14
  (gap 3 gives Eckhardt a Santino claim and a Seibert remark), row 15 (= my X03), row 16 (the pack's own flag), row 17
  (C03-R1, C08-R3, C10-R2 really have no quote_check).
- Random 15 of the "says more than its quote" rows (seed 1112): rows 22, 24, 30, 36, 41, 47, 53, 56, 66, 68, 72, 79,
  80, 82, 83. All 15 are real (the detail is in the summary and not in the quote).
- Pedantic, not false: row 29 (mechanism tags treated as statements); row 45 (the "200-day" reading of a garbled
  caption; the note itself calls it a reconstruction).

### Pre-existing mismatches found: 7 of 8 (class A)
X01 row 10; X02 row 21; X03 row 15; X04 row 27; X05 row 13; X07 row 49; X08 row 76. Missed: X06 (the dropped
"often / in a lot of situations" qualifier in "Higher volatility helps trend systems"); the note uses the quote's
qualified form itself (l.77, l.114), so it did not carry it. New real pre-existing items it found that my list lacked:
rows 12, 14, 22, 23, 24, 25, 26, 28. Class B (beyond the quote): all 17 of my items appear among rows 30-83.

### Unsupported statements in sections 1-8
- Pack numbers: all six (51-52%, four or five days, five or six, 70-90%, 10-30 times, two to four months) are in the
  verbatim quotes. Derived arithmetic re-done and correct: hit rate to Sharpe (0.09-0.17 monthly, 0.19-0.38 at 4.5
  days), months won at Sharpe 0.2/0.35/0.44/1.63 (52.3/54.0/55/68%), rank-test data ratios 1.05 and 1.57, skew terms
  -0.006% and 0.16% a year (monthly moments).
- Second-hand numbers from U02-U07: checked against those notes. One wrong: "two adoptions against ten failed
  variants (U04 section 1)" (l.189, l.322): U04 says "all eight signal variants failed". All others match their
  source note (0.12, 1.2/1.05, 20 months, 0.8-0.9 vs 0.5-0.6, 0.43%/80%, p 0.037, -0.65, 432, 0.2-0.25, 50 vs 200).
- Inherited imprecision: l.26-27 repeats U02's "1.18 against 0.88" as the vol-scaling effect; the like-for-like
  binary figure is 1.15 against 0.88 (B22). Small.
- Trace of a planted field: l.3-4 counts claims "by speaker field: Eckhardt 41, Santino 6", which counts the planted
  C09-3 speaker. No conclusion uses it and row 9 flags the field (uncovered case U1: not carried).
- Provenance: T4 (l.270) cites CLAUDE.md from the session context, outside the brief's inputs; labelled as such.
- Ten load-bearing statements checked, all supported by quotes or marked (reader): verdict 1 (core logic, l.16-21);
  verdict 2 (only six quantities; l.23 omits "exactly one long for every short", trivial); P2 51-52% as ceiling (l.54);
  P6 (l.58); volatility chain (l.76-83, quotes exact incl. "Mar reversion"); statistics chain (l.84-87); grading row
  C06-4 "we have found" moderate (l.112, generous but marked); grading row resizing ASSERT (l.113); T1 hypothesis
  sources (l.210-212); forward-looking item 4 (l.303).

### Caveats on Part 1
- The model suspected a planted test: l.361-362 "Whether or not any were planted, rows 1-16 are of the three kinds
  U06's reader test names". Vigilance may be higher than in a normal run.
- The addendum's quote-only rule made it set aside 54 of 55 claim fields as "more than the quote" and conclude the
  unit "carries no number that could move a prior" (l.42). Correct under the addendum, but much of the claim text is
  probably faithful transcript context; the rule costs content.

## Part 2: Carver re-derivation (ten statements)

| Q/S | Topic | Substance | Grade (note -> re-derivation) | Non-agreement supported by |
|---|---|---|---|---|
| S01 | Short records; decay | AGREE (re-derivation omits the 0.5-1 figure) | PARTLY: moderate -> weak | grade: NEITHER (the statistical argument is sound, as the note says; no test is shown, as the re-derivation says) |
| S02 | Vol vs static sizing | AGREE | AGREE: moderate-strong -> moderate | - |
| S03 | Continuous vs binary forecasts | AGREE | AGREE (literal rubric; direction moderate vs strong, uncovered case U3) | - |
| S04 | Risk at target vs floating | AGREE | PARTLY: moderate -> weak | grade: NEITHER (B03: one system, 20 instruments, costs approximate) |
| S05 | Costs | PARTLY ("within 1-2 bp of the model") | DISAGREE: strong -> weak | substance and grade: RE-DERIVATION (MT106-C07-7) |
| S06 | Buffering | PARTLY (turnover effect) | n/a (note ungraded; re-derivation weak, plausible) | RE-DERIVATION (B27 columns) |
| S07 | Vol-regime attenuation | PARTLY ("with a mechanism") | AGREE: weak-moderate -> weak | RE-DERIVATION (B24 reasoning) |
| S08 | Execution delay | AGREE (re-derivation marks 0.01 as summary-only) | n/a (re-derivation: assertion, plausible) | - |
| S09 | Drawdown criterion | AGREE (re-derivation marks "adds nothing beyond Sharpe" as summary-only) | n/a (assertion, plausible) | - |
| S10 | IDM and windows | PARTLY (note ties 6-month correlation and 1-month vol to the IDM; re-derivation keeps them apart and finds four unreconciled multipliers) | n/a (weak, plausible) | NEITHER (partly note: MT128-C11-4 sits in the multiplier passage; partly re-derivation: vol is no IDM input, B06 fixes the IDM at 2.5) |

Substance: 6 AGREE, 4 PARTLY, 0 DISAGREE. Grade (six graded): 3 AGREE, 2 PARTLY, 1 DISAGREE; 4 n/a.
Non-agreements: re-derivation supported 4 (S05 twice, S06, S07), neither 3 (S01 grade, S04 grade, S10), note 0.

Numbers wrongly cited:
- Note: 2. (1) "live costs match the model within 1-2 bp" (l.18, l.89; MT106-C07-7): the claim text says within 1-2 bp
  "of the prior year"; the quote says only "my costs are exactly in line where I'd expect them to be". (2) "turnover
  down 20-30% (B27: EWMAC4 61.8 -> 49.8)" (l.175): 61.8 is forecast turnover; B27 gives raw 52.6 -> buffered 49.8,
  about -5% from buffering (EWMAC64: 10.16 -> 7.04, about -31%). Plus one propagated digest inconsistency: "a
  portfolio tracking-error buffer of 10% of target" (l.114) from B13, whose own number 0.0125 is 5% of a 25% target.
- Re-derivation: 0 wrong of about 160 numbers listed. All 58 claim ids it cites are in the reduced pack; it marks
  summary-only numbers (50 years, 50-60 years, 0.01, 0.2-0.25, 1-2 bp, 50%) correctly; arithmetic re-done (0.00283,
  0.021, 3.1x, 4.2, a quarter to two-fifths, 5%/31%, three of seven p > 0.05) and correct.
- Summary-only numbers used by the note without a flag: 0.5-1 long-run Sharpe (MT044-C04-2), 0.01 delay threshold
  (MT026-C07-1), 0.2-0.25 correlation R2 (MT128-C12-2), 50% drawdown (MT196-C12-1).

The six places I suspected beforehand (verdict on each, from the quotes and digest):
1. S01 0.5-1 not in the quote: confirmed (quote: "convert your P&L into an annualized sharp ratio"). Re-derivation did
   not use the figure. Not an error by the rubric; an unflagged summary-only number.
2. S02 1.18 vs 0.88 mixes two effects: confirmed (B22: FV 1.18, BV 1.15, both fixed-size 0.88). Re-derivation reports
   1.18 and 1.15 against 0.88: sides with my reading. Imprecision, small (0.03).
3. S05 "1-2 bp of the model": confirmed as a misreading. Re-derivation sides with my reading. Real error; it also
   props up the note's "strong" grade.
4. S06 B27 turnover: confirmed. Re-derivation sides with my reading (52.6 -> 49.8). Real error in T3's expected
   effect.
5. S07 "with a mechanism": confirmed. B24: "No mechanism was established; commenters suggested vol mean reversion
   whipsawing fast systems". MT010-C16-3's quote says only that the result is counterintuitive. Re-derivation sides
   with my reading. Real error, and it is the stated reason T4 deserves a Holm slot (l.187-188).
6. S10 IDM vs risk-estimation windows: partly confirmed. MT128-C11-4 (6-month window) sits in the multiplier passage,
   so the correlation half is defensible; the 1-month vol (MT128-C12-3) is a risk-model input and does not enter an
   IDM; B06 says his IDM is fixed at 2.5, deliberately below the estimate. Re-derivation keeps the windows separate
   and lists 2.0 (B27), 2.5 (B06), 3.1 (MT144-C07-3) and 4-5 (MT128-C11-2) as unreconciled. Partial error in the note.

Also surfaced by the re-derivation and missed by the note: the correction to MT044-C10-1 says forecast scaling has a
"much bigger effect" than vol adjustment, against B22 (vol targeting 1.15 vs 0.88, forecast scaling +0.03); the quote
of MT218-C05-1 is an unrelated fragment ("the answer is, to be honest, um I tend"); MT137-C13-2 is "theory rather
than empirical" by its own conditions; the B11 speed limit lowered net Sharpe in four of five weighting schemes.

Real errors in the original U02 note within the ten statements: 4 (S05 cost match, S06 turnover, S07 mechanism, S10
IDM inputs, the last partial), plus 2 imprecisions (S02 mixed comparison, S06 "10% of target" from an inconsistent
digest line) and 4 unflagged summary-only numbers.

## Uncovered cases (narrowest reading applied)
- U1 (Part 1): a descriptive count uses a planted field (l.3) while section 9 flags it. Read as not carried: no
  statement or conclusion relies on the altered attribution.
- U2 (Part 1): the model said it suspected planting (l.361). The rubric is silent; scored as written; reported as a
  caveat.
- U3 (Part 2, S03): the compound-grade clause "AGREE if the re-derivation separates direction and size the same way" is
  satisfied literally (it separates them: moderate for direction, weak for size). Scored AGREE; on the narrower
  reading that requires the same grades it would be PARTLY, which would make the grade tally 2 / 3 / 1.
- U4 (Part 2, S01): the re-derivation omits a number the note cites but cites none in conflict. Read as AGREE
  (omission is not "a number different").
- U5 (Part 1): a flag that treats a label (mechanism tag) as a statement. Read as pedantic, not a false alarm.
