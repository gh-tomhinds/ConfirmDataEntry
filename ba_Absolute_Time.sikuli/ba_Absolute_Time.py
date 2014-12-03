from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fAbsoluteTime_Setup():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba AbsoluteTime")
    logging.debug("ba AbsoluteTime")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Absolute-Time")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(4)
    
# switch to absolute
    type(Key.HOME)
    myTools.pressDOWN(4)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("1000")
    myTools.pressTAB(3)
    type("Absolute FF - Time")
    
# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fAbsolute_Time():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    client_Create.fCreate_Client("BA-Absolute-Time","BA-Absolute-Time","Absolute FF - Time","Absolute FF - Time","Absolute FF - Time")
    # create some slips
    ba__Common.fCreate_BASlips("BA-Absolute-Time")
    # set up billing arrangement
    fAbsoluteTime_Setup() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-Absolute-Time",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-Absolute-Time1")
