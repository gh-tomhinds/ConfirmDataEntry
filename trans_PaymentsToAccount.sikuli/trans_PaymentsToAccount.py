from sikuli import *
import logging
import csv
import myTools
import names_Init

#---------------------------------------------------#
def fCreate_OnePayToAccount(client,cliNum,month):
#---------------------------------------------------#

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

    if exists("you_deposited_money.png"):
        type("n")    

#---------------------------------------------------#
def fCreate_PaymentsToAccount(month):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("paystoaccount" + str(month))
    logging.debug('Create_PaysToAccount: ' + str(month))

    allClients = names_Init.fInit_Clients()
    count = 0

    myTools.getFocus()

    # open funds list
    type("f",KeyModifier.CTRL)

    # create PTA for first 5 clients and then every 6th client

    for oneClient in allClients:
        count += 1
        if (count in range(6)) or ((count + month) % 6 == 0):
            fCreate_OnePayToAccount(oneClient,count,month)
        else:
            logging.debug('-- skip: ' + str(month) + "-" + oneClient)           
     
    type(Key.F4,KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)
    
    myTools.sectionEndTimeStamp()
