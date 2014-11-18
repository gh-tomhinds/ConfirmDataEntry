from sikuli import *
import logging
import myTools
import createClient
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_AdjustTimekeeperTime_Arrangement():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba AdjustTimekeeperTime")
    logging.debug("ba AdjustTimekeeperTime")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-AdjTK-Time")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    ba__Common.moveto_BAPage()        
    myTools.pressTAB(4)
    
# switch to adjust by timekeeper    
    type(Key.HOME)
    myTools.pressDOWN(2)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("n",KeyModifier.ALT)
    type("t")    
    type(Key.TAB)    
    type("25")
    type(Key.TAB)    
    type(Key.RIGHT)

    if int(Settings.tsVersion) < 2014:
        myTools.pressTAB(3)
    else:
        type("d",KeyModifier.ALT)
    type("Adjust Timekeeper - Time")

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
def BA_AdjustTimekeeper_Time():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug(' ')
    logging.debug('BA_AdjustTimekeeper_Time')

    # create a new client    
    createClient.Create_Client("BA-AdjTK-Time","BA-AdjTK-Time","Adjust Timekeeper - Time","Adjust Timekeeper - Time","Adjust Timekeeper - Time")
    # create some slips
    ba__Common.BA_Create_Slips("BA-AdjTK-Time")
    # set up billing arrangement
    BA_AdjustTimekeeperTime_Arrangement() 
    # print a bill to text
    ba__Common.BA_Bill("BA-AdjTK-Time",1)
    # compare at bill values
    ba__ReviewBills.Review_Bill("BA-AdjTK-Time1")
