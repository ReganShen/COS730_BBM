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

  Future<void> sendMessage(Message message) async {
    try {
      final url = 'http://localhost:8000/send_message'; // Replace with your server's URL
      final response = await http.post(
        Uri.parse(url),
        headers: {'Content-Type': 'application/json'},
        body: {"Message" : message},
      );
      if (response.statusCode == 200) {
        print('Message sent successfully!');
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
                  title: Text(message.text),
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
                      );
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
