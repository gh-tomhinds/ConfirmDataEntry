from sikuli import *
import logging
import myTools
import createClient
import baCommon
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_ContingencyExp_Arrangement1():
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
    baCommon.moveto_BAPage()
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
def BA_ContingencyExp_Arrangement2():
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
    baCommon.moveto_BAPage()
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
def BA_Contingency_Exp():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-Cont-Exp","BA-Cont-Exp","Contingency - Exp","Contingency - Exp","Contingency - Exp")
    # create some slips
    baCommon.BA_Create_Slips("BA-Cont-Exp")
    # set up billing arrangement
    BA_ContingencyExp_Arrangement1() 
    # print a bill to text
    baCommon.BA_Bill("BA-Cont-Exp",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-Cont-Exp1")

    # create some more slips
    baCommon.BA_Create_Slips("BA-Cont-Exp")
    # change billing arrangement
    BA_ContingencyExp_Arrangement2() 
    # print the 2nd bill to text
    baCommon.BA_Bill("BA-Cont-Exp",2)
    # compare 2nd bill's values
    baReviewBills.Review_Bill("BA-Cont-Exp2")
