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

# point to source data folder on desktop and data files
    Settings.dataFolder = os.environ['USERPROFILE']+'\\desktop\\Sikuli\\DataFiles'
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

# point to TS paths
    Settings.baseRepFolder = Settings.sikFolder + "\\Reports\\Baseline"
    logging.debug("- Baseline Reports folder:    %s" %Settings.baseRepFolder)
    
    Settings.repFolder = Settings.sikFolder + "\\Reports\\" + Settings.tsVersion
    logging.debug("- Report folder:    %s" %Settings.repFolder)

    Settings.tsFolder = "C:\\Program Files (x86)\\Timeslips " + Settings.tsVersion
    logging.debug("- Timeslips folder: %s" %Settings.tsFolder)

    Settings.tsEXE = Settings.tsFolder + "\\timeslip.exe" 
    logging.debug("- Timeslips EXE:    %s" %Settings.tsEXE)

    Settings.tsimpEXE = Settings.tsFolder + "\\tsimport.exe" 
    logging.debug("- TSImport EXE:     %s" %Settings.tsimpEXE)

    Settings.dbFolder = Settings.tsFolder + "\\Sikuli" 
    logging.debug("- DB folder:        %s" %Settings.dbFolder)

    Settings.BALogFile = Settings.repFolder + "\\BA-Log.txt"
    # delete BA Log File
    # os.remove(Settings.BALogFile)    

