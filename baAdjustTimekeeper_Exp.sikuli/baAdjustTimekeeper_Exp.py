from sikuli import *
import logging
import myTools
import createClient
import baCommon
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_AdjustTimekeeperExp_Arrangement():
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
    baCommon.moveto_BAPage()
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
def BA_AdjustTimekeeper_Exp():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug(' ')
    logging.debug('BA_AdjustTimekeeper_Exp')

    # create a new client    
    createClient.Create_Client("BA-AdjTK-Exp","BA-AdjTK-Exp","Adjust Timekeeper - Expense","Adjust Timekeeper - Expense","Adjust Timekeeper - Expense")
    # create some slips
    baCommon.BA_Create_Slips("BA-AdjTK-Exp")
    # set up billing arrangement
    BA_AdjustTimekeeperExp_Arrangement() 
    # print a bill to text
    baCommon.BA_Bill("BA-AdjTK-Exp",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-AdjTK-Exp1")
