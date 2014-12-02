from sikuli import *
import logging
import myTools
import createClient
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fAdjustTask_Setup():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba AdjustTask")
    logging.debug("ba AdjustTask")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-AdjTask")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    ba__Common.fMoveto_BAPage()       
    myTools.pressTAB(4)
    
# switch to adjust by tasks    
    type(Key.HOME)
    myTools.pressDOWN(3)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("n",KeyModifier.ALT)
    type("bu")    
    type(Key.TAB)    
    type("25")
    type(Key.TAB)    
    type(Key.RIGHT)
    
    if int(Settings.tsVersion) < 2014:
        myTools.pressTAB(3)
    else:
        type("d",KeyModifier.ALT)
    type("Adjust Task")
    
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
def fAdjustTask():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug(' ')
    logging.debug('BA_AdjustTask')

    # create a new client    
    createClient.Create_Client("BA-AdjTask","BA-AdjTask","Adjust Task","Adjust Task","Adjust Task")
    # create some slips
    ba__Common.fCreate_BASlips("BA-AdjTask")
    # set up billing arrangement
    fAdjustTask_Setup() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-AdjTask",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-AdjTask1")
