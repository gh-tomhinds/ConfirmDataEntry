from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fMaximumBoth_Setup():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba MaximumBoth")
    logging.debug("ba MaximumBoth")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Maximum-Both")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for both
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(3)
    
    type(Key.RIGHT)
    time.sleep(1)    
    type(Key.ENTER)

    if int(Settings.tsVersion) > 2014:
        type(Key.TAB)    
    
# switch to maximum
    type(Key.HOME)    
    myTools.pressDOWN(4)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("500")
    myTools.pressTAB(2)

    if int(Settings.tsVersion) > 2014:
        type(Key.TAB)
    
    type("Maximum FF - Both")
    
# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fMaximum_Both():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    client_Create.fCreate_Client("BA-Maximum-Both","BA-Maximum-Both","Maximum FF - Both","Maximum FF - Both","Maximum FF - Both")
    # create some slips
    ba__Common.fCreate_BASlips("BA-Maximum-Both")
    # set up billing arrangement
    fMaximumBoth_Setup() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-Maximum-Both",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-Maximum-Both1")
