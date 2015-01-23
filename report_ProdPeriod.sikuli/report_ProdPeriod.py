from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def print_ProdPeriod(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print ProdPer")

    # name report file: ex: ProdPer-03
    reportName = myTools.monthToName(pReportMonth,"-ProdPer-",pRepExt)
    logging.debug('Print_ProdPeriod: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("s")
    time.sleep(1)
    
    logging.debug('- set up report')
    type("prod")
    time.sleep(1)
    type("o",KeyModifier.CTRL)
    time.sleep(1)

    # Options
    myTools.pressSHIFTTAB(4)
    type(Key.SPACE)
    time.sleep(1)

    # Default
    myTools.pressSHIFTTAB(4)
    type(Key.SPACE)
    time.sleep(1)

    # OK
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)

    # choose CSV
    myTools.pressTAB(2)
    type("c")
    time.sleep(1)

    myTools.enterSlipFilter(pReportMonth,"report")

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