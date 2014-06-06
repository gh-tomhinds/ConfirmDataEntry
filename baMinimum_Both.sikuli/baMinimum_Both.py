from sikuli import *
import logging
import myTools
import createClient
import baCommon
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_MinimumBoth_Arrangement():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba MinimumBoth")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Minimum-Both")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for both
    baCommon.moveto_BAPage()
    myTools.pressTAB(3)
    
    type(Key.RIGHT)
    time.sleep(1)    
    type(Key.ENTER)

    if int(Settings.tsVersion) > 2014:
        type(Key.TAB)
    
# switch to minimum
    type(Key.HOME)
    myTools.pressDOWN(3)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("5000")
    myTools.pressTAB(2)

    if int(Settings.tsVersion) > 2014:
        type(Key.TAB)
    
    type("Minimum FF - Both")
    
# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_Minimum_Both():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-Minimum-Both","BA-Minimum-Both","Minimum FF - Both","Minimum FF - Both","Minimum FF - Both")
    # create some slips
    baCommon.BA_Create_Slips("BA-Minimum-Both")
    # set up billing arrangement
    BA_MinimumBoth_Arrangement() 
    # print a bill to text
    baCommon.BA_Bill("BA-Minimum-Both",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-Minimum-Both1")
