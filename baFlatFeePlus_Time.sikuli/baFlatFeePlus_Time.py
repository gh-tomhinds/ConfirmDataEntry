from sikuli import *
import logging
import myTools
import createClient
import baCommon
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_FlatFeePlusTime_Arrangement():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba FFPlusTime")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-FFPlus-Time")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    baCommon.moveto_BAPage()
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
def BA_FlatFeePlus_Time():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-FFPlus-Time","BA-FFPlus-Time","FF Plus - Time","FF Plus - Time","FF Plus - Time")
    # create some slips
    baCommon.BA_Create_Slips("BA-FFPlus-Time")
    # set up billing arrangement
    BA_FlatFeePlusTime_Arrangement() 
    # print a bill to text
    baCommon.BA_Bill("BA-FFPlus-Time",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-FFPlus-Time1")
