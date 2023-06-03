import difflib
import json


class trainedTopics():
    def __init__(self):
        #Topic must be Artificial Intelligence, sports, Gym, Cook, Paint, Gaming, music
        self.listOfTopics = self.getListOfTopicKeywords()

    def writeToJSON(self):
        with open("NLP_Model\keywords.json", "w") as fp:
            json.dump(self.listOfTopics, fp)
            fp.close()

    def readFromJSON(self):
        with open('NLP_Model\keywords.json', 'rb') as fp:
            n_list = json.load(fp)
            fp.close()
            return n_list


    def getListOfTopicKeywords(self):
        dict = self.readFromJSON()
        return dict

    def classifierIfExist(self,listOfWordsAndPercent):
        newListWithShit = []
        for p in listOfWordsAndPercent:
            percent = p[0]
            word = p[1]
            for t in self.listOfTopics:
                for keywords in self.listOfTopics[t]:
                    wordBefore = word + " "
                    wordAfter = " " + word
                    if word == keywords.lower():
                        # print(t + " : " + word)
                        stringsss = "#" + t #The # in front of a word means its a definite in the topic
                        tempShit = [percent,stringsss]
                        newListWithShit.append(tempShit)
                        break
                        break
                    elif wordBefore in keywords.lower() or wordAfter in keywords.lower():
                        r = self.string_similarity(word,keywords.lower()) #Here we updating the weighting when assigning a topic
                        stringsss = "#" + t  # The # in front of a word means its a definite in the topic
                        temp = r*percent
                        tempShit = [temp, stringsss]
                        newListWithShit.append(tempShit)
        #print(newListWithShit) #Now with this new list count all the classified topics and their percentage
        return self.getMajorityTopic(newListWithShit)
    def getMajorityTopic(self,ls):
        tempDict = {}
        for p in ls:
            percent = p[0]
            word = p[1] #If word begins with a #
            if word.startswith('#'):
                if word[1:] in tempDict:
                    tempDict[word[1:]] = tempDict[word[1:]] + float(percent)
                else:
                    tempDict[word[1:]] = float(percent)

        sortedDict = sorted(tempDict.items(), key=lambda x: x[1], reverse=True)
        converted_dict = dict(sortedDict)
        theOneAndOnly = ""
        for theTopic in converted_dict:
            theOneAndOnly = theTopic
            break
        return theOneAndOnly

    def string_similarity(self,str1, str2):
        result = difflib.SequenceMatcher(a=str1.lower(), b=str2.lower())
        return result.ratio()