from sikuli import *
import logging
import myTools
import createClient
import baCommon
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_AdjustTotalTime_Arrangement():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-AdjTot-Time")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    baCommon.moveto_BAPage()
    myTools.pressTAB(4)

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
    type("Adjust Total Charges - Time")

# save and close
    type(Key.TAB)
    type(Key.SPACE)
    myTools.pressTAB(4)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_AdjustTotal_Time():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug(' ')
    logging.debug('BA_AdjustTotal_Time')

    # create a new client    
    createClient.Create_Client("BA-AdjTot-Time","BA-AdjTot-Time","Adjust Total - Time","Adjust Total - Time","Adjust Total - Time")
    # create some slips
    baCommon.BA_Create_Slips("BA-AdjTot-Time")
    # set up billing arrangement
    BA_AdjustTotalTime_Arrangement() 
    # print a bill to text
    baCommon.BA_Bill("BA-AdjTot-Time",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-AdjTot-Time1")
