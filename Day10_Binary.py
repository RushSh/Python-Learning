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

def convertIntToBinary(number):
    BinaryStack = []
    while(number > 0):
        remainder = number%2
        number = number//2
        BinaryStack.append(remainder)
    
    if(BinaryStack[0] == 0):
        BinaryStack.pop(BinaryStack[0])
        BinaryStack.append(0)
    #BinaryNumber = ''.join(map(str,BinaryStack))
    return (BinaryStack)


def maxNumberof1InBinary(number):

    BStack = convertIntToBinary(number)
    #a, b = tee(BStack)
    #next(b, None)
    #return any(num1 == num2 and num1 == 2 for num1, num2 in izip(a, b))
    #val  = max(len(list(v)) for g,v in itertools.groupby(BStack))
    lengthOf1 = 0 
    for k, g in groupby (BStack):
        group = list(g)
        if(k == 1 and (len(group) > lengthOf1) ):
            lengthOf1 = len(group)
    #BinaryNumber = ''.join(map(str,BStack))
    #print(BinaryNumber)
    #maxLength = max(len(groups))
    print(lengthOf1)

if __name__ == '__main__':
    n = int(input())
    maxNumberof1InBinary(n)



