from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def Import_Layout(this_layout):
#---------------------------------------------------#

    logging.debug('- open layout list')
    type("b",KeyModifier.ALT)
    type("t")
    time.sleep(1)
    logging.debug('- import layout')
    click(Pattern("import_button.png").targetOffset(3,-9))
    time.sleep(2)

    layoutFilePath = Settings.dataFolder + "\\" + this_layout + ".tsl"
    type(layoutFilePath)
    type(Key.ENTER)
    time.sleep(2)
    type(this_layout)
    
    logging.debug('- save layout')    
    type("l",KeyModifier.ALT)
    type("s")
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)

#---------------------------------------------------#
def Assign_Layout(this_layout):
#---------------------------------------------------#

    logging.debug('- assign layout')
    type("a",KeyModifier.ALT)
    type(Key.INSERT)
    type("a",KeyModifier.ALT)
    type(Key.ENTER)

    wait("assigned_message.png",FOREVER)
    type(Key.ENTER)
    
#---------------------------------------------------#
def Import_BillLayout(layoutName):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("import layout")
    logging.debug('Import_BillLayout')
    
    # make sure timeslips has focus
    myTools.getFocus()

    Import_Layout(layoutName)
    Assign_Layout()

    type(Key.F4,KeyModifier.CTRL)
    myTools.sectionEndTimeStamp()    