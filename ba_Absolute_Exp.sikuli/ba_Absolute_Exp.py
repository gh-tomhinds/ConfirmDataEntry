from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fAbsoluteExp_Setup():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba AbsoluteExp")
    logging.debug("ba AbsoluteExp")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Absolute-Exp")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for exp
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
    
# switch to absolute
    type(Key.HOME)
    myTools.pressDOWN(4)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("1000")
    myTools.pressTAB(3)
    type("Absolute FF - Expense")
    
# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fAbsolute_Exp():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    client_Create.fCreate_Client("BA-Absolute-Exp","BA-Absolute-Exp","Absolute FF - Expense","Absolute FF - Expense","Absolute FF - Expense")
    # create some slips
    ba__Common.fCreate_BASlips("BA-Absolute-Exp")
    # set up billing arrangement
    fAbsoluteExp_Setup() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-Absolute-Exp",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-Absolute-Exp1")
