from sikuli import *
import logging
import myTools
import createClient
import baCommon
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_AdjustTask_Arrangement():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-AdjTask")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    baCommon.moveto_BAPage()       
    myTools.pressTAB(4)
    
# switch to adjust by tasks    
    type(Key.HOME)
    myTools.pressDOWN(3)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("n",KeyModifier.ALT)
    type("bu")    
    type(Key.TAB)    
    type("25")
    type(Key.TAB)    
    type(Key.RIGHT)
    
    if int(Settings.tsVersion) < 2014:
        myTools.pressTAB(3)
    else:
        type("d",KeyModifier.ALT)
    type("Adjust Task")
    
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
def BA_AdjustTask():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug(' ')
    logging.debug('BA_AdjustTask')

    # create a new client    
    createClient.Create_Client("BA-AdjTask","BA-AdjTask","Adjust Task","Adjust Task","Adjust Task")
    # create some slips
    baCommon.BA_Create_Slips("BA-AdjTask")
    # set up billing arrangement
    BA_AdjustTask_Arrangement() 
    # print a bill to text
    baCommon.BA_Bill("BA-AdjTask",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-AdjTask1")
