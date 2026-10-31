# Global Macro Book (paper) - gm-1.2.0

Positions decided at the end of **2026-09**; built 2026-10-31 03:57 UTC. Paper research only, not investment advice.

## Backtest record (design and extra-check periods only; holdout 2011-2026 not run yet)
```
1975..1989 gross      ret 10.4% vol 10.5% SR 0.99 maxDD -20% worst12m -16% corrSPX 0.21
1975..1989 net        ret 9.8% vol 10.5% SR 0.93 maxDD -21% worst12m -16% corrSPX 0.21
1975..1989 net 2xcost ret 9.1% vol 10.5% SR 0.87 maxDD -21% worst12m -17%
1990..2010 gross      ret 15.4% vol 9.8% SR 1.56 maxDD -12% worst12m -10% corrSPX -0.06
1990..2010 net        ret 14.2% vol 9.8% SR 1.45 maxDD -12% worst12m -11% corrSPX -0.06
1990..2010 net 2xcost ret 13.0% vol 9.8% SR 1.33 maxDD -13% worst12m -11%
```

## Current positions (risk = notional x annual vol; book targets 10% vol; 62 markets)

| Market | Notional | Risk | Trend | Econ | Carry | Value | XS mom |
|---|---|---|---|---|---|---|---|
| bd_de_10y | -0.24 | -1.44% | -0.25% | -0.28% | +0.05% | -0.86% | -0.10% |
| fx_chf | -0.14 | -1.24% | -0.31% | -0.28% | -0.42% | -0.10% | -0.14% |
| fx_krw | +0.10 | +1.03% | +0.31% | +0.21% | -0.19% | +0.68% | +0.03% |
| fx_gbp | -0.14 | -0.95% | -0.10% | -0.24% | -0.10% | -0.48% | -0.03% |
| st_jp_2y | -1.56 | -0.88% | -0.25% | -0.63% | -0.10% | +0.00% | +0.10% |
| bd_jp_10y | -0.23 | -0.86% | -0.25% | -0.63% | +0.20% | +0.00% | -0.18% |
| fx_eur | -0.12 | -0.85% | -0.31% | +0.07% | -0.24% | -0.29% | -0.08% |
| fx_nzd | -0.07 | -0.76% | -0.31% | -0.30% | -0.15% | +0.00% | +0.00% |
| fx_sek | -0.07 | -0.76% | -0.31% | -0.30% | -0.33% | +0.29% | -0.11% |
| bd_ca_10y | -0.12 | -0.73% | -0.25% | -0.29% | +0.29% | -0.43% | -0.05% |
| bd_au_10y | -0.11 | -0.67% | -0.25% | -0.28% | -0.01% | +0.00% | -0.13% |
| cm_natgas | -0.01 | -0.57% | -0.44% | -0.04% | +0.00% | +0.00% | -0.08% |
| st_au_2y | -0.38 | -0.55% | -0.25% | -0.28% | -0.07% | +0.00% | +0.05% |
| bd_us_30y | +0.04 | +0.54% | -0.25% | -0.23% | +0.32% | +0.86% | -0.15% |
| eq_hk_hsi | +0.03 | +0.54% | +0.07% | -0.03% | +0.00% | +0.50% | -0.00% |
| eq_us_spx | -0.04 | -0.52% | +0.07% | -0.09% | +0.00% | -0.50% | +0.00% |
| st_de_2y | -0.36 | -0.49% | -0.25% | -0.28% | -0.04% | +0.00% | +0.08% |
| cm_wti | +0.01 | +0.49% | +0.44% | -0.04% | +0.00% | +0.00% | +0.08% |
| cm_coffee | -0.01 | -0.48% | -0.44% | -0.04% | +0.00% | +0.00% | +0.00% |
| cm_cattle | -0.03 | -0.48% | -0.44% | -0.04% | +0.00% | +0.00% | +0.00% |
| cm_brent | +0.01 | +0.47% | +0.44% | -0.04% | +0.00% | +0.00% | +0.07% |
| eq_gb_ftse | +0.05 | +0.46% | -0.07% | +0.16% | +0.00% | +0.36% | +0.01% |
| fx_aud | +0.05 | +0.45% | +0.10% | +0.01% | +0.26% | +0.00% | +0.08% |
| eq_de_dax | -0.04 | -0.44% | -0.07% | -0.13% | +0.00% | -0.22% | -0.01% |
| cm_soybeans | +0.02 | +0.40% | +0.44% | -0.04% | +0.00% | +0.00% | +0.00% |
| cm_heatoil | +0.01 | +0.40% | +0.44% | -0.04% | +0.00% | +0.00% | +0.00% |
| eq_in | -0.03 | -0.39% | -0.22% | -0.10% | +0.00% | +0.00% | -0.07% |
| eq_jp_nikkei | -0.03 | -0.39% | +0.07% | -0.16% | +0.00% | -0.36% | +0.06% |
| st_ca_2y | -0.26 | -0.34% | -0.25% | -0.29% | +0.02% | +0.00% | +0.18% |
| bd_us_5y | -0.08 | -0.34% | -0.25% | -0.23% | +0.17% | +0.00% | -0.03% |
| eq_au_asx | -0.03 | -0.31% | -0.22% | -0.25% | +0.00% | +0.22% | -0.05% |
| eq_br_ibov | +0.02 | +0.29% | +0.22% | +0.11% | +0.00% | +0.00% | -0.04% |
| eq_tw | +0.01 | +0.28% | +0.22% | -0.01% | +0.00% | +0.00% | +0.07% |
| fx_nok | +0.03 | +0.28% | +0.10% | -0.24% | +0.26% | +0.10% | +0.05% |
| st_us_2y | -0.15 | -0.25% | -0.25% | -0.23% | +0.10% | +0.00% | +0.14% |
| bd_us_2y | -0.15 | -0.25% | -0.25% | -0.23% | +0.10% | +0.00% | +0.14% |
| fx_zar | +0.03 | +0.24% | +0.10% | -0.35% | +0.38% | +0.00% | +0.11% |
| eq_za | -0.01 | -0.23% | -0.22% | +0.03% | +0.00% | +0.00% | -0.03% |
| eq_cn | -0.01 | -0.19% | -0.07% | -0.03% | +0.00% | +0.00% | -0.08% |
| eq_eu_stoxx50 | -0.02 | -0.18% | -0.07% | -0.13% | +0.00% | +0.00% | +0.02% |
| cm_cotton | +0.01 | +0.15% | +0.15% | -0.04% | +0.00% | +0.00% | +0.05% |
| eq_mx_ipc | -0.01 | -0.15% | -0.22% | +0.14% | +0.00% | +0.00% | -0.06% |
| cm_silver | +0.00 | +0.13% | +0.15% | -0.04% | +0.00% | +0.00% | +0.03% |
| eq_us_r2k | -0.01 | -0.12% | -0.07% | -0.09% | +0.00% | +0.00% | +0.04% |
| cm_wheat | +0.01 | +0.12% | +0.15% | -0.04% | +0.00% | +0.00% | +0.01% |
| fx_jpy | +0.01 | +0.11% | +0.10% | +0.55% | -0.38% | +0.00% | -0.16% |
| cm_gasoline | +0.00 | +0.11% | +0.15% | -0.04% | +0.00% | +0.00% | +0.00% |
| cm_sugar | +0.00 | +0.11% | +0.15% | -0.04% | +0.00% | +0.00% | +0.00% |
| fx_cad | -0.02 | -0.10% | -0.31% | +0.06% | -0.28% | +0.48% | -0.05% |
| bd_us_10y | +0.01 | +0.10% | -0.25% | -0.23% | +0.23% | +0.43% | -0.08% |
| cm_copper | +0.00 | +0.10% | +0.15% | -0.04% | +0.00% | +0.00% | -0.01% |
| st_gb_5y | -0.02 | -0.09% | -0.25% | -0.01% | +0.14% | +0.00% | +0.03% |
| eq_fr_cac | -0.01 | -0.08% | -0.07% | -0.06% | +0.00% | +0.07% | -0.02% |
| cm_corn | +0.01 | +0.08% | +0.15% | -0.04% | +0.00% | +0.00% | -0.03% |
| fx_brl | -0.01 | -0.07% | +0.31% | -0.29% | +0.42% | -0.68% | +0.16% |
| cm_gold | +0.00 | +0.06% | +0.15% | -0.04% | +0.00% | +0.00% | -0.05% |
| fx_mxn | -0.01 | -0.05% | -0.10% | -0.41% | +0.33% | +0.00% | +0.14% |
| cm_platinum | +0.00 | +0.04% | +0.15% | -0.04% | +0.00% | +0.00% | -0.07% |
| eq_ca_tsx | -0.00 | -0.03% | +0.07% | -0.09% | +0.00% | -0.07% | +0.05% |
| eq_us_ndx | +0.00 | +0.02% | +0.07% | -0.09% | +0.00% | +0.00% | +0.03% |
| eq_kr_kospi | -0.00 | -0.00% | -0.07% | -0.01% | +0.00% | +0.00% | +0.08% |
| bd_gb_10y | -0.00 | -0.00% | -0.25% | -0.01% | +0.26% | +0.00% | +0.00% |

Gross notional and net risk by class: EQ 0.35x / -1.4%, FI 3.72x / -6.3%, FX 0.78x / -2.7%, CM 0.14x / +1.1%

## Exposure of today's positions (last 36 months of market moves)
Betas: equity (S&P 500) -0.02, bonds (US 10y) -0.65, US dollar +0.49, commodities +0.30; explained by these factors 83%, residual (the book's own risk) 17%.

Stress test: P&L of today's positions if past market moves repeated (book targets 10% annual vol):
- 2008 Lehman (Sep-Dec 2008): -6.2% (62 of 62 positions had data)
- 2020 Covid (Feb-Mar 2020): -0.0% (62 of 62 positions had data)
- 2022 rates shock (Jan-Oct 2022): +22.5% (62 of 62 positions had data)
- 1994 bond rout (Feb-Nov 1994): +6.9% (34 of 62 positions had data)

## Family risk shares (fixed)
trend 30%, econ 30%, carry 20%, value 15%, xsmom 5%

## Placeholders (not yet in this version)
- BLOOMBERG commodity curves and pre-2000 commodity returns
- EQUITY value for emerging markets (only DM + US by dividend yield so far); equity carry (failed)
- WRDS revisions (research only)
- Early-warning risk scaler (tested, not adopted)
- Econ growth theme on first-release data (left out in v1.1)

## Data flags

- eq_us_ndx: div proxy before ETF
- eq_us_r2k: div proxy before ETF
- eq_eu_stoxx50: div proxy before ETF
- eq_gb_ftse: div proxy before ETF
- eq_fr_cac: div proxy before ETF
- eq_jp_nikkei: div proxy before ETF
- eq_ca_tsx: div proxy before ETF
- eq_au_asx: div proxy before ETF
- eq_hk_hsi: div proxy before ETF
- eq_cn: div proxy before ETF
- eq_kr_kospi: div proxy before ETF
- eq_tw: div proxy before ETF
- eq_in: div proxy before ETF
- eq_br_ibov: div proxy before ETF
- eq_mx_ipc: div proxy before ETF
- eq_za: div proxy before ETF
- cm_wti: unadjusted front future (roll gaps)
- cm_brent: unadjusted front future (roll gaps)
- cm_natgas: unadjusted front future (roll gaps)
- cm_heatoil: unadjusted front future (roll gaps)
- cm_gasoline: unadjusted front future (roll gaps)
- cm_gold: unadjusted front future (roll gaps)
- cm_silver: unadjusted front future (roll gaps)
- cm_copper: unadjusted front future (roll gaps)
- cm_platinum: unadjusted front future (roll gaps)
- cm_corn: unadjusted front future (roll gaps)
- cm_wheat: unadjusted front future (roll gaps)
- cm_soybeans: unadjusted front future (roll gaps)
- cm_sugar: unadjusted front future (roll gaps)
- cm_coffee: unadjusted front future (roll gaps)
- cm_cotton: unadjusted front future (roll gaps)
- cm_cattle: unadjusted front future (roll gaps)
- cm_aqr_ew: index-level, pre-2001 only
- sp_us_breakeven10: no TIPS before 2003

## Signal families alone (design period)
```
Signal families alone, gross, monthly; design 1990-2010 and extra check 1975-89 (holdout not shown)
  trend  1975..1989  ALL SR 1.13 (t 4.4) | EQ SR 0.19 (t 0.7) | FI SR 1.08 (t 4.2) | FX SR 0.90 (t 3.5) | CM SR 0.32 (t 1.2)
  trend  1990..2010  ALL SR 1.18 (t 5.4) | EQ SR 0.50 (t 2.3) | FI SR 0.87 (t 4.0) | FX SR 0.96 (t 4.4) | CM SR 0.56 (t 2.5)
  econ   1975..1989  ALL SR 0.37 (t 1.4) | EQ SR -0.04 (t -0.2) | FI SR 0.51 (t 2.0) | FX SR -0.03 (t -0.1) | CM SR 0.42 (t 1.6)
  econ   1990..2010  ALL SR 0.58 (t 2.6) | EQ SR 0.63 (t 2.9) | FI SR 0.29 (t 1.3) | FX SR 0.46 (t 2.1) | CM SR -0.12 (t -0.6)
  carry  1975..1989  ALL SR 0.30 (t 1.1) | EQ SR -0.49 (t -1.8) | FI SR 0.92 (t 3.6) corrAQR 0.29 | FX SR 0.14 (t 0.6) corrAQR 0.35 | CM SR 0.58 (t 1.2) corrAQR -0.09
  carry  1990..2010  ALL SR 0.92 (t 4.2) | EQ SR -0.01 (t -0.0) | FI SR 0.75 (t 3.5) corrAQR 0.36 | FX SR 0.76 (t 3.5) corrAQR 0.43 | CM SR 0.36 (t 1.7) corrAQR 0.24
  carryD 1975..1989  ALL SR 0.33 (t 1.3) | EQ SR -0.60 (t -2.2) | FI SR 0.91 (t 3.5) | FX SR 0.19 (t 0.7) | CM SR 0.58 (t 1.2)
  carryD 1990..2010  ALL SR 0.87 (t 4.0) | EQ SR -0.07 (t -0.3) | FI SR 0.64 (t 2.9) | FX SR 0.73 (t 3.3) | CM SR 0.44 (t 2.0)
  carryX 1975..1989  ALL SR 0.09 (t 0.4) | EQ SR -0.21 (t -0.8) | FI SR 0.41 (t 1.6) corrAQR 0.25 | FX SR 0.06 (t 0.2) corrAQR 0.49 | CM n/a
  carryX 1990..2010  ALL SR 0.79 (t 3.6) | EQ SR 0.15 (t 0.7) | FI SR 0.71 (t 3.3) corrAQR 0.48 | FX SR 0.61 (t 2.8) corrAQR 0.27 | CM SR 0.06 (t 0.2) corrAQR 0.09
  value  1975..1989  ALL SR -0.12 (t -0.5) | EQ SR -0.39 (t -1.4) corrAQR 0.25 | FI SR 0.58 (t 2.1) corrAQR -0.01 | FX SR -0.28 (t -1.0) corrAQR 0.16 | CM n/a
  value  1990..2010  ALL SR 0.14 (t 0.6) | EQ SR 0.26 (t 1.2) corrAQR 0.47 | FI SR 0.06 (t 0.3) corrAQR 0.45 | FX SR 0.39 (t 1.8) corrAQR 0.29 | CM SR -0.62 (t -2.1) corrAQR 0.25
markets with a signal 1990-2010: {'econ': np.int64(63), 'carry': np.int64(40), 'value': np.int64(31)}
```
