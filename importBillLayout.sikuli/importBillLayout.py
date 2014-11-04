from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def Import_BillLayout():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("import layout")
    logging.debug('Import_BillLayout')
    
    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open layout list')
    type("b",KeyModifier.ALT)
    type("t")
    time.sleep(1)
    logging.debug('- import layout')
    click(Pattern("1366207860086.png").targetOffset(3,-9))
    time.sleep(2)

    type(Settings.dataFolder + "\\Bill with Taxes.tsl")
    type(Key.ENTER)
    time.sleep(2)
    type("Bill with Taxes")
    
    logging.debug('- save layout')    
    type("l",KeyModifier.ALT)
    type("s")
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)

    logging.debug('- assign layout')
    type("a",KeyModifier.ALT)
    type(Key.INSERT)
    type("a",KeyModifier.ALT)
    type(Key.ENTER)

    wait("1415050608582.png",FOREVER)
    type(Key.ENTER)
    
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()