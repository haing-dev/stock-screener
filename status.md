# Triage run 40042964432
event: schedule · step: auto · history_years: 2 · finished: 2026-10-24 00:04 UTC
job status: success

```
Triage steps: mark, exits, build, site
== mark
Mark-to-market: 2026-10-22 (12616 closes)
== exits
Exits: 0 replaced with the last close (47 lookups); 47 still at -30%
== build
Triage build over 47 months (2024-11-15 .. 2026-10-15)
  events through 2025-10-31: hidden 441, emerging 182, core 260
  events through 2026-10-15: hidden 1011, emerging 377, core 525
  13F covered through 2026-08-31 (244894 conviction positions); insider data sets through 2026-09-30
  hidden: 1011 events, 408 with a full year, overdone 214, close 264, justified 533, tbu 0
  emerging: 377 events, 176 with a full year, overdone 115, close 185, justified 77, tbu 0
  core: 525 events, 247 with a full year, overdone 224, close 231, justified 70, tbu 0
  live calls: 122 before, 0 new
== site
Site: 1913 events in 3 triages -> /home/runner/work/stock-screener/stock-screener/triage_site
```

## Built data
scans ['2024-11-15', '2026-10-15'] · prices to 2026-10-22
- hidden: 1011 events, 408 with a full year, {'overdone': 214, 'close': 264, 'justified': 533, 'tbu': 0}
- emerging: 377 events, 176 with a full year, {'overdone': 115, 'close': 185, 'justified': 77, 'tbu': 0}
- core: 525 events, 247 with a full year, {'overdone': 224, 'close': 231, 'justified': 70, 'tbu': 0}

### hidden
- overdone: n 93, median 23.3%, mean 35.2%, similar 27.8%, index 24.1%, beat similar 53%
- close: n 99, median 16.1%, mean 40.2%, similar 27.3%, index 22.3%, beat similar 48%
- justified: n 216, median 18.4%, mean 55.6%, similar 42.8%, index 22.4%, beat similar 46%
- regression overdone: 19 months, alpha 22.5%/yr (t 2.52), betas {'Mkt-RF': [0.67, 4.8], 'SMB': [1.44, 7.7], 'HML': [-0.61, -1.6], 'RMW': [0.36, 1.7], 'CMA': [0.25, 1.0], 'UMD': [-0.36, -2.0]}
- regression close: 20 months, alpha 20.4%/yr (t 2.28), betas {'Mkt-RF': [0.87, 3.5], 'SMB': [1.46, 4.0], 'HML': [-0.92, -2.4], 'RMW': [0.22, 1.1], 'CMA': [0.04, 0.1], 'UMD': [-0.09, -0.6]}
- regression justified: 21 months, alpha 9.8%/yr (t 0.64), betas {'Mkt-RF': [1.22, 3.3], 'SMB': [0.54, 1.6], 'HML': [-0.09, -0.2], 'RMW': [-0.81, -3.4], 'CMA': [-0.3, -1.1], 'UMD': [-0.12, -0.5]}
- regression long_short: 19 months, alpha -3.2%/yr (t -0.35), betas {'Mkt-RF': [-0.24, -0.9], 'SMB': [0.95, 3.8], 'HML': [0.01, 0.0], 'RMW': [0.99, 3.8], 'CMA': [0.44, 1.3], 'UMD': [-0.36, -1.6]}
- cell trend: green (131, 0.7) red (233, -8.4) n/a 0
- cell fcf: green (131, 3.1) red (160, -0.2) n/a 13
- cell ev_ebit: green (84, -1.1) red (89, 3.1) n/a 191
- cell roic: green (82, -16.8) red (259, -0.8) n/a 21
- cell sales: green (278, -3.1) red (50, -12.7) n/a 38
- cell insider: green (65, -8.4) red (174, -9.1) n/a 0
- cell funds: green (181, 0.1) red None n/a 0
- cell top: green None red None n/a 0

### emerging
- overdone: n 57, median 30.1%, mean 37.6%, similar 18.8%, index 24.6%, beat similar 60%
- close: n 90, median 5.4%, mean 21.1%, similar 17.2%, index 23.4%, beat similar 48%
- justified: n 29, median 16.0%, mean 34.4%, similar 16.6%, index 29.8%, beat similar 52%
- regression overdone: 21 months, alpha 16.6%/yr (t 1.76), betas {'Mkt-RF': [1.01, 8.4], 'SMB': [0.89, 5.1], 'HML': [-0.13, -0.5], 'RMW': [-0.03, -0.2], 'CMA': [0.67, 1.5], 'UMD': [0.09, 0.6]}
- regression close: 21 months, alpha 3.4%/yr (t 0.74), betas {'Mkt-RF': [0.73, 4.3], 'SMB': [1.12, 7.7], 'HML': [-0.24, -0.9], 'RMW': [0.19, 2.6], 'CMA': [0.41, 1.5], 'UMD': [0.12, 1.6]}
- regression justified: 21 months, alpha 35.2%/yr (t 2.68), betas {'Mkt-RF': [0.64, 3.3], 'SMB': [1.35, 5.8], 'HML': [-0.59, -1.7], 'RMW': [-0.08, -0.3], 'CMA': [0.74, 1.2], 'UMD': [0.62, 3.4]}
- regression long_short: 21 months, alpha -14.0%/yr (t -1.27), betas {'Mkt-RF': [0.36, 1.4], 'SMB': [-0.47, -1.9], 'HML': [0.46, 1.3], 'RMW': [0.06, 0.3], 'CMA': [-0.07, -0.2], 'UMD': [-0.53, -2.9]}
- cell own: green None red None n/a 176
- cell peers: green (176, 5.4) red None n/a 0
- cell growth: green (48, 8.5) red (60, 5.2) n/a 2
- cell recent: green (68, 9.5) red (56, 4.1) n/a 0
- cell oplev: green (103, 7.7) red (55, -0.6) n/a 2
- cell gm: green (92, -5.6) red (18, 15.6) n/a 25
- cell dilution: green (131, 7.2) red (11, -45.1) n/a 7
- cell insider: green (16, -9.6) red (86, 1.2) n/a 0
- cell funds: green (75, 3.1) red None n/a 0
- cell top: green None red None n/a 0

### core
- overdone: n 112, median 10.1%, mean 14.7%, similar 17.2%, index 19.6%, beat similar 43%
- close: n 103, median 8.8%, mean 30.7%, similar 16.9%, index 20.0%, beat similar 49%
- justified: n 32, median 15.8%, mean 23.1%, similar 10.4%, index 18.0%, beat similar 50%
- regression overdone: 21 months, alpha 1.9%/yr (t 0.26), betas {'Mkt-RF': [0.82, 4.5], 'SMB': [0.42, 2.3], 'HML': [0.23, 1.2], 'RMW': [0.19, 1.3], 'CMA': [-0.04, -0.3], 'UMD': [-0.05, -0.5]}
- regression close: 21 months, alpha 2.3%/yr (t 0.56), betas {'Mkt-RF': [0.89, 15.2], 'SMB': [0.67, 4.2], 'HML': [0.2, 1.7], 'RMW': [0.01, 0.2], 'CMA': [0.4, 1.7], 'UMD': [0.1, 1.7]}
- regression justified: 21 months, alpha 14.2%/yr (t 2.19), betas {'Mkt-RF': [0.7, 5.5], 'SMB': [0.72, 4.6], 'HML': [-0.42, -2.1], 'RMW': [0.11, 1.4], 'CMA': [1.29, 5.1], 'UMD': [0.19, 2.1]}
- regression long_short: 21 months, alpha -10.9%/yr (t -0.96), betas {'Mkt-RF': [0.11, 0.4], 'SMB': [-0.3, -1.3], 'HML': [0.65, 2.1], 'RMW': [0.08, 0.5], 'CMA': [-1.33, -4.9], 'UMD': [-0.24, -1.6]}
- cell own: green None red None n/a 247
- cell peers: green (247, -3.6) red None n/a 0
- cell roic: green (92, -7.2) red (104, -3.8) n/a 4
- cell persist: green (95, -7.0) red (112, -2.6) n/a 1
- cell growth: green (156, -4.3) red (18, 4.4) n/a 0
- cell conversion: green (164, -7.2) red (20, 20.2) n/a 22
- cell trend: green (170, -6.7) red (43, 2.7) n/a 0
- cell insider: green (12, -3.4) red (96, -0.3) n/a 0
- cell funds: green (165, 0.7) red None n/a 0
- cell top: green None red None n/a 0
