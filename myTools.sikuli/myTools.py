from sikuli import *
import datetime
import logging
import shutil

#---------------------------------------------------#
def setupLog():
#---------------------------------------------------#

    Settings.myLogFile = os.environ['USERPROFILE'] + '\desktop\Sikuli\Sikuli.log'
    logging.basicConfig(filename=Settings.myLogFile, level=logging.DEBUG, format='%(message)s', filemode='w')
    # Level = DEBUG, INFO, WARNING, ERROR, CRITICAL

#---------------------------------------------------#
def pressTAB(number):
#---------------------------------------------------#

    if number != 0:
        for i in range(number):
            type(Key.TAB)

#---------------------------------------------------#
def pressSHIFTTAB(number):
#---------------------------------------------------#

    if number != 0:
        for i in range(number):
            type(Key.TAB,KeyModifier.SHIFT)

#---------------------------------------------------#
def pressF6(number):
#---------------------------------------------------#

    if number != 0:
        for i in range(number):
            type(Key.F6)

#---------------------------------------------------#
def pressSHIFTF6(number):
#---------------------------------------------------#

    if number != 0:
        for i in range(number):
            type(Key.F6,KeyModifier.SHIFT)

#---------------------------------------------------#
def pressDOWN(number):
#---------------------------------------------------#

    if number != 0:
        for i in range(number):
            type(Key.DOWN)

#---------------------------------------------------#
def pressUP(number):
#---------------------------------------------------#

    if number != 0:
        for i in range(number):
            type(Key.UP)

#---------------------------------------------------#
def pressLEFT(number):
#---------------------------------------------------#

    if number != 0:
        for i in range(number):
            type(Key.LEFT)

#---------------------------------------------------#
def pressRIGHT(number):
#---------------------------------------------------#

    if number != 0:
        for i in range(number):
            type(Key.RIGHT)

#---------------------------------------------------#
def getFocus():
#---------------------------------------------------#

    if int(Settings.tsVersion) > 2013:
        click("billing_date_statusbar.png")

#---------------------------------------------------#
def waitForExportSuccess():
#---------------------------------------------------#

    if int(Settings.tsVersion) > 2014:
        wait("export_successful_small.png", FOREVER)
    else:        
        wait("export_successful_wide.png", FOREVER)
    type(Key.ENTER)

#---------------------------------------------------#
def enterSlipFilter(pMonth,pExtraTab):
#---------------------------------------------------#

    logging.debug('- enterSlipFilter: ' + str(pMonth) + ' ' + pExtraTab)

    wait("slip_trans_date.png",60)
    time.sleep(1)
    
    click("slip_trans_date.png")
    time.sleep(1)
    click("add_filter.png")
    wait("apply_this_rule.png",60)

    # choose TODAY to get to manual date entry
    logging.debug('-- choose TODAY')
    
    type(Key.DOWN)
    type(Key.ENTER)
    time.sleep(1)

    # type in dates
    logging.debug('-- enter date range')
    
    if pExtraTab == "y":       
        pressTAB(7)
    else:
        pressTAB(6)

    time.sleep(1)

    startDate = "1/1/" + Settings.dataYear
    type(startDate)
    type(Key.TAB)
    
    if pMonth > 12:
        endDate = "12/31/" + Settings.dataYear
    else:
        endDate = str(pMonth) + "/27/" + Settings.dataYear
        
    type(endDate)
    time.sleep(1)

#---------------------------------------------------#
def waitForReport():
#---------------------------------------------------#

    logging.debug('- wait for report')
    time.sleep(1)

    if exists("replace_it.png"):
        logging.debug('-- replace msg exists')            
        type(Key.ENTER)
        time.sleep(1)        

    if exists("recalc_msg.png"):
        logging.debug('-- budget msg exists')        
        type(Key.ENTER)
        time.sleep(5)        

    #wait for "calculating" box to disappear
    while exists(Pattern("completed.png").similar(0.90)):
        logging.debug('-- completed msg exists')
        time.sleep(3)

#---------------------------------------------------#
def waitForTransList():
#---------------------------------------------------#
    time.sleep(2)
    wait("inv_num_column.png",60)
    time.sleep(2)

#---------------------------------------------------#
def waitForTransEntry():
#---------------------------------------------------#
    time.sleep(2)
    wait("ar_balance.png",60)
    time.sleep(2)

#---------------------------------------------------#
def waitForFundsList():
#---------------------------------------------------#
    time.sleep(1)
    wait("funds_account.png",60)
    time.sleep(1)

#---------------------------------------------------#
def startTSImport():
#---------------------------------------------------#

    logging.debug('- start TSImport')
    type("r",KeyModifier.KEY_WIN)
    time.sleep(1)
    type(Settings.tsimpEXE)
    type(Key.ENTER)
    time.sleep(2)

    wait("tsimport_menubar.png",FOREVER)
    time.sleep(4)

#---------------------------------------------------#
def doNotSaveReport():
#---------------------------------------------------#
        
    time.sleep(1)
    if exists("save_msg.png"):
        type("n")

#---------------------------------------------------#
def checkForUnappliedAmount():
#---------------------------------------------------#

    time.sleep(1)
    if exists("go_back_edit_transaction.png"):
        logging.debug("--> UNAPPLIED AMOUNT")
        type(Key.ENTER)
        time.sleep(1)

#---------------------------------------------------#
def padZero(pNumber):
#---------------------------------------------------#

    padNumber = str(pNumber)
    
    if pNumber < 10:
        padNumber = "0" + padNumber

    return(padNumber)

#---------------------------------------------------#
def monthToName(aMonth,aName,anExt):
#---------------------------------------------------#

    fileName = padZero(aMonth)

    # prefix the version
    fileName = Settings.tsVersion + aName + fileName + anExt    
        
    return(fileName)

#---------------------------------------------------#
def startTimeStamp():
#---------------------------------------------------#
    Settings.startTime = datetime.datetime.now()
    logging.debug(' ')
    logging.debug('---------------------------------------')
    logging.debug(Settings.startTime.strftime("Started at: %Y-%m-%d %H:%M:%S"))
    logging.debug('---------------------------------------')

#---------------------------------------------------#
def endTimeStamp():
#---------------------------------------------------#
    Settings.endTime = datetime.datetime.now()
    logging.debug(' ')
    logging.debug('---------------------------------------')
    logging.debug(Settings.endTime.strftime("Stopped at: %Y-%m-%d %H:%M:%S"))
    logging.debug('---------------------------------------')

    elapsedTime = Settings.endTime - Settings.startTime
    logging.debug("Elapsed:    %s" %elapsedTime)

#---------------------------------------------------#
def sectionStartTimeStamp(aSectionName):
#---------------------------------------------------#

    Settings.sectionName = aSectionName
    Settings.sectionStartTime = datetime.datetime.now()
    
    logging.debug(' ')
    logging.debug(' ')
    logging.debug('=======================================')
    logging.debug(Settings.sectionStartTime.strftime("Started at: %Y-%m-%d %H:%M:%S"))
    logging.debug('=======================================')

#---------------------------------------------------#
def sectionEndTimeStamp():
#---------------------------------------------------#
    Settings.sectionEndTime = datetime.datetime.now()
    logging.debug('---------------------------------------')
    logging.debug(Settings.sectionEndTime.strftime("Stopped at: %Y-%m-%d %H:%M:%S"))
    logging.debug('---------------------------------------')

    sectionElapsedTime = Settings.sectionEndTime - Settings.sectionStartTime

    totalMinutes = sectionElapsedTime.seconds / float(60)
    totalMinutes = int(totalMinutes * 100) / 100.0
    
    logging.debug("Elapsed:    %s" %totalMinutes)

    durationLog = open(Settings.durationFile, "a")

    durationLog.write(Settings.sectionName + "," + str(totalMinutes) + "\n")
    durationLog.close()

#---------------------------------------------------#
def pushReportLog(pReportName,pReportStatus):
#---------------------------------------------------#

    reportTime = datetime.datetime.now()
    reportTime = reportTime.strftime("%Y-%m-%d %H:%M:%S")
    reportLogLine = reportTime + "  " + pReportStatus + ": " + pReportName + "\n"

    reportLog = open(Settings.reportLogFile, "a")    
    reportLog.write(reportLogLine)
    reportLog.close()

#---------------------------------------------------#
def getScreenshot():
#---------------------------------------------------#

    logging.debug(' ')
    logging.debug('Get screenshot')

    wholeScreen = getBounds()
    ssIn = capture(wholeScreen)
    logging.debug('- old path: ' + ssIn)

    ssTime = datetime.datetime.now()    
    # add date to screenshot name
    ssOut = padZero(ssTime.year) + "-" + padZero(ssTime.month) + "-" + padZero(ssTime.day)
    # add time to screenshot name
    ssOut = ssOut + "-" + padZero(ssTime.hour) + padZero(ssTime.minute) + padZero(ssTime.second)
    # add extension to screenshot name
    ssOut = ssOut + ".png"
    # add path
    ssOut = Settings.sikFolder + "\\" + ssOut
    logging.debug('- new path: ' + ssOut)

    print(ssOut)

    shutil.move(ssIn,ssOut)    

#---------------------------------------------------#
def testRestore():
#---------------------------------------------------#

    # using this to test AVs when i try to restore

    logging.debug(' ')
    logging.debug('test restore')

    type("f",KeyModifier.ALT)
    type("r")
    time.sleep(3)
    type(Key.ESC)
