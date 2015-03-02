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
import report_Statement
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

    csvExt = pAorB + ".csv"
    textExt = pAorB + ".txt"

    report_AgedARBal.Print_ARAgedBal(pMonth,csvExt)
    report_UDSlip.fPrint_SlipListDetailed(pMonth,csvExt)
    report_UDSlip.fPrint_SlipFields(pMonth,csvExt)
    report_UDClient.fPrint_ClientListHistory(pMonth,csvExt)
    report_UDFunds.fPrint_FundsListFields(pMonth,csvExt)
    report_UDInvoice.fPrint_InvoiceListFields(pMonth,csvExt)
    report_TkHistory.Print_TkHistory(pMonth,csvExt)
    report_TkCC.Print_TkCC(pMonth,csvExt)
    report_FundsBal.fPrint_FundsBal(pMonth,csvExt)
    report_Hold.Print_Hold(pMonth,csvExt)
    report_Taxes.Print_Taxes(pMonth,csvExt)
    report_TOWorksheet.Print_Worksheet(pMonth,csvExt)
    report_Budgets.printCliBudget(pMonth,csvExt)
    report_Budgets.printTkBudget(pMonth,csvExt)
    report_Budgets.printFirmBudget(pMonth,csvExt)
    report_ProdPeriod.print_ProdPeriod(pMonth,csvExt)
    report_ProfPeriod.print_ProfPeriod(pMonth,csvExt)
    report_Markup.print_Markup(pMonth,csvExt)
    report_SlipSummary.print_SlipSummary(pMonth,csvExt)
    report_Statement.fPrint_Statement(pMonth,txtExt)
    report_GLXfer.Print_GLXfer(pMonth,csvExt)

#    report_UDClient.fPrint_ClientListValues(pMonth,repExt)
#    report_DaysToPay.print_DaysToPay(pMonth,repExt)

    if (pMonth == 1) and (pAorB == "a"):        
        # fee allocation cannot be run without some payments entered
        logging.debug('SKIP FEE ALLOCATION REPORT')
        logging.debug('SKIP PAYMENT DISTR REPORT')        
    else:
        report_FeeAlloc.Print_FeeAlloc(pMonth,csvExt)
        report_PayDistr.Print_PayDistr(pMonth,csvExt)
