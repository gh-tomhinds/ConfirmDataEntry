from sikuli import *
import logging
import myTools
import createClient
import ba_Common
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_MaximumExp_Arrangement():
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
    ba_Common.moveto_BAPage()
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
def BA_Maximum_Exp():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-Maximum-Exp","BA-Maximum-Exp","Maximum FF - Exp","Maximum FF - Exp","Maximum FF - Exp")
    # create some slips
    ba_Common.BA_Create_Slips("BA-Maximum-Exp")
    # set up billing arrangement
    BA_MaximumExp_Arrangement() 
    # print a bill to text
    ba_Common.BA_Bill("BA-Maximum-Exp",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-Maximum-Exp1")
