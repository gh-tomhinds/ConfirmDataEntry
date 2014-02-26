from sikuli import *
import logging
import myTools

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def checkFor_Sample():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('checkFor_Sample')

    time.sleep(1)     
    if exists("Youarepresen.png"):
        logging.debug('- Sample message exists')
        type(Key.ENTER)        

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def checkFor_PEP():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('checkFor_PEP')

    time.sleep(1)     
    if exists("ProductEnhan.png"):
        logging.debug('- PEP message exists')
        type(Key.ENTER)        

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def checkFor_SPS():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('checkFor_SPS')

    time.sleep(1)     
    if exists("SagePavment.png"):
        logging.debug('- SPS message exists')
        type(Key.ENTER)        

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def checkFor_BillingDate():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('checkFor_BillingDate')

    time.sleep(1)     
    if exists("1386630096436.png"):
        logging.debug('- billing date message exists')
        type(Key.ENTER)


# - - - - - - - - - - - - - - - - - - - - - - - - - #
def StartTS_CreateNewDB():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('StartTS_CreateNewDB')
    
# start timeslips
    logging.debug('- start Timeslips')

    App.open(Settings.tsEXE)   
    time.sleep(3)
    
    logging.debug('- wait until TS is open')

    wait("1387825071114.png")

    checkFor_PEP()

# start the new db process
    logging.debug('Check for database')

    if exists("DatabaseNotF.png"):
        logging.debug('- db not found')
        type(Key.ENTER)
        time.sleep(2)
        type("n")
    else:
        logging.debug('- db found')
        if exists("1386630258779.png"):
            type(Key.ENTER)        
            time.sleep(1)
        checkFor_Sample()
        checkFor_PEP()
        checkFor_BillingDate()
        checkFor_SPS()
        time.sleep(1)

        # File > New > Database
        logging.debug('- create new database')
        type("f",KeyModifier.ALT)
        type("n")
        type("d")
        
    time.sleep(1)    
    type("n",KeyModifier.ALT)

# new db path and settings
    logging.debug('- enter path')
    type(Settings.dbFolder)
    type(Key.ENTER)
    type("Timeslips Handyman Services")
    type(Key.ENTER)    
    logging.debug('- db settings')
    time.sleep(1)     
    type(Key.ENTER)        
    myTools.pressDOWN(6)
    type(Key.ENTER)            
    type("12345")
    type(Key.ENTER)

# bill with firm heading    
    myTools.pressDOWN(2)

# unmark cover page
    type(Key.TAB,KeyModifier.SHIFT)
    type(Key.SPACE)
    time.sleep(1)        
    type(Key.ENTER)
    
#    click("Idonotuseana.png")    
    time.sleep(1)        
    type(Key.ENTER)

# unmark outlook
    type(Key.SPACE)
    time.sleep(1)        
    type(Key.ENTER)
    
    time.sleep(1)     
    type(Key.ENTER)
    wait("1351889503018.png",FOREVER)
    type(Key.ENTER)
    time.sleep(1)

# address
    type(Key.TAB)
    type("239 Western Avenue")
    myTools.pressTAB(2)
    type("Essex")
    type(Key.TAB)
    type("MA")
    type(Key.TAB)
    type("01929")
    type(Key.TAB)
    type("USA")
    type(Key.TAB)
    type("508-768-6100")
    time.sleep(1)
    type(Key.ENTER)    

# getting started
    logging.debug('- getting started wiz')
    wait("EIltly0UlIIH.png",FOREVER)
    type("Xander Yakuza Zork")
    type(Key.TAB)
    time.sleep(1)     
    type(Key.ENTER)    
    type("XanderZ")
    type(Key.TAB)
    type("XZork")
    click("1351889503018-1.png")

# backup
    time.sleep(1)
    if exists("BackUpCurren.png"):
        click("N0.png")
        time.sleep(1)
        type("n")

# date
    checkFor_BillingDate()

# SPS
    checkFor_SPS()

# PEP
    checkFor_PEP()
