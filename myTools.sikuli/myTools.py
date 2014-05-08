from sikuli import *
import datetime
import logging
#reload(logging)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def setupLog():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    Settings.myLogFile = os.environ['USERPROFILE'] + '\desktop\Sikuli\Sikuli.log'
    logging.basicConfig(filename=Settings.myLogFile, level=logging.DEBUG, format='%(message)s', filemode='w')
    # Level = DEBUG, INFO, WARNING, ERROR, CRITICAL

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def pressTAB(number):
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    if number != 0:
        for i in range(number):
            type(Key.TAB)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def pressSHIFTTAB(number):
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    if number != 0:
        for i in range(number):
            type(Key.TAB,KeyModifier.SHIFT)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def pressF6(number):
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    if number != 0:
        for i in range(number):
            type(Key.F6)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def pressSHIFTF6(number):
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    if number != 0:
        for i in range(number):
            type(Key.F6,KeyModifier.SHIFT)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def pressDOWN(number):
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    if number != 0:
        for i in range(number):
            type(Key.DOWN)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def pressUP(number):
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    if number != 0:
        for i in range(number):
            type(Key.UP)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def pressLEFT(number):
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    if number != 0:
        for i in range(number):
            type(Key.LEFT)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def pressRIGHT(number):
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    if number != 0:
        for i in range(number):
            type(Key.RIGHT)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def getFocus():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    if int(Settings.tsVersion) > 2013:
        click("1397240284893.png")

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def waitForExportSuccess():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    if int(Settings.tsVersion) > 2014:
        wait("1398732299997.png", FOREVER)
    else:        
        wait("1398732235702.png", FOREVER)
    type(Key.ENTER)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def startTimeStamp():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    Settings.startTime = datetime.datetime.now()
    logging.debug(' ')
    logging.debug('- - - - - - - - - - - - - - -')
    logging.debug(Settings.startTime.strftime("Started at: %Y-%m-%d %H:%M:%S"))
    logging.debug('- - - - - - - - - - - - - - -')

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def endTimeStamp():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    Settings.endTime = datetime.datetime.now()
    logging.debug(' ')
    logging.debug('- - - - - - - - - - - - - - -')
    logging.debug(Settings.endTime.strftime("Stopped at: %Y-%m-%d %H:%M:%S"))
    logging.debug('- - - - - - - - - - - - - - -')

    elapsedTime = Settings.endTime - Settings.startTime
    logging.debug("Elapsed:    %s" %elapsedTime)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def sectionStartTimeStamp(aSectionName):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    Settings.sectionName = aSectionName
    Settings.sectionStartTime = datetime.datetime.now()
    
    logging.debug(' ')
    logging.debug('- - - - - - - - - - - - - - -')
    logging.debug(Settings.sectionStartTime.strftime("Started at: %Y-%m-%d %H:%M:%S"))
    logging.debug('- - - - - - - - - - - - - - -')

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def sectionEndTimeStamp():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    Settings.sectionEndTime = datetime.datetime.now()
    logging.debug(' ')
    logging.debug('= = = = = = = = = = = = = = = = = = = =')
    logging.debug(Settings.sectionEndTime.strftime("Stopped at: %Y-%m-%d %H:%M:%S"))
    logging.debug('= = = = = = = = = = = = = = = = = = = =')

    sectionElapsedTime = Settings.sectionEndTime - Settings.sectionStartTime

    totalMinutes = sectionElapsedTime.seconds / float(60)
    totalMinutes = int(totalMinutes * 100) / 100.0
    
    logging.debug("Elapsed:    %s" %totalMinutes)

    durationLog = open(Settings.durationFile, "a")

    durationLog.write(Settings.sectionName + "," + str(totalMinutes) + "\n")
    durationLog.close()
