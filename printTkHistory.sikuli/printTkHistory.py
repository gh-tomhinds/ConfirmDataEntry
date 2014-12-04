from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def Print_TkHistory(reportMonth):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print tk history")
    logging.debug('Print_TkHistory: ' + str(reportMonth))

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report')
    type("r",KeyModifier.ALT)
    type("t")
    time.sleep(1)   
    type("timekeeper history")
    time.sleep(1)
    type("o",KeyModifier.CTRL)
    time.sleep(1)

    # remove all filters
    myTools.pressTAB(4)
    type(Key.ENTER)

    logging.debug('- default options')

    # options button
    myTools.pressTAB(3)
    type(Key.ENTER)
    time.sleep(1)
    
    # default button   
    myTools.pressSHIFTTAB(4)
    type(Key.ENTER)
    time.sleep(1)

    # period = quarterly
    myTools.pressSHIFTTAB(2)
    type("q")

    # unmark "show analysis"
    myTools.pressSHIFTTAB(8)
    type(Key.SPACE)

    # close dialog
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

    # name report file: ex: TkHistory-03
    reportName = myTools.monthToName(reportMonth,"-TkHistory-",".csv")

    # fill in path and name; press ENTER
    type(Settings.repFolder + "\\" + reportName)
    time.sleep(1)
    type(Key.ENTER)    

    if exists("replace_it.png"):
        type(Key.ENTER)  

    # wait for report to complete
    myTools.waitForReport()

    # compare the report with baseline
    reports_Compare.Compare_OneReport(reportName)

    # close the report
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)            
    if exists("preferences_msg.png"):
        type("n")
    type(Key.F4,KeyModifier.CTRL)
        
    myTools.sectionEndTimeStamp()