from sikuli import *
import logging
import myTools
import createClient
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_MinimumTime_Arrangement():
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
    ba__Common.moveto_BAPage()
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
def BA_Minimum_Time():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-Minimum-Time","BA-Minimum-Time","Minimum FF - Time","Minimum FF - Time","Minimum FF - Time")
    # create some slips
    ba__Common.BA_Create_Slips("BA-Minimum-Time")
    # set up billing arrangement
    BA_MinimumTime_Arrangement() 
    # print a bill to text
    ba__Common.BA_Bill("BA-Minimum-Time",1)
    # compare at bill values
    ba__ReviewBills.Review_Bill("BA-Minimum-Time1")
