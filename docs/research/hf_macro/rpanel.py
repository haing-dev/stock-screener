"""Wide monthly research panel (month-end, USD total returns where possible). Builds rpanel.pkl next to this file.
Assets: ETFs (Yahoo adjusted, month-end) spliced onto long proxies:
  US equity = tool market (SPY / French); sectors = tool's 20 industries; T-bills = French RF;
  Treasuries 10y/30y/2y synthetic from yields; TLT/IEF/SHY after inception; gold GC=F then month-end estimate of
  monthly average; commodities = AQR equal-weight commodity futures excess return + T-bill (1877-2025-05), then DBC;
  country equity = ETF; before it, local index price in USD + 2%/yr dividend proxy (Nikkei 1985, KOSPI 1997, Bovespa 1993,
  Hang Seng 1987, TAIEX 1997, Sensex 1997, IPC 1991, DAX 1988, FTSE 1985...) - flagged 'proxy'.
  Trend-following = AQR TSMOM factor (excess) + T-bill, 1985+.  Global equity/bond/commodity 'market' and multi-style
  premia from AQR Century of Factor Premia (excess returns, 1926+).
Signals: everything in the tool panel (ind, sc, F) + research FRED series + Shiller (CPI, earnings 1871).
"""
import math
import os
import pickle
import sys
import warnings

warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/claude/stock-screener"
RD = os.path.join(REPO, "cache", "macro", "raw", "research")
sys.path.insert(0, REPO)
os.chdir(REPO)
from macro import engine as E  # noqa

P = pickle.load(open("/home/claude/research_notes/Macro Compass return and risk upgrades/empirical/panel.pkl", "rb"))
grid = P["grid"]
Per = lambda s: pd.Period(s, "M")


def csvm(path):
    if not os.path.exists(path):
        return pd.Series(np.nan, index=grid)
    s = pd.read_csv(path)
    if "value" not in s:
        return pd.Series(np.nan, index=grid)
    s = s[pd.to_numeric(s["value"], errors="coerce").notna()]
    d = pd.to_datetime(s["date"], errors="coerce")
    m = pd.Series(s["value"].astype(float).values, index=d.dt.to_period("M")).groupby(level=0).last()
    return m.reindex(grid)


def y(sym):
    import re
    return csvm(os.path.join(RD, "Y_" + re.sub(r"[^A-Za-z0-9]", "_", sym) + ".csv"))


def yr(sym):
    return y(sym).pct_change(fill_method=None)


def fr(sid):
    return csvm(os.path.join(RD, sid + ".csv"))


rf = P["rf"]
mkt = P["mkt"]
R = pd.DataFrame(index=grid)
SRC = {}


def put(name, *parts):
    s = pd.Series(np.nan, index=grid)
    for p in parts:
        s = s.combine_first(p)
    R[name] = s


# ---------------- AQR files
def aqr(fname, hdr_key):
    d = pd.read_excel(os.path.join(RD, fname), sheet_name=0, header=None)
    hi = d.index[d.iloc[:, 0].astype(str).str.strip().eq("Date") | d.iloc[:, 1].astype(str).str.contains(hdr_key, na=False)][0]
    cols = d.iloc[hi].astype(str).tolist()
    body = d.iloc[hi + 1:].copy()
    body.columns = cols
    dt = pd.to_datetime(body.iloc[:, 0], errors="coerce")
    body = body[dt.notna()]
    body.index = pd.to_datetime(body.iloc[:, 0]).dt.to_period("M")
    return body.iloc[:, 1:].apply(pd.to_numeric, errors="coerce").groupby(level=0).last().reindex(grid)


com = aqr("aqr_commodities_long_run.xlsx", "Excess return")
com_ex = com.iloc[:, 0]                                    # EW commodity futures excess return
com_ls = com.iloc[:, 5]                                    # long/short (momentum-like) excess return
ts = aqr("aqr_tsmom_factors.xlsx", "TSMOM")
cp = aqr("aqr_century_premia.xlsx", "Stock")
dbc = yr("DBC")
put("commod", dbc, com_ex + rf)
put("commod_ls", com_ls + rf)
put("trend", ts["TSMOM"] + rf)
put("trend_cm", ts["TSMOM^CM"] + rf)
for c in ["Equity indices Market", "Fixed income Market", "Commodities Market", "All Macro Multi-style",
          "All Macro Momentum", "All Macro Carry", "All Macro Value", "Currencies Carry", "Equity indices Momentum",
          "Commodities Momentum", "Fixed income Momentum", "Currencies Momentum", "All asset classes Multi-style",
          "Equity indices Defensive"]:
    if c in cp:
        R["aqr_" + c.lower().replace(" ", "_").replace("-", "_")] = cp[c] + rf

# ---------------- rates and bonds
F = P["F"]
syn = lambda yy, d: yy.shift(1) / 1200 - d * (yy - yy.shift(1)) / 100
gs30 = E.fred_monthly("GS30", grid) if "GS30" in E.R.FRED else fr("DGS30")
put("tbill", rf)
put("t2y", yr("SHY"), syn(F["GS2"], 1.9))
put("t10y", yr("IEF"), syn(F["GS10"], 7))
put("t30y", yr("TLT"), syn(gs30, 15), syn(F["GS10"], 7))
put("t30y_long", yr("EDV"), syn(gs30, 22))
put("tips", yr("TIP"))
put("ig", yr("LQD"))
put("hy", yr("HYG"))
put("em_debt", yr("EMB"))
put("em_local", yr("EMLC"))


# ---------------- gold, silver, single commodities
def end_est(avg):
    return np.sqrt(avg * avg.shift(-1))


g_avg = E._csv("GOLD")
g_avg = pd.Series(g_avg.values, index=g_avg.index.to_period("M")).groupby(level=0).last().reindex(grid)
put("gold", yr("GLD"), yr("GC=F"), end_est(g_avg).pct_change(fill_method=None))
put("silver", yr("SLV"), yr("SI=F"))
put("oil", yr("USO"), yr("CL=F"))
put("copper", yr("CPER"), yr("HG=F"))
put("ags", yr("DBA"))
put("base_metals", yr("DBB"))
put("energy_fut", yr("DBE"))
put("btc", yr("BTC-USD"))

# ---------------- equity: US slices
put("spx", mkt)
put("ndx", yr("QQQ"), yr("^IXIC"))
put("small", yr("IWM"), yr("^RUT"))
put("eqw", yr("RSP"))
put("lowvol", yr("USMV"), yr("SPLV"))
put("value", yr("IWD"))
put("growth", yr("IWF"))
for k in P["rets"].columns:
    R["sec_" + k] = P["rets"][k]

# ---------------- countries: ETF, then local index in USD + 2%/yr dividend proxy
FX = {"KRW": fr("DEXKOUS"), "BRL": fr("DEXBZUS"), "CNY": fr("DEXCHUS"), "INR": fr("DEXINUS"), "MXN": fr("DEXMXUS"),
      "JPY": E.fred_monthly("EXJPUS", grid) if False else csvm(os.path.join(REPO, "cache/macro/raw/EXJPUS.csv"))}
fxy = {"KRW": y("KRW=X"), "BRL": y("BRL=X"), "INR": y("INR=X"), "MXN": y("MXN=X"), "JPY": y("JPY=X"), "CNY": y("CNY=X")}
for k in FX:
    FX[k] = fxy[k].combine_first(FX[k])                    # local per USD, month-end where Yahoo has it


def local_usd(idx, cur):
    p = y(idx)
    if cur:
        p = p / FX[cur]
    return p.pct_change(fill_method=None) + 0.02 / 12


COUNTRY = {"korea": ("EWY", "^KS11", "KRW"), "brazil": ("EWZ", "^BVSP", "BRL"), "japan": ("EWJ", "^N225", "JPY"),
           "china": ("FXI", "^HSI", None), "india": ("INDA", "^BSESN", "INR"), "taiwan": ("EWT", None, None),
           "mexico": ("EWW", "^MXX", "MXN"), "germany": ("EWG", None, None), "uk": ("EWU", None, None),
           "canada": ("EWC", None, None), "australia": ("EWA", None, None), "hongkong": ("EWH", "^HSI", None),
           "s_africa": ("EZA", None, None), "chile": ("ECH", None, None), "turkey": ("TUR", None, None),
           "indonesia": ("EIDO", None, None), "europe": ("VGK", None, None), "em": ("EEM", None, None),
           "eafe": ("EFA", None, None), "latam": ("ILF", None, None), "acwx": ("ACWX", None, None)}
for k, (etf, idx, cur) in COUNTRY.items():
    parts = [yr(etf)]
    if idx:
        parts.append(local_usd(idx, cur))
    put("eq_" + k, *parts)
    SRC["eq_" + k] = (str(yr(etf).first_valid_index()), str(R["eq_" + k].first_valid_index()))
R["eq_em"] = R["eq_em"].combine_first(yr("VWO"))

# ---------------- currencies
put("usd", yr("UUP"))
put("jpy", yr("FXY"))
put("chf", yr("FXF"))
put("eur", yr("FXE"))
put("aud", yr("FXA"))
put("em_fx", yr("CEW"))
put("vix_fut", yr("VIXY"), yr("VXX"))
put("tail", yr("TAIL"))
R = R.astype(float)
R[R.abs() > 3] = np.nan                                     # bad ticks

# ---------------- signals
S = {}
for f in os.listdir(RD):
    if f.endswith(".csv") and not f.startswith(("Y_", "msci", "D_", "cboe", "cftc")):
        S["fred_" + f[:-4]] = fr(f[:-4])
for sym in ["^VIX", "^VIX3M", "^MOVE", "^TNX", "^IRX", "DX-Y.NYB", "CL=F", "HG=F", "GC=F", "^N225", "^KS11", "KRW=X",
            "BRL=X", "CNY=X", "^GSPC"]:
    S["px_" + sym] = y(sym)
S = pd.DataFrame(S)
# Shiller (S&P, dividends, earnings, CPI, 10y rate since 1871)
try:
    sh = pd.read_excel(os.path.join(RD, "shiller_ie_data.xls"), sheet_name="Data", header=7)
    sh = sh[pd.to_numeric(sh["Date"], errors="coerce").notna()]
    dt = sh["Date"].astype(float)
    per = pd.PeriodIndex([pd.Period(f"{int(v)}-{int(round((v % 1) * 100)) or 1:02d}", "M") for v in dt], freq="M")
    for c, nm in (("P", "sh_price"), ("D", "sh_div"), ("E", "sh_eps"), ("CPI", "sh_cpi"), ("Rate GS10", "sh_gs10")):
        if c in sh:
            S[nm] = pd.Series(pd.to_numeric(sh[c], errors="coerce").values, index=per).groupby(level=0).last().reindex(grid)
except Exception as e:
    print("shiller failed", e)
# World Bank pink sheet indices
try:
    wb = pd.read_excel(os.path.join(RD, "wb_pinksheet_monthly.xlsx"), sheet_name="Monthly Indices", header=None)
    hdr = [" ".join(str(wb.iloc[r, c]) for r in range(5, 9) if str(wb.iloc[r, c]) != "nan").strip() for c in range(wb.shape[1])]
    body = wb.iloc[9:]
    body = body[body.iloc[:, 0].astype(str).str.match(r"^\d{4}M\d{2}$")]
    idx = pd.PeriodIndex([pd.Period(s.replace("M", "-"), "M") for s in body.iloc[:, 0]], freq="M")
    for c in range(1, wb.shape[1]):
        S["wb_" + hdr[c].lower().replace(" ", "_").replace("*", "")[:30]] = pd.Series(pd.to_numeric(body.iloc[:, c], errors="coerce").values, index=idx).reindex(grid)
except Exception as e:
    print("pink sheet failed", e)

out = {"grid": grid, "R": R, "S": S, "rf": rf, "mkt": mkt, "P": P, "src": SRC}
pickle.dump(out, open(os.path.join(HERE, "rpanel.pkl"), "wb"))
cov = pd.DataFrame({"first": R.apply(lambda s: s.first_valid_index()), "last": R.apply(lambda s: s.last_valid_index()),
                    "n": R.notna().sum()})
print(cov.to_string())
print("signals:", S.shape, "country splice (ETF start, proxy start):", SRC)
