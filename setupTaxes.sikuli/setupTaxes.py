from sikuli import *
import logging
import myTools


#---------------------------------------------------#
def Create_Jurisdictions():
#---------------------------------------------------#

    logging.debug('- Create_Jurisdiction')

    # move to jurisdictions
    myTools.pressF6(2)
    time.sleep(1)

    # new jurisdication for Zone 1
    logging.debug('-- new jurisdictions')  
    type("n",KeyModifier.ALT)
    time.sleep(1)
    type("o")
    myTools.pressTAB(1)
    type("Zone1")
    myTools.pressTAB(1)
    type("One")
    time.sleep(1)
    
    # OK
    type(Key.ENTER)

#---------------------------------------------------#
def Create_RateRules():
#---------------------------------------------------#
    logging.debug('- Create_RateRules')

    # switch to rate rules page
    myTools.pressSHIFTF6(1)
    time.sleep(1)

    Create_TimeOnly_RateRule()
    Create_ExpenseOnly_RateRule()
    Create_Compound_RateRules()
    Create_Minimum_RateRule()
    Create_Maximum_RateRule()



#---------------------------------------------------#
def Create_TimeOnly_RateRule():
#---------------------------------------------------#
    logging.debug('- Create_TimeOnly_RateRule')

    # new rule
    type("n",KeyModifier.ALT)
    type("Time Only")
    myTools.pressTAB(1)
    type("z")
    time.sleep(1)
    # rate
    myTools.pressTAB(2)
    type("4")
    # options   
    myTools.pressTAB(5)
    type(Key.SPACE)
    myTools.pressTAB(2)
    type(Key.SPACE)
    # save
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)
    # export to all
    type(Key.INSERT)
    myTools.pressTAB(1)
    type(Key.SPACE)    
    time.sleep(1)   

#---------------------------------------------------#
def Create_ExpenseOnly_RateRule():
#---------------------------------------------------#
    logging.debug('- Create_ExpenseOnly_RateRule')

    # new rule
    type("n",KeyModifier.ALT)
    type("Expense Only")
    myTools.pressTAB(1)
    type("z")
    time.sleep(1)
    # rate
    myTools.pressTAB(2)
    type("4.25")
    # type
    myTools.pressTAB(1)
    type("e")
    # options   
    myTools.pressTAB(5)
    type(Key.SPACE)
    myTools.pressTAB(2)
    type(Key.SPACE)
    myTools.pressTAB(1)
    # save
    type(Key.SPACE)
    time.sleep(1)
    # export to all
    type(Key.INSERT)
    myTools.pressTAB(1)
    type(Key.SPACE)    
    time.sleep(1)

#---------------------------------------------------#
def Create_Compound_RateRules():
#---------------------------------------------------#
    logging.debug('- Create_Compound_RateRule')

    # new rule
    type("n",KeyModifier.ALT)
    type("Compound2")
    myTools.pressTAB(1)
    type("z")
    time.sleep(1)
    # rate
    myTools.pressTAB(2)
    type("3")
    myTools.pressTAB(5)
    type(Key.SPACE)
    myTools.pressTAB(2)
    type(Key.SPACE)
    # save
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)
    # export to all
    type(Key.INSERT)
    myTools.pressTAB(1)
    type(Key.SPACE)    
    time.sleep(1)

    # new rule
    type("n",KeyModifier.ALT)
    type("Compound1")
    myTools.pressTAB(1)
    type("z")
    time.sleep(1)
    # rate
    myTools.pressTAB(2)
    type("3.5")
    # Type
    myTools.pressTAB(1)
    myTools.pressDOWN(2)  
    # compound
    myTools.pressTAB(2)    
    type("com")
    # options
    myTools.pressTAB(1)
    type(Key.SPACE)
    myTools.pressTAB(2)
    type(Key.SPACE)
    # save
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)
    # export to all
    type(Key.INSERT)
    myTools.pressTAB(1)
    type(Key.SPACE)    
    time.sleep(1)

#---------------------------------------------------#
def Create_Minimum_RateRule():
#---------------------------------------------------#
    logging.debug('- Create_Minimum_RateRule')

    # new rule
    type("n",KeyModifier.ALT)
    type("Minimum")
    myTools.pressTAB(1)
    type("z")
    time.sleep(1)
    # rate
    myTools.pressTAB(2)
    type("4.5")
    # minimum
    myTools.pressTAB(4)
    myTools.pressDOWN(1)
    time.sleep(1)
    # threshold
    myTools.pressTAB(1)
    type("1000")
    # options
    myTools.pressTAB(2)
    type(Key.SPACE)
    myTools.pressTAB(2)
    type(Key.SPACE)
    # save
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)
    # export to all
    type(Key.INSERT)
    myTools.pressTAB(1)
    type(Key.SPACE)    
    time.sleep(1)

#---------------------------------------------------#
def Create_Maximum_RateRule():
#---------------------------------------------------#
    logging.debug('- Create_Maximum_RateRule')

    # new rule
    type("n",KeyModifier.ALT)
    type("Maximum")
    myTools.pressTAB(1)
    type("z")
    time.sleep(1)
    # rate
    myTools.pressTAB(2)
    type("4.5")
    # maximum
    myTools.pressTAB(4)
    myTools.pressDOWN(2)
    time.sleep(1)
    # threshold
    myTools.pressTAB(1)
    type("1000")   
    # options
    myTools.pressTAB(2)
    type(Key.SPACE)
    myTools.pressTAB(2)
    type(Key.SPACE)
    # save
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)
    # export to all
    type(Key.INSERT)
    myTools.pressTAB(1)
    type(Key.SPACE)    
    time.sleep(1)

#---------------------------------------------------#
def Create_TaxProfile():
#---------------------------------------------------#
    logging.debug('- Create_TaxProfile')

    type("1",KeyModifier.CTRL)
    
    # new profile    
    type("n",KeyModifier.ALT)   
    type("MyTaxes")
    time.sleep(1)

    # Time rule    
    myTools.pressTAB(1)
    type("t")
    # Expense rule
    myTools.pressTAB(1)
    type("e")
    # Compound rule
    myTools.pressTAB(1)
    type("com")
    # Minimum rule
    myTools.pressTAB(1)
    type("min")
    # Maximum rule
    myTools.pressTAB(1)
    type("max")

    # OK
    time.sleep(1)
    type(Key.ENTER)    

    # DONE
    myTools.pressTAB(6)
    type(Key.ENTER)

#---------------------------------------------------#
def Change_TaxRule():
#---------------------------------------------------#
    logging.debug('- Change_TaxRule')

    logging.debug('-- open Taxes')
    type("p",KeyModifier.ALT)   
    type("t")
    time.sleep(2)

    logging.debug('-- open GA tax rule')
    type(Key.F6)
    type("g")
    type(Key.ENTER)
    time.sleep(1)

    logging.debug('-- change rate')
    myTools.pressTAB(3)
    type("7.25")
    type(Key.TAB)
    type(Key.END)
    time.sleep(1)

    logging.debug('-- change settings')
    type("s",KeyModifier.ALT)
    type("i",KeyModifier.ALT)
    type(Key.ENTER)
    click("1365991914214.png")

#---------------------------------------------------#
def Change_ClientSettings():
#---------------------------------------------------#

    logging.debug('- Change_ClientSettings')

    logging.debug('-- change a client')
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type(Key.ENTER)
    time.sleep(1)

    myTools.pressF6(4)
    if Settings.tsVersion == "2015":
        myTools.pressF6(3)       
    time.sleep(1)
    
    myTools.pressTAB(3)   
    time.sleep(1)
    type("my")

    logging.debug('-- save client')
    type("s",KeyModifier.CTRL)
    logging.debug('-- export settings')
    click("1384206308056.png")    
    
    # clear all and highlight tax profile
    type(Key.DELETE)
    time.sleep(1)
    type(Key.UP)
    type(Key.DOWN)

    # mark tax profile
    type(Key.F4)
    type(Key.TAB)

    # mark all clients
    type(Key.INSERT)
    time.sleep(1)

    # click export
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)
    type(Key.ENTER)

    myTools.waitForExportSuccess()
    
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)

#---------------------------------------------------#
def Change_TaskSettings():
#---------------------------------------------------#

    logging.debug('- Change_TaskSettings')

    logging.debug('-- change a task')
    type("y",KeyModifier.CTRL)
    time.sleep(1)
    type(Key.ENTER)
    time.sleep(1)
    type(Key.F6)
    time.sleep(1)
    myTools.pressTAB(3)   
    time.sleep(1)
    type(Key.F4)
    logging.debug('-- save task')
    type("s",KeyModifier.CTRL)
    logging.debug('-- export settings')
    rightClick("1387404402223.png")
    time.sleep(1)
    type("e")
    time.sleep(1)
    type(Key.TAB)    
    type(Key.PAGE_DOWN,KeyModifier.SHIFT)
    type(Key.F4)    
    type(Key.TAB)    
    type(Key.ENTER)    
    time.sleep(1)
    type(Key.ENTER)    
    time.sleep(1)
    type(Key.ENTER)    
    type("s",KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)

#---------------------------------------------------#
def Change_ExpenseSettings():
#---------------------------------------------------#

    logging.debug('- Change_ExpenseSettings')

    logging.debug('-- change an expense')
    type("y",KeyModifier.CTRL + KeyModifier.SHIFT)
    time.sleep(1)
    type(Key.ENTER)
    time.sleep(1)
    type(Key.F6)
    time.sleep(1)
    myTools.pressTAB(3)   
    myTools.pressDOWN(8)
    time.sleep(1)

    type(Key.F4)
    logging.debug('-- save expense')
    type("s",KeyModifier.CTRL)

    logging.debug('-- export settings')
    rightClick("1366001759780.png")
    time.sleep(1)
    type("e")
    time.sleep(1)

    type(Key.TAB)    
    type(Key.PAGE_DOWN,KeyModifier.SHIFT)
    type(Key.F4)    
    type(Key.TAB)    
    type(Key.ENTER)    
    time.sleep(1)
    type(Key.ENTER)    
    time.sleep(1)
    type(Key.ENTER)    
    type("s",KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)

#---------------------------------------------------#
def Setup_Taxes():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("setup taxes")

    logging.debug('Setup_Taxes')
    
    # make sure timeslips has focus
    myTools.getFocus()
    time.sleep(1)

    # open taxes UI
    logging.debug('-- open Taxes')
    type("p",KeyModifier.ALT)   
    type("t")
    time.sleep(2)

    Create_Jurisdictions()
    Create_RateRules()
    Create_TaxProfile()

#    Change_TaxRule()
    Change_ClientSettings()
#    Change_TaskSettings()
#    Change_ExpenseSettings()

    myTools.sectionEndTimeStamp()