from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def print_DaysToPay(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print daystopay")

    # name report file: ex: DaysToPay-03
    reportName = myTools.monthToName(pReportMonth,"-DaysToPay-",pRepExt)
    logging.debug('Print_DaysToPay: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report')
    type("r",KeyModifier.ALT)
    type("a")
    time.sleep(2)   
    type("d")    
    time.sleep(1)
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

    # fill in path and name; press ENTER
    type(Settings.repFolder + "\\" + reportName)
    time.sleep(1)
    type(Key.ENTER)    

    # wait for report to complete
    myTools.waitForReport()

    # compare the report with baseline
    reports_Compare.Compare_OneReport(reportName)

    # close the report
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)            
    type("n")
    type(Key.F4,KeyModifier.CTRL)
        
    myTools.sectionEndTimeStamp()