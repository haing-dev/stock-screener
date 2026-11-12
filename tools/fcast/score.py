"""Forecast ledger step 2.3 (script): score ledger rows mechanically, as written in
docs/research/forecasts/SCORING_RULES.md v1 (committed 5e058b3, frozen). Descriptive only; never a source of weights.

usage: python3 tools/fcast/score.py <macro-vault worktree> [--raw <cache/macro/raw>] [--no-freeze]
  -> <vault>/pipeline/forecasts/outcomes.csv     one row per ledger row that enters a pool (status, reason, outcome)
  -> <vault>/pipeline/forecasts/scored_frozen.csv resolved rows, written once (rules section 1); later runs reuse them
Interpretations where the rules text left a case open are tagged GAP-n in the code and listed in the scorecard."""
import csv, datetime as dt, gzip, json, math, os, re, sys

import numpy as np
import pandas as pd

RULES = "SCORING_RULES v1 (5e058b3)"
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
RAW_DEFAULT = os.path.join(REPO, "cache", "macro", "raw")
BASE_FROM, BASE_TO = pd.Timestamp("1990-01-31"), pd.Timestamp("2010-12-31")
DEFAULT_H = {"direction": 12, "relative": 12, "macro": 12, "event": 12, "volatility": 6, "structural": 36}
MAX_H = 60

# ---------------------------------------------------------------- families and bands (rules section 2)
# fam: (band at 12 months, measure, scaled by sqrt(h/12), price family for level parsing)
FAM = {"eq": (0.04, "pct", True, True), "reit": (0.04, "pct", True, True), "trend": (0.04, "pct", True, True),
       "comm": (0.06, "pct", True, True), "fx": (0.02, "pct", True, True), "btc": (0.15, "pct", True, True),
       "liq": (0.02, "pct", True, True), "house": (0.02, "pct", True, True),
       "yield": (0.25, "pt", True, False), "policy": (0.10, "pt", False, False),
       "credit": (0.10, "pct", True, False), "volidx": (0.15, "pct", False, False),
       "infl": (0.3, "pt", False, False), "unemp": (0.2, "pt", False, False), "gdp": (0.5, "pt", False, False),
       "debt": (1.0, "pt", False, False), "deficit": (0.10, "pct", False, False)}
VOL_RATIO_BAND = 0.10


def band_for(fam, h):
    b, _, scaled, _ = FAM[fam]
    return b * math.sqrt(min(max(h, 1.0), 60.0) / 12.0) if scaled else b


GROUPS = {
    "equity": "US_EQ US_TECH US_SMALL EU_EQ JP_EQ CN_EQ IN_EQ EM_EQ GLOBAL_EQ EQ_SECTOR EQ_SINGLE EQ_VALUE_VS_GROWTH",
    "rates": "US_POLICY_RATE US_2Y US_10Y US_30Y US_CURVE US_REAL_YIELD US_TERM_PREMIUM EU_RATES JP_RATES UK_RATES OTHER_RATES",
    "fx": "USD EURUSD USDJPY GBPUSD USDCNY EM_FX OTHER_FX",
    "commodities": "GOLD SILVER OIL NATGAS COPPER URANIUM AGRI COMMODITIES OTHER_COMMODITY",
    "credit and vol": "CREDIT_SPREADS PRIVATE_CREDIT VIX RATES_VOL",
    "macro": "US_GROWTH US_RECESSION US_INFLATION US_JOBS US_DEFICIT_DEBT GLOBAL_GROWTH CN_GROWTH EU_GROWTH JP_INFLATION LIQUIDITY",
    "other": "BTC REAL_ESTATE TREND_FOLLOWING HEDGE_FUNDS POLICY_EVENT GEOPOLITICS OTHER"}
GROUP_OF = {c: g for g, cs in GROUPS.items() for c in cs.split()}
EQUITY_CODES = set(GROUPS["equity"].split())


def family_of(code):
    return GROUP_OF.get((code or "").split(">")[0], "other")


# ---------------------------------------------------------------- keyword tables (rules section 3)
def kw(text, table):
    t = (text or "").lower()
    for pat, val in table:
        if re.search(pat, t):
            return val
    return None


SECTOR_KW = [(r"semiconductor|semis\b|chip", "SMH"), (r"software", "IGV"), (r"biotech", "XBI"), (r"regional bank", "KRE"),
             (r"bank", "KBE"), (r"insur", "KIE"), (r"financial", "XLF"), (r"junior miner", "GDXJ"),
             (r"gold miner|gold stock", "GDX"), (r"uranium", "URA"), (r"copper miner", "COPX"), (r"lithium", "LIT"),
             (r"rare earth", "REMX"), (r"homebuild", "XHB"), (r"defen[cs]e|aerospace", "ITA"), (r"airline", "JETS"),
             (r"e&p|exploration", "XOP"), (r"energy|oil stock|oil compan", "XLE"), (r"mining|miner", "XME"),
             (r"health|pharma", "XLV"), (r"utilit", "XLU"), (r"staples", "XLP"), (r"retail", "XRT"),
             (r"discretionary|consumer", "XLY"), (r"transport", "IYT"), (r"industrial", "XLI"),
             (r"material|chemical", "XLB"), (r"communication|telecom|media", "VOX"), (r"real estate|reit", "VNQ"),
             (r"tech", "XLK")]
COMMOD_KW = [(r"platinum", "r/D_PL_F"), (r"palladium", "r/Y_PA_F"), (r"cocoa", "r/Y_CC_F"), (r"coffee", "r/D_KC_F"),
             (r"sugar", "r/D_SB_F"), (r"cotton", "r/D_CT_F"), (r"wheat", "r/D_ZW_F"), (r"corn", "r/D_ZC_F"),
             (r"soy", "r/D_ZS_F"), (r"cattle", "r/D_LE_F"), (r"heating oil", "r/D_HO_F"), (r"gasoline", "r/D_RB_F"),
             (r"iron ore", "PIORECRUSDM"), (r"alumini?um", "r/PALUMUSDM"), (r"nickel", "r/PNICKUSDM"),
             (r"zinc", "r/PZINCUSDM"), (r"lithium", "r/Y_LIT")]
# GAP-1: "country name" and "currency keyword" read as the listed code plus its English name / adjective.
RATES_KW = [(r"canad", "CA"), (r"australia", "AU"), (r"ital", "IT"), (r"france|french", "FR"), (r"spain|spanish", "ES"),
            (r"netherlands|dutch", "NL"), (r"switzerland|swiss", "CH"), (r"swed", "SE"), (r"norw", "NO"),
            (r"denmark|danish", "DK"), (r"korea", "KR"), (r"mexic", "MX"), (r"new zealand", "NZ"),
            (r"south africa", "ZA"), (r"austria", "AT"), (r"belgi", "BE"), (r"portug", "PT")]
# (keyword, DEX series, series quotes USD per foreign unit?)
FX_KW = [(r"\baud\b|australian dollar|aussie", "USAL", True), (r"\bnzd\b|new zealand dollar|kiwi", "USNZ", True),
         (r"\bcad\b|canadian dollar|loonie", "CAUS", False), (r"\bchf\b|swiss franc", "SZUS", False),
         (r"\bmxn\b|mexican peso", "MXUS", False), (r"\bbrl\b|brazilian real", "BZUS", False),
         (r"\binr\b|rupee", "INUS", False), (r"\bkrw\b|korean won", "KOUS", False), (r"\bzar\b|\brand\b", "SFUS", False),
         (r"\bnok\b|norwegian krone", "NOUS", False), (r"\bsek\b|swedish krona", "SDUS", False),
         (r"\bhkd\b|hong kong dollar", "HKUS", False), (r"\btwd\b|taiwan dollar", "TAUS", False)]
INDEX_KW = [(r"nasdaq[ -]?100|\bndx\b", None), (r"s&p|\bspx\b", "r/D__GSPC"), (r"nasdaq", "r/D__IXIC"),
            (r"russell", "r/D__RUT"), (r"nikkei", "r/D__N225"), (r"euro ?stoxx|stoxx ?50", "r/D__STOXX50E"),
            (r"\bdax\b", "r/D__GDAXI"), (r"ftse", "r/D__FTSE"), (r"\bcac\b", "r/D__FCHI"), (r"hang seng", "r/D__HSI"),
            (r"shanghai", "r/D_000001_SS"), (r"sensex", "r/D__BSESN"), (r"nifty", "r/Y__NSEI"), (r"kospi", "r/D__KS11"),
            (r"dxy|dollar index", "r/D_DX_Y_NYB"), (r"brent", "r/DCOILBRENTEU")]


def spec_for(code, text):
    """-> dict describing how to measure a single code, or a string (reason it is not scored)."""
    t = (text or "").lower()
    M = lambda s, fam, L=False, rel=None, proxy=None, base_na=False: dict(
        kind="mkt", dir=s, fam=fam, L=L, rel=rel, proxy=proxy, base_na=base_na)
    if code == "US_EQ": return M("r/D__GSPC", "eq", True, "r/D_SPY")
    if code == "US_TECH": return M("r/D__IXIC", "eq", False, "r/D_QQQ")
    if code == "US_SMALL": return M("r/D__RUT", "eq", True, "r/D_IWM")
    if code == "EU_EQ": return M("r/D__STOXX50E", "eq", True, "r/D_EZU", "r/D__FCHI")
    if code == "JP_EQ": return M("r/D__N225", "eq", True, "r/D_EWJ")
    if code == "CN_EQ":
        s = "r/D_000001_SS" if re.search(r"shanghai|a-share|csi", t) else "r/D__HSI"
        return dict(M(s, "eq", True, "r/D_MCHI", "r/Y_FXI"), relproxy="r/Y_FXI")
    if code == "IN_EQ": return M("r/D__BSESN", "eq", False, "r/D_INDA")
    if code == "EM_EQ": return M("r/Y_EEM", "eq", False, "r/Y_EEM")
    if code == "GLOBAL_EQ": return dict(M("r/Y_ACWI", "eq", False, "r/Y_ACWI", "r/D_SPY"), relproxy="r/D_SPY")
    if code == "EQ_SECTOR":
        e = kw(t, SECTOR_KW)
        return M("Y:" + e, "eq", False, "Y:" + e) if e else "sector keyword not matched"
    if code == "EQ_SINGLE": return "no free series (EQ_SINGLE)"
    if code == "EQ_VALUE_VS_GROWTH": return dict(kind="pair", a="r/Y_IWD", b="r/Y_IWF", fam="eq")
    if code == "US_POLICY_RATE":
        return dict(kind="macro", m="r/FEDFUNDS", tf="level", lag=1, fam="policy", shift=1, rel="r/Y_BIL")
    if code in ("US_2Y", "US_10Y", "US_30Y"):
        n = code[3:-1]
        return M("r/DGS" + n, "yield", True, {"2": "Y_SHY", "10": "r/D_IEF", "30": "r/D_TLT"}[n])
    if code == "US_CURVE": return M("r/T10Y2Y", "yield", False)
    if code == "US_REAL_YIELD": return M("r/DFII10", "yield", True, "r/Y_TIP")
    if code == "US_TERM_PREMIUM": return M("THREEFYTP10", "yield", False)
    if code == "EU_RATES":
        return M("r/ECBDFR", "policy", True) if re.search(r"ecb|policy|hike|cut", t) else M("cb:DE10", "yield", True)
    if code == "JP_RATES":
        return M("cb:JP2", "yield", True) if re.search(r"boj|policy|hike|cut", t) else M("cb:JP10", "yield", True)
    if code == "UK_RATES":
        return M("cb:GB5", "yield", True) if re.search(r"boe|policy|hike|cut", t) else M("cb:GB10", "yield", True)
    if code == "OTHER_RATES":
        c = kw(t, RATES_KW)
        return M("r/IRLTLT01%sM156N" % c, "yield", False) if c else "country keyword not matched"
    if code == "USD": return M("r/D_DX_Y_NYB", "fx", True, "r/Y_UUP")
    if code == "EURUSD": return M("r/DEXUSEU", "fx", True)
    if code == "USDJPY": return M("r/DEXJPUS", "fx", True)
    if code == "GBPUSD": return M("r/DEXUSUK", "fx", True)
    if code == "USDCNY": return M("r/DEXCHUS", "fx", True)
    if code == "EM_FX": return M("inv:r/DTWEXEMEGS", "fx", False)
    if code == "OTHER_FX":
        hit = next(((s, usd_per) for pat, s, usd_per in FX_KW if re.search(pat, t)), None)
        if not hit:
            return "currency keyword not matched"
        s, usd_per = hit
        ccy = s[:2] if not usd_per else s[2:]
        pair = re.search(r"\busd\s*/?\s*([a-z]{3})\b|\b([a-z]{3})\s*/?\s*usd\b", t)
        if pair and pair.group(1):            # USDxxx quoted: up = foreign units per USD rise
            inv = usd_per
        elif pair and pair.group(2):          # xxxUSD quoted: up = USD per foreign unit rises
            inv = not usd_per
        else:                                 # no pair: up = the foreign currency gains on USD
            inv = not usd_per
        return M(("inv:" if inv else "") + "r/DEX" + s, "fx", False)
    if code == "GOLD": return M("r/D_GC_F", "comm", True, "r/D_GLD")
    if code == "SILVER": return M("r/D_SI_F", "comm", True, "r/Y_SLV")
    if code == "OIL": return M("r/DCOILBRENTEU" if "brent" in t else "r/DCOILWTICO", "comm", True, "r/Y_USO")
    if code == "NATGAS": return M("r/D_NG_F", "comm", True, "r/Y_UNG")
    if code == "COPPER": return M("r/D_HG_F", "comm", True, "r/Y_CPER")
    if code == "URANIUM": return M("r/PURANUSDM", "comm", True, "r/Y_URA")
    if code == "AGRI":
        s = kw(t, COMMOD_KW)
        return dict(M(s or "r/Y_DBA", "comm", False, "r/Y_DBA", None if s else "r/PFOODINDEXM"), relproxy="r/PFOODINDEXM")
    if code == "COMMODITIES":
        return dict(M("r/Y_DBC", "comm", False, "r/Y_DBC", "r/PALLFNFINDEXM"), relproxy="r/PALLFNFINDEXM")
    if code == "OTHER_COMMODITY":
        s = kw(t, COMMOD_KW)
        return M(s, "comm", False) if s else "commodity keyword not matched"
    if code == "CREDIT_SPREADS": return M("credit", "credit", False, "r/Y_HYG", "credit:BAA")
    if code == "PRIVATE_CREDIT": return "no direction convention (PRIVATE_CREDIT)"
    if code == "VIX": return M("r/D__VIX", "volidx", True)
    if code == "RATES_VOL": return M("r/Y__MOVE", "volidx", True)
    if code == "US_GROWTH": return dict(kind="macro", m="r/GDPC1", tf="yoy4q", lag=30, fam="gdp")
    if code == "US_RECESSION": return dict(kind="rec")
    if code == "US_INFLATION":
        if "core pce" in t: return dict(kind="macro", m="r/PCEPILFE", tf="yoy12", lag=30, fam="infl")
        if "pce" in t: return dict(kind="macro", m="r/PCEPI", tf="yoy12", lag=30, fam="infl")
        if "core" in t: return dict(kind="macro", m="r/CPILFESL_FR", tf="yoy12", lag=15, fam="infl")
        return dict(kind="macro", m="r/CPIAUCNS", tf="yoy12", lag=15, fam="infl")
    if code == "US_JOBS": return dict(kind="macro", m="r/UNRATE_FR", tf="level", lag=7, fam="unemp")
    if code == "US_DEFICIT_DEBT":
        if "debt" in t: return dict(kind="macro", m="r/GFDEGDQ188S", tf="level", lag=90, fam="debt")
        return dict(kind="macro", m="r/MTSDS133FMS", tf="sum12neg", lag=15, fam="deficit")
    if code == "GLOBAL_GROWTH": return "no free series (GLOBAL_GROWTH)"
    if code == "CN_GROWTH": return dict(kind="weo", iso=["CHN"], ind="NGDP_RPCH", fam="gdp")
    if code == "EU_GROWTH": return dict(kind="weo", iso=["DEU", "FRA", "ITA", "ESP"], ind="NGDP_RPCH", fam="gdp")
    if code == "JP_INFLATION": return dict(kind="weo", iso=["JPN"], ind="PCPIPCH", fam="infl")
    if code == "LIQUIDITY":
        # GAP-2: lags for WRESBAL, ECBASSETSW (weekly) and JPNASSETS (monthly) are not listed: 1 day weekly, 30 monthly.
        if re.search(r"\bm2\b|money supply", t): return dict(kind="macro", m="r/M2SL", tf="level", lag=30, fam="liq")
        if "reserves" in t: return dict(kind="macro", m="r/WRESBAL", tf="level", lag=1, fam="liq")
        if "ecb" in t: return dict(kind="macro", m="r/ECBASSETSW", tf="level", lag=1, fam="liq")
        if "boj" in t: return dict(kind="macro", m="r/JPNASSETS", tf="level", lag=30, fam="liq")
        return dict(kind="macro", m="r/WALCL", tf="level", lag=1, fam="liq")
    if code == "BTC": return M("r/Y_BTC_USD", "btc", True, "r/Y_BTC_USD", base_na=True)
    if code == "REAL_ESTATE":
        if re.search(r"(home|house|housing) price", t):
            return dict(kind="macro", m="r/CSUSHPINSA", tf="level", lag=60, fam="house", rel="r/Y_VNQ")
        return M("r/Y_VNQ", "reit", False, "r/Y_VNQ")
    if code == "TREND_FOLLOWING": return M("tsmom", "trend", False, "r/Y_DBMF")
    return "no free series (%s)" % code


# ---------------------------------------------------------------- data access
class Series:
    def __init__(self, s, freq, name):
        self.s = s.sort_index()
        self.freq, self.name = freq, name
        self.idx = self.s.index.values
        self.v = self.s.values.astype(float)
        self.first = self.s.index[0] if len(self.s) else None
        self.last = self.s.index[-1] if len(self.s) else None

    def at_or_before(self, d):
        i = np.searchsorted(self.idx, np.datetime64(d), side="right") - 1
        return (None, None) if i < 0 else (pd.Timestamp(self.idx[i]), self.v[i])

    def first_after(self, d):
        i = np.searchsorted(self.idx, np.datetime64(d), side="right")
        return (None, None) if i >= len(self.v) else (pd.Timestamp(self.idx[i]), self.v[i])

    def window(self, a, b, left_open=True):
        lo = np.searchsorted(self.idx, np.datetime64(a), side="right" if left_open else "left")
        hi = np.searchsorted(self.idx, np.datetime64(b), side="right")
        return self.v[lo:hi], self.idx[lo:hi]


def _dv(path):
    df = pd.read_csv(path, dtype=str, keep_default_na=False)
    d = pd.to_datetime(df.iloc[:, 0], errors="coerce")
    v = pd.to_numeric(df.iloc[:, 1], errors="coerce")
    s = pd.Series(v.values, index=pd.DatetimeIndex(d)).dropna()
    s = s[s.index.notna()]
    return s[~s.index.duplicated(keep="last")].sort_index()


def _infer(s):
    if len(s) < 3:
        return "D"
    gap = np.median(np.diff(s.index.values).astype("timedelta64[D]").astype(float))
    return "D" if gap <= 5 else "W" if gap <= 10 else "M" if gap <= 40 else "Q" if gap <= 120 else "A"


def to_month_end(s, yahoo=False):
    """Monthly value = last observation stamped in the month, indexed at month end. Yahoo: an incomplete last month
    (last stamp before the month's last weekday) is dropped."""
    if not len(s):
        return s
    last_stamp = s.index[-1]
    g = s.groupby(s.index.to_period("M")).last()
    g.index = g.index.to_timestamp(how="end").normalize()
    if yahoo and last_stamp.day != 1:
        me = last_stamp + pd.offsets.MonthEnd(0)
        lastwd = pd.bdate_range(me - pd.Timedelta(days=6), me)[-1]
        if last_stamp < lastwd:
            g = g.iloc[:-1]
    return g


class Data:
    def __init__(self, raw=RAW_DEFAULT):
        self.raw, self.rd = raw, os.path.join(raw, "research")
        self.cache, self._weo = {}, None

    def path(self, name):
        if name.startswith("r/"):
            return os.path.join(self.rd, name[2:] + ".csv")
        return os.path.join(self.raw, name + ".csv")

    def get(self, name):
        if name not in self.cache:
            try:
                self.cache[name] = self._load(name)
            except FileNotFoundError:
                self.cache[name] = None
        return self.cache[name]

    def _load(self, name):
        if name.startswith("inv:"):
            b = self.get(name[4:])
            return None if b is None else Series(1.0 / b.s, b.freq, name)
        if name.startswith("Y:"):
            e = name[2:]
            p = "r/Y_" + e if os.path.exists(self.path("r/Y_" + e)) else "Y_" + e
            return self.get(p)
        if name == "credit:BAA":
            a, b = self.get("r/DBAA"), self.get("r/DGS10")
            j = pd.concat([a.s, b.s], axis=1, join="inner").dropna()
            return Series(j.iloc[:, 0] - j.iloc[:, 1], "D", name)
        if name == "credit:HY":
            return self.get("r/BAMLH0A0HYM2")
        if name == "tsmom":
            x = pd.read_excel(os.path.join(self.rd, "aqr_tsmom_factors.xlsx"), "TSMOM Factors", header=None)
            hdr = next(i for i in range(len(x)) if str(x.iloc[i, 1]).strip() == "TSMOM")
            body = x.iloc[hdr + 1:, :2].copy()
            body = body[pd.to_datetime(body[0], errors="coerce").notna()]
            r = pd.Series(pd.to_numeric(body[1], errors="coerce").values, index=pd.to_datetime(body[0])).dropna()
            if r.abs().median() > 0.5:          # file in percent
                r = r / 100.0
            lvl = 100.0 * (1.0 + r).cumprod()
            return Series(to_month_end(lvl), "M", name)
        if name.startswith("cb:"):
            return Series(self._cb(name[3:]), "D", name)
        p = self.path(name)
        s = _dv(p)
        f = _infer(s)
        base = os.path.basename(p)
        if f == "M":
            s = to_month_end(s, yahoo=base.startswith("Y_"))
        elif f == "Q":
            s.index = (s.index + pd.offsets.QuarterEnd(0)).normalize()
        elif f == "A":
            s.index = (s.index + pd.offsets.YearEnd(0)).normalize()
        return Series(s, f, name)

    def _cb(self, key):
        if key.startswith("DE"):
            rows = list(csv.reader(open(os.path.join(self.rd, "cb_de_%sy.csv" % key[2:]), encoding="utf-8-sig")))
            d = [(r[0], r[1]) for r in rows if len(r) > 1 and re.match(r"\d{4}-\d{2}-\d{2}$", r[0].strip('"'))]
            s = pd.Series(pd.to_numeric([v for _, v in d], errors="coerce"), index=pd.to_datetime([k for k, _ in d]))
        elif key.startswith("JP"):
            col, out = key[2:] + "Y", {}
            for f in ("cb_jp_jgb_all.csv", "cb_jp_jgb_recent.csv"):
                p = os.path.join(self.rd, f)
                if not os.path.exists(p):
                    continue
                rows = list(csv.reader(open(p, encoding="cp932", errors="replace")))
                hdr = next((r for r in rows if r and r[0].strip().lower() == "date"), None)
                if not hdr or col not in [h.strip().upper() for h in hdr]:
                    continue
                c = [h.strip().upper() for h in hdr].index(col)
                for r in rows:
                    if len(r) > c and r[0].strip()[:1] and r[0].strip()[:1] in "SHR12":
                        dd = _jp_date(r[0])
                        try:
                            out[dd] = float(r[c])
                        except ValueError:
                            pass
            s = pd.Series(out)
        else:
            rows = list(csv.reader(open(os.path.join(self.rd, "cb_gb_yields.csv"))))
            hdr = [h.strip().upper() for h in rows[0]]
            c = hdr.index({"GB10": "IUDMNPY", "GB5": "IUDSNPY"}[key])
            d = [(r[0], r[c]) for r in rows[1:] if len(r) > c]
            s = pd.Series(pd.to_numeric([v for _, v in d], errors="coerce"),
                          index=pd.to_datetime([k for k, _ in d], format="%d %b %Y", errors="coerce"))
        s = s.dropna()
        s = s[s.index.notna()]
        return s[~s.index.duplicated(keep="last")].sort_index()

    def weo(self):
        if self._weo is None:
            w = pd.read_csv(os.path.join(self.rd, "imf_weo_vintages.csv.gz"),
                            usecols=["iso3", "indicator_code", "publication_date", "target_year", "forecast_value",
                                     "latest_actual_year"])
            w = w[pd.to_numeric(w.latest_actual_year, errors="coerce") >= pd.to_numeric(w.target_year, errors="coerce")]
            w = w.sort_values("publication_date").groupby(["iso3", "indicator_code", "target_year"]).first()
            self._weo = w
        return self._weo

    def weo_value(self, isos, ind, year):
        w = self.weo()
        vals = []
        for iso in isos:
            try:
                vals.append(float(w.loc[(iso, ind, year), "forecast_value"]))
            except KeyError:
                return None
        return float(np.mean(vals))

    def stamps(self):
        out = {}
        for d, k in ((self.raw, "raw"), (self.rd, "research")):
            try:
                out[k] = json.load(open(os.path.join(d, "manifest.json"))).get("fetched")
            except Exception:
                out[k] = None
        return out


def _jp_date(t):
    t = t.strip()
    if t[:1].isdigit():
        return pd.Timestamp(t.replace("/", "-"))
    era = {"S": 1925, "H": 1988, "R": 2018}[t[0]]
    y, m, d = (int(x) for x in t[1:].split("."))
    return pd.Timestamp(era + y, m, d)


# ---------------------------------------------------------------- helpers
def resolved_made(made, prec):
    made = str(made)
    if prec == "day":
        return pd.Timestamp(made[:10])
    if prec == "month":
        return pd.Timestamp(made[:7] + "-01") + pd.offsets.MonthEnd(0)
    if prec == "quarter":
        return pd.Timestamp(made[:7] + "-01") + pd.offsets.QuarterEnd(0)
    return None


def add_months(d, h):
    whole = int(math.floor(h))
    return d + pd.DateOffset(months=whole) + pd.Timedelta(days=round((h - whole) * 30.44))


def rnd(h):
    return int(math.floor(h + 0.5))            # GAP-3: round half up (not banker's rounding)


def busdays(a, b):
    return int(np.busday_count(a.date(), b.date()))


def category(change, band):
    return "up" if change > band else "down" if change < -band else "flat"


def measure(fam):
    return FAM[fam][1]


def chg(a, b, fam):
    return (b / a - 1.0) if measure(fam) == "pct" else (b - a)


WANT = {"up": "up", "outperform": "up", "higher_vol": "up", "down": "down", "underperform": "down", "lower_vol": "down",
        "flat": "flat", "range": "flat"}


# ---------------------------------------------------------------- level parsing (rules section 2, Level)
NUM = re.compile(r"([+\-−–])?\s*\$?\s*(\d+(?:,\d{3})*(?:\.\d+)?|\.\d+)\s*(k\b|bps?\b|%|pts?\b|percent\b)?")
YEARWORD = re.compile(r"\b(?:jan\w*|feb\w*|mar\w*|apr\w*|may|jun\w*|jul\w*|aug\w*|sep\w*|oct\w*|nov\w*|dec\w*|q[1-4]|by|in|"
                      r"until|end|of|from|since)\s+(?:19|20)\d\d\b")
MOVEWORD = re.compile(r"\b(up|down|gain\w*|fall\w*|rise\w*|rising|drop\w*)\b")


def parse_level(level, fam):
    """-> None or dict(kind=threshold|range|move|moverange, ...) in series units (pct series: moves as fractions)."""
    if not level:
        return None
    t = str(level).lower()
    t = YEARWORD.sub(" ", t)                       # GAP-4: a year after a month word / by / in is a date, not a level
    ms = list(NUM.finditer(t))
    if not ms:
        return None
    price = FAM[fam][3]
    pct_measure = measure(fam) == "pct"

    def val(m, unit=None):
        x = float(m.group(2).replace(",", ""))
        u = (m.group(3) or unit or "").strip()
        if u == "k":
            x *= 1000
        if u.startswith("bp"):
            x /= 100.0
        return x, u

    rng = None
    if len(ms) >= 2:
        between = t[ms[0].end():ms[1].start()].strip()
        s2 = ms[1].group(1)
        if between in ("", "-", "–", "to", "and") and (between or s2 in ("-", "–")):
            if between == "and" and "between" not in t[:ms[0].start()]:
                rng = None
            else:
                rng = (ms[0], ms[1])
        if rng is None:
            return None                            # GAP-5: several numbers that are not a range -> level ignored
    unit_any = (ms[0].group(3) or (rng[1].group(3) if rng else "") or "").strip()
    signed = bool(ms[0].group(1)) or (rng is not None and between != "" and bool(rng[1].group(1)))
    is_move = signed or bool(MOVEWORD.search(t)) or (unit_any == "%" and price)
    if rng:
        a, _ = val(rng[0], unit_any)
        b, _ = val(rng[1], unit_any)
        sa = -1 if rng[0].group(1) in ("-", "−", "–") else 1
        sb = -1 if (between != "" and rng[1].group(1) in ("-", "−", "–")) else (sa if between == "" else 1)
        a, b = sa * a, sb * b
        if is_move:                                # GAP-6: a signed or %-on-price range is a range of moves
            if pct_measure:
                a, b = a / 100.0, b / 100.0
            return dict(kind="moverange", lo=min(a, b), hi=max(a, b))
        return dict(kind="range", lo=min(a, b), hi=max(a, b))
    x, u = val(ms[0])
    sgn = -1 if ms[0].group(1) in ("-", "−", "–") else (1 if ms[0].group(1) == "+" else 0)
    if is_move:
        if pct_measure:
            x /= 100.0
        return dict(kind="move", m=x, sign=sgn)
    side = ">=" if re.search(r"above|over|at least|>", t) else "<=" if re.search(r"below|under|<", t) else None
    return dict(kind="threshold", T=x, side=side)


def level_series_name(spec, text, code):
    k = kw(text, INDEX_KW)
    if k is not None or re.search(INDEX_KW[0][0], (text or "").lower()):
        return k                                   # an index name decides (None = Nasdaq 100: level ignored)
    return spec["dir"] if spec.get("L") else None


# ---------------------------------------------------------------- window values
def mkt_window(S, made, E, h):
    """-> dict(start_date, start, end_date, end) | ('open', resolve_date) | ('unscored', reason)."""
    if S is None or S.last is None:
        return ("unscored", "series file missing")
    if S.freq in ("M", "Q", "A"):
        if h < 1:
            return ("unscored", "horizon under 1 month on a monthly series")
        sm = (made + pd.Timedelta(days=1)) + pd.offsets.MonthEnd(0)
        em = (sm + pd.offsets.MonthEnd(rnd(h))) if rnd(h) > 0 else sm
        if em > S.last:
            return ("open", em)
        sd, sv = S.at_or_before(sm)
        ed, ev = S.at_or_before(em)
        if sd is None or sd != sm or ed != em:
            return ("unscored", "data gap")
        return dict(start_date=sd, start=sv, end_date=ed, end=ev)
    if E > S.last:
        return ("open", E)
    sd, sv = S.first_after(made)
    if sd is None:
        return ("open", E)
    if busdays(made, sd) > 10:
        return ("unscored", "data gap" if S.first <= made else "series starts after made date")
    ed, ev = S.at_or_before(E)
    if ed is None or ed <= sd:
        return ("unscored", "horizon too short for the data")
    if busdays(ed, E) > 10:
        return ("unscored", "data gap")
    return dict(start_date=sd, start=sv, end_date=ed, end=ev)


def month_points(S, h):
    """Base-window start points: month ends 1990-01..2010-12 (or from series start) with t + h <= 2010-12-31."""
    if S is None or S.first is None:
        return []
    first = max(BASE_FROM, (S.first + pd.offsets.MonthEnd(0)).normalize())
    pts = pd.date_range(first, BASE_TO, freq="ME")
    return [t for t in pts if add_months(t, h) <= BASE_TO]


def base_changes(S, h, monthly=False):
    """-> list of (t, start, end) for the base window."""
    out = []
    for t in month_points(S, h):
        e = (t + pd.offsets.MonthEnd(rnd(h))) if (monthly or S.freq != "D" and S.freq != "W") else add_months(t, h)
        sd, sv = S.at_or_before(t)
        ed, ev = S.at_or_before(e)
        if sd is None or ed is None or (t - sd).days > 15 or (e - ed).days > 15:
            continue
        out.append((t, sv, ev))
    return out


def outcome_hit(want, change, band, lev, end_level, start_level):
    """Forecast hit from the band, or from the level when it is usable."""
    if lev is None:
        return {"up": change > band, "down": change < -band, "flat": abs(change) <= band}[want]
    k = lev["kind"]
    if k == "move":
        if lev["sign"] == -1:
            m = -abs(lev["m"])
        elif lev["sign"] == 1:
            m = abs(lev["m"])
        else:
            m = -abs(lev["m"]) if want == "down" else abs(lev["m"])
        if want == "flat":
            return abs(change) <= abs(m)
        return change >= m if m > 0 else change <= m
    if k == "moverange":
        return lev["lo"] <= change <= lev["hi"]
    if k == "range":
        return lev["lo"] <= end_level <= lev["hi"]
    T, side = lev["T"], lev["side"]
    if side is None:
        side = ">=" if want == "up" else "<=" if want == "down" else None
    if side == ">=":
        return end_level >= T
    if side == "<=":
        return end_level <= T
    return abs(end_level / T - 1.0) <= band if lev.get("pctband") else abs(end_level - T) <= band


def base_hit(want, ch, band, lev, start_level, fam, base_start=None):
    """Same outcome test on one base window; thresholds become the move they need from the forecast's start level."""
    if lev is None:
        return {"up": ch > band, "down": ch < -band, "flat": abs(ch) <= band}[want]
    k = lev["kind"]
    if k in ("move", "moverange"):
        return outcome_hit(want, ch, band, lev, None, None)
    if k == "range":
        lo, hi = chg(start_level, lev["lo"], fam), chg(start_level, lev["hi"], fam)
        return lo <= ch <= hi
    need = chg(start_level, lev["T"], fam)
    side = lev["side"] or (">=" if want == "up" else "<=" if want == "down" else None)
    if side == ">=":
        return ch >= need
    if side == "<=":
        return ch <= need
    return abs(ch - need) <= band


# ---------------------------------------------------------------- scoring one row
def score_row(r, D):
    """r: ledger row dict with extra keys made_r (Timestamp) and h (float). Returns dict of outcome fields."""
    code, text, d = r["variable_code"], r["variable_text"], r["direction"]
    made, h = r["made_r"], r["h"]
    E = add_months(made, h)
    o = dict(end_target=E.date().isoformat())
    if "probability" in r and r["probability"] not in ("", None):
        o["probability"] = float(r["probability"])
    legs = code.split(">")
    if len(legs) == 2:
        return _score_relative(r, D, o, legs, E)
    sp = spec_for(code, text)
    if isinstance(sp, str):
        return dict(o, status="unscored", reason=sp)
    if sp["kind"] == "pair":
        return _score_relative(r, D, o, ["_IWD", "_IWF"], E, pair=sp)
    if d in ("outperform", "underperform") and code in EQUITY_CODES:
        return _score_relative(r, D, o, legs, E)
    if d in ("event_yes", "event_no"):
        return _score_event(r, D, o, sp, E)
    if d in ("outperform", "underperform") and len(legs) == 1:
        d = "up" if d == "outperform" else "down"         # other codes: up/down (rules section 2)
    if sp["kind"] == "rec":
        return dict(o, status="unscored", reason="direction not usable for an event variable")
    if d in ("higher_vol", "lower_vol"):
        if code in ("VIX", "RATES_VOL"):
            d = "up" if d == "higher_vol" else "down"
        else:
            return _score_vol(r, D, o, sp, E, d)
    want = WANT[d]
    if sp["kind"] == "macro":
        return _score_macro(r, D, o, sp, E, want)
    if sp["kind"] == "weo":
        return _score_weo(r, D, o, sp, E, want)
    return _score_mkt(r, D, o, sp, E, want)


def _credit_series(D, made):
    hy = D.get("r/BAMLH0A0HYM2")
    if hy is not None and hy.first is not None and hy.first <= made - pd.DateOffset(months=12):
        return hy, "r/BAMLH0A0HYM2"
    return D.get("credit:BAA"), "credit:BAA"


def _trend_cat(S, made, fam, start_level=None):
    a = S.at_or_before(made - pd.DateOffset(months=12))
    b = S.at_or_before(made)
    if a[0] is None or b[0] is None or (made - b[0]).days > 45 or a[0] == b[0]:
        return None
    return category(chg(a[1], b[1], fam), band_for(fam, 12))


def _base(Sbase, h, fn):
    if Sbase is None:
        return None, None
    rows = base_changes(Sbase, h)
    if len(rows) < 60:
        return None, len(rows)
    hits = [fn(sv, ev) for _, sv, ev in rows]
    return float(np.mean(hits)), len(rows)


def _score_mkt(r, D, o, sp, E, want):
    code, text, made, h = r["variable_code"], r["variable_text"], r["made_r"], r["h"]
    fam = sp["fam"]
    if sp["dir"] == "credit":
        S, sname = _credit_series(D, made)
    else:
        S, sname = D.get(sp["dir"]), sp["dir"]
    o.update(series=sname, fam=fam)
    w = mkt_window(S, made, E, h)
    if isinstance(w, tuple):
        return dict(o, status=w[0], reason=w[1] if w[0] == "unscored" else "", resolve_date=(
            w[1].date().isoformat() if w[0] == "open" else ""))
    band = band_for(fam, h)
    change = chg(w["start"], w["end"], fam)
    lev = parse_level(r.get("level"), fam)
    lev_note, end_level, start_level = "", None, None
    if lev is not None:
        lname = level_series_name(sp, text, code) if lev["kind"] in ("threshold", "range") else sname
        if lname is None:
            lev, lev_note = None, "level ignored (no level series)"
        elif lev["kind"] in ("threshold", "range"):
            L = S if lname == sname else D.get(lname)
            lw = mkt_window(L, made, E, h)
            if isinstance(lw, tuple):
                if lw[0] == "open":
                    return dict(o, status="open", reason="", resolve_date=lw[1].date().isoformat())
                lev, lev_note = None, "level ignored (level series: %s)" % lw[1]
            else:
                start_level, end_level = lw["start"], lw["end"]
                bounds = [lev["T"]] if lev["kind"] == "threshold" else [lev["lo"], lev["hi"]]
                bad = any((not (0.25 * start_level <= x <= 4 * start_level)) if FAM[fam][3] or measure(fam) == "pct"
                          else abs(x - start_level) > 10 for x in bounds)
                if bad:
                    lev, lev_note = None, "level ignored (unit mismatch)"
                else:
                    lev["pctband"] = measure(fam) == "pct"
                    lev_note = "level %s on %s" % (lev["kind"], lname)
                    vals, _ = L.window(lw["start_date"], lw["end_date"], left_open=True)
                    if lev["kind"] == "threshold" and len(vals):
                        side = lev["side"] or (">=" if want == "up" else "<=" if want == "down" else None)
                        o["touch_hit"] = (vals.max() >= lev["T"]) if side == ">=" else (vals.min() <= lev["T"]) if side == "<=" else ""
        else:
            lev_note = "level %s" % lev["kind"]
    hit = outcome_hit(want, change, band, lev, end_level, start_level)
    cat = category(change, band)
    o.update(status="resolved", reason="", start_date=w["start_date"].date().isoformat(), start_value=w["start"],
             end_date=w["end_date"].date().isoformat(), end_value=w["end"], resolve_date=w["end_date"].date().isoformat(),
             change=change, band=band, category=cat, want=want, hit=bool(hit), level_use=lev_note,
             sign_hit=(change > 0 if want == "up" else change < 0 if want == "down" else ""),
             move_band=(change / band * (1 if want == "up" else -1) if want != "flat" else ""))
    # baselines
    base_S, base_name = S, sname
    if sp.get("base_na"):
        base_S = None
    elif sp["dir"] == "credit" or len(month_points(S, h)) < 60:
        if sp.get("proxy"):
            base_S, base_name = D.get(sp["proxy"]), sp["proxy"]
    sl = start_level if start_level is not None else w["start"]
    if lev is not None and lev["kind"] in ("threshold", "range") and base_S is not None and base_S is not S:
        pass                                   # thresholds convert to a required move, applied to the proxy too
    p, n = _base(base_S, h, lambda a, b: base_hit(want, chg(a, b, fam), band_for(fam, h), lev, sl, fam))
    o.update(base_p=p if p is not None else "", base_n=n or "", base_series=base_name if p is not None else "")
    tc = _trend_cat(S, made, fam)
    o.update(trend_cat=tc or "", trend_hit=(tc == cat) if tc else "", agree_trend=(tc == want) if tc else "")
    return o


def _ret_series(D, code, text, rel_override=None):
    if rel_override:
        return D.get(rel_override), rel_override, None
    sp = spec_for(code, text)
    if isinstance(sp, str) or not sp.get("rel"):
        return None, None, None
    fam = sp.get("fam")
    legband = fam if fam and FAM[fam][1] == "pct" and fam not in ("credit", "volidx", "deficit", "liq", "house") else None
    if sp.get("kind") == "macro" and code != "REAL_ESTATE":
        legband = None
    if code == "REAL_ESTATE":
        legband = "reit"
    return D.get(sp["rel"]), sp["rel"], dict(band=legband, proxy=sp.get("relproxy"))


def _monthly(S):
    if S.freq in ("M", "Q", "A"):
        return S
    return Series(to_month_end(S.s, yahoo=True), "M", S.name + "@M")


def _score_relative(r, D, o, legs, E, pair=None):
    code, text, d, made, h = r["variable_code"], r["variable_text"], r["direction"], r["made_r"], r["h"]
    if pair:
        A, an, ia = D.get(pair["a"]), pair["a"], dict(band="eq", proxy=None)
        B, bn, ib = D.get(pair["b"]), pair["b"], dict(band="eq", proxy=None)
    else:
        if len(legs) == 1:
            bench = "r/Y_ACWI" if code == "US_EQ" else "r/D_SPY"
            legs = [code, None]
        else:
            bench = None
        A, an, ia = _ret_series(D, legs[0], text)
        if bench:
            B, bn, ib = D.get(bench), bench, dict(band="eq", proxy="r/D_SPY" if bench == "r/Y_ACWI" else None)
        else:
            B, bn, ib = _ret_series(D, legs[1], text)
    o.update(series="%s - %s" % (an, bn), fam="relative")
    if A is None or B is None:
        return dict(o, status="unscored", reason="relative leg without a total-return series")
    if d in ("event_yes", "event_no", "higher_vol", "lower_vol"):
        return dict(o, status="unscored", reason="relative call with an event or volatility direction")
    want = {"outperform": "up", "up": "up", "underperform": "down", "down": "down", "flat": "flat", "range": "flat"}[d]
    bands = [band_for(x["band"], h) for x in (ia, ib) if x and x.get("band")]
    if not bands:
        return dict(o, status="unscored", reason="no % band for either relative leg")      # GAP-7
    band = max(bands)
    monthly = A.freq != "D" or B.freq != "D"
    A2, B2 = (_monthly(A), _monthly(B)) if monthly else (A, B)
    wa, wb = mkt_window(A2, made, E, h), mkt_window(B2, made, E, h)
    for w in (wa, wb):
        if isinstance(w, tuple) and w[0] == "open":
            return dict(o, status="open", reason="", resolve_date=w[1].date().isoformat())
    for w in (wa, wb):
        if isinstance(w, tuple):
            return dict(o, status="unscored", reason=w[1])
    if not monthly and wa["start_date"] != wb["start_date"]:
        # GAP-8: legs on different trading calendars: B taken at A's start/end dates (last observation on or before)
        wb = dict(start_date=wa["start_date"], start=B.at_or_before(wa["start_date"])[1],
                  end_date=wa["end_date"], end=B.at_or_before(wa["end_date"])[1])
    change = (wa["end"] / wa["start"] - 1) - (wb["end"] / wb["start"] - 1)
    cat = category(change, band)
    hit = {"up": change > band, "down": change < -band, "flat": abs(change) <= band}[want]
    o.update(status="resolved", reason="", start_date=wa["start_date"].date().isoformat(),
             end_date=wa["end_date"].date().isoformat(), resolve_date=wa["end_date"].date().isoformat(),
             change=change, band=band, category=cat, want=want, hit=bool(hit),
             sign_hit=(change > 0 if want == "up" else change < 0 if want == "down" else ""),
             move_band=(change / band * (1 if want == "up" else -1) if want != "flat" else ""))
    # base rate on the return difference (leg proxies where listed)
    def leg_base(S, info):
        if S is not None and len(month_points(S, h)) >= 60:
            return S
        px = info.get("proxy") if info else None
        return D.get(px) if px else None
    BA, BB = leg_base(A, ia), leg_base(B, ib)
    p, n = None, None
    if BA is not None and BB is not None:
        BAm, BBm = _monthly(BA), _monthly(BB)
        ra = {t: (sv, ev) for t, sv, ev in base_changes(BAm, h, monthly=True)}
        rb = {t: (sv, ev) for t, sv, ev in base_changes(BBm, h, monthly=True)}
        common = sorted(set(ra) & set(rb))
        if len(common) >= 60:
            diffs = [(ra[t][1] / ra[t][0] - 1) - (rb[t][1] / rb[t][0] - 1) for t in common]
            p = float(np.mean([{"up": x > band, "down": x < -band, "flat": abs(x) <= band}[want] for x in diffs]))
            n = len(common)
    o.update(base_p=p if p is not None else "", base_n=n or "", base_series="legs" if p is not None else "")
    # trend: sign of the 12-month return difference
    def r12(S):
        a, b = S.at_or_before(made - pd.DateOffset(months=12)), S.at_or_before(made)
        return None if a[0] is None or b[0] is None or a[0] == b[0] else b[1] / a[1] - 1
    x, y = r12(A), r12(B)
    tc = None if x is None or y is None else ("up" if x - y > 0 else "down")
    o.update(trend_cat=tc or "", trend_hit=(tc == cat) if tc else "", agree_trend=(tc == want) if tc else "")
    return o


def _rv(vals, pt):
    if len(vals) < 3:
        return None
    d = np.diff(vals) if pt else np.diff(np.log(vals))
    return float(np.std(d, ddof=1) * math.sqrt(252))


def _score_vol(r, D, o, sp, E, d):
    made, h = r["made_r"], r["h"]
    if sp["kind"] != "mkt":
        return dict(o, status="unscored", reason="volatility call on a non-market series")
    S = _credit_series(D, made)[0] if sp["dir"] == "credit" else D.get(sp["dir"])
    o.update(series=sp["dir"], fam=sp["fam"])
    if S is None or S.freq != "D":
        return dict(o, status="unscored", reason="volatility call on a monthly-only series")
    pt = measure(sp["fam"]) == "pt"
    w = mkt_window(S, made, E, h)
    if isinstance(w, tuple):
        return dict(o, status=w[0], reason=w[1] if w[0] == "unscored" else "",
                    resolve_date=w[1].date().isoformat() if w[0] == "open" else "")
    i0 = np.searchsorted(S.idx, np.datetime64(w["start_date"]))
    i1 = np.searchsorted(S.idx, np.datetime64(w["end_date"]))
    n = i1 - i0
    m = max(n, 63)
    if i0 - m < 0:
        return dict(o, status="unscored", reason="too little history before start")
    after, before = _rv(S.v[i0:i1 + 1], pt), _rv(S.v[i0 - m:i0 + 1], pt)
    if not after or not before:
        return dict(o, status="unscored", reason="data gap")
    ratio = after / before
    want = "up" if d == "higher_vol" else "down"
    cat = "up" if ratio > 1 + VOL_RATIO_BAND else "down" if ratio < 1 - VOL_RATIO_BAND else "flat"
    o.update(status="resolved", reason="", start_date=w["start_date"].date().isoformat(),
             end_date=w["end_date"].date().isoformat(), resolve_date=w["end_date"].date().isoformat(),
             change=ratio - 1, band=VOL_RATIO_BAND, category=cat, want=want, hit=cat == want,
             sign_hit=(ratio > 1) if want == "up" else (ratio < 1), move_band=(ratio - 1) / VOL_RATIO_BAND * (1 if want == "up" else -1))
    # base: same ratio on month-end start points of the base window
    hits = []
    for t in month_points(S, h):
        j0 = np.searchsorted(S.idx, np.datetime64(t), side="right") - 1
        j1 = np.searchsorted(S.idx, np.datetime64(add_months(t, h)), side="right") - 1
        nn = j1 - j0
        mm = max(nn, 63)
        if j0 - mm < 0 or nn < 3:
            continue
        a, b = _rv(S.v[j0:j1 + 1], pt), _rv(S.v[j0 - mm:j0 + 1], pt)
        if a and b:
            q = a / b
            c = "up" if q > 1 + VOL_RATIO_BAND else "down" if q < 1 - VOL_RATIO_BAND else "flat"
            hits.append(c == want)
    p = float(np.mean(hits)) if len(hits) >= 60 else None
    o.update(base_p=p if p is not None else "", base_n=len(hits), base_series=sp["dir"] if p is not None else "")
    # trend: vol over the h-length window before start (>= 63 days) against the 12 months before that
    k = np.searchsorted(S.idx, np.datetime64(made), side="right") - 1
    tc = None
    if k - m - 252 >= 0:
        a, b = _rv(S.v[k - m:k + 1], pt), _rv(S.v[k - m - 252:k - m + 1], pt)
        if a and b:
            tc = "up" if a > b else "down"      # GAP-9: "exceeds" -> higher, else lower (no flat for the trend)
    o.update(trend_cat=tc or "", trend_hit=(tc == cat) if tc else "", agree_trend=(tc == want) if tc else "")
    return o


# macro readings ------------------------------------------------------------
def readings(D, sp):
    S = D.get(sp["m"])
    if S is None:
        return None
    s = S.s.copy()
    if S.freq == "M":
        s = s.reindex(pd.date_range(s.index[0], s.index[-1], freq="ME"))
    elif S.freq == "Q":
        s = s.reindex(pd.date_range(s.index[0], s.index[-1], freq="QE-DEC"))
    if sp["tf"] == "yoy12":
        s = (s / s.shift(12) - 1) * 100
    elif sp["tf"] == "yoy4q":
        s = (s / s.shift(4) - 1) * 100
    elif sp["tf"] == "sum12neg":
        s = -s.rolling(12).sum()
    s = s.dropna()
    return Series(s, S.freq, sp["m"])


def _reading_asof(R, sp, d):
    """last reference period published strictly before d (period end + lag < d)."""
    return R.at_or_before(d - pd.Timedelta(days=sp["lag"] + 1))


def _end_period(R, sp, E):
    """last reference period ending on or before E (policy: one month later)."""
    if R.freq == "M":
        p = (E + pd.Timedelta(days=1)) - pd.offsets.MonthEnd(1)
        p = p.normalize()
        if (E + pd.Timedelta(days=1)).day == 1:
            p = E.normalize()
        if sp.get("shift"):
            p = (p + pd.offsets.MonthEnd(sp["shift"])).normalize()
        return p
    if R.freq == "Q":
        q = (E + pd.Timedelta(days=1)) - pd.offsets.QuarterEnd(1)
        return E.normalize() if (E + pd.Timedelta(days=1)).is_quarter_start else q.normalize()
    return E.normalize()                         # weekly: last observation on or before E


def _score_macro(r, D, o, sp, E, want):
    made, h = r["made_r"], r["h"]
    fam = sp["fam"]
    R = readings(D, sp)
    o.update(series=sp["m"], fam=fam)
    if R is None or R.last is None:
        return dict(o, status="unscored", reason="series file missing")
    sd, sv = _reading_asof(R, sp, made)
    ep = _end_period(R, sp, E)
    if R.freq == "W":
        ed, ev = R.at_or_before(ep)
        if ep > R.last:
            return dict(o, status="open", reason="", resolve_date=(ep + pd.Timedelta(days=sp["lag"])).date().isoformat())
    else:
        if ep > R.last:
            return dict(o, status="open", reason="", resolve_date=(ep + pd.Timedelta(days=sp["lag"])).date().isoformat())
        ed, ev = R.at_or_before(ep)
        if ed != ep:
            return dict(o, status="unscored", reason="data gap")
    if sd is None:
        return dict(o, status="unscored", reason="series starts after made date")
    if ed <= sd:
        return dict(o, status="unscored", reason="horizon too short for the data")
    band = band_for(fam, h)
    change = chg(sv, ev, fam)
    lev = parse_level(r.get("level"), fam)
    note = ""
    if lev is not None and lev["kind"] in ("threshold", "range"):
        lev, note = None, "level ignored (no level series)"   # macro codes are not marked L (rules section 3)
    elif lev is not None:
        note = "level %s" % lev["kind"]
    hit = outcome_hit(want, change, band, lev, None, None)
    cat = category(change, band)
    o.update(status="resolved", reason="", start_date=sd.date().isoformat(), start_value=sv,
             end_date=ed.date().isoformat(), end_value=ev,
             resolve_date=(ed + pd.Timedelta(days=sp["lag"])).date().isoformat(), change=change, band=band,
             category=cat, want=want, hit=bool(hit), level_use=note,
             sign_hit=(change > 0 if want == "up" else change < 0 if want == "down" else ""),
             move_band=(change / band * (1 if want == "up" else -1) if want != "flat" else ""))
    hits = []
    for t in month_points(R, h):
        a = _reading_asof(R, sp, t)
        b = R.at_or_before(_end_period(R, sp, add_months(t, h)))
        if a[0] is None or b[0] is None or b[0] <= a[0]:
            continue
        hits.append(base_hit(want, chg(a[1], b[1], fam), band, lev, None, fam))
    p = float(np.mean(hits)) if len(hits) >= 60 else None
    o.update(base_p=p if p is not None else "", base_n=len(hits), base_series=sp["m"] if p is not None else "")
    a = _reading_asof(R, sp, made - pd.DateOffset(months=12))
    tc = None if a[0] is None or a[0] >= sd else category(chg(a[1], sv, fam), band_for(fam, 12))
    o.update(trend_cat=tc or "", trend_hit=(tc == cat) if tc else "", agree_trend=(tc == want) if tc else "")
    return o


def _score_weo(r, D, o, sp, E, want):
    made = r["made_r"]
    fam = sp["fam"]
    o.update(series="WEO %s %s" % (sp["ind"], "+".join(sp["iso"])), fam=fam)
    y0 = made.year - 1
    y1 = E.year if E >= pd.Timestamp(E.year, 7, 1) else E.year - 1
    if y1 <= y0:
        return dict(o, status="unscored", reason="horizon too short for the data")
    v1 = D.weo_value(sp["iso"], sp["ind"], y1)
    if v1 is None:
        # GAP-10: the WEO file holds current/forward years only (no backcast actuals). If a vintage after April of
        # year+1 is already in the file and still no actual is reported, the row cannot resolve: unscored.
        last_pub = str(pd.read_csv(os.path.join(D.rd, "imf_weo_vintages.csv.gz"), usecols=["publication_date"])
                       .publication_date.max()) if D.rd else ""
        if last_pub >= "%d-04-01" % (y1 + 1):
            return dict(o, status="unscored", reason="WEO file reports no actual for the end year")
        return dict(o, status="open", reason="", resolve_date="%d-04-30" % (y1 + 1))
    v0 = D.weo_value(sp["iso"], sp["ind"], y0)
    if v0 is None:
        return dict(o, status="unscored", reason="data gap")
    band = band_for(fam, r["h"])
    change = v1 - v0
    lev = parse_level(r.get("level"), fam)
    note = ""
    if lev is not None and lev["kind"] in ("threshold", "range"):
        lev, note = None, "level ignored (no level series)"
    hit = outcome_hit(want, change, band, lev, None, None)
    cat = category(change, band)
    o.update(status="resolved", reason="", start_date="%d" % y0, start_value=v0, end_date="%d" % y1, end_value=v1,
             resolve_date="%d" % (y1 + 1), change=change, band=band, category=cat, want=want, hit=bool(hit),
             level_use=note, sign_hit=(change > 0 if want == "up" else change < 0 if want == "down" else ""),
             move_band=(change / band * (1 if want == "up" else -1) if want != "flat" else ""),
             base_p="", base_n="", base_series="")
    vm = D.weo_value(sp["iso"], sp["ind"], y0 - 1)
    tc = None if vm is None else category(v0 - vm, band_for(fam, 12))
    o.update(trend_cat=tc or "", trend_hit=(tc == cat) if tc else "", agree_trend=(tc == want) if tc else "")
    return o


# events ---------------------------------------------------------------------
def recession_signs(D):
    """dates on which a recession start becomes visible: USREC 0->1 (month end), two negative quarters (2nd q end + 30)."""
    out = []
    U = D.get("USREC")
    if U is not None:
        v = U.s
        for i in range(1, len(v)):
            if v.iloc[i] == 1 and v.iloc[i - 1] == 0:
                out.append((v.index[i], v.index[i]))       # (reference date, visible date)
    G = D.get("r/A191RL1Q225SBEA")
    if G is not None:
        g = G.s
        for i in range(1, len(g)):
            if g.iloc[i] < 0 and g.iloc[i - 1] < 0 and not (i >= 2 and g.iloc[i - 2] < 0):
                out.append((g.index[i - 1], g.index[i] + pd.Timedelta(days=30)))   # both quarters must end in window
    return out, (U.last if U is not None else None), (G.last if G is not None else None)


def _rec_in(signs, a, b):
    """recession starts inside (a, b]: USREC start month in window, or both negative quarters end in window."""
    for ref, vis in signs:
        if a < ref <= b:
            # for GDP signs ref = first negative quarter end; the second quarter end = vis - 30 days must also be <= b
            if vis - pd.Timedelta(days=30) <= b or vis == ref:
                return vis
    return None


def _score_event(r, D, o, sp, E, ):
    code, text, d, made, h = r["variable_code"], r["variable_text"], r["direction"], r["made_r"], r["h"]
    yes = d == "event_yes"
    o.update(want="event_yes" if yes else "event_no")
    if sp["kind"] == "rec":
        signs, ulast, glast = recession_signs(D)
        o.update(series="USREC + A191RL1Q225SBEA", fam="event")
        vis = _rec_in(signs, made, E)
        final = E + pd.DateOffset(months=12)
        covered = ulast is not None and ulast >= (final + pd.offsets.MonthEnd(0)).normalize() - pd.Timedelta(days=1)
        if yes and vis is not None:
            occurred, rdate = True, vis
        elif covered:
            occurred, rdate = vis is not None, final
        else:
            return dict(o, status="open", reason="", resolve_date=final.date().isoformat())
        hit = occurred == yes
        pts = [t for t in pd.date_range(BASE_FROM, BASE_TO, freq="ME") if add_months(t, h) <= BASE_TO]
        occ = [_rec_in(signs, t, add_months(t, h)) is not None for t in pts]
        p = float(np.mean([x == yes for x in occ])) if len(occ) >= 60 else None
        prior = _rec_in(signs, made - pd.DateOffset(months=12), made) is not None
        o.update(status="resolved", reason="", start_date=made.date().isoformat(), end_date=E.date().isoformat(),
                 resolve_date=rdate.date().isoformat(), category="event_yes" if occurred else "event_no",
                 hit=bool(hit), base_p=p if p is not None else "", base_n=len(occ), base_series="USREC+GDP",
                 trend_cat="event_yes" if prior else "event_no", trend_hit=(prior == occurred),
                 agree_trend=(prior == yes))
        return o
    t = (text or "").lower()
    thr = 0.20 if re.search(r"crash|bear market", t) else 0.10 if "correction" in t else None
    if thr is not None and code in EQUITY_CODES and sp["kind"] == "mkt":
        S = D.get(sp["dir"])
        o.update(series=sp["dir"], fam="event")
        w = mkt_window(S, made, E, h)
        if isinstance(w, tuple):
            return dict(o, status=w[0], reason=w[1] if w[0] == "unscored" else "",
                        resolve_date=w[1].date().isoformat() if w[0] == "open" else "")
        def mdd(vals, start):
            peak = np.maximum.accumulate(np.concatenate([[start], vals]))
            return float(np.max(1 - np.concatenate([[start], vals]) / peak))
        vals, _ = S.window(w["start_date"], w["end_date"])
        occurred = mdd(vals, w["start"]) >= thr
        hits = []
        for tt in month_points(S, h):
            sd, sv = S.at_or_before(tt)
            vv, _ = S.window(tt, add_months(tt, h))
            if sd is not None and len(vv):
                hits.append((mdd(vv, sv) >= thr) == yes)
        p = float(np.mean(hits)) if len(hits) >= 60 else None
        pv, _ = S.window(made - pd.DateOffset(months=12), made)
        a0 = S.at_or_before(made - pd.DateOffset(months=12))
        prior = (mdd(pv, a0[1]) >= thr) if len(pv) and a0[0] is not None else None
        o.update(status="resolved", reason="", start_date=w["start_date"].date().isoformat(),
                 end_date=w["end_date"].date().isoformat(), resolve_date=w["end_date"].date().isoformat(),
                 category="event_yes" if occurred else "event_no", hit=occurred == yes,
                 level_use="drawdown >= %d%%" % round(thr * 100), base_p=p if p is not None else "", base_n=len(hits),
                 base_series=sp["dir"] if p is not None else "",
                 trend_cat=("event_yes" if prior else "event_no") if prior is not None else "",
                 trend_hit=(prior == occurred) if prior is not None else "",
                 agree_trend=(prior == yes) if prior is not None else "")
        return o
    if sp["kind"] == "mkt":
        lev = parse_level(r.get("level"), sp["fam"])
        lname = level_series_name(sp, text, code) if lev and lev["kind"] == "threshold" else None
        if lev and lev["kind"] == "threshold" and lname:
            L = D.get(lname)
            o.update(series=lname, fam="event")
            w = mkt_window(L, made, E, h)
            if isinstance(w, tuple):
                return dict(o, status=w[0], reason=w[1] if w[0] == "unscored" else "",
                            resolve_date=w[1].date().isoformat() if w[0] == "open" else "")
            T, s0 = lev["T"], w["start"]
            fam = sp["fam"]
            if (FAM[fam][3] or measure(fam) == "pct") and not (0.25 * s0 <= T <= 4 * s0) or \
                    (measure(fam) == "pt" and abs(T - s0) > 10):
                return dict(o, status="unscored", reason="event level unit mismatch")
            up = T >= s0
            vals, _ = L.window(w["start_date"], w["end_date"], left_open=False)
            occurred = bool(vals.max() >= T) if up else bool(vals.min() <= T)
            need = chg(s0, T, fam)
            hits = []
            for tt in month_points(L, h):
                sd, sv = L.at_or_before(tt)
                vv, _ = L.window(tt, add_months(tt, h))
                if sd is not None and len(vv):
                    ext = chg(sv, vv.max(), fam) if up else chg(sv, vv.min(), fam)
                    hits.append(((ext >= need) if up else (ext <= need)) == yes)
            p = float(np.mean(hits)) if len(hits) >= 60 else None
            pv, _ = L.window(made - pd.DateOffset(months=12), made)
            prior = (bool(pv.max() >= T) if up else bool(pv.min() <= T)) if len(pv) else None
            o.update(status="resolved", reason="", start_date=w["start_date"].date().isoformat(),
                     end_date=w["end_date"].date().isoformat(), resolve_date=w["end_date"].date().isoformat(),
                     category="event_yes" if occurred else "event_no", hit=occurred == yes, level_use="touch %s" % T,
                     base_p=p if p is not None else "", base_n=len(hits), base_series=lname if p is not None else "",
                     trend_cat=("event_yes" if prior else "event_no") if prior is not None else "",
                     trend_hit=(prior == occurred) if prior is not None else "",
                     agree_trend=(prior == yes) if prior is not None else "")
            return o
    return dict(o, status="unscored", reason="event not scorable in v1")


# ---------------------------------------------------------------- pools, duplicates, run
def pool_of(r):
    k, res, why, ct = r["kind"], r["resolvable"], r["why_not"], r["call_type"]
    if k == "not_forecast":
        return None, "not_forecast"
    if k == "conditional":
        if res == "no" and why != "conditional_unmet_unknown":
            return None, "resolvable=no (%s)" % (why or "?")
        return "D", ""
    if res not in ("yes", "partly"):
        return None, "resolvable=no (%s)" % (why or "?")
    if k == "stance":
        return "C", ""
    if ct == "structural":
        return "E", ""
    if k == "forecast":
        return ("A" if res == "yes" else "B"), ""
    return None, "unknown kind"


def horizon(r, pool):
    hm = r.get("horizon_months")
    if hm not in ("", None):
        return float(hm), "stated"
    ct = r["call_type"]
    if pool == "E":
        return 36.0, "default"
    return float(DEFAULT_H.get(ct, 12)), "default"


OUT_COLS = ["forecast_id", "source_id", "who", "made_date", "date_precision", "made_r", "kind", "variable_code",
            "variable_text", "direction", "level", "call_type", "resolvable", "pool", "h", "h_source", "status",
            "reason", "duplicate_of", "series", "fam", "group", "start_date", "start_value", "end_target", "end_date",
            "end_value", "resolve_date", "change", "band", "category", "want", "hit", "sign_hit", "touch_hit",
            "level_use", "move_band", "probability", "base_p", "base_n", "base_series", "trend_cat", "trend_hit",
            "agree_trend", "rules"]


def run(ledger_rows, D):
    rows = []
    for r in ledger_rows:
        pool, why = pool_of(r)
        x = dict(r, pool=pool or "", rules=RULES)
        if pool is None:
            x.update(status="not pooled", reason=why)
            rows.append(x)
            continue
        made_r = resolved_made(r["made_date"], r["date_precision"])
        if made_r is None:
            x.update(status="excluded", reason="date too coarse (year)")
            rows.append(x)
            continue
        h, hs = horizon(r, pool)
        x.update(made_r=made_r, h=h, h_source=hs)
        rows.append(x)
    # duplicates (rules section 5): same who, variable_code, direction within the 30 days before; earliest kept
    live = sorted([x for x in rows if x.get("made_r") is not None], key=lambda x: (x["made_r"], x["forecast_id"]))
    kept = {}
    for x in live:
        key = (x["who"], x["variable_code"], x["direction"])
        prev = kept.get(key)
        if prev is not None and 0 <= (x["made_r"] - prev["made_r"]).days <= 30:
            x.update(status="duplicate", reason="duplicate", duplicate_of=prev["forecast_id"])
            continue
        kept[key] = x
    for x in live:
        if x.get("status") == "duplicate":
            continue
        if x["h"] > MAX_H:
            x.update(status="excluded", reason="horizon above 60 months")
            continue
        if busdays(x["made_r"], add_months(x["made_r"], x["h"])) < 5:
            x.update(status="excluded", reason="horizon below 5 trading days")   # GAP-11
            continue
        try:
            res = score_row(x, D)
        except Exception as e:                                  # never hide a crash: record it
            res = dict(status="unscored", reason="scorer error: %s" % type(e).__name__)
        x.update({k: (bool(v) if isinstance(v, (np.bool_, bool)) else float(v) if isinstance(v, np.floating) else v)
                  for k, v in res.items()})
    for x in rows:
        x["group"] = family_of(x.get("variable_code"))
        if isinstance(x.get("made_r"), pd.Timestamp):
            x["made_r"] = x["made_r"].date().isoformat()
    return rows


def main():
    a = sys.argv[1:]
    vault = a[0]
    raw = a[a.index("--raw") + 1] if "--raw" in a else RAW_DEFAULT
    freeze = "--no-freeze" not in a
    F = os.path.join(vault, "pipeline", "forecasts")
    led = list(csv.DictReader(open(os.path.join(F, "ledger.csv"))))
    D = Data(raw)
    rows = run(led, D)
    fz_path = os.path.join(F, "scored_frozen.csv")
    frozen = {}
    if os.path.exists(fz_path):
        for z in csv.DictReader(open(fz_path)):
            frozen[z["forecast_id"]] = z
    new = []
    for i, x in enumerate(rows):
        if x["forecast_id"] in frozen:
            rows[i] = dict(frozen[x["forecast_id"]])
        elif x.get("status") == "resolved":
            new.append(x)
    stamp = D.stamps()
    with open(os.path.join(F, "outcomes.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, OUT_COLS + ["run_date", "cache_fetched"], extrasaction="ignore")
        w.writeheader()
        for x in rows:
            w.writerow(dict(x, run_date=dt.date.today().isoformat(), cache_fetched=json.dumps(stamp)))
    if freeze and new:
        exists = os.path.exists(fz_path)
        with open(fz_path, "a", newline="") as f:
            w = csv.DictWriter(f, OUT_COLS + ["run_date", "cache_fetched"], extrasaction="ignore")
            if not exists:
                w.writeheader()
            for x in new:
                w.writerow(dict(x, run_date=dt.date.today().isoformat(), cache_fetched=json.dumps(stamp)))
    import collections
    c = collections.Counter(x.get("status") for x in rows)
    print("rows %d | %s | newly frozen %d | cache %s" % (len(rows), dict(c), len(new) if freeze else 0, stamp))


if __name__ == "__main__":
    main()
