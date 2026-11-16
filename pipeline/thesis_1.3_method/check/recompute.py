"""Independent recomputation of every number in THESIS_1.3_method.md (checker, 2026-11-16)."""
from math import log, exp, sqrt
import itertools
P = print
# --- dice (slide C16 table, columns read by row: Green, Red, White) ---
G = [0.8, 0.9, 1.05, 1.1, 1.2, 1.4]
R = [0.06, 0.2, 1, 3, 3, 3]
W = [0.9, 1, 1, 1, 1, 1.1]
def stats(x):
    m = sum(x)/6 - 1; v = sum((a-1-m)**2 for a in x)/6; return m, v
for n, x in (('Green', G), ('Red', R), ('White', W)):
    m, v = stats(x); geo = exp(sum(log(a) for a in x)/6) - 1
    P(f'{n}: mean {m:.4f} sd {sqrt(v):.4f} var {v:.4f} approx growth {m - v/2:.4f} exact geometric {geo:.4f}')
P('Red approx with slide 1.32:', 0.71 - 1.32**2/2)
pink = [0.5*r + 0.5*w for r in R for w in W]
geo_p = exp(sum(log(a) for a in pink)/36) - 1
mp = sum(pink)/36 - 1; vp = sum((a-1-mp)**2 for a in pink)/36
P(f'Pink: mean {mp:.4f} var {vp:.4f} approx {mp - vp/2:.4f} slide approx {0.355 - 0.435/2:.4f} exact geometric {geo_p:.4f}')
P('0.06^2 =', 0.06**2, ' 1.71^20 =', 1.71**20, ' 0.075/0.04 =', 0.075/0.04)
# --- Bob Fund k=19 ---
k = 19; m = 0
while (1+1/k)**m < 20: m += 1
P(f'Bob fund k=19: gains needed {m}, P = (19/20)^{m} = {(k/(k+1))**m:.4f}; 1/19 = {1/19:.4f}')
for kk in (1, 2, 5, 49):
    mm = 0
    while (1+1/kk)**mm < 20: mm += 1
    P(f'   k={kk}: {mm} gains, P={(kk/(kk+1))**mm:.4f}')
# --- detectable Sharpe, whole stream at 10% vol (slide C20 formula, monthly) ---
v = 0.01/12
def sharpe_needed(n, count):
    g = log(20*count)/n            # log growth per month needed
    m = exp(g) - 1 + v/2           # mean monthly return: (1+m-v/2)^n = 20*count
    return m*12/0.10
for n, c in ((432, 1), (432, 4), (432, 32), (189, 1)):
    P(f'whole stream n={n} count={c}: Sharpe {sharpe_needed(n, c):.3f}')
# best scale: monthly growth S^2/24
for c in (1, 4, 32):
    P(f'best scale count={c}: S = {sqrt(24*log(20*c)/432):.3f}')
# challenger-minus-incumbent stream (variance of the difference ignored)
g = exp(log(20)/432) - 1
P(f'difference stream: {g*12*100:.2f} points a year, dSR {g*12/0.10:.3f}')
d = 0.118*0.10/12
P(f'+0.118 over 432 months: {(1+d)**432:.3f}')
# candidate book
lnW = 15*log(1.116) + 21*log(1.171)
P(f'candidate book value {exp(lnW):.1f}, p {1/exp(lnW):.4f}, x32 {32/exp(lnW):.3f}')
# 15% target: scale means by 1.5, variance by 2.25 (slide C20 formula, annual)
ln15 = 1.5*(lnW + 36*0.005) - 36*0.0225/2
P(f'15% target, drag re-computed: value {exp(ln15):.0f}, x32 p {32/exp(ln15):.4f}')
P(f'15% target, log wealth x1.5 only (drag ignored): value {exp(1.5*lnW):.0f}, x32 p {32/exp(1.5*lnW):.4f}')
# monthly version of the same (monthly vol 0.10/sqrt12)
vm10 = 0.01/12; vm15 = 0.0225/12
ln15m = 0
for yrs, Gr in ((15, 1.116), (21, 1.171)):
    gm = log(Gr)/12; mu = gm + vm10/2; ln15m += yrs*12*(1.5*mu - vm15/2)
P(f'15% target monthly calc: x32 p {32/exp(ln15m):.4f}')
# Bob over 350 months
P(f'1980-01..2009-02 months: {29*12+2}; 1.0016^350 = {1.0016**350:.3f}')
# live promotion: Sharpe 1, vol 10%
P(f'years to 20 at S=1, v=0.10: {log(20)/(0.10-0.005):.1f}')
# sizing
P('growth at v=0.10 zero when S =', 0.005/0.10)
for SB in (1.23, 0.5, 1.46):
    be = (sqrt(5)-2)*SB
    P(f'book {SB}: break-even {be:.3f}; zero-alpha pod -> {2*SB/sqrt(5):.3f} (loss {1-2/sqrt(5):.3f}); pod 0.4 -> gain {(2*SB+0.4)/sqrt(5)-SB:.4f}')
P('sqrt5-2 =', sqrt(5)-2)
# P3
P(f'(1-1/432)^432 = {(1-1/432)**432:.4f}; loss size at 0.4 Sharpe, 10% vol: {0.4*0.10/12*432:.3f} of capital = {0.4*0.10/12*432/(0.10/sqrt(12)):.1f} monthly sd')
# P4
P('0.3*0.375 =', 0.3*0.375, ' 7.5/20 =', 7.5/20)
P('market Sharpe from C09 (total return, not excess):', 0.0064*12/(0.0415*sqrt(12)))
# C24 long-run returns check
for n, mu, sd in (('Exxon', .0089, .0503), ('Berkshire', .0137, .0701), ('Bob', .0064, .0467), ('TEAM', .0014, .0217)):
    P(f'{n}: mean - var/2 = {mu - sd*sd/2:.4f}')
P('Bob alpha 0.0016 x 12 =', 0.0016*12)
P('months 1975-01..2010-12:', 36*12, ' 1978-01 is month', 3*12+1)
P('Holm 2 batches:', 2*0.025, 2*0.05, '1.46-0.23 =', 1.46-0.23)
