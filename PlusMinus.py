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
    positiveCount = negativeCount = zeroCount = 0

    for x in range (0, arrLength):
        if arr[x] == 0:
            zeroCount+=1
        elif arr[x] > 0:
            positiveCount+=1
        else:
            negativeCount+=1

    positiveRatio = positiveCount / arrLength
    negativeRatio = negativeCount/arrLength
    zeroRatio     = zeroCount/arrLength
        
    print(f'{positiveRatio:.6f}')
    print(f'{negativeRatio:.6f}')
    print(f'{zeroRatio:.6f}')


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
