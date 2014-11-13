from sikuli import *

import setupBills
import importBillLayout

import printBills
import createSpecCredits
import createPaymentsForMonth
import createTransfers
import createTransfersToFunds
import createPaymentsToAccount
import createCreditsForMonth
import createFinanceChargesForMonth
import bankDepositSlip_Create

import makeBackup
import printPostbillReports

#---------------------------------------------------#
def run_MonthlyBillCycle(startMonth,endMonth):
#---------------------------------------------------#

    for thisMonth in range(startMonth,endMonth):

        # set up the bill report and import the bill layout before the first month
        if (thisMonth == 1):
            setupBills.Setup_Bills()
            importBillLayout.Import_BillLayout("Bill with Taxes")
        
        printBills.Print_Bills(thisMonth)
        createSpecCredits.Create_SpecCredits(thisMonth)        
        createPaymentsForMonth.Create_PaymentsForMonth(thisMonth)
        createTransfers.Create_Transfers(thisMonth)        
        createTransfersToFunds.Create_TransfersToFunds(thisMonth)        
        createPaymentsToAccount.Create_PaymentsToAccount(thisMonth)
        createCreditsForMonth.Create_CreditsForMonth(thisMonth)
        createFinanceChargesForMonth.Create_FinanceCharges(thisMonth)
        bankDepositSlip_Create.BankDepositSlips_Create(thisMonth)

        makeBackup.Backup_BillData(thisMonth)

        # compare some values each month
        printPostbillReports.print_postbill_reports(thisMonth)
