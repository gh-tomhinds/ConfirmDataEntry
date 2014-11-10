from sikuli import *
import logging
import myTools
from datetime import date

#---------------------------------------------------#
def Set_BillDate(month):
#---------------------------------------------------#
    logging.debug('- change bill date: ' + str(month) + "/27/2013")
    time.sleep(1)
    
    # open revise date
    type("b",KeyModifier.ALT)
    type("d")    
    time.sleep(2)

    # go to today
    type("t")

    #get to 01/01 of current year
    type(Key.HOME,KeyModifier.CTRL)        

    # get to 01/01/2013
    thisYear = date.today().year
    for prevYear in range(2013,thisYear):
        type(Key.PAGE_UP,KeyModifier.CTRL)        
    time.sleep(1)

    # get to 01/27/2013
    myTools.pressDOWN(4)
    myTools.pressLEFT(2)        

    for nextMonth in range(month-1):
        type(Key.PAGE_DOWN)       
    time.sleep(1)
    
    type(Key.ENTER)
    time.sleep(1)  

#---------------------------------------------------#
def Print_BillRun(month):
#---------------------------------------------------#
    logging.debug('- print bill run for month: ' + str(month))

    type("b",KeyModifier.CTRL)
    time.sleep(1)
    
    doubleClick("slip_trans_date.png")
    time.sleep(1)

    # choose TODAY to get to manual date entry
    type(Key.DOWN)
    type(Key.ENTER)
    time.sleep(1)

    # type in dates
    myTools.pressTAB(6)
    type("1/1/2013")
    type(Key.TAB)
    billDate = str(month) + "/27/2013"
    type(billDate)
    time.sleep(1)

    # print bills to PDF
    type(Key.ENTER)    
    time.sleep(1)
    type(Key.ENTER)    

    wait("bills_saved_to_pdf.png",FOREVER)
    type(Key.ENTER)    
    time.sleep(1)

    # approve bills
    wait(Pattern("approve_bills.png").targetOffset(-124,-10),FOREVER)
    click("approve_bills.png")
    type(Key.ENTER)
    waitVanish("approving_statusbar.png",FOREVER) 

    # close report entry / don't save
    logging.debug('-- close report window')
    click("report_generate_bills.png")
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(2)
    type("n")    
    time.sleep(1)

#---------------------------------------------------#
def Print_Bills(month):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("bills" + str(month))
    logging.debug('Print_Bills: ' + str(month))
    
    # make sure timeslips has focus
    myTools.getFocus()

    Set_BillDate(month)
    Print_BillRun(month)
    myTools.sectionEndTimeStamp()
