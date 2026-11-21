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
