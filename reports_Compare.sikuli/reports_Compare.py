from sikuli import *
import os
import logging
import myTools

#---------------------------------------------------#
def Compare_OneReport(pReportName):
#---------------------------------------------------#
    logging.debug('Compare_OneReport: ' + pReportName)

# point to old report, new report, and output file
    logging.debug('- set file names')
    baseFile = Settings.baseRepFolder + "\\" + pReportName[5:] #trim version from name
    newFile = Settings.repFolder + "\\" + pReportName

    global newRepLine

# don't compare if old report doesn't exist
    logging.debug('- check for base file')
    if not os.path.exists(baseFile):
        logging.debug("--> " + pReportName[5:] + " MISSING")
        myTools.pushReportLog(pReportName," MISSING")
        return

# don't compare if new report doesn't exist
    logging.debug('- check for printed file')
    if not os.path.exists(baseFile):
        logging.debug("--> " + pReportName + " MISSING")        
        myTools.pushReportLog(pReportName," MISSING")
        return

# open report files
    logging.debug('- read report files')

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

# compare lengths of files
    logging.debug('- compare lengths')
    
    if len(baseRepLines) < len(newRepLines):
        errorFound = True        
        logging.debug("--> FAILED: " + pReportName)
        logging.debug("--> new report has more lines")
        myTools.pushReportLog(pReportName," WRONG SIZE")
    elif len(baseRepLines) > len(newRepLines):
        errorFound = True        
        logging.debug("--> FAILED: " + pReportName)
        logging.debug("--> base report has more lines")
        myTools.pushReportLog(pReportName," WRONG SIZE")

    # compare each line in base report to new report; jump out on first mismatch
    else:
        logging.debug("-- same length")    
        logging.debug('- compare files')
        for baseRepLine in baseRepLines:
            if baseRepLine != newRepLines[newRepLine]:
                errorFound = True
                logging.debug("--> FAILED: " + pReportName)
                logging.debug("--> Line: %d \n" % (newRepLine+1))
                logging.debug("--> Base: " + baseRepLine)
                logging.debug("--> New:  " + newRepLines[newRepLine])
                myTools.pushReportLog(pReportName," FAILED    ")
                break
            newRepLine += 1
    
    if errorFound != True:
        logging.debug("-- reports match: " + pReportName)
        myTools.pushReportLog(pReportName," pass      ")
        