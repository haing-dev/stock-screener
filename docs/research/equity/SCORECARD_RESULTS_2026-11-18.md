# Investor scorecard: league table by strategy (2026-11-18)

Result of the registered scorecard (`STAGE0_REGISTRATION.md`, registered at commit 184b5d0), job `eq_scorecard_v1` on
WRDS, run once on 2026-11-18 (code sha256 f7f54264..., the registered hash; report
`scorecard_check/eq_scorecard_v1_report.txt`; table `scorecard_check/league_table_2026-11-18.csv`). It orders the
reading of the transcripts. It is not evidence that any strategy works (plan section 5.4).

## How to read it
- **Alpha** = six-factor alpha, percent a year: what the record earned beyond the market, size, value, profitability,
  investment and momentum. It is the registered ranked result. **t** = how sure it is; about 2 is the usual bar.
- **Rank** = place among all 13F filers (for a 13F record) or all US equity funds (for a fund) in that window, 0 worst, 1 best.
- 13F records are copy portfolios: US-listed long positions, bought after the 45-day filing delay, no shorts, no fees.
  Fund records are real returns after fees. Grade B = long/short or non-US book, so the 13F shows only part of it.
- Tier A (record) is set by the registered score (mean of three ranks: 2011-25, 2021-25, share of positive 5-year
  blocks), at most eight per style, and needs 60 months of record. Tier A (explicit) = the ten investors whose
  transcripts state the most explicit criteria. Control = ten drawn at random, for comparison.

## The main finding first: records do not persist
Among all filers, the rank in one five-year block barely predicts the rank in the next: rank correlation +0.14
(2011-15 to 2016-20) and -0.05 (2016-20 to 2021-25); for all US equity funds +0.12 and -0.00. Top-fifth filers of
2016-20 were about as likely to land in the bottom fifth of 2021-25 (101) as in the top fifth (122). What repeats is
being extreme, which is risk-taking, not skill. Of the 53 rankable library investors only two have a 2021-25 t above
2 (David Rosen 2.6, Derek Pilecki 2.0), and over 2011-25 one (Alex Sacerdote 3.0). So, as the plan expected, the
ranking orders the reading; it cannot say who is skilled.

## Quality compounders

| Investor | Record | 2021-25 alpha (t) | 2021-25 return / vs market | 2021-25 rank | 2011-25 alpha (t) | 2011-25 rank | Tier |
|---|---|---|---|---|---|---|---|
| Robert Vinall | 13F A: RV CAPITAL GMBH | +6.09 (+0.73) | +16.3% / +3.2 | .919 | +3.93 (+0.56) | .914 | A (record) |
| Pat Dorsey | 13F A: DORSEY ASSET MANAGEMENT LLC | +2.88 (+0.32) | +4.0% / -9.0 | .863 | +5.89 (+1.15) | .938 | A (record) |
| Chris Hohn | 13F A: CHILDREN'S INV MGMT (UK) LLP / CHILDREN' | +1.17 (+0.39) | +15.7% / +2.6 | .808 | +4.69 (+1.86) | .925 | A (record) |
| Christopher Begg | 13F A: EAST COAST ASSET MGMT, LLC. | +0.63 (+0.26) | +15.9% / +2.9 | .782 | +0.37 (+0.28) | .769 | A (record) |
| Chris Bloomstran | 13F A: SEMPER AUGUSTUS INVTS GRP LLC | -0.23 (-0.05) | +16.6% / +3.6 | .722 | +1.18 (+0.63) | .832 | A (record) |
| Samantha McLemore | fund F: Advisor Managed Portfolios: Patient Opportuni | -0.41 (-0.10) | +6.8% / -6.2 | .790 | -2.09 (-0.78) | .443 | B |
| Chris Davis | fund F: Davis New York Venture Fund, Inc: Davis New Y | -0.43 (-0.13) | +12.8% / -0.3 | .788 | -0.76 (-0.62) | .763 | B |
| Guy Spier | 13F A: AQUAMARINE CAPITAL MGMT, LLC; AQUAMARINE ZURI | -0.66 (-0.23) | +17.3% / +4.2 | .679 | +0.06 (+0.02) | .739 | A (record) |
| Thomas Russo | 13F A: GARDNER RUSSO & GARDNER | -1.23 (-0.41) | +15.3% / +2.2 | .601 | +1.21 (+0.83) | .834 | A (record) |
| Dev Kantesaria | 13F A: VALLEY FORGE ADVISORS, LLC / VALLEY FORG | -1.29 (-0.22) | +15.0% / +1.9 | .591 | +4.76 (+1.14) | .927 | A (record) |
| Warren Buffett | 13F A: BERKSHIRE HATHAWAY / BERKSHIRE HATHAWAY  | -1.55 (-0.41) | +12.0% / -1.0 | .549 | -2.11 (-1.17) | .320 | control |
| Tom Gayner | 13F A: MARKEL GAYNER ASSET MANAGEMENT / MARKEL  | -3.87 (-2.06) | +11.9% / -1.2 | .202 | -0.29 (-0.33) | .696 | B |
| Eddy Elfenbein | fund F: AdvisorShares Trust: AdvisorShares Focused Eq | -4.02 (-1.00) | +10.0% / -3.1 | .343 | -1.79 (-0.87) | .528 | control |
| Kelly Granat | 13F A: LONE PINE CAPITAL LLC / LONE PINE CAPITA | -4.12 (-0.63) | +2.8% / -10.3 | .179 | -1.16 (-0.52) | .536 | B |
| François Rochon | 13F A: GIVERNY CAPITAL INC. | -4.22 (-1.56) | +9.3% / -3.7 | .169 | -2.75 (-1.51) | .226 | A (explicit) |
| Peter Keefe | 13F A: AVENIR CORP / AVENIR CORPORATION | -5.22 (-1.71) | +7.5% / -5.6 | .117 | -1.99 (-1.18) | .348 | control |
| John Armitage | 13F A: EGERTON CAPITAL (UK) LLP / EGERTON CAPIT | -5.27 (-2.21) | +9.7% / -3.4 | .114 | +0.56 (+0.40) | .786 | B |
| Joseph Shaposhnik | fund F: TCW Funds, Inc: TCW New America Premier Equit | -5.65 (-1.31) | +7.7% / -5.3 | .179 | +0.19 (+0.07) | .886 | control |
| Terry Smith | 13F A: FUNDSMITH LLP | -6.89 (-2.10) | +5.8% / -7.2 | .070 | +0.96 (+0.50) | .818 | B |
| Andrew Brenton | 13F A: TURTLE CREEK ASSET MGMT INC. | -10.34 (-2.61) | +4.7% / -8.4 | .033 | -5.19 (-1.95) | .087 | A (explicit) |

## Deep value

| Investor | Record | 2021-25 alpha (t) | 2021-25 return / vs market | 2021-25 rank | 2011-25 alpha (t) | 2011-25 rank | Tier |
|---|---|---|---|---|---|---|---|
| Prem Watsa | 13F A: FAIRFAX FINL HOLDINGS LIMITED / FAIRFAX  | +8.92 (+1.00) | +16.8% / +3.7 | .946 | -3.52 (-0.73) | .157 | A (record) |
| David Rosen | 13F A: RUBRIC CAPITAL MANAGEMENT LP; RUBRIC CAPITAL  | +8.44 (+2.58) | +17.4% / +4.3 | .942 | -0.12 (-0.03) | .720 | A (record) |
| Bob Robotti | 13F A: ROBOTTI & CO ADVISORS, LLC | +7.43 (+0.73) | +20.2% / +7.2 | .934 | +0.54 (+0.13) | .784 | A (record) |
| Joel Greenblatt | fund F: FundVantage Trust: Gotham Absolute Return Fun | +1.99 (+1.16) | +15.6% / +2.5 | .922 | -1.21 (-1.02) | .670 | A (record) |
| Bruce Berkowitz | 13F A: FAIRHOLME CAPITAL MANAGEMENT, / FAIRHOLM | +1.55 (+0.13) | +9.2% / -3.9 | .827 | -1.55 (-0.26) | .446 | B |
| Li Lu | 13F A: HIMALAYA CAPITAL, L.L.C. | +1.37 (+0.22) | +15.7% / +2.6 | .820 | -0.79 (-0.12) | .612 | A (record) |
| Murray Stahl | fund F: Kinetics Mutual Funds, Inc: Paradigm Fund; No | +0.29 (+0.02) | +19.0% / +5.9 | .848 | +0.65 (+0.12) | .919 | A (record) |
| Alex Fitch | fund F: Harris Associates Investment Trust: Oakmark S | -0.33 (-0.09) | +14.2% / +1.1 | .797 | -0.62 (-0.39) | .786 | A (record) |
| Bill Nygren | fund F: Harris Associates Investment Trust: Oakmark F | -0.38 (-0.13) | +15.0% / +1.9 | .794 | +0.37 (+0.31) | .899 | A (record) |
| Matthew McLennan | fund F: First Eagle Funds: First Eagle US Fund; Class | -1.14 (-0.48) | +12.8% / -0.3 | .733 | -0.57 (-0.57) | .796 | B |
| David Einhorn | 13F B: GREENLIGHT CAPITAL INC / GREENLIGHT CAPI | -1.24 (-0.18) | +15.2% / +2.1 | .601 | -2.44 (-0.78) | .264 | control |
| Tobias Carlisle | fund F: ETF Series Solutions: Acquirers Fund | -2.32 (-0.70) | +11.0% / -2.1 | .606 | -5.37 (-1.35) | .053 | control |
| Seth Klarman | 13F A: BAUPOST GROUP INC / BAUPOST GROUP, INC.  | -3.10 (-0.74) | +6.3% / -6.7 | .283 | -4.59 (-1.24) | .106 | B |
| Arnold Van Den Berg | fund F: CM Advisors Family of Funds: CM Advisors Fund | n/a (0 months) | n/a | . | -3.13 (-0.78) | .222 | control |
| John Lennon | 13F A: PLEASANT LAKE PTNR LLC | n/a (34 months) | +3.6% / -19.0 | . | -13.00 (-1.66) | .018 | control |
| Soo Chuen Tan | 13F A: DISCERENE GROUP LP | n/a (58 months) | n/a | .925 | n/a | .947 | B |

## Growth

| Investor | Record | 2021-25 alpha (t) | 2021-25 return / vs market | 2021-25 rank | 2011-25 alpha (t) | 2011-25 rank | Tier |
|---|---|---|---|---|---|---|---|
| Alex Sacerdote | 13F A: WHALE ROCK CAPITAL MGMT LLC / WHALE ROCK | +10.51 (+1.78) | +12.6% / -0.5 | .958 | +8.18 (+2.98) | .959 | A (record) |
| Gavin Baker | 13F A: ATREIDES MANAGEMENT, LP | +8.22 (+1.30) | +11.8% / -1.2 | .940 | +10.16 (+1.82) | .970 | A (record) |
| Brad Gerstner | 13F A: ALTIMETER CAPITAL MGMT, LLC / ALTIMETER  | +4.51 (+0.48) | +1.8% / -11.3 | .897 | +4.88 (+0.89) | .928 | A (record) |
| Fred Martin | 13F A: DISCIPLINED GR INVESTORS, INC / DISCIPLI | -0.14 (-0.02) | +9.7% / -3.4 | .729 | +0.02 (+0.01) | .737 | A (record) |
| Philippe Laffont | 13F A: COATUE MANAGEMENT, LLC | -2.78 (-0.52) | +2.1% / -10.9 | .330 | +0.19 (+0.08) | .753 | A (record) |
| Thomas Laffont | 13F A: COATUE MANAGEMENT, LLC | -2.78 (-0.52) | +2.1% / -10.9 | .330 | +0.19 (+0.08) | .753 | A (record, shares with I056) |
| Cathie Wood | fund F: ARK ETF Trust: ARK Innovation ETF; ARK ETF Tr | -4.21 (-0.58) | -9.5% / -22.6 | .320 | +0.67 (+0.17) | .921 | A (record) |
| Henry Ellenbogen | 13F A: DURABLE CAPITAL PTNR LP | -10.31 (-1.68) | -2.3% / -15.4 | .034 | -10.51 (-1.99) | .030 | control |

## Long/short

| Investor | Record | 2021-25 alpha (t) | 2021-25 return / vs market | 2021-25 rank | 2011-25 alpha (t) | 2011-25 rank | Tier |
|---|---|---|---|---|---|---|---|
| Derek Pilecki | fund F: Caldwell & Orkin Funds, Inc: Gator Capital Lo | +7.92 (+2.01) | +21.0% / +7.9 | .988 | +3.92 (+1.24) | .985 | A (record) |
| Ricky Sandler | 13F B: EMINENCE CAPITAL, L.L.C. / EMINENCE CAPI | +1.64 (+0.45) | +11.3% / -1.7 | .830 | +3.56 (+1.97) | .907 | A (record) |
| Dan Sundheim | 13F B: D1 CAPITAL PTNR L.P. | -5.05 (-0.84) | +3.2% / -9.9 | .123 | -0.12 (-0.02) | .720 | A (record) |
| Jim Chanos | 13F B: KYNIKOS ASSOCIATES LP | n/a (20 months) | +9.7% / -17.7 | . | -4.35 (-2.46) | .113 | control |

## Special situations

| Investor | Record | 2021-25 alpha (t) | 2021-25 return / vs market | 2021-25 rank | 2011-25 alpha (t) | 2011-25 rank | Tier |
|---|---|---|---|---|---|---|---|
| Paul Singer | 13F A: ELLIOTT INTL CAP ADVISORS INC. / ELLIOTT | +9.22 (+1.81) | +25.5% / +12.4 | .950 | -0.54 (-0.17) | .657 | A (record) |
| Matt Mark | 13F A: JET CAPITAL INVESTORS, LP | -4.69 (-0.57) | +6.8% / -4.8 | .141 | -0.85 (-0.31) | .601 | A (record) |
| Dan Loeb | 13F A: THIRD POINT LLC / THIRD POINT MANAGEMENT | -6.23 (-1.54) | +4.3% / -8.8 | .084 | -1.89 (-0.85) | .368 | A (record) |

## No dominant style (macro-minded stock pickers)

| Investor | Record | 2021-25 alpha (t) | 2021-25 return / vs market | 2021-25 rank | 2011-25 alpha (t) | 2011-25 rank | Tier |
|---|---|---|---|---|---|---|---|
| Leon Cooperman | 13F A: OMEGA ADVISORS, INC. / OMEGA ADVR INC | +6.46 (+1.70) | +22.1% / +9.0 | .924 | -3.54 (-1.42) | .154 | A (record) |
| David Tepper | 13F A: APPALOOSA MANAGEMENT, L.P. / APPALOOSA M | +5.84 (+1.55) | +20.6% / +7.5 | .917 | +1.01 (+0.37) | .822 | A (record) |

## Not rankable (37 with a filing that says little, 151 with no record)
Grade C (a 13F exists but is not a stock-picking record): Howard Marks, Jeremy Grantham, Ray Dalio, Stan
Druckenmiller, Ken Griffin, Steve Cohen, Paul Tudor Jones, Dmitry Balyasny, Paul Marshall, Ken Fisher, David Booth,
Mohnish Pabrai (median 4 positions), Vitaliy Katsenelson, private-equity and venture firms and others; their numbers
are in the report but they take no place by record. Grade N: authors, hosts, analysts, executives, and managers inside
large firms or outside the US without a CRSP fund.

## Reading order produced (tiers)
- Tier A by record (30): Sacerdote, Baker, Pilecki, Vinall, Dorsey, Stahl, Sandler, Hohn, Gerstner, Tepper, Greenblatt,
  Begg, Nygren, Rosen, Robotti, Fitch, Martin, Kantesaria, Singer, Bloomstran, Li Lu, Spier, Wood, Russo, Watsa,
  P. Laffont (T. Laffont with him), Cooperman, Sundheim, Mark, Loeb. The last three entered because the style caps
  filled the quality and value places; their scores are low.
- Tier A by explicit criteria (10): Damodaran, Kupperman, Donville, Gamble, Andreola, Goldstein, Brenton, Haley,
  Cassel, Rochon.
- Control (10, random): Carlisle, Einhorn, Shaposhnik, Buffett, Van Den Berg, Elfenbein, Ellenbogen, Chanos, Lennon,
  Keefe. They go through the same pipeline; no agent is told who is control.
- Foundation list: 50 technique documents (ids in the report).
- Soo Chuen Tan (Discerene) has the best deep-value score (.93) but only 58 months of record, two short of the
  registered 60, so he is in tier B.

## Top-ranked managers with no transcript in the library (candidates to add)
13F filers: mostly biotech specialists (Arch Venture, Fairmount, Aisling, Great Point, venBio, Bain Capital Life
Sciences, Sofinnova), plus Cota, Stonepine, Keywise, Exor, L1 Capital, Cape Ann, MAK Capital, CAS. Funds: sector and
theme funds (semiconductors, blockchain, gold) and Invenomic. The six-factor alpha does not take out industry bets,
so sector funds that rode one industry top this list; it is a list to look at, not a list of the skilled.

## After the result
- Stanley Druckenmiller added to the reading list by the user after seeing the result (grade C by the registered
  rule: his library transcripts are macro; his 13F stock book scored .922). Outside tier A; no effect on the control.
- The size-filtered list of managers without a transcript (Addendum A) was registered, built and checked, then
  cancelled before it ran; the user looks for further managers outside the scorecard.

## Limits
- Five years cannot separate skill from luck (see the persistence result); the style cap and the control group are
  there for that reason.
- 13F copies miss shorts, cash, non-US holdings and timing inside the quarter; Grade B records show only the long US part.
- Peer groups covered on average 49-65% of copy-portfolio value (ADRs, funds and stocks without book value have none),
  so the peer-adjusted column is weaker than the alpha.
- These are US years 2011-25: under the plan they are never proof for any family built from these investors.
