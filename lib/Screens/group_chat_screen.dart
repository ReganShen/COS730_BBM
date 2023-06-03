import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class GroupChatScreen extends StatefulWidget {
  @override
  _GroupChatScreenState createState() => _GroupChatScreenState();
}

class _GroupChatScreenState extends State<GroupChatScreen> {
  List<String> groupChats = [];  

 Future<void> runAi(String name) async {
    print('Running AI with name: $name');
    try {
      final msg = jsonEncode({"Name": name});
      final url =
          //'http://127.0.0.1:8000/run_ai'; // For chrome
          'http://10.0.2.2:8000/run_ai'; //For android emulator
      final response = await http.post(
        Uri.parse(url),
        headers: {'Content-Type': 'application/json'},
        body: msg,
      );
      if (response.statusCode == 200) {
        print('AI processing!');
        final jsonResponse = jsonDecode(response.body);
            
            for (var item in jsonResponse) {
          final confirmedTopic = item as String;
          final confirmInterest = await showConfirmationDialog(context, confirmedTopic);
          if (confirmInterest == true) {
            final groupName = confirmedTopic; // Use the confirmed topic as the group name

            if (!groupChats.contains(groupName)) {
              setState(() {
                groupChats.add(groupName);
              });
            }
          }
        }



        // final jsonResponse = List<Map<String, dynamic>>.from(jsonDecode(response.body));
        // for (var item in jsonResponse)
        // {
        //     item.forEach((key, value) {
        //       if (value is List) {
        //         print('Key: $key');
        //         print('Values: $value');
        //       }
        //     });
        // }
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


    Future<bool?> showConfirmationDialog(
    BuildContext context,
    String confirmedTopic,
  ) async {
    return showDialog<bool>(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Our AI picked up : $confirmedTopic'),
          content: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisSize: MainAxisSize.min,
            children: [
              Text(
                'Would you be interested in joining a group chat with people who also have an interest in $confirmedTopic?',
              ),
            ],
          ),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.pop(context, true); // User confirmed interest
              },
              child: Text('Yes'),
            ),
            TextButton(
              onPressed: () {
                Navigator.pop(context, false); // User declined interest
              },
              child: Text('No'),
            ),
          ],
        );
      },
    );    
  }

  void showSelectionPopup(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        String selectedName = '';

        return AlertDialog(
          title: Text('Select a contact to capture topics'),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              ListTile(
                title: Text('Bob'),
                onTap: () {
                  selectedName = 'Bob';
                  Navigator.pop(context, selectedName);
                },
              ),
              ListTile(
                title: Text('Jane'),
                onTap: () {
                  selectedName = 'Jane';
                  Navigator.pop(context, selectedName);
                },
              ),
              ListTile(
                title: Text('Alex'),
                onTap: () {
                  selectedName = 'Alex';
                  Navigator.pop(context, selectedName);
                },
              ),
              ListTile(
                title: Text('Theo'),
                onTap: () {
                  selectedName = 'Theo';
                  Navigator.pop(context, selectedName);
                },
              ),
            ],
          ),
        );
      },
    ).then((selectedName) {
      if (selectedName != null) {
        runAi(selectedName);
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Color.fromARGB(255, 196, 196, 196),
        centerTitle: true,
        title: Text(
          'Group Chats',
          style: TextStyle(fontSize: 24),
        ),
      ),
      body: Column(
        children: [
          Container(
            alignment: Alignment.center,
            padding: EdgeInsets.symmetric(vertical: 16),
            child: ElevatedButton(
              onPressed: () {
                showSelectionPopup(context);
              },
              style: ElevatedButton.styleFrom(
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(10),
                ),
                primary: Color.fromARGB(255, 140, 247, 163),
                padding: EdgeInsets.symmetric(horizontal: 30, vertical: 12),
              ),
              child: Text(
                'Find Groups',
                style: TextStyle(fontSize: 16),
              ),
            ),
          ),
          Expanded(
            child: ListView.builder(
              itemCount: groupChats.length,
              itemBuilder: (context, index) {
                final groupName = groupChats[index];
                return ListTile(
                  title: Text(groupName),
                  onTap: () {
                    // Handle group chat selection
                  },
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}