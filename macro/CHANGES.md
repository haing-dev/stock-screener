# Macro Compass changes

## 5.0.1 (2026-10-29) - page only: McKinsey-style redesign + story-led Analysis (user request)
- Visual language from the user's style guide: white page, black text, Georgia Bold titles and stats, Arial body,
  Deep Blue data, one highlight colour per section, thin rules instead of cards, action-sentence titles, chart title +
  units line. Light theme only.
- Analysis: action first (title + mix stats), then a five-step "Why" story linking to the evidence; eight numbered
  sections (1 economy, 2 inflation, 3 market stress, 4 the Fed, 5 growth and trend, 6 bonds as a hedge,
  7 commodities, 8 sector leadership), each with an action title and a so-what paragraph; sub-points numbered 1.1,
  1.2 ... with "This chart measures X. It is currently Y, versus Z a year ago, meaning W." Warning-share chart removed.
- Recommendation: action titles for the mix and the sector calls; status squares instead of pills.

## 5.0.0 (2026-10-29) - package P1 (user choice) + Analysis rebuilt around the six checks
- Rule (SETTINGS.derisk): 4.1 exposure unchanged; plus 10% of the book in a commodity index (DBC; AQR commodity futures
  index + T-bill before 2006) while it is up over 12 months and above its 10-month average (Gromen; the only one of
  731 transcript hypotheses to pass placebo + FDR); plus sector momentum tilt (top/bottom 5 of 20 by 12-1 month
  return, 1.5x/0.5x) while fully in stocks. Backtest now charges 0.2% per 100% traded. Since 1975: 14.5%/yr, worst
  -18%, Sharpe 0.81 (4.1 without costs 14.3%). Research: docs/research/hf_macro (audit, 731 hypotheses, packages).
- Page: Analysis = hero with today's mix and six checks (warning signals, the Fed, growth and trend, bonds as a hedge,
  commodities, sector leadership), each a section with its chart; the 28 core indicator boxes sit under check 1.
  Economy-stage hero and the macro-playbook sector calls removed. Recommendation: mix incl. commodities; sector calls
  = momentum tilts with a logical reason (horizon toggle removed). Ledger columns reset (no rows yet).
- Fetch: AQR commodity index (raw AQR_COMMOD).

## 4.1.0 (2026-10-29) - what to hold outside stocks + simpler recommendation chart (user request)
- Tested for the non-stock share (docs/research/macro_combos/assets.py): T-bills, 10y (IEF), long (TLT), short (SHY)
  Treasuries, gold, defensive sectors; rules by correlation, inflation, cause of the cut, walk-forward, momentum.
  Adopted: growth-trend cut while stocks and bonds move opposite -> long Treasuries (TLT; synthetic 30y/10y before);
  any other cut -> T-bills. Since 1975 14.2%/yr (4.0.0: 13.9%), worst -20%, Sharpe 0.78. Gold instead of bills when
  inflation is hot: 1966-74 15.2% vs 7.7%, but 1975-2026 13.8% and worst -27% -> not adopted.
- Page: section 1 = current mix (equity / cash / bond), stacked portfolio bars by quarter, growth of $100 below; hover
  shows the mix and the quarter's performance vs the S&P 500. Scoreboard, footnote, shading and labels removed.
  Data: derisk.alloc {equity, bond, cash}. Fetch adds GS30/GS5/GS1/TB3MS, TLT/SHY/TIP/GLD/DBC/GC=F, gold history.

## 4.0.0 (2026-10-28) - Fed-gated de-risking + growth-trend cut + conditional Treasuries (user choice)
- From the 5,637-rule combination test (docs/research/macro_combos/README.md). Rule (SETTINGS.derisk): the same
  track-record-weighted warnings cut stocks only while the Fed is tightening (funds rate >= 1 pt above its 24-month
  low); share <= 15% -> 100% stocks, >= 35% -> 0%, linear between. Separately, S&P 500 below its 10-month average AND
  unemployment above its 12-month average -> 0% stocks. The rest in 7-10y Treasuries (IEF; synthetic 10-year before
  2002-08) while the 12-month stock-bond correlation < 0, else T-bills.
- Since 1975: 13.9%/yr vs S&P 12.4%, worst fall -20% vs -51%, Sharpe 0.78 vs 0.58, average 81% stocks. 1966-74
  (untouched): 7.8%/yr vs -0.6%. Search-adjusted p 0.25: expect about half the gain live. Today: 100% stocks.
- Sector-momentum tilt from the test not adopted: it would replace the sector calls section. Page format unchanged
  (the non-equity share is labelled Treasuries or cash). Ledger: + defensive, fed_gate, growth_cut.

## Research note (2026-10-23, no rule change) - trend confirmation (macro/research_trend.py)
- Current 3.2 (graded + track-record): 11.3%/yr since 1975, worst -29%, protected +36 pts / lost -102 pts; 2006+ 10.0%.
- Graded, cut only while the S&P is below its 10-month average: 12.0%, -31%, +37 / -64 pts; 2006+ 10.5%, -30%.
- Switch at 30% of weighted warnings -> 80%, + S&P below 10-month average -> 50%: 12.1%, -31%, +36 / -64; 2006+ 10.9%.
- Switch 30% AND S&P below its 6-month average -> 50%: 12.2%, -34%, +41 / -58; 2006+ 11.4%, -33%.
- S&P 500: 12.4%, -51%; 2006+ 11.2%. Confirmation roughly halves the cost of false alarms; their number stays 16-20.

## 3.2.1 (2026-10-23) - page only (user request)
- Recommendation chart reworked: scoreboard (points protected / lost / worst fall), growth of $100, quarterly bars of
  the gain or loss vs the S&P 500 (green / red) with each cut shaded and labelled, portfolio exposure bars.
- Tabs renamed Analysis / Recommendation. Recommendation 1: current-quarter call (latest reading, updated as data
  arrive) + one chart by quarter: growth of $100, recommended exposure vs S&P 500, S&P falls of 15%+ and costly false
  alarms marked with the difference (+x% / -x%), portfolio exposure bars; hover snaps to quarters. The rule itself
  still updates monthly. Checked: calls made 1 or 2 quarters ahead keep most of the protection on average
  (11.2% / 11.6%/yr, worst -30% / -33% vs -29% now) but miss sudden shocks; quarter-end-only rebalancing 11.0%, -31%.
- Analysis: last-2-years panel and sector chips removed from each indicator box.

## 3.2.0 (2026-10-23) - de-risking: track-record weights + graded cut (user choice, ideas 1 + 2b)
- Rule (SETTINGS.derisk): warnings = core indicators in their worst fifth, each weighted walk-forward by how much
  more often than normal a 15%+ S&P fall followed within 12 months (shrink 24); weighted share <= 15% -> 100% stocks,
  >= 35% -> 50%, linear between; cash earns the 3-month T-bill rate. Variant 'graded 0.15-0.35, lift 15/12, core28'
  from the research grid (not the best-scoring one). Since 1975: 11.4%/yr vs S&P 12.4%, worst fall -29% vs -51%,
  Sharpe 0.62 vs 0.58, average 85% in stocks. Today: 68% stocks (28% of weighted warnings).
- Page: two tabs. The reading (state + sections 1-3, recession key on each chart, no chart key panel). The calls:
  one master chart (S&P and rule falls from peak, cuts marked dodged / cost, share held in stocks) and sector calls
  as sector / call / why now (registry.WHY, logic not numbers). Ledger: stock_exposure, warning_share.

## Research note (2026-10-23, no rule change) - can de-risking warn earlier and more precisely?
macro/research_derisk.py: 523 monthly rules (walk-forward track-record weights 'lift'/'edge' on 15%-in-12m or
10%-in-6m falls; one switch / two steps / graded / with market trend AND, OR, two-step; fast re-entry; 28 or 43
indicators), judged 1975-2000 and 2001-2026 separately, like-for-like pairs per idea; weekly checks via daily data
(step 'derisk_weekly', Actions). Headline (1975-2026 monthly; S&P 500 12.4%/yr, worst -51%, Sharpe 0.58):
- live rule 11.5%/yr, worst -39%, Sharpe 0.58, 4/8 falls of 15%+ cut before the S&P was 10% down, 14 false alarms;
- trend only (S&P below 10-month average -> 50%) 11.7%, -30%, 0.61, 6/8, 24 false alarms;
- indicators 0.25 (track-record weights) OR trend: 11.4%, -29%, 0.64, 7/8, 36 false alarms (better than live in both halves);
- one switch 0.30 + track-record weights + fast re-entry: 12.3%, -32%, 0.64 (best overall, but picked with hindsight).
Per idea: track-record weights small consistent gain (+0.1-0.2%/yr, Sharpe better in ~2/3 of pairs in both halves);
two steps worse after 2000 (worst falls 4.5 pts deeper, median); graded smaller worst falls (~3-4 pts) but -0.5%/yr
after 2000; fast re-entry helped before 2000, hurt after; 43 vs 28 indicators no difference; weekly checks (1990-2026)
no material change (live 10.6 vs 10.5%/yr, worst -38.5 vs -39.7%) with twice the trades. Rules picked on 1975-2000
only did not beat the live rule's 2001-2026 Sharpe (0.56-0.67 vs 0.62) but had smaller worst falls.

## 3.1.0 (2026-10-23) - main action: de-risking (user request)
- Rule (SETTINGS.derisk): at each month end, count the core indicators (growth, market health, inflation, market
  stress; 28) scoring in their worst fifth (>= 80). If at least a third are, hold 50% S&P 500 / 50% T-bills next
  month; otherwise 100% S&P 500. Chosen as proposed in the research note (not the best of the variants tested).
- Backtest (engine.derisk), seen before publishing: since 1975 11.6%/yr vs S&P 500 12.4%, worst fall -39% vs -51%,
  Sharpe 0.59 vs 0.58, stocks cut in 18% of months, 25 episodes (7 protected, 18 missed gains); since Aug 2006
  11.3% vs 11.2%, worst fall -29% vs -51%, Sharpe 0.80 vs 0.67. Variants seen earlier (stress flag; >= 1/4;
  stress or >= 1/3): 10.1-11.3%/yr since 2006, worst falls -29% to -31%.
- Page: stock-exposure section after the reading (signal, indicators in their worst fifth, count history, backtest
  since 1975 / 2006, every episode); sector calls now marked secondary. Ledger gains derisk_on, derisk_count.

## Research note (2026-10-23, no rule change) - more sensitive instruments
- Bigger bets on the same calls (1.5x/0.5x up to 4x/-2x, i.e. leveraged instruments): excess vs equal weight grows
  to +0.5 to +1.2%/yr but the information ratio stays at 0.05-0.14 and relative drawdowns grow to -15% to -32%.
- Most sensitive stocks (macro/research_stocks.py, run via step 'stocks'; today's large holdings, survivorship-biased,
  compared basket vs basket): +0.4%/yr (12m) / +0.8%/yr (6m) vs equal-weight baskets, but the same stocks with no
  tilt give +0.5 / +0.7 and with the calls reversed +0.5 / +0.5 -> the gain is from holding high-beta survivors,
  not from the calls (value of the calls alone -0.1 / +0.1%/yr). Long/short spread of called sectors via
  sensitive stocks: -1.0 / -0.8%/yr. Not adopted.

## 3.0.0 (2026-10-23) - act only on extreme readings; benchmark = 20-sector average (user request)
- Calls are made only in months when a reading is extreme (SETTINGS.extreme): economy indicators' 6-month average
  score >= 60 (clearly weak) or <= 40 (clearly strong), market-stress score >= 70, or inflation 6-month average >= 70.
  Otherwise all 20 sectors stay at equal weight. Extreme in 52% of months since 1960.
- Benchmark for the history check, odds, sector history and relative charts: equal-weight average of the 20 sectors
  (was the S&P 500). Live ledger scored the same way; ledger gains an 'extreme' column (no rows written before).
- Tested before choosing (in sample, documented): every month vs dial extremes vs >= 1/4 or >= 1/3 of the 28 core
  indicators in their worst/best fifth, against both benchmarks. All within +-0.5%/yr of equal weight (IR <= 0.3);
  dial extremes chosen as the simplest with hit rates at or above base. Result: +0.2%/yr since 2006 (ETFs) and
  0.0%/yr since 1971 (industry indexes) vs equal weight.
- Also tested, not built: cutting stocks to 50% (rest T-bills) when >= 1/3 of core indicators are in their worst
  fifth: since 2006 11.3%/yr vs S&P 500 11.2%, worst fall -29% vs -51%; since 1975 11.8% vs 12.7%, -39% vs -51%.

## 2.2.1 (2026-10-23) - page only (user request)
- Per-chart notes replaced by one sticky chart key on the right (floating, collapsible on small screens); warning
  level moved into each summary sentence.
- Removed from the page: trade test, state x sector table, track record, background indicators, method. The engine
  still computes them and the live ledger still records every month.

## 2.2.0 (2026-10-23) - page layout + trade test (user request)
- Indicator boxes stacked full width, numbered 1.1, 1.2 ... with official names and one naming convention
  (vs L12M / L6M / L3M); each has a generated summary (what it measures, zone, change vs a year ago, what it
  indicates), a long-history chart and a last-2-years chart marking the reading a year ago vs now, round axis
  levels, and footnotes instead of explanatory text. Section headers show a warning/normal/supportive bar.
- New trade test (engine.entry_test): every past month the economy entered today's situation, $100k in that
  month's calls (long/short equal amounts, no leverage; and long only) vs $100k in the S&P 500, after 1, 2, 3
  years. Descriptive; no effect on the calls.

## 2.1.0 (2026-10-23) - page shows the data, not scores (user request)
- Page rebuilt: conclusion + points A (economy), B (inflation), C (market stress), each with real-unit time series
  of its signals (warning zone = worst third of the signal's own history, recessions shaded), what each signal means
  in plain words, and which sectors did best/worst after past months in the same zone; sector calls with the logic
  and the history check; state x sector table (average next 6/12-month return vs S&P 500); no 0-100 scores and no
  investor names on the page (sources stay in registry.py).
- Data fix: first-published (ALFRED) values that switch units between vintages (billions vs millions) are rescaled
  (engine._unit_breaks); this corrected 'share of household savings in stocks' (froth, background only). Calls unchanged.
- registry.DISPLAY: unit, decimals and plain explanation per indicator (display only).

## 2.0.0 (2026-10-23) - user request: one decision flow from transcript/Galt logic
- Indicators: 38 -> 43. Added Galt's market-stress signals (VIX via Yahoo ^VIX same-day + FRED VIXCLS, S&P 500
  below its 10-month average, junk bonds vs Treasuries 3-month, dollar breakout, chip stocks 12-month drawdown),
  staples vs discretionary, home builders drawdown, stocks-bonds correlation, dollar/oil/rates squeeze.
- New pillar "Market stress" (replaces "credit"); pillars: growth, internals, inflation, stress, liquidity, froth.
- State = three dials: economy stage (mean of growth + market health, same stage rule as 1.0.0), inflation hot
  (6-month average, on 60 / off 50) -> Overheating (expansion/late) or Stagflation (contraction), market stress
  high (on 65 / off 55) as an overlay.
- Industry calls: per-industry drivers and quintile odds removed. Investor playbook per state (registry.RULES, cited
  to Druckenmiller, Karniol-Tambour, Calderini, Eisman, Galt) + stress overlay (registry.STRESS) -> +1/-1 tilt;
  a tilt stands only if past months of the same situation (state+stress, else state; >= 24 months; outcomes
  finished by t) had a mean return vs SPY with the same sign. Backtest adds a "playbook only" curve.
- Seen before publishing (in sample): ETF backtest Aug 2006 - Oct 2026, calls +10.9%/yr vs equal weight +10.4%,
  SPY +11.2%; call hit rates close to base rates. Tested and rejected: adding Money and rates and/or Froth to the
  economy dial or the stress dial (calls 0.1-0.4%/yr worse, fewer recession months marked); they stay as background.
- Ledger columns now record state, inflation_hot, stress_high, six pillars and the investor tilt (no rows had been
  written under 1.0.0).

## 1.0.0 (2026-10-23) - pre-registered
- Indicators, pillars, industries, drivers, thresholds as in registry.py.
- Design choices made while building, before publishing:
  - stage settings (6-month average, 12-month direction +-8, level 45/55, 3-month confirm) were picked for a
    steady stage that marks past recessions as Contraction, checked on 1970-2026 data (in sample). The stage does
    not feed the industry odds or the backtest.
  - the first full build's backtest (calls ~ equal weight, Aug 2006 - Oct 2026) was seen before publishing; no
    rule was changed after it.
- 2026-10-23: FRED_API_KEY added; builds use first-published values from here on (no rule change).
- 2026-10-23: Cloudflare secrets added; the workflow deploys the Worker itself.
- 2026-10-23: page moved off the stock-screener site to its own Worker "macro-compass" (branch macro-site); no rule change.
- 2026-10-23: password removed (user); page and data public. No rule change.
- Known gaps: household-equity indicator needs the next download (series id fixed); FRED_API_KEY not yet set,
  so the first builds use revised data (first-published values once the key is in).
