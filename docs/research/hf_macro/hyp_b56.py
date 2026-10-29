from harness import *  # noqa
"""Hypotheses from transcript rule batches 5 and 6 (/home/claude/macro_read/out/batch5.md, batch6.md).

Conventions (all conditions known at the end of month t):
  - FRED monthly macro (CPI, payrolls, IP, retail sales, M2, EPU ...): .shift(1); OECD/BIS monthly: .shift(1)-(2);
    quarterly series dated at quarter start: ffill(limit=2).shift(4) (BIS house prices .shift(6)); annual fiscal-year
    deficit (dated January): .shift(10). P['F'], P['ind'], P['sc'] are already point in time. Daily/weekly FRED and
    Yahoo px_* are month-end values (no lag). Shiller earnings are interpolated from quarters -> .shift(6).
  - "cut/exit/sell" -> level 0.0; "reduce/underweight/lower" -> level 0.5.
  - "underweight long Treasuries" (a return bet) -> overlay short 20% t30y vs T-bills (uw_t);
    "Treasuries are not the hedge" (a hedge choice) -> overlay that removes the base book's TLT holding (no_long_t).
  - Pair trades (overlay) are only switched on in months where every leg has data next month.
  - Where the rule states a horizon ("for 12 months") the signal is held that long (hold()); else it is applied while true.
  - Baskets added to R (prefix x56_): equal-weight mixes for multi-asset actions; dynamic baskets select at t, earn t+1.
"""
import numpy as np  # noqa
import pandas as pd  # noqa
import warnings

warnings.filterwarnings("ignore")

# ----------------------------------------------------------------------------------------------- helpers
TRUE = pd.Series(True, index=grid)


def B(x):
    return x.reindex(grid).fillna(False).astype(bool)


def hold(c, n):
    """True if c was true in any of the last n months (incl. t): a signal held for n months."""
    return B(B(c).astype(float).rolling(n, min_periods=1).max() > 0)


def consec(c, n):
    return B(B(c).astype(float).rolling(n, min_periods=n).sum() >= n)


def latch(enter, exit_):
    """On from the month `enter` is true until `exit_` is true (hysteresis)."""
    en, ex = B(enter).values, B(exit_).values
    out, on = [], False
    for a, b in zip(en, ex):
        if on and b:
            on = False
        elif not on and a:
            on = True
        out.append(on)
    return pd.Series(out, index=grid)


def m(sid, lag=1):
    return S[sid].shift(lag)


def q(sid, lag=4):
    return S[sid].ffill(limit=2).shift(lag)


def ann(sid, lag=10):
    return S[sid].ffill(limit=11).shift(lag)


def ch(x, n):
    return x - x.shift(n)


def pc(x, n):
    return (x / x.shift(n) - 1) * 100


def lv(c):
    return lvl(R[c]).where(R[c].notna().cummax())


def ddh(c, n=12):
    l_ = lv(c)
    return l_ / l_.rolling(n, min_periods=1).max() - 1


def rel(a, b, n):
    return mom(a, n) - mom(b, n)


def rpct(x, n=120, min_n=60):
    """Percentile (0-100) of x within its own last n months (known at t)."""
    return x.rolling(n, min_periods=min_n).apply(lambda a: (a[~np.isnan(a)] <= a[-1]).mean() * 100, raw=True)


def zroll(x, n=240, min_n=120):
    return (x - x.rolling(n, min_periods=min_n).mean()) / x.rolling(n, min_periods=min_n).std()


def corr12(a, b):
    return a.rolling(12, min_periods=12).corr(b)


def basket(name, sel):
    """Dynamic equal-weight basket: columns selected at t (bool DataFrame) are held in t+1. Returns 'any selected'."""
    sel = sel.reindex(grid).fillna(False).astype(bool)
    Rt = R[list(sel.columns)]
    w = sel.shift(1).fillna(False).astype(bool) & Rt.notna()
    R[name] = Rt.where(w).mean(axis=1)
    return sel.any(axis=1)


# base book's long-Treasury weight in the c5 book (held only in a growth-trend cut with corr < 0 and 10y >= FF)
_xs = X5["gold"] + X5["commod"]
T30 = (gtt & cneg & curve_ok).astype(float) * (1 - _xs)


def no_long_t(cf, frac=1.0):
    return lambda: pd.DataFrame({"t30y": -frac * T30 * B(cf()).astype(float)}, index=grid)


def uw_t(cf, w=0.2, asset="t30y"):
    return lambda: pd.DataFrame({asset: -w * B(cf()).astype(float)}, index=grid)


def pair(cf, longs, shorts, w=0.2):
    def f():
        c = (B(cf()) & have(list(longs) + list(shorts))).astype(float)
        d = {}
        for a in longs:
            d[a] = d.get(a, 0.0) + w / len(longs) * c
        for a in shorts:
            d[a] = d.get(a, 0.0) - w / len(shorts) * c
        return pd.DataFrame(d, index=grid)
    return f


# ----------------------------------------------------------------------------------------------- shared series
spxl = lv("spx")
dd_spx = spxl / spxl.cummax() - 1
trend_up = B(ind["spx_trend"] > 0)
unr = F["UNRATE"]
unr_ok = B(unr <= unr.rolling(12).mean())
cpi_sa = m("fred_CPIAUCSL")
core_yy = ind["core_cpi"].combine_first(cpi_yy)                          # core CPI y/y (headline CPI before 1998)
core3 = (((F["CPILFESL"] / F["CPILFESL"].shift(3)) ** 4 - 1) * 100).combine_first(((cpi_sa / cpi_sa.shift(3)) ** 4 - 1) * 100)
corepce_yy = pc(F["PCEPILFE"], 12).combine_first(pc(m("fred_PCEPI"), 12))  # core PCE y/y (headline PCE before 2001)
corepce3 = ((F["PCEPILFE"] / F["PCEPILFE"].shift(3)) ** 4 - 1) * 100
gs2 = F["GS2"]
real10 = ind["realyield"].combine_first(gs10 - cpi_yy)
rpol = ff - cpi_yy                                                        # real policy rate
dollar12 = ind["dollar"]
dxy = S["px_DX-Y.NYB"]
_tw = F["TWEXMMTH"]
dxy_below = B(B(dxy < dxy.rolling(12).mean()).where(dxy.notna(), B(_tw < _tw.rolling(12).mean())))
oil_l = F["WTISPLC"]
oil6 = ind["oil"]
vixm = S["px_^VIX"].combine_first(ind["vix"])
tnx = S["px_^TNX"]
cape = ind["cape"]
cape_p = pctl(cape)
curve = ind["curve"]
stockbond = ind["stockbond"]
share_ = P["share"]
stage = P["stage"]
hotP = B(P["hot"])
overheat = B(stage.isin(["expansion", "late"])) & hotP
stagfl = B(stage == "contraction") & hotP
rgdp = q("fred_GDPC1")
ngdp = rgdp * q("fred_GDPDEF") / 100
rgdp_yy = pc(rgdp, 12)
ngdp_yy = pc(ngdp, 12)
_def_m = -S["fred_MTSDS133FMS"].shift(1).rolling(12, min_periods=12).sum() / 1000 / ngdp * 100
deficit = _def_m.combine_first(-ann("fred_FYFSGDA188S", 10))             # federal deficit, % of GDP (+ = deficit)
debt_gdp = q("fred_GFDEGDQ188S")
int_rec = q("fred_A091RC1Q027SBEA", 5) / q("fred_FGRECPT", 5) * 100
tariff = q("fred_B235RC1Q027SBEA", 5) / q("fred_IMPGS", 5) * 100                # customs duties / imports of goods+services
tariff12 = ch(tariff, 12)
realdef_yy = pc(q("fred_FDEFX", 5) / q("fred_GDPDEF", 5), 12)
fedbs12 = pc(S["fred_WALCL"], 12).combine_first(pc(m("fred_BOGMBASE"), 12))
fedbs3 = pc(S["fred_WALCL"], 3).combine_first(pc(m("fred_BOGMBASE"), 3))
gcb6 = pd.concat([pc(S["fred_WALCL"], 6), pc(S["fred_ECBASSETSW"], 6), pc(m("fred_JPNASSETS"), 6)], axis=1).mean(axis=1, skipna=False)
_gd = q("fred_GFDEBTN")
fed_share = q("fred_FDHBFRBN", 6) * 1000 / _gd * 100
hold_share = (q("fred_FDHBFIN", 6) + q("fred_FDHBFRBN", 6)) * 1000 / _gd * 100
epu = m("fred_USEPUINDXM")
epu_p10 = rpct(epu, 120, 60)
epu_p = pctl(epu)
tp = F["THREEFYTP10"]
ecb = S["fred_ECBDFR"]
_mv = (ff.diff().abs() / 0.25).round().fillna(0) + (ecb.diff().abs() / 0.25).round().fillna(0)
moves12 = _mv.rolling(12, min_periods=12).sum().where(ff.notna())       # 25bp policy moves, Fed + ECB (BoE missing)
bp12 = moves12 * 25
drill = m("fred_IPN213111N")                                              # IP: drilling oil & gas wells (rig proxy)
philly = S["fred_GACDFSA066MSFRBPHI"]                                     # released within the month
gas = S["fred_GASREGW"]
sloos = q("fred_DRTSCILM")
cards_q = q("fred_DRCCLACBS", 5)
truck_yy = pc(F["TRUCKD11"], 12)
real_retail = m("fred_RSAFS") / cpi_sa
mort = F["MORTGAGE30US"]
move = S["px_^MOVE"]
jgb10 = m("fred_IRLTLT01JPM156N")
bund10 = m("fred_IRLTLT01DEM156N")
jcpi_yy = pc(m("fred_JPNCPIALLMINMEI", 2), 12)
boj = m("fred_IRSTCB01JPM156N")
krate = m("fred_IRSTCI01KRM156N")
khouse_yy = pc(q("fred_QKRR628BIS", 6), 12)
svc = m("fred_CUSR0000SASLE")
svc3 = ((svc / svc.shift(3)) ** 4 - 1) * 100
svc12 = pc(svc, 12)
nickel6 = pc(m("fred_PNICKUSDM"), 6)
tga = S["fred_WTREGEN"]
m2 = m("fred_M2SL")
m2_yy = pc(m2, 12)
reer_us = m("fred_RBUSBIS")
tbill3 = S["fred_DTB3"]
cli = m("fred_USALOLITONOSTSAM", 2)
baa_sp = F["BAA"] - gs10
# Shiller trailing earnings yield (earnings lagged 6 months: quarterly interpolation + reporting lag)
_px = S["sh_price"].combine_first(S["px_^GSPC"])
ey = S["sh_eps"].shift(6).ffill(limit=6) / _px * 100
pe = 100 / ey
y10_ngdp = ind["y10_ngdp"].combine_first(gs10 - ngdp_yy)
hh_p = pctl(ind["hh_equity"], min_n=36)

# growth-pillar warnings in the worst fifth
GROWTH = ["jobs_alarm", "truck", "permits", "autos", "curve", "youth", "cards"]
growth_n = (sc[GROWTH] >= 80).sum(axis=1)

# trend agreement on 3 horizons (10m and 3m averages of month-end levels, 1-month change)
up_n = (B(spxl > ma(spxl, 10)).astype(int) + B(spxl > ma(spxl, 3)).astype(int) + B(R["spx"] > 0).astype(int))

# ex-US equity, EM proxy
COUNTRIES = ["eq_korea", "eq_brazil", "eq_japan", "eq_china", "eq_india", "eq_taiwan", "eq_mexico", "eq_germany",
             "eq_uk", "eq_canada", "eq_australia", "eq_hongkong", "eq_s_africa", "eq_chile", "eq_turkey", "eq_indonesia"]
_ab = pd.DataFrame({c: above_ma(c).where(R[c].notna().cummax()) for c in COUNTRIES})
_nav = _ab.notna().sum(axis=1)
cty_breadth = (_ab.astype(float).sum(axis=1) / _nav * 100).where(_nav >= 8)

# ----------------------------------------------------------------------------------------------- baskets
R["x56_real"] = R[["gold", "commod", "tips"]].mean(axis=1)               # real assets: gold, commodities, TIPS
R["x56_metals"] = R[["gold", "silver", "copper"]].mean(axis=1)
R["x56_oilcu"] = R[["oil", "copper"]].mean(axis=1)
R["x56_goldmin"] = R[["gold", "sec_GDX"]].mean(axis=1)
R["x56_emproxy"] = R[["eq_brazil", "eq_mexico", "eq_korea", "eq_india"]].mean(axis=1)
em_dd = ddh("x56_emproxy", 12)

# devaluation basket: currency down >15% in 6m (BIS real broad index, or bilateral vs USD), held 12 months
_fx = {"eq_brazil": m("fred_RBBRBIS"), "eq_china": m("fred_RBCNBIS"), "eq_japan": m("fred_RBJPBIS"),
       "eq_korea": m("fred_RBKRBIS"), "eq_mexico": 1 / S["fred_DEXMXUS"], "eq_india": 1 / S["fred_DEXINUS"]}
_dev = pd.DataFrame({k: hold(pc(v, 6) < -15, 12) for k, v in _fx.items()})
deval_any = basket("x56_deval", _dev)
# cheap EM currencies (BIS real broad index > 1 sd below its 20-year mean)
_cheap = pd.DataFrame({k: B(zroll(_fx[k]) < -1) for k in ("eq_brazil", "eq_china", "eq_korea")})
cheapfx_any = basket("x56_cheapfx", _cheap)
# sector baskets (tool's 20 industries)
SECS = ["sec_" + c for c in P["rets"].columns]
_r6 = pd.DataFrame({c: rel(c, "spx", 6) for c in SECS})
strong_any = basket("x56_strong", _r6 > 0.10)
_sec_up = pd.DataFrame({c: above_ma(c) for c in SECS})
_r12 = pd.DataFrame({c: mom(c, 12) for c in SECS})
_secular = pd.DataFrame({c: hold(_r12[c] > 1.0, 24) & B(_sec_up[c]) for c in SECS})
secular_any = basket("x56_secular", _secular)
_turn = pd.DataFrame({c: hold(B(rel(c, "spx", 36) < -0.30) & B(_r6[c] > 0) & B(_sec_up[c]), 12) for c in SECS})
turn_any = basket("x56_turn", _turn)

# live book's own returns (for sizing-by-own-P&L rules)
_lb = (1 + REF["live"].fillna(0)).cumprod()
live_dd6 = _lb / _lb.rolling(6, min_periods=1).max() - 1
live_dd = _lb / _lb.cummax() - 1

# post-bubble bear: months since the S&P peak, rally from the 6-month low
_since = []
_pk, _k = -np.inf, 0
for v in spxl.values:
    if v >= _pk:
        _pk, _k = v, 0
    else:
        _k += 1
    _since.append(_k)
since_peak = pd.Series(_since, index=grid)

# M2 gap vs its 2010-2019 log trend (trend fitted on data known by 2020-01; used only from 2020)
_w = m2[(grid >= Per("2010-01")) & (grid <= Per("2019-12"))].dropna()
_x = np.arange(len(_w))
_b = np.polyfit(_x, np.log(_w.values), 1)
_t = pd.Series(np.arange(T) - int(np.where(grid == _w.index[0])[0][0]), index=grid)
m2gap = ((np.log(m2) - (_b[1] + _b[0] * _t)) * 100).where(grid >= Per("2020-01"))

# ----------------------------------------------------------------------------------------------- hypotheses
HYP = []


def add(source, desc, kind, cond, **kw):
    if kind == "sleeve":                                   # a sleeve only exists once its asset has data
        cond = (lambda c0, a: (lambda: B(c0()) & have([a])))(cond, kw["asset"])
    HYP.append(dict(id=f"C{len(HYP) + 1:03d}", source=source, desc=desc, kind=kind, cond=cond, **kw))


J = "Greg Jensen - NBIM In Good Company 2025"
D22 = "Stanley Druckenmiller - Sohn 2022"
DA = "Ray Dalio - Five Forces (Money Maze)"
BP = "Bob Prince - Generating Alpha Ep 12"
BG1 = "Gerstner/Gurley - BG2 Thanksgiving 2024"
GP = "Graham panel - 2022 Discretionary Strategies"
KT1 = "Kenneth Tropin - Why Macro Investing Matters"
FZ = "Felix Zulauf - Generating Alpha Ep 15"
BG2 = "Gerstner/Gurley - BG2 Tariffs 2025-04"
SB = "Scott Bessent - Macro Maven"
KG = "Krishna Guha - Real Eisman Playbook Ep 78"
GG = "Geoffrey Garrett - NBIM In Good Company"
KT2 = "Ken Tropin - Macro Hive"
D23 = "Stanley Druckenmiller - AI Dominating (Bloomberg 2023)"
D26 = "Stanley Druckenmiller - Invest, then investigate (2026)"
CR = "Crescat Capital - Gold, Silver and Fiat Money"

# ---- batch 5 / Jensen
add(J, "US lags EAFE by >10 pts over 12m -> 50% of equities in EAFE for 12m", "location",
    lambda: hold(rel("eq_eafe", "spx", 12) > 0.10, 12), assets=["eq_eafe"], s=0.5)
add(J, "same, only while the dollar is falling (US exceptionalism unwinding)", "location",
    lambda: hold(B(rel("eq_eafe", "spx", 12) > 0.10) & B(dollar12 < 0), 12), assets=["eq_eafe"], s=0.5)
add(J, "equal-weight lags cap-weight >5% in 6m, S&P up, EAFE beats equal weight -> half equities to EAFE + equal wt", "location",
    lambda: B(rel("eqw", "spx", 6) < -0.05) & B(mom("spx", 6) >= 0) & B(mom("eq_eafe", 6) > mom("eqw", 6)),
    assets=["eq_eafe", "eqw"], s=0.5)
add(J, "gold 12m beats S&P 12m and dollar falling -> 10% gold", "sleeve",
    lambda: B(mom("gold", 12) > mom("spx", 12)) & B(dollar12 < 0), asset="gold", w=0.1)
add(J, "tariff rate +2 pts y/y or real defence spending +5% y/y -> long TIPS / short 10y (20%) for 12m", "overlay",
    lambda: hold(B(tariff12 > 2) | B(realdef_yy > 5), 12),
    weights=pair(lambda: hold(B(tariff12 > 2) | B(realdef_yy > 5), 12), ["tips"], ["t10y"]))
add(J, "tariff rate +2 pts y/y or real defence spending +5% y/y -> 10% commodities for 12m", "sleeve",
    lambda: hold(B(tariff12 > 2) | B(realdef_yy > 5), 12), asset="commod", w=0.1)
add(J, "unemployment rising but real GDP >1% and nominal GDP >4% y/y -> no growth-trend cut (ex-AI capex split missing)", "block",
    lambda: gtt & B(rgdp_yy > 1) & B(ngdp_yy > 4))
add(J, "core PCE 3m annualised > 5y breakeven + 0.5 -> long TIPS / short 10y (20%) for 6m", "overlay",
    lambda: hold(corepce3 > S["fred_T5YIE"] + 0.5, 6),
    weights=pair(lambda: hold(corepce3 > S["fred_T5YIE"] + 0.5, 6), ["tips"], ["t10y"]))
_c7 = lambda: hold(B(ch(ff, 12) < 0) & unr_ok & B(core_yy > 2.5), 12)
add(J, "Fed cutting while unemployment <= 12m avg and core CPI > 2.5% -> 10% gold/commodities/TIPS for 12m", "sleeve",
    _c7, asset="x56_real", w=0.1)
add(J, "same -> short 20% long Treasuries for 12m", "overlay", _c7, weights=uw_t(_c7))
_c9 = lambda: hold(B(ch(tnx, 1) > 0.25) & B(pc(dxy, 1) < -2), 6)
add(J, "10y +25bp and dollar -2% in the same month (fiscal-constraint) -> 10% gold for 6m", "sleeve", _c9, asset="gold", w=0.1)
add(J, "same -> no long Treasuries in the de-risk book for 6m", "overlay", _c9, weights=no_long_t(_c9))
_c10 = lambda: B(debt_gdp > 100) & B(deficit > 5)
add(J, "debt/GDP > 100% and deficit > 5% -> no long Treasuries as hedge", "overlay", _c10, weights=no_long_t(_c10))
add(J, "debt/GDP > 100% and deficit > 5% -> trend-following instead of T-bills in cuts", "defensive", _c10, asset="trend")
add(J, "China 6m return > 0 and above 10m avg -> strategic 5% of equities in China", "location",
    lambda: B(mom("eq_china", 6) > 0) & above_ma("eq_china").fillna(False), assets=["eq_china"], s=0.05)
add(J, "real 10y > 1.5% -> 20% in 10y Treasuries", "sleeve", lambda: B(real10 > 1.5), asset="t10y", w=0.2)
add(J, "gold-trust regime (gold beats S&P 12m, dollar falling) -> 2% bitcoin", "sleeve",
    lambda: B(mom("gold", 12) > mom("spx", 12)) & B(dollar12 < 0), asset="btc", w=0.02)
add(J, "utilities and semis both beat S&P over 12m (resource grab) and S&P below 10m avg -> stocks 50%", "cut",
    lambda: B(rel("sec_XLU", "spx", 12) > 0) & B(rel("sec_SMH", "spx", 12) > 0) & trend_dn, level=0.5)

# ---- Druckenmiller Sohn 2022
_c22 = lambda: B(cpi_yy > 5) & B(ff < cpi_yy)
add(D22, "CPI > 5% and Fed funds < CPI -> stocks 50% until Fed funds >= CPI", "cut", _c22, level=0.5)
add(D22, "CPI > 5% and Fed funds < CPI -> 10% commodities", "sleeve", _c22, asset="commod", w=0.1)
add(D22, "CPI > 5% and Fed funds < CPI -> short 20% long Treasuries", "overlay", _c22, weights=uw_t(_c22))
add(D22, "CPI crossed above 5% in last 24m and unemployment rising or S&P below 10m avg -> stocks 50%", "cut",
    lambda: hold(B(cpi_yy > 5) & B(cpi_yy.shift(1) <= 5), 24) & (unr_up | trend_dn), level=0.5)
add(D22, "CPI peak > 4.5% in a hiking cycle -> warnings acted on until the Fed starts cutting", "gate",
    lambda: latch(B(cpi_yy.rolling(24).max() > 4.5) & B(ch(ff, 12) > 0), B(ch(ff, 3) < -0.2)))
add(D22, "post-bubble bear (<12m old, CAPE top decile, Fed not easing): 15% rally off the low -> stocks 0", "cut",
    lambda: B((dd_spx <= -0.20).astype(float).rolling(6, min_periods=1).max() > 0) & B(since_peak <= 12)
    & B(cape_p.rolling(24, min_periods=1).max() >= 90) & B(spxl / spxl.rolling(6, min_periods=1).min() - 1 >= 0.15)
    & B(ch(ff, 3) >= 0), level=0.0)
_ld = ["sec_ITB", "sec_IYT", "sec_XRT"]
_A26 = lambda: B(pd.concat([ddh(c) <= -0.40 for c in _ld], axis=1).all(axis=1))
_B26 = lambda: B(pd.concat([rel(c, "spx", 6) < 0 for c in _ld], axis=1).all(axis=1))
add(D22, "homebuilders, transports and retail each 40%+ below 12m high OR all three lag S&P 6m -> stocks 50%", "cut",
    lambda: _A26() | _B26(), level=0.5)
add(D22, "homebuilders, transports and retail each 40%+ below 12m high -> stocks 50%", "cut", _A26, level=0.5)
add(D22, "all three were 40%+ off highs within 12m and are now back above 10m avg -> no cut (early cycle)", "block",
    lambda: hold(_A26(), 12) & B(pd.concat([above_ma(c) for c in _ld], axis=1).all(axis=1)))
add(D22, "retail lags S&P >10% over 6m while real GDP > 2% -> stocks 50%", "cut",
    lambda: B(rel("sec_XRT", "spx", 6) < -0.10) & B(rgdp_yy > 2), level=0.5)
add(D22, "strong data (Philly Fed > 0 and rising) but 10y yield falling in the month -> 20% in 10y Treasuries", "sleeve",
    lambda: B(philly > 0) & B(ch(philly, 1) > 0) & B(ch(gs10, 1) < 0), asset="t10y", w=0.2)
_sq = lambda: hold(sc["squeeze"] >= 80, 6)
add(D22, "oil+rates+dollar squeeze (score >= 80) -> 10y Treasuries instead of T-bills for 6m", "defensive", _sq, asset="t10y")
add(D22, "oil+rates+dollar squeeze (score >= 80) -> stocks 50% for 6m", "cut", _sq, level=0.5)
add(D22, "S&P below 10m avg and CPI < 10y yield -> long Treasuries instead of T-bills", "defensive",
    lambda: trend_dn & B(cpi_yy < gs10), asset="t30y")
add(D22, "S&P below 10m avg and CPI > 10y yield -> commodities instead of T-bills", "defensive",
    lambda: trend_dn & B(cpi_yy > gs10), asset="commod")
add(D22, "CPI > 10y yield -> no long Treasuries as hedge", "overlay", lambda: B(cpi_yy > gs10),
    weights=no_long_t(lambda: B(cpi_yy > gs10)))
_c32 = lambda: B(cpi_yy > 5) & B(ch(cpi_yy, 3) > 0) & B(ff < cpi_yy)
add(D22, "CPI > 5% and rising, Fed funds < CPI -> 10% oil+copper", "sleeve", _c32, asset="x56_oilcu", w=0.1)
add(D22, "CPI > 5% and rising, Fed funds < CPI -> short 20% long Treasuries", "overlay", _c32, weights=uw_t(_c32))
add(D22, "same short, covered once 3+ growth warnings fire", "overlay", lambda: _c32() & B(growth_n < 3),
    weights=uw_t(lambda: _c32() & B(growth_n < 3)))
_c34 = lambda: hold(B(ind["dollar_break"] >= -2) & B(ch(ff, 12) > 2) & B(ch(ecb, 6) > ch(ff, 6)), 6)
add(D22, "dollar near 12m high, Fed +2 pts in 12m, ECB hiking faster -> half equities to EAFE/EM for 6m", "location",
    _c34, assets=["eq_eafe", "eq_em"], s=0.5)
add(D22, "drilling activity below 10y avg and oil above 10m avg, no growth cut -> 25% of equities in energy", "location",
    lambda: B(drill < drill.rolling(120, min_periods=120).mean()) & B(oil_l > ma(oil_l, 10)) & ~gtt,
    assets=["sec_XLE"], s=0.25)
add(D22, "CPI > 3% and S&P above 10m avg -> 5% bitcoin", "sleeve", lambda: B(cpi_yy > 3) & trend_up, asset="btc", w=0.05)
add(D22, "CPI > 3% and S&P below 10m avg -> 10% gold", "sleeve", lambda: B(cpi_yy > 3) & trend_dn, asset="gold", w=0.1)
add(D22, "bitcoin 40%+ below 6m high -> long S&P / short Nasdaq 20% for 3m", "overlay",
    lambda: hold(ddh("btc", 6) < -0.40, 3), weights=pair(lambda: hold(ddh("btc", 6) < -0.40, 3), ["spx"], ["ndx"]))
add(D22, "live book down >10% within 6 months -> stocks 50% (cold streak)", "cut", lambda: B(live_dd6 < -0.10), level=0.5)
add(D22, "live book drawdown > 15% -> stocks 0 for 2 months (take a break)", "cut",
    lambda: hold(B(live_dd < -0.15) & B(live_dd.shift(1) >= -0.15), 2), level=0.0)
add(D22, "CAPE top 5% and Fed balance sheet shrinking y/y -> 10% trend-following", "sleeve",
    lambda: B(cape_p >= 95) & B(fedbs12 < 0), asset="trend", w=0.1)

# ---- Dalio Five Forces
add(DA, "currency down >15% in 6m (Brazil, China, Japan, Korea REER; Mexico, India vs USD) -> 25% of equities there for 12m", "location",
    lambda: deval_any, assets=["x56_deval"], s=0.25)
add(DA, "dollar down >15% in 6m without oil/inflation shock -> no cut", "block",
    lambda: B(pc(dxy, 6) < -15) & ~(B(oil6 > 50) | B(ch(cpi_yy, 12) > 2)))
add(DA, "dollar down >15% in 6m with oil +50% in 6m or CPI +2 pts in 12m -> stocks 50%", "cut",
    lambda: B(pc(dxy, 6) < -15) & (B(oil6 > 50) | B(ch(cpi_yy, 12) > 2)), level=0.5)
add(DA, "real policy rate > 2% and dollar +10% in 12m -> long S&P / short EM 20%", "overlay",
    lambda: B(rpol > 2) & B(dollar12 > 10), weights=pair(lambda: B(rpol > 2) & B(dollar12 > 10), ["spx"], ["eq_em"]))
add(DA, "EM stocks 30%+ below 12m high and Fed easing -> no cut for 3m (crisis = bottom)", "block",
    lambda: hold(B(em_dd < -0.30) & B(ch(ff, 3) < 0), 3))
add(DA, "real 10y < 0 and federal interest/receipts > 15% and rising -> 10% gold for 12m", "sleeve",
    lambda: hold(B(real10 < 0) & B(int_rec > 15) & B(ch(int_rec, 12) > 0), 12), asset="gold", w=0.1)
_c50 = lambda: B(deficit > 5) & B(ch(hold_share, 12) < 0)
add(DA, "deficit > 5%, Fed+foreign share of debt falling, Fed balance sheet shrinking (3m) -> stocks 50%", "cut",
    lambda: _c50() & B(fedbs3 < 0), level=0.5)
add(DA, "deficit > 5%, Fed+foreign share falling, Fed balance sheet growing (3m) -> 10% gold", "sleeve",
    lambda: _c50() & B(fedbs3 > 0), asset="gold", w=0.1)
add(DA, "Fed balance sheet -5% y/y (QT) -> short 20% long Treasuries", "overlay", lambda: B(fedbs12 < -5),
    weights=uw_t(lambda: B(fedbs12 < -5)))
add(DA, "foreign holdings of Treasuries falling y/y -> long gold / short long Treasuries 10% (CB gold buying missing)", "overlay",
    lambda: B(pc(q("fred_FDHBFIN", 6), 12) < 0),
    weights=pair(lambda: B(pc(q("fred_FDHBFIN", 6), 12) < 0), ["gold"], ["t30y"], w=0.1))
add(DA, "T-bill minus core CPI > 1.5 and deficit > 5% -> T-bills, not long Treasuries, as hedge", "overlay",
    lambda: B(tbill3 - core_yy > 1.5) & B(deficit > 5),
    weights=no_long_t(lambda: B(tbill3 - core_yy > 1.5) & B(deficit > 5)))
add(DA, "T-bill minus core CPI > 1.5 -> T-bills, not long Treasuries, as hedge", "overlay",
    lambda: B(tbill3 - core_yy > 1.5), weights=no_long_t(lambda: B(tbill3 - core_yy > 1.5)))
add(DA, "drilling activity in bottom quartile of 20y range and inflation hot -> 25% of equities in energy", "location",
    lambda: B(rpct(drill, 240, 120) <= 25) & hotP, assets=["sec_XLE"], s=0.25)
add(DA, "debt/GDP > 100%, Fed holds > 20% of debt, rates near zero or real rates < 0 -> 10% gold", "sleeve",
    lambda: B(debt_gdp > 100) & B(fed_share > 20) & (B(ff < 0.5) | B(rpol < 0)), asset="gold", w=0.1)

# ---- Bob Prince
add(BP, "dollar +10% in 12m -> long S&P / short industrials 20% for 12m", "overlay",
    lambda: hold(dollar12 > 10, 12), weights=pair(lambda: hold(dollar12 > 10, 12), ["spx"], ["sec_XLI"]))


def _oil_w():
    dn, up = B(oil6 < -30), B(oil6 > 30)
    imp, exp_ = ["eq_india", "eq_japan", "eq_korea"], ["eq_canada", "eq_brazil", "eq_mexico"]
    ok = have(imp + exp_)
    sgn = (dn.astype(float) - up.astype(float)) * ok.astype(float)
    d = {a: 0.2 / 3 * sgn for a in imp}
    d.update({a: -0.2 / 3 * sgn for a in exp_})
    return pd.DataFrame(d, index=grid)


add(BP, "oil -30% in 6m -> long importers (India, Japan, Korea) / short exporters (Canada, Brazil, Mexico) 20%; reverse at +30%",
    "overlay", lambda: B(oil6 < -30) | B(oil6 > 30), weights=_oil_w)
_c64 = lambda: B(ind["core_pce"] < 0) & B(ch(ind["core_pce"], 3) < 0) & unr_up & cneg
add(BP, "core inflation 3m < 12m and falling, unemployment rising, corr < 0 -> ultra-long Treasuries instead of T-bills", "defensive",
    _c64, asset="t30y_long")
add(BP, "ultra-long duration hedge: 70% EDV-type instead of 100% TLT whenever the book holds TLT", "overlay", lambda: B(T30 > 0),
    weights=lambda: pd.DataFrame({"t30y": -T30, "t30y_long": 0.7 * T30}, index=grid))
add(BP, "contraction state (not hot) -> ultra-long Treasuries instead of T-bills", "defensive",
    lambda: B(stage == "contraction") & ~hotP, asset="t30y_long")
add(BP, "overheating or stagflation state -> 2y Treasuries instead of T-bills", "defensive", lambda: overheat | stagfl, asset="t2y")
add(BP, "gold system: real 10y down over 6m or dollar below 12m avg -> 10% gold", "sleeve",
    lambda: B(ch(real10, 6) < 0) | dxy_below, asset="gold", w=0.1)
add(BP, "balanced macro (CPI 2-3%, unemployment and Fed steady) but policy uncertainty top decile (10y) -> 10% gold", "sleeve",
    lambda: B((cpi_yy >= 2) & (cpi_yy <= 3)) & B((unr - unr.rolling(12).mean()).abs() < 0.3) & B(ch(ff, 12).abs() < 0.5)
    & B(epu_p10 > 90), asset="gold", w=0.1)

# ---- BG2 2024
add(BG1, "federal outlay growth below receipt growth for 4 quarters -> 20% long Treasuries", "sleeve",
    lambda: consec(pc(q("fred_FGEXPND", 5), 12) < pc(q("fred_FGRECPT", 5), 12), 10), asset="t30y", w=0.2)
add(BG1, "gasoline +30% in 6m -> long staples / short retail 20% for 6m", "overlay",
    lambda: hold(pc(gas, 6) > 30, 6), weights=pair(lambda: hold(pc(gas, 6) > 30, 6), ["sec_XLP"], ["sec_XRT"]))

# ---- Graham panel
add(GP, "Fed put on: S&P 10%+ below peak and core CPI < 2.5% -> no cut for 6m", "block",
    lambda: hold(B(dd_spx <= -0.10) & B(core_yy < 2.5), 6))
add(GP, "Fed put off: core CPI > 3.5% and S&P below 10m avg -> stocks 0 until trend recovers", "cut",
    lambda: B(core_yy > 3.5) & trend_dn, level=0.0)
add(GP, "stock-bond corr > 0 and core CPI > 3% -> trend-following instead of T-bills in cuts", "defensive",
    lambda: B(stockbond > 0) & B(core_yy > 3), asset="trend")
add(GP, "stock-bond corr > 0 and core CPI > 3% -> long dollar instead of T-bills in cuts", "defensive",
    lambda: B(stockbond > 0) & B(core_yy > 3), asset="usd")
_c78 = lambda: latch(B(core_yy > 4) & B(ch(ff, 12) > 2) & B(stockbond > 0), B(ch(ff, 3) <= 0) | B(ind["core_pce"] < 0))
add(GP, "core CPI > 4%, Fed +2 pts in 12m, corr > 0 -> stocks 50% until Fed pauses or core 3m < 12m", "cut", _c78, level=0.5)
add(GP, "same -> long dollar 20% / short long Treasuries 20%", "overlay", _c78,
    weights=lambda: pd.DataFrame({"usd": 0.2 * _c78().astype(float) * have(["usd"]).astype(float),
                                  "t30y": -0.2 * _c78().astype(float)}, index=grid))
add(GP, "EM currencies above 10m avg and VIX < 25 -> 10% EM currency carry basket", "sleeve",
    lambda: above_ma("em_fx").fillna(False) & B(vixm < 25), asset="em_fx", w=0.1)
add(GP, "Japan CPI > 2%, BoJ <= 0, US-Japan 10y gap widening (6m) -> short yen 20%", "overlay",
    lambda: B(jcpi_yy > 2) & B(boj <= 0) & B(ch(gs10 - jgb10, 6) > 0),
    weights=uw_t(lambda: B(jcpi_yy > 2) & B(boj <= 0) & B(ch(gs10 - jgb10, 6) > 0), asset="jpy"))
add(GP, "US-Japan 10y gap widening over 6m -> short yen 20%", "overlay", lambda: B(ch(gs10 - jgb10, 6) > 0),
    weights=uw_t(lambda: B(ch(gs10 - jgb10, 6) > 0), asset="jpy"))
add(GP, "core services 3m annualised > 12m and > 4% -> short 2y Treasuries 20% for 3m", "overlay",
    lambda: hold(B(svc3 > svc12) & B(svc3 > 4), 3), weights=uw_t(lambda: hold(B(svc3 > svc12) & B(svc3 > 4), 3), asset="t2y"))
add(GP, "Fed+ECB+BoJ balance sheets shrinking over 6m -> stocks 50%", "cut", lambda: B(gcb6 < 0), level=0.5)
add(GP, "Fed+ECB+BoJ balance sheets shrinking over 6m -> no long Treasuries as hedge", "overlay", lambda: B(gcb6 < 0),
    weights=no_long_t(lambda: B(gcb6 < 0)))
add(GP, "real 10y +1.5 pts in 12m and Baa spread +1 pt in 6m (central-bank flinch) -> 20% long Treasuries for 6m", "sleeve",
    lambda: hold(B(ch(real10, 12) > 1.5) & B(ind["baa_chg"] > 1), 6), asset="t30y", w=0.2)
add(GP, "deficit widening y/y, unemployment not rising, Fed hiking -> 10% commodities", "sleeve",
    lambda: B(ch(deficit, 12) > 0) & ~unr_up & B(ch(ff, 12) > 0), asset="commod", w=0.1)

# ---- Tropin (iConnections) + Tropin (Macro Hive)
add(KT1, "more than 8 x 25bp policy moves in 12m (Fed+ECB; BoE missing) -> 20% trend-following", "sleeve",
    lambda: B(moves12 > 8), asset="trend", w=0.2)
add(KT2, "policy-rate changes > 200bp in 12m (Fed+ECB; BoE missing) -> 20% trend-following", "sleeve",
    lambda: B(bp12 > 200), asset="trend", w=0.2)
add(KT1, "CAPE top decile and deficit > 5% outside recession -> 20% trend-following", "sleeve",
    lambda: B(cape_p >= 90) & B(deficit > 5) & ~unr_up, asset="trend", w=0.2)
add(KT2, "permanent 20% time-series momentum sleeve (AQR TSMOM)", "sleeve", lambda: TRUE, asset="trend", w=0.2)
add(KT2, "permanent 20% time-series momentum sleeve (own 12m trend on 6 assets)", "sleeve", lambda: TRUE, asset="trend_ls", w=0.2)
add(KT1, "20% trend-following except when policy uncertainty is above its 95th percentile", "sleeve",
    lambda: B(epu_p < 95), asset="trend", w=0.2)
add(KT1, "permanent 20% trend + carry + value multi-style macro sleeve (AQR)", "sleeve", lambda: TRUE,
    asset="aqr_all_macro_multi_style", w=0.2)
add(KT1, "tariff rate +3 pts y/y -> short 2y Treasuries 20% for 6m", "overlay", lambda: hold(tariff12 > 3, 6),
    weights=uw_t(lambda: hold(tariff12 > 3, 6), asset="t2y"))
_c102 = lambda: B(ind["termprem"] > 1) | (B(ch(gs10, 6) > 0) & B(ch(ff, 6) < 0))
add(KT1, "bond canary: term premium +1 pt in 12m or 10y up while Fed cuts (6m) -> stocks 50%", "cut", _c102, level=0.5)
add(KT1, "bond canary -> short 20% long Treasuries", "overlay", _c102, weights=uw_t(_c102))

# ---- Zulauf
add(FZ, "expansion stage -> half equities into materials, industrials, energy", "location",
    lambda: B(stage == "expansion"), assets=["sec_XLB", "sec_XLI", "sec_XLE"], s=0.5)
add(FZ, "contraction stage -> half equities into staples, utilities, health care", "location",
    lambda: B(stage == "contraction"), assets=["sec_XLP", "sec_XLU", "sec_XLV"], s=0.5)
_c108 = lambda: B(mom("commod", 12) > 0.5) & B(ch(ff, 12) > 3)
add(FZ, "commodities +50% in 12m and Fed +3 pts in 12m -> drop commodity sleeve, short commodity stocks 20% vs S&P", "overlay",
    _c108, weights=lambda: pd.DataFrame({"commod": -X5["commod"] * _c108().astype(float)}, index=grid).join(
        pair(_c108, ["spx"], ["sec_XLE", "sec_GDX", "sec_XME"])()))
add(FZ, "1987 setup: 10y +1.5 pts in 6m, earnings yield < 10y - 2, dollar falling -> stocks 0", "cut",
    lambda: B(ch(gs10, 6) > 1.5) & B(ey - gs10 < -2) & B(dollar12 < 0), level=0.0)
add(FZ, "macro cuts only when S&P trend agrees on 2 of 3 horizons (10m, 3m avg, 1m) -> else no cut", "block",
    lambda: B(up_n >= 2))
add(FZ, "S&P at 12m high but < 50% of industries in uptrend -> stocks 50%", "cut",
    lambda: B(spxl >= spxl.rolling(12).max()) & B(ind["breadth"] < 50), level=0.5)
add(FZ, "S&P at 12m high but < 50% of 16 country markets above 10m avg -> stocks 50%", "cut",
    lambda: B(spxl >= spxl.rolling(12).max()) & B(cty_breadth < 50), level=0.5)
add(FZ, "secular bull (S&P above 10-yr avg, 10y lower than a year ago) -> ignore warning share < 25%", "block",
    lambda: B(spxl > ma(spxl, 120)) & B(gs10 < gs10.shift(12)) & B(share_ < 0.25))
add(FZ, "household equity share top decile and trend confirms (2 of 3 horizons down) -> stocks 50%", "cut",
    lambda: B(hh_p >= 90) & B(up_n <= 1), level=0.5)

# ---- batch 6 / Petraeus
add("David Petraeus - Money Maze 2023", "tariff rate rising y/y -> long India+Mexico / short China 20% for 24m", "overlay",
    lambda: hold(tariff12 > 0, 24), weights=pair(lambda: hold(tariff12 > 0, 24), ["eq_india", "eq_mexico"], ["eq_china"]))

# ---- BG2 tariffs 2025
_c9b = lambda: latch(B(epu_p10 > 90), B(epu_p10 < 75))
add(BG2, "policy uncertainty above 90th pct (10y) -> stocks 50% until below 75th pct (speaker: bottom third)", "cut", _c9b, level=0.5)
_c12 = lambda: hold(consec(epu_p10 > 90, 3), 6)
add(BG2, "policy uncertainty above 90th pct for 3 months -> stocks 50% for 6m", "cut", _c12, level=0.5)
add(BG2, "same -> long defensives (staples, utilities, health) / short cyclicals (industrials, materials, retail) 20%", "overlay",
    _c12, weights=pair(_c12, ["sec_XLP", "sec_XLU", "sec_XLV"], ["sec_XLI", "sec_XLB", "sec_XRT"]))
_c13 = lambda: hold((1 + mom("gold", 6)) / (1 + mom("spx", 6)) - 1 > 0.20, 3)
add(BG2, "gold beats S&P by >20% over 6m -> 10% gold for 3m", "sleeve", _c13, asset="gold", w=0.1)
add(BG2, "gold beats S&P by >20% over 6m -> stocks 50% for 3m", "cut", _c13, level=0.5)
_c14 = lambda: B(vixm > 30) & B(pc(dxy, 1) < -2) & B(ch(tnx, 1) > 0.20)
add(BG2, "sell-America month (VIX > 30, dollar -2%, 10y +20bp) -> gold instead of T-bills", "defensive", _c14, asset="gold")
add(BG2, "sell-America month -> no long Treasuries as hedge", "overlay", _c14, weights=no_long_t(_c14))
add(BG2, "effective tariff rate > 10% and rising -> stocks 50%", "cut", lambda: B(tariff > 10) & B(tariff12 > 0), level=0.5)
add(BG2, "tariff rate +3 pts in 12m -> 10% gold for 12m", "sleeve", lambda: hold(tariff12 > 3, 12), asset="gold", w=0.1)
add(BG2, "tariff rate +3 pts in 12m -> long TIPS / short 10y 20% for 12m", "overlay", lambda: hold(tariff12 > 3, 12),
    weights=pair(lambda: hold(tariff12 > 3, 12), ["tips"], ["t10y"]))
add(BG2, "oil +20% in a month -> short oil 10% for 6m (spikes fade)", "overlay", lambda: hold(pc(oil_l, 1) > 20, 6),
    weights=uw_t(lambda: hold(pc(oil_l, 1) > 20, 6), w=0.1, asset="oil"))
add(BG2, "narrow leadership (score >= 80) and tariff rate rising -> all equities in equal weight", "location",
    lambda: B(sc["leadership"] >= 80) & B(tariff12 > 0), assets=["eqw"], s=1.0)
add(BG2, "S&P 10%+ below peak while policy uncertainty >= 75th pct -> stocks 50%", "cut",
    lambda: B(dd_spx <= -0.10) & B(epu_p10 >= 75), level=0.5)
add(BG2, "tariff rate 5+ pts below its 12m peak (walk-back) -> no cut for 3m", "block",
    lambda: hold(tariff <= tariff.rolling(12, min_periods=1).max() - 5, 3))

# ---- Bessent
add(SB, "truck freight +3% y/y -> 25% of equities in industrials, materials, transports for 6m", "location",
    lambda: hold(truck_yy > 3, 6), assets=["sec_XLI", "sec_XLB", "sec_IYT"], s=0.25)
add(SB, "card delinquency rate +0.5 pt y/y -> stocks 50%", "cut", lambda: B(ch(cards_q, 12) > 0.5), level=0.5)
add(SB, "oil above 10m avg -> long oil / short energy stocks 10% (own the commodity)", "overlay",
    lambda: B(oil_l > ma(oil_l, 10)), weights=pair(lambda: B(oil_l > ma(oil_l, 10)), ["oil"], ["sec_XLE"], w=0.1))
add(SB, "Korea hiked into falling house prices within 12m and has paused -> 25% of equities in Korea for 12m", "location",
    lambda: hold(hold(B(ch(krate, 6) > 0) & B(khouse_yy < 0), 12) & B(ch(krate, 3) <= 0), 12), assets=["eq_korea"], s=0.25)
add(SB, "VIX < 12 (cheap vol) -> 5% tail-hedge fund", "sleeve", lambda: B(vixm < 12), asset="tail", w=0.05)
add(SB, "US real effective dollar > 1.5 sd above 20y mean -> half equities to EAFE/EM", "location",
    lambda: B(zroll(reer_us) > 1.5), assets=["eq_eafe", "eq_em"], s=0.5)
add(D26, "US real effective dollar in top decile of own history -> half equities to EAFE/EM (NIIP missing)", "location",
    lambda: B(pctl(reer_us) >= 90), assets=["eq_eafe", "eq_em"], s=0.5)
add(SB, "EM real currency > 1 sd cheap vs 20y mean (Brazil, China, Korea) -> 25% of equities there", "location",
    lambda: cheapfx_any, assets=["x56_cheapfx"], s=0.25)
add(SB, "trend-following lost money over 3 years -> 20% trend (add after a slump)", "sleeve",
    lambda: B(mom("trend", 36) < 0), asset="trend", w=0.2)
add(SB, "VIX > 40 (policy hits the wall) -> no cut for 3m", "block", lambda: hold(vixm > 40, 3))
add(D23, "VIX > 35 -> no cut for 3m (deploy at extremes)", "block", lambda: hold(vixm > 35, 3))
_c41 = lambda: hold(B(ch(ff, 3) < 0) & B(ngdp_yy > 5) & B(core3 > 3), 6)
add(SB, "Fed cuts while nominal GDP > 5% and core CPI 3m > 3% -> short 20% long Treasuries for 6m", "overlay", _c41, weights=uw_t(_c41))
add(SB, "deficit > 6% with unemployment < 5% -> short 20% long Treasuries", "overlay",
    lambda: B(deficit > 6) & B(unr < 5), weights=uw_t(lambda: B(deficit > 6) & B(unr < 5)))
add(D23, "deficit > 5% with unemployment < 4.5% -> short 20% long Treasuries", "overlay",
    lambda: B(deficit > 5) & B(unr < 4.5), weights=uw_t(lambda: B(deficit > 5) & B(unr < 4.5)))
_c43 = lambda: B(mom("eq_china", 1).shift(1) > 0.2) | B(mom("eq_china", 1).shift(2) > 0.2)
add(SB, "China +20% in a month -> fade it 1-3 months later: long EM / short China 10%", "overlay", _c43,
    weights=pair(_c43, ["eq_em"], ["eq_china"], w=0.1))
add(SB, "Japan CPI > 1% y/y -> 25% of equities in Japan", "location", lambda: B(jcpi_yy > 1), assets=["eq_japan"], s=0.25)
add(SB, "r > g (10y above nominal GDP growth) and deficit > 5% -> 10% gold", "sleeve",
    lambda: B(y10_ngdp > 0) & B(deficit > 5), asset="gold", w=0.1)
add(SB, "loan officers tightening > 40% net -> long S&P / short banks 20% for 6m", "overlay", lambda: hold(sloos > 40, 6),
    weights=pair(lambda: hold(sloos > 40, 6), ["spx"], ["sec_KBE"]))
add(SB, "tightening was > 40% within 12m and is now falling -> 25% of equities in banks for 6m", "location",
    lambda: hold(B(sloos.rolling(12, min_periods=1).max() > 40) & B(sloos < sloos.shift(3)), 6), assets=["sec_KBE"], s=0.25)

# ---- Guha
_c53 = lambda n: consec(corepce_yy > 2, n) & ~unr_up
add(KG, "core PCE above 2% for 60 months, unemployment not rising -> short 20% long Treasuries", "overlay",
    lambda: _c53(60), weights=uw_t(lambda: _c53(60)))
add(KG, "core PCE above 2% for 36 months, unemployment not rising -> short 20% long Treasuries", "overlay",
    lambda: _c53(36), weights=uw_t(lambda: _c53(36)))
add(KG, "real 10y > 2% (high neutral rate) -> no long Treasuries as hedge", "overlay", lambda: B(real10 > 2),
    weights=no_long_t(lambda: B(real10 > 2)))
add(KG, "MOVE > 120 -> half the usual long-Treasury hedge", "overlay", lambda: B(move > 120),
    weights=no_long_t(lambda: B(move > 120), frac=0.5))
add(KG, "10y +75bp in 3 months -> 20% long Treasuries for 3m (buy after the overshoot)", "sleeve",
    lambda: hold(ch(gs10, 3) > 0.75, 3), asset="t30y", w=0.2)
add(KG, "net liquidity falling (3m) and 10y 50bp+ below its 12m peak -> stocks 50%", "cut",
    lambda: B(ind["netliq"] < 0) & B(gs10 <= gs10.rolling(12).max() - 0.5), level=0.5)
add(KG, "10y > 5% -> long Nasdaq / short small caps, homebuilders, REITs, regional banks 20%", "overlay",
    lambda: B(gs10 > 5), weights=pair(lambda: B(gs10 > 5), ["ndx"], ["small", "sec_ITB", "sec_IYR", "sec_KRE"]))
add(KG, "10y > 6% -> stocks 50%", "cut", lambda: B(gs10 > 6), level=0.5)
add(KG, "mortgage rate > 7% -> long S&P / short homebuilders 20%", "overlay", lambda: B(mort > 7),
    weights=pair(lambda: B(mort > 7), ["spx"], ["sec_ITB"]))
add(KG, "mortgage rate 1 pt below a >7% peak (24m) -> 25% of equities in homebuilders for 12m", "location",
    lambda: hold(B(mort.rolling(24).max() > 7) & B(mort <= mort.rolling(24).max() - 1), 12), assets=["sec_ITB"], s=0.25)
add(KG, "household equity share high and S&P 15%+ below peak -> long staples / short retail 20% for 9m", "overlay",
    lambda: hold(B(hh_p >= 80) & B(dd_spx <= -0.15), 9),
    weights=pair(lambda: hold(B(hh_p >= 80) & B(dd_spx <= -0.15), 9), ["sec_XLP"], ["sec_XRT"]))
_c66 = lambda: B(corr12(R["spx"], pc(oil_l, 1)) < -0.3) & B(corr12(R["spx"], ch(gs10, 1)) < -0.3)
add(KG, "S&P falls with oil up and yields up (12m corr < -0.3 with both) -> gold instead of T-bills", "defensive", _c66, asset="gold")

# ---- Garrett
_imp = q("fred_IMPGS", 5) / ngdp
add(GG, "imports/GDP falling y/y for 4 quarters (deglobalisation) -> 10% commodities", "sleeve",
    lambda: consec(ch(_imp, 12) < 0, 10), asset="commod", w=0.1)
add(GG, "tariff rate rising y/y -> long TIPS / short 10y 20%", "overlay", lambda: B(tariff12 > 0),
    weights=pair(lambda: B(tariff12 > 0), ["tips"], ["t10y"]))
add(GG, "nickel +20% in 6m -> long Indonesia / short EM 10% for 6m", "overlay", lambda: hold(nickel6 > 20, 6),
    weights=pair(lambda: hold(nickel6 > 20, 6), ["eq_indonesia"], ["eq_em"], w=0.1))

# ---- Tropin Macro Hive
add(KT2, "S&P -10% in a month and core CPI 3m < 4% -> 20% long Treasuries for 3m", "sleeve",
    lambda: hold(B(R["spx"] < -0.10) & B(core3 < 4), 3), asset="t30y", w=0.2)
_c77 = lambda: latch(B(core_yy > 4), B(core3 < 3))
add(KT2, "core CPI > 4% -> short 20% long Treasuries until core 3m annualised < 3%", "overlay", _c77, weights=uw_t(_c77))
add(KT2, "trailing P/E > 18 (forward P/E missing), curve inverted, OECD leading index down 6m -> stocks 50%", "cut",
    lambda: B(pe > 18) & B(curve < 0) & B(cli < cli.shift(6)), level=0.5)
add(KT2, "earnings yield minus T-bill < 1 pt -> stocks 50%", "cut", lambda: B(ey - tbill3 < 1), level=0.5)
add(KT2, "earnings yield minus T-bill > 4 pts -> no cut", "block", lambda: B(ey - tbill3 > 4))
add(KT2, "US-German 10y gap down 50bp in 6m (2y missing) -> half equities to Europe/Germany for 6m", "location",
    lambda: hold(ch(gs10 - bund10, 6) < -0.5, 6), assets=["eq_europe", "eq_germany"], s=0.5)
_c82 = lambda: hold(B(curve.rolling(12).min() < 0) & B(curve - curve.rolling(12).min() > 0.5), 6)
add(KT2, "2s10s steepens 50bp from an inverted trough -> stocks 0 for 6m", "cut", _c82, level=0.0)
add(KT2, "2s10s steepens 50bp from an inverted trough -> 2y Treasuries instead of T-bills for 6m", "defensive", _c82, asset="t2y")
add(KT2, "term premium < 0 -> short 20% long Treasuries", "overlay", lambda: B(tp < 0), weights=uw_t(lambda: B(tp < 0)))
add(KT2, "term premium > 1% -> 20% long Treasuries", "sleeve", lambda: B(tp > 1), asset="t30y", w=0.2)
add(KT2, "2y 50bp+ below Fed funds while core CPI 3m > 3.5% -> short 2y Treasuries 20% for 3m", "overlay",
    lambda: hold(B(gs2 < ff - 0.5) & B(core3 > 3.5), 3),
    weights=uw_t(lambda: hold(B(gs2 < ff - 0.5) & B(core3 > 3.5), 3), asset="t2y"))
add(KT2, "core CPI > 3% and policy-rate changes > 200bp in 12m -> 20% trend-following", "sleeve",
    lambda: B(core_yy > 3) & B(bp12 > 200), asset="trend", w=0.2)

# ---- Druckenmiller 2023
add(D23, "federal interest/receipts > 20% and rising -> gold instead of T-bills in cuts", "defensive",
    lambda: B(int_rec > 20) & B(ch(int_rec, 12) > 0), asset="gold")
add(D23, "Fed +3 pts in 12m after CAPE > 30 -> stocks 50% until Fed cutting y/y and credit spread off its peak", "cut",
    lambda: latch(B(ch(ff, 12) > 3) & (B(cape.rolling(24).max() > 30) | B(sc["mcap_gdp"] >= 90)),
                  B(ch(ff, 12) < 0) & B(baa_sp < baa_sp.rolling(6).max())), level=0.5)
add(D23, "loan officers tightening > 30% net -> long S&P / short REITs, regional banks, small caps 20% for 6m", "overlay",
    lambda: hold(sloos > 30, 6), weights=pair(lambda: hold(sloos > 30, 6), ["spx"], ["sec_IYR", "sec_KRE", "small"]))
add(D23, "curve inverted within the last 24m -> warnings acted on", "gate", lambda: B(curve.rolling(24, min_periods=1).min() < 0))
add(D23, "Treasury cash account +$500bn in 6m (liquidity drain) -> stocks 50%", "cut", lambda: B(ch(tga, 6) > 500000), level=0.5)
add(D23, "M2 more than 5% above its 2010-19 trend -> no cut (recession signals delayed)", "block", lambda: B(m2gap > 5))
add(D23, "truck freight down y/y and real retail sales down over 6m -> stocks 0", "cut",
    lambda: B(truck_yy < 0) & B(pc(real_retail, 6) < 0), level=0.0)
add(D23, "stagflation state -> half equities into energy and materials", "location", lambda: stagfl,
    assets=["sec_XLE", "sec_XLB"], s=0.5)
add(D23, "in cuts hold industries beating the S&P by >10% over 6m instead of T-bills", "defensive", lambda: strong_any,
    asset="x56_strong")
add(D23, "industries up >100% in 12m (last 24m) and still above 10m avg -> 25% of equities in them", "location",
    lambda: secular_any, assets=["x56_secular"], s=0.25)
add(D23, "Japan CPI > 2%, BoJ <= 0.5%, Japan above 10m avg -> half equities in Japan for 12m", "location",
    lambda: hold(B(jcpi_yy > 2) & B(boj <= 0.5) & above_ma("eq_japan").fillna(False), 12), assets=["eq_japan"], s=0.5)
add(D23, "mixed signals (warning share 15-35%) and MOVE > 100 -> 20% trend-following", "sleeve",
    lambda: B((share_ >= 0.15) & (share_ <= 0.35)) & B(move > 100), asset="trend", w=0.2)
add(D23, "net liquidity falling and Fed balance sheet shrinking y/y, VIX < 35 -> stocks 50%", "cut",
    lambda: B(ind["netliq"] < 0) & B(fedbs12 < 0) & B(vixm < 35), level=0.5)

# ---- Druckenmiller 2026
add(D26, "industry lagged S&P by 30%+ over 3y, now above 10m avg and beating S&P over 6m -> 25% of equities for 12m", "location",
    lambda: turn_any, assets=["x56_turn"], s=0.25)
add(D26, "narrow leadership or rally speed in worst fifth -> half equities to equal weight, value, health care, Japan, Korea",
    "location", lambda: B(sc["leadership"] >= 80) | B(sc["rally"] >= 80),
    assets=["eqw", "value", "sec_XLV", "eq_japan", "eq_korea"], s=0.5)
add(D26, "CAPE top decile and real GDP > 2% -> half equities in Japan and Korea", "location",
    lambda: B(sc["cape"] >= 90) & B(rgdp_yy > 2), assets=["eq_japan", "eq_korea"], s=0.5)
add(D26, "copper above 10m avg -> 10% copper futures (mine supply missing)", "sleeve",
    lambda: above_ma("copper").fillna(False), asset="copper", w=0.1)
add(D26, "copper above 10m avg -> long copper / short metals & mining stocks 10%", "overlay",
    lambda: above_ma("copper").fillna(False),
    weights=pair(lambda: above_ma("copper").fillna(False), ["copper"], ["sec_XME"], w=0.1))
add(D26, "expansion/overheating, Fed not hiking (6m), deficit > 5% -> short 20% long Treasuries", "overlay",
    lambda: (B(stage == "expansion") | overheat) & B(ch(ff, 6) <= 0) & B(deficit > 5),
    weights=uw_t(lambda: (B(stage == "expansion") | overheat) & B(ch(ff, 6) <= 0) & B(deficit > 5)))
_c124 = lambda: hold(B(ch(ff, 6) < 0) & B(rgdp_yy > 2.5) & B(mom("commod", 6) > 0.10), 12)
add(D26, "Fed cutting into a boom (real GDP > 2.5%) with commodities +10% in 6m -> short 20% long Treasuries for 12m", "overlay",
    _c124, weights=uw_t(_c124))
add(D26, "same -> 10% gold/commodities/TIPS for 12m", "sleeve", _c124, asset="x56_real", w=0.1)
add(D26, "strong growth, deficit > 5%, Fed easing, CAPE top decile -> half equities to EAFE/EM", "location",
    lambda: B(rgdp_yy > 2.5) & B(deficit > 5) & B(ch(ff, 6) < 0) & B(sc["cape"] >= 90), assets=["eq_eafe", "eq_em"], s=0.5)

# ---- Crescat
add(CR, "deficit > 5% and real policy rate (FF - core PCE) < 1% -> 10% gold/silver/copper", "sleeve",
    lambda: B(deficit > 5) & B(ff - corepce_yy < 1), asset="x56_metals", w=0.1)
_gm = lv("sec_GDX") / lv("gold")
_c134 = lambda: B(lv("gold") >= lv("gold").rolling(12).max()) & B(rpct(_gm, 120, 60) <= 10)
add(CR, "gold at 12m high and miners/gold ratio in bottom decile of 10y -> long miners / short gold 10% for 12m", "overlay",
    lambda: hold(_c134(), 12), weights=pair(lambda: hold(_c134(), 12), ["sec_GDX"], ["gold"], w=0.1))
add(CR, "same, only once miners beat gold over 6m", "overlay", lambda: hold(_c134(), 12) & B(pc(_gm, 6) > 0),
    weights=pair(lambda: hold(_c134(), 12) & B(pc(_gm, 6) > 0), ["sec_GDX"], ["gold"], w=0.1))
_c135 = lambda: hold(B(sc["leadership"] >= 80) & B(core_yy > core_yy.shift(12)) & B(ch(gs10, 12) > 1), 24)
add(CR, "narrow leadership, core CPI rising, 10y +1 pt in 12m -> stocks 50% for 24m", "cut", _c135, level=0.5)
add(CR, "same -> 10% gold + gold miners for 24m", "sleeve", _c135, asset="x56_goldmin", w=0.1)
_fedtsy_yy = pc(S["fred_TREAST"], 12).combine_first(pc(q("fred_FDHBFRBN", 6), 12))
add(CR, "Fed Treasury holdings growing 10 pts faster than nominal GDP -> 10% gold/commodities/TIPS for 24m", "sleeve",
    lambda: hold(_fedtsy_yy - ngdp_yy > 10, 24), asset="x56_real", w=0.1)
add(CR, "money growth top quartile with narrow leadership (last 24m), now M2 falling y/y -> 10% gold", "sleeve",
    lambda: hold(B(pctl(m2_yy) >= 75) & B(sc["leadership"] >= 80), 24) & B(m2_yy < 0), asset="gold", w=0.1)
