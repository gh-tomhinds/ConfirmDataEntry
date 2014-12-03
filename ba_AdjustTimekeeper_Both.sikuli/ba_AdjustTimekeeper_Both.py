from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fAdjustTimekeeperBoth_Setup():
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
    ba__Common.fMoveto_BAPage()
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
def fAdjustTimekeeper_Both():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug(' ')
    logging.debug('BA_AdjustTimekeeper_Both')

    # create a new client    
    client_Create.fCreate_Client("BA-AdjTK-Both","BA-AdjTK-Both","Adjust Timekeeper - Both","Adjust Timekeeper - Both","Adjust Timekeeper - Both")
    # create some slips
    ba__Common.fCreate_BASlips("BA-AdjTK-Both")
    # set up billing arrangement
    fAdjustTimekeeperBoth_Setup() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-AdjTK-Both",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-AdjTK-Both1")
