from sikuli import *              

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
