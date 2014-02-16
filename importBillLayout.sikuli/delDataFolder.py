from sikuli import *
import logging

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Delete_Data_Folder():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('Delete_Data_Folder')
    rightClick("1351991222604-1.png")
    click("OpenWinEx-1.png")
    click("Libraries-1.png")
    type(Settings.tsFolder)
    type(Key.ENTER)

    if not exists(Pattern("Name.png").exact()):
        logging.debug('- need to sort folder by name')
        click("Name-1.png")
    
    if exists("Sikuli-1.png"):
        logging.debug('- the data folder exists')
        rightClick("Sikuli-1.png")
        time.sleep(1)
        type("d")
        time.sleep(1)
        type("y")
    else:
        logging.debug('- the data folder does not exist')
    time.sleep(1)
    type(Key.F4,KEY_ALT)
