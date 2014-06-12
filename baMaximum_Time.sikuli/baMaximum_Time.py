from sikuli import *
import logging
import myTools
import createClient
import baCommon
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_MaximumTime_Arrangement():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba MaximumTime")
    logging.debug("ba MaximumTime")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Maximum-Time")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    baCommon.moveto_BAPage()
    myTools.pressTAB(4)
    
# switch to maximum
    type(Key.HOME)
    myTools.pressDOWN(6)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("500")
    myTools.pressTAB(2)
    type("Maximum FF - Time")
    
# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_Maximum_Time():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-Maximum-Time","BA-Maximum-Time","Maximum FF - Time","Maximum FF - Time","Maximum FF - Time")
    # create some slips
    baCommon.BA_Create_Slips("BA-Maximum-Time")
    # set up billing arrangement
    BA_MaximumTime_Arrangement() 
    # print a bill to text
    baCommon.BA_Bill("BA-Maximum-Time",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-Maximum-Time1")
