#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    
    diag1 = 0
    diag2 = 0   

    n = arr[0].__len__()  

    for x in range(0, n):
        diag1 += arr[x][x]
        diag2 += arr[x][n-x-1]
    return abs(diag1-diag2) 


if __name__ == '__main__':
    
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)