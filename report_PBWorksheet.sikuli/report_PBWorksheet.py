from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fSetup_PreBill():
#---------------------------------------------------#

    logging.debug('- set up prebill')
    
    myTools.getFocus()
    logging.debug('- open worksheet')
    type("b",KeyModifier.ALT)
    type("p")

    myTools.removeDateAndTime()

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type("y")

#---------------------------------------------------#
def fPrint_PreBill(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print worksheet")

    # name report file: ex: PreBill-03
    reportName = myTools.monthToName(pReportMonth,"-PreBill-",pRepExt)
    logging.debug('Print_PreBill: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open worksheet')
    type("b",KeyModifier.ALT)
    type("p")    
    time.sleep(1)
    
    logging.debug('- set up worksheet')
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

    # choose text
    myTools.pressTAB(2)
    type("t")
    time.sleep(1)

    myTools.enterSlipFilter(pReportMonth,"n")

    # print the report
    type(Key.ENTER)    
    time.sleep(1)
    
    # fill in path and name; press ENTER
    type(Settings.repFolder + "\\" + reportName)
    time.sleep(1)
    type(Key.ENTER)    

    # wait for report to complete
    myTools.waitForWorksheet()

    # compare the report with baseline
    reports_Compare.Compare_OneReport(reportName)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)            
    type("n")

    myTools.sectionEndTimeStamp()