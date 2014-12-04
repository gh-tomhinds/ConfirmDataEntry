from sikuli import *

import printARAgedBal
import printTkHistory
import printTkCC
import printFundsBal
import printHold
import printTaxes
import printTOWorksheet
import printFeeAlloc
import report_Budgets

#---------------------------------------------------#
def print_postbill_reports(month):
#---------------------------------------------------#

    # print various reports to check db values and calculations
    # this function is also called from ba__Main

    printARAgedBal.Print_ARAgedBal(month)
    printTkHistory.Print_TkHistory(month)
    printTkCC.Print_TkCC(month)
    printFundsBal.fPrint_FundsBal(month)
    printHold.Print_Hold(month)
    printTaxes.Print_Taxes(month)
    printTOWorksheet.Print_Worksheet(month)
    printFeeAlloc.Print_FeeAlloc(month)
    report_Budgets.printCliBudget(month)
    report_Budgets.printTkBudget(month)
    report_Budgets.printFirmBudget(month)
