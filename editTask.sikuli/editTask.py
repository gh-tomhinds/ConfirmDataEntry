from sikuli import *
import logging
import myTools

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Edit_Task():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('Edit_Task')

    logging.debug('- open task list')
    type("n",KeyModifier.ALT)
    type("f")
    time.sleep(1)
    logging.debug('- edit last task')
    logging.debug('  - names')
    type("ski")
    type(Key.ENTER)
    time.sleep(1)
    type("a",KeyModifier.CTRL)
    type("Build Structure")
    type(Key.TAB)
    type("CON001")
    myTools.pressTAB(2)
    type("Construct Structure")

    type(Key.TAB)
    type("Con")
    type(Key.TAB)
    time.sleep(1)

    logging.debug('  - rates')
    type(Key.TAB)    

    # filling rates with 1.01 thru 1.20
    for i in range(101,121):
        rate = str(float(i)/100)
        type(rate)
        type(Key.TAB)
    time.sleep(1)    

    logging.debug('  - defaults')
    type(Key.TAB)
    type("1.2")
    type(Key.TAB)
    type("1.1")        
    myTools.pressTAB(3)
    type("a",KeyModifier.CTRL)
    time.sleep(1)
    type("Create something new")

    logging.debug('- save and close task list')
    type("s",KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)    
    type(Key.F4,KeyModifier.CTRL)
