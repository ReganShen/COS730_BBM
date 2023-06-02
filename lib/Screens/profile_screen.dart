import 'package:flutter/material.dart';

class ProfileScreen extends StatefulWidget {
  @override
  _ProfileScreenState createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  String displayName = 'Jacques Van Der Merve';
  String statusMessage = 'Hello, world! is Julle Lekker?';
  String bbmPin = '12345678';
  String bbmCode = 'ABCD1234';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Profile'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            CircleAvatar(
              radius: 150,
              backgroundImage: AssetImage('assets/Me.jpg'),
            ),
            SizedBox(height: 20),
            Text(
              '$displayName',
              style: TextStyle(fontSize: 26),
            ),
            SizedBox(height: 10),
            ElevatedButton(
              onPressed: () {
                _showDialog(context);
              },
              child: Text('Change Display Name'),
              style: ElevatedButton.styleFrom(
                padding: EdgeInsets.symmetric(horizontal: 20, vertical: 10),
                textStyle: TextStyle(fontSize: 16),
                primary: Colors.blue, // Change the button color here
                onPrimary: Colors.white, // Change the text color here
              ),
            ),
            SizedBox(height: 20),
            Text(
              '$statusMessage',
              style: TextStyle(fontSize: 18),
            ),
            SizedBox(height: 10),
            ElevatedButton(
              onPressed: () {
                _showDialogStatus(context);
              },
              child: Text('Change Status Message'),
              style: ElevatedButton.styleFrom(
                padding: EdgeInsets.symmetric(horizontal: 20, vertical: 10),
                textStyle: TextStyle(fontSize: 16),
                primary: Colors.green, // Change the button color here
                onPrimary: Colors.white, // Change the text color here
              ),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                _showBBMPinDialog(context);
              },
              child: Text('View BBM Pin and Code'),
              style: ElevatedButton.styleFrom(
                padding: EdgeInsets.symmetric(horizontal: 20, vertical: 10),
                textStyle: TextStyle(fontSize: 16),
                primary: Colors.orange, // Change the button color here
                onPrimary: Colors.white, // Change the text color here
              ),
            ),
          ],
        ),
      ),
    );
  }

  void _showDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Display Name'),
          content: TextField(
            onChanged: (value) {
              setState(() {
                displayName = value;
              });
            },
            decoration: InputDecoration(
              labelText: 'New name',
            ),
          ),
          actions: [
            ElevatedButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: Text('Cancel'),
              style: ElevatedButton.styleFrom(
                padding: EdgeInsets.symmetric(horizontal: 10, vertical: 8),
                textStyle: TextStyle(fontSize: 14),
                primary: Colors.grey, // Change the button color here
                onPrimary: Colors.black, // Change the text color here
              ),
            ),
            ElevatedButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: Text('Save'),
              style: ElevatedButton.styleFrom(
                padding: EdgeInsets.symmetric(horizontal: 10, vertical: 8),
                textStyle: TextStyle(fontSize: 14),
                primary: Colors.grey, // Change the button color here
                onPrimary: Colors.black, // Change the text color here
              ),
            ),
          ],
        );
      },
    );
  }

  void _showDialogStatus(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Status'),
          content: TextField(
            onChanged: (value) {
              setState(() {
                statusMessage = value;
              });
            },
            decoration: InputDecoration(
              labelText: 'New status',
            ),
          ),
          actions: [
            ElevatedButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: Text('Cancel'),
              style: ElevatedButton.styleFrom(
                padding: EdgeInsets.symmetric(horizontal: 10, vertical: 8),
                textStyle: TextStyle(fontSize: 14),
                primary: Colors.grey, // Change the button color here
                onPrimary: Colors.black, // Change the text color here
              ),
            ),
            ElevatedButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: Text('Save'),
              style: ElevatedButton.styleFrom(
                padding: EdgeInsets.symmetric(horizontal: 10, vertical: 8),
                textStyle: TextStyle(fontSize: 14),
                primary: Colors.grey, // Change the button color here
                onPrimary: Colors.black, // Change the text color here
              ),
            ),
          ],
        );
      },
    );
  }

  void _showBBMPinDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return Dialog(
          child: Image.asset('assets/BBM_PIN.jpg'),
        );
      },
    );
  }
}