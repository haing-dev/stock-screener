# Equity pod shop: registration with plan v0.4 (2026-11-20)

Registered before any engine, data pull beyond test files, holdings job or test run exists. It amends
`STAGE0_REGISTRATION.md` (tier rule, section 7) and the samples of plan v0.3 8.2. The commit that adds this file
is the registration. Later changes are appended as dated addenda, never edited in place.

## R1. Roster rule v2
An investor is on the roster when all three hold.
1. Record, one of: (a) `rank_share` >= 0.60 on 2011-25 in `scorecard_check/league_table_2026-11-18.csv` with at
   least five years of record (the top 40% of all measured managers; the bar is set at the lowest record among
   the 21 the user accepted on 20 Nov, Li Lu at 0.61, and is fixed from here on); (b) rank 1-50 in
   `hf_leaderboard/top50_hf_5y_2021-2025.csv`.
2. Material: at least one long document in which the investor explains the method in their own words.
3. Screenability. At registration: grade A or B (incl. B?) in `hf_leaderboard/roster_screenability_2026-11-20.csv`.
   Measured gate, applied when the investor's claims are extracted: share of stated selection criteria that a
   script can compute from the field dictionary >= 0.5, counted by the spec writer and recounted blind by the
   checker (the lower count decides), and the computable criteria alone select between 10 and 300 US stocks on
   the last quarter-end. Fail = off the roster, to the analyst notes; logged here.

Roster at registration (21):
A: Joel Greenblatt, Terry Smith, Dev Kantesaria, Chris Hohn, Glenn Greenberg, Val Zlatev, Derek Pilecki.
B: Bill Nygren and Alex Fitch (one entry), Murray Stahl, Pat Dorsey, Chris Davis, Joseph Shaposhnik, Alex
Sacerdote, David Einhorn, Stan Druckenmiller, Todd Kantor, Bob Robotti, Fred Martin.
B?: Brad Gerstner, Chris Bloomstran, Li Lu.
Open places: 9. A place is filled only by an investor who passes 1-3; each addition is an addendum with the date,
the record line and the documents. No investor is added after the first B1 slot is given.
Control group: the 10 control investors drawn at Stage 0, unchanged. They pass through the same pipeline; rule 3
is measured for them but does not remove them.

## R2. Conviction purchase
Data: `tfn.s34` first versions, quarter-ends 2009-12 to 2025-12, roster and control investors (and all filers for
the "follow the best managers" pod of `STAGE0_REGISTRATION.md` section 10). Weight = value of the holding over the
value of all reported holdings matched to a common stock. New position = held now, not at the previous
quarter-end. Addition = shares up by at least 20% split-adjusted.
Version a: a new position or addition after which the stock is among the five largest weights.
Version b: a new position or addition whose bought value (change in shares times the quarter-end price) is at
least 1% of the portfolio.
Both versions are computed; every use averages them. Known on the filing date (45 days after quarter-end where
the date is missing). The job is seal-exempt and logged (`SEAL_LOG.md`), code hash in
`tools/equity/seal_exempt.json` before it runs; strategy writers receive only aggregates over at least 20
purchases, with odd calendar years setting a threshold and even years checking it.

## R3. Samples
- Main test period: US, 2010-01 to 2025-12 (192 months). Eras 2010-14, 2015-19, 2020-25.
- Universe at each month-end: US-listed primary common shares, the 1,500 largest by market value, price at least
  $5, median daily dollar volume of the last three months at least $2m; banks, insurers, real estate and biotech
  are outside generic pods (sector pods only).
- Side check: US 2001-01 to 2009-12 on WRDS, reported lines only, only for measures whose inputs exist.
- Outside the US (developed markets), 2010-01 to 2025-12: sealed until the freeze, then run once per pod.
- 2026-01 to the month before a pod goes live: run once at the freeze, reported.
- Live: from the go-live month; append-only ledger.
- Access: portfolio, signal and factor returns of 2010-2025 are computed only by the test desk's scripts in runs
  written to the trial log before they start. Levels of company measures are open to every desk.

## R4. Portfolio rule
Monthly formation at month-end data, trade at the next day's close. 12 tranches, each formed once and held 12
months; at each monthly review a holding whose rank has left the top two tenths of the pod's score inside its
sector is sold early. Equal weight inside a tranche; cap 2.5% of the book per stock; a pod selecting fewer than 15
names holds the remainder in the sector-matched universe. Costs: half the quoted spread where available, else 10
basis points per side for the 500 largest and 25 for the rest; doubled in test 3. Nominal account $10m; a
position may not exceed 5% of median daily dollar volume. Missing measure = sector median score; a stock missing
more than half of a pod's measures is not ranked. Open spec choices are versions, equal-weight averaged; no
version is picked.

## R5. Tests and classes
Added return = monthly return of the pod minus its fitted exposure to reference book v1 and to the
sector-matched universe (regression intercept plus residual).
1. Alpha > 0: p-value from the whole-month bootstrap (10,000 draws, blocks of 6 months); Holm at 0.025 per batch.
2. Eras: in each era the point estimate of the added return >= minus one Newey-West standard error of that era.
3. Added return > 0 at doubled costs.
4. Placebo: 1,000 random portfolios with the pod's names per sector, its average holding period, the same
   costs; the pod's added return above their 95th percentile.
5. Tail: worst fall of (reference book + pod at equal risk) not worse than the reference book's by more than 2
   points; worst month not worse by more than 1 point.
Same-period checks: A outside the US, added return > 0, once after the freeze; B added return above the 90th
percentile of the control pods' added returns (all control pods and versions pooled; needs at least 20, else
reported only and the class is capped at Incubator); C with source investors' conviction holdings removed in the
quarters held, the added return keeps its sign and at least half its size.
Classes: Passed on history = tests 1-5 and checks B, C (A added at the freeze; a fail of A moves the pod to
Incubator). Sleeve = fails test 1 but lowers the tail of the book by test 5's measure and passes 3. Exclusion =
an avoid rule whose excluded stocks have an added return below zero by tests 1-3 with the sign reversed.
Incubator = one descriptive run with test 4 passed. Shelved = the rest. Core is given by the live rule only.

## R6. Budget and slots
Batch 0: plumbing, no verdicts. Batch A: reference-book hygiene, targets named in an addendum before it runs.
B1 and B2: at most 4 pods each. A slot is given by script on: number of independent roster investors behind the
pod, a stated reason why the edge persists, measured screenability, power (pass rate of tests 1-2 at an added
information ratio of 0.5 on 192 months at least 50%), distance from the reference book and from pods already
chosen (rank correlation of scores below 0.7). Every other pod: one descriptive run. No re-run after a result
except a logged bug fix checked by a second implementation.

## R7. Reference book v1
Groups and sources (all published before 2011): value = earnings yield (EBIT over enterprise value) and book to
price (Basu 1977; Fama and French 1992); momentum = return of months t-12 to t-2 (Jegadeesh and Titman 1993);
quality = return on equity (Haugen and Baker 1996), accruals (Sloan 1996), the nine-point score of Piotroski
(2000); expectations = change in the FY1 consensus over three months scaled by price (Chan, Jegadeesh and
Lakonishok 1996), slow form: held under the R4 rule. Each measure is ranked inside the GICS sector; a group score
is the mean of its measures' ranks; the book score is the mean of the four group scores. Long book: top tenth,
under R4. Exact field formulas: field dictionary v1.0, registered in an addendum before Batch 0 and before any
return is computed. Gross profitability (2013) and any other post-2010 measure can only enter as a
hindsight-flagged pod.

## R8. What is not registered yet
The pods themselves (charters, specs, versions), Batch A targets, the field dictionary v1.0, the data lock, the
"follow the best managers" pod's place in B1 (it competes under R6), the non-US universe rule.

## Addendum A1 (2026-11-21): universe completeness check
Job `eq_univ_check_v1` (module `tools/equity/wrds/eq_univ.py`, seal-exempt entry `universe_check`, code sha256
46e6bcdc..., input sha256 6eddb7ed...). Input: 43,678 8-digit CUSIPs of US common shares found in LSEG (Datastream dead
and research lists, Workspace screens of test file 2). Reads CRSP names and December price and shares 2009-2025 (levels,
no returns). Output: share of CRSP common shares found per year, for all, the 1,500 largest and the 1,500 largest priced
at $5 or more, and for companies leaving CRSP each year; names of at most 10 large companies not found. Pass rule for
the universe (set before the run): at least 99% of the 1,500 largest priced at $5 or more found in every year 2010-2025;
otherwise the missing ones are added from a further source before the data files are built.

## Addendum A2 (2026-11-21): universe check, result of v1 and version 1.1
Result of `eq_univ_check_v1` (`eq_univ_check_v1_report.txt`): 83-87% of the 1,500 largest priced at $5 or more found
per year; 59-77% of companies leaving. The A1 rule (99%) is NOT met. Cause found in the LSEG files, not yet measured:
the CUSIP key misses (a) companies not incorporated in the US (their LSEG identifier carries no CUSIP: Accenture,
Medtronic, Royal Bank of Canada) and (b) companies whose CUSIP changed after CRSP ends in 2025-12 (Exxon Mobil,
Honeywell, DuPont); all six are in the LSEG lists. So v1 measured the key, not the list.
Logged bug-fix rerun `eq_univ_check_v2` (module version 1.1.0, code sha256 8c28d777..., input sha256 53a82235...):
keys in steps (CUSIP; + current ticker for companies still listed at 2025-12; + normalised name), split by CRSP's
US-incorporation flag. Same data read (CRSP names, December price and shares; no returns). The 99% rule is applied to
the US-incorporated part with all three keys; the part not incorporated in the US is reported, and which of those
companies belong to the universe (R3 says "US-listed primary common shares") is settled in an addendum before the
data files are built. The name key is loose (first four words after dropping legal suffixes), so a pass on names alone
is a lower bar than a CUSIP match and is reported separately.

## Addendum A3 (2026-11-21): universe = US companies; third check run
User decision (20 Nov, after briefly considering UK / Europe): US companies only. Universe rule added to R3: a
company is in when its primary listing is on a US exchange (NYSE, NYSE American, Nasdaq) as LSEG shows it, wherever
it is incorporated (Accenture, Medtronic in); foreign companies whose primary listing is abroad are out (Royal Bank of
Canada, Unilever, ASML), as are depositary receipts. Check A (outside the US) is unchanged: sealed, pulled only before
the freeze.
`eq_univ_check_v3`: same code as v2 (sha256 8c28d777...), input extended with Datastream dead lists DEADUS11 (T-V)
and DEADUS12 (W-Z) from universe file 2 (input sha256 a18f916a...; 47,700 CUSIPs, 86,680 names). Rule as in A2.

## Addendum A4 (2026-11-21): universe check v3 result; universe rule; conviction holdings job
1. `eq_univ_check_v3` (report `eq_univ_check_v3_report.txt`): US-incorporated 1,500 largest priced >= $5 found with
   all three keys 99.3% to 100.0% in every year 2009-2025 (CUSIP alone 98.3-99.5%); US-incorporated companies leaving
   CRSP with a peak in the 1,500: 97-100% found. Rule A2 MET. Still missing (10 in 2009, 0 in 2024): mostly renamed
   or acquired companies (Yahoo, Dr Pepper Snapple, J.C. Penney, Legg Mason); added by hand to the candidate list if
   their data come back by ISIN.
2. Universe (user, 2026-11-21: "RBC, ASML" must not be in): candidates = Datastream equity lines with type EQ,
   Datastream geography United States, primary line, alive at some point 2010-2025. This keeps US-run companies
   incorporated abroad whose primary listing is in the US (Accenture, Medtronic, Spotify show geography United
   States) and drops foreign companies with a US second listing or receipt (Royal Bank of Canada: Canada; ASML:
   Netherlands; UBS: Switzerland; Shopify: Canada). 26,932 candidates (25,620 with ISIN). The monthly rule of R3
   (1,500 largest, $5, $2m volume) selects from them; stage A0 (size file) narrows the set first.
3. Conviction holdings job `eq_conv_v1` (module `tools/equity/wrds/eq_conv.py`, seal-exempt entry
   `conviction_holdings`, code sha256 d9320b04...): R2 as registered, for 21 roster and 8 control investors with 13F
   ids known (20 investors); name search printed for the other 9 (ids enter v2's input; not used in v1). Panel stays
   on WRDS; counts only come back.
4. Control group overlap: David Einhorn and Joseph Shaposhnik are in the Stage 0 control group AND on the roster. They
   stay on the roster; the control group is 8 until two replacements are drawn by the Stage 0 rule (open).

## Addendum A5 (2026-11-21): size selection, monthly files, conviction job v2
1. Size file (LSEG_size_v1, year-end company market value 2009-2025; no block failed): TR.CompanyMarketCap is a
   COMPANY figure, repeated on every line of a company (share classes, preferred and depositary lines, old debt
   lines). Selection: drop lines whose name marks preferred, depositary, debt, fund, unit, warrant or right; group the
   rest by company name; a company is selected when it is among the 2,500 largest companies at any year-end 2009-2025
   (the 1,500th company is $0.9bn at 2009 and $3.3bn at 2025; the 2,500 cut leaves room for moves within a year). All
   its remaining lines go to the monthly files: 5,065 companies, 5,537 lines. 1,312 candidates without an ISIN are not
   in the size file (mostly old dead lines); the WRDS check found US coverage of 99.3-100% without them.
2. Monthly files (3 workbooks): close, security shares, company market value, monthly volume, one-month total return,
   2009-12 .. 2026-10. Security market value = close x security shares; when a company has several common lines the
   R3 rule ranks each line on its own (as CRSP does). The $2m volume rule of R3 uses the average daily dollar value of
   the last three months from monthly volume / trading days (a stand-in for the median, recorded here before any use);
   a check block in part 1 tests whether monthly TR.Volume is the month's total.
3. `eq_conv_v1` had a bug (quarter filter `mod(yyyymm, 3) = 0` kept only years divisible by 3: 24 quarters). v1's
   counts are void. `eq_conv_v2` (code ad0dde91...): filter fixed; 13F ids from v1's name search added: Greenblatt
   (Gotham 10969, 12775), Pilecki (Gator 8799), Nygren / Fitch (Harris Associates 43485, the whole firm), Stahl
   (Horizon Kinetics / Kinetics 44850, 49373), Davis (Davis Selected 78320), Van Den Berg (Century Management 15095).
   No 13F found: Shaposhnik, Carlisle; Elfenbein's hits (CrossingBridge, AdvisorShares) are other people's firms.

## Addendum A6 (2026-11-21): conviction holdings v2 result (counts only; report eq_conv_v2_report.txt)
26 of 29 investors have 13F holdings; 65 quarters (2009-12..2025-12); panel `eq_conv_panel` on WRDS (132,980 rows).
Conviction purchases (version a / b / either) range from 17 (Li Lu, 31 quarters) to about 760 (Kantor). Points for the
holdings module (step 6), not changes to R2:
- Greenblatt's 13F (Gotham) is a quantitative book of about 910 names with 6% in the top five: "conviction" in R2's
  sense does not describe it; his pod is built from his stated rules, and his 13F is reported but not used for
  revealed thresholds.
- Firm-wide filings mix several managers (Harris Associates = Nygren / Fitch plus others; Davis Selected; Horizon
  Kinetics 279 names): revealed thresholds from them are flagged "firm, not person".
- Chanos files longs only (he is known for shorts): control use only, as registered.
- No 13F: Shaposhnik, Carlisle, Elfenbein.

## Addendum A7 (2026-11-21): monthly data checks; liquidity stand-in; company data files
1. Monthly files read (`LSEG_monthly_v1_2026-11-21.md`): 5,436 lines, 99% filled, total return aligned with prices.
2. Liquidity in R3: monthly TR.Volume is one day's volume. The rule "median daily dollar volume of the last three
   months >= $2m" is applied as "median of the last three month-end daily dollar volumes >= $2m" (zeros missing) until
   daily volume is pulled; both are reported once daily data exist. Fixed before any return is computed.
3. Accounts are pulled once per company on its primary line (the selected line with the largest median security
   value; 371 of 5,065 companies have more than one common line). Universe ranking stays per line (R3).
4. Company data files (stage B; builder `docs/data_requests/build_lseg_company_data.py`): quarterly accounts as first
   reported (about 80 quarters, 49 items, period end and announcement date), annual first-reported accounts (27 years,
   19 items), monthly consensus 2009-12..2026-10, quarterly actual EPS with report date, GICS (today), monthly short
   interest from 2010. 12 workbooks.

## Addendum A8 (2026-11-22): field dictionary v1.0 part 1; engine spec choices; Batch 0 (first counted run)
Registered before any return of 2010-2025 is computed (user's go 2026-11-21: engine and reference book on WRDS while
the LSEG files wait).
1. **Field dictionary v1.0, part 1** = `FIELD_DICTIONARY_v1.0.md`: exact formulas of the seven reference-book
   measures (V01, V06, P01, Q03, Q08, B05, E01), market value, liquidity and sector, each in its LSEG and WRDS form.
   Part 2 (the other measures) is registered with the pod specs. No change to part 1 after this entry (= book v2).
2. **Spec choices left open by R3, R4 and R7** (fixed here; the same in the LSEG run):
   a. Universe order: the 1,500 largest US-incorporated common lines (CRSP `usincflg` = Y; LSEG GEOGN = US) by line
      market value, then price >= $5 and liquidity >= $2m (WRDS: median of the last three monthly medians of daily
      dollar volume; LSEG: A7 stand-in). Generic books exclude GICS groups 4010, 4030, 4040, sector 60 and
      sub-industry 35201010 (biotech); a member without a GICS sector is not ranked.
   b. Long book = top tenth of all ranked stocks by book score (not per sector). Monthly review: a holding whose
      inside-sector book percentile is below 0.8, or that is no longer ranked, is sold; its proceeds sit in the
      equal-weight universe of its sector (the sector basket) until the tranche ends. Cap 2.5% of the book per stock
      at formation; the excess goes to the sector basket.
   c. Trade timing: monthly data, so formation and trades at the month-end close (R4's next-day close needs daily
      data; the difference is reported when the daily engine exists).
   d. Costs: 10 bp per side for the 500 largest, 25 bp for the rest; basket trades 10 bp. Gross and net both reported.
   e. Formations from 2009-01 (ramp-up: 1/12 of capital per month for the first 12, the rest in cash at the
      risk-free rate); book returns 2010-01..2025-12.
   f. Benchmarks: the sector-matched universe (the book's sector weights at the start of each month times the
      equal-weight sector universe returns) and the equal-weight universe.
3. **Batch 0** (plumbing; no verdict; nothing is adopted or changed because of its numbers). Run T001
   (`TRIAL_LOG.md`): `eq_ref_pull_v1` then `eq_ref_v1` on WRDS, code c8705b6f... (eq_ref 1.0.1; seal-exempt job 6
   `reference_book`). Prints: universe and coverage by year; rank correlations of the measures; published-form checks
   of each measure (sign, NW t, correlation with the matching Fama-French factor); the reference book's statistics
   (net, gross, against the two benchmarks, by era and by calendar year incl. 2020-21 = stress M4), turnover, costs,
   names, cap and liquidity checks. Series stay on WRDS (`ref_series`, `ref_spreads`).
4. **Known differences of the WRDS form** (reported, not fixed): Compustat values are not first-reported; I/B/E/S
   prices put on the current share basis via CRSP factors; history of GICS (LSEG: today's GICS). The LSEG run of the
   same engine (after the stage-B files) is the registered primary; Batch 0 compares the two.
5. Still open: the second implementation by a separate agent (plan step 5) before Batch A; the daily engine.

## Addendum A9 (2026-11-22): say-do tables (desk 1 gate; descriptive, no return)
What the roster's and control's conviction purchases (R2, `eq_conv_panel`, versions a and b) looked like at the end of
the quarter BEFORE the purchase quarter: inside-sector percentile (all industries, universe members per R3) of 13
measures: the seven book measures (FIELD_DICTIONARY_v1.0 part 1), market value, and five descriptive measures (gross
margin, operating margin, sales growth and asset growth on four quarters, net debt to assets; WRDS form). Per investor
(masked ids M01.., ordered by SHA-256 of the name; key = the frozen list, referee only) and pooled roster / control:
median percentile for version a, version b, their average, share in the top 30%, odd-year and even-year medians;
cells with fewer than 20 purchases are blank. Job `eq_saydo_v1` = eq_ref 1.1.0 `saydo()` (code c6021bb1...; run()
unchanged). Levels only; no portfolio, signal or stock return is computed, so it is not a trial (fence 7). Use: the
say-do table per investor (stated criteria against revealed purchases) and the "revealed by purchases" threshold tags
of the strategy writers (odd years set, even years check). Not used to choose investors or pods.

## Addendum A10 (2026-11-22): plan v0.5: judged on three uses; fidelity gates; scorecard W / R / C; investor form
Source: the user's feedback of 22 Nov (`EQUITY_POD_SHOP_PLAN_v0.5.md`). Registered AFTER Batch 0 (T001: portfolio
returns of the reference book and of its seven measures) and the say-do tables (A9) were seen, and BEFORE any recipe,
pod, first flag, hit rate or concentrated portfolio exists. R1-R7 and A1-A9 stay in force except where stated.

1. **Uses and product.** The tools are judged on three uses: spotting individual winners early (block W), controlling
   risk (block R), constructing portfolios (block C). The product is a private dashboard. The scorecard below replaces
   "added return over the reference book" as the only verdict; R5's tests 1-4 are C1, test 5 is R3.
2. **Definitions.**
   a. Eligible set of a pod at month-end t: the R3 universe members that pass price and liquidity and have a GICS
      sector; a generic pod leaves out the industries of A8 2a; a sector pod takes its sector's members.
   b. Pass set: the eligible stocks the recipe's entry criteria select at t. With several versions every statistic is
      computed per version and averaged.
   c. First flag: a stock in the pass set at t that was in it at none of the 12 month-ends before. A further first
      flag of the same stock within 36 months of a counted one is not counted. Pass sets from 2009-01; first flags
      counted from 2010-01.
   d. Forward return over H months: total return from the close of t to the close of t+H. A stock that leaves the
      data earlier takes its last (delisting) return, then the equal-weight return of the eligible stocks of its
      sector to t+H. H = 36 is decisive (formation months 2010-01..2022-12); H = 12 and 60 are reported.
   e. Outcome, ranked among the eligible stocks of the same sector and month: winner = top fifth, big winner = top
      tenth, loser = bottom fifth, big loser = bottom tenth. Absolute marks: permanent loss = forward return
      <= -50%; double = >= +100%.
   f. Net hit rate = share of counted first flags that are winners minus the share that are losers.
   g. Matched placebo: for each counted first flag one stock drawn at random from the eligible stocks of the same
      month, sector and size third (thirds of market value inside sector and month), the flagged stock excluded;
      5,000 sets, seed fixed in the code. One-sided p = (1 + number of sets at least as extreme) / 5,001.
      Factor-matched placebo: the cell also matches the fifth of the reference-book score inside sector and month; a
      cell with fewer than 5 other stocks drops the size third.
   h. Eras by formation month: 2010-14, 2015-19, 2020-22.
   i. Early flag: the stock's return over the 36 months to t was not in the top fifth of its sector and month (less
      than 36 months of history counts as early). The early placebo draws from early stocks only.
   j. Thesis date of a pod: the earliest document date of a verified rule in the buy part of its recipe.
3. **W (winners early).**
   W1, decisive: net hit rate at H = 36 above the matched placebo, Holm at 0.025 across the pods of a batch; in each
   era with at least 30 counted first flags the net hit rate is not below that era's placebo mean by more than one
   placebo standard deviation; at least 100 counted first flags (fewer: reported only).
   W2, label "beyond the reference book": the same against the factor-matched placebo, p <= 0.05.
   Label "finds them early": the same on early flags against the early placebo, p <= 0.05.
   Reported: H = 12 and 60; share of the 36-month excess over the sector earned in months 13-36 for winners caught;
   business winners (top fifth inside sector and month of the change in four-quarter operating profit from t to
   t+36 months over total assets at t), their net hit rate, and the share of business winners that were price
   winners; W1 on the flags after the thesis date where there are at least 30.
4. **R (risk).**
   R1: big-loser share of counted first flags below the matched placebo's, one-sided p <= 0.05. Permanent-loss share
   reported against the placebo.
   R2 (avoid rules; replaces R5's Exclusion test): on the first flags of the avoid rule (same definition, at least
   100): (a) net hit rate below the matched placebo, Holm at 0.025 across the avoid rules of a batch; (b) loser
   share at least 1.5 times the winner share; (c) big-winner share not above the placebo mean.
   R3 = R5 test 5, unchanged, on the broad form.
   Reported: the investor form under its stated sell rule against never selling and against R4's rank rule.
5. **C (construction).**
   Broad form = all passers under R4 and A8 2b-2f. C1 = R5 tests 1-4 on it.
   Investor form:
   a. N = the number of holdings the investor states (a range: its midpoint); else the median over quarters of the
      effective number of names (1 / sum of squared weights) from `eq_prof`, rounded; bounds 8 and 50. Stated and
      revealed N differing by more than a factor of two: two versions. Revealed N above 50 and none stated: the broad
      form is the investor form. Filers flagged quantitative book or firm-wide (A6): stated N only.
   b. Weights, two versions averaged: equal at purchase; and the revealed profile (median weight by rank over
      quarters, cut at N, rescaled to 1) given in the order of the recipe's ranking. Ranking = the investor's stated
      ranking; else the mean inside-sector percentile of the computable buy criteria.
   c. Reviews at quarter-ends, trades at that month-end close. Entry needs the whole recipe. A holding is sold when a
      stated sell rule fires, when it has failed the keep criteria at four quarter-ends in a row, or when it leaves
      the data. Keep criteria = entry criteria without the price rule unless the investor states a sale on price.
      Proceeds buy the best-ranked passer not held; with none, they sit in the equal-weight eligible universe.
   d. No rebalancing; at a review a position above the cap is cut to it and the excess spread over the others in
      proportion. Cap = the stated maximum position; else the 90th percentile over quarters of the investor's largest
      weight (`eq_prof`); else 2.5 / N. Costs as A8 2d. Start 2010-01 from the 2009-12 pass set.
   C2: 1,000 portfolios by rule c-d (equal weight at purchase) in which every purchase is drawn at random from the
   passers not held. "Concentration sound at N": at least 60% of the draws end 2025-12 ahead of the broad form's
   sector-matched universe (A8 2f) after costs, and at most 10% have a worst fall more than 15 points deeper than
   it. "The ranking helps": the ranked run ends above the 95th percentile of the draws. Reported: the curve at
   N = 5, 10, 20, 40 and all passers (median, 10th and 90th percentile of annual return and of the worst fall). N is
   set by rule a before the run, never from the curve.
6. **Classes** (replace R5's; a pod carries every label it earns).
   Winner list = W1, with check B (the pod's net hit rate minus its placebo mean above the 90th percentile of the
   control pods'; R5's rule of at least 20) and check C (first flags left out when a source investor of the pod held
   the stock at a weight of at least 1% at any quarter-end from 12 months before to 36 months after the flag; the
   excess over the placebo keeps its sign and at least half its size).
   Portfolio = C1, R3 and R5's checks B and C (= "Passed on history").
   Risk rule = R2: shown as a red flag for every company; an exclusion inside its own pod.
   Full pass = Winner list + Portfolio + R1.
   Tail sleeve = R5's Sleeve. Incubator = one descriptive run in which W1's placebo or test 4 is passed at 0.05
   unadjusted. Shelved = the rest. Core by the live rule only. Check A at the freeze: as R5 for Portfolio; for a
   Winner list the net hit rate outside the US above its placebo mean; a fail moves the pod to Incubator.
   Test families: W1 across the pods of a batch, test 1 across the pods of a batch, R2 across the avoid rules of a
   batch, each Holm at 0.025. The chance of at least one false label per batch is therefore up to 7.5% (was 2.5%).
7. **Budget** (amends R6). B1 and B2: at most 4 pods each; a slot is ONE logged run that prints W, R1, C1, C2 and
   R3 for all registered versions and both forms. At most 8 avoid rules per batch: those stated by the most roster
   investors (ties: the earlier thesis date). Added slot conditions: the pod's source investors passed gates G1-G8 of
   plan v0.5 (a pod none of whose source investors passed or could be measured on recall: one descriptive run); the
   number of counted first flags, known from levels before any return, is at least 100. Power note fixed here: under
   the placebo the standard deviation of the net hit rate is about sqrt(0.4 / n), so the strictest Holm level needs
   about 16 points at n = 100, 11 at 200, 8 at 400, 5 at 1,000.
8. **Reading** (desk 1; before a recipe is written).
   Material bar: M1 at least 3 documents of 5,000 words or more in the investor's own words; M2 a primary written
   source (letter, manual, book) or a document graded explicit 3 in the inventory; M3 a verified buy rule from
   quotes, and for price, avoid, sell and size a verified rule, a verified statement that none applies, or "none
   stated" (then from the 13F or a convention, tagged). A file below the bar is "thin": material is collected; the
   investor stays on the roster (R1 unchanged).
   Tags per claim: kind (rule / threshold / example / anecdote / principle / view / mistake), part (buy / price /
   avoid / sell / size / other), scope (all holdings / sector / period / one company), date said, period meant,
   computable (yes / by proxy / no), strength (always / usually / sometimes).
   Verification: a different model tags blind all claims tagged rule or threshold, a random 30% of the rest and 10
   planted items (5 anecdotes dressed as rules, 5 altered thresholds). Pass: agreement on rule-like or not >= 90%,
   on part >= 85%, on computable >= 85%, at least 9 of 10 planted items caught. A claim is a rule only if both
   readers say so; disputes go to a third reading on the quote alone. A file that fails is extracted again.
   Held-out document (investors with at least 3 documents of 5,000 words or more): the one with the smallest
   SHA-256 of investor name plus document id; the card writer never sees it or its claims. Pass: at least 70% of
   its verified rule-like claims match a rule on the card (same part and measure; a number within 20%, or the same
   direction where there is no number), and no open contradiction in the buy, price or sell part (closed = a dated
   change of view or a different scope, recorded on the card). After the test the document is merged. A fail =
   "file not complete": more material, then a new held-out draw.
9. **Recall and the kill criterion.**
   Purchases: the investor's conviction purchases (R2, either version) 2010-2025 whose stock was in the R3 universe
   at the quarter-end before the purchase quarter; for a filer flagged quantitative book, all new positions.
   Recall = share that passed the recipe's entry criteria at that quarter-end. Base rate = pass rate of the eligible
   stocks of the same quarter-end, sector and size third, weighted as the purchases. Lift = recall / base rate; 90%
   interval by bootstrap of quarters (2,000 draws). Decisive form of the recipe: thresholds tagged quote or
   convention only; thresholds revealed by purchases are measured on even-year purchases only and reported.
   Baselines: the same recipe on the pooled control investors' purchases; the reference-book screen (top fifth of
   the book score inside the sector) on this investor's purchases. A cross table of all recipes against all
   investors is reported.
   Pass: lift >= 2.0 with the interval's lower end above 1.25; recall >= 25%; lift above both baselines. Fewer than
   20 purchases in the universe: not measurable.
   Feedback to the recipe writer: recall, base rate, lift and, per criterion, the share of purchases it rejects
   (never names). One revision round per investor; every change cites a quote; old and new results are both logged.
   Kill criterion: after the pilot (Greenblatt, Terry Smith, Zlatev; a pilot investor who is not measurable or whose
   file stays thin is replaced by the next grade-A investor with a ready file, in the order Kantesaria, Hohn,
   Greenberg, Pilecki), the premise stands if at least 2 of the 3 pass. Otherwise no further recipe is written and
   the work switches to the analyst layer on the reference book and the owner panel.
10. **Names review** (when the reference-book LSEG inputs are loaded). Per pilot recipe the current pass list is
    shown beside the investor's latest 13F. Pass: at least 5 of the investor's 10 largest holdings in the universe
    meet the recipe's non-price criteria at the latest quarter-end. Read by the referee and the user, never by the
    recipe writer; a fail uses the same single revision round. It reads levels of current names: not a trial.
11. **Analyst layer and live placebo** (live only; fence 4 unchanged). Per new first flag of a registered pod, and
    per company the user adds: a dated memo with the investor's checklist answered from quoted sources, three
    scenarios, probabilities of winner / loser / permanent loss at H = 36, kill criteria as observable conditions,
    3 to 5 forecasts resolving within 12 months, a grade A / B / C. Append-only. Brier score by script against the
    base rates and against the pod's historical rates. Checkpoint at 200 resolved forecasts: the grade ranks
    candidates on the dashboard only if its Brier score beats the base rate. With every live first flag the script
    records 20 matched random names (2g); live hit rates are compared with theirs.
12. **Construction profile** (seal-exempt job 7 `construction_profile`, module `tools/equity/wrds/eq_prof.py`
    1.0.0, code sha256 10724979..., job `eq_prof_v1`). Reads only the stored panel `eq_conv_panel` (weights, new and
    add flags; no price, no return, no company data). Per roster and control investor: number of names, names of at
    least 1%, effective number of names, largest / top-5 / top-10 weight, 90th percentile of the largest weight,
    starting weight of new positions of at least 1%, holding time of such positions (Kaplan-Meier median and share
    still held after 1, 3 and 5 years; positions already held in the first filing left out), share of the book new
    per year, additions as a share of buys. One line of aggregates per investor comes back. Not a trial.
13. **T002** (to be written in `TRIAL_LOG.md` before it runs): the reference book's own scorecard (W1, early split,
    R1, C2 curve on its pass set = the top tenth by book score), as the bar every pod is shown against and as the
    plumbing test of the scorecard code. No verdict. Implementation choices are fixed in an addendum before the run.
14. **Not registered yet:** the recipes, pods and avoid rules; the analyst memo template; the dashboard; the
    scorecard code and its implementation choices; the non-US universe rule.

## Addendum A11 (2026-11-22): Terry Smith removed; pilot place; LSEG sector and consensus rules
1. **Roster.** Terry Smith is removed from the roster at the user's request (22 Nov: she does not like his style). His
   2021-25 record (scorecard 5.8% a year, 7.2 points behind the market) was known when this was decided, so the
   removal is logged as a choice made with sight of returns. His 13F stays in `eq_conv_panel` and in the frozen input
   of `eq_prof` (reported only; not used for any pod, threshold or check). His place stays open until the user picks a
   replacement; the candidate list is `ROSTER_2026-11-22.md`. A replacement enters only by R1 (record, material,
   screenability), each by a dated addendum. Roster: 20 investors, 10 open places.
2. **Pilot.** Kantesaria takes Smith's pilot place (A10 item 9, first in the order, file ready). Zlatev's file is
   unchanged (2 interviews, 23,100 words; the folder holds no newer Zlatev transcript): his reading waits for one
   more document of 5,000 words or more. Hohn, Greenberg and Pilecki, next in the A10 order, are not ready either.
3. **Sector of companies without a GICS code** (fixed before any LSEG return is computed): P01 gives today's GICS. For
   a company with no GICS code, the sector is the GICS sector most frequent among companies with a GICS code that share
   its Datastream GICS industry (GGISN, piece P19); else the one most frequent for its Datastream industry (INDM); else
   for its ICB industry (ICBIN); else for its SIC code (WC07021, first two digits). A mapping cell needs at least 5
   companies and a most frequent sector held by at least 60% of them; failing that, the next level is used; failing
   all, the company is not ranked and counted in the report. The excluded industries of A8 2a are applied to the
   assigned code at the deepest level it reaches; a company assigned only a sector is excluded when its sector is 60
   or its Datastream industry names a bank, an insurer, a real estate company or biotechnology. Both the share of
   universe members assigned this way and the result without them are reported.
4. **FY1 consensus at a month-end** (LSEG form of E01): the latest FY1 EPS mean dated on or before the month-end and
   at most 60 days before it; dates after 2026-12-31 are dropped as errors.

## Addendum A12 (2026-11-22): roster rule v3 (record)
Source: the user, 22 Nov: managers must be among the top investors over 2011-25 and also beat the market
consistently over the last five years. Registered BEFORE the record check below has run. It is decided with sight of
the scorecard (2026-11-18) and the leaderboard (2026-11-19), so it is a choice made knowing recent results; logged
as such. Replaces R1.1 (record); R1.2 (material) and R1.3 (screenability) stay.
1. **Measure.** 13F copy portfolio: at each quarter-end 2010-12..2025-09, all CRSP-matched holdings of the filer
   (first-version 13F), weighted by value at that quarter-end, earn their total return (CRSP msf_v2 mthret,
   delisting returns included) over the next quarter. Several filers of one investor: value-weighted. Investors
   whose registered record is a fund (R1, scorecard: Greenblatt, Pilecki, Nygren/Fitch, Stahl, Davis, Shaposhnik):
   the fund's monthly return (class TNA-weighted, after fees) decides; the 13F view is reported. Market = SPY total
   return over the same months. Data end 2025-12 (the 2026 months stay sealed).
2. **(a) Long record:** over 2011-01..2025-12, or from the first quarter of the investor's last unbroken run of
   eligible quarters if later (at least 20 quarters; under 40 flagged "short record"), the chained return ranks at
   or above 0.60 among all 13F filers eligible in every quarter of the same window (eligible = at least 5
   CRSP-matched holdings and 13F value at least $100m). Fund records are ranked against the same filers.
3. **(b) Recent:** 2021-01..2025-12 annualised return above SPY's, and above SPY in at least 3 of the 5 calendar
   years 2021-2025.
4. **Pass = (a) and (b).** Applies to every roster member and every candidate; a member who fails leaves the roster
   (logged), a candidate who passes may enter after R1.2-R1.3. The old route "leaderboard top 50" is dropped.
5. **Job:** seal-exempt job 8 `record_check`, module tools/equity/wrds/eq_rec.py 1.0.0 (code d91c44c9...), jobs
   eq_rec_pull_v1 then eq_rec_v1; prints per listed investor only. Listed: the 20 roster members, Terry Smith
   (reference), candidates Harnisch (Peconic), Singer (Elliott), Sosin (CAS), August (Mangrove), Hussman.
6. **Limits (reported with the result):** copying quarter-end weights ignores trades inside the quarter and shorts;
   fund returns are after fees while 13F returns are before; Hussman's fund hedges, his 13F shows only the long book;
   the 0.60 and "3 of 5" lines are noisy (one year can decide).
7. **Amendment after the v1 output (2026-11-22, eq_rec 1.0.1, job eq_rec_v2).** v1 (report `eq_rec_v1_report.txt`)
   applied the peer filter (at least 5 holdings) to the investor's own quarters too, which cut the windows of
   concentrated investors (CAS to 1 quarter; Valley Forge, TCI and Dorsey to 2017 onward). Changed AFTER seeing v1:
   an investor's own quarter needs at least 1 CRSP-matched holding with a return and 13F value at least $100m; the
   peer group (at least 5 holdings) is unchanged. Mangrove's filer (13534) was not found by name in v1; its number is
   now listed. Both reports are kept; v2 decides. Fund records with missing months (Shaposhnik's fund, Greenblatt's
   fund before 2012-10) are unchanged.
8. **Margin and user picks (2026-11-23, user, after seeing v2).** (b) is relaxed: the 2021-25 annualised return may
   trail SPY by up to 1 point a year; "ahead in at least 3 of 5 calendar years" stays. This brings back Kantesaria
   (-0.2) and Li Lu (-0.0). The user also keeps Hohn (2 of 5 years), Sosin (2021-25 10.2%) and Pilecki (fund record
   includes years before his tenure) by her own choice, outside the rule; logged as user picks. Roster: 15. The same
   rule with the margin is run over every 13F filer (eq_rec 1.1.0 `scan`, job eq_rec_scan_v1) to fill open places;
   listed are filers with 13F value at least $500m and 5-200 CRSP holdings at 2025-09. A listed filer still needs
   R1.2 (material) and R1.3 (screenability) before it joins.

## Addendum A13 (2026-11-27): pilot reading of Kantesaria; first blind check failed; spec v1.1
1. **Material (G1).** Record `pilot/G1_MATERIAL_2026-11-27.md`: Kantesaria passes M1 and M2 (5 documents, K065
   explicit 3); held-out document K174 by the A10 hash rule. Sosin passes M1 but fails M2 (highest grade 2, no
   written source; one 2026 document has an unnamed guest and is not counted). Only Kantesaria is ready; the kill
   criterion still needs 3 pilot investors (replacements in the A10 order as files become ready).
2. **Extraction v1 and the first blind check (G3).** Spec `pilot/CLAIM_SPEC_v1.md`; five Sonnet readers (one per
   document, private folders) gave 423 claims, all quotes found verbatim by `pilot/tools/check_quotes.py`. Set by
   `make_verify_set.py` (seed 20261127): 201 rule-like + 30% of the rest + 10 planted = 276 items; key committed
   (ce25e60, sha256 af5505c6...) before the verifier (Opus) tagged blind. Result `pilot/verify/SCORE_v1.md`: FAIL
   (rule-like 85.7% vs 90; part 87.2%; computable 76.7% vs 85; planted 8 of 10 vs 9). Cause read from the
   disagreements: the first reader tagged general beliefs as rules (32 of 38 disputes go rule -> not rule) and
   tagged process facts (team size, watch list) as computable; two planted "anecdotes" were an example with a
   frequency and a research habit, which the verifier read as rules.
3. **Changes made AFTER seeing the v1 disagreements (logged as such).** Spec v1.1 (`pilot/CLAIM_SPEC_v1.1.md`):
   definitions of rule vs principle, threshold (a typical range counts; firmness goes to strength), anecdote,
   computable (company or stock measures only; portfolio rules are `no`), and `value` = every number describing his
   practice. Plants v1.1: anecdotes only, thresholds with a stated value only, every number altered. Scoring v1.1 is
   stricter for altered thresholds (caught only if the verifier gives a value with none of the altered numbers);
   the bars are unchanged. v1 rescored under the v1.1 rule: 5 of 10 (still FAIL; the v1 file keeps its v1 score).
4. **Re-extraction (registered consequence "a file that fails is extracted again").** Fresh Sonnet readers with spec
   v1.1, no sight of the v1 claims; a fresh Opus verifier with a new seed (20261128) and no sight of v1 tags. If
   v1.1 fails too, the reading of this file stops and the result is reported; no third spec version for this file
   without the user.
5. **Result v1.1 (2026-11-27): FAIL** (`pilot/verify_v1.1/SCORE_v1.1.md`; key 1e2ad468... committed 088aca3 before
   the tags). Rule-like 85.5% (bar 90), part 87.9%, computable 82.6% (bar 85), planted 10 of 10. 38 of 41 disputes
   are first reader "rule" vs verifier "principle" (advice phrased "you should" or a self-description with no named
   decision); computable splits are mostly no/yes vs proxy. Per item 4 the reading of this file stops here; the
   next step is the user's choice. Nothing downstream (card, recipe, recall) has been built.
6. **User decision after v1.1 (2026-11-27).** The user chose to keep agreed rules: the 90% / 85% agreement bars are
   reported, not stops, for this file (the planted test, 10 of 10, stays decisive). A claim is a rule only if both
   readers call it rule-like, or a third reader on the quote alone does where they split (the A10 rule). Where the two
   readers split on computable, the weaker tag is used (no < proxy < yes). Claims the first reader did not tag
   rule-like cannot become rules. Logged as a change of the A10 gate, made after seeing both results.
7. **Card and held-out test (2026-11-27).** Card v1 (`pilot/card/CARD_v1.md`, Opus, four documents, 72 rules: buy 21,
   price 9, avoid 14, sell 7, size 5, process 16; 4 open internal contradictions, C3 entry discount, C7 idea counts,
   C9 sizing, C14 healthcare breadth). Held-out test (`pilot/heldout/heldout_result.json`, fresh Opus): 6 of 8 K174
   rules matched (75%, bar 70%) but 3 OPEN contradictions in the buy part, all from the FICO case: he bought on a
   2018 pricing change and on a growth change others had missed, while card rules RB10 and RB6 require a long record
   ("not a sudden change", "not a predicted step change"). Result: FAIL = "file not complete" (A10): more material,
   then a new held-out draw. K174 is not merged yet. The finding itself is kept: the card overstates "long record";
   he also buys an inflection in pricing or growth at a business that already dominates.
8. **User direction 2026-11-27: "keep going with the investors with readily available materials, don't stop".**
   Read as: (a) Kantesaria continues past the held-out FAIL to card v1.1 (K174 merged; the FICO cases recorded as a
   scope rule: an inflection in pricing or growth at an already dominant business) and on to recipe and recall; every
   later result carries the label "held-out failed". (b) Every roster investor with own-words documents of 5,000+
   words in the library is read now through the same gates, without waiting for the material bar; a file below the
   bar carries the label "thin" and cannot be classed above Incubator until it reaches the bar. Batch 2 (sources in
   `pilot/batch2/docs.json`): Hohn 2 documents (one file was a duplicate of the same talk and is dropped), Stahl 3,
   Druckenmiller 6, Sosin 3 (the 2026 unnamed-guest file stays out), Zlatev 2, Pilecki 2, Nygren/Fitch 2 (TIP524 only
   quotes Nygren and is dropped), Li Lu 2. Held-out documents by the A10 hash rule (name + batch id) where there are 3
   or more: Stahl STA2, Druckenmiller DRU2, Sosin SOS1. Gate G3 per A13 item 6 (agreement reported; planted decisive;
   agreed rules + third reading). Spec v1.1 wording made investor-neutral ("his fund does X"; no change of meaning).
9. **Planted items when a file is short (2026-11-27, before any batch-2 verifier tags were read).** If a file has fewer
   than 5 anecdotes outside the sample (or fewer than 5 thresholds with a stated value), as many as exist are planted;
   the bar "9 of 10" becomes "all but one". Hohn's set has 6 plants (1 anecdote + 5 thresholds).
10. **Scorer fix after seeing the Nygren result (2026-11-27, logged as such).** The altered-threshold check read only
    digits, so a verifier who copied the true number in words ("seven year", "about four", "about half") counted as a
    miss. Nygren scored 6 of 10 (FAIL); three of the four misses were this defect (the verifier gave the true value in
    words). score_verify now reads number words too. Rescored with the fixed scorer (files SCORE_scorer1.2.md, the
    first scores kept): Zlatev 10/10, Pilecki 10/10, Hohn 6/6 (was 5/6), Stahl 6/7, Li Lu 5/5, Nygren 9/10 (pass),
    Kantesaria v1.1 10/10. No file moves from pass to fail. Nygren's remaining miss (V101, an anecdote read as a rule)
    stands.
11. **Second scorer fix after seeing Druckenmiller (2026-11-27, logged as such).** The number-word reader of item 10
    read "two or three hundred" as 2, 3 and 100, and 100 was one of the altered numbers, so a true value counted as a
    miss (Druckenmiller 8 of 10). It now reads "three hundred" as 300. Rescored all (SCORE_scorer1.3.md): Zlatev 10/10,
    Pilecki 10/10, Hohn 6/6, Stahl 6/7, Li Lu 5/5, Nygren 9/10, Druckenmiller 9/10, Sosin 6/6, Kantesaria 10/10: every
    file passes the planted test. The remaining misses are anecdotes read as rules (Stahl 1, Nygren V101,
    Druckenmiller V120 "I'm just not playing anything as aggressively as I used to", arguably a sizing rule).
12. **Stahl held-out test (2026-11-27).** `pilot/batch2/STA/heldout/heldout_result.json`: 4 of 13 STA2 rules matched
    (31%, bar 70%), 0 open contradictions -> FAIL ("file not complete"). The card (2 documents) had no size rule, no
    general sell trigger and no private-company rule; STA2 states all three. Per item 8 the card continues as v1.1 with
    STA2 merged, labelled "held-out failed"; the file is also thin (no written source).
