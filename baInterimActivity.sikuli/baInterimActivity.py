from sikuli import *
import logging
import myTools
import createClient
import baCommon
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_InterimActivity_Arrangement1():
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
    baCommon.moveto_BAPage()
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
def BA_InterimActivity_Arrangement2():
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
    baCommon.moveto_BAPage()
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
        if exists("1388160064596-1.png"):
            type("y",KeyModifier.ALT)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_InterimActivity_Arrangement3():
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
    baCommon.moveto_BAPage()
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
        if exists("1388160064596.png"):
            type("y",KeyModifier.ALT)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_InterimActivity():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-InterimAct","BA-InterimAct","Interim Activity FF","Interim Activity FF","Interim Activity FF")
    # create some slips
    baCommon.BA_Create_Slips("BA-InterimAct")
    # set up billing arrangement
    BA_InterimActivity_Arrangement1() 
    # print a bill to text
    baCommon.BA_Bill("BA-InterimAct",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-InterimAct1")

    # create some slips
    baCommon.BA_Create_Slips("BA-InterimAct")
    # set up billing arrangement
    BA_InterimActivity_Arrangement2() 
    # print a bill to text
    baCommon.BA_Bill("BA-InterimAct",2)
    # compare at bill values
    baReviewBills.Review_Bill("BA-InterimAct2")

    # create some slips
    baCommon.BA_Create_Slips("BA-InterimAct")
    # set up billing arrangement
    BA_InterimActivity_Arrangement3() 
    # print a bill to text
    baCommon.BA_Bill("BA-InterimAct",3)
    # compare at bill values
    baReviewBills.Review_Bill("BA-InterimAct3")
