# - - - - - - - - - - - - - - - - - - - - - - - - - - #
# _main
# - - - - - - - - - - - - - - - - - - - - - - - - - - #
#
# These scripts rely on the following:                
#
# 1) Windows Explorer windows opens in primary monitor 
# 2) Timeslips is installed below C:\Program Files (x86)  
# 3) Timeslips install folder is in format: Timeslips 2014
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - #

# import my sikuli scripts
import myTools

import setupStuff
import startTSandNewDB
import tweakPrefs

import createImportEditNames

import createCategories
import createCustomFields

import createSlips
import createSlipsManually

import setupSplitBills

import runMonthlyBillCycle

import reviewBillingArrangements
import baCommon

import makeBackup
import setupCalTerms
import calendarStuff
import printTasks
import printExpenses
import compareReports

#import sendEmail

##############################################################

myTools.setupLog()
myTools.startTimeStamp()
setupStuff.Setup_Stuff()

##############################################################

startTSandNewDB.StartTS_CreateNewDB()

tweakPrefs.Tweak_Prefs()
createCategories.Create_Categories()
createCustomFields.Create_CustomFields()

createImportEditNames.CreateImportEdit_Names()

createSlips.Create_Slips(10,10) # pass in numTimeSlips and numExpSlips to create manually; should be 10, 10
#createSlipsManually.Create_Slips(702,702) # pass in numTimeSlips and numExpSlips to create manually; should be 10, 10

setupSplitBills.Setup_SplitBills()

runMonthlyBillCycle.run_MonthlyBillCycle(1,13) # pass in start and end+1 month; should by 1, 13 unless starting in mid stream

baCommon.Setup_BADefaultLayout()
reviewBillingArrangements.Review_BillingArrangements()

#setupCalTerms.Setup_CalTerms()
#calendarStuff.Calendar_Stuff()
#printTasks.Print_Tasks()
#printExpenses.Print_Expenses()
#compareReports.Compare_Reports()

myTools.endTimeStamp()

#sendEmail.Send_Email()

exit()
