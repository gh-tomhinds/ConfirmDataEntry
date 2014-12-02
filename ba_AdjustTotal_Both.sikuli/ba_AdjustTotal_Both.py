from sikuli import *
import logging
import myTools
import createClient
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fAdjustTotalBoth_Setup():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba AdjustTotalBoth")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-AdjTot-Both")
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

# switch to adjust total charges    
    type(Key.HOME)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("n",KeyModifier.ALT)
    type("25")
    time.sleep(1)   
    type(Key.TAB)    
    type(Key.RIGHT)    

    if int(Settings.tsVersion) < 2014:
        myTools.pressTAB(3)
    else:
        type("d",KeyModifier.ALT)
    type("Adjust Total Charges - Both")
    
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
def fAdjustTotal_Both():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-AdjTot-Both","BA-AdjTot-Both","Adjust Total - Both","Adjust Total - Both","Adjust Total - Both")
    # create some slips
    ba__Common.fCreate_BASlips("BA-AdjTot-Both")
    # set up billing arrangement
    fAdjustTotalBoth_Setup() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-AdjTot-Both",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-AdjTot-Both1")
