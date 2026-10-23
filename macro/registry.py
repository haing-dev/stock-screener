"""Macro Compass: the indicator library, the six pillars and the 20 industries.

Every indicator is a claim made by an investor in the research store (transcript id) or in the X posts of
@AtlasShrug1 ("Galt", dated), turned into a fixed, testable rule. Investors propose, the backtest decides.
v1.0.0 pre-registered 2026-10-23; v2.0.0 the same day (state -> investor sector rules + history check). Change log: macro/CHANGES.md. Never edit a rule in place: add a version.
"""
VERSION = "2.1.0"

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
# (unit, multiplier for display, decimals, why it matters in plain words). Display only: no effect on the calls.
DISPLAY = {
    "jobs_alarm": ("pts", 1, 2, "When the 3-month average jobless rate climbs 0.5 points above its low of the past year, a recession has almost always already started."),
    "truck": ("%", 1, 1, "Trucks move most goods. Freight below last year's level shows demand for goods shrinking before it shows up in GDP."),
    "permits": ("%", 1, 1, "Builders file permits months before they build. Falling permits mean less construction, fewer jobs and less spending ahead."),
    "autos": ("%", 1, 1, "A car is the biggest purchase people can put off. Falling car sales are an early sign households are pulling back."),
    "curve": ("pts", 1, 2, "Long-term minus short-term interest rates. Below 0 (inverted), lending pays less and credit tightens; most recessions followed an inversion."),
    "youth": ("pts", 1, 2, "Young workers are hired last and let go first. Their jobless rate rising faster than the overall rate is an early crack in the job market."),
    "cards": ("pts", 1, 2, "More credit-card bills paid late means households are running out of room. Spending usually slows next."),
    "cyc_def": ("%", 1, 1, "6-month return of economy-sensitive stocks (home builders, banks, transports, retail, miners) minus safe stocks (utilities, staples, health care). Below 0: the market is bracing for a slowdown."),
    "staples_disc": ("%", 1, 1, "6-month return of staples minus discretionary stocks. Above 0: investors expect people to cut back on things they don't need."),
    "breadth": ("%", 1, 0, "Share of the 20 industries above their 10-month average. Healthy rallies lift most industries; a falling share means the rally is narrowing."),
    "breakdowns": ("%", 1, 0, "Share of the 20 industries 20% or more below their 12-month high, i.e. in their own bear market. A rising share often comes before the index falls."),
    "transports": ("%", 1, 1, "6-month return of transport minus industrial stocks. Goods have to be shipped: transports lagging means the market doubts demand will last."),
    "homebuilders": ("%", 1, 1, "Home builders vs the S&P 500, measured from their best point of the last 2 years. Builders react first to rates and household demand; a deep fall has been an early warning."),
    "core_pce": ("pts", 1, 2, "Core inflation (no food or energy) over the last 3 months, annualised, minus the last 12 months. Above 0: inflation is speeding up and the Fed can't cut."),
    "core_cpi": ("%", 1, 1, "Core consumer prices vs a year ago. The further above 2%, the longer interest rates stay high."),
    "ppi": ("%", 1, 1, "What businesses pay for goods and inputs vs a year ago. Rises reach consumer prices or squeeze profits."),
    "inflexp": ("pts", 1, 2, "Change in the inflation rate bond markets expect 5 years ahead. A rise means investors fear inflation is getting stuck."),
    "oil": ("%", 1, 1, "Oil feeds into almost every price. A sharp rise lifts inflation and works like a tax on consumers."),
    "copper": ("%", 1, 1, "Copper goes into buildings, power grids and electronics. A rising price means strong demand and rising costs."),
    "stockbond": ("", 1, 2, "Normally bonds rise when stocks fall (below 0). When they move together (above 0), inflation is the main worry and bonds stop protecting a portfolio."),
    "vix": ("", 1, 1, "The price of insurance against a stock-market fall. Below 15 is calm, above 30 is panic."),
    "spx_trend": ("%", 1, 1, "S&P 500 vs its average of the last 10 months. Below 0 the main trend has turned down; most big bear markets happened below this line."),
    "junk": ("%", 1, 1, "3-month return of junk bonds minus safe Treasuries. Junk lagging means lenders are pulling back from weaker companies; stress usually shows here before stocks."),
    "baa": ("pts", 1, 2, "Extra interest medium-quality companies pay over the government. A wider gap means lenders want more for the risk."),
    "baa_chg": ("pts", 1, 2, "6-month change in that gap. A fast widening means credit is getting harder to get right now."),
    "banks": ("%", 1, 1, "6-month return of bank stocks minus the S&P 500. Banks lend to the whole economy; lagging bank stocks point to loan losses or tighter lending."),
    "dollar_break": ("%", 1, 1, "The dollar vs its highest level of the past 12 months. At or above 0 (a breakout), dollars get scarce worldwide and risky assets get sold."),
    "chips_break": ("%", 1, 1, "Chip stocks vs their 12-month high. They led the market; a fall of 20% or more means investors are selling crowded winners."),
    "fedfunds": ("pts", 1, 2, "Change in the Fed's interest rate over a year. Hikes slow the economy with a delay of 1 to 2 years; cuts help."),
    "y10_chg": ("pts", 1, 2, "Change in the 10-year Treasury yield over a year. It sets mortgage and business borrowing costs; a fast rise tightens conditions."),
    "y10_ngdp": ("pts", 1, 2, "10-year yield minus the economy's growth rate (before inflation). Above 0, debt gets harder to carry."),
    "m2": ("%", 1, 1, "Money supply vs a year ago. More money supports spending and asset prices; shrinking money does the opposite."),
    "dollar": ("%", 1, 1, "The dollar vs a year ago. A stronger dollar tightens money worldwide and cuts US companies' foreign profits."),
    "squeeze": ("", 1, 2, "Dollar, oil and the 10-year yield over the last year, each against its usual swings, combined. Above 0: all three rising together, squeezing company profits."),
    "realyield": ("%", 1, 2, "10-year yield minus core inflation. A high real yield makes cash and bonds more attractive than stocks."),
    "mortgage": ("pts", 1, 2, "Change in the 30-year mortgage rate over a year. Higher rates slow home buying."),
    "termprem": ("pts", 1, 2, "Change over a year in the extra yield investors want for holding long bonds. A rise shows worry about debt and inflation."),
    "netliq": ("$bn", 1, 0, "3-month change in Fed money available to markets (Fed balance sheet minus Treasury cash and reverse repos). Falling liquidity has weighed on stocks."),
    "mcap_gdp": ("% of GDP", 0.1, 0, "Total US stock market value vs the size of the economy. Very high levels have been followed by low long-term returns."),
    "hh_equity": ("%", 100, 0, "Share of household financial assets held in stocks. A high share leaves little cash to buy more."),
    "cape": ("x", 1, 1, "Stock prices vs average earnings of the last 10 years. A high ratio has meant lower returns over the following decade."),
    "rally": ("", 1, 2, "6-month gain of the S&P 500 vs its usual swings. Very fast rallies tend to cool off."),
    "leadership": ("%", 1, 1, "12-month return of the S&P 500 minus the typical industry. High: gains come from a few big stocks, a fragile base."),
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
