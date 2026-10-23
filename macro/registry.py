"""Macro Compass: the indicator library, the six pillars and the 20 industries.

Every indicator is a claim made by an investor in the research store (transcript id) or in the X posts of
@AtlasShrug1 ("Galt", dated), turned into a fixed, testable rule. Investors propose, the backtest decides.
v1.0.0 pre-registered 2026-10-23; v2.0.0 the same day (state -> investor sector rules + history check). Change log: macro/CHANGES.md. Never edit a rule in place: add a version.
"""
VERSION = "3.0.0"

# ------------------------------------------------------------------ fixed settings (pre-registered)
SETTINGS = {
    "start": "1960-01",            # first month of the monthly grid
    "score_min_years": 10,         # an indicator scores only once it has 10 years of its own history
    "warmup_years": 15,            # industry odds need 15 years of past outcomes before they are reported
    "horizons": [6, 12],           # months ahead (the site's switch)
    "outcome_band": {6: 0.07, 12: 0.10},   # beat / lag the market by at least this much = opportunity / risk
    "evidence_min_months": 24,     # a sector call needs 24+ past months of the same situation to be checked
    "tilt_size": 0.5,              # overweight = 1.5x the equal weight, underweight = 0.5x
    "stage_smooth": 6,             # stage reads the 6-month average of growth pressure
    "stage_lookback": 12,          # direction = change in that average over 12 months ...
    "stage_band": 8,               # ... of 8+ points (else the last direction holds)
    "stage_hysteresis": 5,         # weak growth from 55 up, solid from 45 down (else the last level holds)
    "stage_confirm": 3,            # a new stage needs 3 months in a row
    "inflation_hot": (60, 50),     # inflation area, 6-month average: hot from 60, cool again at 50
    "stress_high": (65, 55),       # market stress area: high from 65, normal again at 55
    # 3.0.0: act only on extreme readings; otherwise every sector stays neutral (equal weight)
    "extreme": {"economy": (40, 60), "stress": 70, "inflation": 70},
    "benchmark": "equal-weight average of the 20 sectors",
    "etf_backtest_start": "2006-07",  # first month most of the 20 ETFs trade
}

# ------------------------------------------------------------------ pillars (score 0-100 = pressure; 100 = worst in history)
# role: "stage" areas set the economy stage, "inflation" and "stress" set the two overlays, "context" are shown
PILLARS = [
    ("growth", "Growth", "Is the economy slowing?"),
    ("internals", "Market health", "Are most stocks and industries joining in?"),
    ("inflation", "Inflation", "Are prices speeding up?"),
    ("stress", "Market stress", "Are markets in risk-off mode?"),
    ("liquidity", "Money and rates", "Is money getting tighter?"),
    ("froth", "Froth", "Are stocks priced for perfection?"),
]

# ------------------------------------------------------------------ raw data
# FRED series. fr = use the first-published value (ALFRED) when FRED_API_KEY is set. lag = months after the
# observation month before the number is public (on a month-end grid).
FRED = {
    "UNRATE": dict(fr=True, lag=1), "LNS14024887": dict(fr=True, lag=1),
    "TRUCKD11": dict(fr=True, lag=2), "PERMIT": dict(fr=True, lag=1), "TOTALSA": dict(fr=True, lag=1),
    "GS10": dict(lag=0), "GS2": dict(lag=0), "BAA": dict(lag=0), "FEDFUNDS": dict(lag=0),
    "PCEPILFE": dict(fr=True, lag=2), "CPILFESL": dict(fr=True, lag=1), "PPIACO": dict(fr=True, lag=1),
    "T5YIFR": dict(lag=0), "WTISPLC": dict(lag=1), "PCOPPUSDM": dict(lag=1), "PIORECRUSDM": dict(lag=1),
    "GDP": dict(fr=True, lag=2, q=True), "M2SL": dict(fr=True, lag=1),
    "WALCL": dict(lag=0), "WTREGEN": dict(lag=0), "RRPONTSYD": dict(lag=0),
    "MORTGAGE30US": dict(lag=0), "THREEFYTP10": dict(lag=0), "VIXCLS": dict(lag=0),
    "DRCCLACBS": dict(fr=True, lag=3, q=True), "NCBEILQ027S": dict(fr=True, lag=3, q=True),
    "HNOCEAQ027S": dict(fr=True, lag=3, q=True), "TFAABSHNO": dict(fr=True, lag=3, q=True),
    "USREC": dict(lag=0), "DTWEXBGS": dict(lag=0), "TWEXMMTH": dict(lag=0),
}
YAHOO = ["SPY", "EWY", "DX-Y.NYB", "HYG", "IEF", "XLY", "SOXX", "^VIX"]   # plus every industry ETF below
FRENCH_IND = "49_Industry_Portfolios_CSV.zip"
FRENCH_FF = "F-F_Research_Data_Factors_CSV.zip"

# price-based indicators use the 20 industry series (ETF once it trades, its industry index before)
CYCLICAL = ["ITB", "KBE", "IYT", "XRT", "XME"]
DEFENSIVE = ["XLU", "XLP", "XLV"]


def X(date):
    return ("Galt (X)", date)


def T(name, tid):
    return (name, f"#{tid:03d}")


# ------------------------------------------------------------------ indicators
# calc: how the raw data becomes one number per month (macro/engine.py calc_all). dir +1: a higher number means more
# pressure (weaker growth, hotter prices, more stress, tighter money, more froth, weaker market).
INDICATORS = [
    # growth (economy data; with market health it sets the stage)
    dict(id="jobs_alarm", pillar="growth", name="Unemployment rise from its 12-month low (Sahm rule)", calc=("sahm", "UNRATE"), dir=1,
         plain="Unemployment rising off its low", who=[T("Gerstner", 215)]),
    dict(id="truck", pillar="growth", name="Truck freight vs a year ago", calc=("yoy", "TRUCKD11"), dir=-1,
         plain="Trucking volumes", who=[T("Druckenmiller", 102), T("Druckenmiller", 77)]),
    dict(id="permits", pillar="growth", name="New home permits, 6-month change", calc=("chg6pct", "PERMIT"), dir=-1,
         plain="Home building", who=[T("Druckenmiller", 76)]),
    dict(id="autos", pillar="growth", name="Car sales, 6-month change", calc=("chg6pct", "TOTALSA"), dir=-1,
         plain="Car buying", who=[T("Druckenmiller", 76)]),
    dict(id="curve", pillar="growth", name="Yield curve (10-year minus 2-year)", calc=("spread", "GS10", "GS2"),
         dir=-1, plain="Long vs short interest rates", who=[T("Roche", 265), T("Druckenmiller", 76)]),
    dict(id="youth", pillar="growth", name="Young-adult jobless rate vs overall, 12-month change",
         calc=("gapchg12", "LNS14024887", "UNRATE"), dir=1, plain="Jobs for young adults", who=[T("Eisman", 147)]),
    dict(id="cards", pillar="growth", name="Credit-card late payments, 12-month change", calc=("chg12", "DRCCLACBS"),
         dir=1, plain="Consumers falling behind", who=[T("Bessent", 270), T("Gerstner", 215)]),
    # market health (the inside of the market leads the economy)
    dict(id="cyc_def", pillar="internals", name="Cyclical vs defensive stocks, 6 months", calc=("cycdef",), dir=-1,
         plain="Economy-sensitive stocks vs safe stocks", who=[T("Druckenmiller", 76), T("Druckenmiller", 77)]),
    dict(id="staples_disc", pillar="internals", name="Staples vs discretionary stocks, 6 months",
         calc=("relpair6", "XLP", "XLY"), dir=1, plain="Safe spending vs optional spending", who=[X("2026-10-15")]),
    dict(id="breadth", pillar="internals", name="Industries in an uptrend", calc=("breadth",), dir=-1,
         plain="How many industries are rising", who=[T("Verrone", 156)]),
    dict(id="breakdowns", pillar="internals", name="Industries 20%+ below their 12-month high", calc=("breakdowns",),
         dir=1, plain="How many industries are falling apart", who=[X("2026-09-23")]),
    dict(id="transports", pillar="internals", name="Transport vs industrial stocks, 6 months",
         calc=("relpair6", "IYT", "XLI"), dir=-1, plain="Transports confirming (Dow theory)", who=[X("2026-09-02")]),
    dict(id="homebuilders", pillar="internals", name="Home builders vs market, below their 2-year peak",
         calc=("reldd24", "ITB"), dir=-1, plain="Home builders, the first red flag", who=[X("2026-06-09"), T("Druckenmiller", 76)]),
    # inflation
    dict(id="core_pce", pillar="inflation", name="Core inflation, last 3 months vs last 12",
         calc=("accel", "PCEPILFE"), dir=1, plain="Is core inflation speeding up", who=[T("Calderini", 153), T("Calderini", 155)]),
    dict(id="core_cpi", pillar="inflation", name="Core consumer prices vs a year ago", calc=("yoy", "CPILFESL"), dir=1,
         plain="Core inflation level", who=[T("Druckenmiller", 77)]),
    dict(id="ppi", pillar="inflation", name="Producer prices vs a year ago", calc=("yoy", "PPIACO"), dir=1,
         plain="Business input prices", who=[T("Eisman", 161)]),
    dict(id="inflexp", pillar="inflation", name="5-year inflation expectations, 6-month change", calc=("chg6", "T5YIFR"),
         dir=1, plain="What bond markets expect for inflation", who=[T("Calderini", 153), T("Jensen", 7)]),
    dict(id="oil", pillar="inflation", name="Oil price, 6-month change", calc=("chg6pct", "WTISPLC"), dir=1,
         plain="Oil", who=[T("Druckenmiller", 75), T("Bessent", 269)]),
    dict(id="copper", pillar="inflation", name="Copper price, 6-month change", calc=("chg6pct", "PCOPPUSDM"), dir=1,
         plain="Copper", who=[T("Druckenmiller", 80), T("Verrone", 156)]),
    dict(id="stockbond", pillar="inflation", name="Stocks and bonds moving together (1-year correlation)",
         calc=("stockbond",), dir=1, plain="Bonds no longer hedging stocks", who=[T("Calderini", 155), T("Tropin", 151)]),
    # market stress
    dict(id="vix", pillar="stress", name="Stock market fear gauge (VIX)", calc=("level", "VIXCLS"), dir=1,
         plain="Fear in the stock market", who=[T("Calderini", 155), T("Tropin", 151), X("2026-10-15")]),
    dict(id="spx_trend", pillar="stress", name="S&P 500 vs its 10-month average", calc=("trend", "market"), dir=-1,
         plain="The market's main trend", who=[X("2026-07-14")]),
    dict(id="junk", pillar="stress", name="Junk bonds vs Treasuries, 3 months", calc=("relpx3", "HYG", "IEF"), dir=-1,
         plain="Junk-bond stress", who=[X("2026-10-20"), T("Verrone", 156)]),
    dict(id="baa", pillar="stress", name="Corporate bond spread (Baa minus 10-year)", calc=("spread", "BAA", "GS10"), dir=1,
         plain="Extra yield companies pay to borrow", who=[T("Druckenmiller", 76)]),
    dict(id="baa_chg", pillar="stress", name="Corporate bond spread, 6-month change", calc=("spreadchg6", "BAA", "GS10"),
         dir=1, plain="Is borrowing getting harder", who=[T("Druckenmiller", 76)]),
    dict(id="banks", pillar="stress", name="Bank stocks vs market, 6 months", calc=("rel6", "KBE"), dir=-1,
         plain="Bank stocks", who=[T("Druckenmiller", 76), X("2026-10-14")]),
    dict(id="dollar_break", pillar="stress", name="Dollar vs its 12-month high", calc=("breakout", "dxy"), dir=1,
         plain="Dollar breakout (liquidity squeeze)", who=[X("2026-10-05"), T("Gromen", 159)]),
    dict(id="chips_break", pillar="stress", name="Chip stocks vs their 12-month high", calc=("dd12px", "SOXX", "SMH"), dir=-1,
         plain="Chip stocks breaking down", who=[X("2026-10-14")]),
    # money and rates
    dict(id="fedfunds", pillar="liquidity", name="Fed interest rate, 12-month change", calc=("chg12", "FEDFUNDS"), dir=1,
         plain="Fed raising or cutting", who=[T("van Eck", 81)]),
    dict(id="y10_chg", pillar="liquidity", name="10-year yield, 12-month change", calc=("chg12", "GS10"), dir=1,
         plain="Long-term rates", who=[T("Guha", 136)]),
    dict(id="y10_ngdp", pillar="liquidity", name="10-year yield minus economic growth", calc=("y10ngdp",), dir=1,
         plain="Bond yields vs growth", who=[T("Druckenmiller", 79)]),
    dict(id="m2", pillar="liquidity", name="Money supply (M2) growth", calc=("yoy", "M2SL"), dir=-1,
         plain="Money supply", who=[T("Druckenmiller", 76), T("Druckenmiller", 102)]),
    dict(id="dollar", pillar="liquidity", name="US dollar, 12-month change", calc=("dollar",), dir=1,
         plain="The dollar", who=[T("Gromen", 159), T("Druckenmiller", 75), X("2026-06-11")]),
    dict(id="squeeze", pillar="liquidity", name="Oil, rates and dollar rising together", calc=("squeeze",), dir=1,
         plain="Profit squeeze", who=[T("Druckenmiller", 79), T("Druckenmiller", 77)]),
    dict(id="realyield", pillar="liquidity", name="Real 10-year yield (after inflation)", calc=("realyield",), dir=1,
         plain="Interest rates after inflation", who=[T("Gerstner", 215), T("Rogoff", 264)]),
    dict(id="mortgage", pillar="liquidity", name="Mortgage rate, 12-month change", calc=("chg12", "MORTGAGE30US"), dir=1,
         plain="Mortgage rates", who=[T("Guha", 136)]),
    dict(id="termprem", pillar="liquidity", name="Extra yield on long bonds (term premium), 12-month change",
         calc=("chg12", "THREEFYTP10"), dir=1, plain="Bond investors' nerves", who=[T("Tropin", 151)]),
    dict(id="netliq", pillar="liquidity", name="Fed money in the system, 3-month change", calc=("netliq",), dir=-1,
         plain="Fed liquidity", who=[T("Druckenmiller", 78), T("Citrone", 267)]),
    # froth
    dict(id="mcap_gdp", pillar="froth", name="Stock market value vs the economy", calc=("ratio", "NCBEILQ027S", "GDP"),
         dir=1, plain="Stocks vs GDP", who=[X("2026-08-08")]),
    dict(id="hh_equity", pillar="froth", name="Share of household savings in stocks",
         calc=("ratio", "HNOCEAQ027S", "TFAABSHNO"), dir=1, plain="How much households own in stocks", who=[X("2026-08-08")]),
    dict(id="cape", pillar="froth", name="Price vs 10-year average earnings (CAPE)", calc=("cape",), dir=1,
         plain="Stock valuations", who=[X("2026-08-08"), T("Tropin", 149)]),
    dict(id="rally", pillar="froth", name="Speed of the stock rally (6-month gain vs its swings)", calc=("rally",), dir=1,
         plain="How fast stocks have run", who=[T("Calderini", 155)]),
    dict(id="leadership", pillar="froth", name="Narrow leadership (index vs typical industry, 12 months)",
         calc=("leadership",), dir=1, plain="Is the rise led by a few", who=[T("Druckenmiller", 79)]),
]
IND = {i["id"]: i for i in INDICATORS}

# ------------------------------------------------------------------ how each indicator is shown on the page
# Display only (no effect on the calls). title = official name + measure (L12M / L6M / L3M = vs or over the last
# 12 / 6 / 3 months); short = name inside sentences; unit, scale, dp = number format; vp = text after the value;
# what = what it measures; then what the reading indicates in its warning / normal / supportive zone.
def _d(title, short, unit, dp, vp, what, warn, normal, good, scale=1):
    return dict(title=title, short=short, unit=unit, scale=scale, dp=dp, vp=vp, what=what,
                means={"warn": warn, "normal": normal, "good": good})


DISPLAY = {
    "jobs_alarm": _d("Sahm rule recession indicator", "the Sahm rule indicator", "pts", 2, "",
                     "The Sahm rule measures how far the 3-month average unemployment rate has risen above its low of the past 12 months; a rise of 0.50 points or more has marked every US recession since 1970",
                     "a labour market that is starting to crack", "a stable labour market", "a tightening labour market"),
    "truck": _d("Truck tonnage vs L12M", "truck tonnage", "%", 1, " vs L12M",
                "Truck tonnage measures the weight of freight moved by road, a direct read on demand for goods",
                "weakening demand for goods", "steady demand for goods", "strong demand for goods"),
    "permits": _d("Building permits vs L6M", "building permits", "%", 1, " vs L6M",
                  "Building permits measure planned new homes; builders file them months before construction starts",
                  "less construction and hiring ahead", "steady construction ahead", "more construction and hiring ahead"),
    "autos": _d("Total vehicle sales vs L6M", "vehicle sales", "%", 1, " vs L6M",
                "Vehicle sales measure purchases of cars and light trucks, the largest purchase households can postpone",
                "households pulling back on big purchases", "steady household spending", "confident household spending"),
    "curve": _d("Yield curve (10Y minus 2Y Treasury)", "the yield curve", "pts", 2, "",
                "The yield curve measures the gap between 10-year and 2-year Treasury yields; below zero (inverted), lending becomes less profitable and credit tightens",
                "tight credit and a higher risk of recession", "normal credit conditions", "easy credit that supports growth"),
    "youth": _d("Youth unemployment gap vs L12M", "the youth unemployment gap", "pts", 2, " vs L12M",
                "The youth unemployment gap measures the unemployment rate of 16 to 24 year olds minus the overall rate; young workers are hired last and let go first",
                "early weakness in hiring", "stable hiring", "strong hiring"),
    "cards": _d("Credit card delinquency rate vs L12M", "the credit card delinquency rate", "pts", 2, " vs L12M",
                "The credit card delinquency rate measures the share of card balances at commercial banks that are 30 or more days overdue",
                "households under financial strain", "stable household finances", "improving household finances"),
    "cyc_def": _d("Cyclicals vs defensives, L6M return", "the cyclicals' lead", "%", 1, " (L6M)",
                  "This measures the 6-month return of economy-sensitive sectors (homebuilders, banks, transports, retail, metals) minus defensive sectors (utilities, consumer staples, health care)",
                  "investors positioning for a slowdown", "no strong market view on growth", "investors positioning for stronger growth"),
    "staples_disc": _d("Consumer staples vs discretionary, L6M return", "the staples' lead", "%", 1, " (L6M)",
                       "This measures the 6-month return of consumer staples minus consumer discretionary stocks",
                       "investors expecting consumers to cut back", "no strong market view on consumer spending", "investors expecting consumer spending to grow"),
    "breadth": _d("Sector breadth", "sector breadth", "%", 0, " of sectors",
                  "Sector breadth measures the share of the 20 sectors trading above their 10-month average",
                  "a narrowing market rally", "average participation in the market", "a broad, healthy rally"),
    "breakdowns": _d("Sectors in a bear market", "the share of sectors in a bear market", "%", 0, " of sectors",
                     "This measures the share of the 20 sectors trading 20% or more below their 12-month high",
                     "weakness spreading beneath the index", "contained sector weakness", "few sectors under pressure"),
    "transports": _d("Transports vs industrials, L6M return", "the transports' lead", "%", 1, " (L6M)",
                     "This measures the 6-month return of transport stocks minus industrial stocks; goods that are made must also be shipped",
                     "doubts that demand for goods will last", "no clear signal on demand for goods", "confidence in demand for goods"),
    "homebuilders": _d("Homebuilders vs S&P 500, drawdown from 24-month high", "the homebuilders' relative drawdown", "%", 1, "",
                       "This measures how far homebuilders' performance relative to the S&P 500 sits below its best level of the past 24 months; housing reacts first to interest rates and household demand",
                       "an early warning for the wider economy", "no warning from housing", "a healthy housing market"),
    "core_pce": _d("Core PCE inflation, 3-month annualised minus L12M", "core PCE momentum", "pts", 2, "",
                   "This measures core PCE inflation (excluding food and energy) over the last 3 months, annualised, minus the rate over the last 12 months; above zero, inflation is speeding up",
                   "accelerating inflation", "stable inflation", "slowing inflation"),
    "core_cpi": _d("Core CPI vs L12M", "core CPI inflation", "%", 1, " vs L12M",
                   "Core CPI measures consumer price inflation excluding food and energy; the Federal Reserve aims for about 2%",
                   "inflation above target", "inflation in its usual range", "low inflation"),
    "ppi": _d("Producer Price Index vs L12M", "producer price inflation", "%", 1, " vs L12M",
              "The Producer Price Index measures the prices businesses pay for goods and inputs; increases feed into consumer prices or squeeze margins",
              "rising cost pressure", "normal cost pressure", "easing cost pressure"),
    "inflexp": _d("5-year forward inflation expectations vs L6M", "inflation expectations", "pts", 2, " vs L6M",
                  "This measures the average inflation rate bond markets expect over the 5 years starting 5 years from now",
                  "investors fearing persistent inflation", "stable inflation expectations", "falling inflation expectations"),
    "oil": _d("WTI crude oil vs L6M", "the oil price", "%", 1, " vs L6M",
              "The WTI crude oil price feeds into transport, production and household energy costs",
              "rising inflation pressure and a squeeze on consumers", "neutral energy costs", "falling energy costs"),
    "copper": _d("Copper vs L6M", "the copper price", "%", 1, " vs L6M",
                 "The copper price reflects demand from construction, power grids and electronics",
                 "rising input costs", "neutral input costs", "easing input costs"),
    "stockbond": _d("Stock-bond correlation, L12M", "the stock-bond correlation", "", 2, "",
                    "This measures how closely stock and bond returns moved together over the last 12 months; normally they move in opposite directions",
                    "inflation as the main market risk, with bonds no longer hedging stocks", "bonds partly hedging stocks", "bonds hedging stocks well"),
    "vix": _d("VIX volatility index", "the VIX", "", 1, "",
              "The VIX measures the cost of insuring the S&P 500 against declines over the next 30 days; below 15 is calm, above 30 is panic",
              "elevated fear", "normal levels of fear", "calm markets"),
    "spx_trend": _d("S&P 500 vs 10-month moving average", "the S&P 500", "%", 1, " vs its 10-month average",
                    "This measures the S&P 500 relative to its average of the last 10 months; most major bear markets unfolded below this line",
                    "a broken market trend", "a flat market trend", "a healthy uptrend"),
    "junk": _d("High-yield bonds vs Treasuries, L3M return", "the high-yield bonds' lead", "%", 1, " (L3M)",
               "This measures the 3-month return of high-yield (junk) corporate bonds minus intermediate Treasuries",
               "lenders pulling back from weaker companies", "steady credit markets", "strong appetite for credit risk"),
    "baa": _d("Baa corporate bond spread", "the Baa spread", "pts", 2, "",
              "The Baa spread measures the extra yield medium-quality companies pay over 10-year Treasuries",
              "lenders demanding more for risk", "normal borrowing costs for companies", "easy borrowing for companies"),
    "baa_chg": _d("Baa corporate bond spread vs L6M", "the change in the Baa spread", "pts", 2, " vs L6M",
                  "This measures how much the Baa spread has widened or narrowed over the last 6 months",
                  "credit getting harder to obtain", "stable credit conditions", "credit getting easier to obtain"),
    "banks": _d("Bank stocks vs S&P 500, L6M return", "the banks' lead", "%", 1, " (L6M)",
                "This measures the 6-month return of bank stocks minus the S&P 500; banks lend to the whole economy",
                "expected loan losses or tighter lending", "no stress in banks", "confidence in lending and credit"),
    "dollar_break": _d("US dollar index vs 12-month high", "the dollar", "%", 1, " vs its 12-month high",
                       "This measures the US dollar index relative to its highest level of the past 12 months; a breakout above it makes dollars scarce worldwide",
                       "tightening global liquidity", "neutral global liquidity", "ample global liquidity"),
    "chips_break": _d("Semiconductors vs 12-month high", "semiconductor stocks", "%", 1, " vs their 12-month high",
                      "This measures semiconductor stocks relative to their highest level of the past 12 months; as recent market leaders, a fall of 20% or more signals selling of crowded winners",
                      "investors selling crowded winners", "no stress in market leaders", "strong market leadership"),
    "fedfunds": _d("Fed funds rate vs L12M", "the Fed funds rate", "pts", 2, " vs L12M",
                   "The Fed funds rate is the Federal Reserve's policy rate; increases slow the economy with a lag of 1 to 2 years",
                   "tighter monetary policy", "steady monetary policy", "easier monetary policy"),
    "y10_chg": _d("10-year Treasury yield vs L12M", "the 10-year yield", "pts", 2, " vs L12M",
                  "The 10-year Treasury yield sets the base for mortgage and corporate borrowing costs",
                  "tightening financial conditions", "stable financial conditions", "easing financial conditions"),
    "y10_ngdp": _d("10-year yield minus nominal GDP growth", "the gap", "pts", 2, "",
                   "This measures the 10-year Treasury yield minus nominal GDP growth over the last 12 months; above zero, interest costs grow faster than incomes",
                   "debt becoming harder to carry", "a neutral debt burden", "debt that is easy to carry"),
    "m2": _d("M2 money supply vs L12M", "M2 growth", "%", 1, " vs L12M",
             "M2 measures cash, deposits and money-market funds held by households and businesses",
             "shrinking liquidity", "normal money growth", "ample liquidity supporting spending and asset prices"),
    "dollar": _d("US dollar index vs L12M", "the dollar", "%", 1, " vs L12M",
                 "The US dollar index measures the dollar against major currencies; a stronger dollar tightens global conditions and reduces US companies' foreign earnings",
                 "tightening global conditions", "neutral currency effects", "a tailwind from a weaker dollar"),
    "squeeze": _d("Dollar, oil and yield squeeze index", "the squeeze index", "", 2, "",
                  "This combines the 12-month changes in the dollar, oil and the 10-year yield, each scaled by its usual swings; above zero, all three are rising together",
                  "pressure on company profits", "neutral cost pressure", "falling cost pressure"),
    "realyield": _d("Real 10-year yield", "the real yield", "%", 2, "",
                    "The real yield is the 10-year Treasury yield minus core CPI inflation, the return on bonds after inflation",
                    "cash and bonds competing strongly with stocks", "a neutral real yield", "little competition from bonds"),
    "mortgage": _d("30-year mortgage rate vs L12M", "the mortgage rate", "pts", 2, " vs L12M",
                   "The 30-year fixed mortgage rate sets the monthly cost of buying a home",
                   "a drag on housing", "stable housing affordability", "improving housing affordability"),
    "termprem": _d("10-year term premium vs L12M", "the term premium", "pts", 2, " vs L12M",
                   "The term premium measures the extra yield investors demand to hold a 10-year bond instead of rolling short-term bills",
                   "rising concern about debt and inflation", "stable confidence in bonds", "strong demand for long bonds"),
    "netliq": _d("Fed net liquidity vs L3M", "net liquidity", "$bn", 0, " vs L3M",
                 "Net liquidity measures the Federal Reserve's balance sheet minus the Treasury's cash account and reverse repos, the money available to markets",
                 "liquidity being drained from markets", "stable liquidity", "liquidity being added to markets"),
    "mcap_gdp": _d("Stock market value to GDP", "stock market value", "% of GDP", 0, "",
                   "This measures the total value of US stocks relative to the size of the economy; very high levels have been followed by low long-term returns",
                   "expensive stocks", "fair valuations", "cheap stocks", scale=0.1),
    "hh_equity": _d("Household equity allocation", "the household equity allocation", "%", 0, "",
                    "This measures the share of households' financial assets held in stocks",
                    "households already heavily invested", "a normal allocation", "room for households to buy more stocks", scale=100),
    "cape": _d("Shiller CAPE ratio", "the CAPE ratio", "x", 1, "",
               "The CAPE ratio measures the S&P 500 price relative to average inflation-adjusted earnings of the last 10 years",
               "expensive stocks and lower long-term returns", "fair valuations", "cheap stocks"),
    "rally": _d("S&P 500 L6M return vs volatility", "the speed of the rally", "", 2, "",
                "This measures the S&P 500's 6-month return divided by its usual swings; very fast rallies tend to cool off",
                "a stretched rally", "a normal pace of gains", "room for the market to recover"),
    "leadership": _d("S&P 500 vs median sector, L12M return", "the leadership gap", "%", 1, " (L12M)",
                     "This measures the S&P 500's 12-month return minus that of the typical sector; high readings mean a few large stocks carry the index",
                     "narrow, fragile leadership", "balanced leadership", "broad leadership"),
}
assert set(DISPLAY) == set(IND), set(IND) ^ set(DISPLAY)

# ------------------------------------------------------------------ 20 industries
# etf = what the calls apply to and what the backtest trades; proxy = Kenneth French industries used for history
# before the ETF existed (1960 on).
INDUSTRIES = [
    dict(etf="SMH", name="Semiconductors", proxy=["Chips"]),
    dict(etf="IGV", name="Software", proxy=["Softw"]),
    dict(etf="VOX", name="Communication", proxy=["Telcm"]),
    dict(etf="KBE", name="Banks", proxy=["Banks"]),
    dict(etf="KRE", name="Regional banks", proxy=["Banks"]),
    dict(etf="KIE", name="Insurance", proxy=["Insur"]),
    dict(etf="ITB", name="Home builders", proxy=["Cnstr", "BldMt"]),
    dict(etf="XRT", name="Retail", proxy=["Rtail"]),
    dict(etf="IYT", name="Transportation", proxy=["Trans"]),
    dict(etf="XLI", name="Industrials", proxy=["Mach", "ElcEq"]),
    dict(etf="ITA", name="Aerospace and defense", proxy=["Aero", "Guns"]),
    dict(etf="XLE", name="Energy", proxy=["Oil"]),
    dict(etf="XLU", name="Utilities", proxy=["Util"]),
    dict(etf="XLP", name="Consumer staples", proxy=["Food", "Soda", "Beer", "Smoke", "Hshld"]),
    dict(etf="XLV", name="Health care", proxy=["Hlth", "MedEq", "Drugs"]),
    dict(etf="XBI", name="Biotech", proxy=["Drugs"]),
    dict(etf="XLB", name="Materials", proxy=["Chems", "Steel", "Paper", "Boxes"]),
    dict(etf="XME", name="Metals and mining", proxy=["Mines", "Steel", "Coal"]),
    dict(etf="GDX", name="Gold miners", proxy=["Gold"]),
    dict(etf="IYR", name="Real estate", proxy=["RlEst"]),
]

# ------------------------------------------------------------------ what the investors said each state means
# For every state: (etf list to overweight, etf list to underweight, the reason in plain words, who said it).
# The STRESS overlay is added on top when market stress is high. A call only stands if past months of the same
# situation agree (engine.calls); otherwise the industry stays neutral.
DEF = ["XLU", "XLP", "XLV"]
RULES = {
    "expansion": dict(
        over=["SMH", "IGV", "VOX", "XLI", "XRT"], under=["XLU", "XLP"],
        why="When growth broadens, economy-sensitive stocks lead and safe stocks lag.",
        who=[T("Druckenmiller", 76), T("Druckenmiller", 78)]),
    "late": dict(
        over=["XLE", "XLV", "XBI", "XLP"], under=["ITB", "IYT", "XRT", "ITA", "SMH"],
        why="Peak-margin businesses (retail, trucking) and home builders roll over first; money rotates to biotech "
            "and old-economy names with real earnings; crowded themes like defense and chips crack.",
        who=[T("Druckenmiller", 77), X("2026-06-09"), X("2026-06-24"), X("2026-06-16"), T("Druckenmiller", 79)]),
    "overheating": dict(
        over=["XLE", "XLB", "XME", "GDX"], under=["IGV", "XBI", "IYR", "XLU", "ITB"],
        why="Hot inflation favours commodity producers and hard assets; it hurts stocks valued on distant profits "
            "and anything that needs low rates.",
        who=[T("Karniol-Tambour", 104), T("Calderini", 153), T("Druckenmiller", 79), X("2026-10-16")]),
    "contraction": dict(
        over=["XLU", "XLP", "XLV", "KIE"], under=["KBE", "KRE", "ITB", "XRT", "IYT", "XME", "XLI"],
        why="In a downturn utilities, staples and drug makers hold up while banks, home builders, autos, retail "
            "and trucking fall hardest; property insurers are the safe corner of financials.",
        who=[T("Druckenmiller", 76), T("Druckenmiller", 77), T("Eisman", 148)]),
    "stagflation": dict(
        over=["GDX", "XLE", "XLP", "XLV"], under=["XRT", "ITB", "KBE", "IGV", "SMH", "IYR"],
        why="With weak growth and hot prices, gold and energy hold value; spending-sensitive and rate-sensitive "
            "stocks suffer.",
        who=[T("Druckenmiller", 77), T("Calderini", 153), T("Karniol-Tambour", 104)]),
    "recovery": dict(
        over=["ITB", "KBE", "KRE", "XLB", "XME", "XLI", "IYT", "XRT"], under=["XLU", "XLP", "SMH", "IGV"],
        why="Industries that cut capacity in the downturn earn more as demand returns; commodities lead out of the "
            "bear market and last cycle's tech leaders don't.",
        who=[T("Druckenmiller", 77), X("2026-10-16"), X("2026-08-28")]),
}
STRESS = dict(
    over=["XLP", "XLV", "XLU", "KIE"], under=["SMH", "IGV", "XBI", "KRE", "XME", "IYT"],
    why="When markets turn risk-off, cash and safe stocks first; leveraged, crowded and commodity names get "
        "liquidated, including metals, until the dollar squeeze ends.",
    who=[X("2026-10-16"), X("2026-10-05"), T("Eisman", 148), T("Druckenmiller", 75)])

STAGES = {
    "expansion": ("Expansion", "Growth is solid and getting stronger."),
    "late": ("Late cycle", "Growth is still solid but starting to weaken."),
    "overheating": ("Overheating", "Growth is solid but inflation is running hot."),
    "contraction": ("Contraction", "Growth is weak and getting weaker."),
    "stagflation": ("Stagflation", "Growth is weakening while inflation runs hot."),
    "recovery": ("Recovery", "Growth is weak but starting to improve."),
}
