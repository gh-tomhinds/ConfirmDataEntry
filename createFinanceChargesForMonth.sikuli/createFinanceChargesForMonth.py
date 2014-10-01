from sikuli import *
import logging
import myTools
import initNames

#---------------------------------------------------#
def Create_OneFinanceCharge(client,cliNum,month):
#---------------------------------------------------#

    logging.debug('- Create_OneFinance: ' + str(month) + "-" + client)
    time.sleep(1)

    # choose client
    type(client)
    time.sleep(1)
    type(Key.ENTER)
    time.sleep(1)

    # switch page
    if Settings.tsVersion > "2014":
        myTools.pressF6(7)
    else:
        myTools.pressF6(4)
    time.sleep(1)

    # go to field
    if Settings.tsVersion > "2014":
        myTools.pressSHIFTTAB(4)
    else:    
        myTools.pressSHIFTTAB(3)
    time.sleep(1)

    # set "next bill"
    type("ne")
    myTools.pressTAB(1)
    time.sleep(1)

    # enter finance charge   
    financeCharge = str(cliNum) + ".99"
    type(financeCharge)
    time.sleep(1)
    myTools.pressTAB(1)

    # description
    type("a",KeyModifier.CTRL)
    time.sleep(1)
    financeText = "Finance charge for: " + client + ": Month: " + str(month)
    paste(financeText)

    # save
    type("s",KeyModifier.CTRL)
    time.sleep(1)

    # close client info
    type(Key.F4,KeyModifier.CTRL)

#---------------------------------------------------#
def Create_FinanceCharges(month):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("finance" + str(month))
    logging.debug('Create_FinanceCharges: ' + str(month))

    allClients = initNames.Init_Clients()
    count = 0

    myTools.getFocus()

    # client list
    type("i",KeyModifier.CTRL)

    for oneClient in allClients:
        count += 1
        
        # always create finance charge for first 5 clients 
        # then create finance charge for 1 out of 35 next clients
        
        if (count in range(6)) or ((count + month) % 35 == 0):
            Create_OneFinanceCharge(oneClient,count,month)
        else:
            logging.debug('-- skip: ' + str(month) + "-" + oneClient)           

    type(Key.F4,KeyModifier.CTRL)
    myTools.sectionEndTimeStamp()
