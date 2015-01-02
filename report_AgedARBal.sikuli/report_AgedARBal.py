from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def Print_ARAgedBal(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print aged bal")

    # name report file: ex: ARAgedBal-03
    reportName = myTools.monthToName(pReportMonth,"-ARAgedBal-",pRepExt)    
    logging.debug('Print_ARAgedBal: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report')
    type("r",KeyModifier.ALT)
    type("b")
    time.sleep(1)

    # move to Print To and choose CSV
    myTools.pressSHIFTTAB(2)
    time.sleep(1)
    type("c")

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    # fill in path and name; press ENTER
    type(Settings.repFolder + "\\" + reportName)
    time.sleep(1)
    type(Key.ENTER)    

    if exists("replace_it.png"):
        type(Key.ENTER)  

    # wait for report to complete
    myTools.waitForReport()

    # compare the report with baseline
    reports_Compare.Compare_OneReport(reportName)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)            

    myTools.sectionEndTimeStamp()