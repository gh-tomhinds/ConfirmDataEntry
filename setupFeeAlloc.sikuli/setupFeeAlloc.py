from sikuli import *
import logging
import myTools


# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Setup_CustomFields():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug('- Set Up Custom Fields')
    type("p", KeyModifier.ALT)
    type("c")
    time.sleep(1)    
    type(Key.TAB)

    for customName in ["Originating","Responsible","Other"]:                

        type("n", KeyModifier.ALT)
        type(Key.UP)
        type(Key.ENTER)
        time.sleep(1)
    
        type(customName)
        myTools.pressTAB(2)
        type(Key.DOWN)            
        type(Key.ENTER)    

    myTools.pressTAB(7)
    type(Key.ENTER)
    time.sleep(2)


# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Export_Timekeepers():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug('- Export Timekeepers')

    type("i", KeyModifier.CTRL)
    time.sleep(1)    
    type(Key.ENTER)
    time.sleep(1)    
    
    
    if Settings.tsVersion == "2015":
        myTools.pressF6(4)
        myTools.pressTAB(2)        
    else:
        type(Key.F6)
        myTools.pressTAB(3)
        type(Key.RIGHT)
    
    type(Key.TAB)
    type("t")
    type(Key.TAB)
    type("20")
    
    type(Key.TAB)
    type("c")
    type(Key.TAB)
    type("10")

    type(Key.TAB)
    type("e")
    type(Key.TAB)
    type("5")

    type("s", KeyModifier.CTRL)

    click("1383851432431.png")
    time.sleep(1)

    if Settings.tsVersion == "2015":
        type(Key.DOWN)
        # sometimes a keypress is needed to make INS work
    else:    
        type(Key.DELETE)
        myTools.pressDOWN(8)
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

    wait("1387316703616.png", 10)
    type(Key.ENTER)    

    type(Key.F4,KEY_CTRL)
    time.sleep(1) 
    type(Key.F4,KEY_CTRL)


# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Setup_FeeAlloc():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug('Set Up Fee Allocation')

    Setup_CustomFields()
    Export_Timekeepers()
