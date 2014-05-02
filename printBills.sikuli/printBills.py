from sikuli import *
import logging
import myTools

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Set_BillDate(month):
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug('- change bill date')
    time.sleep(1)
    type("b",KeyModifier.ALT)
    type("d")    
    time.sleep(2)
    
    if month == 1:
        # get to 2013
        type(Key.PAGE_UP,KeyModifier.CTRL)        
        # get to 01/01/2013
        type(Key.HOME,KeyModifier.CTRL)        
        # move to 01/27/2013
        myTools.pressDOWN(4)
        myTools.pressLEFT(2)        
    else:
        type(Key.PAGE_DOWN)
       
    time.sleep(1)
    type(Key.ENTER)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Print_BillRun(month):
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug('- print bill run for month: ' + str(month))

    type("b",KeyModifier.CTRL)
    doubleClick("1368070709186.png")
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

    wait("1368071925388.png",600)
    type(Key.ENTER)    
    time.sleep(1)

    # approve bills
    wait(Pattern("1368108335979.png").targetOffset(-124,-10),600)
    click(Pattern("1368108335979.png").targetOffset(-124,-10))
    type(Key.ENTER)
    waitVanish("1368288231948.png",600) 

    # close report entry / don't save
    logging.debug('-- close report window')
    click("1368113563889.png")
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(2)
    type("n")    
    time.sleep(1)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Print_Bills(month):
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('Print_Bills')
    myTools.sectionStartTimeStamp()
    
    # make sure timeslips has focus
    myTools.getFocus()

    Set_BillDate(month)
    Print_BillRun(month)
    myTools.sectionEndTimeStamp()
