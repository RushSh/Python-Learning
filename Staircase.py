#!/bin/python3

import math
import os
import random
import re
import sys


def printSpace():
    sys.stdout.write (' ')

def printHash():
    sys.stdout.write('#')

# Complete the staircase function below.
def staircase(n):


    #the farthest would be number n
    for x in range(0, n):

       count = count1 = 0
       callHashMethod = x
       callPrintSpaceMethod = n - x -1
      
       while count1 < callPrintSpaceMethod:
              printSpace()
              count1+=1
        
       while count <= callHashMethod:
            printHash()
            count+=1  

       print("")     


#better solution 
#n=int(input())
#m=" "
#t=1
#while n>n-n:
#    print((n-1)*m+t*("#"))
#    n=n-1
#    t=t+1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
