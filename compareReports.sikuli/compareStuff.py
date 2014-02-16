from sikuli import *
import os
import logging

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Compare_Stuff():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('Close_Timeslips')

    global newRepLine

    for reportFile in os.listdir(Settings.repFolder + "NewReports\\"):
        if name.endswith(".csv"):

            oldFile = Settings.repFolder + "\\OldReports\\" + reportFile
            newFile = Settings.repFolder + "\\NewReports\\" + reportFile
            outFile = Settings.repFolder + "\\ReportLog.txt"

            oldRep = open(oldFile)
            newRep = open(newFile)

            oldRepLines = oldRep.read().splitlines()
            newRepLines = newRep.read().splitlines()
    
            oldRep.close()
            newRep.close()
    
            ReportLog = open(outFile, "a")
            ReportLog.write("Report: %s \n" % reportFile)
    
            newRepLine = 0
            errorFound = False
            for oldRepLine in oldRepLines:
    
                if oldRepLine != newRepLines[newRepLine]:
                    errorFound = True
                    ReportLog.write(" Line: %d \n" % (newRepLine+1))
                    ReportLog.write(" Old: " + oldRepLine + "\n")
                    ReportLog.write(" New: " + newRepLines[newRepLine] + "\n\n")
                    break
                newRepLine += 1
    
            if errorFound != True:
                ReportLog.write(" No Error Found \n\n")
    
                
            ReportLog.close()
            