from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fCreate_OneRevPay(pClient,pCliNum,pMonth):
#---------------------------------------------------#

    logging.debug('- Create_OneRevPay: ' + str(pMonth) + "-" + pClient + " - " + str(pCliNum))

    # new transaction
    type("n",KeyModifier.CTRL)
    myTools.waitForTransEntry()

    # switch to Transfer

    type(Key.UP)    # this is to get by a UI defect
    time.sleep(1)
    
    type("rev")
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
        
    # Description
    type("a",KeyModifier.CTRL)
    revDescription = "Reverse Pay: " + pClient + " - " + tranDate + " - " + str(pCliNum)
    type(revDescription)
    type(Key.ENTER)
    time.sleep(1)
    type(Key.TAB)

    # payment list
    type(Key.END)
    time.sleep(1) 
    type("s",KeyModifier.CTRL)   

    # payment fee
    wait("should_there_be_fee.png",FOREVER)
    time.sleep(1) 
    type(Key.DOWN)
    myTools.pressTAB(1)
    revFee = "19.99"
    type(revFee)
    time.sleep(1) 
    myTools.pressTAB(1)

    # fee description
    revFeeDescription = "Note: " + pClient + " - " + revFee
    type(revFeeDescription)

    # close
    time.sleep(1) 
    myTools.pressTAB(1)
    type(Key.ENTER)    

#---------------------------------------------------#
def fCreate_RevPays(pMonth):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("revpays" + str(pMonth))
    logging.debug('fCreate_RevPays: ' + str(pMonth))

    if (pMonth == 1):
        logging.debug('- SKIP MONTH')
        myTools.sectionEndTimeStamp()
        return        

    # list the client that will get a refund each month
    refundClientsA = ["Gardner","Freetown","Franklin","Framingham","Foxborough","Florida","Fitchburg","Falmouth","Fall River","Fairhaven","Everett"]
    oneClientA = refundClientsA[(pMonth - 2)]

    refundClientsB = ["Dover","Douglas","Dighton","Dennis","Deerfield","Dedham","Dartmouth","Danvers","Dalton","Cummington","Conway"]
    oneClientB = refundClientsB[(pMonth - 2)]

    # create a list of clients for current month
    allClients = []
    allClients.append(oneClientA)
    allClients.append(oneClientB)
    count = 0

    myTools.getFocus()

    # open a/r tran list
    type("t",KeyModifier.CTRL)
    myTools.waitForTransList()

    for oneClient in allClients:
        count += 1
        fCreate_OneRevPay(oneClient,count,pMonth)

    type(Key.F4,KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)
    myTools.sectionEndTimeStamp()