from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fCreate_OneFundsTransfer(client,cliNum,month):
#---------------------------------------------------#

    logging.debug('- Create_OneFundsTransfer: ' + str(month) + "-" + client)

    # new transaction
    type("n",KeyModifier.CTRL)
    time.sleep(1)

    # switch to Transfer to Funds

    type(Key.UP)    # this is to get by a UI defect
    time.sleep(1)    
    type("t")
    time.sleep(1)
    type(Key.DOWN)
    time.sleep(1)    
    type(Key.TAB)
       
    # client
    type(client)        
    type(Key.TAB)
        
    # date
    tranDate = str(month) + "/28/2013"
    type(tranDate)
    time.sleep(1)
    type(Key.TAB)       
            
    # Amount
    type(Key.TAB)
        
    # Description
    type("a",KeyModifier.CTRL)
    type(client + " - " + str(cliNum) + " - " + tranDate)
    type(Key.ENTER)
    time.sleep(1)
    type(Key.TAB)

    # payment list
    type(Key.DOWN)
    time.sleep(1)
    type(Key.TAB)

    # funds account
    type(Key.END)
    time.sleep(1)

    type("s",KeyModifier.CTRL)   

#---------------------------------------------------#
def fCreate_TransfersToFunds(month):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("transfer funds" + str(month))
    logging.debug('Create_TransfersFunds: ' + str(month))

    allClients = ["East.Brookfield","North.Andover","West.Bridgewater"]
    count = 0

    myTools.getFocus()

    # open a/r tran list
    type("t",KeyModifier.CTRL)
    time.sleep(2)

    for oneClient in allClients:
        count += 1
        fCreate_OneFundsTransfer(oneClient,count,month)       

    type(Key.F4,KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)
    myTools.sectionEndTimeStamp()
