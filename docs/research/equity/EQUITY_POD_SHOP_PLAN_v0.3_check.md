# Independent check of EQUITY_POD_SHOP_PLAN_v0.3.md (2026-11-15)

Checker: a separate Opus agent that did not write the plan. Scope: the plan, and v0.2 only where the plan relies on
it or amends it. v0.2 as a whole was not reviewed (see section 4).

## 1. Verdict

**PASS WITH CORRECTIONS.** 5 MUST FIX, 17 SHOULD FIX, 14 NOTE.

The pipeline, the fences and most numbers hold. But five points would let outcome information reach the tests or
break a rule the plan says it keeps. The largest: the investor ranking uses returns from before 2011, which is the
design era where the decisive tests run.

## 2. Findings

### MUST FIX

**M1. The ranking reads design-era returns, so the decisive tests inherit the selection.** Sections 5.2, 5.3, 5.4, 8.2.
- What is wrong: 5.3 ranks tier A on "style-adjusted result over the full history, with at least eight years" and on
  the "share of five-year blocks with a positive style-adjusted result". 5.2 also computes 2006-10. 13F history on
  WRDS starts in 1980, so these windows cover 1980-2010, the design era. Tier A investors are then partly picked
  because their holdings beat their peers in the same years where the pods are tested. Their purchases feed the
  pods through revealed thresholds and the say-do gate (the long list must hold their purchases at three times the
  universe rate). So part of the outperformance that got them picked comes back as pod return.
- Size: suppose those purchases make up 5-10% of the pod's long side, and they beat their peers by 5% a year (the
  reason the investors were picked). The pod then gains about 0.25-0.5% a year it did not earn. That is a quarter to
  half of the 1-2% a year the power check is built around (v0.2 8.5).
- It also breaks the plan's own logic. The 5.4 fence says the years that selected a family's investors "are never
  proof for that family". With full-history windows, that would rule out the design era too, and the design era is
  where all the decisive tests run. Line 245 says "Tier A is picked on returns after 2010", and that is not what 5.3
  does.
- Evidence: plan lines 134, 144-146, 158-159, 245; v0.2 4.2, 8.3, 10.
- Smallest fix: build the ranking only from 2011 onward (2011-15, 2016-20, 2021-25, and 2011-25 as the long
  window), and do not compute pre-2011 manager returns before the freeze. The user's request (the last five years)
  is still covered. Pairs C1, C2.

**M2. The non-US holdout "counts toward the verdict of every family". That breaks a kept rule, and its premise is false.** Sections 8.2 and 11 (row 4.2).
- Conflict with rules the plan keeps:
  - v0.2 4.4 still requires "thesis documented before 2011" for Core. Section 11 does not amend it. So a reader cannot
    tell whether a family documented in 2022-26 can ever be Core. That covers 647 of the 695 General documents.
  - The macro independent review set the rule that hindsight-flagged pods can never be Core
    (`docs/research/WORKFLOW.md` lines 30-32, 128, 151-155).
  - v0.2 rule 10 (kept: plan line 6) says a sample counts only if it "could not have shaped the pod's sources".
- The premise "US-based investors were not chosen on these markets" is false for many of the most frequent investors
  in the library. Rochon (Montreal), Brenton (Turtle Creek, Toronto), Terry Smith, Nick Sleep, Li Lu, Guy Spier,
  Pabrai, Hohn (TCI, mostly European holdings), Baid (India) and Russo all built their records partly or mainly
  outside the US. So did the NBIM channel, which has 86 documents. Grade F fund returns include non-US holdings too.
- Requiring both non-US samples to pass does not deal with styles moving together across regions. The quality and
  growth tilt that did well in the US from 2011 also did well outside the US. And the thesis-formation problem
  (people describe what worked for them after 2010) applies in every region.
- What would make the region split defensible:
  1. the family's source investors' records, holdings and examples are mainly US;
  2. a registered diagnostic shows that, in 1990-2010, the pod's added return in the US and outside the US were not
     closely linked;
  3. "pass" on each non-US sample is defined at E3.5;
  4. Core earned this way is marked provisional until a live checkpoint.
- This is a design decision. The options:
  - (a) keep v0.2 4.4: a family documented after 2010 cannot be Core, and the non-US holdout is evidence for an
    Incubator pod's later promotion only.
  - (b) amend 4.4 explicitly, under conditions 1-4 above.
- Pairs C3 and C4 implement (b). For (a), replace the 8.2 row text with "Sealed; one run. Reported for every family;
  a verdict only under the same conditions as the US holdout."

**M3. 13F cannot show "the day they bought it", and quarter-end ranks include price moves after the purchase.** Section 6 (also 1, 11 row 8.3).
- 13F shows a position at quarter-end, not the purchase date. Ranks "at that quarter-end" on past return and
  distance from the 12-month high include up to three months of price moves after the real purchase. That breaks
  the fence "No return after the purchase date appears in any output".
- It also pushes the revealed distribution toward stocks that rose after purchase, and thresholds come from that
  distribution.
- Fix: rank at the end of the previous quarter, the last date surely before the purchase. Pairs C5-C8.

**M4. The two descriptive jobs open the US seal before the freeze, but no rule is amended to allow it.** The US holdout verdict rule also ignores holdings read after 2010. Sections 5.4, 6, 8.2, 11.
- v0.2 gate G8 is kept (plan line 98: "Gates G1-G9 of v0.2"). G8 puts 2011+ behind a one-time key. The scorecard
  reads US returns for 2011-25 and the holdings module reads 2011+ holdings and price ranks, both before the freeze.
  Section 11 does not amend G8. It also says nothing on whether non-US 2011+ stays sealed. That matters because the
  non-US holdout now carries the verdicts.
- 8.2 gives a US holdout verdict to "a family whose thesis is documented before 2011 and whose investors were not
  picked on those years". Such a family can still take its revealed thresholds and its say-do loop (a say-do miss
  goes back to E3.1, v0.2 E3.3) from 2011+ holdings. That is design input from the holdout years.
- Section 11 row 4.2 states the condition differently ("career overlap or picked through the scorecard"). It leaves
  out "thesis documented before 2011", so the two texts disagree.
- Fix: one condition list in 8.2, used in section 11 too, and an explicit G8 amendment. Pairs C9-C11.

**M5. The scorecard computes the "follow the best managers" pod's US holdout before the pod exists, and the pod can never pass the non-US rule.** Section 6, last paragraph; section 11 row 8.5.
- The scorecard computes 2011-25 results of 13F copies for every filer: all holdings, the ten largest, new positions
  only. That is close to this pod's US holdout. Anyone who writes its spec afterwards (lookback, number of managers,
  new positions or all) has already seen the answer.
- 13F has no non-US version, so under 8.2 ("must pass both non-US samples") the pod can never pass.
- Fix: register its spec before E0.4 runs (it needs no transcripts). Report its US 2011+ result only. Judge it on the
  design era and the live record. Pair C12.

### SHOULD FIX

**S1. The ranking mixes two kinds of record and leaves profitability in.** Sections 5.2, 5.3.
- 13F copy returns (before fees, no shorts, no trading within the quarter) and grade F fund returns (after fees) go
  into one rank.
- "Style taken out" means size, value and momentum only. The profitability factor is not taken out. Yet section 1
  says profitability was "all of" the triage result (RESULTS.md: RMW loading +0.6 to +1.1), and it did well in
  2011-25. So the ranking is still partly a style ranking, which the plan says it avoids.
- Fix: rank within each record type, and add profitability to the peer group. Pairs C1, C13.

**S2. Markel is the wrong example for grade F.** Section 5.1.
- A listed insurer's share price mostly reflects the insurance business, not Gayner's stock picking. Greenlight Re
  is the same case. Markel's equity book is visible on its 13F.
- Fix: pairs C14, C15, C16.

**S3. The control comparison cannot deliver what 5.4 promises.** Sections 5.3, 5.4, 11 row 8.5.
- Families are clustered from all cards together, so a family can mix tier A and control investors, and
  "control-sourced" is not defined.
- Ten control investors, with three needed per family (or two plus a published source), may give zero to two pods.
- Control pods are "Incubator only" in B2. The plan does not say whether they get the sealed runs that the 5.4
  comparison ("on untouched data") needs, or whether they use B2 slots.
- With so few pods the comparison has almost no power.
- Fix: define "control-sourced". Give control pods the sealed runs, reported only. Call the comparison descriptive.
  Whether control pods use one of the four B2 slots is a design decision: using a slot costs a tier A pod, and not
  using one adds untracked trials. Pair C17 covers the wording.

**S4. "No agent sees a return" is stated too firmly.** Section 8.3 fence 2; 5.3 control blinding.
- The models know from training how famous investors and their stocks did (v0.2 4.2 says so). With investor names
  on the cards, the strategist can tell stars from control investors, so the blinding is weak.
- Fix: packs for the strategist and spec writers name investors by id. Pair C18.

**S5. Thresholds and the say-do check grade each other.** Section 6.
- A threshold set at "the lower quartile of the family's purchases" places 75% of those purchases above it by
  construction. The say-do gate then checks the long list against the same purchases.
- Fix: set the threshold on one half of the purchases and run the say-do check on the other half. Pair C19.

**S6. Technique tests can grow Batch A without a limit.** Section 7.
- "A version of the construction rule, a hygiene test in Batch A" conflicts with "never adds a test slot". Batch A
  tests are trials too, and the v0.2 section 10 list is fixed. This is the "untracked stream of trials" the plan
  warns about in section 3.
- Fix: pair C20.

**S7. "Company data with dated history" overstates the LSEG probe.** Section 9.
- `lseg_probe_v1.txt` line 43 shows one company's price only (Apple month-end close from 1990, `RDP.Data`). `TR` was
  tried only on the S&P 500 (line 50). No company accounts, estimates or holders were tested.
- Fix: pairs C21, C22.

**S8. The LSEG field claims go beyond the cited thread, and the estimates page is not used.** Section 9.
- The cited thread (community.developers.lseg.com/discussion/132467) shows that `TR.F.SourceDate`, `.FundUpdType` and
  `.periodenddate` exist. But the original-or-restated flag came back empty ("NaT") on weekdays, and the thread does
  not show that first-reported values can be pulled.
- The cited estimates page lists past consensus snapshots only for the last 12 months in that interface. It also
  says I/B/E/S starts in 1976 for the US and 1987 for other countries.
- Fix: pairs C23, C24.

**S9. The Bloomberg fact is out of date.** Section 2.
- "The download allowance ran out on 13 Nov." CLAUDE.md says the block cleared the same day: R8-R11 were pulled on
  13 Nov, R12 on 14 Nov, and lock v2 was built from them.
- Fix: pair C25.

**S10. The triage result is overstated.** Section 1, item 2.
- "The three triage screens separated winners from losers." RESULTS.md says the red flags and Avoid calls picked
  losers in raw terms. The pre-registered Buy-minus-Avoid test had no alpha (Hidden Earnings -12.1% a year, t -1.42;
  Emerging -0.1%; Core +0.3%), and no test passed.
- Fix: pair C26.

**S11. The non-US samples cannot use the same rules.** Sections 8.1, 8.2, 9.
- Outside the US, WRDS has no 13F ownership and no short interest: Compustat short interest is North America only,
  and Markit is not subscribed. So the shortable set of v0.2 9.1 (an ownership floor and a short-interest cap) cannot
  be built there.
- There is no insider data outside the US either, and delisting returns in Compustat Global are not established.
- Two results. "Same universe, same rules for every pod" fails outside the US. And a pod that needs a US-only input
  can never pass "both non-US samples".
- The power check (v0.2 8.5) is defined for the US design era only.
- Fix: pair C27. The non-US shortable stand-in is a design decision, fixed at E1.4.

**S12. Insider history is too short for a design test.** Section 9.
- The SEC Insider Transactions Data Sets start in 2006 Q1 (sec.gov page, range "January 2006 - September 2026").
  The design era therefore has 60 months of insider data. v0.2 section 10 needs 120 months, or the result is
  "insufficient data". The insider cell shared by the triage screens cannot get a design test.
- Fix: pair C28.

**S13. It is unclear which file wins, and section 14 drops two v0.2 requests.** Header and section 14.
- Line 6 lists only v0.2 sections 3, 9, 10, 11 and 20 as in force. Yet the plan relies on v0.2 4.1, 4.2, 4.4, 6.2,
  6.3, 7.3, 8.1-8.5, 11.2, 13, 14 and 16.
- No sentence says which file wins when the two disagree.
- Section 14 replaces v0.2 section 17 and drops two of its items: "PDFs for the equity paper pack" (E0.3 is still in
  Stage 2) and the items needed before real money.
- Fix: pairs C29, C30.

**S14. Some effort figures are not from the log, and the Fable count leaves units out.** Section 10.
- "The figures for Fable and the engine come from the macro program's log." The log (CLAUDE.md) has Fable units of
  0.63-0.67M (0.91M for the two-run audit) and Opus checks of 0.27-0.36M. Those support the Fable line. For an engine
  it has only block 3: about 0.57M to build and 0.32M to check. So "5-8M" for the engine and the Stage 0 figures are
  estimates.
- The Fable count leaves out the playbook cards (E2.8, a Fable step in the plan's own table) and the monthly reviews
  once live.
- Fix: pairs C31, C32.

**S15. The statement that v0.2's statistics hold has never been checked independently.** Section 1.
- "The statistical design of v0.2 holds" is the author's own view. v0.2 step 0 (an independent review of v0.2) was
  never done: CLAUDE.md says "SELF-REVIEW ONLY". This check covered v0.2 only where v0.3 relies on it.
- Fix: pair C33.

**S16. Not every screen gets a history test, and the user is not told.** Section 8.1 (coverage of the request).
- The user asked to "evaluate independently and unbiasedly each screening ... and backtest them". The budget allows
  at most eight pods a design test (v0.2 8.5). The plan never says plainly that most families get no history test.
- This is a design decision. The options:
  - (a) keep eight slots, and run the rest as live screens (Incubator);
  - (b) add a descriptive design-era pass for every family, labelled with the number of trials and never used for a
    verdict.
- Pair C34 implements the wording for (a).

**S17. The two rule texts for the US holdout disagree.** Sections 8.2 and 11 row 4.2, as shown in M4.
- Listed separately so it is not lost if M4 is settled by design rather than by the pairs.

### NOTE

- N1. Section 3: 3% a year over 5 years with 10-15% deviation gives t = 0.67 to 0.45, not "near 0.5" across the
  whole range (3/10 x sqrt 5 = 0.67).
- N2. Section 1: the best-of-20 example uses 15 years. The plan's design era is 36 years, where the same arithmetic
  gives about 0.31.
- N3. Section 2: 2,254 of 2,257 documents have notes (3 pending, all AI CEO interviews). Notes can contain quotes
  marked unverified. So "each has ... a note with machine-checked quotes" is slightly too strong.
- N4. Section 2: the "investors present" heuristic counts authors, bloggers and analysts.
  - The 40 most frequent names include Lyn Alden (macro analyst), Brian Feroldi (educator), Hari Ramachandra
    (blogger) and Cullen Roche.
  - Some Gautam Baid documents are book reviews, counted because his role contains "Partners".
  - So "40 most frequent cover 146 documents" includes people who never ran money. The plan calls it heuristic, and
    the figure is correct for what the script computes.
- N5. Section 2: "about 440" technique documents comes from a loose keyword match:
  - "hedg" matches "hedge fund";
  - "multiple", "quant" and "leverage" match ordinary usage;
  - "concentrat" alone hits 114.
  A stricter match gives 288 (my recount). Pair C35.
- N6. Section 12: "Families need three money-running investors". v0.2 7.4 allows "two plus a published source", and
  amendment 7.4 keeps that.
- N7. Section 4: E2.3 (process maps) and E2.10 (dated stock views) are missing from the step table and the flowchart.
  "E2.2-E2.11" in section 10 covers them. E0.2 moved from Stage 1 (v0.2 section 14) to Stage 2 without a row in
  section 11.
- N8. Section 6: the say-do check now uses "actual purchases" where v0.2 8.3 uses "reported holdings". That change is
  not listed in section 11.
- N9. Section 8.1 calls v0.2 sections 4, 9 and 10 "unchanged", then 8.2 amends 4.2.
- N10. Section 9: the fact sheet's "108K+" includes private and ex-public companies, and its body says "up to
  108,000". "US from 1983, other countries from the 1990s" matches its stat block (1983 and 1995).
- N11. Section 3 and 6: 13F also hides positions under confidential treatment, which are filed later. The scorecard
  must use the filing date of any amended filing, or it looks ahead. Option rows must be dropped from the copy
  portfolio.
- N12. Section 10: the 200-250 documents for extraction do not follow from the tier sizes. The 40 most frequent
  investors cover only 146 documents, and a tier A chosen by record will cover fewer.
- N13. Section 4: the orchestrating chat session should not see the scorecard either, since it writes briefs. Grade F
  Acquirers Fund (ZIG, launched 2019) has under eight years, and 5.3 does not say how ranks combine when a window is
  missing.
- N14. Section 9: "CRSP ... to 2025-12" is not in the WRDS guide, which says only "annual update". The live
  reference book starts before the two-source check G7 (E1.7, Stage 2). v0.2 6.1 says a pod goes live only after G7.
  This is inherited from v0.2.

## 3. Corrections (find and replace against the plan as it stands)

Each "Find" occurs exactly once in the file (checked by script). Line breaks inside a block are part of the text.

C1 (M1, S1)
Find:
```
30 by record: the average of three ranks (style-adjusted result over the
  full history, with at least eight years; the same for 2021-25; share of five-year blocks with a positive
  style-adjusted result), grades A, B or F, at most eight per style.
```
Replace:
```
30 by record: the average of three ranks, all from 2011 onward (style-adjusted result over
  2011-25; the same for 2021-25; share of the blocks 2011-15, 2016-20 and 2021-25 with a positive style-adjusted
  result), grades A, B or F, at most eight per style. Ranks are taken within each kind of record (13F copies, real
  fund returns), never across them. No return from before 2011 enters the ranking, so the design era stays free of
  selection on the investors' returns.
```

C2 (M1)
Find: `- Windows: 2021-25 (the five years asked for), 2016-20, 2011-15, 2006-10, and the full history.`
Replace:
```
- Windows: 2021-25 (the five years asked for), 2016-20, 2011-15 and 2011-25. Years before 2011 are not computed
  before the freeze: they are the design era, and a ranking on them would leak into its tests.
```

C3 (M2, option b)
Find: `| Holdout, outside the US, 2011 onward | Sealed; one run. Counts toward the verdict of every family: US-based investors were not chosen on these markets. It is weaker than a true holdout because styles move together across regions, so a family must pass both non-US samples |`
Replace: `| Holdout, outside the US, 2011 onward | Sealed; one run. Counts toward the verdict only for a family that meets a rule registered at E3.5: its source investors' records, holdings and examples are mainly in the US (proposal: under 20% outside the US), and in 1990-2010 the pod's added return in the US and outside the US were not closely linked (proposal: correlation under 0.5). Then the family must pass both non-US samples, each by a test fixed at E3.5. Otherwise this sample is reported, not a verdict. Even when it counts it is weaker than a true holdout: styles move together across regions, and the thesis was stated after 2010 |`

C4 (M2, option b; insert a row for v0.2 4.4)
Find: `| 6.1 Sources | The library is`
Replace:
```
| 4.4 Verdicts | A family whose thesis is documented after 2010 can be Core only through the non-US holdout under the rule in 8.2, and then only as provisional Core until its first live checkpoint. This departs from the macro rule that hindsight-flagged pods are never Core, because 647 of the 695 General documents are dated 2022 or later |
| 6.1 Sources | The library is
```

C5 (M3)
Find: `## 6. Holdings module: what they bought, on the day they bought it`
Replace: `## 6. Holdings module: what they bought, as it looked just before they bought it`

C6 (M3)
Find: `sector at that quarter-end on every measure`
Replace: `sector at the end of the previous quarter (13F does not show the day of purchase, so this is the last date surely before it) on every measure`

C7 (M3)
Find: `- No return after the purchase date appears in any output. A past return appears only as a rank on the day.`
Replace: `- No return after the purchase date appears in any output. A past return appears only as a rank at the end of the quarter before the purchase.`

C8 (M3)
Find: `Uses ranks on the day, price-based ones included`
Replace: `Uses ranks at the end of the quarter before the purchase, price-based ones included`
(Also, optional: in section 1 replace `(what did a purchase look like on the day?)` with `(what did a stock look like just before they bought it?)`.)

C9 (M4)
Find: `A verdict only for a family whose thesis is documented before 2011 and whose investors were not picked on those years.`
Replace: `A verdict only for a family whose thesis is documented before 2011, whose sources have no career overlap, whose investors were not picked on those years, and whose spec took nothing from holdings after 2010 (its revealed thresholds and say-do check use quarters before 2011 only).`

C10 (M4, S17)
Find: `The holdout is split by region. For a family with career overlap or picked through the scorecard, the US part is reported only; the non-US part counts, and both non-US samples must pass (8.2 above)`
Replace: `The holdout is split by region. The US part gives a verdict only under the conditions in 8.2; otherwise it is reported only. The non-US part counts only under the rule in 8.2, and then both non-US samples must pass`

C11 (M4; insert a row for gate G8)
Find: `| 7.1 Pilot | 16 documents`
Replace:
```
| 6.3 Gate G8 | The two registered descriptive jobs (scorecard and holdings module) may read US data from 2011 on before the freeze. Each run is logged as an opening of the seal. Data outside the US from 2011 on stays sealed until the freeze |
| 7.1 Pilot | 16 documents
```

C12 (M5)
Find: `ranked walk-forward. It competes for a test slot like any family.`
Replace:
```
ranked walk-forward (each month uses only the records known by then). Its spec is registered before the scorecard
runs, because the scorecard shows how such copies did after 2010. Its US result from 2011 is reported only, and 13F
has no version outside the US, so it is judged on the design era and the live record. It competes for a test slot
like any family.
```

C13 (S1)
Find: `peer group of similar size, value and`
Replace: `peer group of similar size, value, profitability and`

C14 (S2)
Find: `| F | A public fund or listed vehicle with real returns after fees | Oakmark (Nygren), Acquirers Fund (Carlisle), Markel (Gayner) |`
Replace: `| F | A public fund with real returns after fees. A listed company that also runs a business, such as an insurer, is graded on its 13F instead, because its share price mostly reflects that business | Oakmark (Nygren), Acquirers Fund (Carlisle). Markel (Gayner) is graded A or B through its 13F |`

C15 (S2)
Find: `(CRSP mutual funds and listed vehicles on WRDS;`
Replace: `(CRSP mutual funds and exchange-traded funds on WRDS;`

C16 (S2)
Find: `| Fund returns for the scorecard | CRSP mutual funds, listed vehicles in CRSP |`
Replace: `| Fund returns for the scorecard | CRSP mutual funds, including exchange-traded and closed-end funds |`

C17 (S3)
Find: `  pipeline. No agent is told who is control.`
Replace:
```
  pipeline. No agent is told who is control. A family counts as control-sourced when most of its investors are
  control. Control pods get the same sealed runs as other pods, reported only. With ten investors there may be only
  one or two such pods, so the comparison in 5.4 is descriptive, not a test.
```

C18 (S4)
Find: `2. **Returns.** No agent that writes claims, cards, charters or specs sees a return, of a stock or of an investor.`
Replace:
```
2. **Returns.** No agent that writes claims, cards, charters or specs is given a return, of a stock or of an
   investor. The models still know from training how famous investors and stocks did, so the packs for the
   strategist and the spec writers name investors by an id, not by name or firm.
```

C19 (S5)
Find: `  revealed distribution, for example the lower quartile of the family's purchases. The source is logged as`
Replace:
```
  revealed distribution, for example the lower quartile of the family's purchases in odd years. The say-do check
  then uses the even years, so it does not check a threshold against the purchases that set it. The source is logged as
```

C20 (S6)
Find: `A technique is never tested for returns on its own and never adds a test slot.`
Replace: `A technique is never tested for returns on its own and never adds a test slot. Batch A keeps the list of v0.2 section 10, with a maximum number of hygiene tests fixed at E3.5; a technique can only take a place on that list.`

C21 (S7)
Find: ``company data with dated history (`RDP.Data`, the older `TR`), and``
Replace: ``dated price history for one company (Apple month-end closes from 1990, `RDP.Data`; the older `TR` was tried only on the S&P 500), and``

C22 (S7)
Find: ``  Datastream (`DSGRID`). Source: `tools/bbgq/results/lseg_probe_v1.txt`.``
Replace: ``  Datastream (`DSGRID`). Source: `tools/bbgq/results/lseg_probe_v1.txt`. Company accounts, estimates and holders were not tested.``

C23 (S8)
Find: `- Fields carry the period end, the source filing date and whether a value is original or restated`
Replace: `- Fields exist for the period end, the source filing date and whether a value is original or restated (in the cited thread the last one came back empty on weekdays, and it does not show that first-reported values can be pulled)`

C24 (S8)
Find: `  Source: LSEG developer community.`
Replace:
```
  Source: LSEG developer community. The Data Library's estimates page lists past consensus snapshots for the last
  12 months only in that interface; I/B/E/S itself starts in 1976 for the US and 1987 elsewhere.
```

C25 (S9)
Find: `| Bloomberg | Campus only; the download allowance ran out on 13 Nov | No role in the design; optional cross-check sample |`
Replace: `| Bloomberg | Campus only, and the download allowance can run out: on 13 Nov it blocked every request until it cleared later that day (files R8-R12 were pulled on 13-14 Nov) | No role in the design; optional cross-check sample |`

C26 (S10)
Find: `   screens separated winners from losers, and all of it was the profitability factor`
Replace: `   screens' warnings picked losers, all of it was the profitability factor, and the registered buy-minus-avoid test found no return after factors`

C27 (S11)
Find: `| Markets outside the US | Compustat Global and Global Factor Data on WRDS (to be checked) | LSEG, Datastream | |`
Replace: `| Markets outside the US | Compustat Global and Global Factor Data on WRDS (to be checked) | LSEG, Datastream | No 13F ownership, short interest or insider data outside the US; delisting returns to be checked. The shortable set there needs a stand-in fixed at E1.4, and a pod that needs a US-only input is judged on the design era and the live record |`

C28 (S12)
Find: ``| Insider trades | SEC Form 4 data sets (free; `triage/owners.py` reads them) | same | WRDS insider table: no permission |``
Replace: ``| Insider trades | SEC Form 4 data sets (free; `triage/owners.py` reads them) | same | WRDS insider table: no permission. The SEC data sets start in 2006, so the design era has five years of insider data, under the ten years a design test needs |``

C29 (S13)
Find: `not change: its rules (section 3), portfolio and risk design (9), test sheet (10), live cycle (11) and terms (20).`
Replace:
```
not change, every section included; in particular its rules (section 3), evidence design (4), data gates (6.3),
portfolio and risk design (9), test sheet (10), live cycle (11) and terms (20). Where the two files differ, this
plan wins.
```

C30 (S13)
Find: `4. How long WRDS and LSEG access will last.`
Replace:
```
4. How long WRDS and LSEG access will last, and whether the LSEG licence is for academic use only.
5. PDFs for the equity paper pack (the list comes with E0.3).
Only before real money: account size, broker, and whether the account can short.
```

C31 (S14)
Find:
```
Effort, in tokens. The figures for Fable and the engine come from the macro program's log; the extraction figure
is a guess that the pilot replaces with a measurement.
```
Replace:
```
Effort, in tokens. The Fable figures come from the macro program's log. The other figures are estimates (the log
has about 0.6M for one engine build and 0.3M for its check); the pilot replaces the extraction figure with a
measurement.
```

C32 (S14)
Find: `- Fable: one map, 6-12 charters, one register review, two batch reviews, one verdict: 11-17 units of 0.65-0.9M,`
Replace: `- Fable: one map, 6-12 charters, one register review, two batch reviews, one verdict (playbook cards and the monthly reviews once live are not counted): 11-17 units of 0.65-0.9M,`

C33 (S15)
Find: `The statistical design of v0.2 holds.`
Replace: `The statistical design of v0.2 holds in the author's view. v0.2 never had its own independent review (its step 0); the check in section 13 covers v0.2 only where this plan relies on it.`

C34 (S16, option a)
Find: `  pod is not re-run with tweaks.`
Replace:
```
  pod is not re-run with tweaks. So not every screen gets a history test: at most eight pods do, chosen by a
  script (v0.2 8.5). The rest run as live screens (Incubator) and are judged on their live record.
```

C35 (N5)
Find: `Tags of about 440 General documents mention valuation, analysis, screening, portfolio construction, risk or shorting (overlapping counts)`
Replace: `Tags of up to about 440 General documents mention valuation, analysis, screening, portfolio construction, risk or shorting (overlapping counts; a loose word match, and a stricter one gives about 290)`

### Plain language (F): real obstacles for a reader who does not code
1. Section 1 item 2: "Sharpe ratio", "standard error", "the largest of 20 draws averages about 1.9 standard errors".
   None is explained. Suggest: "return per unit of risk", "the usual size of the error in that number".
2. Section 3 row 1: "t-value near 0.5". It needs "(a t-value of 2 is the usual bar for 'probably not luck')".
3. Section 1 item 1 and later: "13F" and "filer" are first used without saying what a 13F filing is (a quarterly
   list of US-listed stocks held by a manager with over $100M).
4. Section 5.2: "five-factor plus momentum alpha with its t-value", "percentile", "peer group of similar size, value
   and momentum".
5. Section 5.3: "a seeded script" (meaning a random draw that can be repeated exactly).
6. Section 6: "walk-forward", "lower quartile", "revealed distribution".
7. Section 8.1: "Core, Sleeve, Exclusion, Incubator or Shelved" are not defined in this file. They are in v0.2 4.4,
   and a one-line pointer would do.
8. Section 9: "the two-source gate (G7)", "StarMine scores", "the Python interface", and the field codes
   (`TR.F.SourceDate` ...). The codes are fine as references, but the sentence around them should say what they show.
9. Sections 5.4 and 6: "registered descriptive job". It is never defined (a run whose output form is fixed and
   checked before it runs, and which only describes, never decides).
10. Misreadable, not only jargon:
    - "Tier A is picked on returns after 2010" (false as 5.3 stands; see M1).
    - "Sealed; one run" for the US holdout, while two jobs read it earlier (see M4).
    - "style taken out" (profitability is not; see S1).
    - "Counts toward the verdict of every family" (see M2).

## 4. What was verified, and what was not

Verified and found correct:
- Every inventory number in section 2. I re-ran `tools/equity/library_stats.py` on the manifest, and the output is
  identical to `library_inventory_2026-11-15.md`:
  - 2,257 documents and 17.0M words;
  - 695 General documents and 8.3M words, 60 of them in "macro nov 26";
  - 327 / 153 / 123 / 92 by document kind;
  - 239 / 191 / 48 investors;
  - the 40 most frequent cover 146 documents and 2.0M words;
  - 647 of 695 dated 2022-26;
  - 440 technique documents (but see N5);
  - the other folders 431 / 883 / 214 / 24 / 10.
  The "about six times larger" claim holds for documents (2,257 / 397 = 5.7).
- Section 1 arithmetic. A 15-year Sharpe standard error is 1/sqrt(15) = 0.26. The expected maximum of 20 standard
  normal draws is about 1.87, and 1.87 x 0.26 = 0.48 ("near 0.5"). Section 3: t = 0.45 to 0.67 (N1).
- RESULTS.md: profitability loadings and nothing left after FF5+UMD; that the plan's wording overstates (S10).
- LSEG probe v1: Apple monthly closes 1990-01 to 2026-10 via `RDP.Data` (line 43). `TR` was tried only on .SPX
  (line 50), and `DSGRID` works.
- LSEG web pages (fetched 2026-11-15):
  - Usage guide: about 5 requests a second, about 50 MB a minute, about 3,000 rows per interday history request, and
    a daily limit that resets at local midnight. All correct.
  - Fact sheet: "108K+ active & inactive companies", "US history since 1983 & 1995 for non-US", "700+ operating
    metrics across 22 industries", restated values, and the point-in-time sentence. All correct (N10).
  - Ownership thread: holders with a past date via `TR.InvestorFullName` / `TR.PctOfSharesOutHeld` with SDate, and
    `TR.SIInstitutionalOwn` has no date window. Correct.
  - Fundamentals thread: the fields exist but are unreliable (S8).
  - Estimates page: see S8.
- WRDS guide: CRSP mutual funds, mutual fund holdings, Compustat Global, Financial Ratios and Global Factor Data are
  on the subscription list. Insider data is not permitted. The licence is "academic, non-commercial research and
  paper trading only", and loading data into AI tools is prohibited. All match the plan.
- SEC Insider Transactions Data Sets start in 2006 Q1 (sec.gov).
- Every v0.2 section and step number cited in the plan points to the right thing: 3, 4.1, 4.2, 6.3/G7, 7.1, 7.2,
  7.3, 7.4, 8.1, 8.3, 8.4, 8.5, 9, 10, 11, 11.2, 13, 14, 16, 20, E1.1-E1.8, E1.3, E3.3, E3.5, E5.5. Exceptions are
  noted in M2, M4, S13, N6-N9.
- Effort figures checked against the CLAUDE.md log (S14).
- Every "Find" string in section 3 occurs exactly once (script check).

Not verified:
- The SEC Form 13F data sets page did not load (sec.gov/data-research/sec-markets-data/form-13f-data-sets, the
  permission request timed out). "SEC 13F data sets from 2013" is therefore unconfirmed, though consistent with
  search results.
- Whether the named managers (Giverny, Valley Forge, Semper Augustus, etc.) actually file 13F with the coverage the
  grades assume. The plan itself defers this to E0.4.
- Compustat Global delisting returns and its early-1990s coverage, Compustat short-interest coverage, and the CRSP
  data end date. These need the WRDS table check (E1.2).
- The mermaid diagram was read as text only, not rendered.
- v0.2 as a whole (its own step 0 review). I read all of it, but only checked what v0.3 relies on.
- No transcript text was read.

## 5. Effort
- Time: about 25 minutes of work (21:49 to about 22:15 UTC).
- Tokens: I cannot see an exact count; my rough estimate is 150-200k tokens in total, including the two design files,
  the script runs and seven web fetches.
