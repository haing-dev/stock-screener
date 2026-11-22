# Field dictionary v1.0, part 1: reference book v1 and universe (registered 2026-11-22, V04_REGISTRATION.md A8)

Exact formulas for the measures of reference book v1 (R7) and the universe (R3), in the two data forms: **LSEG**
(the registered primary source; stage-B files, first-reported accounts) and **WRDS** (CRSP / Compustat / I/B/E/S; the
second source and the first engine run, `tools/equity/wrds/eq_ref.py`). Part 2 (the other measures of v0.1, used by
pods) is registered with the pod specs; no reference-book measure may change after this file (a change = book v2).

Rules for every measure (from v0.1, now fixed):
1. As known on the day. LSEG: accounts as first reported (`ReportingState=Orig`), usable from the original
   announcement date + 1 day. WRDS: Compustat quarterly values (restated where Compustat restated; a known difference),
   usable from `rdq` + 1 day. Missing date: period end + 45 days. A latest known quarter more than 270 days before the
   month-end = accounts missing.
2. Flows (TTM) = sum of the last four reported quarters, all four present and consecutive; balances = latest quarter;
   averages = (latest + four quarters earlier) / 2. WRDS quarterly cash flow from operations = year-to-date `oancfy`
   differenced inside the fiscal year.
3. A ratio whose denominator is at or below zero is missing (not negative).
4. Ranks: percentile inside the GICS sector at each month-end among ranked universe members (higher = better;
   accruals reversed). Missing measure = 0.5 (the sector median). More than 3 of the 7 book measures missing = not
   ranked.
5. Money: Compustat in millions; CRSP shares in thousands; LSEG in units as returned (USD).

| id | measure | formula | LSEG inputs | WRDS inputs |
|---|---|---|---|---|
| L01 | Market value (line) | price x shares outstanding at month-end | TR.PriceClose x TR.SharesOutstanding (monthly file) | abs(mthprc) x shrout x 1000 (crsp.msf_v2) |
| L01c | Market value (company) | sum of L01 over the company's common lines | TR.CompanyMarketCap | sum over permco |
| L02 | Liquidity | median of the last three month-end daily dollar volumes (A7 stand-in) / median of the last three monthly medians of daily dollar volume | TR.Volume x TR.PriceClose (month-end day) | crsp.dsf_v2: monthly median of abs(dlyprc) x dlyvol |
| X01 | Sector | GICS sector (2 digits); groups 4010, 4030, 4040, sector 60, sub-industry 35201010 excluded from generic books | TR.GICSSector etc. (today; known look-ahead) | comp.co_hgic at the month (history); else comp.company (today) |
| V01 | Earnings yield | EBIT TTM / EV; EV = L01c + short-term debt + long-term debt + preferred + minority - cash and short-term investments; EV <= 0 missing | R08 TR.F.EBIT; R30 TR.F.DebtTot (= short + long); R36 TR.F.PrefShHoldEq; R35 TR.F.MinIntrEq; R18 TR.F.CashSTInvstTot | oiadpq; dlcq + dlttq; pstkq; mibq; cheq |
| V06 | Book to price | common equity / L01c | R33 TR.F.ComEqTot | ceqq |
| P01 | Momentum | compound total return of months t-11 .. t-1 (formation at the end of month t; the last month skipped); at least 9 of the 11 months present | TR.TotalReturn1Mo (monthly file) | mthret (incl. delisting) |
| Q03 | Return on equity | net income TTM / average common equity | R13 TR.F.NetIncAfterTax; R33 | niq; ceqq |
| Q08 | Accruals | (net income TTM - cash flow from operations TTM) / average total assets; low = good | R13; R41 TR.F.NetCashFlowOp; R25 TR.F.TotAssets | niq; oancfy (differenced); atq |
| B05 | Piotroski score | nine 0/1 signals on TTM against TTM a year earlier: ROA = NI / assets a year ago > 0; CFO > 0; ROA up; CFO / assets > ROA; long-term debt / average assets down; current ratio up; split-adjusted shares not up; gross margin up; sales / assets a year ago up. At least 7 of 9 present; score = sum / present x 9 | R13, R41, R25, R29 TR.F.DebtLTTot, R21, R27, R39 TR.F.ComShrOutsTot, R03 (or R01 - R02), R01 | niq, oancfy, atq, dlttq, actq, lctq, cshoq x ajexq, saleq - cogsq, saleq |
| E01 | Consensus revision | (FY1 EPS mean at month-end - FY1 EPS mean three month-ends earlier) / price, both on the same share basis; mean = latest value within 35 days before the month-end | TR.EPSMean(Period=FY1) monthly; TR.PriceClose | ibes.statsum_epsus fpi 1 meanest; CRSP price put on the I/B/E/S (current) share basis with mthcumfacpr |

Group scores: value = mean(V01, V06); momentum = P01; quality = mean(Q03, Q08, B05); expectations = E01. Book score =
mean of the four group scores. Published-form checks (Batch 0): top minus bottom tenth inside the sector, equal
weight, next month; Piotroski as published (score 8-9 minus 0-1).
