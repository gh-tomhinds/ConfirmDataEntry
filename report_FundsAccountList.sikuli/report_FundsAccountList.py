from sikuli import *
import logging
import myTools
import compareOneReport

#---------------------------------------------------#
def fPrint_Funds(pReportName):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print funds")

    reportName = Settings.tsVersion + "-" + pReportName
    logging.debug('fPrint_Funds: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()
    
    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("f")    
    time.sleep(1)
    
    logging.debug('- set up funds account listing')
    type("funds")    
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

    # show all fields
    myTools.pressSHIFTTAB(3)
    type(Key.SPACE)
    time.sleep(1)   

    # OK
    myTools.pressTAB(4)
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

    if exists("replace_it.png"):
        type(Key.ENTER)  

    # wait for report to complete
    myTools.waitForReport()

    # compare the report with baseline
    compareOneReport.Compare_OneReport(reportName)

    type(Key.F4,KeyModifier.CTRL)

    time.sleep(1)            
    type("n")
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()