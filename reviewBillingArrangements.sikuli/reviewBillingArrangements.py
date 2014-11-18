from sikuli import *
import logging
import ba__Common
import datetime
import myTools
import makeBackup

import ba_AdjustTotal_Time
import ba_AdjustTotal_Exp
import ba_AdjustTotal_Both

import ba_AdjustTimekeeper_Time
import ba_AdjustTimekeeper_Exp
import ba_AdjustTimekeeper_Both

import ba_AdjustTask
import ba_AdjustExpense

import ba_Absolute_Time
import ba_Absolute_Exp
import ba_Absolute_Both

import ba_Minimum_Time
import ba_Minimum_Exp
import ba_Minimum_Both

import ba_Maximum_Time
import ba_Maximum_Exp
import ba_Maximum_Both

import ba_FlatFeePlus_Time
import ba_FlatFeePlus_Exp
import ba_FlatFeePlus_Both

import ba_Contingency_Time
import ba_Contingency_Exp
import ba_Contingency_Both

import ba_MinimumHours
import ba_Percent

import ba_ProgressTotal
import ba_ProgressActivity
import ba_InterimTotal
import ba_InterimActivity

import ba_SlipsRoundMin
import ba_SlipsRoundDol
import ba_Precision

import printPostbillReports

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def baLogHeader():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    if os.path.isfile(Settings.BALogFile):
        outFile = Settings.repFolder + "\\!BA-Log.txt"
        billLog = open(outFile, "a")
        billLog.write("\n")
        billLog.write("==================================================\n")
        baTime = datetime.datetime.now()
        billLog.write(baTime.strftime("Started: %Y-%m-%d %H:%M:%S\n"))
        billLog.write("==================================================\n")

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Review_BillingArrangements():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug(' ')
    logging.debug('Review_BillingArrangements')
    
    # make sure timeslips has focus
    myTools.getFocus()

    baLogHeader()

    ba_AdjustTotal_Time.BA_AdjustTotal_Time()
    ba_AdjustTotal_Exp.BA_AdjustTotal_Exp()
    ba_AdjustTotal_Both.BA_AdjustTotal_Both()
    
    ba_AdjustTimekeeper_Time.BA_AdjustTimekeeper_Time()
    ba_AdjustTimekeeper_Exp.BA_AdjustTimekeeper_Exp()
    ba_AdjustTimekeeper_Both.BA_AdjustTimekeeper_Both()

    ba_AdjustTask.BA_AdjustTask()
    ba_AdjustExpense.BA_AdjustExpense()

    ba_Absolute_Time.BA_Absolute_Time()
    ba_Absolute_Exp.BA_Absolute_Exp()
    ba_Absolute_Both.BA_Absolute_Both()

    ba_Minimum_Time.BA_Minimum_Time()
    ba_Minimum_Exp.BA_Minimum_Exp()
    ba_Minimum_Both.BA_Minimum_Both()
    
    ba_Maximum_Time.BA_Maximum_Time()
    ba_Maximum_Exp.BA_Maximum_Exp()
    ba_Maximum_Both.BA_Maximum_Both()

    ba_FlatFeePlus_Time.BA_FlatFeePlus_Time()
    ba_FlatFeePlus_Exp.BA_FlatFeePlus_Exp()
    ba_FlatFeePlus_Both.BA_FlatFeePlus_Both()

    ba_Contingency_Time.BA_Contingency_Time()
    ba_Contingency_Exp.BA_Contingency_Exp()
    ba_Contingency_Both.BA_Contingency_Both()

    ba_MinimumHours.BA_MinimumHours()

    ba_Percent.BA_Percent()

    ba_ProgressTotal.BA_ProgressTotal()
    ba_ProgressActivity.BA_ProgressActivity()    
    ba_InterimTotal.BA_InterimTotal()    
    ba_InterimActivity.BA_InterimActivity()    

    ba_SlipsRoundMin.BA_SlipsRoundMin()    
    ba_SlipsRoundDol.BA_SlipsRoundDol()    
    ba_Precision.BA_Precision()
   
    makeBackup.Backup_Checkpoint("ba")

    printPostbillReports.print_postbill_reports(13)