import json


class groupChat():
    def __init__(self, topic):
        self.topic = topic

    def addMessage(self,message):
        luist = self.readFromJSON()
        if self.topic in luist:
            t = luist[self.topic]
            messages = t["Messages"]
            temp = {"Sender":  "You", "Message": message}
            messages.append(temp)
            t["Messages"] = messages
        self.writeToJSON(luist)


    def retrievedetailsAndCheckExist(self):
        luist = self.readFromJSON()
        if self.topic in luist:
            return luist[self.topic]
        else:
            return None

    def readFromJSON(self):
        with open('NLP_Model\groupChat.json', 'rb') as fp:
            n_list = json.load(fp)
            return n_list

    def writeToJSON(self, kak):
        with open("NLP_Model\groupChat.json", "w") as fp:
            json.dump(kak, fp)