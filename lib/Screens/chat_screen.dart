import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:COS730_BBM/Models/message.dart';

class ChatScreen extends StatefulWidget {
  final String conversation;

  ChatScreen({required this.conversation});

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
      final url =
        //  'http://127.0.0.1:8000/get_messages'; // For chrome
        'http://10.0.2.2:8000/get_messages'; //For android emulator
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
              reciever: md["Receiver"]);
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
        "Reciever": message.reciever
      });
      final url =          
          //'http://127.0.0.1:8000/send_message'; // For chrome
        'http://10.0.2.2:8000/send_message'; //For android emulator
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
          reciever: jsonResponse["Reciever"],
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

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.conversation),
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              itemCount: messages.length,
              itemBuilder: (context, index) {
                final message = messages[index];
                return ListTile(
                  title: Align(
                    alignment: message.sender == 'You'
                        ? Alignment.centerRight
                        : Alignment.centerLeft,
                    child: Container(
                      padding: EdgeInsets.all(8),
                      decoration: BoxDecoration(
                        borderRadius: BorderRadius.circular(12),
                        color:
                            message.sender == 'You' ? Colors.blue : Colors.grey,
                      ),
                      child: Text(
                        message.text,
                        style: TextStyle(
                          color: Colors.white,
                        ),
                      ),
                    ),
                  ),
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
                          reciever: widget.conversation);
                      addMessage(newMessage);
                      _textEditingController.clear();
                      sendMessage(newMessage); // Send the message via HTTP
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
