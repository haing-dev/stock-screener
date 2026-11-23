# Agent B notes (step 3.1): Curve carry and Strip reversion

Opus 5.5, 2026-11-23. Specs: SPEC_Curve_carry.md, SPEC_Strip_reversion.md. Helper scripts only in work/ (lookup.py
prints the quote of a claim id; joincheck.sh runs tools/check_ids.py on a copy with line breaks joined, so quotes
that span two lines are checked too). No data read, nothing run, nothing from 2011+.

## (a) Contradictions and gaps between register, notes and code

1. Leverage against the caps (both pods). Both are quiet spreads. With the leg cap defined as the book's per-market
   cap (config.py market_risk_cap x book_vol x 3 / vol) and the 5x gross cap (strip contracts at 0.25/1.9, the
   gm/variants.py convention), neither pod is likely to reach the 10% target; it is tested at the size the caps
   allow. The notes want exactly this (U05: "if you try to make this spread provide you with that risk you will have
   to leverage your position" (MT073-C05-1)), but no note defines "the shop's standard position" after the engine's
   block scaler (book.py run(), multiplier up to 50), which would undo any cap applied before it. Closed in both
   specs (section 5) with the book-level cap; 3.2 should check the choice, 3.3 must simulate with the caps on.
2. Engine costs have no 3-month contract class. book.py cost_bp() charges bd_/st_ markets 1 bp of notional one way,
   which on a 3-month contract is 4 bp of rate per side, eight times QP06's half bp. Strip reversion is closed at
   0.5 bp of rate per contract per side (0.125 bp of notional), gate and P&L alike (spec s9; 1.3a point 9).
3. Contract identity is missing from the data plan. LSEG curves are continuous c-series (c1..cN) that roll at expiry.
   Both pods need, for every observation, the delivery or expiry month of the contract held (returns on one
   identified contract; Strip normals grouped by expiry month), and Strip needs to know whether the Eurodollar
   c-series include serial months. Register D8/D14 list start dates only. The LSEG reader must output it before lock.
4. Seal at the window's end. Strip reversion trades at the next settlement, so the December 2010 holding ends on
   2011-01-03: its last design return month is 2010-11 (register T11 says the design sample runs to 2010-12). R1 reads
   the day after 2010-12-31 as written (register D15); proposal: end R1 at month-end 2010-11. Curve carry trades at the
   month-end settlement (engine convention) and ends at return month 2010-12.
5. Code answers register D7 and H item 3: book.py family_positions() drops Value's commodity signal ("commodity value:
   failed, out") and equity carry ("equity carry: weak in design, out"). Value holds no commodities in the book.
6. Carry and Curve carry read the same curves where Bloomberg loads (register D6, D16): signals.py carry_values()
   fills commodity carry with bloomberg.py commodity_carry() = ln(F1 / farthest contract present) for all 16
   markets. Curve carry's spec never reads Bloomberg curves; Carry's spec (Agent A) must fix the switch.
7. Strip reversion open point 1 (measures on contract rates) is closed as KEPT on curve points (the note's final text):
   it is the translation of the dated QP06 rule, R1 and the cost gate were checked in that form, and a contract-rate
   form would be an undated new rule. A checker may prefer contract rates (QP07's habitat bends live in forward rates;
   spread S_n spans up to 21 months, against "Differences in yields of adjacent contracts are non-stationary as time
   gap increases" (QP12-C31-1)). Changing it would change R1's computation; 3.2 decides.
8. The "outside the batch's error count" question (register B13, 1.3a point 3) is asked only for Strip reversion, but
   Curve carry is in the same position: no registered live source (rule 7) and dating C (rule 5), so it cannot be
   Core either. Register E still counts it as the one B1 candidate inside the Holm count.
9. Weekly-implementation check: impossible for Curve carry until daily far-contract settlements are pulled (LSEG L9a
   holds c1 and c2 only); register D9 names only non-energy commodities before 2000. Strip reversion can run it.
10. Curve carry markets closed to the 16 panel commodities (the engine's cost table and outright volatilities cover
    these); LME (cash and 3 months only), cocoa and the alternative commodities are out. Precious-metal spreads are
    mostly interest- and lease-rate bets (reader); kept because no note excludes them. 3.2 may revisit.
11. Strip currency set: Canada BA is out (LSEG has c1 and c9-c12, Bloomberg BA2-BA8: no single source holds 1-8; the
    spec forbids mixing sources inside one strip); sterling has eight contracts only on LSEG from 2002-03; Euribor
    depth and Euroswiss daily data are not verified. In the design years the pod is the dollar alone.
12. Live dollar strip: Eurodollar ended in 2023; SOFR (from 2018) gets a new normal, so even with LSEG registered the
    dollar has no live position until 60 months of SOFR month-ends exist.
13. Strip falsifier 2 (signal-price artefact) needs a non-tradeable variant (entry at the signal's own settlement) as a
    reported line; it is a design-data computation and must be logged as such (WORKFLOW 7.1).
14. Licence: register D3 says LSEG's licence for trading use is unverified. CLAUDE.md records a user statement
    (2026-11-20, equity section) that LSEG data may be used freely if not published; that covers research use, not a
    live trading source. Rule 7 verdicts in both specs stand.
15. No contradiction found between register rows T08/T11 and the final note texts.

## (b) Items for step 3.4 (spec, section)

| # | Item | Spec, section |
|---|---|---|
| 1 | Inside or outside the batch's error count for a pod without a live source (B13, 1.3a point 3) | Strip s0/s15; Curve carry s15 |
| 2 | Curve carry in B1 or B2: B2 if the LSEG contract history is not locked when B1 is registered (charter s3) | Curve carry s0/s15 |
| 3 | R1: end its month-ends at 2010-11 (seal, D15); outlier screen or December-contract check (1.3a point 5) | Strip s13 |
| 4 | Futures cost c = 0.5 bp of rate per contract per side, gate and P&L; confirm or replace (1.3a point 9) | Strip s9 |
| 5 | Rule 5 reading: Strip dating B (rule on yields dated 2006, futures form translated); Curve carry C | both s0 |
| 6 | Book share used in the P2 Sharpe-difference line (WORKFLOW 5.1 against config.py, F8) | both s5 |
| 7 | Era test with one era of data (Strip: 1990-2010 only; F2) | Strip s7 |
| 8 | Data preconditions: LSEG reader, lock and 2011+ seal with contract identity per observation; pull daily Eurodollar c3, c5, c6, c7 and monthly c5-c8 start dates; pull daily far contracts for the Curve carry weekly check | both s8 |
| 9 | Register the leg-cap definition (book per-market cap per leg) and the 0.25/1.9 gross weight as engine items for these pods | both s5 |
| 10 | 3.3 power check with the caps on; scale-free p-value of P2 holds only at constant scale | both s5 |
| 11 | Zero-slot shape report per pod (charter check point 2) | both s13 |

## (c) check_ids results

| Spec | tools/check_ids.py as written | Same check, line breaks joined (work/joincheck.sh) |
|---|---|---|
| SPEC_Curve_carry.md | 18 ids, 0 missing, 13 quotes checked: ALL IDS AND QUOTES OK | 18 ids, 18 quotes: ALL IDS AND QUOTES OK |
| SPEC_Strip_reversion.md | 24 ids, 0 missing, 15 quotes checked: ALL IDS AND QUOTES OK | 24 ids, 18 quotes: ALL IDS AND QUOTES OK |
| NOTES.md | 2 ids, 0 missing: ALL IDS AND QUOTES OK | 2 ids, 2 quotes: ALL IDS AND QUOTES OK |
