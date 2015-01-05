from sikuli import *
import logging
import myTools
import slips_Create
import sys
from bill_ImportLayout import fImport_Layout

#---------------------------------------------------#
def fImport_DefaultLayout():
#---------------------------------------------------#

    fImport_Layout("Low Detail")

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
def fSetup_NewNamesDefault():
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
def fMoveto_BAPage():
#---------------------------------------------------#

    if int(Settings.tsVersion) > 2014:
        myTools.pressSHIFTF6(9)
    else:
        myTools.pressF6(3)

#---------------------------------------------------#
def fSetup_BABills():
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
def fSetup_BADefaultLayout():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("ba setup")

    myTools.getFocus()

    fImport_DefaultLayout()
    fSetup_NewNamesDefault()
    fSetup_BABills()

    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def fCreate_BASlips(pBAClient):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("ba slips")
    logging.debug('fCreate_BASlips')

    type("m",KeyModifier.CTRL)
    time.sleep(1)

    slips_Create.Create_OneSlip("t","TomH","con001",pBAClient,1)
    slips_Create.Create_OneSlip("t","CoreyM","gen004",pBAClient,2)
    slips_Create.Create_OneSlip("t","SamS","gen005",pBAClient,3)
    slips_Create.Create_OneSlip("t","ShawnR","lnd010",pBAClient,4)

# create some expense slips
    slips_Create.Create_OneSlip("e","ShawnR","e004",pBAClient,5)
    slips_Create.Create_OneSlip("e","SamS","e005",pBAClient,6)
    slips_Create.Create_OneSlip("e","CoreyM","e006",pBAClient,7)
    slips_Create.Create_OneSlip("e","TomH","e003",pBAClient,8)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def fPrint_BABill(pBAClient,pBillNum):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("ba bill")
    logging.debug('BA_Bill: ' + pBAClient + ' ' + str(pBillNum))

    type("b",KeyModifier.CTRL)
    click("remove_filters.png")
    time.sleep(1)
    type(Key.ENTER)
    type(Key.DOWN)
    type(Key.TAB)
    type(Key.SPACE)
    type(pBAClient)
    time.sleep(1)
    type(Key.F4)
    type(Key.ENTER)

    myTools.pressSHIFTTAB(3)    
    
    type("t")
    type(Key.ENTER)  
    time.sleep(1)
    type(Settings.repFolder + "\\" + pBAClient + str(pBillNum) + ".txt")

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
