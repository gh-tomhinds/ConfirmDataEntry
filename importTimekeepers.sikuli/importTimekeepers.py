from sikuli import *
import logging
import myTools

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Add_TkCustomField(name, downArrow):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    type(Key.ENTER)
    type(Key.TAB)
    type("a",KeyModifier.CTRL)

    for i in range(downArrow+1):
        type(Key.DOWN)

    type(Key.ENTER)
    type(Key.TAB,KeyModifier.SHIFT)


# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Import_Timekeepers():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('Import_Timekeepers')

# start tsimport
    logging.debug('- start TSImport')
    type("r",KeyModifier.KEY_WIN)
    time.sleep(1)
    type(Settings.tsimpEXE)
    type(Key.ENTER)
    time.sleep(2)

    wait("1386702753073.png",FOREVER)
    time.sleep(2)

    logging.debug('- set up timekeeper template')
    type("f",KeyModifier.ALT)
    type("n")
    time.sleep(1)
    
    type("c")
    type(Key.ENTER)
    time.sleep(1)

    myTools.pressDOWN(2)
    type(Key.ENTER)

#choose source
    wait("1386702883681.png")
    time.sleep(1)
    type("g",KeyModifier.ALT)
    time.sleep(1)
    type(Settings.tkFile)

#choose fields
    myTools.pressTAB(7)
# NN1
    myTools.pressDOWN(3)
    type(Key.ENTER)
# NN2
    myTools.pressDOWN(1)
    type(Key.ENTER)
# Full Name
    myTools.pressDOWN(1)
    type(Key.ENTER)
#initials
    myTools.pressDOWN(1)
    type(Key.ENTER) 
#email
    myTools.pressDOWN(1)
    type(Key.ENTER) 
    time.sleep(1)

#rates 1 - 20
    for i in range(1,21):
        myTools.pressDOWN(1)
        type(Key.ENTER) 
    time.sleep(1)           

#overhead
    myTools.pressDOWN(1)
    type(Key.ENTER) 
    time.sleep(1)        

    # custom
    type("c")
    time.sleep(1)        
    
    customFields = ['Date','Hours','CountyList','Money','Number','Percent','Text']
    for customField in customFields:
        Add_TkCustomField(customField, customFields.index(customField))

# omit 1st record
    click("1386713105865.png")
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
    if exists(Pattern("FailedImport.png").similar(0.95)):
        logging.debug('- import complete - no failed names')
    else:
        logging.debug('- import complete - some failed names')

# close tsimport
    logging.debug('- close TSImport')
    time.sleep(1)
    type(Key.RIGHT)
    type(Key.ENTER)   

#    popup("xxx")

    time.sleep(1)

    type("f",KeyModifier.ALT)
    type("x")
    time.sleep(1)
    type("n")        
