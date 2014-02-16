from sikuli import *
import logging


# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Close_Timeslips():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    popup("make sure Timeslips is closed")

    #show desktop
    type("d",KeyModifier.KEY_WIN)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Old_Stuff():
# - - - - - - - - - - - - - - - - - - - - - - - - - #


    logging.debug(' ')
    logging.debug('Close_Timeslips')
    
    #show desktop
    type("d",KeyModifier.KEY_WIN)


    tsCheck = 0
    while App.focus("Sage Timeslips 201"):
        tsCheck += 1
        logging.debug('- TS was open')
        time.sleep(1)     

        #restore window
        type(Key.SPACE,KeyModifier.ALT)
        type("r")
        time.sleep(2)     

        type("f",KEY_ALT)
        type("x")
        if exists("D0youwanttum.png"):
            click("1351892439140.png")
        
        if tsCheck == 3:
            popup("can't close timeslips")            
        
