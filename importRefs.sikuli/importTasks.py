from sikuli import *
import logging

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Import_Tasks():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('Import_Tasks')

# start tsimport
    logging.debug('- start TSImport')
    click("1351991222604-3.png")
    time.sleep(1)
    click("run-2.png")
    type(Settings.tsimpEXE)
    type(Key.ENTER)
    time.sleep(2)
    wait("SaqeTimeslip-1.png")

    logging.debug('- set up task template')
    time.sleep(1)
    type("f",KEY_ALT)
    type("n")
    time.sleep(1)
    type("c")
    type(Key.ENTER)
    time.sleep(1)
    type(Key.DOWN) 
    type(Key.DOWN) 
    type(Key.DOWN) 
    type(Key.ENTER)

    #choose source
    wait("Untitled.png")
    time.sleep(1)
    type("g",KEY_ALT)
    time.sleep(1)
    type(Settings.dataFolder)
    type("\\tasks.csv")
    logging.debug('- exit')    

    #choose fields
    doubleClick("Nickname1.png")
    doubleClick("9Nickname2.png")
    doubleClick("9FullName.png")    
    #description
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.ENTER) 
    #category
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.ENTER) 
    #time estimated
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.ENTER) 
    #time spent
    type(Key.UP)
    type(Key.ENTER) 
    #rate 01    
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.ENTER) 
    #rate 20
    type("rrrrrrrrrrrrrrrrrrr")
    type(Key.ENTER) 
    time.sleep(1)        

# omit 1st record
    click("Limitrecords.png")
    type(Key.TAB)
    time.sleep(1)    
    type("2")

# import data
    logging.debug('- import data')
    click("1352092489137.png")
    wait("1352092526314.png")
    click("1352092535682.png")
     
# verify data
    wait("EndOfImport.png",FOREVER)
    if exists(Pattern("FailedImport.png").similar(0.95)):
        logging.debug('- import complete - no failed names')
    else:
        logging.debug('- import complete - some failed names')

# close tsimport
    logging.debug('- close TSImport')
    click("1352132780143.png")
    time.sleep(1)
    type("f",KEY_ALT)
    type("x")
    time.sleep(1)
    type("n")        

