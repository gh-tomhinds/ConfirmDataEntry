from sikuli import *
import logging
import myTools

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Backup_Data(bkuName):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("make backup " + bkuName)
    logging.debug('Backup_Data: ' + bkuName)
    
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
    time.sleep(1)

    # enter backup name
    type(bkuName)
    time.sleep(1)

    # SAVE button
    type(Key.ENTER)
    time.sleep(1)

    
    if exists("1397592513401.png"):
        type(Key.ENTER)
        logging.debug('- overwrite backup')
        
    wait("1397592560374.png",FOREVER)
    
    # OK button
    type(Key.ENTER)

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Backup_Checkpoint(checkpointName):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug(' ')
    logging.debug('Backup_Data: ' + checkpointName)

    # name backup file: ex: 2015-slips
    strBackupFile = Settings.tsVersion + "-" + checkpointName
    Backup_Data(strBackupFile)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Backup_BillData(billMonth):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug(' ')
    logging.debug('Backup_Data: ' + str(billMonth))

    # make month number a string
    strMonth = str(billMonth)
    
    # if month is under 10, prefix with 0        
    if billMonth < 10:
        strMonth = "0" + strMonth

    # name backup file: ex: 2015-bill-03
    strBackupFile = Settings.tsVersion + "-bill-" + strMonth
    Backup_Data(strBackupFile)
