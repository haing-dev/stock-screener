"""Bloomberg pull v5 (2026-11-04): supplement workbooks to v4 (Bloomberg_macro_UBC.xlsx), built for the pod-model
research program (Layer 0 indicator list + Global Macro Book batches 2+). Same block layout as v4 (row 2 label, row 3
ticker, row 4 field names, row 5 BDH formula spilling down), so one reader handles every file.

python3 docs/data_requests/build_bloomberg_v5.py OUT_DIR  -> 2_..6_ workbooks + bloomberg_v5_tickers.csv
Labels ending in '?' are best-guess tickers: the Check sheet (BDP NAME) shows invalid ones first.
"""
import csv
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter as L

F = "Arial"
YEL = PatternFill("solid", start_color="FFFF00")
MON = '"Per=M","Days=A","Fill=P","Dir=V","Dts=S"'
DAY = '"Per=D","Days=W","Fill=B","Dir=V","Dts=S"'
M0, D0 = "12/31/1969", "12/31/1989"
NM, ND = 683, 9200          # periods (upper bound) for the point estimates
ECOF = "ECO_RELEASE_DT,ACTUAL_RELEASE,BN_SURVEY_MEDIAN,PX_LAST"
EQF = "TOT_RETURN_INDEX_GROSS_DVDS,PX_LAST,PE_RATIO,BEST_PE_RATIO,BEST_EPS,PX_TO_BOOK_RATIO,EQY_DVD_YLD_12M,CUR_MKT_CAP"
ETFF = "TOT_RETURN_INDEX_GROSS_DVDS,PX_LAST,FUND_TOTAL_ASSETS,EQY_SH_OUT"
FUTF = "PX_LAST,OPEN_INT,PX_VOLUME,FUT_AGGTE_OPEN_INT,FUT_AGGTE_VOL"


def T(s, suffix):
    """'Label|TICKER;Label2|TICKER2' -> [(label, 'TICKER suffix')]"""
    out = []
    for part in s.strip().split(";"):
        part = part.strip()
        if part:
            lab, tk = [x.strip() for x in part.split("|")]
            if tk.endswith("?"):
                tk = tk.rstrip(" ?")
                lab = lab if lab.endswith("?") else lab + " ?"
            out.append((lab, tk + " " + suffix))
    return out


# ---------------------------------------------------------------- 2: economics, policy, money, conditions (monthly)
ECO_US = T("""US core CPI y/y|CPI XYOY;US core CPI m/m|CPUPXCHG;US CPI m/m|CPI CHNG;US PCE deflator y/y|PCE DEFY;
US core PCE y/y|PCE CYOY;US PPI final demand y/y|PPI YOY;US import prices y/y|IMP1YOY%;US avg hourly earnings y/y|AHE YOY%;
US employment cost index q/q|ECI SA%;US initial jobless claims|INJCJC;US continuing claims|INJCSP;US JOLTS openings|JLTOTOTL;
US ISM services|NAPMNMI;US ISM new orders|NAPMNEWO;US ISM prices paid|NAPMPRIC;US ISM employment|NAPMEMPL;
US Chicago PMI|CHPMINDX;US Philly Fed|OUTFGAF;US Empire State|EMPRGBCI;US Michigan sentiment|CONSSENT;
US Michigan 1y inflation expectation|CONSP5MD;US Michigan 5-10y inflation expectation|CONSPXMD;US Conference Board confidence|CONCCONF;
US NFIB small business|SBOITOTL;US retail sales control group m/m|RSTAXAG%;US industrial production level|IP;
US capacity utilisation|CPTICHNG;US durable goods m/m|DGNOCHNG;US core capex orders m/m|CGNOXAI%;US housing starts|NHSPSTOT;
US building permits|NHSPATOT;US new home sales|NHSLTOT;US existing home sales|ETSLTOTL;US Case-Shiller 20 y/y|SPCS20Y%;
US NAHB housing index|USHBMIDX;US leading index m/m|LEI CHNG;US personal income m/m|PITLCHNG;US personal spending m/m|PCE CRCH;
US saving rate|PITLSAVE ?;US trade balance|USTBTOT;US federal budget balance|FDDSSD;US GDP price index|GDP PIQQ;
US real GDP y/y|GDP CYOY;US Atlanta Fed GDPNow ?|GDGCAFJP;US senior loan officers C&I tightening|SLDETIGT;
US consumer credit|CICRTOT;US nonfarm productivity|PRODNFR;US unit labour costs|COSTNFR;US labour force participation|PRUSTOT;
US U6 underemployment|USUDMAER;US Chicago Fed national activity|CFNAI""", "Index")
ECO_INTL = T("""Euro core HICP y/y|CPEXEMUY;Euro composite PMI|MPMIEZCA;Euro services PMI|MPMIEZSA;Euro economic sentiment|EUESEMU;
Euro retail sales y/y|RSSAEMUY ?;Euro industrial production y/y|EUITEMUY;Euro M3 y/y|ECMAM3YY;Euro loans to companies y/y ?|ECMSLNFY;
Germany ZEW expectations|GRZEWI;Germany Ifo expectations|GRIFPEX;Germany manufacturing PMI|MPMIDEMA;Germany factory orders y/y|GRIORTYA ?;
Sentix euro investor confidence|SNTEEUGX;France manufacturing PMI|MPMIFRMA;Italy manufacturing PMI|MPMIITMA;Spain manufacturing PMI|MPMIESMA;
UK services PMI|MPMIGBSA;UK GDP q/q|UKGRABIQ;UK retail sales y/y|UKRVAYOY ?;UK average earnings ex bonus y/y ?|UKAWXTOM;UK core CPI y/y ?|UKHCA9IQ;
Japan core CPI y/y (ex fresh food)|JNCPIXFF;Japan manufacturing PMI|MPMIJPMA;Japan Tankan non-manufacturers|JNTSNMFG;Japan GDP q/q annualised|JGDPAGDP;
Japan machinery orders y/y ?|JNMOCHNY;Japan exports y/y|JNTBEXPY;Japan wages y/y ?|JNLSUCTL;Canada GDP m/m ?|CGE9MOM;Canada Ivey PMI ?|IVEY;
Canada employment change|CANLNETJ;Australia GDP y/y|AUNAGDPY;Australia employment change|AUEMC;Australia NAB business confidence ?|NABSCONF;
New Zealand CPI y/y|NZCPIYOY;Switzerland CPI y/y|SZCPIYOY;Switzerland KOF leading ?|KOFETOT;Sweden CPI y/y|SWCPYOY;Norway CPI y/y|NOCPIYOY;
China GDP y/y|CNGDPYOY;China Caixin manufacturing PMI|MPMICNMA;China official non-manufacturing PMI|CPMINMAN ?;China retail sales y/y|CNRSCYOY;
China fixed asset investment ytd y/y|CNFAYOY;China exports y/y|CNFREXPY;China imports y/y|CNFRIMPY;China PPI y/y|CHEFTYOY;China M2 y/y|CNMS2YOY;
China new yuan loans|CNLNNEW;China aggregate financing ?|CNLNTSF;China foreign reserves|CNGFOREX;Korea exports y/y|KOEXTOTY;Taiwan exports y/y ?|TWTREXPY;
Korea manufacturing PMI|MPMIKRMA;Taiwan manufacturing PMI|MPMITWMA;India CPI y/y|INFUTOTY;India industrial production y/y|INPIINDY;
India manufacturing PMI|MPMIINMA;Brazil unemployment|BZUETOTN;Brazil industrial production y/y|BZIPYOY%;Mexico industrial production y/y ?|MXIPTYOY;
Mexico unemployment ?|MXUEUNSA;Indonesia CPI y/y|IDCPIY;Turkey CPI y/y|TUCPIY;Poland CPI y/y|POCPIYOY;Russia CPI y/y ?|RUCPIYOY;
Global manufacturing PMI|MPMIGLMA;Global composite PMI|MPMIGLCA;EM manufacturing PMI ?|MPMIEMMA;OECD US leading indicator ?|OEUSKLAC""", "Index")
POLICY = T("""Fed funds target upper|FDTR;Fed funds lower|FDTRFTRL;Fed funds effective|FEDL01;SOFR|SOFRRATE;US 2y Treasury|USGG2YR;
ECB main refi|EURR002W;ECB deposit rate|EUORDEPO;ESTR|ESTRON ?;EONIA (to 2021)|EONIA;BoE Bank Rate|UKBRBASE;BoJ policy rate ?|BOJDTR;
Japan uncollateralised call|MUTKCALM;Bank of Canada|CABROVER;RBA cash rate|RBATCTR;SNB policy rate ?|SZLTTR;Riksbank|SWRRATEI;Norges Bank|NOBRDEP;
RBNZ OCR|NZOCRS;Brazil Selic target|BZSTSETA;Banxico target|MXONBR;SARB repo|SARPRT;RBI repo ?|INRPYLD;Bank of Korea|KORP7D ?;
China 1y loan prime rate ?|CHLR12M;PBoC 7d reverse repo ?|CHRR7D ?;Turkey 1w repo ?|TUBR1W ?;Indonesia BI rate ?|IDBIRATE;
Poland reference rate|PORERATE ?;Fed total assets|FARBAST;Fed reserve balances ?|FARBRSBL ?;Fed reverse repo ?|RRPONTSYD;
ECB total assets|EBBSTOTA;BoJ total assets|BJACTOTL;BoE total assets ?|UKBSTOTA ?;SNB sight deposits ?|SZNBSIGH ?;
US M2 y/y ?|M2% YOY;US M2 level|M2;Euro M1 y/y ?|ECMAM1YY;Japan M2 y/y ?|JNMSM2Y;NY Fed ACM 10y term premium|ACMTP10;
Kim-Wright 10y term premium ?|THREEFYTP10""", "Index")
CONDITIONS = T("""Bloomberg US financial conditions|BFCIUS;Bloomberg euro financial conditions ?|BFCIEU;Goldman US financial conditions ?|GSUSFCI;
Chicago Fed NFCI|NFCIINDX;St Louis Fed stress ?|STLFSI4;OFR financial stress ?|OFRFSI;Citi surprise US inflation ?|CESIUSDI ?;
Citi surprise euro inflation ?|CESIEURI ?;Citi surprise Sweden ?|CESISEK;Citi surprise Switzerland ?|CESICHF;Citi surprise Norway ?|CESINOK;
Citi surprise NZ ?|CESINZD;Citi surprise Asia Pacific ?|CESIAPAC;Citi surprise LatAm ?|CESILTAM;Citi surprise EEMEA ?|CESIEEMA ?;
Bloomberg US surprise ?|BBGUSSUR ?;Economic policy uncertainty US ?|EPUCNUSD;Global economic policy uncertainty ?|EPUCGLCP;
AAII bulls|AAIIBULL;AAII bears|AAIIBEAR;CBOE equity put/call|PCUSEQTR;CBOE total put/call ?|PCUSTOTR ?;
Investors Intelligence bulls ?|BULLISH ?""", "Index")

# ---------------------------------------------------------------- 3: rates, credit, FX (monthly)
YLD_EXTRA = []
for cty, fmt, mats in [("US", "USGG%s Index", ("3M", "6M", "12M", "1YR", "3YR", "20YR")),
                       ("Japan", "GJGB%s Index", ("1", "3", "20", "40")),
                       ("Germany", "GDBR%s Index", ("1", "3", "20")), ("UK", "GUKG%s Index", ("1", "3", "20")),
                       ("Spain", "GSPG%sYR Index", ("2", "5", "10")), ("Netherlands", "GNTH%sYR Index", ("2", "10")),
                       ("Belgium", "GBGB%sYR Index", ("2", "10")), ("Austria ?", "GAGB%sYR Index", ("10",)),
                       ("Ireland", "GIGB%sYR Index", ("10",)), ("Portugal", "GSPT%sYR Index", ("10",)),
                       ("Greece", "GGGB%sYR Index", ("10",)), ("Norway", "GNOR%sYR Index", ("2", "10")),
                       ("Denmark", "GDGB%sYR Index", ("2", "10")), ("New Zealand", "GNZGB%s Index", ("2", "10")),
                       ("Korea", "GVSK%sYR Index", ("3", "10")), ("China", "GCNY%sYR Index", ("2", "10")),
                       ("India", "GIND%sYR Index", ("2", "10")), ("Indonesia", "GIDN%sYR Index", ("2", "10")),
                       ("Thailand ?", "GVTL%sYR Index", ("2", "10")), ("Malaysia ?", "MGIY%sY Index", ("3", "10")),
                       ("Singapore ?", "MASB%sY Index", ("2", "10")), ("Hong Kong ?", "HKGG%sY Index", ("2", "10")),
                       ("Taiwan ?", "GTWN%sY Index", ("10",)), ("Philippines ?", "PDSF%sYR Index", ("10",)),
                       ("Brazil ?", "GEBR%sY Index", ("2", "10")), ("Mexico ?", "GMXN%sYR Index", ("2", "10")),
                       ("Colombia ?", "GCOL%sY Index", ("10",)), ("Chile ?", "CLGB%sY Index", ("10",)),
                       ("Peru ?", "GRPE%sY Index", ("10",)), ("South Africa ?", "GSAB%sYR Index", ("2", "10")),
                       ("Poland", "POGB%sYR Index", ("2", "10")), ("Hungary", "GHGB%sYR Index", ("3", "10")),
                       ("Czech", "CZGB%sYR Index", ("2", "10")), ("Turkey ?", "IECM%sY Index", ("2", "10")),
                       ("Israel ?", "GISR%sYR Index", ("2", "10")), ("Russia ?", "RUGE%sY Index", ("10",))]:
    for m in mats:
        YLD_EXTRA.append(("%s %s" % (cty.replace(" ?", ""), m) + (" ?" if "?" in cty else ""), fmt % m))
SWAPS = []
for lab, fmt, mats in [("USD swap (Libor, to 2023)", "USSW%s Curncy", ("2", "5", "10", "30")),
                       ("USD SOFR swap", "USOSFR%s Curncy", ("1", "2", "5", "10", "30")),
                       ("EUR swap", "EUSA%s Curncy", ("2", "5", "10", "30")), ("GBP swap", "BPSW%s Curncy", ("2", "5", "10", "30")),
                       ("GBP SONIA swap ?", "BPSWS%s Curncy", ("1", "2", "10")), ("JPY swap", "JYSW%s Curncy", ("2", "5", "10", "30")),
                       ("CAD swap", "CDSW%s Curncy", ("2", "5", "10")), ("AUD swap ?", "ADSWAP%s Curncy", ("2", "5", "10")),
                       ("CHF swap", "SFSW%s Curncy", ("2", "10")), ("SEK swap", "SKSW%s Curncy", ("2", "10")),
                       ("NOK swap", "NKSW%s Curncy", ("2", "10")), ("NZD swap ?", "NDSWAP%s Curncy", ("2", "10")),
                       ("USD OIS (Fed funds) ?", "USSO%s Curncy", ("1", "2", "5")), ("EUR OIS ?", "EESWE%s Curncy", ("1", "2", "5")),
                       ("USD inflation swap", "USSWIT%s Curncy", ("1", "2", "5", "10", "30")),
                       ("EUR inflation swap", "EUSWI%s Curncy", ("1", "2", "5", "10")),
                       ("GBP RPI inflation swap ?", "BPSWIT%s Curncy", ("5", "10")), ("JPY inflation swap ?", "JYSWIT%s Curncy", ("10",)),
                       ("USD swaption normal vol 1y10y ?", "USSN0%s Curncy", ("110",)),
                       ("USD swaption normal vol 3m10y ?", "USSN0%s Curncy", ("C10",))]:
    for m in mats:
        SWAPS.append(("%s %s" % (lab.replace(" ?", ""), m) + (" ?" if "?" in lab else ""), fmt % m))
SWAPS += T("""US 5y5y inflation swap forward|FWISUS55;Euro 5y5y inflation swap forward|FWISEU55;UK 5y5y inflation swap forward ?|FWISBP55;
US 5y breakeven|USGGBE05;US 30y breakeven ?|USGGBE30;US 5y real yield|USGGT05Y;US 30y real yield|USGGT30Y;US 2y10y slope ?|USYC2Y10;
US 3m10y slope ?|USYC3M10 ?;US 10y swap spread ?|USSP10;US 30y swap spread ?|USSP30;Euribor-OIS 3m ?|EUR003M ?;
FRA-OIS 3m ?|USFOSC1 ?;TED spread ?|BASPTDSP""", "Index")
CREDIT = T("""US IG OAS|LUACOAS;US HY OAS|LF98OAS;US IG total return|LUACTRUU;US HY total return|LF98TRUU;US Aggregate total return|LBUSTRUU;
US Treasury total return|LUATTRUU;US long Treasury total return ?|LUTLTRUU;US TIPS total return ?|LBUTTRUU;Global Aggregate TR (unhedged)|LEGATRUU;
Global Aggregate TR (USD hedged) ?|LEGATRUH;Global Treasury TR ?|LGTRTRUU;Euro Aggregate TR ?|LBEATREU;Euro corporate OAS ?|LECPOAS;
Pan-European HY OAS ?|LP01OAS;Euro HY total return ?|LP01TREU;EM USD aggregate OAS ?|EMUSOAS ?;EM USD aggregate TR ?|EMUSTRUU;
JPM EMBI Global Diversified spread ?|JPEIDIVS ?;JPM EMBI Global Diversified TR ?|JPEIDIVR;JPM GBI-EM Global Diversified TR ?|JGENVUUG;
US BBB OAS ?|LUCBOAS ?;US CCC OAS ?|LF98CCC ?;Leveraged loan index ?|SPBDAL;Moody's Baa yield ?|MOODCBAA;Moody's Aaa yield ?|MOODCAAA""", "Index")
CREDIT += T("""CDX IG 5y|CDX IG CDSI GEN 5Y;CDX HY 5y price|CDX HY CDSI GEN 5Y PRC;CDX EM 5y price ?|CDX EM CDSI GEN 5Y PRC;
iTraxx Europe main 5y|ITRX EUR CDSI GEN 5Y;iTraxx crossover 5y|ITRX XOVER CDSI GEN 5Y;iTraxx senior financials 5y ?|ITRX SNRFIN CDSI GEN 5Y""", "Corp")
CREDIT += [("%s sovereign CDS 5y ?" % c, "%s CDS USD SR 5Y D14 Corp" % c.upper()) for c in
           ("Italy", "Spain", "France", "Germany", "United States", "Japan", "China", "Brazil", "Mexico", "Turkey", "South Africa",
            "Indonesia", "Korea", "UK", "Greece", "Portugal")]
FX_SPOT = T("""EURUSD|EURUSD;USDJPY|USDJPY;GBPUSD|GBPUSD;AUDUSD|AUDUSD;NZDUSD|NZDUSD;USDCAD|USDCAD;USDCHF|USDCHF;USDSEK|USDSEK;USDNOK|USDNOK;
USDDKK|USDDKK;EURJPY|EURJPY;EURGBP|EURGBP;EURCHF|EURCHF;AUDJPY|AUDJPY;USDCNY|USDCNY;USDCNH|USDCNH;USDHKD|USDHKD;USDSGD|USDSGD;USDKRW|USDKRW;
USDTWD|USDTWD;USDINR|USDINR;USDIDR|USDIDR;USDMYR|USDMYR;USDTHB|USDTHB;USDPHP|USDPHP;USDBRL|USDBRL;USDMXN|USDMXN;USDCLP|USDCLP;USDCOP|USDCOP;
USDPEN|USDPEN;USDARS|USDARS;USDZAR|USDZAR;USDTRY|USDTRY;USDPLN|USDPLN;USDHUF|USDHUF;USDCZK|USDCZK;USDILS|USDILS;USDRUB|USDRUB;USDSAR|USDSAR;
Gold spot|XAU;Silver spot|XAG;Platinum spot|XPT;Palladium spot|XPD;Bitcoin|XBTUSD;Ether|XETUSD;
USDDEM (pre-1999) ?|USDDEM;USDFRF (pre-1999) ?|USDFRF;USDITL (pre-1999) ?|USDITL;USDESP (pre-1999) ?|USDESP;USDNLG (pre-1999) ?|USDNLG;
USDXEU (ECU) ?|USDXEU""", "Curncy")
FX_SPOT += T("""Dollar index DXY|DXY;Bloomberg dollar index|BBDXY;JPM EM FX index ?|FXJPEMCS;Bloomberg EM FX carry index ?|FXCTEM8;
Deutsche Bank G10 FX carry ?|DBHVG10U ?""", "Index")
FX_FWD = []
for p in ("EUR", "JPY", "GBP", "AUD", "NZD", "CAD", "CHF", "SEK", "NOK", "DKK", "MXN", "ZAR", "TRY", "PLN", "HUF", "CZK", "ILS", "SGD",
          "HKD", "THB ?"):
    q = p.replace(" ?", "")
    for t in ("1M", "3M", "12M"):
        FX_FWD.append(("%s %s forward points" % (q, t) + (" ?" if "?" in p else ""), "%s%s Curncy" % (q, t)))
for p, root in (("KRW", "KWN"), ("TWD", "NTN"), ("INR", "IRN"), ("IDR", "IHN"), ("PHP", "PPN"), ("CNY", "CCN"), ("BRL", "BCN"),
                ("CLP", "CHN"), ("COP", "CLN"), ("MYR", "MRN"), ("RUB", "RUB")):
    for t in ("1M", "3M", "12M"):
        FX_FWD.append(("%s %s NDF outright ?" % (p, t), "%s%s Curncy" % (root, t)))
FX_VOL = []
for p in ("EURUSD", "USDJPY", "GBPUSD", "AUDUSD", "USDCAD", "USDCHF", "NZDUSD", "EURJPY", "AUDJPY", "EURGBP", "EURCHF", "USDCNH",
          "USDMXN", "USDBRL", "USDZAR", "USDTRY", "USDKRW", "USDINR"):
    for t in ("1M", "3M", "1Y"):
        FX_VOL.append(("%s %s ATM implied vol" % (p, t), "%sV%s Curncy" % (p, t)))
    for t in ("1M", "3M"):
        FX_VOL.append(("%s %s 25d risk reversal" % (p, t), "%s25R%s Curncy" % (p, t)))
        FX_VOL.append(("%s %s 25d butterfly ?" % (p, t), "%s25B%s Curncy" % (p, t)))
FX_VOL += T("""JPM G7 FX vol|JPMVXYG7;JPM EM FX vol|JPMVXYEM;JPM global FX vol ?|JPMVXYGL;Deutsche Bank FX vol ?|CVIX""", "Index")
FX_BASIS = [("%s %s cross-currency basis ?" % (c, t), "%sBS%s Curncy" % (r, t))
            for c, r in (("EUR", "EU"), ("JPY", "JY"), ("GBP", "BP"), ("CHF", "SF"), ("AUD", "AD"), ("CAD", "CD"))
            for t in ("C", "V1", "V5")]
RATES_FUT_X = []
for lab, root in (("Eurodollar", "ED"), ("SOFR 3m", "SFR"), ("Euribor", "ER"), ("Short sterling", "L "), ("SONIA 3m", "SFI"),
                  ("Canada BAX", "BA"), ("Australia 90d bill", "IR")):
    for k in range(9, 13):
        RATES_FUT_X.append(("%s %d" % (lab, k), "%s%d Comdty" % (root, k)))
RATES_FUT_X += [("Fed funds %d" % k, "FF%d Comdty" % k) for k in (2, 3, 4, 5, 7, 8, 9, 10, 11)]
RATES_FUT_X += T("""US ultra 10y 1st|UXY1;US ultra 10y 2nd|UXY2;Korea 3y 1st ?|KE1;Korea 10y 1st ?|KAA1;Italy short BTP 1st ?|BTS1;
Spain Bono 1st ?|FBON1;Swiss bond 1st ?|FB1;Canada 2y 1st ?|CV1;Canada 5y 1st ?|CF1 ?;JGB mini 1st ?|JBA1 ?""", "Comdty")

# ---------------------------------------------------------------- 4: equity markets, vol, benchmarks (monthly)
EQ_IDX = T("""S&P 500|SPX;Dow Jones|INDU;Nasdaq Composite|CCMP;Nasdaq 100|NDX;Russell 2000|RTY;Russell 1000|RIY;S&P 400 midcap|MID;
S&P 500 equal weight ?|SPW;S&P/TSX|SPTSX;Mexico IPC|MEXBOL;Ibovespa|IBOV;Chile IPSA|IPSA;Argentina Merval|MERVAL;Colombia ?|COLCAP;Peru ?|SPBLPGPT;
FTSE 100|UKX;FTSE 250|MCX;DAX|DAX;CAC 40|CAC;FTSE MIB|FTSEMIB;IBEX 35|IBEX;AEX|AEX;SMI|SMI;OMX Stockholm 30|OMX;Oslo OBX|OBX;
OMX Copenhagen 25 ?|KFX;OMX Helsinki 25 ?|HEX25;BEL 20|BEL20;ATX|ATX;PSI|PSI20;ISEQ|ISEQ;Athens general|ASE;WIG 20|WIG20;
Budapest BUX|BUX;Prague PX|PX;BIST 100|XU100;MOEX Russia ?|IMOEX;South Africa Top 40|TOP40;JSE all share|JALSH;Tel Aviv 35|TA-35;
Saudi Tadawul|SASEIDX;Abu Dhabi ?|ADSMI;Qatar ?|DSM;Egypt EGX30 ?|EGX30;Nikkei 225|NKY;TOPIX|TPX;Hang Seng|HSI;HS China enterprises|HSCEI;
Shanghai composite|SHCOMP;CSI 300|SHSZ300;Shenzhen composite ?|SZCOMP;Taiwan TAIEX|TWSE;KOSPI|KOSPI;KOSDAQ ?|KOSDAQ;Sensex|SENSEX;Nifty 50|NIFTY;
Jakarta composite|JCI;FTSE Bursa Malaysia KLCI|FBMKLCI;Thailand SET|SET;Philippines PSEi|PCOMP;Singapore STI|FSSTI;Vietnam VN ?|VNINDEX;
Pakistan KSE100 ?|KSE100;S&P/ASX 200|AS51;NZX 50 ?|NZSE50FG;Euro Stoxx 50|SX5E;Stoxx Europe 600|SXXP;Euro Stoxx|SXXE;
MSCI World|MXWO;MSCI ACWI|MXWD;MSCI EAFE|MXEA;MSCI Emerging Markets|MXEF;MSCI Europe|MXEU;MSCI Asia ex Japan|MXASJ;MSCI EM Asia ?|MXMS;
MSCI EM Latin America ?|MXLA;MSCI EM EMEA ?|MXEE ?;MSCI Frontier ?|MXFM;MSCI World net TR USD|NDDUWI;MSCI EM net TR USD|NDUEEGF;MSCI ACWI net TR USD|NDUEACWF""", "Index")
SECTORS = T("""S&P 500 energy|S5ENRS;S&P 500 materials|S5MATR;S&P 500 industrials|S5INDU;S&P 500 consumer discretionary|S5COND;
S&P 500 consumer staples|S5CONS;S&P 500 health care|S5HLTH;S&P 500 financials|S5FINL;S&P 500 info tech|S5INFT;S&P 500 communication|S5TELS;
S&P 500 utilities|S5UTIL;S&P 500 real estate|S5RLST;S&P 500 banks ?|S5BANKX;S&P semiconductors ?|S5SECO ?;Philadelphia semiconductor|SOX;
KBW bank|BKX;Stoxx Europe banks|SX7P;Euro Stoxx banks|SX7E;Stoxx Europe oil & gas|SXEP;Stoxx Europe basic resources|SXPP;
Stoxx Europe technology|SX8P;Stoxx Europe health care|SXDP;Stoxx Europe utilities|SX6P;Stoxx Europe autos|SXAP;Stoxx Europe insurance|SXIP;
Stoxx Europe industrial goods|SXNP;Stoxx Europe food & beverage|SX3P;Stoxx Europe telecoms|SXKP;Stoxx Europe real estate ?|SX86P;
Stoxx Europe chemicals|SX4P;Stoxx Europe retail|SXRP;TOPIX banks ?|TPNBNK;Russell 1000 value|RLV;Russell 1000 growth|RLG;
Russell 2000 value|RUJ;Russell 2000 growth|RUO;S&P 500 value|SVX;S&P 500 growth|SGX;MSCI World value ?|MXWO000V;MSCI World growth ?|MXWO000G;
MSCI World momentum ?|M1WOMOM ?;MSCI World quality ?|M1WOQU ?;MSCI World min vol ?|M1WOMVOL ?;MSCI USA momentum ?|M1USMMT ?;
MSCI World small cap ?|MXWOSC;Goldman cyclicals vs defensives ?|GSPUCYDE;Goldman most shorted ?|GSCBMSAL;Goldman non-profitable tech ?|GSXUNPTC;
Bloomberg Magnificent 7 ?|BM7T;S&P 500 top 10 ?|SPXT10UP ?;NYSE FANG+ ?|NYFANG;Alerian MLP ?|AMZ;FTSE NAREIT all equity ?|FNER""", "Index")
VOLX = T("""VIX 9-day|VIX9D;VIX 3-month|VIX3M;VIX 6-month|VIX6M;VVIX|VVIX;CBOE SKEW|SKEW;Nasdaq vol VXN|VXN;Russell 2000 vol RVX|RVX;
EM equity vol VXEEM|VXEEM;Crude oil vol OVX|OVX;Gold vol GVZ|GVZ;Treasury 10y vol TYVIX ?|TYVIX;Hang Seng vol|VHSI;KOSPI 200 vol ?|VKOSPI;
Implied correlation 1m|COR1M;Implied correlation 3m|COR3M;Implied correlation (legacy) ?|KCJ;Dispersion index ?|DSPX;
Euro Stoxx 50 vol (VSTOXX)|V2X;DAX vol ?|V1X;FTSE 100 vol ?|IVUKX30;Nikkei vol|VNKY;S&P 500 30d realised ?|SPXRV30 ?;
MOVE|MOVE;Merrill swaption vol ?|SMOVE1M ?;VIX futures 1st|UX1;VIX futures 2nd|UX2;VIX futures 3rd|UX3;VIX futures 4th|UX4;
VIX futures 5th|UX5;VIX futures 6th|UX6;VIX futures 7th|UX7;VIX futures 8th|UX8;VSTOXX futures 1st ?|FVS1;VSTOXX futures 2nd ?|FVS2;
VSTOXX futures 3rd ?|FVS3;Cboe S&P 500 put-write ?|PUT;Cboe S&P 500 buy-write ?|BXM;Cboe tail hedge ?|VXTH ?;Cboe 25d put skew ?|SKEW25D ?""", "Index")
BENCH_X = T("""SG Short-Term Traders Index ?|NEIXSTTI;SG Trend Indicator ?|NEIXTI ?;SG Macro Trading Index ?|NEIXMTI ?;SG Multi-Alt ?|NEIXMULT ?;
Barclay BTOP50 ?|BARCBTOP ?;Barclay Systematic Traders ?|BARCSYST ?;Credit Suisse managed futures ?|HEDGMF;Credit Suisse global macro ?|HEDGGLMA;
HFRX global|HFRXGL;HFRX macro/CTA|HFRXM;HFRX equity hedge|HFRXEH;HFRX relative value ?|HFRXRVA;HFRI fund weighted|HFRIFWI;
HFRI equity hedge|HFRIEHI;HFRI relative value ?|HFRIRVA;Eurekahedge CTA ?|EHFI251 ?;Eurekahedge macro ?|EHFI253 ?;
S&P risk parity 10% vol ?|SPRPAU10 ?;SG CTA Mutual Fund Index ?|NEIXMFI ?;BarclayHedge CTA ?|BARCCTA""", "Index")
ETFS = T("""SPY|SPY US;IVV|IVV US;QQQ|QQQ US;IWM|IWM US;EFA|EFA US;EEM|EEM US;VWO|VWO US;TLT|TLT US;IEF|IEF US;SHY|SHY US;AGG|AGG US;
LQD|LQD US;HYG|HYG US;JNK|JNK US;EMB|EMB US;TIP|TIP US;GLD|GLD US;IAU|IAU US;SLV|SLV US;GDX|GDX US;USO|USO US;DBC|DBC US;PDBC|PDBC US;
GSG|GSG US;UUP|UUP US;FXE|FXE US;FXY|FXY US;VNQ|VNQ US;XLE|XLE US;XLF|XLF US;XLK|XLK US;XLU|XLU US;XLP|XLP US;XLV|XLV US;SMH|SMH US;
ARKK|ARKK US;DBMF (managed futures)|DBMF US;KMLM (managed futures)|KMLM US;CTA (Simplify managed futures)|CTA US;
RSST (return stacked stocks+trend)|RSST US;RSSB (return stacked stocks+bonds)|RSSB US;NTSX (90/60)|NTSX US;TAIL (tail hedge)|TAIL US;
SVOL|SVOL US;JEPI|JEPI US;BITO (bitcoin futures) ?|BITO US;IBIT (spot bitcoin)|IBIT US;FBTC|FBTC US;GBTC|GBTC US;
TQQQ (3x Nasdaq)|TQQQ US;SQQQ|SQQQ US;SPXL|SPXL US;SOXL|SOXL US;UVXY|UVXY US;SVXY|SVXY US;VXX ?|VXX US;MTUM|MTUM US;QUAL|QUAL US;
USMV|USMV US;VLUE|VLUE US;BIL|BIL US;SGOV|SGOV US;EWJ|EWJ US;FXI|FXI US;MCHI|MCHI US;INDA|INDA US;EWZ|EWZ US;EWY|EWY US;EWT|EWT US""", "Equity")

# ---------------------------------------------------------------- 5: commodities extended (monthly)
COM_ROOTS = [("WTI", "CL"), ("Brent", "CO"), ("Natural gas", "NG"), ("Heating oil", "HO"), ("RBOB", "XB"), ("Gasoil", "QS"),
             ("Gold", "GC"), ("Silver", "SI"), ("Copper", "HG"), ("Platinum", "PL"), ("Palladium", "PA"), ("Aluminium LME", "LA"),
             ("Zinc LME", "LX"), ("Nickel LME", "LN"), ("Lead LME", "LL"), ("Tin LME", "LT"), ("Corn", "C "), ("Wheat", "W "),
             ("KC wheat", "KW"), ("Soybeans", "S "), ("Soy meal", "SM"), ("Soy oil", "BO"), ("Sugar", "SB"), ("Coffee", "KC"),
             ("Cocoa", "CC"), ("Cotton", "CT"), ("Orange juice", "JO"), ("Live cattle", "LC"), ("Feeder cattle", "FC"),
             ("Lean hogs", "LH"), ("Oats", "O "), ("Rough rice", "RR"), ("Lumber ?", "LB"), ("EU carbon", "MO"), ("TTF gas", "TZT"),
             ("London cocoa ?", "QC"), ("London coffee robusta ?", "DF"), ("London sugar white ?", "QW"), ("Canola ?", "RS"),
             ("Milling wheat Paris ?", "CA"), ("Rapeseed Paris ?", "IJ"), ("Iron ore SGX ?", "SCO"), ("Newcastle coal ?", "XW"),
             ("Uranium ?", "UXA"), ("UK natural gas NBP ?", "FN"), ("Japan rubber ?", "JN"), ("Palm oil ?", "KO"), ("Class III milk ?", "DA")]
COM_FRONT = [("%s 1st" % n, "%s1 Comdty" % r) for n, r in COM_ROOTS]
COM_CURVE = [("%s %d" % (n, k), "%s%d Comdty" % (r, k)) for n, r in COM_ROOTS for k in range(2, 13)]
COM_IDX = T("""BCOM total return|BCOMTR;BCOM excess return|BCOM;BCOM spot|BCOMSP;BCOM energy TR|BCOMENTR;BCOM industrial metals TR|BCOMINTR;
BCOM precious metals TR|BCOMPRTR;BCOM agriculture TR|BCOMAGTR;BCOM livestock TR|BCOMLITR;BCOM grains TR ?|BCOMGRTR;BCOM softs TR ?|BCOMSOTR;
BCOM roll select TR ?|BCOMRST;BCOM 3-month forward TR ?|BCOMF3T;S&P GSCI total return|SPGSCITR;S&P GSCI excess return|SPGSCIP;
S&P GSCI spot|SPGSCI;S&P GSCI energy TR|SPGSENTR;S&P GSCI industrial metals TR|SPGSINTR;S&P GSCI precious TR|SPGSPMTR;
S&P GSCI agriculture TR|SPGSAGTR;S&P GSCI livestock TR|SPGSLVTR;Refinitiv/CRB index|CRY;Goldman commodity carry ?|GSCBCAR ?;
Bloomberg commodity curve ?|BCOMCRV ?""", "Index")
COM_FUND = T("""US crude inventories (EIA)|DOESCRUD;Cushing crude stocks|DOESCUSH;US gasoline stocks ?|DOESMGTT ?;US distillate stocks ?|DOESDIST ?;
US crude production ?|DOETCRUD;US refinery utilisation ?|DOEPRUTL ?;US natural gas storage ?|NGSWTOTL ?;Baker Hughes US rigs|BAKETOT;
Baker Hughes US oil rigs ?|BAKEOIL;Baltic Dry|BDIY;Baltic capesize ?|BCI14 ?;Drewry container index ?|DRWCTOTL ?;
LME copper stocks ?|NLSCA ?;LME aluminium stocks ?|NLSAA ?;COMEX gold stocks|COMXGOLD;COMEX copper stocks|COMXCOPR;COMEX silver stocks|COMXSILV;
SHFE copper stocks ?|SHFCCOPD;Gold ETF holdings total ?|ETFGTOTL ?;LBMA gold PM fix ?|GOLDLNPM;Copper LME cash|LMCADY;
Aluminium LME cash|LMAHDY;China iron ore port stocks ?|IOPIINVT ?;US ethanol stocks ?|DOEETHST ?;OPEC crude production ?|OPCRTOTL""", "Index")
COM_FUND += T("""LME copper cash|LMCADY;LME aluminium cash|LMAHDY;LME copper 3m|LMCADS03;LME aluminium 3m|LMAHDS03;LME zinc 3m|LMZSDS03;
LME nickel 3m|LMNIDS03;Iron ore 62% Fe ?|IOE62CNF ?""", "Comdty")

# ---------------------------------------------------------------- 6: daily (1990+): tradable core
DAILY_FUT = [(n + " 1st", r + "1 Comdty") for n, r in COM_ROOTS[:35]] + [(n + " 2nd", r + "2 Comdty") for n, r in COM_ROOTS[:35]]
DAILY_FUT += [(n + " %s" % k, r + k + " Comdty") for n, r in (("US 2y", "TU"), ("US 5y", "FV"), ("US 10y", "TY"), ("US bond", "US"),
              ("US ultra", "WN"), ("Ultra 10y", "UXY"), ("Schatz", "DU"), ("Bobl", "OE"), ("Bund", "RX"), ("Buxl", "UB"),
              ("Long gilt", "G "), ("JGB", "JB"), ("Canada 10y", "CN"), ("Aus 3y", "YM"), ("Aus 10y", "XM"), ("BTP", "IK"),
              ("OAT", "OAT")) for k in ("1", "2")]
DAILY_FUT += [("%s %d" % (lab, k), "%s%d Comdty" % (root, k)) for lab, root in (("Eurodollar", "ED"), ("SOFR 3m", "SFR"),
              ("Euribor", "ER"), ("Short sterling", "L "), ("SONIA 3m", "SFI"), ("BAX", "BA"), ("Aus bill", "IR"), ("Euroyen ?", "YE"),
              ("Euroswiss ?", "ES")) for k in (1, 2, 3, 4, 8)] + [("Fed funds %d" % k, "FF%d Comdty" % k) for k in (1, 3, 6, 12)]
DAILY_FUT += T("""S&P 500 e-mini|ES1;Nasdaq 100 e-mini|NQ1;Russell 2000 ?|RTY1;Dow mini|DM1;Euro Stoxx 50|VG1;DAX|GX1;FTSE 100|Z 1;CAC 40|CF1;
FTSE MIB|ST1;IBEX|IB1;AEX|EO1;SMI|SM1;Nikkei 225 ?|NK1;Nikkei USD CME ?|NX1;TOPIX|TP1;Hang Seng|HI1;HSCEI|HC1;KOSPI 200|KM1;Taiwan ?|FT1;
SPI 200|XP1;S&P/TSX 60|PT1;Ibovespa ?|BZ1;Mexico IPC ?|IS1;FTSE/JSE Top 40 ?|AI1;OMXS30 ?|QC1;FTSE China A50|XU1;Nifty SGX/GIFT ?|IH1;
MSCI EM mini|MES1;MSCI EAFE mini ?|MFS1;MSCI Singapore|QZ1;MSCI Taiwan SGX ?|TW1;VIX futures 1st|UX1;VIX futures 2nd|UX2;
VSTOXX futures 1st ?|FVS1;Bitcoin CME ?|BTC1 Curncy""", "Index")
DAILY_FUT = [(a, b.replace(" Curncy Index", " Curncy")) for a, b in DAILY_FUT]
DAILY_FX = [x for x in FX_SPOT if "pre-1999" not in x[0] and "ECU" not in x[0]]
DAILY_RATES = T("""US 3m bill|USGG3M;US 2y|USGG2YR;US 5y|USGG5YR;US 10y|USGG10YR;US 30y|USGG30YR;US 10y real|USGGT10Y;US 10y breakeven|USGGBE10;
Germany 2y|GDBR2;Germany 10y|GDBR10;Germany 30y|GDBR30;UK 2y|GUKG2;UK 10y|GUKG10;UK 30y|GUKG30;Japan 2y|GJGB2;Japan 10y|GJGB10;Japan 30y|GJGB30;
France 10y|GFRN10;Italy 2y|GBTPGR2;Italy 10y|GBTPGR10;Spain 10y|GSPG10YR;Canada 2y|GCAN2YR;Canada 10y|GCAN10YR;Australia 3y|GACGB3;
Australia 10y|GACGB10;Switzerland 10y|GSWISS10;Sweden 10y ?|GSGB10YR;Norway 10y|GNOR10YR;NZ 10y|GNZGB10;China 10y|GCNY10YR;Korea 10y|GVSK10YR;
India 10y|GIND10YR;Fed funds effective|FEDL01;SOFR|SOFRRATE;ESTR ?|ESTRON;Euribor 3m|EUR003M;SONIA|SONIO/N;US IG OAS|LUACOAS;US HY OAS|LF98OAS;
NY Fed ACM term premium|ACMTP10;US 5y5y inflation fwd|FWISUS55;MOVE|MOVE""", "Index")
DAILY_RATES += T("""USD SOFR swap 2y|USOSFR2;USD SOFR swap 10y|USOSFR10;EUR swap 2y|EUSA2;EUR swap 10y|EUSA10;GBP swap 10y|BPSW10;JPY swap 10y|JYSW10;
USD inflation swap 10y|USSWIT10;EUR inflation swap 10y|EUSWI10""", "Curncy")
DAILY_EQ = T("""S&P 500|SPX;Nasdaq 100|NDX;Russell 2000|RTY;Euro Stoxx 50|SX5E;Stoxx 600|SXXP;DAX|DAX;FTSE 100|UKX;CAC 40|CAC;FTSE MIB|FTSEMIB;
IBEX|IBEX;AEX|AEX;SMI|SMI;OMX 30|OMX;Nikkei|NKY;TOPIX|TPX;Hang Seng|HSI;HSCEI|HSCEI;CSI 300|SHSZ300;KOSPI|KOSPI;TAIEX|TWSE;Sensex|SENSEX;
Nifty|NIFTY;ASX 200|AS51;S&P/TSX|SPTSX;Ibovespa|IBOV;Mexico IPC|MEXBOL;South Africa Top 40|TOP40;Singapore STI|FSSTI;MSCI World|MXWO;
MSCI EM|MXEF;MSCI ACWI|MXWD""", "Index")
DAILY_VOL = T("""VIX|VIX;VIX 3m|VIX3M;VIX 9d|VIX9D;VVIX|VVIX;SKEW|SKEW;VSTOXX|V2X;Nikkei vol|VNKY;Hang Seng vol|VHSI;Implied correlation 3m|COR3M;
Crude vol OVX|OVX;Gold vol GVZ|GVZ;Bloomberg US financial conditions|BFCIUS""", "Index") + \
    [x for x in FX_VOL if x[1].endswith("V1M Curncy") or x[1].endswith("25R1M Curncy")][:24]
DAILY_CIDX = T("""BCOM TR|BCOMTR;GSCI TR|SPGSCITR;GSCI ER|SPGSCIP;BCOM energy TR|BCOMENTR;BCOM industrial metals TR|BCOMINTR;BCOM precious TR|BCOMPRTR;
BCOM agriculture TR|BCOMAGTR;BCOM livestock TR|BCOMLITR;SG CTA|NEIXCTA;SG Trend|NEIXCTAT;SG Short-Term Traders ?|NEIXSTTI""", "Index")

FILES = [
    ("2_Bloomberg_econ_policy_monthly.xlsx", "Economics (first release + consensus), central banks, money, financial conditions, sentiment", [
        ("EconUS", ECO_US, ECOF, "M"), ("EconIntl", ECO_INTL, ECOF, "M"), ("PolicyMoney", POLICY, "PX_LAST", "M"),
        ("Conditions", CONDITIONS, "PX_LAST", "M")]),
    ("3_Bloomberg_rates_credit_fx_monthly.xlsx", "More yields (DM + EM), swaps, OIS, inflation swaps, credit, FX spot/forwards/vol/basis, STIR strips 9-12", [
        ("YieldsExtra", YLD_EXTRA, "PX_LAST", "M"), ("Swaps", SWAPS, "PX_LAST", "M"), ("Credit", CREDIT, "PX_LAST", "M"),
        ("FXSpot", FX_SPOT, "PX_LAST", "M"), ("FXForwards", FX_FWD, "PX_LAST", "M"), ("FXVol", FX_VOL, "PX_LAST", "M"),
        ("FXBasis", FX_BASIS, "PX_LAST", "M"), ("RatesFutExtra", RATES_FUT_X, "PX_LAST", "M")]),
    ("4_Bloomberg_equity_vol_funds_monthly.xlsx", "Equity indexes (TR + valuation + forward EPS + market cap), sectors/styles, vol complex, CTA/HF benchmarks, ETFs (TR + AUM)", [
        ("EquityIndexes", EQ_IDX, EQF, "M"), ("SectorsStyles", SECTORS, "TOT_RETURN_INDEX_GROSS_DVDS,PX_LAST,BEST_PE_RATIO,BEST_EPS", "M"),
        ("VolComplex", VOLX, "PX_LAST", "M"), ("Benchmarks2", BENCH_X, "PX_LAST", "M"), ("ETFs", ETFS, ETFF, "M")]),
    ("5_Bloomberg_commodities_ext_monthly.xlsx", "Commodity front contracts with open interest/volume, full curves 2-12, indexes and subindexes, fundamentals", [
        ("ComFront", COM_FRONT, FUTF, "M"), ("ComCurve", COM_CURVE, "PX_LAST", "M"), ("ComIndexes", COM_IDX, "PX_LAST", "M"),
        ("ComFundamentals", COM_FUND, "PX_LAST", "M")]),
    ("6_Bloomberg_daily_A_futures_fx.xlsx", "DAILY from 1990: futures 1st/2nd (commodities, bonds, STIR, equity, VIX), FX spot", [
        ("DailyFutures", DAILY_FUT, "PX_LAST", "D"), ("DailyFX", DAILY_FX, "PX_LAST", "D")]),
    ("7_Bloomberg_daily_B_rates_equity_vol.xlsx", "DAILY from 1990: yields/swaps/credit, equity index TR, vol, commodity and CTA indexes", [
        ("DailyRates", DAILY_RATES, "PX_LAST", "D"), ("DailyEquity", DAILY_EQ, "TOT_RETURN_INDEX_GROSS_DVDS,PX_LAST", "D"),
        ("DailyVol", DAILY_VOL, "PX_LAST", "D"), ("DailyIndexes", DAILY_CIDX, "PX_LAST", "D")]),
]


def block_sheet(wb, name, cols, fields, per):
    s = wb.create_sheet(name)
    note = ("DAILY (weekdays, blank on holidays) from 1990. If '#N/A Limit': Ctrl+H, replace Per=D with Per=W (weekly)."
            if per == "D" else "Monthly from 1969 (series start when they start). Yellow = ticker.")
    s.cell(1, 1, note).font = Font(name=F, italic=True)
    n = len(fields.split(","))
    step = n + 2
    for j, (label, tk) in enumerate(cols):
        c = 1 + step * j
        s.cell(2, c, label).font = Font(name=F, bold=True)
        t = s.cell(3, c, tk)
        t.font = Font(name=F)
        t.fill = YEL
        s.cell(4, c, "date").font = Font(name=F, italic=True)
        for i, f in enumerate(fields.split(",")):
            s.cell(4, c + 1 + i, f).font = Font(name=F, italic=True)
        s.cell(5, c, '=BDH(%s3,"%s","%s","",%s)' % (L(c), fields, M0 if per == "M" else D0, MON if per == "M" else DAY)).font = Font(name=F)
        s.column_dimensions[L(c)].width = 11
        for i in range(n):
            s.column_dimensions[L(c + 1 + i)].width = 13
        s.column_dimensions[L(c + n + 1)].width = 2
    s.freeze_panes = "A5"


def main(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    master, summary = [], []
    for fname, what, sheets in FILES:
        wb = Workbook()
        rd = wb.active
        rd.title = "Read me"
        chk = wb.create_sheet("Check")
        for k, h in enumerate(("sheet", "label", "ticker", "best guess?", "Bloomberg NAME (blank or #N/A = fix ticker)")):
            chk.cell(1, k + 1, h).font = Font(name=F, bold=True)
        r, pts, ntk = 2, 0, 0
        for sname, cols, fields, per in sheets:
            block_sheet(wb, sname, cols, fields, per)
            nf = len(fields.split(","))
            pts += len(cols) * nf * (NM if per == "M" else ND)
            ntk += len(cols)
            for lab, tk in cols:
                guess = "?" if lab.rstrip().endswith("?") or " ? " in tk + " " else ""
                chk.cell(r, 1, sname)
                chk.cell(r, 2, lab)
                chk.cell(r, 3, tk).fill = YEL
                chk.cell(r, 4, guess)
                chk.cell(r, 5, '=BDP(C%d,"NAME")' % r)
                master.append((fname, sname, lab, tk, fields, per, guess))
                r += 1
        for col, w in zip("ABCDE", (16, 42, 34, 10, 44)):
            chk.column_dimensions[col].width = w
        chk.freeze_panes = "A2"
        txt = [fname.replace(".xlsx", "") + ": " + what, "",
               "%d tickers, at most ~%.2fM data points (real number lower: many series start after 1969/1990)." % (ntk, pts / 1e6), "",
               "1. Open on the Bloomberg terminal (Bloomberg tab visible in Excel). Formulas start by themselves.",
               "2. Look at the Check sheet first: a blank or #N/A NAME = wrong ticker. Fix it in the yellow cell of the data sheet",
               "   (search the series with SECF or the Bloomberg search bar; futures: CT <GO>). Labels with '?' are best guesses.",
               "   Skip anything that takes more than a minute: missing series are fine, the build handles gaps.",
               "3. Wait until no cell says 'Requesting Data...', then File > Save As: keep this name and add _VALUES",
               "   after Bloomberg > Convert to values if offered (that copy opens at home without a terminal).",
               "4. '#N/A Limit' = the terminal's download allowance is used up: save, stop, continue another day.",
               "Data stays private: never on GitHub, never shared. Copy to Documents\\WRDS results\\mscifreedata."]
        for i, t in enumerate(txt, 1):
            rd.cell(i, 1, t).font = Font(name=F, bold=(i == 1), size=12 if i == 1 else 10)
        rd.column_dimensions["A"].width = 125
        for k, (sname, cols, fields, per) in enumerate(sheets):
            rd.cell(len(txt) + 2 + k, 1, "Sheet %s: %d tickers x %s (%s)" % (sname, len(cols), fields, "daily" if per == "D" else "monthly"))
        wb.save(os.path.join(out_dir, fname))
        summary.append((fname, ntk, pts))
        print("%-46s %5d tickers  <= %.2fM points" % (fname, ntk, pts / 1e6))
    with open(os.path.join(out_dir, "bloomberg_v5_tickers.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(("file", "sheet", "label", "ticker", "fields", "per", "best_guess"))
        w.writerows(master)
    print("total tickers", len(master), "unique", len({m[3] for m in master}), "best-guess", sum(1 for m in master if m[6]))
    return summary


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "bloomberg_v5")
