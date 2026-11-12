"""LSEG Workspace pull set v1 (2026-11-12), built after probe v1 (tools/bbgq/results/lseg_probe_v1.txt).
Only methods that returned DATED data in the probe are used in the L files:
  RHistory (Workspace quotes: BID.Timestamp;BID.Close)   -> FX spot, forwards, implied vol, swaps
  RDP.Data (TR fields with .date)                         -> government yields, equity and volatility indexes
  DSGRID   (Datastream)                                   -> benchmark bond yields and return indexes, equity markets
P2 is a second probe: futures (how to get dates, which roots exist, curve depth), commodity indexes, MSCI, short
rates, swaps, economics with polls. Some codes are guesses; an error text is a useful answer.
Layout of every data sheet: one block per series, block width W columns; row 2 id, row 3 label, row 4 formula text,
row 6 the formula (results fill down and right). First sheet "Check": live status per block.
usage: python3 docs/data_requests/build_lseg_pull.py [out dir]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lseg_pull_helpers import build, hp, ds, rd, rh   # noqa: E402

DELIV = ["EUR", "JPY", "GBP", "CHF", "CAD", "AUD", "NZD", "SEK", "NOK", "DKK", "MXN", "ZAR", "TRY", "PLN", "HUF", "CZK", "ILS",
         "SGD", "THB", "HKD", "CNH"]
NDF = ["KRW", "INR", "IDR", "PHP", "TWD", "CNY", "MYR", "BRL", "CLP", "COP", "PEN"]
# L1a FX spot and forward points
P = [("Spot", "%s spot vs USD" % c, rh(c + "=")) for c in DELIV + NDF]
for t in ("1M", "3M", "1Y"):
    P += [("Fwd " + t, "%s %s forward points" % (c, t), rh("%s%s=" % (c, t))) for c in DELIV]
    P += [("Fwd " + t, "%s %s non-deliverable forward" % (c, t), rh("%s%sNDF=" % (c, t))) for c in NDF]
n = build("L1a_fx_spot_forwards", "LSEG pull L1a: FX spot and forwards (monthly)", P)
# L1b FX implied volatility, swaps
VOL = ["EUR", "JPY", "GBP", "CHF", "CAD", "AUD", "NZD", "SEK", "NOK", "MXN", "BRL", "ZAR", "TRY", "PLN", "KRW", "INR", "CNH", "SGD", "HUF", "ILS"]
P = []
for t in ("1M", "3M", "1Y"):
    P += [("Vol " + t, "%s/USD %s implied volatility" % (c, t), rh("%s%sO=" % (c, t))) for c in VOL]
P += [("Swaps", "USD SOFR swap %s" % t, rh("USDSROIS%s=" % t)) for t in ("1Y", "2Y", "3Y", "5Y", "7Y", "10Y", "30Y")]
n += build("L1b_fx_vol_swaps", "LSEG pull L1b: FX implied volatility and SOFR swaps (monthly)", P)
# L2 rates: Datastream benchmark government indexes (yield + return index) and Workspace yields
DSC = [("US", "United States"), ("UK", "United Kingdom"), ("BD", "Germany"), ("FR", "France"), ("IT", "Italy"), ("ES", "Spain"),
       ("NL", "Netherlands"), ("BG", "Belgium"), ("SW", "Switzerland"), ("SD", "Sweden"), ("NW", "Norway"), ("DK", "Denmark"),
       ("JP", "Japan"), ("AU", "Australia"), ("NZ", "New Zealand"), ("CN", "Canada")]
P = []
for t in ("02", "05", "10", "30"):
    P += [("DS bench %sy" % t, "%s %sy benchmark: yield, return index" % (nm, t), ds("BM%s%sY" % (cc, t), "RY,RI")) for cc, nm in DSC]
n += build("L2a_rates_datastream", "LSEG pull L2a: Datastream benchmark government bonds (monthly)", P)
RC = ["US", "DE", "GB", "FR", "IT", "ES", "NL", "BE", "CH", "SE", "NO", "DK", "JP", "AU", "NZ", "CA"]
P = []
for t in ("2", "5", "10", "30"):
    P += [("Yield %sy" % t, "%s %sy government bid yield" % (cc, t), rd("%s%sYT=RR" % (cc, t), "TR.BIDYIELD")) for cc in RC]
n += build("L2b_rates_workspace", "LSEG pull L2b: Workspace government yields (monthly)", P)
# L3 equity markets and indexes
TM = [("US", "United States"), ("UK", "United Kingdom"), ("BD", "Germany"), ("FR", "France"), ("IT", "Italy"), ("ES", "Spain"),
      ("NL", "Netherlands"), ("SW", "Switzerland"), ("SD", "Sweden"), ("JP", "Japan"), ("AU", "Australia"), ("CN", "Canada"),
      ("HK", "Hong Kong"), ("KO", "Korea"), ("TA", "Taiwan"), ("IN", "India"), ("BR", "Brazil"), ("MX", "Mexico"),
      ("SA", "South Africa"), ("CH", "China"), ("WD", "World")]
P = [("DS markets", "%s total market: price, return, P/E, dividend yield, market value" % nm, ds("TOTMK" + cc, "PI,RI,PE,DY,MV")) for cc, nm in TM]
IDX = [(".SPX", "S&P 500"), (".NDX", "Nasdaq 100"), (".RUT", "Russell 2000"), (".STOXX50E", "Euro Stoxx 50"), (".GDAXI", "DAX"),
       (".FTSE", "FTSE 100"), (".FCHI", "CAC 40"), (".N225", "Nikkei 225"), (".TOPX", "Topix"), (".HSI", "Hang Seng"),
       (".AXJO", "ASX 200"), (".GSPTSE", "TSX"), (".KS11", "Kospi"), (".TWII", "Taiex"), (".BSESN", "Sensex"), (".BVSP", "Bovespa"),
       (".MXX", "IPC Mexico"), (".SSEC", "Shanghai Composite"), (".CSI300", "CSI 300"), (".VIX", "VIX"), (".V2TX", "VStoxx"),
       (".MOVE", "MOVE"), (".DXY", "Dollar index")]
P += [("Indexes", nm + " close", rd(r, "TR.PriceClose")) for r, nm in IDX]
P += [("DS other", lab, ds(c, dt)) for c, dt, lab in [
    ("S&PCOMP", "PI,RI", "S&P 500 price and total return"), ("MSWRLD$", "PI,RI", "MSCI World price and total return"),
    ("GSCITOT", "", "S&P GSCI total return"), ("CRUDOIL", "", "WTI spot"), ("GOLDBLN", "", "Gold bullion"),
    ("LCPCASH", "", "LME copper cash"), ("NCLCS00", "", "WTI continuous future"), ("USCONPRCE", "", "US CPI"),
    ("USUN%TOTQ", "", "US unemployment rate"), ("USCNFBUSQ", "", "US ISM manufacturing")]]
n += build("L3_equity_markets", "LSEG pull L3: equity markets, indexes, a few Datastream series (monthly)", P, W=8)

# P2: second probe
P = []
for ric in ("CLc1", "TYc1"):
    P += [("Futures dates", "%s: dates by display option" % ric, hp(ric, disp="CH:Fd RH:Timestamp")),
          ("Futures dates", "%s: dates by display option, sorted" % ric, hp(ric, disp="SORT:ASC TSREPEAT:NO CH:Fd RH:Timestamp")),
          ("Futures dates", "%s: DATE as a field" % ric, hp(ric, fields="DATE;CLOSE")),
          ("Futures dates", "%s: RHistory default fields" % ric, rh(ric, fam="")),
          ("Futures dates", "%s: RHistory trade price" % ric, rh(ric, fam="TRDPRC_1")),
          ("Futures dates", "%s: RHistory settlement" % ric, rh(ric, fam="SETTLE")),
          ("Futures dates", "%s: through Datastream" % ric, ds("<%s>" % ric)),
          ("Futures dates", "%s: settlement price data field" % ric, rd(ric, "TR.SETTLEMENTPRICE")),
          ("Futures dates", "%s: close price data field" % ric, rd(ric, "TR.CLOSEPRICE"))]
P += [("Futures dates", "US 10y yield: RHistory bid yield", rh("US10YT=RR", fam="B_YLD_1")),
      ("Futures dates", "US 10y yield: RHistory default fields", rh("US10YT=RR", fam="")),
      ("Futures dates", "S&P 500: RHistory default fields", rh(".SPX", fam="")),
      ("Futures dates", "Datastream monthly from a month-end start", ds("S&PCOMP", "PI", "1989-12-31")),
      ("Futures dates", "Datastream WTI continuous, 2nd position guess", ds("NCLCS20")),
      ("Futures dates", "Datastream WTI continuous, type 01", ds("NCLCS01"))]
ROOTS = [("CL", "WTI crude"), ("LCO", "Brent"), ("HO", "Heating oil"), ("RB", "Gasoline"), ("LGO", "Gasoil"), ("NG", "Natural gas"),
         ("GC", "Gold"), ("SI", "Silver"), ("HG", "Copper"), ("PL", "Platinum"), ("PA", "Palladium"), ("C", "Corn"), ("S", "Soybeans"),
         ("W", "Wheat"), ("KW", "Kansas wheat"), ("BO", "Soybean oil"), ("SM", "Soybean meal"), ("SB", "Sugar"), ("KC", "Coffee"),
         ("CC", "Cocoa"), ("CT", "Cotton"), ("LC", "Live cattle"), ("LH", "Lean hogs"), ("FC", "Feeder cattle"), ("OJ", "Orange juice"),
         ("LB", "Lumber"), ("MCU", "LME copper"), ("MAL", "LME aluminium"), ("MZN", "LME zinc"), ("MNI", "LME nickel"),
         ("TU", "US 2y note"), ("FV", "US 5y note"), ("TY", "US 10y note"), ("US", "US long bond"), ("UB", "US ultra bond"),
         ("FGBS", "Schatz"), ("FGBM", "Bobl"), ("FGBL", "Bund"), ("FGBX", "Buxl"), ("FLG", "Long gilt"), ("FOAT", "OAT"),
         ("FBTP", "BTP"), ("JGB", "JGB 10y"), ("CGB", "Canada 10y"), ("YTC", "Australia 10y"), ("YTT", "Australia 3y"),
         ("SRA", "3m SOFR"), ("FF", "Fed funds"), ("FEI", "Euribor"), ("SON3", "3m SONIA"), ("FSS", "Short sterling"),
         ("BAX", "Canada BA"), ("YBA", "Australia bank bills"), ("FES", "Euroswiss"), ("ED", "Eurodollar"),
         ("ES", "S&P 500 e-mini"), ("NQ", "Nasdaq e-mini"), ("RTY", "Russell 2000 e-mini"), ("YM", "Dow e-mini"),
         ("STXE", "Euro Stoxx 50"), ("FDX", "DAX"), ("FFI", "FTSE 100"), ("JNI", "Nikkei"), ("HSI", "Hang Seng"), ("YAP", "ASX SPI"),
         ("SXF", "TSX 60"), ("VX", "VIX future")]
P += [("Futures roots", "%s, 1st contract (%sc1)" % (nm, r), hp(r + "c1")) for r, nm in ROOTS]
P += [("Curve depth", "%s contract %d" % (r, k), hp("%sc%d" % (r, k))) for r, ks in [
    ("CL", (6, 18, 24, 36)), ("LCO", (12, 24)), ("NG", (12, 24)), ("GC", (6, 12)), ("HG", (6, 12)), ("C", (6, 9)), ("S", (6, 9)),
    ("W", (6,)), ("SB", (6,)), ("KC", (6,)), ("CT", (6,)), ("LC", (6,)), ("LH", (6,)), ("SRA", (4, 8, 12)), ("FF", (6, 12)),
    ("FEI", (4, 8)), ("TY", (2,)), ("FGBL", (2,)), ("ES", (2,)), ("VX", (2, 4))] for k in ks]
P += [("Indexes rates", lab, f) for lab, f in [
    ("S&P GSCI excess return (DS guess)", ds("GSCIEXR")), ("S&P GSCI spot (DS guess)", ds("GSCISPT")),
    ("GSCI crude total return (DS guess)", ds("GSCLTOT")), ("GSCI crude excess return (DS guess)", ds("GSCLEXR")),
    ("GSCI gold total return (DS guess)", ds("GSGCTOT")), ("GSCI copper total return (DS guess)", ds("GSICTOT")),
    ("GSCI natural gas total return (DS guess)", ds("GSNGTOT")), ("GSCI corn total return (DS guess)", ds("GSCNTOT")),
    ("GSCI wheat total return (DS guess)", ds("GSWHTOT")), ("GSCI soybeans total return (DS guess)", ds("GSSOTOT")),
    ("GSCI sugar total return (DS guess)", ds("GSSBTOT")), ("GSCI live cattle total return (DS guess)", ds("GSLCTOT")),
    ("S&P GSCI index (Workspace code)", hp(".SPGSCI")), ("S&P GSCI total return (Workspace code)", hp(".SPGSCITR")),
    ("GSCI crude excess return (Workspace code guess)", hp(".SPGSCLP")), ("GSCI crude total return (Workspace code guess)", hp(".SPGSCLTR")),
    ("Bloomberg commodity index (Workspace code)", hp(".BCOM")), ("Bloomberg commodity total return (Workspace code)", hp(".BCOMTR")),
    ("Bloomberg commodity index (DS guess)", ds("DJUBSTR")), ("Bloomberg commodity index (DS guess 2)", ds("BCOMTR")),
    ("MSCI World P/E (MSPE)", ds("MSWRLD$", "MSPE")), ("MSCI World dividend yield (MSDY)", ds("MSWRLD$", "MSDY")),
    ("MSCI World P/E (PE)", ds("MSWRLD$", "PE")), ("MSCI World price/book (MSPB)", ds("MSWRLD$", "MSPB")),
    ("MSCI USA local (DS guess)", ds("MSUSAML", "MSRI")), ("MSCI EAFE (DS guess)", ds("MSEAFE$", "RI")),
    ("MSCI Emerging Markets (DS guess)", ds("MSEMKF$", "RI")), ("MSCI Europe (DS guess)", ds("MSEROP$", "RI")),
    ("MSCI Japan (DS guess)", ds("MSJPAN$", "RI")), ("MSCI AC World (DS guess)", ds("MSACWF$", "RI")),
    ("US 3m eurocurrency rate (DS guess)", ds("ECUSD3M")), ("Euro 3m (DS guess)", ds("ECEUR3M")), ("Japan 3m (DS guess)", ds("ECJAP3M")),
    ("UK 3m (DS guess)", ds("ECUKP3M")), ("Swiss 3m (DS guess)", ds("ECSWF3M")), ("Canada 3m (DS guess)", ds("ECCAD3M")),
    ("Australia 3m (DS guess)", ds("ECAUD3M")), ("US Treasury bill 3m (DS guess)", ds("USTBL3M")), ("US Fed funds (DS guess)", ds("USFDFUND")),
    ("USD swap 10y (DS guess)", ds("ICUSD10")), ("EUR swap 10y (DS guess)", ds("ICEUR10")), ("JPY swap 10y (DS guess)", ds("ICJPY10")),
    ("GBP swap 10y (DS guess)", ds("ICGBP10")), ("USD Libor swap 10y (Workspace guess)", hp("USDIRS10Y=")),
    ("EUR swap 10y (Workspace guess)", hp("EURIRS10Y=")), ("EUR/USD basis swap 1y (Workspace guess)", hp("EURCBS1Y=")),
    ("JPY/USD basis swap 1y (Workspace guess)", hp("JPYCBS1Y=")), ("US 10y breakeven (Workspace guess)", hp("US10YBEI=RR")),
    ("US 10y TIPS yield (Workspace guess)", hp("US10YTIP=RR")), ("US 3m bill (Workspace)", hp("US3MT=RR")),
    ("VIX (Datastream)", ds("CBOEVIX")), ("S&P 500 P/E (DSPE)", ds("S&PCOMP", "DSPE")), ("S&P 500 dividend yield (DSDY)", ds("S&PCOMP", "DSDY"))]]
EF = "ECON_ACT;RTR_POLL;ECON_PRIOR;FCAST_MED;FCAST_HIGH;FCAST_LOW;ACT_REL_ST;VALUE;ACTUAL;MEDIAN;OFF_CLOSE;GEN_VAL1"
P += [("Economics", lab, f) for lab, f in [
    ("US payrolls: which fields exist (the error lists the missing ones)", hp("USNFAR=ECI", fields=EF)),
    ("US payrolls: actual", hp("USNFAR=ECI", fields="ECON_ACT")), ("US payrolls: poll", hp("USNFAR=ECI", fields="RTR_POLL")),
    ("US payrolls: VALUE", hp("USNFAR=ECI", fields="VALUE")), ("US payrolls: RHistory default fields", rh("USNFAR=ECI", fam="")),
    ("US payrolls: RHistory ECONOMIC", '=RHistory("USNFAR=ECI","ECONOMIC.Timestamp;ECONOMIC.Value","START:01-Jan-1990 INTERVAL:1MO",,"TSREPEAT:NO CH:Fd")'),
    ("US payrolls through Datastream", ds("<USNFAR=ECI>")),
    ("US payrolls: indicator fields", rd("USNFAR=ECI", "TR.IndicatorValue")),
    ("US CPI y/y: actual", hp("USCPNY=ECI", fields="ECON_ACT")), ("US ISM manufacturing: actual", hp("USPMI=ECI", fields="ECON_ACT")),
    ("US real GDP (DS guess)", ds("USGDP...D")), ("US industrial production (DS guess)", ds("USIPTOT.G")),
    ("US nonfarm payrolls (DS guess)", ds("USEMPALLO")), ("US retail sales (DS guess)", ds("USRETTOTB")),
    ("US core CPI (DS guess)", ds("USCPCOREE")), ("US consumer confidence (DS guess)", ds("USCNFCONQ")),
    ("Germany Ifo (DS guess)", ds("BDIFOIDXE")), ("Euro area CPI (DS guess)", ds("EMCONPRCF")), ("Japan CPI (DS guess)", ds("JPCONPRCF")),
    ("China industrial production (DS guess)", ds("CHIPTOT.H")), ("UK CPI (DS guess)", ds("UKCONPRCF")),
    ("OECD leading indicator US (DS guess)", ds("USOL2000Q")), ("Citi surprise index US (DS guess)", ds("USCESIR")),
    ("Citi surprise index US (Workspace guess)", hp(".CESIUSD")), ("Citi surprise index euro (Workspace guess)", hp(".CESIEUR"))]]
n2 = build("P2_probe_futures_indexes_econ", "LSEG probe 2: futures, commodity indexes, MSCI, short rates, economics", P)
print("L files: %d series | P2: %d test formulas" % (n, n2))
