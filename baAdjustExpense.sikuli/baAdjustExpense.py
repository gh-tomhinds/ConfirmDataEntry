from sikuli import *
import logging
import myTools
import createClient
import baCommon
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_AdjustExpense_Arrangement():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba AdjustExp")
    logging.debug("ba AdjustExp")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-AdjExpense")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    baCommon.moveto_BAPage()
    myTools.pressTAB(5)

# switch to adjust by expense
    type(Key.HOME)
    myTools.pressDOWN(3)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("n",KeyModifier.ALT)
    type("p")    
    type(Key.TAB)    
    type("25")
    type(Key.TAB)    
    type(Key.RIGHT)    
    
    if int(Settings.tsVersion) < 2014:
        myTools.pressTAB(3)
    else:
        type("d",KeyModifier.ALT)
    type("Adjust Expense")
    
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
def BA_AdjustExpense():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug(' ')
    logging.debug('BA_AdjustExpense')

    # create a new client    
    createClient.Create_Client("BA-AdjExpense","BA-AdjExpense","Adjust Expense","Adjust Expense","Adjust Expense")
    # create some slips
    baCommon.BA_Create_Slips("BA-AdjExpense")
    # set up billing arrangement
    BA_AdjustExpense_Arrangement() 
    # print a bill to text
    baCommon.BA_Bill("BA-AdjExpense",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-AdjExpense1")
