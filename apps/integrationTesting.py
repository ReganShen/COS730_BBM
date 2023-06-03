import unittest
from unittest.mock import patch
from flask_testing import TestCase
from main import app, sendMessage, getMessage, conflictOFinterest, tra, groupChat, groupChatSendMessage

class createInstance(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

class integrationTesting(createInstance):

    def test_send_Message(self):
        rawTransactionData = {
                "Sender": "You",
            "Message" : "Test Message",
            "Receiver" : "Alex",
        }
        response = self.client.post('send_message', json = rawTransactionData)
        self.assert200(response)
        data = {}
        data["Sender"] = "Alex"
        data["Message"] = "你好|~|"
        data["Receiver"] = "You"
        self.assertEqual(response.json, data)

    def test_get_Messages(self):
        rawTransactionData = {
                "conversation" : "Jane"
        }
        response = self.client.post('get_messages', json = rawTransactionData)
        self.assert200(response)
        self.assertEqual(response.json, [])

    def test_AI_Server(self):
        rawTransactionData = {
                "Name": "Alex"
        }
        response = self.client.post('run_ai', json = rawTransactionData)
        self.assert200(response)
        self.assertEqual(response.json, ['Gaming'])

    def test_translate(self):
        rawTransactionData = {
            "Name": "Jane"
        }
        response = self.client.post('translate', json=rawTransactionData)
        self.assert200(response)
        self.assertEqual(response.json, [])

    def test_create_Group_Chat(self):
        rawTransactionData = {
            "Topic": "Traveling"
        }
        response = self.client.post('groupChat', json=rawTransactionData)
        self.assert200(response)
        self.assertEqual(response.json, {'Decsription': 'Welcome to the traveling group chat, where we all have a '
                'interest in traveling',
 'Messages': [{'Message': 'Howzit Everyone Welcome', 'Sender': 'Bob'},
              {'Message': 'Thanks bob good to be here', 'Sender': 'John'}]})

    def test_groupChat_message(self):
        rawTransactionData = {
            "Topic": "Art",
            "Message" : "Test Message"
        }
        response = self.client.post('groupChatSendMessage', json=rawTransactionData)
        self.assert200(response)
        self.assertEqual(response.json, {'Message': 'Howzit Juan, welcome. Excited to have you joining us',
 'Receiver': 'you',
 'Sender': 'Fred'})



if __name__ == '__main__':
    unittest.main()