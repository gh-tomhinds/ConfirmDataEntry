from sikuli import *
import logging
import myTools
import createClient
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fContingencyExp_Setup1():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba ContExp1")
    logging.debug("ba ContExp1")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Cont-Exp")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for exp
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
    
# switch to contingency
    type(Key.HOME)
    myTools.pressDOWN(8)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("500")
    myTools.pressTAB(3)
    type("Contingency - Expense")
    
# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fContingencyExp_Setup2():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba ContExp2")
    logging.debug("ba ContExp2")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Cont-Exp")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for exp
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(6)
    
# enter details    
    type(Key.ENTER)
    time.sleep(1)
    if int(Settings.tsVersion) > 2014:
        myTools.pressTAB(1)
    else:
        myTools.pressTAB(2)
    
    type(Key.DOWN)
    
# save and close    
    type(Key.ENTER)
    type("s",KeyModifier.CTRL)
    
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fContingency_Exp():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-Cont-Exp","BA-Cont-Exp","Contingency - Exp","Contingency - Exp","Contingency - Exp")
    # create some slips
    ba__Common.fCreate_BASlips("BA-Cont-Exp")
    # set up billing arrangement
    fContingencyExp_Setup1() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-Cont-Exp",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-Cont-Exp1")

    # create some more slips
    ba__Common.fCreate_BASlips("BA-Cont-Exp")
    # change billing arrangement
    fContingencyExp_Setup2() 
    # print the 2nd bill to text
    ba__Common.fPrint_BABill("BA-Cont-Exp",2)
    # compare 2nd bill's values
    ba__ReviewBills.fReview_BABill("BA-Cont-Exp2")
