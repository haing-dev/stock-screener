# Data availability sheet (2026-11-13; metadata only, written by the orchestrator from the repo handoff notes)

Rules: history files (Bloomberg, LSEG) stay on the user's PC; jobs run there; only summary statistics return. 2011+ is
sealed until the one holdout run. A pod without a live source for every input cannot be Core (WORKFLOW rule 7).

## Free data (in the engine today, gm-1.2.1; live every week)
65-market month-end panel 1975+ (equity indexes, government bonds, currencies, commodities from free sources), daily
closes for volatility, official economic statistics with release delay. This is what BASE and CANDIDATE are tested on.

## LSEG Workspace + Datastream (user's own PC, refreshable any day; pulled 2026-11-12; NOT yet read into the engine,
## NOT yet registered as a source; a reader + lock with the 2011+ seal is the proposed next data step)
- FX: spot from 1975, forwards from 1982 (median start 1996), implied vol from 1995, risk reversals only from 2010;
  emerging-market non-deliverable forwards only from about 2010.
- Government bonds: Datastream benchmark yields and return indexes from 1979-12 (some 2y/30y missing for small markets);
  bond futures from 1977 (US 10y 1982, Bund 1990, JGB 1987).
- Short-rate futures: Eurodollar 12 contracts (1981-87 to 2023), Euroswiss 8 (1991+), Euroyen 6 (1989+), Euribor (1994+),
  Fed funds (2000+), SOFR/SONIA (2018+); short sterling only from 1999-2002; Canada BA only contracts 1 and 9-12.
- Swaps: USD/EUR/GBP/JPY/CHF from 1987-89, AUD/SEK/NZD/NOK from 1992-97; overnight swaps USD 2001, GBP 2007, JPY 2005,
  EUR 1999-2005; US and UK inflation swaps from 2007; US inflation-linked yields from 1997-2004; UK from 2010.
- Equity: total-market price, return, P/E, dividend yield from 1973 for about 25 markets; index futures; S&P 500
  12-month forward earnings from 1985. No MSCI valuation ratios, no VIX (free source instead).
- Commodities: futures curves from 1973 (grains, softs, metals), WTI 1983 (24 contracts from 1995), Brent 1988, natural
  gas 1990; S&P GSCI total and excess return by commodity from 1970-87; LME metals cash and 3 months from 1970; about 17
  other commodities (first 3 contracts) from 1973-2013; daily first and second contracts from 1990.
- Economics: national series for 18 countries (prices, unemployment, production, GDP, leading indicators); Citi surprise
  indexes only from 2003. NO first-release values, NO consensus forecasts, NO surprise by release.
- 3-month deposit rates from 1975; cross-currency basis.

## Bloomberg (campus visits only; first pull of 2026-11-04 locked as lock v1)
Usable now: daily files (from 1990), equity total return and valuation, the Economics sheet of file 1, files 2 and 4.
First-release and consensus economics were requested in the first pull; which of those series are usable is NOT
confirmed on this sheet (treat as unconfirmed). Not usable (copied or still-loading blocks): most monthly rates futures, curves, swaps, breakevens,
surprise. A short visit set (237 series) is being pulled on 2026-11-13: short sterling, Canada BA 2-8, non-US breakevens,
CTA benchmark indexes, Canadian swaps, euro/yen inflation swaps, swaption vol, credit spreads and indexes, commodity
fundamentals (inventories), non-deliverable forwards, plus an 85-series cross-check of LSEG. No live Bloomberg feed.

## Not available from any source in hand
Economic surprise by release, first-release values and consensus forecasts (Bloomberg only, usability unconfirmed); euro and Japan
inflation swaps and non-US breakevens outside Bloomberg; lumber; MSCI valuation; positioning data other than free CFTC.
