from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def Print_PayDistr(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print pay dist")

    # name report file: ex: PayDistr-03
    reportName = myTools.monthToName(pReportMonth,"-PayDistr-",pRepExt)
    logging.debug('Print_PayDistr: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report')
    type("r",KeyModifier.ALT)
    type("a")
    time.sleep(2)
    
    type("pay")
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

    # pay dist = with tax
    myTools.pressSHIFTTAB(3)
    type("w")
    
    # OK
    type(Key.ENTER)
    time.sleep(1)

    # Sort page
    type(Key.F6)
    time.sleep(1)

    # clear any existing sorts
    if exists("remove_all.png"):
        click("remove_all.png")   
        time.sleep(1)

    # sort by tran id
    type(Key.DOWN)
    time.sleep(1)
    click("add_filter.png")
    time.sleep(1)

    logging.debug('- print report')

    # move to Print To and choose CSV
    myTools.pressSHIFTTAB(3)
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