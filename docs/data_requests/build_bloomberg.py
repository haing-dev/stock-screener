"""Builds Bloomberg_commodities_UBC.xlsx: Bloomberg-terminal workbook (BDH formulas) for the Global Macro Book.
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
F = "Arial"
YEL = PatternFill("solid", start_color="FFFF00")


def block_sheet(wb, name, cols, fields, note, width=3):
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
        s.cell(5, c, '=BDH(%s3,"%s","12/31/1969","","Per=M","Days=A","Fill=P","Dir=V","Dts=S")' % (L(c), fields)).font = Font(name=F)
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
        "Sheets (priority order if time is short): Economics, Curves, Returns, Surprise.",
        " Economics: for each macro series, the value as FIRST RELEASED, the economists' consensus median before the",
        "   release, the release date and today's revised value, monthly. This is what we cannot get for free.",
        " Curves: front, second and ~12-month futures prices (commodity carry).",
        " Returns: per-commodity excess-return indexes from the earliest date (commodities before 2000).",
        " Surprise: Citi economic surprise indexes.",
        "Monthly data for ~150 tickers stays well inside the terminal's monthly download limit.",
    ]
    for i, t in enumerate(txt, 1):
        ws.cell(i, 1, t).font = Font(name=F, bold=(i == 1), size=12 if i == 1 else 10)
    ws.column_dimensions["A"].width = 120
    block_sheet(wb, "Economics", ECO, "ECO_RELEASE_DT,ACTUAL_RELEASE,BN_SURVEY_MEDIAN,PX_LAST",
                "Monthly: release date, first-released value, consensus median, latest value. Yellow = ticker.")
    curves = []
    for n, g, b, c1, c2, c12 in C:
        curves += [(n + " 1st", c1), (n + " 2nd", c2), (n + " ~12m", c12)]
    block_sheet(wb, "Curves", curves, "PX_LAST", "Monthly PX_LAST of generic futures. Yellow = ticker.")
    rets = []
    for n, g, b, *_ in C:
        rets.append((n + " GSCI ER", g))
        if b:
            rets.append((n + " BCOM ER", b))
    block_sheet(wb, "Returns", rets, "PX_LAST", "Monthly PX_LAST of excess-return indexes. Yellow = ticker.")
    block_sheet(wb, "Surprise", SURPRISE, "PX_LAST", "Monthly PX_LAST. Yellow = ticker.")
    wb.save(out)
    print("saved", out, len(ECO), "eco,", len(curves), "curve,", len(rets), "return,", len(SURPRISE), "surprise tickers")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "Bloomberg_commodities_UBC.xlsx")
