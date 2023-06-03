from NLP_Model import firstModel
from flask import Flask, request, jsonify
import messages
from flask_cors import CORS
from Translator import translator
app = Flask(__name__)
CORS(app)

@app.route('/send_message', methods=['POST'])
def sendMessage():
    rawTransactionData = request.get_json()
    # print(rawTransactionData) #Need to add the raw transaction onto the chat conversation
    messages.storeMessagesIsent(rawTransactionData)
    toSendBack = MockConversationNow(rawTransactionData["Receiver"])
    dataJsonify = jsonify(toSendBack)  # This is used to return the Json back to the front end. so return the final value
    return dataJsonify

@app.route('/get_messages', methods=['POST'])
def getMessage():
    rawTransactionData = request.get_json()
    name = rawTransactionData["conversation"]
    list = messages.readFilesAndCreateMessage(name)
    dataJsonify = jsonify(list)  # This is used to return the Json back to the front end. so return the final value
    return dataJsonify

@app.route('/run_ai', methods=['POST'])
def conflictOFinterest():
    rawTransactionData = request.get_json()
    name = rawTransactionData["Name"]
    # print(name)
    # #For now I am going to change the code such that it only creates whatsapp groups with already learnt chats

    lst = runAI(name)
    classifiedTopics = []
    for r in lst:
        for p in r:
            if p not in classifiedTopics and p != "None":
                classifiedTopics.append(p)

    print(classifiedTopics)
    dataJsonify = jsonify(classifiedTopics)  # This is used to return the Json back to the front end. so return the final value
    return dataJsonify

@app.route('/translate', methods=['POST'])
def tra():
    rawTransactionData = request.get_json()
    name = rawTransactionData["Name"]
    list = messages.readFilesAndCreateMessage(name)
    #We will grab the chat and then translate everything

    for m in list:
        messag = m["Message"]
        t = translator.translateMessage(messag)
        m["Message"] = t
    messages.replaceAllMessages(name,list)
    dataJsonify = jsonify(list)  # This is used to return the Json back to the front end. so return the final value
    return dataJsonify


def checkIfNeedingTranslationForFront(list):
    #So first identify messages if it is not english then attach some shit to the user name or something to work on the front end side
    for message in list:
        NeedTranslation = translator.indentifyLanguage(message["Message"])
        if NeedTranslation == True:
            message["Message"] = message["Message"] + "|~|"
    return list

def MockConversationNow(person):
    #If the person is Alex we will do the translation shit, otherwise just random messages
    data = {}
    if person == "Alex":
        data["Sender"] = "Alex"
        data["Message"] = "你好"
        data["Receiver"] = "You"
    else:
        data["Sender"] = person
        data["Message"] = "Hello"
        data["Receiver"] = "you"
    # If a message needs to be translated it will add a little language thing at the end to identify, only for here cause then it always translates the message
    messages.storeMessagesRecieved(data)
    temp = checkIfNeedingTranslationForFront([data])
    return temp[0]




def runAI(name):
    message = []
    allDets = messages.readFilesAndCreateMessage(name)
    for l in allDets:
        message.append(l["Message"])

    listOfShit = firstModel.mainFunctionTorun(message)
    return listOfShit


if __name__ == "__main__":
    # checkIfNeedingTranslationForFront( messages.readFilesAndCreateMessage("Bob"))
    app.run(debug=True, port=8000)
    #runAI()