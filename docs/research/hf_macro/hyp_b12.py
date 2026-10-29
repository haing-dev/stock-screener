from harness import *  # noqa
"""Hypotheses from transcript rule batches 1 and 2 (/home/claude/macro_read/out/batch1.md, batch2.md).
Every condition is known at the end of month t (the weight is earned in t+1). Lags: monthly FRED macro .shift(1)
(JOLTS 2, Case-Shiller 3), quarterly series dated at quarter start ffill(2) + shift(4..6), market series none.
Size conventions where the speaker gave none: cut 0.0 for "cut", 0.5 for "reduce/underweight/trim"; sleeve 10%;
location 50% for countries/regions/small caps/Nasdaq, 20% for a single sector; overlay +-10%."""
import numpy as np
import pandas as pd

HYP = []


def H(src, desc, kind, cond, **kw):
    if kind == "sleeve":                     # a sleeve is only switched on once its asset has data (no cash drag before)
        c0, a0 = cond, kw["asset"]
        cond = lambda: Bo(c0()) & R[a0].notna().cummax()
    d = dict(id=f"A{len(HYP) + 1:03d}", source=src, desc=desc, kind=kind, cond=cond)
    d.update(kw)
    HYP.append(d)


# ------------------------------------------------------------------ helpers
def Bo(x):
    return x.reindex(grid).fillna(False).astype(bool)


ALWAYS = pd.Series(True, index=grid)
HM = pd.Series((grid + 1).month, index=grid)      # calendar month being HELD (decided at end of t)
HY = pd.Series((grid + 1).year, index=grid)
YR = pd.Series(grid.year, index=grid)
MO = pd.Series(grid.month, index=grid)


def hold(months, mod=None, years=None):
    c = HM.isin(months)
    if mod is not None:
        c &= (HY % 4 == mod)
    if years is not None:
        c &= HY.isin(years)
    return c


def keep(c, n):
    """True for n months starting with each month c is true."""
    return Bo(c).astype(float).rolling(n, min_periods=1).max().astype(bool)


def streak(c, n):
    return Bo(c).astype(int).rolling(n, min_periods=n).sum() >= n


def yy(x, n=12):
    return (x / x.shift(n) - 1) * 100


def ann(x, n=3):
    return ((x / x.shift(n)) ** (12 / n) - 1) * 100


def qtr(name, lag=4):
    return S[name].ffill(limit=2).shift(lag)


def pr(a):
    return lvl(R[a]).where(R[a].notna().cummax())


def ret(a, n):
    return mom(a, n)


def rel(a, b, n):
    return (1 + mom(a, n)) / (1 + mom(b, n)) - 1


def dd(a, n=12):
    p = pr(a)
    return p / p.rolling(n, min_periods=1).max() - 1


def slope_up(a, n=10):
    m = ma(pr(a), n)
    return m > m.shift(1)


def mx(c):
    return c.astype(float)


# ------------------------------------------------------------------ point-in-time series
SPX = pr("spx")
dd12 = SPX / SPX.rolling(12, min_periods=1).max() - 1
ddpk = SPX / SPX.cummax() - 1
spx_up = above_ma("spx").fillna(False)
gs2 = F["GS2"]
tb3 = S["fred_DTB3"]
y5 = (gs2 + gs10) / 2                                         # 5y yield proxy (DGS5 not in store)
ff12 = ff - ff.shift(12)
# core CPI: tool series (1998+) spliced with a services-less-energy / goods-less-food-energy proxy (published t+1)
_sas, _sac = S["fred_CUSR0000SASLE"], S["fred_CUSR0000SACL1E"]
core_yy = ind["core_cpi"].combine_first((0.7 * yy(_sas) + 0.3 * yy(_sac)).shift(1))
core3 = ann(F["CPILFESL"]).combine_first((0.7 * ann(_sas) + 0.3 * ann(_sac)).shift(1))
core_mom = core3 - core_yy
pce_yy = yy(F["PCEPILFE"])
pce3 = ann(F["PCEPILFE"])
cpi3 = ann(cpi).shift(1)
sahm = ind["jobs_alarm"]
curve = ind["curve"]
c103 = S["fred_T10Y3M"].combine_first(gs10 - tb3)
cape_p = sc["cape"]                                           # expanding percentile of CAPE (0-100)
realff = ff - core_yy
m2 = ind["m2"]
dlr12 = ind["dollar"]
vix = F["VIXCLS"]
baa = ind["baa"]
tp = F["THREEFYTP10"]
ngdp = (S["fred_GDPC1"] * S["fred_GDPDEF"] / 100).ffill(limit=2).shift(4)
deficit = -(S["fred_MTSDS133FMS"].rolling(12).sum().shift(1) / 1000) / ngdp * 100   # federal deficit, % of GDP
debt_gdp = qtr("fred_GFDEGDQ188S", 4)
tariff = qtr("fred_B235RC1Q027SBEA", 4) / qtr("fred_IMPGS", 4) * 100                 # customs / imports (G&S)
int_rcpt = qtr("fred_A091RC1Q027SBEA", 4) / qtr("fred_FGRECPT", 4) * 100
int_gdp = qtr("fred_A091RC1Q027SBEA", 4) / ngdp * 100
profits = qtr("fred_CPATAX", 5)
corpdebt = qtr("fred_BCNSDODNS", 6)
eps = S["sh_eps"].shift(6)
eps_up = (eps > eps.shift(3)).fillna(False)
eps_dn = (eps <= eps.shift(3)).fillna(False)
bankcred = S["fred_TOTBKCR"].shift(1)
jolts = S["fred_JTSJOL"].shift(2)
cshp = S["fred_CSUSHPINSA"].shift(3)
sloos_ci = qtr("fred_DRTSCILM", 2)
fdh = qtr("fred_FDHBFIN", 5)
cli_us = S["fred_USALOLITONOSTSAM"].shift(2)
prod = qtr("fred_OPHNFB", 5)
rgdp = qtr("fred_GDPC1", 4)
oilp = S["fred_MCOILWTICO"]
jp10 = S["fred_IRLTLT01JPM156N"].shift(1)
de10 = S["fred_IRLTLT01DEM156N"].shift(1)
boj = S["fred_IRSTCB01JPM156N"].shift(1)
reer_jp = S["fred_RBJPBIS"].shift(1)
reer_us = S["fred_RBUSBIS"].shift(1)
br_rate = S["fred_IRSTCI01BRM156N"].shift(1)
br_cpi = yy(S["fred_BRACPIALLMINMEI"]).shift(2)
br_reer = S["fred_RBBRBIS"].shift(1)
move = S["px_^MOVE"]
dfii10 = S["fred_DFII10"]
t10ie = S["fred_T10YIE"]
t5ie = S["fred_T5YIE"]
nfci = S["fred_NFCI"]
walcl = S["fred_WALCL"]
gbs = walcl + S["fred_ECBASSETSW"] * 1.15 + S["fred_JPNASSETS"].shift(1) * 100 / 130   # $m, constant FX
# ---- extra series from the raw research store (read only)
import os
import warnings
RD = "/home/claude/stock-screener/cache/macro/raw/research"
warnings.filterwarnings("ignore")


def _mon(dates, vals):
    s = pd.Series(pd.to_numeric(pd.Series(vals).values, errors="coerce"), index=pd.PeriodIndex(pd.to_datetime(dates), freq="M"))
    return s.groupby(level=0).last().reindex(grid)


def ycsv(name):
    d = pd.read_csv(os.path.join(RD, name + ".csv"))
    return _mon(d["date"], d["value"])


_g = pd.read_excel(os.path.join(RD, "gpr_index.xls"))
gpr = _mon(_g["month"], _g["GPR"]).shift(1)                                  # published early t+1
gpr_spike = (gpr >= gpr.rolling(12, min_periods=12).mean() + 2 * gpr.rolling(12, min_periods=12).std()).fillna(False)
_t = pd.read_excel(os.path.join(RD, "trade_epu.xlsx"), sheet_name="Indices")
_t = _t[pd.to_numeric(_t["Month"], errors="coerce").notna()]
tpu = _mon(pd.to_datetime(dict(year=_t["Year"].astype(int), month=_t["Month"].astype(int), day=1)), _t["9. Trade policy"]).shift(1)
_a = pd.read_excel(os.path.join(RD, "aaii_sentiment.xls"), sheet_name="SENTIMENT", header=None)
_a = _a[pd.to_datetime(_a[0], errors="coerce").notna() & pd.to_numeric(_a[6], errors="coerce").notna()]
aaii = _mon(pd.to_datetime(_a[0]), _a[6])                                    # bull-bear spread, last weekly reading
_s = pd.read_excel(os.path.join(RD, "nyfed_gscpi.xlsx"), sheet_name="GSCPI Monthly Data")
_s = _s[pd.to_datetime(_s["Date"], errors="coerce", format="%d-%b-%Y").notna()]
gscpi = _mon(pd.to_datetime(_s["Date"], format="%d-%b-%Y"), _s["GSCPI"]).shift(1)
_c = pd.read_csv(os.path.join(RD, "cftc_cot_selected.csv"), low_memory=False)
_c.columns = [c.strip() for c in _c.columns]
_c["nm"] = _c["Market and Exchange Names"].str.strip()


def cot(name):
    x = _c[_c["nm"] == name]
    L = pd.to_numeric(x["Noncommercial Positions-Long (All)"], errors="coerce")
    Sh = pd.to_numeric(x["Noncommercial Positions-Short (All)"], errors="coerce")
    OI = pd.to_numeric(x["Open Interest (All)"], errors="coerce")
    d = pd.DataFrame({"d": pd.to_datetime(x["As of Date in Form YYYY-MM-DD"]), "v": (L - Sh) / OI * 100}).sort_values("d")
    return _mon(d["d"], d["v"]).shift(1)


COT = {"gold": cot("GOLD - COMMODITY EXCHANGE INC."), "oil": cot("CRUDE OIL, LIGHT SWEET - NEW YORK MERCANTILE EXCHANGE"),
       "copper": cot("COPPER-GRADE #1 - COMMODITY EXCHANGE INC."), "silver": cot("SILVER - COMMODITY EXCHANGE INC.")}
bizd, bkln, psp = ycsv("Y_BIZD"), ycsv("Y_BKLN"), ycsv("Y_PSP")
sphb, splv = ycsv("Y_SPHB"), ycsv("Y_SPLV")
_d = pd.read_csv(os.path.join(RD, "D__GSPC.csv"), parse_dates=["date"]).set_index("date")["value"].dropna()


def _ddd(x, n=12):
    return x / x.rolling(n, min_periods=1).max() - 1


def _daily_flags():
    """January indicators from the daily S&P (1970+): Santa Claus rally, first five days, January."""
    out = {}
    yrs = sorted(set(_d.index.year))
    for y in yrs[1:]:
        dec = _d[(_d.index.year == y - 1) & (_d.index.month == 12)]
        jan = _d[(_d.index.year == y) & (_d.index.month == 1)]
        if len(dec) < 6 or len(jan) < 5:
            continue
        santa = jan.iloc[1] / dec.iloc[-6] - 1
        first5 = jan.iloc[4] / dec.iloc[-1] - 1
        janr = jan.iloc[-1] / dec.iloc[-1] - 1
        out[y] = (santa, first5, janr)
    return pd.DataFrame(out, index=["santa", "first5", "jan"]).T


JF = _daily_flags()


def year_val(col):
    """Value for the current calendar year, available from the end of January (t month >= 1)."""
    return pd.Series([JF[col].get(int(y), np.nan) for y in YR], index=grid)


def _macd_state():
    e12, e26 = _d.ewm(span=12, adjust=False).mean(), _d.ewm(span=26, adjust=False).mean()
    m = e12 - e26
    sg = m.ewm(span=9, adjust=False).mean()
    up = (m > sg).groupby(_d.index.to_period("M")).last().reindex(grid)
    out, st = [], False
    for t_, u in zip(grid, up.values):
        if t_.month in (4, 5, 6, 7, 8, 9) and u is not None and u == False:   # noqa: E712  sell on/after Apr 1
            st = True
        if t_.month in (10, 11, 12, 1, 2, 3) and u is not None and u == True:  # noqa: E712  buy on/after Oct 1
            st = False
        out.append(st)
    return pd.Series(out, index=grid)


def _rsi(x, n=14):
    dlt = x.diff()
    up = dlt.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    dn = (-dlt.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + up / dn)


def _rsi_div():
    r = _rsi(_d)
    hi = _d >= _d.rolling(252, min_periods=200).max()
    lo = _d <= _d.rolling(252, min_periods=200).min()
    bear, bull = pd.Series(False, index=_d.index), pd.Series(False, index=_d.index)
    last_hi = last_lo = None
    for i, dt in enumerate(_d.index):
        if hi.iloc[i]:
            if last_hi is not None and i - last_hi[0] > 20 and r.iloc[i] <= last_hi[1] - 10:
                bear.iloc[i] = True
            if last_hi is None or i - last_hi[0] > 20:
                last_hi = (i, r.iloc[i])
        if lo.iloc[i]:
            if last_lo is not None and i - last_lo[0] > 20 and r.iloc[i] > last_lo[1]:
                bull.iloc[i] = True
            if last_lo is None or i - last_lo[0] > 20:
                last_lo = (i, r.iloc[i])
    pm = _d.index.to_period("M")
    return (bear.groupby(pm).max().reindex(grid).fillna(False).astype(bool),
            bull.groupby(pm).max().reindex(grid).fillna(False).astype(bool),
            r.groupby(pm).last().reindex(grid), r.groupby(pm).max().reindex(grid))


RSI_BEAR, RSI_BULL, RSI_END, RSI_MAX = _rsi_div()
hot_core = (core_yy > 3).fillna(False)
xs5 = X5["gold"] + X5["commod"]                               # candidate-5 inflation sleeve share
TL = (g_l & curve_ok)                                         # months both books hold long Treasuries


def no_tlt(c, frac=1.0):
    """Overlay: drop (a share of) the long-Treasury leg -> T-bills while c holds."""
    return lambda: pd.DataFrame({"t30y": -frac * mx(Bo(c()) & TL) * (1 - xs5)})


def swap(c, to, frac=1.0):
    """Overlay: hold `to` instead of the long-Treasury leg while c holds."""
    def f():
        w = frac * mx(Bo(c()) & TL) * (1 - xs5)
        return pd.DataFrame({"t30y": -w, to: w})
    return f


def mk_overlay(c, w):
    return lambda: pd.DataFrame({a: v * mx(Bo(c())) for a, v in w.items()})


def OV(src, desc, c, w):
    H(src, desc, "overlay", c, weights=mk_overlay(c, w))


SEC = ["sec_" + k for k in P["rets"].columns]
CTRY = ["eq_japan", "eq_germany", "eq_uk", "eq_china", "eq_korea", "eq_hongkong", "eq_canada", "eq_australia",
        "eq_brazil", "eq_mexico", "eq_taiwan", "eq_india"]

# ================================================================== BATCH 1
s = "Cullen Roche - TIP486 Macro Investing"
H(s, "10y yield > 4%: hold 10y Treasuries instead of bills for the non-stock part", "defensive",
  lambda: Bo(gs10 > 4), asset="t10y")
H(s, "10y yield in top third of its 20y range: 10y Treasuries instead of bills", "defensive",
  lambda: Bo(gs10 >= gs10.rolling(240, min_periods=120).min() + 2 / 3 * (gs10.rolling(240, min_periods=120).max() - gs10.rolling(240, min_periods=120).min())), asset="t10y")
H(s, "10y yield < 1.5%: no long Treasuries (bills)", "overlay", lambda: Bo(gs10 < 1.5), weights=no_tlt(lambda: gs10 < 1.5))


def _brk():
    y = S["fred_DGS30"].combine_first(gs10) / 100
    dmod = (1 / y) * (1 - (1 + y / 2) ** (-60))                # par 30y bond modified duration
    return y * 100 / dmod


H(s, "30y breakeven yield rise (yield/duration) > 0.75 pt: long Treasuries for the non-stock part", "defensive",
  lambda: Bo(_brk() > 0.75), asset="t30y")
H(s, "30y breakeven yield rise < 0.25 pt: drop long Treasuries for bills", "overlay", lambda: Bo(_brk() < 0.25),
  weights=no_tlt(lambda: _brk() < 0.25))
H(s, "Fed funds < 0.5% and 10y < 2%: cap long Treasuries at 25% of the de-risk leg", "overlay",
  lambda: Bo((ff < 0.5) & (gs10 < 2)), weights=no_tlt(lambda: (ff < 0.5) & (gs10 < 2), 0.75))
H(s, "Short Treasuries (2y) instead of long Treasuries in the de-risk leg, always", "overlay", lambda: ALWAYS,
  weights=swap(lambda: ALWAYS, "t2y"))
H(s, "TIPS for the non-stock part in hot inflation (tool hot flag)", "defensive", lambda: Bo(P["hot"]), asset="tips")
H(s, "Earnings yield (1/CAPE) below T-bill yield: stocks capped at 50%", "cut",
  lambda: Bo(100 / ind["cape"] - tb3 < 0), level=0.5)
H(s, "S&P 25%+ below its peak: re-enter stocks (no cuts)", "block", lambda: Bo(ddpk <= -0.25))
H(s, "Liquidity bucket: keep 10% in bills always (stocks capped at 90%)", "cut", lambda: ALWAYS, level=0.9)
H(s, "Ex-US beats S&P over 12m and 10y ex-US relative return in bottom fifth: 50% of equity ex-US", "location",
  lambda: Bo((mom("intl_eq", 12) > mom("spx", 12)) & (pctl(rel("intl_eq", "spx", 120)) <= 20)), assets=["intl_eq"])
H(s, "Ex-US beats S&P over 12m (momentum only): 50% of equity ex-US", "location",
  lambda: Bo(mom("intl_eq", 12) > mom("spx", 12)), assets=["intl_eq"])
H(s, "10y yield up > 1 pt in 12m: 50% of equity in value", "location", lambda: Bo(ind["y10_chg"] > 1), assets=["value"])
H(s, "Stock-bond correlation > 0 and core CPI > 4%: commodities instead of bills in the de-risk part", "defensive",
  lambda: Bo((ind["stockbond"] > 0) & (core_yy > 4)), asset="commod")
H(s, "Dollar falling (12m change < 0): gold instead of bills in the de-risk part", "defensive",
  lambda: Bo(dlr12 < 0), asset="gold")
H(s, "Inverted curve (10y-2y < 0): 10y Treasuries for the non-stock part", "defensive", lambda: Bo(curve < 0), asset="t10y")
H(s, "Inverted curve (10y-2y < 0): stocks capped at 50% (Druckenmiller 'red' too)", "cut", lambda: Bo(curve < 0), level=0.5)
H(s, "Deficit/GDP widens > 2 pts in 12m: stay in stocks (no cuts)", "block", lambda: Bo(deficit - deficit.shift(12) > 2))
H(s, "Deficit/GDP widens > 2 pts in 12m: 10% commodities", "sleeve", lambda: Bo(deficit - deficit.shift(12) > 2), asset="commod")
H(s, "Bank credit 6m annualised growth < 0: stocks to 0", "cut", lambda: Bo(ann(bankcred, 6) < 0))
H(s, "Bank credit y/y < 0: stocks to 0", "cut", lambda: Bo(yy(bankcred) < 0))
H(s, "Bank stocks 3m rel < -20% and Fed balance sheet 3m > +5% (emergency liquidity proxy): re-enter for 3m", "block",
  lambda: keep(keep(rel("sec_KBE", "spx", 3) < -0.20, 3) & (yy(walcl, 3) > 5), 3))

s = "Kyle Bass - Hoover Global Macro"
H(s, "Case-Shiller home prices y/y < 0 (bank-leverage leg missing): stocks to 0", "cut", lambda: Bo(yy(cshp) < 0))
OV(s, "BoJ at zero (basic loan rate <= 0.3%) and JGB 10y < 0.5% (capped yields; debt/GDP > 200% throughout): short yen 10%",
   lambda: (boj <= 0.3) & (jp10 < 0.5), {"jpy": -0.1})
H(s, "Deficit > 6% of GDP outside recession, debt/GDP rising: 10% gold", "sleeve",
  lambda: Bo((deficit > 6) & ~unr_up & (debt_gdp > debt_gdp.shift(12))), asset="gold")
H(s, "Deficit > 6% of GDP outside recession, debt/GDP rising: 10% commodities", "sleeve",
  lambda: Bo((deficit > 6) & ~unr_up & (debt_gdp > debt_gdp.shift(12))), asset="commod")
H(s, "US CPI > 4% and dollar up 12m: 50% of equity in commodity exporters (Brazil, Canada, Australia)", "location",
  lambda: Bo((cpi_yy > 4) & (dlr12 > 0)), assets=["eq_brazil", "eq_canada", "eq_australia"])
H(s, "Deficit > 6% of GDP at full employment (unemployment < 5%): 2y instead of long Treasuries", "overlay",
  lambda: Bo((deficit > 6) & (unr < 5)), weights=swap(lambda: (deficit > 6) & (unr < 5), "t2y"))

s = "Jeffrey Hirsch - Eisman Playbook Ep56"
H(s, "Midterm year Aug-Oct with S&P 10%+ below 12m high: re-enter (no cuts)", "block",
  lambda: Bo(hold([8, 9, 10], 2) & (dd12 <= -0.10)))
H(s, "Midterm Oct through pre-election Dec: no cuts", "block",
  lambda: Bo(hold([10, 11, 12], 2) | (HY % 4 == 3)))
H(s, "Sweet spot (Q4 midterm to Q2 pre-election): no cuts", "block",
  lambda: Bo(hold([10, 11, 12], 2) | hold([1, 2, 3, 4, 5, 6], 3)))
H(s, "Weak spot Q2-Q3 of midterm year: stocks capped at 50%", "cut", lambda: Bo(hold([4, 5, 6, 7, 8, 9], 2)), level=0.5)
H(s, "Pre-election year: no cuts", "block", lambda: Bo(HY % 4 == 3))
H(s, "Best six months: out of stocks May-Oct", "cut", lambda: Bo(hold([5, 6, 7, 8, 9, 10])), level=0.0)
H(s, "Best six months: stocks capped at 50% May-Oct", "cut", lambda: Bo(hold([5, 6, 7, 8, 9, 10])), level=0.5)
H(s, "Macro cuts act only May-Oct (no cuts Nov-Apr)", "block", lambda: Bo(hold([11, 12, 1, 2, 3, 4])))
H(s, "Nasdaq best eight months: 50% of equity in Nasdaq-100 Nov-Jun", "location",
  lambda: Bo(hold([11, 12, 1, 2, 3, 4, 5, 6])), assets=["ndx"])
H(s, "Best three months Nov-Jan: no cuts", "block", lambda: Bo(hold([11, 12, 1])))
H(s, "September: stocks capped at 50%", "cut", lambda: Bo(hold([9])), level=0.5)
H(s, "Utilities Mar-Oct: 25% of equity in utilities", "location", lambda: Bo(hold([3, 4, 5, 6, 7, 8, 9, 10])),
  assets=["sec_XLU"], s=0.25)
H(s, "Copper and energy seasonal (Jan-Apr): 25% of equity in energy stocks + copper", "location",
  lambda: Bo(hold([1, 2, 3, 4])), assets=["sec_XLE", "copper"], s=0.25)
H(s, "Best six months only with confirmation: out May-Oct if S&P below 10m avg or Fed tightening", "cut",
  lambda: Bo(hold([5, 6, 7, 8, 9, 10]) & (trend_dn | fed)))
H(s, "Dead September reverse barometer (control): September up -> stocks 50% Oct-Dec", "cut",
  lambda: Bo(hold([10, 11, 12]) & (R["spx"].where(MO == 9).groupby(YR).transform("max") > 0)), level=0.5)
_jan = R["spx"].where(MO == 1).groupby(YR).transform("max")
H(s, "January barometer: January down -> stocks capped at 50% Feb-Dec", "cut",
  lambda: Bo((MO <= 11) & (_jan < 0)), level=0.5)
H(s, "January barometer: January down -> macro warnings acted on Feb-Dec", "gate", lambda: Bo((MO <= 11) & (_jan < 0)))
H(s, "Small caps mid-Dec to Jan: 50% of equity in small caps Dec-Jan", "location", lambda: Bo(hold([12, 1])), assets=["small"])
H(s, "Small caps Nov-Jan: 50% of equity in small caps", "location", lambda: Bo(hold([11, 12, 1])), assets=["small"])


def _nov_jan_neg():
    r3 = (1 + R["spx"]).rolling(3).apply(np.prod, raw=True) - 1          # Nov-Jan return, known end of Jan
    v = r3.where(MO == 1).groupby(YR).transform("max")
    return (MO >= 4) & (MO <= 9) & (v < 0)


H(s, "Failed seasonal rally: Nov-Jan down -> stocks capped at 50% May-Oct", "cut", lambda: Bo(_nov_jan_neg()), level=0.5)


def _superboom():
    rl = SPX / cpi.shift(1)
    trig = (rl / rl.shift(120) - 1 < 0) & (cpi_yy.rolling(120, min_periods=60).max() > 6)
    return keep(trig, 120)


H(s, "Super boom: within 10y of a negative 10y real S&P return after CPI > 6%: no cuts", "block", lambda: _superboom())
H(s, "Trump-era seasonal: no cuts Apr-Dec in Trump years", "block",
  lambda: Bo(hold(list(range(4, 13)), years=[2017, 2018, 2019, 2020, 2025, 2026])))
H("Steve Eisman - Eisman Playbook Ep56", "BDCs (BIZD) 15%+ below 12m high or SLOOS C&I net tightening > 20%: stocks capped at 50%",
  "cut", lambda: Bo((sloos_ci > 20) | (_ddd(bizd) <= -0.15)), level=0.5)

s = "Stanley Druckenmiller - Sohn 2023"
_low = (ff.rolling(36, min_periods=36).max() < 2).fillna(False)
H(s, "Fed funds < 2% for 3+ years and CAPE top decile: stocks capped at 60%", "cut",
  lambda: Bo(_low & (cape_p >= 90)), level=0.6)
H(s, "After 3y+ of sub-2% rates, CAPE top decile and Fed hiking (12m > +1 pt): stocks to 0", "cut",
  lambda: Bo(keep(_low, 36) & (cape_p >= 90) & (ff12 > 1)))


def _core_at_start():
    v, out = ff.values, np.full(T, np.nan)
    cv = core_yy.values
    for t in range(24, T):
        w = v[t - 23:t + 1]
        if np.isnan(w).all():
            continue
        j = t - 23 + (len(w) - 1 - int(np.nanargmin(w[::-1])))        # last month at the 24m low = cycle start
        out[t] = cv[j]
    return pd.Series(out, index=grid)


_cs = _core_at_start()
H(s, "Reactive hiking (Fed funds +3 pts in 12m, began with core CPI > 4%): stocks to 0 for 12m", "cut",
  lambda: keep((ff12 > 3) & (_cs > 4), 12))
H(s, "Proactive hiking (began with core CPI < 2.5%): no cuts while the Fed gate is on", "block",
  lambda: Bo(fed & (_cs < 2.5)))
H(s, "Truck freight y/y < 0 for 3 months: stocks capped at 50%", "cut", lambda: streak(ind["truck"] < 0, 3), level=0.5)
H(s, "In a cut, homebuilders beat S&P over 3m (months' supply leg missing): re-enter", "block",
  lambda: Bo((e41 < 1) & (rel("sec_ITB", "spx", 3) > 0)))
H(s, "Regional banks fall > 25% vs S&P over 3m: stocks to 0", "cut", lambda: Bo(rel("sec_KRE", "spx", 3) < -0.25))
H(s, "Fed funds minus 5y yield 3y earlier > 2 pts and banks lagging: stocks capped at 50%", "cut",
  lambda: Bo((ff - y5.shift(36) > 2) & (ind["banks"] < 0)), level=0.5)
H(s, "Fed cutting while core CPI > 3% (Burns): 10% commodities for 24m", "sleeve",
  lambda: keep((ff - ff.shift(6) < 0) & (core_yy > 3), 24), asset="commod")
H(s, "Fed cutting while core CPI > 3% (Burns): 10% gold for 24m", "sleeve",
  lambda: keep((ff - ff.shift(6) < 0) & (core_yy > 3), 24), asset="gold")
H(s, "Bust after bubble: S&P 30%+ off peak, CAPE was top decile, Baa spread +1 pt in 6m: long Treasuries", "defensive",
  lambda: Bo((ddpk <= -0.30) & (cape_p.rolling(24, min_periods=1).max() >= 90) & (ind["baa_chg"] > 1)), asset="t30y")
H(s, "Breakdown from top-decile CAPE with core inflation not falling: commodities instead of bills", "defensive",
  lambda: Bo(trend_dn & (cape_p.rolling(12, min_periods=1).max() >= 90) & (core_mom >= 0)), asset="commod")
H(s, "Breakdown from top-decile CAPE with core inflation not falling: energy stocks instead of bills", "defensive",
  lambda: Bo(trend_dn & (cape_p.rolling(12, min_periods=1).max() >= 90) & (core_mom >= 0)), asset="sec_XLE")
H(s, "After a recession signal, Fed cutting and copper 6m up: 50% of equity in metals & mining", "location",
  lambda: Bo(keep(sahm >= 0.5, 24) & (ff12 < -1) & (ind["copper"] > 0)),
  assets=["sec_XME"])
H(s, "Foreign official Treasury holdings falling y/y and deficit > 5%: 10% gold", "sleeve",
  lambda: Bo((yy(fdh) < 0) & (deficit > 5)), asset="gold")
H(s, "Fat pitch: in any cut with 10y >= Fed funds, long Treasuries for the non-stock part", "defensive",
  lambda: Bo((e41 < 1) & (gs10 >= ff)), asset="t30y")
H(s, "Deep inversion (10y < Fed funds - 1 pt): bills, not long Treasuries", "overlay", lambda: Bo(gs10 < ff - 1),
  weights=no_tlt(lambda: gs10 < ff - 1))
H(s, "2y < 0.5% and M2 y/y > 10%: no long Treasuries", "overlay", lambda: Bo((gs2 < 0.5) & (m2 > 10)),
  weights=no_tlt(lambda: (gs2 < 0.5) & (m2 > 10)))
OV(s, "2y < 0.5% and M2 y/y > 10%: short 2y Treasuries 10%", lambda: (gs2 < 0.5) & (m2 > 10), {"t2y": -0.1})
_dials = mx(fed) + mx(share > 0.25) + mx(trend_dn)
H(s, "Mixed dials (1-2 of Fed tight / warnings / trend down): stocks capped at 50%", "cut",
  lambda: Bo((_dials >= 1) & (_dials <= 2)), level=0.5)
H(s, "All three dials agree (Fed tight, warnings > 25%, trend down): stocks to 0", "cut", lambda: Bo(_dials >= 3))


def _ddlimit():
    r = REF["live"].fillna(0)
    lv_ = (1 + r).cumprod()
    d = (lv_ / lv_.cummax() - 1).values
    on, out = False, []
    for v in d:
        on = (v < -0.15) or (on and v < -0.075)
        out.append(on)
    return pd.Series(out, index=grid)


H(s, "Portfolio drawdown > 15% (live book): stocks capped at 50% until back within 7.5%", "cut", lambda: _ddlimit(), level=0.5)
_dsh = lambda: (deficit > 5) & ~unr_up & (gs2 < ff - 0.5)
OV(s, "Deficit > 5% outside recession and 2y < Fed funds - 0.5: short dollar 10%", _dsh, {"usd": -0.1})
H(s, "Deficit > 5% outside recession and 2y < Fed funds - 0.5: 50% of equity ex-US", "location", lambda: Bo(_dsh()),
  assets=["intl_eq"])
H(s, "Foreign official Treasury holdings down > 3% y/y: 10% gold", "sleeve", lambda: Bo(yy(fdh) < -3), asset="gold")
H(s, "Federal interest > 20% of receipts: no long Treasuries", "overlay", lambda: Bo(int_rcpt > 20),
  weights=no_tlt(lambda: int_rcpt > 20))
H(s, "Federal interest > 20% of receipts: 10% gold", "sleeve", lambda: Bo(int_rcpt > 20), asset="gold")


def _fiscal_space():
    rec = keep(sahm >= 0.5, 12)
    two_up = spx_up & spx_up.shift(1).fillna(False)
    return Bo(rec & (debt_gdp > 100) & (deficit > 5) & ~two_up)


H(s, "Recession with debt > 100% and deficit > 5% (also Brende): out until S&P above 10m avg 2 months", "cut",
  lambda: _fiscal_space())
H(s, "CAPE top decile and profit margin top decile: macro warnings acted on", "gate",
  lambda: Bo((cape_p >= 90) & (pctl(profits / ngdp) >= 90)))


def _stag_mom():
    mo6 = pd.DataFrame({c: mom(c, 6) for c in SEC})
    rk = mo6.rank(axis=1, ascending=False)
    on = Bo((P["stage"] != "expansion") & (core_yy > 3)) & (e41 > 0.99) & (e5 > 0.99)
    w = (rk <= 3).astype(float) * 0.5 / 3
    w = w.mul(on.astype(float), axis=0)
    w["spx"] = -0.5 * on.astype(float)
    return w


H(s, "Flat/stagflation (core CPI > 3%, not expansion): half the equity in the top 3 sectors by 6m momentum",
  "overlay", lambda: Bo((P["stage"] != "expansion") & (core_yy > 3) & (e41 > 0.99) & (e5 > 0.99)), weights=_stag_mom)
H(s, "Tech fell 40%+ and Nasdaq-100 back above 10m avg: 50% of equity in Nasdaq-100", "location",
  lambda: Bo(keep(dd("ndx", 36) <= -0.40, 24) & above_ma("ndx")), assets=["ndx"])
H(s, "Biotech 4y relative return in bottom decile and above 10m avg: 20% of equity in biotech", "location",
  lambda: Bo((pctl(rel("sec_XBI", "spx", 48)) <= 10) & above_ma("sec_XBI")), assets=["sec_XBI"], s=0.2)
H(s, "Volcker: after a recession with real Fed funds > 3 pts, no cuts for 5 years", "block",
  lambda: Bo(keep((realff > 3) & (sahm >= 0.5), 60) & (sahm < 0.5)))
H(s, "Japan route: after a recession, real Fed funds < 0: stocks capped at 50%", "cut",
  lambda: Bo(keep(sahm >= 0.5, 24) & (sahm < 0.5) & (realff < 0)), level=0.5)

H("Mike Pompeo - Money Maze", "Breaks are unforecastable: 5% gold always", "sleeve", lambda: ALWAYS, asset="gold", w=0.05)

s = "Pablo Calderini - New World Order"
H(s, "Core CPI > 3% (no Fed put; also Roche, Jones, van Eck, Cohen): no long Treasuries", "overlay", lambda: hot_core,
  weights=no_tlt(lambda: hot_core))
H(s, "Core CPI > 3%: 10% trend-following", "sleeve", lambda: hot_core, asset="trend")
H(s, "Core CPI > 3% and S&P below 10m avg: stocks to 0 (re-entry needs trend repair)", "cut", lambda: Bo(hot_core & trend_dn))
H(s, "Hiking surprise: Fed funds > 2y yield of 12m earlier + 1 pt: stocks to 0", "cut", lambda: Bo(ff - gs2.shift(12) > 1))
H(s, "Hikes > 3 pts within 18 months: stocks to 0 for 12m", "cut", lambda: keep(ff - ff.rolling(18, min_periods=12).min() >= 3, 12))
H(s, "Headline-only inflation spike (headline - core > 2, core stable): no cuts", "block",
  lambda: Bo((cpi_yy - core_yy > 2) & ((core_yy - core_yy.shift(6)).abs() < 0.5)))
H(s, "Deflation regime: core CPI < 1.5% and rising: no cuts", "block", lambda: Bo((core_yy < 1.5) & (core_mom > 0)))
H(s, "Core CPI > 3%: gold instead of long Treasuries", "overlay", lambda: hot_core, weights=swap(lambda: hot_core, "gold"))
H(s, "Long-run equity vol ~21%: vol target 10% -> stocks capped at 50% always", "cut", lambda: ALWAYS, level=0.5)
H(s, "20% cross-asset trend-following always", "sleeve", lambda: ALWAYS, asset="trend", w=0.2)
H(s, "10% own-built trend (long/short) always", "sleeve", lambda: ALWAYS, asset="trend_ls", w=0.1)
H(s, "MOVE > 150: halve long Treasuries", "overlay", lambda: Bo(move > 150), weights=no_tlt(lambda: move > 150, 0.5))
H(s, "Wrong quadrant: EPS 6m down, CAPE top third, real 10y > 1%: stocks capped at 50%", "cut",
  lambda: Bo((eps < eps.shift(6)) & (cape_p >= 67) & (ind["realyield"] > 1)), level=0.5)
H(s, "Market prices cuts (2y < FF - 0.5) while core CPI 3m annualised > 4%: stocks capped at 50%", "cut",
  lambda: Bo((gs2 < ff - 0.5) & (core3 > 4)), level=0.5)
OV(s, "German minus US 10y (2y proxy) up > 0.3 pt in 3m: long euro 10%",
   lambda: ((de10 - gs10) - (de10 - gs10).shift(3)) > 0.3, {"eur": 0.1})
OV(s, "Yen REER bottom decile and JGB 10y +0.2 pt in 3m: long yen 10%",
   lambda: (pctl(reer_jp) <= 10) & (jp10 - jp10.shift(3) > 0.2), {"jpy": 0.1})
H(s, "Real 10y yield down > 0.25 pt in 3m: 10% gold", "sleeve", lambda: Bo(dfii10 - dfii10.shift(3) < -0.25), asset="gold")
H(s, "10y breakeven up > 0.25 pt in 3m with nominal 10y flat: 10% gold", "sleeve",
  lambda: Bo((t10ie - t10ie.shift(3) > 0.25) & ((gs10 - gs10.shift(3)).abs() < 0.25)), asset="gold")
H(s, "Quant macro (trend+value+carry+fundamentals): 20% AQR multi-style macro always", "sleeve", lambda: ALWAYS,
  asset="aqr_all_macro_multi_style", w=0.2)

s = "Pablo Calderini - Resilient Strategies"
H(s, "Core PCE < 2.5% and S&P 10%+ off 12m high: buy the dip (no cuts)", "block", lambda: Bo((pce_yy < 2.5) & (dd12 <= -0.10)))
H(s, "Core PCE > 3% and S&P below 10m avg: stocks to 0", "cut", lambda: Bo((pce_yy > 3) & trend_dn))
H(s, "Dovish pivot (2y -0.5 pt in 3m) with Sahm off: no cuts for 6m", "block",
  lambda: keep((gs2 - gs2.shift(3) < -0.5) & (sahm < 0.5), 6))
H(s, "Recessionary pivot (2y -0.5 pt in 3m) with Sahm on: stocks to 0", "cut", lambda: Bo((gs2 - gs2.shift(3) < -0.5) & (sahm >= 0.5)))
H(s, "Core PCE 3m annualised > 4% after core PCE was < 3%: stocks capped at 50% for 6m", "cut",
  lambda: keep((pce3 > 4) & (pce_yy.rolling(12, min_periods=1).min() < 3), 6), level=0.5)
H(s, "Strong earnings (EPS y/y > 10%) with CAPE high: valuation not a sell (no cuts)", "block",
  lambda: Bo((yy(eps) > 10) & (cape_p >= 80)))
H(s, "Fast rally (S&P 6m > 20%) with low VIX (< 15): 2% VIX futures as a hedge", "sleeve",
  lambda: Bo((ret("spx", 6) > 0.20) & (vix < 15)), asset="vix_fut", w=0.02)
H(s, "Core CPI > 3%: trend-following instead of bills for the non-stock part", "defensive", lambda: hot_core, asset="trend")
H(s, "2022 template: core CPI > 4% and real Fed funds < 0: stocks capped at 50%", "cut",
  lambda: Bo((core_yy > 4) & (realff < 0)), level=0.5)
OV(s, "2022 template: core CPI > 4% and real Fed funds < 0: long dollar 10%", lambda: (core_yy > 4) & (realff < 0), {"usd": 0.1})
OV(s, "Steepener: market expects cuts (2y < FF) and deficit > 5%: long 2y / short long Treasuries 10%",
   lambda: (gs2 < ff) & (deficit > 5), {"t2y": 0.1, "t30y": -0.1})
H(s, "Central banks in action (|Fed funds 12m change| > 1.5): extra 10% trend-following", "sleeve",
  lambda: Bo(ff12.abs() > 1.5), asset="trend")
H(s, "Narrow market (equal weight lags cap weight > 10% in 12m) and chips 25%+ off high: stocks to 0", "cut",
  lambda: Bo((ret("eqw", 12) - ret("spx", 12) < -0.10) & (ind["chips_break"] < -25)))
H("Former Norwegian PM - What is the fiscal rule", "Commodities +20% in 12m and still rising (3m): 50% of equity in "
  "no-fiscal-rule exporters (Brazil, South Africa)", "location",
  lambda: Bo((ret("commod", 12) > 0.20) & (ret("commod", 3) > 0)), assets=["eq_brazil", "eq_s_africa"])

# ================================================================== BATCH 2
s = "Brad Gerstner - BG2 Ep14"
H(s, "Skew unfavourable (S&P at a high after 6m +15%, EPS not rising, no cuts priced): stocks capped at 30%", "cut",
  lambda: Bo((ddpk >= -0.01) & (ret("spx", 6) >= 0.15) & eps_dn & (gs2 >= ff)), level=0.3)
H(s, "Skew favourable (S&P 15%+ off high, EPS rising, cuts priced): no cuts", "block",
  lambda: Bo((dd12 <= -0.15) & eps_up & (gs2 < ff)))
H(s, "S&P at a 12m high with 6m return >= 25%: stocks capped at 50% for 3m", "cut",
  lambda: keep((dd12 >= -0.001) & (ret("spx", 6) >= 0.25), 3), level=0.5)
H(s, "Nasdaq-100 at a 12m high with 6m return >= 33%: stocks capped at 50% for 3m", "cut",
  lambda: keep((dd("ndx") >= -0.001) & (ret("ndx", 6) >= 0.33), 3), level=0.5)
H(s, "Fiscal tightening (deficit/GDP down >= 0.5 pt over 12m, trailing): stocks capped at 50%", "cut",
  lambda: Bo(deficit - deficit.shift(12) <= -0.5), level=0.5)
H(s, "Sahm rule >= 0.5: stocks to 0", "cut", lambda: Bo(sahm >= 0.5))
H(s, "JOLTS openings below 12m avg for 6 months: macro warnings acted on", "gate",
  lambda: streak(jolts < jolts.rolling(12).mean(), 6))
H(s, "Real 10y >= 1.5% and Sahm >= 0.3: 10% 10y Treasuries", "sleeve", lambda: Bo((dfii10 >= 1.5) & (sahm >= 0.3)), asset="t10y")
H(s, "Fed funds >= 10y + 1 pt: 10% 10y Treasuries", "sleeve", lambda: Bo(ff - gs10 >= 1), asset="t10y")
H(s, "Real Fed funds at 24m high, core disinflating, unemployment rising: 10% 2y Treasuries", "sleeve",
  lambda: Bo((realff >= realff.rolling(24, min_periods=12).max() - 0.05) & (core_mom < 0) & unr_up), asset="t2y")


def _first_cut():
    mx12 = ff.rolling(12, min_periods=6).max()
    on = (ff <= mx12 - 0.25).fillna(False)
    hikes = (mx12 - ff.rolling(36, min_periods=12).min()) >= 0.5
    return on & ~on.shift(1).fillna(False) & hikes


_rflag = (sahm >= 0.5) | (curve.rolling(12, min_periods=1).min() < 0)
H(s, "First Fed cut with recession flag (Sahm or recent inversion): stocks to 0 for 6m", "cut",
  lambda: keep(_first_cut() & _rflag, 6))
H(s, "First Fed cut without recession flag (insurance cut): no cuts for 6m", "block",
  lambda: keep(_first_cut() & ~_rflag, 6))
H(s, "Emergency/large cut (Fed funds monthly average down >= 0.45 pt): stocks capped at 50% for 6m", "cut",
  lambda: keep(ff.diff() <= -0.45, 6), level=0.5)
H(s, "Yen surge >= 7% in a month after a 2y yen decline (carry unwind) or BoJ hike: stocks capped at 50% for 2m", "cut",
  lambda: keep(((R["jpy"] >= 0.07) & (mom("jpy", 24) < 0)) | (boj - boj.shift(1) > 0.05), 2), level=0.5)
OV(s, "US-Japan 10y gap (2y proxy) >= 4 pts and narrowing 0.5 pt in 3m: long yen 10%",
   lambda: ((gs10 - jp10) >= 4) & ((gs10 - jp10) - (gs10 - jp10).shift(3) <= -0.5), {"jpy": 0.1})
H(s, "Geopolitical spike (GPR) with oil +20% in a month: stocks capped at 50%", "cut",
  lambda: Bo((gpr_spike | gpr_spike.shift(1).fillna(False)) & (oilp / oilp.shift(1) - 1 >= 0.20)), level=0.5)
H(s, "Geopolitical spike (GPR) with oil +20% in a month: 20% of equity in energy stocks", "location",
  lambda: Bo((gpr_spike | gpr_spike.shift(1).fillna(False)) & (oilp / oilp.shift(1) - 1 >= 0.20)), assets=["sec_XLE"], s=0.2)
H(s, "S&P YTD >= +15% and warning share up since December: stocks capped at 50%", "cut",
  lambda: Bo((SPX / SPX.where(MO == 12).ffill().shift(1) - 1 >= 0.15) & (share > share.where(MO == 12).ffill().shift(1))), level=0.5)
OV(s, "Semis 12m return >= 100% (air pocket): short semis 10%", lambda: ret("sec_SMH", 12) >= 1.0, {"sec_SMH": -0.1})
H(s, "Within 3 months of a presidential election with stocks at a 12m high: stocks capped at 50%", "cut",
  lambda: Bo(hold([8, 9, 10], 0) & (dd12 >= -0.02)), level=0.5)
H(s, "Card delinquencies +1 pt in 12m: macro warnings acted on", "gate", lambda: Bo(ind["cards"] >= 1))

s = "Chris Jones - Graham Completion Portfolios"
H(s, "Fed hiking (12m >= +1) and core CPI >= 3%: no long Treasuries", "overlay", lambda: Bo((ff12 >= 1) & (core_yy >= 3)),
  weights=no_tlt(lambda: (ff12 >= 1) & (core_yy >= 3)))


def _corr24():
    a, b = R["spx"] - rf, R["t10y"] - rf
    return a.rolling(24, min_periods=24).corr(b)


H(s, "24m stock-bond correlation > +0.2: no long Treasuries", "overlay", lambda: Bo(_corr24() > 0.2),
  weights=no_tlt(lambda: _corr24() > 0.2))
H("Judy Posnikoff - Graham Completion Portfolios", "CPI >= 4% and rising (3m > 12m): stocks capped at 50%", "cut",
  lambda: Bo((cpi_yy >= 4) & (cpi3 > cpi_yy)), level=0.5)
H("Judy Posnikoff - Graham Completion Portfolios", "CPI >= 4% and rising: 10% commodities", "sleeve",
  lambda: Bo((cpi_yy >= 4) & (cpi3 > cpi_yy)), asset="commod")
_infl_state = lambda: Bo(P["hot"] & (P["stage"] != "recovery"))            # overheating (hot+expansion/late) or stagflation (hot+contraction)
H("Judy Posnikoff - Graham Completion Portfolios", "Overheating or stagflation state (hot flag): 10% gold", "sleeve",
  _infl_state, asset="gold")
H("Judy Posnikoff - Graham Completion Portfolios", "Overheating or stagflation state (hot flag): 10% TIPS", "sleeve",
  _infl_state, asset="tips")
H("Judy Posnikoff - Graham Completion Portfolios", "CPI > 3%: 20% trend-following", "sleeve", lambda: Bo(cpi_yy > 3),
  asset="trend", w=0.2)
H("Judy Posnikoff - Graham Completion Portfolios", "Core inflation rising (3m > 12m): 20% of equity in energy", "location",
  lambda: Bo(core_mom > 0), assets=["sec_XLE"], s=0.2)

s = "Todd Sohn - Eisman Playbook Ep66"
H(s, "S&P 10m average slope <= 0: stocks to 0", "cut", lambda: Bo(~slope_up("spx")))


def _laggards():
    on = dd12 >= -0.005
    cols = {}
    for c in SEC:
        cols[c] = -0.05 * mx(Bo(on & (dd(c) <= -0.10) & ~slope_up(c)))
    w = pd.DataFrame(cols)
    tot = w.sum(axis=1).abs()
    return w.mul(np.minimum(1.0, 0.2 / tot.replace(0, np.nan)).fillna(1.0), axis=0)


H(s, "S&P at a 12m high: short 5% each sector 10%+ below its high with falling 10m avg (max 20%)", "overlay",
  lambda: Bo(dd12 >= -0.005), weights=_laggards)
OV(s, "Semis vs staples 12m in top 5% and semis 10m avg turning down: long staples / short semis 10%",
   lambda: (pctl(rel("sec_SMH", "sec_XLP", 12)) >= 95) & ~slope_up("sec_SMH"), {"sec_XLP": 0.1, "sec_SMH": -0.1})


def _cycdef3():
    cy = pd.concat([mom(c, 3) for c in ["sec_XLI", "sec_XLB", "sec_XRT", "sec_KBE"]], axis=1).mean(axis=1)
    de = pd.concat([mom(c, 3) for c in ["sec_XLE", "sec_XLP", "sec_XLU", "sec_XLV"]], axis=1).mean(axis=1)
    return pctl(cy - de)


H(s, "Cyclicals vs defensives 3m in bottom fifth (contrarian): no cuts", "block", lambda: Bo(_cycdef3() <= 20))
H(s, "Cyclicals vs defensives 3m in bottom fifth (risk appetite weak): stocks capped at 50%", "cut",
  lambda: Bo(_cycdef3() <= 20), level=0.5)
H(s, "Equal-weight retail (XRT proxy for EW discretionary) 6m vs S&P in bottom decile: warnings acted on", "gate",
  lambda: Bo(pctl(rel("sec_XRT", "spx", 6)) <= 10))
H(s, "Small caps vs S&P 3y in bottom decile (outflow proxy): 50% of equity in small caps", "location",
  lambda: Bo(pctl(rel("small", "spx", 36)) <= 10), assets=["small"])
H(s, "Tech concentration (NDX/S&P 5y rel top fifth) and Nasdaq 10m avg falling: 20% of equity in REITs", "location",
  lambda: Bo((pctl(rel("ndx", "spx", 60)) >= 80) & ~slope_up("ndx")), assets=["sec_IYR"], s=0.2)
_gh = lambda: Bo((dfii10 - dfii10.shift(3) > 0.3) & (yy(S["px_DX-Y.NYB"], 3) > 2))
H(s, "Real 10y +0.3 pt and dollar index +2% in 3m: no gold (drops the c5 gold sleeve; short gold in live)", "overlay",
  _gh, weights=lambda: pd.DataFrame({"gold": -X5["gold"] * mx(_gh())}))
H(s, "Gold blow-off (12m > +40%): no gold (drops the c5 gold sleeve; short gold in live)", "overlay",
  lambda: Bo(ret("gold", 12) > 0.40), weights=lambda: pd.DataFrame({"gold": -X5["gold"] * mx(Bo(ret("gold", 12) > 0.40))}))
H(s, "VIX > 30: 20% of equity in staples", "location", lambda: Bo(vix > 30), assets=["sec_XLP"], s=0.2)

s = "Stanley Druckenmiller - Bloomberg Dec 2018"


def _inside():
    cyc = pd.concat([dd(c) for c in ["sec_ITB", "sec_KBE", "sec_XRT", "small"]], axis=1).mean(axis=1)
    de = pd.concat([mom(c, 6) for c in ["sec_XLU", "sec_XLP", "sec_XLV"]], axis=1).mean(axis=1)
    return Bo((cyc - dd12 <= -0.15) & (de >= 0))


H(s, "Inside the market: early cyclicals 15+ pts deeper below highs than S&P, defensives flat/up: stocks capped at 50%",
  "cut", _inside, level=0.5)
H(s, "Inside the market warning: 10y Treasuries for the non-stock part", "defensive", _inside, asset="t10y")
H(s, "10y-3m curve inverted: stocks capped at 50%", "cut", lambda: Bo(c103 < 0), level=0.5)
H(s, "Bull flattening while the Fed hikes (curve and 10y down in 3m, FF up 6m): 10% 10y Treasuries", "sleeve",
  lambda: Bo((curve - curve.shift(3) < 0) & (gs10 - gs10.shift(3) < 0) & (ff - ff.shift(6) > 0)), asset="t10y")
H(s, "2y <= Fed funds while the Fed still hikes: 10% 2y Treasuries", "sleeve",
  lambda: Bo((gs2 <= ff) & (ff - ff.shift(6) > 0)), asset="t2y")
_credit = lambda: Bo((baa - baa.rolling(6, min_periods=3).min() >= 0.5) | (_ddd(bkln) <= -0.03))
H(s, "Credit leads: Baa spread 0.5+ pt above 6m low (HY OAS proxy) or leveraged loans (BKLN) 3%+ off high: stocks to 0",
  "cut", _credit)
H(s, "Credit-dependent financials (insurers, banks) 25%+ below high while S&P within 15%: warnings acted on", "gate",
  lambda: Bo((dd("sec_KIE") <= -0.25) & (dd("sec_KBE") <= -0.25) & ((_ddd(psp) <= -0.25) | psp.isna()) & (dd12 > -0.15)))
OV(s, "Late cycle (curve < 0.5, credit weakening): long 10y Treasuries / short high yield 10%",
   lambda: (curve < 0.5) & ((ind["junk"] < 0) | (ind["baa_chg"] > 0)), {"t10y": 0.1, "hy": -0.1})
H(s, "Bear signals on (any cut) and 2y > FF - 1.5: 2y Treasuries for the non-stock part", "defensive",
  lambda: Bo((e41 < 1) & (gs2 > ff - 1.5)), asset="t2y")
OV(s, "Shorting stocks is hard (test): 20% short S&P in a growth-trend cut", lambda: gtt, {"spx": -0.2})
H(s, "M2 growth down >= 3 pts over 24m or below 4%: warnings acted on", "gate", lambda: Bo((m2 - m2.shift(24) <= -3) | (m2 < 4)))
H(s, "Global QT: Fed + ECB + BoJ balance sheets down over 12m (constant FX): stocks capped at 50%", "cut",
  lambda: Bo(gbs - gbs.shift(12) < 0), level=0.5)
H(s, "Fed shrinking balance sheet and deficit > 4%: warnings acted on", "gate",
  lambda: Bo((walcl - walcl.shift(12) < 0) & (deficit > 4)))


def _hike_meltdown():
    trig = (ff - ff.shift(1) > 0.1) & (dd12 <= -0.10) & (pd.concat([dd(c) for c in ["sec_ITB", "sec_KBE", "sec_XRT"]], axis=1).mean(axis=1) <= -0.25)
    k = keep(trig, 6)
    return Bo(k & ~(ff - ff.shift(3) <= 0) | Bo(trig))


H(s, "Fed hikes into a meltdown (S&P 10%+, cyclicals 25%+ off highs): stocks to 0 until the Fed pauses (max 6m)", "cut",
  _hike_meltdown)
H(s, "Unemployment near 10y low and Fed tightening (late cycle): stocks capped at 50%", "cut",
  lambda: Bo((unr <= unr.rolling(120, min_periods=60).min() + 0.2) & fed), level=0.5)
H(s, "Permits 6m < -10% and car sales 6m < -5% with Fed funds < 3%: warnings acted on", "gate",
  lambda: Bo((ind["permits"] < -10) & (ind["autos"] < -5) & (ff < 3)))
H(s, "Corporate debt 5y growth exceeds profits 5y growth by 25+ pts: stocks capped at 70%", "cut",
  lambda: Bo(yy(corpdebt, 60) - yy(profits, 60) >= 25), level=0.7)
H(s, "Fed balance sheet/GDP up 10+ pts in 5y and corporate debt/GDP at a record: stocks capped at 50%", "cut",
  lambda: Bo(((walcl / 1000 / ngdp * 100) - (walcl / 1000 / ngdp * 100).shift(60) >= 10) & (corpdebt / ngdp >= (corpdebt / ngdp).cummax() * 0.99)), level=0.5)


def _glob_breadth():
    av = pd.DataFrame({c: ma(pr(c), 10).notna() for c in CTRY})
    below = pd.DataFrame({c: ~above_ma(c).fillna(True) for c in CTRY}).where(av)
    n = av.sum(axis=1)
    return Bo((below.mean(axis=1) >= 0.6) & (n >= 6) & spx_up)


H(s, "Global breadth: 60%+ of country indexes below 10m avg while S&P above: warnings acted on", "gate", _glob_breadth)
H(s, "Washed out (S&P 15%+ off high, AAII bull-bear < -20) and Fed pausing: re-enter", "block",
  lambda: Bo((dd12 <= -0.15) & (aaii < -0.20) & (ff - ff.shift(3) <= 0)))
OV(s, "Fed tightening (12m > +1) with curve flattening: short banks 10%", lambda: (ff12 > 1) & (curve - curve.shift(6) < 0),
   {"sec_KBE": -0.1})
H(s, "Real GDP growth <= 2% and 10y falling 12m: 50% of equity in growth stocks", "location",
  lambda: Bo((yy(rgdp, 12) <= 2) & (ind["y10_chg"] < 0)), assets=["growth"])
H(s, "Commodity index 6m <= -15% (disinflation ahead): 10% 10y Treasuries", "sleeve", lambda: Bo(ret("commod", 6) <= -0.15),
  asset="t10y")
H(s, "Trendless high volatility (VIX > 25, |S&P 12m| < 5%, flat 10m avg): stocks capped at 50%", "cut",
  lambda: Bo((vix > 25) & (ret("spx", 12).abs() < 0.05) & ((ma(SPX, 10) / ma(SPX, 10).shift(1) - 1).abs() < 0.005)), level=0.5)
H(s, "Reflation reaction (cyclicals beat defensives 5%+ in 1m, 10y +0.3 pt): 50% of equity in small caps for 6m", "location",
  lambda: keep((pd.concat([R[c] for c in ["sec_XLI", "sec_XLB", "sec_XRT", "sec_KBE"]], axis=1).mean(axis=1)
                - pd.concat([R[c] for c in ["sec_XLU", "sec_XLP", "sec_XLV"]], axis=1).mean(axis=1) >= 0.05)
               & (gs10 - gs10.shift(1) >= 0.3), 6), assets=["small"])
H(s, "Swing big: 3+ of inside-market, inverted curve, credit, liquidity warnings: stocks to 0", "cut",
  lambda: Bo(mx(_inside()) + mx(Bo(curve < 0)) + mx(_credit()) + mx(Bo((m2 - m2.shift(24) <= -3) | (m2 < 4))) >= 3))
H(s, "Fed hikes are benign in booming conditions (S&P within 5% of high, NFCI loose): no cuts", "block",
  lambda: Bo(fed & (dd12 > -0.05) & (nfci < 0)))

s = "Jan van Eck - Insightful Investor 133"
H(s, "Deficit >= 5% outside recession (two feet on the gas): no cuts", "block", lambda: Bo((deficit >= 5) & ~unr_up))
H(s, "Deficit >= 5% outside recession: 10% commodities", "sleeve", lambda: Bo((deficit >= 5) & ~unr_up), asset="commod")
H(s, "Fed slamming the brakes (12m change >= +2.5 pts): stocks capped at 50%", "cut", lambda: Bo(ff12 >= 2.5), level=0.5)
H(s, "Fed 12m change >= +2 pts: stocks capped at 50% (his benchmark)", "cut", lambda: Bo(ff12 >= 2), level=0.5)
H(s, "Liquidity crisis (10y +1 pt in 3m, or VIX > 40 with Treasuries down): no gold (drops c5 gold)", "overlay",
  lambda: Bo((gs10 - gs10.shift(3) >= 1) | ((vix > 40) & (R["t10y"] < 0))),
  weights=lambda: pd.DataFrame({"gold": -X5["gold"] * mx(Bo((gs10 - gs10.shift(3) >= 1) | ((vix > 40) & (R["t10y"] < 0))))}))
_halv = [Per("2012-11"), Per("2016-07"), Per("2020-05"), Per("2024-04")]
H(s, "Bitcoin 0-12 months after a halving: 5% bitcoin", "sleeve",
  lambda: pd.Series([any(0 <= (g - h).n < 12 for h in _halv) for g in grid], index=grid), asset="btc", w=0.05)
H(s, "Commodities 12m > +15% and above 10m avg: 50% of equity in commodity-exporter markets", "location",
  lambda: Bo((ret("commod", 12) > 0.15) & above_ma("commod")),
  assets=["eq_brazil", "eq_mexico", "eq_chile", "eq_australia", "eq_canada"])
H(s, "Dollar falling and ex-US/S&P trending up: 40% of equity ex-US", "location",
  lambda: Bo((dlr12 < 0) & (ma(pr("intl_eq") / SPX, 10) > ma(pr("intl_eq") / SPX, 10).shift(1))), assets=["intl_eq"], s=0.4)
H(s, "India 15%+ behind ex-US over 12m (shock): 20% of equity in India", "location",
  lambda: Bo(rel("eq_india", "intl_eq", 12) <= -0.15), assets=["eq_india"], s=0.2)
H(s, "Oil +30% in 3m: 50% of equity in oil-exporter markets (Brazil, Canada)", "location",
  lambda: Bo(oilp / oilp.shift(3) - 1 >= 0.30), assets=["eq_brazil", "eq_canada"])
H(s, "CAPE top 5% and 10m avg falling: stocks to 0", "cut", lambda: Bo((cape_p >= 95) & ~slope_up("spx")))

s = "Borge Brende - NBIM In Good Company"
H(s, "Effective tariff rate +3 pts in 12m (labour-force leg missing): 10% TIPS", "sleeve",
  lambda: Bo(tariff - tariff.shift(12) >= 3), asset="tips")
H(s, "Productivity 5y average growth > 2%: no cuts", "block", lambda: Bo(yy(prod, 60).pipe(lambda x: ((1 + x / 100) ** 0.2 - 1) * 100) > 2))
OV(s, "Semis lag software 10%+ over 3m: long software / short semis 10%", lambda: rel("sec_SMH", "sec_IGV", 3) <= -0.10,
   {"sec_IGV": 0.1, "sec_SMH": -0.1})

s = "Jackie Rosner - Global Alts 2025"
H(s, "Trump put: S&P 10%+ off high in Trump years: re-enter", "block",
  lambda: Bo(YR.isin([2017, 2018, 2019, 2020, 2025, 2026]) & (dd12 <= -0.10)))
H("Pablo Calderini - Global Alts 2025", "Fiscal stress (federal interest/GDP rising, term premium +0.5 in 12m): 10% gold",
  "sleeve", lambda: Bo((int_gdp > int_gdp.shift(12)) & (tp - tp.shift(12) > 0.5)), asset="gold")

s = "Karen Karniol-Tambour - Sohn 2025"
H(s, "Inflationary regime (core CPI > 3%, dollar falling; trade leg missing): 40% of equity ex-US", "location",
  lambda: Bo(hot_core & (dlr12 < 0)), assets=["intl_eq"], s=0.4)
OV(s, "Dollar REER top decile and dollar falling 12m (NIIP leg missing): short dollar 10%",
   lambda: (pctl(reer_us) >= 90) & (dlr12 < 0), {"usd": -0.1})
OV(s, "Dollar REER top quintile and US-DE/JP 10y gap (2y proxy) narrowing 6m: long euro + yen 5% each",
   lambda: (pctl(reer_us) >= 80) & (((gs10 - (de10 + jp10) / 2) - (gs10 - (de10 + jp10) / 2).shift(6)) < 0),
   {"eur": 0.05, "jpy": 0.05})


def _fx_trend():
    q = MO.isin([3, 6, 9, 12])
    out = {}
    for a in ("eur", "jpy"):
        sg = np.sign(mom(a, 12)).where(q).ffill()
        out[a] = 0.05 * sg.fillna(0)
    return pd.DataFrame(out)


H(s, "Currency trend: 12m momentum on euro and yen vs USD, quarterly rebalance, 5% each", "overlay",
  lambda: Bo(R["eur"].notna()), weights=_fx_trend)
s = "Rob Citrone - Sohn 2025"
H(s, "Brazil real policy rate >= 4 pts and REER in bottom fifth of 10y (political leg missing): 50% of equity in Brazil",
  "location", lambda: Bo((br_rate - br_cpi >= 4) & (br_reer.rolling(120, min_periods=60).rank(pct=True) <= 0.2)),
  assets=["eq_brazil"])
H(s, "Brazil after 400bp+ hikes, hiking stopped, inflation past peak: 50% of equity in Brazil", "location",
  lambda: Bo(keep((br_rate - br_rate.shift(12)) >= 4, 12)
             & (br_rate - br_rate.shift(3) <= 0) & (br_cpi < br_cpi.rolling(6).max())), assets=["eq_brazil"])
OV(s, "Deficit widening 1+ pt, Fed on hold, term premium < 0.5: short long Treasuries 10%",
   lambda: (deficit - deficit.shift(12) >= 1) & ((ff - ff.shift(6)).abs() < 0.25) & (tp < 0.5), {"t30y": -0.1})
H("Karen Karniol-Tambour - Sohn 2025", "No Treasury risk premium (10y-3m <= 0.5, term premium <= 0.5): bills not long Treasuries",
  "overlay", lambda: Bo((c103 <= 0.5) & (tp <= 0.5)), weights=no_tlt(lambda: (c103 <= 0.5) & (tp <= 0.5)))
H("Karen Karniol-Tambour - Sohn 2025", "10y-3m >= 2 pts: long Treasuries for the non-stock part", "defensive",
  lambda: Bo((e41 < 1) & (c103 >= 2)), asset="t30y")
H(s, "Dollar falling and US CAPE > 30: 70% of equity ex-US (half developed, half EM)", "location",
  lambda: Bo((dlr12 < 0) & (ind["cape"] > 30)), assets=["intl_eq", "eq_em"], s=0.7)
H("Karen Karniol-Tambour - Sohn 2025", "Core CPI > 3% or 5y breakeven > 2.5%: 10% commodities", "sleeve",
  lambda: Bo(hot_core | (t5ie > 2.5)), asset="commod")
H(s, "Deficit widens 1+ pt outside recession (fiscal boom): no cuts for 12m", "block",
  lambda: keep((deficit - deficit.shift(12) >= 1) & ~unr_up, 12))
H("Karen Karniol-Tambour - Sohn 2025", "Stagflation-lite (CPI >= 3%, industrial production 6m down): 10% gold", "sleeve",
  lambda: Bo((cpi_yy >= 3) & (yy(S["fred_INDPRO"].shift(1), 6) < 0)), asset="gold")

s = "Steve Cohen - Sohn 2025"
H(s, "Effective tariff rate +5 pts in 12m: stocks capped at 50% for 12m", "cut", lambda: keep(tariff - tariff.shift(12) >= 5, 12), level=0.5)
H(s, "CAPE top fifth and OECD US leading indicator falling: stocks capped at 65%", "cut",
  lambda: Bo((cape_p >= 80) & (cli_us < cli_us.shift(3))), level=0.65)
H(s, "Warnings rising but S&P up on the month (priced in): no cuts", "block", lambda: Bo((share > share.shift(1)) & (R["spx"] >= 0)))
H(s, "Warnings rising and S&P down 3%+ on the month: stocks to 0", "cut", lambda: Bo((share > share.shift(1)) & (R["spx"] <= -0.03)))
H(s, "Retest after a 15%+ fall (within 5% of 12m low): buy zone, no cuts", "block",
  lambda: Bo((dd12.rolling(6, min_periods=1).min() <= -0.15) & (SPX <= SPX.rolling(12, min_periods=1).min() * 1.05)))
H(s, "V-shaped recovery: back above 10m avg within 3 months of a 15%+ fall: no cuts", "block",
  lambda: Bo(spx_up & (dd12.rolling(3, min_periods=1).min() <= -0.15)))


def _regime_change():
    dec = MO == 12
    yr_ret = (SPX / SPX.shift(12) - 1).where(dec)
    cp = (ind["cape"] / ind["cape"].shift(12) - 1).where(dec)
    flag = ((yr_ret >= 0.20) & (cp >= 0.15)).where(dec).dropna()
    fy = {int(k.year) + 1: bool(v) for k, v in flag.items()}          # applies to the following calendar year
    return Bo(pd.Series([fy.get(int(y), False) for y in HY], index=grid)) & eps_dn


H(s, "After a 20%+ year with 15%+ P/E expansion and EPS not rising: stocks capped at 80% next year", "cut",
  _regime_change, level=0.8)


# ================================================================== rules covered by the raw research store
s = "Jeffrey Hirsch - Eisman Playbook Ep56"
H(s, "First five days of January down: stocks capped at 50% Feb-Dec", "cut",
  lambda: Bo((MO <= 11) & (year_val("first5") < 0)), level=0.5)
H(s, "Santa Claus rally fails: stocks capped at 50% Feb-Mar", "cut", lambda: Bo(MO.isin([1, 2]) & (year_val("santa") < 0)), level=0.5)
_tri = (year_val("santa") > 0).astype(int) + (year_val("first5") > 0).astype(int) + (year_val("jan") > 0).astype(int)
H(s, "January trifecta all up: no cuts Feb-Dec", "block", lambda: Bo((MO <= 11) & (_tri == 3) & year_val("jan").notna()))
H(s, "January trifecta <= 1 of 3 up and S&P below 10m avg: stocks capped at 50% Feb-Dec", "cut",
  lambda: Bo((MO <= 11) & (_tri <= 1) & year_val("jan").notna() & trend_dn), level=0.5)
H(s, "Best six months with MACD(12,26,9) timing on the daily S&P: out from the first sell after Apr 1 to the first buy after Oct 1",
  "cut", lambda: _macd_state())
H(s, "War shock (GPR spike) a month ago and S&P within 15% of high: buy, no cuts", "block",
  lambda: Bo(gpr_spike.shift(1).fillna(False) & (dd12 > -0.15)))

s = "Todd Sohn - Eisman Playbook Ep66"
H(s, "RSI divergence at a new 52-week high (RSI 10+ below the prior high's): stocks capped at 50% for 1m", "cut",
  lambda: RSI_BEAR, level=0.5)
H(s, "Bullish RSI divergence at a new 52-week low: re-enter", "block", lambda: RSI_BULL)
H(s, "Uptrend (10m avg rising), RSI > 70 in the last 2 months, now 40-55: buy (no cuts) for 3m", "block",
  lambda: keep(slope_up("spx") & (RSI_MAX.rolling(2, min_periods=1).max() > 70) & RSI_END.between(40, 55), 3))
H(s, "High beta vs low vol 12m spread (SPHB-SPLV) in top 5%: stocks capped at 50%", "cut",
  lambda: Bo(pctl((sphb / sphb.shift(12)) - (splv / splv.shift(12)), 36) >= 95), level=0.5)
_gs = lambda: Bo(gpr_spike & (R["gold"] < 0))
H(s, "Gold fails on a war spike (GPR spike, gold down on the month): no gold for 3m (drops c5 gold)", "overlay",
  lambda: keep(_gs(), 3), weights=lambda: pd.DataFrame({"gold": -X5["gold"] * mx(keep(_gs(), 3))}))

H("Kyle Bass - Hoover Global Macro", "Middle East / geopolitical spike (GPR): 10% gold for 3 months, then fade", "sleeve",
  lambda: keep(gpr_spike, 3), asset="gold")
H("Mike Pompeo - Money Maze", "Geopolitical risk regime (GPR spike): 20% of equity in defence + energy for 12m", "location",
  lambda: keep(gpr_spike, 12), assets=["sec_ITA", "sec_XLE"], s=0.2)
OV("Mike Pompeo - Money Maze", "US-China trade escalation (trade-policy uncertainty 2 sd above 5y mean): long allied Asia / short China 10% for 12m",
   lambda: keep(tpu >= tpu.rolling(60, min_periods=36).mean() + 2 * tpu.rolling(60, min_periods=36).std(), 12),
   {"eq_japan": 0.025, "eq_korea": 0.025, "eq_india": 0.025, "eq_australia": 0.025, "eq_china": -0.1})
H("Stanley Druckenmiller - Bloomberg Dec 2018", "Trade war: trade-policy uncertainty 2 sd above 5y mean: stocks capped at 50% for 6m", "cut",
  lambda: keep(tpu >= tpu.rolling(60, min_periods=36).mean() + 2 * tpu.rolling(60, min_periods=36).std(), 6), level=0.5)
H("Pablo Calderini - Resilient Strategies", "Low vol (VIX < 14, MOVE < 100) while GPR above its 5y average: 2% VIX futures", "sleeve",
  lambda: Bo((vix < 14) & (move < 100) & (gpr > gpr.rolling(60, min_periods=36).mean())), asset="vix_fut", w=0.02)
H("Pablo Calderini - Resilient Strategies", "State-on-state Middle East strike (GPR spike) with oil up: 5% of equity in energy for 3m",
  "location", lambda: keep(gpr_spike & (oilp > oilp.shift(1)), 3), assets=["sec_XLE"], s=0.05)
H("Brad Gerstner - BG2 Ep14", "Geopolitical flare-up (GPR spike, S&P -5% in a month) without an oil shock (< +30%): buy, no cuts for 6m",
  "block", lambda: keep(gpr_spike & (R["spx"] <= -0.05) & (oilp / oilp.shift(1) - 1 < 0.30), 6))
H("Jan van Eck - Insightful Investor 133", "War liquidation: in a GPR spike month hold bills, not long Treasuries", "overlay",
  lambda: gpr_spike, weights=no_tlt(lambda: gpr_spike))
H("Borge Brende - NBIM In Good Company", "GPR 12m average in top fifth since 1985: 5% gold", "sleeve",
  lambda: Bo(pctl(gpr.rolling(12).mean(), 36) >= 80), asset="gold", w=0.05)
H("Borge Brende - NBIM In Good Company", "GPR 12m average in top fifth since 1985: 20% of equity in defence", "location",
  lambda: Bo(pctl(gpr.rolling(12).mean(), 36) >= 80), assets=["sec_ITA"], s=0.2)
H("Jackie Rosner - Global Alts 2025", "Inflationary geopolitics (GPR and oil both up 3m): 10% commodities", "sleeve",
  lambda: Bo((gpr.rolling(3).mean() > gpr.rolling(3).mean().shift(3)) & (oilp > oilp.shift(3))), asset="commod")
H("Jackie Rosner - Global Alts 2025", "Disinflationary geopolitics (GPR and oil both down 3m): 10% 10y Treasuries", "sleeve",
  lambda: Bo((gpr.rolling(3).mean() < gpr.rolling(3).mean().shift(3)) & (oilp < oilp.shift(3))), asset="t10y")


def _oil_cheap():
    lo5, hi5 = oilp.rolling(60, min_periods=36).min(), oilp.rolling(60, min_periods=36).max()
    pos = COT["oil"].rolling(36, min_periods=24).rank(pct=True)
    return Bo((oilp <= lo5 + 0.2 * (hi5 - lo5)) & (gpr > gpr.rolling(12).mean()) & (pos <= 0.2))


H("Rob Citrone - Sohn 2025", "Oil in bottom fifth of 5y range, GPR above 12m mean, speculators short (COT bottom fifth): 10% oil for 3m",
  "sleeve", lambda: keep(_oil_cheap(), 3), asset="oil")


def _cot_contra():
    out = {}
    for a, x in COT.items():
        r = x.rolling(36, min_periods=24).rank(pct=True)
        out[a] = 0.05 * (mx(Bo(r <= 0.1)) - mx(Bo(r >= 0.9)))
    return pd.DataFrame(out)


H("Karen Karniol-Tambour - Sohn 2025", "Contrarian COT: speculative net position top decile of 3y -> short 5%, bottom decile -> long 5% "
  "(gold, crude, copper, silver)", "overlay",
  lambda: Bo((_cot_contra().abs().sum(axis=1) > 0)), weights=_cot_contra)
H("Karen Karniol-Tambour - Sohn 2025", "Tariffs rising, core goods CPI > 2% and supply-chain pressure (GSCPI) > 1: 10% TIPS", "sleeve",
  lambda: Bo((tariff > tariff.shift(12)) & (yy(_sac).shift(1) > 2) & (gscpi > 1)), asset="tips")
