from sikuli import *
import logging
import myTools
import createClient
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fAdjustTimekeeperExp_Setup():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba AdjustTimekeeperExp")
    logging.debug("ba AdjustTimekeeperExp")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-AdjTK-Exp")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for exp
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
        
# switch to adjust by timekeeper    
    type(Key.HOME)
    myTools.pressDOWN(2)    

# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("n",KeyModifier.ALT)
    type("sh")    
    type(Key.TAB)    
    type("25")
    type(Key.TAB)    
    type(Key.RIGHT)    

    if int(Settings.tsVersion) < 2014:
        myTools.pressTAB(3)
    else:
        type("d",KeyModifier.ALT)
    type("Adjust Timekeeper - Exp")

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
def fAdjustTimekeeper_Exp():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug(' ')
    logging.debug('BA_AdjustTimekeeper_Exp')

    # create a new client    
    createClient.Create_Client("BA-AdjTK-Exp","BA-AdjTK-Exp","Adjust Timekeeper - Expense","Adjust Timekeeper - Expense","Adjust Timekeeper - Expense")
    # create some slips
    ba__Common.fCreate_BASlips("BA-AdjTK-Exp")
    # set up billing arrangement
    fAdjustTimekeeperExp_Setup() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-AdjTK-Exp",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-AdjTK-Exp1")
