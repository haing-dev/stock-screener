# Data availability for value, momentum and carry pods (2026-11-14; metadata only, written by the orchestrator from the repo notes)

Rules: history files stay on the user's PC; jobs run there; only summary statistics return. 2011+ is sealed until the one
holdout run. Design months end 2010-12. A pod without a live source for every input cannot be Core (WORKFLOW rule 7).
The book trades asset classes and country markets (61 markets: equity indexes, government bonds, currencies,
commodities). It does not trade individual stocks.

## In the engine today (free data, gm-1.2.1; live every week)
Month-end panel 1975+ for 61 markets (equity indexes, government bonds, currencies, commodities), 3-month rates per
country, consumer prices, daily closes for volatility. Existing families: Trend, Carry, Value, Economic trend; what
each one's rule uses is described in the charter digest (section 3), not on this sheet.

## LSEG Workspace + Datastream (user's own PC, refreshable any day; pulled 2026-11-12; not yet read into the engine)
- Currencies: spot from 1975, forwards from 1982 (median start 1996), implied volatility from 1995; emerging-market
  non-deliverable forwards only from about 2010.
- Equity markets: Datastream total-market price, return, P/E, dividend yield and market value from 1973 for about 25
  countries; index futures; S&P 500 12-month forward earnings from 1985. No book-to-price series for country indexes
  was pulled; MSCI valuation ratios are not licensed.
- Bonds: benchmark yields and return indexes at 2/3/5/7/10/30y for about 20 countries from 1979-12; bond futures from
  1977 (US 10y 1982, Bund 1990, JGB 1987); swaps from 1987-89.
- Commodities: futures curves from 1973 (grains, softs, metals), WTI 1983, Brent 1988, natural gas 1990; S&P GSCI
  spot, excess and total return by commodity from 1970-87; LME cash and 3 months from 1970.
- Short-rate futures: Eurodollar 12 contracts 1981-2023, Euribor 1994, Euroswiss, Euroyen.
## Bloomberg (campus pulls, on the PC, lock v2; no live feed)
First pull: equity total return and valuation sheets, daily futures and FX from 1990, economics. Visit of 2026-11-13:
short sterling and Canada BA futures, non-US breakevens, credit spreads and indexes, some commodity inventories,
non-deliverable forwards, an 85-series cross-check of LSEG.
## Not available
Individual-stock data inside this book (a separate equity project exists, design only); book-to-market for country
indexes; consensus forecasts; dealer positioning other than free CFTC.
