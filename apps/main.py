from NLP_Model import firstModel
from flask import Flask, request, jsonify
import messages
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/send_message', methods=['POST'])
def sendMessage():
    rawTransactionData = request.get_json()
    print(rawTransactionData)
    data = {"Sender" : "Bob", "Message" : "Test message", "Reciever" : "You" }
    dataJsonify = jsonify(data)  # This is used to return the Json back to the front end. so return the final value
    return dataJsonify

@app.route('/get_messages', methods=['POST'])
def getMessage():
    rawTransactionData = request.get_json()
    name = rawTransactionData["conversation"]
    print(name)
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


def runAI(name):
    message = []
    allDets = messages.readFilesAndCreateMessage(name)
    for l in allDets:
        message.append(l["Message"])

    listOfShit = firstModel.mainFunctionTorun(message)
    return listOfShit


if __name__ == "__main__":
    app.run(debug=True, port=8000)
    #runAI()