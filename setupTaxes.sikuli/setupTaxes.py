from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def Change_TaxRule():
#---------------------------------------------------#
    logging.debug('- Change_TaxRule')

    logging.debug('-- open Taxes')
    type("p",KeyModifier.ALT)   
    type("t")
    time.sleep(2)

    logging.debug('-- open GA tax rule')
    type(Key.F6)
    type("g")
    type(Key.ENTER)
    time.sleep(1)

    logging.debug('-- change rate')
    myTools.pressTAB(3)
    type("7.25")
    type(Key.TAB)
    type(Key.END)
    time.sleep(1)

    logging.debug('-- change settings')
    type("s",KeyModifier.ALT)
    type("i",KeyModifier.ALT)
    type(Key.ENTER)
    click("1365991914214.png")

#---------------------------------------------------#
def Change_ClientSettings():
#---------------------------------------------------#

    logging.debug('- Change_ClientSettings')

    logging.debug('-- change a client')
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type(Key.ENTER)
    time.sleep(1)

    myTools.pressF6(4)
    if Settings.tsVersion == "2015":
        myTools.pressF6(3)       
    time.sleep(1)
    
    myTools.pressTAB(3)   
    time.sleep(1)
    type("g")

    logging.debug('-- save client')
    type("s",KeyModifier.CTRL)
    logging.debug('-- export settings')
    click("1384206308056.png")    
    
    # clear all and highlight tax profile
    type(Key.DELETE)
    time.sleep(1)
    type(Key.UP)
    type(Key.DOWN)

    # mark tax profile
    type(Key.F4)
    type(Key.TAB)

    # mark all clients
    type(Key.INSERT)
    time.sleep(1)

    # click export
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)
    type(Key.ENTER)

    myTools.waitForExportSuccess()
    
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)

#---------------------------------------------------#
def Change_TaskSettings():
#---------------------------------------------------#

    logging.debug('- Change_TaskSettings')

    logging.debug('-- change a task')
    type("y",KeyModifier.CTRL)
    time.sleep(1)
    type(Key.ENTER)
    time.sleep(1)
    type(Key.F6)
    time.sleep(1)
    myTools.pressTAB(3)   
    time.sleep(1)
    type(Key.F4)
    logging.debug('-- save task')
    type("s",KeyModifier.CTRL)
    logging.debug('-- export settings')
    rightClick("1387404402223.png")
    time.sleep(1)
    type("e")
    time.sleep(1)
    type(Key.TAB)    
    type(Key.PAGE_DOWN,KeyModifier.SHIFT)
    type(Key.F4)    
    type(Key.TAB)    
    type(Key.ENTER)    
    time.sleep(1)
    type(Key.ENTER)    
    time.sleep(1)
    type(Key.ENTER)    
    type("s",KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)

#---------------------------------------------------#
def Change_ExpenseSettings():
#---------------------------------------------------#

    logging.debug('- Change_ExpenseSettings')

    logging.debug('-- change an expense')
    type("y",KeyModifier.CTRL + KeyModifier.SHIFT)
    time.sleep(1)
    type(Key.ENTER)
    time.sleep(1)
    type(Key.F6)
    time.sleep(1)
    myTools.pressTAB(3)   
    myTools.pressDOWN(8)
    time.sleep(1)

    type(Key.F4)
    logging.debug('-- save expense')
    type("s",KeyModifier.CTRL)

    logging.debug('-- export settings')
    rightClick("1366001759780.png")
    time.sleep(1)
    type("e")
    time.sleep(1)

    type(Key.TAB)    
    type(Key.PAGE_DOWN,KeyModifier.SHIFT)
    type(Key.F4)    
    type(Key.TAB)    
    type(Key.ENTER)    
    time.sleep(1)
    type(Key.ENTER)    
    time.sleep(1)
    type(Key.ENTER)    
    type("s",KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)

#---------------------------------------------------#
def Setup_Taxes():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("setup taxes")

    logging.debug('Setup_Taxes')
    
    # make sure timeslips has focus
    myTools.getFocus()

    time.sleep(1)
    Change_TaxRule()
    Change_ClientSettings()
    Change_TaskSettings()
    Change_ExpenseSettings()

    myTools.sectionEndTimeStamp()