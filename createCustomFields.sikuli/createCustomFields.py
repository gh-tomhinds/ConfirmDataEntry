from sikuli import *
import logging

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def CreateOne(name, downArrow):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug('- create ' + name)

    type("n",KeyModifier.ALT)
    time.sleep(1)
    for i in range(downArrow+1):
        type(Key.DOWN)
    type(Key.ENTER)
    time.sleep(1)
    type(name)
    type(Key.ENTER)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def FillList():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug('- fill list')

    doubleClick("ListList-1.png")
    listItems = ['Barnstable','Berkshire','Bristol','Dukes','Essex','Franklin','Hampden','Hampshire','Middlesex','Nantucket','Norfolk','Plymouth','Suffolk','Worcester']

    for listItem in listItems:
        type("n",KeyModifier.ALT)
        type(listItem)
        time.sleep(1)
        type(Key.ENTER)
        time.sleep(1)
    type(Key.ENTER)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Create_CustomFields():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug(' ')
    logging.debug('Create_CustomFields')

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open custom fields dialog box')
    type("p",KeyModifier.ALT)
    type("c")
    time.sleep(1)

    customFields = ['Date','Hours','List','Money','Number','Percent','Text','Timekeeper']
    for customField in customFields:
        CreateOne(customField, customFields.index(customField))
    FillList()
    type(Key.ENTER)
    time.sleep(10)
