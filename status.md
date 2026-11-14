# Triage run 43552230306
event: schedule · step: auto · history_years: 2 · finished: 2026-11-14 03:34 UTC
job status: success

```
Triage steps: mark, exits, build, site
== mark
Mark-to-market: 2026-11-12 (12596 closes)
== exits
Exits: 0 replaced with the last close (44 lookups); 44 still at -30%
== build
Triage build over 45 months (2024-12-13 .. 2026-10-15)
  events through 2025-11-28: hidden 509, emerging 194, core 274
  events through 2026-10-15: hidden 1010, emerging 365, core 504
  13F covered through 2026-08-31 (244894 conviction positions); insider data sets through 2026-09-30
  hidden: 1010 events, 407 with a full year, overdone 213, close 265, justified 532, tbu 0
  emerging: 365 events, 164 with a full year, overdone 108, close 181, justified 76, tbu 0
  core: 504 events, 225 with a full year, overdone 216, close 221, justified 67, tbu 0
  live calls: 122 before, 0 new
== site
Site: 1879 events in 3 triages -> /home/runner/work/stock-screener/stock-screener/triage_site
```

## Built data
scans ['2024-12-13', '2026-10-15'] · prices to 2026-11-12
- hidden: 1010 events, 407 with a full year, {'overdone': 213, 'close': 265, 'justified': 532, 'tbu': 0}
- emerging: 365 events, 164 with a full year, {'overdone': 108, 'close': 181, 'justified': 76, 'tbu': 0}
- core: 504 events, 225 with a full year, {'overdone': 216, 'close': 221, 'justified': 67, 'tbu': 0}

### hidden
- overdone: n 93, median 23.3%, mean 35.2%, similar 27.8%, index 24.1%, beat similar 53%
- close: n 99, median 16.1%, mean 40.2%, similar 27.3%, index 22.3%, beat similar 48%
- justified: n 215, median 18.4%, mean 55.8%, similar 43.1%, index 22.5%, beat similar 46%
- regression overdone: 20 months, alpha 23.5%/yr (t 3.25), betas {'Mkt-RF': [0.65, 5.4], 'SMB': [1.4, 6.9], 'HML': [-0.64, -2.0], 'RMW': [0.37, 1.8], 'CMA': [0.29, 1.4], 'UMD': [-0.34, -2.2]}
- regression close: 21 months, alpha 24.2%/yr (t 3.53), betas {'Mkt-RF': [0.81, 3.2], 'SMB': [1.34, 3.4], 'HML': [-1.02, -2.8], 'RMW': [0.22, 1.1], 'CMA': [0.17, 0.4], 'UMD': [-0.03, -0.2]}
- regression justified: 21 months, alpha 20.9%/yr (t 2.15), betas {'Mkt-RF': [1.09, 3.5], 'SMB': [0.54, 2.0], 'HML': [-0.24, -0.5], 'RMW': [-0.64, -3.6], 'CMA': [-0.58, -1.6], 'UMD': [-0.11, -0.5]}
- regression long_short: 20 months, alpha 1.5%/yr (t 0.15), betas {'Mkt-RF': [-0.34, -1.2], 'SMB': [0.73, 2.9], 'HML': [-0.13, -0.4], 'RMW': [0.99, 4.4], 'CMA': [0.64, 1.5], 'UMD': [-0.25, -1.2]}
- cell trend: green (131, 0.7) red (232, -8.8) n/a 0
- cell fcf: green (131, 3.1) red (159, -0.4) n/a 13
- cell ev_ebit: green (84, -1.1) red (89, 3.1) n/a 190
- cell roic: green (82, -16.8) red (258, -0.8) n/a 21
- cell sales: green (278, -3.1) red (50, -12.7) n/a 37
- cell insider: green (65, -8.4) red (173, -11.0) n/a 0
- cell funds: green (180, 0.1) red None n/a 0
- cell top: green None red None n/a 0

### emerging
- overdone: n 51, median 30.1%, mean 36.1%, similar 20.7%, index 27.2%, beat similar 57%
- close: n 85, median 5.8%, mean 23.5%, similar 18.8%, index 24.7%, beat similar 49%
- justified: n 28, median 17.6%, mean 36.7%, similar 17.8%, index 31.2%, beat similar 54%
- regression overdone: 21 months, alpha 9.9%/yr (t 1.03), betas {'Mkt-RF': [1.05, 8.8], 'SMB': [1.05, 5.3], 'HML': [-0.06, -0.2], 'RMW': [-0.07, -0.4], 'CMA': [0.6, 1.7], 'UMD': [0.02, 0.2]}
- regression close: 21 months, alpha 9.5%/yr (t 1.22), betas {'Mkt-RF': [0.62, 2.9], 'SMB': [1.0, 5.0], 'HML': [-0.44, -1.0], 'RMW': [0.24, 2.1], 'CMA': [0.54, 1.9], 'UMD': [0.21, 2.0]}
- regression justified: 21 months, alpha 26.7%/yr (t 2.16), betas {'Mkt-RF': [0.7, 2.8], 'SMB': [1.63, 5.1], 'HML': [-0.73, -1.3], 'RMW': [-0.11, -0.4], 'CMA': [1.0, 1.3], 'UMD': [0.54, 2.7]}
- regression long_short: 21 months, alpha -13.5%/yr (t -1.68), betas {'Mkt-RF': [0.35, 1.2], 'SMB': [-0.58, -1.9], 'HML': [0.68, 1.3], 'RMW': [0.04, 0.2], 'CMA': [-0.4, -0.7], 'UMD': [-0.51, -3.1]}
- cell own: green None red None n/a 164
- cell peers: green (164, 5.2) red None n/a 0
- cell growth: green (43, 7.7) red (58, 5.2) n/a 2
- cell recent: green (62, 9.5) red (52, 4.1) n/a 0
- cell oplev: green (93, 7.3) red (54, -0.9) n/a 2
- cell gm: green (85, -6.4) red (18, 20.2) n/a 25
- cell dilution: green (124, 6.4) red (10, -31.5) n/a 7
- cell insider: green (16, -10.0) red (80, 4.3) n/a 0
- cell funds: green (69, -0.6) red None n/a 0
- cell top: green None red None n/a 0

### core
- overdone: n 103, median 11.6%, mean 16.3%, similar 18.1%, index 20.2%, beat similar 41%
- close: n 93, median 8.8%, mean 34.3%, similar 21.0%, index 20.8%, beat similar 47%
- justified: n 29, median 16.9%, mean 31.6%, similar 16.3%, index 19.7%, beat similar 52%
- regression overdone: 21 months, alpha 6.9%/yr (t 1.13), betas {'Mkt-RF': [0.72, 4.0], 'SMB': [0.34, 1.7], 'HML': [0.11, 0.6], 'RMW': [0.21, 1.4], 'CMA': [0.04, 0.3], 'UMD': [-0.02, -0.2]}
- regression close: 21 months, alpha 4.6%/yr (t 0.83), betas {'Mkt-RF': [0.81, 6.3], 'SMB': [0.64, 2.7], 'HML': [-0.08, -0.3], 'RMW': [0.07, 0.7], 'CMA': [0.72, 1.6], 'UMD': [0.14, 1.7]}
- regression justified: 21 months, alpha 13.7%/yr (t 2.19), betas {'Mkt-RF': [0.73, 5.0], 'SMB': [0.91, 4.9], 'HML': [-0.37, -1.5], 'RMW': [0.09, 1.1], 'CMA': [1.18, 3.5], 'UMD': [0.15, 1.8]}
- regression long_short: 21 months, alpha -6.0%/yr (t -0.62), betas {'Mkt-RF': [-0.01, -0.0], 'SMB': [-0.56, -2.2], 'HML': [0.48, 1.4], 'RMW': [0.13, 0.7], 'CMA': [-1.14, -2.9], 'UMD': [-0.16, -1.1]}
- cell own: green None red None n/a 225
- cell peers: green (225, -4.7) red None n/a 0
- cell roic: green (85, -7.5) red (91, -8.1) n/a 4
- cell persist: green (89, -7.4) red (99, -4.7) n/a 1
- cell growth: green (139, -4.7) red (17, -6.4) n/a 0
- cell conversion: green (148, -9.7) red (18, 3.7) n/a 21
- cell trend: green (156, -8.0) red (39, -1.8) n/a 0
- cell insider: green (12, 13.5) red (85, -1.4) n/a 0
- cell funds: green (149, -2.1) red None n/a 0
- cell top: green None red None n/a 0
