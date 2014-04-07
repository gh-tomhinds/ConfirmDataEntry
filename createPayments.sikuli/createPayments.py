from sikuli import *
import logging
import csv
import myTools

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Create_TwelvePayments(client,cliNum):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug('- Create_TwelvePayments: ' + client)

    time.sleep(1)

    for month in range(1,13):
        # new payment
        type("n",KeyModifier.CTRL)
        time.sleep(1)
        # type
        type(Key.TAB)
        # source
        myTools.pressDOWN(month-1)
        type(Key.TAB)
        # check number
        if month == 1:
            type(str(cliNum))
            type(Key.TAB)
        # skip card options
        if month in (3,4,5,6,7,8):
            type(Key.TAB)
        # client
        type(client)        
        type(Key.TAB)
        # date
        payDate = str(month) + "/28/2013"
        type(payDate)
        type(Key.TAB)
        # skip deposit slip
        if month in (1,2):
            type(Key.TAB)
        # Amount
        amount = 100 + int(cliNum) + month/float(100)
        type(str(amount))
        type(Key.TAB)
        # Description
        type("a",KeyModifier.CTRL)
        type(client + " - " + str(cliNum) + " - " + payDate)
        type(Key.ENTER)
        time.sleep(1)
        type("s",KeyModifier.CTRL)
        time.sleep(1)  


# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Create_Payments():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug(' ')
    logging.debug('Create_Payments')

    # make sure timeslips has focus
    if int(Settings.tsVersion) > 2013:
        click("1388176090422.png")

    # start with manually entered client, then load other clients from file
    allClients = ["Agawam"]
    fileClients = csv.DictReader(open(Settings.cliFile))

    for oneClient in fileClients:
        allClients.append(oneClient["NN1"])
    allClients.sort()

    count = 0

    type("t",KeyModifier.CTRL)

    for oneClient in allClients:
        count += 1
        Create_TwelvePayments(oneClient,count)
     
    type(Key.F4,KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)
