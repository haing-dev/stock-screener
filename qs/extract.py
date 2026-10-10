"""Turn SEC 'companyfacts' JSON into clean annual series, trailing-12-month figures and the latest balance
sheet, with full provenance.

Key rules (all visible in the output Evidence sheet):
  * Annual series use only facts from annual reports (10-K, 20-F, 40-F and amendments) covering 340-390 days.
  * The period is identified by its END DATE, not the filing's 'fy' field (a 10-K for FY2024 also contains
    FY2023 and FY2022 comparatives labelled fy=2024).
  * When several filings report the same period, the most recently filed value is used (picks up
    restatements); the first-reported value is kept for comparison.
  * Fiscal-year label = calendar year of the period end, or the prior year if the period ends January-May
    (so Walmart's year to Jan-2025 is labelled 2024).
  * Trailing twelve months (TTM) = latest fiscal year + current year-to-date - prior-year year-to-date, all
    from 10-Q filings filed after that fiscal year, using the same XBRL tag as the annual figure. If there is
    no newer 10-Q (or the company files 20-F/40-F), TTM = the latest fiscal year.
"""
import math
import re
from collections import Counter, defaultdict
from datetime import date, timedelta

SUBSET_VERSION = 8   # 5: discontinued ops; 6: statement-model lines (Excel); 7: resource capex, pre-2018 securities, leases;
                     # 8: industry lines for the Excel model (impairments, exploration, benefits, cash reconciliation)
ANNUAL_FORMS = {"10-K", "10-K/A", "10-KT", "10-KT/A", "20-F", "20-F/A", "40-F", "40-F/A"}
QUARTERLY_FORMS = {"10-Q", "10-Q/A"}

G, I, D = "us-gaap", "ifrs-full", "dei"

# kind: duration (flow over the year) or instant (balance-sheet date)
# agg:  first = first tag in list order that has a value for that year
#       max   = largest value among the tags (guards against a tag that only covers part of revenue)
CONCEPTS = {
    # Revenue: 'Revenues' (the total line) wins when present; ASC 606 'RevenueFromContract...' can be GROSS of
    # rebates (Mastercard 2018-21: $21.8B vs $15.0B net), so taking the largest tag would be wrong.
    "revenue": {"kind": "duration", "agg": "first", "tags": [
        (G, "Revenues"), (G, "RevenueFromContractWithCustomerExcludingAssessedTax"),
        (G, "RevenueFromContractWithCustomerIncludingAssessedTax"), (G, "SalesRevenueNet"),
        (G, "SalesRevenueGoodsNet"), (G, "SalesRevenueServicesNet"), (G, "RevenuesNetOfInterestExpense"),
        (G, "RevenueMineralSales"), (G, "OilAndGasRevenue"), (G, "RealEstateRevenueNet"),
        (G, "HomeBuildingRevenue"), (G, "RegulatedAndUnregulatedOperatingRevenue"), (G, "ElectricUtilityRevenue"),
        (I, "Revenue"), (I, "RevenueFromContractsWithCustomers"), (I, "RevenueFromSaleOfGoods")]},
    "gross_profit": {"kind": "duration", "agg": "first", "tags": [(G, "GrossProfit"), (I, "GrossProfit")]},
    "cost_of_revenue": {"kind": "duration", "agg": "first", "tags": [
        (G, "CostOfRevenue"), (G, "CostOfGoodsAndServicesSold"), (G, "CostOfGoodsSold"),
        (G, "CostOfServices"), (G, "CostOfGoodsAndServiceExcludingDepreciationDepletionAndAmortization"),
        (G, "CostOfGoodsSoldExcludingDepreciationDepletionAndAmortization"), (I, "CostOfSales")]},
    "sga": {"kind": "duration", "agg": "first", "tags": [
        (G, "SellingGeneralAndAdministrativeExpense"), (G, "GeneralAndAdministrativeExpense"),
        (I, "SellingGeneralAndAdministrativeExpense"), (I, "AdministrativeExpense")]},
    "operating_income": {"kind": "duration", "agg": "first", "tags": [
        (G, "OperatingIncomeLoss"), (I, "ProfitLossFromOperatingActivities")]},
    "costs_and_expenses": {"kind": "duration", "agg": "first", "tags": [(G, "CostsAndExpenses")]},
    "eps_diluted": {"kind": "duration", "agg": "first", "unit": "per_share", "tags": [
        (G, "EarningsPerShareDiluted"), (G, "EarningsPerShareBasicAndDiluted"), (I, "DilutedEarningsLossPerShare"),
        (I, "BasicAndDilutedEarningsLossPerShare")]},
    "pretax_income": {"kind": "duration", "agg": "first", "tags": [
        (G, "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest"),
        (G, "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"),
        (G, "IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic"),
        (I, "ProfitLossBeforeTax")]},
    "nonoperating_income": {"kind": "duration", "agg": "first", "tags": [
        (G, "NonoperatingIncomeExpense"), (G, "OtherNonoperatingIncomeExpense")]},
    "income_tax": {"kind": "duration", "agg": "first", "tags": [
        (G, "IncomeTaxExpenseBenefit"), (I, "IncomeTaxExpenseContinuingOperations")]},
    "net_income": {"kind": "duration", "agg": "first", "tags": [
        (G, "NetIncomeLoss"), (G, "ProfitLoss"), (G, "NetIncomeLossAvailableToCommonStockholdersBasic"),
        (I, "ProfitLossAttributableToOwnersOfParent"), (I, "ProfitLoss")]},
    "ocf": {"kind": "duration", "agg": "first", "tags": [
        (G, "NetCashProvidedByUsedInOperatingActivities"),
        (G, "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"),
        (I, "CashFlowsFromUsedInOperatingActivities")]},
    # largest tag wins: a narrow line (office equipment) listed first must not beat total capex (Range Resources)
    "capex_ppe": {"kind": "duration", "agg": "max", "tags": [
        (G, "PaymentsToAcquirePropertyPlantAndEquipment"), (G, "PaymentsToAcquireProductiveAssets"),
        (G, "PaymentsToAcquireOtherPropertyPlantAndEquipment"), (G, "PaymentsForCapitalImprovements"),
        (G, "PaymentsToAcquireMachineryAndEquipment"), (G, "PaymentsForProceedsFromProductiveAssets"),
        (G, "PaymentsToAcquireOilAndGasPropertyAndEquipment"), (G, "PaymentsToExploreAndDevelopOilAndGasProperties"),
        (G, "PaymentsToAcquireOilAndGasProperty"), (G, "PaymentsToAcquireMiningAssets"),
        (G, "PaymentsForConstructionInProcess"), (G, "PaymentsToAcquireTimberlands"),
        (I, "PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"),
        (I, "PurchaseOfPropertyPlantAndEquipment"),
        (I, "PurchaseOfPropertyPlantAndEquipmentIntangibleAssetsOtherThanGoodwillInvestmentPropertyAndOtherNoncurrentAssets")]},
    "capex_software": {"kind": "duration", "agg": "first", "tags": [
        (G, "PaymentsToDevelopSoftware"), (G, "PaymentsForSoftware"), (G, "PaymentsToAcquireSoftware"),
        (G, "PaymentsToAcquireIntangibleAssets"),
        (I, "PurchaseOfIntangibleAssetsClassifiedAsInvestingActivities")]},
    "acquisitions": {"kind": "duration", "agg": "first", "tags": [
        (G, "PaymentsToAcquireBusinessesNetOfCashAcquired"), (G, "PaymentsToAcquireBusinessesGross"),
        (I, "CashFlowsUsedInObtainingControlOfSubsidiariesOrOtherBusinessesClassifiedAsInvestingActivities")]},
    "buybacks": {"kind": "duration", "agg": "first", "tags": [
        (G, "PaymentsForRepurchaseOfCommonStock"), (I, "PaymentsToAcquireOrRedeemEntitysShares")]},
    "dividends": {"kind": "duration", "agg": "first", "tags": [
        (G, "PaymentsOfDividends"), (G, "PaymentsOfDividendsCommonStock"),
        (I, "DividendsPaidClassifiedAsFinancingActivities"), (I, "DividendsPaid")]},
    "equity_issued": {"kind": "duration", "agg": "first", "tags": [
        (G, "ProceedsFromIssuanceOfCommonStock"), (G, "ProceedsFromIssuanceOrSaleOfEquity"),
        (I, "ProceedsFromIssuingShares")]},
    "sbc": {"kind": "duration", "agg": "first", "tags": [
        (G, "ShareBasedCompensation"), (G, "AllocatedShareBasedCompensationExpense"),
        (I, "AdjustmentsForSharebasedPayments")]},
    # largest wins: 'ResearchAndDevelopmentExpense' can hold only acquired in-process R&D (J&J from 2021)
    "rnd": {"kind": "duration", "agg": "max", "tags": [
        (G, "ResearchAndDevelopmentExpense"), (G, "ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost"),
        (I, "ResearchAndDevelopmentExpense")]},
    # largest wins: 'DepreciationAndAmortization' can be a small sub-line (Intel 2015-19: $0.2B vs ~$8B)
    "da": {"kind": "duration", "agg": "max", "tags": [
        (G, "DepreciationDepletionAndAmortization"), (G, "DepreciationAndAmortization"),
        (G, "DepreciationAmortizationAndAccretionNet"), (G, "DepreciationAmortizationAndOther"),
        (G, "Depreciation"),
        (I, "AdjustmentsForDepreciationAndAmortisationExpense"), (I, "DepreciationAndAmortisationExpense")]},
    "interest_expense": {"kind": "duration", "agg": "first", "tags": [
        (G, "InterestExpense"), (G, "InterestExpenseNonoperating"), (G, "InterestExpenseDebt"),
        (G, "InterestAndDebtExpense"), (I, "InterestExpense"), (I, "FinanceCosts")]},
    "interest_paid": {"kind": "duration", "agg": "first", "tags": [
        (G, "InterestPaidNet"), (G, "InterestPaid"), (I, "InterestPaidClassifiedAsOperatingActivities"),
        (I, "InterestPaidClassifiedAsFinancingActivities")]},
    "reorganization_items": {"kind": "duration", "agg": "first", "tags": [(G, "ReorganizationItems")]},
    # discontinued operations (a unit sold or spun off): marks spin-off parents and divestitures (Hidden Earnings)
    "disc_ops": {"kind": "duration", "agg": "first", "tags": [
        (G, "IncomeLossFromDiscontinuedOperationsNetOfTax"),
        (G, "IncomeLossFromDiscontinuedOperationsNetOfTaxAttributableToReportingEntity"),
        (G, "DiscontinuedOperationIncomeLossFromDiscontinuedOperationNetOfTax"),
        (G, "IncomeLossFromDiscontinuedOperationsNetOfTaxIncludingPortionAttributableToNoncontrollingInterest"),
        (G, "DiscontinuedOperationIncomeLossFromDiscontinuedOperationBeforeIncomeTax"),
        (G, "IncomeLossFromDiscontinuedOperationsBeforeIncomeTax"),
        (I, "ProfitLossFromDiscontinuedOperations")]},
    "disc_ops_revenue": {"kind": "duration", "agg": "first", "tags": [
        (G, "DisposalGroupIncludingDiscontinuedOperationRevenue"), (I, "RevenueFromDiscontinuedOperations")]},
    "diluted_shares": {"kind": "duration", "agg": "first", "unit": "shares", "tags": [
        (G, "WeightedAverageNumberOfDilutedSharesOutstanding"),
        (G, "WeightedAverageNumberOfSharesOutstandingBasic"),
        (I, "AdjustedWeightedAverageShares"), (I, "WeightedAverageShares")]},
    # balance sheet
    "assets": {"kind": "instant", "agg": "first", "tags": [(G, "Assets"), (I, "Assets")]},
    "assets_current": {"kind": "instant", "agg": "first", "tags": [(G, "AssetsCurrent"), (I, "CurrentAssets")]},
    "liabilities_current": {"kind": "instant", "agg": "first", "tags": [
        (G, "LiabilitiesCurrent"), (I, "CurrentLiabilities")]},
    "ppe_net": {"kind": "instant", "agg": "first", "tags": [
        (G, "PropertyPlantAndEquipmentNet"),
        (G, "PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization"),
        (I, "PropertyPlantAndEquipment")]},
    "equity": {"kind": "instant", "agg": "first", "tags": [
        (G, "StockholdersEquity"), (G, "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"),
        (I, "EquityAttributableToOwnersOfParent"), (I, "Equity")]},
    "minority_interest": {"kind": "instant", "agg": "first", "tags": [
        (G, "MinorityInterest"), (I, "NoncontrollingInterests")]},
    "preferred_equity": {"kind": "instant", "agg": "first", "tags": [
        (G, "PreferredStockValue"), (G, "TemporaryEquityCarryingAmountAttributableToParent")]},
    "cash": {"kind": "instant", "agg": "first", "tags": [
        (G, "CashAndCashEquivalentsAtCarryingValue"),
        (G, "CashAndCashEquivalentsAtFairValue"), (G, "Cash"),
        (G, "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"),
        (I, "CashAndCashEquivalents")]},
    "cash_and_sti_combined": {"kind": "instant", "agg": "first", "tags": [
        (G, "CashCashEquivalentsAndShortTermInvestments"), (I, "CashAndCashEquivalentsAndShorttermInvestments")]},
    "st_investments": {"kind": "instant", "agg": "first", "tags": [
        (G, "ShortTermInvestments"), (G, "MarketableSecuritiesCurrent"), (G, "AvailableForSaleSecuritiesCurrent"),
        (G, "AvailableForSaleSecuritiesDebtSecuritiesCurrent"), (G, "HeldToMaturitySecuritiesCurrent"),
        (I, "ShorttermDepositsNotClassifiedAsCashEquivalents"), (I, "CurrentInvestments")]},
    "lt_investments": {"kind": "instant", "agg": "first", "tags": [
        (G, "MarketableSecuritiesNoncurrent"), (G, "AvailableForSaleSecuritiesDebtSecuritiesNoncurrent"),
        (G, "AvailableForSaleSecuritiesNoncurrent"), (G, "LongTermInvestments"),
        (G, "HeldToMaturitySecuritiesNoncurrent")]},
    "debt_combined": {"kind": "instant", "agg": "first", "tags": [
        (G, "DebtLongtermAndShorttermCombinedAmount"), (I, "Borrowings")]},
    "lt_debt_incl_current": {"kind": "instant", "agg": "first", "tags": [
        (G, "LongTermDebt"), (G, "LongTermDebtAndCapitalLeaseObligationsIncludingCurrentMaturities")]},
    "lt_debt_noncurrent": {"kind": "instant", "agg": "first", "tags": [
        (G, "LongTermDebtNoncurrent"), (G, "LongTermDebtAndCapitalLeaseObligations"),
        (G, "ConvertibleNotesPayableNoncurrent"), (G, "SeniorNotesNoncurrent"),
        (I, "NoncurrentPortionOfNoncurrentBorrowings"), (I, "LongtermBorrowings")]},
    "debt_current": {"kind": "instant", "agg": "first", "tags": [
        (G, "DebtCurrent"), (G, "LongTermDebtAndCapitalLeaseObligationsCurrent"),
        (I, "CurrentBorrowingsAndCurrentPortionOfNoncurrentBorrowings")]},
    "lt_debt_current": {"kind": "instant", "agg": "first", "tags": [
        (G, "LongTermDebtCurrent"), (I, "CurrentPortionOfNoncurrentBorrowings")]},
    "st_borrowings": {"kind": "instant", "agg": "first", "tags": [
        (G, "ShortTermBorrowings"), (G, "LinesOfCreditCurrent"), (G, "ShortTermBankLoansAndNotesPayable"),
        (G, "OtherShortTermBorrowings"), (G, "NotesPayableCurrent"), (I, "ShorttermBorrowings"),
        (I, "CurrentBorrowings")]},
    "commercial_paper": {"kind": "instant", "agg": "first", "tags": [(G, "CommercialPaper")]},
    # IFRS filers often show bonds on their own line, separate from bank borrowings (e.g. TSMC)
    "ifrs_bonds_noncurrent": {"kind": "instant", "agg": "first", "tags": [
        (I, "NoncurrentPortionOfNoncurrentBondsIssued"), (I, "NoncurrentBondsIssued"), (I, "BondsIssued")]},
    "ifrs_bonds_current": {"kind": "instant", "agg": "first", "tags": [
        (I, "CurrentPortionOfNoncurrentBondsIssued"), (I, "CurrentBondsIssuedAndCurrentPortionOfNoncurrentBondsIssued")]},
    "convertible_debt": {"kind": "instant", "agg": "first", "tags": [
        (G, "ConvertibleNotesPayable"), (G, "ConvertibleDebtNoncurrent"), (G, "ConvertibleLongTermNotesPayable"),
        (G, "ConvertibleDebt"), (G, "ConvertibleNotesPayableCurrent")]},
    # largest wins: notes, loans and credit lines are often tagged separately (Toll Brothers: secured debt $0.2B vs
    # $2.3B on the line-of-credit tag)
    "other_debt": {"kind": "instant", "agg": "max", "tags": [
        (G, "LongTermNotesPayable"), (G, "NotesPayable"), (G, "LongTermLoansPayable"), (G, "SecuredDebt"),
        (G, "UnsecuredDebt"), (G, "OtherLongTermDebtNoncurrent"), (G, "LongTermLineOfCredit"), (G, "LineOfCredit"),
        (G, "SeniorLongTermNotes"), (G, "OtherLongTermDebt"), (G, "SeniorNotes"), (G, "UnsecuredLongTermDebt"),
        (G, "SecuredLongTermDebt"), (G, "SubordinatedDebt"), (G, "SeniorSubordinatedNotes"), (G, "LoansPayable"),
        (G, "DebtInstrumentCarryingAmount")]},
    "liabilities_subject_to_compromise": {"kind": "instant", "agg": "first", "tags": [
        (G, "LiabilitiesSubjectToCompromise")]},
    "debt_due_1y": {"kind": "instant", "agg": "first", "tags": [
        (G, "LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths")]},
    "debt_due_2y": {"kind": "instant", "agg": "first", "tags": [
        (G, "LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo")]},
    "goodwill": {"kind": "instant", "agg": "first", "tags": [(G, "Goodwill"), (I, "Goodwill")]},
    "intangibles": {"kind": "instant", "agg": "first", "tags": [
        (G, "IntangibleAssetsNetExcludingGoodwill"), (G, "FiniteLivedIntangibleAssetsNet"),
        (I, "IntangibleAssetsOtherThanGoodwill")]},
    # restructuring charges (Red Flags: 'non-recurring' charges booked most years are ordinary costs)
    "restructuring": {"kind": "duration", "agg": "max", "tags": [
        (G, "RestructuringCharges"), (G, "RestructuringCosts"), (G, "RestructuringCostsAndAssetImpairmentCharges"),
        (G, "RestructuringSettlementAndImpairmentProvisions")]},
    "lease_rou": {"kind": "instant", "agg": "first", "tags": [(G, "OperatingLeaseRightOfUseAsset")]},
    "lease_liab_current": {"kind": "instant", "agg": "first", "tags": [(G, "OperatingLeaseLiabilityCurrent")]},
    "shares_outstanding_bs": {"kind": "instant", "agg": "first", "unit": "shares", "tags": [
        (G, "CommonStockSharesOutstanding"), (I, "NumberOfSharesOutstanding")]},
    # ---- statement-model lines (annual only; used by the Excel 3-statement model, never by a rule)
    "selling_marketing": {"kind": "duration", "agg": "first", "model": True, "tags": [
        (G, "SellingAndMarketingExpense"), (G, "SellingExpense"), (G, "MarketingAndAdvertisingExpense"),
        (I, "SellingExpense"), (I, "DistributionCosts")]},
    "general_admin": {"kind": "duration", "agg": "first", "model": True, "tags": [
        (G, "GeneralAndAdministrativeExpense"), (I, "AdministrativeExpense")]},
    "interest_income": {"kind": "duration", "agg": "first", "model": True, "tags": [
        (G, "InvestmentIncomeInterest"), (G, "InvestmentIncomeInterestAndDividend"),
        (G, "InterestIncomeOther"), (I, "FinanceIncome"), (I, "InterestRevenueExpense")]},
    "basic_shares": {"kind": "duration", "agg": "first", "unit": "shares", "model": True, "tags": [
        (G, "WeightedAverageNumberOfSharesOutstandingBasic"),
        (I, "WeightedAverageShares")]},
    "cfi": {"kind": "duration", "agg": "first", "model": True, "tags": [
        (G, "NetCashProvidedByUsedInInvestingActivities"),
        (G, "NetCashProvidedByUsedInInvestingActivitiesContinuingOperations"),
        (I, "CashFlowsFromUsedInInvestingActivities")]},
    "cff": {"kind": "duration", "agg": "first", "model": True, "tags": [
        (G, "NetCashProvidedByUsedInFinancingActivities"),
        (G, "NetCashProvidedByUsedInFinancingActivitiesContinuingOperations"),
        (I, "CashFlowsFromUsedInFinancingActivities")]},
    "debt_issued": {"kind": "duration", "agg": "first", "model": True, "tags": [
        (G, "ProceedsFromIssuanceOfLongTermDebt"), (G, "ProceedsFromIssuanceOfDebt"),
        (G, "ProceedsFromIssuanceOfSeniorLongTermDebt"), (G, "ProceedsFromConvertibleDebt"),
        (G, "ProceedsFromLongTermLinesOfCredit"),
        (I, "ProceedsFromBorrowingsClassifiedAsFinancingActivities"), (I, "ProceedsFromNoncurrentBorrowings")]},
    "debt_repaid": {"kind": "duration", "agg": "first", "model": True, "tags": [
        (G, "RepaymentsOfLongTermDebt"), (G, "RepaymentsOfDebt"), (G, "RepaymentsOfSeniorDebt"),
        (G, "RepaymentsOfConvertibleDebt"), (G, "RepaymentsOfLongTermLinesOfCredit"),
        (I, "RepaymentsOfBorrowingsClassifiedAsFinancingActivities"), (I, "RepaymentsOfNoncurrentBorrowings")]},
    "fx_effect": {"kind": "duration", "agg": "first", "model": True, "tags": [
        (G, "EffectOfExchangeRateOnCashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"),
        (G, "EffectOfExchangeRateOnCashAndCashEquivalents"),
        (I, "EffectOfExchangeRateChangesOnCashAndCashEquivalents")]},
    "accounts_receivable": {"kind": "instant", "agg": "first", "model": True, "tags": [
        (G, "AccountsReceivableNetCurrent"), (G, "ReceivablesNetCurrent"),
        (G, "AccountsNotesAndLoansReceivableNetCurrent"), (G, "AccountsReceivableNet"),
        (I, "TradeAndOtherCurrentReceivables"), (I, "CurrentTradeReceivables")]},
    "inventory": {"kind": "instant", "agg": "first", "model": True, "tags": [
        (G, "InventoryNet"), (G, "InventoryGross"), (I, "Inventories"), (I, "CurrentInventories")]},
    "accounts_payable": {"kind": "instant", "agg": "first", "model": True, "tags": [
        (G, "AccountsPayableCurrent"), (G, "AccountsPayableAndAccruedLiabilitiesCurrent"),
        (G, "AccountsPayableTradeCurrent"),
        (I, "TradeAndOtherCurrentPayables"), (I, "CurrentTradePayables")]},
    "accrued_liabilities": {"kind": "instant", "agg": "first", "model": True, "tags": [
        (G, "AccruedLiabilitiesCurrent"), (G, "EmployeeRelatedLiabilitiesCurrent")]},
    "deferred_revenue_current": {"kind": "instant", "agg": "first", "model": True, "tags": [
        (G, "ContractWithCustomerLiabilityCurrent"), (G, "DeferredRevenueCurrent"),
        (I, "CurrentContractLiabilities")]},
    "deferred_revenue_noncurrent": {"kind": "instant", "agg": "first", "model": True, "tags": [
        (G, "ContractWithCustomerLiabilityNoncurrent"), (G, "DeferredRevenueNoncurrent"),
        (I, "NoncurrentContractLiabilities")]},
    "liabilities": {"kind": "instant", "agg": "first", "model": True, "tags": [
        (G, "Liabilities"), (I, "Liabilities")]},
    "liabilities_and_equity": {"kind": "instant", "agg": "first", "model": True, "tags": [
        (G, "LiabilitiesAndStockholdersEquity"), (I, "EquityAndLiabilities")]},
    "retained_earnings": {"kind": "instant", "agg": "first", "model": True, "tags": [
        (G, "RetainedEarningsAccumulatedDeficit"), (I, "RetainedEarnings")]},
    # industry lines (v2.6): shown only when a company tags them
    "impairments": {"kind": "duration", "agg": "max", "model": True, "tags": [
        (G, "AssetImpairmentCharges"), (G, "GoodwillImpairmentLoss"), (G, "GoodwillAndIntangibleAssetImpairment"),
        (G, "ImpairmentOfLongLivedAssetsHeldForUse"), (G, "ImpairmentOfOilAndGasProperties"),
        (I, "ImpairmentLossRecognisedInProfitOrLoss")]},
    "exploration": {"kind": "duration", "agg": "first", "model": True, "tags": [
        (G, "ExplorationExpense"), (G, "ExplorationExpenseMining"), (I, "ExplorationAndEvaluationExpense")]},
    "benefits_expense": {"kind": "duration", "agg": "first", "model": True, "tags": [
        (G, "PolicyholderBenefitsAndClaimsIncurredNet"), (G, "PolicyholderBenefitsAndClaimsIncurredHealthCare")]},
    "premiums": {"kind": "duration", "agg": "first", "model": True, "tags": [
        (G, "PremiumsEarnedNet"), (G, "HealthCareOrganizationPremiumRevenue"), (I, "InsuranceRevenue")]},
    "cash_cf_end": {"kind": "instant", "agg": "first", "model": True, "tags": [
        (G, "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"),
        (I, "CashAndCashEquivalentsIfDifferentFromStatementOfFinancialPosition")]},
    "cash_change": {"kind": "duration", "agg": "first", "model": True, "tags": [
        (G, "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect"),
        (G, "CashAndCashEquivalentsPeriodIncreaseDecrease"),
        (I, "IncreaseDecreaseInCashAndCashEquivalents")]},
    "lease_liab_noncurrent": {"kind": "instant", "agg": "first", "model": True, "tags": [
        (G, "OperatingLeaseLiabilityNoncurrent")]},
}
MODEL_CONCEPTS = tuple(k for k, v in CONCEPTS.items() if v.get("model"))

# cover-page data (dei)
DEI_TAGS = {"EntityCommonStockSharesOutstanding": "shares", "EntityPublicFloat": "money"}

# concepts kept from 10-Q filings (for TTM and the latest balance sheet)
TTM_CONCEPTS = ("revenue", "gross_profit", "cost_of_revenue", "sga", "operating_income", "pretax_income",
                "income_tax", "net_income", "ocf", "capex_ppe", "capex_software", "da", "interest_expense",
                "interest_paid", "nonoperating_income", "reorganization_items", "diluted_shares",
                "costs_and_expenses", "eps_diluted", "disc_ops", "disc_ops_revenue")
BS_CONCEPTS = tuple(k for k, v in CONCEPTS.items() if v["kind"] == "instant" and not v.get("model"))
QUARTERLY_KEEP = set(TTM_CONCEPTS) | set(BS_CONCEPTS)
QUARTERLY_MAX_AGE_DAYS = 3 * 366

# When none of the listed tags exist, look for these patterns (us-gaap) and report the candidates in the
# 'Data gaps' sheet. For capex the first candidate is also USED (flagged), because capex tag names vary
# a lot and a missing capex would make free cash flow - and every cash test - fail.
FALLBACK_PATTERNS = {
    "capex_ppe": (re.compile(r"^PaymentsTo(Acquire|Purchase)\w*(PropertyPlant|ProductiveAssets|Equipment|"
                             r"CapitalExpenditure)\w*$"), True),
    "revenue": (re.compile(r"^\w*(Revenue|Revenues|Sales)\w*$"), False),
    "operating_income": (re.compile(r"^OperatingIncome\w*$"), False),
    "cost_of_revenue": (re.compile(r"^CostOf\w*$"), False),
    "ocf": (re.compile(r"^NetCashProvidedByUsedInOperatingActivities\w*$"), False),
    "lt_debt_noncurrent": (re.compile(r"^(?!\w*(Securities|Investment|Receivable|Interest|Maturit|FairValue|Proceeds|"
                                      r"Repayment|Payment|Issuance|Extinguishment|Amortization|Expense|Discount|"
                                      r"Premium|Rate|Covenant|Face|Conversion|Increase|Decrease|Gain|Loss))"
                                      r"\w*(Debt|Notes|Borrowing|LineOfCredit|LinesOfCredit|Loans)\w*$"), False),
}
# patterns that must not be reported as revenue candidates (costs, deferred revenue, receivables...)
REVENUE_CANDIDATE_EXCLUDE = re.compile(r"(Cost|Deferred|Receivable|Unbilled|Percentage|Expense|Tax|Remaining|"
                                       r"Performance|Recognized\w*Previously|Liability|Discount|Allowance)")

WANTED = {(tax, tag) for c in CONCEPTS.values() for tax, tag in c["tags"]}
WANTED_Q = {(tax, tag) for k, c in CONCEPTS.items() if k in QUARTERLY_KEEP for tax, tag in c["tags"]}
CURRENCY_HINT_CONCEPTS = ("revenue", "operating_income", "net_income", "assets")
FY_ANCHOR_CONCEPTS = ("revenue", "operating_income", "net_income", "ocf")
DATE_TOLERANCE_DAYS = 7

# filings that mark events for the Special Situations screen
EVENT_FORMS = {"10-12B", "10-12B/A", "10-12G", "10-12G/A", "S-1", "S-1/A", "F-1", "F-1/A", "424B4", "8-K",
               "8-K/A", "S-4", "S-4/A"}
EVENT_8K_ITEMS = {"1.03", "2.01", "5.02"}
EVENT_MAX_AGE_DAYS = 4 * 366


def _d(s):
    return date.fromisoformat(s[:10])


def fy_label(end):
    """Calendar year of the period end, or the prior year if it ends January-May. 52/53-week years that end in
    the first week of June (e.g. 'Saturday nearest May 31') are shifted back a week so they label like May."""
    d = _d(end) - timedelta(days=7)
    return d.year if d.month >= 6 else d.year - 1


# ---------------------------------------------------------------- subsets for cache
def submissions_subset(sub, today=None):
    """Keep only what the screens need from the (large) submissions JSON."""
    today = today or date.today()
    recent = (sub.get("filings") or {}).get("recent") or {}
    forms = recent.get("form") or []
    n = len(forms)

    def col(name):
        v = recent.get(name) or []
        return v if len(v) == n else list(v) + [""] * (n - len(v))
    accn, fdate, rdate, pdoc, items = (col("accessionNumber"), col("filingDate"), col("reportDate"),
                                       col("primaryDocument"), col("items"))
    latest = None
    n_annual = 0
    first_annual = None
    events = []
    latest_periodic = None
    cutoff = (today - timedelta(days=EVENT_MAX_AGE_DAYS)).isoformat()
    for i, form in enumerate(forms):
        if form in ("10-K", "10-Q", "20-F", "40-F", "10-K/A", "10-Q/A", "20-F/A", "40-F/A"):
            latest_periodic = max(latest_periodic or "", fdate[i] or "")
        if form in ("10-K", "20-F", "40-F"):
            n_annual += 1
            first_annual = fdate[i] or first_annual
            if latest is None:
                latest = {"form": form, "accn": accn[i], "filingDate": fdate[i], "reportDate": rdate[i],
                          "primaryDocument": pdoc[i]}
        if form in EVENT_FORMS and (fdate[i] or "") >= cutoff:
            its = [x.strip() for x in str(items[i] or "").split(",") if x.strip()]
            if form.startswith("8-K"):
                its = [x for x in its if x in EVENT_8K_ITEMS]
                if not its:
                    continue
            events.append({"form": form, "date": fdate[i], "accn": accn[i], "items": its,
                           "doc": pdoc[i]})
    older_pages = (sub.get("filings") or {}).get("files") or []
    return {
        "subset_version": SUBSET_VERSION,
        "cik": int(sub.get("cik") or 0),
        "name": sub.get("name"),
        "entityType": sub.get("entityType"),
        "sic": str(sub.get("sic") or ""),
        "sicDescription": sub.get("sicDescription") or "",
        "tickers": sub.get("tickers") or [],
        "exchanges": sub.get("exchanges") or [],
        "fiscalYearEnd": sub.get("fiscalYearEnd"),
        "category": sub.get("category") or "",
        "stateOfIncorporation": sub.get("stateOfIncorporation") or "",
        "latest_annual": latest,
        "latest_periodic_filing": latest_periodic,
        "n_recent_annual_reports": n_annual,
        "first_annual_in_recent": first_annual,
        "has_older_filing_pages": bool(older_pages),
        "events": events,
        "former_names": [f.get("name") for f in (sub.get("formerNames") or []) if f.get("name")],
    }


def facts_subset(cf, today=None):
    """Keep the concepts in CONCEPTS from annual reports, the TTM/balance-sheet concepts from recent 10-Qs,
    cover-page share counts, and candidate tags for concepts that are missing (see FALLBACK_PATTERNS)."""
    today = today or date.today()
    q_cutoff = (today - timedelta(days=QUARTERLY_MAX_AGE_DAYS)).isoformat()
    out = {"subset_version": SUBSET_VERSION, "cik": cf.get("cik"), "entityName": cf.get("entityName"),
           "facts": {}, "candidates": {}}
    facts = cf.get("facts") or {}

    def slim(e):
        return {k: e.get(k) for k in ("start", "end", "val", "accn", "fy", "fp", "form", "filed")}

    for tax, tags in facts.items():
        for tag, body in tags.items():
            key = (tax, tag)
            if tax == D and tag in DEI_TAGS:
                units = {}
                for unit, entries in (body.get("units") or {}).items():
                    keep = [slim(e) for e in entries if e.get("val") is not None and (e.get("end") or "") >= q_cutoff]
                    if keep:
                        units[unit] = keep
                if units:
                    out["facts"].setdefault(tax, {})[tag] = units
                continue
            if key not in WANTED:
                continue
            units = {}
            for unit, entries in (body.get("units") or {}).items():
                keep = []
                for e in entries:
                    if e.get("val") is None:
                        continue
                    f = e.get("form")
                    if f in ANNUAL_FORMS or (f in QUARTERLY_FORMS and key in WANTED_Q
                                             and (e.get("end") or "") >= q_cutoff):
                        keep.append(slim(e))
                if keep:
                    units[unit] = keep
            if units:
                out["facts"].setdefault(tax, {})[tag] = units

    # candidates for missing concepts
    present = {(tax, tag) for tax, tags in out["facts"].items() for tag in tags}
    gaap = facts.get(G) or {}
    for concept, (pat, use) in FALLBACK_PATTERNS.items():
        if any(t in present for t in CONCEPTS[concept]["tags"]):
            continue
        cands = []
        for tax in (G, I):
            for tag, body in (facts.get(tax) or {}).items():
                if not pat.match(tag) or (tax, tag) in WANTED:
                    continue
                if concept == "revenue" and REVENUE_CANDIDATE_EXCLUDE.search(tag):
                    continue
                annual = [e for unit, ents in (body.get("units") or {}).items() if len(unit) == 3
                          for e in ents if e.get("form") in ANNUAL_FORMS and e.get("val") is not None]
                if annual:
                    last = max(annual, key=lambda e: (e.get("end") or "", e.get("filed") or ""))
                    cands.append({"tag": tag if tax == G else f"{tax}:{tag}", "latest_end": last.get("end"),
                                  "latest_val": last.get("val"), "n_annual_facts": len(annual)})
        if cands:
            cands.sort(key=lambda c: (-c["n_annual_facts"], c["tag"]))
            out["candidates"][concept] = cands[:8]
            if use and ":" not in cands[0]["tag"]:
                tag = cands[0]["tag"]
                units = {}
                for unit, entries in (gaap[tag].get("units") or {}).items():
                    keep = [slim(e) for e in entries if e.get("val") is not None and (
                        e.get("form") in ANNUAL_FORMS or (e.get("form") in QUARTERLY_FORMS
                                                         and (e.get("end") or "") >= q_cutoff))]
                    if keep:
                        units[unit] = keep
                if units:
                    out["facts"].setdefault(G, {})[tag] = units
                    out.setdefault("fallback_tags", {})[concept] = tag
    return out


# ---------------------------------------------------------------- annual series
class Fact:
    __slots__ = ("concept", "val", "tax", "tag", "unit", "accn", "form", "filed", "start", "end",
                 "orig_val", "orig_accn", "fy_label")

    def __init__(self, concept, e, first, tax, tag, unit, label):
        self.concept, self.tax, self.tag, self.unit, self.fy_label = concept, tax, tag, unit, label
        self.val = float(e["val"])
        self.accn, self.form, self.filed = e.get("accn"), e.get("form"), e.get("filed")
        self.start, self.end = e.get("start"), e.get("end")
        self.orig_val = float(first["val"])
        self.orig_accn = first.get("accn")

    def as_row(self):
        return {"concept": self.concept, "fy": self.fy_label, "value": self.val, "unit": self.unit,
                "taxonomy": self.tax, "tag": self.tag, "period_start": self.start, "period_end": self.end,
                "form": self.form, "filed": self.filed, "accession": self.accn,
                "first_reported_value": self.orig_val, "first_reported_accession": self.orig_accn}


class DerivedFact:
    """A yearly figure computed from two reported ones (e.g. revenue = gross profit + cost of sales)."""
    def __init__(self, concept, val, how, base, label):
        self.concept, self.val, self.tax, self.tag, self.unit = concept, float(val), "derived", how, base.unit
        self.accn, self.form, self.filed = base.accn, base.form, base.filed
        self.start, self.end, self.fy_label = base.start, base.end, label
        self.orig_val, self.orig_accn = float(val), base.accn

    def as_row(self):
        return {"concept": self.concept, "fy": self.fy_label, "value": self.val, "unit": self.unit,
                "taxonomy": "derived", "tag": self.tag, "period_start": self.start, "period_end": self.end,
                "form": self.form, "filed": self.filed, "accession": self.accn,
                "first_reported_value": None, "first_reported_accession": None}


class Point:
    """A single derived value (TTM or latest balance sheet) with provenance."""
    __slots__ = ("concept", "val", "end", "method", "tag", "accns", "extra")

    def __init__(self, concept, val, end, method, tag, accns, extra=None):
        self.concept, self.val, self.end, self.method, self.tag, self.accns = concept, val, end, method, tag, accns
        self.extra = extra or {}

    def as_row(self):
        return {"concept": self.concept, "fy": "TTM" if self.method.startswith("TTM") or self.method == "FY"
                else "latest", "value": self.val, "unit": "", "taxonomy": "", "tag": self.tag,
                "period_start": None, "period_end": self.end, "form": self.method, "filed": None,
                "accession": ", ".join(a for a in self.accns if a), "first_reported_value": None,
                "first_reported_accession": None}


class CompanyData:
    def __init__(self, subset):
        self.facts = subset.get("facts") or {}
        self.entity_name = subset.get("entityName")
        self.candidates = subset.get("candidates") or {}
        self.fallback_tags = subset.get("fallback_tags") or {}
        self.flags = set()
        self.currency = self._detect_currency()
        self.taxonomies = sorted(k for k in self.facts.keys() if k != D)
        self.label_end = {}
        self.series = {}
        self.share_ratios = {}
        for concept, tag in self.fallback_tags.items():
            self.flags.add(f"{concept} taken from non-standard tag {tag} (check)")
        if self.currency:
            self._build()

    # -- helpers
    def _units(self, tax, tag):
        return (self.facts.get(tax) or {}).get(tag) or {}

    def _tags(self, concept):
        tags = list(CONCEPTS[concept]["tags"])
        fb = self.fallback_tags.get(concept)
        if fb:
            tags.append((G, fb))
        return tags

    def _detect_currency(self):
        counts = Counter()
        for c in CURRENCY_HINT_CONCEPTS:
            for tax, tag in CONCEPTS[c]["tags"]:
                for unit, ents in self._units(tax, tag).items():
                    if len(unit) == 3 and unit.isalpha() and unit.isupper():
                        counts[unit] += sum(1 for e in ents if e.get("form") in ANNUAL_FORMS)
        counts = Counter({k: v for k, v in counts.items() if v})
        if not counts:
            return None
        top = counts.most_common(2)
        if len(top) > 1 and top[1][1] >= 0.1 * top[0][1]:
            # a convenience translation (TSMC's USD figures) gives only the current year in each report; a real
            # change of reporting currency restates comparative years in the new currency too
            second = top[1][0]
            ends = defaultdict(set)
            for c in CURRENCY_HINT_CONCEPTS:
                for tax, tag in CONCEPTS[c]["tags"]:
                    for e in self._units(tax, tag).get(second) or []:
                        if e.get("form") in ANNUAL_FORMS:
                            ends[(tag, e.get("accn"))].add(e.get("end"))
            if any(len(v) > 1 for v in ends.values()):
                self.flags.add("multiple reporting currencies")
        return top[0][0]

    def _entries(self, tax, tag, unit_kind):
        units = self._units(tax, tag)
        if unit_kind == "shares":
            unit = "shares"
        elif unit_kind == "per_share":
            unit = f"{self.currency}/shares"
        else:
            unit = self.currency
        return unit, units.get(unit) or []

    @staticmethod
    def _pick(by_end, e):
        key = (e.get("filed") or "", e.get("accn") or "")
        k = e["end"]
        cur = by_end.get(k)
        if cur is None:
            by_end[k] = [key, e, key, e]  # latest_key, latest, first_key, first
        else:
            if key > cur[0]:
                cur[0], cur[1] = key, e
            if key < cur[2]:
                cur[2], cur[3] = key, e

    def _period_map(self, tax, tag, kind, unit_kind):
        unit, ents = self._entries(tax, tag, unit_kind)
        by_end = {}
        for e in ents:
            if not e.get("end") or e.get("form") not in ANNUAL_FORMS:
                continue
            if kind == "duration":
                if not e.get("start"):
                    continue
                try:
                    dur = (_d(e["end"]) - _d(e["start"])).days
                except ValueError:
                    continue
                if not 340 <= dur <= 390:
                    continue
            else:
                if e.get("start"):
                    continue
            self._pick(by_end, e)
        return unit, {k: (v[1], v[3]) for k, v in by_end.items()}

    def _label_for(self, end):
        lab = fy_label(end)
        anchor = self.label_end.get(lab)
        if anchor is None:
            return None
        if abs((_d(end) - _d(anchor)).days) <= DATE_TOLERANCE_DAYS:
            return lab
        return None

    # -- main build
    def _build(self):
        ends = set()
        for c in FY_ANCHOR_CONCEPTS:
            for tax, tag in self._tags(c):
                _, m = self._period_map(tax, tag, "duration", "money")
                ends.update(m.keys())
        for e in sorted(ends):
            lab = fy_label(e)
            prev = self.label_end.get(lab)
            if prev is None:
                self.label_end[lab] = e
            elif abs((_d(e) - _d(prev)).days) > DATE_TOLERANCE_DAYS:
                self.flags.add("fiscal year-end changed (check transition years)")
                self.label_end[lab] = max(prev, e)
            else:
                self.label_end[lab] = max(prev, e)

        rev_cands = {}
        for concept, spec in CONCEPTS.items():
            unit_kind = spec.get("unit", "money")
            per_label = {}
            for tax, tag in self._tags(concept):
                unit, m = self._period_map(tax, tag, spec["kind"], unit_kind)
                for end, (latest, first) in m.items():
                    lab = self._label_for(end)
                    if lab is None:
                        continue
                    f = Fact(concept, latest, first, tax, tag, unit, lab)
                    if concept == "revenue":
                        rev_cands.setdefault(lab, []).append(f)
                    cur = per_label.get(lab)
                    if cur is None:
                        per_label[lab] = f
                    elif spec["agg"] == "max" and f.val > cur.val:
                        per_label[lab] = f
                    # agg == first: keep the earlier tag in list order
            self.series[concept] = per_label
        self._rev_cands = rev_cands
        if rev_cands:
            self.series["revenue"] = self._select_revenue(rev_cands)
        else:
            self.series["revenue"] = self._derive_revenue()

        self._share_chain()
        self._quality_checks()

    def _share_chain(self):
        """Split-proof share-count change: compare years only WITHIN the same filing.

        A 10-K restates prior-year share counts for stock splits, so the ratio between
        two years taken from one filing is split-adjusted. Ratios are then chained.
        """
        for tax, tag in CONCEPTS["diluted_shares"]["tags"]:
            unit, ents = self._entries(tax, tag, "shares")
            by_accn = defaultdict(dict)
            filed = {}
            for e in ents:
                if not (e.get("start") and e.get("end") and e.get("accn")) or e.get("form") not in ANNUAL_FORMS:
                    continue
                try:
                    dur = (_d(e["end"]) - _d(e["start"])).days
                except ValueError:
                    continue
                if not 340 <= dur <= 390 or not e.get("val"):
                    continue
                lab = self._label_for(e["end"])
                if lab is None:
                    continue
                by_accn[e["accn"]][lab] = float(e["val"])
                filed[e["accn"]] = e.get("filed") or ""
            ratios = {}
            for accn in sorted(by_accn, key=lambda a: (filed[a], a)):  # later filings overwrite
                vals = by_accn[accn]
                for lab, v in vals.items():
                    p = vals.get(lab - 1)
                    if p and p > 0 and v > 0:
                        ratios[lab] = {"ratio": v / p, "accn": accn, "tag": tag}
            if ratios:
                self.share_ratios = ratios
                return

    def _select_revenue(self, cands):
        """One revenue figure per year when several revenue tags exist. Companies sometimes put a PART of revenue
        (a segment, 'other revenue', even zero) on the 'Revenues' tag in some years (Applied Industrial 2011-16:
        $21M vs $2.5B of sales; Flowserve: 'Revenues' = 0). So: the latest year uses the preferred tag unless it is
        under 20% of the largest candidate; earlier years keep the preferred tag unless it is more than 1.5x away
        from the following year's figure while another tag is closer (continuity)."""
        labs = sorted(cands)
        chosen = {}
        last = labs[-1]
        opts = cands[last]
        pick, mx = opts[0], max(opts, key=lambda f: f.val)
        if mx.val > 0 and pick.val <= 0.2 * mx.val:
            pick = mx
            self.flags.add(f"revenue: tag {opts[0].tag} is only a part of revenue in FY{last}; {mx.tag} used")
        chosen[last] = pick
        ref = pick
        swapped = []

        def agrees(tag, lab_ref, val_ref):
            # the candidate tag reports the (already chosen) later year within 5% of the chosen figure
            return any(f.tag == tag and val_ref and abs(f.val / val_ref - 1) <= 0.05 for f in cands.get(lab_ref, []))

        for lab in reversed(labs[:-1]):
            opts = cands[lab]
            pick = opts[0]
            if len(opts) > 1 and ref is not None and ref.val > 0:
                def dist(f, r=ref.val):
                    return abs(math.log(f.val / r)) if f.val > 0 else float("inf")
                if dist(pick) > math.log(1.5):
                    # switch only to a tag that is consistent with the later figure (the same tag, or one reporting
                    # that later year at the same value) - never to whatever partial line happens to be closest,
                    # so a genuine fall in revenue is not rewritten
                    ok = [f for f in opts if f.val > 0 and (f.tag == ref.tag or agrees(f.tag, ref.fy_label, ref.val))]
                    if ok:
                        best = min(ok, key=dist)
                        if dist(best) < dist(pick):
                            pick = best
                            swapped.append(lab)
            elif pick.val <= 0:
                pos = [f for f in opts if f.val > 0]
                if pos:
                    pick = pos[0]
            chosen[lab] = pick
            ref = pick
        self.revenue_tag_swaps = sorted(swapped)
        if swapped:
            self.flags.add(f"revenue: in {len(swapped)} year(s) ({min(swapped)}-{max(swapped)}) the preferred tag holds "
                           "only part of revenue - the tag consistent with later years is used (see Evidence)")
        return chosen

    def _derive_revenue(self):
        """No standard revenue tag at all (companies using their own revenue element, e.g. Novartis, Sanofi):
        revenue = gross profit + cost of sales, else operating income + total costs and expenses."""
        out = {}
        gp, cogs = self.series.get("gross_profit", {}), self.series.get("cost_of_revenue", {})
        oi, cx = self.series.get("operating_income", {}), self.series.get("costs_and_expenses", {})
        for lab in sorted(set(gp) | set(oi)):
            if lab in gp and lab in cogs and gp[lab].val + abs(cogs[lab].val) > 0:
                out[lab] = DerivedFact("revenue", gp[lab].val + abs(cogs[lab].val), "gross profit + cost of sales",
                                       gp[lab], lab)
            elif lab in oi and lab in cx and oi[lab].val + abs(cx[lab].val) > 0:
                out[lab] = DerivedFact("revenue", oi[lab].val + abs(cx[lab].val),
                                       "operating income + costs and expenses", oi[lab], lab)
        if out:
            how = sorted({f.tag for f in out.values()})
            self.flags.add("revenue not tagged with a standard revenue tag - derived as " + " / ".join(how))
        return out

    def rev_candidate(self, lab, tag):
        for f in (getattr(self, "_rev_cands", {}) or {}).get(lab, []):
            if f.tag == tag:
                return f.val
        return None

    def _quality_checks(self):
        rev = self.series.get("revenue", {})
        labs = sorted(rev)
        if not labs:
            return
        start = labs[-1] - 10       # jumps before the 10-year window don't affect any screen ...
        for a, b in zip(labs, labs[1:]):
            if b != a + 1 or (a <= start and not 2006 <= a <= 2010):   # ... except the 2008-09 recession test
                continue
            ra, rb = rev[a], rev[b]
            if ra.val > 0 and ra.tag != rb.tag:
                g = rb.val / ra.val - 1
                if g > 0.5 or g < -0.33:
                    alt = self.rev_candidate(a, rb.tag)     # does the new tag also report the earlier year?
                    if alt is not None and alt > 0 and abs(alt / ra.val - 1) < 0.05:
                        continue                            # both tags agree: the jump is real growth
                    if alt is None and -0.5 <= g <= 1.0:
                        continue                            # plausible growth, nothing contradicts it
                    self.flags.add(f"revenue jumps {g:+.0%} where tag changes ({a}->{b}); check consistency")

    def restated(self, concept, labels, tol):
        out = []
        for lab in labels:
            f = self.series.get(concept, {}).get(lab)
            if f and f.orig_val and abs(f.val - f.orig_val) / abs(f.orig_val) > tol:
                out.append(lab)
        return out

    def get(self, concept, lab):
        f = self.series.get(concept, {}).get(lab)
        return None if f is None else f.val

    def fact(self, concept, lab):
        return self.series.get(concept, {}).get(lab)

    # -- trailing twelve months & latest balance sheet
    def revenue_ratios(self):
        """{label: revenue(label) / revenue(label - 1)} taken from the latest annual report that shows both years
        under the tag chosen for that year. A report restates its comparative year after a spin-off or sale, so the
        ratio is like-for-like (J&J after Kenvue) where comparing figures from different reports is not."""
        if getattr(self, "_rev_ratios", None) is not None:
            return self._rev_ratios
        out, cache = {}, {}
        for lab, f in (self.series.get("revenue") or {}).items():
            if f.tax == "derived" or not f.tag:
                continue
            key = (f.tax, f.tag)
            if key not in cache:
                _, ents = self._entries(f.tax, f.tag, "money")
                by_accn, filed = defaultdict(dict), {}
                for e in ents:
                    if e.get("form") not in ANNUAL_FORMS or not (e.get("start") and e.get("end") and e.get("accn")):
                        continue
                    try:
                        dur = (_d(e["end"]) - _d(e["start"])).days
                    except ValueError:
                        continue
                    if not 340 <= dur <= 390 or e.get("val") is None:
                        continue
                    lb = self._label_for(e["end"])
                    if lb is not None:
                        by_accn[e["accn"]][lb] = float(e["val"])
                        filed[e["accn"]] = e.get("filed") or ""
                cache[key] = (by_accn, filed)
            by_accn, filed = cache[key]
            best = None
            for accn, vals in by_accn.items():
                a, b = vals.get(lab), vals.get(lab - 1)
                if a is not None and b and b > 0 and a >= 0:
                    k = (filed[accn], accn)
                    if best is None or k > best[0]:
                        best = (k, a / b)
            if best and 0.2 <= best[1] <= 5.0:
                out[lab] = best[1]
        self._rev_ratios = out
        return out

    def latest_fy(self):
        """Latest fiscal year with any anchor fact (revenue, operating income, net income or cash flow)."""
        return max(self.label_end) if self.label_end else None

    def _q_durations(self, tax, tag, unit_kind):
        """10-Q duration facts as {(start, end): latest-filed entry}."""
        unit, ents = self._entries(tax, tag, unit_kind)
        out = {}
        for e in ents:
            if e.get("form") not in QUARTERLY_FORMS or not e.get("start") or not e.get("end"):
                continue
            k = (e["start"][:10], e["end"][:10])
            cur = out.get(k)
            if cur is None or (e.get("filed") or "", e.get("accn") or "") > (cur.get("filed") or "", cur.get("accn") or ""):
                out[k] = e
        return out

    def ttm(self, concept):
        """Trailing twelve months for a flow concept, or the latest fiscal year if no newer 10-Q exists."""
        lab = self.latest_fy()
        if lab is None:
            return None
        fy_fact = self.fact(concept, lab)
        fy_end = self.label_end.get(lab)
        if fy_fact is None or fy_end is None:
            return None
        fy_end_d = _d(fy_end)
        if fy_fact.tax == "derived":
            parts = {"gross profit + cost of sales": ("gross_profit", "cost_of_revenue"),
                     "operating income + costs and expenses": ("operating_income", "costs_and_expenses")}.get(fy_fact.tag)
            if parts:
                a, b = self.ttm(parts[0]), self.ttm(parts[1])
                if a is not None and b is not None and a.end == b.end and a.method.split(" ")[0] == b.method.split(" ")[0]:
                    return Point(concept, a.val + abs(b.val), a.end, a.method + " (derived)", fy_fact.tag,
                                 a.accns + b.accns, a.extra and {k: (a.extra.get(k) or 0) + abs(b.extra.get(k) or 0)
                                                                  if k != "ytd_days" else a.extra.get(k)
                                                                  for k in a.extra})
            return Point(concept, fy_fact.val, fy_end, "FY", fy_fact.tag, [fy_fact.accn])
        tags = [(fy_fact.tax, fy_fact.tag)] + [t for t in self._tags(concept) if t[1] != fy_fact.tag]
        unit_kind = CONCEPTS[concept].get("unit", "money")
        main_q = self._q_durations(fy_fact.tax, fy_fact.tag, unit_kind) if fy_fact.tax != "derived" else {}
        for tax, tag in tags:
            q = self._q_durations(tax, tag, unit_kind)
            if not q:
                continue
            if tag != fy_fact.tag:
                # another tag's year-to-date figures are only used if that tag measures the same thing: it reports
                # the same fiscal-year total, or the same prior-year year-to-date figure as the main tag (a company
                # that switched tags in its newest 10-Qs)
                unit, m = self._period_map(tax, tag, "duration", unit_kind)
                same = [v[0] for e2, v in m.items() if abs((_d(e2) - fy_end_d).days) <= DATE_TOLERANCE_DAYS]
                consistent = bool(same and fy_fact.val and abs(float(same[0]["val"]) / fy_fact.val - 1) <= 0.02)
                if not consistent:
                    for k, v in q.items():
                        mv = main_q.get(k)
                        if mv is not None and float(mv["val"]) and abs(float(v["val"]) / float(mv["val"]) - 1) <= 0.02:
                            consistent = True
                            break
                if not consistent and not main_q and fy_fact.val:
                    # nothing to compare with (the main tag has no 10-Q figures at all): accept the 10-Q tag if its
                    # prior-year year-to-date figure is a plausible share of that fiscal year's total (a partial line
                    # such as one segment would be far too small)
                    for (ps, pe), v in q.items():
                        try:
                            in_fy = _d(ps) > fy_end_d - timedelta(days=380) and _d(pe) <= fy_end_d + timedelta(days=10)
                            days = (_d(pe) - _d(ps)).days
                        except ValueError:
                            continue
                        if in_fy and 80 <= days <= 300:
                            share, expect = float(v["val"]) / fy_fact.val, days / 365.0
                            if 0.5 * expect <= share <= 1.6 * expect:
                                consistent = True
                                break
                if not consistent:
                    continue
            # current year-to-date: starts right after the fiscal year end
            cur = [(s, e, v) for (s, e), v in q.items()
                   if abs((_d(s) - fy_end_d).days - 1) <= 10 and _d(e) > fy_end_d]
            if not cur:
                continue
            s, e, ce = max(cur, key=lambda x: x[1])
            dur = (_d(e) - _d(s)).days
            if not 80 <= dur <= 300:
                continue
            # prior-year comparative with the same length, one year earlier
            prior = [v for (ps, pe), v in q.items()
                     if abs((_d(pe) - _d(e)).days + 365) <= 10 and abs((_d(pe) - _d(ps)).days - dur) <= 10]
            if not prior:
                # some filers tag the comparative only in the prior year's 10-Q
                continue
            pe = max(prior, key=lambda x: (x.get("filed") or ""))
            val = fy_fact.val + float(ce["val"]) - float(pe["val"])
            return Point(concept, val, e, f"TTM (FY{lab} + YTD to {e} - prior YTD)", tag,
                         [fy_fact.accn, ce.get("accn"), pe.get("accn")],
                         {"ytd_current": float(ce["val"]), "ytd_prior": float(pe["val"]), "ytd_days": dur})
        return Point(concept, fy_fact.val, fy_end, "FY", fy_fact.tag, [fy_fact.accn])

    def latest_instant(self, concept):
        """Most recent balance-sheet value from any annual report or 10-Q (latest date wins; for the same
        date the earlier tag in list order wins)."""
        best = None
        unit_kind = CONCEPTS[concept].get("unit", "money")
        for rank, (tax, tag) in enumerate(self._tags(concept)):
            unit, ents = self._entries(tax, tag, unit_kind)
            for e in ents:
                if e.get("start") or not e.get("end") or e.get("form") not in (ANNUAL_FORMS | QUARTERLY_FORMS):
                    continue
                key = (e["end"][:10], -rank, e.get("filed") or "")
                if best is None or key > best[0]:
                    best = (key, e, tag)
        if best is None:
            return None
        _, e, tag = best
        return Point(concept, float(e["val"]), e["end"][:10], f"balance sheet ({e.get('form')})", tag, [e.get("accn")])

    def latest_bs_date(self):
        p = self.latest_instant("assets")
        return p.end if p else None

    def bs_at(self, concept, end):
        """Balance-sheet value at a specific date (annual or 10-Q), used to keep the latest balance sheet
        internally consistent."""
        unit_kind = CONCEPTS[concept].get("unit", "money")
        for tax, tag in self._tags(concept):
            unit, ents = self._entries(tax, tag, unit_kind)
            hits = [e for e in ents if not e.get("start") and (e.get("end") or "")[:10] == end
                    and e.get("form") in (ANNUAL_FORMS | QUARTERLY_FORMS)]
            if hits:
                e = max(hits, key=lambda x: x.get("filed") or "")
                return Point(concept, float(e["val"]), end, f"balance sheet ({e.get('form')})", tag, [e.get("accn")])
        return None

    def dei_latest(self, tag):
        """Latest cover-page value. Companies with several share classes report one value per class in the same
        filing and date (the class dimension is dropped by the SEC API): those values are summed."""
        units = (self.facts.get(D) or {}).get(tag) or {}
        best = None
        for unit, ents in units.items():
            for e in ents:
                k = ((e.get("end") or "")[:10], e.get("filed") or "")
                if best is None or k > best[0]:
                    best = (k, e, unit)
        if best is None:
            return None
        _, e, unit = best
        same = {float(x["val"]) for x in units[unit]
                if (x.get("end") or "")[:10] == (e.get("end") or "")[:10] and x.get("accn") == e.get("accn")
                and x.get("val") is not None}
        val = sum(same) if tag == "EntityCommonStockSharesOutstanding" else float(e["val"])
        return {"val": val, "end": (e.get("end") or "")[:10], "unit": unit, "accn": e.get("accn"),
                "form": e.get("form"), "classes": len(same)}

    def dei_shares_near(self, day, max_days=150):
        """Cover-page shares outstanding from the filing whose cover date is closest to `day` (e.g. the public-float
        date), summed over share classes reported in that filing; None if none within max_days."""
        units = (self.facts.get(D) or {}).get("EntityCommonStockSharesOutstanding") or {}
        try:
            target = _d(day)
        except (TypeError, ValueError):
            return None
        best = None
        for unit, ents in units.items():
            for e in ents:
                try:
                    gap = abs((_d(e.get("end") or "") - target).days)
                except ValueError:
                    continue
                if gap <= max_days and (best is None or gap < best[0]):
                    best = (gap, e, unit)
        if best is None:
            return None
        _, e, unit = best
        # one entry per share class in the same filing and date (same summing as dei_latest)
        same = {float(x["val"]) for x in units[unit]
                if (x.get("end") or "")[:10] == (e.get("end") or "")[:10] and x.get("accn") == e.get("accn")
                and x.get("val") is not None}
        return {"val": sum(same), "end": (e.get("end") or "")[:10]}

    def latest_diluted_shares(self):
        """Weighted diluted shares from the latest period (10-Q quarter/YTD or fiscal year)."""
        best = None
        for rank, (tax, tag) in enumerate(CONCEPTS["diluted_shares"]["tags"]):
            unit, ents = self._entries(tax, tag, "shares")
            for e in ents:
                if not e.get("start") or not e.get("end") or not e.get("val"):
                    continue
                k = (e["end"][:10], -rank, e.get("filed") or "")
                if best is None or k > best[0]:
                    best = (k, e, tag)
        if best is None:
            return None
        _, e, tag = best
        return Point("diluted_shares", float(e["val"]), e["end"][:10], f"weighted diluted ({e.get('form')})", tag,
                     [e.get("accn")], {"filed": (e.get("filed") or "")[:10]})
