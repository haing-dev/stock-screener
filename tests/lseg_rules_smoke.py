"""Smoke test of tools/lseg/lseg_rules.py (exchange-rule dates and registered listing models). No market data."""
import datetime as dt
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools", "lseg"))
import lseg_rules as R  # noqa: E402

D = dt.date
ok = True


def check(name, got, want):
    global ok
    flag = got == want
    ok &= flag
    print("%s %s: got %s want %s" % ("PASS" if flag else "FAIL", name, got, want))


check("CL Dec-2005 last trade", R.dates("CL", 2005, 12)[0], D(2005, 11, 21))
check("ED Mar-2008 last trade", R.dates("ED", 2008, 3)[0], D(2008, 3, 17))
check("GC Dec-2005 last trade", R.dates("GC", 2005, 12)[0], D(2005, 12, 28))
check("C Dec-2005 last trade", R.dates("C", 2005, 12)[0], D(2005, 12, 14))
check("NG c1 2005-11-30", R.held_contract("NG", 1, D(2005, 11, 30)), (2006, 1))
check("GC c1..c5 2005-11-30", [R.held_contract("GC", n, D(2005, 11, 30)) for n in range(1, 6)],
      [(2005, 12), (2006, 1), (2006, 2), (2006, 4), (2006, 6)])
check("KC c1 2005-12-30", R.held_contract("KC", 1, D(2005, 12, 30)), (2006, 3))
check("observed expiry overrides the rule", R.held_contract("NG", 1, D(2005, 11, 25), {(2005, 12): D(2005, 11, 24)}),
      (2006, 1))
check("root without a model", R.held_contract("CL", 1, D(2005, 12, 30)), None)
print("ALL LSEG RULES CHECKS PASSED" if ok else "LSEG RULES CHECKS FAILED")
sys.exit(0 if ok else 1)
