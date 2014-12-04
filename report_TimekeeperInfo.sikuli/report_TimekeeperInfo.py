from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fPrint_TimekeeperInfo(pReportName):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print timekeepers")

    reportName = Settings.tsVersion + "-" + pReportName
    logging.debug('fPrint_TimekeeperInfo: ' + pReportName)

    # make sure timeslips has focus
    myTools.getFocus()
    
    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("t")    
    time.sleep(1)
    
    logging.debug('- set up timekeeper info listing')
    type("timekeeper info")    
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

    # overhead costs
    myTools.pressTAB(6)
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
    type(Settings.repFolder + "\\" + pReportName)
    time.sleep(1)
    type(Key.ENTER)    

    if exists("replace_it.png"):
        type(Key.ENTER)  

    # wait for report to complete
    myTools.waitForReport()

    # compare the report with baseline
    reports_Compare.Compare_OneReport(pReportName)

    type(Key.F4,KeyModifier.CTRL)

    time.sleep(1)            
    type("n")
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()