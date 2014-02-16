from sikuli import *
import logging
import myTools
import createClient
import baCommon
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_MinimumHours_Arrangement():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-MinimumHours")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    baCommon.moveto_BAPage()
    myTools.pressTAB(4)
    
# switch to minimum
    type(Key.HOME)
    myTools.pressDOWN(9)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("1000")
    type(Key.TAB)
    type("1")
    type(Key.TAB)
    type("500")
    myTools.pressTAB(3)
    type("Minimum Hours FF")
# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_MinimumHours():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-MinimumHours","BA-MinimumHours","Minimum Hours FF","Minimum Hours FF","Minimum Hours FF")
    # create some slips
    baCommon.BA_Create_Slips("BA-MinimumHours")
    # set up billing arrangement
    BA_MinimumHours_Arrangement() 
    # print a bill to text
    baCommon.BA_Bill("BA-MinimumHours",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-MinimumHours1")
