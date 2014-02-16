from sikuli import *
import logging
import myTools

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Create_Expense():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('Create_Expense')

    logging.debug('- open expense list')
    type("n",KeyModifier.ALT)
    type("o")
    time.sleep(1)

    logging.debug('- create new expense')
    type("n",KeyModifier.CTRL)

    logging.debug('  - names')
    type("Lip stick")
    type(Key.TAB)
    type("Z123")
    type(Key.ENTER)
    type("Makeup")

    type(Key.TAB)
    type("m")
    type(Key.TAB)

    time.sleep(1)
    logging.debug('  - prices')
    type(Key.TAB)    
    type("1.1001")
    type(Key.TAB)    
    if int(Settings.tsVersion) > 2012:
        
        type("1.1002")    
        type(Key.TAB)    
        type("1.1003")
        type(Key.TAB)    
        type("1.1004")    
        type(Key.TAB)    
        type("1.1005")
        type(Key.TAB)    
        type("1.1006")    
        type(Key.TAB)    
        type("1.1007")
        type(Key.TAB)    
        type("1.1008")    
        type(Key.TAB)    
        type("1.1009")
        type(Key.TAB)    
        type("1.1010")    
        type(Key.TAB)    
        type("1.1011")
        type(Key.TAB)    
        type("1.1012")    
        type(Key.TAB)    
        type("1.1013")
        type(Key.TAB)    
        type("1.1014")    
        type(Key.TAB)    
        type("1.1015")
        type(Key.TAB)    
        type("1.1016")    
        type(Key.TAB)    
        type("1.1017")
        type(Key.TAB)    
        type("1.1018")    
        type(Key.TAB)    
        type("1.1019")
        type(Key.TAB)    
        type("1.1020")    

        time.sleep(1)
        type(Key.TAB)    
        type("2")
        type(Key.TAB)        

    type("1116.789")
    type(Pattern("Description.png").targetOffset(29,0), "Stuff to make us pretty") 

    logging.debug('- save and close expense list')
    type("s",KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)  
    time.sleep(1)    
    type(Key.F4,KeyModifier.CTRL)
