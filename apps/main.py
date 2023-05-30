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
    data1 = {"Sender": "Bob", "Message": "Test message 1", "Reciever": "You"}
    data2 = {"Sender": "You", "Message": "Test message 2", "Reciever": "Bob"}
    data3 = {"Sender": "Bob", "Message": "Test message 3", "Reciever": "You"}
    data4 = {"Sender": "You", "Message": "Test message 4", "Reciever": "Bob"}
    data5 = {"Sender": "Bob", "Message": "Test message 5", "Reciever": "You"}
    data6 = {"Sender": "You", "Message": "Test message 6", "Reciever": "Bob"}
    data7 = {"Sender": "Bob", "Message": "Test message 7", "Reciever": "You"}
    data8 = {"Sender": "You", "Message": "Test message 8", "Reciever": "Bob"}
    list = [data1,data2,data3,data4,data5,data6,data7,data8]
    dataJsonify = jsonify(list)  # This is used to return the Json back to the front end. so return the final value

    return dataJsonify


def runAI():
    messages = [
        "Hey! How's it going?",
        "Hi! I'm doing great, thanks for asking. How about you?",
        "I'm good too. Just finished work for the day. Any plans for the evening?",
        "Not much, just thinking of catching a movie. Any recommendations?",
        "Well, if you're into action movies, 'John Wick' is a must-watch!",
        "Oh, I've heard a lot about it. I'll definitely check it out. Thanks!",
        "No problem! Let me know how you like it. So, any exciting news on your end?",
        "Actually, I just got promoted at work! I'm really thrilled about it.",
        "Wow, congratulations! That's fantastic news. You've been working hard for it.",
        "Thank you! It feels great to see the efforts paying off. How's everything going on your side?",
        "Things are good. I've been trying out some new recipes in the kitchen lately.",
        "That sounds fun! What's been your favorite dish so far?",
        "I made a delicious pasta dish with homemade sauce. It turned out surprisingly well.",
        "Yum! I'm getting hungry just thinking about it. Any chance you can share the recipe?",
        "Of course! I'll send it to you later. I'm sure you'll enjoy it. So, what's your favorite type of cuisine?",
        "I'm a big fan of Mexican food. Tacos and guacamole are my weaknesses.",
        "Same here! sMexican cuisine is so flavorful. We should plan a taco night sometime.",
        "That's a great idea! I'll bring the guacamole. Let's make it happen next week.",
        "Perfect! Looking forward to it. Oh, by the way, did you catch the latest sports game?",
        "Unfortunately, I missed it. Who won? Fill me in on the highlights.",
        "It was an intense match, but the home team managed to secure a victory in overtime.",
        "That sounds thrilling! I'll have to catch the highlights later. Which sport was it?",
        "It was a basketball game. The level of competition was off the charts.",
        "Basketball games can be so exciting. I'll make sure to watch the recap. Thanks for sharing.",
        "No problem! Let me know your thoughts once you've seen it. So, anything else new happening?",
        "Well, I'm planning a trip to Europe next month. It's going to be an amazing adventure.",
        "That's incredible! Which countries are you planning to visit?",
        "I'm starting in Italy, then heading to France and Spain. Can't wait to explore the different cultures.",
        "That's a fantastic itinerary. Take lots of pictures and make incredible memories!",
        "Absolutely! I'll be sure to share the highlights with you. So, what's been your favorite movie lately?",
        "Recently, I watched 'Inception' and it blew my mind. The concept was mind-bending.",
        "I've heard great things about 'Inception.' It's on my watchlist. I'll definitely check it out soon.",
        "Trust me, you won't be disappointed. Christopher Nolan's direction is brilliant. Let's discuss it once you've seen it.",
        "Deal! Looking forward to it. Well, I should get going now. Have a fantastic evening!",
        "You too! Enjoy the movie and have a wonderful time. Catch up with you later!",
        "Thanks! Talk to you soon. Take care and bye for now!"]

    firstModel.runProgramTest(messages)

if __name__ == "__main__":
    app.run(debug=True, port=8000)