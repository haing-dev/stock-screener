# Step 3.2 spec check, Checker B: Curve carry and Strip reversion

Opus 5.5 (independent checker), 2026-11-23. Read in full: agent_B/NOTES.md, both specs, BRIEF_OPUS.md, the register
(sections 2a, A-I), CHARTER_1.2 and its check, THESIS_1.3_rates and its check, the 1.3b rows on Curve carry, the 1.3c
P3 text, WORKFLOW, TESTING_PROTOCOL, gm_CHANGES.md, gm_trials.csv, BOOK_FACTS (relevant rows); code gm/config.py,
book.py, vol.py, variants.py, signals.py carry_values / value_values / CLASSES, panel.py COMMOD / eia_*, bloomberg.py
CURVE_ROOT / commodity_carry / short_rate_market; tools/bbgq/engine_ref.json (market_months). Every claim id in both
specs looked up in the ledger (quote and claim text). No backtest, no market data, nothing from 2011+.

## 1. Verdict

| Spec | Verdict | A | B | C | D | E | F | G | Corrections |
|---|---|---|---|---|---|---|---|---|---|
| SPEC_Curve_carry.md | APPROVED WITH CORRECTIONS | 1 | 3 | 1 | 6 | 0 | 3 | 0 | 14 |
| SPEC_Strip_reversion.md | APPROVED WITH CORRECTIONS | 0 | 2 | 1 | 7 | 0 | 0 | 1 | 11 |

Counts are corrections per check. Neither spec needs a new thesis; every defect is a specification or wording gap.

## 2. Findings

### SPEC_Curve_carry.md

A. Faithful
- Thesis, grade ("ASSERTED (by a seller; no Sharpe or cost given)", charter s2 row 12, register T08), dating C, status
  B1-or-B2 (charter s3, register T08, E), 2 versions (charter s4, register B6), no gating diagnostic: all match.
- The 18 ids exist; the 13 quoted phrases are in their quotes (tools/check_ids.py ALL OK). Quotes support their uses:
  MT130-C10-4's quote does not contain the switch (spec says so, check B25); MT204-C15-1 is about volatility selling in
  its claim text, and the spec marks its transfer as reader; MT167-C11-X9 refers to curve carry in its claim text.
- Section 2 attributes "largest in contango that is steepest at the front" to 1.3b s3. 1.3b's row (switch, line 95)
  says only that the pair loses carry in backwardation when the curve is steepest in front; the contango statement is
  the writer's mirror (correction 1).
- Far leg "one year after F" with F at least 3 months out puts the far leg about 15-17 months out, not the charter's
  "about 12 months out". It matches 1.3a s3.3 (same delivery month a year later) and QP08-C10-3 ("exactly expiring one
  year later" than the first future). Accepted.

B. Can it fail
- Falsifier 1 (V1 gross mean <= 0) and 4 (non-inflationary recession) are fixed and numeric. Accepted.
- Falsifier 3 can pass by construction: with 16 markets, a month in which at least one front moves into backwardation
  is likely common, so "at least half of the ten worst months" may hold for any return series. A base-rate clause is
  needed (correction 12).
- Falsifier 2 does not say how a pooled month is split by state when markets differ in state (correction 13).
- P3 loss flag: the 1990 oil spike counts only if an oil spread is held then; whether a 12-month-later WTI, Brent or
  heating-oil contract exists before 1995 is not on the sheet (register D14). The flag must be conditional
  (correction 9).
- Section 11 kills are observable live. Accepted.

C. Hindsight
- One knob chosen after results (hybrid estimator, gm_trials.csv "vol hybrid" and "batch0 B0.1 hybrid volatility");
  confirmed. Market risk cap, 5x gross cap, 36-month block window: no trial selected them (CHANGES gm-1.0; scenario
  limit was the tested risk item and was rejected). Already-seen carry results (ablate-carry; BOOK_FACTS 1987 carry CM)
  correctly listed. Dating C and "no holdout verdict" match register T08 and G.
- Section 12 omits book target, 5x gross cap with legs at weight 1, block multiplier cap 50 and the market list
  (correction 14).

D. Specified and point in time (walked as a builder)
- Step 2: the calendar reason names NYMEX, COMEX, CBOT, ICE US. Cattle (CME) and Brent (ICE Futures Europe) are not
  covered. Checker's knowledge, not verifiable in the pack: before 2016 Brent expired about mid-month before delivery
  (rule holds); since 2016 it expires on the last business day of the second month before delivery, so a t+3 Brent
  contract expires on the holding month's exit day (live issue). Correction 2; item for 3.4.
- Step 10: signal (V2 state, stale screen) and trade use the same settlement. WORKFLOW s5: "Every input is used with
  its live delay (free daily data: one day ...)"; the spec's own section 8 gives a one-day live delay. The engine has
  the same convention (book.py run(); live rule "trade on the first trading day after month end", CHANGES), and no
  daily far-contract prices are pulled. Accepted as a stated departure, reported via WORKFLOW s5's one-period delay line
  (correction 3; item for 3.4).
- Section 5.1: "divide by the number of markets with a position" differs from book.py family_positions(), whose n
  counts every non-missing position, zero scores included. For V2 this changes weights in backwardation months
  (correction 5).
- Section 5.4 "the book's per-instrument cap" can be read as a second cap on the cc_ spread instrument (0.03 / spread
  vol, far looser) beside the leg cap of 5.5; and the scalers' minimum windows are not stated: book.py uses rolling 36
  with min_periods 24 for both (lines 191, 198) (correction 6).
- Section 7: the 120-month rule does not say whether it counts positions or scaled test returns; the two scalers need
  about 48 months before the first test return (correction 11). Weekly tranches 1-3 decided in December 2010 hold into
  2011 (correction 10).
- Step 2 "nearest listed contract": which months are listed (serial months in metals, non-cycle months) is defined only
  by what the LSEG c-series hold; item for 3.4 (contract identity, already in NOTES 3).
- Closed-here choices judged: front leg >= 3 months (accept: minimal rule that keeps NG, HO, RB out of expiry);
  far leg same month +1 year (accept); stale screen monthly form (accept); 36 spread returns before entry (accept;
  vol.py would allow 12 months of the fast part alone); 8 of 16 markets start rule (accept: metadata only); leg cap =
  engine per-market cap (accept as the engine's only per-instrument face-value limit, but its volatility source fails,
  see F); costs per identified contract (accept, see F).

E. Code
- carry_values (signals.py:330-349): EIA F1/F2 carry for wti, natgas, heatoil, gasoline; Bloomberg commodity_carry for
  every CURVE_ROOT market in R, Bloomberg first, EIA filling (combine_first), after a >24-month gate. The spec's
  "replaces or fills ... for all 16 markets" is right and more exact than register D6 ("non-energy"). commodity_carry
  divides by an approximate maturity in years (bloomberg.py:139-142); the spec omits this, harmless.
- book.py:105 drops commodity value, :106 equity carry, :131 Carry "half": confirmed. cost_bp (book.py:46-57) energy
  4 bp / natgas 6 bp, 12 rolls; other commodities 4 bp, 5 rolls: confirmed. Cap formula book.py:200-201 and
  config.py market_risk_cap 0.10: confirmed. STRESS_WINDOWS "1990 oil spike" 1990-08..10 (config.py:69): confirmed.
  vol.py hybrid with monthly EWMA half-life 6 when no daily data: confirmed.

F. Data and costs
- The leg cap's volatility (section 5.5, section 8 row 3) comes from "the outright panel market". engine_ref.json
  market_months (design months to 2010-12) for the panel commodities are: cm_brent 33, cm_corn 92, cm_soybeans 88,
  cm_cattle 84, cm_copper 89, cm_wheat 90, cm_sugar 94, cm_coffee 96, cm_platinum 96, cm_silver 104, cm_gasoline 105,
  cm_gold 108, cm_cotton 131, cm_heatoil 202, cm_natgas 203, cm_wti 311. So for most of the design window (grains,
  softs, metals from 1973 on LSEG) the cap is undefined: a builder choice. Section 4's claim that the engine's
  "outright volatilities cover exactly these" is true only from about 2000 (corrections 4, 7, 8).
- History starts (LSEG grains/softs/metals 1973, WTI 1983 with 24 contracts from 1995, Brent 1988, gas 1990; Bloomberg
  curves unusable; EIA contracts 1-4) match the digest and panel.py eia_curve. Probe depth (digest: "CL to c36, LCO/NG
  to c24, metals c12, grains c9") may not reach F + 12 months for markets with consecutive monthly listings (copper)
  or for WTI before 1995: then the market never holds a position. Metadata check at lock; item for 3.4.
- Cost closure: each leg at the engine's front-month cost, rolls as real trades: consistent with book.py and with
  MT073-C08-4. But the far leg is 12-17 months out and less liquid; no note gives a deferred-contract cost; exchange
  calendar-spread quotes would be cheaper. Accepted as written; item for 3.4.
- Rule 7: no registered live source (LSEG not registered, licence unverified): cannot be Core. Correct.

G. Rules of the shop
- 2 versions averaged; sign fixed (long far, short front); sample fixed by rule at lock; nothing claimed as registered
  or run; no 2011+ number; nothing left to the user. OK.

### SPEC_Strip_reversion.md

A. Faithful
- Grade "Evidence grade: weak" (1.3a s3.1), dating B (register T11), status B2 behind stronger candidates, only if
  daily contracts 1-8 locked and R1 passes (1.3a s3.1 Batch; register T11, A), R1 gate as fixed after the check,
  2 versions, fixed rules (cost gate, leg cap, stale screen, no normal across reference rates): all match.
- 24 ids exist; 15 quoted phrases verbatim (ALL OK). QP07-C10-4, C17-2, QP06-C25-2, QP12-C31-1, C26-1 used as the
  1.3a check required.
- Open point 1 (contract rates) closed as KEPT on curve points: the note's final rule family defines points as
  averages of contract rates; changing it would change R1 and the checked cost conversion. Accepted.
- Open point 7 (expiry-month pooling): no adjustment, reported table. Accepted (arithmetic 60/4 = 15 per group right).

B. Can it fail
- Falsifiers 1-3 fixed and numeric. Falsifier 4 compares a roll part with the pod's gross mean but gives the roll part
  without step 11's units (x_j x 0.25 x price change / 100), so the comparison is undefined by a scale factor
  (correction 9).
- P3 events (funding stress; 1998, 2007, 2008 windows, config.py STRESS_WINDOWS): any window of >= 120 test months
  ending 2010-11 contains 2007-2008. Accepted.
- Kill 1 "flat at 9 of 12 decision days" is ambiguous with four tranches (correction 10). Kills 2-4 observable.

C. Hindsight
- One knob after results (hybrid estimator): confirmed. Batch 1 S1 rejection and TESTING_PROTOCOL s5 reading of QP06
  correctly listed as seen. Section 12 omits book target, gross cap, block multiplier cap and the currency-set rule
  (correction 11).

D. Specified and point in time
- Sizing closure (the checker's main point). Section 5.5 caps each contract at market_risk_cap x book_vol x 3 / vol_j.
  book.py clips each column alone (book.py:200-201). The strip's contracts have different vol_j and different x_j, so
  clipping contract by contract leaves a net long or short rate position: the level-neutral pair becomes a directional
  bet exactly when the caps bind, which the spec expects "often". The cap must scale the currency's whole contract
  vector by one factor (correction 5). Order of operations is otherwise sound: the caps act after the book scaler,
  which is computed on the uncapped book (book.py:197-201), so no scaler undoes them; the gross cap scales all columns
  in proportion and keeps neutrality. Rough order of size (checker arithmetic, no data): a contract with 0.25%
  outright vol has a cap of about 12x notional; eight contracts at 0.25/1.9 can exceed the 5x gross cap, so both caps
  bind and the achieved volatility will be well under 10%. 3.3 must simulate with caps on (NOTES item 10 agrees).
- vol_j "hybrid volatility of that strip position's outright monthly return" leaves open whether the fast part is
  daily (step 12) or monthly (correction 5).
- Section 5.4 "per-instrument cap" ambiguity and scaler minimum windows, as in Curve carry (correction 4).
- Step 5: the normal's month-ends must use the step 1 strip as defined at each month-end (contract 1 at a month-end
  can be the c2 series when c1 expires within the next holding period) (correction 1).
- Step 12: past rate changes "by strip position" must be measured on identified contracts, never across a c-series
  roll (correction 2).
- Section 4: "Euribor, each with a new normal" contradicts step 5, which drops a normal only at a change of reference
  rate (correction 3).
- Section 7: tranche holdings crossing into 2011 (tranche 0 decided end-November 2010 is already excluded by the
  return-month rule; tranches 1-3 decided in December 2010 are not) (correction 6). 120-month count versus the
  ~48-month scaler warm-up: likely decisive here, since the window starts in the 1990s (correction 7).
- Cost closure: c = 0.5 bp of rate per contract per side (0.125 bp of notional) for gate and P&L; double-cost at 1 bp.
  The conversion (0.25 DV01 per notional, bloomberg.py:145-149; variants.py:30 uses -0.25 x change / 100) is right; the
  engine's bd_/st_ class (1 bp of notional, book.py:50-51) would indeed be 4 bp of rate. Weights and sums |w| = 2/n and
  (2n+4)/(n(n+1)) recomputed and level-neutral; the gate is the round trip of a unit position. Accepted; the level
  itself (borrowed from 2003 Treasury spreads, 1.3a JP9) stays for 3.4.
- R1: whether R1 applies the step 9 stale screen is not stated in the note or the spec; a stale contract can create a
  gap that persists to the next day and passes R1. Item for 3.4 with the outlier and December screens.
- Monthly Datastream values are the last weekday, not the last trading day (digest); month-ends on a US holiday give a
  stale value that enters the normal unscreened. Item for 3.4 (reader).

E. Code
- signals.py carry_values bond carry (yield minus lagged 3-month rate, BD ids), panel.py SPREADS untraded (CLASSES has
  no sp_ class, signals.py:28), variants.py st_us_3m gross weight 0.25/1.9, bloomberg.py short_rate_market units: all
  confirmed.

F. Data and costs
- Dollar strip monthly c1-c4 1981-12, c9-c12 1987-06, to 2023; daily c1, c2, c4, c8 from 1989-12; Euroswiss c1-c8 1991
  (c5+ 1996-98); short sterling LSEG c1 1999-06, c2-c8 2002-03, Bloomberg L1-L5 only; Canada BA split across sources;
  Euroyen six contracts; SOFR/SONIA from 2018: all match the digest and register D8, T10, T11.
- Rule 7: cannot be Core. Correct. Licence reading (NOTES 14) consistent with the digest.

G. Rules of the shop
- Section 7 says the 1975-89 era test "cannot run"; under TESTING_PROTOCOL test 3 an era with no new data passes by
  construction (identical returns), which is the precise statement (correction 8). Otherwise: versions averaged, sign
  fixed, sample fixed by rule, nothing registered or run, no 2011+ number, nothing left to the user.

## 3. Required corrections

### SPEC_Curve_carry.md

1. Section 2: the contango statement is the writer's mirror of 1.3b, not 1.3b's text.
- Find: `front (1.3b s3: far against near loses carry in backwardation if the curve is steepest in front), and, by the`
- Replace: `front (reader, mirroring 1.3b s3, which says only that far against near loses carry in backwardation if the curve is steepest in front), and, by the`
Reason: THESIS_1.3_xs.md line 95 (switch row); check A.

2. Section 3 step 2: the calendar reason does not cover cattle (CME) or Brent (ICE Futures Europe).
- Find: `expiry during the holding month on NYMEX, COMEX, CBOT and ICE US calendars ("no front contract in its delivery`
- Replace: `expiry during the holding month on NYMEX, COMEX, CBOT and ICE US calendars as the writer states them (cattle trades on CME and Brent on ICE Futures Europe, which this reason does not cover: step 3.4 confirms both from the contract specifications) ("no front contract in its delivery`
Reason: section 4 market list includes cm_cattle and cm_brent; check D.

3. Section 3 step 10: state the departure from WORKFLOW s5's one-day live delay.
- Find: `runs assume (positions decided at month-end t earn month t+1, book.py run()).`
- Replace: `runs assume (positions decided at month-end t earn month t+1, book.py run()). This departs from WORKFLOW s5 (free daily data used with a one-day delay; section 8 gives a one-day live delay): V2's state and the stale screen use the settlement that is traded. The departure is reported through WORKFLOW s5's one-period trading delay line and listed for step 3.4 (a next-day trade needs daily far-contract settlements, not pulled).`
Reason: WORKFLOW s5 "Every input is used with its live delay (free daily data: one day"; spec section 8.

4. Section 4: the free panel's outright returns cover the panel commodities only from about 2000.
- Find: `the panel list, because the engine's cost table (book.py cost_bp) and outright volatilities cover exactly these;`
- Replace: `the panel list, because the engine's cost table (book.py cost_bp) covers exactly these (the free panel's outright returns cover them for only 33 to 311 design months each, engine_ref.json market_months);`
Reason: tools/bbgq/engine_ref.json market_months (cm_brent 33 ... cm_wti 311); check F.

5. Section 5 item 1: the equal-weight divisor must follow book.py, which counts zero scores.
- Find: `a position, book.py family_positions()).`
- Replace: `a score that month, zero scores of V2 included, as book.py family_positions() counts every non-missing position; markets without a position for data reasons, section 3 steps 3-4, are not counted).`
Reason: book.py:138-139 (n = p.notna().sum); check D.

6. Section 5 item 4: one per-instrument cap only, and the scalers' minimum windows.
- Find: `per-instrument cap and 5x gross cap, net of costs (book.py run() conventions).`
- Replace: `per-instrument cap, applied as the leg cap of item 5 (no separate cap on the spread instrument), and 5x gross cap, net of costs (book.py run() conventions; both 36-month scalers need at least 24 months, book.py min_periods, and are lagged one month).`
Reason: book.py:191, 198, 200-201; check D.

7. Section 5 item 5: the leg cap's volatility must exist in the design years and be one cap for both legs.
- Find: `the engine's volatility of the outright panel market. Reason: it is the engine's only face-value limit per`
- Replace: `the hybrid volatility (monthly form, section 3 step 8) of the monthly returns of the front leg F itself (identified LSEG contracts); both legs take this one cap, so they stay at equal face value (the free panel's outright commodity returns cover only 33 to 311 design months, engine_ref.json, so they cannot set the cap in most design years). Reason: it is the engine's only face-value limit per`
Reason: engine_ref.json market_months; book.py:200-201 clips each column alone; check F.

8. Section 8: the volatility row follows correction 7.
- Find: `| Outright volatility for the leg cap | free panel (gm/panel.py), engine vol | free, one day | free |`
- Replace: `| Outright volatility for the leg cap | front leg F's own monthly returns (LSEG contracts, as the first row); the free panel covers only 33 to 311 design months per commodity (engine_ref.json) | LSEG, one day | as the first row |`
Reason: engine_ref.json market_months; check F.

9. Section 0, loss flag: the 1990 event counts only if an oil spread is held then.
- Find: `design months with such an event exist (1990 oil spike), so the pod is not flagged "loss not seen". |`
- Replace: `the 1990 oil spike counts only if a crude or oil-product spread is held then (whether a 12-month-later oil contract exists before 1995 is not on the sheet, register D14); otherwise the months of section 10 item 3 decide, and with none the pod is flagged "loss not seen". |`
Reason: 1.3c P3 ("a spec with none is flagged"); register D14; check B.

10. Section 7: weekly tranches must not hold into 2011.
- Find: `- Excluded: every month from 2011-01 (sealed). Nothing reads forward: volatility and screens are trailing.`
- Replace: `- Excluded: every month from 2011-01 (sealed), and in the weekly check every holding whose exit settlement falls after 2010-12-31 (tranches 1-3 decided in December 2010). Nothing reads forward: volatility and screens are trailing.`
Reason: section 3 step 11 (one-month hold per tranche); WORKFLOW rule 5 seal; check D.

11. Section 7: the 120-month rule counts scaled test returns, after the scalers' warm-up.
- Find: `months result, the pod is "insufficient data" (TESTING_PROTOCOL s1).`
- Replace: `months with a scaled test return result (counted after the warm-up of both scalers of section 5, about 48 months after the first position), the pod is "insufficient data" (TESTING_PROTOCOL s1).`
Reason: book.py:191, 198 (min_periods 24 each); TESTING_PROTOCOL s1; check D.

12. Section 10 item 3: add a base rate so the test cannot pass by construction.
- Find: `from below to above its far contract, the risk is something else (reader threshold).`
- Replace: `from below to above its far contract, or if that share is not above the share of all design-window months with such a move in any of the pod's markets, the risk is something else (reader threshold; the base-rate clause stops the test passing by construction when such moves are common across 16 markets).`
Reason: BRIEF_CHECK_3.2 check B ("not satisfied by construction").

13. Section 10 item 2: define the split by state per market-month.
- Find: `contango months (B = 0) is zero or below while it is positive only because of backwardation months, the profit is`
- Replace: `contango market-months (B = 0 for that market at the decision; V1's pooled return split by each market's own state) is zero or below while it is positive only because of backwardation market-months, the profit is`
Reason: B is defined per market (section 3 step 5); check B.

14. Section 12: list the remaining engine conventions and the market list.
- Find: `| Leg cap | book per-market cap | engine convention (config.py market_risk_cap); closed here as the definition |`
- Replace: `| Leg cap | book per-market cap, from front-leg F's volatility, one cap for both legs | engine convention (config.py market_risk_cap); closed here as the definition; book target 10%, 5x gross cap (legs at weight 1) and block multiplier cap 50 are engine conventions too (config.py, book.py run()); markets = the 16 panel commodities, closed here (section 4) |`
Reason: BRIEF_OPUS section 12 (every parameter in sections 3-6); check C.

### SPEC_Strip_reversion.md

1. Section 3 step 5: the normal's month-ends use the step 1 strip as defined at each month-end.
- Find: `December), the simple average of that measure at all earlier month-ends (last trading days of earlier months) at`
- Replace: `December), the simple average of that measure, built on the strip of step 1 as defined at each such month-end (its own holding period), at all earlier month-ends (last trading days of earlier months) at`
Reason: section 3 step 1 (strip depends on the holding period); check D.

2. Section 3 step 12: past changes by strip position are measured on identified contracts.
- Find: `annualised volatility of the return of today's q applied to past rate changes by strip position: fast part =`
- Replace: `annualised volatility of the return of today's q applied to past rate changes by strip position (each change measured on the identified contract that held that position at the start of the period, never a c-series change across a roll): fast part =`
Reason: section 8 row 2 (c-series roll at expiry); check D.

3. Section 4: Euribor keeps its normal; only a change of reference rate starts a new one.
- Find: `its result. Live contracts: SOFR and SONIA futures (from 2018) and Euribor, each with a new normal.`
- Replace: `its result. Live contracts: SOFR and SONIA futures (from 2018), each with a new normal, and Euribor, whose normal continues (no change of reference rate, section 3 step 5).`
Reason: section 3 step 5 ("No normal passes from a reference rate to its successor"); check D.

4. Section 5 item 4: one per-instrument cap only, and the scalers' minimum windows.
- Find: `per-instrument cap and the 5x gross cap, net of costs. Each contract counts at 0.25/1.9 of its notional in the`
- Replace: `per-instrument cap, applied as the leg cap of item 5, and the 5x gross cap, net of costs (both 36-month scalers need at least 24 months, book.py min_periods, and are lagged one month). Each contract counts at 0.25/1.9 of its notional in the`
Reason: book.py:191, 198, 200-201; check D.

5. Section 5 item 5: scale a currency's contracts jointly under the cap; define vol_j's fast part.
- Find: `(config.py, book.py run()), with vol_j = the hybrid volatility of that strip position's outright monthly return.`
- Replace: `(config.py, book.py run()), with vol_j = the hybrid volatility of that strip position's outright return (fast part from daily returns, slow part monthly, as section 3 step 12). Where any contract exceeds its cap, the currency's whole contract vector is multiplied by the smallest ratio cap_j / |x_j| over its contracts, never clipped contract by contract, so the position stays level-neutral (book.py clips each column alone, which would leave a net rate position).`
Reason: book.py:200-201; section 3 step 7 (level-neutral weights); check D.

6. Section 7: no tranche holding may exit after 2010-12-31.
- Find: `- Excluded: every month from 2011-01; no input reads forward (normal, screen and volatility are trailing).`
- Replace: `- Excluded: every month from 2011-01, and every holding of any tranche whose exit settlement falls after 2010-12-31 (tranche 0 decided at end-November 2010; tranches 1-3 decided in December 2010); no input reads forward (normal, screen and volatility are trailing).`
Reason: section 3 step 13 (exit the trade day after the next decision day); WORKFLOW rule 5 seal; check D.

7. Section 7: the 120-month rule counts scaled test returns, after the scalers' warm-up.
- Find: `it is excluded. If the window has fewer than 120 months, the pod is "insufficient data" (TESTING_PROTOCOL s1).`
- Replace: `it is excluded. If the window has fewer than 120 months with a scaled test return (counted after the warm-up of both scalers of section 5, about 48 months after the first position), the pod is "insufficient data" (TESTING_PROTOCOL s1).`
Reason: book.py:191, 198 (min_periods 24 each); TESTING_PROTOCOL s1; check D.

8. Section 7: state the era rule precisely.
- Find: `- Eras: only 1990-2010 has data; the 1975-89 era test cannot run (TESTING_PROTOCOL test 3 and WORKFLOW s5 disagree on`
- Replace: `- Eras: only 1990-2010 has data; under TESTING_PROTOCOL test 3 the 1975-89 era has no new data and passes by construction, so it tests nothing (TESTING_PROTOCOL test 3 and WORKFLOW s5 disagree on`
Reason: TESTING_PROTOCOL s2 test 3 ("An era with no new data must give identical returns ... and passes"); check G.

9. Section 10 item 4: put the roll part in the units of the pod's return.
- Find: `4. Roll, not reversion (1.3a point 2): ex-ante roll part = minus the sum over held contracts of x_j times the change`
- Replace: `4. Roll, not reversion (1.3a point 2): ex-ante roll part = the step 11 return of the held x_j, with each contract's price change set to minus the change (in points, bp / 100)`
Reason: section 3 step 11 (x_j x 0.25 x price change / 100); check B.

10. Section 11 item 1: name which decision days count.
- Find: `such trades). Review when the pod is flat at 9 of 12 decision days (reader threshold).`
- Replace: `such trades). Review when the pod is flat at 9 of the last 12 month-end (tranche 0) decision days (reader threshold).`
Reason: four tranches give about 48 decision days a year (section 3); check B.

11. Section 12: list the remaining engine conventions and the closed currency rule.
- Find: `| Gross weight | 0.25/1.9 | engine convention (gm/variants.py) |`
- Replace: `| Gross weight | 0.25/1.9 | engine convention (gm/variants.py); book target 10%, 5x gross cap and block multiplier cap 50 are engine conventions too (config.py, book.py run()); currency set (eight contracts, daily, one source) and joint scaling of a currency's contracts under the leg cap are closed here |`
Reason: BRIEF_OPUS section 12 (every parameter in sections 3-6); check C.

## 4. Items for step 3.4

- Both, s5: register the leg cap as joint scaling per market (Curve carry: one cap from F's volatility; Strip: one factor per currency vector), and the 0.25/1.9 gross weight; 3.3 simulates with caps on, since both pods will likely run well under 10% volatility.
- Both, s5/s7: the scalers' warm-up (about 48 months) shortens the test window; 3.4 decides whether the window rule counts test months (as corrected) and records the expected length from metadata at the lock, before any run.
- Both, s14: Strip's return months run first trading day to first trading day; the Core book's run month-end to month-end. The P2 alpha regression needs one alignment rule.
- Both, s3: define tranche decision days ("one, two, three weeks later") when a date is a holiday; shared with every pod.
- Curve carry, s3 step 10: departure from WORKFLOW s5 one-day delay; the existing engine does the same (book.py run(); CHANGES live rule "trade on the first trading day after month end"). 3.4 either accepts it for all monthly pods with the reported delay line or requires a daily far-contract pull.
- Curve carry, s3 step 2: confirm cattle (CME) and Brent (ICE Futures Europe) calendars; from 2016 Brent's t+3 contract expires on the exit day (checker's knowledge); the LSEG reader should output last trading and first notice days per contract.
- Curve carry, s4/s8: metadata check at lock that each market's curve reaches F + 12 months (probe depth: metals c12, grains c9; WTI 24 contracts only from 1995); which months count as "listed" (serial months) per market.
- Curve carry, s9: the far leg (12-17 months out) is charged the front-month cost; no note gives a deferred-contract cost. Confirm or set a higher far-leg cost; the double-cost run applies either way.
- Curve carry, s14: TESTING_PROTOCOL Batch 2 plans for Carry "commodity carry from the 2nd/3rd or 12-month slope with same-calendar-month spreads", which is Curve carry's signal; reconcile with register F7 so the same signal is not registered twice.
- Curve carry, s4: the 16 panel commodities inherit the panel's "hand-picked surviving universe" (CHANGES gm-1.2.0, known and documented); record it.
- Strip, s13: R1's use of the step 9 stale screen is unstated (stale contracts can create a persistent gap that passes R1); decide with the outlier and December screens (1.3a JP5) and the 2010-11 end (register D15).
- Strip, s3 step 5: Datastream monthly values are the last weekday, not the last trading day; holiday month-ends enter the normal unscreened. The reader should flag them.
- Strip, s9: the cost level 0.5 bp of rate per contract per side (borrowed from 2003 Treasury spreads) awaits confirmation (1.3a JP9).
- Both, s0/s15: inside or outside the batch's error count without a live source (register B13); rule 5 reading (register H1).

## 5. What I could not verify

- Exchange calendars for Brent, cattle and the other markets: checker's knowledge only, no contract specifications in
  the pack.
- LSEG c-series roll rules, whether they hold serial months, and the depth of each commodity curve in the design years.
- Whether 0.5 bp of rate per side matches Eurodollar dealing costs for contracts 1-8 in 1990-2010.
- How often the caps bind and the achieved volatility (needs the 3.3 simulation).
- Euribor contract count and daily coverage; LSEG licence terms for trading use.
- Disclosure: while reading the structure of tools/bbgq/engine_ref.json I printed the BASE book's yearly design-era
  returns (to 2010 only, no 2011+); none is used in this check. Only market_months (metadata) is cited.
