import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:COS730_BBM/Models/message.dart';

class ChatScreen extends StatefulWidget {
  final String conversation;
  final String displayImage;

  ChatScreen({required this.conversation, required this.displayImage});

  @override
  _ChatScreenState createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  List<Message> messages = [];
  TextEditingController _textEditingController = TextEditingController();

  @override
  void initState() {
    super.initState();
    fetchPreviousMessages();
  }

  Future<void> fetchPreviousMessages() async {
    try {
      final url = 'http://10.0.2.2:8000/get_messages'; //For android emulator
      final response = await http.post(
        Uri.parse(url),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({"conversation": widget.conversation}),
      );
      if (response.statusCode == 200) {
        final jsonResponse = jsonDecode(response.body);
        
        final List<Message> previousMessages = [];
        for (var md in jsonResponse) {
          final message = Message(
            sender: md["Sender"],
            text: md["Message"],
            receiver: md["Receiver"],
          );
          previousMessages.add(message);
        }
        setState(() {
          messages = previousMessages;
        });
        print('Fetched previous messages successfully!');
      } else {
        print(
            'Failed to fetch previous messages. Error: ${response.statusCode}');
      }
    } catch (e) {
      print('Failed to fetch previous messages. Exception: $e');
    }
  }

  Future<void> sendMessage(Message message) async {
    try {
      final msg = jsonEncode({
        "Sender": message.sender,
        "Message": message.text,
        "Receiver": message.receiver,
      });
      final url = 'http://10.0.2.2:8000/send_message'; //For android emulator
      final response = await http.post(
        Uri.parse(url),
        headers: {'Content-Type': 'application/json'},
        body: msg,
      );
      if (response.statusCode == 200) {
        print('Message sent successfully!');
        final jsonResponse = jsonDecode(response.body);
        final newMessage = Message(
          sender: jsonResponse["Sender"],
          text: jsonResponse["Message"],
          receiver: jsonResponse["Receiver"],
        );
        addMessage(newMessage);
        print(jsonResponse);
        // Handle any further actions after successful message sending
      } else {
        print('Failed to send message. Error: ${response.statusCode}');
        // Handle any error cases
      }
    } catch (e) {
      print('Failed to send message. Exception: $e');
      // Handle any exceptions
    }
  }

  void addMessage(Message message) {
    setState(() {
      messages.add(message);
    });
  }

  Future<void> translateMessage(Message message) async {
    
    try {
      final url = 'http://10.0.2.2:8000/translate'; //For android emulator
      final response = await http.post(
        Uri.parse(url),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({"Name": widget.conversation}),
      );
      if (response.statusCode == 200) {
        final jsonResponse = jsonDecode(response.body);
        
        final List<Message> previousMessages = [];
        for (var md in jsonResponse) {
          final message = Message(
            sender: md["Sender"],
            text: md["Message"],
            receiver: md["Receiver"],
          );
          previousMessages.add(message);
        }
        setState(() {
          messages = previousMessages;
        });
        print('Fetched previous messages successfully!');
      } else {
        print(
            'Failed to fetch previous messages. Error: ${response.statusCode}');
      }
    } catch (e) {
      print('Failed to fetch previous messages. Exception: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Row(
          children: [
            Container(
              width: 50,
              height: 50,
              decoration: BoxDecoration(
                shape: BoxShape.rectangle,
                image: DecorationImage(
                  image: AssetImage(widget.displayImage),
                  fit: BoxFit.cover,
                ),
              ),
            ),
            SizedBox(width: 30),
            Text(widget.conversation),
          ],
        ),
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              itemCount: messages.length,
              itemBuilder: (context, index) {
                final message = messages[index];
                final bool shouldTranslate = message.text.endsWith("|~|");
                final String displayText = shouldTranslate
                    ? message.text.substring(0, message.text.length - 3)
                    : message.text;

                return ListTile(
                  title: Align(
                    alignment: message.sender == 'You'
                        ? Alignment.centerRight
                        : Alignment.centerLeft,
                    child: Stack(
                      children: [
                        Container(
                          padding: EdgeInsets.all(8),
                          decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(12),
                            color: message.sender == 'You'
                                ? Colors.blue
                                : Colors.grey,
                          ),
                          child: Text(
                            displayText + "   ",
                            style: TextStyle(
                              color: Colors.white,
                            ),
                          ),
                        ),
                        if (message.sender == 'You')
                          Positioned(
                            bottom: 0,
                            right: 0,
                            child: Container(
                              decoration: BoxDecoration(
                                color: Colors.blue,
                                borderRadius: BorderRadius.only(
                                  topLeft: Radius.circular(10),
                                ),
                              ),
                              width: 20,
                              height: 20,
                              child: Icon(
                                Icons.check,
                                color: Colors.white,
                                size: 14,
                              ),
                            ),
                          ),
                      ],
                    ),
                  ),
                  subtitle: shouldTranslate
                      ? Row(
                          children: [
                            IconButton(
                              icon: Icon(Icons.translate),
                              color: Colors.blue,
                              onPressed: () {
                                translateMessage(message);
                              },
                            ),
                          ],
                        )
                      : null,
                );
              },
            ),
          ),
          Container(
            padding: EdgeInsets.symmetric(horizontal: 8),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _textEditingController,
                    decoration: InputDecoration(
                      hintText: 'Type a message...',
                    ),
                  ),
                ),
                IconButton(
                  icon: Icon(Icons.send),
                  onPressed: () {
                    final text = _textEditingController.text;
                    if (text.isNotEmpty) {
                      final newMessage = Message(
                        sender: 'You',
                        text: text,
                        receiver: widget.conversation,
                      );
                      addMessage(newMessage);
                      _textEditingController.clear();
                      sendMessage(newMessage);
                    }
                  },
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
