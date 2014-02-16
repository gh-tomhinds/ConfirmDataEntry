from sikuli import *
import logging

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Print_Clients():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
 
    logging.debug(' ')
    logging.debug('Print_Clients')

    logging.debug('- open report list')
    click("Beports.png")
    type("c")

    logging.debug('- set up client info listing')
    doubleClick("ClientInfoLi.png")
    click("MZElpticns.png")
    click("1352843528241.png")
    click("Showclient.png")
    time.sleep(1)
    click("5howreferenc.png")
    type(Key.ENTER)

# choose CSV
    type(Key.TAB)
    type(Key.TAB)
    type(Key.F4)
    time.sleep(1)
    type("c")    
    type(Key.ENTER)

    logging.debug('- print')
    click("1352843841109.png")
    time.sleep(1)

    if Settings.tsVersion == "2014":
        type(Settings.repFolder + "\\NewReports\\clientlist.csv")
    else:
        type(Settings.repFolder + "\\OldReports\\clientlist.csv")        

    time.sleep(1)
    click("7.png")
    type(Key.ENTER)
    if exists("Confirm.png"):
        type(Key.ENTER)
    time.sleep(3)        
    type(Key.F4,KEY_CTRL)
    time.sleep(1)            
    type("n")
    type(Key.F4,KEY_CTRL)    
