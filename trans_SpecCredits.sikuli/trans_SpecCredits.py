from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fFilter_Invoices():
#---------------------------------------------------#

    # selection
    logging.debug('- filters')
    click("selection_button.png")
    time.sleep(1)

    # clear any existing filters
    if exists("remove_all.png"):
        click("remove_all.png")   
        time.sleep(1)

    # add tran type filter
    click("trans_type.png")
    time.sleep(1)
    click("add_filter-1.png")
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
    myTools.waitForTransList()    

#---------------------------------------------------#
def fClear_Filter():
#---------------------------------------------------#

    # selection
    click("selection_button.png")
    time.sleep(1)
    # clear
    click("remove_all.png")
    time.sleep(1)
    # OK    
    type(Key.ENTER)
    time.sleep(1)
    # Update
    myTools.pressTAB(1)
    type(Key.ENTER)
    myTools.waitForTransList()    

#---------------------------------------------------#
def fCreate_SpecCredits(pMonth):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("specialCredits" + str(pMonth))
    logging.debug('Create_SpecCredits: ' + str(pMonth))

    myTools.getFocus()

    # open a/r tran list
    type("t",KeyModifier.CTRL)
    myTools.waitForTransList()

    fFilter_Invoices()

    # move to last transaction (which should be an invoice)
    type(Key.END)
    time.sleep(1)
    
    # open it
    type(Key.ENTER)
    myTools.waitForTransEntry()

    # apply a new special credit
    click("apply_new.png")
    myTools.pressDOWN(5)    
    type(Key.ENTER)
    time.sleep(1)

    # type
    type(Key.TAB)

    # client
    type(Key.TAB)
        
    # date
    tranDate = str(pMonth) + "/28/" + Settings.dataYear
    type(tranDate)
    time.sleep(1)
    type(Key.TAB)       
            
    # Description
    type(Key.END)
    type(" - " + tranDate)
    time.sleep(1)
    myTools.pressTAB(2)

    # Fees
    feeAmount = 5 + pMonth/float(100)
    type(str(feeAmount))
    time.sleep(1)    
    type(Key.TAB)

    # Costs
    costAmount = 4 + pMonth/float(100)
    type(str(costAmount))
    time.sleep(1)    
    type(Key.TAB)

    # Interest
    interestAmount = 3 + pMonth/float(100)
    type(str(interestAmount))
    time.sleep(1)    

    #save
    type("s",KeyModifier.CTRL)
    myTools.checkForUnappliedAmount()

    # close
    type(Key.F4,KeyModifier.CTRL)

    fClear_Filter()

    # close   
    type(Key.F4,KeyModifier.CTRL)
    myTools.sectionEndTimeStamp()