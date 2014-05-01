from sikuli import *

import setupBills
import importBillLayout

import printBills
import createPaymentsForMonth
import createPaymentsToAccount

import printARAgedBal
import printTkHistory

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def run_MonthlyBillCycle(startMonth,endMonth)
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    for thisMonth in range(1,13):

        # set up the bill report and import the bill layout before the first month
        if (thisMonth == 1):
            setupBills.Setup_Bills()
            importBillLayout.Import_BillLayout()         
        
        printBills.Print_Bills(thisMonth)
        createPaymentsForMonth.Create_PaymentsForMonth(thisMonth)
        createPaymentsToAccount.Create_PaymentsToAccount(thisMonth)
        makeBackup.Backup_BillData(thisMonth)

    # after whole bill run is done, compare some reports
    printARAgedBal.Print_ARAgedBal("ARAgedBal-02.csv")
    printTkHistory.Print_TkHistory("TkHistory-01.csv")
