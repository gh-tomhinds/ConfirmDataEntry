from sikuli import *
import logging
import myTools


# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Setup_ExpMarkups():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug('Set Up Exp Markups')
    
    # make sure timeslips has focus
    myTools.getFocus()
    
    logging.debug('- open Expense List')
    type("y", KeyModifier.CTRL + KeyModifier.SHIFT)
    time.sleep(1)
    
    logging.debug('- open Expense, switch to Billing tab')
    type(Key.ENTER)
    time.sleep(1)
    type(Key.F6)
    time.sleep(1)

    logging.debug('- open change markup settings')
    myTools.pressTAB(4)
    type("y")
    type(Key.TAB)
    type("5")
    type("s", KeyModifier.CTRL)

    logging.debug('- export settings')
    click("1383856692334.png")
    time.sleep(1)
    
    type(Key.DELETE)
    type(Key.DOWN)
    type(Key.DOWN, KeyModifier.SHIFT)
    type(Key.F4)
    time.sleep(1)

    type(Key.TAB)    
    type(Key.INSERT)
    type(Key.TAB)    
    
    type(Key.ENTER)    
    time.sleep(1)
    type(Key.ENTER)    

    wait("1383856805063.png", FOREVER)
    type(Key.ENTER)    

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1) 
    type(Key.ENTER)    
    type(Key.F4,KeyModifier.CTRL)
