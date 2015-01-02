from sikuli import *

import bill_Setup
import bill_ImportLayout

import bill_Print
import trans_SpecCredits
import trans_Payments
import trans_Transfers
import trans_TransfersToFunds
import trans_PaymentsToAccount
import trans_Credits
import client_FinanceCharges
import trans_BankDepositSlip

import backup_Data
import reports_PostBill

#---------------------------------------------------#
def fRun_BillCycle(startMonth,endMonth):
#---------------------------------------------------#

    for thisMonth in range(startMonth,endMonth):

        # set up the bill report and import the bill layout before the first month
        if (thisMonth == 1):
            bill_Setup.fSetup_BillReport()
            bill_ImportLayout.fImport_BillLayout("Bill with Taxes")
        
        bill_Print.fPrint_Bills(thisMonth)

        # back up data and compare some values each month
        backup_Data.fBackup_BillData(thisMonth,"a")        
        reports_PostBill.fPrint_PostbillReports(thisMonth,"a")

        # enter transactions for month
        trans_SpecCredits.fCreate_SpecCredits(thisMonth)        
        trans_Payments.fCreate_PaymentsForMonth(thisMonth)
        trans_Transfers.fCreate_Transfers(thisMonth)        
        trans_TransfersToFunds.fCreate_TransfersToFunds(thisMonth)        
        trans_PaymentsToAccount.fCreate_PaymentsToAccount(thisMonth)
        trans_Credits.fCreate_CreditsForMonth(thisMonth)
        client_FinanceCharges.fCreate_FinanceCharges(thisMonth)
        trans_BankDepositSlip.fBankDepositSlips_Create(thisMonth)

        # back up data and compare some values each month
        backup_Data.fBackup_BillData(thisMonth,"b")        
        reports_PostBill.fPrint_PostbillReports(thisMonth,"b")
