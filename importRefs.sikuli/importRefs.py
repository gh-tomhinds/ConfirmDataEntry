from sikuli import *
import logging
import myTools

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Import_Refs():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('Import_Refs')

# start tsimport
    logging.debug('- start TSImport')
    
    type("r",KeyModifier.KEY_WIN)
    time.sleep(1)
    type(Settings.tsimpEXE)
    type(Key.ENTER)
    time.sleep(2)

    wait("1386702753073.png",FOREVER)
    time.sleep(5)

    logging.debug('- set up ref template')
    time.sleep(1)
    type("f",KeyModifier.ALT)
    type("n")
    time.sleep(1)

# comma
    type("c")
    type(Key.ENTER)
    time.sleep(1)

# ref info
    myTools.pressDOWN(5)
    type(Key.ENTER)

# choose source
    wait("1386702883681.png",FOREVER)
    time.sleep(1)
    type("g",KeyModifier.ALT)
    time.sleep(1)
    type(Settings.refFile)

#choose fields
    logging.debug('- choose fields')        
    myTools.pressTAB(6)

# nn1
    myTools.pressDOWN(1)
    type(Key.ENTER)
    
# nn2
    myTools.pressDOWN(1)
    type(Key.ENTER) 
    
#CliNN1
    myTools.pressDOWN(1)
    type(Key.ENTER) 

# omit 1st record
    click("Limitrecords.png")
    type(Key.TAB)
    time.sleep(1)    
    type("2")

# import data
    logging.debug('- import data')
    type(Key.F9)
    time.sleep(1)    
    type(Key.RIGHT)
    type(Key.ENTER)   
     
# verify data
    wait("1386704518399.png",FOREVER)
    if exists(Pattern("FailedImport-1.png").similar(0.95)):
        logging.debug('- import complete - no failed names')
    else:
        logging.debug('- import complete - some failed names')

# close tsimport
    logging.debug('- close TSImport')
    time.sleep(1)
    type(Key.RIGHT)
    type(Key.ENTER)   
    
    time.sleep(1)
    type("f",KeyModifier.ALT)
    type("x")
    time.sleep(1)
    type("n")        