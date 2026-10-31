"""Builds Bloomberg_macro_UBC.xlsx (v3): Bloomberg-terminal workbook (BDH formulas) for the Global Macro Book.
Sheets: Read me, Returns (commodity excess-return indexes), Curves (generic futures 1st/2nd/~12m), Economics (first
release, consensus median, release date, latest value for key macro series), Surprise (Citi economic surprise indexes).
Tickers marked '?' in the label are best guesses; '#N/A Invalid Security' means: look the series up and fix the cell.
"""
import sys

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter as L

C = [
 ("WTI crude", "SPGSCLP Index", "BCOMCL Index", "CL1 Comdty", "CL2 Comdty", "CL13 Comdty"),
 ("Brent crude", "SPGSBRP Index", "BCOMCO Index", "CO1 Comdty", "CO2 Comdty", "CO13 Comdty"),
 ("Natural gas", "SPGSNGP Index", "BCOMNG Index", "NG1 Comdty", "NG2 Comdty", "NG13 Comdty"),
 ("Heating oil", "SPGSHOP Index", "BCOMHO Index", "HO1 Comdty", "HO2 Comdty", "HO13 Comdty"),
 ("Gasoline (RBOB)", "SPGSRBP Index", "BCOMRB Index", "XB1 Comdty", "XB2 Comdty", "XB13 Comdty"),
 ("Gold", "SPGSGCP Index", "BCOMGC Index", "GC1 Comdty", "GC2 Comdty", "GC7 Comdty"),
 ("Silver", "SPGSSIP Index", "BCOMSI Index", "SI1 Comdty", "SI2 Comdty", "SI6 Comdty"),
 ("Copper", "SPGSICP Index", "BCOMHG Index", "HG1 Comdty", "HG2 Comdty", "HG13 Comdty"),
 ("Platinum", "SPGSPLP Index", "", "PL1 Comdty", "PL2 Comdty", "PL5 Comdty"),
 ("Corn", "SPGSCNP Index", "BCOMCN Index", "C 1 Comdty", "C 2 Comdty", "C 6 Comdty"),
 ("Wheat", "SPGSWHP Index", "BCOMWH Index", "W 1 Comdty", "W 2 Comdty", "W 6 Comdty"),
 ("Soybeans", "SPGSSOP Index", "BCOMSY Index", "S 1 Comdty", "S 2 Comdty", "S 8 Comdty"),
 ("Sugar", "SPGSSBP Index", "BCOMSB Index", "SB1 Comdty", "SB2 Comdty", "SB5 Comdty"),
 ("Coffee", "SPGSKCP Index", "BCOMKC Index", "KC1 Comdty", "KC2 Comdty", "KC6 Comdty"),
 ("Cotton", "SPGSCTP Index", "BCOMCT Index", "CT1 Comdty", "CT2 Comdty", "CT6 Comdty"),
 ("Live cattle", "SPGSLCP Index", "BCOMLC Index", "LC1 Comdty", "LC2 Comdty", "LC7 Comdty"),
]
ECO = [  # (label, ticker)
 ("US CPI y/y", "CPI YOY Index"), ("US industrial production m/m", "IP CHNG Index"),
 ("US unemployment rate", "USURTOT Index"), ("US nonfarm payrolls change", "NFP TCH Index"),
 ("US ISM manufacturing", "NAPMPMI Index"), ("US GDP q/q saar", "GDP CQOQ Index"),
 ("US retail sales m/m", "RSTAMOM Index"),
 ("Euro area HICP y/y", "ECCPEMUY Index"), ("Euro area unemployment", "UMRTEMU Index"),
 ("Euro area manufacturing PMI", "MPMIEZMA Index"), ("Euro area GDP q/q", "EUGNEMUQ Index"),
 ("Germany CPI y/y", "GRCP20YY Index"), ("Germany industrial production y/y", "GRIPIYOY Index"),
 ("Germany unemployment rate", "GRUEPR Index"), ("Germany Ifo business climate", "GRIFPBUS Index"),
 ("France CPI y/y", "FRCPIYOY Index"),
 ("UK CPI y/y", "UKRPCJYR Index"), ("UK industrial production y/y", "UKIPIYOY Index"),
 ("UK unemployment (ILO)", "UKUEILOR Index"), ("UK manufacturing PMI", "MPMIGBMA Index"),
 ("Japan CPI y/y", "JNCPIYOY Index"), ("Japan industrial production y/y", "JNIPYOY Index"),
 ("Japan unemployment rate", "JNUE Index"), ("Japan Tankan large manufacturers", "JNTSMFG Index"),
 ("Canada CPI y/y", "CACPIYOY Index"), ("Canada unemployment rate", "CANLXEMR Index"),
 ("Australia CPI y/y (quarterly)", "AUCPIYOY Index"), ("Australia unemployment rate", "AULFUNEM Index"),
 ("China CPI y/y", "CNCPIYOY Index"), ("China industrial production y/y", "CHVAIOY Index"),
 ("China official manufacturing PMI", "CPMINDX Index"),
 ("Korea CPI y/y", "KOCPIYOY Index"), ("Mexico CPI y/y", "MXCPYOY Index"), ("Brazil IPCA y/y", "BZPIIPCY Index"),
 ("South Africa CPI y/y", "SACPIYOY Index"),
]
SURPRISE = [("Citi surprise US", "CESIUSD Index"), ("Citi surprise euro area", "CESIEUR Index"),
            ("Citi surprise UK", "CESIGBP Index"), ("Citi surprise Japan", "CESIJPY Index"),
            ("Citi surprise Canada", "CESICAD Index"), ("Citi surprise Australia", "CESIAUD Index"),
            ("Citi surprise China", "CESICNY Index"), ("Citi surprise G10", "CESIG10 Index"),
            ("Citi surprise EM", "CESIEM Index")]
# v3 (2026-10-31, after the transcript gap review: Winton/Harding, Carver, Baltas, Quantica, Babbage)
ALT = [  # alternative commodities: (name, GSCI ER, BCOM ER, 1st, 2nd, ~12m)
 ("Cocoa", "SPGSCCP Index", "", "CC1 Comdty", "CC2 Comdty", "CC6 Comdty"),
 ("Orange juice", "", "", "JO1 Comdty", "JO2 Comdty", "JO6 Comdty"),
 ("Lean hogs", "SPGSLHP Index", "BCOMLH Index", "LH1 Comdty", "LH2 Comdty", "LH7 Comdty"),
 ("Feeder cattle", "SPGSFCP Index", "", "FC1 Comdty", "FC2 Comdty", "FC6 Comdty"),
 ("KC wheat", "SPGSKWP Index", "BCOMKW Index", "KW1 Comdty", "KW2 Comdty", "KW6 Comdty"),
 ("Oats", "", "", "O 1 Comdty", "O 2 Comdty", "O 5 Comdty"),
 ("Rough rice", "", "", "RR1 Comdty", "RR2 Comdty", "RR6 Comdty"),
 ("Soybean meal", "", "BCOMSM Index", "SM1 Comdty", "SM2 Comdty", "SM8 Comdty"),
 ("Soybean oil", "", "BCOMBO Index", "BO1 Comdty", "BO2 Comdty", "BO8 Comdty"),
 ("Lumber ?", "", "", "LB1 Comdty", "LB2 Comdty", "LB6 Comdty"),
 ("Palladium", "", "", "PA1 Comdty", "PA2 Comdty", "PA5 Comdty"),
 ("Aluminium (LME)", "SPGSIAP Index", "BCOMAL Index", "LA1 Comdty", "LA2 Comdty", "LA13 Comdty"),
 ("Zinc (LME)", "SPGSIZP Index", "BCOMZS Index", "LX1 Comdty", "LX2 Comdty", "LX13 Comdty"),
 ("Nickel (LME)", "SPGSIKP Index", "BCOMNI Index", "LN1 Comdty", "LN2 Comdty", "LN13 Comdty"),
 ("Lead (LME)", "SPGSILP Index", "", "LL1 Comdty", "LL2 Comdty", "LL13 Comdty"),
 ("Tin (LME)", "", "", "LT1 Comdty", "LT2 Comdty", "LT13 Comdty"),
 ("Gasoil (ICE)", "SPGSGOP Index", "", "QS1 Comdty", "QS2 Comdty", "QS13 Comdty"),
 ("EU carbon (EUA)", "", "", "MO1 Comdty", "MO2 Comdty", "MO3 Comdty"),
 ("TTF gas", "", "", "TZT1 Comdty", "TZT2 Comdty", "TZT13 Comdty"),
]
RATES_FUT = [  # short-rate futures: market-implied policy path and a real front-end market (replaces 2y-note proxy)
 ("Eurodollar 1st", "ED1 Comdty"), ("Eurodollar 4th", "ED4 Comdty"), ("Eurodollar 8th", "ED8 Comdty"),
 ("SOFR 3m 1st", "SFR1 Comdty"), ("SOFR 3m 4th", "SFR4 Comdty"), ("SOFR 3m 8th", "SFR8 Comdty"),
 ("Fed funds 1st", "FF1 Comdty"), ("Fed funds 6th", "FF6 Comdty"),
 ("Euribor 1st", "ER1 Comdty"), ("Euribor 4th", "ER4 Comdty"), ("Euribor 8th", "ER8 Comdty"),
 ("Short sterling 1st", "L 1 Comdty"), ("Short sterling 4th", "L 4 Comdty"), ("Short sterling 8th", "L 8 Comdty"),
 ("SONIA 3m 1st", "SFI1 Comdty"), ("SONIA 3m 4th", "SFI4 Comdty"), ("SONIA 3m 8th", "SFI8 Comdty"),
 ("Canada BAX 1st", "BA1 Comdty"), ("Canada BAX 4th", "BA4 Comdty"),
 ("Australia 90d bill 1st", "IR1 Comdty"), ("Australia 90d bill 4th", "IR4 Comdty"),
 ("Euroyen 1st ?", "YE1 Comdty"), ("Euroyen 4th ?", "YE4 Comdty"),
]
EQ_VAL = [  # MSCI country indexes: valuation + forward EPS (EM value gap; live substitute for WRDS revisions)
 ("MSCI USA", "MXUS Index"), ("MSCI Japan", "MXJP Index"), ("MSCI UK", "MXGB Index"), ("MSCI Germany", "MXDE Index"),
 ("MSCI France", "MXFR Index"), ("MSCI Canada", "MXCA Index"), ("MSCI Australia", "MXAU Index"),
 ("MSCI Hong Kong", "MXHK Index"), ("MSCI Switzerland", "MXCH Index"), ("MSCI Sweden", "MXSE Index"),
 ("MSCI Italy", "MXIT Index"), ("MSCI Spain", "MXES Index"), ("MSCI Netherlands", "MXNL Index"),
 ("MSCI China", "MXCN Index"), ("MSCI Korea", "MXKR Index"), ("MSCI Taiwan", "MXTW Index"), ("MSCI India", "MXIN Index"),
 ("MSCI Brazil", "MXBR Index"), ("MSCI Mexico", "MXMX Index"), ("MSCI South Africa", "MXZA Index"),
 ("MSCI EMU", "MXEM Index"), ("MSCI Emerging Markets", "MXEF Index"), ("MSCI World", "MXWO Index"),
]
BREAKEVENS = [("US 10y breakeven", "USGGBE10 Index"), ("Germany 10y breakeven", "DEGGBE10 Index"),
              ("UK 10y breakeven", "UKGGBE10 Index"), ("France 10y breakeven", "FRGGBE10 Index"),
              ("Italy 10y breakeven", "ITGGBE10 Index"), ("Japan 10y breakeven ?", "JYGGBE10 Index"),
              ("Canada 10y breakeven ?", "CAGGBE10 Index"), ("Australia 10y breakeven ?", "ADGGBE10 Index"),
              ("US 10y real yield (TIPS)", "USGGT10Y Index")]
BENCH = [("SG CTA Index", "NEIXCTA Index"), ("SG Trend Index", "NEIXCTAT Index"),
         ("HFRI Macro", "HFRIMI Index"), ("HFRI Systematic Diversified", "HFRIMTI Index"),
         ("Barclay CTA Index ?", "BARCCTA Index"), ("Barclay BTOP50 ?", "BTOP50 Index")]
FX_BASIS = [("EUR-USD 1y cross-currency basis ?", "EUBSV1 Curncy"), ("JPY-USD 1y cross-currency basis ?", "JYBSV1 Curncy"),
            ("GBP-USD 1y cross-currency basis ?", "BPBSV1 Curncy")]

F = "Arial"
YEL = PatternFill("solid", start_color="FFFF00")


def block_sheet(wb, name, cols, fields, note, per="M", start="12/31/1969"):
    s = wb.create_sheet(name)
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
        s.cell(5, c, '=BDH(%s3,"%s","%s","","Per=%s","Days=A","Fill=P","Dir=V","Dts=S")' % (L(c), fields, start, per)).font = Font(name=F)
        s.column_dimensions[L(c)].width = 12
        for i in range(n):
            s.column_dimensions[L(c + 1 + i)].width = 14
        s.column_dimensions[L(c + n + 1)].width = 3
    s.freeze_panes = "A5"


def main(out):
    wb = Workbook()
    ws = wb.active
    ws.title = "Read me"
    txt = [
        "Bloomberg download for the Global Macro Book (paper research only; keep the data private, do not share)",
        "",
        "1. On a UBC Bloomberg terminal, log in, open this file in Excel; check the Bloomberg tab is in the ribbon.",
        "2. Bloomberg tab -> Refresh Workbook. Wait until no cell shows 'Requesting Data...' (a few minutes).",
        "3. A cell showing '#N/A Invalid Security': search the series name in Bloomberg, paste the right ticker into",
        "   the yellow cell, refresh again. Leave it if you cannot find it.",
        "4. Bloomberg tab -> Convert to values (if offered), then File -> Save As .xlsx to email/USB.",
        "5. Put the file into Documents\\WRDS results\\mscifreedata.",
        "",
        "Sheets in priority order (do them left to right; stop wherever time runs out; save after each):",
        " 1 Economics: value as FIRST RELEASED, consensus median before release, release date, revised value.",
        " 2 Returns: per-commodity excess-return indexes (properly rolled) incl. alternative commodities.",
        " 3 Curves: front, second and ~12-month futures (commodity carry), incl. alternative commodities.",
        " 4 RatesFutures: short-rate futures (implied policy path; a real front-end market).",
        " 5 EquityValuation: MSCI country P/E, forward P/E, P/B, dividend yield, forward EPS (value + revisions).",
        " 6 Breakevens: 10y breakevens and US real yield (real-rate FX and gold).",
        " 7 Benchmarks: CTA / macro fund indexes (crowding check).",
        " 8 Surprise: Citi economic surprise indexes.",
        " 9 FXBasis (optional): cross-currency basis (dollar funding stress).",
        " 10 DailyCommodities (optional, only if the limit allows): daily commodity excess-return indexes from 1990.",
        "If cells show '#N/A Limit' the terminal's monthly download allowance is used up: save what you have.",
        "Check UBC's Bloomberg terms of use; the file stays private (like the MSCI files, it is never put on GitHub).",
    ]
    for i, t in enumerate(txt, 1):
        ws.cell(i, 1, t).font = Font(name=F, bold=(i == 1), size=12 if i == 1 else 10)
    ws.column_dimensions["A"].width = 120
    block_sheet(wb, "Economics", ECO, "ECO_RELEASE_DT,ACTUAL_RELEASE,BN_SURVEY_MEDIAN,PX_LAST",
                "Monthly: release date, first-released value, consensus median, latest value. Yellow = ticker.")
    rets = []
    for n, g, b, *_ in C + ALT:
        if g:
            rets.append((n + " GSCI ER", g))
        if b:
            rets.append((n + " BCOM ER", b))
    block_sheet(wb, "Returns", rets, "PX_LAST", "Monthly PX_LAST of excess-return indexes. Yellow = ticker.")
    curves = []
    for n, g, b, c1, c2, c12 in C + ALT:
        curves += [(n + " 1st", c1), (n + " 2nd", c2), (n + " ~12m", c12)]
    block_sheet(wb, "Curves", curves, "PX_LAST", "Monthly PX_LAST of generic futures. Yellow = ticker.")
    block_sheet(wb, "RatesFutures", RATES_FUT, "PX_LAST", "Monthly PX_LAST of short-rate futures (100 - rate).")
    block_sheet(wb, "EquityValuation", EQ_VAL, "PE_RATIO,BEST_PE_RATIO,PX_TO_BOOK_RATIO,EQY_DVD_YLD_12M,BEST_EPS",
                "Monthly: trailing P/E, forward P/E, price/book, 12m dividend yield, forward EPS (consensus).")
    block_sheet(wb, "Breakevens", BREAKEVENS, "PX_LAST", "Monthly PX_LAST. Yellow = ticker.")
    block_sheet(wb, "Benchmarks", BENCH, "PX_LAST", "Monthly PX_LAST of fund indexes. Yellow = ticker.")
    block_sheet(wb, "Surprise", SURPRISE, "PX_LAST", "Monthly PX_LAST. Yellow = ticker.")
    block_sheet(wb, "FXBasis", FX_BASIS, "PX_LAST", "Optional. Monthly PX_LAST. Yellow = ticker.")
    daily = [(n + " GSCI ER", g) for n, g, b, *_ in C + ALT if g]
    block_sheet(wb, "DailyCommodities", daily, "PX_LAST", "Optional, last priority. DAILY PX_LAST from 1990.",
                per="D", start="12/31/1989")
    wb.save(out)
    n_t = len(ECO) + len(rets) + len(curves) + len(RATES_FUT) + len(EQ_VAL) + len(BREAKEVENS) + len(BENCH) + \
        len(SURPRISE) + len(FX_BASIS) + len(daily)
    print("saved", out, "tickers:", n_t, {"eco": len(ECO), "returns": len(rets), "curves": len(curves),
                                          "rates": len(RATES_FUT), "eqval": len(EQ_VAL), "daily": len(daily)})


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "Bloomberg_commodities_UBC.xlsx")
