from sikuli import *

import setupBills
import importBillLayout

import printBills
import createPaymentsForMonth
import createPaymentsToAccount

import makeBackup

import printARAgedBal
import printTkHistory

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def run_MonthlyBillCycle(startMonth,endMonth):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    for thisMonth in range(startMonth,endMonth):

        # set up the bill report and import the bill layout before the first month
        if (thisMonth == 1):
            setupBills.Setup_Bills()
            importBillLayout.Import_BillLayout()         
        
        printBills.Print_Bills(thisMonth)
        createPaymentsForMonth.Create_PaymentsForMonth(thisMonth)
        createPaymentsToAccount.Create_PaymentsToAccount(thisMonth)
        makeBackup.Backup_BillData(thisMonth)

        # compare some values each month
        printARAgedBal.Print_ARAgedBal(thisMonth)
        printTkHistory.Print_TkHistory(thisMonth)
