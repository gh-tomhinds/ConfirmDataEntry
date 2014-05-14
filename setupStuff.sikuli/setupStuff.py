from sikuli import *
import logging
import os
import datetime

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Setup_Stuff():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('Setup_Stuff')

# get current month and year (forget where this is used)
    rightNow = datetime.datetime.now()
    Settings.thisMonth = rightNow.month
    Settings.thisYear = rightNow.year

# point to Sikuli folder on desktop
    Settings.sikFolder = os.environ['USERPROFILE']+'\\desktop\\Sikuli'
    logging.debug("- Sikuli folder:    %s" %Settings.sikFolder)

# point to scripts folder on desktop
    Settings.scriptFolder = Settings.sikFolder + '\\ConfirmDataEntry'
    logging.debug("- Script folder:    %s" %Settings.scriptFolder)

# point to source data folder on desktop and data files
    Settings.dataFolder = Settings.scriptFolder + '\\!data'
    logging.debug("- Data folder:      %s" %Settings.dataFolder)
    
    Settings.cliFile = Settings.dataFolder + '\\towns.csv'
    Settings.tkFile = Settings.dataFolder + '\\timekeepers.csv'
    Settings.taskFile = Settings.dataFolder + '\\tasks.csv'
    Settings.expFile = Settings.dataFolder + '\\expenses.csv'
    Settings.refFile = Settings.dataFolder + '\\refs.csv'
    Settings.tSlipsFile = Settings.dataFolder + '\\tslips.csv'
    Settings.eSlipsFile = Settings.dataFolder + '\\eslips.csv'

# get TS version
    Settings.tsVersion = input("Enter 2013, 2014, or 2015:", "2015")
    time.sleep(1)

# point to report paths
    Settings.rootRepFolder = Settings.scriptFolder + "\\!reports"
    logging.debug("- Rep root folder:  %s" %Settings.rootRepFolder)

    Settings.baseRepFolder = Settings.rootRepFolder + "\\Baseline"
    logging.debug("- Base Rep folder:  %s" %Settings.baseRepFolder)
    
    Settings.repFolder = Settings.rootRepFolder + "\\" + Settings.tsVersion
    logging.debug("- Report folder:    %s" %Settings.repFolder)

# point to TS paths
    Settings.tsFolder = "C:\\Program Files (x86)\\Timeslips " + Settings.tsVersion
    logging.debug("- Timeslips folder: %s" %Settings.tsFolder)

    Settings.tsEXE = Settings.tsFolder + "\\timeslip.exe" 
    logging.debug("- Timeslips EXE:    %s" %Settings.tsEXE)

    Settings.tsimpEXE = Settings.tsFolder + "\\tsimport.exe" 
    logging.debug("- TSImport EXE:     %s" %Settings.tsimpEXE)

    Settings.dbFolder = Settings.tsFolder + "\\Sikuli" 
    logging.debug("- DB folder:        %s" %Settings.dbFolder)

    Settings.BALogFile = Settings.repFolder + "\\!BA-Log.txt"
    # delete BA Log File
    # os.remove(Settings.BALogFile)    

    # set up duration log and add version to it
    Settings.durationFile = Settings.sikFolder + "\\Durations-" + Settings.tsVersion + ".csv" 
    durationLog = open(Settings.durationFile, "a")
    durationLog.write(" ," + str(Settings.tsVersion) + "\n")
    durationLog.close()   
