from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fCreate_SlipListDetailed():
#---------------------------------------------------#

    logging.debug('- fCreate_SlipListDetailed')

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
    time.sleep(1)        

#---------------------------------------------------#
def fCreate_SlipFields():
#---------------------------------------------------#

    logging.debug('- fCreate_SlipFields')

    # make sure timeslips has focus
    myTools.getFocus()

    type("r",KeyModifier.ALT)         # slip reports
    type("s")
    time.sleep(1)

    type("slip")                      # highlight "slip listing - detailed"
    time.sleep(1)
    type(Key.DOWN)
    time.sleep(1)

    click("design_tool.png")
    time.sleep(2)

    type("l",KeyModifier.ALT)         # duplicate
    type("a")
    time.sleep(1)

    type("a",KeyModifier.CTRL)        # rename
    time.sleep(1)
    type("Slip Fields")
    time.sleep(1)

    type("l",KeyModifier.ALT)         # import fields
    type("p")
    time.sleep(1)

    templateName = Settings.dataFolder + '\\UDS SlipFields.tsl'
    paste(templateName)
    time.sleep(1)
    type(Key.ENTER)
    time.sleep(1)
    type(Key.ENTER)
    time.sleep(1)

    type(Key.F4,KeyModifier.CTRL)      # close / save
    time.sleep(1)
    type(Key.ENTER)

    type(Key.F4,KeyModifier.CTRL)      # close
    time.sleep(1)

#---------------------------------------------------#
def fPrint_SlipListDetailed(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print sliplistdetailed")

    # name report file: ex: UDSlip1-03
    reportName = myTools.monthToName(pReportMonth,"-UDSlip1-",pRepExt)
    logging.debug('Print_UDSlip1: ' + reportName)
    myTools.getFocus()

    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("s")
    time.sleep(1)

    logging.debug('- choose report')
    type("slip listing - d")
    time.sleep(1)

    # choose CSV
    myTools.pressSHIFTTAB(2)
    time.sleep(1)
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

    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def fPrint_SlipFields(pReportMonth,pRepExt):
#---------------------------------------------------#

    # this does not include applied fields, since we fixed some stuff in ts2016

    myTools.sectionStartTimeStamp("print slipfields")

    # name report file: ex: UDSlip1-03
    reportName = myTools.monthToName(pReportMonth,"-UDSlip2-",pRepExt)
    logging.debug('Print_UDSlip2: ' + reportName)
    myTools.getFocus()

    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("s")
    time.sleep(1)

    logging.debug('- choose report')
    type("slip f")
    time.sleep(1)

    # choose CSV
    myTools.pressSHIFTTAB(2)
    time.sleep(1)
    type("c")
    time.sleep(1)

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    # fill in path and name
    type(Settings.repFolder + "\\" + reportName)
    time.sleep(1)

    # export column titles
    myTools.pressTAB(2)
    time.sleep(1)
    type(Key.SPACE)
    time.sleep(1)

    # press ENTER to print
    type(Key.ENTER)    

    # wait for report to complete
    myTools.waitForReport()

    # compare the report with baseline
    reports_Compare.Compare_OneReport(reportName)

    # close the report
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()
