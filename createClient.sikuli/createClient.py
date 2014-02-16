from sikuli import *
import logging
import myTools

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Create_Client(nn1,nn2,fullname,inrefto,clinotes):
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('Create_Client' + nn1)

    logging.debug('- open client list')
    type("i",KeyModifier.CTRL)
    time.sleep(1)

    logging.debug('- create new client')
    type("n",KeyModifier.CTRL)

    logging.debug('- nicknames')
    time.sleep(1)
    type(nn1)
    type(Key.TAB)
    type(nn2)
    type(Key.ENTER)    
    time.sleep(1)

    logging.debug('- name and address')
    type(fullname)
    type(Key.TAB)
    type("Address 1a")
    type(Key.TAB)   
    type("Address 1b")
    type(Key.TAB)    
    type("Address 1c")
    type(Key.TAB)
    type("City1")
    type(Key.TAB)
    type("ST1")
    type(Key.TAB)
    type("ZipCode1")
    type(Key.TAB)
    type("Country1")
    type(Key.TAB)

    # TS2015 has secondard address
    if int(Settings.tsVersion) > 2014:
        type("Address 2a")
        type(Key.TAB)   
        type("Address 2b")
        type(Key.TAB)    
        type("Address 2c")
        type(Key.TAB)
        type("City2")
        type(Key.TAB)
        type("ST2")
        type(Key.TAB)
        type("ZipCode2")
        type(Key.TAB)
        type("Country2")
        type(Key.TAB)
        
    type(Key.TAB)
    time.sleep(1)

    logging.debug('- other info')    
# phone
    type("Phone1")
# in ref to

    if int(Settings.tsVersion) > 2014:
        type(Key.F6)
    else:
        click("Inreferencet-1.png")
    type(inrefto)

# notes
# go to first page, then shift+f6

    type("1",KeyModifier.CTRL)
    type(Key.F6,KeyModifier.SHIFT)

    type(clinotes)
    
    logging.debug('- save')
    type("s",KeyModifier.CTRL)
    time.sleep(1)
    
    if exists("1386699132805.png"):
        logging.debug('- conflict check')    
        type(Key.ENTER)
        time.sleep(2)        
        type(Key.ENTER)
        
        type(Key.F4,KeyModifier.CTRL)
        time.sleep(1)    
        
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1) 
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1) 
    type(Key.F4,KeyModifier.CTRL)
