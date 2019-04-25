#Context
#Given a 6x6 2D Array A:
#HourGlass pattern
#a b c
#  d
#e f g
#16 hour glasses in A
#Task
#Calculate the hourglass sum of every hourglass in A, then print the maximum hourglass sum

#Things Given 
#2D Array is 6x6
#Max noOf Outcome is 16


import math
import os
import random
import re
import sys

#Calculate's for any array HourGlass with above structure. This is tested sucesfully with 6x6 Array
def calculateMaxHourGlass(array2DInput):

    SumAllHourGlass = []
    i = j = 0
    while( i+2 < len(array2DInput[0])):
        while(j+2 < len(array2DInput[0])):
            sum = array2DInput[i][j] + array2DInput[i][j+1] + array2DInput[i][j+2] + array2DInput[i+1][j+1] + array2DInput[i+2][j] + array2DInput[i+2][j+1] + array2DInput[i+2][j+2]
            SumAllHourGlass.append(sum)
            j+=1
        i+=1
        j=0
   
    print(max(SumAllHourGlass))

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    calculateMaxHourGlass(arr)