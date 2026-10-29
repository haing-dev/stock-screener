from harness import *  # noqa
"""Batch 7 hypotheses (transcript_rules batch7.md) + Galt (X) rules cited in macro/registry.py.
D001... = batch 7 rules; G001... = @AtlasShrug1 rules. Every cond is known at the end of month t:
monthly FRED macro .shift(1) (or more), quarterly series dated at quarter start .shift(4) (GDP, imports, customs,
productivity) or .shift(6) (Z.1 balance sheets, profits), daily/weekly market series = last value of the month."""
import os

RAW = "/home/claude/stock-screener/cache/macro/raw"           # repo cache (latest-vintage FRED csv), read only


def _raw(sid):
    p = os.path.join(RAW, sid + ".csv")
    if not os.path.exists(p):
        return pd.Series(np.nan, index=grid)
    d = pd.read_csv(p)
    d = d[pd.to_numeric(d["value"], errors="coerce").notna()]
    s = pd.Series(d["value"].astype(float).values, index=pd.to_datetime(d["date"]).dt.to_period("M"))
    return s.groupby(level=0).last().reindex(grid)


# ------------------------------------------------------------------ small helpers
def B(x):
    return pd.Series(x, index=grid).reindex(grid).fillna(False).astype(bool) if not isinstance(x, pd.Series) \
        else x.reindex(grid).fillna(False).astype(bool)


def mo(sid, lag=1):            # monthly FRED macro series: value for month m is public in m+1
    return S[sid].shift(lag)


def qt(sid, lag=4):            # quarterly series dated at quarter start
    return S[sid].ffill(limit=2).shift(lag)


def hold(x, n):                # true for n months starting at each true month
    return B(x).astype(float).rolling(n, min_periods=1).max().astype(bool)


def onset(x):
    x = B(x)
    return x & ~x.shift(1, fill_value=False)


def latch(entry, exit_=None, n=None):
    """On at an entry month, off at the first exit month (or after n months); re-arms on a new entry."""
    en, ex = B(entry).values, (B(exit_).values if exit_ is not None else np.zeros(T, bool))
    out, on, k = np.zeros(T, bool), False, 0
    for i in range(T):
        if on:
            k += 1
            if ex[i] or (n is not None and k >= n):
                on = False
        if not on and en[i] and not ex[i]:
            on, k = True, 0
        out[i] = on
    return pd.Series(out, index=grid)


def ow(cond, w):               # overlay weights: {asset: weight} while cond
    c = B(cond).astype(float)
    return pd.DataFrame({a: v * c for a, v in w.items()}, index=grid)


def Lv(a):                     # price level of an R asset (NaN before it trades)
    return lvl(R[a]).where(R[a].notna().cummax())


def ch(x, n=12):
    return x - x.shift(n)


def pc(x, n=12):
    return (x / x.shift(n) - 1) * 100


def ann(x, n=3):
    return ((x / x.shift(n)) ** (12 / n) - 1) * 100


def zx(x, n=60):               # expanding z-score (known at t)
    return (x - x.expanding(n).mean()) / x.expanding(n).std()


def relm(a, b, n):             # n-month return of a minus b (decimal)
    return mom(a, n) - mom(b, n)


# ------------------------------------------------------------------ shared series (all point in time)
FF, U, G10, G2 = F["FEDFUNDS"], F["UNRATE"], F["GS10"], F["GS2"]
SPX = Lv("spx")
DD = SPX / SPX.cummax() - 1
NDX = Lv("ndx")
cut_m = B((FF - FF.shift(1)) <= -0.15)                         # Fed cut this month (monthly average fell 15bp+)
first_cut = cut_m & ~hold(cut_m.shift(1), 12)                  # first cut after 12 months without one
hike12 = ch(FF, 12)

# core CPI: official from 1998; before, core goods (35%) + services less energy (65%), same lag
_c = F["CPILFESL"]
_cg, _cs = mo("fred_CUSR0000SACL1E"), mo("fred_CUSR0000SASLE")
CORE = pc(_c).combine_first(0.35 * pc(_cg) + 0.65 * pc(_cs))
CORE3 = ann(_c).combine_first(0.35 * ann(_cg) + 0.65 * ann(_cs))
ACCEL = B(CORE3 > CORE)

# nominal GDP: PIT GDP (1992+) else real GDP x deflator (quarterly, lag 4)
_ng = (S["fred_GDPC1"] * S["fred_GDPDEF"] / 100).ffill(limit=2).shift(4)
NGDP = F["GDP"].combine_first(_ng)
NGDP_YY = pc(F["GDP"]).combine_first(pc(_ng))

# federal deficit, % of GDP (12-month sum of the Monthly Treasury Statement, lag 1)
DEF = -S["fred_MTSDS133FMS"].shift(1).rolling(12, min_periods=12).sum() / 1000 / NGDP * 100
M2YY = pc(mo("fred_M2SL"))
BASE = mo("fred_BOGMBASE")                                     # monetary base, $bn (Fed liabilities proxy pre-2002)
WAL = S["fred_WALCL"]                                          # Fed total assets, $mn (weekly, month-end)

# G3 central-bank balance-sheet 12-month flow in USD bn (local-currency change at today's FX)
EURUSD, USDJPY = _raw("EXUSEU").ffill(limit=1), _raw("EXJPUS").ffill(limit=1)
_ecb, _boj = S["fred_ECBASSETSW"], mo("fred_JPNASSETS")
G3FLOW = ch(WAL) / 1000 + ch(_ecb) * EURUSD / 1000 + ch(_boj) / (10 * USDJPY)
LIQ_NEG = B((G3FLOW < 0).where(G3FLOW.notna(), ch(BASE) < 0))

BAA_SP = ind["baa"]                                             # Baa minus 10y (stand-in for HY OAS before 2023)
BAA_P = BAA_SP.rolling(240, min_periods=120).apply(lambda a: (a <= a[-1]).mean() * 100, raw=True)  # trailing 20y pct (spread drifts up)
BANKS6 = ind["banks"]
VIX = S["px_^VIX"]
TP = F["THREEFYTP10"]
EPU = mo("fred_USEPUINDXM")
NFCI = S["fred_NFCI"]
PHIL = mo("fred_GACDFSA066MSFRBPHI")
ECBR = S["fred_ECBDFR"]
BOJR = _raw("IRSTCI01JPM156N").shift(1).combine_first(mo("fred_IRSTCB01JPM156N")).ffill(limit=3)
JGB = mo("fred_IRLTLT01JPM156N")
DOLLAR12 = ind["dollar"]                                        # dollar index, 12-month % change
OIL = F["WTISPLC"]
CUSTOMS = qt("fred_B235RC1Q027SBEA") / qt("fred_IMPGS") * 100   # effective tariff on goods AND services imports
REAL10 = G10 - CORE
trend_dn_ = B(ind["spx_trend"] < 0)
fed_hiking6 = B(ch(FF, 6) > 0.25)


# EM currency crisis: local currency down 20%+ vs USD in 6 months (USD price of it up 25%+)
def _fxcrash(sid):
    s = S[sid]
    return B(s / s.shift(6) - 1 >= 0.25)


EMFX_BRL = _fxcrash("fred_DEXBZUS")
EMFX_ANY = EMFX_BRL | _fxcrash("fred_DEXMXUS") | _fxcrash("fred_DEXKOUS") | _fxcrash("fred_DEXINUS")
EM_REL6 = relm("eq_em", "spx", 6)

# ------------------------------------------------------------------ derived tradeable assets (added to R at import)
_fee = lambda a: R[a] - FEE.get(a, 0.0)
R["b7_real"] = pd.concat([_fee("commod"), _fee("gold"), R["tips"]], axis=1).mean(axis=1)   # equal-weight real assets
R["b7_trend3"] = trend_sleeve(n=3, long_only=False)
R["b7_trend_blend"] = (trend_sleeve(n=1, long_only=False) + trend_sleeve(n=3, long_only=False)
                       + trend_sleeve(n=12, long_only=False)) / 3


def dyn(name, act):
    """Equal weight of the assets active at t (bool DataFrame), earned in t+1; inner turnover costs 0.1%."""
    A = R[list(act.columns)]
    act = act.reindex(grid).fillna(False) & A.notna()
    w = act.astype(float).div(act.sum(axis=1).replace(0, np.nan), axis=0)
    r = (w.shift(1) * A).sum(axis=1, min_count=1)
    r[w.shift(1).isna().all(axis=1)] = np.nan
    R[name] = r - 0.001 * w.fillna(0).diff().abs().sum(axis=1).shift(1).fillna(0)
    return act.any(axis=1)


# devaluation: currency down 10%+ vs USD in one month -> that country's equities for 12 months
_DEV = {"eq_brazil": "fred_DEXBZUS", "eq_mexico": "fred_DEXMXUS", "eq_korea": "fred_DEXKOUS",
        "eq_india": "fred_DEXINUS", "eq_china": "fred_DEXCHUS"}
DEV_ON = dyn("b7_deval", pd.DataFrame({a: hold(S[s] / S[s].shift(1) - 1 >= 1 / 0.9 - 1, 12) for a, s in _DEV.items()}))
# dominoes: semis +50% in 12 months -> second-order beneficiaries that have started to outperform (3m)
_smh_run = B(mom("sec_SMH", 12) >= 0.5)
DOM_ON = dyn("b7_domino", pd.DataFrame({a: _smh_run & B(relm(a, "spx", 3) > 0) for a in ("sec_XLU", "sec_XLI", "copper")}))


# ------------------------------------------------------------------ rule-specific state machines
def _ndx_ride(entry, n, stop=None, ma_exit=False):
    lv, m10 = NDX.values, ma(NDX, 10).values
    en, out, on, k, pk = onset(entry).values, np.zeros(T, bool), False, 0, 0.0
    for i in range(T):
        if on:
            k += 1
            pk = max(pk, lv[i])
            if k >= n or (stop and lv[i] <= pk * (1 - stop)) or (ma_exit and lv[i] < m10[i]):
                on = False
        if not on and en[i] and not np.isnan(lv[i]):
            on, k, pk = True, 0, lv[i]
        out[i] = on
    return pd.Series(out, index=grid)


def _brazil_ticket():
    px = Lv("eq_brazil")
    dd2 = px / px.rolling(24, min_periods=12).max() - 1
    carry = mo("fred_IRSTCI01BRM156N") - FF
    en = onset(B(dd2 <= -0.40) & B(carry > 4)).values
    pv, f3 = px.values, ch(FF, 3).values
    out, on, k, e = np.zeros(T, bool), False, 0, 0.0
    for i in range(T):
        if on:
            k += 1
            if k >= 12 or pv[i] >= 1.5 * e or (f3[i] > 0 and pv[i] <= 0.85 * e):
                on = False
        if not on and en[i]:
            on, k, e = True, 0, pv[i]
        out[i] = on
    return pd.Series(out, index=grid)


def _cut_then_10y_up():
    g, fc = G10.values, first_cut.values
    trig = np.zeros(T, bool)
    for i in range(1, T):
        if fc[i]:
            for j in range(i + 1, min(i + 4, T)):
                if g[j] - g[i - 1] >= 0.4:
                    trig[j] = True
                    break
    return hold(pd.Series(trig, index=grid), 12)


def _druck_short10():
    en = (first_cut & B(U < 4.5) & B(CORE > 2.5) & B(SPX >= 0.95 * SPX.cummax())).values
    g, ng, c = G10.values, NGDP_YY.values, CORE.values
    out, on, cm = np.zeros(T, bool), False, -99.0
    for i in range(T):
        if on:
            cm = max(cm, c[i]) if not np.isnan(c[i]) else cm
            if (g[i] >= ng[i]) or (c[i] <= cm - 0.3):
                on = False
        if not on and en[i]:
            on, cm = True, c[i]
        out[i] = on
    return pd.Series(out, index=grid)


def _live_dd_control():
    eq = (1 + run(W41).fillna(0)).cumprod()
    return latch(eq / eq.cummax() - 1 <= -0.10, eq >= eq.shift(1).rolling(3).max())


def _crash_rebound():
    lv = SPX.values
    out = np.zeros(T, bool)
    pk, low, armed, left = lv[0], lv[0], False, 0
    for i in range(T):
        x = lv[i]
        if np.isnan(x):
            continue
        if left > 0:
            left -= 1
            out[i] = True
        if x > pk:
            pk, armed = x, False
        if x <= 0.75 * pk:                       # crash of 25%+ from the peak
            armed, low = True, min(low, x) if armed else x
        if armed:
            low = min(low, x)
            if x >= 1.10 * low:                  # 10% rally off the low -> no new shorts / cuts for 6 months
                left, armed, pk = 6, False, x
                out[i] = True
    return pd.Series(out, index=grid)


def _cb_moves():
    cnt = lambda s: np.floor(s.diff().abs() / 0.25 + 0.1).clip(lower=0).rolling(12, min_periods=12).sum()   # 0.225+ = 1 move
    fed = cnt(FF)
    other = cnt(ECBR).fillna(0) + cnt(BOJR).fillna(0)
    return fed + other


def _neg_rates():
    e = hold(onset(B(ch(ECBR, 6) < 0) & B(ch(ECBR - FF, 6) <= -0.5) & B(ch(FF, 6) >= 0)) | onset(B(ECBR < 0)), 12)
    j = hold(onset(B(ch(BOJR, 6) < 0) & B(ch(BOJR - FF, 6) <= -0.5) & B(ch(FF, 6) >= 0)) | onset(B(BOJR < 0)), 12)
    return e, j


_NE, _NJ = _neg_rates()

# narrow leadership (6m): median of the 20 industries lags the S&P by 5%+
_med6 = (1 + P["rets"].fillna(0)).rolling(6).apply(np.prod, raw=True).where(P["rets"].notna().rolling(6).sum() == 6).median(axis=1) - 1
NARROW = B(_med6 - mom("spx", 6) <= -0.05)
KBE3 = relm("sec_KBE", "spx", 3)

# ------------------------------------------------------------------ sources
s1 = "BG2 DeepSeek/Tariffs/DOGE (2025-02)"
s2 = "Monetary Policy & Markets (Real Vision 2018)"
s3 = "Inside America's Economic Divide (Eisman Ep.29)"
s4 = "Boardroom Masterclass (Sheffield 2020)"
s5 = "In Good Company (NBIM 2024)"
s6 = "Jim Rogers Episode 5 (2025)"
s7 = "Tropin Macro Hive (2025-12)"
s8 = "Melt-Up making me nervous (2026-05)"
s9 = "Tropin Why Macro is Killing It (2022)"

HYP = []


def H(src, desc, kind, cond, **kw):
    HYP.append(dict(id=f"D{len([h for h in HYP if h['id'][0] == 'D']) + 1:03d}", source=src, desc=desc, kind=kind,
                    cond=cond, **kw))


def OV(src, desc, cond, w):
    H(src, desc, "overlay", cond, weights=lambda c=cond, w=w: ow(c(), w))


# ================================================================== File 1 BG2
H("Brad Gerstner - " + s1, "EPU 3m avg above 80th pct of trailing 10y -> stocks capped at 50%", "cut",
  lambda: B(EPU.rolling(3).mean() > EPU.rolling(120, min_periods=60).quantile(0.8)), level=0.5)
H("Ken Tropin - " + s7, "policy uncertainty (EPU) above its 80th pct (expanding) -> gross risk 50%", "cut",
  lambda: B(pctl(EPU) > 80), level=0.5)
OV("Brad Gerstner - " + s1, "effective tariff rate > 5% for 3+ months -> short retail (XRT) vs S&P 10%",
   lambda: B((CUSTOMS > 5).astype(float).rolling(3).min() == 1), {"sec_XRT": -0.1, "spx": 0.1})
OV("Brad Gerstner - " + s1, "effective tariff rate +2 pts in 12m -> TIPS over nominal 10y (10%)",
   lambda: hold(B(ch(CUSTOMS) >= 2), 12), {"tips": 0.1, "t10y": -0.1})
OV("Ken Tropin - " + s7, "effective tariff rate +5 pts in 12m -> TIPS over nominal 10y (10%)",
   lambda: hold(B(ch(CUSTOMS) >= 5), 12), {"tips": 0.1, "t10y": -0.1})
H("Brad Gerstner - " + s1, "deficit/GDP falls 1+ pt in 12m (credible cut) -> 10% long Treasuries for 12m", "sleeve",
  lambda: hold(B(ch(DEF) <= -1), 12), asset="t30y", w=0.1)
OV("Brad Gerstner - " + s1, "deficit/GDP widens 1+ pt in 12m outside a downturn -> short 10% long Treasuries",
   lambda: B(ch(DEF) >= 1) & B(U <= U.rolling(12).mean()), {"t30y": -0.1})
OV("Brad Gerstner - " + s1, "term premium up over 12m AND deficit widening 1+ pt -> short 10% long Treasuries",
   lambda: B(ch(TP) > 0) & B(ch(DEF) >= 1), {"t30y": -0.1})
H("Brad Gerstner - " + s1, "earnings yield (1/CAPE) below 10y yield -> stocks capped at 50%", "cut",
  lambda: B(100 / ind["cape"] - G10 < 0), level=0.5)

# ================================================================== File 2 Druckenmiller 2018
H("Stanley Druckenmiller - " + s2, "G3 central-bank 12m flow turns <= 0 after > +$500bn in past year -> stocks 50%", "cut",
  lambda: B(G3FLOW <= 0) & B(G3FLOW.rolling(12, min_periods=1).max() > 500), level=0.5)
H("Stanley Druckenmiller - " + s2, "G3 12m flow down $1tn+ vs a year earlier -> stocks 50%", "cut",
  lambda: B(ch(G3FLOW) <= -1000), level=0.5)
H("Stanley Druckenmiller - " + s2, "liquidity composite (base money 6m + M2 y/y, z) falling AND Fed hiking -> stocks 50%",
  "cut", lambda: (lambda c: B(c < c.shift(3)) & fed_hiking6)(pd.concat([zx(pc(BASE, 6)), zx(M2YY)], axis=1).mean(axis=1)),
  level=0.5)
H("Stanley Druckenmiller - " + s2, "Fed tightening AND EM lags S&P by 10%+ over 6m -> stocks 50%", "cut",
  lambda: (B(hike12 >= 1) | B(ch(WAL) < 0)) & B(EM_REL6 <= -0.10), level=0.5)
H("Stanley Druckenmiller - " + s2, "Fed hiking AND BRL down 20%+ in 6m -> stocks 50% until Fed pauses 3m", "cut",
  lambda: latch(B(hike12 > 0) & EMFX_BRL, B(FF <= FF.shift(3) + 0.05)), level=0.5)
H("Stanley Druckenmiller - " + s2, "Fed hiking AND any of BRL/MXN/KRW/INR down 20%+ in 6m -> stocks 50% until pause",
  "cut", lambda: latch(B(hike12 > 0) & EMFX_ANY, B(FF <= FF.shift(3) + 0.05)), level=0.5)
H("Stanley Druckenmiller - " + s2, "Brazil -40% from 2y high with carry > 4 pts -> 5% Brazil, 12m or +50%", "sleeve",
  _brazil_ticket, asset="eq_brazil", w=0.05)
H("Stanley Druckenmiller - " + s2, "oil +30%, dollar +5%, 2y +1 pt (12m) -> 50% into 2y Treasuries for 12m", "sleeve",
  lambda: hold(B(pc(OIL) > 30) & B(DOLLAR12 > 5) & B(ch(G2) > 1), 12), asset="t2y", w=0.5)
H("Stanley Druckenmiller - " + s2, "2y below Fed funds AND Philly Fed < 0 and falling 3m -> 25% in 2y for 12m", "sleeve",
  lambda: hold(B(G2 < FF) & B(PHIL < 0) & B(PHIL < PHIL.shift(3)), 12), asset="t2y", w=0.25)
H("Stanley Druckenmiller - " + s2, "CAPE and profits/GDP both in top fifth AND CB liquidity flow negative -> stocks 50%",
  "cut", lambda: B(sc["cape"] >= 80) & B(pctl(qt("fred_CPATAX", 6) / NGDP) >= 80) & LIQ_NEG, level=0.5)
H("Stanley Druckenmiller - " + s2, "Fed pause after NFCI +0.5 sd in 3m during hikes -> re-enter (no cuts) 12m", "block",
  lambda: hold(onset(hold(B(ch(NFCI, 3) >= 0.5) & B(hike12 >= 0.5), 12) & B(FF <= FF.shift(3) + 0.05)), 12)
  & B(FF <= FF.shift(1) + 0.1))
H("Stanley Druckenmiller - " + s2, "Fed cuts near cycle-low unemployment with S&P at new high -> 50% Nasdaq, 12m, 15% stop",
  "location", lambda: _ndx_ride(cut_m & B(U <= U.rolling(24).min() + 0.3) & B(SPX.rolling(3).max() >= SPX.cummax()), 12, stop=0.15),
  assets=["ndx"], s=0.5)
H("Stanley Druckenmiller - " + s5, "Fed cuts during an EM crisis with low unemployment -> 50% Nasdaq, 15m, exit below 10m avg",
  "location", lambda: _ndx_ride(cut_m & B(U <= U.rolling(24).min() + 0.3) & (hold(EMFX_ANY, 12) | B(EM_REL6 <= -0.10)),
                                15, ma_exit=True), assets=["ndx"], s=0.5)
H("Stanley Druckenmiller - " + s2, "Nasdaq +10% in Q4 AND liquidity flow negative -> stocks 50% in Q1", "cut",
  lambda: hold(B(pd.Series(grid.month == 12, index=grid)) & B(NDX / NDX.shift(3) - 1 >= 0.10) & LIQ_NEG, 3), level=0.5)
H("Stanley Druckenmiller - " + s2, "July-August seasonal weakness -> stocks 50% in Jul-Aug", "cut",
  lambda: B(pd.Series(np.isin(grid.month, [6, 7]), index=grid)), level=0.5)
OV("Stanley Druckenmiller - " + s2, "S&P below 10m avg -> short Nasdaq vs S&P 10% (cut high-multiple)",
   lambda: trend_dn_, {"ndx": -0.1, "spx": 0.1})
OV("Druckenmiller/Tropin - " + s5, "deficit > 5% GDP with unemployment < 5% -> short 10% long Treasuries",
   lambda: B(DEF > 5) & B(U < 5), {"t30y": -0.1})
OV("Karl Sokoloff - " + s2, "deficit > 4% GDP with unemployment < 4.5% -> short 10% long Treasuries",
   lambda: B(DEF > 4) & B(U < 4.5), {"t30y": -0.1})
OV("Stanley Druckenmiller - " + s2, "HY spread bottom decile (Baa proxy) AND Fed tightening -> short HY vs 10y 10%",
   lambda: B(BAA_P <= 10) & fed, {"hy": -0.1, "t10y": 0.1})
H("Stanley Druckenmiller - " + s2, "credit spread (Baa) 1+ pt above its 24m low -> stocks 50%", "cut",
  lambda: B(BAA_SP - BAA_SP.rolling(24, min_periods=12).min() >= 1.0), level=0.5)
H("Stanley Druckenmiller - " + s2, "credit spread (Baa) 0.5+ pt above its 24m low -> stocks 50%", "cut",
  lambda: B(BAA_SP - BAA_SP.rolling(24, min_periods=12).min() >= 0.5), level=0.5)
H("Stanley Druckenmiller - " + s2, "nonfin corporate debt/GDP +3 pts in 3y at a cycle high -> warnings acted on", "gate",
  lambda: (lambda r: B(ch(r, 36) >= 3) & B(r >= r.cummax() - 0.5))(qt("fred_BCNSDODNS", 6) / 1000 / NGDP * 100))
H("Stanley Druckenmiller - " + s2, "nominal GDP growth minus Fed funds > 4 pts for 4 quarters -> 10% real assets", "sleeve",
  lambda: B((NGDP_YY - FF > 4).astype(float).rolling(12).min() == 1), asset="b7_real", w=0.1)
H("Stanley Druckenmiller - " + s2, "wage share rising AND deficit widening (populism, no top-1% data) -> 10% real assets",
  "sleeve", lambda: B(ch(qt("fred_PRS85006173", 5)) > 0) & B(ch(DEF) > 0), asset="b7_real", w=0.1)
H("Stanley Druckenmiller - " + s2, "use 3y stock-bond correlation: growth cut with 36m corr < 0 -> long Treasuries",
  "defensive", lambda: gtt & B(R["spx"].rolling(36).corr(R["t10y"]) < 0), asset="t30y")

# ================================================================== File 3 Eisman / Liesman
H("Steve Liesman - " + s3, "semis below 10m avg OR lag S&P over 6m -> stocks 50%", "cut",
  lambda: B(~above_ma("sec_SMH")) | B(relm("sec_SMH", "spx", 6) < 0), level=0.5)
H("Steve Liesman - " + s3, "semis below 10m avg -> stocks 50%", "cut", lambda: B(~above_ma("sec_SMH").astype(bool)), level=0.5)
H("Eisman/Liesman - " + s3, "equity-only bear (S&P < 10m, Baa spread below median, banks not lagging) -> 10y Treasuries",
  "defensive", lambda: trend_dn_ & B(BAA_P < 50) & B(BANKS6 >= 0), asset="t10y")
H("Steve Eisman - " + s3, "youth jobless gap +1 pt in 12m -> stocks 50%", "cut",
  lambda: B(ch(F["LNS14024887"] - U) >= 1), level=0.5)
H("Steve Liesman - " + s3, "productivity > 2.5% y/y -> half of equities into equal-weight S&P", "location",
  lambda: B(pc(qt("fred_OPHNFB", 5), 12) > 2.5), assets=["eqw"], s=0.5)
OV("Steve Liesman - " + s3, "effective tariff rate +5 pts in 12m -> short small caps vs S&P 10%",
   lambda: hold(B(ch(CUSTOMS) >= 5), 12), {"small": -0.1, "spx": 0.1})
OV("Steve Liesman - " + s3, "Fed cuts and 10y rises 0.4+ within 3m of the first cut -> short 10% long Treasuries 12m",
   _cut_then_10y_up, {"t30y": -0.1})
OV("Steve Liesman - " + s3, "Fed cuts with core >= 3% and accelerating -> steepener (long 2y, short 30y) 12m",
   lambda: hold(cut_m & B(CORE >= 3) & ACCEL, 12), {"t2y": 0.1, "t30y": -0.1})
H("Steve Liesman - " + s3, "Fed cuts with core >= 3% and accelerating -> 10% real assets 12m", "sleeve",
  lambda: hold(cut_m & B(CORE >= 3) & ACCEL, 12), asset="b7_real", w=0.1)
OV("Steve Liesman - " + s3, "C&I standards loosened 4 quarters AND private credit/GDP +2 pts/yr -> short banks vs S&P 10%",
   lambda: B((qt("fred_DRTSCILM", 3) < 0).astype(float).rolling(12).min() == 1)
   & B(ch((qt("fred_CMDEBT", 6) + qt("fred_BCNSDODNS", 6)) / 1000 / NGDP * 100) >= 2), {"sec_KBE": -0.1, "spx": 0.1})

# ================================================================== File 4 Andrew Law
H("Andrew Law - " + s4, "cross-asset 3m time-series momentum (long/short) sleeve 20%, always", "sleeve",
  lambda: B(pd.Series(True, index=grid)), asset="b7_trend3", w=0.2)
H("Andrew Law - " + s4, "VIX above 40 in last 3 months and now 20% below that peak -> re-enter (no cuts)", "block",
  lambda: B(VIX.rolling(3).max() > 40) & B(VIX <= 0.8 * VIX.rolling(3).max()))
H("Andrew Law - " + s4, "jobless claims 4-wk avg 20%+ above 6-month low -> stocks 50%", "cut",
  lambda: B(mo("fred_IC4WSA") / mo("fred_IC4WSA").rolling(6).min() - 1 >= 0.20), level=0.5)
H("Andrew Law - " + s4, "tail hedge: 10% in TAIL when VIX < 15", "sleeve", lambda: B(VIX < 15), asset="tail", w=0.1)
H("Law/Druckenmiller - " + s4, "strategy drawdown 10%+ -> stocks 50% until a new 3-month high", "cut",
  _live_dd_control, level=0.5)
H("Andrew Law - " + s4, "after 30% crash: Fed at zero + QE + deficit +5 pts GDP -> re-enter (no cuts) 12m", "block",
  lambda: hold(onset(hold(B(DD <= -0.30), 12) & B(FF <= 0.25) & hold(B(pc(WAL.combine_first(BASE * 1000), 3) > 5), 12)
                     & B(ch(DEF, 12) >= 5)), 12))      # 12m-sum deficit (no monthly seasonality) up 5 pts in a year

# ================================================================== File 5 Druckenmiller 2024
OV("Stanley Druckenmiller - " + s5, "Fed cuts with tight credit, gold at 12m high, S&P within 5% of high -> short 10% long T 12m",
   lambda: hold(cut_m & B(BAA_P <= 20) & B(Lv("gold").rolling(2).max() >= Lv("gold").rolling(12).max())
                & B(SPX >= 0.95 * SPX.cummax()), 12), {"t30y": -0.1})
H("Stanley Druckenmiller - " + s5, "core fell 4+ pts from a peak > 6% and Fed cuts with core > 2.5% -> 10% real assets 18m",
  "sleeve", lambda: hold(cut_m & B(CORE.rolling(60).max() > 6) & B(CORE <= CORE.rolling(60).max() - 4) & B(CORE > 2.5), 18),
  asset="b7_real", w=0.1)
H("Stanley Druckenmiller - " + s5, "M2 growth > 15% y/y -> 10% real assets for 12m", "sleeve",
  lambda: hold(B(M2YY > 15), 12), asset="b7_real", w=0.1)
H("Stanley Druckenmiller - " + s5, "M2 growth > 10% y/y -> 10% real assets for 12m", "sleeve",
  lambda: hold(B(M2YY > 10), 12), asset="b7_real", w=0.1)
OV("Stanley Druckenmiller - " + s5, "first cut with unemp < 4.5, core > 2.5, S&P near high -> short 10y 25% until core peaks or 10y >= NGDP",
   _druck_short10, {"t10y": -0.25})
OV("Stanley Druckenmiller - " + s5, "10y 1+ pt below NGDP growth and core accelerating -> short 10% long T until 10y >= NGDP",
   lambda: latch(B(NGDP_YY - G10 >= 1) & ACCEL, B(G10 >= NGDP_YY)), {"t30y": -0.1})
H("Stanley Druckenmiller - " + s5, "no narrow leadership (median industry vs S&P 6m) in past 12m -> no cuts", "block",
  lambda: ~hold(NARROW, 12))
H("Stanley Druckenmiller - " + s5, "no narrow leadership unless banks broaden (3m) in past 12m -> no cuts", "block",
  lambda: ~hold(NARROW & B(KBE3 <= 0), 12))
OV("Stanley Druckenmiller - " + s5, "Fed cutting (6m) while core accelerates -> short 10% long Treasuries",
   lambda: B(ch(FF, 6) < 0) & ACCEL, {"t30y": -0.1})
H("Stanley Druckenmiller - " + s5, "energy 50%+ below 5y high AND drilling output -40% y/y -> 10% energy stocks 24m", "sleeve",
  lambda: hold(onset(B(Lv("sec_XLE") / Lv("sec_XLE").rolling(60, min_periods=36).max() - 1 <= -0.5)
                     & B(pc(mo("fred_IPN213111N")) <= -40)), 24), asset="sec_XLE", w=0.1)
H("Stanley Druckenmiller - " + s5, "currency -10% in a month -> 20% of equities into that country for 12m", "location",
  lambda: DEV_ON, assets=["b7_deval"], s=0.2)
H("Stanley Druckenmiller - " + s5, "semis +50% 12m -> 20% of equities into outperforming XLU/XLI/copper", "location",
  lambda: DOM_ON, assets=["b7_domino"], s=0.2)
H("Stanley Druckenmiller - " + s5, "growth-trend cut -> non-stock share in cross-asset trend instead of bills", "defensive",
  lambda: gtt, asset="trend_ls")
H("Druckenmiller (Hyman) - " + s5, "dollar 50%/oil 25%/10y 25% 12m-change composite z > 1.5 -> 50% into 10y", "sleeve",
  lambda: B(zx(0.5 * zx(DOLLAR12) + 0.25 * zx(pc(OIL)) + 0.25 * zx(ch(G10))) > 1.5), asset="t10y", w=0.5)
H("Druckenmiller (Hyman) - " + s5, "same composite z > 1.0 -> 50% into 10y", "sleeve",
  lambda: B(zx(0.5 * zx(DOLLAR12) + 0.25 * zx(pc(OIL)) + 0.25 * zx(ch(G10))) > 1.0), asset="t10y", w=0.5)
H("Stanley Druckenmiller - " + s5, "S&P +50% in 12m then 3m momentum < 12m/4 -> stocks 50%", "cut",
  lambda: B(hold(B(mom("spx", 12) > 0.5), 12)) & B(mom("spx", 3) < mom("spx", 12) / 4), level=0.5)

# ================================================================== File 6 Jim Rogers
_WB = ["wb_agriculture_", "wb_energy", "wb_metals__&_minerals"]
H("Jim Rogers - " + s6, "commodity group 50%+ below 10y high and back above 10m avg -> 10% commodities 36m", "sleeve",
  lambda: hold(onset(np.logical_or.reduce([B(mo(g) / mo(g).rolling(120, min_periods=60).max() - 1 <= -0.5) & B(mo(g) > ma(mo(g), 10))
                                           for g in _WB])), 36), asset="commod", w=0.1)
H("Jim Rogers - " + s6, "real commodity group price in bottom fifth (expanding) and above 10m avg -> 10% commodities 36m",
  "sleeve", lambda: hold(onset(np.logical_or.reduce([B(pctl(mo(g) / mo("fred_CPIAUCSL"), 120) <= 20) & B(mo(g) > ma(mo(g), 10))
                                                     for g in _WB])), 36), asset="commod", w=0.1)
H("Jim Rogers - " + s6, "China above its 10m avg -> 10% of equities in China", "location",
  lambda: B(above_ma("eq_china")), assets=["eq_china"], s=0.1)
H("Jim Rogers - " + s6, "Fed balance sheet/GDP +5 pts in 12m -> 10% real assets 36m", "sleeve",
  lambda: hold(B(ch(WAL / 1000 / NGDP * 100).combine_first(ch(BASE / NGDP * 100)) >= 5), 36), asset="b7_real", w=0.1)
H("Jim Rogers - " + s6, "after a 25% crash and a 10% rebound -> no cuts for 6 months", "block", _crash_rebound)
H("Jim Rogers - " + s6, "grains index +25% in 6m -> 10% commodities", "sleeve",
  lambda: B(pc(mo("wb_grains"), 6) > 25), asset="commod", w=0.1)

# ================================================================== File 7 Tropin 2025
OV("Ken Tropin - " + s7, "term premium below 20y median, deficit > 5%, Fed cutting -> steepener until 2s10s > 1.5 or TP top fifth",
   lambda: latch(B(TP < TP.rolling(240, min_periods=120).median()) & B(DEF > 5) & B(ch(FF) <= -0.5),
                 B(G10 - G2 > 1.5) | B(pctl(TP) > 80)), {"t2y": 0.1, "t30y": -0.1})
OV("Ken Tropin - " + s7, "BoJ +0.25 in 6m or JGB 10y at 10y high -> short 10% long T, long 10% yen",
   lambda: B(ch(BOJR, 6) >= 0.25) | B(JGB >= JGB.rolling(120, min_periods=60).max()), {"t30y": -0.1, "jpy": 0.1})
OV("Stanley Druckenmiller - " + s2, "JGB +0.3 in 6m or 12m high, AND ECB assets and Fed assets shrinking (6m) -> short long T, long yen",
   lambda: (B(ch(JGB, 6) >= 0.3) | B(JGB >= JGB.rolling(12).max())) & B(ch(_ecb, 6) <= 0) & B(ch(WAL, 6) < 0),
   {"t30y": -0.1, "jpy": 0.1})
H("Ken Tropin - " + s7, "narrow leadership top fifth AND CAPE > 30 -> 10% tail hedge (TAIL)", "sleeve",
  lambda: B(sc["leadership"] >= 80) & B(ind["cape"] > 30), asset="tail", w=0.1)
H("Ken Tropin - " + s7, "after an emergency Fed cut, stay out until S&P is back above its 10m avg", "cut",
  lambda: hold(B(FF - FF.shift(1) <= -0.4), 6) & trend_dn_, level=0.0)
OV("Ken Tropin - " + s7, "year before an election AND deficit widening -> steepener",
   lambda: B(pd.Series(grid.year % 2 == 1, index=grid)) & B(ch(DEF) > 0), {"t2y": 0.1, "t30y": -0.1})
H("Ken Tropin - " + s7, "midterm-year Q4 strength -> no cuts Oct-Dec of midterm years", "block",
  lambda: B(pd.Series((grid.year % 4 == 2) & np.isin(grid.month, [9, 10, 11]), index=grid)))

# ================================================================== File 8 Eisman melt-up
OV("Steve Eisman - " + s8, "S&P +12% (or Nasdaq +20%) in 2 months -> short Nasdaq vs S&P 10% for 3m (trim high flyers)",
   lambda: hold(B(mom("spx", 2) >= 0.12) | B(mom("ndx", 2) >= 0.20), 3), {"ndx": -0.1, "spx": 0.1})
H("Steve Eisman - " + s8, "oil +30% in 12m while S&P at a 12m high -> 10% energy stocks", "sleeve",
  lambda: B(pc(OIL) > 30) & B(SPX >= SPX.rolling(12).max()), asset="sec_XLE", w=0.1)
OV("Steve Eisman - " + s8, "PPI +1% m/m or +5% y/y -> short 10% long Treasuries for 6m",
   lambda: hold(B(pc(F["PPIACO"], 1) >= 1) | B(pc(F["PPIACO"]) >= 5), 6), {"t30y": -0.1})
OV("Steve Eisman - " + s8, "10y crosses above 4.5% -> short small caps + homebuilders vs S&P for 3m",
   lambda: hold(B(G10 > 4.5) & B(G10.shift(1) <= 4.5), 3), {"small": -0.05, "sec_ITB": -0.05, "spx": 0.1})
OV("Steve Eisman - " + s8, "10y at a 3-year high -> short small caps + homebuilders vs S&P for 3m",
   lambda: hold(B(G10 >= G10.rolling(36).max()), 3), {"small": -0.05, "sec_ITB": -0.05, "spx": 0.1})
OV("Steve Eisman - " + s8, "oil +30% in 3m -> long energy vs transports 10% for 6m",
   lambda: hold(B(pc(OIL, 3) >= 30), 6), {"sec_XLE": 0.1, "sec_IYT": -0.1})

# ================================================================== File 9 Tropin 2022
H("Ken Tropin - " + s9, "10+ 25bp-equivalent moves by Fed+ECB+BoJ in 12m -> 25% cross-asset trend", "sleeve",
  lambda: B(_cb_moves() >= 10), asset="trend_ls", w=0.25)
OV("Ken Tropin - " + s9, "Fed 12m change minus BoJ 12m change > 2 pts -> short yen 10% until BoJ hikes",
   lambda: latch(B(ch(FF) - ch(BOJR) > 2), B(BOJR - BOJR.shift(1) > 0)), {"jpy": -0.1})
H("Ken Tropin - " + s9, "Fed most hawkish of Fed/ECB/BoJ (12m) -> long USD 10% (5% if real dollar top decile)", "overlay",
  lambda: B(hike12 > 0) & B(hike12 > ch(ECBR).fillna(-99)) & B(hike12 > ch(BOJR).fillna(-99)),
  weights=lambda: ow(B(hike12 > 0) & B(hike12 > ch(ECBR).fillna(-99)) & B(hike12 > ch(BOJR).fillna(-99)), {"usd": 1.0})
  .mul(np.where(pctl(mo("fred_RBUSBIS"), 60) > 90, 0.05, 0.1), axis=0))
OV("Ken Tropin - " + s9, "core > 4%, accelerating, Fed hiking -> short 10% 10y Treasuries",
   lambda: B(CORE > 4) & ACCEL & B(hike12 > 0), {"t10y": -0.1})
H("Ken Tropin - " + s9, "energy CPI > 20% y/y and oil above 10m avg -> 10% energy stocks", "sleeve",
  lambda: B(pc(mo("fred_CPIENGSL")) > 20) & B(OIL > ma(OIL, 10)), asset="sec_XLE", w=0.1)
OV("Ken Tropin - " + s9, "Fed eases within 18m of a core peak > 5% with core > 3% -> short 10% long T 12m",
   lambda: hold(cut_m & B(CORE.rolling(18).max() > 5) & B(CORE > 3), 12), {"t30y": -0.1})
OV("Ken Tropin - " + s9, "2y 1+ pt below Fed funds (4 cuts priced) while core > 3% -> short 10% 2y (fade cuts)",
   lambda: B(G2 - FF <= -1.0) & B(CORE > 3), {"t2y": -0.1})
H("Ken Tropin - " + s9, "after core peaked > 6%, inflation hot until core < 3% for 6m -> 10% real assets", "sleeve",
  lambda: latch(B(CORE > 6), B((CORE < 3).astype(float).rolling(6).min() == 1)), asset="b7_real", w=0.1)
H("Ken Tropin - " + s9, "job openings per unemployed > 1.5 -> 10% real assets", "sleeve",
  lambda: B(mo("fred_JTSJOL", 2) / (mo("fred_PAYEMS", 2) * (U / 100) / (1 - U / 100)) > 1.5), asset="b7_real", w=0.1)
H("Ken Tropin - " + s9, "after Fed +3 pts in 12m, Sahm trigger -> long Treasuries instead of bills", "defensive",
  lambda: hold(B(hike12 >= 3), 24) & B(ind["jobs_alarm"] >= 0.5), asset="t30y")
OV("Ken Tropin - " + s9, "2s10s inverted, 1y inflation expectations > 3%, term premium < 0 -> short long T, long 2y",
   lambda: B(G10 - G2 < 0) & B(mo("fred_MICH") > 3) & B(TP < 0), {"t30y": -0.1, "t2y": 0.1})
H("Ken Tropin - " + s9, "core > 3%: trim to 50% at S&P all-time highs (trading range)", "cut",
  lambda: B(CORE > 3) & B(SPX >= SPX.cummax()), level=0.5)
H("Ken Tropin - " + s9, "core > 3%: buy S&P 15%+ below its high (no cuts)", "block",
  lambda: B(CORE > 3) & B(DD <= -0.15))
H("Ken Tropin - " + s9, "blend of 1/3/12m cross-asset momentum sleeve 20%, always", "sleeve",
  lambda: B(pd.Series(True, index=grid)), asset="b7_trend_blend", w=0.2)
H("Ken Tropin - " + s9, "gold 10% only when above 10m avg and real yield or dollar falling (12m)", "sleeve",
  lambda: B(above_ma("gold")) & (B(ch(REAL10) < 0) | B(DOLLAR12 < 0)), asset="gold", w=0.1)
OV("Ken Tropin - " + s9, "real 10y +1 pt in 12m and dollar rising -> short gold 10%",
   lambda: B(ch(REAL10) >= 1) & B(DOLLAR12 > 0), {"gold": -0.1})
H("Ken Tropin - " + s9, "unless core < 2.5% and Fed on hold, 25% in cross-asset trend", "sleeve",
  lambda: ~(B(CORE < 2.5) & B(hike12.abs() < 0.5)), asset="trend_ls", w=0.25)
H("Ken Tropin - " + s9, "bitcoin 2% only above its 10m avg", "sleeve", lambda: B(above_ma("btc")), asset="btc", w=0.02)
OV("Stanley Druckenmiller - " + s2, "deficit widening 1+ pt AND real Fed funds rising (loose fiscal, tight money) -> long USD 10%",
   lambda: B(ch(DEF) >= 1) & B(ch(FF - CORE) > 0), {"usd": 0.1})
OV("Stanley Druckenmiller - " + s2, "ECB/BoJ go negative or cut 0.5+ vs a non-easing Fed -> short that currency 10% for 12m",
   lambda: _NE | _NJ, None)
HYP[-1]["weights"] = lambda: pd.DataFrame({"eur": -0.1 * _NE.astype(float), "jpy": -0.1 * _NJ.astype(float)}, index=grid)

H("Stanley Druckenmiller - " + s2, "conviction: squeeze AND EM stress AND G3 liquidity drop all on (NFIB leg missing) -> stocks 0%",
  "cut", lambda: (B(pc(OIL) > 30) & B(DOLLAR12 > 5) & B(ch(G2) > 1)) & B(EM_REL6 <= -0.10) & (B(ch(G3FLOW) <= -1000) | LIQ_NEG),
  level=0.0)

# ================================================================== Galt (X) rules from macro/registry.py
_G = [("staples_disc", "2026-10-15", "staples beat discretionary (6m)"), ("breakdowns", "2026-09-23", "industries 20%+ below 12m high"),
      ("transports", "2026-09-02", "transports lag industrials (6m)"), ("homebuilders", "2026-06-09", "homebuilders vs market below 2y peak"),
      ("vix", "2026-10-15", "VIX"), ("junk", "2026-10-20", "junk bonds lag Treasuries (3m)"),
      ("banks", "2026-10-14", "bank stocks lag market (6m)"), ("dollar_break", "2026-10-05", "dollar vs 12m high"),
      ("chips_break", "2026-10-14", "chip stocks vs 12m high"), ("dollar", "2026-06-11", "dollar 12m change"),
      ("mcap_gdp", "2026-08-08", "stock market value / GDP"), ("hh_equity", "2026-08-08", "household equity share"),
      ("cape", "2026-08-08", "CAPE")]


def G(date, desc, kind, cond, **kw):
    HYP.append(dict(id=f"G{len([h for h in HYP if h['id'][0] == 'G']) + 1:03d}", source=f"Galt (X) - {date}", desc=desc,
                    kind=kind, cond=cond, **kw))


for _k, _d, _t in _G:
    G(_d, f"{_t} in its worst fifth (score >= 80) -> stocks 50%", "cut", lambda k=_k: B(sc[k] >= 80), level=0.5)
G("2026-10-15", "VIX above 30 (panic) -> stocks 50%", "cut", lambda: B(VIX > 30), level=0.5)
G("2026-07-14", "S&P 500 below its 10-month average -> stocks 50%", "cut", lambda: trend_dn_, level=0.5)
G("2026-10-05", "dollar at a new 12-month high (breakout) -> stocks 50%", "cut", lambda: B(ind["dollar_break"] >= 0), level=0.5)
G("2026-10-14", "chip stocks 20%+ below their 12-month high -> stocks 50%", "cut", lambda: B(ind["chips_break"] <= -20), level=0.5)

_REG = {"late": ("2026-06-09/06-24/06-16", ["XLE", "XLV", "XBI", "XLP"], ["ITB", "IYT", "XRT", "ITA", "SMH"]),
        "overheating": ("2026-10-16", ["XLE", "XLB", "XME", "GDX"], ["IGV", "XBI", "IYR", "XLU", "ITB"]),
        "recovery": ("2026-10-16/08-28", ["ITB", "KBE", "KRE", "XLB", "XME", "XLI", "IYT", "XRT"], ["XLU", "XLP", "SMH", "IGV"])}
for _st, (_d, _o, _u) in _REG.items():
    _w = {**{"sec_" + a: 0.2 / len(_o) for a in _o}, **{"sec_" + a: -0.2 / len(_u) for a in _u}}
    G(_d, f"state '{_st}': long its favoured sectors / short its avoided ones (20% each side)", "overlay",
      lambda s=_st: B(P["reg"] == s), weights=lambda s=_st, w=_w: ow(B(P["reg"] == s), w))
_wS = {**{"sec_" + a: 0.2 / 4 for a in ["XLP", "XLV", "XLU", "KIE"]},
       **{"sec_" + a: -0.2 / 6 for a in ["SMH", "IGV", "XBI", "KRE", "XME", "IYT"]}}
G("2026-10-16/10-05", "market stress high: long safe sectors / short crowded ones (20% each side)", "overlay",
  lambda: B(P["high"]), weights=lambda: ow(B(P["high"]), _wS))
