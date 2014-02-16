from sikuli import *
import logging
import myTools
import createClient
import baCommon
import baReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_Change_Precision():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Precision")
    type(Key.ENTER)
    time.sleep(1)

# get to Rounding field
    if int(Settings.tsVersion) < 2015:
        myTools.pressF6(4)
        time.sleep(1)
        myTools.pressTAB(8)
    else:
        myTools.pressF6(7)
        time.sleep(1)
        myTools.pressTAB(7)               

    time.sleep(1)
    type(Key.UP) 
    
# save and close    
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_Precision():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    createClient.Create_Client("BA-Precision","BA-Precision","Precision Settings","Precision Settings","Precision Settings")
    # create some slips
    baCommon.BA_Create_Slips("BA-Precision")
    # set up billing arrangement
    BA_Change_Precision() 
    # print a bill to text
    baCommon.BA_Bill("BA-Precision",1)
    # compare at bill values
    baReviewBills.Review_Bill("BA-Precision1")
