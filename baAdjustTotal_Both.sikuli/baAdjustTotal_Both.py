from sikuli import *
import logging
import myTools
import createClient
import baCommon
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_AdjustTotalBoth_Arrangement():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba AdjustTotalBoth")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-AdjTot-Both")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for both
    baCommon.moveto_BAPage()
    myTools.pressTAB(3)
    
    type(Key.RIGHT)
    time.sleep(1)    
    type(Key.ENTER)  

    if int(Settings.tsVersion) > 2014:
        type(Key.TAB)

# switch to adjust total charges    
    type(Key.HOME)
    
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
    type("Adjust Total Charges - Both")
    
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
def BA_AdjustTotal_Both():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-AdjTot-Both","BA-AdjTot-Both","Adjust Total - Both","Adjust Total - Both","Adjust Total - Both")
    # create some slips
    baCommon.BA_Create_Slips("BA-AdjTot-Both")
    # set up billing arrangement
    BA_AdjustTotalBoth_Arrangement() 
    # print a bill to text
    baCommon.BA_Bill("BA-AdjTot-Both",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-AdjTot-Both1")
