from sikuli import *
import logging
import myTools
import createClient
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_InterimTotal_Arrangement1():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba InterimTot1")
    logging.debug("ba InterimTot1")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-InterimTot")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    ba__Common.moveto_BAPage()
    myTools.pressTAB(4)
    
# switch to interim
    type(Key.HOME)
    myTools.pressDOWN(13)
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("500")
    time.sleep(1)    
    type(Key.ENTER)
# save and close    
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_InterimTotal_Arrangement2():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba InterimTot2")
    logging.debug("ba InterimTot2")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-InterimTot")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    ba__Common.moveto_BAPage()
    myTools.pressTAB(5)
    
# enter details    
    type(Key.ENTER)
    time.sleep(1)    
    type("600")
    time.sleep(1)    
    type(Key.ENTER)
# save and close    
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_InterimTotal_Arrangement3():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba InterimTot3")
    logging.debug("ba InterimTot3")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-InterimTot")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    ba__Common.moveto_BAPage()
    myTools.pressTAB(5)
    
# enter details    
    type(Key.ENTER)
    time.sleep(1)    
    type("700")
    time.sleep(1)    

    type("u",KeyModifier.ALT)
    type(Key.END)
    type(Key.ENTER)

# save and close    
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_InterimTotal():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-InterimTot","BA-InterimTot","Interim Total FF","Interim Total FF","Interim Total FF")
    # create some slips
    ba__Common.BA_Create_Slips("BA-InterimTot")
    # set up billing arrangement
    BA_InterimTotal_Arrangement1() 
    # print a bill to text
    ba__Common.BA_Bill("BA-InterimTot",1)
    # compare at bill values
    ba__ReviewBills.Review_Bill("BA-InterimTot1")

    # create some slips
    ba__Common.BA_Create_Slips("BA-InterimTot")
    # set up billing arrangement
    BA_InterimTotal_Arrangement2() 
    # print a bill to text
    ba__Common.BA_Bill("BA-InterimTot",2)
    # compare at bill values
    ba__ReviewBills.Review_Bill("BA-InterimTot2")

    # create some slips
    ba__Common.BA_Create_Slips("BA-InterimTot")
    # set up billing arrangement
    BA_InterimTotal_Arrangement3() 
    # print a bill to text
    ba__Common.BA_Bill("BA-InterimTot",3)
    # compare at bill values
    ba__ReviewBills.Review_Bill("BA-InterimTot3")
