from sikuli import *

import setupBills
import importBillLayout

import printBills
import createPaymentsForMonth
import createPaymentsToAccount
import createCreditsForMonth
import createFinanceChargesForMonth

import makeBackup
import printPostbillReports

#---------------------------------------------------#
def run_MonthlyBillCycle(startMonth,endMonth):
#---------------------------------------------------#

    for thisMonth in range(startMonth,endMonth):

        # set up the bill report and import the bill layout before the first month
        if (thisMonth == 1):
            setupBills.Setup_Bills()
            importBillLayout.Import_BillLayout()         
        
        printBills.Print_Bills(thisMonth)
        createPaymentsForMonth.Create_PaymentsForMonth(thisMonth)
        createPaymentsToAccount.Create_PaymentsToAccount(thisMonth)
        createCreditsForMonth.Create_CreditsForMonth(thisMonth)
        createFinanceChargesForMonth.Create_FinanceCharges(thisMonth)

        makeBackup.Backup_BillData(thisMonth)

        # compare some values each month
        printPostbillReports.print_postbill_reports(thisMonth)
