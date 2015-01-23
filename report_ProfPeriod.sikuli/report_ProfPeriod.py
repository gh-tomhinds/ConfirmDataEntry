from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def print_ProfPeriod(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print ProdPer")

    # name report file: ex: ProfPer-03
    reportName = myTools.monthToName(pReportMonth,"-ProfPer-",pRepExt)
    logging.debug('Print_ProfPeriod: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("s")
    time.sleep(1)
    
    logging.debug('- set up report')
    type("prof")
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

    type(Key.F4,KeyModifier.CTRL)

    time.sleep(1)            
    type("n")
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()