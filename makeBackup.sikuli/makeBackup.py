from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def Backup_Data(bkuName):
#---------------------------------------------------#

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

    
    if exists("replace_old_one.png"):
        type(Key.ENTER)
        logging.debug('- overwrite backup')
        
    wait("backup_successful.png",FOREVER)
    
    # OK button
    type(Key.ENTER)

#---------------------------------------------------#
def Backup_Checkpoint(checkpointName):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("backup checkpoint")
    logging.debug('Backup_Checkpoint: ' + checkpointName)

    # name backup file: ex: 2015-slips
    strBackupFile = Settings.tsVersion + "-" + checkpointName
    Backup_Data(strBackupFile)

    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def Backup_BillData(billMonth):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("backup billdata")
    logging.debug('Backup_Data: ' + str(billMonth))

    # name backup file: ex: 2015-bill-03
    strBackupFile = myTools.monthToName(billMonth,"-bill-",".bku")
    Backup_Data(strBackupFile)

    myTools.sectionEndTimeStamp()