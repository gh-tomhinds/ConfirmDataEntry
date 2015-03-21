from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fCreate_OneFundsTransfer(pClient,pCliNum,pMonth):
#---------------------------------------------------#

    logging.debug('- Create_OneFundsTransfer: ' + str(pMonth) + "-" + pClient)

    # new transaction
    type("n",KeyModifier.CTRL)
    myTools.waitForTransEntry()

    # switch to Transfer to Funds

    type(Key.UP)    # this is to get by a UI defect
    time.sleep(1)    
    type("t")
    time.sleep(1)
    type(Key.DOWN)
    time.sleep(1)    
    type(Key.TAB)
       
    # client
    type(pClient)
    type(Key.TAB)
        
    # date
    tranDate = str(pMonth) + "/28/" + Settings.dataYear
    type(tranDate)
    time.sleep(1)
    type(Key.TAB)       
            
    # Amount
    type(Key.TAB)
        
    # Description
    type("a",KeyModifier.CTRL)
    type(pClient + " - " + str(pCliNum) + " - " + tranDate)
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
    time.sleep(1)

#---------------------------------------------------#
def fCreate_TransfersToFunds(pMonth):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("transfer funds" + str(pMonth))
    logging.debug('Create_TransfersFunds: ' + str(pMonth))

    allClients = ["East.Brookfield","North.Andover","West.Bridgewater"]
    count = 0

    myTools.getFocus()

    # open a/r tran list
    type("t",KeyModifier.CTRL)
    myTools.waitForTransList()

    for oneClient in allClients:
        count += 1
        fCreate_OneFundsTransfer(oneClient,count,pMonth)

    type(Key.F4,KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)
    myTools.sectionEndTimeStamp()
