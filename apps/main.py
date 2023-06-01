from NLP_Model import firstModel
from flask import Flask, request, jsonify
import requests
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
    print(rawTransactionData["conversation"])
    data1 = {"Sender": "Bob", "Message": "Hey, how's it going?", "Receiver": "You"}
    data2 = {"Sender": "You", "Message": "Hey Bob! I'm doing great, thanks for asking. How about you?",
             "Receiver": "Bob"}
    data3 = {"Sender": "Bob",
             "Message": "I'm doing well too. Just wanted to catch up and see what you've been up to lately.",
             "Receiver": "You"}
    data4 = {"Sender": "You",
             "Message": "That's awesome! I've been busy with work but also managed to go on a short vacation. It was refreshing!",
             "Receiver": "Bob"}
    data5 = {"Sender": "Bob", "Message": "Oh, that sounds nice. Where did you go for your vacation?", "Receiver": "You"}
    data6 = {"Sender": "You",
             "Message": "I went to a beach resort in Mexico. The weather was perfect, and I had a great time relaxing by the ocean.",
             "Receiver": "Bob"}
    data7 = {"Sender": "Bob",
             "Message": "That sounds amazing. I'm a bit jealous! Maybe I should plan a vacation soon too.",
             "Receiver": "You"}
    data8 = {"Sender": "You",
             "Message": "Definitely! You deserve a break. Let me know if you need any recommendations or help planning your trip.",
             "Receiver": "Bob"}
    data9 = {"Sender": "Bob",
             "Message": "Thanks, I appreciate it! By the way, have you watched any good movies recently?",
             "Receiver": "You"}
    data10 = {"Sender": "You",
              "Message": "Yes, I watched a really interesting sci-fi movie last weekend. The plot was mind-bending!",
              "Receiver": "Bob"}
    data11 = {"Sender": "Bob",
              "Message": "Oh, I love sci-fi movies! What was the name of the movie? I'd like to check it out.",
              "Receiver": "You"}
    data12 = {"Sender": "You",
              "Message": "It's called 'The Matrix'. I highly recommend it. The special effects and storyline are exceptional.",
              "Receiver": "Bob"}
    data13 = {"Sender": "Bob",
              "Message": "I've heard of 'The Matrix'. It's considered a classic. I'll definitely add it to my watchlist. Thanks for the recommendation!",
              "Receiver": "You"}
    data14 = {"Sender": "You",
              "Message": "You're welcome, Bob! I'm sure you'll enjoy it. Let me know what you think after watching it.",
              "Receiver": "Bob"}

    list = [data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14]
    dataJsonify = jsonify(list)  # This is used to return the Json back to the front end. so return the final value

    return dataJsonify


def runAI():
    messages = readFilesAndCreateMessage()[1]
    firstModel.mainFunctionTorun(messages)

def readFilesAndCreateMessage():
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
if __name__ == "__main__":
    # app.run(debug=True, port=8000)
    runAI()