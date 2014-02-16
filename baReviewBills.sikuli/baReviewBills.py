from sikuli import *
import os
import logging
import csv


# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Get_BillValues(fullBill,phrase):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # searches the bill text file for a phrase and returns the value associated with it

    logging.debug('- Get_BillValues')

    for billLine in fullBill:
        if billLine.find(phrase) != -1:
            # after finding the line, remove the phrase, $, commas, and trailing spaces
            billLine = billLine.replace(phrase,"")
            billLine = billLine.replace("$","")
            billLine = billLine.replace(",","")
            billLine = billLine.strip()            
            return(billLine)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Compare_Results(billName,valueType,savedValue,billValue):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug("- Compare_Results: " + billName + ": " + valueType)

    outFile = Settings.repFolder + "\\BA-Log.txt"
    billLog = open(outFile, "a")

    print(savedValue)
    print(billValue)

    if float(savedValue) == float(billValue):
        billLog.write(" " + valueType + " matches.\n")
    else:
        billLog.write(" !!!" + valueType + " does not match.")
        billLog.write(" Expected: " + savedValue + ", ")        
        billLog.write(" Actual: " + billValue + "\n")        

    billLog.close()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Review_Bill(billName):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug(' ')
    logging.debug('Review_Bill')

    # open the file that contain bill data
    baDataFile = Settings.dataFolder + "\\baData.csv"
    allBills = csv.DictReader(open(baDataFile))

    # pull the values from the csv to compare to the values in the txt

    stopLooking = False

    for oneBill in allBills:
        if stopLooking == False:
            if oneBill["name"] == billName:
                savedFeesValue = oneBill["fees"]
                savedCostsValue = oneBill["costs"]
                savedTotalValue = oneBill["total"]
                stopLooking = True

    billPath = Settings.repFolder + "\\" + billName + ".txt"

    if os.path.exists(billPath):

        # set up default strings used to identify specific lines on the bill
        if "Progress" in billName and "3" in billName:
            timeText = "Net Time Charges"
        elif "Progress" in billName:
            timeText = "Progress billing amount"
        else:            
            timeText = "For professional services rendered"

        print(timeText)

        expText = "Total additional charges"
        totalText = "Balance due"

        # open txt file of printed bill
        billFile = open(billPath)
        # read in file and break it up into lines
        billLines = billFile.read().splitlines()            
        billFile.close()

        # read values from printed bill
        billFeesValue = Get_BillValues(billLines,timeText)
        print("* * *")        
        print(billFeesValue)
        billCostsValue = Get_BillValues(billLines,expText)
        billTotalValue = Get_BillValues(billLines,totalText)

        # open log file
        outFile = Settings.repFolder + "\\BA-Log.txt"
        billLog = open(outFile, "a")
        
        # print results      
        billLog.write("\nBill: " +  billName)
        for dashes in range(50-len(billName)):
            billLog.write("-")
        billLog.write("\n")
        billLog.close()

        Compare_Results(billName,"Fees",savedFeesValue,billFeesValue)
        Compare_Results(billName,"Costs",savedCostsValue,billCostsValue)
        Compare_Results(billName,"Total",savedTotalValue,billTotalValue)

    else:
        logging.debug(" - MISSING: " + billName)
