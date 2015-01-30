from sikuli import *
import logging

#---------------------------------------------------#
def fPrint_SlipListSimple():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print sliplistsimple")

    # name report file: ex: UDSlip1-03
    reportName = myTools.monthToName(13,"-UDSlip1-",".csv")
    logging.debug('fPrint_SlipListSimple')

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

    type(Key.DOWN)                    # Slip Listing Simple
    type("n",KeyModifier.ALT)         # next
    time.sleep(1)

    type("n",KeyModifier.ALT)         # next
    type(Key.ENTER)                   # Open Report Entry
    time.sleep(1)

    myTools.pressSHIFTTAB(2)          # print to csv
    type("c")
    type(Key.ENTER)                   # print
    time.sleep(1)

    type(Settings.repFolder + "\\" + reportName)
    time.sleep(1)    
    type(Key.ENTER)

    # wait for report to complete
    myTools.waitForReport()
    type("n")   

    # compare the report with baseline
    reports_Compare.Compare_OneReport(reportName)

    # close the report
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)            
    type("n")
    type(Key.F4,KeyModifier.CTRL)
        
    myTools.sectionEndTimeStamp()