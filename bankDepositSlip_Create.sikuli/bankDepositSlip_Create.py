# creates new bank deposit slips each month
# adds new transactions to them

from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def Payment_CreateOne(pay_client,pay_month,pay_count):
#---------------------------------------------------#

    logging.debug('- Pay_Create: ' + str(pay_month) + "-" + pay_client)

    # new payment
    type("n",KeyModifier.CTRL)
    myTools.waitForTransaction()
    
    # type
    type(Key.TAB)
       
    # source
    type(Key.TAB)
        
    # check number
    check_num = "pay-" + str(pay_count) + "-" + str(pay_month)
    type(check_num)
    type(Key.TAB)
    time.sleep(1)        
            
    # client
    type(pay_client)
    time.sleep(1)
    type(Key.TAB)
        
    # date
    pay_date = str(pay_month) + "/28/2013"
    type(pay_date)
    time.sleep(1)
    type(Key.TAB)
        
    # skip deposit slip
    type(Key.TAB)
            
    # Amount
    pay_amount = 30 + pay_count + pay_month/float(100)
    type(str(pay_amount))
    type(Key.TAB)
        
    # Description
    type("a",KeyModifier.CTRL)
    type("bds-pay: " + pay_client + " - " + pay_date)
    type(Key.ENTER)
    time.sleep(1)

    # close / save
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.ENTER)

    myTools.checkForUnappliedAmount()

#---------------------------------------------------#
def PayToAccount_CreateOne(pta_client,pta_month,pta_count):
#---------------------------------------------------#

    logging.debug('- PTA_Create: ' + str(pta_month) + "-" + pta_client)

    # new pta
    type("n",KeyModifier.CTRL + KeyModifier.SHIFT)
    myTools.waitForTransaction()
    
    # skip type
    type(Key.TAB)      
        
    # skip deposit slip
    type(Key.TAB)
    
    # client
    type(pta_client)
    time.sleep(1)
    type(Key.TAB)

    # account
    type(Key.END)
    type(Key.TAB)   

    # date
    pta_date = str(pta_month) + "/28/2013"
    type(pta_date)
    time.sleep(1)
    type(Key.TAB)
            
    # check number
    check_num = "pta-" + str(pta_count) + "-" + str(pta_month)
    type(check_num)
    type(Key.TAB)
    time.sleep(1)        
    
    # Amount
    pta_amount = 20 + pta_count + pta_month/float(100)
    type(str(pta_amount))
    type(Key.TAB)
        
    # Description
    type("a",KeyModifier.CTRL)
    type("bds-pta: " + pta_client + " - " + pta_date)
    type(Key.ENTER)
    time.sleep(1)

    # close / save
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.ENTER)
    
    if exists("you_deposited_money.png"):
        type("n")  

#---------------------------------------------------#
def DepToAccount_CreateOne(dep_client,dep_month,dep_count):
#---------------------------------------------------#

    logging.debug('- DEP_Create: ' + str(dep_month) + "-" + dep_client)

    # new dep
    type("d",KeyModifier.CTRL + KeyModifier.SHIFT)
    myTools.waitForTransaction()
    
    # skip type
    type(Key.TAB)      
        
    # skip deposit slip
    type(Key.TAB)
    
    # client
    type(dep_client)
    time.sleep(1)
    type(Key.TAB)

    # account
    type(Key.END)
    type(Key.TAB)   

    # date
    dep_date = str(dep_month) + "/28/2013"
    type(dep_date)
    time.sleep(1)
    type(Key.TAB)
            
    # check number
    check_num = "dep-" + str(dep_count) + "-" + str(dep_month)
    type(check_num)
    type(Key.TAB)
    time.sleep(1)        
    
    # Amount
    dep_amount = 10 + dep_count + dep_month/float(100)
    type(str(dep_amount))
    type(Key.TAB)
        
    # Description
    type("a",KeyModifier.CTRL)
    type("bds-dep: " + dep_client + " - " + dep_date)
    type(Key.ENTER)
    time.sleep(1)

    # close / save
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.ENTER)
    
    if exists("you_deposited_money.png"):
        type("n")  

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BankDepositSlip_CreateOne(bds_month):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # open bank deposit slip list
    type("t",KeyModifier.ALT)
    type("b")
    time.sleep(1)

    if exists("create_bankdepositslip.png"):
        type("n")

    # create a new deposit slip
    rightClick("deposit_number.png")
    time.sleep(1)
    type(Key.DOWN)
    type(Key.ENTER)
    time.sleep(1)

    # for even months, use "new bank" otherwise use "default"
    if bds_month % 2 == 0:
        type(Key.END)
    else:
        type(Key.HOME)

    type(Key.TAB)

    # date
    bds_date = str(bds_month) + "/28/2013"
    type(bds_date)
    time.sleep(1)
    type(Key.TAB)

    # planned
    bds_planned = bds_month * 10
    type(str(bds_planned))
    time.sleep(1)

    # close
    type(Key.ENTER)
    time.sleep(1)
    

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def BankDepositSlips_Create(bds_month):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("bank deposit slip")
    logging.debug('BankDepositSlip_Create')

    # make sure timeslips has focus
    myTools.getFocus()

    BankDepositSlip_CreateOne(bds_month)

    clientList = ["Hadley","Halifax"]
    bds_count = 0

    # add transactions to deposit slip
    for bds_client in clientList:
        bds_count += 1
        Payment_CreateOne(bds_client,bds_month,bds_count)
        PayToAccount_CreateOne(bds_client,bds_month,bds_count)
        DepToAccount_CreateOne(bds_client,bds_month,bds_count)

    # close
    type(Key.F4,KeyModifier.CTRL)

    if exists("please_note.png"):
        type(Key.ENTER)  
   