from sikuli import *
import logging
import myTools
import createClient
import ba_Common
import ba_ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_AbsoluteTime_Arrangement():
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
    ba_Common.moveto_BAPage()
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
def BA_Absolute_Time():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-Absolute-Time","BA-AdjTot-Time","Absolute FF - Time","Absolute FF - Time","Absolute FF - Time")
    # create some slips
    ba_Common.BA_Create_Slips("BA-Absolute-Time")
    # set up billing arrangement
    BA_AbsoluteTime_Arrangement() 
    # print a bill to text
    ba_Common.BA_Bill("BA-Absolute-Time",1)
    # compare at bill values
    ba_ReviewBills.Review_Bill("BA-Absolute-Time1")
