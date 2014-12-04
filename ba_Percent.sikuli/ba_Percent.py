from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fPercent_Setup1():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba Percent1")
    logging.debug("ba Percent1")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Percent")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(4)
    
# switch to contingency
    type(Key.HOME)
    myTools.pressDOWN(10)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("1000")

# enter phases

    myTools.pressTAB(3)
    
    type(Key.SPACE)
    time.sleep(1)    
    type("Phase1")
    type(Key.TAB)
    type("50")
    myTools.pressTAB(3)
    type("25")   
    type(Key.ENTER)
    
    type(Key.SPACE)
    time.sleep(1)    
    type("Phase2")
    type(Key.TAB)
    type("30")
    myTools.pressTAB(3)
    type("25")   
    type(Key.ENTER)
    
    type(Key.SPACE)
    time.sleep(1)    
    type("Phase3")
    type(Key.TAB)
    type("20")
    myTools.pressTAB(3)
    type("25")   
    type(Key.ENTER)

    if int(Settings.tsVersion) > 2014:
        myTools.pressTAB(5)
    else:
        myTools.pressTAB(6)
    type("Percent Complete")

# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    time.sleep(1)    
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fPercent_Setup2():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba Percent2")
    logging.debug("ba Percent2")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Percent")
    type(Key.ENTER)
    time.sleep(1)

# enter details    
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
    type(Key.ENTER)
    time.sleep(1)    

    myTools.pressTAB(2)
    type("o",KeyModifier.CTRL)
    myTools.pressTAB(4)
    type("80")
    type(Key.ENTER)
    time.sleep(1)    

    type(Key.DOWN)
    type("o",KeyModifier.CTRL)
    myTools.pressTAB(4)
    type("80")
    type(Key.ENTER)
    time.sleep(1)    

    type(Key.DOWN)
    type("o",KeyModifier.CTRL)
    myTools.pressTAB(4)
    type("80")
    type(Key.ENTER)
    time.sleep(1)    

    # save and close

    if int(Settings.tsVersion) > 2014:
        myTools.pressTAB(8)        
    else:
        myTools.pressTAB(9)

    type(Key.SPACE)
    time.sleep(1)    
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fPercent_Setup3():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba Percent3")
    logging.debug("ba Percent3")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Percent")
    type(Key.ENTER)
    time.sleep(1)

# enter details    
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
    type(Key.ENTER)
    time.sleep(1)    

    type(Key.TAB)
    type(Key.DOWN)
    type(Key.TAB)
    
    type("o",KeyModifier.CTRL)
    myTools.pressTAB(4)
    type("100")
    type(Key.ENTER)
    time.sleep(1)    

    type(Key.DOWN)
    type("o",KeyModifier.CTRL)
    myTools.pressTAB(4)
    type("100")
    type(Key.ENTER)
    time.sleep(1)    

    type(Key.DOWN)
    type("o",KeyModifier.CTRL)
    myTools.pressTAB(4)
    type("100")
    type(Key.ENTER)
    time.sleep(1)    

    # save and close

    if int(Settings.tsVersion) > 2014:
        myTools.pressTAB(8)        
    else:
        myTools.pressTAB(9)

    type(Key.SPACE)
    time.sleep(1)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fPercent():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    client_Create.fCreate_Client("BA-Percent","BA-Percent","Percent Comp","Percent Comp","Percent Comp")
    # create some slips
    ba__Common.fCreate_BASlips("BA-Percent")
    # set up billing arrangement
    fPercent_Setup1() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-Percent",1)
    # compare bill values
    ba__ReviewBills.fReview_BABill("BA-Percent1")

    # create some more slips
    ba__Common.fCreate_BASlips("BA-Percent")
    # set up billing arrangement
    fPercent_Setup2() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-Percent",2)
    # compare bill values
    ba__ReviewBills.fReview_BABill("BA-Percent2")

    # create some more slips
    ba__Common.fCreate_BASlips("BA-Percent")
    # set up billing arrangement
    fPercent_Setup3() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-Percent",3)
    # compare bill values
    ba__ReviewBills.fReview_BABill("BA-Percent3")
