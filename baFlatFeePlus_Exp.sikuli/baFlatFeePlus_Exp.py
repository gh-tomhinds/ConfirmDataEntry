from sikuli import *
import logging
import myTools
import createClient
import baCommon
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_FlatFeePlusExp_Arrangement():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-FFPlus-Exp")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for exp
    baCommon.moveto_BAPage()
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

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_FlatFeePlus_Exp():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-FFPlus-Exp","BA-FFPlus-Exp","FF Plus - Exp","FF Plus - Exp","FF Plus - Exp")
    # create some slips
    baCommon.BA_Create_Slips("BA-FFPlus-Exp")
    # set up billing arrangement
    BA_FlatFeePlusExp_Arrangement() 
    # print a bill to text
    baCommon.BA_Bill("BA-FFPlus-Exp",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-FFPlus-Exp1")
