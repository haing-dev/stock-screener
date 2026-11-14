# Data availability for rates and curve pods (2026-11-14; metadata only, written by the orchestrator from the repo notes)

Rules: history files stay on the user's PC; jobs run there; only summary statistics return. 2011+ is sealed until the one
holdout run. A pod without a live source for every input cannot be Core (WORKFLOW rule 7). Design months end 2010-12.

## In the engine today (free data, gm-1.2.1)
Government bond markets at fixed maturities (monthly returns built from par yields; US 2/5/10/30y and about ten other
countries' 10y), 3-month rates per country, daily yields for volatility. No futures strips, no swaps. Three yield-spread
series are built but not traded. Note: the engine holds the US 2-year note twice (a known defect, fix pending).

## LSEG Workspace + Datastream (user's own PC, refreshable any day; pulled 2026-11-12; not yet read into the engine)
- Eurodollar futures: contracts 1-12 monthly (contracts 1-4 from 1981-12, 9-12 from 1987-06; ends 2023 when the contract
  ended), daily contracts 1, 2, 4, 8 from 1989-12. Successor SOFR futures from 2018.
- Other short-rate futures: Euribor from 1994, Euroswiss 8 contracts (1991+, ended), Euroyen 6 contracts (1989+),
  Fed funds from 2000, SONIA from 2018, short sterling only from 1999-2002, Canada BA contracts 1 and 9-12.
- Swaps: USD, EUR, GBP, JPY, CHF at 1/2/3/5/7/10/30y from 1987-89; AUD, SEK, NZD, NOK from 1992-97; overnight swaps
  USD 2001, GBP 2007, JPY 2005, EUR 1999-2005.
- Government benchmark bonds (Datastream): yield and return index at 2/3/5/7/10/30y for about 20 countries from 1979-12
  (some 2y/30y missing for small markets). Bond futures from 1977 (US 10y 1982, Bund 1990, JGB 1987).
- 3-month deposit rates from 1975; US inflation-linked yields from 1997-2004; US and UK inflation swaps from 2007.
- Commodity futures curves: WTI from 1983 (24 contracts from 1995), Brent 1988, natural gas 1990 (24 contracts),
  heating oil, soybeans and other grains from 1973 (9 contracts).
## Bloomberg (campus pull of 2026-11-13; on the PC, being merged; no live feed)
Short sterling contracts 1-5 from 1988; Canada BA contracts 2-8 from 1990-91; Canadian swaps from 1989; non-US breakevens
(UK 1992, Australia 2000, France 2003, Japan 2004, Germany 2009); euro inflation swaps from 2004.
## Not available
LIBOR cash fixings as a separate series (3-month deposit rates stand in); Eurodollar after 2023 (contract ended: the live
instrument is SOFR futures, a different underlying rate); economic consensus forecasts; dealer positioning.
