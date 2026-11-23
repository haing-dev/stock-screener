---
tags: [fable, thesis]
code_commit: c32ce07
---
> Fresh Opus check of the registration draft. See [[Registration 3.4]]. Source: [repo file](https://github.com/haing-dev/stock-screener/blob/c32ce077b96bb13f580359e8f3e937f418e1191c/docs/research/registration/CHECK_3.4.md).
# Independent check of the step 3.4 registration draft (2026-11-23)

Checker: Opus 5.5 (quant and risk officer), fresh agent; did not write the draft. Read: REGISTRATION_3.4.md, SUMMARY_FOR_USER.md,
BRIEF_OPUS.md; WORKFLOW.md (whole); TESTING_PROTOCOL.md (whole); THESIS_REGISTER_1.5.md (rows T01-T36, sections A-I);
spec section 0 of the six systematic specs, SPEC_Curve_carry s3, section 11 of five specs, SPEC_Value s3/s8 lines,
SPEC_Carry s9, SPEC_Card1/2 episode text; NOTES_3.1_agent_A/B/C (b); CHECK_3.2_A/B/C s4; POWER_3.3.md (whole);
THESIS_1.3_method s11-13; gm/CHANGES.md (gm-1.2.1, gm-1.2.2, gm-2.0, protocol, audit entries); gm/trials.csv;
gm/config.py (BASE, CANDIDATE, STRESS_WINDOWS); gm/book.py (run, _fw); gm/signals.py (equity_dy, carry_values);
gm/bloomberg.py EQ_INDEX; gm/timing.py header. Nothing run; no market data; no 2011+ result.

## 1. Verdict

APPROVED WITH CORRECTIONS (32 Find/Replace corrections: 25 in REGISTRATION_3.4.md, 7 in SUMMARY_FOR_USER.md; none rejects a reading).
Three readings: rule 5 sound with corrections (4); "no new pod Core" and Holm over Core-eligible pods sound with corrections (2); existing pods to Core without a decisive alpha sound with corrections (6, incl. a precision fix to "equal risk").
Numbers: 41 checked against sources, 40 match, 1 mis-scoped (batch false adoption does not cover Strip reversion alone); 1 drafter-computed set (live power) confirmed.
Precision / look-ahead: 5 corrections (rule-layer window, FRED one-day tolerance stated as fact, E2 rule clause, C3-D1 reason, INCUB note); no window, holding or diagnostic reads past 2010-12.
Engine list (c): 2 corrections (card rule-layer builds missing; E5 cannot cover paths built later); shop/holdout rules: 4 corrections (live checkpoint vs 120-month minimum, mark-down could raise the expected Sharpe, pod-verdict bar without reason, A1 untested against WORKFLOW s6); summary: 7.

## 2. Findings

### 2.1 Reading 1, rule 5 (7.2): SOUND WITH CORRECTIONS

- Argued, not asserted. The draft reads "thesis documented before 2011" as "rule family stated by a confirmed pre-2011
  source", from the purpose WORKFLOW rule 5 states ("205 of the 227 sources were recorded in 2024-26, and the models
  know market history to mid-2026"): hindsight in the choice of a rule is what would contaminate 2011-2026. This is a
  coherent reading of rule 5, s5 ("thesis documented before 2011") and s8 item 3, and the register leaves exactly this
  reading to 3.4 (register header: class B "stays hindsight-flagged unless step 3.4 reads rule 5 otherwise"; H1).
  The power-context bullet (7.2 item 5, last) is a consequence, not a reason; the purpose argument carries the choice.
- Mixed-leg pods: dating per pod x leg x version follows the register's unit (T03-T05 separate rows) and the specs
  (SPEC_Carry s0 "Whether a pod with mixed legs can be Core: 3.4"). But the draft claims "the pod stays the unit of
  testing (rule 1)" while 7.6 step 6 tests and holds each Core part on its own. That is a departure from WORKFLOW rule 1
  ("the unit of work, testing and risk") and must be registered as one (correction R4).
- Applied leg by leg:
  - Trend: register T01 and SPEC_Trend s0 say Fung and Hsieh's "rule form is a lookback straddle, not this return-sign
    rule". The draft's "yes" ignores that caveat although it says "nothing new is dated here". Defensible under the
    draft's own clause (lookbacks are parameters; the family is trend following on futures of every class), but the row
    must say so (R1).
  - Currency carry v2 (rank): class A, consistent. v1 (sign): Fama 1984 pattern, not qualified: consistent with the
    pattern/rule line.
  - Energy carry v1 and v2: qualified on Erb and Harvey 2006 "rule form" (register T04). Whether the source states the
    directional sign version, not only a cross-commodity comparison, is not recorded in the register; cannot verify
    without the paper (section 5). The draft treats currency v1 and energy v1 differently only through the pattern/rule
    line, which is consistent if Erb and Harvey report a rule on each commodity's own slope.
  - Equity value: the draft's definition requires the source to state "what is measured"; the register records the
    source's measure as book to market and ours as dividend yield, and names no analogue (T06; SPEC_Value s0; register H1
    calls it "a pattern documented for another measure"). As written, the row contradicts the definition. Either the
    definition carries a measure-family clause or equity value is not qualified. Corrections R2, R3 make the clause
    explicit and the dependence visible; the dividend-yield measure was chosen on design data after the 5-year reversal
    failed (gm-1.1.0), a design-era choice, not a 2011+ one.
  - Strip reversion: qualified through "an analogue the source itself names" ([[QP06 - Profiting from Mean-Reverting Yield Curve Trading Strategies (Chua, Koh, Ramaswamy)#^QP06-C22-2|QP06-C22-2]]): consistent with the clause.
  - Economic trend, bond carry, bond and currency value, Curve carry: not qualified, consistent with register class C.
  - Card rules: never qualified by WORKFLOW s6, whatever their class: correct.
- Stricter reading (mechanism and rule, register class A): Core-eligible = currency carry v2 only; Trend, energy carry,
  equity value and Strip reversion would be Incubator at best; the Core book would be one leg and the holdout would
  judge one leg. Under an exact-measure (not family) reading, Value has no Core part and the Core book = Trend + Carry
  (currency v2 + energy). The draft states the first, not the second (R3 states it).

### 2.2 Reading 2, no new pod Core today; Holm over Core-eligible pods only: SOUND WITH CORRECTIONS

- Follows from WORKFLOW s5 (Core needs rule 5, a live source and the rebuild) and rule 7: Curve carry is class C;
  Strip reversion is qualified but has no registered live source (register D3). Eligibility frozen at batch start (7.7
  verdicts) prevents re-opening by a later live source: not gamed.
- WORKFLOW s6 promises "wrongly adopt a useless pod with at most 2.5%"; adoption means Core. Counting only pods that can
  be adopted is the right Holm family, and leaving rule layers out matches power s3.3 (0.34 / 0.49 vs 0.19 / 0.32 power,
  false adoption unchanged at about 0.03). With no eligible pod the promise holds trivially; Incubator passes are
  outside any error promise (WORKFLOW s5), and the draft states their rate (0.04-0.06 per null layer).
- Mis-scoped number: the stated batch figure 3.0-3.3% (power s3.3, Holm over 2 or 7 pods) does not apply to the
  realistic case in which Strip reversion is the only Core-eligible pod (after LSEG registration): its single-pod size
  at the null boundary is 0.040 (power s3.1 WF_025) / 0.038 (s3.10). R7, R8 state it.

### 2.3 Reading 3, existing pods to Core by placebo, double costs, tail, rebuild: SOUND WITH CORRECTIONS

- The reason (the parts were adopted after seeing the same design months, so a p-value is not evidence) is sound, and
  no Core book exists to test against before step 6. But it departs from WORKFLOW s5 "Decisive, all four", and the
  draft never says so in the conflict table, in step 6 or in the summary. Plain consequence, from power s3.2: S1-S3 pass
  a working timing part almost always (placebo 0.86-1.00, tail 0.73-0.84), so the existing book has no decisive "adds
  to the book" test on history and the holdout is its only independent test (R5, R6; summary S2).
- Precision: "Core parts at equal family shares" (7.6 step 6, E9) is not "equal risk" (7.1 F8, WORKFLOW 5.1) in this
  engine: book.py scales each family-and-class block to unit volatility and multiplies by the family weight (run(),
  line 193), so a 4-block part (Trend) carries up to about twice the risk of a 1-block part (Value equities) at equal
  weights. R9-R11 define equal risk exactly.
- Asymmetry, not a correction: non-Core parts of existing pods face the Incubator rule's alpha point estimate on the
  same seen months that the draft says cannot be read as evidence for Core parts (section 4).

### 2.4 Numbers checked (all others match their source)

Power s3.1/s3.2/s3.3/s3.6/s3.8/s3.10 figures in 7.1 F1-F4, 7.6 step 9, 7.7 table, 7.9 item 7 (0.037/0.176/0.560;
0.021/0.167/0.544; 0.040/0.138/0.383; 0.041/0.143/0.380/0.470; 0.057/0.227/0.569; 0.18 under 48 months; 0.030-0.033;
0.04-0.06; 0.41 and bound 0.37; 0.05/0.31/0.58/0.76; 1.00/0.92; 0.56 to 0.23; 8-12 points; 0.34/0.49 to 0.19/0.32;
break-even 0.24); register counts (17 rules, 76 / 128 versions, card grids 28/8/16/16/8 and 56/8/32/16/16; systematic
26); gm/trials.csv 39 "book" + 4 "fix" rows (43 data rows); BASE econ 30% / CANDIDATE 15% (config.py); CRSP bond
correlation floor 0.965 (CHANGES gm-2.0); timing loss (0.95 to 0.85 at one day, CHANGES gm-2.0); strip cost
8 x 0.25/1.9 = 1.05 bp and rolls 4 x 1/8 = 0.5 (SPEC_Carry s9); 189 holdout months to 2026-09; LOCK_v2 id;
spec s11 thresholds (Curve carry, Strip reversion, cards 1-3). Live power in 7.10 item 4 (0.14 / 0.24 / 0.10 / 0.5) is
the drafter's arithmetic, confirmed (normal approximation), but see 2.6.

### 2.5 Precision and look-ahead

- Seal and holding cut (7.3 item 5), D3 to 2009-12, C4-D1 to 2010-06, C5-D2 to 2008-12, R1 to 2010-11, December-2010
  tranches, k = 1 holding of 2010-11 ending 2010-12-31: all inside 2010. k = 1 return form (7.3 item 2) is correct.
- 7.3 item 4 states as fact that FRED monthly averages are "known on the trade day"; the last business day's daily
  value is published on the next business day, possibly after the trade-day close (CHECK_3.2_C s4 item 2 asked for a
  registered tolerance). R12.
- Rule-layer window: 7.7 defines the window by the block and book scalers' warm-up, which rule layers do not have
  ("no rescaling"); whether off months enter at 0 is a builder choice. R14.
- C3-D1's stated reason ("no Core book exists before B2") is false under the draft's own order (it runs after Core book
  v1); the paragraph under the table gives the right reason. R15.
- E2's clause "a mapping returns only for a ticker of the same index listed in LOCK_v2" would also remove the kept
  country mappings (Nikkei to MSCI Japan etc. are not the same index; bloomberg.py EQ_INDEX). R16.
- 7.7 note: the halving of Incubator rates under the alpha reading is reasoned, not simulated (power s4 item 9). R23.

### 2.6 Engine list, shop rules, holdout, live

- (c) has no build entry for the card rule-layer engine (rule states, tails, entry versions, netting across cards,
  shadow book) or the F0 / card diagnostics, while it has one for Curve carry and Strip reversion (R24). E5 (seal in
  every path) sits in the fix version although the k = 1, tranche and daily paths only exist in the feature version
  (R25). Bundling numbered items inside one version entry follows the gm-1.2.1 and gm-1.2.2 precedent.
- A1 is "report, no adoption test" (WORKFLOW 4.1) although WORKFLOW s6 lists the data swap under "Test = does not
  hurt"; the draft does not name the conflict or the reason (R13).
- Holdout consequences restate WORKFLOW s6 verbatim. But the defined mark-down ("Fail: the holdout net Sharpe, floored
  at 0") raises the expected Sharpe when a book fails on the fall, correlation or 2022 criterion with a holdout Sharpe
  above design minus inflation (R21). The pod-verdict bar "above 0" has no stated reason (brief rule; R22).
- Live promotion at 60 live months applies T1-T4 to a window that 7.7 calls "insufficient data, not tested" (fewer than
  120 months, section 1 rule kept). R17-R20 move the first checkpoint to 120 months.
- No decision is handed to the user (the LSEG licence statement and the PC block are named as blockers with their
  unblock conditions); versions averaged, never picked (C2-D2 and C3-D2 prune by pre-registered counts, not returns);
  nothing claimed as run; no 2011+ number.

### 2.7 Summary for the user

Accurate in substance; seven fixes: A1 is not tested; existing parts skip the decisive alpha test; version count
omits the 128 with entry and sizing; null pass rate 3-4% (spread pods 4%); mark-down wording; live checkpoints.

## 3. Required corrections

### REGISTRATION_3.4.md

1. Trend row: state the register's rule-form caveat and how the reading absorbs it.
- Find: `| yes (strategy family on futures; mechanism not) |`
- Replace: `| yes (trend following on futures of every class, position with the past move; the source models it as a lookback straddle, not our return-sign rule (register T01, SPEC_Trend s0), which item 2 treats as a parameter of the family; mechanism not) |`
Reason: THESIS_REGISTER_1.5 T01 and SPEC_Trend s0 record that the rule form differs; the row must not silently drop it.

2. Definition: make the measure-family clause explicit, since equity value depends on it.
- Find: `parameters (lookbacks, thresholds) need not match.`
- Replace: `parameters (lookbacks, thresholds, and the particular ratio inside a measure family the source uses, such as one valuation ratio for another) need not match; a row that relies on this clause says so.`
Reason: THESIS_REGISTER_1.5 T06 and H1: the source measures book to market, the pod dividend yield; without the clause the draft's own "what is measured" test fails.

3. Equity value row: show the dependence and the stricter outcome.
- Find: `| yes (valuation-ratio rank of country indexes; our ratio is dividend yield) |`
- Replace: `| yes, under item 2's measure-family clause (rank of country indexes on a valuation ratio; the source's ratio is book to market, ours dividend yield, chosen on design data after the 5-year reversal failed, gm-1.1.0); without the clause: not qualified, and Value would have no Core part |`
Reason: SPEC_Value s0, register T06; gm/CHANGES.md gm-1.1.0 and trial log item 4.

4. Pod unit: register the split as a departure from rule 1 instead of denying it.
- Find: `   - The pod stays the unit of testing (rule 1): Batch A tests whole pods; the split only decides which positions the`
- Replace: `   - Departure from WORKFLOW rule 1 ("the unit of work, testing and risk"), registered here: Batch A tests whole pods, but from Core book v1 on each Core part is tested (7.6 step 6) and held at its own equal-risk share, because rule 5 dates legs, not pods (item 1); the split decides which positions the`
Reason: WORKFLOW s2 rule 1; the draft's own 7.6 step 6 (S1-S4 per part) and E9.

5. Step 6: name the departure from WORKFLOW s5.
- Find: `   Reported, not decisive: leave-one-out alpha of the part on the other Core parts with its bootstrap p. Reason: these`
- Replace: `   Departure from WORKFLOW s5 ("Decisive, all four"): test 1 is not decisive for these parts. Reported, not decisive: leave-one-out alpha of the part on the other Core parts with its bootstrap p. Reason: these`
Reason: WORKFLOW s5 lists "Adds to the book" among the four decisive tests; the departure must be stated where it applies.

6. Step 6: state the consequence plainly.
- Find: `a broken part or a standing exposure (costs, placebo, tail) stay decisive.`
- Replace: `a broken part or a standing exposure (costs, placebo, tail) stay decisive. Consequence: no Core part of the existing book has a decisive "adds to the book" test on history; S1-S3 pass a working timing part almost always (power s3.2: placebo 0.86-1.00, tail 0.73-0.84), so the holdout is the existing book's only independent test.`
Reason: POWER_3.3 s3.2 (T3 0.859-0.998, T4 0.733-0.836); BRIEF_CHECK reading 3.

7. E9: define equal risk exactly (family weights alone are not equal risk in this engine).
- Find: `Core book family shares equal`
- Replace: `Core book at equal risk: each Core part's summed scaled-block return is rescaled to unit volatility (trailing 36-month realised volatility, lagged one month, as the block scaler) and weighted 1/n before the book scaler (book.py family weights alone give a 4-block part up to about twice the risk of a 1-block part)`
Reason: gm/book.py run(): each family-and-class block is scaled to unit volatility and multiplied by the family weight; WORKFLOW 5.1 "Core pods at equal risk"; 7.1 F8.

8. Step 6: use the defined equal risk.
- Find: `   family shares, 10% target, the engine's caps. Every other part`
- Replace: `   risk as defined in 7.4 E9, 10% target, the engine's caps. Every other part`
Reason: as item 7; the sentence begins "Core book v1 = the Core parts at equal".

9. Part (c): same wording.
- Find: `equal-share Core book`
- Replace: `equal-risk Core book (7.4 E9)`
Reason: as item 7.

10. F1: state the measured size for the case that can actually arise in B2.
- Find: `up to about 5% for one pod at correlation 0.6 |`
- Replace: `up to about 5% for one pod at correlation 0.6; about 4% when Strip reversion is the only Core-eligible pod (250 months, rho 0.3: power s3.1 0.040, s3.10 0.038) |`
Reason: POWER_3.3 s3.1 (Strip 250, alpha = 0: 0.040) and s3.10 (0.038); the 3.0-3.3% figure is for Holm over 2 or 7 pods (s3.3).

11. 7.7 table: same scope.
- Find: `| Batch false adoption (B2 at the null) | - | 0.030-0.033 | - | - | nominal 0.025 |`
- Replace: `| Batch false adoption (B2 at the null, Holm over 2 or 7) | - | 0.030-0.033 | - | - | nominal 0.025; Strip reversion alone (m = 1): 0.040 |`
Reason: POWER_3.3 s3.1, s3.3.

12. 7.3 item 4: register the one-day tolerance instead of asserting the data are known.
- Find: `business day, so they are known on the trade day.`
- Replace: `business day, possibly after the trade-day close: registered as a known one-day tolerance (CHECK_3.2_C s4 item 2), reported, no engine change.`
Reason: CHECK_3.2_C s4 item 2 ("register a one-day tolerance or build the averages from daily series"); WORKFLOW s5 "official statistics: release date"; publication time not verified in any source.

13. A1: name the conflict with WORKFLOW s6 and the reason.
- Find: `Step 2. Batch A1, data swap (report, no adoption test; WORKFLOW 4.1 "differences explained"). CANDIDATE on the A1 data`
- Replace: `Step 2. Batch A1, data swap (report, no adoption test; WORKFLOW 4.1 "differences explained" governs over s6 "Test = does not hurt", because a data swap kept or dropped by its effect on returns would pick data by results). CANDIDATE on the A1 data`
Reason: WORKFLOW s6 lists the data swap under "Test = does not hurt"; 4.1 says "differences explained"; the draft settles silently.

14. Window for rule layers (no scalers, so the warm-up rule does not define it).
- Find: `SPEC_Strip_reversion s7). The expected window`
- Replace: `SPEC_Strip_reversion s7). A rule layer's window is every month from the first month all its inputs exist (its spec s7) to 2010-12, off months entering with return 0. The expected window`
Reason: 7.7 held size ("no rescaling" for rule layers); POWER_3.3 s2 simulated rule layers over all months with flat off months.

15. C3-D1: correct the stated reason.
- Find: `since no Core book exists before B2`
- Replace: `because the question is content, not trading status (Core book v1 exists by then but holds Core parts only)`
Reason: the draft's own order (7.5 order item 3: C3-D1 runs after Core book v1) and the paragraph under the 7.5 table.

16. E2: remove the clause that would also delete the kept mappings.
- Find: `a mapping returns only for a ticker of the same index listed in LOCK_v2`
- Replace: `every remaining mapping (a local index to the MSCI index of the same country) is used only if the A1 rule of 7.6 step 2 admits the series`
Reason: gm/bloomberg.py EQ_INDEX maps every local index to an MSCI country index, none "the same index"; the clause as written leaves the builder a choice.

17. Live checkpoints: first checkpoint at the window minimum of 7.7.
- Find: `   60 and 120 live months after a pod's first ledger week, then every 60 months. Promotion to the traded book needs: at`
- Replace: `   120 and 180 live months after a pod's first ledger week, then every 60 months. Promotion to the traded book needs: at`
Reason: 7.7 window: "Fewer than 120 such months = insufficient data, not tested (section 1 rule kept)"; T1-T4 on 60 months contradicts it.

18. Live minimum sample.
- Find: `   least 60 live months (rule layers also 48 live held months and 3 live episodes); a registered live source for every`
- Replace: `   least 120 live months (7.7 window minimum; rule layers also 48 live held months and 3 live episodes); a registered live source for every`
Reason: as item 17.

19. Live power, first line.
- Find: `   estimate is at or below 0. Power stated with it: at true IR 0.4 the alpha test passes about 0.14 at 60 months and`
- Replace: `   estimate is at or below 0. Power stated with it: at true IR 0.4 the alpha test passes about 0.24 at 120 months and`
Reason: normal approximation as in the draft: 1 - N(1.96 - 0.4 x root(10)) = 0.24.

20. Live power, second line.
- Find: `   0.24 at 120 months (normal approximation, t = 0.4 x root(years)); at true IR 0.4 the 120-month shelving rule removes`
- Replace: `   about 0.34 at 180 months (normal approximation, t = 0.4 x root(years)); at true IR 0.4 the 120-month shelving rule removes`
Reason: 1 - N(1.96 - 0.4 x root(15)) = 0.34.

21. Mark-down must never raise the expected Sharpe.
- Find: `   the selection inflation of 7.8 item 2. Fail: the holdout net Sharpe, floored at 0. A pod that fails its pod verdict`
- Replace: `   the selection inflation of 7.8 item 2. Fail: the lower of that figure and the holdout net Sharpe, floored at 0 (a mark-down never raises it). A pod that fails its pod verdict`
Reason: WORKFLOW s6 "expected Sharpe marked down"; a book can fail on fall, correlation or 2022 with a holdout Sharpe above design minus inflation.

22. Pod verdict: give the reason for the bar.
- Find: `   verdict: pass if the pod's net Sharpe at its held size over the holdout is above 0. Every other registered pod, part`
- Replace: `   verdict: pass if the pod's net Sharpe at its held size over the holdout is above 0 (no source sets a pod bar; the four criteria are registered for the book; above 0 is the weakest reading of pass, since a part's Sharpe over 189 months has a standard error of about 0.25). Every other registered pod, part`
Reason: BRIEF_OPUS rules ("Do not invent thresholds without a reason"); TESTING_PROTOCOL s6 (standard error about 0.27 over 15 years).

23. 7.7 note: the halving was reasoned, not simulated.
- Find: `about half that under the alpha reading registered here).`
- Replace: `about half that under the alpha reading registered here, a halving reasoned from the alpha estimate's symmetry at the null, not simulated: power s4 item 9).`
Reason: POWER_3.3 s4 item 9.

24. Part (c): add the build entries for the card rule layers and the diagnostics.
- Find: `   Curve carry and Strip reversion pod builds as new code under their specs (no rule change, so a build entry only).`
- Replace: `   Curve carry and Strip reversion pod builds, the card rule-layer engine (rule states, tails, entry versions, held size 0.10 / 0.40, netting across cards, shadow book) and the F0 and card diagnostics, as new code under their specs (no rule change, so build entries only).`
Reason: register B14-B19, B2 contents of 7.6 step 9 and 7.5 F0/C1-C5 need code that no entry lists; 7.4 intro "Each item needs its gm/CHANGES.md entry before its code".

25. Part (c): E5 can only cover paths that exist when it is coded.
- Find: `truncation test including the k = 1, tranche and daily paths.`
- Replace: `truncation test including the k = 1, tranche and daily paths; E5's seal and holding cut are built into each new path in this entry (entry 1 covers only the monthly k = 0 path that exists then).`
Reason: 7.4 E5 names k = 1, tranche and daily paths, which E6, E8 and E14 create in the feature version.

### SUMMARY_FOR_USER.md

1. A1 is not tested.
- Find: `start (needs the PC to run pandas again)`
- Replace: `start (reported, not tested; needs the PC to run pandas again)`
Reason: REGISTRATION_3.4 7.6 step 2 ("report, no adoption test").

2. Existing parts skip the decisive alpha test.
- Find: `3. Core book v1 is formed from the parts of the existing pods allowed into Core (below).`
- Replace: `3. Core book v1 is formed from the parts of the existing pods allowed into Core (below). They must pass placebo, double costs, tail and an independent rebuild; "adds to the book" is only reported for them (they were designed on the same years), so the holdout is the existing book's only independent test.`
Reason: REGISTRATION_3.4 7.6 step 6 (with corrections 5-6).

3. Version count.
- Find: `   to 76 versions in 17 rules).`
- Replace: `   to 76 versions in 17 rules, 128 with entry and sizing versions, more if card 2 or card 4 diagnostics add versions).`
Reason: REGISTRATION_3.4 7.6 step 9; register G.

4. Null pass rate.
- Find: `and about 3% if it adds nothing.`
- Replace: `and about 3-4% if it adds nothing (4% for the spread pods).`
Reason: POWER_3.3 s3.1 (0.037 full, 0.040 Strip, 0.041 Curve carry).

5. Mark-down wording.
- Find: `  Sharpe cut to the holdout Sharpe (not below 0), and no real-money step before the live checkpoints. Nothing is`
- Replace: `  Sharpe cut to the holdout Sharpe if that is lower (not below 0), and no real-money step before the live checkpoints. Nothing is`
Reason: REGISTRATION_3.4 7.9 item 5 (correction 21).

6. Live checkpoints, line 1.
- Find: `- After the holdout any pod is promoted only on its live record, at checkpoints after 60 and 120 live months (a good`
- Replace: `- After the holdout any pod is promoted only on its live record, at checkpoints after 120 and 180 live months (a good`
Reason: REGISTRATION_3.4 7.10 item 4 (corrections 17-20).

7. Live checkpoints, line 2.
- Find: `  pod passes only about 1 in 7 at 60 months and 1 in 4 at 120). Analysts are scored at every 200 resolved forecasts;`
- Replace: `  pod passes only about 1 in 4 at 120 months and 1 in 3 at 180). Analysts are scored at every 200 resolved forecasts;`
Reason: as item 6.

## 4. Open points that are not corrections

- Energy carry version 1 (directional sign) is qualified on Erb and Harvey 2006 "rule form"; whether the paper states the per-commodity sign rule (not only a cross-commodity comparison) should be recorded at the next bibliographic look-up (register H2 kind).
- Non-Core parts of existing pods face the Incubator alpha point estimate on the same seen months that 7.6 step 6 says cannot be evidence for Core parts; registered asymmetry, unargued.
- WORKFLOW 4.2 names weekly tranches as part of A2; the draft tests tranches only in the reported weekly check (consistent with WORKFLOW s5 monthly design tests), so tranches enter live without a decisive test.
- E4 lags non-US dividend yields 12 months "design and live alike"; if the annual Ken French file is staler than t-12 in some months (ffill limit 12 can lapse, CHECK_3.2_A s4 item 5), live goes missing; a data-health flag should cover it.
- A1's "same instrument (same index family or contract root)" needs a per-series list in the A1 data entry ((c) item 3) so the builder does not judge family membership.
- Core book v1 at equal risk gives Value's equity leg (8 markets) the same risk as all of Trend; its design Sharpe is first seen at step 6 and never compared before the holdout (follows from WORKFLOW 5.1; worth a reported line).
- Code fact not recorded in 7.4: signals.py value_values computes a commodity value signal that book.py drops (register D7; SPEC_Value s13).
- F0 counts held months including tails, C1-D1 counts condition months excluding tails; both kept, the difference should be printed with the gate.

## 5. What I could not verify

- Contents of Fung and Hsieh 2001, Erb and Harvey 2006, Asness, Liew and Stevens 1997 beyond the register's text (no web): in particular whether Asness, Liew and Stevens rank countries on dividend yield and whether Erb and Harvey state a directional rule.
- Publication times of H.15 / H.10 data relative to the NYSE close (correction 12 registers a tolerance instead).
- Release lags of quarterly CPI for AU and NZ in the design years (E3's "end of the month after the quarter").
- Ken French international file update dates (E4's bound).
- That Carry's two versions reproduce today's half-and-half exactly (7.6 step 3; SPEC_Carry not read in full).
- Per-spec section 7 start dates and section 10 loss-event months behind the "loss not seen" flags.

