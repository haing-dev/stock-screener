# Bloomberg pull guide (v5, 2026-11-04)

Eight workbooks, about 2,400 tickers, about 1,950 of them unique. Overlap between files is deliberate: if one series fails, a twin usually works.
Data stays private: never on GitHub, never shared.

## Order (stop wherever time or the allowance runs out; save after each file)
| # | File | What it feeds later | Tickers |
|---|---|---|---|
| 1 | `1_Bloomberg_macro_UBC.xlsx` (v4) | pre-registered batch 2: first-release economics, short-rate futures, commodity curves, yields, equity TR, bond futures | 494 |
| 2 | `2_Bloomberg_econ_policy_monthly.xlsx` | growth/inflation pods on data as first released + consensus (surprises); central banks, balance sheets, money; financial conditions; sentiment | 185 |
| 3 | `3_Bloomberg_rates_credit_fx_monthly.xlsx` | FX carry (forwards, NDFs), curve/swap pods, inflation swaps, credit pods, FX vol and risk reversals, funding basis, more EM yields | 534 |
| 4 | `4_Bloomberg_equity_vol_funds_monthly.xlsx` | equity value/revisions per country (forward EPS), sectors/styles, VIX term structure, skew, implied correlation, SG CTA / short-term traders, ETF assets (flows) | 261 |
| 5 | `5_Bloomberg_commodities_ext_monthly.xlsx` | full commodity curves 1-12, open interest and volume, sub-indexes, inventories and freight | 631 |
| 6 | `6_Bloomberg_daily_A_futures_fx.xlsx` | DAILY from 1990: futures (all markets) + FX spot: daily risk, faster trend, crash tests | 238 |
| 7 | `7_Bloomberg_daily_B_rates_equity_vol.xlsx` | DAILY from 1990: yields, swaps, credit, equity TR, vol, CTA indexes | 127 |
| 8 | `8_Bloomberg_equities_UBC.xlsx` | stock screener (separate project). Formulas are OFF; follow its own Read me. Another day if needed | 4,512 stocks |

Files 1-5 are monthly from 1969 and are the must-haves. Files 6-7 are daily and heavy. If they hit the limit, use Ctrl+H to replace `Per=D` with `Per=W` (weekly) and refresh again.

## At the terminal
1. Bring the files on a USB stick or OneDrive, or open this chat on the terminal and download them. Bring a second USB stick for the results.
2. Open one file at a time in Excel on the Bloomberg terminal. The formulas start by themselves.
3. Open the **Check** sheet. A blank or `#N/A` in the NAME column means the ticker is wrong. Labels ending in "?" are best guesses (about 370 of them).
   - Fix a ticker in the yellow cell on the data sheet. To find the right one, search the series name in the Bloomberg search bar, `SECF` (any security) or `CT` (futures).
   - Skip anything that takes more than a minute. Gaps are fine.
4. Wait until no cell says "Requesting Data...".
5. Save the file under its own name. Then convert to values (Bloomberg tab > Convert/Paste values, or copy all and paste values) and save it again as `<name>_VALUES.xlsx`.
6. If you see `#N/A Limit`, the download allowance is used up. Save, stop, and continue another day.

## At home
Copy everything into `Documents\WRDS results\mscifreedata\Bloomberg_UBC_pull_2026-11-04\pulled\` (file 8 goes to `Documents\Screenerdata\bloomberg`) and say so in chat.

## Not needed from Bloomberg (free elsewhere)
FRED/ALFRED (US first releases, Fed data), CFTC positioning, Ken French factors, AQR data sets, BIS (effective FX, credit), EIA, World Gold Council, economic policy uncertainty, NY Fed term premium (Bloomberg copies are included anyway as backup).
Builder: `docs/data_requests/build_bloomberg_v5.py` (files 2-7). Ticker master: `bloomberg_v5_tickers.csv`.
