from sikuli import *
import logging
import myTools
import createClient
import ba_Common
import baReviewBills


# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_AdjustTotalExp_Arrangement():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba AdjustTotalExp")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-AdjTot-Exp")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for expense
    ba_Common.moveto_BAPage()
    myTools.pressTAB(5)

# switch to adjust total charges    
    type(Key.HOME)
    type(Key.DOWN)

# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("n",KeyModifier.ALT)
    type("25")
    time.sleep(1)   
    type(Key.TAB)    
    type(Key.RIGHT)

    if int(Settings.tsVersion) < 2014:
        myTools.pressTAB(3)
    else:
        type("d",KeyModifier.ALT)
    type("Adjust Total Charges - Exp")
    
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
def BA_AdjustTotal_Exp():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-AdjTot-Exp","BA-AdjTot-Exp","Adjust Total - Expense","Adjust Total - Expense","Adjust Total - Expense")
    # create some slips
    ba_Common.BA_Create_Slips("BA-AdjTot-Exp")
    # set up billing arrangement
    BA_AdjustTotalExp_Arrangement() 
    # print a bill to text
    ba_Common.BA_Bill("BA-AdjTot-Exp",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-AdjTot-Exp1")
