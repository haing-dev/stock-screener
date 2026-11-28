# Investor reading: status after the first full pass (2026-11-27)

Nine roster investors read through gates G1-G6 from the documents already in the library (user: "keep going with the
investors with readily available materials, don't stop"; V04_REGISTRATION A13 items 1-15). No price, return or 13F
holding was read for any of this; the recall test (G8) is the next step and runs on WRDS.

| Investor | Docs read | Claims (quotes all verbatim) | Verified rules | Blind check: planted caught | Held-out test | Card rules | Recipe: buy rules covered (decisive) | Recall (G8) | Labels |
|---|---|---|---|---|---|---|---|---|---|
| Dev Kantesaria | 5 | 461 | 183 | 10/10 (v1.1) | FAIL: 6/8 matched, 3 open buy contradictions (FICO inflection) | 72 -> v1.1 (K174 merged, new RB22) | 7 of 22 (32%) | v1 FAIL 10.3%, lift 8.3 [0, 17.6]; v2 PASS 37.9%, lift 6.41 [4.19, 8.91] (not independent) | held-out failed |
| Stanley Druckenmiller | 6 | 375 | 92 | 9/10 | FAIL: 17/26 (65%), 3 open buy contradictions | 41 -> 49 (v1.1) | 3 of 11 (27%); no price rule | FAIL: 16.5%, lift 1.69 [1.27, 2.12]; v2 written | thin; held-out failed; 13F = equity longs only |
| Murray Stahl | 3 | 188 | 27 | 6/7 | FAIL: 4/13 (31%), 0 contradictions | 10 -> 20 (v1.1) | 3 of 6 (50%), stand-ins only | FAIL: 39.3%, lift 1.36 [1.04, 1.68]; v2 written | thin; held-out failed |
| Cliff Sosin | 3 | 209 | 54 | 6/6 | FAIL: 4/9 (44%), 2 open sell contradictions | 26 -> 29 (v1.1) | 1 of 6 fully | not measured (not in 13F panel) | thin; held-out failed; no 13F profile |
| Chris Hohn | 2 | 142 | 57 | 6/6 | not possible (2 docs) | 35 | 5 of 14 (36%) | FAIL: 15.9%, lift 2.24 [1.42, 3.17]; v2 written | thin |
| Val Zlatev | 2 | 126 | 37 | 10/10 | not possible | 22 | 3 of 5 (60%) | FAIL: 7.4%, lift 2.12 [0.70, 3.78]; v2 written | thin; long/short |
| Derek Pilecki | 2 | 202 | 60 | 10/10 | not possible | 31 | 2 of 7 fully (29%) | FAIL: 18.6%, lift 1.89 [0.95, 3.09]; v2 written | thin; financials only |
| Bill Nygren / Alex Fitch | 2 | 197 | 78 | 9/10 | not possible | 41 | 2 of 8 fully (25%) | PASS: 31.0%, lift 2.05 [1.54, 2.54] (13F firm-wide) | thin |
| Li Lu | 2 | 168 | 47 | 5/5 | not possible | 30 | 3 of 6 (50%) | not measurable (14 purchases) | thin |

Agreement between the two readers was reported, not used as a stop (A13 item 6): rule-like agreement 76-92%; the
recurring split is advice phrased "you should ..." (one reader: rule; the other: belief). The scorer was corrected
twice after seeing results (number words; "three hundred"), logged in A13 items 10-11; both scores are kept.

## What the pass shows
1. **Every held-out test failed** (4 of 4 investors with 3+ documents). Two to five interviews leave real gaps; the
   missing parts are mostly sizing, sell triggers and the exception cases investors use for their best ideas
   (Kantesaria's FICO inflection, Druckenmiller's countercyclical buys).
2. **Screens cover a minority of the buy rules** (25-60%). The parts that cannot be computed are the ones the
   investors call decisive: dominance and pricing power (Kantesaria, Hohn), doubted businesses (Sosin), dormant assets
   (Stahl), macro timing (Druckenmiller), management trust (Li Lu, Nygren).
3. **Every recipe writer predicts the same risk**: the screen selects a generic factor portfolio (quality, value,
   growth or momentum) rather than the investor's own kind of company. The recall test on their 13F purchases measures
   exactly this.
4. Two independent recipe writers for Kantesaria agreed on all criteria and coverage but chose different cuts,
   windows and rankings (pilot/recipe/SECOND_WRITER_COMPARISON.md).

## Next
- Recall test (G8) DONE for all nine (pilot/recall/RECALL_RESULTS_v2.md): PASS Kantesaria v2 (after revision, not
  independent) and Nygren/Fitch (thin, firm-wide 13F); FAIL Druckenmiller, Stahl, Hohn, Zlatev, Pilecki; Li Lu not
  measurable (14 purchases); Sosin not in the 13F panel. Revision rounds written for the five failures (recipe/RECIPE_v2.md
  in each folder); next: eq_recall 1.2.0 with the v2 recipes, independent check, run. Kill criterion: pilot = Kantesaria,
  Druckenmiller, Stahl (A13 item 23); 2 of 3 must pass after their rounds.
- More material lifts the "thin" label and allows held-out tests: letters or written sources for every investor
  (search prompt of 2026-11-24).
