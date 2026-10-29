"""Final packages on corrected data (0.2% costs), built only from layers that survived: sector tilt (3.x research,
positive in both halves), commodity-trend sleeve (B004, the one FDR survivor), melt-up cut (2 episodes, prior
reasoning), presidential-cycle pair (A032/A033, placebo p ~0.05, published 1967 -> mostly out of sample),
squeeze (fragile; for reference)."""
import lab
lab.COST = 0.002
from base import *  # noqa
import exp_combo as X  # noqa
import validate5 as V5  # noqa

mo = np.array([p.month for p in grid]); yr = np.array([p.year for p in grid])
# A033: decided end of Mar..Aug of a midterm year (held Apr..Sep) -> 50%; A032: Q4 midterm .. Q2 pre-election -> no cuts
midterm = pd.Series((yr % 4 == 2) & (mo >= 3) & (mo <= 8), index=grid)
sweet = pd.Series(((yr % 4 == 2) & (mo >= 9)) | ((yr % 4 == 3) & (mo <= 5)), index=grid)
com12 = (lvl(R["commod"]) / lvl(R["commod"]).shift(12) - 1 > 0) & above_ma("commod")
SL = {"commod": 0.1 * com12.fillna(False)}


def pkg(tilt=True, sleeve=True, melt=False, pres=False, sq=False):
    e = e41.copy()
    if melt:
        e = np.minimum(e, pd.Series(np.where(V5.melt, 0.0, 1.0), index=grid))
    if sq:
        e = np.minimum(e, pd.Series(np.where((V5.sq_ext >= 80).fillna(False), 0.0, 1.0), index=grid))
    if pres:
        e = e.where(~sweet, 1.0)
        e = np.minimum(e, pd.Series(np.where(midterm, 0.5, 1.0), index=grid))
    return run(X.build(e, X.D_["D0"], SL if sleeve else {}, "L4" if tilt else "L0"))


W = (("1966-02", "1974-12"), ("1975-02", "2000-12"), ("2001-01", "2026-10"), ("1975-02", "2026-10"))
print("== corrected data, 0.2% costs. CAGR / worst / Sharpe: 1966-74 | 1975-2000 | 2001-2026 | 1975-2026")
print(line("S&P 500", R["spx"], W))
print(line("live 4.1", run(W41), W))
P = {"P1 live + sector tilt + commodity-trend sleeve": pkg(),
     "P2 P1 + melt-up cut": pkg(melt=True),
     "P3 P2 + presidential cycle": pkg(melt=True, pres=True),
     "P4 P3 + squeeze cut": pkg(melt=True, pres=True, sq=True),
     "P1 + presidential only": pkg(pres=True)}
for k, r in P.items():
    print(line(k, r, W))
print("\n== by decade CAGR: live / P1 / P2 / P3 / S&P")
for a, b in (("1966-01", "1974-12"), ("1975-01", "1984-12"), ("1985-01", "1994-12"), ("1995-01", "2004-12"),
             ("2005-01", "2014-12"), ("2015-01", "2026-10")):
    print(f"  {a[:4]}-{b[:4]}: " + " / ".join(f"{stats(r, a, b)['cagr']:5.1f}" for r in (run(W41), P['P1 live + sector tilt + commodity-trend sleeve'], P['P2 P1 + melt-up cut'], P['P3 P2 + presidential cycle'], R['spx'])))
t = grid[-1]
print(f"\ntoday {t}: commodity trend sleeve {'ON' if com12.iloc[-1] else 'off'}; midterm window {'ON' if midterm.iloc[-1] else 'off'}; "
      f"sweet spot {'ON' if sweet.iloc[-1] else 'off'}; melt-up {'ON' if V5.melt.iloc[-1] else 'off'}; live exposure {e41.iloc[-1]:.0%}")
