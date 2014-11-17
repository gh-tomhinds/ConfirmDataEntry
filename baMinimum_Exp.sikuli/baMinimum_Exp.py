from sikuli import *
import logging
import myTools
import createClient
import ba_Common
import ba_ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_MinimumExp_Arrangement():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba MinimumExp")
    logging.debug("ba MinimumExp")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Minimum-Exp")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for exp
    ba_Common.moveto_BAPage()
    myTools.pressTAB(5)
    
# switch to minimum
    type(Key.HOME)
    myTools.pressDOWN(5)
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("5000")
    myTools.pressTAB(2)
    type("Minimum FF - Expense")
# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_Minimum_Exp():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-Minimum-Exp","BA-Minimum-Exp","Minimum FF - Exp","Minimum FF - Exp","Minimum FF - Exp")
    # create some slips
    ba_Common.BA_Create_Slips("BA-Minimum-Exp")
    # set up billing arrangement
    BA_MinimumExp_Arrangement() 
    # print a bill to text
    ba_Common.BA_Bill("BA-Minimum-Exp",1)
    # compare at bill values
    ba_ReviewBills.Review_Bill("BA-Minimum-Exp1")
