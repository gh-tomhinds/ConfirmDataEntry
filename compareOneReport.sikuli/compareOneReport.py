from sikuli import *
import os
import logging

#---------------------------------------------------#
def Compare_OneReport(reportName):
#---------------------------------------------------#
    logging.debug('Compare_OneReport: ' + reportName)

# point to old report, new report, and output file
    logging.debug('- set file names')
    baseFile = Settings.baseRepFolder + "\\" + reportName[5:] #trim version from name
    newFile = Settings.repFolder + "\\" + reportName

    global newRepLine

# don't compare if old report doesn't exist
    logging.debug('- check for base file')
    if not os.path.exists(baseFile):
        logging.debug(" - " + reportName[5:] + " MISSING")
        return

# don't compare if new report doesn't exist
    logging.debug('- check for printed file')
    if not os.path.exists(baseFile):
        logging.debug(" - " + reportName + " MISSING")        
        return

# open report files
    logging.debug('- load files')

    baseRep = open(baseFile)
    newRep = open(newFile)

# read lines of the report files
    baseRepLines = baseRep.read().splitlines()
    newRepLines = newRep.read().splitlines()

# close report files
    baseRep.close()
    newRep.close()

# open reset line counter and error flag
    newRepLine = 0
    errorFound = False

# compare each line in base report to new report; jump out on first mismatch
    logging.debug('- compare files')
    for baseRepLine in baseRepLines:        
        if baseRepLine != newRepLines[newRepLine]:
            errorFound = True
            logging.debug(" - FAILED : " + reportName)
            logging.debug(" Line: %d \n" % (newRepLine+1))
            logging.debug(" Base: " + baseRepLine)
            logging.debug(" New:  " + newRepLines[newRepLine])
            break
        newRepLine += 1
    
    if errorFound != True:
        logging.debug(" - passed : " + reportName)