from sikuli import *
import logging
import shutil

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Delete_Data_Folder():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('Delete_Data_Folder')

    if os.path.exists(Settings.dbFolder):
        logging.debug("- Delete folder:     %s" % Settings.dbFolder)
        shutil.rmtree(Settings.dbFolder)
    else:
        logging.debug("- Missing:           %s" % Settings.dbFolder)

