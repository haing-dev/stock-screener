# Equity pod shop, Stage 0: registration of the investor scorecard, the tier rule and the "follow the best managers" signal

Status: DRAFT (2026-11-17). It becomes binding when it is committed with the line "REGISTERED" below filled in, and
that happens before the scorecard job reads any return from 2011 on. Plan: `EQUITY_POD_SHOP_PLAN_v0.3.md` sections
5, 6, 8.2 and 11. Every number here is fixed by this file; nothing in it may be changed after the scorecard has run.
A later change is a new version of this file with its own date, and the old result is kept.

REGISTERED: (not yet)

## 1. What this job may read, and what comes back
- The scorecard is a registered descriptive job (plan 5.4): its output form is fixed here and checked before it
  runs, it describes records, it sets the reading order through the tier rule in section 4, and it judges no
  strategy.
- It runs on WRDS Cloud. It may read holdings and returns of US-listed securities and of mutual funds from 2010-06
  to the latest month. It is logged in `SEAL_LOG.md` as an opening of the seal on the years from 2011.
- What comes back: one row of statistics per library investor that could be matched, distribution tables for all
  filers, the persistence table, and the names of up to 30 top-ranked filers for whom the library has no document.
  No holdings, no return series, no stock names.
- Who may open the output: the session that runs Stage 0 and the user. Sessions and agents that write claims,
  cards, charters or specs do not open it (plan section 4).

## 2. The copy portfolio of a 13F filer (grades A, B, C)
Source tables are fixed in section 7 after the WRDS table check.
1. **Filing.** For each manager and quarter-end, the first version of the holdings filed for that quarter-end. Later
   amendments are not used. (The WRDS file has no filing date for amendments; using first versions only is the
   conservative reading of plan 5.2.)
2. **Positions.** Long positions in securities that match a CRSP security at the quarter-end. Option rows are not in
   the file. The share of filed value that matches CRSP is reported.
3. **Weights.** Value at the quarter-end (shares times the CRSP price at the quarter-end), as filed.
4. **Timing.** A filing for quarter-end Q is public by day 45. The copy buys at the end of the second month after Q
   and holds for three months at buy-and-hold weights (example: the 31 March filing is held June, July, August).
   Monthly CRSP total returns, delisting returns included. A position without a return in a month earns zero that
   month and is counted in a "missing return" share.
5. **Which filer-quarters count.** 10 to 150 matched positions and at least $100M of matched value at that
   quarter-end. A month counts for a filer only if its holding quarter passes this screen.
6. **Variants**, same timing: (a) all positions; (b) the ten largest, weights rescaled; (c) new positions only:
   securities not in the filer's previous quarter filing, weights rescaled, held three months.

## 3. Columns, windows and ranks
**Windows:** 2011-01 to 2015-12, 2016-01 to 2020-12, 2021-01 to 2025-12, and 2011-01 to 2025-12. No month before
2011-01 is computed.

**A filer has a result for a five-year window** if it has at least 54 of the 60 months. For 2011-25 it needs at
least 60 months in total; statistics use the months it has.

**Columns per window** (variant (a) unless stated):
1. Return, percent a year (geometric).
2. Return minus the CRSP value-weighted market, percent a year.
3. **Style-adjusted return**, percent a year, and its t-value. For each common stock and month: its return minus
   the value-weighted return of its peer group. Peer groups are formed every month from the characteristics known at
   the end of the previous month: size (3 groups, NYSE breakpoints), book-to-market (3), operating profitability (3)
   and return over months t-12 to t-2 (3), independent sorts, 81 groups. A group with fewer than 5 stocks is merged
   into its size-by-value group. The portfolio figure is the weighted sum over its common stocks with weights
   rescaled; the share of value outside common stocks or without characteristics is reported.
4. Six-factor alpha, percent a year, and its t-value: regression of the monthly return over the T-bill rate on the
   market, size, value, profitability, investment and momentum factors (Fama-French), Newey-West errors with 3 lags.
5. Worst fall from a peak (monthly data).
6. Share of calendar years with a positive style-adjusted return.
7. Average number of positions; weight of the ten largest; turnover a year (half the sum of absolute weight changes
   between consecutive filings, times four).
8. Style-adjusted return of variants (b) and (c).

**Ranks.** For every window and for columns 3 and 4: the filer's place among all filers with a result in that
window, as a share from 0 (worst) to 1 (best).

## 4. Public funds (grade F)
- Monthly net return of the fund from the CRSP mutual fund file, share classes combined by assets. Funds outside
  CRSP are left for the LSEG probe and get no rank in this version.
- Style-adjusted result of a fund = its six-factor alpha (column 4). Rank among US domestic equity funds in CRSP
  (objective code starting "ED", index funds and funds under $15M left out) with a result in that window.
- A fund is used for an investor only if the investor is named in the library as its manager for most of the window.

## 5. Record grades (plan 5.1), by rule
| Grade | Rule |
|---|---|
| A | Matched 13F filer; passes the screen of 2.5 in at least 20 quarters after 2010; inventory style is not long_short, macro_multi_asset, credit_distressed, quant_systematic, private_venture or index_allocation; inventory region is us or global |
| B | Matched 13F filer that passes the screen in at least 20 quarters after 2010, with inventory style long_short, or inventory region europe, asia, emerging or other |
| C | Matched 13F filer that fails the screen (too many or too few positions, too small, too few quarters), or whose inventory style is macro_multi_asset, credit_distressed, quant_systematic, private_venture or index_allocation |
| F | No usable 13F record (not A or B), and a public fund matched under section 4 with at least 60 months after 2010 |
| N | None of the above |

"Inventory style" and "region" are the most frequent codes for that investor in the E0.1 inventory.

## 6. Persistence check (all filers, and all funds)
Between 2011-15 and 2016-20, and between 2016-20 and 2021-25, for filers with a result in both blocks: the rank
correlation of the style-adjusted return; the share of the top fifth that is again in the top fifth, and above the
middle; the same for filers with 10 to 40 positions. The same three numbers for funds, on the six-factor alpha.
The result is reported. It does not change the tier rule (plan 13).

## 7. Tier rule (plan 5.3)
1. **Score.** For each investor with grade A, B or F and at least 60 months after 2010: the average of three rank
   shares from section 3 (for F: section 4): (i) style-adjusted result 2011-25; (ii) the same for 2021-25; (iii) the
   share of the blocks 2011-15, 2016-20, 2021-25 with a positive style-adjusted result, turned into a rank share
   among the same group. A missing item is left out of the average. An investor with both a 13F record and a fund
   is scored on the 13F record if graded A or B.
2. **Tier A by record: 30 investors.** Highest score first, at most eight per inventory style (the investor's most
   frequent style code). Ties go to the investor with more documents.
3. **Tier A by explicit criteria: 10 investors**, whatever their grade, from those not yet chosen: highest
   `explicit_max` in the inventory, then highest `explicit_mean`, then more documents. Only people coded as
   investor with `ran_money` = yes or unclear.
4. **Control: 10 investors**, drawn at random (seed 20261117) from grades A, B and F outside tier A.
5. **Tier B:** everyone else. **Foundation list:** the 50 documents with the highest `technique_depth`, ties by
   number of technique areas, then by words.
6. If fewer than 30 investors have a score, the unfilled places are left empty. They are not filled by another rule.

The league table shown to the user lists every scored investor by inventory style with the 2021-25 column first
(the five years asked for), then the other columns, the grade, and tier.

## 8. "Follow the best managers" signal (plan section 6), registered before the scorecard runs
- Each month t, take every filer that passes the screen of 2.5 in its latest public filing and has at least 36
  months of copy-portfolio history ending at t.
- Rank filers on the t-value of the style-adjusted return over the 60 months ending at t (or the months they have).
- The 20 highest are "followed". The pod's score for a stock is the number of followed filers for whom the stock is
  a new position in their latest public filing or the one before, divided by 20. Stocks nobody bought score zero.
- Two versions, averaged: new positions only (above), and all positions of followed filers weighted as filed.
- Its US result from 2011 is reported only. It is judged on the design era and the live record (plan section 6).

## 9. Checks before the run
- The code is built by one agent and read by another that did not build it.
- A planted-error test on invented data: a look-ahead of one quarter, a dropped delisting return, a peer group
  built with the current month's size, a filer that stops filing, a doubled share class. The code check must catch
  each one. Catch rate on record.
- The run is logged in `SEAL_LOG.md` with the code version and the lock id.
