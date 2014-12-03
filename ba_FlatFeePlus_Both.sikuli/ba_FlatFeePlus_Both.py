from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fFlatFeePlusBoth_Setup():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba FFPlusBoth")
    logging.debug("ba FFPlusBoth")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-FFPlus-Both")
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

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fFlatFeePlus_Both():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    client_Create.fCreate_Client("BA-FFPlus-Both","BA-FFPlus-Both","FF Plus - Both","FF Plus - Both","FF Plus - Both")
    # create some slips
    ba__Common.fCreate_BASlips("BA-FFPlus-Both")
    # set up billing arrangement
    fFlatFeePlusBoth_Setup() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-FFPlus-Both",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-FFPlus-Both1")
