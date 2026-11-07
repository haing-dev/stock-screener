# Triage run 42332908901
event: schedule · step: auto · history_years: 2 · finished: 2026-11-07 03:13 UTC
job status: success

```
Triage steps: mark, exits, build, site
== mark
Mark-to-market: 2026-11-05 (12718 closes)
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
scans ['2024-12-13', '2026-10-15'] · prices to 2026-11-05
- hidden: 1010 events, 407 with a full year, {'overdone': 213, 'close': 265, 'justified': 532, 'tbu': 0}
- emerging: 365 events, 164 with a full year, {'overdone': 108, 'close': 181, 'justified': 76, 'tbu': 0}
- core: 504 events, 225 with a full year, {'overdone': 216, 'close': 221, 'justified': 67, 'tbu': 0}

### hidden
- overdone: n 93, median 23.3%, mean 35.2%, similar 27.8%, index 24.1%, beat similar 53%
- close: n 99, median 16.1%, mean 40.2%, similar 27.3%, index 22.3%, beat similar 48%
- justified: n 215, median 18.4%, mean 55.8%, similar 43.1%, index 22.5%, beat similar 46%
- regression overdone: 19 months, alpha 22.3%/yr (t 2.51), betas {'Mkt-RF': [0.67, 4.8], 'SMB': [1.43, 7.5], 'HML': [-0.61, -1.6], 'RMW': [0.37, 1.7], 'CMA': [0.24, 1.0], 'UMD': [-0.36, -2.0]}
- regression close: 20 months, alpha 20.6%/yr (t 2.32), betas {'Mkt-RF': [0.87, 3.6], 'SMB': [1.47, 4.1], 'HML': [-0.93, -2.4], 'RMW': [0.22, 1.1], 'CMA': [0.05, 0.1], 'UMD': [-0.09, -0.6]}
- regression justified: 20 months, alpha 24.5%/yr (t 3.2), betas {'Mkt-RF': [1.03, 3.3], 'SMB': [0.42, 1.2], 'HML': [-0.33, -0.8], 'RMW': [-0.64, -3.8], 'CMA': [-0.46, -1.2], 'UMD': [-0.04, -0.2]}
- regression long_short: 19 months, alpha -2.9%/yr (t -0.3), betas {'Mkt-RF': [-0.24, -0.9], 'SMB': [0.9, 3.4], 'HML': [0.04, 0.1], 'RMW': [0.99, 3.8], 'CMA': [0.44, 1.3], 'UMD': [-0.35, -1.5]}
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
- regression overdone: 20 months, alpha 11.9%/yr (t 1.11), betas {'Mkt-RF': [1.01, 7.8], 'SMB': [0.98, 5.7], 'HML': [-0.12, -0.4], 'RMW': [-0.07, -0.4], 'CMA': [0.67, 1.6], 'UMD': [0.06, 0.4]}
- regression close: 20 months, alpha 6.9%/yr (t 1.02), betas {'Mkt-RF': [0.67, 3.1], 'SMB': [1.1, 7.7], 'HML': [-0.36, -0.9], 'RMW': [0.24, 2.7], 'CMA': [0.44, 1.4], 'UMD': [0.15, 1.5]}
- regression justified: 20 months, alpha 31.7%/yr (t 2.28), betas {'Mkt-RF': [0.61, 2.2], 'SMB': [1.47, 5.2], 'HML': [-0.86, -1.4], 'RMW': [-0.11, -0.4], 'CMA': [1.16, 1.3], 'UMD': [0.63, 3.0]}
- regression long_short: 20 months, alpha -15.4%/yr (t -1.75), betas {'Mkt-RF': [0.4, 1.3], 'SMB': [-0.49, -1.6], 'HML': [0.74, 1.3], 'RMW': [0.04, 0.3], 'CMA': [-0.49, -0.8], 'UMD': [-0.56, -3.3]}
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
- regression overdone: 20 months, alpha 5.3%/yr (t 0.73), betas {'Mkt-RF': [0.75, 4.0], 'SMB': [0.41, 2.3], 'HML': [0.15, 0.8], 'RMW': [0.21, 1.4], 'CMA': [-0.02, -0.1], 'UMD': [-0.05, -0.6]}
- regression close: 20 months, alpha 5.9%/yr (t 0.92), betas {'Mkt-RF': [0.78, 5.0], 'SMB': [0.59, 2.4], 'HML': [-0.12, -0.3], 'RMW': [0.07, 0.7], 'CMA': [0.77, 1.5], 'UMD': [0.16, 1.8]}
- regression justified: 20 months, alpha 14.7%/yr (t 1.87), betas {'Mkt-RF': [0.71, 3.9], 'SMB': [0.87, 3.6], 'HML': [-0.4, -1.4], 'RMW': [0.09, 1.1], 'CMA': [1.22, 3.2], 'UMD': [0.17, 1.5]}
- regression long_short: 20 months, alpha -8.3%/yr (t -0.66), betas {'Mkt-RF': [0.04, 0.1], 'SMB': [-0.46, -1.8], 'HML': [0.56, 1.3], 'RMW': [0.13, 0.7], 'CMA': [-1.24, -3.1], 'UMD': [-0.22, -1.3]}
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
