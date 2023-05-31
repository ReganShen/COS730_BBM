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
    l = [
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

    messages = ["How much time before there's regular travel back and forth to Mars? Roughly. Like a real civilization on Mars.",
"Well, I think it's going to take a while to build a real civilization that the real of the threshold that really matters is if we're getting past the great filter is do we have enough resources on Mars such that if the if the spaceships from Earth stop coming, you could survive?",
"Yeah. So that can only be just missing one little thing.",
"You'd be like you're on a long sea voyage and the only thing you're missing is vitamin C. Uh, it's only a matter of time, you know. Yeah. And those can be curtains. So you've got to have all the things necessary to sustain civilization on Mars.",
"And the reason that those ships stopped coming could be. World War three, or it could be due to a slow decline of civilization, so civilization here on Earth could end with a bang or a whimper or natural disasters.",
"Yeah, asteroid impacts in the bank category. Yeah, it could be like a whole series of things like. So like what killed the dinosaurs. Well, it wasn't just one thing, you know, it was like a whole bunch of things happened in a row and. You know, while they could have taken any one of those things, they had like three things happen and no dinosaurs, which is kind of amazing that crocodiles are still here.",
"Yeah, those fuckers, well, they're resilient crocodiles that they all that live on decayed meat and they love rotting meat. And so in a any kind of disastrous situation, there's a lot of dead creatures and the crocodiles love it. So that's why they're around crocodiles and bugs and mushrooms and shrews truths, which is why we're here. Yeah, exactly.",
"Our great, great, great, great, great, great grandparents were. What a strange thing someone like you had to come from. So there's hope.",
"There's hope for all you rodents out there. Yeah, well, you can go to Mars. Just keep doing your homework. Absolutely. So so there will be you see the great filter. What did you mean by that?",
"Well, so there's something called like the Fermi paradox of like, where are the aliens? Yeah. So, you know, where are the aliens? And I think it was Carl Sagan that said, like, if there either are a lot of aliens or none and the either they're equally terrifying. Hmm. If there are a lot of aliens.",
"Well, I mean, the invasion ship, you know, bug infestation just, you know, like the Starship Troopers style.",
"Well, yeah. I mean, it's like an alien civilization might just give us, like, a bug infestation. You know, it's like, hey, we left. That planet was fine. Now it's got a bunch of bugs. Just go fumigate it, you know, like we fumigate a house. And that's certainly possible. And then but if there are no aliens, well, could it be that all civilizations are just destroyed before they become interstellar?",
"You know? So, uh, and I want to be clear like that. To the best of my knowledge, there is no evidence for alien life on Earth. That alien there's no there's no evidence for alien life. There's no direct evidence.",
"For alien life, no. You know, and if somebody says, oh, what about this alien four of, you know, sighting or whatever, I'm like, listen, it's got to be at least as good as a 7-Eleven or ATM cam.",]
    for x in l:
        messages.append(x)
    firstModel.runProgramTest(messages)

if __name__ == "__main__":
    # app.run(debug=True, port=8000)
    runAI()