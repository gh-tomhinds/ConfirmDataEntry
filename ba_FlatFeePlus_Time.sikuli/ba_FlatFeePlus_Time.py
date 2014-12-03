from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fFlatFeePlusTime_Setup():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba FFPlusTime")
    logging.debug("ba FFPlusTime")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-FFPlus-Time")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(4)
    
# switch to flat fee plus charges
    type(Key.HOME)
    myTools.pressDOWN(7)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("500")
    myTools.pressTAB(2)
    type("FF Plus - Time")
    
# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fFlatFeePlus_Time():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    client_Create.fCreate_Client("BA-FFPlus-Time","BA-FFPlus-Time","FF Plus - Time","FF Plus - Time","FF Plus - Time")
    # create some slips
    ba__Common.fCreate_BASlips("BA-FFPlus-Time")
    # set up billing arrangement
    fFlatFeePlusTime_Setup() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-FFPlus-Time",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-FFPlus-Time1")
