import difflib
import json


def readFilesAndCreateMessage(otherPerson):
    dictOfShit = readFromJSON()
    messages = []
    if otherPerson in dictOfShit:
        messages = dictOfShit[otherPerson]
    else:
        messages = []

    return messages


def readFilesAndCreateMessageForWhatsappFormat():
    file1 = open('test.txt', 'r')
    fulldetails = []
    Messages = []

    Lines = file1.readlines()
    for line in Lines:
        s = line.split(" - ")
        if len(s) == 2:
            p = s[1].split(": ")
            if len(p) >= 2:
               #Then #p[0] is name and p[1] is message
               fulldetails.append(p)
               Messages.append(str(p[1]))
    return fulldetails,Messages

def writeToJSON():
    with open("chats.json", "w") as fp:
        print("Ekse")

def readFromJSON():
    with open('chats.json', 'rb') as fp:
        n_list = json.load(fp)
        return n_list