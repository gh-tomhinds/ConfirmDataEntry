from sikuli import *
import logging
import myTools
import createClient
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fMinimumHours_Setup():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba MinHours")
    logging.debug("ba MinHours")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-MinimumHours")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(4)
    
# switch to minimum
    type(Key.HOME)
    myTools.pressDOWN(9)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("1000")
    type(Key.TAB)
    type("1")
    type(Key.TAB)
    type("500")
    myTools.pressTAB(3)
    type("Minimum Hours FF")
# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fMinimumHours():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-MinimumHours","BA-MinimumHours","Minimum Hours FF","Minimum Hours FF","Minimum Hours FF")
    # create some slips
    ba__Common.fCreate_BASlips("BA-MinimumHours")
    # set up billing arrangement
    fMinimumHours_Setup() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-MinimumHours",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-MinimumHours1")
