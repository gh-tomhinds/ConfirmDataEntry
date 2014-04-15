from sikuli import *
import logging
import myTools

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Backup_Data(month):
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('Backup_Data: ' + str(month))
    
    # make sure timeslips has focus
    myTools.getFocus()

    type("f",KeyModifier.ALT)
    type("b")
    time.sleep(1)

    # no subfolders
    type("s",KeyModifier.ALT)
    time.sleep(1)

    # YES button
    type(Key.ENTER)

    # make month number a string
    strMonth = str(month)
    
    # if month is under 10, prefix with 0        
    if month < 10:
        strMonth = "0" + strMonth

    # name backup file: ex: 2015-bill-03
    strBackupFile = Settings.tsVersion + "-bill-" + strMonth
    time.sleep(1)   
    type(strBackupFile)
    logging.debug('- backup file:' + strBackupFile)    
    time.sleep(1)

    # SAVE button
    type(Key.ENTER)
    
    if exists("1397592513401.png"):
        type(Key.ENTER)
        logging.debug('- overwrite backup')
        
    wait("1397592560374.png",FOREVER)
    
    # OK button
    type(Key.ENTER)
