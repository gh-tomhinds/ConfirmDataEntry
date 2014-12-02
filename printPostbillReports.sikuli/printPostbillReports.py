from sikuli import *

import printARAgedBal
import printTkHistory
import printTkCC
import printFundsBal
import printHold
import printTaxes
import printTOWorksheet
import printFeeAlloc
import reportBudgets

#---------------------------------------------------#
def print_postbill_reports(month):
#---------------------------------------------------#

    # print various reports to check db values and calculations
    # this function is also called from ba__Main

    printARAgedBal.Print_ARAgedBal(month)
    printTkHistory.Print_TkHistory(month)
    printTkCC.Print_TkCC(month)
    printFundsBal.Print_FundsBal(month)
    printHold.Print_Hold(month)
    printTaxes.Print_Taxes(month)
    printTOWorksheet.Print_Worksheet(month)
    printFeeAlloc.Print_FeeAlloc(month)
    reportBudgets.printCliBudget(month)
    reportBudgets.printTkBudget(month)
    reportBudgets.printFirmBudget(month)
