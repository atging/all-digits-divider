# Test cases for AllDigitsDivider


import AllDigitsDivider
from colorama import Fore, Style


def testResult(top, bottom, sigDig=0):
    print(top, '/', bottom, '=', top / bottom, '(True result)')
    print('vs.')
    testResult = AllDigitsDivider.AllDigitsDivider(top, bottom, sigDig)
    print(testResult)

    testValue = ''
    decimalFound = False
    mySigDig = sigDig

    for c in testResult:
        if c == '.':
            decimalFound = True
            testValue += '.'
        elif decimalFound is True:
            if mySigDig > 0:
                testValue += str(c)
                mySigDig -= 1
            else:
                break
        else:
            testValue += str(c)

    print(testValue)
    trueValue = float(int(top / bottom * (10**sigDig))/(10**sigDig))
    print(trueValue)

    if trueValue == float(testValue):
        print(Fore.GREEN + 'PASS' + Style.RESET_ALL)
    else:
        print(Fore.RED + "FAIL" + Style.RESET_ALL)


testResult(6, 2)
testResult(30, 5)
testResult(30, 12)
testResult(1500, 16, 2)
testResult(17, 8, 2)
testResult(17, 64, 5)
testResult(2987235, 64, 5)
testResult(987654321987654321987654321, 64, 5)
testResult(25.5, 1.6, 3)
testResult(22, 7, 30)
testResult(25.55, 1.51, 10)  # TODO: bug, zeroes are skipped after decimal...
testResult(1000, 10, 2)  # TODO: bug, result is [10, 0]
