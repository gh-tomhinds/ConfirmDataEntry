from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fMaximumExp_Setup():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba MaximumExp")
    logging.debug("ba MaximumExp")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Maximum-Exp")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for exp
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
    
# switch to maximum
    type(Key.HOME)
    myTools.pressDOWN(6)
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("500")
    myTools.pressTAB(2)
    type("Maximum FF - Expense")
# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fMaximum_Exp():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    client_Create.fCreate_Client("BA-Maximum-Exp","BA-Maximum-Exp","Maximum FF - Exp","Maximum FF - Exp","Maximum FF - Exp")
    # create some slips
    ba__Common.fCreate_BASlips("BA-Maximum-Exp")
    # set up billing arrangement
    fMaximumExp_Setup() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-Maximum-Exp",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-Maximum-Exp1")
