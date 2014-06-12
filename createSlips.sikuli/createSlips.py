from sikuli import *
import logging
import myTools
import initNames
import makeBackup

#---------------------------------------------------#
def Create_OneSlip(slipType,tk,act,cli,slipnum):
#---------------------------------------------------#

    logging.debug('- Create_OneSlip: ' + str(slipnum))

    type("n",KeyModifier.CTRL)
    time.sleep(1)

    # slip type
    type(slipType)

    # timekeeper
    type(Key.TAB)
    type(tk)

    # activity
    type(Key.TAB)
    type("2",KeyModifier.CTRL + KeyModifier.SHIFT)
    time.sleep(1)
    type(act)

    # client
    type(Key.TAB)
    time.sleep(1)   
    type(cli)
    time.sleep(1)

    # reference
    type(Key.TAB)
    # use down arrow for ref; skip every 8th one
    type(Key.HOME)
    for ref in range(slipnum%8):
        type(Key.DOWN)
    time.sleep(1)

    # extra
    type(Key.TAB)
    type("Slip: ")
    type(slipType)
    type(str(slipnum))
    time.sleep(1)

    # description
    type(Key.TAB)

    # start date for the first slip is 1/1/2013; increment the date every 4th slip.
    type(Key.TAB)
    if slipnum == 1:
        type("1/1/2013")
    elif (slipnum-1) % 4 == 0:
        type("+")

    type("s",KeyModifier.CTRL)
    time.sleep(1)

#---------------------------------------------------#
def Import_TimeSlips():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("import time slips")
    logging.debug('Import_TimeSlips')
    
# start tsimport
    logging.debug('- start TSImport')

    type("r",KeyModifier.KEY_WIN)
    time.sleep(1)
    type(Settings.tsimpEXE)
    type(Key.ENTER)
    time.sleep(2)

    wait("1386702753073.png",FOREVER)
    time.sleep(2)

    logging.debug('- set up slip template')
    type("f",KeyModifier.ALT)
    type("n")
    time.sleep(1)
    
    type("c")
    type(Key.ENTER)
    time.sleep(1)
    type(Key.ENTER)

#choose source
    wait("1386702883681.png")
    time.sleep(1)
    type("g",KeyModifier.ALT)
    time.sleep(1)
    paste(Settings.tSlipsFile)

#choose fields
    myTools.pressTAB(7)

# type
    myTools.pressDOWN(1)
    type(Key.ENTER)

# timekeeper
    myTools.pressDOWN(1)
    type(Key.ENTER)

# client
    myTools.pressDOWN(2)
    type(Key.ENTER)

# activity
    myTools.pressDOWN(2)
    type(Key.ENTER)

# reference
    myTools.pressDOWN(2)
    type(Key.ENTER)
    
# extra
    myTools.pressDOWN(2)
    type(Key.ENTER)
    
# date
    myTools.pressDOWN(2)
    type(Key.ENTER)


# omit 1st 10 records
    click("1386713105865-1.png")
    type(Key.TAB)
    type("12")
    time.sleep(1)        

# import data
    logging.debug('- import data')
    type(Key.F9)
    time.sleep(1)    
    type(Key.RIGHT)
    type(Key.ENTER)   
     
# verify data
    wait("1386704518399.png",FOREVER)
    if exists(Pattern("FailedImport-1.png").similar(0.95)):
        logging.debug('- import complete - no failed names')
    else:
        logging.debug('- import complete - some failed names')

# close tsimport
    logging.debug('- close TSImport')
    time.sleep(1)
    type(Key.RIGHT)
    type(Key.ENTER)   
    
    time.sleep(1)
    type("f",KeyModifier.ALT)
    type("x")
    time.sleep(1)
    type("n")
    
    myTools.sectionEndTimeStamp()
    
# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Import_ExpenseSlips():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("import expense slips")
    logging.debug('Import_ExpenseSlips')
    
# start tsimport
    logging.debug('- start TSImport')

    type("r",KeyModifier.KEY_WIN)
    time.sleep(1)
    type(Settings.tsimpEXE)
    type(Key.ENTER)
    time.sleep(2)

    wait("1386702753073.png",FOREVER)
    time.sleep(2)

    logging.debug('- set up slip template')
    type("f",KeyModifier.ALT)
    type("n")
    time.sleep(1)
    
    type("c")
    type(Key.ENTER)
    time.sleep(1)
    type(Key.ENTER)

#choose source
    wait("1386702883681.png")
    time.sleep(1)
    type("g",KeyModifier.ALT)
    time.sleep(1)
    paste(Settings.eSlipsFile)

#choose fields
    myTools.pressTAB(7)

# type
    myTools.pressDOWN(1)
    type(Key.ENTER)

# timekeeper
    myTools.pressDOWN(1)
    type(Key.ENTER)

# client
    myTools.pressDOWN(2)
    type(Key.ENTER)

# activity
    myTools.pressDOWN(2)
    type(Key.ENTER)

# reference
    myTools.pressDOWN(2)
    type(Key.ENTER)
    
# extra
    myTools.pressDOWN(2)
    type(Key.ENTER)
    
# date
    myTools.pressDOWN(2)
    type(Key.ENTER)


# omit 1st 10 records
    click("1386713105865-1.png")
    type(Key.TAB)
    type("12")
    time.sleep(1)        

# import data
    logging.debug('- import data')
    type(Key.F9)
    time.sleep(1)    
    type(Key.RIGHT)
    type(Key.ENTER)   
     
# verify data
    wait("1386704518399.png",FOREVER)
    if exists(Pattern("FailedImport-1.png").similar(0.95)):
        logging.debug('- import complete - no failed names')
    else:
        logging.debug('- import complete - some failed names')

# close tsimport
    logging.debug('- close TSImport')
    time.sleep(1)
    type(Key.RIGHT)
    type(Key.ENTER)   
    
    time.sleep(1)
    type("f",KeyModifier.ALT)
    type("x")
    time.sleep(1)
    type("n")        
    
    myTools.sectionEndTimeStamp()    

#---------------------------------------------------#
def Create_Slips(tmslips,exslips):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("init names")
    logging.debug('Init Names')    

    clients = initNames.Init_Clients()
    timekeepers = initNames.Init_Timekeepers()
    tasks = initNames.Init_Tasks()
    expenses = initNames.Init_Expenses()
    count = 0
    myTools.sectionEndTimeStamp()

    myTools.sectionStartTimeStamp("create time slips")
    myTools.getFocus()
    type("m",KeyModifier.CTRL)
    time.sleep(1)

    for slip in range(tmslips):
        Create_OneSlip("t",timekeepers[count%len(timekeepers)],tasks[count%len(tasks)],clients[count%len(clients)],count+1)
        count += 1
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)
    myTools.sectionEndTimeStamp()

    Import_TimeSlips()

    myTools.sectionStartTimeStamp("create expense slips")
    # increase count to account for imported slips
    count += 692

    myTools.getFocus()

    type("m",KeyModifier.CTRL)
    time.sleep(1)

    # for expenses, got to the end of the list and open the slip so we can copy dates.
    type(Key.END)
    type(Key.ENTER)
    time.sleep(1)

    for slip in range(exslips):
        Create_OneSlip("e",timekeepers[count%len(timekeepers)],expenses[count%len(expenses)],clients[count%len(clients)],count+1)
        count += 1
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)

    type(Key.F4,KeyModifier.CTRL)
    myTools.sectionEndTimeStamp()

    Import_ExpenseSlips()

    makeBackup.Backup_Checkpoint("slips")