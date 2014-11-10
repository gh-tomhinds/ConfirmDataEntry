from sikuli import *
import logging
import myTools
import shutil

#---------------------------------------------------#
def delete_dataFolder():
#---------------------------------------------------#
    logging.debug('- delete_dataFolder')

    if os.path.exists(Settings.dbFolder):
        logging.debug("-- Delete folder:     %s" % Settings.dbFolder)
        shutil.rmtree(Settings.dbFolder)
    else:
        logging.debug("-- Missing:           %s" % Settings.dbFolder)

#---------------------------------------------------#
def checkFor_Sample():
#---------------------------------------------------#
    logging.debug('- checkFor_Sample')

    time.sleep(1)     
    if exists("demo_database_msg.png"):
        logging.debug('-- Sample message exists')
        type(Key.ENTER)        

#---------------------------------------------------#
def checkFor_PEP():
#---------------------------------------------------#
    logging.debug('- checkFor_PEP')

    time.sleep(1)     
    if exists("pep.png"):
        logging.debug('-- PEP message exists')
        type(Key.ENTER)        

#---------------------------------------------------#
def checkFor_SPS():
#---------------------------------------------------#
    logging.debug('- checkFor_SPS')

    time.sleep(1)     
    if exists("sps.png"):
        logging.debug('-- SPS message exists')
        type(Key.ENTER)        

#---------------------------------------------------#
def checkFor_BillingDate():
#---------------------------------------------------#
    logging.debug('- checkFor_BillingDate')

    time.sleep(1)     
    if exists("bill_date.png"):
        logging.debug('-- billing date message exists')
        type(Key.ENTER)

#---------------------------------------------------#
def StartTS_CreateNewDB():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("new db")
    
    logging.debug('StartTS_CreateNewDB')

    popup("make sure Timeslips is closed")

# delete the data folder
    delete_dataFolder()

# show desktop
    type("d",KeyModifier.KEY_WIN)

# start timeslips
    logging.debug('- start Timeslips')

    App.open(Settings.tsEXE)   
    time.sleep(3)
    
    logging.debug('-- wait until TS is open')

    wait("sage_timeslips.png",300)

    checkFor_PEP()

# start the new db process
    logging.debug('- Check for database')

    if exists("database_not_found.png"):
        logging.debug('-- db not found')
        type(Key.ENTER)
        time.sleep(2)
        type("n")
    else:
        logging.debug('-- db found')
        if exists("supervisor.png"):
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
    
# Empty database, press Next
    type("n",KeyModifier.ALT)

# new db path and settings
    logging.debug('- enter path')
    type(Settings.dbFolder)
    type(Key.ENTER)

# Firm name
    type("Timeslips Handyman Services")
    type(Key.ENTER)    
    logging.debug('- db settings')

# Decimals
    time.sleep(1)     
    type(Key.ENTER)        

# set Fiscal month to July
    myTools.pressDOWN(6)
    type(Key.ENTER)

# starting invoice number    
    type("12345")
    type(Key.ENTER)

# bill with firm heading    
    myTools.pressDOWN(2)
# mark cover page
    type(Key.TAB,KeyModifier.SHIFT)
    type(Key.SPACE)
    time.sleep(1)        
    type(Key.ENTER)    
    
#    click("do_not_use_tal.png")    
    time.sleep(1)        
    type(Key.ENTER)

# unmark outlook
    type(Key.SPACE)
    time.sleep(1)        
    type(Key.ENTER)

# Ready to Create Your Database
    time.sleep(1)     
    type(Key.ENTER)

# Wait for db to be created    
    wait("finish.png",FOREVER)

# press Finish    
    type(Key.ENTER)
    time.sleep(1)

# Firm name/address
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

# project separator
    myTools.pressF6(6)
    time.sleep(1)
    type(".")

# close General settings
    type(Key.ENTER)    

# getting started
    logging.debug('- getting started wiz')
    wait("enter_your_name.png",FOREVER)
    type("Xander Yakuza Zork")
    type(Key.TAB)
    time.sleep(1)     
    type(Key.ENTER)    
    type("XanderZ")
    type(Key.TAB)
    type("XZork")
    click("finish.png")

# backup
    time.sleep(1)
    if exists("backup_database.png"):
        click("no_btn.png")
        time.sleep(1)
        type("n")

    checkFor_BillingDate()
    checkFor_SPS()
    checkFor_PEP()

    myTools.sectionEndTimeStamp()
