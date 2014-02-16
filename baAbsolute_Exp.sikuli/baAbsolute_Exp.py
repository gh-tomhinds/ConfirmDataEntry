from sikuli import *
import logging
import myTools
import createClient
import baCommon
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_AbsoluteExp_Arrangement():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Absolute-Exp")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for exp
    baCommon.moveto_BAPage()
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

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_Absolute_Exp():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-Absolute-Exp","BA-Absolute-Exp","Absolute FF - Expense","Absolute FF - Expense","Absolute FF - Expense")
    # create some slips
    baCommon.BA_Create_Slips("BA-Absolute-Exp")
    # set up billing arrangement
    BA_AbsoluteExp_Arrangement() 
    # print a bill to text
    baCommon.BA_Bill("BA-Absolute-Exp",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-Absolute-Exp1")
