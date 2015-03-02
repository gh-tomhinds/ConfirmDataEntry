from sikuli import *
import logging
import myTools
import report_UDSlip
import report_UDClient
import report_UDInvoice
import report_UDFunds
import report_Statement
import backup_Data


#---------------------------------------------------#
def create_UDReports():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("create udreports")
    logging.debug('create_UDReports')

    report_UDSlip.fCreate_SlipListDetailed()
    report_UDSlip.fCreate_SlipFields()
    report_UDClient.fCreate_ClientListHistory()
    report_UDClient.fCreate_ClientListValues()
    report_UDInvoice.fCreate_InvoiceListFields()
    report_UDInvoice.fSort_InvoiceListFields()    
    report_UDFunds.fCreate_FundsListFields()
    report_Statement.fImport_Statement()

    myTools.sectionEndTimeStamp()
    backup_Data.fBackup_Checkpoint("udReports")