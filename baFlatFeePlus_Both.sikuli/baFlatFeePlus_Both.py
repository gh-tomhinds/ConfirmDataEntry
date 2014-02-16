from sikuli import *
import logging
import myTools
import createClient
import baCommon
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_FlatFeePlusBoth_Arrangement():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-FFPlus-Both")
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
    
# switch to ffplus
    type(Key.HOME)
    myTools.pressDOWN(5)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("500")
    myTools.pressTAB(2)
    
    type("FF Plus - Both")

# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_FlatFeePlus_Both():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-FFPlus-Both","BA-FFPlus-Both","FF Plus - Both","FF Plus - Both","FF Plus - Both")
    # create some slips
    baCommon.BA_Create_Slips("BA-FFPlus-Both")
    # set up billing arrangement
    BA_FlatFeePlusBoth_Arrangement() 
    # print a bill to text
    baCommon.BA_Bill("BA-FFPlus-Both",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-FFPlus-Both1")
