"""LSEG Workspace pull set 4 (2026-11-12): L10 = what the L8 read-back proved, pulled in full, so the Bloomberg visit can
drop it: full strips of the ended short-rate futures (Eurodollar, short sterling, Canada BA, Euroswiss through the
Workspace code in Datastream; Euroyen through Workspace), their daily history, the remaining swap tenors, plus a
last round of guesses for what still failed (a failed block just stays on the Bloomberg list).
usage: python3 docs/data_requests/build_lseg_pull4.py [out dir]"""
import os, sys
sys.argv = sys.argv[:1] + ([sys.argv[1]] if len(sys.argv) > 1 else [])
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lseg_pull_helpers import build, hp, ds   # noqa: E402

DATED = "SORT:ASC TSREPEAT:NO CH:Fd RH:Timestamp"
def fut(ric, fields="CLOSE"):
    return hp(ric, fields=fields, disp=DATED)
def futd(ric, fields="CLOSE"):
    return hp(ric, fields=fields, start="01-Jan-1990", interval="P1D", disp=DATED)

P = []
# 1 full strips, monthly (proved in L8 for c1, and for Eurodollar c4 and c8)
DSF = [("ED", "Eurodollar", 12), ("FSS", "Short sterling", 8), ("BAX", "Canada BA", 12), ("FES", "Euroswiss", 8)]
P += [("Rate futures strips", "%s contract %d" % (nm, k), ds("<%sc%d>" % (r, k))) for r, nm, n in DSF for k in range(1, n + 1)]
P += [("Rate futures strips", "Euroyen contract %d" % k, fut("JEYc%d" % k)) for k in range(1, 9)]
# 2 the same, daily from 1990 (front contracts)
P += [("Rate futures daily", "%s contract %d, daily" % (nm, k), ds("<%sc%d>" % (r, k), start="1989-12-29", frq="D"))
      for r, nm, ks in [("ED", "Eurodollar", (1, 2, 4, 8)), ("FSS", "Short sterling", (1, 2)), ("BAX", "Canada BA", (1, 2)),
                        ("FES", "Euroswiss", (1, 2))] for k in ks]
P += [("Rate futures daily", "Euroyen contract %d, daily" % k, futd("JEYc%d" % k)) for k in (1, 2)]
# 3 swaps: remaining tenors of the codes that worked, then guesses for the ones that failed
SW = [("USDAM3L", "USD swap vs 3m Libor", ("1Y", "3Y", "7Y")), ("EURAB6E", "EUR swap vs 6m Euribor", ("1Y", "3Y", "7Y")),
      ("GBPSB6L", "GBP swap vs 6m Libor", ("1Y", "3Y", "7Y")), ("JPYSB6L", "JPY swap vs 6m Libor", ("1Y", "3Y", "7Y")),
      ("CHFAB6L", "CHF swap vs 6m Libor", ("5Y", "30Y")), ("AUDQM3AB", "AUD swap", ("5Y", "30Y")), ("SEKAB3S", "SEK swap", ("5Y", "30Y")),
      ("NZDSM3NB", "NZD swap", ("5Y",))]
P += [("Swaps", "%s %s" % (nm, t), fut("%s%s=" % (c, t))) for c, nm, ts in SW for t in ts]
P += [("Swaps", lab, fut(r)) for r, lab in [
    ("EUREON5Y=", "EUR OIS 5y"), ("EUREON10Y=", "EUR OIS 10y"), ("EUREST2Y=", "EUR estr OIS 2y"), ("EUREST5Y=", "EUR estr OIS 5y"),
    ("EUREST10Y=", "EUR estr OIS 10y"), ("USCPIZ1Y=", "US inflation swap 1y"), ("USCPIZ2Y=", "US inflation swap 2y"),
    ("USCPIZ30Y=", "US inflation swap 30y"), ("GBRPIZ5Y=", "UK inflation swap 5y"), ("GBRPIZ30Y=", "UK inflation swap 30y"),
    ("GB5YIL=RR", "UK 5y index-linked yield"), ("GB30YIL=RR", "UK 30y index-linked yield")]]
G = [("CADIRS%s=", "CAD swap (guess 2)"), ("CADSB3C%s=", "CAD swap (guess 3)"), ("NOKIRS%s=", "NOK swap (guess 2)"),
     ("NOKAB6O%s=", "NOK swap (guess 3)"), ("USD%sOIS=", "USD OIS (guess 2)"), ("GBP%sOIS=", "GBP SONIA OIS (guess)"),
     ("GBPOIS%s=", "GBP SONIA OIS (guess 2)"), ("JPY%sOIS=", "JPY OIS (guess)"), ("EUHICPXTZ%s=", "Euro inflation swap (guess 2)"),
     ("EUCPIZ%s=", "Euro inflation swap (guess 3)"), ("JPCPIZ%s=", "Japan inflation swap (guess)")]
P += [("Swap guesses", "%s %s" % (nm, t), fut(c % t)) for c, nm in G for t in ("2Y", "10Y")]
# 4 commodities and bond futures still on the Bloomberg list: guesses
ALT = [("LCC", "London cocoa (guess)"), ("NCFM", "Newcastle coal (guess)"), ("ATW", "Rotterdam coal (guess)"), ("COM", "Rapeseed Paris (guess)"),
       ("NGLNM", "UK natural gas NBP (guess)"), ("LBR", "Lumber, new contract (guess)"), ("DCS", "Class III milk (guess 2)")]
P += [("Commodity guesses", "%s contract %d" % (nm, k), fut("%sc%d" % (r, k))) for r, nm in ALT for k in (1, 2, 3)]
P += [("Commodity guesses", lab, fut(r)) for r, lab in [
    ("10TBc1", "Korea 10y bond (guess 2)"), ("CONFc1", "Swiss bond (guess)"), ("FCONc1", "Swiss bond (guess 2)"), ("JGBMc1", "JGB mini (guess)"),
    ("TFMBMc12", "Dutch TTF gas contract 12"), ("TFMBMc13", "Dutch TTF gas contract 13"), ("Oc5", "Oats contract 5"), ("RRc6", "Rough rice contract 6")]]
P += [("Commodity guesses", lab, ds(c)) for c, lab in [
    ("GSPLTOT,GSPLEXR", "GSCI platinum (code PL)"), ("BALTICF", "Baltic Dry index (guess 2)")]]
n = build("L10_rate_strips_swaps_guesses", "LSEG pull L10: full strips of ended rate futures, more swap tenors, last guesses", P)
print("L10: %d formulas" % n)
