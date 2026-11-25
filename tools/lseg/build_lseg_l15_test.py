"""L15_test_pull.xlsx: small test of which formula forms return expired-contract prices (after the L14 files stayed
on 'retrieving'). 17 formulas, each named by its form. usage: python3 build_lseg_l15_test.py [out dir]"""
import os
import sys

import build_lseg_l14 as B14
import build_lseg_contract_pull as B11

OUT = sys.argv[1] if len(sys.argv) > 1 else "out"
M = dict(start="01-Jan-2002", end="31-Dec-2005")
TESTS = [
    ("A HP one contract, monthly (worked in L12)", B11.hp("CLZ5^0", **M)),
    ("B DS one contract, monthly", B11.ds("<CLZ5^0>", start="2002-01-31", end="2005-12-31")),
    ("C DS two contracts in one formula", B11.ds("<CLZ5^0>,<CLF6^0>", start="2002-01-31", end="2005-12-31")),
    ("D DS twelve contracts in one formula (L14 form)",
     B11.ds(",".join("<CL%s5^0>" % c for c in "FGHJKMNQUVXZ"), start="2002-01-31", end="2005-12-31")),
    ("E RDP.Data three contracts, settlement, monthly",
     B11.rd("CLZ5^0,CLF6^0,CLG6^0", "TR.SETTLEMENTPRICE.date;TR.SETTLEMENTPRICE",
            "SDate=2002-01-01 EDate=2005-12-31 Frq=M CH=Fd RH=IN")),
    ("F RDP.Data three contracts, close, monthly",
     B11.rd("CLZ5^0,CLF6^0,CLG6^0", "TR.CLOSEPRICE.date;TR.CLOSEPRICE",
            "SDate=2002-01-01 EDate=2005-12-31 Frq=M CH=Fd RH=IN")),
    ("G HP two contracts in one formula", B11.hp("CLZ5^0,CLF6^0", **M)),
    ("H HP one contract 1985 (WTI)", B11.hp("CLZ5^8", start="01-Jan-1983", end="31-Dec-1985")),
    ("I HP one contract 1975 (corn)", B11.hp("CZ5^7", start="01-Jan-1972", end="31-Dec-1975")),
    ("J HP one contract 1980 (silver)", B11.hp("SIZ0^8", start="01-Jan-1977", end="31-Dec-1980")),
    ("K DS one contract 1975 (corn)", B11.ds("<CZ5^7>", start="1972-01-31", end="1975-12-31")),
    ("L DS one contract 1985 (WTI)", B11.ds("<CLZ5^8>", start="1983-01-31", end="1985-12-31")),
    ("M DS one Eurodollar contract, daily", B11.ds("<EDZ5^9>", start="1993-01-01", end="1995-12-31", frq="D")),
    ("N DS four Eurodollar contracts, daily",
     B11.ds("<EDH5^9>,<EDM5^9>,<EDU5^9>,<EDZ5^9>", start="1993-01-01", end="1995-12-31", frq="D")),
    ("O HP one Euribor contract, daily", B11.hp("FEIZ5^0", start="01-Jan-2003", end="31-Dec-2005", interval="P1D")),
    ("P HP one sugar contract 1985", B11.hp("SBH5^8", start="01-Jan-1982", end="31-Mar-1985")),
    ("Q HP one cattle contract 1995", B11.hp("LCZ5^9", start="01-Jan-1992", end="31-Dec-1995")),
]

if __name__ == "__main__":
    items = []
    for lab, f in TESTS:
        items.append(("Tests", "D" if "daily" in lab else "M", 0, ["x"], f, 1200 if "daily" in lab else 60, lab))
    wb = B14.write("L15_test_pull", items)
    os.makedirs(OUT, exist_ok=True)
    wb.save(os.path.join(OUT, "L15_test_pull.xlsx"))
    print("L15_test_pull.xlsx | %d formulas" % len(items))
