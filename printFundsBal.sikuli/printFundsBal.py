from sikuli import *
import logging
import myTools
import compareOneReport

#---------------------------------------------------#
def Print_FundsBal(reportMonth):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print fundsbal")
    logging.debug('Print_FundsBal: ' + str(reportMonth))

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

    if exists("1372861767712.png"):
        type(Key.ENTER)  

    #this report is long; wait for "calculating" box to disappear
    while exists("1402586543101.png"):
        time.sleep(3)

    # compare the report with baseline
    compareOneReport.Compare_OneReport(reportName)

    # close the report
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)            
    if exists("1397850458110.png"):
        type("n")
    type(Key.F4,KeyModifier.CTRL)
        
    myTools.sectionEndTimeStamp()