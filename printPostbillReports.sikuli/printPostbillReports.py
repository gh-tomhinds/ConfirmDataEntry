from sikuli import *

import printARAgedBal
import printTkHistory
import printTkCC
import printFundsBal
import printHold

#---------------------------------------------------#
def print_postbill_reports(month):
#---------------------------------------------------#

    # print various reports to check db values and calculations
    # this function is also called from reviewBillingArrangements

    printARAgedBal.Print_ARAgedBal(month)
    printTkHistory.Print_TkHistory(month)
    printTkCC.Print_TkCC(month)
    printFundsBal.Print_FundsBal(month)
    printHold.Print_Hold(month)
