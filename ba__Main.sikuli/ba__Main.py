from sikuli import *
import logging
import ba__Common
import datetime
import myTools
import backup_Data

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

import reports_PostBill

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fLogHeader():
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
def fReview_Arrangements():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug(' ')
    logging.debug('Review_Arrangements')
    
    # make sure timeslips has focus
    myTools.getFocus()

    fLogHeader()

    ba_AdjustTotal_Time.fAdjustTotal_Time()
    ba_AdjustTotal_Exp.fAdjustTotal_Exp()
    ba_AdjustTotal_Both.fAdjustTotal_Both()
    
    ba_AdjustTimekeeper_Time.fAdjustTimekeeper_Time()
    ba_AdjustTimekeeper_Exp.fAdjustTimekeeper_Exp()
    ba_AdjustTimekeeper_Both.fAdjustTimekeeper_Both()

    ba_AdjustTask.fAdjustTask()
    ba_AdjustExpense.fAdjustExpense()

    ba_Absolute_Time.fAbsolute_Time()
    ba_Absolute_Exp.fAbsolute_Exp()
    ba_Absolute_Both.fAbsolute_Both()

    ba_Minimum_Time.fMinimum_Time()
    ba_Minimum_Exp.fMinimum_Exp()
    ba_Minimum_Both.fMinimum_Both()
    
    ba_Maximum_Time.fMaximum_Time()
    ba_Maximum_Exp.fMaximum_Exp()
    ba_Maximum_Both.fMaximum_Both()

    ba_FlatFeePlus_Time.fFlatFeePlus_Time()
    ba_FlatFeePlus_Exp.fFlatFeePlus_Exp()
    ba_FlatFeePlus_Both.fFlatFeePlus_Both()

    ba_Contingency_Time.fContingency_Time()
    ba_Contingency_Exp.fContingency_Exp()
    ba_Contingency_Both.fContingency_Both()

    ba_MinimumHours.fMinimumHours()

    ba_Percent.fPercent()

    ba_ProgressTotal.fProgressTotal()
    ba_ProgressActivity.fProgressActivity()    
    ba_InterimTotal.fInterimTotal()    
    ba_InterimActivity.fInterimActivity()    

    ba_SlipsRoundMin.fSlipsRoundMin()
    ba_SlipsRoundDol.fSlipsRoundDol()
    ba_Precision.fPrecision()
   
    backup_Data.fBackup_Checkpoint("ba")

    reports_PostBill.print_postbill_reports(13)