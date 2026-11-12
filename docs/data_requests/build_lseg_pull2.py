"""LSEG Workspace pull set 2 (2026-11-12), built after probe 2 (tools/bbgq/results/lseg_probe_v2.txt):
dated futures by RDP.HistoricalPricing with the display option "SORT:ASC TSREPEAT:NO CH:Fd RH:Timestamp" (proved on
CLc1 and TYc1); every futures root and curve depth below returned data in probe 2 unless marked; Datastream codes for
S&P GSCI single-commodity indexes follow the pattern that worked (GS<code>TOT / GS<code>EXR).
usage: python3 docs/data_requests/build_lseg_pull2.py [out dir]"""
import os, sys
sys.argv = sys.argv[:1] + ([sys.argv[1]] if len(sys.argv) > 1 else [])
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lseg_pull_helpers import build, hp, ds, rd, rh   # noqa: E402

DATED = "SORT:ASC TSREPEAT:NO CH:Fd RH:Timestamp"
def fut(ric):
    return hp(ric, disp=DATED)

# L4a energy curves, L4b other commodity curves
EN = [("CL", "WTI crude", list(range(1, 25)) + [36]), ("LCO", "Brent", list(range(1, 25))), ("HO", "Heating oil", range(1, 13)),
      ("RB", "Gasoline", range(1, 13)), ("LGO", "Gasoil", range(1, 13)), ("NG", "Natural gas", range(1, 25))]
P = [(nm, "%s contract %d" % (nm, k), fut("%sc%d" % (r, k))) for r, nm, ks in EN for k in ks]
n = build("L4a_curves_energy", "LSEG pull L4a: energy futures curves (monthly)", P)
OT = [("GC", "Gold", 12), ("SI", "Silver", 12), ("HG", "Copper", 12), ("PL", "Platinum", 6), ("PA", "Palladium", 6),
      ("C", "Corn", 9), ("S", "Soybeans", 9), ("W", "Wheat", 9), ("KW", "Kansas wheat", 9), ("BO", "Soybean oil", 9),
      ("SM", "Soybean meal", 9), ("SB", "Sugar", 6), ("KC", "Coffee", 6), ("CC", "Cocoa", 6), ("CT", "Cotton", 6),
      ("OJ", "Orange juice", 6), ("LC", "Live cattle", 6), ("LH", "Lean hogs", 6), ("FC", "Feeder cattle", 6)]
grp = {"GC": "Metals", "SI": "Metals", "HG": "Metals", "PL": "Metals", "PA": "Metals", "C": "Grains", "S": "Grains", "W": "Grains",
       "KW": "Grains", "BO": "Grains", "SM": "Grains", "SB": "Softs", "KC": "Softs", "CC": "Softs", "CT": "Softs", "OJ": "Softs",
       "LC": "Livestock", "LH": "Livestock", "FC": "Livestock"}
P = [(grp[r], "%s contract %d" % (nm, k), fut("%sc%d" % (r, k))) for r, nm, d in OT for k in range(1, d + 1)]
n += build("L4b_curves_metals_agri", "LSEG pull L4b: metals, grains, softs, livestock futures curves (monthly)", P)
# L5 financial futures
BOND = [("TU", "US 2y note"), ("FV", "US 5y note"), ("TY", "US 10y note"), ("US", "US long bond"), ("UB", "US ultra bond"),
        ("FGBS", "Schatz"), ("FGBM", "Bobl"), ("FGBL", "Bund"), ("FGBX", "Buxl"), ("FLG", "Long gilt"), ("FOAT", "OAT"),
        ("FBTP", "BTP"), ("JGB", "JGB 10y"), ("CGB", "Canada 10y"), ("YTC", "Australia 10y"), ("YTT", "Australia 3y")]
P = [("Bond futures", "%s contract %d" % (nm, k), fut("%sc%d" % (r, k))) for r, nm in BOND for k in (1, 2)]
STIR = [("SRA", "3m SOFR", 12), ("FF", "Fed funds", 12), ("FEI", "Euribor", 12), ("SON3", "3m SONIA", 8), ("YBA", "Australia bank bills", 8)]
P += [("Rate futures", "%s contract %d" % (nm, k), fut("%sc%d" % (r, k))) for r, nm, d in STIR for k in range(1, d + 1)]
EQ = [("ES", "S&P 500 e-mini"), ("NQ", "Nasdaq e-mini"), ("RTY", "Russell 2000 e-mini"), ("YM", "Dow e-mini"), ("STXE", "Euro Stoxx 50"),
      ("FDX", "DAX"), ("FFI", "FTSE 100"), ("JNI", "Nikkei"), ("HSI", "Hang Seng"), ("YAP", "ASX SPI"), ("SXF", "TSX 60")]
P += [("Equity futures", "%s contract %d" % (nm, k), fut("%sc%d" % (r, k))) for r, nm in EQ for k in (1, 2)]
P += [("Equity futures", "VIX future contract %d" % k, fut("VXc%d" % k)) for k in range(1, 9)]
n += build("L5_financial_futures", "LSEG pull L5: bond, short-rate, equity-index and VIX futures (monthly)", P)
# L6 commodity and equity indexes through Datastream (month-end start = last weekday of each month)
GS = [("CI", "S&P GSCI composite", "GSCITOT,GSCIEXR,GSCISPT"), ("EN", "Energy", None), ("IN", "Industrial metals", None),
      ("PM", "Precious metals", None), ("AG", "Agriculture", None), ("LV", "Livestock", None), ("CL", "Crude oil", None),
      ("BR", "Brent crude", None), ("HO", "Heating oil", None), ("HU", "Unleaded gasoline", None), ("GO", "Gasoil", None),
      ("NG", "Natural gas", None), ("GC", "Gold", None), ("SI", "Silver", None), ("IC", "Copper", None), ("IA", "Aluminium", None),
      ("IK", "Nickel", None), ("IZ", "Zinc", None), ("IL", "Lead", None), ("PL", "Platinum", None), ("CN", "Corn", None),
      ("WH", "Wheat", None), ("KW", "Kansas wheat", None), ("SO", "Soybeans", None), ("SB", "Sugar", None), ("KC", "Coffee", None),
      ("CC", "Cocoa", None), ("CT", "Cotton", None), ("LC", "Live cattle", None), ("LH", "Lean hogs", None), ("FC", "Feeder cattle", None)]
P = [("GSCI", "GSCI %s: total return, excess return%s" % (nm, ", spot" if codes else ""), ds(codes or "GS%sTOT,GS%sEXR" % (c, c)))
     for c, nm, codes in GS]
P += [("Other indexes", lab, f) for lab, f in [
    ("Bloomberg commodity total return (Datastream)", ds("DJUBSTR")), ("Bloomberg commodity index (Workspace)", fut(".BCOM")),
    ("Bloomberg commodity total return (Workspace)", fut(".BCOMTR")),
    ("MSCI World, USA, EAFE: total return", ds("MSWRLD$,MSUSAML,MSEAFE$", "RI")),
    ("MSCI EM, Europe, Japan, AC World: total return", ds("MSEMKF$,MSEROP$,MSJPAN$,MSACWF$", "RI")),
    ("S&P 500: price, total return, P/E, dividend yield", ds("S&PCOMP", "PI,RI,DSPE,DSDY")),
    ("Citi surprise US (Datastream)", ds("USCESIR")), ("Citi surprise US (Workspace)", fut(".CESIUSD")),
    ("Citi surprise euro area", fut(".CESIEUR")), ("Citi surprise UK", fut(".CESIGBP")), ("Citi surprise Japan", fut(".CESIJPY")),
    ("Citi surprise China", fut(".CESICNY")), ("Citi surprise Canada", fut(".CESICAD")), ("Citi surprise Australia", fut(".CESIAUD")),
    ("Citi surprise Switzerland", fut(".CESICHF")), ("Citi surprise G10", fut(".CESIG10")), ("Citi surprise emerging markets", fut(".CESIEM")),
    ("MOVE index", fut(".MOVE")), ("Dollar index", fut(".DXY"))]]
n += build("L6_indexes_datastream", "LSEG pull L6: commodity indexes, MSCI, surprise indexes (monthly)", P)
# L7 short rates, swaps, inflation-linked, economics
P = [("Short rates", "%s 3m deposit rate" % nm, ds(c)) for c, nm in [
    ("ECUSD3M", "US dollar"), ("ECEUR3M", "Euro"), ("ECWGM3M", "German mark (guess)"), ("ECJAP3M", "Japanese yen"),
    ("ECUKP3M", "UK sterling"), ("ECSWF3M", "Swiss franc"), ("ECCAD3M", "Canadian dollar"), ("ECAUD3M", "Australian dollar"),
    ("ECNZD3M", "New Zealand dollar (guess)"), ("ECSWE3M", "Swedish krona (guess)"), ("ECNOR3M", "Norwegian krone (guess)"),
    ("ECDKN3M", "Danish krone (guess)")]]
P += [("Short rates", "US Fed funds rate", ds("USFDFUND")), ("Short rates", "US Treasury bill 3m (Workspace)", fut("US3MT=RR"))]
P += [("Swaps", "USD swap %s" % t, fut("USDIRS%s=" % t)) for t in ("2Y", "5Y", "10Y", "30Y")]
P += [("Swaps", "%s/USD basis swap %s" % (c, t), fut("%sCBS%s=" % (c, t))) for c in ("EUR", "JPY", "GBP", "CHF", "AUD", "CAD") for t in ("1Y", "5Y")]
P += [("Swaps", "US %sy TIPS yield" % t, fut("US%sYTIP=RR" % t)) for t in ("5", "10", "30")]
ECO = [("CONPRCF", "consumer prices"), ("UN%TOTQ", "unemployment rate"), ("IPTOT.G", "industrial production"),
       ("GDP...D", "real GDP"), ("OL2000Q", "OECD leading indicator")]
CC = [("US", "US"), ("EM", "Euro area"), ("BD", "Germany"), ("FR", "France"), ("IT", "Italy"), ("ES", "Spain"), ("UK", "UK"),
      ("JP", "Japan"), ("CN", "Canada"), ("AU", "Australia"), ("SW", "Switzerland"), ("SD", "Sweden"), ("NW", "Norway"),
      ("CH", "China"), ("IN", "India"), ("KO", "Korea"), ("BR", "Brazil"), ("MX", "Mexico")]
P += [("Economics", "%s %s (pattern guess)" % (nm, lab), ds(cc + code)) for code, lab in ECO for cc, nm in CC]
P += [("Economics", lab, ds(c)) for c, lab in [
    ("USCONPRCE", "US CPI seasonally adjusted"), ("USCPCOREE", "US core CPI"), ("USEMPALLO", "US nonfarm payrolls"),
    ("USRETTOTB", "US retail sales"), ("USCNFBUSQ", "US ISM manufacturing"), ("USCNFCONQ", "US consumer confidence"),
    ("BDIFOIDXE", "Germany Ifo"), ("CHIPTOT.H", "China industrial production"), ("<USNFAR=ECI>", "US payrolls change (release code)")]]
n += build("L7_rates_swaps_economics", "LSEG pull L7: short rates, swaps, inflation-linked, economics (monthly)", P)
print("set 2: %d formulas" % n)
