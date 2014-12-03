from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fMinimumExp_Setup():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba MinimumExp")
    logging.debug("ba MinimumExp")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Minimum-Exp")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for exp
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
    
# switch to minimum
    type(Key.HOME)
    myTools.pressDOWN(5)
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("5000")
    myTools.pressTAB(2)
    type("Minimum FF - Expense")
# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fMinimum_Exp():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    client_Create.fCreate_Client("BA-Minimum-Exp","BA-Minimum-Exp","Minimum FF - Exp","Minimum FF - Exp","Minimum FF - Exp")
    # create some slips
    ba__Common.fCreate_BASlips("BA-Minimum-Exp")
    # set up billing arrangement
    fMinimumExp_Setup() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-Minimum-Exp",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-Minimum-Exp1")
