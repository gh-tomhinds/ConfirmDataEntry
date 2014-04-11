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

#import python
import logging
reload(logging)
import os
import datetime

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
import importBillLayout
import printBills
import setupCalTerms
import calendarStuff
import printClients
import printTasks
import printExpenses
import printTimekeepers
import compareReports

# setup logging
logging.basicConfig(filename=os.environ['USERPROFILE']+'\desktop\Sikuli\Sikuli.log', level=logging.DEBUG, format='%(message)s', filemode='w')
# Level = DEBUG, INFO, WARNING, ERROR, CRITICAL

# stamp start time
startTime = datetime.datetime.now()
logging.debug(' ')
logging.debug('- - - - - - - - - - - - - - -')
logging.debug(startTime.strftime("Started at: %Y-%m-%d %H:%M:%S"))
logging.debug('- - - - - - - - - - - - - - -')

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
#importTasks.Import_Tasks()
#editTask.Edit_Task()
#importExpenses.Import_Expenses()
#editExpense.Edit_Expense()
#createRefs.Create_Refs()
#importRefs.Import_Refs()
#setupFeeAlloc.Setup_FeeAlloc()
#setupExpMarkups.Setup_ExpMarkups()
#setupTaxes.Setup_Taxes()
#createSlips.Create_Slips(10,10)

#createPayments.Create_Payments()
#importBillLayout.Import_BillLayout()
#printBills.Print_Bills()
#baCommon.Setup_BADefaultLayout()
#reviewBillingArrangements.Review_BillingArrangements()

#setupCalTerms.Setup_CalTerms()
#calendarStuff.Calendar_Stuff()
#printClients.Print_Clients()
#printTasks.Print_Tasks()
#printExpenses.Print_Expenses()
#printTimekeepers.Print_Timekeepers()
compareReports.Compare_Reports()

endTime = datetime.datetime.now()
logging.debug(' ')
logging.debug('- - - - - - - - - - - - - - -')
logging.debug(endTime.strftime("Stopped at: %Y-%m-%d %H:%M:%S"))
logging.debug('- - - - - - - - - - - - - - -')

elapsedTime = endTime - startTime
logging.debug("Elapsed:    %s" %elapsedTime)

exit()
