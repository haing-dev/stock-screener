---
tags: [fable, thesis]
code_commit: 78799ed
---
> Step 3.1 spec, approved with corrections at 3.2. Inputs: _data/spec_3.1/. Register: [[Thesis register 1.5]]. Source: [repo file](https://github.com/haing-dev/stock-screener/blob/78799edd251d9e74a749bd23aa6fc507e9a99d0c/docs/research/specs/SPEC_Economic_trend.md).
# SPEC: Economic trend (step 3.1, Agent A, 2026-11-23)

> **Status (2026-11-23): APPROVED WITH CORRECTIONS at step 3.2.** Written at step 3.1 (Opus, agent A); checked by a
> fresh Opus agent (checks/CHECK_3.2_A.md); its 8 corrections to this spec are applied. Claim ids and quotes
> script-checked (ALL OK). Nothing registered or run; open items go to step 3.4 (check section 4, NOTES_3.1_agent_A.md).

Engine read: gm-1.2.2 / gm-2.0.2-candidate (gm/signals.py, book.py, config.py, panel.py, vol.py), read only. Nothing run.

## 0. Header
- Pod: Economic trend. Type: existing pod.
- Register rows: T02 (pod); T10 (short-rate futures strips, gated market set, shared with Trend and Carry). Dropped
  rows that name this pod: T37 (forecast themes), T63, T75, T84, T97, T99, T106 (card items "held by Economic trend").
- Source notes: CHARTER_1.2 s2 row 7, s3 Economic trend, s4, s5 D5, s6, s11 and its check (tables B, C item Y, D);
  foundation U01 (= F1_economic_trend, pre-audit; where it differs, the charter's check-corrected text is final);
  THESIS_1.3_rates s4 (T10); THESIS_1.3_method P3.
- Register status: existing book; grid in Batch A2; spec text gated by D5.
- Dating class: C. Sources are 2017 and 2023 ("as Brooks (2017)", [[QP01 - Economic Trend (AQR Brooks, Feilbogen, Ooi, Akant, April 2023)#^QP01-C03-7|QP01-C03-7]]; 2023 from TESTING_PROTOCOL); the
  paper's pre-2011 citations support single signs only; no candidate for the combined rule. Rule 5 then allows: no
  holdout verdict; the pod is hindsight-flagged, so by WORKFLOW s5 it cannot be Core and runs as Incubator at best.
  That would take 15% (CANDIDATE) or 30% (BASE) of the traded book out untested (charter JP6): consequence at 3.4.

## 1. Economic claim
Prices react late to macro news: "Its persistent profitability stems from the tendency of asset prices to systematically underreact to new information" ([[QP01 - Economic Trend (AQR Brooks, Feilbogen, Ooi, Akant, April 2023)#^QP01-C02-3|QP01-C02-3]]),
so the 12-month change of a macro theme, signed by theory, predicts each market's return with the same sign as the
same-month link: "contemporaneous and predictive relationships between returns and news must have the same sign" ([[QP01 - Economic Trend (AQR Brooks, Feilbogen, Ooi, Akant, April 2023)#^QP01-C04-8|QP01-C04-8]]).
Who pays (the slow side) is not named. U01 reads the result as cross-asset price momentum (reader).
Evidence grade, as the charter gives it (row 7, after its check): "Result summary only" (Sharpe figures are chart
reads in claim text); cause ASSERTED. U01's earlier "SHOWN, moderate strength" is superseded.
D5 sets the final wording: if the edge fades with delay, the claim is "slow reaction"; else "a lasting macro state".

## 2. What is predicted
- Quantity: each market's next-month excess return (panel.py excess returns).
- Sign: theme sign x the sign of its 12-month change, averaged over the themes present (section 3).
- Largest: when prices "cue off fundamental news again" ([[QP01 - Economic Trend (AQR Brooks, Feilbogen, Ooi, Akant, April 2023)#^QP01-C03-6|QP01-C03-6]]) and macro themes move a lot; weakest when "returns are disconnected from changes in fundamentals (as can happen)" ([[QP01 - Economic Trend (AQR Brooks, Feilbogen, Ooi, Akant, April 2023)#^QP01-C03-6|QP01-C03-6]]).

## 3. Signal
Code now (signals.py:94-98 zchg, :202-220 themes, :223-228 SIGNS, :231 ECON_THEMES, :235-261 econ_scores; book.py:107
kind "dir"). Four themes are coded: inflation, trade, monetary, risk. There is NO growth theme: ECON_THEMES excludes
it, GROWTH_PIT is False and GROWTH_SOURCE is off (signals.py:179-180, 231; config.py BASE econ_themes); the
growth series computed in themes() (signals.py:205-210) never enters a score. Steps, per country cc, at month-end t:
1. zchg(x) = (x(t) - x(t-12)) / standard deviation of that 12-month change over the last 120 months (at least 36),
   clipped to [-3, 3]; no mean removed.
2. Inflation = zchg(OECD CPI year-on-year rate, FRED CPALTT01 fallback; euro uses Germany) lagged 1 month.
3. Trade = zchg(-ln BIS nominal effective exchange rate; the euro uses Germany's index NBDEBIS, because the euro's themes are Germany's, signals.py:255 with FX_MACRO, and the map BIS EZ -> XM at signals.py:43 is never reached) lagged 1 month (positive =
   currency weakening).
4. Monetary = zchg(2-year yield at month end for US, DE, CA, AU, JP; else the OECD 3-month rate of the previous month;
   spliced, the 2-year yield first) with no further lag (positive = tightening).
5. Risk = mean of (a) the 12-month sum of the first listed index's monthly excess return for cc (signals.py EQ_CC
   order; for DE that is eq_eu_stoxx50, not eq_de_dax, so Germany's risk theme, which also serves fx_eur and the commodity block, is the credit part alone until about 2003-07; CN uses eq_hk_hsi, KR eq_kr_kospi; the mean takes the parts present) over its 120-month standard deviation (at least 36) x sqrt(12), clipped to [-3, 3], and (b)
   zchg(-BAA10YM) lagged 1 month (US Baa spread for every country) (positive = falling risk aversion).
6. Market mapping: equity index -> its country; bond or note -> its country (signals.py BD); currency -> local theme
   minus US theme (the currency's macro country); commodity -> equal mean of the US, DE, JP and CN themes.
7. Signs (AQR Exhibit 1, signals.py:223-228): EQ inflation -1, trade +1, monetary -1, risk +1; FI all -1; FX
   inflation +1, trade -1, monetary +1, risk +1; CM inflation +1, trade -1, monetary -1, risk +1.
8. Version shape f: "tanh" f(z) = tanh(z / 2) (today); "sign" f(z) = sign(z), 0 if z = 0 (closed here: the charter's
   "its sign" read as the sign of each theme's scaled change, the simplest form).
9. Score = mean over themes with a value of sign x f(z); no score unless at least 2 themes have a value.
10. Version position = score x 0.40 / vol (CANDIDATE hybrid estimate, as for every pod but Trend; charter s4 Fixed),
    divided by the count of markets in the class with a position. Pod position = mean of the two versions, a missing
    version counted as 0.
11. Rebalancing: month-end decision, traded the first trading day after; tranches as in SPEC_Trend section 3 (weekly
    check only).
The theme signs are fixed by the source and cannot change after results (charter s5, U01-T2 dropped).
As-of rule: only values public at month-end t. Closed here: where a country's OECD CPI series is quarterly in the
design years (to check as metadata: AU, NZ), a quarter's value enters at the end of the month after the quarter ends,
not by the 1-month lag; this is a look-ahead fix to register in gm/CHANGES.md before A1 (step 3.4).

## 4. Markets
All non-alternative ids with a signal: EQ 18, FI 14, FX 13, CM 16 (not cm_aqr_ew: book.py:121-122). Market list and
first return months as SPEC_Trend section 4. A market's first position needs at least 2 themes with 36 months of
12-month changes (about 48 months of the theme series) and a volatility estimate; commodity markets therefore start
with their returns (the earliest is cm_wti 1985-02). Through a gate only: T10 strips (D1 extension at 3.4; FI signs,
themes of the strip's country, as signals.py BD maps st_de_2y to DE).

## 5. Sizing
As SPEC_Trend section 5 (0.40 / vol, equal weight in class, unit-vol class blocks, book target 10%, caps). Pod share:
config.py BASE econ 0.30, CANDIDATE 0.15; WORKFLOW 5.1 "Core pods at equal risk": they disagree; 3.4 decides. If rule 5
makes the pod Incubator, its share leaves the traded book (3.4).

## 6. Version grid
| v | Shape f | Everything else |
|---|---|---|
| 1 | tanh(z / 2) | as section 3 |
| 2 | sign(z) | as section 3 |
Total 2, averaged with equal weight. None opened by a diagnostic. Not versions (closed in section 15): equity momentum
in the risk theme; growth.

## 7. Sample
Design window 1975-01 to 2010-12; markets enter as section 4 says; months before a position are flat. Eras 1975-89,
1990-2010. No month after 2010-12.

## 8. Data
| Input | History | Live (delay) | Licence |
|---|---|---|---|
| CPI year-on-year | OECD csv / FRED CPALTT01, latest vintage (revised), 1975 or earlier for most | same, about 1 month | free |
| Nominal effective exchange rate | BIS via FRED NB..BIS, monthly average | same, 1 month | free |
| 2-year yields | FRED DGS2 (1976-06), Bundesbank, BoC, RBA, MoF Japan files, month end | same, 1 day | free |
| 3-month rates | OECD IR3TIB01 / TB3MS, monthly average | same, 1 month; GB and euro-area OECD series end 2026-01 and are carried forward at most 12 months (panel.py:368-370) | free |
| Baa spread | FRED BAA10YM, monthly average | same, 1 month | free |
| Equity excess returns | panel | panel, 1 day | free |
| T10 strips | LSEG, not locked | LSEG only | not registered |
Rule 7: every input has a free live source, so the pod passes rule 7 (the GB and euro 3-month rates need a
replacement source before 2027-01: 3.4). History uses revised values, lagged to release, not first releases (register D12).
Rule 5, not rule 7, keeps it from Core.

## 9. Costs
As SPEC_Trend section 9 (book.py:46-57 by class, rolls, EM borrow); double-cost test applies. The notes give no
turnover figure.

## 10. What would prove it wrong (design window)
- The averaged pod's net return is zero or below in both eras.
- Not a design-window test (D5 picks the reading the design data agree with, so neither line can fail on 1975-2010); both lines bind the holdout report and the live record only. If D5 makes the claim "slow reaction": no fading with delay (Sharpe at 3 months' delay at least half the no-delay
  Sharpe) proves it wrong. If D5 makes it "a lasting state": a large fade with delay contradicts it.
- The news reading fails if the profit comes only from the price-built parts. Reported split, closed here: the score is
  a mean of theme parts and never exceeds 1 in size, so each theme's part of the position is exact (part / themes
  present x 0.40 / vol / n); if the inflation part (the only part built from an official statistic) earns zero or less
  in both eras while the others earn, the result is cross-asset price momentum, not under-reaction to economic news.
- Loss event (P3): prices detached from fundamentals; the paper names "June 1999 and December 2000" ([[QP01 - Economic Trend (AQR Brooks, Feilbogen, Ooi, Akant, April 2023)#^QP01-C09-5|QP01-C09-5]]),
  inside the window. Not flagged.

## 11. When it should stop working (live)
- Prices disconnected from fundamentals for long ([[QP01 - Economic Trend (AQR Brooks, Feilbogen, Ooi, Akant, April 2023)#^QP01-C03-6|QP01-C03-6]], C09-5).
- Quiet macro data and pinned or guided policy rates: the 12-month change of 2-year yields near zero mutes the
  monetary theme (reader, U01 s7).
- More capital in the same signals (reader, U01 s7). Live bands: W5, numbers at 3.4.

## 12. Knobs that were tuned
| Knob | Value | Origin |
|---|---|---|
| Themes | 4, growth off | growth left out after design results (gm_CHANGES gm-1.1.0: family 0.71 -> 0.60, already seen); point-in-time growth trial seen (gm_CHANGES trial log 10) |
| Risk theme content | equity 12-month return + credit | source ([[QP01 - Economic Trend (AQR Brooks, Feilbogen, Ooi, Akant, April 2023)#^QP01-C04-5|QP01-C04-5]]); credit-only already seen and rejected (gm_trials.csv cand2 econ risk=credit only) |
| Structure | one score per market | E1 theme blocks already seen and rejected (protocol_batch1.md) |
| 12-month change | 12 | source paper |
| z scale, cap | 120-month sd (min 36), cap 3 | engine convention |
| Shape | tanh(z/2); sign | grid (tanh: engine convention; source silent) |
| At least 2 themes | 2 | engine convention |
| Signs | Exhibit 1 | source ([[QP01 - Economic Trend (AQR Brooks, Feilbogen, Ooi, Akant, April 2023)#^QP01-C04-6|QP01-C04-6]], title quote; values in code); monetary sign conflict resolved for Exhibit 1 (U01 s4) |
| Lags | CPI 1, NEER 1, credit 1, 3-month rate 1, yields 0 | engine convention (gm-1.2.0 audit) |
| Commodity themes | equal mean US, DE, JP, CN | engine convention (paper: consumption weights) |
| Pod share | 0.30 / 0.15 | 0.15 adopted after design results (protocol_batch0.md B0.2); book level |
Chosen or kept after seeing design results, fixed: growth off, risk-theme content, one score per market = 3 (+3 book: pod share, no risk scaler, no scenario limit; SPEC_Trend section 12).

## 13. Gating diagnostics
- D5 (charter): Economic trend alone, net, positions 0, 1, 3, 6, 12 months late. Gate: Sharpe at 3 months' delay under
  half the no-delay Sharpe -> claim "slow reaction", falsifier "no fading with delay"; else claim
  "a lasting macro state". Reads no sealed month (returns only to 2010-12). Caution (JP8, 3.4): 9 of 12 months overlap at a 3-month
  delay, so D5 may not separate the readings.
- D1 extension (3.4): gates T10 strip markets, as SPEC_Trend section 13.

## 14. Overlaps (re-checked in signals.py)
| Item | Code fact | Measure at |
|---|---|---|
| Trend (C11) | risk theme = half the country index's own 12-month return, exact for 13 of 18 indexes | A2 report |
| No growth theme (C1; T63, T75, T84, T97, T99, T106) | growth-based items (falling growth so long bonds; weak growth with hot inflation; large recession so short oil; China reopening) are NOT held; nor is T75's cross-country bond spread (the pod is directional per market) | 3.2 re-checks each card claim |
| Rising inflation: short stocks and bonds, long commodities | held directionally: EQ -1, FI -1, CM +1 on the 12-month change of the headline (all-items) CPI inflation rate (not its level, not surveys); core inflation is not an input, so a core-only rise (T84's core point, passed to this spec) is not held | card D2s at B2 |
| T23 card 3 R1 (C2) | FX monetary theme = local minus US 12-month change of the 2-year yield or 3-month rate, sign +1: about one quarter of the currency score | card 3 D1 at B2, against this pod's positions |
| T17 card 1 R5 (C3) | trade theme: EQ +1 after the trade-weighted currency weakens; FI -1, where R5's bond version buys | card 1 D2 |
| T21 card 2 R2 (C4) | EQ monetary -1: short US equities after a 12-month rise in the US 2-year yield; partial overlap | card 2 D2 |
| T16 card 1 R4, T20, T25 | partial at most: FI inflation -1 and monetary -1 short bonds after a 12-month rise in inflation or yields, while these rules fire on levels (core inflation above 5% with Fed funds below it; real yield below a bar; priced easing with core PCE above 3), and T25 needs the 2-year yield 0.5 below Fed funds, a state the pod does not read | card D2s |
| T32 card 4 R5 | falling CPI change -> FI long on both maturities (inflation theme), so only R5's long 2-year leg agrees; its short 10-year leg is opposite | card 4 D2 |
| T10, T11 | strips would take FI signs | D1 extension |

## 15. Open choices
| Choice | Closed as |
|---|---|
| Equity momentum in the risk theme as a version (charter JP4) | rule: kept as coded; the source builds the risk theme from equity returns on purpose "From 1970 through November 1987 risk aversion is represented entirely by 12-month equity market momentum" ([[QP01 - Economic Trend (AQR Brooks, Feilbogen, Ooi, Akant, April 2023)#^QP01-C04-13|QP01-C04-13]]); overlap reported (section 14). |
| Sign shape | version 2, defined in section 3 step 8. |
| Quarterly CPI lag | rule in section 3 (as-of), registered as an engine fix at 3.4. |
| GB and euro 3-month rates after 2026-01 | 3.4 (live source). |
| Rule 5 and the Incubator consequence (JP6) | 3.4. |
| Card claims of "held by Economic trend" | 3.2 (code facts in section 14). |
| Register vs note | none found: the register's T02 text matches the charter's corrected text. |

## 16. Builder must not change
The four themes and their signs; no growth theme; 12-month change, 10-year scale, cap 3; the two shapes, averaged;
lags and as-of rule; market mapping; design window and eras; free data sources; costs.

