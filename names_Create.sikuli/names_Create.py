from sikuli import *

#import editDefaultClient

import client_Create
import task_Create
import expense_Create

import timekeeper_Import
import timekeeper_Edit

import client_Import
import client_Edit
import client_FundsEdit

import task_Import
import task_Edit
import expense_Import
import expense_Edit

import ref_Create
import ref_Import

import client_FeeAlloc
import expense_Markup
import taxes_Setup
import client_Hold
import client_PayDistrib
import client_FundsNew
import budget_Setup

import backup_Data

import report_FundsAccountList
import report_TimekeeperInfo
import report_ClientInfo

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fCreateImportEdit_Names():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
 
#    editDefaultClient.Edit_DefaultClient()

# - - - - - - - - - - - - - - - - - - - - - - - - - #

    client_Create.fCreate_Client("ZZZlient","Client001","9999 - First Client","In Ref to","Client Notes")
    task_Create.fCreate_Task()
    expense_Create.fCreate_Expense()
    
    timekeeper_Import.fImport_Timekeepers()
    timekeeper_Edit.fEdit_Timekeeper()
    
    client_Import.fImport_Clients()
    client_Edit.fEdit_Client()    
    client_FundsEdit.fEdit_ClientFunds()
    report_FundsAccountList.fPrint_Funds("FundsSettings-01.csv")
    client_Hold.fSetup_ClientHold()
    client_FeeAlloc.fSetup_FeeAlloc()
    
    task_Import.fImport_Tasks()
    task_Edit.fEdit_Task()
    expense_Import.fImport_Expenses()
    expense_Edit.fEdit_Expense()
    
    expense_Markup.fSetup_ExpMarkups()
    taxes_Setup.fSetup_Taxes()
    client_PayDistrib.fSetup_PayDist()
    client_FundsNew.fFundsAccouts_Setup()

    ref_Create.fCreate_Refs()
    ref_Import.fImport_Refs()

    budget_Setup.fBudget_Setup()

    report_TimekeeperInfo.fPrint_TimekeeperInfo("Timekeepers-01.csv")
    report_ClientInfo.fPrint_ClientInfo("Clients-01.csv")

    backup_Data.fBackup_Checkpoint("names")