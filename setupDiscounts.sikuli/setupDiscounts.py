from sikuli import *
import logging
import myTools


# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Setup_Discounts():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug('Set Up Discounts')
    click("Names-1.png")
    type("i")
    time.sleep(1)

    type(Key.ENTER)
    time.sleep(1)

    myTools.pressF6(5)
    myTools.pressSHIFTTAB(10)
    time.sleep(1)
    
    type("10")
    type(Key.TAB)
    type("30")
    type(Key.TAB)
    myTools.pressDOWN(2)
    time.sleep(1)

    type("s", KeyModifier.CTRL)
    click("1377193090523.png")
    time.sleep(1)
    
    type(Key.DELETE)
    type(Key.UP)
    type(Key.DOWN)
    type(Key.DOWN, KeyModifier.SHIFT)
    type(Key.DOWN, KeyModifier.SHIFT)    
    type(Key.F4)
    time.sleep(1)

    type(Key.TAB)    
    type(Key.INSERT)
    type(Key.TAB)    
    
    type(Key.ENTER)    
    time.sleep(1)
    type(Key.ENTER)    

    wait("1377193370762.png", FOREVER)
    type(Key.ENTER)    

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1) 
    type(Key.F4,KeyModifier.CTRL)
