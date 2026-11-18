# Investor scorecard: build note (2026-11-18)

Code built to the binding spec `STAGE0_REGISTRATION.md` sections 2-9 and 11. Nothing has run on WRDS yet. The
spec gaps (section 3) need an entry in the spec before REGISTERED gets a commit id.

## 1. Files
| File | What it is |
|---|---|
| `tools/equity/wrds/eq_scorecard.py` | The WRDS lib module (seal-exempt). The frozen investor table and the document list sit between the `FROZEN INPUT` markers |
| `tools/equity/make_scorecard_job.py` | Reads `inventory/frozen_investors.csv` and `inventory/inventory.csv` (with word counts), rewrites only the input block, and writes `tools/wrdsq/jobs/eq_scorecard_v1.json`. Prints the code hash and the input hash |
| `tools/equity/wrds/eq_reader.py` | The seal reader. Every equity table is declared with its date column and region. A read that touches a sealed month is refused unless `exempt=True` is passed |
| `tools/equity/seal_check.py` | The pre-send checker. Prints PASS or REFUSED and the lock id |
| `tools/equity/seal_exempt.json` | The exempt list: the scorecard entry, `job_pattern eq_scorecard_v\d+[a-z]?` plus the code SHA-256 |
| `tests/eq_scorecard_smoke.py` | Invented data: 25 scorecard checks, 13 seal checks and the 6 planted-error mutations |

## 2. Functions (module)
| Function | Does |
|---|---|
| `pull_base` | Pulls `tfn.s34names`, the `stocknames_v2` CUSIP map, `ff.fivefactors_monthly`, and `firm_ratio` book-to-market for public dates in Jan-Jun 2010-25. Also pulls `fund_hdr` and `fund_style` |
| `pull_crsp` | Pulls `crsp.msf_v2`, all securities, 2009-06..2025-12, one data set per year |
| `pull_agg` | Runs one SQL aggregate per year: matched positions, matched value and filed value per filer and quarter (first versions, 2010-06..2025-12) |
| `candidates` / `pull_hold` | Keeps the filers that could be in a rank group of any window, using a loose filter: median positions 3-200, median value at least $75M, at least 30 months. Library filers are always kept. Pulls their raw holdings rows per year. The exact rank group is computed later in `build` |
| `pull_funds` | Pulls CRSP monthly returns and assets of classes that ever had an `ED` code, plus every share class of the library funds |
| `Panel`, `Peers` | Build the CRSP arrays and the DGTW groups, formed each June and held July-June, with value-weighted group returns |
| `_positions` | Matches holdings to CRSP: CUSIP valid at the quarter-end, CRSP price at the quarter-end. Computes filed and used value per filing |
| `_schedule`, `_hold`, `_books` | Handle holding months, buy and hold, the spell rules and the two variants. Build books for all filers and for library investors |
| `_book_windows`, `_fund_windows`, `_stats`, `ols_nw` | Compute window statistics, the rank-group tests and the six-factor Newey-West alpha |
| `_results`, `_tiers`, `_persist` | Compute rank shares, scores, tiers, best-scored lists, persistence and counts |
| `build` / `report` | `build` saves the report lines as data set `eq_sc_report`. `report` prints one part of under 55,000 characters per python step |

## 3. Spec gaps: the reading taken, and proposed spec text
The code implements each proposed text exactly as written below.

1. **Rank share of a library investor.** Proposed text: "A library investor's alpha over its frozen months is placed in the window's rank group in place of its own filers (or fund portfolios). The share is (number below + half the number equal) / (group size − 1). It exists only if one of its filers (funds) is a member of that window's rank group."
2. **The window's filings.** Proposed text: "A window's filings are the filings whose holding months, cut to the frozen months, fall in the window."
3. **Empty filings.** Proposed text: "A filing with no position matched to a CRSP price counts as a missed quarter."
4. **Bridging.** Proposed text: "Only a next filing exactly two quarters later is bridged. The six months are one buy-and-hold period."
5. **Entry weights.** Proposed text: "The quarter-end weights are the weights at entry, with no drift between the quarter-end and the entry month."
6. **CRSP security.** Proposed text: "Any `msf_v2` security with a price in the quarter-end month counts as matched, including funds and ADRs. The CUSIP match uses the `stocknames_v2` row with namedt ≤ quarter-end ≤ nameenddt, ties to the lowest permno. A row's filed value uses the 13F price, 0 if missing."
7. **Peer-adjusted return.** Proposed text: "A holding with no return that month is left out of the peer-adjusted return, with weights rescaled. The monthly differences are annualised as mean × 12, for the main book and the variants. Coverage shares are means over months (peer group, missing return) or over filings (filed value used)."
8. **DGTW details.** Proposed text: "Universe: CRSP common shares (EQTY/COM/NS) on NYSE, NYSE American or Nasdaq at the end of June, with market value |price| × shares > 0. Book-to-market comes from the latest `firm_ratio` row dated January-June of the formation year and must be > 0. Momentum needs all twelve returns. NYSE breakpoints use the NYSE stocks of that universe. Book-to-market and momentum fifths are taken over all stocks of the cell, ties by permno. Group returns weight by the previous month-end market value."
9. **CRSP value-weighted market.** `crsp.msi` is not in section 2, so the code uses `ff.fivefactors_monthly` mktrf + rf. Proposed text: "Market = Fama-French market excess return + T-bill (CRSP value-weighted)."
10. **Years ahead of the market.** Proposed text: "Only calendar years with all twelve months in the record and in the window count."
11. **Turnover and medians.** Proposed text: "Turnover uses only pairs of filings exactly one quarter apart, both in the window, averaged and × 4. The ten-largest weight is the sum of the ten largest weights of each filing; medians are taken over the window's filings."
12. **New positions.** Proposed text: "New positions are measured against the filing exactly one quarter earlier. With no such filing, or no new position, the variant has no months for that quarter."
13. **Funds.** Proposed text: "Share classes are grouped by `fund_hdr` (current) crsp_cl_grp, else crsp_portno, else the class alone. A frozen fundno stands for every class of its group. A class's weight is its TNA at the previous month-end; months without it are dropped. 'ED' means every record month in the window has a class with an objective code starting ED in force. A fund portfolio is index if any class has a non-empty index_fund_flag; active ETFs stay. Mean assets = mean over record months of the summed class TNA."
14. **Several mgrno for one investor.** This follows the coordinator's rule from phase A. Proposed text: "They are one filer. If two file the same quarter, the larger matched value is used."
15. **Population of score part (iii).** Proposed text: "Filers (funds) in the rank group of at least one block with a result there. The value is the share of blocks with 36 months in which alpha > 0."
16. **Score and eligibility.** Proposed text: "Months of record = months with a return 2011-01..2025-12 after the cut, of the record kind. An investor with no rank share has no score and takes no place by record, but can be drawn as control. If 10 or fewer investors are eligible for control, all are taken. Grade does not override `record_kind`."
17. **Explicit places.** The frozen file has no role column, so every row is taken as role investor; an optional `role` column overrides this. Missing explicitness ranks last.
18. **Best-scored lists.** Proposed text: "Score = the same three-part mean computed for every filer (fund), with at least 60 months in 2011-25. Filers listed in any frozen `mgrnos`, and fund groups of any frozen fundno, are left out. The list prints the name, the score and the three rank shares."
19. **Statistics or rank shares only.** Proposed text: "Per window, the statistics are printed if the window or the whole record (2011-25) has 60 months."
20. **Newey-West.** The code uses Bartlett weights with the small-sample factor n/(n−k), as in `qs/btstats.ols_nw`. Gaps in a record are treated as adjacent months.
21. **Foundation list.** `inventory.csv` has no word counts, so the generator stops until it gets them. Proposed text: "words = the word count of the document in the library manifest, added as column `words` to inventory.csv before the job is generated."
22. **Seal.** Proposed text for SEAL_LOG: "Equity jobs may not use pull or export steps. The exempt scorecard runs under names `eq_scorecard_v<n>[letter]`. Its code hash leaves out the frozen input block, which may hold only JSON literals; each run logs the input hash printed by seal_check." Under these rules `eq_match_v1` (phase A, before the seal) would be refused.

## 4. Expected run on WRDS (estimates; nothing measured)
| Step | Rows (est.) | Stored (est.) | Time (est.) |
|---|---|---|---|
| pull_base | cusip map ~0.1M, bm ~0.4M, fund header/style ~0.3M | ~20 MB | < 5 min |
| pull_crsp | ~1.7M | ~40 MB | ~5 min |
| pull_agg | ~0.5M filer-quarters (SQL join over 3-9M s34 rows per year) | ~15 MB | 30-90 min |
| pull_hold | 4-7k candidate filers, 10-20M rows | 200-400 MB | 20-40 min |
| pull_funds | ~3M | ~60 MB | 5-10 min |
| build | memory peak est. 3-6 GB | report only | 15-40 min |

Total is about 1.5-3 hours and about 0.4-0.6 GB of the 10 GB quota. The pulls stop starting new data sets after their budgets and resume on the next run, so a re-run as `eq_scorecard_v1b` may be needed. Every run that reaches `build` is an opening of the seal and goes in SEAL_LOG B with the code hash, the input hash and the lock id.

## 5. Output vs spec section 8
| Section 8 item | Report block |
|---|---|
| Row per matched investor: grade, kind, months, section 4 columns per window, rank shares | `LIBRARY INVESTORS`: an `INV` header line, then one line per window. The columns are a, t, r, rm, pa, pv, dd, yb, np, tw, to, p10, pn, fv, ms and rk |
| Tier lists of section 7 | `TIERS`: by record, explicit, control, tier B, foundation |
| 25 filers and 10 funds without a document | `BEST-SCORED ...` blocks: name, score and the three rank shares |
| Persistence and counts | `PERSISTENCE`: rho and the 5x6 table, 13F and funds apart. `COUNTS`: rank-group sizes and coverage |

The report holds no holding, no stock, no return series and no style, sector or factor average. The smoke test checks that no CUSIP or permno appears in it.
