from sikuli import *
import logging
import myTools
import initNames

#---------------------------------------------------#
def Create_OneCredit(client,cliNum,month):
#---------------------------------------------------#

    logging.debug('- Create_OneCred: ' + str(month) + "-" + client)

    # new payment
    type("n",KeyModifier.CTRL)
    time.sleep(1)
       
    # type = credit
    type(Key.HOME)
    myTools.pressDOWN(1)
    type(Key.TAB)     
        
    # client
    time.sleep(1)        
    type(client)        
    type(Key.TAB)
        
    # date
    credDate = str(month) + "/28/2013"
    type(credDate)
    time.sleep(1)
    type(Key.TAB)       
            
    # Amount
    amount = month + month/float(100)
    type(str(amount))
    type(Key.TAB)
        
    # Description
    type("a",KeyModifier.CTRL)
    type(client + " - " + str(cliNum) + " - " + credDate)
    type(Key.ENTER)
    time.sleep(1)
    type(Key.TAB)

    # Invoice list; go to last entry
    type(Key.END, KeyModifier.CTRL)
    click("apply_one_button.png")
    time.sleep(1) 

    # save
    type("s",KeyModifier.CTRL)
    myTools.checkForUnappliedAmount()

#---------------------------------------------------#
def Create_CreditsForMonth(month):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("credits" + str(month))
    logging.debug('Create_CreditsForMonth: ' + str(month))

    allClients = initNames.Init_Clients()
    count = 0

    myTools.getFocus()

    # open a/r tran list
    type("t",KeyModifier.CTRL)

    for oneClient in allClients:
        count += 1
        
        # always create credits for first 5 clients 
        # then create credits for 1 out of 9 next clients
        
        if (count in range(6)) or ((count + month) % 9 == 0):
            Create_OneCredit(oneClient,count,month)
        else:
            logging.debug('-- skip: ' + str(month) + "-" + oneClient)           

    type(Key.F4,KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)
    myTools.sectionEndTimeStamp()
