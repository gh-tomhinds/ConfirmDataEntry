from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fAdjustTotalTime_Setup():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba AdjustTotalTime")
    logging.debug("ba AdjustTotalTime")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-AdjTot-Time")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(4)

# switch to adjust total charges    
    type(Key.HOME)
    type(Key.DOWN)

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
    type("Adjust Total Charges - Time")

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
def fAdjustTotal_Time():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug(' ')
    logging.debug('BA_AdjustTotal_Time')

    # create a new client    
    client_Create.fCreate_Client("BA-AdjTot-Time","BA-AdjTot-Time","Adjust Total - Time","Adjust Total - Time","Adjust Total - Time")
    # create some slips
    ba__Common.fCreate_BASlips("BA-AdjTot-Time")
    # set up billing arrangement
    fAdjustTotalTime_Setup() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-AdjTot-Time",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-AdjTot-Time1")
