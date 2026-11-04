"""Builds Bloomberg_equities_UBC.xlsx (v1, 2026-11-04): Bloomberg-terminal workbook for every US-listed stock our
screens can touch (the 14 archived screens, the 3 triage screens, the clinical-biotech checks).

Universe: NYSE + Nasdaq + NYSE American listings (Nasdaq screener lists mirrored at github.com/rreichel3/US-Stock-Symbols,
fetched 2026-11-04), minus warrants, rights, units, preferreds, notes, funds and SPACs, market cap >= $25M; the live
triage calls (branch triage-record) come first, then by market cap. Snapshot of that list: equity_universe.csv.

All Bloomberg formulas are live (v2, 2026-11-04, at the user's request): open on the terminal and Refresh Workbook. Field mnemonics sit in row 3 of each sheet; formulas read them from there, so a
wrong mnemonic is fixed once per column. Confidence 'check' = mnemonic not certain (verify with FLDS on the terminal).

    python3 docs/data_requests/build_bloomberg_equities.py [--universe-json DIR] [--small N] [OUT.xlsx]
"""
import csv
import json
import os
import re
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter as L

HERE = os.path.dirname(os.path.abspath(__file__))
UNIV_CSV = os.path.join(HERE, "equity_universe.csv")
F = "Arial"
YEL = PatternFill("solid", fgColor="FFFF00")
GREY = PatternFill("solid", fgColor="E7E6E6")
BLUE = PatternFill("solid", fgColor="DDEBF7")
BLOCK = 500
MIN_MCAP = 25e6
USD = ("EQY_FUND_CRNCY", "USD")
FY1, FY2, BF = ("BEST_FPERIOD_OVERRIDE", "1FY"), ("BEST_FPERIOD_OVERRIDE", "2FY"), ("BEST_FPERIOD_OVERRIDE", "1BF")

# ---------------------------------------------------------------- snapshot fields: (mnemonic, override, label, used for, ok)
# ok: 'yes' = standard mnemonic; 'check' = verify with FLDS (a wrong one shows '#N/A Invalid Field' in that column only)
ALL = "all screens"
S1 = ("S1_Identity", "Tier 1 - identity, listing, industry, dates", [
    ("NAME", None, "Short name", ALL, "yes"),
    ("LONG_COMP_NAME", None, "Full company name", ALL, "yes"),
    ("TICKER", None, "Ticker", ALL, "yes"),
    ("EXCH_CODE", None, "Exchange code", "universe (NYSE/Nasdaq/NYSE American)", "yes"),
    ("EQY_PRIM_EXCH", None, "Primary exchange", "universe; ADR check", "yes"),
    ("ID_BB_GLOBAL", None, "FIGI (matches our 13F/OpenFIGI mapping)", "13F owners cells", "yes"),
    ("ID_BB_COMPANY", None, "Bloomberg company id", "links share classes", "check"),
    ("ID_ISIN", None, "ISIN", "matching to SEC/WRDS", "yes"),
    ("ID_CUSIP", None, "CUSIP (matches 13F filings)", "13F owners cells", "yes"),
    ("ID_SEDOL1", None, "SEDOL", "matching", "yes"),
    ("SECURITY_TYP", None, "Security type (Common Stock, ADR, REIT, ...)", "universe: no funds/SPACs/REITs", "yes"),
    ("SECURITY_TYP2", None, "Security type 2", "universe", "yes"),
    ("MARKET_STATUS", None, "Active / delisted / halted", "universe", "yes"),
    ("CNTRY_OF_DOMICILE", None, "Country of domicile", "US-only triage; foreign filers", "yes"),
    ("CNTRY_OF_INCORPORATION", None, "Country of incorporation", "US-only triage", "yes"),
    ("CRNCY", None, "Quote currency", "price / market cap units", "yes"),
    ("EQY_FUND_CRNCY", None, "Reporting currency of the financials", "foreign filers; USD conversion", "yes"),
    ("ADR_SH_PER_ADR", None, "Ordinary shares per ADR", "ADR market caps (known gap)", "check"),
    ("ADR_UNDL_TICKER", None, "Underlying ordinary-share ticker", "ADR market caps (known gap)", "check"),
    ("GICS_SECTOR_NAME", None, "GICS sector", "peer groups; industry exclusions", "yes"),
    ("GICS_INDUSTRY_GROUP_NAME", None, "GICS industry group", "peer groups", "yes"),
    ("GICS_INDUSTRY_NAME", None, "GICS industry", "peer groups (Core/Emerging cheap vs peers)", "yes"),
    ("GICS_SUB_INDUSTRY_NAME", None, "GICS sub-industry", "peer groups; similar stocks", "yes"),
    ("GICS_SUB_INDUSTRY", None, "GICS sub-industry code (8 digits)", "peer groups", "yes"),
    ("INDUSTRY_SECTOR", None, "Bloomberg (BICS legacy) sector", "peer groups", "yes"),
    ("INDUSTRY_GROUP", None, "Bloomberg industry group", "peer groups", "yes"),
    ("INDUSTRY_SUBGROUP", None, "Bloomberg industry subgroup", "peer groups", "yes"),
    ("BICS_LEVEL_1_SECTOR_NAME", None, "BICS level 1", "peer groups", "yes"),
    ("BICS_LEVEL_2_INDUSTRY_GROUP_NAME", None, "BICS level 2", "peer groups", "yes"),
    ("BICS_LEVEL_3_INDUSTRY_NAME", None, "BICS level 3", "peer groups", "yes"),
    ("BICS_LEVEL_4_SUB_INDUSTRY_NAME", None, "BICS level 4", "peer groups", "check"),
    ("SIC_CODE", None, "US SIC code (our universe rules use SIC)", "every screen's universe; Tech/Healthcare/Cyclicals", "check"),
    ("NAICS_CODE", None, "NAICS code", "industry rules backup", "check"),
    ("EQY_INIT_PO_DT", None, "IPO date", "Special Situations (IPO <= 36 months); history length", "yes"),
    ("EQY_FISCAL_YR_END", None, "Fiscal year end month", "TTM / fiscal alignment", "check"),
    ("LATEST_PERIOD_END_DT_FULL_RECORD", None, "Latest reported period end", "recent report <= 1.6 yrs; balance sheet <= 200 days", "yes"),
    ("LATEST_ANNOUNCEMENT_DT", None, "Latest earnings announcement date", "point in time; recent report", "check"),
    ("EXPECTED_REPORT_DT", None, "Next expected report date", "catalyst calendar", "yes"),
    ("NUM_OF_EMPLOYEES", None, "Employees", "sales per employee; size", "check"),
    ("ULT_PARENT_TICKER_EXCHANGE", None, "Ultimate parent ticker", "spin-offs / subsidiaries (Special Situations)", "check"),
    ("COMPANY_WEB_ADDRESS", None, "Website", "human / AI review", "check"),
    ("CIE_DES", None, "Business description (long text)", "human / AI review (moat, segments)", "yes"),
])
S2 = ("S2_Market", "Tier 1 - price, trading, size, momentum, risk, short interest, implied vol", [
    ("PX_LAST", None, "Last price", ALL, "yes"),
    ("PX_CLOSE_1D", None, "Previous close", "returns", "yes"),
    ("PX_OPEN", None, "Open", "entry price (triage enters at the next open)", "yes"),
    ("PX_HIGH", None, "Day high", "", "yes"),
    ("PX_LOW", None, "Day low", "", "yes"),
    ("PX_BID", None, "Bid", "trading cost", "yes"),
    ("PX_ASK", None, "Ask", "trading cost", "yes"),
    ("PX_VOLUME", None, "Volume today (shares)", "liquidity", "yes"),
    ("TURNOVER", None, "Value traded today", "liquidity", "yes"),
    ("VOLUME_AVG_10D", None, "Average volume 10 days (shares)", "liquidity", "yes"),
    ("VOLUME_AVG_30D", None, "Average volume 30 days (shares)", "liquidity: avg daily value traded gates", "yes"),
    ("VOLUME_AVG_3M", None, "Average volume 3 months (shares)", "liquidity gates (x price = $ traded)", "yes"),
    ("VOLUME_AVG_6M", None, "Average volume 6 months (shares)", "liquidity", "yes"),
    ("EQY_SH_OUT", None, "Shares outstanding (millions)", "market cap; dilution", "yes"),
    ("EQY_FLOAT", None, "Float (millions of shares)", "insider share = 1 - float / shares (Owner-Operators O4)", "yes"),
    ("EQY_FREE_FLOAT_PCT", None, "Free float %", "Owner-Operators O4 (insider ownership)", "yes"),
    ("CUR_MKT_CAP", None, "Market cap (quote currency)", "size gates in every screen; ADR fix", "yes"),
    ("CURR_ENTP_VAL", None, "Enterprise value", "EV multiples (Emerging, Hidden, Special, Owner-Op, Hard Assets, Clinical)", "yes"),
    ("HIGH_52WEEK", None, "52-week high", "Hidden Earnings event (40%+ below 12-month high)", "yes"),
    ("HIGH_DT_52WEEK", None, "Date of 52-week high", "Hidden Earnings event", "yes"),
    ("LOW_52WEEK", None, "52-week low", "drawdown", "yes"),
    ("LOW_DT_52WEEK", None, "Date of 52-week low", "", "yes"),
    ("CHG_PCT_1D", None, "Price change 1 day %", "", "yes"),
    ("CHG_PCT_5D", None, "Price change 5 days %", "", "yes"),
    ("CHG_PCT_1M", None, "Price change 1 month %", "similar-stock matching (momentum)", "yes"),
    ("CHG_PCT_3M", None, "Price change 3 months %", "", "yes"),
    ("CHG_PCT_6M", None, "Price change 6 months %", "", "yes"),
    ("CHG_PCT_YTD", None, "Price change year to date %", "", "yes"),
    ("CHG_PCT_1YR", None, "Price change 1 year %", "similar-stock matching (12-month return)", "yes"),
    ("CHG_PCT_2YR", None, "Price change 2 years %", "", "check"),
    ("CHG_PCT_5YR", None, "Price change 5 years %", "", "check"),
    ("MOV_AVG_50D", None, "50-day moving average", "trend", "yes"),
    ("MOV_AVG_200D", None, "200-day moving average", "trend", "yes"),
    ("RSI_14D", None, "RSI 14 days", "", "yes"),
    ("EQY_BETA", None, "Beta (raw)", "risk", "yes"),
    ("BETA_ADJ_OVERRIDABLE", None, "Beta (adjusted)", "risk", "yes"),
    ("VOLATILITY_30D", None, "Realised volatility 30 days", "risk", "yes"),
    ("VOLATILITY_90D", None, "Realised volatility 90 days", "risk", "yes"),
    ("VOLATILITY_260D", None, "Realised volatility 1 year", "risk; similar stocks", "yes"),
    ("30DAY_IMPVOL_100.0%MNY_DF", None, "Implied volatility 30 days at the money", "risk (no OptionMetrics on WRDS)", "yes"),
    ("3MTH_IMPVOL_100.0%MNY_DF", None, "Implied volatility 3 months at the money", "risk; event pricing", "yes"),
    ("SHORT_INT", None, "Short interest (shares)", "Red Flags review (short interest / squeeze risk)", "yes"),
    ("SHORT_INT_RATIO", None, "Short interest days to cover", "Red Flags review", "yes"),
    ("SI_PERCENT_EQUITY_FLOAT", None, "Short interest % of float", "Red Flags review", "check"),
])
S3 = ("S3_Valuation_LTM", "Tier 1 - valuation, last 12 months, latest balance sheet (money fields in USD)", [
    ("PE_RATIO", None, "P/E (trailing)", "valuation", "yes"),
    ("PX_TO_BOOK_RATIO", None, "Price / book", "Asset-Floor", "yes"),
    ("PX_TO_TANG_BV_PER_SH", None, "Price / tangible book", "Asset-Floor K4 (P/TBV <= 1)", "check"),
    ("PX_TO_SALES_RATIO", None, "Price / sales", "Red Flags W3; Tech A16", "yes"),
    ("PX_TO_CASH_FLOW", None, "Price / cash flow", "valuation", "yes"),
    ("PX_TO_FREE_CASH_FLOW", None, "Price / free cash flow", "Trough Cyclical T8; Hidden cash yield", "yes"),
    ("CURRENT_EV_TO_T12M_EBITDA", None, "EV / EBITDA (LTM)", "Emerging E12 / cheap vs own past and peers", "yes"),
    ("EV_TO_T12M_SALES", None, "EV / sales (LTM)", "Red Flags W3 (>= 6x); Tech A16", "check"),
    ("EV_TO_T12M_EBIT", None, "EV / EBIT (LTM)", "Hidden X9, Special S4, Owner-Op O11, Hard Assets R10; Core cheapness", "check"),
    ("ENTERPRISE_VALUE", None, "Enterprise value (latest balance sheet)", "EV multiples", "yes"),
    ("FREE_CASH_FLOW_YIELD", None, "Free cash flow yield", "Hidden Earnings cash yield cell", "yes"),
    ("EARN_YLD", None, "Earnings yield", "cheapness", "check"),
    ("EQY_DVD_YLD_IND", None, "Dividend yield (indicated)", "shareholder returns", "yes"),
    ("EQY_DVD_YLD_12M", None, "Dividend yield (12 months)", "shareholder returns", "yes"),
    ("DVD_PAYOUT_RATIO", None, "Dividend payout ratio", "shareholder returns", "yes"),
    ("TRAIL_12M_NET_SALES", USD, "Revenue LTM (USD)", "size gates; growth", "yes"),
    ("TRAIL_12M_GROSS_PROFIT", USD, "Gross profit LTM (USD)", "gross margin gates (Emerging E6, Tech A7, HC H6)", "check"),
    ("TRAIL_12M_OPER_INC", USD, "Operating income LTM (USD)", "Hidden X4, Special S2; EV/EBIT", "check"),
    ("TRAIL_12M_EBITDA", USD, "EBITDA LTM (USD)", "Emerging E3/E12; leverage", "yes"),
    ("TRAIL_12M_NET_INC", USD, "Net income LTM (USD)", "cash conversion", "yes"),
    ("TRAIL_12M_EPS", None, "EPS LTM", "", "yes"),
    ("TRAIL_12M_FREE_CASH_FLOW", USD, "Free cash flow LTM (USD)", "Hidden X6; cash yield", "yes"),
    ("TRAIL_12M_CASH_FROM_OPER", USD, "Operating cash flow LTM (USD)", "Asset-Floor K5; Clinical burn", "check"),
    ("TRAIL_12M_CAPITAL_EXPEND", USD, "Capex LTM (USD)", "FCF; Hard Assets R4", "check"),
    ("BS_CASH_NEAR_CASH_ITEM", USD, "Cash and equivalents (USD)", "net debt; Clinical runway B2; Asset-Floor K4", "yes"),
    ("BS_MKT_SEC_OTHER_ST_INVEST", USD, "Short-term investments (USD)", "net cash (biotech holds T-bills)", "yes"),
    ("BS_ACCT_NOTE_RCV", USD, "Receivables (USD)", "Tech A13 receivable days", "yes"),
    ("BS_INVENTORIES", USD, "Inventories (USD)", "Tech A13 inventory days; Asset-Floor", "yes"),
    ("BS_CUR_ASSET_REPORT", USD, "Current assets (USD)", "net-net / Asset-Floor", "yes"),
    ("BS_TOT_ASSET", USD, "Total assets (USD)", "ROIC; Altman", "yes"),
    ("BS_ST_BORROW", USD, "Short-term debt incl. current portion (USD)", "Fortress F11 refinancing (debt due soon)", "yes"),
    ("BS_LT_BORROW", USD, "Long-term debt (USD)", "leverage gates", "yes"),
    ("SHORT_AND_LONG_TERM_DEBT", USD, "Total debt (USD)", "leverage gates; Clinical B3 debt / cash", "yes"),
    ("NET_DEBT", USD, "Net debt (USD)", "leverage gates in every screen", "yes"),
    ("BS_CUR_LIAB", USD, "Current liabilities (USD)", "net-net; invested capital", "yes"),
    ("BS_TOT_LIAB2", USD, "Total liabilities (USD)", "Asset-Floor", "check"),
    ("TOTAL_EQUITY", USD, "Total equity (USD)", "book value", "yes"),
    ("BS_GOODWILL", USD, "Goodwill (USD)", "tangible book; acquisitions", "check"),
    ("BS_DISCLOSED_INTANGIBLES", USD, "Intangibles (USD)", "tangible book", "check"),
    ("MINORITY_NONCONTROLLING_INTEREST", USD, "Minority interest (USD)", "EV", "check"),
    ("BS_SH_OUT", None, "Shares on the balance sheet (millions)", "dilution; market cap check", "yes"),
    ("BOOK_VAL_PER_SH", None, "Book value per share", "Asset-Floor", "yes"),
    ("TANG_BOOK_VAL_PER_SH", None, "Tangible book per share", "Asset-Floor K4 (TBV/share not down over 3 yrs)", "yes"),
    ("NET_DEBT_TO_EBITDA", None, "Net debt / EBITDA", "leverage gates (backend)", "check"),
    ("TOT_DEBT_TO_EBITDA", None, "Total debt / EBITDA", "leverage", "yes"),
    ("TOT_DEBT_TO_TOT_EQY", None, "Debt / equity", "leverage", "yes"),
    ("CUR_RATIO", None, "Current ratio", "liquidity of the balance sheet", "yes"),
    ("QUICK_RATIO", None, "Quick ratio", "", "yes"),
    ("INTEREST_COVERAGE_RATIO", None, "EBIT / interest", "Fortress F10 (>= 6x)", "check"),
    ("ALTMAN_Z_SCORE", None, "Altman Z-score", "distress check (Hidden, Trough Cyclical)", "check"),
])
S4 = ("S4_LastFY", "Tier 2 - latest fiscal year detail and quality ratios (money fields in USD)", [
    ("SALES_REV_TURN", USD, "Revenue, last FY (USD)", "size gates; growth", "yes"),
    ("IS_COG_AND_SERVICES_SOLD", USD, "Cost of goods sold (USD)", "gross margin", "check"),
    ("GROSS_PROFIT", USD, "Gross profit (USD)", "gross margin gates", "yes"),
    ("GROSS_MARGIN", None, "Gross margin %", "Emerging E6, Tech A7, HC H6, Fortress F13", "yes"),
    ("IS_SGA_EXPENSE", USD, "SG&A (USD)", "Emerging E7 operating leverage", "check"),
    ("IS_RD_EXPEND", USD, "R&D (USD)", "Tech; Clinical burn", "check"),
    ("IS_OPER_INC", USD, "Operating income (USD)", "profit gates; ROIC; EV/EBIT", "yes"),
    ("OPER_MARGIN", None, "Operating margin %", "Fortress F7; Hard Assets R5; Cyclicals C7", "yes"),
    ("EBITDA", USD, "EBITDA (USD)", "leverage; EV/EBITDA", "yes"),
    ("EBIT", USD, "EBIT (USD)", "EV/EBIT; coverage", "yes"),
    ("CF_DEPR_AMORT", USD, "Depreciation and amortisation (USD)", "D&A share of EBITDA; Trough T6 capex/D&A", "yes"),
    ("IS_INT_EXPENSE", USD, "Interest expense (USD)", "Fortress F10", "yes"),
    ("PRETAX_INC", USD, "Pretax income (USD)", "tax rate for ROIC", "yes"),
    ("IS_INC_TAX_EXP", USD, "Income tax (USD)", "tax rate for ROIC", "yes"),
    ("NET_INCOME", USD, "Net income (USD)", "cash conversion G7/H7/O7", "yes"),
    ("PROF_MARGIN", None, "Net margin %", "", "yes"),
    ("IS_EPS", None, "EPS (basic)", "", "yes"),
    ("IS_DILUTED_EPS", None, "EPS (diluted)", "", "yes"),
    ("IS_SH_FOR_DILUTED_EPS", None, "Diluted share count", "dilution gates (E8, A10)", "check"),
    ("IS_ABNORMAL_ITEM", USD, "Unusual items (USD)", "Hidden Earnings (one-offs)", "check"),
    ("IS_DISCONTINUED_OPERATIONS", USD, "Discontinued operations (USD)", "Hidden Earnings X3 (discontinued ops >= 1% of revenue)", "check"),
    ("CF_CASH_FROM_OPER", USD, "Operating cash flow (USD)", "FCF; Hard Assets R4", "yes"),
    ("CAPITAL_EXPEND", USD, "Capex (USD)", "FCF; Trough T6; Tech A11", "yes"),
    ("CF_FREE_CASH_FLOW", USD, "Free cash flow (USD)", "cash gates in most screens", "yes"),
    ("CF_STOCK_BASED_COMPENSATION", USD, "Stock-based pay (USD)", "cash conversion (FCF - stock pay); Tech A6/A9", "check"),
    ("CF_DVD_PAID", USD, "Dividends paid (USD)", "Trough industry cash returned", "yes"),
    ("CF_DECR_CAP_STOCK", USD, "Buybacks (USD)", "Trough industry cash returned", "yes"),
    ("CF_INCR_CAP_STOCK", USD, "Shares issued (USD)", "dilution; Clinical funding", "yes"),
    ("RETURN_ON_INV_CAPITAL", None, "ROIC %", "Core G5, Fortress F8, HC H5, Owner-Op O6, Cyclicals C4, Hidden X7", "yes"),
    ("RETURN_COM_EQY", None, "ROE %", "", "yes"),
    ("RETURN_ON_ASSET", None, "ROA %", "", "yes"),
    ("ASSET_TURNOVER", None, "Asset turnover", "", "yes"),
    ("INVENT_TURN", None, "Inventory turnover", "Tech A13 (hardware)", "yes"),
    ("ACCT_RCV_TURN", None, "Receivables turnover", "Tech A13 (software)", "check"),
    ("CASH_CONVERSION_CYCLE", None, "Cash conversion cycle (days)", "working capital", "check"),
    ("SALES_GROWTH", None, "Revenue growth %, last FY", "Emerging E5; Tech A5", "yes"),
    ("EBITDA_GROWTH", None, "EBITDA growth %", "", "check"),
    ("EPS_GROWTH", None, "EPS growth %", "", "check"),
    ("EFF_TAX_RATE", None, "Effective tax rate", "ROIC (NOPAT)", "check"),
])
S5 = ("S5_Estimates", "Tier 2 - analyst consensus (BEst): forward estimates, targets, ratings", [
    ("BEST_EPS", FY1, "EPS estimate, this fiscal year", "forward valuation; revisions", "yes"),
    ("BEST_EPS", FY2, "EPS estimate, next fiscal year", "forward valuation", "yes"),
    ("BEST_EPS", BF, "EPS estimate, blended 12 months forward", "forward P/E", "yes"),
    ("BEST_SALES", FY1, "Revenue estimate, this FY", "growth not fading (Emerging E5, Tech A5)", "yes"),
    ("BEST_SALES", FY2, "Revenue estimate, next FY", "growth", "yes"),
    ("BEST_EBITDA", FY1, "EBITDA estimate, this FY", "forward EV/EBITDA", "yes"),
    ("BEST_EBITDA", FY2, "EBITDA estimate, next FY", "forward EV/EBITDA", "yes"),
    ("BEST_EBIT", FY1, "EBIT estimate, this FY", "forward EV/EBIT", "check"),
    ("BEST_NET_INCOME", FY1, "Net income estimate, this FY", "", "check"),
    ("BEST_CAPEX", FY1, "Capex estimate, this FY", "forward FCF", "check"),
    ("BEST_PE_RATIO", BF, "Forward P/E", "cheapness", "yes"),
    ("BEST_EV_TO_BEST_EBITDA", BF, "Forward EV / EBITDA", "cheapness", "check"),
    ("BEST_EPS_HI", FY1, "Highest EPS estimate, this FY", "dispersion", "check"),
    ("BEST_EPS_LO", FY1, "Lowest EPS estimate, this FY", "dispersion", "check"),
    ("BEST_EPS_NUMEST", FY1, "Number of EPS estimates", "coverage (no coverage = weak Hidden events)", "check"),
    ("BEST_TARGET_PRICE", None, "Consensus target price", "upside", "yes"),
    ("BEST_ANALYST_RATING", None, "Consensus rating (1-5)", "", "yes"),
    ("EQY_REC_CONS", None, "Consensus recommendation", "", "check"),
    ("TOT_ANALYST_REC", None, "Number of analyst recommendations", "coverage", "yes"),
    ("TOT_BUY_REC", None, "Buy recommendations", "", "yes"),
    ("TOT_HOLD_REC", None, "Hold recommendations", "", "yes"),
    ("TOT_SELL_REC", None, "Sell recommendations", "", "yes"),
    ("BEST_EST_LONG_TERM_GROWTH", None, "Long-term EPS growth estimate", "Tech S-curve; PEG", "check"),
])
S6 = ("S6_Owners_Credit", "Tier 2 - ownership, credit, governance", [
    ("EQY_INST_PCT_SH_OUT", None, "Institutional ownership % of shares", "High Conviction / Top Performer owners context", "check"),
    ("PCT_INSIDER_SHARES_OUT", None, "Insider ownership % of shares", "Owner-Operators O4 (>= 20%)", "check"),
    ("EQY_FREE_FLOAT_PCT", None, "Free float % (repeat; insider proxy)", "Owner-Operators O4", "yes"),
    ("RTG_SP_LT_LC_ISSUER_CREDIT", None, "S&P long-term issuer rating", "Fortress; distress", "check"),
    ("RTG_MDY_LT_CORP_FAMILY", None, "Moody's corporate family rating", "Fortress; distress", "check"),
    ("RTG_FITCH_LT_ISSUER_DEFAULT", None, "Fitch issuer default rating", "Fortress; distress", "check"),
    ("BB_1YR_DEFAULT_PROB", None, "Bloomberg 1-year default probability (DRSK)", "distress (Hidden, Trough, Clinical)", "check"),
    ("ESG_DISCLOSURE_SCORE", None, "ESG disclosure score", "", "check"),
    ("BOARD_SIZE", None, "Board size", "governance (Owner-Operators review)", "check"),
    ("PCT_INDEPENDENT_DIRECTORS", None, "% independent directors", "governance", "check"),
    ("CEO_DUALITY", None, "CEO is also chair", "governance", "check"),
])
SNAPS = [S1, S2, S3, S5, S4, S6]

# ---------------------------------------------------------------- history blocks (BDH, Dir=H, one row per field)
H_ANNUAL = ["SALES_REV_TURN", "GROSS_PROFIT", "IS_OPER_INC", "EBITDA", "CF_DEPR_AMORT", "IS_INT_EXPENSE", "PRETAX_INC",
            "IS_INC_TAX_EXP", "NET_INCOME", "CF_CASH_FROM_OPER", "CAPITAL_EXPEND", "CF_FREE_CASH_FLOW", "CF_DVD_PAID",
            "CF_DECR_CAP_STOCK", "BS_CASH_NEAR_CASH_ITEM", "BS_MKT_SEC_OTHER_ST_INVEST", "BS_ACCT_NOTE_RCV",
            "BS_INVENTORIES", "BS_CUR_ASSET_REPORT", "BS_TOT_ASSET", "BS_CUR_LIAB", "BS_ST_BORROW", "BS_LT_BORROW",
            "TOTAL_EQUITY", "BS_SH_OUT", "CUR_MKT_CAP", "BS_GOODWILL", "IS_RD_EXPEND", "IS_SGA_EXPENSE",
            "CF_STOCK_BASED_COMPENSATION", "IS_DISCONTINUED_OPERATIONS"]
H_QUARTER = ["SALES_REV_TURN", "GROSS_PROFIT", "IS_OPER_INC", "EBITDA", "NET_INCOME", "IS_DILUTED_EPS",
             "CF_CASH_FROM_OPER", "CAPITAL_EXPEND", "CF_FREE_CASH_FLOW", "BS_CASH_NEAR_CASH_ITEM",
             "BS_MKT_SEC_OTHER_ST_INVEST", "SHORT_AND_LONG_TERM_DEBT", "BS_SH_OUT", "IS_RD_EXPEND",
             "CF_STOCK_BASED_COMPENSATION"]
H_MONTH = ["PX_LAST", "TOT_RETURN_INDEX_GROSS_DVDS", "CUR_MKT_CAP", "PX_VOLUME", "BEST_EPS", "BEST_SALES",
           "BEST_PE_RATIO", "BEST_TARGET_PRICE", "SHORT_INT", "PE_RATIO", "PX_TO_BOOK_RATIO", "CURRENT_EV_TO_T12M_EBITDA"]
HISTS = [  # (prefix, fields, start, options, tickers (None = all), per-sheet, what)
    ("H1_Annual", H_ANNUAL, "12/31/2003", '"Per=Y","Dir=H","Dts=S","EQY_FUND_CRNCY=USD"', None, BLOCK,
     "Tier 2 - annual statements FY2004 to date (USD): 10-year ROIC, CAGR, margin stability, downturn years "
     "2008-09/2015-16/2020/2022, cash conversion, dilution. Our SEC data starts 2009; this fills 2004-2009."),
    ("H2_Quarterly", H_QUARTER, "12/31/2014", '"Per=Q","Dir=H","Dts=S","EQY_FUND_CRNCY=USD"', 1000, BLOCK,
     "Tier 3 - quarterly statements 2015 to date (USD): TTM, year-to-date growth, burn rate, balance-sheet age."),
    ("H3_Monthly", H_MONTH, "12/31/2004", '"Per=M","Dir=H","Dts=S","BEST_FPERIOD_OVERRIDE=1BF"', 500, BLOCK,
     "Tier 3 - month-end prices, total-return index, market cap, consensus EPS/sales (12 months forward, as it "
     "was each month = estimate revisions), short interest, multiples, 2005 to date."),
]
BULKS = [  # (sheet, [(label, formula pattern with {t})], rows per ticker, tickers, what)
    ("B1_Holders", [("Top 20 holders (13F, funds, insiders)", '=BDS({t},"TOP_20_HOLDERS_PUBLIC_FILERS")')], 24, 300,
     "Tier 3 - largest holders (High Conviction / Top Performer owners cross-check; insider stakes)."),
    ("B2_Dividends", [("Dividends, specials, spin-offs since 2015", '=BDS({t},"DVD_HIST_ALL","DVD_START_DT","20150101")')],
     50, 300, "Tier 3 - dividend history incl. special dividends and SPIN-OFFS (Special Situations)."),
    ("B3_Segments", [("Revenue by product segment", '=BDS({t},"PG_REVENUE","PRODUCT_GEO_OVERRIDE","P")'),
                     ("Revenue by region", '=BDS({t},"PG_REVENUE","PRODUCT_GEO_OVERRIDE","G")')], 25, 300,
     "Tier 3 - segment and geographic revenue (Hidden Earnings: which segment the market fears; check)."),
    ("B4_EarningsDates", [("Earnings announcement history", '=BDS({t},"EARN_ANN_DT_TIME_HIST_WITH_EPS")')], 40, 300,
     "Tier 3 - past announcement dates with EPS (point-in-time timing; check)."),
]


# ---------------------------------------------------------------- universe
def make_universe(json_dir, ledger_csv=None):
    bad = re.compile(r"warrant|\bright|\bunits?\b|preferred|notes due|debenture|%|subordinated|\bfund\b|\betf\b|"
                     r"municipal|acquisition corp", re.I)
    rows, seen = [], set()
    exch = {"nasdaq": "Nasdaq", "nyse": "NYSE", "amex": "NYSE American"}
    for ex, nm in exch.items():
        for d in json.load(open(os.path.join(json_dir, ex + "_full_tickers.json")) if os.path.exists(
                os.path.join(json_dir, ex + "_full_tickers.json")) else open(os.path.join(json_dir, ex + ".json"))):
            s = (d.get("symbol") or "").strip()
            if not s or "^" in s or bad.search(d.get("name") or "") or s in seen:
                continue
            try:
                mc = float(d.get("marketCap") or 0)
            except ValueError:
                mc = 0.0
            seen.add(s)
            rows.append({"symbol": s, "name": (d.get("name") or "").strip(), "exchange": nm,
                         "country": d.get("country") or "", "sector": d.get("sector") or "",
                         "industry": d.get("industry") or "", "mcap_musd": round(mc / 1e6, 1)})
    live = []
    if ledger_csv and os.path.exists(ledger_csv):
        live = sorted({r["ticker"].replace("-", "/") for r in csv.DictReader(open(ledger_csv, encoding="utf-8"))})
    by = {r["symbol"]: r for r in rows}
    out = []
    for s in live:
        r = by.get(s) or {"symbol": s, "name": "", "exchange": "", "country": "", "sector": "", "industry": "",
                          "mcap_musd": 0}
        out.append(dict(r, priority="A (live triage call)"))
    rest = sorted((r for r in rows if r["symbol"] not in set(live) and r["mcap_musd"] * 1e6 >= MIN_MCAP),
                  key=lambda r: -r["mcap_musd"])
    out += [dict(r, priority="B") for r in rest]
    with open(UNIV_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["symbol", "name", "exchange", "country", "sector", "industry", "mcap_musd",
                                          "priority"])
        w.writeheader()
        w.writerows(out)
    return out


def load_universe():
    return list(csv.DictReader(open(UNIV_CSV, encoding="utf-8")))


def bbg(sym):
    return sym.strip() + " US Equity"


# ---------------------------------------------------------------- sheets
def title(ws, t, note):
    ws.cell(1, 1, t).font = Font(name=F, bold=True, size=12)
    ws.cell(2, 1, note).font = Font(name=F, italic=True, size=9)


def universe_sheet(wb, uni):
    ws = wb.create_sheet("Universe")
    title(ws, "Universe: %d US-listed stocks (priority A = live triage calls, then by market cap)" % len(uni),
          "Yellow = Bloomberg ticker: fix it here if a row shows '#N/A Invalid Security' (all sheets read it). "
          "Block = which 500-row block the stock is in on the S sheets and which H1 sheet it is on.")
    hdr = ["#", "Bloomberg ticker", "Symbol", "Name", "Exchange", "Country", "Sector (Nasdaq)", "Industry (Nasdaq)",
           "Mkt cap $M (list, 2026-11-04)", "Priority", "Block", "S-sheet rows"]
    for j, h in enumerate(hdr, 1):
        c = ws.cell(4, j, h)
        c.font = Font(name=F, bold=True)
        c.fill = GREY
    for i, r in enumerate(uni):
        row = 5 + i
        b = i // BLOCK + 1
        lo, hi = 5 + (b - 1) * BLOCK, min(4 + b * BLOCK, 4 + len(uni))
        vals = [i + 1, bbg(r["symbol"]), r["symbol"], r["name"], r["exchange"], r["country"], r["sector"],
                r["industry"], float(r["mcap_musd"] or 0), r["priority"], b, "%d-%d" % (lo, hi)]
        for j, v in enumerate(vals, 1):
            c = ws.cell(row, j, v)
            c.font = Font(name=F, size=9)
        ws.cell(row, 2).fill = YEL
        ws.cell(row, 9).number_format = "#,##0.0"
    for j, w in enumerate([6, 18, 9, 40, 13, 14, 20, 30, 12, 18, 7, 11], 1):
        ws.column_dimensions[L(j)].width = w
    ws.freeze_panes = "C5"


def snap_sheet(wb, spec, n):
    name, what, fields = spec
    ws = wb.create_sheet(name)
    title(ws, "%s: %s" % (name, what),
          "Live formulas. Row 3 = field (fix a wrong one there); row 4 = what it is; grey = override used.")
    ws.cell(3, 1, "Ticker").font = Font(name=F, bold=True)
    ws.cell(3, 2, "Name").font = Font(name=F, bold=True)
    for j, (fld, ov, lab, _use, ok) in enumerate(fields, 3):
        c = ws.cell(3, j, fld)
        c.font = Font(name=F, bold=True, size=9, color="C00000" if ok == "check" else "000000")
        c.fill = YEL
        d = ws.cell(4, j, lab + (" [check]" if ok == "check" else ""))
        d.font = Font(name=F, size=8)
        d.alignment = Alignment(wrap_text=True, vertical="top")
        if ov:
            d.fill = GREY
        ws.column_dimensions[L(j)].width = 14
    ws.row_dimensions[4].height = 48
    for i in range(n):
        r = 5 + i
        ws.cell(r, 1, "=Universe!B%d" % r).font = Font(name=F, size=9)
        ws.cell(r, 2, "=Universe!D%d" % r).font = Font(name=F, size=9)
        for j, (fld, ov, *_x) in enumerate(fields, 3):
            col = L(j)
            if ov:
                f = '=BDP($A%d,%s$3,"%s","%s")' % (r, col, ov[0], ov[1])
            else:
                f = "=BDP($A%d,%s$3)" % (r, col)
            ws.cell(r, j, f)
    ws.column_dimensions["A"].width = 18
    ws.column_dimensions["B"].width = 26
    ws.freeze_panes = "C5"
    return n * len(fields)


def hist_sheets(wb, spec, uni):
    prefix, fields, start, opts, top, per, what = spec
    periods = {"Y": 22, "Q": 47, "M": 262}[opts.split("Per=")[1][0]]   # 2004-2025 / 2015Q1-2026Q3 / 2005-01-2026-10
    tick = list(range(len(uni)))[: (top or len(uni))]
    k = len(fields)
    step = k + 2
    sheets, cells = [], 0
    for s0 in range(0, len(tick), per):
        idx = tick[s0:s0 + per]
        nm = "%s_%02d" % (prefix, s0 // per + 1)
        ws = wb.create_sheet(nm)
        title(ws, "%s: Universe rows %d-%d. %s" % (nm, idx[0] + 1, idx[-1] + 1, what),
              "Live formulas. Each stock = one block: dates in its first row, one row per field below (column B).")
        for b, ui in enumerate(idx):
            r = 4 + b * step
            ws.cell(r, 1, "=Universe!B%d" % (5 + ui)).font = Font(name=F, bold=True, size=9)
            ws.cell(r, 2, "date").font = Font(name=F, italic=True, size=8)
            for i, fld in enumerate(fields):
                ws.cell(r + 1 + i, 2, fld).font = Font(name=F, size=8)
            ws.cell(r, 3, '=BDH($A%d,$B%d:$B%d,"%s","",%s)' % (r, r + 1, r + k, start, opts))
        ws.column_dimensions["A"].width = 18
        ws.column_dimensions["B"].width = 30
        ws.freeze_panes = "C4"
        sheets.append(nm)
        cells += len(idx) * k * periods
    return sheets, cells


def bulk_sheet(wb, spec, uni):
    nm, forms, rows, top, what = spec
    ws = wb.create_sheet(nm)
    title(ws, "%s: first %d Universe rows. %s" % (nm, top, what),
          "Live formulas. Each stock has %d rows; a list longer than that is cut off (fine)." % rows)
    for b in range(min(top, len(uni))):
        r = 4 + b * rows
        ws.cell(r, 1, "=Universe!B%d" % (5 + b)).font = Font(name=F, bold=True, size=9)
        for j, (lab, pat) in enumerate(forms):
            c0 = 3 + j * 8
            ws.cell(r, c0 - 1 if j else 2, lab).font = Font(name=F, italic=True, size=8)
            ws.cell(r + 1, c0, pat.format(t="$A%d" % r))
    ws.column_dimensions["A"].width = 18
    ws.column_dimensions["B"].width = 24
    ws.freeze_panes = "A4"


def check_sheet(wb):
    ws = wb.create_sheet("Universe_Check")
    title(ws, "Universe_Check (optional): Russell 3000 members straight from Bloomberg",
          "Anything here that is missing from Universe can be pasted at the bottom "
          "of Universe column B (then extend the S sheets by copying the last row down).")
    for j, f in enumerate(["INDX_MEMBERS", "INDX_MEMBERS2", "INDX_MEMBERS3"]):
        ws.cell(4, 1 + 2 * j, "RAY Index %s" % f).font = Font(name=F, bold=True)
        ws.cell(5, 1 + 2 * j, '=BDS("RAY Index","%s")' % f)
        ws.column_dimensions[L(1 + 2 * j)].width = 18


def fields_sheet(wb):
    ws = wb.create_sheet("Fields")
    title(ws, "Fields: every Bloomberg field in this workbook and what it is for",
          "'check' = mnemonic not certain: if its column shows '#N/A Invalid Field', type FLDS <GO> on the terminal, "
          "search the description, and put the right mnemonic in row 3 of that column.")
    hdr = ["Sheet", "Field", "Override", "What it is", "Used for (screen / criterion)", "Mnemonic"]
    for j, h in enumerate(hdr, 1):
        c = ws.cell(4, j, h)
        c.font = Font(name=F, bold=True)
        c.fill = GREY
    r = 5
    for name, _w, fields in SNAPS:
        for fld, ov, lab, use, ok in fields:
            for j, v in enumerate([name, fld, ("%s=%s" % ov) if ov else "", lab, use, ok], 1):
                ws.cell(r, j, v).font = Font(name=F, size=9, color="C00000" if (j == 6 and ok == "check") else "000000")
            r += 1
    unsure = {"IS_SGA_EXPENSE", "CF_STOCK_BASED_COMPENSATION", "IS_DISCONTINUED_OPERATIONS", "IS_RD_EXPEND",
              "BS_GOODWILL"}
    for prefix, fields, start, opts, *_ in HISTS:
        for fld in fields:
            for j, v in enumerate([prefix + "_*", fld, opts.replace('"', ""), "history from %s" % start,
                                   "see the sheet description", "check" if fld in unsure else "yes"], 1):
                ws.cell(r, j, v).font = Font(name=F, size=9)
            r += 1
    for nm, forms, *_ in BULKS:
        for lab, pat in forms:
            for j, v in enumerate([nm, pat.split('"')[1], "", lab, "human / AI review", "check"], 1):
                ws.cell(r, j, v).font = Font(name=F, size=9)
            r += 1
    for j, w in enumerate([18, 32, 30, 44, 70, 10], 1):
        ws.column_dimensions[L(j)].width = w
    ws.freeze_panes = "A5"


def readme(wb, n, counts, hist, n_blocks):
    ws = wb.active
    ws.title = "README"
    tot = sum(counts.values()) + sum(c for _s, c in hist.values())
    lines = [
        ("Bloomberg equities pull v1 (2026-11-04): every US-listed stock our screens can touch (%d stocks)" % n, "h"),
        ("Private: Bloomberg data stays on your computer (never GitHub). Check UBC's Bloomberg rules on exporting data.", ""),
        ("", ""),
        ("AT THE TERMINAL", "b"),
        ("1. Log in to Bloomberg, open this file in Excel (Bloomberg tab in the ribbon).", ""),
        ("2. Bloomberg tab -> Refresh -> Refresh Workbook. Wait until no cell shows 'Requesting Data...' (can take long).", ""),
        ("3. File -> Save As Bloomberg_equities_UBC.xlsx (USB or OneDrive). If offered, also save a copy with", ""),
        ("   Bloomberg -> Convert to values (or Copy -> Paste Special -> Values per sheet) so it opens without the terminal.", ""),
        ("4. At home put it in Documents\\Screenerdata\\bloomberg (NOT Screenerdata\\data) and tell Claude.", ""),
        ("", ""),
        ("IF SOMETHING SHOWS", "b"),
        ("'#N/A Limit' / 'Daily capacity reached' = download allowance used up: save; the rest fills on the next visit.", ""),
        ("'#N/A Invalid Field' down a column = mnemonic wrong (red ones are uncertain): FLDS <GO>, fix row 3 of that column.", ""),
        ("'#N/A Invalid Security' = fix the yellow ticker in Universe column B. '#N/A N/A' = no data (fine).", ""),
        ("'#NAME?' = Bloomberg add-in not loaded when the file opened: Bloomberg tab -> Refresh Workbook again.", ""),
        ("", ""),
        ("WHAT IS IN IT (most useful first)", "b"),
        ("Rows: live triage calls first (priority A), then by market cap, so a partial pull still covers what matters.", ""),
    ]
    order = [
        ("1", "S2_Market", "price, liquidity, market cap, 52-week high, short interest, implied vol"),
        ("2", "S3_Valuation_LTM", "EV multiples, last-12-month figures, balance sheet, leverage"),
        ("3", "S1_Identity", "IDs, industry codes, IPO date, report dates, ADR ratio"),
        ("4", "S5_Estimates", "consensus estimates, targets, ratings"),
        ("5", "H1_Annual_01, _02 ...", "annual history 2004+ (one sheet per 500 stocks, priority order)"),
        ("6", "S4_LastFY", "latest fiscal year detail, ROIC, SBC, R&D, discontinued ops"),
        ("7", "S6_Owners_Credit", "insider/institutional %, ratings, default probability"),
        ("8", "H2_Quarterly_01, _02", "quarterly history 2015+ (top 1,000)"),
        ("9", "B1-B4", "holders, dividends + spin-offs, segments, earnings dates (top 300)"),
        ("10", "H3_Monthly_01", "monthly prices, total return, consensus history (top 500) - heaviest per stock"),
        ("11", "Universe_Check", "optional: Russell 3000 list from Bloomberg to spot missing stocks"),
    ]
    r = 1
    for t, kind in lines:
        c = ws.cell(r, 1, t)
        c.font = Font(name=F, bold=kind in ("h", "b"), size=12 if kind == "h" else 10)
        r += 1
    for j, h in enumerate(["#", "Sheet", "What", "Data points (approx.)"], 1):
        c = ws.cell(r, j, h)
        c.font = Font(name=F, bold=True)
        c.fill = GREY
    r += 1
    size = dict(counts)
    for k, (sheets, cnt) in hist.items():
        size[k] = cnt
    sz = {"S2_Market": size["S2_Market"], "S3_Valuation_LTM": size["S3_Valuation_LTM"],
          "S1_Identity": size["S1_Identity"], "S5_Estimates": size["S5_Estimates"],
          "H1_Annual_01, _02 ...": size["H1_Annual"], "S4_LastFY": size["S4_LastFY"],
          "S6_Owners_Credit": size["S6_Owners_Credit"], "H2_Quarterly_01, _02": size["H2_Quarterly"],
          "B1-B4": 300 * 4 * 25, "H3_Monthly_01": size["H3_Monthly"], "Universe_Check": 3000}
    for num, sh, what in order:
        for j, v in enumerate([num, sh, what, sz.get(sh, 0)], 1):
            c = ws.cell(r, j, v)
            c.font = Font(name=F, size=10)
            if j == 4:
                c.number_format = "#,##0"
        r += 1
    r += 1
    more = [
        ("History data points count fields x periods (annual 22, quarterly ~47, monthly ~262). Bloomberg does not publish", ""),
        ("exact limits; the whole workbook (~%s data points) will likely take more than one visit. Sheets 1-4 first." % format(tot, ","), ""),
        ("", ""),
        ("LEGEND", "b"),
        ("Yellow cell = you may edit (Universe ticker; field mnemonic in row 3). Red mnemonic = not certain, verify with FLDS.", ""),
        ("Grey description = the formula uses an override (USD financials: EQY_FUND_CRNCY=USD; estimates: BEST_FPERIOD_OVERRIDE).", ""),
        ("A cell looks like:  =BDP($A5,C$3)  -> returns the field in row 3 for the ticker in column A.", ""),
        ("History block (H sheets): row 1 of each stock = period-end dates across, then one row per field (names in column B).", ""),
        ("History is Bloomberg's current (restated) figures, not as first reported; fine for 10-year screens, noted for backtests.", ""),
        ("", ""),
        ("WHAT THIS FILLS IN THAT WE CANNOT GET NOW", "b"),
        ("ADR market caps and ordinary shares per ADR; insider ownership (Owner-Operators); short interest (Red Flags);", ""),
        ("fundamentals before 2009 (Fortress 2009 test, Core downturn years); forward estimates and their monthly history;", ""),
        ("implied volatility (no OptionMetrics on WRDS); credit ratings; segments; spin-off dates; IDs to match everything.", ""),
        ("Universe source: NYSE/Nasdaq/NYSE American listings (Nasdaq screener, mirrored on GitHub rreichel3/US-Stock-Symbols,", ""),
        ("2026-11-04), minus warrants/rights/units/preferreds/notes/funds/SPACs and market cap < $25M; %d blocks of %d." % (n_blocks, BLOCK), ""),
    ]
    for t, kind in more:
        ws.cell(r, 1, t).font = Font(name=F, bold=kind == "b", size=10)
        r += 1
    ws.column_dimensions["A"].width = 6
    ws.column_dimensions["B"].width = 26
    ws.column_dimensions["C"].width = 80
    ws.column_dimensions["D"].width = 20


def main(argv):
    small = None
    out = os.path.join(HERE, "Bloomberg_equities_UBC.xlsx")
    args = list(argv)
    if "--universe-json" in args:
        i = args.index("--universe-json")
        ledger = os.path.join(args[i + 1], "ledger.csv")
        make_universe(args[i + 1], ledger)
        del args[i:i + 2]
    if "--small" in args:
        i = args.index("--small")
        small = int(args[i + 1])
        del args[i:i + 2]
    if args:
        out = args[0]
    uni = load_universe()
    if small:
        uni = uni[:small]
    n = len(uni)
    wb = Workbook()
    counts = {}
    universe_sheet(wb, uni)
    for spec in SNAPS:
        counts[spec[0]] = snap_sheet(wb, spec, n)
    hist = {}
    for spec in HISTS:
        hist[spec[0]] = hist_sheets(wb, spec, uni)
    for spec in BULKS:
        bulk_sheet(wb, spec, uni)
    check_sheet(wb)
    fields_sheet(wb)
    readme(wb, n, counts, hist, (n + BLOCK - 1) // BLOCK)
    wb.move_sheet("Fields", offset=-(len(wb.sheetnames) - 3))
    wb.save(out)
    print("saved", out, "stocks", n, "snapshot cells", sum(counts.values()),
          "history", {k: (len(s), c) for k, (s, c) in hist.items()}, "sheets", len(wb.sheetnames))


if __name__ == "__main__":
    main(sys.argv[1:])
