from sikuli import *
import logging
import myTools

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Create_Categories():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug(' ')
    logging.debug('Create_Categories')

    logging.debug('- open category list')
    type("p",KeyModifier.ALT)
    
    # hot keys changed for TS2014
    if Settings.tsVersion == "2013":
        type("i")
    else:
        type("o")
    time.sleep(1)

    for category in ["Construction","General","Landscape","Hardware","Supplies","Materials","Other"]:
        logging.debug('- create: ' + category)
        type("n",KEY_ALT)
        type(category)
        type(Key.ENTER)

    logging.debug('- close list')
    myTools.pressTAB(4)
    type(Key.ENTER)    
