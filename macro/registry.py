"""Macro Compass: the indicator library, the six pillars and the 20 industries.

Every indicator is a claim made by an investor in the research store (transcript id) or in the X posts of
@AtlasShrug1 ("Galt", dated), turned into a fixed, testable rule. Investors propose, the backtest decides.
Pre-registered 2026-10-23 (v1.0.0). Change log: macro/CHANGES.md. Never edit a rule in place: add a version.
"""
VERSION = "1.0.0"

# ------------------------------------------------------------------ fixed settings (pre-registered)
SETTINGS = {
    "start": "1960-01",            # first month of the monthly grid
    "score_min_years": 10,         # an indicator scores only once it has 10 years of its own history
    "warmup_years": 15,            # industry odds need 15 years of past outcomes before they are reported
    "horizons": [6, 12],           # months ahead (the site's switch)
    "outcome_band": {6: 0.07, 12: 0.10},   # beat / lag the market by at least this much = opportunity / risk
    "driver_buckets": 5,           # past months are grouped by driver score into fifths
    "tilt_ratio": 1.5,             # odds must be 1.5x their normal rate to act
    "tilt_size": 0.5,              # overweight = 1.5x the equal weight, underweight = 0.5x
    "stage_smooth": 6,             # stage reads the 6-month average of growth pressure
    "stage_lookback": 12,          # direction = change in that average over 12 months ...
    "stage_band": 8,               # ... of 8+ points (else the last direction holds)
    "stage_hysteresis": 5,         # weak growth from 55 up, solid from 45 down (else the last level holds)
    "stage_confirm": 3,            # a new stage needs 3 months in a row
    "etf_backtest_start": "2006-07",  # first month most of the 20 ETFs trade
}

# ------------------------------------------------------------------ pillars (score 0-100 = pressure; 100 = worst in history)
PILLARS = [
    ("growth", "Growth", "Is the economy slowing?"),
    ("inflation", "Inflation", "Are prices speeding up?"),
    ("liquidity", "Money and rates", "Is money getting tighter?"),
    ("credit", "Credit stress", "Are borrowers and lenders under strain?"),
    ("froth", "Froth", "Are stocks priced for perfection?"),
    ("internals", "Market health", "Are most stocks joining in?"),
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
YAHOO = ["SPY", "EWY", "DX-Y.NYB", "HYG", "IEF", "XLY", "SOXX"]   # plus every industry ETF below
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
# calc: how the raw data becomes one number per month (macro/engine.py CALCS). dir +1: a higher number means more
# pressure (weaker growth, hotter prices, tighter money, more stress, more froth, weaker market). pillar None =
# used only inside an industry's cause chain.
INDICATORS = [
    # growth
    dict(id="jobs_alarm", pillar="growth", name="Jobs alarm (Sahm rule)", calc=("sahm", "UNRATE"), dir=1,
         plain="Unemployment rising off its low", who=[T("Gerstner", 215)]),
    dict(id="truck", pillar="growth", name="Truck freight vs a year ago", calc=("yoy", "TRUCKD11"), dir=-1,
         plain="Trucking volumes", who=[T("Druckenmiller", 102), T("Druckenmiller", 77)]),
    dict(id="permits", pillar="growth", name="New home permits, 6-month change", calc=("chg6pct", "PERMIT"), dir=-1,
         plain="Home building", who=[T("Druckenmiller", 76)]),
    dict(id="autos", pillar="growth", name="Car sales, 6-month change", calc=("chg6pct", "TOTALSA"), dir=-1,
         plain="Car buying", who=[T("Druckenmiller", 76)]),
    dict(id="cyc_def", pillar="growth", name="Cyclical vs defensive stocks, 6 months", calc=("cycdef",), dir=-1,
         plain="Economy-sensitive stocks vs safe stocks", who=[T("Druckenmiller", 76), T("Druckenmiller", 77)]),
    dict(id="curve", pillar="growth", name="Yield curve (10-year minus 2-year)", calc=("spread", "GS10", "GS2"),
         dir=-1, plain="Long vs short interest rates", who=[T("Roche", 265), T("Druckenmiller", 76)]),
    dict(id="youth", pillar="growth", name="Young-adult jobless rate vs overall, 12-month change",
         calc=("gapchg12", "LNS14024887", "UNRATE"), dir=1, plain="Jobs for young adults",
         who=[T("Eisman", 147)]),
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
    # money and rates
    dict(id="fedfunds", pillar="liquidity", name="Fed interest rate, 12-month change", calc=("chg12", "FEDFUNDS"), dir=1,
         plain="Fed raising or cutting", who=[T("van Eck", 81)]),
    dict(id="y10_ngdp", pillar="liquidity", name="10-year yield minus economic growth", calc=("y10ngdp",), dir=1,
         plain="Bond yields vs growth", who=[T("Druckenmiller", 79)]),
    dict(id="m2", pillar="liquidity", name="Money supply (M2) growth", calc=("yoy", "M2SL"), dir=-1,
         plain="Money supply", who=[T("Druckenmiller", 76), T("Druckenmiller", 102)]),
    dict(id="dollar", pillar="liquidity", name="US dollar, 12-month change", calc=("dollar",), dir=1,
         plain="The dollar", who=[T("Gromen", 159), T("Druckenmiller", 75), X("2026-06-11")]),
    dict(id="realyield", pillar="liquidity", name="Real 10-year yield (after inflation)", calc=("realyield",), dir=1,
         plain="Interest rates after inflation", who=[T("Gerstner", 215), T("Rogoff", 264)]),
    dict(id="mortgage", pillar="liquidity", name="Mortgage rate, 12-month change", calc=("chg12", "MORTGAGE30US"), dir=1,
         plain="Mortgage rates", who=[T("Guha", 136)]),
    dict(id="termprem", pillar="liquidity", name="Extra yield on long bonds (term premium), 12-month change",
         calc=("chg12", "THREEFYTP10"), dir=1, plain="Bond investors' nerves", who=[T("Tropin", 151)]),
    dict(id="netliq", pillar="liquidity", name="Fed money in the system, 3-month change", calc=("netliq",), dir=-1,
         plain="Fed liquidity", who=[T("Druckenmiller", 78), T("Citrone", 267)]),
    # credit stress
    dict(id="baa", pillar="credit", name="Corporate bond spread (Baa minus 10-year)", calc=("spread", "BAA", "GS10"), dir=1,
         plain="Extra yield companies pay to borrow", who=[T("Druckenmiller", 76)]),
    dict(id="baa_chg", pillar="credit", name="Corporate bond spread, 6-month change", calc=("spreadchg6", "BAA", "GS10"),
         dir=1, plain="Is borrowing getting harder", who=[T("Druckenmiller", 76)]),
    dict(id="banks", pillar="credit", name="Bank stocks vs market, 6 months", calc=("rel6", "KBE"), dir=-1,
         plain="Bank stocks", who=[T("Druckenmiller", 76), X("2026-10-14")]),
    dict(id="vix", pillar="credit", name="Stock market fear gauge (VIX)", calc=("level", "VIXCLS"), dir=1,
         plain="Fear in the stock market", who=[T("Calderini", 155), T("Tropin", 151)]),
    dict(id="cards", pillar="credit", name="Credit-card late payments, 12-month change", calc=("chg12", "DRCCLACBS"),
         dir=1, plain="Consumers falling behind", who=[T("Bessent", 270), T("Gerstner", 215)]),
    # froth
    dict(id="mcap_gdp", pillar="froth", name="Stock market value vs the economy", calc=("ratio", "NCBEILQ027S", "GDP"),
         dir=1, plain="Stocks vs GDP", who=[X("2026-08-08")]),
    dict(id="hh_equity", pillar="froth", name="Share of household savings in stocks",
         calc=("ratio", "HNOCEAQ027S", "TFAABSHNO"), dir=1, plain="How much households own in stocks",
         who=[X("2026-08-08")]),
    dict(id="cape", pillar="froth", name="Price vs 10-year average earnings (CAPE)", calc=("cape",), dir=1,
         plain="Stock valuations", who=[X("2026-08-08"), T("Tropin", 149)]),
    dict(id="rally", pillar="froth", name="Speed of the stock rally (6-month gain vs its swings)", calc=("rally",), dir=1,
         plain="How fast stocks have run", who=[T("Calderini", 155)]),
    # market health
    dict(id="breadth", pillar="internals", name="Industries in an uptrend", calc=("breadth",), dir=-1,
         plain="How many industries are rising", who=[T("Verrone", 156)]),
    dict(id="breakdowns", pillar="internals", name="Industries 20%+ below their 12-month high", calc=("breakdowns",),
         dir=1, plain="How many industries are falling apart", who=[X("2026-09-23")]),
    dict(id="leadership", pillar="internals", name="Narrow leadership (index vs typical industry, 12 months)",
         calc=("leadership",), dir=1, plain="Is the rise led by a few", who=[T("Druckenmiller", 79)]),
    dict(id="transports", pillar="internals", name="Transport vs industrial stocks, 6 months",
         calc=("relpair6", "IYT", "XLI"), dir=-1, plain="Transports confirming", who=[X("2026-09-02")]),
    dict(id="homebuilders", pillar="internals", name="Home builders vs market, 12 months", calc=("rel12", "ITB"),
         dir=-1, plain="Home builders", who=[X("2026-06-09"), T("Druckenmiller", 76)]),
    # used only in industry cause chains
    dict(id="y2", pillar=None, name="2-year Treasury yield, 6-month change", calc=("chg6", "GS2"), dir=1,
         plain="Short-term rates", who=[T("Druckenmiller", 76)]),
    dict(id="korea", pillar=None, name="Korea stocks vs chip stocks, 6 months", calc=("korea",), dir=-1,
         plain="Korea leading chips", who=[X("2026-06-29")]),
    dict(id="cu_fe", pillar=None, name="Copper vs iron ore, 6 months", calc=("cufe",), dir=-1,
         plain="Build-out demand vs China demand", who=[T("Verrone", 156)]),
]
IND = {i["id"]: i for i in INDICATORS}

# ------------------------------------------------------------------ 20 industries
# etf = what the actions apply to and what the backtest trades; proxy = Kenneth French industries used to teach the
# model before the ETF existed (1960 on). drivers: (indicator or pillar id, sign). sign +1: pressure on that
# indicator is a headwind for the industry; -1: it is a tailwind.
INDUSTRIES = [
    dict(etf="SMH", name="Semiconductors", proxy=["Chips"],
         drivers=[("liquidity", 1), ("froth", 1), ("korea", 1), ("cu_fe", 1)],
         who=[X("2026-06-29"), T("Eisman", 148), T("Gurley", 215)]),
    dict(etf="IGV", name="Software", proxy=["Softw"], drivers=[("realyield", 1), ("liquidity", 1), ("froth", 1)],
         who=[T("Citrone", 267), T("Gerstner", 214)]),
    dict(etf="VOX", name="Communication", proxy=["Telcm"], drivers=[("realyield", 1), ("growth", 1)], who=[]),
    dict(etf="KBE", name="Banks", proxy=["Banks"], drivers=[("y2", -1), ("curve", 1), ("credit", 1)],
         who=[T("Druckenmiller", 76), X("2026-10-14")]),
    dict(etf="KRE", name="Regional banks", proxy=["Banks"], drivers=[("y2", -1), ("curve", 1), ("credit", 1), ("mortgage", 1)],
         who=[T("Druckenmiller", 102)]),
    dict(etf="KIE", name="Insurance", proxy=["Insur"], drivers=[("growth", -1), ("credit", 1)], who=[T("Eisman", 148)]),
    dict(etf="ITB", name="Home builders", proxy=["Cnstr", "BldMt"], drivers=[("mortgage", 1), ("permits", 1), ("homebuilders", 1)],
         who=[T("Guha", 136), X("2026-06-09")]),
    dict(etf="XRT", name="Retail", proxy=["Rtail"], drivers=[("youth", 1), ("cards", 1), ("oil", 1), ("growth", 1)],
         who=[T("Gerstner", 215), T("Eisman", 147)]),
    dict(etf="IYT", name="Transportation", proxy=["Trans"], drivers=[("truck", 1), ("oil", 1), ("transports", 1), ("growth", 1)],
         who=[T("Druckenmiller", 77), X("2026-09-02")]),
    dict(etf="XLI", name="Industrials", proxy=["Mach", "ElcEq"], drivers=[("growth", 1), ("dollar", 1)], who=[]),
    dict(etf="ITA", name="Aerospace and defense", proxy=["Aero", "Guns"], drivers=[("growth", 1), ("froth", 1)],
         who=[X("2026-06-16")]),
    dict(etf="XLE", name="Energy", proxy=["Oil"], drivers=[("oil", -1), ("inflation", -1), ("dollar", 1)],
         who=[T("Bessent", 269), T("Lagarde", 261)]),
    dict(etf="XLU", name="Utilities", proxy=["Util"], drivers=[("growth", -1), ("realyield", 1)], who=[T("Druckenmiller", 76)]),
    dict(etf="XLP", name="Consumer staples", proxy=["Food", "Soda", "Beer", "Smoke", "Hshld"],
         drivers=[("growth", -1), ("internals", -1)], who=[T("Druckenmiller", 76), T("Eisman", 148)]),
    dict(etf="XLV", name="Health care", proxy=["Hlth", "MedEq", "Drugs"], drivers=[("growth", -1), ("internals", -1)],
         who=[T("Druckenmiller", 76), T("Eisman", 148)]),
    dict(etf="XBI", name="Biotech", proxy=["Drugs"], drivers=[("liquidity", 1), ("realyield", 1)], who=[]),
    dict(etf="XLB", name="Materials", proxy=["Chems", "Steel", "Paper", "Boxes"],
         drivers=[("dollar", 1), ("copper", -1), ("growth", 1)], who=[T("Gromen", 159)]),
    dict(etf="XME", name="Metals and mining", proxy=["Mines", "Steel", "Coal"],
         drivers=[("dollar", 1), ("copper", -1), ("growth", 1)], who=[T("Verrone", 156), X("2026-10-14")]),
    dict(etf="GDX", name="Gold miners", proxy=["Gold"], drivers=[("realyield", 1), ("dollar", 1)],
         who=[T("Calderini", 153), T("Bessent", 270), X("2026-10-14")]),
    dict(etf="IYR", name="Real estate", proxy=["RlEst"], drivers=[("realyield", 1), ("credit", 1)], who=[]),
]

STAGES = {
    "expansion": ("Expansion", "Growth is solid and getting stronger."),
    "late": ("Late cycle", "Growth is still solid but starting to weaken."),
    "contraction": ("Contraction", "Growth is weak and getting weaker."),
    "recovery": ("Recovery", "Growth is weak but starting to improve."),
}
