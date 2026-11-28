# Triage run 46109868967
event: schedule · step: auto · history_years: 2 · finished: 2026-11-28 04:58 UTC
job status: success

```
Triage steps: mark, exits, build, site
== mark
Mark-to-market: 2026-11-27 (12466 closes)
== exits
Exits: 0 replaced with the last close (45 lookups); 45 still at -30%
== build
Triage build over 46 months (2024-12-13 .. 2026-10-30)
  events through 2025-11-28: hidden 509, emerging 194, core 274
  events through 2026-10-30: hidden 1043, emerging 371, core 517
  13F covered through 2026-08-31 (244894 conviction positions); insider data sets through 2026-09-30
  hidden: 1043 events, 440 with a full year, overdone 221, close 275, justified 547, tbu 0
  emerging: 371 events, 170 with a full year, overdone 109, close 184, justified 78, tbu 0
  core: 517 events, 238 with a full year, overdone 222, close 226, justified 69, tbu 0
  live calls: 174 before, 0 new
== site
Site: 1931 events in 3 triages -> /home/runner/work/stock-screener/stock-screener/triage_site
```

## Built data
scans ['2024-12-13', '2026-10-30'] · prices to 2026-11-27
- hidden: 1043 events, 440 with a full year, {'overdone': 221, 'close': 275, 'justified': 547, 'tbu': 0}
- emerging: 371 events, 170 with a full year, {'overdone': 109, 'close': 184, 'justified': 78, 'tbu': 0}
- core: 517 events, 238 with a full year, {'overdone': 222, 'close': 226, 'justified': 69, 'tbu': 0}

### hidden
- overdone: n 100, median 22.1%, mean 35.0%, similar 27.1%, index 23.3%, beat similar 52%
- close: n 107, median 22.3%, mean 40.3%, similar 28.3%, index 21.5%, beat similar 50%
- justified: n 233, median 17.8%, mean 51.2%, similar 41.1%, index 21.7%, beat similar 45%
- regression overdone: 20 months, alpha 23.5%/yr (t 3.25), betas {'Mkt-RF': [0.65, 5.4], 'SMB': [1.4, 6.9], 'HML': [-0.64, -2.0], 'RMW': [0.37, 1.8], 'CMA': [0.29, 1.4], 'UMD': [-0.34, -2.2]}
- regression close: 21 months, alpha 24.2%/yr (t 3.53), betas {'Mkt-RF': [0.81, 3.2], 'SMB': [1.34, 3.4], 'HML': [-1.02, -2.8], 'RMW': [0.22, 1.1], 'CMA': [0.17, 0.4], 'UMD': [-0.03, -0.2]}
- regression justified: 21 months, alpha 20.9%/yr (t 2.15), betas {'Mkt-RF': [1.09, 3.5], 'SMB': [0.54, 2.0], 'HML': [-0.24, -0.5], 'RMW': [-0.64, -3.6], 'CMA': [-0.58, -1.6], 'UMD': [-0.11, -0.5]}
- regression long_short: 20 months, alpha 1.5%/yr (t 0.15), betas {'Mkt-RF': [-0.34, -1.2], 'SMB': [0.73, 2.9], 'HML': [-0.13, -0.4], 'RMW': [0.99, 4.4], 'CMA': [0.64, 1.5], 'UMD': [-0.25, -1.2]}
- cell trend: green (144, 1.5) red (249, -10.8) n/a 0
- cell fcf: green (144, 3.1) red (167, -11.0) n/a 15
- cell ev_ebit: green (91, 0.7) red (98, 2.8) n/a 203
- cell roic: green (89, -14.8) red (277, -3.3) n/a 24
- cell sales: green (298, -3.3) red (54, -12.7) n/a 40
- cell insider: green (74, -10.9) red (186, -11.6) n/a 0
- cell funds: green (196, -0.4) red None n/a 0
- cell top: green None red None n/a 0

### emerging
- overdone: n 52, median 29.5%, mean 35.6%, similar 20.7%, index 26.9%, beat similar 56%
- close: n 88, median 5.7%, mean 22.9%, similar 19.5%, index 24.4%, beat similar 49%
- justified: n 30, median 21.4%, mean 38.2%, similar 17.6%, index 30.2%, beat similar 57%
- regression overdone: 21 months, alpha 9.9%/yr (t 1.03), betas {'Mkt-RF': [1.05, 8.8], 'SMB': [1.05, 5.3], 'HML': [-0.06, -0.2], 'RMW': [-0.07, -0.4], 'CMA': [0.6, 1.7], 'UMD': [0.02, 0.2]}
- regression close: 21 months, alpha 9.5%/yr (t 1.22), betas {'Mkt-RF': [0.62, 2.9], 'SMB': [1.0, 5.0], 'HML': [-0.44, -1.0], 'RMW': [0.24, 2.1], 'CMA': [0.54, 1.9], 'UMD': [0.21, 2.0]}
- regression justified: 21 months, alpha 26.7%/yr (t 2.16), betas {'Mkt-RF': [0.7, 2.8], 'SMB': [1.63, 5.1], 'HML': [-0.73, -1.3], 'RMW': [-0.11, -0.4], 'CMA': [1.0, 1.3], 'UMD': [0.54, 2.7]}
- regression long_short: 21 months, alpha -13.5%/yr (t -1.68), betas {'Mkt-RF': [0.35, 1.2], 'SMB': [-0.58, -1.9], 'HML': [0.68, 1.3], 'RMW': [0.04, 0.2], 'CMA': [-0.4, -0.7], 'UMD': [-0.51, -3.1]}
- cell own: green None red None n/a 170
- cell peers: green (170, 4.1) red None n/a 0
- cell growth: green (44, 8.5) red (60, 5.2) n/a 2
- cell recent: green (65, 7.7) red (55, 3.1) n/a 0
- cell oplev: green (97, 7.0) red (55, -1.2) n/a 2
- cell gm: green (88, -6.5) red (18, 20.2) n/a 27
- cell dilution: green (128, 6.0) red (11, -17.9) n/a 7
- cell insider: green (16, -10.0) red (83, 3.1) n/a 0
- cell funds: green (73, 0.9) red None n/a 0
- cell top: green None red None n/a 0

### core
- overdone: n 112, median 12.7%, mean 15.5%, similar 18.8%, index 19.5%, beat similar 40%
- close: n 95, median 8.8%, mean 33.7%, similar 20.6%, index 20.6%, beat similar 48%
- justified: n 31, median 16.9%, mean 31.7%, similar 16.7%, index 19.2%, beat similar 52%
- regression overdone: 21 months, alpha 6.9%/yr (t 1.13), betas {'Mkt-RF': [0.72, 4.0], 'SMB': [0.34, 1.7], 'HML': [0.11, 0.6], 'RMW': [0.21, 1.4], 'CMA': [0.04, 0.3], 'UMD': [-0.02, -0.2]}
- regression close: 21 months, alpha 4.6%/yr (t 0.83), betas {'Mkt-RF': [0.81, 6.3], 'SMB': [0.64, 2.7], 'HML': [-0.08, -0.3], 'RMW': [0.07, 0.7], 'CMA': [0.72, 1.6], 'UMD': [0.14, 1.7]}
- regression justified: 21 months, alpha 13.7%/yr (t 2.19), betas {'Mkt-RF': [0.73, 5.0], 'SMB': [0.91, 4.9], 'HML': [-0.37, -1.5], 'RMW': [0.09, 1.1], 'CMA': [1.18, 3.5], 'UMD': [0.15, 1.8]}
- regression long_short: 21 months, alpha -6.0%/yr (t -0.62), betas {'Mkt-RF': [-0.01, -0.0], 'SMB': [-0.56, -2.2], 'HML': [0.48, 1.4], 'RMW': [0.13, 0.7], 'CMA': [-1.14, -2.9], 'UMD': [-0.16, -1.1]}
- cell own: green None red None n/a 238
- cell peers: green (238, -4.5) red None n/a 0
- cell roic: green (90, -7.6) red (94, -7.3) n/a 5
- cell persist: green (95, -7.4) red (103, -4.7) n/a 1
- cell growth: green (147, -4.0) red (17, -6.4) n/a 0
- cell conversion: green (156, -9.7) red (19, 13.8) n/a 22
- cell trend: green (166, -7.5) red (40, -2.7) n/a 0
- cell insider: green (12, 13.5) red (88, -1.3) n/a 0
- cell funds: green (159, -2.1) red None n/a 0
- cell top: green None red None n/a 0
