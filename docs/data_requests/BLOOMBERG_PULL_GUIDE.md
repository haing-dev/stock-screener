# Bloomberg pull guide (v4, for the UBC visit, 2026-11-02)

File: `Bloomberg_macro_UBC.xlsx` (v4, 494 tickers, monthly from Dec 1969 unless noted). Data stays private: never on GitHub.

## Before you go
- Bring the file on a USB stick or in OneDrive; bring a second USB for the results.
- Plan 2-3 hours. Sheets 1-5 are the must-haves (about 1 hour); the rest is a bonus.

## At the terminal
1. Log in to Bloomberg, open the file in Excel, check the **Bloomberg** tab is in the ribbon.
2. Work **one sheet at a time, in order** (tab names below). Click the sheet, then Bloomberg tab -> Refresh -> Selected sheet (or Refresh Workbook). Wait until no cell says "Requesting Data...".
3. A cell shows `#N/A Invalid Security`: type the series name in the Bloomberg window (`SECF` for any security, `CT` for futures contracts, `FLDS` for field names), paste the right ticker into the yellow cell, refresh again. Labels with "?" are best guesses. Skip anything that takes more than two minutes.
4. **Save after every sheet** (keep formulas). If the ribbon offers "Convert to values", also save a values copy (`Bloomberg_macro_UBC_values.xlsx`); that copy is the one that opens at home.
5. `#N/A Limit` = the terminal's download allowance is used up: save and stop.

## Order and why
| # | Sheet | What | Why we need it |
|---|---|---|---|
| 1 | Economics | first-released value, consensus, release date, revised value (35 series) | growth theme on first-release data; surprises |
| 2 | RatesFutures | short-rate futures strips 1-8: Eurodollar/SOFR, Euribor, short sterling/SONIA, BAX, Australian bills, Euroyen, Euroswiss; Fed funds | new pod: trend and carry on the front end; AQR's best markets; the 1987 crash test |
| 3 | SpotRates3m | 3-month cash rates | carry of short-rate futures (implied minus spot) |
| 4 | Curves | commodity futures 1st, 2nd, 3rd, ~12-month (35 commodities) | commodity carry without the seasonal noise of 1st/2nd |
| 5 | Returns | GSCI/BCOM excess-return indexes | properly rolled commodity returns before 2000 |
| 6 | Yields | government yields 2/5/7/10/30y, 10 countries | bond roll-down carry, curve signals |
| 7 | EquityTR | local total-return index per equity market (21) | replaces our estimated dividends before 2010 (data audit) |
| 8 | BondFutures | 1st and 2nd bond futures (16 contracts) | checks our yield-built bond returns |
| 9 | EquityValuation | MSCI country P/E, forward P/E, P/B, dividend yield, forward EPS | equity value pod, earnings revisions |
| 10-15 | Breakevens, Benchmarks, Surprise, Volatility, FXBasis, DailyCommodities | inflation compensation, CTA indexes, surprise indexes, implied vols/risk reversals, funding stress, daily commodities | secondary; daily sheet only if the limit allows |

## At home
Copy the saved file(s) into `Documents\WRDS results\mscifreedata` and tell Claude in chat. Claude reads it from there through the desktop link; nothing is uploaded to GitHub.

## Not needed from Bloomberg (we already have it or get it elsewhere)
FRED/ALFRED series (first releases for US data), CFTC positioning (free), WRDS: CRSP Treasuries (bond check done), Compustat Global, I/B/E/S (analyst revisions), Fama-French. MSCI country prices from 1997 (your free download).
