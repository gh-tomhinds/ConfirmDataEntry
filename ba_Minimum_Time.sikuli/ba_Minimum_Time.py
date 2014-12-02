from sikuli import *
import logging
import myTools
import createClient
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fMinimumTime_Setup():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba MinimumTime")
    logging.debug("ba MinimumTime")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Minimum-Time")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(4)
    
# switch to minimum
    type(Key.HOME)
    myTools.pressDOWN(5)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("5000")
    myTools.pressTAB(2)
    type("Minimum FF - Time")
    
# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fMinimum_Time():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-Minimum-Time","BA-Minimum-Time","Minimum FF - Time","Minimum FF - Time","Minimum FF - Time")
    # create some slips
    ba__Common.fCreate_BASlips("BA-Minimum-Time")
    # set up billing arrangement
    fMinimumTime_Setup() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-Minimum-Time",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-Minimum-Time1")
