# Series the free weekly cycle can observe (from the repo: macro/registry.py, gm/panel.py header, CLAUDE.md)

Use only these ids. If an indicator needs a series that is not here, write 'no live series'. lag = months before a monthly number is treated as known.

## FRED series fetched today (id, release lag in months, first-published values available)

- UNRATE (lag 1, first-published)
- LNS14024887 (lag 1, first-published)
- TRUCKD11 (lag 2, first-published)
- PERMIT (lag 1, first-published)
- TOTALSA (lag 1, first-published)
- GS10 (lag 0)
- GS2 (lag 0)
- GS30 (lag 0)
- GS5 (lag 0)
- GS1 (lag 0)
- TB3MS (lag 0)
- BAA (lag 0)
- FEDFUNDS (lag 0)
- PCEPILFE (lag 2, first-published)
- CPILFESL (lag 1, first-published)
- PPIACO (lag 1, first-published)
- T5YIFR (lag 0)
- WTISPLC (lag 1)
- PCOPPUSDM (lag 1)
- PIORECRUSDM (lag 1)
- GDP (lag 2, first-published)
- M2SL (lag 1, first-published)
- WALCL (lag 0)
- WTREGEN (lag 0)
- RRPONTSYD (lag 0)
- MORTGAGE30US (lag 0)
- THREEFYTP10 (lag 0)
- VIXCLS (lag 0)
- DRCCLACBS (lag 3, first-published)
- NCBEILQ027S (lag 3, first-published)
- HNOCEAQ027S (lag 3, first-published)
- TFAABSHNO (lag 3, first-published)
- USREC (lag 0)
- DTWEXBGS (lag 0)
- TWEXMMTH (lag 0)

## More FRED series fetched for research
EXJPUS, EXSZUS, EXUSEU, EXUSUK, EXCAUS, EXSDUS, IR3TIB01JPM156N, IR3TIB01CHM156N, IR3TIB01DEM156N, IR3TIB01EZM156N, IR3TIB01GBM156N, IR3TIB01CAM156N, IR3TIB01SEM156N, IRSTCI01JPM156N, IRSTCI01CHM156N, EXGEUS

## Yahoo daily prices fetched today
SPY, EWY, DX-Y.NYB, HYG, IEF, XLY, SOXX, ^VIX, TLT, SHY, TIP, GLD, DBC, GC=F, UUP, FXY, FXF, FXE; 20 US industry ETFs: SMH, IGV, VOX, KBE, KRE, KIE, ITB, XRT, IYT, XLI, ITA, XLE, XLU, XLP, XLV, XBI, XLB, XME, GDX, IYR

## Indicators already computed by the Macro Compass (id: name)

- jobs_alarm: Unemployment rise from its 12-month low (Sahm rule)
- truck: Truck freight vs a year ago
- permits: New home permits, 6-month change
- autos: Car sales, 6-month change
- curve: Yield curve (10-year minus 2-year)
- youth: Young-adult jobless rate vs overall, 12-month change
- cards: Credit-card late payments, 12-month change
- cyc_def: Cyclical vs defensive stocks, 6 months
- staples_disc: Staples vs discretionary stocks, 6 months
- breadth: Industries in an uptrend
- breakdowns: Industries 20%+ below their 12-month high
- transports: Transport vs industrial stocks, 6 months
- homebuilders: Home builders vs market, below their 2-year peak
- core_pce: Core inflation, last 3 months vs last 12
- core_cpi: Core consumer prices vs a year ago
- ppi: Producer prices vs a year ago
- inflexp: 5-year inflation expectations, 6-month change
- oil: Oil price, 6-month change
- copper: Copper price, 6-month change
- stockbond: Stocks and bonds moving together (1-year correlation)
- vix: Stock market fear gauge (VIX)
- spx_trend: S&P 500 vs its 10-month average
- junk: Junk bonds vs Treasuries, 3 months
- baa: Corporate bond spread (Baa minus 10-year)
- baa_chg: Corporate bond spread, 6-month change
- banks: Bank stocks vs market, 6 months
- dollar_break: Dollar vs its 12-month high
- chips_break: Chip stocks vs their 12-month high
- fedfunds: Fed interest rate, 12-month change
- y10_chg: 10-year yield, 12-month change
- y10_ngdp: 10-year yield minus economic growth
- m2: Money supply (M2) growth
- dollar: US dollar, 12-month change
- squeeze: Oil, rates and dollar rising together
- realyield: Real 10-year yield (after inflation)
- mortgage: Mortgage rate, 12-month change
- termprem: Extra yield on long bonds (term premium), 12-month change
- netliq: Fed money in the system, 3-month change
- mcap_gdp: Stock market value vs the economy
- hh_equity: Share of household savings in stocks
- cape: Price vs 10-year average earnings (CAPE)
- rally: Speed of the stock rally (6-month gain vs its swings)
- leadership: Narrow leadership (index vs typical industry, 12 months)

## Global macro book panel (gm/panel.py header)
About 61 markets, monthly futures-style excess returns from free data: equity indexes (local total return minus local 3-month rate), 10-year government bonds, 2-year notes, currencies against the dollar, commodities; plus daily closes for the markets with a free daily source.

## LSEG Workspace on the user's PC (refreshable any day; history checked, see CLAUDE.md)
FX spot and forwards; Datastream benchmark bond yields and return indexes (2/5/10/30-year, many countries); equity indexes with P/E and yield; commodity futures curves; bond, equity-index and short-rate futures (SOFR, Fed funds, Euribor, SONIA; Eurodollar history to 2023); swap rates and OIS for the main currencies; US and UK inflation swaps; US TIPS yields; Citi economic surprise indexes; S&P 500 12-month forward EPS; 3-month deposit rates; national economic series for 18 countries.

## Not available
VIX on LSEG (free source instead), credit spreads beyond the FRED ones, economic releases with consensus, positioning and flow data, Fed or Treasury operational detail beyond what FRED carries (if a FRED id is not listed above it is not fetched today; say so).