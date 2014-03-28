from sikuli import *
import logging
import myTools
import createClient
import baCommon
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_ContingencyTime_Arrangement1():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Cont-Time")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    baCommon.moveto_BAPage()
    myTools.pressTAB(4)
    
# switch to contingency
    type(Key.HOME)
    myTools.pressDOWN(8)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("1000")
    myTools.pressTAB(3)
    type("Contingency - Time")
    
# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_ContingencyTime_Arrangement2():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Cont-Time")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement fields
    baCommon.moveto_BAPage()
    myTools.pressTAB(5)
    
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

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_Contingency_Time():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-Cont-Time","BA-Cont-Time","Contingency - Time","Contingency - Time","Contingency - Time")
    # create some slips
    baCommon.BA_Create_Slips("BA-Cont-Time")
    # set up billing arrangement
    BA_ContingencyTime_Arrangement1() 
    # print a bill to text
    baCommon.BA_Bill("BA-Cont-Time",1)
    # compare bill values
    baReviewBills.Review_Bill("BA-Cont-Time1")

    # create some more slips
    baCommon.BA_Create_Slips("BA-Cont-Time")
    # change billing arrangement
    BA_ContingencyTime_Arrangement2() 
    # print 2nd bill to text
    baCommon.BA_Bill("BA-Cont-Time",2)
    # compare 2nd bill's values
    baReviewBills.Review_Bill("BA-Cont-Time2")
