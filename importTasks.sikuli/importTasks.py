from sikuli import *
import logging
import myTools

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Add_TaskCustomField(name, downArrow):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    type(Key.ENTER)
    type(Key.TAB)
    type("a",KeyModifier.CTRL)

    for i in range(downArrow+1):
        type(Key.DOWN)

    type(Key.ENTER)
    type(Key.TAB,KeyModifier.SHIFT)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Import_Tasks():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("import tasks")

    logging.debug(' ')
    logging.debug('Import_Tasks')

# start tsimport
    logging.debug('- start TSImport')

    type("r",KeyModifier.KEY_WIN)
    time.sleep(1)
    type(Settings.tsimpEXE)
    type(Key.ENTER)
    time.sleep(2)

    wait("1386702753073.png",FOREVER)
    time.sleep(5)

    logging.debug('- set up task template')
    time.sleep(1)
    type("f",KeyModifier.ALT)
    type("n")
    time.sleep(1)

    # comma
    type("c")
    type(Key.ENTER)
    time.sleep(1)

    # time activity info
    myTools.pressDOWN(3)
    type(Key.ENTER)

    #choose source
    wait("1386702883681.png",FOREVER)
    time.sleep(1)
    type("g",KeyModifier.ALT)
    time.sleep(1)
    type(Settings.taskFile)   

#choose fields
    logging.debug('- choose fields')        
    myTools.pressTAB(7)

# nn1
    myTools.pressDOWN(3)
    type(Key.ENTER)

# nn2
    myTools.pressDOWN(1)
    type(Key.ENTER)

# full
    myTools.pressDOWN(1)
    type(Key.ENTER)

# description
    myTools.pressDOWN(4)
    type(Key.ENTER) 

# bill status
    myTools.pressDOWN(1)
    type(Key.ENTER) 

# category
    myTools.pressDOWN(2)
    type(Key.ENTER) 

# time estimated
    myTools.pressDOWN(2)
    type(Key.ENTER) 

# time spent
    type(Key.UP)
    type(Key.ENTER) 

#rate 01    
    myTools.pressDOWN(2)
    type(Key.ENTER) 

    #rates 2 - 20
    for i in range(1,20):
        myTools.pressDOWN(1)
        type(Key.ENTER) 
    time.sleep(1)        

    # custom
    type("c")
    time.sleep(1)        
    
    customFields = ['Date','Hours','CountyList','Money','Number','Percent','Text']
    for customField in customFields:
        Add_TaskCustomField(customField, customFields.index(customField))

# omit 1st record
    click("Limitrecords.png")
    type(Key.TAB)
    type("2")
    time.sleep(1)    

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

    myTools.sectionEndTimeStamp()