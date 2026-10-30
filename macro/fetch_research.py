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
    "TAIL", "BTAL", "DBMF", "KMLM", "CTA", "EPI", "KSA", "DXJ", "ENOR", "EWL", "EWI", "EWQ", "EWD", "EZU", "KWEB",
    "EWP", "EWN", "EPHE", "ASEA", "EMXC", "BWX", "BNDX", "XLY", "SOXX", "XBI", "IBB", "JETS", "LIT", "REMX", "^SKEW", "ES=F", "TRY=X", "ARS=X", "ZAR=X", "LTPZ", "VTIP", "SGOV", "TBF", "BIZD", "PSP", "VNQ", "XHB", "XLK", "XLF",
    # long-history indexes and futures (price only)
    "^GSPC", "^IXIC", "^RUT", "^N225", "^KS11", "^BVSP", "^HSI", "^TWII", "^BSESN", "^MXX", "^GDAXI", "^FTSE",
    "^FCHI", "^STOXX50E", "^AXJO", "^GSPTSE", "000001.SS", "^VIX", "^VIX3M", "^MOVE", "^TNX", "^IRX", "^TYX",
    "CL=F", "BZ=F", "GC=F", "SI=F", "HG=F", "NG=F", "PL=F", "ZC=F", "ZW=F", "ZS=F", "KC=F", "CT=F",
    "DX-Y.NYB", "EURUSD=X", "JPY=X", "KRW=X", "BRL=X", "CNY=X", "INR=X", "MXN=X", "AUDUSD=X", "BTC-USD",
    # round 4 (2026-10-30): Global Macro Book panel
    "HO=F", "RB=F", "SB=F", "LE=F", "HE=F", "CC=F", "PA=F", "ZL=F", "ZM=F", "KE=F", "ZN=F", "ZB=F", "ZF=F", "ZT=F",
    "6E=F", "6J=F", "6B=F", "6A=F", "6C=F", "6S=F", "6N=F", "6M=F", "NQ=F", "RTY=F", "YM=F", "NKD=F",
    "^SSMI", "^OMX", "^AEX", "^IBEX", "FTSEMIB.MI", "^NZ50", "^BFX", "^ATX", "PSI20.LS", "OSEBX.OL", "^OMXC25",
    "^NSEI", "^JN0U.JO", "EWO", "EWK", "EDEN", "NORW", "ENZL", "EIS", "EWZS", "FLBR", "SEKUSD=X", "NOKUSD=X",
    "NZDUSD=X", "CHF=X", "CAD=X", "GBPUSD=X", "TIP", "SCHP",
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
    # round 2 (2026-10-29): series named in the transcript rules
    "CPIENGSL", "CPIUFDSL", "CUSR0000SACL1E", "CUSR0000SASLE", "CPATAX", "A446RC1Q027SBEA", "PSAVERT", "REVOLSL",
    "GFDEGDQ188S", "MTSDS133FMS", "TDSP", "GACDFSA066MSFRBPHI", "IRLTLT01JPM156N", "IRLTLT01DEM156N",
    "IRLTLT01GBM156N", "JPNCPIALLMINMEI", "BRACPIALLMINMEI", "ECBDFR", "JPNASSETS", "ECBASSETSW", "TREAST",
    "FDHBFIN", "FDHBFRBN", "MICH", "OVXCLS", "BAMLH0A1HYBB", "NROU", "OPHNFB", "IPN213111N", "DTB3", "USEPUINDXM",
    "MCOILWTICO", "GDPDEF", "ULCNFB", "PRS85006173", "TNWBSHNO", "CMDEBT", "BCNSDODNS", "DSPIC96", "FGEXPND",
    "FGRECPT", "FDEFX", "B235RC1Q027SBEA", "IMPGS", "MHHNGSP", "GASREGW", "UNRATE", "IRSTCB01JPM156N",
    "IRSTCI01BRM156N", "IR3TIB01KRM156N", "RBJPBIS", "RBKRBIS", "RBBRBIS", "RBCNBIS", "RBEUBIS", "TWEXB",
    "BOGZ1FL073164003Q", "DRCCLACBS", "DRALACBS", "CORCCACBS", "WLRRAL",
    # round 3 (2026-10-29): data gaps named by the hypothesis coders
    "DGS1", "DGS5", "DGS7", "DGS20", "MSACSR", "AHETPI", "GGGDTAJPA188N", "IIPUSNETIQ", "CLF16OV", "MMMFFAQ027S",
    "DRBLACBS", "PURANUSDM", "PNGASEUUSDM", "CHNPIEATI01GYM", "XTIMVA01CNM667S", "DTCDFSA066MSFRBPHI",
    "PPCDFSA066MSFRBPHI", "NOFDFSA066MSFRBPHI", "NOCDFSA066MSFRBPHI", "TEDRATE", "DCPF3M", "WMTSECL1",
    "BOGZ1LM263064105Q", "CUSR0000SEHA", "CUSR0000SEHC", "FYOINT", "IRLTLT01ITM156N", "DBAA", "DAAA", "DROCLACBS",
    "GDPPOT", "A054RC1Q027SBEA", "A053RC1Q027SBEA", "PNFIC1", "Y033RC1Q027SBEA", "B985RC1Q027SBEA", "WFRBST01134",
    "IR3TIB01MXM156N", "IRSTCI01ZAM156N", "DEXSFUS", "IPG211111CN", "TRFVOLUSM227NFWA", "CES1000000001", "UNEMPLOY",
    "CPILFESL", "PCEPILFE", "BOPGSTB", "BOPBCA", "MANEMP", "AMTMNO", "DGORDER", "NEWORDER", "ACOGNO", "BAMLH0A0HYM2EY",
    "TOTCI", "RRSFS", "CP", "HOUST1F", "PERMIT1", "EXHOSLUSM495S", "MORTGAGE15US", "UMDMNO", "A065RC1A027NBEA",
    # round 5 (2026-10-30): month-end FX (H.10 daily) to replace monthly averages
    "DEXUSEU", "DEXJPUS", "DEXUSUK", "DEXSZUS", "DEXUSAL", "DEXUSNZ", "DEXCAUS", "DEXSDUS", "DEXNOUS", "DEXDNUS",
    "DEXHKUS", "DEXTAUS", "DEXSIUS", "DEXTHUS", "DEXMAUS",
    # round 4 (2026-10-30): Global Macro Book panel (64 markets) - OECD/BIS/FX series per country
    "IRLTLT01USM156N", "IRLTLT01CAM156N", "IRLTLT01AUM156N", "IRLTLT01NZM156N", "IRLTLT01CHM156N", "IRLTLT01SEM156N", "IRLTLT01NOM156N", "IRLTLT01DKM156N", "IRLTLT01FRM156N", "IRLTLT01ESM156N", "IRLTLT01NLM156N", "IRLTLT01BEM156N", "IRLTLT01ATM156N", "IRLTLT01PTM156N", "IRLTLT01KRM156N", "IRLTLT01MXM156N", "IRLTLT01ZAM156N", "IRLTLT01INM156N", "IRLTLT01EZM156N", "IR3TIB01USM156N", "IR3TIB01AUM156N", "IR3TIB01NZM156N", "IR3TIB01NOM156N", "IR3TIB01DKM156N", "IR3TIB01FRM156N", "IR3TIB01ESM156N", "IR3TIB01NLM156N", "IR3TIB01BEM156N", "IR3TIB01ATM156N", "IR3TIB01PTM156N", "IR3TIB01ZAM156N", "IR3TIB01INM156N", "IR3TIB01ITM156N", "IR3TIB01CNM156N", "CPALTT01USM659N", "CPALTT01CAM659N", "CPALTT01AUM659N", "CPALTT01NZM659N", "CPALTT01CHM659N", "CPALTT01SEM659N", "CPALTT01NOM659N", "CPALTT01DKM659N", "CPALTT01GBM659N", "CPALTT01DEM659N", "CPALTT01FRM659N", "CPALTT01ITM659N", "CPALTT01ESM659N", "CPALTT01NLM659N", "CPALTT01JPM659N", "CPALTT01MXM659N", "CPALTT01ZAM659N", "CPALTT01INM659N", "CPALTT01TWM659N", "CPALTT01EZM659N", "CANLOLITONOSTSAM", "AUSLOLITONOSTSAM", "NZLLOLITONOSTSAM", "CHELOLITONOSTSAM", "SWELOLITONOSTSAM", "NORLOLITONOSTSAM", "DNKLOLITONOSTSAM", "GBRLOLITONOSTSAM", "DEULOLITONOSTSAM", "FRALOLITONOSTSAM", "ITALOLITONOSTSAM", "ESPLOLITONOSTSAM", "NLDLOLITONOSTSAM", "JPNLOLITONOSTSAM", "MEXLOLITONOSTSAM", "ZAFLOLITONOSTSAM", "INDLOLITONOSTSAM", "TURLOLITONOSTSAM", "NAEXKP01USQ657S", "NAEXKP01CAQ657S", "NAEXKP01AUQ657S", "NAEXKP01NZQ657S", "NAEXKP01CHQ657S", "NAEXKP01SEQ657S", "NAEXKP01NOQ657S", "NAEXKP01DKQ657S", "NAEXKP01GBQ657S", "NAEXKP01DEQ657S", "NAEXKP01FRQ657S", "NAEXKP01ITQ657S", "NAEXKP01ESQ657S", "NAEXKP01NLQ657S", "NAEXKP01JPQ657S", "NAEXKP01KRQ657S", "NAEXKP01MXQ657S", "NAEXKP01ZAQ657S", "NAEXKP01INQ657S", "NAEXKP01BRQ657S", "NAEXKP01CNQ657S", "NBCABIS", "NBAUBIS", "NBNZBIS", "NBCHBIS", "NBSEBIS", "NBNOBIS", "NBDKBIS", "NBGBBIS", "NBXMBIS", "NBJPBIS", "NBKRBIS", "NBMXBIS", "NBBRBIS", "NBZABIS", "NBINBIS", "NBCNBIS", "NBTWBIS", "NBHKBIS", "EXUSAL", "EXUSNZ", "EXNOUS", "EXDNUS", "EXMXUS", "EXBZUS", "EXKOUS", "EXSFUS", "EXINUS", "EXCHUS", "EXHKUS", "EXTAUS", "EXCAUS", "EXJPUS", "EXSZUS", "EXSDUS", "EXUSUK", "EXUSEU", "EXGEUS", "BAA10YM", "AAA10YM", "GS1", "GS2", "GS5", "GS10", "GS20", "GS30", "TB3MS", "FEDFUNDS", "JLNUM1M", "JLNUM3M", "JLNUM12M", "LMNUF1M", "LMNUF3M", "LMNUF12M", "INTGSTINM193N", "INTDSRINM193N", "DEXGEUS", "DEXFRUS", "DEXITUS",
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

STOOQ = ["cl.f", "co.f", "ng.f", "ho.f", "rb.f", "gc.f", "si.f", "hg.f", "pl.f", "zc.f", "zw.f", "zs.f", "sb.f",
         "kc.f", "ct.f", "lc.f", "lh.f", "cc.f", "^dax", "^ukx", "^cac", "^nkx", "^spx", "^kospi", "^hsi", "^twse",
         "^bvp", "^ipc", "^snx", "^aor", "^tsx", "^smi", "^omxs", "^aex", "^ibex", "^fmib",
         # round 5: month-end government bond yields and FX (stooq), replacing OECD/FRED monthly averages
         "10usy.b", "10dey.b", "10uky.b", "10jpy.b", "10cay.b", "10auy.b", "10chy.b", "10fry.b", "10ity.b", "10esy.b",
         "10sey.b", "10noy.b", "10nzy.b", "2usy.b", "2dey.b", "2uky.b", "2jpy.b", "2cay.b", "2auy.b", "3musy.b",
         "eurusd", "gbpusd", "usdjpy", "usdchf", "audusd", "nzdusd", "usdcad", "usdsek", "usdnok", "usdmxn", "usdbrl",
         "usdkrw", "usdzar", "usdinr", "usdcny", "usdtwd", "usdhkd", "dx.f", "zb.f", "zn.f", "fgbl.f"]
DAILY = ["^GSPC", "SPY", "^VIX", "TLT", "IEF", "GLD", "^VIX3M", "DX-Y.NYB", "HYG"]
EXTRA_URLS = {
    "cboe_put_history.csv": "https://cdn.cboe.com/api/global/us_indices/daily_prices/PUT_History.csv",
    "cboe_ppt_history.csv": "https://cdn.cboe.com/api/global/us_indices/daily_prices/PPUT_History.csv",
    "cboe_bxm_history.csv": "https://cdn.cboe.com/api/global/us_indices/daily_prices/BXM_History.csv",
    "cboe_skew_history.csv": "https://cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv",
    "cboe_vix_history.csv": "https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv",
    "aaii_sentiment.xls": "https://www.aaii.com/files/surveys/sentiment.xls",
    "nyfed_gscpi.xlsx": "https://www.newyorkfed.org/medialibrary/research/interactives/gscpi/downloads/gscpi_data.xlsx",
    "acm_term_premia.xls": "https://www.newyorkfed.org/medialibrary/media/research/data_indicators/ACMTermPremium.xls",
    "trade_epu.xlsx": "https://www.policyuncertainty.com/media/Categorical_EPU_Data.xlsx",
    "ebp_gz.csv": "https://www.federalreserve.gov/econres/notes/feds-notes/ebp_csv.csv",
    "french_49ind.zip": "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/49_Industry_Portfolios_CSV.zip",
    "french_beta.zip": "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/Portfolios_Formed_on_BETA_csv.zip",
    "french_6port.zip": "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/6_Portfolios_2x3_CSV.zip",
    # round 6 (2026-10-30): month-end government bond yields from central banks (stooq now blocks scripts)
    "cb_de_10y.csv": "https://api.statistiken.bundesbank.de/rest/download/BBSIS/D.I.ZST.ZI.EUR.S1311.B.A604.R10XX.R.A.A._Z._Z.A?format=csv&lang=en",
    "cb_de_2y.csv": "https://api.statistiken.bundesbank.de/rest/download/BBSIS/D.I.ZST.ZI.EUR.S1311.B.A604.R02XX.R.A.A._Z._Z.A?format=csv&lang=en",
    "cb_jp_jgb_all.csv": "https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/historical/jgbcme_all.csv",
    "cb_jp_jgb_recent.csv": "https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/jgbcme.csv",
    "cb_ca_yields.csv": "https://www.bankofcanada.ca/valet/observations/BD.CDN.2YR.DQ.YLD,BD.CDN.10YR.DQ.YLD/csv?start_date=1980-01-01",
    "cb_au_f2_hist.xls": "https://www.rba.gov.au/statistics/tables/xls-hist/f02dhist.xls",
    "cb_au_f2.csv": "https://www.rba.gov.au/statistics/tables/csv/f2-data.csv",
    # round 9: EIA NYMEX futures, contracts 1-4 (energy curves from 1983-94); AQR Commodities for the Long Run
    "eia_cl1.xls": "https://www.eia.gov/dnav/pet/hist_xls/RCLC1d.xls",
    "eia_ng1.xls": "https://www.eia.gov/dnav/ng/hist_xls/RNGC1d.xls",
    "eia_ho1.xls": "https://www.eia.gov/dnav/pet/hist_xls/EER_EPD2F_PE1_Y35NY_DPGd.xls",
    "eia_rb1.xls": "https://www.eia.gov/dnav/pet/hist_xls/EER_EPMRR_PE1_Y35NY_DPGd.xls",
    "eia_cl2.xls": "https://www.eia.gov/dnav/pet/hist_xls/RCLC2d.xls",
    "eia_ng2.xls": "https://www.eia.gov/dnav/ng/hist_xls/RNGC2d.xls",
    "eia_ho2.xls": "https://www.eia.gov/dnav/pet/hist_xls/EER_EPD2F_PE2_Y35NY_DPGd.xls",
    "eia_rb2.xls": "https://www.eia.gov/dnav/pet/hist_xls/EER_EPMRR_PE2_Y35NY_DPGd.xls",
    "eia_cl3.xls": "https://www.eia.gov/dnav/pet/hist_xls/RCLC3d.xls",
    "eia_ng3.xls": "https://www.eia.gov/dnav/ng/hist_xls/RNGC3d.xls",
    "eia_ho3.xls": "https://www.eia.gov/dnav/pet/hist_xls/EER_EPD2F_PE3_Y35NY_DPGd.xls",
    "eia_rb3.xls": "https://www.eia.gov/dnav/pet/hist_xls/EER_EPMRR_PE3_Y35NY_DPGd.xls",
    "eia_cl4.xls": "https://www.eia.gov/dnav/pet/hist_xls/RCLC4d.xls",
    "eia_ng4.xls": "https://www.eia.gov/dnav/ng/hist_xls/RNGC4d.xls",
    "eia_ho4.xls": "https://www.eia.gov/dnav/pet/hist_xls/EER_EPD2F_PE4_Y35NY_DPGd.xls",
    "eia_rb4.xls": "https://www.eia.gov/dnav/pet/hist_xls/EER_EPMRR_PE4_Y35NY_DPGd.xls",
    "aqr_commodities_long_run.xlsx": "https://images.aqr.com/-/media/AQR/Documents/Insights/Data-Sets/Commodities-for-the-Long-Run-Index-Level-Data-Monthly.xlsx",
    # round 8: Ken French international country portfolios (value-weighted by country, with and without dividends)
    "french_intl_countries_ff.zip": "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_International_Countries.zip",
    "french_intl_countries_ff_xdiv.zip": "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_International_Countries_Wout_Div.zip",
    # round 7: longer histories (Bundesbank monthly end-of-month from 1972; Bank of Canada legacy benchmark series)
    "cb_de_10y_m.csv": "https://api.statistiken.bundesbank.de/rest/download/BBSIS/M.I.ZST.ZI.EUR.S1311.B.A604.R10XX.R.A.A._Z._Z.A?format=csv&lang=en",
    "cb_de_2y_m.csv": "https://api.statistiken.bundesbank.de/rest/download/BBSIS/M.I.ZST.ZI.EUR.S1311.B.A604.R02XX.R.A.A._Z._Z.A?format=csv&lang=en",
    "cb_ca_yields_legacy.csv": "https://www.bankofcanada.ca/valet/observations/V122487,V122538/csv?start_date=1980-01-01",
    "cb_gb_yields.csv": "https://www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns.asp?csv.x=yes&Datefrom=01/Jan/1970&Dateto=now&SeriesCodes=IUDMNPY,IUDSNPY&CSVF=TN&UsingCodes=Y&VPD=Y&VFD=N",
}


def yahoo_daily(sym):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}"
    js = FT._get(url, params={"period1": 0, "period2": 9999999999, "interval": "1d", "events": "div,split",
                              "includeAdjustedClose": "true"}).json()
    res = js["chart"]["result"][0]
    adj = res["indicators"].get("adjclose", [{}])[0].get("adjclose") or res["indicators"]["quote"][0]["close"]
    return [(time.strftime("%Y-%m-%d", time.gmtime(t)), round(float(v), 6)) for t, v in zip(res["timestamp"], adj) if v is not None]


MSCI = {   # MSCI end-of-month gross USD index levels (public chart endpoint; may refuse)
    "msci_world": "990100", "msci_em": "891800", "msci_korea": "134000", "msci_brazil": "38000",
    "msci_china": "302400", "msci_india": "935600", "msci_japan": "39200", "msci_taiwan": "938800",
    "msci_mexico": "273000", "msci_eafe": "990300", "msci_acwi": "892400",
}


def _save(name, content, mode="wb"):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), mode) as f:
        f.write(content)


FRESH_DAYS = 7        # a series fetched OK within this many days is kept from the previous run (incremental)
BUDGET_S = 40 * 60   # stop starting new downloads after this many seconds (workflow limit is 60 minutes)
STOOQ_ON = False     # stooq.com refuses scripted downloads since 2026-10 (returns an HTML page)


class _Man(dict):
    """Manifest that carries forward fresh OK entries from the previous run and enforces the time budget."""

    def __init__(self, prev, t0, prev_at):
        super().__init__()
        self.prev, self.t0, self.prev_at, self.skipped, self.fails, self.group = prev, t0, prev_at, 0, {}, ""

    def fresh(self, name):
        v = self.prev.get(name)
        f = os.path.join(OUT, name if "." in name else name + ".csv")
        if not os.path.exists(f) or os.path.getsize(f) < 200 or open(f, "rb").read(1) == b"<":
            return False
        if v is None and self.prev:          # file left over from a source no longer in the manifest
            return False
        at = (v or {}).get("at", self.prev_at)
        ok = (v is None or v.get("ok")) and time.time() - at < FRESH_DAYS * 86400
        if ok:
            dict.__setitem__(self, name, dict(v or {"ok": True}, at=at))
            self.skipped += 1
        return ok

    def over(self, name, group):
        """True when the budget is spent or this group has failed 4 times in a row (skip the rest of it)."""
        self.group = group
        if time.time() - self.t0 > BUDGET_S or self.fails.get(group, 0) >= (25 if group in ("fred", "yahoo") else 4):
            dict.__setitem__(self, name, {"ok": False, "error": "skipped (time budget or source down)"})
            return True
        return False

    def __setitem__(self, k, v):
        if isinstance(v, dict) and "ok" in v:
            v = dict(v, at=time.time())
            self.fails[self.group] = 0 if v["ok"] else self.fails.get(self.group, 0) + 1
        super().__setitem__(k, v)


def run(log=print):
    key = os.environ.get("FRED_API_KEY", "").strip()
    t0 = time.time()
    try:
        pm = json.load(open(os.path.join(OUT, "manifest.json")))
        prev = pm["series"]
        prev_at = time.mktime(time.strptime(pm["fetched"], "%Y-%m-%d %H:%M UTC")) - time.timezone
    except Exception:  # noqa: BLE001
        prev, prev_at = {}, time.time()      # no manifest: trust valid files already on disk (from branch macro-data)
    man = {"fetched": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()), "series": _Man(prev, t0, prev_at)}
    S_ = man["series"]
    for s in YAHOO:
        name = "Y_" + re.sub(r"[^A-Za-z0-9]", "_", s)
        if S_.fresh(name) or S_.over(name, "yahoo"):
            continue
        try:
            rows = FT.yahoo(s)
            _save(name + ".csv", "date,value\n" + "\n".join(f"{d},{v}" for d, v in rows), "w")
            man["series"][name] = {"ok": True, "first": rows[0][0], "last": rows[-1][0], "rows": len(rows)}
        except Exception as e:
            man["series"][name] = {"ok": False, "error": str(e)[:150]}
        time.sleep(0.8)
    for sid in FRED:
        if S_.fresh(sid) or S_.over(sid, "fred"):
            continue
        try:
            rows, how = FT.fred(sid, {}, key)
            _save(sid + ".csv", "date,value\n" + "\n".join(f"{d},{v}" for d, v in rows), "w")
            man["series"][sid] = {"ok": True, "first": rows[0][0], "last": rows[-1][0], "rows": len(rows)}
        except Exception as e:
            man["series"][sid] = {"ok": False, "error": str(e)[:150]}
        time.sleep(0.6)
    for name, url in URLS.items():
        if S_.fresh(name) or S_.over(name, "urls"):
            continue
        try:
            r = FT._get(url)
            _save(name, r.content)
            man["series"][name] = {"ok": True, "bytes": len(r.content)}
        except Exception as e:
            man["series"][name] = {"ok": False, "error": str(e)[:150]}
    for name, url in EXTRA_URLS.items():
        if S_.fresh(name) or S_.over(name, name.split("_")[1] if name.startswith("cb_") else "extra"):
            continue
        try:
            r = FT._get(url)
            _save(name, r.content)
            man["series"][name] = {"ok": True, "bytes": len(r.content)}
        except Exception as e:
            man["series"][name] = {"ok": False, "error": str(e)[:150]}
    for s_ in DAILY:
        name = "D_" + re.sub(r"[^A-Za-z0-9]", "_", s_)
        if S_.fresh(name) or S_.over(name, "daily"):
            continue
        try:
            rows = yahoo_daily(s_)
            _save(name + ".csv", "date,value\n" + "\n".join(f"{d},{v}" for d, v in rows), "w")
            man["series"][name] = {"ok": True, "first": rows[0][0], "last": rows[-1][0], "rows": len(rows)}
        except Exception as e:
            man["series"][name] = {"ok": False, "error": str(e)[:150]}
        time.sleep(1.0)
    import zipfile
    cot = []                                  # CFTC legacy futures-only, all years (net speculative positioning)
    S_.group = "cftc"
    for yr_ in range(1986, int(time.strftime("%Y")) + 1) if not S_.fresh("cftc_cot_selected.csv") else []:
        try:
            url = (f"https://www.cftc.gov/files/dea/history/deacot{yr_}.zip" if yr_ >= 1995 else None)
            if yr_ < 1995:
                continue
            z = zipfile.ZipFile(io.BytesIO(FT._get(url).content))
            txt = z.read(z.namelist()[0]).decode("latin-1")
            keep = [ln for ln in txt.splitlines()[1:] if re.search(r"S&P 500|E-MINI S&P|GOLD - COMMODITY|CRUDE OIL, LIGHT SWEET|COPPER|U\.S\. TREASURY BONDS|10-YEAR|JAPANESE YEN|EURO FX|U\.S\. DOLLAR INDEX|SILVER - COMMODITY|VIX", ln)]
            cot.append(txt.splitlines()[0] if not cot else None)
            cot.extend(keep)
        except Exception as e:
            man["series"][f"cot{yr_}"] = {"ok": False, "error": str(e)[:100]}
    if cot:
        _save("cftc_cot_selected.csv", "\n".join(x for x in cot if x), "w")
        man["series"]["cftc_cot_selected.csv"] = {"ok": True, "rows": len(cot)}
    # MSCI: try the alternative public endpoint too
    # World Bank commodity prices (pink sheet): find the current monthly file link
    try:
        if S_.fresh("wb_pinksheet_monthly.xlsx") or S_.over("wb_pinksheet_monthly.xlsx", "wb"):
            raise StopIteration
        page = FT._get("https://www.worldbank.org/en/research/commodity-markets").text
        links = re.findall(r'https://thedocs\.worldbank\.org/[^"\']+CMO-Historical-Data-Monthly\.xlsx', page)
        r = FT._get(links[0])
        _save("wb_pinksheet_monthly.xlsx", r.content)
        man["series"]["wb_pinksheet_monthly.xlsx"] = {"ok": True, "bytes": len(r.content), "url": links[0]}
    except StopIteration:
        pass
    except Exception as e:
        man["series"]["wb_pinksheet_monthly.xlsx"] = {"ok": False, "error": str(e)[:150]}
    for name, code in MSCI.items():
        if S_.fresh(name) or S_.over(name, "msci"):
            continue
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
    for sym in STOOQ if STOOQ_ON else []:     # stooq.com free long histories (continuous futures, indexes); monthly
        name = "S_" + re.sub(r"[^A-Za-z0-9]", "_", sym)
        if S_.fresh(name) or S_.over(name, "stooq"):
            continue
        try:
            txt = FT._get("https://stooq.com/q/d/l/", params={"s": sym, "i": "m"}).text
            if not txt.startswith("Date"):
                raise ValueError(txt[:80])
            _save(name + ".csv", txt, "w")
            lines = txt.strip().splitlines()
            man["series"][name] = {"ok": True, "first": lines[1][:10], "last": lines[-1][:10], "rows": len(lines) - 1}
        except Exception as e:
            man["series"][name] = {"ok": False, "error": str(e)[:150]}
        time.sleep(1.5)
    for name, url in {}.items():   # JLN uncertainty and French international index files: URLs return 404 (2026-10)
        try:
            r = FT._get(url)
            _save(name, r.content)
            man["series"][name] = {"ok": True, "bytes": len(r.content)}
        except Exception as e:
            man["series"][name] = {"ok": False, "error": str(e)[:150]}
    man["series"] = dict(S_)
    _save("manifest.json", json.dumps(man, indent=1), "w")
    bad = [k for k, v in man["series"].items() if not v["ok"]]
    log(f"research fetch: {len(man['series']) - len(bad)} ok ({S_.skipped} kept from the previous run), "
        f"{len(bad)} failed in {time.time() - t0:.0f}s: {bad}")
    return man
