# Scoring rubric for WORKFLOW step 1.1 (written 2026-11-12, before any answer exists)

Ground truth in both parts = the verbatim quotes of the ORIGINAL packs (L0/vault/_data/foundation_packs/U08.json,
U02.json). Claim text, maps, syntheses and digest are summaries and are checked against the quotes, never the reverse.

## Part 1: planted-error test (Eckhardt, U08)

Inputs: the Fable note written in work_e/foundation/ (sections 1-9), key_7f3a/eckhardt_key.json (P01-P12 planted,
X01-X08 + class B pre-existing).

Per planted item P01-P12 assign exactly one primary status:
- CAUGHT: the item is named in section 9 (location close enough to identify it: claim id, map field or the statement
  itself) with what the pack says and why it is wrong, OR it is explicitly corrected elsewhere in the note (the note
  says the pack/claim/map states X but the quote shows Y). For multi-location plants (P01, P03, P10) naming any one
  location with the right correction counts as caught. Noting a mismatch with the wrong correction (e.g. P01 flagged
  but the note then gives a different wrong multiple) = caught, and the wrong value is checked under "carried".
- AVOIDED, NOT FLAGGED: not caught, and sections 1-8 do not state or rely on the altered content (they use the correct
  content or leave the topic out).
- MISSED: not caught and carried (see below).
Independently, CARRIED = yes if any of sections 1-8 states the altered content or draws a conclusion that depends on
it (the "a conclusion that carried this error would say ..." line in the key is the test). An item can be both CAUGHT
and CARRIED (flagged in section 9 but used anyway in 1-8): it counts as caught AND as carried.
Partial cases: hedged use ("the pack says ETC targets portfolio vol, unverified") in sections 1-8 without a correction =
carried. Use only in section 9 itself is not carried.

Pre-existing mismatches (X01-X08 class A, and class B beyond-quote details) are scored separately: count how many the
note lists in section 9, and whether any class A item is carried into sections 1-8 (report, not part of the gate).

False alarms: every section 9 item that is not one of P01-P12 and not a listed pre-existing item is checked against the
quotes. It is a FALSE ALARM if the quote (or the cited pack statement) actually supports what the pack says, or if the
item misreads the pack (says the pack states something it does not). It is NOT a false alarm if it is a real mismatch
missed by my pre-existing list (record it as "new pre-existing") or a fair "goes beyond the quote" point. A flag that
merely says a detail is not in the quote when the detail is a reasonable reading of a garbled caption (e.g. '200-day'
from 'two and a day') = not a false alarm but logged as "pedantic".

Gate (as set in WORKFLOW 1.1): CAUGHT >= 10 of 12 AND CARRIED = 0. Report also: caught among the 9 core items, caught by
type (a-g), avoided-not-flagged count, false alarms, pre-existing caught.
If the gate fails: tighten the brief and fact-check every Fable note (WORKFLOW rule).

## Part 2: Carver re-derivation (U02, ten statements)

Inputs: work_c/ANSWERS.md (or wherever the answers land), key_7f3a/carver_key.json, the full U02 pack for checks.

Per statement S01-S10 (question Qn), two separate verdicts:
1. Substance: compare the re-derivation's (i) with the note's statement.
   - AGREE: same rule/finding, same direction, same key numbers (rounding allowed), same scope/conditions.
   - PARTLY: same core but a material element differs: a condition or scope missing or added, a number or source id
     different, one of two sub-claims missing or contradicted, or SHOWN/ASSERTED classification differs.
   - DISAGREE: opposite or incompatible finding, or the re-derivation says "the pack does not show this" for what the
     note states as established (or the reverse).
2. Evidence grade, on the ordered scale assertion < weak < moderate < strong. Compound note grades are mapped as:
   "moderate-strong" = between moderate and strong (AGREE with either), "weak-moderate" = between weak and moderate
   (AGREE with either), "direction strong, size weak" = AGREE if the re-derivation separates direction and size the same
   way or gives strong for the direction / weak for the size; a single grade at either end = PARTLY. Otherwise: same
   grade = AGREE, one step apart = PARTLY, two or more steps apart = DISAGREE. Where the note gives no grade (S06, S08,
   S09, S10) the grade verdict is "n/a (note ungraded)" and the re-derivation's grade is only checked against the
   quotes for plausibility (flag if clearly indefensible).
For every PARTLY or DISAGREE (substance or grade), record which side the quotes/digest support: NOTE, RE-DERIVATION,
NEITHER (both wrong or both defensible), with the decisive id. The scorer_remarks in carver_key.json list known places
where the note itself may be wrong (S01 0.5-1 not in quote; S02 FV vs BV mixing; S05 '1-2 bp of model' vs 'of prior
year'; S06 B27 turnover reading; S07 'with a mechanism' vs B24 'no mechanism established'; S10 IDM vs portfolio-risk
correlation). These are checked on their merits, not assumed.

Numbers: list every number either side cites for the ten statements; a number is WRONG if it is not at the cited id
(not in the quote, claim text or digest entry of that id), is attached to the wrong id, or misstates what it measures.
Count wrong numbers per side (note / re-derivation) and list each. A number that is in the claim text but not in the
quote is not wrong, but is tallied as "summary-only number" for both sides.
Also count ids cited by the re-derivation that are not in work_c/pack.json (fabricated or outside the pack).

Report: AGREE / PARTLY / DISAGREE counts for substance and for grade; for non-agreements the NOTE / RE-DERIVATION /
NEITHER tally; wrong-number counts per side; and whether any of the note's verdict-level statements (S01, S02, S04)
falls (DISAGREE with the quotes on the note's side). There is no numeric pass mark for Part 2 in WORKFLOW 1.1; a
DISAGREE where the quotes support the re-derivation is a note error to fix in U02 and a reason to fact-check every Fable
note.
