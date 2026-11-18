# Equity pod shop, Stage 0: registration of the investor scorecard, the tier rule and the "follow the best managers" signal

Status: REGISTERED v2 (2026-11-18), after the independent review of v0.2 (`EQUITY_POD_SHOP_DESIGN_v0.2_review.md`, Part 1).
It becomes binding when the line REGISTERED below carries a commit id, and that happens before the scorecard job
computes any return. Plan: `EQUITY_POD_SHOP_PLAN_v0.3.md` sections 5, 6, 8.2 and 11. Every number here is fixed by
this file. A later change is a new version of this file with its own date, and the old result is kept.

REGISTERED: (not yet)

## 1. Order of work, and what each part may see
| Phase | What | May read | Comes back |
|---|---|---|---|
| A. Match (job `eq_match_v1`) | Candidate 13F filers and CRSP funds for each library investor | Names, ids, dates, number of quarters and positions, size. No return | Candidate lists |
| A2. Freeze (`inventory/frozen_investors.csv`) | For each investor: filer id or fund, the years the investor ran it, grade, primary style, explicitness. Set by an agent that sees the candidate lists and the notes, and no return; a tenth checked by a second agent | as phase A | The frozen file, committed with this registration |
| B. Scorecard (seal-exempt job, plan 5.4) | Copy portfolios, fund returns, ranks, persistence, tier rule | Holdings and returns of US-listed securities and CRSP funds, 2010-06 to the seal end | Section 8 only |

The scorecard output is read only by the user and the session that runs Stage 0. Sessions and agents that write
claims, cards, charters or specs do not open it.

## 2. Data (WRDS table check, jobs `eq_tables_v1` and `eq_tables_v2`, 2026-11-17)
- 13F holdings: `tfn.s34` (LSEG). It carries the quarter and a file date, not the SEC filing date. The SEC-based
  tables (`wrdssec`) are not in the subscription. So only the first version of each quarter's holdings is used (rows
  with file date equal to report date) and amendments are ignored.
- Stocks: `crsp.msf_v2` (monthly total return with delisting returns; ends 2025-12), `crsp.stocknames_v2` (match on
  the 8-character CUSIP valid at the quarter-end).
- Characteristics for peer groups: size from CRSP; book-to-market from `wrdsapps_finratio.firm_ratio` (as of its
  public date); momentum from CRSP.
- Factors: `ff.fivefactors_monthly` (market, size, value, profitability, investment, momentum, T-bill).
- Funds: `crsp.monthly_tna_ret_nav`, `crsp.fund_hdr`, `crsp.fund_style`.
- **Seal end: 2025-12** (the last CRSP stock month). Months after it are never holdout.
- Data facts checked before registration (`eq_precheck_v1`, counts only, 2026-11-18): `msf_v2` monthly return
  already includes the delisting return (every one of 5,402 delistings in 2001-10 has a return in its delisting
  month), so no separate delisting adjustment is made; first versions exist for all but 21 manager-quarters of
  2010-25; Fama-French factors are in decimals; 958 of 311,949 firm_ratio permno-dates in 2005-10 carry two different
  book-to-market values and get none that year (reading 8).

## 3. The copy portfolio of a 13F filer
1. **Filing.** First version of the holdings for each manager and quarter-end (section 2).
2. **Positions.** Rows with positive shares whose CUSIP matches a CRSP security at the quarter-end. Holdings without
   a match are left out and the weights rescaled. The share of filed value used is a column. Option rows are not in
   the file.
3. **Weights.** Shares times the CRSP price at the quarter-end.
4. **Timing.** Holdings for quarter-end Q enter at the close of the month in which the 45-day deadline falls and are
   held for three months, buy and hold (the 31 March holdings are held June, July, August). Monthly CRSP total
   returns, delisting returns included. A position whose return is missing in a month keeps its weight and earns
   zero that month; the share of weight affected is a column.
5. **Missed quarters and stopping.** If a quarter's filing is missing, the last filed portfolio is held three more
   months. If the following quarter is missing too, the spell ends there and no return is filled in; a later
   filing starts a new spell. This is decided from what was public at the time: a copier cannot know whether a
   filer has stopped or only skipped a quarter.
6. **Rank group for a window:** filers whose median number of matched positions over the window's filings is 5 to
   150 and whose median matched value is at least $100M.
7. **Variants** (reported, not ranked): the ten largest positions, weights rescaled; new positions only (securities
   not in the filer's previous quarter filing), weights rescaled.

## 4. Columns, windows, ranks
**Windows:** 2011-01 to 2015-12, 2016-01 to 2020-12, 2021-01 to 2025-12, and 2011-01 to 2025-12. No month before
2011-01 is computed. For a library investor the months are cut to the years the investor ran the book (frozen file).
**A window has a result** if it holds at least 36 months of returns.

1. **Six-factor alpha (the ranked result),** percent a year, with its t-value: regression of the monthly return
   minus the T-bill rate on the market, size, value, profitability, investment and momentum factors; Newey-West
   errors, 3 lags.
2. Return, percent a year (geometric); return minus the CRSP value-weighted market.
3. **Peer-adjusted return** (reported), percent a year: each common stock's return minus the value-weighted return of
   its peer group, weighted by the portfolio. Peer groups (after Daniel, Grinblatt, Titman and Wermers): each June,
   size fifths on NYSE breakpoints, then book-to-market fifths inside each size group, then fifths of the return
   over the twelve months to May inside each of those; 125 groups, held July to June. Holdings without a peer group
   (no book value, ADRs, funds) are left out and the weights rescaled; the share of value used is a column.
4. Worst fall from a peak (monthly). Share of calendar years in which the return beat the CRSP market.
5. Median number of positions; median weight of the ten largest; turnover a year (half the sum of absolute weight
   changes between consecutive filings, times four).
6. Peer-adjusted return of the two variants.

**Ranks.** For each window, the filer's six-factor alpha as a share of the rank group from 0 (worst) to 1 (best);
ties take the average rank.

## 5. Public funds
- Monthly net return from CRSP, share classes of one portfolio combined by assets at the start of the month.
- Rank group: US domestic equity funds in CRSP (objective code starting "ED"), index funds and exchange-traded index
  funds left out, mean assets of at least $15M, with a result in the window. The ranked result is the six-factor
  alpha of section 4, ranked among funds only.
- Funds outside CRSP (for example UK funds) are reported if the LSEG probe returns them. They enter neither the tier
  rule nor the persistence check.
- An investor with both a CRSP fund and a 13F record is ranked on the fund (real returns after fees).

## 6. Record grades (frozen in phase A2, before any return)
| Grade | Rule |
|---|---|
| F | A CRSP fund in the rank group of section 5 that the investor managed for at least 60 months after 2010 |
| A | Not F. Matched 13F filer with at least 20 quarters after 2010, median positions 5 to 150, median value at least $100M; primary style not long_short, macro_multi_asset, credit_distressed, quant_systematic, private_venture or index_allocation; region us or global |
| B | Not F. Matched 13F filer with at least 20 quarters after 2010, median positions 5 to 150, median value at least $100M; primary style long_short, or region europe, asia, emerging or other |
| C | Matched 13F filer that is not A or B (too many or too few positions, too small, too few quarters, or a style in the list under A) |
| N | No match |

A person coded as allocator at E0.1 (chooses managers or asset classes) is graded C if a filer is matched and N
otherwise: the filing is not a stock-picking record. Matching follows `E0.4_MATCH_SPEC.md`; the blind second
matcher gave the same filer for 16 of 19 investors and the same funds for 17 of 19 (`inventory/match_agreement.md`).
The first matcher's answer stands. Two rules are applied by script after the matching
(`tools/equity/freeze_investors.py`): (i) where every matched fund names the investor in its manager field with a
"manager since" date after 2011-01, the record starts at the earliest of those dates; (ii) investors with the very
same record (same filer numbers or same funds) share one place: the one with more own-words documents holds it,
and the others join that investor's tier without taking a place (`shares_record_with`). A co-manager whose own
start date the data do not show (one case, a fund co-managed with its lead manager) keeps the fund's full period;
that record is the fund's, not proof of the person's own tenure.

"Primary style": the style code given most often across the investor's own-words documents (kind `investor_talk`)
in the E0.1 inventory, ties by the order of the style list in the spec; none coded = "none". "Region": the most
frequent region code in those documents. "Explicitness": the highest `explicit` value in those documents, then the
mean. E0.1 agreement on the blind recode was 94% for style (any overlap), 88% for explicitness (98% within one step)
and 70% for region; all three are used as coded.

## 7. Tier rule (plan 5.3 with its definitions)
1. **Eligible for the places by record:** grade A, B or F, at least one own-words document, and 60 months of record
   after 2010.
2. **Score:** the mean of the rank shares that exist: (i) window 2011-25; (ii) window 2021-25; (iii) the share of
   the blocks 2011-15, 2016-20 and 2021-25 (those with 36 months) in which the six-factor alpha is positive, turned
   into a rank share within the investor's record kind (13F filers, funds).
3. **Tier A by record: 30 investors,** highest score first, at most eight per primary style; when the cap binds the
   next ranked investor of another style takes the place. Ties by number of own-words documents, then investor id.
   If fewer than 30 are eligible the places stay empty.
4. **Tier A by explicit criteria: exactly 10** (fewer only if fewer are eligible), from people coded investor with
   `ran_money` = yes who are not already chosen: highest explicitness, then mean explicitness, then number of
   own-words documents, then investor id.
5. **Control: 10,** drawn with seed 20261117 (Python `random.Random(seed).sample`) from the eligible investors of
   point 1 outside tier A, sorted by investor id.
6. **Tier B:** everyone else. **Foundation list:** the 50 documents with the highest `technique_depth`, ties by
   number of technique areas, then by words, then by document number.
7. The persistence result does not change this rule.

## 8. What comes back from the scorecard (WRDS rule: no data rows)
- One row per matched library investor: grade, record kind, months, and for each window the columns of section 4
  (statistics only where the window has 60 months or the whole record has 60 months; otherwise rank shares only).
- The tier lists of section 7, computed in the same job.
- The 25 best-scored filers and the 10 best-scored funds for which the library has no document: name and rank
  share only.
- Persistence (section 9) and counts: filers and funds in each rank group, coverage shares.
- Nothing else. No holdings, no return series, no stock names, and no average by style, sector or factor.

## 9. Persistence check
Between 2011-15 and 2016-20, and between 2016-20 and 2021-25, among filers in the rank group in the first block
with 36 months there: the rank correlation of the six-factor alpha with the second block (filers with 36 months in
both); and the table of first-block fifth against second-block fifth with an extra column "stopped filing or under
36 months". The same for CRSP funds, apart.

## 10. "Follow the best managers" signal (plan section 6)
- Each month t: every filer whose latest public filing is in the rank group form of 3.6 (5 to 150 positions, at
  least $100M) and that has at least 36 months of copy-portfolio returns ending at t.
- Rank on the t-value of the six-factor alpha over the 60 months ending at t (or the months it has).
- The 20 highest are "followed". Version 1: a stock's score is the number of followed filers for whom it is a new
  position in their latest public filing or the one before, divided by 20. Version 2: the sum over followed filers
  of the stock's weight in their latest public filing, divided by 20. The pod averages the two.
- Its US result from 2011 is reported only; it has no version outside the US; it is judged on the design era
  (13F data start in 1980 and the rule needs three years of history) and the live record.
- **What the author had seen when this was written** (review P6): the triage tests on WRDS 2008-24
  (`docs/research/triage_wrds/RESULTS.md`: no test passed; the owner cells loaded on the profitability factor) and
  the biotech re-run 2020-26 (the "top performer" subset of 23 buy calls carried the buy result). The settings
  above (20 managers, 60 months, t-value of a six-factor alpha, new positions) were not copied from the triage
  rules, whose "top performer" definition was not consulted. No result of a 13F-following rule on 2011-25 had been
  seen. The scorecard has not run.

## 11. Checks before the scorecard runs
- The code is built by one agent and read by another that did not build it.
- A planted-error test on invented data: a look-ahead of one quarter in the holdings, a dropped delisting return,
  a peer group built with the same month's size, a filer that stops filing kept with zero returns, a doubled share
  class, a rank computed across record kinds. The code check must catch each one. Catch rate on record.
- The job passes the seal checker as one of the two seal-exempt jobs, and the run is logged in `SEAL_LOG.md` with
  the code hash and the lock id.

## 12. Exact readings (fixed with this registration)
Where the sections above left room, the reading is the one written in `SCORECARD_BUILD_NOTE.md` section 3, items 1
to 22, which the code implements. They are part of this registration. The ones that matter most:
- A library investor's alpha over its frozen months takes the place of its own filers or funds in the window's rank
  group; the rank share is (number below + half the number equal) / (group size - 1).
- Quarter-end weights are the weights at entry. Section 3.5 replaces reading 4 of the build note: the three extra
  months after a missed quarter are held whether or not the filer files again.
- An investor's several funds are one record, combined by assets at the previous month-end.
- The frozen file lists every filer and fund matched to a library investor (`known_mgrnos`, `known_fundnos`); all
  of them are left out of the lists of best-scored filers and funds without a document.
- Any CRSP security with a price at the quarter-end counts as matched (funds and ADRs included); peer groups cover
  common shares on NYSE, NYSE American and Nasdaq only.
- The market is the Fama-French market return (excess return plus T-bill).
- Statistics are printed for a window if the window or the whole 2011-25 record has 60 months; otherwise rank
  shares only.
- An investor with no rank share takes no place by record. If ten or fewer are eligible for control, all are taken.
- The frozen file carries the role coded at E0.1; only role investor with `ran_money` = yes can take an explicit
  place.
- Equity jobs use no pull or export steps outside the reader. The scorecard runs under names `eq_scorecard_v<n>`;
  a re-run on the same inputs fixes a logged bug only.
- An investor that shares a record (`shares_record_with`) can still take an explicit place on its own documents.
  If the holder of a shared record is not eligible, no one takes a place by record on it.
- A change of `PULL_VERSION` means deleting every `eq_sc_*` data set on WRDS before the next pull.
- Code reviewed: three independent reads (`SCORECARD_CODE_CHECK.md`: FIX FIRST 5, FIX FIRST 2, RUN), a hidden-error
  test (6 of 6 planted defects found, no false alarm; `scorecard_check/`), smoke test with 6 of 6 registered and 13
  of 14 extra planted errors caught. Module code sha256 f7f542646da4da43a96cbfdfe8e817247ccb519b7872519dab299188f6bb5db8
  (input block excluded); input sha256 c77e38e77851ee3124548ca374ec78e0414cbde50d5e6f536c04380242ab0b6f (241 investors:
  13F 77, fund 13, none 151; 635 documents); lock id e680ca33c77ec51ed50372ec66e5733001cd4867adf1e692f88a4e2645015099.
