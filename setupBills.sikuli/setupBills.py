from sikuli import *
import logging
import myTools

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Setup_Bills():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug('- set up bill report')

    myTools.getFocus()

    type("b",KeyModifier.CTRL)
    time.sleep(1)

    myTools.pressTAB(4)
    type(Key.ENTER)
    time.sleep(1)

# default button
    type("d",KeyModifier.ALT)

# mark a/r tran follow slip date
    myTools.pressTAB(6)
    time.sleep(1)
    type(Key.SPACE)

# unmark send bills by email
    if int(Settings.tsVersion) > 2014:
        myTools.pressTAB(4)
    else:
        myTools.pressTAB(5)        
    time.sleep(1)
    type(Key.SPACE)

# unmark envelopes
    myTools.pressTAB(4)
    time.sleep(1)
    type(Key.SPACE)

# OK
    time.sleep(1)
    type(Key.ENTER)

# Print to PDF
    myTools.pressTAB(2)
    type(Key.END)

# PDF Options
    myTools.pressTAB(2)
    type(Key.SPACE)
    time.sleep(1)
    type(Key.UP)
    time.sleep(1)
    type(Key.ENTER) 

# SAVE and Close
    type("s",KeyModifier.CTRL)
    type(Key.ENTER)
    type(Key.F4,KeyModifier.CTRL)
