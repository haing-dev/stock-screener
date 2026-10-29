import os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "assets.py")).read().split("def run(wdef")[0]
exec(compile(src, "a", "exec"))
exec(compile("def run(wdef" + open(os.path.join(HERE, "assets.py")).read().split("def run(wdef")[1].split("log(\"\\n== non-stock")[0], "b", "exec"))
OUT.clear()
g, f_ = cneg & cause_g, cneg & ~cause_g
V = {"L1 live": L["L1 10y if corr<0 (live)"], "L6 growth->long, Fed->bills": L["L6 by cause"],
     "L6a growth->10y, Fed->bills": W(**{"10y": g, "bills": ~g}),
     "L6b growth->long, Fed->10y": W(long=g, **{"10y": f_, "bills": ~cneg}),
     "L6c growth->long (any corr), Fed->bills": W(long=cause_g, bills=~cause_g),
     "L6d growth->long, Fed->short": W(long=g, short=~g)}
for nm, w in V.items():
    print(line(nm, run(w)))
# decade split for L6 vs L1
for nm in ("L1 live", "L6 growth->long, Fed->bills"):
    r = run(V[nm]); print(nm, [round(st(r, a, b)[0], 1) for a, b in (("1975-02","1989-12"),("1990-01","2004-12"),("2005-01","2026-10"))])
