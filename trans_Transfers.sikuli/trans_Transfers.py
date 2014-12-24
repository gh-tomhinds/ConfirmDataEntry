from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fCreate_OneTransfer(client,cliNum,month):
#---------------------------------------------------#

    logging.debug('- Create_OneTransfer: ' + str(month) + "-" + client)

    # new transaction
    type("n",KeyModifier.CTRL)
    myTools.waitForTransEntry()

    # switch to Transfer

    type(Key.UP)    # this is to get by a UI defect
    time.sleep(1)
    
    type("t")
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
    amount = 10 + int(cliNum) + month/float(100)
    type(str(amount))
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
    type("s",KeyModifier.CTRL)   

#---------------------------------------------------#
def fCreate_Transfers(month):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("transfers" + str(month))
    logging.debug('Create_Transfers: ' + str(month))

    allClients = ["East.Bridgewater","North.Adams","West.Boylston"]
    count = 0

    myTools.getFocus()

    # open a/r tran list
    type("t",KeyModifier.CTRL)
    myTools.waitForTransList()

    for oneClient in allClients:
        count += 1
        fCreate_OneTransfer(oneClient,count,month)       

    type(Key.F4,KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)
    myTools.sectionEndTimeStamp()
