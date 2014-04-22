# - - - - - - - - - - - - - - - - - - - - - - - - - - #
# tsMain
# - - - - - - - - - - - - - - - - - - - - - - - - - - #
#
# These scripts rely on the following:                
#
# 1) Windows Explorer windows opens in primary monitor 
# 2) Timeslips is installed below C:\Program Files (x86)  
# 3) Timeslips install folder is in format: Timeslips 2014
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - #

import os
import myTools

# import my sikuli scripts
import setupStuff
import closeTimeslips
import delDataFolder
import startTSandNewDB
import tweakPrefs
import createCategories
import createCustomFields
import createClient
import createTask
import createExpense
import importClients
import importTimekeepers
import importTasks
import importExpenses
import editTimekeeper
import editTask
import editExpense
import editClient
import setupFeeAlloc
import setupExpMarkups
import createRefs
import importRefs
import setupTaxes
import createSlips

import reviewBillingArrangements
import baCommon

import createPayments
import createPaymentsForMonth

import setupBills
import importBillLayout
import printBills
import makeBackup
import setupCalTerms
import calendarStuff
import printClients
import printTasks
import printExpenses
import printTimekeepers
import printARAgedBal
import printTkHistory
import compareReports

#import sendEmail

# setup logging
myTools.setupLog()
myTools.startTimeStamp()
setupStuff.Setup_Stuff()

#closeTimeslips.Close_Timeslips()
#delDataFolder.Delete_Data_Folder()
#startTSandNewDB.StartTS_CreateNewDB()
#tweakPrefs.Tweak_Prefs()
#createCategories.Create_Categories()
#createCustomFields.Create_CustomFields()
#createClient.Create_Client("ZZZlient","Client001","9999 - First Client","In Ref to","Client Notes")
#createTask.Create_Task()
#createExpense.Create_Expense()
#importTimekeepers.Import_Timekeepers()
#editTimekeeper.Edit_Timekeeper()
#importClients.Import_Clients()
#editClient.Edit_Client()
importTasks.Import_Tasks()
editTask.Edit_Task()
#importExpenses.Import_Expenses()
#editExpense.Edit_Expense()
#createRefs.Create_Refs()
#importRefs.Import_Refs()
#setupFeeAlloc.Setup_FeeAlloc()
#setupExpMarkups.Setup_ExpMarkups()
#setupTaxes.Setup_Taxes()
#createSlips.Create_Slips(10,10)

#setupBills.Setup_Bills()
#importBillLayout.Import_BillLayout()

#for count in range(1,13):
#    printBills.Print_Bills(count)
#    createPaymentsForMonth.Create_PaymentsForMonth(count)
#    makeBackup.Backup_Data(count)

#printARAgedBal.Print_ARAgedBal("ARAgedBal-02.csv")
#printTkHistory.Print_TkHistory("TkHistory-01.csv")

#baCommon.Setup_BADefaultLayout()
#reviewBillingArrangements.Review_BillingArrangements()

#setupCalTerms.Setup_CalTerms()
#calendarStuff.Calendar_Stuff()
#printClients.Print_Clients()
#printTasks.Print_Tasks()
#printExpenses.Print_Expenses()
#printTimekeepers.Print_Timekeepers()
#compareReports.Compare_Reports()

myTools.endTimeStamp()

#sendEmail.Send_Email()

exit()
