from sikuli import *
import logging
import csv
import myTools

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Create_OnePayToAccount(client,cliNum,month):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug('- Create_OnePayment: ' + str(month) + "-" + client)
    time.sleep(1)

    # new payment
    type("n",KeyModifier.CTRL)
    time.sleep(1)
       
    # skip type
    type(Key.TAB)

    # skip deposit slip
    type(Key.TAB)

    # client
    time.sleep(1)        
    type(client)        
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
    amount = 10 + month/float(100)
    type(str(amount))
    type(Key.TAB)

    # Description
    type("a",KeyModifier.CTRL)
    type(client + " - " + str(cliNum) + " - " + payDate)
    type(Key.ENTER)
    time.sleep(1)
    type("s",KeyModifier.CTRL)

    if exists("1398349359000.png"):
        type("n")    
    time.sleep(1)  

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Create_PaysToAccount(month):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug(' ')
    logging.debug('Create_PaymentsForMonth: ' + str(month))
    myTools.sectionStartTimeStamp()

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
