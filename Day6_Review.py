#Given a string "S" of length #N indexed from @0 to @N-1
#Print "Even" Index and "Odd" Indexed Characters as #2 space seperated strings on a single line 
#@0 is even index
#Input = 1st Line #of Test Cases, subsequent lines string "S"

#Constraints
#1<= T <= 10
#2<= length of S <= 10000
import sys

noOfCases = int(input())
stringLines = []

while len(stringLines) < noOfCases:
    try:
        line = input()
    except EOFError:
        break
    stringLines.append(line)

for line in stringLines:
    evenWord = []
    oddWord = []
    count = 0
    for char in line:
        if(count == 0):
            evenWord.append(char)
            count = 1
        else:
            oddWord.append(char)
            count = 0
    print(*evenWord, " " ,*oddWord , sep = "")

#Completed Working 