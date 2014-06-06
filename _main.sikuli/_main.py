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

import reviewBillingArrangements
import baCommon

import runMonthlyBillCycle

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

#startTSandNewDB.StartTS_CreateNewDB()

#tweakPrefs.Tweak_Prefs()
#createCategories.Create_Categories()
#createCustomFields.Create_CustomFields()

#createImportEditNames.CreateImportEdit_Names()

#createSlips.Create_Slips(10,10) # pass in num-time-slips and num-exp-slips to create manually; should by 10, 10
#runMonthlyBillCycle.run_MonthlyBillCycle(1,13) # pass in start and end+1 month; should by 1, 13 unless starting in mid stream

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
