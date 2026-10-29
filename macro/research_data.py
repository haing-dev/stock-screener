"""Research only (not used by the page): download a wide multi-asset data set for the macro-book research.
Everything lands in cache/macro/raw/more/ (pushed with the raw downloads to branch 'macro-data'); manifest.json lists
what worked. Run in GitHub Actions: python -m macro.run fetch,more  (the sandbox has no network)."""
import io
import json
import os
import re
import time

from . import fetch as FT

OUT = os.path.join("cache", "macro", "raw", "more")

# Yahoo monthly adjusted closes (dividends included for ETFs; indexes are price only)
YAHOO_M = """
EWY EWZ EWJ EWG EWU EWQ EWI EWP EWL EWN EWD EWC EWA EWH EWS EWT EWW EZA ECH EPOL TUR INDA EIDO THD EWM EPHE FXI MCHI
ASHR KWEB EEM EFA VEU VWO IEMG VGK ACWI ARGT GREK KSA VNM EPU GXG NORW EWO EWK ENZL EIS EZU HEZU DXJ
^KS11 ^BVSP ^N225 ^HSI ^GDAXI ^FTSE ^FCHI ^STOXX50E ^BSESN ^NSEI 000001.SS ^MXX ^TWII ^AXJO ^GSPTSE ^JKSE ^KLSE ^STI
^MERV ^IPSA ^SSMI ^AEX ^IBEX ^GSPC ^IXIC ^RUT ^DJI ^NDX ^SP500TR ^W5000
QQQ IWM IWD IWF IWN IWO MTUM QUAL USMV SPLV RSP MDY IJR VTV VUG SPHB SPLV SCHD DVY
BIL SHV SHY IEI IEF TLH TLT EDV ZROZ GOVT TIP VTIP STIP LTPZ LQD VCIT HYG JNK SJNK EMB EMLC PCY BNDX BWX MBB AGG BND
FLOT SRLN BKLN CWB PFF
DBC GSG DJP PDBC COMT BCI USO BNO UNG DBO DBA DBB DBE DBP GLD IAU SLV PPLT PALL CPER URA URNM GDX GDXJ SIL XME COPX
LIT REMX WOOD MOO CORN WEAT SOYB XOP OIH AMLP
CL=F BZ=F NG=F HO=F RB=F GC=F SI=F HG=F PL=F PA=F ZC=F ZW=F ZS=F KC=F SB=F CC=F CT=F LE=F HE=F ZB=F ZN=F ZF=F ZT=F
ES=F NQ=F YM=F RTY=F 6E=F 6J=F 6B=F 6A=F 6C=F 6S=F DX=F
UUP UDN FXE FXY FXF FXB FXA FXC CYB CEW EURUSD=X JPY=X KRW=X BRL=X CNY=X INR=X MXN=X AUDUSD=X TRY=X ZAR=X
^VIX ^VIX3M ^VVIX ^VXN ^MOVE ^SKEW VXX VIXY SVXY UVXY VIXM
SH PSQ SDS RWM TBF TBT EUM EFZ
DBMF KMLM CTA WTMF QAI TAIL SWAN CAOS BTAL
VNQ IYR REM RWX VNQI
BTC-USD ETH-USD GBTC IBIT
"""
# Yahoo daily closes (for a crash / volatility cap test)
YAHOO_D = "^GSPC ^VIX SPY TLT IEF GLD ^TNX ^IRX HYG EEM UUP DBC"

FRED = """
CPIAUCSL PCEPI MICH T10Y3M T10Y2Y DGS3MO DGS2 DGS10 DGS30 NFCI ANFCI STLFSI4 KCFSI CFNAI GACDFSA066MSFRBPHI ICSA
SAHMREALTIME RECPROUSM156N BAMLH0A0HYM2 BAMLC0A0CM BAMLHYH0A0HYM2TRIV BAMLCC0A0CMTRIV BAMLEMCBPITRIV BAMLEMHBHYCRPITRIV
AAA DFII10 T10YIE T5YIE WALCL ECBASSETSW JPNASSETS BOGMBASE TOTRESNS DTWEXBGS DTWEXEMEGS DTWEXAFEGS INDPRO TCU
USALOLITONOSTSAM CHNLOLITONOSTSAM KORLOLITONOSTSAM BRALOLITONOSTSAM JPNLOLITONOSTSAM DEULOLITONOSTSAM G7LOLITONOSTSAM
OECDLOLITONOSTSAM XTEXVA01KRM667S XTEXVA01CNM667S XTEXVA01JPM667S XTEXVA01DEM667S XTEXVA01BRM667S XTEXVA01TWM667S
DEXKOUS DEXBZUS DEXCHUS DEXINUS DEXMXUS DEXHKUS DEXTAUS DEXSIUS DEXTHUS DEXMAUS DEXSFUS DEXUSAL DEXUSNZ DEXUSEU DEXJPUS
IRSTCI01BRM156N IRSTCI01KRM156N IRSTCI01INM156N IRSTCI01MXM156N IRSTCI01ZAM156N IRSTCI01AUM156N IRSTCI01NZM156N
IRLTLT01DEM156N IRLTLT01JPM156N IRLTLT01KRM156N IRLTLT01GBM156N IRLTLT01AUM156N IRLTLT01CAM156N
POILBREUSDM PALUMUSDM PNICKUSDM PWHEAMTUSDM PMAIZMTUSDM PSUGAISAUSDM PCOFFOTMUSDM PCOTTINDUSDM PNGASUSUSDM PNGASEUUSDM
PALLFNFINDEXM PNRGINDEXM PMETAINDEXM PFOODINDEXM PSILVERUSDM PURANUSDM PZINCUSDM PLEADUSDM PTINUSDM
WPU10 WPU05 WPU01 WPU0561 PPIIDC
MORTGAGE30US HOUST CSUSHPISA DRSFRMACBS DRALACBS TOTALSL UMCSENT BUSLOANS TOTCI M1SL M2REAL WM2NS
GFDEGDQ188S FYFSGDA188S A091RC1Q027SBEA
"""

AQR = ["Commodities-for-the-Long-Run-Index-Level-Data-Monthly", "Time-Series-Momentum-Factors-Monthly",
       "Century-of-Factor-Premia-Monthly", "Value-and-Momentum-Everywhere-Factors-Monthly",
       "Betting-Against-Beta-Equity-Factors-Monthly", "Quality-Minus-Junk-Factors-Monthly",
       "Credit-Risk-Premium-Preliminary-Paper-Data"]
CBOE = ["PPUT", "BXM", "PUT", "CLL", "VXTH", "BFLY", "CNDR", "VIX", "VIX3M", "SKEW", "VVIX", "BXMD", "CLLZ", "LOVOL"]
URLS = {
    "shiller_ie_data.xls": "http://www.econ.yale.edu/~shiller/data/ie_data.xls",
    "nareit_monthly.xls": "https://www.reit.com/sites/default/files/returns/MonthlyHistoricalReturns.xls",
    "aaii_sentiment.xls": "https://www.aaii.com/files/surveys/sentiment.xls",
    "cboe_totalpc.csv": "https://cdn.cboe.com/resources/options/volume_and_call_put_ratios/totalpc.csv",
    "cboe_equitypc.csv": "https://cdn.cboe.com/resources/options/volume_and_call_put_ratios/equitypc.csv",
    "sp500_datahub.csv": "https://raw.githubusercontent.com/datasets/s-and-p-500/main/data/data.csv",
}


def _save(name, content, man):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "wb") as f:
        f.write(content if isinstance(content, bytes) else content.encode())
    man[name] = {"ok": True, "bytes": len(content)}


def yahoo_daily(sym):
    js = FT._get(f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}",
                 params={"period1": -1325635200, "period2": 9999999999, "interval": "1d", "events": "div,split",
                         "includeAdjustedClose": "true"}).json()
    res = js["chart"]["result"][0]
    adj = res["indicators"].get("adjclose", [{}])[0].get("adjclose") or res["indicators"]["quote"][0]["close"]
    return "date,value\n" + "\n".join(f"{time.strftime('%Y-%m-%d', time.gmtime(t))},{v}" for t, v in zip(res["timestamp"], adj) if v is not None)


def run(log=print):
    man = {}
    key = os.environ.get("FRED_API_KEY", "").strip()
    for s in YAHOO_M.split():
        nm = "Y_" + re.sub(r"[^A-Za-z0-9]", "_", s) + ".csv"
        try:
            rows = FT.yahoo(s)
            _save(nm, "date,value\n" + "\n".join(f"{d},{v}" for d, v in rows), man)
        except Exception as e:        # noqa: BLE001
            man[nm] = {"ok": False, "error": str(e)[:120]}
        time.sleep(0.8)
    for s in YAHOO_D.split():
        nm = "YD_" + re.sub(r"[^A-Za-z0-9]", "_", s) + ".csv"
        try:
            _save(nm, yahoo_daily(s), man)
        except Exception as e:        # noqa: BLE001
            man[nm] = {"ok": False, "error": str(e)[:120]}
        time.sleep(0.8)
    for s in FRED.split():
        try:
            rows, how = FT.fred(s, {}, key)
            _save(f"F_{s}.csv", "date,value\n" + "\n".join(f"{d},{v}" for d, v in rows), man)
        except Exception as e:        # noqa: BLE001
            man[f"F_{s}.csv"] = {"ok": False, "error": str(e)[:120]}
        time.sleep(0.6)
    # Ken French library: every international / developed / emerging / daily / variance / beta file
    try:
        base = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/"
        html = FT._get(base + "data_library.html").text
        links = sorted(set(re.findall(r'ftp/([A-Za-z0-9_\-]+_CSV\.zip)', html)))
        man["french_index"] = {"ok": True, "files": links}
        want = re.compile(r"(Countr|Developed|Emerging|Europe|Japan|Asia_Pacific|North_America|International|daily|"
                          r"Variance|Beta|Momentum|Size|ME_Portfolios|Industry|LT_Reversal|ST_Reversal|_5_Factors|"
                          r"Research_Data)", re.I)
        for fn in links:
            if not want.search(fn):
                continue
            try:
                _save("FR_" + fn, FT._get(base + "ftp/" + fn).content, man)
            except Exception as e:    # noqa: BLE001
                man["FR_" + fn] = {"ok": False, "error": str(e)[:120]}
            time.sleep(0.3)
    except Exception as e:            # noqa: BLE001
        man["french_index"] = {"ok": False, "error": str(e)[:120]}
    for a in AQR:
        for host in ("https://images.aqr.com", "https://www.aqr.com"):
            try:
                _save(f"AQR_{a}.xlsx", FT._get(f"{host}/-/media/AQR/Documents/Insights/Data-Sets/{a}.xlsx", tries=2).content, man)
                break
            except Exception as e:    # noqa: BLE001
                man[f"AQR_{a}.xlsx"] = {"ok": False, "error": str(e)[:120]}
    for c in CBOE:
        try:
            _save(f"CBOE_{c}.csv", FT._get(f"https://cdn.cboe.com/api/global/us_indices/daily_prices/{c}_History.csv", tries=2).content, man)
        except Exception as e:        # noqa: BLE001
            man[f"CBOE_{c}.csv"] = {"ok": False, "error": str(e)[:120]}
    for nm, u in URLS.items():
        try:
            _save(nm, FT._get(u, tries=2).content, man)
        except Exception as e:        # noqa: BLE001
            man[nm] = {"ok": False, "error": str(e)[:120]}
    try:                               # World Bank pink sheet (link hash changes monthly)
        html = FT._get("https://www.worldbank.org/en/research/commodity-markets").text
        m = re.search(r'href="([^"]+CMO-Historical-Data-Monthly\.xlsx)"', html)
        if m:
            u = m.group(1) if m.group(1).startswith("http") else "https://www.worldbank.org" + m.group(1)
            _save("WB_CMO_monthly.xlsx", FT._get(u).content, man)
        else:
            man["WB_CMO_monthly.xlsx"] = {"ok": False, "error": "link not found"}
    except Exception as e:            # noqa: BLE001
        man["WB_CMO_monthly.xlsx"] = {"ok": False, "error": str(e)[:120]}
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "manifest.json"), "w") as f:
        json.dump(man, f, indent=1)
    ok = sum(1 for v in man.values() if v.get("ok"))
    log(f"more: {ok} ok, {len(man) - ok} failed: " + ", ".join(k for k, v in man.items() if not v.get("ok"))[:1500])
    return man
