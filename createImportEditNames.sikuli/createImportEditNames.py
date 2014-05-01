from sikuli import *

import editDefaultClient

import createClient
import createTask
import createExpense

import importTimekeepers
import editTimekeeper

import importClients
import editClient
import editClientFunds

import importTasks
import editTask
import importExpenses
import editExpense

import createRefs
import importRefs

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def CreateImportEdit_Names():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
 
    editDefaultClient.Edit_DefaultClient()
    
    createClient.Create_Client("ZZZlient","Client001","9999 - First Client","In Ref to","Client Notes")
    createTask.Create_Task()
    createExpense.Create_Expense()
    
    importTimekeepers.Import_Timekeepers()
    editTimekeeper.Edit_Timekeeper()
    
    importClients.Import_Clients()
    editClient.Edit_Client()    
    editClientFunds.Edit_ClientFunds()
    
    importTasks.Import_Tasks()
    editTask.Edit_Task()
    importExpenses.Import_Expenses()
    editExpense.Edit_Expense()
    
    createRefs.Create_Refs()
    importRefs.Import_Refs()
