from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fSetup_TkCollections():
#---------------------------------------------------#

    logging.debug('- set up collections')
    
    myTools.getFocus()
    logging.debug('- open report')

    type("r",KeyModifier.ALT)
    type("t")
    time.sleep(1)

    type("timekeeper col")
    time.sleep(1)
    
    myTools.removeDateAndTime()

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type("y")

#---------------------------------------------------#
def Print_TkCollections(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print tkcollections")

    # name report file: ex: TkCC-03
    reportName = myTools.monthToName(pReportMonth,"-TkColl-",pRepExt)
    logging.debug('Print_TkColl: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report')
    type("r",KeyModifier.ALT)
    type("t")
    time.sleep(2)   
    type("timekeeper col")
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

    # itemize
    myTools.pressTAB(4)
    type(Key.SPACE)
    time.sleep(1)

    # close dialog
    type(Key.ENTER)
    time.sleep(1)   

    logging.debug('- print report')

    # move to Print To and choose text
    myTools.pressTAB(2)
    type("t")
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