from sikuli import *
import logging
import myTools
import createClient
import ba_Common
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_AdjustTimekeeperBoth_Arrangement():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba AdjustTimekeeperBoth")
    logging.debug("ba AdjustTimekeeperBoth")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-AdjTK-Both")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for both
    ba_Common.moveto_BAPage()
    myTools.pressTAB(3)
    
    type(Key.RIGHT)
    time.sleep(1)    
    type(Key.ENTER)  

# extra TAB starting in TS2015
    if int(Settings.tsVersion) > 2014:
        type(Key.TAB)

# switch to adjust by timekeeper    
    type(Key.HOME)
    myTools.pressDOWN(1)    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("n",KeyModifier.ALT)
    type("t")    
    type(Key.TAB)    
    type("25")
    type(Key.TAB)    
    type(Key.RIGHT)    

    if int(Settings.tsVersion) < 2014:
        myTools.pressTAB(3)
    else:
        type("d",KeyModifier.ALT)
    type("Adjust Timekeeper - Both")

# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    myTools.pressTAB(4)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_AdjustTimekeeper_Both():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug(' ')
    logging.debug('BA_AdjustTimekeeper_Both')

    # create a new client    
    createClient.Create_Client("BA-AdjTK-Both","BA-AdjTK-Both","Adjust Timekeeper - Both","Adjust Timekeeper - Both","Adjust Timekeeper - Both")
    # create some slips
    ba_Common.BA_Create_Slips("BA-AdjTK-Both")
    # set up billing arrangement
    BA_AdjustTimekeeperBoth_Arrangement() 
    # print a bill to text
    ba_Common.BA_Bill("BA-AdjTK-Both",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-AdjTK-Both1")
