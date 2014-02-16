from sikuli import *
import logging
import csv

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Create_OneSlip(slipType,tk,act,cli,slipnum):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

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

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Create_Slips(tmslips,exslips):
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('- Create_Slips')

    # start with manually entered client, then load other clients from file
    clients = ["Agawam"]
    allClis = csv.DictReader(open(Settings.cliFile))

    for oneCli in allClis:
        clients.append(oneCli["NN1"])
    clients.sort()

    # start with manually entered timekeeper, then load other tks from file
    timekeepers = ["TomH"]
    allTks = csv.DictReader(open(Settings.tkFile))

    for oneTk in allTks:
        timekeepers.append(oneTk["NN1"])
    timekeepers.sort()

    # start with manually entered task, then load other tasks from file
    tasks = ["CON001"]
    allTasks = csv.DictReader(open(Settings.taskFile))

    for oneTask in allTasks:
        tasks.append(oneTask["nn2"])
    tasks.sort()

    # start with manually entered expense, then load other exps from file
    expenses = ["E001"]
    allExps = csv.DictReader(open(Settings.expFile))

    for oneExp in allExps:
        expenses.append(oneExp["NN2"])
    expenses.sort()

    type("m",KEY_CTRL)
    time.sleep(1)

    count = 0

    for slip in range(tmslips):
        Create_OneSlip("t",timekeepers[count%len(timekeepers)],tasks[count%len(tasks)],clients[count%len(clients)],count+1)
        count += 1
    type(Key.F4,KEY_CTRL)
    time.sleep(1)

    # for expenses, got to the end of the list and open the slip so we can copy dates.
    type(Key.END)
    type(Key.ENTER)
    time.sleep(1)

    for slip in range(exslips):
        Create_OneSlip("e",timekeepers[count%len(timekeepers)],expenses[count%len(expenses)],clients[count%len(clients)],count+1)
        count += 1
    type(Key.F4,KEY_CTRL)
    time.sleep(1)

    type(Key.F4,KEY_CTRL)