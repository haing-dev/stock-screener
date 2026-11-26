"""L16: contracts Datastream did not return in L14 (lseg_build_v4: 'E100 invalid code'), in the HistoricalPricing
form that worked for these roots in L12 (one contract per formula, monthly).
  L16a-L16e  Brent (LCO) all months, deliveries 1988-2012, 60 contracts per file
  L16f       probe: copper 1975-87, cotton and cattle 1975-79 (also invalid in Datastream): do they exist at all?
Small files (user rule 2026-11-26). usage: python3 build_lseg_l16.py [out dir]"""
import os
import string
import sys

import build_lseg_contract_pull as B11
import build_lseg_l14 as B14

OUT = sys.argv[1] if len(sys.argv) > 1 else "out"
PER_FILE = 60


def item(root, rr, name, y, m):
    code = B11.ric(rr, y, m, True)
    f = B11.hp(code, start="01-Jan-%d" % (y - 3), end="31-Dec-%d" % y)
    return (root, "M", 0, [code], f, 60, "%s %s (delivery %d-%02d), monthly" % (name, code, y, m))


def build(out=OUT):
    os.makedirs(out, exist_ok=True)
    brent = [item("LCO", "LCO", "Brent", y, m) for y in range(1988, 2013) for m in range(1, 13)]
    files = [brent[i:i + PER_FILE] for i in range(0, len(brent), PER_FILE)]
    probe = [item("HG", "HG", "Copper", y, m) for y in (1976, 1980, 1984, 1987) for m in (3, 12)]
    probe += [item("CT", "CT", "Cotton", y, m) for y in (1976, 1979) for m in (3, 12)]
    probe += [item("LC", "LC", "Live cattle", y, m) for y in (1976, 1979) for m in (4, 12)]
    files.append(probe)
    for i, fl in enumerate(files):
        tag = "L16" + string.ascii_lowercase[i]
        name = "%s_%s" % (tag, "Brent" if fl[0][0] == "LCO" else "probe")
        B14.write(name, fl).save(os.path.join(out, name + ".xlsx"))
        print("%s.xlsx | %d formulas" % (name, len(fl)))


if __name__ == "__main__":
    build()
