from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def setupReport():
#---------------------------------------------------#

    # open report
    type("o",KeyModifier.CTRL)
    time.sleep(1)

    logging.debug('- default options')
    # options button
    myTools.pressSHIFTTAB(4)
    type(Key.ENTER)
    time.sleep(1)
    
    # default button   
    myTools.pressSHIFTTAB(4)
    type(Key.ENTER)
    time.sleep(1)

    # close dialog
    myTools.pressTAB(1)
    type(Key.ENTER)
    time.sleep(1)   

    logging.debug('- print report')

    # move to Print To and choose CSV
    myTools.pressTAB(2)
    type("c")
    time.sleep(1)

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

#---------------------------------------------------#
def finishReport(pReportName):
#---------------------------------------------------#

    # fill in path and name; press ENTER
    type(Settings.repFolder + "\\" + pReportName)
    time.sleep(1)
    type(Key.ENTER)

    if exists("replace_it.png"):
        type(Key.ENTER)

    if exists("recalc_msg.png"):
        type(Key.ENTER)

    # wait for report to complete
    myTools.waitForReport()

    # compare the report with baseline
    reports_Compare.Compare_OneReport(pReportName)

    # close the report
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)

    # check for save message
    myTools.doNotSaveReport()
    
    type(Key.F4,KeyModifier.CTRL)
        
    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def printCliBudget(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print cli budget")

    reportName = myTools.monthToName(pReportMonth,"-CliBud-",pRepExt)   
    logging.debug('Print_CliBudget: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report')
    type("r",KeyModifier.ALT)
    type("c")
    time.sleep(2)
    
    type("client budgets by none")
    time.sleep(1)

    setupReport()
    finishReport(reportName)

#---------------------------------------------------#
def printTkBudget(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print tk budget")

    reportName = myTools.monthToName(pReportMonth,"-TkBud-",pRepExt)    
    logging.debug('Print_TkBudget: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report')
    type("r",KeyModifier.ALT)
    type("t")
    time.sleep(2)
    
    type("timekeeper budgets by none")
    time.sleep(1)

    setupReport()
    finishReport(reportName)

#---------------------------------------------------#
def printFirmBudget(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print firm budget")

    reportName = myTools.monthToName(pReportMonth,"-FirmBud-",pRepExt)
    logging.debug('Print_FirmBudget: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report')
    type("r",KeyModifier.ALT)
    type("h")
    time.sleep(2)
    
    type("firm")
    time.sleep(1)

    setupReport()
    finishReport(reportName)
