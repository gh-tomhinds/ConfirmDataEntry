from sikuli import *
import logging
import csv
import myTools

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Create_OnePayToAccount(client,cliNum,month):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug('- Create_OnePTA: ' + str(month) + "-" + client)

    # new payment
    type("n",KeyModifier.CTRL)
    time.sleep(1)
       
    # type (skip)
    type(Key.TAB)

    # deposit slip (skip)
    type(Key.TAB)

    # client
    type(client)        
    time.sleep(1)        
    type(Key.TAB)    
        
    # skip account
    type(Key.TAB)

    # date
    payDate = str(month) + "/28/2013"
    type(payDate)
    type(Key.TAB)
        
    # skip check number
    type(Key.TAB)
            
    # Amount
    amount = 25 + month/float(100)
    type(str(amount))
    type(Key.TAB)

    # Description
    type("a",KeyModifier.CTRL)
    type(client + " - " + str(cliNum) + " - " + payDate)
    type(Key.ENTER)
    time.sleep(.5)
    type("s",KeyModifier.CTRL)

    if exists("1398349359000.png"):
        type("n")    

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Create_PaymentsToAccount(month):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp()
    logging.debug(' ')
    logging.debug('Create_PaysToAccount: ' + str(month))

    # enter PFAs for month 1,4,7,10
    if month in (2,3,5,6,8,9,11,12):
        logging.debug('- skip payments for: ' + str(month))
        myTools.sectionEndTimeStamp()
        return

    # make sure timeslips has focus
    myTools.getFocus()

    # start with manually entered client, then load other clients from file
    allClients = ["Agawam"]
    fileClients = csv.DictReader(open(Settings.cliFile))

    for oneClient in fileClients:
        allClients.append(oneClient["NN1"])
    allClients.sort()

    count = 0

    # open funds list
    type("f",KeyModifier.CTRL)

    for oneClient in allClients:
        count += 1
        Create_OnePayToAccount(oneClient,count,month)
     
    type(Key.F4,KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)
    myTools.sectionEndTimeStamp()
