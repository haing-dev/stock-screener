# Pod spec: Curve carry (step 3.1, draft for the 3.2 check)

> **Status (2026-11-23): APPROVED WITH CORRECTIONS at step 3.2.** Written at step 3.1 (Opus, agent B); checked by a
> fresh Opus agent (checks/CHECK_3.2_B.md); its 14 corrections to this spec are applied. Claim ids and quotes
> script-checked (ALL OK). Nothing registered or run; open items go to step 3.4 (check section 4, NOTES_3.1_agent_B.md).

Opus 5.5 (Agent B), 2026-11-23. Read only: register 1.5, charter 1.2 and its check, notes 1.3a, 1.3b, 1.3c and their
checks, card 5 and its check, foundation U04 and U05, WORKFLOW, TESTING_PROTOCOL, gm/*.py. No data, no backtest.
Nothing here is registered or run. "Closed here" marks a computation the notes left open, closed by this spec.

## 0. Header
| Item | Value |
|---|---|
| Pod | Curve carry |
| Type | New systematic pod |
| Register rows | T08; overlaps C9 (with T04, T35, T45), D6, D14, D16; T106 (card 5 "already held") |
| Source notes | Charter 1.2 s3 (Curve carry), s4 (grid), s6 (data), s7 (numbers), s11 point 5; charter check A17, A18, B24, B25, B26, corrections 14, 15, 23; note 1.3a s3.3 (QP12 data rules), s10 point 8; note 1.3b s3 "Other candidates" (the switch); card 5 s4 (contract month); foundation U04-T3 (first proposal; its numbers are unverified, audit 1.1) |
| Register status | B1, "or B2 if its history is not locked when B1 is registered" (charter s3). No diagnostic of register section A gates it. Precondition: a locked LSEG contract history with the 2011+ seal (register D3). |
| Dating class | C (hindsight-flagged). The only dated text is a product design of about 2011: "probably goes back 15 years" (MT130-C08-X1); Erb and Harvey 2006 and de Roon, Nijman and Veld 2000 are not this spread (register T08). |
| What rule 5 allows | No holdout verdict: the holdout result is descriptive. With no registered live source either (rule 7), the best verdict is Incubator. |
| Loss flag (protocol item P3) | Loss event named in section 10; the 1990 oil spike counts only if a crude or oil-product spread is held then (whether a 12-month-later oil contract exists before 1995 is not on the sheet, register D14); otherwise the months of section 10 item 3 decide, and with none the pod is flagged "loss not seen". |

## 1. Economic claim
Commodity holders and hedgers trade the near contracts (reader). Near contracts lose more on each roll than far
ones: "doing it on the front has a negative roll yield" (MT167-C03-X2). The gap is pay for taking the other side, in the
seller's words, "the risk premium that is shared between consumers and and and producers" (MT167-C02-X1); who pays
is not named. Grade, exactly as the charter gives it after its check: "ASSERTED (by a seller; no Sharpe or cost given)"
(charter s2 row 12); no grade word. The check removed the clause that the premium survives crowding (check B24).

## 2. What is predicted
The one-month excess return of a spread, long the contract that delivers 12 months after the front leg and short the
front leg, equal face value, per commodity. Sign: positive on average. Largest in contango that is steepest at the
front (reader, mirroring 1.3b s3, which says only that far against near loses carry in backwardation if the curve is steepest in front), and, by the
seller's words, "in a non-inflationary recession, it actually performs well" (MT167-C11-X9). Worst when a supply shock
lifts the front: "you are exposed to what we call uh shifting to a backwardation" (MT130-C08-2).

## 3. Signal
For each market m in section 4, at each decision day (tranche 0 = last trading day of month t):
1. Contract data. Use real contracts identified by delivery month, never interpolated fixed maturities: "Approach is
   to follow a contract over time rather than fixed maturity" (QP12-C23-1). Every return is the change of one
   identified contract from settlement to settlement; never a change of a continuous c-series across its roll.
2. Front leg F = the nearest listed contract of m whose delivery month is at least three calendar months after month
   t. Closed here: it is the simplest rule that keeps every leg out of its delivery month, first-notice day and
   expiry during the holding month on NYMEX, COMEX, CBOT and ICE US calendars as the writer states them (cattle trades on CME and Brent on ICE Futures Europe, which this reason does not cover: step 3.4 confirms both from the contract specifications) ("no front contract in its delivery
   month", 1.3a s3.3; and "Contracts end, becoming more variable as" (QP12-C29-1) expiry nears).
3. Far leg D = the contract of m with the same delivery month one year after F's. Closed here: one rule for every
   market; it is "about 12 months" (charter s3); it meets 1.3a's seasonal rule (s3.3), which rests on "Strong seasonal
   pattern for heating oil" (QP12-C11-1); and it is QP08's carry measure, "the contract exactly expiring one year
   later" (QP08-C10-3).
   If D has no settlement at t, market m holds nothing that month (no substitute contract).
4. Stale screen (1.3a s3.3; a stale price "price stayed same as on prior day" (QP12-C22-1) bends a curve). Where daily settlements of a leg
   exist: the leg counts only if its settlement changed on at least 15 of the last 20 trading days before the
   decision day. Closed here: where only month-end prices exist, a leg whose month-end settlement equals the previous
   month-end's is stale. A stale leg sets market m to no position for that decision.
5. State: B(t) = 1 if F's settlement > D's settlement at t (backwardation), else 0 (equal counts as not backwardated).
6. Score s(m, t): version V1 "always on" s = +1; version V2 "flat in backwardation" s = +1 if B = 0, else 0.
   The sign is fixed: long D, short F. It cannot be flipped after results.
7. Spread return per unit face value over the holding month: r_s = r_D - r_F, each r the contract's settlement-to-
   settlement price return (futures excess return).
8. Volatility v(m, t) of r_s: the engine's hybrid estimate (gm/vol.py estimate(), model hybrid) on the monthly series
   of r_s, with the monthly EWMA fast part (half-life 6 months; no daily spread series exists in the engine), slow
   part 120 months (minimum 36), fast weight 0.7, floor 0.75 x slow. Closed here: a market is eligible only after 36
   monthly spread returns, so the slow part and the floor exist.
9. Raw position per version: face value p(m) = s x 0.40 / v on the far leg and -p(m) on the front leg (book.py
   family_positions() form: score x 40% / vol).
10. As-of: settlements are public the same day; no other input; no publication lag. The decision uses only
    settlements up to the decision day; the trade is made at the decision day's settlement, as the engine's monthly
    runs assume (positions decided at month-end t earn month t+1, book.py run()). This departs from WORKFLOW s5 (free daily data used with a one-day delay; section 8 gives a one-day live delay): V2's state and the stale screen use the settlement that is traded. The departure is reported through WORKFLOW s5's one-period trading delay line and listed for step 3.4 (a next-day trade needs daily far-contract settlements, not pulled).
11. Rebalancing: monthly, one-month hold, then a new decision. Four weekly tranches (rule 2; charter s4: tranche 0
    decides at month-end, tranches 1-3 one, two, three weeks later). Monthly design runs use tranche 0; the weekly
    check uses all four (section 7).

## 4. Markets
The 16 panel commodities (gm/panel.py COMMOD): cm_wti, cm_brent, cm_natgas, cm_heatoil, cm_gasoline, cm_gold,
cm_silver, cm_copper, cm_platinum, cm_corn, cm_wheat, cm_soybeans, cm_sugar, cm_coffee, cm_cotton, cm_cattle. Each
spread is a new instrument (id cc_ plus the market name, for example cc_wti), built from LSEG contracts. Closed here:
the panel list, because the engine's cost table (book.py cost_bp) covers exactly these (the free panel's outright returns cover them for only 33 to 311 design months each, engine_ref.json market_months);
other commodities would be a breadth choice no note registers for this pod.

| Group | LSEG curve history (data sheet, register T08) | Earliest usable design month |
|---|---|---|
| Grains (corn, wheat, soybeans), softs (sugar, coffee, cotton), metals (gold, silver, copper, platinum) | from 1973 | first month with both legs priced, plus 36 months of spread returns; the 12-month contract's start is not on the sheet |
| WTI | 1983; 24 contracts only from 1995 | as above (start of a 12-month contract unknown) |
| Brent | 1988 | as above |
| Natural gas | 1990 | as above |
| Heating oil, gasoline, cattle | start not on the sheet | as above |

Gasoline changed contract (unleaded to RBOB, 2005-06): a spread pair is always two contracts of one root, which
step 3.1 of this spec already implies. Out: LME metals (cash and 3 months only), cocoa and the alternative
commodities (no panel id). No market enters through a gate.

## 5. Sizing
1. Per version: raw positions from section 3 step 9; equal weight inside the pod (divide by the number of markets with
   a score that month, zero scores of V2 included, as book.py family_positions() counts every non-missing position; markets without a position for data reasons, section 3 steps 3-4, are not counted).
2. Pod = equal-weight average of the two versions' positions (charter s4). In contango both versions hold the full
   spread; in backwardation the pod holds half of it.
3. Pod block scaled to unit ex-ante volatility: trailing 36-month realised volatility of the block's return, lagged,
   multiplier capped at 50 (book.py run(), block_vol_months).
4. The pod's test return: the block alone at the book's 10% target (trailing 36 months, lagged), with the book's
   per-instrument cap, applied as the leg cap of item 5 (no separate cap on the spread instrument), and 5x gross cap, net of costs (book.py run() conventions; both 36-month scalers need at least 24 months, book.py min_periods, and are lagged one month).
5. Leg cap (charter s3: "a cap on the face value of each leg"; U05's warning: "if you try to make this spread provide
   you with that risk you will have to leverage your position" (MT073-C05-1)). Closed here: each leg's face value is
   at most the book's per-market cap, market_risk_cap x book_vol x 3 / vol (config.py, book.py run()), with vol =
   the hybrid volatility (monthly form, section 3 step 8) of the monthly returns of the front leg F itself (identified LSEG contracts); both legs take this one cap, so they stay at equal face value (the free panel's outright commodity returns cover only 33 to 311 design months, engine_ref.json, so they cannot set the cap in most design years). Reason: it is the engine's only face-value limit per
   instrument; a cap before the block scaler would be undone by it. Both legs count at full face value in the 5x
   gross cap (gross weight 1). Reported: share of months a leg cap binds, and the achieved volatility.
6. In the book: WORKFLOW 5.1 puts Core pods at equal risk; config.py has no share for this pod (BASE family_w
   30/30/20/15/5, CANDIDATE 45/15/25/15/0). Since the pod cannot be Core, the share matters only for the reported
   Sharpe-difference line of protocol item P2; step 3.4 fixes it (register F8).

## 6. Version grid
| Version | Backwardation switch | Everything else |
|---|---|---|
| V1 | always on | as section 3 |
| V2 | flat when the front settles above the far contract | as section 3 |

Total 2, averaged with equal weight, never picked. No version depends on a diagnostic. Why the switch is uncertain:
it exists only in the claim text of MT130-C10-4, whose quote is "There are implementations that beta hedge the front of
the back." (MT130-C10-4; check B25), but 1.3b and 1.3a give it reasons that do not rest on the seller (section 15). Beta hedging and
dynamic choice of the far contract are not versions (no note registers them).

## 7. Sample
- Design window: from the first month at which at least 8 of the 16 markets are eligible (section 3 step 8), to the
  return month 2010-12 (last decision 2010-11 month-end). Closed here: half the markets, the brief's "half" rule
  applied to inputs, because both versions share every input; the month is fixed by metadata (contract start dates)
  at the LSEG lock, never by returns. Markets enter as they become eligible after that month. If fewer than 120
  months with a scaled test return result (counted after the warm-up of both scalers of section 5, about 48 months after the first position), the pod is "insufficient data" (TESTING_PROTOCOL s1).
- Eras: 1975-89 and 1990-2010 (TESTING_PROTOCOL s2 test 3; WORKFLOW s5 reports them, register F2: step 3.4).
- Weekly-implementation check (1990-2010): needs daily settlements of the far contracts, which no pulled file holds
  (LSEG daily L9a has c1 and c2 only). Until such a pull is locked, the weekly check for this pod is not run and
  the result sheet says so (register D9 extended).
- Excluded: every month from 2011-01 (sealed), and in the weekly check every holding whose exit settlement falls after 2010-12-31 (tranches 1-3 decided in December 2010). Nothing reads forward: volatility and screens are trailing.

## 8. Data
| Input | History (source, first date) | Live (source, delay) | Licence status |
|---|---|---|---|
| Contract settlements by delivery month, front and 12-month legs | LSEG Datastream / Workspace curves: grains, softs, metals 1973; WTI 1983 (24 contracts from 1995); Brent 1988; natural gas 1990; others not on the sheet. Bloomberg monthly curves: not usable (first-pull copies) | LSEG on the user's PC, one day | LSEG: not registered as a source (no reader, lock or seal), licence for trading use unverified |
| Contract identity per observation (delivery month of the contract a c-series held) | must come with the LSEG reader; a market-month without it is out | as history | as above |
| Outright volatility for the leg cap | front leg F's own monthly returns (LSEG contracts, as the first row); the free panel covers only 33 to 311 design months per commodity (engine_ref.json) | LSEG, one day | as the first row |

Free EIA files hold contracts 1-4 only, no 12-month contract (panel.py eia_curve()). Rule 7: the pod has no
registered live source for its main input, so it cannot be Core.

## 9. Costs
Each leg pays the one-way cost of its commodity on every change of face value in each identified contract
(book.py cost_bp(): 4 bp for WTI, Brent, heating oil, gasoline and the other commodities, 6 bp for natural gas).
Closed here: rolls are charged as the trades they are (closing one contract and opening the next), not by the
engine's rolls-per-year approximation; with the section 3 legs this is about 12 roll trades a year per leg in
monthly energy contracts and about 5 in grains, matching the engine's counts. Two legs double the cost of one
outright: "per turnover the spread will be more expensive than trading outright" (MT073-C08-4). Exchange spread
quotes are not used. No turnover figure is given in the notes. The double-cost test applies (WORKFLOW s5 test 2).

## 10. What would prove it wrong (design window, fixed now)
1. No premium: the mean monthly gross return of V1, pooled at equal risk over markets, is zero or below.
2. Wrong source: the premium is said to come from the roll on a front-steep curve. If V1's mean gross return in
   contango market-months (B = 0 for that market at the decision; V1's pooled return split by each market's own state) is zero or below while it is positive only because of backwardation market-months, the profit is
   a bet on backwardation ending, not the roll premium.
3. Wrong loss state: the loss is said to be "the number one risk factor" (MT130-C09-2), a front lifted into
   backwardation. If fewer than half of V1's ten worst months fall in months where at least one market's front moved
   from below to above its far contract, or if that share is not above the share of all design-window months with such a move in any of the pod's markets, the risk is something else (reader threshold; the base-rate clause stops the test passing by construction when such moves are common across 16 markets).
4. Side claim (reported): mean return in NBER recession months (USREC) with falling 12-month CPILFESL change is zero or
   below: "in a non-inflationary recession, it actually performs well" (MT167-C11-X9) fails.
5. Loss event for P3: a supply shock that shifts the front into backwardation; design months with such an event:
   1990-08 to 1990-10 (config.py STRESS_WINDOWS "1990 oil spike"), plus every month counted under item 3.

## 11. When it should stop working (live kill and review conditions)
1. A lasting supply shock: "unless um you know, the supply shock is permanent, uh mean reverts very quickly"
   (MT167-C02-2). Review when more than half of the pod's markets settle in backwardation for 12 consecutive
   month-ends (reader threshold).
2. Competition for the premium: the check removed "survives crowding"; an insurance-type premium falls as sellers
   arrive: "the premium to insure your car is going to drop" (MT204-C15-1), said of volatility selling, applied here by
   the reader. Review if the live 36-month mean return falls below the design-era 10th percentile of rolling
   36-month means (W5 performance band).
3. Contract change in a market (for example a new delivery specification): that market leaves until 36 months of the
   new contract's spread returns exist.

## 12. Knobs that were tuned
| Knob | Value | Origin |
|---|---|---|
| Far leg | same delivery month, one year after the front | charter s3 (U04-T3's choice; the quote says only "the back end of the curve", check A18); QP08-C10-3; QP12-C11-1 |
| Front leg | nearest contract delivering at least 3 months after t | closed here (1.3a s3.3 rule, QP12-C29-1) |
| Weights of the legs | equal face value | charter s3 (convention); MT130-C08-1 gives the legs, not the weights |
| Backwardation switch | V1 / V2 | grid; the switch is claim text of MT130-C10-4; V1 is the charter author's (charter s10) |
| Score to position | 0.40 / vol, equal weight, block at unit vol over 36 months | engine convention (book.py) |
| Volatility estimator | hybrid 0.7 fast / 0.3 slow, floor 0.75 | chosen after design results: adopted on book Sharpe (gm_trials.csv "vol hybrid", 2026-11-01; batch 0 B0.1) |
| Minimum history | 36 spread returns | closed here |
| Stale screen | 15 of 20 days; unchanged month-end | 1.3a s3.1 reader setting; monthly form closed here |
| Leg cap | book per-market cap, from front-leg F's volatility, one cap for both legs | engine convention (config.py market_risk_cap); closed here as the definition; book target 10%, 5x gross cap (legs at weight 1) and block multiplier cap 50 are engine conventions too (config.py, book.py run()); markets = the 16 panel commodities, closed here (section 4) |
| Start rule | 8 of 16 markets eligible | closed here |
| Costs | book.py cost_bp per leg | engine convention |
| Tranches | four weekly | rule 2 convention |

Knobs chosen after seeing design results: 1 (the hybrid estimator, chosen on the whole book, not on this pod). No
design result of this pod exists. Already seen and related: the carry family's design contribution, which includes
the engine's commodity carry (gm_trials.csv "ablate-carry", 2026-10-31; BOOK_FACTS s3, 1987 carry in commodities).
U04-T3's "Sharpe 0.5-0.8 gross" is an unverified expectation, not a result.

## 13. Gating diagnostics
None in register section A gates this pod or a version. X1 gates Carry's energy leg (T04), not this pod. Entry
condition (not a diagnostic): the LSEG contract history locked with the 2011+ seal before B1 is registered, else
the pod moves to B2 (charter s3). No diagnostic here reads sealed months. Proposal carried for 3.4: the zero-slot
shape report per pod (charter check point 2: five-state equity table).

## 14. Overlaps
1. Carry, energy leg (T04; register C9). Code: signals.py carry_values() sets energy carry to 12 x (F1/F2 - 1) from
   EIA contracts 1-2 (panel.py eia_rolled()); book.py family_positions() runs Carry as "half" (half sign, half rank in
   class) on the front-rolled panel market. In backwardation Carry is long the front; V1 is short it. Same curves,
   opposite front exposure.
2. Carry, Bloomberg curve carry (register D6, D16). Code: carry_values() replaces or fills commodity carry with
   bloomberg.py commodity_carry() = ln(F1 / farthest contract present) wherever Bloomberg curves load, for all 16
   markets (CURVE_ROOT). If Carry keeps it, Carry reads the same curve shape as this pod. Fixing that is Carry's spec
   (Agent A); this pod never reads Bloomberg curves.
3. Card 5 R2 (T35, held back; Carry's long) and the dropped QP12 forecast pod (T45): no position while held back or
   dropped.
4. Card 5 "already held" (T106) lists "Curve carry's contract month": he says only "we'll pick like a month"
   (MT124-C03-X1), and the quote names the front month; this pod does not hold his choice of month (reader). For 3.2.
5. Value: book.py drops Value's commodity signal ("commodity value: failed, out", family_positions()), so Value holds
   no commodities in the book (register D7 answered by code).
What must be measured: decisively, test 1 (alpha on the Core book, which contains Carry; protocol item P2) at 4.3.
Reported at 4.3: correlation of the pod's monthly return with Carry's commodity block and with Trend's commodity
block, by era.

## 15. Open choices
| Choice | Closed as |
|---|---|
| Two versions or one (charter point 5; 1.3a point 8) | Two versions (section 6). 1.3b: far against near loses carry in backwardation if the curve is steepest in front; 1.3a: in backwardation the pair pays roll while waiting for a fade of unknown size. Neither reason rests on the seller. |
| 12-month contract start per commodity (register T08, D14) | Rule: a market enters at its first eligible month (section 3 step 8); the dates are metadata reported by the LSEG reader at lock (3.4 precondition). |
| Front and far leg | Rules in section 3 steps 2-3 (closed here). |
| Leg cap level | Rule in section 5 item 5 (closed here). |
| Markets: precious metals | Kept: no note excludes them. Their spread is mostly an interest-rate and lease-rate bet (reader); 3.2 checks. |
| Inside or outside B1's error count | Step 3.4: the pod cannot be Core (rule 7, rule 5); 1.3a's "outside the error count" reading for Strip reversion would apply here too (register B13, E). |
| B1 or B2 | Rule (charter s3): B2 if the history is not locked when B1 is registered; 3.4. |
| Book share | Step 3.4 (WORKFLOW 5.1 against config.py, register F8). |
| Trade price | The decision day's settlement, the engine's monthly convention (book.py run()); no daily far-contract prices exist to trade a day later. Strip reversion trades a day later because it has daily data. |

Register and notes agree on this pod; no conflict to resolve.

## 16. Builder must not change
Sign (long the 12-month contract, short the front); the leg rules of section 3; the two versions and their equal
weight; the sample rule and its end at return month 2010-12; LSEG contract data only (no Bloomberg curves, no c-series
returns across a roll); costs per leg as section 9 and the double-cost run; the leg cap.
