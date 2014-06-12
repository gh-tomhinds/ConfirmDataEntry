from sikuli import *
import logging
import myTools
import createClient
import baCommon
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_Percent_Arrangement1():
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
    baCommon.moveto_BAPage()
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
def BA_Percent_Arrangement2():
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
    baCommon.moveto_BAPage()
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
def BA_Percent_Arrangement3():
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
    baCommon.moveto_BAPage()
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
def BA_Percent():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-Percent","BA-Percent","Percent Comp","Percent Comp","Percent Comp")
    # create some slips
    baCommon.BA_Create_Slips("BA-Percent")
    # set up billing arrangement
    BA_Percent_Arrangement1() 
    # print a bill to text
    baCommon.BA_Bill("BA-Percent",1)
    # compare bill values
    baReviewBills.Review_Bill("BA-Percent1")

    # create some more slips
    baCommon.BA_Create_Slips("BA-Percent")
    # set up billing arrangement
    BA_Percent_Arrangement2() 
    # print a bill to text
    baCommon.BA_Bill("BA-Percent",2)
    # compare bill values
    baReviewBills.Review_Bill("BA-Percent2")

    # create some more slips
    baCommon.BA_Create_Slips("BA-Percent")
    # set up billing arrangement
    BA_Percent_Arrangement3() 
    # print a bill to text
    baCommon.BA_Bill("BA-Percent",3)
    # compare bill values
    baReviewBills.Review_Bill("BA-Percent3")

