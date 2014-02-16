from sikuli import *
import logging

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Import_BillLayout():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('Import_BillLayout')

    logging.debug('- open layout list')
    type("b",KeyModifier.ALT)
    type("t")
    time.sleep(1)
    logging.debug('- import layout')
    click(Pattern("1366207860086.png").targetOffset(3,-9))
    time.sleep(2)

    logging.debug('- save layout')
    type(Settings.dataFolder + "\\Bill with Taxes.tsl")
    type(Key.ENTER)
    time.sleep(1)
    type("Bill with Taxes")
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
    time.sleep(1)
    type(Key.ENTER)
    type(Key.F4,KeyModifier.CTRL)
