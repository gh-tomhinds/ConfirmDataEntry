from sikuli import *
import logging
import myTools
import client_Create
import slips_ReplacementSlips
import ba__Common
import ba__ReviewBills

#===================================================#
def fReplaceTimeA():
#===================================================#

    # create a new client    
    client_Create.fCreate_Client("BA-ReplaceTimeA","BA-ReplaceTimeA","Replace Time A","Replace Time A","Replace Time A")
    # create some slips
    slips_ReplacementSlips.fCreate_ReplacementSlips("BA-ReplaceTimeA")
    # set up rule
    slips_ReplacementSlips.fCreate_ReplacementRule("BA-ReplaceTimeA","t","c","General")
    # print a bill to text
    ba__Common.fPrint_BABill("BA-ReplaceTimeA",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-ReplaceTimeA1")