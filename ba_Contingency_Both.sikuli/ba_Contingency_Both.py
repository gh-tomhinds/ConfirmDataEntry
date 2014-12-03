from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fContingencyBoth_Setup1():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba ContBoth1")
    logging.debug("ba ContBoth1")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Cont-Both")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for both
    ba__Common.fMoveto_BAPage()
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
def fContingencyBoth_Setup2():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba ContBoth2")
    logging.debug("ba ContBoth2")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Cont-Both")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for both
    ba__Common.fMoveto_BAPage()
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
def fContingency_Both():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    client_Create.fCreate_Client("BA-Cont-Both","BA-Cont-Both","Contingency - Both","Contingency - Both","Contingency - Both")
    # create some slips
    ba__Common.fCreate_BASlips("BA-Cont-Both")
    # set up billing arrangement
    fContingencyBoth_Setup1() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-Cont-Both",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-Cont-Both1")

    # create some more slips
    ba__Common.fCreate_BASlips("BA-Cont-Both")
    # change billing arrangement
    fContingencyBoth_Setup2() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-Cont-Both",2)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-Cont-Both2")
