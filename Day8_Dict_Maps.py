#Dictionary - Key Value Pairs - No size restrain 
#Value == definiton of the Key 

import sys

myDictionary = {}

def addAContact (contactInfo):
    info = contactInfo.split()
    myDictionary[info[0]] = info[1]

def phoneNumberLookup(contactName):
    if contactName in myDictionary.keys():
        print(contactName,"=", myDictionary.get(contactName), sep='')
    else:
        print("Not found")


noOfContacts = int(input())
i = 0
#stringContactInformations = input("Enter Info ")

while i < noOfContacts:
    try:
        contactInfo = input()
    except EOFError:
        break
    addAContact(contactInfo)
    i += 1

while True:
    try:
        inp = input()
        if inp == "":
            break
        phoneNumberLookup(inp)
    except EOFError:
        break


