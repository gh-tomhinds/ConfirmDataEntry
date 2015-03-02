from sikuli import *
import logging

import report_AgedARBal
import report_Budgets
import report_DaysToPay
import report_FeeAlloc
import report_FundsBal
import report_Hold
import report_PayDistr
import report_ProdPeriod
import report_ProfPeriod
import report_Markup
import report_SlipSummary
import report_Taxes
import report_TkCC
import report_TkHistory
import report_TOWorksheet
import report_UDSlip
import report_UDClient
import report_UDFunds
import report_UDInvoice
import report_GLXfer

#---------------------------------------------------#
def fPrint_PostbillReports(pMonth,pAorB):
#---------------------------------------------------#

    # print various reports to check db values and calculations

    repExt = pAorB + ".csv"

    report_AgedARBal.Print_ARAgedBal(pMonth,repExt)
    report_UDSlip.fPrint_SlipListDetailed(pMonth,repExt)    
    report_UDSlip.fPrint_SlipFields(pMonth,repExt)
    report_UDClient.fPrint_ClientListHistory(pMonth,repExt)
    report_UDFunds.fPrint_FundsListFields(pMonth,repExt)
    report_UDInvoice.fPrint_InvoiceListFields(pMonth,repExt)
    report_TkHistory.Print_TkHistory(pMonth,repExt)
    report_TkCC.Print_TkCC(pMonth,repExt)
    report_FundsBal.fPrint_FundsBal(pMonth,repExt)
    report_Hold.Print_Hold(pMonth,repExt)
    report_Taxes.Print_Taxes(pMonth,repExt)
    report_TOWorksheet.Print_Worksheet(pMonth,repExt)    
    report_Budgets.printCliBudget(pMonth,repExt)
    report_Budgets.printTkBudget(pMonth,repExt)
    report_Budgets.printFirmBudget(pMonth,repExt)
    report_ProdPeriod.print_ProdPeriod(pMonth,repExt)
    report_ProfPeriod.print_ProfPeriod(pMonth,repExt)
    report_Markup.print_Markup(pMonth,repExt)
    report_SlipSummary.print_SlipSummary(pMonth,repExt)
    report_GLXfer.Print_GLXfer(pMonth,repExt)

#    report_UDClient.fPrint_ClientListValues(pMonth,repExt)
#    report_DaysToPay.print_DaysToPay(pMonth,repExt)

    if (pMonth == 1) and (pAorB == "a"):        
        # fee allocation cannot be run without some payments entered
        logging.debug('SKIP FEE ALLOCATION REPORT')
        logging.debug('SKIP PAYMENT DISTR REPORT')        
    else:
        report_FeeAlloc.Print_FeeAlloc(pMonth,repExt)
        report_PayDistr.Print_PayDistr(pMonth,repExt)
