---
tags: [method, equity, check]
status: PASS WITH CORRECTIONS: 0 must-fix, 9 should-fix, 10 notes; applied
---
> Source: repo `docs/research/equity/EQUITY_POD_SHOP_PLAN_v0.3_recheck.md` (commit 466ced5). Independent Opus re-check of the corrected text of [[Equity pod shop plan v0.3]] (first check: [[Equity pod shop plan v0.3 - Independent check]]).

# Re-check of EQUITY_POD_SHOP_PLAN_v0.3.md (corrected text, 2026-11-15)

Checker: a separate Opus agent that wrote neither the plan nor the first check. Scope: the corrected plan against the
first check (`EQUITY_POD_SHOP_PLAN_v0.3_check.md`), the draft it checked (f9c4509), v0.2, WORKFLOW.md and the inventory note.

## 1. Verdict

**PASS WITH CORRECTIONS: 0 must-fix, 9 should-fix, 10 notes.**

Every must-fix of the first check is applied or settled by a stated decision, and the rewrite added no leak of design-era
returns. The open points are about order and completeness: the scorecard runs before the seal it is logged against,
the persistence fallback and the merge of the two record kinds are not fixed before it runs, and what "promoted" and "Incubator" mean for investor
families is left open.

## 2. Part A: the first check's findings

| Finding | Status | Comment |
|---|---|---|
| M1 ranking on design-era returns | APPLIED | 5.2 and 5.3 use 2011 on only; 8.2 "picked on returns after 2010" is now true |
| M2 non-US holdout for every family | ADAPTED, sound | Option (a); conditions of (b) kept for promotion support (8.2, 11 row 4.2). See S6 |
| M3 13F has no purchase day | APPLIED | Title, 1, 4 (E2.5), 6, 11 row 8.3 |
| M4 seal opened without a rule | APPLIED | G8 row; one condition list in 8.2, reused in 11. New ordering gap: S1 |
| M5 follow-the-managers pod | ADAPTED, sound | "Its signal" registered before the scorecard; N9 |
| S1 record kinds, profitability | APPLIED | How the two kinds' ranks merge is not said: S4 |
| S2, S3, S4, S6, S7, S8, S10, S12, S13, S15, S17 | APPLIED | S4: masking is partial (N4). S15: also a Stage 0 item; order: S2 |
| S5 thresholds grade themselves | ADAPTED, sound | Odd and even years: adjacent years are alike, so weaker than a random half, but not circular. N3 |
| S9 Bloomberg status | ADAPTED, sound | Pull detail dropped; the fact is correct |
| S11 non-US rules | APPLIED | Power check still US-only; acceptable, non-US runs decide nothing for investor families |
| S14 effort figures | APPLIED | 110-200 docs x 50-60k = 5.5-12M ("6-12M" holds); 1+6..12+1+2+1 = 11-17 Fable units |
| S16 not every screen tested | ADAPTED, sound | Option (b), one descriptive run per family. Status of those pods: S7 |
| N1, N2 arithmetic | APPLIED | t 0.45-0.67; 1.87 / 6 = 0.31 |
| N5 technique count | ADAPTED, sound | Uses the inventory's strict column (347, "about 350"), not the checker's 288; both are word matches |
| N3, N4, N6, N8-N13 | APPLIED | |
| N7 E2.3, E2.10, E0.2 | APPLIED | Rows added; E0.2 back in Stage 1 as in v0.2; the diagram still omits them (fine for a sketch) |
| N14 CRSP end; G7 before live | APPLIED | E1.7 now in Stage 1. CRSP end date: N7 below |
| Plain language 1-10 | APPLIED | All ten fixed; new items in part E (N10) |

## 3. Findings from parts B to E

S and N numbers from here on are this re-check's own (in the table above, S1-S17 and N1-N14 in the first column are the first check's).

### SHOULD

**S1. The scorecard runs before the seal exists.** Sections 10, 11 (G8), 5.4. The G8 amendment logs each scorecard run
"as an opening of the seal". The seal and its lock id are made at E1.4, which section 10 puts in Stage 1; the scorecard
(E0.4) runs in Stage 0. There is nothing to log the opening against, and the 2011+ data are not yet behind a key when
the first sealed-year read happens. Pair R3.

**S2. The v0.2 review runs in Stage 0 next to the jobs it could change.** Sections 1, 10, 11 row 14. The review is
listed in Stage 0 with no order. The scorecard reads sealed years and cannot be un-read; if the review changes the
seal, sample or ranking rules after it ran, a second run is a second opening. v0.2 14 also says the review's
findings fold into v0.3, which is this file. Pairs R3, R4.

**S3. The persistence fallback is decided after the scorecard runs.** Sections 5.3, 12. 5.3 commits the tier rule before
the scorecard runs. Section 12 says that if records do not persist, "the tier then leans on how explicit the
documents are". That is a change of tier rule made after seeing the scorecard, with no threshold for "do not
persist" and no column named. It is a forking path in who gets read. Pairs R2a, R2b.

**S4. The tier rule cannot be run as written.** Section 5.3. "Ranks are taken within each kind of record, never across
them", yet 30 places are filled from one list. Nothing says how the two rankings merge, or among which funds a fund
is ranked (5.2 defines the peer set for 13F filers only). A rule committed before the scorecard must be complete.
Pair R1.

**S5. The leave-out test can look ahead.** Section 8.1 (new). "The source investors' own holdings left out" does not say
which holdings. If it removes stocks the investors held at any time, a design-era run drops stocks they bought later,
which is future knowledge, and the line misleads. Pair R5.

**S6. "Promoted" is undefined, and it collides with a kept rule.** Sections 1, 8.2, 13. 8.2 keeps the macro rule that a
hindsight-flagged pod "is never Core", then says the live record can promote the pod. Promoted to what is not said.
If to Core, it breaks the rule it just kept (WORKFLOW.md lines 30-33, 155); if not, the reader cannot tell what
changes. Pair R6.

**S7. A descriptive pod is Incubator whatever its result.** Sections 1, 8.1. 8.1 makes every family without a slot an
Incubator pod after its descriptive run. v0.2 4.4 defines Incubator as positive after costs and passing placebo and
tail, and section 1 says "history can reject them". For families without a slot it cannot. Control pods, which run
"for Incubator status only", can be Shelved, so the two groups are treated differently. State it as a deliberate
exception. Pairs R7a, R7b, R8.

**S8. The E3.3 say-do check reads sealed years outside the two registered jobs.** Sections 6, 11 rows 8.3 and G8. With
the odd and even split, the check runs on even years up to 2024. It needs the pod's long list in those quarters,
built partly from price ranks. G8 allows only the scorecard and the holdings job to read 2011 on. No verdict leaks
(8.2 already denies a US verdict to a spec that used later holdings), but the read is not covered or logged. Pair R9.

**S9. New documents can reshuffle fixed tiers.** Section 2 (new line). "Raw folders ... join when they are, and E0.1 is
re-run." After E0.5, a re-run changes the inventory, the tiers and the slot ranking, which section 8.2 needs fixed
before the freeze. No cut-off is given. Pair R10.

### NOTE

- N1. Section 11 row 8.5 does not amend v0.2 8.5's "is not tested on history", which the descriptive run replaces.
  Covered by "this plan wins", but section 11 says it lists every amendment. Pair R8.
- N2. Section 11 G8 row: "data outside the US from 2011 on stays sealed", but grade F fund returns (CRSP, LSEG) include
  non-US holdings after 2010. Low risk; say so. Pair R11.
- N3. Section 6: with purchases split by year, a half can fall below the 20-purchase floor. Pair R12.
- N4. Section 8.3 fence 2: quotes often name the firm or its stocks, so masking names gives partial blinding only. Pair R13.
- N5. Section 8.2: "records mainly in the US (under 20% outside)" has no measure; a 13F cannot show non-US holdings. Pair R14.
- N6. Section 2: the list of raw folders (Tech&AI, Energy, ...) is not in any repo file I could find; it is unverified here.
- N7. Section 9: "ended 2025-12 at our October pull" matches the `END = "2025-12-31"` setting in
  `tools/wrdsq/tri_wrds_adapter.py`, which is a chosen setting, not proof of where CRSP ends. E1.2 settles it.
- N8. Section 5.3: "outside the four slots of a batch, like single-investor playbooks (v0.2 section 10)". v0.2 10 says
  playbooks run in B2 for Incubator status only; it does not say outside the four slots. That is a reading, not a quote.
- N9. Section 6: "Its signal is registered" should also fix lookback, number of managers and new or all positions
  (the first check's M5 list). Wording only.
- N10. Part E, plain language: terms used without a short explanation at first use: "sealed" (5.4), "career overlap"
  (8.2, a deciding condition), "hygiene" (8.1), "shortable set" (8.1), "tail" (8.1), "tranches" and "no-trade band"
  (8.1). Pairs R15-R20. "Freeze" is explained by R15.

Checked with no finding: decisions 1 and 2 read the same in sections 1, 5, 6, 8, 10, 11 and 12 apart from S6-S7.
The new items (ranks per kind, odd and even years, persistence check on 2011-25 inside the registered job, E1.7 in
Stage 1, the v0.2 review) leak nothing from the design era. v0.2 references, gates, E-steps, section 13 counts and
section 2 numbers are correct.

## 4. Corrections (find and replace against the corrected plan)

Each Find occurs exactly once in the plan; I checked this with a script (`recheck/verify_pairs.py` in my work folder).

- R1 (S4) Find: `of record (13F copies, real fund returns), never across them.`
  Replace: `of record (13F copies, real fund returns), never across them. Each rank is then turned into a share of its own group (0 for the worst, 1 for the best), and the 30 are taken on that common scale. Funds are ranked among the US stock funds in CRSP (proposal).`
- R2a (S3) Find: `- **Tier B.** Everyone else stays`
  Replace: `- **Fallback, fixed with this rule.** If the persistence check (5.2) finds that the style-adjusted rank hardly persists (proposal: rank correlation under 0.1 in both pairs of blocks), the 30 places by record go to the investors whose documents are most explicit about criteria.\n- **Tier B.** Everyone else stays` (where `\n` is a line break)
- R2b (S3) Find: `| Records do not persist | The persistence check says so in Stage 0, before any reading is ordered by record. The tier then leans on how explicit the documents are |`
  Replace: `| Records do not persist | The persistence check says so in Stage 0. The fallback in 5.3 is fixed before the scorecard runs: the places by record then go to the most explicit documents |`
- R3 (S1, S2) Find: `E1.2 WRDS table check; the independent review of v0.2 as a whole |`
  Replace: `E1.2 WRDS table check; the seal and lock id of E1.4, made before the scorecard runs; the independent review of v0.2 as a whole, finished before the tier rule is fixed and the scorecard runs |`
- R4 (S2) Find: `| 14 Order | Stage 0 precedes Stage 1.`
  Replace: `| 14 Order | Stage 0 precedes Stage 1. Step 0 (the independent review of v0.2) runs in Stage 0, and its findings go into the next version of this plan.`
- R5 (S5) Find: `own holdings left out (does`
  Replace: `own holdings left out, using only holdings filed by each date and never stocks they bought later (does`
- R6 (S6) Find: `then its live record, where it can be promoted.`
  Replace: `then its live record, where it can be promoted at a registered checkpoint. A promoted pod joins the book on its live record; it keeps its hindsight flag and is never labelled Core.`
- R7a (S7) Find: `counted in the trial log, and such a pod is an Incubator pod judged on its live record.`
  Replace: `counted in the trial log, and such a pod stays an Incubator pod judged on its live record, whatever the run shows. This is an exception to the Incubator test of v0.2 4.4, as v0.2 8.5 already made for pods without a slot.`
- R7b (S7) Find: `History can reject them or support them;`
  Replace: `History can reject or support a family that gets a test slot;`
- R8 (S7, N1) Find: `| 8.5 Slots | Control-sourced pods run for Incubator status only, outside the slots.`
  Replace: `| 8.5 Slots | Control-sourced pods run for Incubator status only, outside the slots. Families without a slot are no longer left untested on history: each gets one descriptive run (8.1).`
- R9 (S8) Find: `The check uses the half of the purchases that did not set a threshold |`
  Replace: `The check uses the half of the purchases that did not set a threshold. For quarters after 2010 it runs inside the registered holdings job and is logged the same way |`
- R10 (S9) Find: `join when they are, and E0.1 is re-run`
  Replace: `join when they are, and E0.1 is re-run. Documents that arrive after the tiers are fixed (E0.5) go to tier B and a later round; a family found only in them enters as Incubator`
- R11 (N2) Find: `Data outside the US from 2011 on stays sealed until the freeze |`
  Replace: `Data outside the US from 2011 on stays sealed until the freeze, except the fund returns the scorecard reads for grade F, which are logged the same way |`
- R12 (N3) Find: `- Outputs are aggregates over at least 20 purchases per investor (proposal).`
  Replace: `- Outputs are aggregates over at least 20 purchases per investor (proposal), and at least 20 in each half where purchases are split by year.`
- R13 (N4) Find: `with names and firms masked.`
  Replace: `with names and firms masked. Quotes can still show who is speaking, so this blinding is partial.`
- R14 (N5) Find: `built their records mainly in the US (proposal: under 20% outside)`
  Replace: `built their records mainly in the US (proposal: under 20% outside, measured on fund holdings where they exist and on the stocks named in their claims)`
- R15 (N10) Find: `- The scorecard reads returns inside the sealed years.`
  Replace: `- The scorecard reads returns inside the sealed years (2011 on: kept unseen until the rules are frozen, then run once).`
- R16 (N10) Find: `whose sources have no career overlap`
  Replace: `whose sources have no career overlap (they did not build their record mainly after 2010)`
- R17 (N10) Find: `Batch A (hygiene on the reference book), B1`
  Replace: `Batch A (hygiene on the reference book: checks of costs, data and trading rules, no new return idea), B1`
- R18 (N10) Find: `shortable set needs a stand-in (section 9).`
  Replace: `shortable set (the stocks we allow ourselves to sell short, v0.2 9.1) needs a stand-in (section 9).`
- R19 (N10) Find: `does not worsen the tail.`
  Replace: `does not worsen the tail (the worst falls and worst months).`
- R20 (N10) Find: `no net market exposure, monthly tranches, a no-trade band.`
  Replace: `no net market exposure, monthly tranches (the book is built in slices that start in different months), a no-trade band (small changes are not traded).`

## 5. Part F: does the plan answer the request?

Yes, with two honest changes the user should notice. (1) The five-year ranking is computed and shown first (5.5),
widened to several windows since 2011, and used to pick 30 of the 40 tier A investors. Technique transcripts get
their own foundation track (7). (2) The workflow runs from transcript to claims, cards, families, specs, registered
tests and a live screen (4), and every screen is measured on one sheet (8.1). "Evaluated on the stocks they actually
bought" becomes a profile of each purchase just before it was made and a say-do check, not a test of those stocks'
later returns; the plan explains why. (3) WRDS holds history, LSEG is live, Bloomberg has no role (9). The goal of a
consistent, unbiased evaluation is met for measurement. Proof is limited by design: an investor family stated after
2010 cannot be Core on history, so high risk-adjusted returns for such families are confirmed only by the live record.
The plan says this in section 1, and the user should read it as the main limit.

## 6. Not verified

LSEG and SEC pages, the inventory script, the best-of-20 arithmetic (first check); the raw folder names (N6); transcript
texts; the rendered diagram (read as text); v0.2 as a whole (still the Stage 0 review).

## 7. Effort

About 25 minutes of wall time, 21 tool calls, roughly 110k tokens.
