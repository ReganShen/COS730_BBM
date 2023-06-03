import difflib
import json


def readFilesAndCreateMessage(otherPerson):
    dictOfShit = readFromJSON()
    messages = []
    if otherPerson in dictOfShit:
        messages = dictOfShit[otherPerson]
    else:
        messages = []
    return messages#

def storeMessagesIsent(kaak):
    otherPerson = kaak["Receiver"]
    tempDict = {}
    tempDict["Sender"] = "You"
    tempDict["Message"] = str(kaak["Message"])
    tempDict["Receiver"] = str(kaak["Receiver"])
    dictOfShit = readFromJSON()
    messages = []
    if otherPerson in dictOfShit:
        messages = dictOfShit[otherPerson]
    else:
        messages = []
    messages.append(tempDict)
    dictOfShit[otherPerson] = messages
    writeToJSON(dictOfShit)

def storeMessagesRecieved(kaak):
    otherPerson = kaak["Sender"]
    dictOfShit = readFromJSON()
    messages = []
    if otherPerson in dictOfShit:
        messages = dictOfShit[otherPerson]
    else:
        messages = []
    messages.append(kaak)
    dictOfShit[otherPerson] = messages
    writeToJSON(dictOfShit)


def replaceAllMessages(person, info):
    dictOfShit = readFromJSON()
    if person in dictOfShit:
        del dictOfShit[person]
        dictOfShit[person] = info
    writeToJSON(dictOfShit)

def writeToJSON(stufftoRight):
    json_object = json.dumps(stufftoRight)
    with open("chats.json", "w") as fp:
       fp.write(json_object)
    fp.close()

def readFromJSON():
    with open('chats.json', 'rb') as fp:
        n_list = json.load(fp)
        fp.close()
        return n_list




