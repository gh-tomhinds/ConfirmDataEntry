from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fInterimActivity_Setup1():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba InterimAct1")
    logging.debug("ba InterimAct1")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-InterimAct")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(4)
    
# switch to Interim
    type(Key.END)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1) 
    type(Key.DOWN)
    time.sleep(1) 
    type("o",KeyModifier.ALT)    
    type("500")
    time.sleep(1)    
    type(Key.ENTER)
    time.sleep(1)    
    type(Key.ENTER)
# save and close    
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fInterimActivity_Setup2():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba InterimAct2")
    logging.debug("ba InterimAct2")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-InterimAct")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
    
# enter details    
    type(Key.ENTER)
    time.sleep(1)
    type(Key.DOWN)
    time.sleep(1)
    type("o",KeyModifier.ALT)        
    type("600")
    time.sleep(1)    
    type(Key.ENTER)
    time.sleep(1)    
    type(Key.ENTER)
    
# save and close    
    type("s",KeyModifier.CTRL)
    time.sleep(1)

    if int(Settings.tsVersion) > 2014:
        if exists("are_you_sure.png"):
            type("y",KeyModifier.ALT)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fInterimActivity_Setup3():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba InterimAct3")
    logging.debug("ba InterimAct3")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-InterimAct")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
    
# enter details    
    type(Key.ENTER)
    time.sleep(1)
    type(Key.DOWN)
    time.sleep(1)
    type("o",KeyModifier.ALT)        
    type("700")
    time.sleep(1)    
    type(Key.ENTER)
    time.sleep(1)    
    type("u",KeyModifier.ALT)
    type(Key.DOWN)
    type(Key.ENTER)
    
# save and close    
    type("s",KeyModifier.CTRL)
    time.sleep(1)

    if int(Settings.tsVersion) > 2014:
        if exists("are_you_sure.png"):
            type("y",KeyModifier.ALT)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fInterimActivity():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    client_Create.fCreate_Client("BA-InterimAct","BA-InterimAct","Interim Activity FF","Interim Activity FF","Interim Activity FF")
    # create some slips
    ba__Common.fCreate_BASlips("BA-InterimAct")
    # set up billing arrangement
    fInterimActivity_Setup1() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-InterimAct",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-InterimAct1")

    # create some slips
    ba__Common.fCreate_BASlips("BA-InterimAct")
    # set up billing arrangement
    fInterimActivity_Setup2() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-InterimAct",2)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-InterimAct2")

    # create some slips
    ba__Common.fCreate_BASlips("BA-InterimAct")
    # set up billing arrangement
    fInterimActivity_Setup3() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-InterimAct",3)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-InterimAct3")
