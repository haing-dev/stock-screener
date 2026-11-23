---
tags: [fable, thesis]
code_commit: 78799ed
---
> Fresh Opus check of the step 3.1 specs (group A). See [[Thesis register 1.5]]. Source: [repo file](https://github.com/haing-dev/stock-screener/blob/78799edd251d9e74a749bd23aa6fc507e9a99d0c/docs/research/specs/checks/CHECK_3.2_A.md).
# Step 3.2 spec check, Checker A (Trend, Economic trend, Carry, Value), 2026-11-23

Inputs read in full: agent_A/SPEC_Trend.md, SPEC_Economic_trend.md, SPEC_Carry.md, SPEC_Value.md, NOTES.md; BRIEF_OPUS.md;
register rows T01-T12, the dropped rows the specs cite, sections A-I; CHARTER_1.2 (all) and its check (tables C, D,
section 3); THESIS_1.3_xs (all) and its check (sections D-F, corrections 17-22, open points); THESIS_1.3_rates s4 and
check corrections 14-16; WORKFLOW rules and sections 5-6; TESTING_PROTOCOL sections 1-4; gm_CHANGES.md; gm_trials.csv
(trial labels); BOOK_FACTS sections 1-3. Code read: gm/config.py, book.py, vol.py, signals.py, panel.py, bloomberg.py,
timing.py, variants.py, daily.py (header). engine_ref.json: market_months counts only. Quotes: every cited id printed
from the ledger (check_A/work/q.py). No backtest, no market data, no 2011+ result.

## 1. Verdicts

| Spec | Verdict | A faithful | B can fail | C hindsight | D specified / point in time | E code | F data / costs | G shop rules | Corrections |
|---|---|---|---|---|---|---|---|---|---|
| SPEC_Trend.md | APPROVED WITH CORRECTIONS | 2 | 1 | 1 | 4 | 1 | 1 | 0 | 8 |
| SPEC_Economic_trend.md | APPROVED WITH CORRECTIONS | 1 | 1 | 1 | 2 | 5 | 0 | 0 | 8 |
| SPEC_Carry.md | APPROVED WITH CORRECTIONS | 0 | 3 | 2 | 1 | 0 | 3 | 0 | 12 |
| SPEC_Value.md | APPROVED WITH CORRECTIONS | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 3 |

Counts are findings that need a correction or a 3.4 item (minor notes in section 2 not counted). No spec is rejected:
every defect is a wording, closure or code-description fix; no thesis, grade, gate or version count is wrong.

## 2. Findings per spec

### SPEC_Trend.md

A. Faithful
- Thesis, grade ("ASSERTED in four notes (row 8), tested in none"), dating B, 16 versions, A2 status, T09/T10 gates and
  T12 as a reported line all match CHARTER_1.2 s3-s5 and register T01, T09, T10, T12. OK.
- Section 10 lists "young, shallow equity falls" as a loss event unconditionally, while charter D4 (and the spec's own
  section 13) adds that line only if D4's gate opens. The cited id [[MT194 - Trend Following during Trump Tariff Turmoil! - Systematic Investor 344#^MT194-C06-4|MT194-C06-4]] supports "first part of the drawdown",
  not "V-shaped"; the V-shape quote is [[MT042 - Diversification is more important than ever! - Systematic Investor - Ep.385#^MT042-C09-2|MT042-C09-2]] (charter row 3). Corrected.
- Section 15 calls [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C21-5|QP09-C21-5]] "1989-97 fund shares"; the quote and claim are a citation of Billingsley and Chance (1996).
  Corrected.

B. Can it fail
- The four section-10 lines are observable on 1975-2010 and not true by construction (D4's cell beyond 15% is a
  separate cell from the young 5-15% cell that decides the spec line). The 1987 crash decomposition (trend EQ -6.38)
  is already seen (BOOK_FACTS s3); that is why the loss event is named, fine. The loss-event line conflicted with D4
  (A above). Counted once under A; B count 1 = same item.

C. Hindsight
- The four pod-level knobs kept after results are right (gm_trials.csv trend-3/6/12, trend-6/12, trend-12; trend cont;
  vol hybrid; cluster weights; trend spot-only; timing grid; stats audit EM-before-2000). Missing at book level: the
  book runs with no early-warning risk scaler (gm_trials.csv scaler-credit, scaler-corr, scaler-ddbrake, none adopted)
  and no scenario limit (scenario limit 3%, cand2 + scenario 5% / 3%, rejected). Both are section-5 sizing facts kept
  after results. Book-level count 3, not 1. Corrected (and the same line in the other three specs).

D. Specified and point in time
- Trade timing: the spec says "traded on the first trading day after month end; earns month t+1". The engine's monthly
  run earns from the decision-day close (book.py:209 pos.shift(1) x R; timing.py docstring "k = 0 is the normal book"),
  i.e. it reads and trades the same close. WORKFLOW s5: "Every input is used with its live delay (free daily data: one
  day ...)". The spec does not say which the design run uses. Corrected (code fact + k = 1 report; decisive form to 3.4).
- Weekly tranche calendar left open ("trading day 5 x j": whose trading days?). Closed in the correction.
- Graded shape: book.py:75 rolling(h, min_periods=h) gives no value if any month in the window is missing, unlike the
  sign shape (gaps as 0). Not stated. Corrected.
- Windows past 2010-12: tranches 1-3 decided in December 2010 hold into January 2011, and a k = 1 trade decided at
  2010-11 earns through day 1 of January 2011. Section 7 only covers lookbacks and vol windows. Corrected (cut at the
  2010-12-31 close).
- Minor, no correction: section 4's "first position = first return month + max(h, 12)" is off by one (m36 needs 12
  returns, so month + 11) and ignores hybrid versions that can start sooner where daily data exist; the builder confirms
  with panel.coverage() as the spec says.
- Closed-here choices judged: averaging at the unscaled position (accept: keeps book.py arithmetic); cap vol = CANDIDATE
  hybrid for every version (accept: the cap is a book-level item, one estimate avoids a version-dependent cap); tranche
  offsets 0/5/10/15 (accept); static or slow-only vol not added (accept: the m36 level is the slow end at market level and
  the fixed block and book scalers would resize a static-at-entry book anyway; charter s4 "Fixed"); class risk equal
  (accept: an alternative vector would be fitted to fund shares); T12 split (accept: exact decomposition of the version
  position); card 5's front-above-second rule not imported (accept: B18 passed it as a note only).

E. Code
- Code-now description checked line by line: trend_signal (book.py:60-76), family_positions (95-151; dir kind clip,
  /n per class, 30% alt cap 140-148), run (188-204: block scale 36/24 cap 50, book 10% on 36/24, market cap
  0.1 x 0.1 x 3 / vol, gross 5x with gross_weights), vol.py m36 / hybrid (16-17, 38-52 as numbered in the file), costs
  (46-57, roll formula 213, borrow 214), BASE/CANDIDATE (config.py 15-35, 63-65), xsmom 12-1 (book.py:104, 11 months
  t-11..t-1). All true. Market list and first return months match engine_ref market_months exactly (61 ids + cm_aqr_ew).
- Trade-timing description (D above) is the one code statement that is incomplete. Counted under D and E.

F. Data and costs
- Costs match cost_bp exactly. Daily-data starts match daily.py.
- Rule 7: "every input of the 61 ids has a free live source" omits the gap the Carry and Economic trend specs record:
  rate3m("GB") and rate3m("EZ") stop at 2026-01 + 12 months (panel.py:368-370), and every excess return subtracts the
  local rate (equities 427-431 with the US stand-in, bonds 478, notes 504, FX 511). From early 2027 fx_gbp, fx_eur,
  bd_gb_10y, st_gb_5y, bd_de_10y, st_de_2y have no return, so no vol and no P&L. Corrected.

G. Shop rules: versions averaged, sign fixed, sample fixed, nothing claimed run, no 2011+ number. OK.

### SPEC_Economic_trend.md

A. Faithful
- Thesis, grade ("Result summary only", cause ASSERTED), dating C and the Incubator consequence, 2 versions, D5 gate and
  JP8 caution match charter s3-s5, its check (table C D5, item Y) and register T02. OK.
- Register T84 says "core-inflation point passes to the Economic trend spec"; the spec does not address it. Corrected
  (section 14 row: headline CPI only, core not held).

B. Can it fail
- Section 10's D5 lines cannot fail on the design window: D5 picks "slow reaction" exactly when the 3-month-delay
  Sharpe is under half, so "no fading with delay" is false on 1975-2010 by construction, and likewise for "lasting
  state". This is the charter's design (D5), so the fix is to say both lines bind only the holdout report and the live
  record. Corrected. The other lines (net return in both eras, inflation-part split, 1999-2000 loss event) can fail.

C. Hindsight: three pod knobs right (gm_CHANGES gm-1.1.0 and trial log 10; cand2 econ risk=credit only; batch1 E1).
  Book-level count 3 (see Trend). Corrected.

D. Specified and point in time
- Risk theme: "the first listed index's ... (signals.py EQ_CC order)" is literally right but hides that for DE the first
  listed index is eq_eu_stoxx50 (EQ_CC order, signals.py:32-35; :215), whose returns start 2000-08 and whose 120-month
  vol needs 36 months, so Germany's risk theme (which also serves fx_eur via FX_MACRO and the commodity block via
  GLOBAL) is the credit part alone until about 2003-07, although eq_de_dax starts 1988-01. Also the theme is the mean of
  whichever parts exist (pandas mean skipna). Made explicit by correction; whether to change it is an engine-version
  question (3.4 item).
- As-of: lags as coded (CPI 1, NEER 1, Baa 1, 3-month rate 1, yields 0) are release-safe on a month-end basis; the
  quarterly-CPI closure is accepted (simplest release rule). Add for 3.4: oecd_sdmx (signals.py:65-77) swallows any
  read error and returns an empty table, so a quarterly stamp that fails the monthly parse would silently move EVERY
  country to the FRED fallback; the metadata check must cover that too.
- Closed-here sign shape (sign of each theme's scaled change): accept.

E. Code
- Trade theme: "euro uses the euro-area index" is false. fx_eur's rate country is "EZ" (panel.py FXM), econ_scores
  calls th(FX_MACRO.get("EZ")) = th("DE") (signals.py:255), and themes("DE") reads neer("DE") = NBDEBIS; the map
  BIS = {"EZ": "XM"} (signals.py:43) is never reached. Corrected.
- Section 14 overlap rows re-checked against signals.py:202-261:
  - Trend overlap (13 of 18 exact), no growth theme, T23 (FX monetary +1, one of four themes), T17 (EQ trade +1, FI
    trade -1), T21 (EQ monetary -1 on the US 2-year): true.
  - "Rising inflation ... on the 12-month change of realised CPI": the input is the 12-month change of the
    year-on-year headline (all-items) inflation rate (zchg of cpi_yoy), not of the CPI level. Wording corrected.
  - T16, T20, T25 row: these rules fire on LEVELS (core inflation above 5% with Fed funds below it; real yield below a
    bar; priced easing with core PCE above 3); the pod reads 12-month CHANGES. Partial overlap at most; corrected.
  - T32 row: the pod is long both maturities when inflation falls, so only R5's long 2-year leg agrees. Corrected.
  - T75's cross-country bond spread is not held (the pod is directional per market). Added.

F. Data: sources and lags match the code; rule 7 caveat on GB/EZ rates present. OK.
G. OK.

### SPEC_Carry.md

A. Faithful: thesis by leg, grade "weak on this pack", dating (A cross-sectional currency only, B energy, C bonds), 2
  versions, X1 gate and form, D4 stop line, T10 measure duty (1.3a correction 15) match 1.3b s3, s5, register T03-T05,
  T10. Equities out (1.3b "Fixed") confirmed. OK.

B. Can it fail
- "Currencies: losses that come without a bad state": "bad state" is undefined, so the line is not observable as
  written. Fixed here with the design stress windows and the worst fifth of S&P 500 months.
- Profit-source line: "price part strongly negative and income positive is paid as carry says" is not the carry claim
  (a price part that offsets the income fully is uncovered parity, no carry pay) and "mostly by price" has no threshold.
  Rewritten with fixed conditions.
- Bond line depends on a placebo that may never be registered; rewritten as a fixed comparison against a constant
  position equal to the leg's average position.

C. Hindsight
- Three pod knobs right. The T10 strip knobs omit that a short-rate market was already tested and rejected
  (protocol_batch1.md S1, synthetic US 3-month market; BOOK_FACTS s2), and the gross weight 0.25 / 1.9 comes from that
  rejected trial. Corrected. Book-level count 3. Corrected.

D. Specified and point in time
- T10 strip carry scaling (closed here: per unit of face value, "as bond carry"): rejected with reason. With r_i rising
  linearly along the strip, per-face strip carry is about a quarter of the US 2-year note's carry on the same curve
  ((r_8 - r_0)/800 against about 4.5/8 of (r_8 - r_0)/100), so in the FI rank the strip sits near the bottom most
  months and version 2 holds it as a standing relative short (the writer's own NOTES item 10). The spec already counts
  the strip at 2-year equivalent in the gross cap (0.25 / 1.9); the carry should use the same basis. Corrected to
  carry x 1.9 / 0.25. Protocol_batch1 C1 (per-duration bond carry) is about bonds and stays unchanged.
- Other closures accepted: version 1 / version 2 averaging reproduces today's half-and-half exactly (checked: book.py:131
  w = 0.5 cs_rank.fillna(0) + 0.5 sign, and with fewer than 3 markets 0.5 sign = mean with a missing version as 0; both
  versions share the same per-class count); Bloomberg curve carry off (bloomberg.py:128-142 farthest contract,
  signals.py:342-348 combine_first); X1 adjustment as 1.3b corrections 17-18.

E. Code: carry_values (signals.py:330-349), eia_rolled (panel.py:254-261, positive = backwardation), cs_rank
  (388-393), book.py:106 equity carry out: all true. T25 / Carry and T99 / T106 / T35 overlap facts true.

F. Data and costs
- "EIA contracts 1 and 2: CL from 1983": engine_ref market_months gives cm_wti 311 design months, i.e. returns from
  1985-02 if without gaps; cm_wti's return is the EIA contract-2-to-1 roll first (panel.py:524-525; Bloomberg empty on
  free data), so contract 2, and with it carry, very likely starts about 1985-01, not 1983. Corrected (hedged; builder
  confirms) in sections 4 and 8.
- Strip cost "8 bp (D1 admission cost)": unit not stated. Per unit of strip face value 8 bp equals 32 bp of rate per
  contract side (face P&L = 0.25 x rate change), 64 times Strip reversion's "half a bp of rate per contract traded"
  (1.3a s3.1). On the 2-year-equivalent basis of the gross weight it is about 1.05 bp per unit of face (4.2 bp of rate),
  still a penalty above Strip reversion's. Corrected; confirm with the D1 extension at 3.4.
- Rule 7 conclusion with the GB/EZ caveat: right. Costs of the 31 markets match cost_bp.
- Minor: "4 rolls a year" for a strip over-costs (only one of eight contracts expires each quarter); conservative, 3.4.

G. OK.

### SPEC_Value.md

A. Faithful: thesis (working reading, rivals apart), grade "weak", dating v1 B / v2 C, cross-asset only, 2 versions,
  the 60-month bond lag (1.3b correction 19), the currency-v2 sign (1.3b check D3 asked the spec to write it), X2 gate on
  the averaged position (correction 18): all match 1.3b and register T06, T07. OK.

B. Can it fail: X2 line, both-eras line and the "lose together with Trend's relative part" line are observable. The
  late-1990s US example could not be verified (section 5). OK.

C. Hindsight: three pod knobs right; the V1 composite finding (version 2's bond leg already seen through
  variants.py bond_value_composite: average rank of the real yield and the 60-month rise on the same 7 bonds) is
  confirmed in code and BOOK_FACTS s2, and is a real gap in register T07. Book-level count 3. Corrected.

D. Specified and point in time
- Code and closures accepted (equity_dy, value_values, cs_rank; v2 expanding mean uses months up to t).
- Not a look-ahead but a backtest-live mismatch, for 3.4: the design signal uses each month's dividends as soon as the
  month ends, while the registered live source (Ken French annual file) is up to 12 months old (and with ffill limit 12
  can lapse before the next annual update). The design run is fresher than live. 3.4 item.

E. Code: all statements true (book.py:105 drops commodity value; signals.py:359-372 composite switch; bloomberg.py
  EQ_INDEX maps eq_eu_stoxx50 to "MXEM Index" and eq_us_ndx, eq_us_r2k to "MXUS Index"). Register T70 (card 2, "short the
  most successful stock market", "Value may hold it") is named in the header but not re-checked in section 14. Added.

F. Rule 7: the spec lists no 3-month rate, but Value's vol and P&L use the excess returns of fx_gbp, fx_eur, bd_gb_10y
  and bd_de_10y, which lose their local rate in early 2027 (panel.py:368-370). Caveat added.

G. OK.

## 3. Required corrections

### SPEC_Trend.md

1. Trade timing: state what the monthly design run does and send the decisive form to 3.4.
- Find: `earns month t+1. Weekly tranches (B7, charter s4), closed here:`
- Replace: `earns month t+1. Code fact: the monthly design run earns from the decision-day close (book.py:209, pos.shift(1) x R; timing.py k = 0), so it reads and trades the same close; WORKFLOW s5 asks for the one-day delay of free daily data (timing.py k = 1); the k = 1 form is reported for every version at A2 and which form is decisive is fixed at 3.4. Weekly tranches (B7, charter s4), closed here:`
Reason: book.py:209; gm/timing.py docstring "k = 0 is the normal book"; WORKFLOW s5 "Every input is used with its live delay (free daily data: one day".
2. Close the tranche calendar.
- Find: `day 5 x j after the month's last trading day, holds one quarter of the pod until its next decision day`
- Replace: `day 5 x j after the month's last trading day (trading days = weekdays the New York Stock Exchange is open; a market without a price that day uses its last price; closed in 3.2), holds one quarter of the pod until its next decision day`
Reason: section 3 step 7 left whose trading days open; markets have different calendars (daily.py sources).
3. Graded shape: state the missing-month rule of the code.
- Find: `(book.py:73-76, cap 2.0 from config.py BASE trend cap). vol_v is the version's own estimate (step 4).`
- Replace: `(book.py:73-76, cap 2.0 from config.py BASE trend cap); no value if any of the h months is missing (book.py:75, min_periods = h), unlike the sign shape. vol_v is the version's own estimate (step 4).`
Reason: book.py:75 lr.rolling(h, min_periods=h); book.py:71 fills gaps with 0 only for the sign shape.
4. Holding periods must stop at 2010-12-31.
- Find: `No month after 2010-12 is read, printed or used, including by the`
- Replace: `No day after 2010-12-31 is read, printed or used: in the weekly check and in the one-day-late (k = 1) report every holding period is cut at the close of 2010-12-31 (tranches 1-3 decided in December 2010 and the k = 1 trade decided at 2010-11 would otherwise earn January 2011 days). No month after 2010-12 is read, printed or used, including by the`
Reason: section 3 step 7 (tranches hold to the next decision day); register D15 (R1 reads one day into 2011 for the same reason).
5. Rule 7: add the GB and euro-area rate gap.
- Find: `Rule 7: every input of the 61 ids has a free live source, so Trend can be Core on rule 7.`
- Replace: `Rule 7: every input of the 61 ids has a free live source, so Trend can be Core on rule 7, once the GB and euro-area OECD 3-month rates have a replacement: they end 2026-01 and are carried forward at most 12 months (panel.py:368-370), so from early 2027 (the carried rate ends 2027-01 and is used one month late) fx_gbp, fx_eur, bd_gb_10y, st_gb_5y, bd_de_10y and st_de_2y have no excess return and eq_gb_ftse and eq_eu_stoxx50 fall back to the US rate (panel.py:427-431, 478, 504, 511); 3.4.`
Reason: panel.py:368-370; SPEC_Carry s8 and SPEC_Economic_trend s8 already carry this caveat.
6. Loss event: make the D4 line conditional and cite the V-shape quote.
- Find: `- Loss event (P3): sharp V-shaped reversals and young, shallow equity falls ([[MT194 - Trend Following during Trump Tariff Turmoil! - Systematic Investor 344#^MT194-C06-4|MT194-C06-4]]); in the window: 1987-10 to`
- Replace: `- Loss event (P3): sharp V-shaped reversals ([[MT042 - Diversification is more important than ever! - Systematic Investor - Ep.385#^MT042-C09-2|MT042-C09-2]]; the line young, shallow equity fall is added here only if D4 opens it, section 13); in the window: 1987-10 to`
Reason: charter s5 D4 "If Trend's mean is negative in the young 5-15% cell and positive beyond 15%, its spec lists ... else no such line"; [[MT042 - Diversification is more important than ever! - Systematic Investor - Ep.385#^MT042-C09-2|MT042-C09-2]] quote "this extreme V-shaped move".
7. Book-level hindsight count.
- Find: `market list = 4 pod-level knobs; plus 1 book-level (pod share 0.45). Hindsight count: 4 (+1 book).`
- Replace: `market list = 4 pod-level knobs; plus 3 book-level: pod share 0.45; no early-warning risk scaler (gm_trials.csv scaler-credit, scaler-corr, scaler-ddbrake, none adopted); no scenario limit (gm_trials.csv scenario limit 3%, cand2 + scenario 5% / 3%, rejected). Hindsight count: 4 (+3 book).`
Reason: gm_trials.csv rows; gm_CHANGES trial log 6 and gm-2.0 table.
8. Correct the description of the fund-share quote.
- Find: `[[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C21-5|QP09-C21-5]]'s 1989-97 fund shares`
- Replace: `the CTA trading shares [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C21-5|QP09-C21-5]] cites from Billingsley and Chance (1996)`
Reason: [[QP09 - Fung and Hsieh The Risk in Hedge Fund Strategies Theory and Evidence from Trend Followers#^QP09-C21-5|QP09-C21-5]] quote "41.2% trade bonds and three- month interest rate futures ..."; claim "Citation (Billingsley and Chance 1996)".

### SPEC_Economic_trend.md

1. Euro trade theme uses Germany's index.
- Find: `euro uses the euro-area index)`
- Replace: `the euro uses Germany's index NBDEBIS, because the euro's themes are Germany's, signals.py:255 with FX_MACRO, and the map BIS EZ -> XM at signals.py:43 is never reached)`
Reason: panel.py FXM fx_eur rate country "EZ"; signals.py:42-43, 90-91, 255.
2. Risk theme: name the German index and the mean of present parts.
- Find: `order) over its 120-month standard deviation (at least 36) x sqrt(12), clipped to [-3, 3], and (b)`
- Replace: `order; for DE that is eq_eu_stoxx50, not eq_de_dax, so Germany's risk theme, which also serves fx_eur and the commodity block, is the credit part alone until about 2003-07; CN uses eq_hk_hsi, KR eq_kr_kospi; the mean takes the parts present) over its 120-month standard deviation (at least 36) x sqrt(12), clipped to [-3, 3], and (b)`
Reason: signals.py:32-35 EQ_CC order, :215-219 (eq[0], rolling std min_periods 36, mean skipna); engine_ref eq_eu_stoxx50 first return 2000-08.
3. D5 lines are not design-window falsifiers.
- Find: `- If D5 makes the claim`
- Replace: `- Not a design-window test (D5 picks the reading the design data agree with, so neither line can fail on 1975-2010); both lines bind the holdout report and the live record only. If D5 makes the claim`
Reason: charter s5 D5 gate; brief check B ("not satisfied by construction").
4. Levels against changes in the T16, T20, T25 row.
- Find: `| T16 card 1 R4, T20, T25 | FI inflation -1 and monetary -1 short bonds on rising inflation or yields | card D2s |`
- Replace: `| T16 card 1 R4, T20, T25 | partial at most: FI inflation -1 and monetary -1 short bonds after a 12-month rise in inflation or yields, while these rules fire on levels (core inflation above 5% with Fed funds below it; real yield below a bar; priced easing with core PCE above 3), and T25 needs the 2-year yield 0.5 below Fed funds, a state the pod does not read | card D2s |`
Reason: register T16, T20, T25 rule cells; signals.py:94-98, 211, 214 (12-month changes).
5. Inflation row: what the input is, and the core point of T84.
- Find: `| held directionally: EQ -1, FI -1, CM +1 on the 12-month change of realised CPI (not its level, not surveys) |`
- Replace: `| held directionally: EQ -1, FI -1, CM +1 on the 12-month change of the headline (all-items) CPI inflation rate (not its level, not surveys); core inflation is not an input, so a core-only rise (T84's core point, passed to this spec) is not held |`
Reason: signals.py:80-82, 211 (zchg of cpi_yoy, CPALTT01 all items); register T84 "core-inflation point passes to the Economic trend spec".
6. T32 row: only one leg agrees.
- Find: `| T32 card 4 R5 | falling CPI change -> FI long (inflation theme) | card 4 D2 |`
- Replace: `| T32 card 4 R5 | falling CPI change -> FI long on both maturities (inflation theme), so only R5's long 2-year leg agrees; its short 10-year leg is opposite | card 4 D2 |`
Reason: register T32 (long 2-year, short 10-year); signals.py SIGNS FI inflation -1 on every bond.
7. T75's cross-country spread.
- Find: `large recession so short oil; China reopening) are NOT held |`
- Replace: `large recession so short oil; China reopening) are NOT held; nor is T75's cross-country bond spread (the pod is directional per market) |`
Reason: register T75 "Economic trend is directional per country, not a cross-country spread"; signals.py:248-252.
8. Book-level hindsight count.
- Find: `one score per market = 3 (+1 book).`
- Replace: `one score per market = 3 (+3 book: pod share, no risk scaler, no scenario limit; SPEC_Trend section 12).`
Reason: gm_trials.csv scaler-credit, scaler-corr, scaler-ddbrake, scenario limit 3%, cand2 + scenario 5% / 3%.

### SPEC_Carry.md

1. WTI carry start (section 4).
- Find: `from 1983) and a volatility estimate (12 months);`
- Replace: `from 1983 for contract 1; the WTI return, the EIA contract 2 to 1 roll, has 311 design months in engine_ref.json, i.e. starts 1985-02 if without gaps, so CL carry very likely starts about 1985-01; the builder confirms) and a volatility estimate (12 months);`
Reason: panel.py:254-261, 524-525; tools/bbgq/engine_ref.json market_months cm_wti 311.
2. WTI carry start (section 8).
- Find: `EIA NYMEX daily, from 1983 (CL)`
- Replace: `EIA NYMEX daily, contract 1 from 1983, contract 2 very likely from 1985 (CL; section 4)`
Reason: as item 1.
3. Strip carry on the basis of its gross weight.
- Find: `Scaling: the same per-unit-of-face-value, per-year basis as bond`
- Replace: `Scaling: 2-year equivalent, carry x 1.9 / 0.25 = (r_8 - r_0) x 0.0095 a year, the basis of its gross weight (variants.py us_3m_rate 0.25 / 1.9); per unit of face value the strip's carry is about a quarter of the US 2-year note's on the same curve, so it would rank near the bottom of the FI class most months and version 2 would hold a standing relative short that no carry reading supports (corrected in 3.2); bond`
Reason: NOTES item 10; THESIS_1.3_rates s4 (scaling "against bond carry in the fixed-income rank the spec writes at step 3.1"); arithmetic in section 2 D.
4. Knob table: strip scale and the seen short-rate trial.
- Find: `| Strip carry and scale | (r_8 - r_0) / 800, per face value | closed here |`
- Replace: `| Strip carry and scale | (r_8 - r_0) / 800 per face value, x 1.9 / 0.25 (2-year equivalent) | closed here, scale corrected in 3.2; a short-rate market was already seen and rejected (protocol_batch1.md S1, synthetic US 3-month market), and the 0.25 / 1.9 gross weight comes from it |`
Reason: BOOK_FACTS s2 S1 row; variants.py us_3m_rate.
5. Open-choice row for the scale.
- Find: `rule in section 3; per face value, as bond carry.`
- Replace: `rule in section 3; 2-year equivalent, the basis of its gross weight (corrected in 3.2).`
Reason: as item 3.
6. Strip cost unit (section 9).
- Find: `Strip markets: 8 bp (D1 admission cost), 4`
- Replace: `Strip markets: 8 bp (D1 admission cost) per 2-year-equivalent unit, i.e. 8 x 0.25 / 1.9 = about 1.05 bp per unit of strip face value, the basis of its gross weight (8 bp per unit of strip face value would be 32 bp of rate per contract side, 64 times Strip reversion's half a bp of rate; closed in 3.2, confirmed with the D1 extension at 3.4), 4`
Reason: book.py:210-213 costs in bp of notional; THESIS_1.3_rates s3.1 "at least half a bp of rate per contract traded"; face P&L = 0.25 x rate change.
7. Open-choice row for the cost.
- Find: `rule: 8 bp (D1), 0.25 / 1.9 (variants.py).`
- Replace: `rule: 8 bp (D1) per 2-year-equivalent unit, 0.25 / 1.9 (variants.py).`
Reason: as item 6.
8. Define the bad state of the currency falsifier.
- Find: `- Currencies: losses that come without a bad state (the risk story predicts losses in bad states and pay otherwise).`
- Replace: `- Currencies: losses that come without a bad state (the risk story predicts losses in bad states and pay otherwise). Fixed here: bad-state months = the design stress windows of config.py STRESS_WINDOWS that end by 2010-12 (1987-10..11, 1990-08..10, 1994-02..11, 1998-08..10, 2007-07..08, 2008-09..12) plus the worst fifth of eq_us_spx months over 1975-2010; the claim fails if the currency leg's mean return in those months is not below its mean in the other months.`
Reason: brief check B ("fixed, numeric where the notes allow"); config.py:68-75; [[QP08 - Dissecting Investment Strategies in the Cross Section and Time Series (Baz, Granger, Harve#^QP08-C04-5|QP08-C04-5]] names bad consumption states without a measure.
9. Profit-source line with fixed conditions.
- Find: `end): a Carry leg whose price part is strongly negative and income part positive is paid as carry says; a leg paid`
- Replace: `end): the carry claim fails for a leg whose income part is zero or below, or whose price part is larger than its income part (paid by price moves, not by carry); in short, a leg paid`
Reason: a price part that fully offsets income is uncovered parity, not carry pay; "strongly" and "mostly" had no threshold.
10. Bond falsifier without a conditional placebo.
- Find: `- Bonds: the leg is only a standing long: its return is matched by a position with the same average exposure and no`
- Replace: `- Bonds: the leg is only a standing long: its design net return is not above that of a constant position in each bond equal to the leg's average position in it (same sizing and costs; computed whether or not 3.4 registers a placebo for existing pods), a position with the same average exposure and no`
Reason: 1.3b s3 "the directional bond leg may be a standing long position (C17-2b)"; the line depended on a 3.4 decision.
11. Book-level hindsight count.
- Find: `market list = 3 (+1 book).`
- Replace: `market list = 3 (+3 book: pod share, no risk scaler, no scenario limit; SPEC_Trend section 12).`
Reason: gm_trials.csv scaler and scenario rows.
12. Strip cost rolls note.
- Find: `Double-cost test applies. No turnover figure in the notes.`
- Replace: `Double-cost test applies. No turnover figure in the notes. A strip rolls one of its eight contracts a quarter, so charging 4 full rolls a year over-costs it (conservative; 3.4).`
Reason: book.py:213 roll charge on the whole position; strip = eight contracts in equal parts (section 3).

### SPEC_Value.md

1. Rule 7: add the GB and euro-area rate gap.
- Find: `Rule 7: every input has a free live source (non-US dividend yield weak), so Value passes rule 7;`
- Replace: `Rule 7: every input has a free live source (non-US dividend yield weak), so Value passes rule 7 once the GB and euro-area OECD 3-month rates have a replacement (they end 2026-01, panel.py:368-370; Value's sizing and returns use the excess returns of fx_gbp, fx_eur, bd_gb_10y and bd_de_10y, missing from early 2027; 3.4);`
Reason: panel.py:368-370, 478, 511; book.py:102, 132 (vol from R).
2. Re-check of T70.
- Find: `against the currency leg (C14): recorded, no change.`
- Replace: `against the currency leg (C14): recorded, no change. Card 2 T70 (short the most successful stock market, "Value may hold it"): held only in part: Value ranks 8 developed indexes on dividend yield, not on past return, and the 10 indexes without a free dividend yield (emerging, Nasdaq 100, Russell 2000, Euro Stoxx 50) are never ranked.`
Reason: register T70; signals.py:293-327 (FRENCH_DY 7 + US), book.py:105.
3. Book-level hindsight count.
- Find: `Hindsight count: 3 (+1 seen version leg).`
- Replace: `Hindsight count: 3 (+1 seen version leg; +3 book: pod share, no risk scaler, no scenario limit; SPEC_Trend section 12).`
Reason: gm_trials.csv scaler and scenario rows.

## 4. Items for step 3.4

1. All four specs, s3: decisive trade timing. The monthly run trades at the decision-day close (timing.py k = 0);
   WORKFLOW s5 asks for the one-day live delay (k = 1, needs daily returns; free daily data lack non-energy commodities
   before 2000, register D9). Register which form is decisive before A2.
2. All four, s3/s5: WORKFLOW s5 says "Anything estimated from data ... uses an expanding window"; the engine uses
   trailing rolling windows (vol 36 / 120 months, zchg 120, block and book scalers 36). Point in time, but not
   expanding: read "expanding" as "trailing, never full-sample", or register a change.
3. All four, s8: rule 7 gap of the GB and euro-area 3-month rates after 2026-01 hits every pod through the excess
   returns, not only Carry and Economic trend.
4. All four, s12: book-level hindsight count is 3 (pod share vector, no risk scaler, no scenario limit).
5. SPEC_Value s8 / s3: the design equity signal uses month-t dividends; the live Ken French file lags up to 12 months
   (and can lapse under ffill limit 12). Register a design lag that mirrors the live delay, or a monthly live source
   (LSEG, not registered).
6. SPEC_Economic_trend s3: Germany's risk theme (also fx_eur's and the commodity block's) uses eq_eu_stoxx50 by dict
   order and so lacks its equity part until about 2003-07 although DAX starts 1988-01; the euro trade theme uses
   Germany's NEER (BIS EZ -> XM map is dead code). Record as code facts; any change is a registered engine version.
7. SPEC_Economic_trend s3, SPEC_Value s8: the quarterly-CPI metadata check must also confirm the OECD csv is read at
   all (signals.py:74-75 swallows any parse error and returns an empty table, which moves every country to FRED).
8. SPEC_Carry s3, s9: T10 strip carry scale and cost on the 2-year-equivalent basis of the gross weight; roll charge
   for a strip; register with the D1 extension. Same strip enters Trend and Economic trend: the S1 short-rate trial is
   already seen for all three hosts.
9. SPEC_Trend s3, s7: the tranche calendar and the 2010-12-31 cut also bind the weekly check of every other pod
   (all specs point to SPEC_Trend s3).
10. SPEC_Economic_trend s10: D5's two claim lines are holdout/live statements; 3.4 states how the holdout report uses
    them.
11. SPEC_Carry s10: the bad-state set (stress windows + worst fifth of S&P months) can be shared with card 2 D1 and
    charter D4 so that the shop has one crisis-state table (register A, D4 note).
12. Writer's NOTES (b) items 1-13 stand as written (rule 5 reading, pod shares vs WORKFLOW 5.1, engine flags for the
    Bloomberg switches before A1, quarterly CPI fix, V1 already seen, D3 end at 2009-12, placebo for existing pods, X2
    noise band, D5 power, shape report, W5 bands); bloomberg.py EQ_INDEX (MXEM for eq_eu_stoxx50; MXUS for Nasdaq and
    Russell) is a defect to fix before any Bloomberg composite is ever used.

## 5. What I could not verify

- Data facts behind the code: the start of EIA CL contract 2 (inferred from the market_months count, which assumes no
  gaps); whether oecd_cpi_yoy.csv holds AU and NZ, and how quarterly values are stamped; whether FRED NB..BIS series
  are monthly averages; the publication lags of the OECD 3-month and CPI series by country in the design years.
- tools/bbgq/results/gm_bbg_map_v1.txt (NOTES item 3: Value composite live for 18 indexes): not read, outside the
  read list.
- SPEC_Value s10 loss example (late-1990s US run): needs data; from public history Japan's dividend yield was also very
  low then, so the US may not have been the dearest of the 8 indexes.
- Whether card 4's "neglected market" (T94) is a commodity (card 4 text not read in full; Checker C's scope).
- Licence terms of the MSCI manual file for live use.

