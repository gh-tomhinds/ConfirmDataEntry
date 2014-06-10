from sikuli import *
import logging
import myTools
import initNames

#---------------------------------------------------#
def Create_OnePayment(client,cliNum,month):
#---------------------------------------------------#

    logging.debug('- Create_OnePay: ' + str(month) + "-" + client)

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
    time.sleep(1)        
    type(client)        
    type(Key.TAB)
        
    # date
    payDate = str(month) + "/28/2013"
    type(payDate)
    time.sleep(1)
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
    
    if exists("1397586037229.png"):
        type(Key.ENTER)

#---------------------------------------------------#
def Create_PaymentsForMonth(month):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("payments" + str(month))
    logging.debug('Create_PaymentsForMonth: ' + str(month))

    allClients = initNames.Init_Clients()
    count = 0

    myTools.getFocus()

    # open a/r tran list
    type("t",KeyModifier.CTRL)

    for oneClient in allClients:
        count += 1
        if (count in range(6)) or ((count + month) % 5 == 0):
            Create_OnePayment(oneClient,count,month)
        else:
            logging.debug('-- skip: ' + str(month) + "-" + oneClient)           

    type(Key.F4,KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)
    myTools.sectionEndTimeStamp()
