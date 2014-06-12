from sikuli import *
import logging
import myTools
import createClient
import baCommon
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_Round_Dollars():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba RoundDollars")
    logging.debug("ba RoundDollars")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-RoundDol")
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
    type(Key.TAB)
    type("u")
    
# save and close    
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_SlipsRoundDol():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-RoundDol","BA-RoundDol","Rounding Dollars","Rounding Dollars","Rounding Dollars")
    # create some slips
    baCommon.BA_Create_Slips("BA-RoundDol")
    # set up billing arrangement
    BA_Round_Dollars() 
    # print a bill to text
    baCommon.BA_Bill("BA-RoundDol",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-RoundDol1")
