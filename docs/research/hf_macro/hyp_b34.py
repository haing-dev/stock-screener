from harness import *  # noqa
"""Hypotheses from transcript rules in macro_read/out/batch3.md and batch4.md (one per codeable rule, merged where the
rules are duplicates, at most one alternative threshold). Ids B001.. are assigned in list order at the bottom.

Publication lags (all conditions known at the end of month t):
  P['F'] / P['ind'] / P['sc']   already point in time
  S monthly macro (CPI parts, sentiment, saving, income, M2, EPU monthly, NFCI, Philly Fed excluded) .shift(1);
  consumer credit, Korea exports, OECD country data .shift(2)
  S quarterly NIPA (GDP, deflator, productivity) .shift(4); NIPA government/profits/customs, debt/GDP .shift(5);
  Z.1 (household net worth, household and business debt), TDSP, foreign holdings .shift(6); BIS house prices .shift(7)
  annual fiscal-year deficit .shift(11) (only used before the monthly Treasury statement starts in 1981)
  daily market series in S (yields, breakevens, FX, Brent, T-bill, ECB rate, MOVE, EPU daily) and Yahoo px_*: no lag
  Philly Fed survey is released in the same month: no lag
"""

# ------------------------------------------------------------------ helpers
TT = pd.Series(range(T), index=grid)


def B(x):
    return pd.Series(x, index=grid).reindex(grid).fillna(False).astype(bool)


def hold(c, n):
    """Signal stays on for n months including the trigger month."""
    return B(c).astype(float).rolling(n, min_periods=1).max().astype(bool)


def hyst(on, off):
    """On when `on`, stays on until `off` (off wins)."""
    on, off = B(on).values, B(off).values
    st, out = False, []
    for a, b in zip(on, off):
        st = (st or a) and not b
        out.append(st)
    return pd.Series(out, index=grid)


def avail(a):
    x = R[a].shift(-1).notna()
    x.iloc[-1] = bool(pd.notna(R[a].iloc[-1]))
    return x


def q(k, lag):
    """Quarterly S series (dated at quarter start), carried to the next two months, then lagged."""
    return S[k].ffill(limit=2).shift(lag)


def lv_(a):
    return lvl(R[a]).where(R[a].notna().cummax())


def rn(a, n):
    l_ = lv_(a)
    return l_ / l_.shift(n) - 1


def chg(x, n):
    return x - x.shift(n)


def pch(x, n):
    return (x / x.shift(n) - 1) * 100


def legs(cond_fn, w, need=None):
    """Overlay with explicit weights {asset: weight}; zero in months where any needed leg has no data."""
    need = [a for a in w if a != "spx"] if need is None else need

    def f():
        c = B(cond_fn())
        ok = c.copy()
        for a in need:
            ok &= avail(a)
        return pd.DataFrame({a: v * ok.astype(float) for a, v in w.items()}, index=grid)
    return f


def pair(cond_fn, longs, shorts, w=0.1):
    """Overlay: +w split equally over available longs, -w split equally over available shorts."""
    def f():
        c = B(cond_fn())
        cols = list(dict.fromkeys(list(longs) + list(shorts)))
        out = pd.DataFrame(0.0, index=grid, columns=cols)
        AL = pd.DataFrame({a: avail(a) for a in longs}) if longs else None
        AS = pd.DataFrame({a: avail(a) for a in shorts}) if shorts else None
        ok = c.copy()
        if longs:
            nl = AL.sum(axis=1)
            ok &= nl > 0
        if shorts:
            ns = AS.sum(axis=1)
            ok &= ns > 0
        for a in longs:
            out[a] += np.where(ok & AL[a], w / nl.clip(lower=1), 0.0)
        for a in shorts:
            out[a] -= np.where(ok & AS[a], w / ns.clip(lower=1), 0.0)
        return out
    return f


def ret_assets(c):
    return c


# ------------------------------------------------------------------ shared signals (all point in time)
spx_l = lv_("spx")
dd = spx_l / spx_l.cummax() - 1                                   # S&P drawdown from its high (total return, month-end)
spx1 = R["spx"]
gs10, gs2, ff, unr = F["GS10"], F["GS2"], F["FEDFUNDS"], F["UNRATE"]
# core CPI: tool series from 1997; before that rebuilt from its two parts (core goods, services less energy), weights
# from BLS relative importance (core goods ~40% of core in 1967 falling to ~25% by 2024); fit 1998-2026: corr 0.998
_yr = pd.Series(grid.year + (grid.month - 1) / 12, index=grid)
_wg = (0.40 - 0.15 * (_yr - 1967) / 57).clip(0.25, 0.40)
_rprx = (_wg * S["fred_CUSR0000SACL1E"].shift(1).pct_change(fill_method=None)
         + (1 - _wg) * S["fred_CUSR0000SASLE"].shift(1).pct_change(fill_method=None))
_rc = F["CPILFESL"].pct_change(fill_method=None).combine_first(_rprx)
core = (1 + _rc.fillna(0)).cumprod().where(_rc.notna().cummax())
core_yy = (core / core.shift(12) - 1) * 100
core3 = ((core / core.shift(3)) ** 4 - 1) * 100
sahm = ind["jobs_alarm"]
curve = ind["curve"]
vix = ind["vix"]
cape = ind["cape"]
cape_p = pctl(cape)
corr = ind["stockbond"]
ff3, ff12 = chg(ff, 3), chg(ff, 12)
y10_3, y10_6, y10_12 = chg(gs10, 3), chg(gs10, 6), chg(gs10, 12)

# dollar: DXY (Yahoo, month-end, 1985+) spliced by returns onto the Fed trade-weighted dollar before 1985
_dxy = S["px_DX-Y.NYB"]
_tw = F["TWEXMMTH"].combine_first(F["DTWEXBGS"])
_dr = _dxy.pct_change(fill_method=None).combine_first(_tw.pct_change(fill_method=None))
dl = (1 + _dr.fillna(0)).cumprod().where(_dr.notna().cummax())


def dch(n):
    return pch(dl, n)


dpos5 = (dl - dl.rolling(60, min_periods=36).min()) / (dl.rolling(60, min_periods=36).max() - dl.rolling(60, min_periods=36).min())

# real 10y: TIPS yield from 2003, before that 10y minus core CPI y/y (tool's definition, extended with the core proxy)
_rt, _rp = S["fred_DFII10"], gs10 - core_yy
real10 = _rt.combine_first(_rp)


def rch(n):
    return chg(_rt, n).combine_first(chg(_rp, n))


be10, be5 = S["fred_T10YIE"], S["fred_T5YIE"]


def bech(n):                                                       # breakeven change; before 2003 core CPI y/y change
    return chg(be10, n).combine_first(chg(core_yy, n))


gold_l, com_l = lv_("gold"), lv_("commod")
oil = F["WTISPLC"]
oil3, oil6 = pch(oil, 3), ind["oil"]
brent = S["fred_DCOILBRENTEU"]
copper, iron = F["PCOPPUSDM"], F["PIORECRUSDM"]
walcl = F["WALCL"]
tp = F["THREEFYTP10"]

# fiscal
# nominal GDP $bn SAAR: tool series (real time, 1992+); before that real GDP x deflator (latest vintage, lag 4)
gdp = F["GDP"].combine_first(q("fred_GDPC1", 4) * q("fred_GDPDEF", 4) / 100)
y10_ngdp = ind["y10_ngdp"].combine_first(gs10 - pch(q("fred_GDPC1", 4) * q("fred_GDPDEF", 4) / 100, 12))
_mts = S["fred_MTSDS133FMS"].shift(1)                              # monthly surplus, $mn
_def_m = -(_mts.rolling(12).sum()) / 1000 / gdp * 100
deficit = _def_m.combine_first(-S["fred_FYFSGDA188S"].ffill(limit=11).shift(11))   # deficit % GDP, positive = deficit
debt_gdp = q("fred_GFDEGDQ188S", 5)
interest = q("fred_A091RC1Q027SBEA", 5)
int_gdp = interest / gdp * 100
int_rev = interest / q("fred_FGRECPT", 5) * 100
defense = q("fred_FDEFX", 5)
tariff = q("fred_B235RC1Q027SBEA", 5) / q("fred_IMPGS", 5) * 100
cust_gdp = q("fred_B235RC1Q027SBEA", 5) / gdp * 100
imp_gdp = q("fred_IMPGS", 5) / gdp * 100
_net12 = -(_mts.rolling(12).sum())                                 # net borrowing over 12 months, $mn
fed_share = chg(S["fred_TREAST"], 12) / _net12 * 100              # Fed Treasury purchases / net issuance, %
rff = ff - core_yy                                                 # real fed funds

# profits, households, labour
prof_gdp = q("fred_CPATAX", 5) / gdp * 100
nw = q("fred_TNWBSHNO", 6)
debt_nw = q("fred_GFDEBTN", 5) / nw * 100
hh_debt, bus_debt = q("fred_CMDEBT", 6), q("fred_BCNSDODNS", 6)
priv = hh_debt + bus_debt
priv_borrow = chg(priv, 12) / 1000 / gdp * 100
credit_gdp = priv / 1000 / gdp * 100
credit_gap = credit_gdp - credit_gdp.rolling(120, min_periods=60).mean()    # one-sided gap vs trailing 10y mean
psav = S["fred_PSAVERT"].shift(1)
revol = S["fred_REVOLSL"].shift(2)
dpi = S["fred_DSPIC96"].shift(1)
kalecki = deficit + priv_borrow - psav
ulc, defl, lshare = q("fred_ULCNFB", 4), q("fred_GDPDEF", 4), q("fred_PRS85006173", 4)
rgdp = q("fred_GDPC1", 4)
rgdp_yy = pch(rgdp, 12)
hp_real = q("fred_QUSR628BIS", 7)
tdsp = q("fred_TDSP", 6)
nrou = S["fred_NROU"].ffill(limit=2)                               # CBO estimate (revised; see notes)
fh = q("fred_FDHBFIN", 6)                                          # foreign holdings of federal debt

# prices, sentiment, activity
cpi_yy_ = cpi_yy
food_yy = pch(S["fred_CPIUFDSL"].shift(1), 12)
en_yy = pch(S["fred_CPIENGSL"].shift(1), 12)
fe_gap = 0.65 * food_yy + 0.35 * en_yy - core_yy
cgoods3 = ((S["fred_CUSR0000SACL1E"].shift(1) / S["fred_CUSR0000SACL1E"].shift(4)) ** 4 - 1) * 100
umich = S["fred_UMCSENT"].shift(1)
epu = S["fred_USEPUINDXM"].shift(1)
epud = S["fred_USEPUINDXD"]
philly = S["fred_GACDFSA066MSFRBPHI"]
kx = S["fred_XTEXVA01KRM667S"].shift(2)
kx_yy = pch(kx, 12)
nfci = S["fred_NFCI"].shift(1)
tb3 = S["fred_DTB3"]
move = S["px_^MOVE"]
tnx = S["px_^TNX"]
drill = S["fred_IPN213111N"].shift(1)
ey = (S["sh_eps"] / S["sh_price"] * 100).shift(3)                  # Shiller E/P, earnings with a 3-month lag
pe = (S["sh_price"] / S["sh_eps"]).shift(3)
eps_g = pch(S["sh_eps"].shift(3), 12)
share_ = P["share"]
jp10 = S["fred_IRLTLT01JPM156N"].shift(1)
de10 = S["fred_IRLTLT01DEM156N"].shift(1)
gb10 = S["fred_IRLTLT01GBM156N"].shift(1)
reer_us = S["fred_RBUSBIS"].shift(1)
reer_br = S["fred_RBBRBIS"].shift(1)
br_rate = S["fred_IRSTCI01BRM156N"].shift(1)
br_cpi = S["fred_CPALTT01BRM659N"].shift(2)
cn_cpi = S["fred_CPALTT01CNM659N"].shift(2)
cn_hp = q("fred_QCNR628BIS", 7)
boj = S["fred_JPNASSETS"].shift(1)
ecb = S["fred_ECBDFR"]

# frequently used compound conditions
REAL = {"gold": 0.05, "commod": 0.05, "t30y": -0.1}               # real assets vs nominal long Treasuries
EXPORTERS = ["eq_brazil", "eq_australia", "eq_canada", "eq_chile"]
COUNTRIES = ["eq_korea", "eq_brazil", "eq_japan", "eq_china", "eq_india", "eq_taiwan", "eq_mexico", "eq_germany",
             "eq_uk", "eq_canada", "eq_australia", "eq_hongkong", "eq_s_africa", "eq_chile", "eq_turkey",
             "eq_indonesia"]


def since_recovery():
    """Months since the S&P regained its prior high after the last 20%+ fall (NaN while still recovering)."""
    out, bear, rec = [], False, None
    for t, v in enumerate(dd.values):
        if v <= -0.20:
            bear, rec = True, None
        elif bear and v >= -1e-9:
            bear, rec = False, t
        out.append(np.nan if rec is None else t - rec)
    return pd.Series(out, index=grid)


def cred_loss():                                                   # Krugman: yields up, dollar down, gold up (3m)
    return (y10_3 > 0.3) & (dch(3) < -3) & (rn("gold", 3) > 0.05)


def checklist():                                                   # Oppenheimer bottom checklist, >= 3 of 4
    c1 = cape <= cape.rolling(240, min_periods=120).median()
    c2 = (chg(philly, 3) > 0) & (philly < 0)
    c3 = gs2 <= gs2.rolling(6).max() - 0.5
    c4 = cpi_yy <= cpi_yy.rolling(12).max() - 1
    return (c1.astype(int) + c2.astype(int) + c3.astype(int) + c4.astype(int)) >= 3


def reversal_w(w=0.1):
    """Nations: countries that fell > 30% in 12 months, held 36 months, long vs S&P."""
    def f():
        sig = pd.DataFrame({c: hold(rn(c, 12) < -0.30, 36) & avail(c) for c in COUNTRIES})
        n = sig.sum(axis=1)
        out = sig.astype(float).mul(w / n.clip(lower=1), axis=0)
        out["spx"] = -out.sum(axis=1)
        return out
    return f


FXMAP = {"eq_brazil": "fred_DEXBZUS", "eq_korea": "fred_DEXKOUS", "eq_mexico": "fred_DEXMXUS",
         "eq_india": "fred_DEXINUS", "eq_china": "fred_DEXCHUS"}


def fxlead_w(w=0.1):
    """Citrone: EM equities lag FX. Currency -10% in 3m -> short the country 3m; +10% -> long; vs S&P."""
    def f():
        sg = {}
        for c, k in FXMAP.items():
            x = S[k] / S[k].shift(3) - 1                           # local per USD: up = local currency weaker
            weak, strong = hold(x > 1 / 0.9 - 1, 3), hold(x < 0.9 - 1, 3)
            sg[c] = (strong.astype(float) - weak.astype(float)) * avail(c).astype(float)
        sg = pd.DataFrame(sg)
        n = (sg != 0).sum(axis=1)
        out = sg.mul(w / n.clip(lower=1), axis=0)
        out["spx"] = -out.sum(axis=1)
        return out
    return f


def fxlead_c():
    x = pd.DataFrame({c: (S[k] / S[k].shift(3) - 1).abs() > 0.1 for c, k in FXMAP.items()})
    return x.any(axis=1)


def policy_changes():                                              # Tropin: 25bp-equivalent moves, Fed + ECB, 12m
    n = (ff.diff().abs() / 0.25).fillna(0) + (ecb.diff().abs() / 0.25).fillna(0)
    return n.rolling(12).sum()


YCC = B((grid >= Per("2016-09")) & (grid <= Per("2024-02")))      # BoJ yield-curve control (announced policy)
foreign10 = pd.concat([jp10, de10, gb10], axis=1).mean(axis=1, skipna=False)

# ------------------------------------------------------------------ hypotheses
G = "Luke Gromen - Saudis Break the Petrodollar"
RG = "Kenneth Rogoff - In Good Company NBIM"
NA = "Scott Nations - Act Rationally in a Crisis"
BS = "Scott Bessent - Inside Trump's Treasury"
TR = "Kenneth Tropin - Risk and Return Podcast"
KR = "Paul Krugman - Generating Alpha Ep 28"
YA = "Jeff Yass - Economic Myths Ep 55"
KT = "Karen Karniol-Tambour - Sohn 2022"
GE = "Brad Gerstner - BG2 AI Middle East Tariffs"
CI = "Rob Citrone - Capital Allocators EP261"
BR = "Scott Bessent - Real Vision macro strategy"
EI = "Verrone/Trennert - Eisman Playbook Ep 73"
OP = "Peter Oppenheimer - Money Maze (Goldman)"
LA = "Christine Lagarde - In Good Company NBIM"
KG = "Kristalina Georgieva - IMF In Good Company"
EW = "Steve Eisman - Weekly Wrap OpenAI"


def H(source, desc, kind, cond, **kw):
    d = dict(source=source, desc=desc, kind=kind, cond=cond)
    if kind == "sleeve":                                           # no fake cash where the asset has no data yet
        a, c0 = kw["asset"], cond
        d["cond"] = lambda: B(c0()) & avail(a)
    if kind == "location":                                         # on only where at least one target has data
        aa, c1 = kw["assets"], cond
        d["cond"] = lambda: B(c1()) & pd.concat([avail(x) for x in aa], axis=1).any(axis=1)
    d.update(kw)
    return d


def OV(source, desc, cond, w):
    return H(source, desc, "overlay", cond, weights=legs(cond, w))


def PR(source, desc, cond, longs, shorts, w=0.1):
    return H(source, desc, "overlay", cond, weights=pair(cond, longs, shorts, w))


HYP = [
    # ======================= batch 3, file 1: Gromen
    OV(G, "debt/GDP>100% and real fed funds<0 (exit real FF>+1%): 5% gold+5% commodities vs short 10% long Treasuries",
       lambda: hyst((debt_gdp > 100) & (rff < 0), rff > 1), REAL),
    OV(G, "alt: debt/GDP>100% and real 10y<0: real assets vs long Treasuries",
       lambda: (debt_gdp > 100) & (real10 < 0), REAL),
    OV(G, "Fed bought >50% of 12m net Treasury issuance and CPI y/y>4%: real assets vs long Treasuries (repression)",
       lambda: (fed_share > 50) & (cpi_yy > 4), REAL),
    H(G, "commodity index 12m change>0 and above its 10m average: 10% commodities", "sleeve",
      lambda: (rn("commod", 12) > 0) & above_ma("commod"), asset="commod", w=0.1),
    H(G, "Fed hiking (funds +1pt in 12m) and dollar within 5% of its 12m high: stocks to 0 (deflationary fit)", "cut",
      lambda: (ff12 > 1) & (ind["dollar_break"] >= -5), level=0.0),
    H(G, "alt: Fed hiking and DXY >= 96 (his level): stocks to 0", "cut",
      lambda: (ff12 > 1) & (_dxy >= 96), level=0.0),
    H(G, "Fed-tightening gate on but dollar fell >3% in 3m: hikes tolerable, no cut (also 'dollar falls -> Fed can hike')",
      "block", lambda: fed & (dch(3) < -3)),
    H(G, "10y up >50bp in 3m with the dollar up: risk-off, stocks to 0", "cut",
      lambda: (y10_3 > 0.5) & (dch(3) > 0), level=0.0),
    H(G, "10y up >50bp in 3m with the dollar down: benign reflation, no cut", "block",
      lambda: (y10_3 > 0.5) & (dch(3) < 0)),
    H(G, "Nasdaq-100 trails value by >10% over 6m (money leaves US tech): 30% of equities to EM/gold/commodities, 6m",
      "location", lambda: hold((rn("ndx", 6) - rn("value", 6)) < -0.10, 6), assets=["eq_em", "gold", "commod"], s=0.3),
    H(G, "recovery (unemployment down 6m, Philly Fed up 6m) and dollar 6m<0, until dollar 6m>0: half of equities to EM",
      "location", lambda: hyst((unr < unr.shift(6)) & (chg(philly, 6) > 0) & (dch(6) < 0), dch(6) > 0),
      assets=["eq_em", "eq_brazil", "eq_korea"], s=0.5),
    OV(G, "dollar in top 20% of its 5y range (foreign officials sell Treasuries): short 10% long Treasuries",
       lambda: dpos5 >= 0.8, {"t30y": -0.1}),
    H(G, "dollar in bottom 20% of its 5y range (foreign officials buy): 10% long Treasuries", "sleeve",
      lambda: dpos5 <= 0.2, asset="t30y", w=0.1),
    H(G, "Fed balance sheet 3m change < -2% (aggressive QT): stocks to 50%", "cut",
      lambda: pch(walcl, 3) < -2, level=0.5),
    OV(G, "Fed bought >60% of 12m net issuance: short 10% dollar (UUP) for 12m",
       lambda: hold(fed_share > 60, 12), {"usd": -0.1}),
    H(G, "S&P >=20% below high with debt/GDP>100% (deflationary fit, QE coming): 10% long Treasuries", "sleeve",
      lambda: (dd <= -0.20) & (debt_gdp > 100), asset="t30y", w=0.1),
    H(G, "Fed balance sheet +10% in 3m with debt/GDP>100%: rotate to 10% gold for 12m", "sleeve",
      lambda: hold((pch(walcl, 3) > 10) & (debt_gdp > 100), 12), asset="gold", w=0.1),
    H(G, "gold 3m>0 while real 10y up >25bp in 3m (debasement): 10% gold for 6m", "sleeve",
      lambda: hold((rn("gold", 3) > 0) & (rch(3) > 0.25), 6), asset="gold", w=0.1),
    H(G + " / " + BR, "alt (Bessent): gold 6m>+10% while real 10y up >25bp in 6m: 10% gold for 12m", "sleeve",
      lambda: hold((rn("gold", 6) > 0.10) & (rch(6) > 0.25), 12), asset="gold", w=0.1),
    H(G, "gold at a 12m high while the dollar fell over 6m: 10% gold for 6m", "sleeve",
      lambda: hold((gold_l >= gold_l.rolling(12).max()) & (dch(6) < 0), 6), asset="gold", w=0.1),
    H(G, "debasement regime (debt>100%, real FF<0) and gold >=10% below 12m high on a hawkish shift (2y up 3m): 10% gold 12m",
      "sleeve", lambda: hold((debt_gdp > 100) & (rff < 0) & (gold_l / gold_l.rolling(12).max() - 1 <= -0.10)
                             & (chg(gs2, 3) > 0), 12), asset="gold", w=0.1),
    H(G, "10y-2y <0.5pt and flattening over 3m while the Fed hikes: stocks to 50%", "cut",
      lambda: (curve < 0.5) & (curve < curve.shift(3)) & (ff3 > 0), level=0.5),

    # ======================= batch 3, file 2: Rogoff
    OV(RG, "tariff rate +5pts in 12m and Fed cutting with core CPI>3% (1970s/Nixon): real assets vs long Treasuries 12m",
       lambda: hold((chg(tariff, 12) > 5) & (ff3 < 0) & (core_yy > 3), 12), REAL),
    H(RG, "consumer sentiment -20% in 6m or policy uncertainty >2x its 5y average: stocks to 50%", "cut",
      lambda: (pch(umich, 6) < -20) | (epu > 2 * epu.rolling(60, min_periods=36).mean()), level=0.5),
    H(RG, "'sell America': term premium +50bp and dollar -5% over 6m: half of equities ex-US", "location",
      lambda: (chg(tp, 6) > 0.5) & (dch(6) < -5), assets=["intl_eq"], s=0.5),
    H(RG, "China growth proxy (Korea exports) above its 12m average: half of equities in commodity exporters", "location",
      lambda: kx > ma(kx, 12), assets=EXPORTERS, s=0.5),
    PR(RG, "China japanification (China CPI<0.5%, real house prices falling; until CPI>1.5% 6m): short China vs S&P",
       lambda: hyst((cn_cpi < 0.5) & (pch(cn_hp, 12) < 0), (cn_cpi > 1.5).astype(float).rolling(6).min() == 1),
       ["spx"], ["eq_china"]),
    OV(RG, "big shock (unemployment +2pts in 6m, deficit +3pts GDP in 12m): months 6-24 after, real assets vs long T",
       lambda: hold(((chg(unr, 6) > 2) & (chg(deficit, 12) > 3)).shift(6), 18), REAL),
    OV(RG, "debt/GDP>100% and deficit>5% outside recession (Sahm<0.5): short 10% long Treasuries",
       lambda: (debt_gdp > 100) & (deficit > 5) & (sahm < 0.5), {"t30y": -0.1}),
    OV(RG, "second inflation episode (core>4% within 10y) and core 3m annualised>3.5%: short 10% long Treasuries",
       lambda: (core3 > 3.5) & ((core_yy > 4).astype(float).shift(13).rolling(108, min_periods=1).max() == 1),
       {"t30y": -0.1}),
    H(RG, "bitcoin >50% below its 12m high (crypto stress; stablecoin leg not available): stocks to 50%", "cut",
      lambda: lv_("btc") / lv_("btc").rolling(12).max() - 1 <= -0.5, level=0.5),
    H(RG, "tech boom: Nasdaq-100 12m return >50% (tech-share leg not available): half of equities to equal weight",
      "location", lambda: rn("ndx", 12) > 0.5, assets=["eqw"], s=0.5),
    OV(RG, "financial repression (real 10y<0 with CPI>3%): real assets vs long Treasuries",
       lambda: (real10 < 0) & (cpi_yy > 3), REAL),
    OV(RG, "Fed will hike: core 3m annualised>3% and unemployment below its 12m average: short 10% 2y Treasuries",
       lambda: (core3 > 3) & (unr < unr.rolling(12).mean()), {"t2y": -0.1}),
    OV(RG, "interest outlays>3% of GDP or >15% of revenue: 10% gold vs short 10% long Treasuries",
       lambda: (int_gdp > 3) | (int_rev > 15), {"gold": 0.1, "t30y": -0.1}),
    OV(RG + " / " + BR, "alt (Bessent): federal interest outlays > defence spending: gold vs long Treasuries",
       lambda: interest > defense, {"gold": 0.1, "t30y": -0.1}),
    H(RG, "global downturn (ex-US stocks below 10m avg, Korea exports y/y<0): half of equities in low-debt countries 12m",
      "location", lambda: hold((lv_("intl_eq") < ma(lv_("intl_eq"), 10)) & (kx_yy < 0), 12),
      assets=["eq_germany", "eq_australia", "eq_korea"], s=0.5),
    OV(RG, "dollar +5% in 6m (EM dollar debt breaks): short 10% EM dollar bonds",
       lambda: dch(6) > 5, {"em_debt": -0.1}),

    # ======================= batch 3, file 3: Nations
    H(NA, "never sell in a bear market: S&P >=20% below its high -> no cut", "block", lambda: dd <= -0.20),
    H(NA + " / " + BS, "fast mechanical re-entry: no cut while the S&P is above its 10m average (trend must confirm)",
      "block", lambda: ind["spx_trend"] > 0),
    H(NA + " / " + OP, "alt: re-enter at -30% from the high (Oppenheimer: scale in at -30%)", "block",
      lambda: dd <= -0.30),
    H(NA, "overreaction: countries down >30% in 12m bought for 3y vs S&P, 10% (CAPE leg not available)", "overlay",
      lambda: pd.DataFrame({c: rn(c, 12) < -0.30 for c in COUNTRIES}).any(axis=1), weights=reversal_w()),
    PR(NA, "real house prices +10% y/y (rent leg not available): short homebuilders+banks vs S&P for 24m",
       lambda: hold(pch(hp_real, 12) > 10, 24), ["spx"], ["sec_ITB", "sec_KBE"]),

    # ======================= batch 3, file 4: Bessent (2026)
    H(BS + " / " + NA + " / " + BR, "crowd is right / let winners run / big trend: 10% in a 12m-trend sleeve always",
      "sleeve", lambda: pd.Series(True, index=grid), asset="trend_lo", w=0.1),
    OV(BS, "yen -10% vs USD in 6m: long 10% hedged Japan equities (Japan long, yen short) funded from the S&P",
       lambda: rn("jpy", 6) < -0.10, {"eq_japan": 0.1, "jpy": -0.1, "spx": -0.1}),
    H(BS, "oil >50% above its 12m average for 3+ months (duration, not level): stocks to 0", "cut",
      lambda: (oil > 1.5 * oil.rolling(12).mean()).astype(float).rolling(3).min() == 1, level=0.0),
    OV(BS, "oil +30% in 3m and 5y breakeven +30bp in 3m (Fed delays cuts): short 10% 2y Treasuries",
       lambda: (oil3 > 30) & (chg(be5, 3) > 0.3), {"t2y": -0.1}),
    OV(BS, "Fed balance sheet still growing 12m+ after the S&P regained its high: TIPS+commodities vs long Treasuries",
       lambda: (pch(walcl, 6) > 0) & (since_recovery() >= 12), {"tips": 0.05, "commod": 0.05, "t30y": -0.1}),
    H(BS, "foreign holdings of Treasuries rising and accelerating (12m change>0 and up): 10% long Treasuries", "sleeve",
      lambda: (chg(fh, 12) > 0) & (chg(fh, 12) > chg(fh, 12).shift(3)), asset="t30y", w=0.1),
    H(BS, "Treasury-market stress: MOVE > its 36m mean + 2 SD: stocks to 0", "cut",
      lambda: move > move.rolling(36, min_periods=24).mean() + 2 * move.rolling(36, min_periods=24).std(), level=0.0),
    PR(BS, "effective tariff rate >8%: short trade-exposed EM (Korea, Taiwan, Mexico) vs S&P",
       lambda: tariff > 8, ["spx"], ["eq_korea", "eq_taiwan", "eq_mexico"]),

    # ======================= batch 3, file 5: Tropin
    H(TR, ">6 25bp-equivalent policy-rate moves (Fed+ECB) in 12m: 10% in managed futures", "sleeve",
      lambda: policy_changes() > 6, asset="trend", w=0.1),
    OV(TR, "10y-2y <0.5pt and deficit >5% GDP (duration not paid): short 10% long Treasuries",
       lambda: (curve < 0.5) & (deficit > 5), {"t30y": -0.1}),
    H(TR, "10y-2y >2pts: 10% long Treasuries", "sleeve", lambda: curve > 2, asset="t30y", w=0.1),
    H(TR, "combined vulnerability: S&P within 3% of high, CAPE top 5%, stock-bond corr>0.3, core>2.5%: stocks to 50%",
      "cut", lambda: (dd >= -0.03) & (cape_p >= 95) & (corr > 0.3) & (core_yy > 2.5), level=0.5),
    H(TR, "stock-bond correlation >0.3: hedge with gold instead of T-bills during cuts", "defensive",
      lambda: corr > 0.3, asset="gold"),
    H(TR, "macro/trend performs in corrections: managed futures instead of T-bills during cuts", "defensive",
      lambda: pd.Series(True, index=grid), asset="trend"),
    H(TR, "stocks and bonds sold together (10y +40bp and S&P -5% in a month; daily rule done monthly): stocks to 0 1m",
      "cut", lambda: (chg(tnx, 1) > 0.4) & (spx1 < -0.05), level=0.0),
    H(TR, "VIX<15 with CAPE in its top 10%: 10% in a tail-hedge fund (TAIL)", "sleeve",
      lambda: (vix < 15) & (cape_p >= 90), asset="tail", w=0.1),
    H(TR, "stagflation lite: core 3m annualised>3% and unemployment +0.2pt in 3m: stocks to 50%", "cut",
      lambda: (core3 > 3) & (chg(unr, 3) > 0.2), level=0.5),
    OV(TR, "fiscal scare: 30y +50bp in 3m without higher breakevens and term premium +30bp: short long Treasuries",
       lambda: (chg(S["fred_DGS30"], 3) > 0.5) & (chg(be10, 3) <= 0) & (chg(tp, 3) > 0.3), {"t30y": -0.1}),
    H(TR, "10y yield >=5% draws a bid: 10% long Treasuries", "sleeve", lambda: gs10 >= 5, asset="t30y", w=0.1),
    H(TR, "alt: first touch of 5% after 12m below: 10% long Treasuries for 6m", "sleeve",
      lambda: hold((gs10 >= 5) & (gs10.shift(1).rolling(12).max() < 5), 6), asset="t30y", w=0.1),
    H(TR, "permanent diversifier: 5% gold always", "sleeve", lambda: pd.Series(True, index=grid), asset="gold", w=0.05),
    H(TR, "permanent diversifier: 10% of equities ex-US always", "location", lambda: pd.Series(True, index=grid),
      assets=["intl_eq"], s=0.1),
    OV(TR, "hawkish repricing: 2y minus fed funds rises >50bp in 3m from below -50bp: short 10% 2y Treasuries",
       lambda: (chg(gs2 - ff, 3) > 0.5) & ((gs2 - ff).shift(3) < -0.5), {"t2y": -0.1}),
    OV(TR, "ECB cut more than the Fed over 12m: short 10% euro (long USD vs EUR)",
       lambda: (chg(ecb, 12) < 0) & (chg(ecb, 12) < ff12), {"eur": -0.1}),

    # ======================= batch 3, file 7: Krugman
    OV(KR, "strawman Krugman rejects: debt/GDP>100% alone -> short 10% long Treasuries (expect no edge)",
       lambda: debt_gdp > 100, {"t30y": -0.1}),
    OV(KR, "credibility loss (10y +30bp, dollar -3%, gold +5% in 3m): gold vs long Treasuries for 6m",
       lambda: hold(cred_loss(), 6), {"gold": 0.1, "t30y": -0.1}),
    OV(KR, "term premium >0.5% and up over 12m: short 10% long Treasuries",
       lambda: (tp > 0.5) & (ind["termprem"] > 0), {"t30y": -0.1}),
    H(KR, "credibility-loss regime: 15% of equities to Europe, China, Brazil for 12m", "location",
      lambda: hold(cred_loss(), 12), assets=["eq_europe", "eq_china", "eq_brazil"], s=0.15),

    # ======================= batch 3, file 8: Yass
    OV(YA, "federal debt / household net worth >20% or +2pts in 2y: short 10% long Treasuries",
       lambda: (debt_nw > 20) | (chg(debt_nw, 24) > 2), {"t30y": -0.1}),
    H(YA, "household net worth -15% y/y (wealth annihilated): 10% long Treasuries for 6m", "sleeve",
      lambda: hold(pch(nw, 12) < -15, 6), asset="t30y", w=0.1),

    # ======================= batch 3, file 9: Karniol-Tambour
    H(KT, "profits/GDP in top 10% of history and falling over 4 quarters: stocks to 50%", "cut",
      lambda: (pctl(prof_gdp) >= 90) & (chg(prof_gdp, 12) < 0), level=0.5),
    H(KT, "Kalecki profit sources (deficit + private borrowing - saving rate) down >2pts of GDP in 12m: stocks to 50%",
      "cut", lambda: chg(kalecki, 12) < -2, level=0.5),
    H(KT, "dissaving: saving rate 3pts below 5y avg, revolving credit +10% y/y, real income y/y<0: stocks to 50%", "cut",
      lambda: (psav < psav.rolling(60).mean() - 3) & (pch(revol, 12) > 10) & (pch(dpi, 12) < 0), level=0.5),
    PR(KT, "mortgage rate +1.5pts in 12m: short homebuilders+retail vs S&P for 12m",
       lambda: hold(ind["mortgage"] > 1.5, 12), ["spx"], ["sec_ITB", "sec_XRT"]),
    H(KT, "margin squeeze: unit labour costs y/y beat the GDP deflator by >1pt or labour share up 4 quarters: stocks 50%",
      "cut", lambda: ((pch(ulc, 12) - pch(defl, 12)) > 1)
      | ((lshare > lshare.shift(3)) & (lshare.shift(3) > lshare.shift(6)) & (lshare.shift(6) > lshare.shift(9))
         & (lshare.shift(9) > lshare.shift(12))), level=0.5),
    H(KT, "inelastic inflation: food+energy CPI y/y beats core by >3pts: 25% of equities to energy and metals", "location",
      lambda: fe_gap > 3, assets=["sec_XLE", "sec_XME"], s=0.25),
    H(KT, "inflation regime (core>4% and rising, or food+energy gap>3pts): hold 10% commodities directly", "sleeve",
      lambda: ((core_yy > 4) & (core_yy > core_yy.shift(3))) | (fe_gap > 3), asset="commod", w=0.1),
    H(KT, "CPI y/y >5% (until <4% and falling): stocks to 50% (higher risk premium)", "cut",
      lambda: hyst(cpi_yy > 5, (cpi_yy < 4) & (cpi_yy < cpi_yy.shift(3))), level=0.5),
    H(KT, "S&P 6m move within 5pts of -10x the 10y change (only rates priced): act on warnings", "gate",
      lambda: ((spx_l / spx_l.shift(6) - 1) * 100 - (-10 * y10_6)).abs() <= 5),
    H(KT, "S&P 6m drop >10pts worse than rate-implied (slowdown priced): no cut", "block",
      lambda: ((spx_l / spx_l.shift(6) - 1) * 100 < -10 * y10_6 - 10) & ((spx_l / spx_l.shift(6) - 1) < -0.10)),
    H(KT, "US beat ex-US by >5%/yr over 10y (exceptionalism priced): half of equities ex-US", "location",
      lambda: ((1 + rn("spx", 120)) ** 0.1 - (1 + rn("intl_eq", 120)) ** 0.1) > 0.05, assets=["intl_eq"], s=0.5),
    H(KT, "easing via transfers (deficit +5pts GDP in 12m): 10% commodities for 24m", "sleeve",
      lambda: hold(chg(deficit, 12) > 5, 24), asset="commod", w=0.1),
    H(KT, "easing via QE (Fed assets +10% in 12m, deficit change <1pt): favour financial assets, no cut", "block",
      lambda: (pch(walcl, 12) > 10) & (chg(deficit, 12).abs() < 1)),

    # ======================= batch 4, file 1: Gerstner
    H(GE, "customs revenue >1.5% of GDP (until <1%): stocks to 50%", "cut",
      lambda: hyst(cust_gdp > 1.5, cust_gdp < 1.0), level=0.5),
    H(GE, "policy-shock fall >=15% and policy uncertainty down >=30% from its 3m peak: re-enter, no cut for 6m", "block",
      lambda: hold((dd.rolling(3).min() <= -0.15) & (epud <= 0.7 * epud.rolling(3).max()), 6)),
    H(GE, "fiscal impulse proxy (deficit +1pt GDP in 12m while unemployment not rising): 25% of equities to industrials"
      " and equal weight, 12m", "location",
      lambda: hold((chg(deficit, 12) > 1) & (unr <= unr.rolling(12).mean()), 12), assets=["sec_XLI", "eqw"], s=0.25),
    OV(GE, "deficit >6% outside recession and term premium rising: short 10% long Treasuries",
       lambda: (deficit > 6) & (sahm < 0.5) & (ind["termprem"] > 0), {"t30y": -0.1}),
    H(GE, "Middle East oil hedge: Brent +10% in a month (5-day rule done monthly): 5% energy stocks for 3m", "sleeve",
      lambda: hold(pch(brent, 1) > 10, 3), asset="sec_XLE", w=0.05),

    # ======================= batch 4, file 2: Citrone
    H(CI, "Fed put: S&P >=20% down with core CPI <=3%: buy the crash, no cut for 12m", "block",
      lambda: hold((dd <= -0.20) & (core_yy <= 3), 12)),
    H(CI, "no Fed put: S&P >=20% down with core CPI >4%: stocks 50% until fed funds stop rising", "cut",
      lambda: hyst((dd <= -0.20) & (core_yy > 4), ff3 <= 0), level=0.5),
    H(CI, "QT phase: Fed assets -3% in 6m while funds rise (until 3m change >=0): stocks to 50%", "cut",
      lambda: hyst((pch(walcl, 6) < -3) & (ff3 > 0), pch(walcl, 3) >= 0), level=0.5),
    H(CI, "core inflation peak (core y/y down 3 months, m/m below 6m avg): 10% 10y Treasuries for 6m", "sleeve",
      lambda: hold((core_yy.diff() < 0) & (core_yy.diff().shift(1) < 0) & (core_yy.diff().shift(2) < 0)
                   & (core.pct_change(fill_method=None) < core.pct_change(fill_method=None).rolling(6).mean()), 6), asset="t10y", w=0.1),
    H(CI, "alt: core peak but not while oil 6m>+20% or food CPI>8% (headline caveat)", "sleeve",
      lambda: hold((core_yy.diff() < 0) & (core_yy.diff().shift(1) < 0) & (core_yy.diff().shift(2) < 0)
                   & (core.pct_change(fill_method=None) < core.pct_change(fill_method=None).rolling(6).mean()) & ~((oil6 > 20) | (food_yy > 8)), 6),
      asset="t10y", w=0.1),
    OV(CI, "global risk-off VIX>30 (until <25): long 10% dollar vs short 10% EM currencies",
       lambda: hyst(vix > 30, vix < 25), {"usd": 0.1, "em_fx": -0.1}),
    OV(CI, "inflating debt away (nominal GDP growth - 10y > 3pts): real assets vs long Treasuries",
       lambda: y10_ngdp < -3, REAL),
    H(CI, "Japan fiscal year-end ramp: 25% of equities in Japan for February-March", "location",
      lambda: pd.Series(grid.month.isin([1, 2]), index=grid), assets=["eq_japan"], s=0.25),
    H(CI, "EM equities lag FX: currency -10%/+10% in 3m -> short/long that country vs S&P for 3m (5 countries)",
      "overlay", fxlead_c, weights=fxlead_w()),
    H(CI, "top-down dials: dollar 12m<0 and 10y 12m change<0: half of equities in EM", "location",
      lambda: (ind["dollar"] < 0) & (y10_12 < 0), assets=["eq_em", "eq_brazil", "eq_korea", "eq_mexico"], s=0.5),
    H(CI, "India structural long: 10% of equities in India except when oil 6m>+30%", "location",
      lambda: ~(oil6 > 30), assets=["eq_india"], s=0.1),
    H(CI, "Brazil: real rate>5%, inflation down 3 months, commodities 12m>0: 25% of equities in Brazil for 12m",
      "location", lambda: hold(((br_rate - br_cpi) > 5) & (br_cpi.diff() < 0) & (br_cpi.diff().shift(1) < 0)
                               & (br_cpi.diff().shift(2) < 0) & (rn("commod", 12) > 0), 12),
      assets=["eq_brazil"], s=0.25),
    H(CI, "EM carry: Brazil REER >=15% below its 10y avg and carry >6pts: 10% EM local bonds for 12m", "sleeve",
      lambda: hold((reer_br <= 0.85 * reer_br.rolling(120, min_periods=60).mean()) & ((br_rate - tb3) > 6), 12),
      asset="em_local", w=0.1),
    OV(CI, "10y minus core CPI < -2 with core>3% (until real yield>0): short 10% long Treasuries",
       lambda: hyst((_rp < -2) & (core_yy > 3), _rp > 0), {"t30y": -0.1}),
    OV(CI, "BoJ yield cap while US 10y +1pt in 12m: short 10% yen",
       lambda: YCC & (y10_12 > 1), {"jpy": -0.1}),
    OV(CI, "Fed tightening (+1pt 12m) with QT: long value vs short Nasdaq-100 10% for 12m",
       lambda: hold((ff12 > 1) & (pch(walcl, 6) < 0), 12), {"value": 0.1, "ndx": -0.1}),

    # ======================= batch 4, file 3: Bessent (Real Vision 2024)
    H(BR, "fade event panics: S&P -5% month with VIX in top 5% and few warnings (<15%): no cut for 3m", "block",
      lambda: hold((spx1 < -0.05) & (pctl(vix) >= 95) & (share_ < 0.15), 3)),
    OV(BR, "fiscal-dominance endgame: deficit>6% with unemployment<5%, interest/GDP rising, gold +15% 12m: gold vs long T",
       lambda: (deficit > 6) & (unr < 5) & (chg(int_gdp, 12) > 0) & (rn("gold", 12) > 0.15),
       {"gold": 0.1, "t30y": -0.1}),
    OV(BR, "structural deficit (deficit - 2x unemployment gap) >4pts: short 10% long Treasuries",
       lambda: (deficit - 2 * (unr - nrou)) > 4, {"t30y": -0.1}),
    OV(BR, "financial conditions ease >1 SD in 6m (NFCI) with core>3%: short 10% long Treasuries",
       lambda: (chg(nfci, 6) < -1) & (core_yy > 3), {"t30y": -0.1}),
    OV(BR, "Fed still doing QE with core CPI>4% (behind the curve): short 10% long Treasuries",
       lambda: (pch(walcl, 3) > 0) & (core_yy > 4), {"t30y": -0.1}),
    OV(BR, "Abenomics: BoJ balance sheet +10% in 6m: long hedged Japan (Japan long, yen short) vs S&P for 24m",
       lambda: hold(pch(boj, 6) > 10, 24), {"eq_japan": 0.1, "jpy": -0.1, "spx": -0.1}),
    OV(BR, "fiscal dominance: debt/GDP>100% and Fed cutting with core>3%: real assets vs long Treasuries",
       lambda: (debt_gdp > 100) & (ff3 < 0) & (core_yy > 3), REAL),
    OV(BR, "kindness of strangers: foreign holdings 12m change<0 and Japan 10y +0.5pt in 12m: short long T for 6m",
       lambda: hold((chg(fh, 12) < 0) & (chg(jp10, 12) > 0.5), 6), {"t30y": -0.1}),

    # ======================= batch 4, file 4: Eisman Ep 73 (Verrone, Trennert)
    H(EI, "healthy rotation: breadth +15pts in 2m, S&P flat/down, chips >=20% off high: no cut for 6m", "block",
      lambda: hold((chg(ind["breadth"], 2) >= 15) & (rn("spx", 2) <= 0) & (ind["chips_break"] <= -20), 6)),
    H(EI, "10y yield >4.5% competes with stocks: stocks to 50%", "cut", lambda: gs10 > 4.5, level=0.5),
    H(EI + " / " + EW, "alt (relative): 10y above the S&P earnings yield or above nominal GDP growth: stocks to 50%",
      "cut", lambda: (gs10 > ey) | (y10_ngdp > 0), level=0.5),
    H(EI, "melt-up with yields jumping (S&P 12m>+25%, 10y +1.5pts): stocks to 50% for 12m", "cut",
      lambda: hold((rn("spx", 12) > 0.25) & (y10_12 > 1.5), 12), level=0.5),
    H(EI, "yields rising via breakevens (BE 6m change > real 6m change): stocks to 50%", "cut",
      lambda: (y10_6 > 0) & (bech(6) > rch(6)), level=0.5),
    H(EI, "yields rising via real rates (growth): 25% of equities to banks and industrials", "location",
      lambda: (y10_6 > 0) & (rch(6) > bech(6)), assets=["sec_KBE", "sec_XLI"], s=0.25),
    H(EI, "earnings-driven market (P/E -2 turns in 12m, EPS +10%): 25% of equities to cyclical sectors", "location",
      lambda: (chg(pe, 12) < -2) & (eps_g > 10), assets=["sec_XLI", "sec_XLB", "sec_IYT", "sec_KBE"], s=0.25),
    PR(EI + " / " + LA, "oil 6m>+30%: short Germany (Europe) vs S&P for 6m",
       lambda: hold(oil6 > 30, 6), ["spx"], ["eq_germany"]),
    H(LA, "oil 6m>+30%: 25% of equities to energy exporters (Canada, Brazil) for 6m", "location",
      lambda: hold(oil6 > 30, 6), assets=["eq_canada", "eq_brazil"], s=0.25),
    PR(EI, "copper +10% and iron ore -10% in 6m (AI capex, not China): long industrials vs China/Australia/Brazil",
       lambda: (pch(copper, 6) > 10) & (pch(iron, 6) < -10), ["sec_XLI"], ["eq_china", "eq_australia", "eq_brazil"]),
    H(EI, "concentration (narrow-leadership score >=80; top-10 weight not available): half of equities equal weight",
      "location", lambda: sc["leadership"] >= 80, assets=["eqw"], s=0.5),
    OV(EI, "full employment (unemployment <= NAIRU) and core 3m annualised>3%: short 10% long Treasuries",
       lambda: (unr <= nrou) & (core3 > 3), {"t30y": -0.1}),
    H(EI, "banks at a 12m relative high with Baa spread at a 12m low (benign credit): 25% of equities in banks",
      "location", lambda: (ind["banks"] >= ind["banks"].rolling(12).max()) & (ind["baa"] <= ind["baa"].rolling(12).min()),
      assets=["sec_KBE"], s=0.25),
    H(EI, "curve steepens >0.5pt in 6m with Sahm<0.3: 25% of equities in banks for 6m", "location",
      lambda: hold((chg(curve, 6) > 0.5) & (sahm < 0.3), 6), assets=["sec_KBE", "sec_KRE"], s=0.25),
    OV(EI, "Japan 10y above German 10y (reflation): long Japan vs short Germany 10%",
       lambda: (jp10 - de10) > 0, {"eq_japan": 0.1, "eq_germany": -0.1}),
    PR(EI, "China demand weak (iron ore 6m change<0): short Germany, Australia, China vs S&P",
       lambda: pch(iron, 6) < 0, ["spx"], ["eq_germany", "eq_australia", "eq_china"]),
    H(EI, "defensives ranking: health care instead of T-bills during cuts", "defensive",
      lambda: pd.Series(True, index=grid), asset="sec_XLV"),
    H(EI, "rate shock: 10y 12m range >1.5pts or 10y +1pt in 12m: stocks to 50%", "cut",
      lambda: ((gs10.rolling(12).max() - gs10.rolling(12).min()) > 1.5) | (y10_12 > 1), level=0.5),

    # ======================= batch 4, file 5: Oppenheimer
    H(OP, "structural bear setup (CAPE top 10%, real house prices +30% in 5y, credit gap >10pts, banks -20% rel 6m):"
      " stocks to 0 for 24m", "cut",
      lambda: hold((cape_p >= 90) & (pch(hp_real, 60) > 30) & (credit_gap > 10) & (ind["banks"] < -20), 24), level=0.0),
    H(OP, "cyclical bear setup (funds +1.5pts in 12m, core>3%, credit gap <=10): stocks to 50%", "cut",
      lambda: (ff12 > 1.5) & (core_yy > 3) & (credit_gap <= 10), level=0.5),
    H(OP, "event-driven fall (S&P -20%, credit gap <5, Fed not tightening): buy, no cut for 12m", "block",
      lambda: hold((dd <= -0.20) & (credit_gap < 5) & ~fed, 12)),
    H(OP, "recession signal (Sahm>=0.5) before a 25% fall: expect more downside, stocks to 0", "cut",
      lambda: (sahm >= 0.5) & (dd > -0.25), level=0.0),
    H(OP, "bottom checklist (3 of 4: CAPE <= 20y median, Philly Fed improving below 0, 2y 0.5pt off its 6m high, CPI 1pt"
      " off its 12m peak): re-enter", "block", checklist),
    H(OP, "real 10y +1pt in 6m: stocks to 50% for 6m", "cut", lambda: hold(rch(6) > 1, 6), level=0.5),
    H(OP, "TARA: real 10y >1%: 15% TIPS", "sleeve", lambda: _rt > 1, asset="tips", w=0.15),
    H(OP, "stagflation (core>4%, real GDP y/y<1.5%): stocks to 50%", "cut",
      lambda: (core_yy > 4) & (rgdp_yy < 1.5), level=0.5),
    H(OP, "Fed tightening with core>3%: half of equities in energy and materials", "location",
      lambda: fed & (core_yy > 3), assets=["sec_XLE", "sec_XLB"], s=0.5),
    H(OP, "higher-for-longer (10y above its 60m average): half of equities equal weight", "location",
      lambda: gs10 > gs10.rolling(60).mean(), assets=["eqw"], s=0.5),
    H(OP, "US rate edge shrinking (10y vs Germany/Japan/UK 6m change<0) and USD REER >10% above 20y avg: half ex-US 12m",
      "location", lambda: hold((chg(gs10 - foreign10, 6) < 0) & (reer_us > 1.1 * reer_us.rolling(240, min_periods=60).mean()), 12),
      assets=["intl_eq"], s=0.5),
    H(OP, "stock-bond corr>0 and core>3%: commodities instead of T-bills during cuts", "defensive",
      lambda: (corr > 0) & (core_yy > 3), asset="commod"),
    H(OP, "commodity super-cycle: drilling activity in bottom 20% of its 10y range (36m) and commodities above 10m avg:"
      " 10% commodities", "sleeve",
      lambda: hold(((drill - drill.rolling(120, min_periods=60).min())
                    / (drill.rolling(120, min_periods=60).max() - drill.rolling(120, min_periods=60).min())) <= 0.2, 36)
      & above_ma("commod"), asset="commod", w=0.1),
    H(OP, "copper 6m>0 with global demand (Korea exports y/y>0): 10% copper", "sleeve",
      lambda: (pch(copper, 6) > 0) & (kx_yy > 0), asset="copper", w=0.1),

    # ======================= batch 4, file 6: Lagarde
    H(LA, "tech boom (CAPE>30) plus fragmentation (tariff>10% or imports/GDP below 3y ago): stocks to 50%", "cut",
      lambda: (cape > 30) & ((tariff > 10) | (imp_gdp < imp_gdp.shift(36))), level=0.5),
    OV(LA, "energy pass-through: oil +30% in 3m: long 10% TIPS vs short 10% 10y Treasuries",
       lambda: oil3 > 30, {"tips": 0.1, "t10y": -0.1}),
    OV(LA + " / " + EW, "alt (Eisman): Brent +15% in a month: TIPS vs 10y Treasuries",
       lambda: pch(brent, 1) > 15, {"tips": 0.1, "t10y": -0.1}),
    OV(LA, "forward-guidance trap: core 3m annualised>4% while the Fed is not hiking: short 10% long Treasuries",
       lambda: (core3 > 4) & (ff3 <= 0), {"t30y": -0.1}),
    OV(LA, "pressure on the Fed: 10y breakeven +30bp in 3m while the Fed cuts: gold+TIPS vs long Treasuries",
       lambda: (chg(be10, 3) > 0.3) & (ff3 < 0), {"gold": 0.05, "tips": 0.05, "t30y": -0.1}),
    H(LA, "dollar fails as a haven (dollar down while S&P -8% in a month): gold instead of T-bills during cuts, 3m",
      "defensive", lambda: hold((dch(1) < 0) & (spx1 < -0.08), 3), asset="gold"),
    H(LA, "acute crisis VIX>35: dollar (UUP) instead of T-bills during cuts", "defensive",
      lambda: vix > 35, asset="usd"),

    # ======================= batch 4, file 7: Georgieva
    OV(KG, "tariff pass-through: core goods CPI 3m annualised>3% after the tariff rate rose >1pt in 12m: short long T",
       lambda: (cgoods3 > 3) & (chg(tariff, 12) > 1), {"t30y": -0.1}),
    H(KG, "no buffers (debt/GDP>100%, policy rate<2%): gold instead of T-bills during cuts", "defensive",
      lambda: (debt_gdp > 100) & (ff < 2), asset="gold"),
    H(KG, "policy space (policy rate>4%): long Treasuries instead of T-bills during cuts", "defensive",
      lambda: ff > 4, asset="t30y"),
    OV(KG, "debt service crowding out: interest/GDP +0.5pt in 2y: gold vs long Treasuries",
       lambda: chg(int_gdp, 24) > 0.5, {"gold": 0.1, "t30y": -0.1}),
    H(KG, "coordinated rescue: S&P -25% with Fed assets +5% in a month and funds cut: re-enter, no cut for 12m", "block",
      lambda: hold((dd <= -0.25) & (pch(walcl, 1) > 5) & (ff3 < 0), 12)),

    # ======================= batch 4, file 8: Eisman Weekly Wrap
    PR(EW, "positive real cash (3m bill > core CPI + 1pt): short utilities, REITs, small caps vs S&P",
       lambda: tb3 > core_yy + 1, ["spx"], ["sec_XLU", "sec_IYR", "small"]),
    H(EW, "AI capex shock proxy: semis -25% in 3m (capex-share leg not available): stocks to 50%", "cut",
      lambda: rn("sec_SMH", 3) < -0.25, level=0.5),
    H(EW, "AI unwind (chips >=20% off 12m high, leadership narrowing reversing; until chips above 10m avg): half of"
      " equities to low vol, health care, staples, insurers", "location",
      lambda: hyst((ind["chips_break"] <= -20) & (chg(ind["leadership"], 3) < 0), above_ma("sec_SMH")),
      assets=["lowvol", "sec_XLV", "sec_XLP", "sec_KIE"], s=0.5),
    H(EW, "prepare, don't predict: warnings >=15% while S&P above 10m avg: 15% of equities to defensives", "location",
      lambda: (share_ >= 0.15) & (ind["spx_trend"] > 0), assets=["sec_XLV", "sec_XLP", "sec_XLU"], s=0.15),
]

for _i, _h in enumerate(HYP):
    _h["id"] = f"B{_i + 1:03d}"
