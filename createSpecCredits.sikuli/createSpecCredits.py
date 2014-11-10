from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def Filter_Invoices():
#---------------------------------------------------#

    # selection
    click("1415390994179.png")
    time.sleep(1)
    doubleClick("1415391053826.png")
    time.sleep(1)
    # unselect all
    type(Key.DELETE)
    # select invoice
    myTools.pressDOWN(5)    
    type(Key.F4)
    time.sleep(1)
    # OK
    myTools.pressTAB(1)
    type(Key.ENTER)
    time.sleep(1)
    # OK    
    type(Key.ENTER)
    time.sleep(1)
    # Update
    myTools.pressTAB(1)
    type(Key.ENTER)
    time.sleep(1)

#---------------------------------------------------#
def Clear_Filter():
#---------------------------------------------------#

    # selection
    click("1415390994179.png")
    time.sleep(1)
    # clear
    click("1415391577558.png")
    time.sleep(1)
    # OK    
    type(Key.ENTER)
    time.sleep(1)
    # Update
    myTools.pressTAB(1)
    type(Key.ENTER)
    time.sleep(1)    

#---------------------------------------------------#
def Create_SpecCredits(month):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("specialCredits" + str(month))
    logging.debug('Create_SpecCredits: ' + str(month))

    myTools.getFocus()

    # open a/r tran list
    type("t",KeyModifier.CTRL)
    time.sleep(2)

    Filter_Invoices()

    # move to last transaction (which should be an invoice) and open in
    type(Key.END)
    time.sleep(1)
    type(Key.ENTER)
    time.sleep(1)

    # apply a new special credit
    click("1415376820659.png")
    myTools.pressDOWN(5)    
    type(Key.ENTER)
    time.sleep(1)

    # type
    type(Key.TAB)

    # client
    type(Key.TAB)
        
    # date
    tranDate = str(month) + "/28/2013"
    type(tranDate)
    time.sleep(1)
    type(Key.TAB)       
            
    # Description
    type(Key.END)
    type(" - " + tranDate)
    time.sleep(1)
    myTools.pressTAB(2)

    # Fees
    feeAmount = 5 + month/float(100)
    type(str(feeAmount))
    time.sleep(1)    
    type(Key.TAB)

    # Costs
    costAmount = 4 + month/float(100)
    type(str(costAmount))
    time.sleep(1)    
    type(Key.TAB)

    # Interest
    interestAmount = 3 + month/float(100)
    type(str(interestAmount))
    time.sleep(1)    

    #save
    type("s",KeyModifier.CTRL)
    myTools.checkForUnappliedAmount()

    # close
    type(Key.F4,KeyModifier.CTRL)

    Clear_Filter()

    # close   
    type(Key.F4,KeyModifier.CTRL)
    myTools.sectionEndTimeStamp()