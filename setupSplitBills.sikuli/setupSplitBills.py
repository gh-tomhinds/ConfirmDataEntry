from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def Setup_SplitBills():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("setup split")
    logging.debug('- set up split bills')

    myTools.getFocus()

    # open split billing rule list
    type("b",KeyModifier.ALT)
    time.sleep(1)
    type("i")
    time.sleep(1)

    # new primary
    type("n",KeyModifier.ALT)
    time.sleep(1)
    
    # beverly
    type("bev")
    
    # split bill info
    myTools.pressTAB(1)    
    type("Beverly")
    
    # recurring
    myTools.pressTAB(2)
    type(Key.SPACE)

    # OK
    myTools.pressTAB(3)
    type(Key.SPACE)
    time.sleep(1)

    # new secondary
    myTools.pressTAB(7)
    type(Key.SPACE)
        
    # peabody
    type("pea")

    # percentages
    myTools.pressTAB(2)
    type("15")
    myTools.pressTAB(1)
    type("20")

    # ok
    myTools.pressTAB(3)
    type(Key.SPACE)
    time.sleep(1)

    # new secondary
    type(Key.SPACE)

    # saugus
    type("sau")

    # percentages
    myTools.pressTAB(2)
    type("20")
    myTools.pressTAB(1)
    type("25")

    # ok
    myTools.pressTAB(3)
    type(Key.SPACE)
    time.sleep(1)

    # done
    myTools.pressTAB(4)
    type(Key.SPACE)

    myTools.sectionEndTimeStamp()