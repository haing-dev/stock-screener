# LSEG Workspace for stocks: what the equity probe returned (2026-11-18)

Step E1.1 of `EQUITY_POD_SHOP_PLAN_v0.3.md`. Workbook `docs/data_requests/lseg_equity_probe_2026-11-17/LSEG_equity_probe_v1.xlsx`
(181 formulas), refreshed by the user on her PC and saved 2026-11-18 09:06 PC time. Read on the PC by the metadata
reader `tools/bbgq/jobs/lseg_eq_probe_v1.py`; report `tools/bbgq/results/lseg_eq_probe_v1.txt` (counts, date ranges,
kinds of text; no values). Test set: 6 live large caps, 3 dead or taken-private companies (Lehman, Enron, Twitter), 3
companies that restated (GE, Kraft Heinz, Super Micro).

Totals: 115 formulas returned numbers, 61 returned text or dates only (lists, identifiers, dates; also the wrong
field names), 5 returned an LSEG message. No block was still loading. Three pairs of blocks hold the same numbers, all
expected (the same series asked twice).

## What works, and how far back

| Need | Result | Use in the plan |
|---|---|---|
| **First-reported vs restated accounts** | **Works.** `TR.F.*` fields with `ReportingState=Orig` and `=Rsdt` both return dated annual and quarterly series. They differ where restatements happened: GE revenue in 28 of 43 years, GE assets 20 of 43, GE operating cash flow 27 of 43, Kraft Heinz revenue 2 of 14 years and 8 of 51 quarters, Super Micro revenue 2 of 25 years, Apple (control) 2 of 44. Original announcement and source dates exist (`TR.F.OriginalAnnouncementDate`, `TR.ISOriginalAnnouncementDate` from 1993). History from 1983 (annual), 1989 (quarterly) | A point-in-time second source for accounts (gate G7), and a check of Compustat's restated values. The biggest open question of the plan is answered yes |
| Accounts of dead companies | Enron by ISIN from 1983 (Workspace); Lehman fails by ISIN in Workspace but works in Datastream Worldscope (`WC01001` etc.) | Dead companies are reachable, through one route or the other |
| Field names | Revenue, total assets, operating cash flow (`TR.F.NetCashFlowOp`), shares (`TR.F.ComShrOutsTot`) work; the guessed net-income names failed; older fields (`TR.NetIncome`) work | Net income needs the right `TR.F` name (one more probe line) |
| **Consensus as it stood on past dates** | **Works.** EPS mean FY1 and FY2, monthly from 1990-01 (Apple, GE); dead Lehman 1994-2008; revenue mean from 1996; number of estimates from 1990 (Datastream `EPS1NE` from 1981); 12-month forward from 2000; actual EPS and report dates from 1996 (quarterly) | Expectations signals and the analyst layer can be checked against LSEG; history stays on I/B/E/S at WRDS |
| **Holders by quarter** | **Works from about 1999.** Top holders per quarter (Coca-Cola from 1999, holders as of 1999-12 and 2005-12 with % of shares out); dead Lehman holders as of 2007-12; all 8,310 current Apple holders in one formula; investor PermIDs for joining. 1990: nothing | Second source for 13F; ownership cells live |
| A manager's whole portfolio | **Fails** (all three guessed fields) | Copy portfolios stay on WRDS 13F |
| **Insider trades** | **Works, full history from 1998**, dead Enron included (1998-2002) | Fills part of the design-era gap: SEC data sets start only in 2006. To be checked against SEC filings before use |
| Short interest | Workspace `TR` fields give only a few points; Datastream `SHORTINT` gives Apple monthly from 2001 | Short interest from 2001 via Datastream (one more probe to confirm coverage across stocks) |
| Universe incl. dead companies | Workspace screen active OR inactive: 16,369 US primary common shares (14,355 active, about 2,000 inactive with retire dates from 2006 only). Datastream dead list `DEADUS1`: 6,286 items, dates 1986-2026. `WSCOPEUS` and `DEADUS` too large in one formula | The Workspace screen loses companies that died before 2006; Datastream dead lists reach 1986. History stays on CRSP |
| Past index members | Datastream `LS&PCOMP` with a date suffix: S&P 500 as of Jan 2000 and Jan 1990 (500 each). The Workspace chain with a date (`0#.SPX`) returned today's members: unusable for history. Russell 3000 history: not found | Datastream for past S&P 500 lists |
| Prices and returns | Monthly closes from 1980 for live stocks; dead companies by ISIN (Lehman to 2008, Enron to 2002, Twitter to 2022); Datastream total return index for all 12. Datastream pads a dead stock's index flat after delisting (Lehman rows to 2026): cut at the delisting date. Daily: 40 years for one stock in one formula | Live prices; second source for returns |
| Identifiers | CUSIP, ISIN, SEDOL, ticker, RIC, PermID, CIK, status and retire date for all 12; CUSIP history only latest; delisted RIC guesses work for Lehman and Enron, not Twitter | Join with WRDS by CUSIP or CIK |
| **Fund returns** | Lipper NAV monthly from 1990; Fundsmith Equity NAV from 2010 (by ISIN); Vanguard 500 from 2000; Datastream total return index for funds by ISIN | Non-US funds (for example Fundsmith) can get a real record: they are outside CRSP. Not used in the registered scorecard (section 5: funds outside CRSP are reported only) |
| StarMine scores | **Today only.** Earnings quality, ARM, value-momentum and price momentum ranks return one current value; no history | Live inputs at most; never in a backtest |
| Size of requests | 14,355 rows x 1 field, 503 x 6 fields, 8,310 holders, 10,659 daily rows and a 95,000-number Datastream grid all returned in one refresh | Excel handles the sizes the plan needs |

## Consequences for the plan
1. **History stays on WRDS** (CRSP, Compustat, I/B/E/S, 13F): LSEG's Workspace universe loses companies that died
   before 2006, and holder history starts about 1999.
2. **LSEG is a usable second source and live source**, as planned, and better than expected on one point:
   first-reported accounts with announcement dates exist back to 1983. The two-source check (gate G7, step E1.7) can
   compare Compustat point-in-time values with LSEG's original values.
3. **New possibility:** insider trades from 1998, before the SEC data sets (2006). Before any use, a registered
   check against SEC Form 4 filings for 2006-2010 (design era).
4. **Not available:** StarMine history, a manager's portfolio by date, Russell membership history.
5. **Open probe lines** (small, for the next LSEG pull): the right net-income field, short interest across many
   stocks, Datastream dead lists by number (`DEADUS2...`), the Workspace screen with a retire-date filter before 2006.
