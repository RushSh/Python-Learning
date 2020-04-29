#!/bin/python3

import math
import os
import random
import re
import sys
from decimal import *

# Complete the plusMinus function below.
def plusMinus(arr):

    arrLength = arr.__len__()
    getcontext().prec = 2
    positiveValues = negativeValues = zeroValues = 0
    for x in range (0, arrLength):
        if arr[x] == 0:
            zeroValues+=1
        elif arr[x] > 0:
            positiveValues+=1
        else:
            negativeValues+=1
    positiveValues = positiveValues/arrLength
    negativeValues = negativeValues/arrLength
    zeroValues = zeroValues/arrLength
        
    print(Decimal(positiveValues))
    print(Decimal(negativeValues))
    print(Decimal(zeroValues))
        

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
