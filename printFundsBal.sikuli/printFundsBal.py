from sikuli import *
import logging
import myTools
import compareOneReport

#---------------------------------------------------#
def fPrint_FundsBal(reportMonth):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print fundsbal")
    logging.debug('fPrint_FundsBal: ' + str(reportMonth))

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report')

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

    # OK
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)

    # choose CSV
    myTools.pressTAB(2)
    type("c")    
    type(Key.ENTER)
    time.sleep(1)

    # name report file: ex: TkCC-03
    reportName = myTools.monthToName(reportMonth,"-FundsBal-",".csv")

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