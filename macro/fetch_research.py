"""Research downloads (not used by the page): a wide instrument universe for strategy research.
Saved to cache/macro/raw/research/ (pushed with the raw data to branch macro-data). Each source fails on its own;
research/manifest.json says what worked. Run: python -m macro.run research_fetch (GitHub Actions; needs network)."""
import io
import json
import os
import re
import time

from . import fetch as FT

OUT = os.path.join(FT.RAW, "research")

YAHOO = [
    # country / region equity ETFs (USD, dividends included)
    "EWY", "EWZ", "EWJ", "FXI", "MCHI", "INDA", "EWT", "EWW", "EWG", "EWU", "EWC", "EWA", "EWH", "EWS", "EZA",
    "TUR", "EIDO", "THD", "EWM", "ECH", "EPU", "ARGT", "VNM", "EEM", "VWO", "EFA", "VGK", "ILF", "ACWI", "ACWX",
    # US size / style
    "IWM", "QQQ", "MDY", "RSP", "IWD", "IWF", "MTUM", "USMV", "QUAL", "SPHB", "SPLV",
    # commodities
    "DBC", "GSG", "PDBC", "DBA", "DBB", "DBE", "DBO", "USO", "BNO", "UNG", "SLV", "GLD", "IAU", "CPER", "PPLT",
    "URA", "XOP", "COPX", "GDXJ", "SIL", "WEAT", "CORN",
    # bonds and credit
    "BIL", "SHV", "SHY", "IEI", "IEF", "TLH", "TLT", "EDV", "ZROZ", "TIP", "STIP", "LQD", "HYG", "JNK", "EMB",
    "EMLC", "BWX", "MBB", "AGG", "BND", "BKLN", "FLOT",
    # currencies, volatility, inverse, hedges
    "UUP", "UDN", "FXE", "FXY", "FXF", "FXB", "FXA", "FXC", "CEW", "CYB", "VIXY", "VXX", "SVXY", "SH", "PSQ",
    "TAIL", "BTAL", "DBMF", "KMLM", "CTA",
    # long-history indexes and futures (price only)
    "^GSPC", "^IXIC", "^RUT", "^N225", "^KS11", "^BVSP", "^HSI", "^TWII", "^BSESN", "^MXX", "^GDAXI", "^FTSE",
    "^FCHI", "^STOXX50E", "^AXJO", "^GSPTSE", "000001.SS", "^VIX", "^VIX3M", "^MOVE", "^TNX", "^IRX", "^TYX",
    "CL=F", "BZ=F", "GC=F", "SI=F", "HG=F", "NG=F", "PL=F", "ZC=F", "ZW=F", "ZS=F", "KC=F", "CT=F",
    "DX-Y.NYB", "EURUSD=X", "JPY=X", "KRW=X", "BRL=X", "CNY=X", "INR=X", "MXN=X", "AUDUSD=X", "BTC-USD",
]

FRED = [
    "CPIAUCSL", "CPIAUCNS", "PCEPI", "PAYEMS", "ICSA", "INDPRO", "RSAFS", "UMCSENT", "NFCI", "ANFCI", "STLFSI4",
    "BAMLH0A0HYM2", "BAMLC0A0CM", "BAMLEMCBPIOAS", "T10Y3M", "T10Y2Y", "DGS3MO", "DGS2", "DGS10", "DGS30", "DFII10",
    "T10YIE", "T5YIE", "BOGMBASE", "TOTRESNS", "WRESBAL", "M2SL", "M1SL", "TOTBKCR", "BUSLOANS", "DRTSCILM",
    "CSUSHPINSA", "HOUST", "AWHMAN", "TEMPHELPS", "CCSA", "IC4WSA", "JTSJOL", "GDPC1", "A191RL1Q225SBEA",
    "XTEXVA01KRM667S", "XTEXVA01CNM667S", "XTEXVA01DEM667S", "XTEXVA01JPM667S", "XTEXVA01TWM667S",
    "USALOLITONOSTSAM", "CHNLOLITONOSTSAM", "OECDLOLITOAASTSAM", "KORLOLITONOSTSAM", "BRALOLITONOSTSAM",
    "CPALTT01CNM659N", "CPALTT01BRM659N", "CPALTT01KRM659N", "INTDSRBRM193N", "IRSTCI01KRM156N",
    "DEXKOUS", "DEXBZUS", "DEXCHUS", "DEXINUS", "DEXMXUS", "DTWEXEMEGS", "DTWEXAFEGS", "RBUSBIS", "NBUSBIS",
    "DCOILWTICO", "DCOILBRENTEU", "PCOPPUSDM", "PALUMUSDM", "PNICKUSDM", "PZINCUSDM", "PWHEAMTUSDM", "PMAIZMTUSDM",
    "PSOYBUSDM", "PNGASUSUSDM", "PALLFNFINDEXM", "PNRGINDEXM", "PMETAINDEXM", "PFOODINDEXM", "PRAWMINDEXM",
    "PINDUINDEXM", "PSILVERUSDM", "WTREGEN", "RRPONTSYD", "WALCL", "GFDEBTN", "FYFSGDA188S", "A091RC1Q027SBEA",
    "QUSR628BIS", "QKRR628BIS", "QBRR628BIS", "QCNR628BIS", "USEPUINDXD", "GEPUCURRENT", "SP500",
]

URLS = {   # long-history research data sets (files saved as downloaded)
    "aqr_commodities_long_run.xlsx": "https://www.aqr.com/-/media/AQR/Documents/Insights/Data-Sets/Commodities-for-the-Long-Run-Index-Level-Data-Monthly.xlsx",
    "aqr_tsmom_factors.xlsx": "https://www.aqr.com/-/media/AQR/Documents/Insights/Data-Sets/Time-Series-Momentum-Factors-Monthly.xlsx",
    "aqr_century_premia.xlsx": "https://www.aqr.com/-/media/AQR/Documents/Insights/Data-Sets/Century-of-Factor-Premia-Monthly.xlsx",
    "aqr_vme_factors.xlsx": "https://www.aqr.com/-/media/AQR/Documents/Insights/Data-Sets/Value-and-Momentum-Everywhere-Factors-Monthly.xlsx",
    "shiller_ie_data.xls": "https://img1.wsimg.com/blobby/go/e5e77e0b-59d1-44d9-ab25-4763ac982e53/downloads/ie_data.xls",
    "french_intl_countries.zip": "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/International_Countries_CSV.zip",
    "french_em_factors.zip": "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/Emerging_5_Factors_CSV.zip",
    "french_dev_factors.zip": "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/Developed_5_Factors_CSV.zip",
    "french_mom.zip": "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Momentum_Factor_CSV.zip",
    "french_5f.zip": "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip",
    "gpr_index.xls": "https://www.matteoiacoviello.com/gpr_files/data_gpr_export.xls",
}

MSCI = {   # MSCI end-of-month gross USD index levels (public chart endpoint; may refuse)
    "msci_world": "990100", "msci_em": "891800", "msci_korea": "134000", "msci_brazil": "38000",
    "msci_china": "302400", "msci_india": "935600", "msci_japan": "39200", "msci_taiwan": "938800",
    "msci_mexico": "273000", "msci_eafe": "990300", "msci_acwi": "892400",
}


def _save(name, content, mode="wb"):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), mode) as f:
        f.write(content)


def run(log=print):
    key = os.environ.get("FRED_API_KEY", "").strip()
    man = {"fetched": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()), "series": {}}
    for s in YAHOO:
        name = "Y_" + re.sub(r"[^A-Za-z0-9]", "_", s)
        try:
            rows = FT.yahoo(s)
            _save(name + ".csv", "date,value\n" + "\n".join(f"{d},{v}" for d, v in rows), "w")
            man["series"][name] = {"ok": True, "first": rows[0][0], "last": rows[-1][0], "rows": len(rows)}
        except Exception as e:
            man["series"][name] = {"ok": False, "error": str(e)[:150]}
        time.sleep(0.8)
    for sid in FRED:
        try:
            rows, how = FT.fred(sid, {}, key)
            _save(sid + ".csv", "date,value\n" + "\n".join(f"{d},{v}" for d, v in rows), "w")
            man["series"][sid] = {"ok": True, "first": rows[0][0], "last": rows[-1][0], "rows": len(rows)}
        except Exception as e:
            man["series"][sid] = {"ok": False, "error": str(e)[:150]}
        time.sleep(0.6)
    for name, url in URLS.items():
        try:
            r = FT._get(url)
            _save(name, r.content)
            man["series"][name] = {"ok": True, "bytes": len(r.content)}
        except Exception as e:
            man["series"][name] = {"ok": False, "error": str(e)[:150]}
    # World Bank commodity prices (pink sheet): find the current monthly file link
    try:
        page = FT._get("https://www.worldbank.org/en/research/commodity-markets").text
        links = re.findall(r'https://thedocs\.worldbank\.org/[^"\']+CMO-Historical-Data-Monthly\.xlsx', page)
        r = FT._get(links[0])
        _save("wb_pinksheet_monthly.xlsx", r.content)
        man["series"]["wb_pinksheet_monthly.xlsx"] = {"ok": True, "bytes": len(r.content), "url": links[0]}
    except Exception as e:
        man["series"]["wb_pinksheet_monthly.xlsx"] = {"ok": False, "error": str(e)[:150]}
    for name, code in MSCI.items():
        try:
            url = ("https://app2.msci.com/products/service/index/indexmaster/getLevelDataForGraph?currency_symbol=USD"
                   f"&index_variant=GRTR&start_date=19691231&end_date={time.strftime('%Y%m%d')}"
                   f"&data_frequency=END_OF_MONTH&index_codes={code}")
            js = FT._get(url).json()
            rows = [(x["calc_date"], x["level_eod"]) for x in js["indexes"]["INDEX_LEVELS"]]
            _save(name + ".csv", "date,value\n" + "\n".join(f"{d},{v}" for d, v in rows), "w")
            man["series"][name] = {"ok": True, "first": rows[0][0], "last": rows[-1][0], "rows": len(rows)}
        except Exception as e:
            man["series"][name] = {"ok": False, "error": str(e)[:150]}
    _save("manifest.json", json.dumps(man, indent=1), "w")
    bad = [k for k, v in man["series"].items() if not v["ok"]]
    log(f"research fetch: {len(man['series']) - len(bad)} ok, {len(bad)} failed: {bad}")
    return man
