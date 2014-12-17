from sikuli import *

import report_AgedARBal
import report_TkHistory
import report_TkCC
import report_FundsBal
import report_Hold
import report_Taxes
import report_TOWorksheet
import report_FeeAlloc
import report_Budgets

#---------------------------------------------------#
def fPrint_PostbillReports(pMonth):
#---------------------------------------------------#

    # print various reports to check db values and calculations
    # this function is also called from ba__Main

    report_AgedARBal.Print_ARAgedBal(pMonth)
    report_TkHistory.Print_TkHistory(pMonth)
    report_TkCC.Print_TkCC(pMonth)
    report_FundsBal.fPrint_FundsBal(pMonth)
    report_Hold.Print_Hold(pMonth)
    report_Taxes.Print_Taxes(pMonth)
    report_TOWorksheet.Print_Worksheet(pMonth)
    report_FeeAlloc.Print_FeeAlloc(pMonth)
    report_Budgets.printCliBudget(pMonth)
    report_Budgets.printTkBudget(pMonth)
    report_Budgets.printFirmBudget(pMonth)
