from sikuli import *
import logging
import myTools
import createClient
import ba_Common
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_AbsoluteBoth_Arrangement():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba AbsoluteBoth")
    logging.debug("ba AbsoluteBoth")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Absolute-Both")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for both
    ba_Common.moveto_BAPage()
    myTools.pressTAB(3)
    
    type(Key.RIGHT)
    time.sleep(1)    
    type(Key.ENTER)

    if int(Settings.tsVersion) > 2014:
        type(Key.TAB)  
    
# switch to absolute
    type(Key.HOME)
    myTools.pressDOWN(2)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("1000")
    myTools.pressTAB(2)

    if int(Settings.tsVersion) > 2014:
        type(Key.TAB)

    type("Absolute FF - Both")
    
# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_Absolute_Both():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-Absolute-Both","BA-Absolute-Both","Absolute FF - Both","Absolute FF - Both","Absolute FF - Both")
    # create some slips
    ba_Common.BA_Create_Slips("BA-Absolute-Both")
    # set up billing arrangement
    BA_AbsoluteBoth_Arrangement() 
    # print a bill to text
    ba_Common.BA_Bill("BA-Absolute-Both",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-Absolute-Both1")
