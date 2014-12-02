from sikuli import *
import logging
import myTools
import createClient
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fFlatFeePlusExp_Setup():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba FFPlusExp")
    logging.debug("ba FFPlusExp")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-FFPlus-Exp")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for exp
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
    
# switch to flat fee plus charges
    type(Key.HOME)
    myTools.pressDOWN(7)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("500")
    myTools.pressTAB(2)
    type("FF Plus - Expense")
# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fFlatFeePlus_Exp():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-FFPlus-Exp","BA-FFPlus-Exp","FF Plus - Exp","FF Plus - Exp","FF Plus - Exp")
    # create some slips
    ba__Common.fCreate_BASlips("BA-FFPlus-Exp")
    # set up billing arrangement
    fFlatFeePlusExp_Setup() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-FFPlus-Exp",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-FFPlus-Exp1")
