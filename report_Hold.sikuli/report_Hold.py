from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def Print_Hold(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print hold")

    # name report file: ex: Hold-03
    reportName = myTools.buildRepName("Hold",pRepExt)
    logging.debug('Print_Hold: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("c")    
    time.sleep(1)
    
    logging.debug('- set up hold report')
    type("ch")
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

    myTools.enterSlipFilter(pReportMonth,"n")

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)