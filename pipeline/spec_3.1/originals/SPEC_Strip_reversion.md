# Pod spec: Strip reversion (step 3.1, draft for the 3.2 check)

Opus 5.5 (Agent B), 2026-11-23. Read only: register 1.5, note 1.3a and its check, charter 1.2, note 1.3c, WORKFLOW,
TESTING_PROTOCOL, gm/*.py. No data, no backtest. Nothing here is registered or run. "Closed here" marks a computation
the note left open, closed by this spec. bp = basis point of rate unless "of notional" is written.

## 0. Header
| Item | Value |
|---|---|
| Pod | Strip reversion |
| Type | New systematic pod |
| Register rows | T11; R1 (section A); B13; C10; D8, D15; overlaps T10, T05, T43, T44 |
| Source notes | Note 1.3a s3.1 (mechanism, other side, grade, rule family, grid, fixed rules, data, stops, relation, rule 5, batch), s4 (U05-T5 spread gate, U01-T4), s5 (R1), s6, s10 points 1-9; check sections C, D, E and corrections 5-13, 19, 20 |
| Register status | B2, "behind every stronger candidate", only if (a) daily prices of dollar contracts 1-8 are locked and (b) R1 passes; else dropped unbuilt and logged, not re-run (1.3a s3.1 Batch). With a live source it takes a place only if one is free after every candidate graded moderate or strong. |
| Dating class | B. Chua, Koh and Ramaswamy 2006 (Journal of Fixed Income 15(4)) state the rule on estimated Treasury yields and name the futures route, "highly liquid Eurodollar futures gives identical payoff" (QP06-C22-2), untested; the habitat mechanism came after the results; our eight-contract construction is a translation (register T11). |
| What rule 5 allows | Hindsight-flagged unless step 3.4 reads rule 5 otherwise (register H1). With no registered live source (rule 7) the best verdict is Incubator in any case. |
| Loss flag (protocol item P3) | Loss event named in section 10; design months with such events exist (1998, 2007, 2008), so the pod is not flagged "loss not seen". |

## 1. Economic claim
Some borrowers and lenders deal at one maturity, "primarily concerned with their natural maturity habitat, with
little regard for the implication of the forward rates on future spot rates" (QP07-C08-3). Their demand bends the
curve there; the bend fades: "they decay towards zero at some rate" (QP07-C10-5, an assumption); the trader who holds
the cheap point against its neighbours is paid by the maturity-bound side. ASSERTED, offered after the results. Against
it, in the quotes: QP07 models habitat bends as smooth: "investors treat them as close substitutes" (QP07-C10-4) and
contract-level misfits as lasting: "can be expected to persist over the short-term" (QP07-C17-2); arbitrage capital
already sits in this segment: "frequently constructed in the transition between the short- end and the long-end" (QP06-C25-2). Grade, exactly as the note gives it: "Evidence grade: weak" (1.3a s3.1).

## 2. What is predicted
The one-month excess return of positions that are long the cheap point of a local bend against its neighbours on a
strip of 3-month rate futures, i.e. the one-month fall of each measure's gap times the gap's sign. Sign: positive.
Largest when gaps are large: "correlation = 0.814 for strategy 2-B" (QP06-C24-3) and around the 10-23 month segment
(QP06-C24-5), which the strip's points 4-8 span. The paper's edge "diminished since the late 1980s" (QP06-C03-6):
the design window lies wholly after that.

## 3. Signal
Per currency c, at each decision day d (tranche 0 = last trading day of the month; tranches 1-3 one, two, three
weeks later):
1. Strip. Contracts 1-8 = the first eight quarterly (March, June, September, December) 3-month rate futures whose
   last trading day falls after the end of the holding period (the trading day after the same tranche's next
   decision day, when the position is exited). Serial-month
   contracts are not used (closed here: the note says "quarterly"). A strip exists only if all eight contracts have
   daily settlements in one locked source at d (1.3a correction 12; one source closed here, so no strip mixes
   settlement conventions).
2. Rates: r_k = 100 minus the settlement price of contract k, in bp.
3. Points (note's construction, kept; section 15): y_n = (r_1 + ... + r_n) / n, n = 1..8.
4. Measures. Version A, adjacent spread (rule 2-B): S_n = y_n - y_(n-1), n = 2..8 (7 measures). Version B, adjacent
   curvature (rule 3-B), "the spread into a point minus the spread out of it": K_n = 2 y_n - y_(n-1) - y_(n+1),
   n = 2..7 (6 measures).
5. Normal, no look-ahead: for each currency, measure and expiry month g of contract n (March, June, September,
   December), the simple average of that measure at all earlier month-ends (last trading days of earlier months) at
   which contract n expired in month g, averaging "till the preceding month" (QP06-C10-6). Month-end values enter the normal
   whenever every contract the measure uses has a month-end settlement (monthly history from 1981-12), screened or not.
   A normal is used only once the measure's first month-end value is at least 60 calendar months before d. No normal
   passes from a reference rate to its successor (Eurodollar to SOFR; LIBOR sterling to SONIA).
6. Gap: G = measure at d's settlements minus its normal.
7. Contract weights w (level-neutral; sums verified in the check, section D2). S_n: +1/n on contract n, -1/(n(n-1))
   on each of contracts 1..n-1. K_n: -1/(n+1) on contract n+1, (n+2)/(n(n+1)) on contract n, -2/((n-1)n(n+1)) on each
   of contracts 1..n-1.
8. Cost gate: no position from a measure while |G| < 2 x c x A, with c = 0.5 bp per contract per side and A = sum of
   |w|: 2/n for S_n, (2n+4)/(n(n+1)) for K_n (the round-trip cost of a position earning 1 per bp of the measure).
9. Stale screen: a contract counts only if its settlement changed on at least 15 of the 20 trading days before d.
   Closed here: a measure with a non-zero weight on a failing contract gives no position at d.
10. Position, sign fixed: for each measure that passes 8 and 9, add sign(G) x w_j to contract j (a positive gap buys
   the point whose yield is high: for S_n long contract n against an equal-weight short of contracts 1..n-1 at
   equal DV01; for K_n long the middle point against both neighbours). The version's raw position q_j (in DV01 units)
   is the sum over its measures. Equal weight per bp of gap change: each measure enters at weight 1 (QP06-C14-2).
11. Units: holding x_j of notional per unit capital in contract j earns x_j x 0.25 x (price change) / 100 per unit
    capital (gm/bloomberg.py short_rate_market() convention). Since every 3-month contract has the same DV01 per
    notional, x_j = lambda x q_j.
12. Risk scaling per currency: lambda = 0.40 / sigma, sigma = the engine's hybrid estimate (gm/vol.py) of the
    annualised volatility of the return of today's q applied to past rate changes by strip position: fast part =
    EWMA of daily squared returns (half-life 35 trading days), slow part = standard deviation of monthly returns over
    120 months (minimum 36), fast weight 0.7, floor 0.75 x slow. Closed here: "scaled to the shop's standard market
    target on its current volatility" (1.3a s3.1) in the engine's own estimator.
13. Timing: signal at d's settlements; trade at the next trading day's settlement (1.3a correction 11); hold to the
    trade day after the same tranche's next decision day (one month: "the holding period of a trade is fixed at one
    month" (QP06-C11-1)), then the new position replaces it. Trades are changes of notional per identified contract; an expiring or dropped contract is a
    trade. Monthly design runs use tranche 0: the return of month m runs from the settlement of the first trading
    day of m to that of the first trading day of m+1.
14. As-of: settlements are public the same day; there is no other input.

## 4. Markets
| Id (new, not in gm/panel.py) | Contracts | Status |
|---|---|---|
| sr_usd | Eurodollar, LSEG Datastream; design market | in from the design start (section 7) |
| sr_eur | Euribor, LSEG from 1994 (number of contracts not verified) | enters when all eight have locked daily settlements |
| sr_chf | Euroswiss c1-c8, LSEG from 1991 (c5+ from 1996-98; daily not verified) | as above |
| sr_gbp | short sterling: LSEG c1 from 1999-06, c2-c8 from 2002-03; Bloomberg L1-L5 only | as above (LSEG only; Bloomberg has no L6-L8) |
| Canada BA | LSEG c1 and c9-c12; Bloomberg BA2-BA8 | out: no single source holds contracts 1-8 |
| Euroyen | six contracts | out |

Entry gate for every market: the data rule of section 3 step 1. R1 tests the dollar only; other currencies inherit
its result. Live contracts: SOFR and SONIA futures (from 2018) and Euribor, each with a new normal.

## 5. Sizing
1. Per version: currency positions as section 3 steps 10-12; currencies at equal risk (divide by the number of
   currencies with a strip).
2. Pod = equal-weight average of the two versions' positions.
3. Pod block scaled to unit ex-ante volatility (trailing 36-month realised volatility of its return, lagged,
   multiplier capped at 50; book.py run()).
4. The pod's test return: the block alone at the book's 10% target (trailing 36 months, lagged), with the
   per-instrument cap and the 5x gross cap, net of costs. Each contract counts at 0.25/1.9 of its notional in the
   gross cap (gm/variants.py, st_us_3m: "2-year equivalent").
5. Leg cap (1.3a s3.1: "no contract is held larger than the shop's standard position in that contract alone").
   Closed here: each contract's notional is at most the book's per-market cap, market_risk_cap x book_vol x 3 / vol_j
   (config.py, book.py run()), with vol_j = the hybrid volatility of that strip position's outright monthly return.
   Same rule as Curve carry; reason: the engine's only face-value limit per instrument; a cap before the block scaler
   would be undone by it. Expected: the caps bind often, because quiet spreads at constant risk need high leverage:
   "if you try to make this spread provide you with that risk you will have to leverage your position" (MT073-C05-1). Reported: share of months a cap binds, and the achieved volatility.
6. In the book: WORKFLOW 5.1 equal risk for Core pods; config.py has no share. The pod cannot be Core, so the share
   matters only for the reported Sharpe-difference line of protocol item P2; step 3.4 fixes it (register F8).

## 6. Version grid
| Version | Local measure | Everything else |
|---|---|---|
| A | adjacent spread S_n, n = 2..8 (rule 2-B) | as section 3 |
| B | adjacent curvature K_n, n = 2..7 (rule 3-B) | as section 3 |

Total 2, averaged with equal weight, never picked (1.3a s3.1: "Which measures a habitat bend is unsettled"). Both
exist only if R1 passes (section 13); if it fails, neither is built. No other dimension.

## 7. Sample
- Design window start: the later of 1990-01 (the note's design sample, "the dollar from 1990-01 at the earliest") and
  the first month-end at which (a) all eight Eurodollar contracts have locked daily settlements and (b) every measure
  of at least one version has its 60-month normal (both versions need contract 8; dollar contracts 5-8 have no known
  monthly start, register D8). Measures enter one by one as their normals mature. Fixed by metadata, not returns.
- End: return month 2010-11. Closed here: the December 2010 holding ends at the settlement of 2011-01-03 (sealed), so
  it is excluded. If the window has fewer than 120 months, the pod is "insufficient data" (TESTING_PROTOCOL s1).
- Eras: only 1990-2010 has data; the 1975-89 era test cannot run (TESTING_PROTOCOL test 3 and WORKFLOW s5 disagree on
  whether eras are decisive, register F2: step 3.4).
- Weekly-implementation check 1990-2010: possible (the pod runs on daily data); all four tranches.
- Excluded: every month from 2011-01; no input reads forward (normal, screen and volatility are trailing).

## 8. Data
| Input | History (source, first date) | Live (source, delay) | Licence status |
|---|---|---|---|
| Eurodollar settlements, contracts 1-8 | LSEG Datastream monthly: c1-c4 from 1981-12, c9-c12 from 1987-06, c5-c8 start unknown, to 2023. Daily: c1, c2, c4, c8 from 1989-12; c3, c5, c6, c7 not pulled (precondition: one small LSEG pull, then lock) | none: Eurodollar ended (2023); SOFR futures on LSEG from 2018, one day | LSEG: not registered (no reader, lock or seal), licence for trading use unverified |
| Contract identity per c-series observation (expiry month; whether the series hold serial months) | must come with the LSEG reader | as history | as above |
| Other strips | section 4 | SONIA (2018), Euribor on LSEG | LSEG as above; Bloomberg (LOCK_v2) research only, no live feed |

Rule 7: no registered live source for any input, so the pod cannot be Core. A live dollar strip needs 60 months of
SOFR month-ends before its normal exists.

## 9. Costs
- Engine class: book.py cost_bp() has no 3-month contract class; its fixed-income class (bd_, st_: 1 bp of notional
  one way, 4 rolls a year) is for notes and would equal 4 bp of rate per side on a 3-month contract.
- Closed here: c = 0.5 bp of rate per contract per side, i.e. 0.125 bp of notional one way, charged on every change
  of notional per identified contract (rolls are trades, no separate roll charge). Source: "pay a transaction cost
  of half basis point" (QP06-C21-2), borrowed from bond spreads (1.3a point 9). The same c sets the gate.
- Double-cost test (WORKFLOW s5 test 2): P&L costs at 1 bp of rate per side; positions and the gate unchanged.
- Turnover: the note gives no figure; every position is re-decided each month, so turnover is high.

## 10. What would prove it wrong (design window, fixed now)
1. No reversion on traded prices: the pod's mean monthly gross return (and each version's) is zero or below.
2. Signal-price artefact (1.3a s3.1 evidence bullet, reader): the same pod entered at the decision day's settlement
   (not tradeable, reported only) has a positive gross mean while the traded pod's is zero or below: the gaps were
   noise in the price that gave the signal.
3. Not paid by bends fading: the correlation of the pod's monthly gross return with the sum of |G| over the measures
   held is zero or below (the paper's payoff tracks gap size, QP06-C24-3).
4. Roll, not reversion (1.3a point 2): ex-ante roll part = minus the sum over held contracts of x_j times the change
   in r_j that ageing by the holding period implies on the decision-day strip (linear interpolation in time to
   expiry; below contract 1, extrapolation from contracts 1 and 2). If its mean is at least the pod's gross mean, the
   profit is Carry (the front-end carry of QP07, whose model will "predict a fall in forward rates" (QP07-C19-3)).
5. Loss event for P3: funding stress, when bends widen before they fade and dealers withdraw (1.3a stop 3, reader).
   Design months: 1998-08 to 1998-10, 2007-07 to 2007-08, 2008-09 to 2008-12 (config.py STRESS_WINDOWS).

## 11. When it should stop working (live kill and review conditions)
1. Ample arbitrage capital: gaps stay below cost and the rule goes flat (traders "rapidly seek out" (QP06-C26-2)
   such trades). Review when the pod is flat at 9 of 12 decision days (reader threshold).
2. A front end pinned by policy: a flat strip. Review while the policy rate of the currency is below 0.25%.
3. Funding stress: review when any held gap exceeds the largest gap of that measure in the design window.
4. A new reference rate or contract design: the currency is flat until its new contract has a 60-month normal.

## 12. Knobs that were tuned
| Knob | Value | Origin |
|---|---|---|
| Strip | 8 quarterly contracts | note reader setting (two years, QP06-C24-5) |
| Points | averages of contract rates | note's construction (reader translation of QP06) |
| Measures | 2-B spread, 3-B curvature | QP06 rules (QP06-C13-5, QP06-C15-4); grid |
| Normal | expanding mean of earlier month-ends | QP06-C10-6 |
| Normal groups | expiry month of contract n | note reader setting; "persistent blips in the data for December contracts" (QP07-C13-5) |
| Normal start | 60 calendar months | note reader setting (paper used 102 months, QP06-C11-3) |
| Sign at fixed size | sign of gap, weight 1 | QP06-C14-1 (tested form), QP06-C14-2 |
| Cost gate and cost | 0.5 bp per contract per side | QP06-C21-2; threshold idea "exceed certain thresholds" (QP06-C22-1) |
| Hold | one month, trade next day | QP06-C11-1; check correction 11 |
| Stale screen | 15 of 20 days | note reader setting; measure rule closed here |
| Risk scaling | 0.40 / sigma, currencies equal risk, block unit vol | engine convention (book.py) |
| Volatility estimator | hybrid 0.7 / 0.3, floor 0.75 | chosen after design results: adopted on book Sharpe (gm_trials.csv "vol hybrid", 2026-11-01; batch 0 B0.1) |
| Leg cap | book per-market cap | engine convention; definition closed here |
| Gross weight | 0.25/1.9 | engine convention (gm/variants.py) |
| Sample end | return month 2010-11 | closed here (seal) |

Knobs chosen after seeing design results: 1 (the hybrid estimator, chosen on the whole book). No design result of
this pod exists. Already seen and related: batch 1 S1, a directional US 3-month short-rate market, was rejected
(gm_trials.csv "batch1 S1 US 3m short-rate market", 2026-11-01; BOOK_FACTS s2); TESTING_PROTOCOL s5 ("considered and
not registered") read QP06's winning trades as likely measurement noise at the bill/note seam: a paper reading, not
a result of ours.

## 13. Gating diagnostics
R1 (register section A; 1.3a s5): for the dollar strip at month-ends from the design start to 2010-12, and the six
curvature measures K_2..K_7 where a normal exists, take G on the signal day and on the next trading day, each
against its cost (2 x c x (2n+4)/(n(n+1))); count triple-months where both exceed the cost with the same sign; no
return is computed. Gate fixed after the check: at least half of triple-months qualify, both versions go to B2
registration; fewer, the pod is dropped unbuilt and logged. Data: daily settlements of dollar contracts 1-8 (3, 5,
6, 7 missing), monthly from 1981-12 for the normal. R1 uses this spec's measures, groups and cost formula exactly.
Sealed read as written: the next trading day after 2010-12-31 is in 2011. Proposal for 3.4 (register D15): end R1's
month-ends at 2010-11. Open for 3.4: an outlier screen or December-contract check in R1 (1.3a point 5;
"cannot patch a period with a sustained anomaly" (QP12-C26-1)).

## 14. Overlaps
1. Short-rate futures markets (T10; register C10): the same contracts join Trend, Economic trend and Carry in non-US
   currencies (not the dollar). In the design years the pod trades the dollar, so no currency is shared unless sr_eur
   and the euro strip market both enter. Reported at 4.3: correlation of each shared currency's pod return with that
   strip market's returns in Trend and Carry.
2. Carry, bond and front-end leg (T05): code: signals.py carry_values() sets bond carry to yield minus the 3-month rate
   for the BD ids (st_us_2y removed, gm-1.2.2); front-end carry would be Carry's mechanism (1.3a s3.2). The pod's
   weights are level-neutral by construction, but residual roll is not shown (check E): falsifier 4 measures it.
3. Whole-curve reversion (T43) and the engine's three spreads: panel.py SPREADS (sp_us_2s10s, sp_de_2s10s,
   sp_us_breakeven10) are built but not traded (signals.py CLASSES has no sp_ class). This spec adds no whole-curve
   version; 3.4 may register one (register T43).
4. QP07 model as a signal (T44): dropped, "its profit is Carry".
Decisive handling of every overlap: test 1, alpha on the Core book (protocol item P2), at 4.3.

## 15. Open choices
| Choice (1.3a point) | Closed as |
|---|---|
| Measures on contract rates (point 1) | Kept on curve points y_n, the note's final text. Reasons: it is the translation of the dated rule (QP06's spread and curvature of zero yields; a contract is the adjacent-bond pair, QP06-C22-2), so rule 5's B rests on it; R1 and the cost gate were checked in this form; a contract-rate form would be a new, undated rule. Cost of keeping: S_n compares contract n with an average up to 21 months nearer, where "Differences in yields of adjacent contracts are non-stationary as time gap increases" (QP12-C31-1). 3.2 checks this closure. |
| Residual roll (point 2) | Reported decomposition and falsifier 4. |
| Outside the batch's error count (point 3) | Step 3.4 (not in WORKFLOW; register B13). |
| Futures form documented before 2011 (point 4) | Recorded as dating B (register); reading at 3.4. |
| R1 outlier and December screens (point 5) | Step 3.4. |
| Expiry-month pooling (point 7) | No adjustment: groups by expiry month keep about 15 month-ends per group at the 60-month start; grouping by calendar month would leave about 5. Reported (no returns): mean absolute gap by months to expiry. |
| Cost floor (point 9) | 0.5 bp per contract per side for gate and P&L (section 9); 3.4 may confirm. |
| Currency set | Rule: eight contracts, daily, one locked source (section 3 step 1). |
| Leg cap and gross weight | Rules in section 5. |
| Sample end | Return month 2010-11 (section 7). |

Register and note agree; the note's final text is followed throughout.

## 16. Builder must not change
Sign of every measure's position; points, measures, weights and normal as section 3; the cost gate and c; one-month
hold with the trade at the next settlement; the two versions and their equal weight; R1 and its gate; the sample
(start rule, end at return month 2010-11); LSEG contract data only, no normal across reference rates; costs and the
double-cost run; the leg cap and the 0.25/1.9 gross weight.
