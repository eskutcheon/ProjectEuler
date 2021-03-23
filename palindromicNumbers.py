# palindromic number calculator
import numbers
import numpy as np


class PalindromeNumbers:
    def __init__(self, *args):
        if(len(args) < 1): # might just use the multipledispatch module next time
            self.base = 10 # if no base provided, assume you're working in the decimals
        else:
            assert isinstance(int(args[0]), numbers.Integral) and int(args[0]) >= 2 and int(args[0]) <= 10
            self.base = args[0]

    def isPalindromic(self, pNum: int) -> bool: # going to need to process stuff like hexadecimal input later
        pNum = getCorrectedNum(pNum)
        numDigits = self.getNumDigits(pNum)
        digits = getDigits(pNum, numDigits)
        if numDigits == 1:
            return True
        else:
            for i in range(numDigits//2):
                if(digits[i] != digits[numDigits-i-1]):
                    return False
            return True

    def highestPNum(self, upperBound): # doesn't take base into account with current version
        length = self.getNumDigits(upperBound)
        numArray = getDigits(upperBound, length)
        midIndex = length//2
        if(length % 2 == 0):
            if(numArray[midIndex-1] > numArray[midIndex]): ### PROBLEM: in the case that they're equal, it needs to move to the adjacent numbers for comparison
                numArray[midIndex-1] -= 1
            elif (numArray[midIndex-1] == numArray[midIndex]):
                pass ################################################ FIX
            for i in range(midIndex):
                numArray[i+midIndex] = numArray[midIndex-i-1]
        else:
            if(numArray[midIndex-1] > numArray[midIndex+1]):
                numArray[midIndex] -= 1
            for i in range(1,midIndex+1): # midIndex + i won't go out of bounds for an odd length since 2*midIndex < length
                numArray[midIndex+i] = numArray[midIndex-i]
        return int(''.join(map(str,numArray)))


    def getNumDigits(self, num: int) -> int:
        if num == 0:
            return 1
        else:
            return int(1 + (np.floor(np.log(num)/np.log(self.base))))


def getDigits(num: int, numDigits: int) -> list:
    digits = np.ones(numDigits).astype(int)
    # digits stored from leftmost to rightmost
    for i in range(numDigits):
        digits[numDigits-i-1] = num % 10
        num = num // 10
    return digits

def getCorrectedNum(num):
    assert isinstance(int(num), numbers.Integral) ### maybe rewrite later to ask user about alternate meaning, i.e. 'test 314 instead of 3.14?'
    return np.absolute(int(num)) # convert to positive integer


numby = PalindromeNumbers()
print(numby.highestPNum(999*999))