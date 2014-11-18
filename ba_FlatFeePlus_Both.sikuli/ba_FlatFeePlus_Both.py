from sikuli import *
import logging
import myTools
import createClient
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_FlatFeePlusBoth_Arrangement():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba FFPlusBoth")
    logging.debug("ba FFPlusBoth")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-FFPlus-Both")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for both
    ba__Common.moveto_BAPage()
    myTools.pressTAB(3)
    
    type(Key.RIGHT)
    time.sleep(1)    
    type(Key.ENTER)

    if int(Settings.tsVersion) > 2014:
        type(Key.TAB)    
    
# switch to ffplus
    type(Key.HOME)
    myTools.pressDOWN(5)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("500")
    myTools.pressTAB(2)
    
    type("FF Plus - Both")

# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_FlatFeePlus_Both():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-FFPlus-Both","BA-FFPlus-Both","FF Plus - Both","FF Plus - Both","FF Plus - Both")
    # create some slips
    ba__Common.BA_Create_Slips("BA-FFPlus-Both")
    # set up billing arrangement
    BA_FlatFeePlusBoth_Arrangement() 
    # print a bill to text
    ba__Common.BA_Bill("BA-FFPlus-Both",1)
    # compare at bill values
    ba__ReviewBills.Review_Bill("BA-FFPlus-Both1")
