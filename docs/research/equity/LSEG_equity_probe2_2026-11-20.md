# LSEG test file 2: what came back (2026-11-20)

Workbook `LSEG_equity_probe_v2.xlsx` (184 formulas), refreshed and saved by the user, read with
`tools/bbgq/jobs/lseg_eq_probe_v2.py` (report `tools/bbgq/results/lseg_eq_probe_v2.txt`; counts and header labels).
173 of 175 blocks on the first six sheets returned; no block was still loading. The reader ran out of memory on
the two widest grids (E-183, E-184), which were looked at directly.

## Works
| Need | Result |
|---|---|
| Account items as first reported | 48 of 52 raw items have a working `TR.F` name (annual, 18 years). Net income: `TR.F.NetIncAfterTax`. Capex: `TR.F.CAPEXNetCF`. Free cash flow: `TR.F.FOCF`. Gross profit: `TR.F.GrossProfIndPropTot`. D&A: `TR.F.DeprDeplAmortCF`. Receivables: `TR.F.LoansRcvblNetST`. Tax: `TR.F.IncTax` |
| Quarterly, first reported vs restated | Both return 51 quarters for Kraft Heinz; they differ in 8 quarters for revenue and cash flow, 6 for net income. Quarterly cash flow is per quarter, not year to date (GE checked by eye). `Period=LTM` works |
| Announcement dates | Annual and quarterly, whole test set in one formula |
| Many companies in one formula | 32 companies x 8 fields x 18 years and x 70 quarters; S&P 500 x 8 fields x 18 years (8,664 company-years); S&P 500 x 4 fields x 70 quarters (33,659 rows); S&P 500 monthly total return and EPS mean (about 94,000 rows each); all 14,369 active US companies x 4 fields |
| Dead companies by ISIN | Accounts, EPS mean, total return, market value for all 11 dead test companies |
| Estimates | EPS mean FY1 / FY2 / next 12 months, revenue, EBITDA, EBIT, dividend, long-term growth, price target, recommendation, number of estimates, actual EPS with report date, surprise: all monthly from 2009-12. Free-cash-flow mean and SmartEstimate only from 2013. Revision counts up / down: Datastream `EPS1UP`, `EPS1DN` (Workspace names failed) |
| Prices | `TR.TotalReturn1Mo`, close, market value, shares, volume monthly for many companies; daily; dividends; splits; 10-year Treasury yield; S&P 500 total return |
| Sector | GICS names and codes today; Datastream industry names for dead companies (`INDM`, `ICBIN`) |
| Past size | `TR.CompanyMarketCap(SDate=...)` over the whole screen: 6,342 companies with a value on 2010-12-31, 9,616 on 2018-12-31 |
| Owners | Holders with investor type on a past date; insider transactions for 21 companies from 2010 in one formula (62,684 rows); free float (Datastream `NOSHFF` monthly; Workspace today) |
| Past index members | S&P 500 lists of Dec 2010 and Dec 2017 (Datastream), and their total returns in one grid; S&P 1500 today |

## Does not work, or open
1. **Company list with dead companies (the main risk).** The Workspace screen "active or inactive" holds about
   2,000 inactive companies. Of 1,930 companies above $300m at the end of 2010 it marks only 70 as retired; the true
   number is several hundred. So the screen cannot give the 2010-2025 universe. Datastream dead lists `DEADUS1` to
   `DEADUS7` hold about 42,600 dead items with dates (all security types), and dead companies work by ISIN. The
   universe must be built as: Datastream dead lists + research lists, filtered to common shares, then size on each
   date, and the count per year checked against CRSP delistings on WRDS. The research lists (`FAMERA`...) need all
   letters pulled.
2. **Short interest history.** Datastream `SHORTINT` fails for lists of codes (invalid code) though it worked for
   one mnemonic in probe 1; Workspace gives today's value only. Needs one more test by Datastream mnemonic, else
   short interest comes from WRDS (Compustat) or is left out of history.
3. **Sector on a past date** is not available in Workspace (`SDate` not accepted). History uses today's GICS code
   (Datastream industry for dead companies); the limit is logged.
4. **Insider and institutional ownership totals:** the guessed names failed; totals can be summed from holders by
   type, or the right field found.
5. Four account items returned nothing for Apple and need a second company before the name is judged: goodwill
   (`TR.F.GoodwNet`), minority interest, preferred equity, net debt issuance. Interest expense and debt return
   fewer years for Apple, as expected.
6. Russell 1000 / 3000 lists and a dated S&P 1500 list: not found. `DEADUS1` x total return in one grid stops at
   the first invalid code: dead companies are pulled in smaller groups.
7. Datastream I/B/E/S `EPS1` gives the last 12 months only; history of the mean comes from Workspace `TR.EPSMean`.

## Consequences
- LSEG can carry the company data for 2010-2025 as first reported. The field dictionary v1.0 can be written with
  the working names.
- Before the data files are built: one short universe file (dead and research lists, all letters, with ISIN,
  type, dates, industry) and the count check against CRSP on WRDS. The data files are then built per group of
  about 500 companies (the size that worked), by ISIN.
