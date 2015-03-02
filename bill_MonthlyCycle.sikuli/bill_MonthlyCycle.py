from sikuli import *
import logging

import backup_Data

import bill_Setup
import bill_ImportLayout
import bill_Print

import trans_PostBill
import reports_CreateReports
import reports_PostBill

#---------------------------------------------------#
def fRun_BillCycle(startMonth,endMonth):
#---------------------------------------------------#

    logging.debug(' ')
    logging.debug('start bill cycle')

    for thisMonth in range(startMonth,endMonth):
        logging.debug('- month: ' + str(thisMonth))
        
        if (thisMonth == 1):                                        # before 1st month, set up bill report and import the layout
            bill_Setup.fSetup_BillReport()
            bill_ImportLayout.fImport_BillLayout("Bill with Taxes")
            backup_Data.fBackup_BillData(0,"a")                     # backup before first bill

        bill_Print.fPrint_Bills(thisMonth)        
        backup_Data.fBackup_BillData(thisMonth,"a")       
        reports_PostBill.fPrint_PostbillReports(thisMonth,"a")      # compare some values before trans

        trans_PostBill.fEnter_Transactions(thisMonth)               # enter all transactions
        backup_Data.fBackup_BillData(thisMonth,"b")        
        reports_PostBill.fPrint_PostbillReports(thisMonth,"b")      # compare some values after trans