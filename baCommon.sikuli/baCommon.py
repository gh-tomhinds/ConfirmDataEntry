from sikuli import *
import logging
import myTools
import createSlips
import sys

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Import_DefaultLayout():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug('- open layout list')
    type("b",KeyModifier.ALT)
    type("t")
    time.sleep(1)
    logging.debug('- import layout')
    click(Pattern("1366207860086.png").targetOffset(3,-9))
    time.sleep(2)

    logging.debug('- save layout')
    type(Settings.dataFolder + "\\Low Detail.tsl")
    type(Key.ENTER)
    time.sleep(1)
    type("Low Detail")
    type("l",KeyModifier.ALT)
    type("s")
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)

    logging.debug('- assign layout')
    type("a",KeyModifier.ALT)
    click("1372778077901.png")   
    type(Key.INSERT)
    type("a",KeyModifier.ALT)
    type(Key.ENTER)
    time.sleep(1)
    type(Key.ENTER)
    type(Key.F4,KeyModifier.CTRL)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Setup_NewNamesDefault():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug('- open gen settings')
    type("p",KeyModifier.ALT)
    type("g")
    time.sleep(1)

# get to New Names page    
    myTools.pressF6(7)
    time.sleep(2)
    type("i",KeyModifier.ALT)
    type(Key.DOWN)

# get to Layout field
    myTools.pressTAB(9)
    time.sleep(1)
    type("t")

    type(Key.ENTER)


# - - - - - - - - - - - - - - - - - - - - - - - - - #
def moveto_BAPage():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    if int(Settings.tsVersion) > 2014:
        myTools.pressSHIFTF6(9)
    else:
        myTools.pressF6(3)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def setup_BABills():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug('- set up bill report')

    type("b",KeyModifier.CTRL)
    time.sleep(1)

# Print to text
    myTools.pressTAB(6)
    type("t")

# Save AS    
    myTools.pressTAB(2)
    type(Key.ENTER)

# no column stops
    type("u",KeyModifier.ALT)  
    time.sleep(1)
    type(Key.ENTER)
    
    if exists("1387468197615.png"):
        type(Key.ENTER)        

# SAVE and Close
    type("s",KeyModifier.CTRL)
    type(Key.ENTER)
    type(Key.F4,KeyModifier.CTRL)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Setup_BADefaultLayout():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    Import_DefaultLayout()
    Setup_NewNamesDefault()
    setup_BABills()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_Create_Slips(baClient):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug('- BA_Create_Slips')

    type("m",KeyModifier.CTRL)
    time.sleep(1)

    createSlips.Create_OneSlip("t","TomH","con001",baClient,1)
    createSlips.Create_OneSlip("t","CoreyM","gen004",baClient,2)
    createSlips.Create_OneSlip("t","SamS","gen005",baClient,3)
    createSlips.Create_OneSlip("t","ShawnR","lnd010",baClient,4)

# create some expense slips
    createSlips.Create_OneSlip("e","ShawnR","e004",baClient,5)
    createSlips.Create_OneSlip("e","SamS","e005",baClient,6)
    createSlips.Create_OneSlip("e","CoreyM","e006",baClient,7)
    createSlips.Create_OneSlip("e","TomH","e003",baClient,8)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BA_Bill(baClient,billNum):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug('- BA_Bill')

    type("b",KeyModifier.CTRL)
    click("1372861568498.png")
    time.sleep(1)
    type(Key.ENTER)
    type(Key.DOWN)
    type(Key.TAB)
    type(Key.SPACE)
    type(baClient)
    time.sleep(1)
    type(Key.F4)
    type(Key.ENTER)

    myTools.pressSHIFTTAB(3)    
    
    type("t")
    type(Key.ENTER)  
    time.sleep(1)
    type(Settings.repFolder + "\\" + baClient + str(billNum) + ".txt")

#    for checkmark in findAll("1372861662125.png"):
#        click(checkmark)

    time.sleep(1)
    type(Key.ENTER)  
    time.sleep(1)

    if exists("1372861767712.png"):
        type(Key.ENTER)  
        time.sleep(1)
     
    click("1372861816835.png")
    type(Key.ENTER)  
    time.sleep(1)

    if exists("1387471435110.png"):
        type(Key.ESC)  

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type("n")
