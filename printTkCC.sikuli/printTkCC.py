from sikuli import *
import logging
import myTools
import compareOneReport

#---------------------------------------------------#
def Print_TkCC(reportMonth):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print tkcc")
    logging.debug('Print_TkCC: ' + str(reportMonth))

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report')
    type("r",KeyModifier.ALT)
    type("t")
    time.sleep(2)   
    type("timekeeper cont")    
    time.sleep(1)
    myTools.pressDOWN(1)
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

    # close dialog
    myTools.pressTAB(1)
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

    # name report file: ex: TkCC-03
    reportName = myTools.monthToName(reportMonth,"-TkCC-",".csv")

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

    # close the report
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)            
    if exists("preferences_msg.png"):
        type("n")
    type(Key.F4,KeyModifier.CTRL)
        
    myTools.sectionEndTimeStamp()