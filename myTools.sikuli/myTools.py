from sikuli import *
import datetime
import logging


def pressTAB(number):
    if number != 0:
        for i in range(number):
            type(Key.TAB)

def pressSHIFTTAB(number):
    if number != 0:
        for i in range(number):
            type(Key.TAB,KeyModifier.SHIFT)

def pressF6(number):
    if number != 0:
        for i in range(number):
            type(Key.F6)

def pressSHIFTF6(number):
    if number != 0:
        for i in range(number):
            type(Key.F6,KeyModifier.SHIFT)

def pressDOWN(number):
    if number != 0:
        for i in range(number):
            type(Key.DOWN)

def pressUP(number):
    if number != 0:
        for i in range(number):
            type(Key.UP)

def pressLEFT(number):
    if number != 0:
        for i in range(number):
            type(Key.LEFT)

def pressRIGHT(number):
    if number != 0:
        for i in range(number):
            type(Key.RIGHT)

def getFocus():
    if int(Settings.tsVersion) > 2013:
        click("1397240284893.png")

def startTimeStamp():
    Settings.startTime = datetime.datetime.now()
    logging.debug(' ')
    logging.debug('- - - - - - - - - - - - - - -')
    logging.debug(Settings.startTime.strftime("Started at: %Y-%m-%d %H:%M:%S"))
    logging.debug('- - - - - - - - - - - - - - -')

def endTimeStamp():
    endTime = datetime.datetime.now()
    logging.debug(' ')
    logging.debug('- - - - - - - - - - - - - - -')
    logging.debug(endTime.strftime("Stopped at: %Y-%m-%d %H:%M:%S"))
    logging.debug('- - - - - - - - - - - - - - -')

    elapsedTime = endTime - Settings.startTime
    logging.debug("Elapsed:    %s" %elapsedTime)


