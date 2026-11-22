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
