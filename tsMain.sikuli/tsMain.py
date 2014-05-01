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
import startTSandNewDB
import tweakPrefs

import createImportEditNames

import createCategories
import createCustomFields
import setupFeeAlloc
import setupExpMarkups
import setupTaxes
import createSlips

import reviewBillingArrangements
import baCommon

import createPaymentsForMonth
import createPaymentsToAccount

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

myTools.setupLog()
myTools.startTimeStamp()
setupStuff.Setup_Stuff()

startTSandNewDB.StartTS_CreateNewDB()
tweakPrefs.Tweak_Prefs()
createCategories.Create_Categories()
createCustomFields.Create_CustomFields()

createImportEditNames.CreateImportEdit_Names()

#setupFeeAlloc.Setup_FeeAlloc()
#setupExpMarkups.Setup_ExpMarkups()
#setupTaxes.Setup_Taxes()
#createSlips.Create_Slips(10,10)

#setupBills.Setup_Bills()
#importBillLayout.Import_BillLayout()

#for count in range(1,13):
#    printBills.Print_Bills(count)
#    createPaymentsForMonth.Create_PaymentsForMonth(count)
#    createPaymentsToAccount.Create_PaymentsToAccount(count)
#    makeBackup.Backup_BillData(count)

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
