from sikuli import *
import logging
import myTools
import compareOneReport

#---------------------------------------------------#
def Print_Hold(reportName):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print hold")

    reportName = Settings.tsVersion + "-" + reportName

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
    type(Key.ENTER)
    time.sleep(1)

    # fill in path and name; press ENTER
    type(Settings.repFolder + "\\" + reportName)
    time.sleep(1)
    type(Key.ENTER)    

    if exists("1372861767712.png"):
        type(Key.ENTER)  
        
    time.sleep(5)

    # compare the report with baseline
    compareOneReport.Compare_OneReport(reportName)

    type(Key.F4,KeyModifier.CTRL)

    time.sleep(1)            
    type("n")
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()