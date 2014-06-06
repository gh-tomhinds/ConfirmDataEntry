from sikuli import *
import logging
import myTools
import createClient
import baCommon
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_ContingencyBoth_Arrangement1():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba ContBoth1")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Cont-Both")
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
    
# switch to cont
    type(Key.HOME)
    myTools.pressDOWN(6)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("500")
    myTools.pressTAB(3)
    type("Contingency - Both")
    
# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    type("s",KEY_CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_ContingencyBoth_Arrangement2():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba ContBoth2")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Cont-Both")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for both
    baCommon.moveto_BAPage()
    myTools.pressTAB(5)
    
    time.sleep(1)    
    type(Key.ENTER)
    time.sleep(1)
    
# enter details    

    if int(Settings.tsVersion) > 2014:
        myTools.pressTAB(1)
    else:
        myTools.pressTAB(2)
    
    type(Key.DOWN)
    type(Key.ENTER)
    
# save and close    
    time.sleep(1)    
    type("s",KeyModifier.CTRL)   

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_Contingency_Both():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-Cont-Both","BA-Cont-Both","Contingency - Both","Contingency - Both","Contingency - Both")
    # create some slips
    baCommon.BA_Create_Slips("BA-Cont-Both")
    # set up billing arrangement
    BA_ContingencyBoth_Arrangement1() 
    # print a bill to text
    baCommon.BA_Bill("BA-Cont-Both",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-Cont-Both1")

    # create some more slips
    baCommon.BA_Create_Slips("BA-Cont-Both")
    # change billing arrangement
    BA_ContingencyBoth_Arrangement2() 
    # print a bill to text
    baCommon.BA_Bill("BA-Cont-Both",2)
    # compare at bill values
    baReviewBills.Review_Bill("BA-Cont-Both2")
