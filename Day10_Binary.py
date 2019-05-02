#Task
#Given a Base-10 Integer (n) convert to Base-2. Plus find and print Base-10 int denoting the max number of consecutives 1's in n's Base-2 representation. 
#Constraints 1 <= n <= 10^6 (n is positive)
#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby

#Converts a Positive Base10 int to Base2 (Binary Number) - Positive Integer Only
def convertIntToBinary(number):
    BinaryStack = []
    while(number > 0):
        remainder = number%2
        number = number//2
        BinaryStack.append(remainder)
    
    while BinaryStack[0] == 0:
        BinaryStack.pop(BinaryStack[0])
        BinaryStack.append(0)

    #BinaryNumber = ''.join(map(str,BinaryStack)) - To Check BinaryNumber
    return (BinaryStack)

#Returns the max number of Consectuive 1's of a Binary Number with given postive input in Base10 integer
def consecutiveNumberof1InBinary(number):
    BStack = convertIntToBinary(number)
    lengthOf1 = 0 
    print(BStack)
    for k, g in groupby (BStack):
        group = list(g)
        lengthOfGroup = len(group)
        if(k == 1 and (lengthOfGroup > lengthOf1) ):
            lengthOf1 = lengthOfGroup

    print(lengthOf1)

if __name__ == '__main__':
    n = int(input())
    consecutiveNumberof1InBinary(n)



