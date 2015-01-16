from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fPrint_ClientInfo(pReportName):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print clients")

    reportName = Settings.tsVersion + "-" + pReportName
    logging.debug('fPrint_ClientInfo: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()
    
    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("c")    
    time.sleep(1)
    
    logging.debug('- set up client info listing')
    type("client info")    
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

    # hide a/r fields
    myTools.pressSHIFTTAB(5)
    type(Key.SPACE)
    time.sleep(1)

    # OK
    myTools.pressTAB(6)
    type(Key.SPACE)
    time.sleep(1)

    # choose CSV
    myTools.pressTAB(2)
    type("c")    
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