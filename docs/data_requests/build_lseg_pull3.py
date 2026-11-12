"""LSEG Workspace pull set 3 (2026-11-12): L8 = fixes for failed codes + LSEG alternatives for what the plan still
took from Bloomberg (ended rate futures through Datastream, swaps, inflation-linked yields, LME metals, other
commodities, extra bond futures, FX option quotes, Fed series). Many codes are guesses: a failed block just stays on
the Bloomberg list. L9a / L9b = DAILY history from 1990 for the main markets (for volatility and the weekly cycle).
usage: python3 docs/data_requests/build_lseg_pull3.py [out dir]"""
import os, sys
sys.argv = sys.argv[:1] + ([sys.argv[1]] if len(sys.argv) > 1 else [])
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lseg_pull_helpers import build, hp, ds, rd   # noqa: E402

DATED = "SORT:ASC TSREPEAT:NO CH:Fd RH:Timestamp"
def fut(ric, fields="CLOSE"):
    return hp(ric, fields=fields, disp=DATED)
def rhd(ric, start="01-Jan-1975", interval="1MO"):       # RHistory with the instrument's default fields (proved on futures and yields)
    return '=RHistory("%s",".Timestamp;.Close","START:%s INTERVAL:%s",,"TSREPEAT:NO CH:Fd")' % (ric, start, interval)

P = []
# 1 fixes
P += [("Fixes", lab, f) for lab, f in [
    ("Norway 3y benchmark: yield, return index", ds("BMNW03Y", "RY,RI")),
    ("GSCI platinum: total, excess return (code PT)", ds("GSPTTOT,GSPTEXR")), ("GSCI platinum (code PA)", ds("GSPATOT,GSPAEXR")),
    ("GSCI palladium (code PD)", ds("GSPDTOT,GSPDEXR")),
    ("Euro area consumer prices (EK)", ds("EKCONPRCF")), ("Euro area unemployment rate (EK)", ds("EKUN%TOTQ")),
    ("Euro area industrial production (EK)", ds("EKIPTOT.G")), ("Euro area real GDP (EK)", ds("EKGDP...D")),
    ("Euro area OECD leading indicator (EK)", ds("EKOL2000Q")), ("China real GDP y/y (guess)", ds("CHGDP..YR")),
    ("India industrial production (guess)", ds("INIPTOT.H")), ("Canada industrial production (guess)", ds("CNIPTOT.H")),
    ("US TIPS 5y: yield and price", fut("US5YTIP=RR", "B_YLD_1;CLOSE")), ("US TIPS 10y: yield and price", fut("US10YTIP=RR", "B_YLD_1;CLOSE")),
    ("US TIPS 30y: yield and price", fut("US30YTIP=RR", "B_YLD_1;CLOSE")), ("US 10y Treasury: yield and price", fut("US10YT=RR", "B_YLD_1;CLOSE"))]]
# 2 ended rate futures through Datastream (guessed continuous codes) and through Workspace codes
P += [("Ended rate futures", lab, f) for lab, f in [
    ("Eurodollar continuous (DS guess IED)", ds("IEDCS00")), ("Eurodollar continuous (DS guess CED)", ds("CEDCS00")),
    ("Eurodollar 2nd (DS guess)", ds("IEDCS20")), ("Eurodollar via Workspace code in Datastream", ds("<EDc1>")),
    ("Eurodollar 4th via Workspace code in Datastream", ds("<EDc4>")), ("Eurodollar 8th via Workspace code in Datastream", ds("<EDc8>")),
    ("Short sterling continuous (DS guess)", ds("LSSCS00")), ("Short sterling via Workspace code in Datastream", ds("<FSSc1>")),
    ("Canada BA continuous (DS guess)", ds("MBACS00")), ("Canada BA via Workspace code in Datastream", ds("<BAXc1>")),
    ("Euroswiss continuous (DS guess)", ds("LESCS00")), ("Euroswiss via Workspace code in Datastream", ds("<FESc1>")),
    ("Euroyen continuous (DS guess)", ds("TEYCS00")), ("Euroyen (Workspace guess)", fut("JEYc1")),
    ("Euribor continuous (DS guess, for comparison)", ds("LEICS00")), ("Fed funds continuous (DS guess)", ds("CFFCS00")),
    ("US Treasury 10y constant maturity (Fed, DS)", ds("FRTCM10")), ("US Treasury 2y constant maturity (Fed, DS)", ds("FRTCM02")),
    ("US Treasury bill 3m (Fed, DS)", ds("FRTBS3M")), ("US Fed funds effective (Fed, DS guess)", ds("FRFEDFD")),
    ("Moody's Aaa corporate yield (DS guess)", ds("FRCBAAA")), ("Moody's Baa corporate yield (DS guess)", ds("FRCBBAA")),
    ("Baltic Dry index (DS guess)", ds("BALTICF"))]]
# 3 swaps (Workspace quote codes; guesses by the usual naming)
SW = [("USDAM3L", "USD swap vs 3m Libor"), ("EURAB6E", "EUR swap vs 6m Euribor"), ("GBPSB6L", "GBP swap vs 6m Libor"),
      ("JPYSB6L", "JPY swap vs 6m Libor"), ("CHFAB6L", "CHF swap vs 6m Libor"), ("CADSB3B", "CAD swap"), ("AUDSB6B", "AUD swap (guess)"),
      ("AUDQM3AB", "AUD swap (guess 2)"), ("SEKAB3S", "SEK swap"), ("NOKAB6N", "NOK swap"), ("NZDSM3NB", "NZD swap (guess)")]
P += [("Swaps", "%s %s" % (nm, t), fut("%s%s=" % (c, t))) for c, nm in SW for t in ("2Y", "10Y")]
P += [("Swaps", "%s %s" % (nm, t), fut("%s%s=" % (c, t))) for c, nm in SW[:4] for t in ("5Y", "30Y")]
P += [("Swaps", lab, fut(r)) for r, lab in [
    ("USDOIS1Y=", "USD OIS 1y (guess)"), ("USDOIS2Y=", "USD OIS 2y (guess)"), ("USDOIS5Y=", "USD OIS 5y (guess)"),
    ("EUREON1Y=", "EUR OIS 1y (guess)"), ("EUREON2Y=", "EUR OIS 2y (guess)"), ("EUREST1Y=", "EUR estr OIS 1y (guess)"),
    ("USCPIZ5Y=", "US inflation swap 5y (guess)"), ("USCPIZ10Y=", "US inflation swap 10y (guess)"),
    ("EUHICPZ10Y=", "Euro inflation swap 10y (guess)"), ("GBRPIZ10Y=", "UK inflation swap 10y (guess)"),
    ("GB10YIL=RR", "UK 10y index-linked yield (guess)"), ("DE10YIL=RR", "Germany 10y inflation-linked yield (guess)"),
    ("FR10YIL=RR", "France 10y inflation-linked yield (guess)"), ("IT10YIL=RR", "Italy 10y inflation-linked yield (guess)"),
    ("JP10YIL=RR", "Japan 10y inflation-linked yield (guess)"), ("CA30YIL=RR", "Canada 30y real return yield (guess)"),
    ("AU10YIL=RR", "Australia 10y inflation-linked yield (guess)")]]
# 4 LME metals through Datastream, other commodities and extra futures through Workspace
P += [("Other commodities", "LME %s: cash, 3 months" % nm, ds("%sCASH,%s3MTH" % (c, c))) for c, nm in [
    ("LCP", "copper"), ("LAH", "aluminium"), ("LZZ", "zinc"), ("LNI", "nickel"), ("LED", "lead"), ("LTI", "tin")]]
ALT = [("O", "Oats"), ("RR", "Rough rice"), ("TFMBM", "Dutch TTF gas"), ("LRC", "Robusta coffee"), ("LSU", "White sugar"),
       ("RS", "Canola"), ("FCPO", "Palm oil"), ("BL2", "Milling wheat (Paris)"), ("SZZF", "Iron ore (Singapore)"),
       ("DA", "Class III milk (guess)"), ("UX", "Uranium (guess)"), ("CFI2Z", "EU carbon allowance, December"), ("JRU", "Rubber (Osaka)")]
P += [("Other commodities", "%s contract %d" % (nm, k), fut("%sc%d" % (r, k))) for r, nm in ALT for k in (1, 2, 3)]
P += [("Other futures", lab, fut(r)) for r, lab in [
    ("TNc1", "US ultra 10y note"), ("TNc2", "US ultra 10y note, 2nd"), ("FBTSc1", "Short BTP"), ("FBONc1", "Bono"),
    ("CGFc1", "Canada 5y"), ("CGZc1", "Canada 2y"), ("KTBc1", "Korea 3y bond (guess)"), ("LKTBc1", "Korea 10y bond (guess)"),
    ("FGBLc3", "Bund, 3rd"), ("EDcm1", "Eurodollar (guess)")]]
# 5 FX extras, indexes
def rh(ric, fam="BID", start="01-Jan-1975"):
    return '=RHistory("%s","%s.Timestamp;%s.Close","START:%s INTERVAL:1MO",,"TSREPEAT:NO CH:Fd")' % (ric, fam, fam, start)
P += [("FX extras", lab, rh(r)) for r, lab in [
    ("XAU=", "Gold spot"), ("XAG=", "Silver spot"), ("XPT=", "Platinum spot"), ("XPD=", "Palladium spot"), ("BTC=", "Bitcoin"),
    ("DEM=", "German mark (ended)"), ("FRF=", "French franc (ended)"), ("ITL=", "Italian lira (ended)"),
    ("EUR1MRR=", "EUR/USD 1m risk reversal (guess)"), ("EUR3MRR=", "EUR/USD 3m risk reversal (guess)"),
    ("EUR3MBF=", "EUR/USD 3m butterfly (guess)"), ("JPY3MRR=", "USD/JPY 3m risk reversal (guess)"),
    ("JPY3MBF=", "USD/JPY 3m butterfly (guess)"), ("EURRR3M=", "EUR/USD 3m risk reversal (guess 2)"),
    ("EUR25R3M=", "EUR/USD 3m 25-delta risk reversal (guess 3)"), ("EURJPY=", "EUR/JPY cross"), ("EURGBP=", "EUR/GBP cross"),
    ("EURCHF=", "EUR/CHF cross"), ("AUDJPY=", "AUD/JPY cross")]]
P += [("Indexes", nm + " close", rd(r, "TR.PriceClose")) for r, nm in [
    (".SPXEW", "S&P 500 equal weight"), (".BUX", "Budapest BUX"), (".KQ11", "Kosdaq"), (".STI", "Straits Times"), (".JKSE", "Jakarta"),
    (".SETI", "Thailand SET"), (".KLSE", "Malaysia KLCI"), (".JTOPI", "South Africa Top 40"), (".XU100", "Turkey BIST 100"),
    (".WIG20", "Poland WIG 20"), (".MERV", "Argentina Merval"), (".IPSA", "Chile IPSA"), (".NSEI", "India Nifty 50")]]
P += [("Indexes", lab, f) for lab, f in [
    ("MSCI World net total return (DS)", ds("MSWRLD$", "MSNR")), ("MSCI EM Europe (DS guess)", ds("MSEEUR$", "RI")),
    ("SG CTA index (Workspace guess)", fut(".NEIXCTA")), ("SG Trend index (Workspace guess)", fut(".NEIXCTAT")),
    ("BTOP50 (Workspace guess)", fut(".BTOP50")), ("S&P 500 12m forward EPS (IBES aggregate guess)", ds("@:USSP500", "A12FE")),
    ("US market 12m forward EPS (IBES aggregate guess 2)", ds("@:USM1", "A12FE")), ("US total market: forward P/E guess", ds("TOTMKUS", "PE,DY,PC"))]]
n = build("L8_fixes_and_alternatives", "LSEG pull L8: fixes and LSEG alternatives for the Bloomberg list (monthly)", P)

# L9 daily from 1990
def futd(ric, fields="CLOSE"):
    return hp(ric, fields=fields, start="01-Jan-1990", interval="P1D", disp=DATED)
COM = ["CL", "LCO", "HO", "RB", "LGO", "NG", "GC", "SI", "HG", "PL", "PA", "C", "S", "W", "KW", "BO", "SM", "SB", "KC", "CC", "CT", "LC", "LH"]
P = [("Commodities c%d" % k, "%s contract %d, daily" % (r, k), futd("%sc%d" % (r, k))) for k in (1, 2) for r in COM]
n9 = build("L9a_daily_commodities", "LSEG pull L9a: commodity futures, daily from 1990 (large: allow 10 minutes)", P)
FIN = ["TU", "FV", "TY", "US", "FGBS", "FGBM", "FGBL", "FLG", "JGB", "CGB", "YTC", "FEI", "FF"]
P = [("Rates c%d" % k, "%s contract %d, daily" % (r, k), futd("%sc%d" % (r, k))) for k in (1, 2) for r in FIN]
P += [("Equity futures", "%s contract 1, daily" % r, futd(r + "c1")) for r in ["ES", "NQ", "STXE", "FDX", "FFI", "JNI", "HSI", "YAP", "SXF"]]
P += [("FX spot", "%s spot vs USD, daily" % c, futd(c + "=", "BID")) for c in
      ["EUR", "JPY", "GBP", "CHF", "CAD", "AUD", "NZD", "SEK", "NOK", "MXN", "BRL", "ZAR", "TRY", "PLN", "KRW", "INR", "CNY", "SGD", "HUF", "ILS"]]
P += [("Yields 10y", "%s 10y government yield, daily" % cc, futd("%s10YT=RR" % cc, "B_YLD_1")) for cc in
      ["US", "DE", "GB", "FR", "IT", "ES", "JP", "AU", "CA", "CH", "SE", "NZ"]]
P += [("Yields 10y", "%s 2y government yield, daily" % cc, futd("%s2YT=RR" % cc, "B_YLD_1")) for cc in ["US", "DE", "GB", "JP", "AU", "CA"]]
n9 += build("L9b_daily_financial", "LSEG pull L9b: rates, equity futures, FX, yields, daily from 1990 (large: allow 10 minutes)", P)
print("L8: %d formulas | L9: %d daily series" % (n, n9))
