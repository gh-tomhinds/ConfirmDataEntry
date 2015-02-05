from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fCreate_SlipListDetailed():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("create sliplistdetailed")
    logging.debug('fCreate_SlipListDetailed')

    # make sure timeslips has focus
    myTools.getFocus()

    type(Key.F3,KeyModifier.CTRL)     # create a report
    time.sleep(1)
    type("r",KeyModifier.ALT)         # ud report
    type("n",KeyModifier.ALT)         # next
    time.sleep(1)

    type("s")                         # slip
    type("n",KeyModifier.ALT)         # next
    time.sleep(1)

    myTools.pressDOWN(2)              # detailed Listing Simple
    type("n",KeyModifier.ALT)         # next
    time.sleep(1)

    type("n",KeyModifier.ALT)         # next
    type(Key.ENTER)                   # Open Report Entry
    time.sleep(1)

    type("s",KeyModifier.CTRL)        # save
    type(Key.ENTER)                   # OK
    time.sleep(1)
    
    type(Key.F4,KeyModifier.CTRL)     # close report
        
    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def fPrint_SlipListDetailed():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print sliplistdetailed")

    # name report file: ex: UDSlip1-03
    reportName = myTools.monthToName(13,"-UDSlip1-",".csv")
    logging.debug('fPrint_SlipListSimple')
    myTools.getFocus()

    type("r",KeyModifier.ALT)         # slip reports
    type("s")
    time.sleep(1)

    type("slip listing - d")
    time.sleep(1)

    type("o",KeyModifier.CTRL)
    time.sleep(1)

    # move to Print To and choose CSV
    myTools.pressSHIFTTAB(2)
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
