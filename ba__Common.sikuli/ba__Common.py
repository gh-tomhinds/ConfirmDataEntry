from sikuli import *
import logging
import myTools
import createSlips
import sys
from importBillLayout import Import_Layout

#---------------------------------------------------#
def Import_DefaultLayout():
#---------------------------------------------------#

    Import_Layout("Low Detail")

    logging.debug('- assign layout')
    type("a",KeyModifier.ALT)
    click("template_list.png")
    type(Key.INSERT)
    type("a",KeyModifier.ALT)
    type(Key.ENTER)
    time.sleep(1)
    type(Key.ENTER)
    type(Key.F4,KeyModifier.CTRL)

#---------------------------------------------------#
def Setup_NewNamesDefault():
#---------------------------------------------------#

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

    if int(Settings.tsVersion) > 2014:
        myTools.pressTAB(10)
    else:
        myTools.pressTAB(9)
    type("t")

    type(Key.ENTER)

#---------------------------------------------------#
def moveto_BAPage():
#---------------------------------------------------#

    if int(Settings.tsVersion) > 2014:
        myTools.pressSHIFTF6(9)
    else:
        myTools.pressF6(3)

#---------------------------------------------------#
def setup_BABills():
#---------------------------------------------------#
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
    
    if exists("replace_msg.png"):
        type(Key.ENTER)        

# SAVE and Close
    type("s",KeyModifier.CTRL)
    type(Key.ENTER)
    type(Key.F4,KeyModifier.CTRL)

#---------------------------------------------------#
def Setup_BADefaultLayout():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("ba setup")

    myTools.getFocus()

    Import_DefaultLayout()
    Setup_NewNamesDefault()
    setup_BABills()

    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def BA_Create_Slips(baClient):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("ba slips")
    logging.debug('BA_Create_Slips')

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

    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def BA_Bill(baClient,billNum):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("ba bill")
    logging.debug('BA_Bill: ' + baClient + ' ' + str(billNum))

    type("b",KeyModifier.CTRL)
    click("remove_filters.png")
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

#    for checkmark in findAll("checkmark.png"):
#        click(checkmark)

    time.sleep(1)
    type(Key.ENTER)  
    time.sleep(1)

    if exists("replace_msg.png"):
        type(Key.ENTER)  
        time.sleep(1)
     
    click("approve_bill.png")
    type(Key.ENTER)  
    time.sleep(1)

    if exists("select_report_to_print.png"):
        type(Key.ESC)  

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type("n")
    
    myTools.sectionEndTimeStamp()
