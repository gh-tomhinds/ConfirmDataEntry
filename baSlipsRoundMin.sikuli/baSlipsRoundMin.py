from sikuli import *
import logging
import myTools
import createClient
import baCommon
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_Round_Minutes():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba RoundMins")
    logging.debug("ba RoundMins")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-RoundMin")
    type(Key.ENTER)
    time.sleep(1)

# get to Rounding field
    if int(Settings.tsVersion) < 2015:
        myTools.pressF6(4)
        time.sleep(1)
        myTools.pressTAB(6)
    else:
        myTools.pressF6(7)
        time.sleep(1)
        myTools.pressTAB(5)               

    time.sleep(1)
    type("5") 
    
# save and close    
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_SlipsRoundMin():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-RoundMin","BA-RoundMin","Rounding Minutes","Rounding Minutes","Rounding Minutes")
    # create some slips
    baCommon.BA_Create_Slips("BA-RoundMin")
    # set up billing arrangement
    BA_Round_Minutes() 
    # print a bill to text
    baCommon.BA_Bill("BA-RoundMin",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-RoundMin1")
