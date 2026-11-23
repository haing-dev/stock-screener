---
tags: [fable, thesis]
code_commit: 78799ed
---
> Fresh Opus check of the step 3.1 specs (group C). See [[Thesis register 1.5]]. Source: [repo file](https://github.com/haing-dev/stock-screener/blob/78799edd251d9e74a749bd23aa6fc507e9a99d0c/docs/research/specs/checks/CHECK_3.2_C.md).
# Step 3.2 spec check, Checker C (card pods 1-5), 2026-11-23

Checker: Opus 5.5 (quant and risk officer), independent of the writer. Read in full: the five specs and agent_C/NOTES.md;
BRIEF_OPUS.md; the five cards and their checks (rule, diagnostic, process and check-verdict sections in full, the rest
by section); THESIS_REGISTER_1.5.md (all); WORKFLOW sections 1-8; TESTING_PROTOCOL eras; gm_trials.csv; gm_CHANGES
search; BOOK_FACTS search; DATA_DIGEST search; DATA_SHEET (the five are one file, md5 identical). Code read: gm/config.py,
book.py, vol.py, signals.py (all), panel.py (universe, fx_usd_value, build, par_ret), daily.py header, bloomberg.py
(COMMOD_ER, ALT_COMMOD, CURVE_ROOT); tools/bbgq/engine_ref.json (keys and market_months only, the design-month count
per market up to 2010-12); macro/registry.py comment lines 25-47 (to trace two "Compass" knobs). Every quoted phrase in
the specs was looked up in its ledger quote (all 66 present; each supports its use). No backtest, no market data, no
2011+ result, no web.

## 1. Verdict

| Spec | Verdict | A faithful | B can fail | C hindsight | D specified / point in time | E code | F data, costs | G shop rules | Corrections |
|---|---|---|---|---|---|---|---|---|---|
| SPEC_Card1_policy_liquidity.md | APPROVED WITH CORRECTIONS | 1 | 0 | 1 | 6 | 2 | 4 | 0 | 16 |
| SPEC_Card2_regime_debt_cycle.md | APPROVED WITH CORRECTIONS | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 5 |
| SPEC_Card3_relative_value_risk.md | APPROVED WITH CORRECTIONS | 0 | 2 | 0 | 3 | 1 | 1 | 0 | 7 |
| SPEC_Card4_flows_volatility.md | APPROVED WITH CORRECTIONS | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 4 |
| SPEC_Card5_commodity_balances.md | APPROVED WITH CORRECTIONS | 0 | 0 | 0 | 1 | 0 | 4 | 1 | 6 |

Counts are findings that need a correction (some findings take two Find/Replace pairs). No spec is rejected: every
defect is a wording, data-fact or closure fix; no rule needs a new thesis. Theses, grades, gates, version counts (28/56,
8, 16/32, 16/+14, 8/16; total 76 as in register G), dating classes (C; card 4 R1, R2, R4 B) and statuses match the notes
and the register.

## 2. Findings per spec

### SPEC_Card1_policy_liquidity.md

A. Faithful
- Theses, labels (C2 SHOWN one case, C3 SHOWN words, C1/C4/C5 ASSERTED, C6 one case), rules R1-R5, R6 held back,
  12-month tail, entry thirds, 28 (56) versions, gates C1-D1 (6 episodes) and C1-D2 (80%) match card s4, s6, s10 and
  register T13-T19. All 17 quoted phrases are in their quotes and support their use.
- C1-D2 counts "months in which the leg holds a position (any version, tail included)"; the card says "on-months". The
  held-month base is the better reading of "already held", but it is a choice and is not labelled "closed here"
  (correction 15).

B. Can it fail
- Falsifiers are numeric and not satisfied by construction. Two read sealed months (listed under D).

C. Hindsight
- The R3 10-month S&P average is not a neutral convention: it is the Macro Compass growth-trend cut ("S&P 500 below its
  10-month average", macro/registry.py derisk, 4.0.0), adopted "from the combination tests" backtested from 1975-01
  through the holdout years. The rule differs (Compass cuts stocks; R3 buys them), so this is "seen in a related rule",
  not a gm_trials row; it belongs in the tally (corrections 13-14). No gm_trials.csv row or CHANGES entry touches a card
  knob (checked: rows are book-level families, scalers, speeds, batch 0/1, fixes). The R4 gate tally of 1 is right.

D. Specified and point in time
- Entry E3 "cumulative excess return ... above zero" is wrong for short legs (R3 10-year, R4 bonds and S&P): the test
  must be signed by the leg's direction (correction 1).
- R1 step 3 cites "R4 step 2" for the state; the state is R4 step 1 (correction 2).
- R3 gold version: panel gold has about 108 design months in the free engine (engine_ref.json market_months, so from
  about 2002). The spec does not say what the gold versions do before 12 panel month-ends exist (correction 4).
- Section 10 R1/R2: "GS2 ... 12 months after the last condition month" reads 2011 for episodes ending after 2009-12
  (correction 11). R5: "over the 12 months after triggers" reads 2011 for triggers after 2009-12 (correction 12).
- R5 universe: whether "in the panel" is static or monthly, and what a leg without a return does, is open; read
  monthly with both markets required it would bar every trigger before about 1995 (bonds: GB 1994, AU 1995, CA 2001),
  including the 1992 source case (correction 6).
- Accepted closures: first-vintage reading, TWEXMMTH/DTWEXBGS splice inside one series, R1 2-year leg absent before
  bd_us_2y (k fixed at 2, so the 10-year carries half a unit; deterministic), basket legs, R5 price-change trigger and
  median set, episode gap, D2 combination via the incumbent book's sign, tranche 0 in monthly runs (charter s4 text),
  no trailing rescaling. JP1 (R6: no short-gold form without new card text) and JP3 (keep the gate as a version,
  counted in the tally) are accepted as 3.2's answers.
- Lag 0 for FRED monthly averages (FEDFUNDS, GS2, GS5, GS10, BAA, TWEXMMTH) follows the data sheet, but the last
  business days are published after the month end (H.15 next day, H.10 weekly): item for 3.4 (shared).

E. Code
- "^GSPC close, the series panel.py reads" is false: panel.py never reads ^GSPC; eq_us_spx is SPY total return less
  cash, before 1993 the French US market (panel.build); ^GSPC is read by signals.equity_dy and daily.py EQ_DAILY
  (correction 3).
- "Carry ... is short a bond whose yield is below the 3-month rate": Carry is kind "half" in book.family_positions
  (half sign, half cross-sectional rank), so only its directional half is short by construction (correction 16).
- Verified true: CANDIDATE trend = mean sign of 1/3/12-month excess-return levels (book.trend_signal); hybrid vol as
  described (vol.estimate); 0.40/vol (family_positions); costs (cost_bp); Economic trend monetary m = zchg of 2-year
  yield or lagged 3-month rate, FI -1; trade theme minus log NEER, EQ +1, FI -1; inflation theme headline CPI yoy (OECD
  file, then CPALTT01), EQ -1, FI -1, CM +1; ECON_THEMES has no growth; panel has no CH/NZ/SE/NO stock index. Note: in
  CANDIDATE the econ family is ONE averaged score per market (econ_structure not set, so econ_scores), so a theme is a
  quarter of the position; the specs' "partly" wording is right.

F. Data and costs
- "before about 2000 many [commodities] are World Bank monthly average spot" is false for the code: panel.py
  ALLOW_AVG = False, so no World Bank spot enters; free-engine design months: cm_wti 311 (from 1985), cm_natgas 203,
  cm_heatoil 202 (1994), others 84-131 (2000-2003), cm_brent 33 (corrections 8, 10).
- R4-B's basket is therefore empty in every 1970s state month (the card calls the 1970s one long episode, s13): action
  B is A plus the S&P short there. The rule stays deterministic (k fixed at 4); the fact must be stated (correction 5).
- fx_eur: 143 design months (from 1999); the panel has no mark series (fx_usd_value: DEXUSEU, Yahoo, stooq; EXGEUS is
  not used). "mark, then euro" cannot be built (corrections 7, 9). NOTES (a) 6 is wrong on this.
- bd_us_2y: 414 design months, so returns from 1976-07, consistent with the reader's GS2 1976-06.
- Costs match cost_bp. Rule 7 conclusion (cannot be Core) right.

G. Shop rules: versions averaged, signs fixed, sample fixed, nothing registered, no 2011+ number. OK.

### SPEC_Card2_regime_debt_cycle.md

A. R1, R2, grids (4 + 4), C2-D2 gates (24 on-months, 3 episodes, two thirds), C2-D1 gate and its effect on card 1, and
the falsifiers match card s4, s8, s10 and register T20-T22. Quotes (8) verified. "Either threshold" = the 4.5 state is
right (the 5.0 state is a subset). C2-D1 country list (US, JP, DE, GB, CA) checked against panel.BONDS and EQUITY.
B. Falsifiers are the card's; fine apart from the sealed read (D).
C. The R1 hedge gate (12-month stock-bond correlation above zero) has the window and threshold of the Macro Compass
  stockbond switch (data sheet "stockbond"; macro/registry.py derisk 4.1.0, bonds_if_corr_below 0.0), adopted after
  backtests from 1975 that include the holdout years (corrections 3-4).
D. Section 10 R2 falsifier and mechanism check: "12 months after on-months" and "other months" read 2011 for months
  after 2009-12 (corrections 1-2). Other closures accepted (first vintage, episode gap, "either threshold", Japan pooled
  as written).
E. Verified: Value kind "cs" (no directional bond short); bond value = 10-year minus trailing 36-month CPI mean; equity
  monetary theme EQ -1 on the US 2-year change (partial overlap with R2, contrary to the card); growth not held.
F. ^GSPC is listed as a panel series; it is a Yahoo file read by signals.py and daily.py, first date not confirmed
  (correction 5). Costs right. Rule 7 right.
G. OK.

### SPEC_Card3_relative_value_risk.md

A. R1-R4, grids (8, 2, 4, 2; 32 with the floor), C3-D1 and C3-D2 gates, falsifiers (a)-(d), process rules and the 10
  questions match card s4-s10 and register T23-T27. Quotes (12) verified. The C3-D1 "Core book" problem is correctly
  flagged with a proposal for 3.4 (kept, section 4).
B. Falsifiers for R2 and R4 are only "(a) not positive after costs or fails placebo", which is "fails the test", not a
  rejection of the claim (correction 6). Section 11's "central banks on hold" can be made observable with R1's own gate
  measure (correction 7).
C. Tally of 2 (activity gate, 1.0 bar) is the card's and right.
D. R1 starts are one month early: with lag 1 the first L-month change needs r(t-1-L), so 1975-08 (L 6) and 1976-02
  (L 12), not 1975-07 and 1976-01 (corrections 1-2). A currency without a panel return (the euro before 1999) is not
  excluded from shape A's comparison or shape B's ranking and baskets (correction 3). "Fixed size while on" breaks R1:
  its gate-off versions are never off, so one notional would be fixed from 1975 to 2010; an on-run must be a same-sign,
  same-role run per leg (correction 4). Accepted: lag 1 for the whole rate row, semiannual par durations (matches
  panel.par_ret), pair volatility on the pair's monthly series (daily.py has no pair, so vol.estimate falls back to the
  monthly fast part), R4 lag 0.
E. "the level the panel already reads" (^GSPC) is false (correction 5). Verified true: Economic trend FX monetary
  theme = local minus US change of the 2-year yield (US, DE for the euro, CA, AU, JP) else lagged 3-month rate, FX +1;
  no sp_ market is in any family (CLASSES has no sp_ prefix); Carry kind half, bond carry = yield minus lagged TB3MS.
F. fx_eur from 1999 and fx_sek from about 1982 in the free engine (143 and 347 design months); the mark has no panel
  series (in correction 1). Costs right (G10 FX 2.0 bp, 4 rolls). Rule 7 right.
G. OK.

### SPEC_Card4_flows_volatility.md

A. R1-R5, grids (6, 4, 2, 2, 2 = 16; +14 with the C4-D1 sizing version), C4-D1, C4-D2, falsifiers and the 10 questions
  match card s4-s10 and register T28-T33. Quotes (21) verified. Open choice 1 (gap after expiry) is closed here as 3.2:
  [[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293|MT076]] was uploaded 2024-05-02 and May 2024's third Friday was the 17th, so "for the next two weeks" runs into expiry,
  and [[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C06-X1|MT076-C06-X1]]'s quote puts the weakness after the expiry weekend (correction 4).
B. Loss path error: X in October 1987 was Friday the 16th; the next trading day was Monday the 19th, so the crash lies
  inside the two R2 versions that exit at the next day's close, not "in the gap" (correction 3; calendar computed).
D. The daily build is sound (outcome measure; no look-ahead), but the monthly aggregation for the monthly test sheet is
  not stated (correction 2). C4-D1's sealed read is correctly flagged with the 2010-06 proposal. Window cut at
  2010-12-31 and the C4-D2 closures accepted.
E/F. c(m) is not "dividends minus cash" before 1993: the panel's eq_us_spx is then the French US market, so c(m) also
  carries the French-minus-S&P gap (correction 1). daily.py EQ_DAILY reads ^GSPC: true. Costs right. Rule 7 right.
G. OK. The 1983 options split is a reported line, not a thesis: accepted.

### SPEC_Card5_commodity_balances.md

A. R1, R2 held back with its release condition, grid 8/16, C5-D1 (75%) and C5-D2 (15 points, 10 breaks, cut 2008-12)
  match card s4, s10 and register T34-T36. Restricting C5-D2's slow class to tradable markets matches the card check's
  JP3 reading ("which base metals have an LSEG futures curve and a panel return"). Quotes (12) verified.
D. C5-D1 "R1's on-months" is undefined; R1's trigger months are new all-time highs at which every 12-month Trend
  version is long by construction, so a trigger-month base decides the gate by construction (correction 5). The
  real-ceiling re-entry restriction ("stays flat until ...") goes beyond the card's "ends" but is deterministic:
  accepted.
F. "cm_copper ... before futures data is World Bank monthly average spot" is false (ALLOW_AVG off); free-engine copper
  has about 89 design months (from about 2003), WTI 311 (from 1985), so copper runs before 2003 earn nothing unless the
  A1 Bloomberg swap supplies GSCI copper (corrections 1-4). Code facts verified: COMMOD has copper as the only base
  metal and no cocoa; ALT_COMMOD holds cm_cocoa, cm_alu, cm_zinc, cm_nickel, cm_lead; CURVE_ROOT maps cm_copper to HG;
  Value keeps fx_, bd_, eq_ only ("commodity value: failed, out"). Costs right. Rule 7 right.
G. Section 16 says "markets copper and WTI only" while section 3 lets a registered Batch A item add a slow-class
  market (correction 6).

## 3. Required corrections

### SPEC_Card1_policy_liquidity.md

1. Entry E3 test must be signed by the leg's direction.
- Find: `full once that leg's cumulative excess return since the entry month end is above zero at a month end`
- Replace: `full once that leg's cumulative excess return since the entry month end, multiplied by the leg's direction (+1 long, -1 short), is above zero at a month end`
Reason: card s6 "moved the trade's way"; R3's 10-year leg and R4's legs are short. Check D.

2. Wrong cross-reference for R4's state.
- Find: `R4's state at 5.0 is on (R4 step 2)`
- Replace: `R4's state at 5.0 is on (R4 step 1)`
Reason: spec s3 R4 step 1 defines the state, step 2 the action. Check D.

3. ^GSPC is not a panel.py series.
- Find: `(^GSPC close, the series panel.py reads; spx_trend live)`
- Replace: `(^GSPC month-end close from the Yahoo file that signals.equity_dy and daily.py read; panel.py holds no S&P price level, its eq_us_spx is the French US market before SPY; first date of the file not confirmed; spx_trend live)`
Reason: gm/panel.py build (eq_us_spx = SPY or French mkt_rf); signals.equity_dy and daily.py EQ_DAILY read ^GSPC. Check E.

4. Gold version before panel gold exists.
- Find: `live from GC=F.`
- Replace: `live from GC=F. In the free engine cm_gold has about 108 design months (tools/bbgq/engine_ref.json market_months, so from about 2002); until 12 month-ends of panel gold exist the gold versions are off (zero), unless A1's Bloomberg data swap has given cm_gold an earlier history before B2 is registered (3.4 records which).`
Reason: engine_ref.json market_months cm_gold 108; spec s3 step 6 (off = zero). Check D/F.

5. State what R4-B's basket holds in the design years.
- Find: `cm_cattle; not cm_aqr_ew, no Bloomberg alternative commodities), equal risk inside the basket.`
- Replace: `cm_cattle; not cm_aqr_ew, no Bloomberg alternative commodities), equal risk inside the basket. Code fact: panel.py uses no World Bank spot (ALLOW_AVG off); in the free engine the first of these returns starts in 1985 (cm_wti) and most start in 2000-2003 (engine_ref.json market_months), so in the 1970s state months (card s13: one long episode) the basket is empty, its leg holds zero (k stays 4) and action B is A plus the S&P short; whether cm_aqr_ew or A1's Bloomberg indexes should fill it is for 3.4 and changes no rule here.`
Reason: panel.py ALLOW_AVG = False and build(); engine_ref.json; card s13. Check F.

6. R5 universe membership and missing legs.
- Find: `Universe: G10 currencies in the panel, other than the dollar, whose stock index and 10-year bond are in the panel:`
- Replace: `Universe: G10 currencies in the panel, other than the dollar, whose stock index and 10-year bond are panel markets (panel.py ids; membership is static, so the trigger set does not wait for the bonds; a leg without a return that month holds zero and k stays as in section 5):`
Reason: card R5 text; bond panel starts (engine_ref.json: bd_gb_10y 205, bd_au_10y 191, bd_ca_10y 119 design months) would otherwise bar triggers before about 1995, including 1992. Check D.

7. The panel holds no mark.
- Find: `fx_eur (mark, then euro: eq_de_dax, bd_de_10y; check item 20)`
- Replace: `fx_eur (euro only: the panel holds no mark series and fx_eur has about 143 design months in engine_ref.json, so from 1999; eq_de_dax, bd_de_10y; the card's mark mapping, check item 20, cannot be built from the panel)`
Reason: panel.fx_usd_value (DEXUSEU, Yahoo, stooq; EXGEUS unused); engine_ref.json fx_eur 143. Check F.

8. Commodity history statement is wrong for the code.
- Find: `each from its first panel month; before about 2000 many are World Bank monthly average spot (panel flag "spot avg")`
- Replace: `each from its first panel month: in the free engine WTI from 1985, natural gas and heating oil from 1994, the rest from 2000-2003 (engine_ref.json market_months); no World Bank spot is used (panel.py ALLOW_AVG off)`
Reason: panel.py ALLOW_AVG = False; engine_ref.json. Check F.

9. FX row: euro start and no mark.
- Find: `first month of panel.fx_usd_value; fx_eur before 1999: the panel's source (stooq eurusd) is not shown to be the mark in the code; builder records what it is`
- Replace: `first month of panel.fx_usd_value (H.10 daily from 1971 for JPY, GBP, AUD, CAD); fx_eur from 1999 only (engine_ref.json: 143 design months); there is no mark series in the panel`
Reason: panel.DEX and fx_usd_value; engine_ref.json. Check F.

10. Data table start dates.
- Find: `| free panel (gm/panel.py) from 1975 |`
- Replace: `| free panel (gm/panel.py): US bonds and equities from 1975, each other market from its own first month (free engine: euro 1999, gold about 2002, copper about 2003, WTI 1985; engine_ref.json); ^GSPC is a Yahoo file read by signals.py and daily.py, first date not confirmed |`
Reason: engine_ref.json market_months; panel.py. Check F.

11. GS2 test must not read 2011.
- Find: `than half of the episodes, GS2 is higher 12 months after the last condition month than at it (the Fed did not reverse,`
- Replace: `than half of the episodes whose last condition month is 2009-12 or earlier (so the 12-month look stays inside the design window), GS2 is higher 12 months after the last condition month than at it (the Fed did not reverse,`
Reason: WORKFLOW rule 5 and s6 (holdout sealed); register D15 logic. Check D.

12. R5 falsifier window.
- Find: `the stock leg's mean excess return over the 12 months after triggers is zero or less`
- Replace: `the stock leg's mean excess return over its held months up to 2010-12 is zero or less`
Reason: triggers after 2009-12 would read 2011 returns. Check D.

13. The 10-month average was seen in a related backtest.
- Find: `| R3 0.25 over 3 months, median / lowest third, 10-month average, gold 12-month high |`
- Replace: `| R3 0.25 over 3 months, median / lowest third, 10-month average, gold 12-month high (the 10-month S&P average is the Macro Compass growth-trend cut, macro/registry.py derisk 4.0.0, adopted after combination backtests from 1975 that include the design and holdout years: seen in a related rule) |`
Reason: macro/registry.py lines 28-36 ("from the combination tests", "backtest_from": "1975-01"). Check C.

14. Hindsight tally.
- Find: `Chosen after seeing design results: 0 (no gm_trials.csv row or CHANGES entry touches any card knob).`
- Replace: `Chosen after seeing design results: 0 in gm_trials.csv and CHANGES (no row touches a card knob); seen in a related rule of another tool: 1 (the 10-month S&P average, Macro Compass).`
Reason: as item 13. Check C.

15. Label the C1-D2 month base as a closed choice.
- Find: `Share of months in which the leg holds a position (any version, tail`
- Replace: `Share of months in which the leg holds a position (closed here: held months, not only condition months, because the question is whether the position is already held; the card says "on-months"; any version, tail`
Reason: card s10 D2 wording; brief: every closure flagged. Check A.

16. Carry is half directional.
- Find: `Carry (signals.carry_values: yield minus 3-month rate) is short a bond`
- Replace: `Carry's directional half (signals.carry_values: yield minus 3-month rate; book.family_positions kind half = half sign, half rank) is short a bond`
Reason: gm/book.py family_positions, fams carry kind "half". Check E.

### SPEC_Card2_regime_debt_cycle.md

1. R2 falsifier must not read 2011.
- Find: `- R2: the S&P's return in the 12 months after on-months is no lower than in other months (card's own falsifier).`
- Replace: `- R2: the S&P's return in the 12 months after on-months is no lower than in other months (card's own falsifier); both sets use months up to 2009-12 only, so no 12-month look reads 2011.`
Reason: WORKFLOW rule 5 / s6 seal; register D15 logic. Check D.

2. Same for the mechanism check.
- Find: `over the same 12 months`
- Replace: `over the same 12 months (on-months up to 2009-12 only)`
Reason: as item 1. Check D.

3. Hedge gate origin.
- Find: `| R1 hedge gate, 12-month correlation above zero | reader, joining [[MT138 - Rob Citrone and Karen Karniol-Tambour at Sohn 2025#^MT138-C06-X1|MT138-C06-X1]] and [[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C10-3|MT068-C10-3]] |`
- Replace: `| R1 hedge gate, 12-month correlation above zero | reader, joining [[MT138 - Rob Citrone and Karen Karniol-Tambour at Sohn 2025#^MT138-C06-X1|MT138-C06-X1]] and [[MT068 - Greg Jensen - Co-CIO of Bridgewater Podcast In Good Company Norges Bank Investment Managem#^MT068-C10-3|MT068-C10-3]]; same window and threshold as the Macro Compass stockbond switch (data sheet; macro/registry.py derisk 4.1.0, bonds_if_corr_below 0.0), adopted there after backtests from 1975 that include the design and holdout years: seen in a related rule |`
Reason: macro/registry.py lines 35-40; DATA_SHEET Compass list. Check C.

4. Hindsight tally.
- Find: `Chosen after seeing design results: 0.`
- Replace: `Chosen after seeing design results: 0 in gm_trials.csv and CHANGES; seen in a related rule of another tool: 1 (the hedge gate's window and threshold, Macro Compass).`
Reason: as item 3. Check C.

5. ^GSPC is not a panel series.
- Find: `| ^GSPC month-end; panel eq_us_spx, bd_us_10y | free panel, 1975 |`
- Replace: `| ^GSPC month-end (Yahoo file read by signals.equity_dy and daily.py, not a panel series; first date not confirmed); panel eq_us_spx, bd_us_10y | free panel, 1975 |`
Reason: gm/panel.py build; signals.equity_dy. Check F.

### SPEC_Card3_relative_value_risk.md

1. R1 market starts: lag-1 arithmetic, euro and krona starts, no mark.
- Find: `first month with a panel return and a rate change of length L; with LSEG deposit rates from 1975 (digest), 1975-07 (L 6) and 1976-01 (L 12); fx_eur before 1999 is the panel's EUR series, whose pre-1999 source (stooq eurusd) is not shown to be the mark: the builder records it`
- Replace: `first month with a panel return and a rate change of length L at lag 1; with LSEG deposit rates from 1975-01 (digest), 1975-08 (L 6) and 1976-02 (L 12); fx_sek from about 1982 and fx_eur from 1999 only (engine_ref.json: 347 and 143 design months); the panel holds no mark series, so that leg cannot trade before 1999`
Reason: spec s3 R1 step 2 (change at t = r(t-1) - r(t-1-L)); engine_ref.json; panel.fx_usd_value. Check D/F.

2. Same arithmetic in the sample section.
- Find: `1975-07 if every LSEG deposit rate starts in 1975-01 (the L 6 versions; L 12 join 1976-01)`
- Replace: `1975-08 if every LSEG deposit rate starts in 1975-01 (the L 6 versions, lag 1; L 12 join 1976-02)`
Reason: as item 1. Check D.

3. Currencies without a return.
- Find: `7. Positions in the panel FX markets (long a currency = long fx_xxx).`
- Replace: `7. Positions in the panel FX markets (long a currency = long fx_xxx). A currency without a panel return that month (the euro before 1999; the panel has no mark) is left out of shape A's comparison and of shape B's ranking and baskets (closed here).`
Reason: otherwise shape B can pick a leg with no market; engine_ref.json fx_eur 143. Check D.

4. Fixed size needs an on-run definition for R1.
- Find: `and kept until it turns off (each weekly tranche fixes its own notional on its own on-day).`
- Replace: `and kept until it turns off (each weekly tranche fixes its own notional on its own on-day). For R1 an on-run is a run of months in which a leg keeps the same sign and the same role (R1's gate-off versions are never off, so without this one notional would be fixed from 1975 to 2010).`
Reason: spec s3 R1 steps 4-5 (always long or short unless equal). Check D.

5. ^GSPC is not a panel.py series.
- Find: `(^GSPC close; closed here: the level the panel already reads)`
- Replace: `(^GSPC month-end close; closed here: the Yahoo file the engine already reads in signals.equity_dy and daily.py; panel.py holds no S&P price level)`
Reason: gm/panel.py build; signals.equity_dy. Check E.

6. Claim-level falsifiers for R2 and R4.
- Find: `(b) R1's gate-on versions do no better than its gate-off versions (against C1).`
- Replace: `(b) R1's gate-on versions do no better than its gate-off versions (against C1). R2: the pair's mean monthly return over on-months is zero or less, or more than 80% of its P&L comes in months with FEDFUNDS down over 6 months (the easing trade, not the duration premium; numbers as card 4 R5, this check's). R4: the S&P's mean excess return in on-months is no lower than in off-months.`
Reason: brief s10 (reject the claim, not just fail the test); card C4 and R4 mechanisms. Check B.

7. Make the stop condition observable.
- Find: `Card s8: central banks on hold and guiding the path (their account of 2010-21);`
- Replace: `Card s8: central banks on hold and guiding the path (their account of 2010-21; observable live as R1's activity gate off, FEDFUNDS 12-month range below 0.50);`
Reason: brief s11 (observable live); spec s3 R1 step 6. Check B.

### SPEC_Card4_flows_volatility.md

1. What c(m) holds before SPY.
- Find: `(dividends minus cash for that month)`
- Replace: `(dividends minus cash for that month; before SPY in 1993 also the gap between the French US market return and the S&P 500 price return, since the panel's eq_us_spx is the French market then)`
Reason: gm/panel.py build, eq_us_spx = first(SPY - rf, French mkt_rf). Check E/F.

2. Monthly aggregation for the test sheet.
- Find: `Live: SPY total return minus the daily cash rate.`
- Replace: `Live: SPY total return minus the daily cash rate. A rule's monthly return for the test sheet = the sum over the month's trading days of its position times e(d) (closed here).`
Reason: WORKFLOW s5 design tests are monthly; the builder otherwise chooses sum or compounding. Check D.

3. October 1987 loss path.
- Find: `and the 19 October crash fell in the gap after it.`
- Replace: `and in the two versions that exit at the close of the next trading day the 19 October crash (the Monday after X) is inside the window; in the other two it falls in the gap.`
Reason: calendar: third Friday of October 1987 = 16th, next trading day Monday 19th; spec s3 R2 step 3. Check B.

4. Close open choice 1 at 3.2.
- Find: `| 1 | Support before X: reading of "for the next two weeks" ([[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C07-4|MT076-C07-4]]) (check JP1) | kept as the card places it; 3.2 |`
- Replace: `| 1 | Support before X: reading of "for the next two weeks" ([[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C07-4|MT076-C07-4]]) (check JP1) | kept as the card places it; confirmed at 3.2: [[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293|MT076]] was uploaded 2024-05-02 and May 2024's expiry was the 17th, so the two weeks run into expiry, and the weakness comes after it: "a lot of the all that Bond and charm is now passed coming out of that weekend" ([[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C06-X1|MT076-C06-X1]]) |`
Reason: [[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293|MT076]] metadata (upload 2024-05-02); [[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C06-X1|MT076-C06-X1]] and [[MT076 - How Global Conflicts affect the Economy & 2024 Outlook - Systematic Investor 293#^MT076-C07-4|MT076-C07-4]] quotes. Check A.

### SPEC_Card5_commodity_balances.md

1. Copper return history.
- Find: `returns: cm_copper's panel source, which before futures data is World Bank monthly average spot (panel flag "spot avg")`
- Replace: `returns: cm_copper's panel source, which in the free engine covers only about 89 design months (engine_ref.json market_months, so from about 2003; no World Bank spot, panel.py ALLOW_AVG off): copper runs before then earn nothing unless A1's Bloomberg swap has given cm_copper a GSCI excess-return history before B2 is registered (3.4 records which)`
Reason: panel.py ALLOW_AVG = False, COMMOD pieces, bloomberg.COMMOD_ER; engine_ref.json. Check F.

2. WTI return start.
- Find: `returns: panel, EIA contracts from 1983`
- Replace: `returns: panel, EIA contracts (cm_wti has 311 design months in engine_ref.json, so from 1985)`
Reason: engine_ref.json market_months. Check F.

3. Data table.
- Find: `| free panel (copper before futures: World Bank monthly average) |`
- Replace: `| free panel (free engine: copper from about 2003, WTI from 1985; engine_ref.json) |`
Reason: as items 1-2. Check F.

4. Pack note does not apply.
- Find: `Pack note: monthly-average spot returns before futures data smooth returns (TESTING_PROTOCOL warns of false trends);`
- Replace: `Pack note: the panel uses no monthly-average spot returns (panel.py ALLOW_AVG off), so TESTING_PROTOCOL's false-trend warning does not apply to these returns;`
Reason: gm/panel.py ALLOW_AVG. Check F.

5. Define C5-D1's on-months.
- Find: `- C5-D1 overlap (gates R1). Share of R1's on-months`
- Replace: `- C5-D1 overlap (gates R1). Share of R1's on-months (closed here: months in which any version holds a position, because trigger months are new all-time highs at which every 12-month Trend version is long by construction)`
Reason: card s10 D1 leaves "on-months" undefined for a hold rule; spec s3 R1 step 2. Check D.

6. Market list consistent with section 3.
- Find: `markets copper and WTI only;`
- Replace: `markets as fixed at 3.4 (copper, and WTI in the crude version, unless a registered Batch A item has added a slow-class market, section 3);`
Reason: spec s3 R1 step 5 vs s16. Check G.

## 4. Items for step 3.4

1. All cards with commodities (card 1 R3 gold, R4-B; card 5 R1): the free engine's commodity history starts 1985 (WTI) and
   2000-2003 (the rest); A1's Bloomberg swap would change it. 3.4 must record which panel history B2 runs on before any
   card run, and whether cm_aqr_ew may stand in for R4-B's basket before 2001.
2. Cards 1-4: FRED monthly averages used at lag 0 (FEDFUNDS, GS1, GS2, GS5, GS10, BAA, TB3MS, TWEXMMTH) include
   business days published after the month end (H.15 next day, H.10 weekly), against WORKFLOW s5 "official
   statistics: release date"; register a one-day tolerance or build the averages from daily series up to t.
3. All pods with weekly tranches (cards 1-3, card 4 R5, card 5 R1; also Agent A and B pods): tranches 1-3 of December
   2010 decide in January 2011, inside the seal; end the weekly check's decisions on or before 2010-12-31.
4. Hindsight reading: knobs borrowed from Macro Compass action rules (10-month S&P average; stock-bond correlation
   sign) were adopted after 1975-2026 backtests; register how such "seen in a related rule" knobs count in the tally.
   Compass indicator windows (6, 12 months) are recorded as such in the specs.
5. Register C13 asks 3.2 to set one duplicate threshold; I did not: one number would override fixed gates in four
   notes (80%, two thirds, 0.80/0.50, 0.80, 75%). 3.4 decides whether one registered number replaces them before any run.
6. Card 3 C3-D1 "Core book" (proposal in the spec); card 4 C4-D1 state months to end 2010-06 (proposal in the spec).
7. Budget: five card rule layers against WORKFLOW's "at most 4" per B batch; shadow shares, book caps and netting
   across cards (register B19, E, F8).
8. Euro and mark: fx_eur exists only from 1999 and no mark series is in the panel; card 1 R5 and card 3 R1 lose that
   leg for 1975-98 unless a registered panel change adds DEM (FRED EXGEUS is on the research list).
9. Register C7 (nets across cards leave no standing position) and C2 (card 3 R1 a duplicate of Economic trend's
   monetary theme) need design positions; not checkable here; measure with C3-D1's added line and a netting report.
10. Card 4: placebo for date rules (spec proposal) and the tranche exception against rule 2.
11. Section 11 conditions are mostly qualitative (card 4 "widely known", card 5 "long-horizon money arrives", card 1
    quotes); 3.4 translates each into a series or labels it analyst review text.
12. Versions suggested by the card checks and not added (card 1 no-tail; card 2 6-month window, 5x; card 2 R1 long
    side; card 5 per-class lag): register before any run or record as dropped.
13. LSEG registration: card 3 R1 history before FRED starts and R4; card 5 R1 prices; card 3 Q2 and card 5 scoring.
14. Series starts to record at the lock: GS2 (bd_us_2y has 414 design months, so returns from 1976-07), TWEXMMTH,
    ^GSPC monthly and daily files, IR3TIB01 and LSEG deposit rates, LSEG forward EPS and copper/WTI c1; ALFRED first
    vintages for CPILFESL, M2SL, PCEPILFE, UNRATE.
15. agent_C/NOTES.md (a) 6 and 10 are wrong for the code (no pre-1999 euro series; no World Bank spot in the panel);
    the register's D11 note "card 1 R4-B's commodity leg is this list" should carry the start dates.

## 5. What I could not verify

- First dates of GS2, TWEXMMTH, the Yahoo ^GSPC monthly and daily files, the IR3TIB01 series, ALFRED vintages, LSEG
  deposit rates, LSEG forward EPS and LSEG c1 curves (digest only); whether I/B/E/S forward EPS on Datastream is ever
  revised.
- Whether engine_ref.json market_months are contiguous runs ending 2010-12 (assumed; the starts quoted above are
  2010-12 minus the count) and what A1's Bloomberg swap would add (LOCK_v2 coverage of GSCI excess-return indexes).
- Whether ALLOW_AVG stays off in the engine version B2 runs on (it is off in the code read).
- Pre-1983 listed index options (card 4 reported split): reader's knowledge, not in the pack.
- Whether card 1 R5 or card 3 R1 would trigger on any given past episode, the episode counts of every D1, and the
  overlap shares of every D2: all need design positions, not run here.

