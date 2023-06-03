import unittest
from unittest import mock
import messages
from unittest.mock import mock_open, patch
import os
from NLP_Model import firstModel,GroupChat, trainedTopics
import NLP_Model.trainedTopics as trainedTopics
import json
import main
from flask import Flask
from flask_cors import CORS
from Translator import translator
from googletrans import Translator as GoogleTranslator

class testTranslator(unittest.TestCase):

    def test_indentifyLanguage_returns_false_for_english_message(self):
        message = "Hello"
        with mock.patch.object(GoogleTranslator, 'translate') as mock_translate:
            mock_translate.return_value.src = 'en'
            result = translator.indentifyLanguage(message)
            self.assertFalse(result)

    def test_indentifyLanguage_returns_true_for_non_english_message(self):
        message = "Bonjour"
        with mock.patch.object(GoogleTranslator, 'translate') as mock_translate:
            mock_translate.return_value.src = 'fr'
            result = translator.indentifyLanguage(message)
            self.assertTrue(result)

    def test_translateMessage_returns_translation(self):
        message = "Hello"
        expected_translation = "Bonjour"
        with mock.patch.object(GoogleTranslator, 'translate') as mock_translate:
            mock_translate.return_value.text = expected_translation
            result = translator.translateMessage(message)
            self.assertEqual(result, expected_translation)


class Testmessages(unittest.TestCase):
    def setUp(self):
        # Create a temporary test file
        self.test_file = 'test_chats.json'
        with open(self.test_file, 'w') as f:
            json.dump({}, f)

    def tearDown(self):
        # Remove the temporary test file
        os.remove(self.test_file)

    @patch('builtins.open', new_callable=mock_open, read_data='{}')
    def test_readFilesAndCreateMessage_existing_person(self, mock_open):
        otherPerson = "Alice"
        dictOfShit = {
            "Alice": [
                {
                    "Sender": "Alice",
                    "Message": "Hello",
                    "Receiver": "You",
                },
                {
                    "Sender": "Alice",
                    "Message": "Hi",
                    "Receiver": "You",
                },
            ]
        }
        expected_message = dictOfShit[otherPerson]
        with patch('messages.readFromJSON', return_value=dictOfShit):
            message = messages.readFilesAndCreateMessage(otherPerson)
        self.assertEqual(message, expected_message)

    @patch('builtins.open', new_callable=mock_open, read_data='{}')
    def test_readFilesAndCreateMessage_non_existing_person(self, mock_open):
        otherPerson = "Bob"
        dictOfShit = {}
        expected_message = []
        with patch('messages.readFromJSON', return_value=dictOfShit):
            message = messages.readFilesAndCreateMessage(otherPerson)
        self.assertEqual(message, expected_message)

    @patch('builtins.open', new_callable=mock_open)
    @patch('messages.readFromJSON')
    @patch('messages.writeToJSON')
    def test_storemessageIsent_existing_person(self, mock_writeToJSON, mock_readFromJSON, mock_open):
        kaak = {
            "Receiver": "Alice",
            "Message": "Hey",
        }
        otherPerson = kaak["Receiver"]
        dictOfShit = {
            "Alice": [
                {
                    "Sender": "Alice",
                    "Message": "Hello",
                    "Receiver": "You",
                },
            ],
        }
        expected_dictOfShit = dictOfShit.copy()
        expected_dictOfShit[otherPerson].append({
            "Sender": "You",
            "Message": "Hey",
            "Receiver": "Alice",
        })
        mock_readFromJSON.return_value = dictOfShit

        messages.storeMessagesIsent(kaak)

        mock_writeToJSON.assert_called_once_with(expected_dictOfShit)

    @patch('builtins.open', new_callable=mock_open)
    @patch('messages.readFromJSON')
    @patch('messages.writeToJSON')
    def test_storemessageIsent_non_existing_person(self, mock_writeToJSON, mock_readFromJSON, mock_open):
        kaak = {
            "Receiver": "Bob",
            "Message": "Hi",
        }
        otherPerson = kaak["Receiver"]
        dictOfShit = {}
        expected_dictOfShit = {
            "Bob": [
                {
                    "Sender": "You",
                    "Message": "Hi",
                    "Receiver": "Bob",
                },
            ],
        }
        mock_readFromJSON.return_value = dictOfShit

        messages.storeMessagesIsent(kaak)

        mock_writeToJSON.assert_called_once_with(expected_dictOfShit)

    @patch('builtins.open', new_callable=mock_open)
    @patch('messages.readFromJSON')
    @patch('messages.writeToJSON')
    def test_storemessageRecieved_existing_person(self, mock_writeToJSON, mock_readFromJSON, mock_open):
        kaak = {
            "Sender": "Alice",
            "Message": "Hey",
        }
        otherPerson = kaak["Sender"]
        dictOfShit = {
            "Alice": [
                {
                    "Sender": "Alice",
                    "Message": "Hello",
                    "Receiver": "You",
                },
            ],
        }
        expected_dictOfShit = dictOfShit.copy()
        expected_dictOfShit[otherPerson].append(kaak)
        mock_readFromJSON.return_value = dictOfShit

        messages.storeMessagesRecieved(kaak)

        mock_writeToJSON.assert_called_once_with(expected_dictOfShit)

    @patch('builtins.open', new_callable=mock_open)
    @patch('messages.readFromJSON')
    @patch('messages.writeToJSON')
    def test_storemessageRecieved_non_existing_person(self, mock_writeToJSON, mock_readFromJSON, mock_open):
        kaak = {
            "Sender": "Bob",
            "Message": "Hi",
        }
        otherPerson = kaak["Sender"]
        dictOfShit = {}
        expected_dictOfShit = {
            "Bob": [
                {
                    "Sender": "Bob",
                    "Message": "Hi",
                },
            ],
        }
        mock_readFromJSON.return_value = dictOfShit

        messages.storeMessagesRecieved(kaak)

        mock_writeToJSON.assert_called_once_with(expected_dictOfShit)

    @patch('builtins.open', new_callable=mock_open)
    @patch('messages.readFromJSON')
    @patch('messages.writeToJSON')
    def test_replaceAllmessage_existing_person(self, mock_writeToJSON, mock_readFromJSON, mock_open):
        person = "Alice"
        info = [
            {
                "Sender": "Bob",
                "Message": "Hi",
            },
        ]
        dictOfShit = {
            "Alice": [
                {
                    "Sender": "Alice",
                    "Message": "Hello",
                    "Receiver": "You",
                },
            ],
        }
        expected_dictOfShit = dictOfShit.copy()
        expected_dictOfShit[person] = info
        mock_readFromJSON.return_value = dictOfShit

        messages.replaceAllMessages(person, info)

        mock_writeToJSON.assert_called_once_with(expected_dictOfShit)



    @patch('builtins.open', new_callable=mock_open, read_data='{"name": "John", "age": 30}')
    def test_readFromJSON(self, mock_open):
        expected_data = {"name": "John", "age": 30}

        data = messages.readFromJSON()
        mock_open.assert_called_once_with('chats.json', 'rb')
        self.assertEqual(data, expected_data)
        mock_open.return_value.close.assert_called_once()

class TestTrainedTopics(unittest.TestCase):
    def setUp(self):
        self.topics = trainedTopics.trainedTopics()

    def tearDown(self):
        pass

    def test_writeToJSON(self):
        self.topics.writeToJSON()
        # Assert that the JSON file has been created successfully
        # and contains the expected data
        # You can add assertions here to check the contents of the JSON file

    def test_readFromJSON(self):
        # Write some data to the JSON file first
        self.topics.writeToJSON()

        # Read the data from the JSON file
        topic_list = self.topics.readFromJSON()

        # Assert that the returned list matches the expected list
        # You can add assertions here to check the contents of the list


    def test_getListOfTopicKeywords(self):
        expected_result = {'topic1': ['keyword1', 'keyword2'], 'topic2': ['keyword3']}
        self.topics.readFromJSON = lambda: expected_result
        result = self.topics.getListOfTopicKeywords()
        self.assertEqual(result, expected_result)

    def test_classifierIfExist(self):
        self.topics.listOfTopics = {'topic1': ['keyword1', 'keyword2'], 'topic2': ['keyword3']}
        listOfWordsAndPercent = [(0.8, 'keyword1'), (0.6, 'keyword3')]
        result = self.topics.classifierIfExist(listOfWordsAndPercent)
        self.assertEqual(result, 'topic1')

    def test_getMajorityTopic(self):
        ls = [(0.8, '#topic1'), (0.6, '#topic2'), (0.7, '#topic1')]
        result = self.topics.getMajorityTopic(ls)
        self.assertEqual(result, 'topic1')

    def test_string_similarity(self):
        str1 = 'hello'
        str2 = 'hola'
        result = self.topics.string_similarity(str1, str2)
        self.assertAlmostEqual(result, 0.4444444444444444, places=1)


class TestGroupChat(unittest.TestCase):
    def setUp(self):
        self.chat = GroupChat.groupChat("Test Topic")

    @patch('builtins.open', new_callable=mock_open, read_data='{"Test Topic": {"Description":"Test","Messages": [{"Sender": "Alice", "Message": "Hello, everyone!"}]}}')
    def test_addMessage(self, mock_file):
        # Add a message to the group chat
        self.chat.addMessage("Alice", "Hello, everyone!")

        # Retrieve the details and check if the message exists
        details = self.chat.retrievedetailsAndCheckExist()
        self.assertIsNotNone(details)

        # Check if the message is added correctly
        messages = details["Messages"]
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]["Sender"], "Alice")
        self.assertEqual(messages[0]["Message"], "Hello, everyone!")

    @patch('builtins.open', new_callable=mock_open, read_data='{}')
    def test_retrievedetailsAndCheckExist(self, mock_file):
        # Create a new group chat with a different topic
        chat = GroupChat.groupChat("Different Topic")

        # Retrieve details for a non-existent topic
        details = chat.retrievedetailsAndCheckExist()

        # Check if the details are empty
        self.assertEqual(details, None)

    @patch('builtins.open', new_callable=mock_open, read_data='{"Test Topic": {"Messages": []}}')
    def test_readFromJSON(self, mock_file):
        # Read data from the JSON file
        data = self.chat.readFromJSON()

        # Check if the data is loaded correctly
        self.assertIsInstance(data, dict)

    @patch('builtins.open', new_callable=mock_open)
    def test_writeToJSON(self, mock_file):
        # Prepare data to write to the JSON file
        data = {"Test Topic": {"Messages": [{"Sender": "Bob", "Message": "Hello!"}]}}

        # Write data to the JSON file
        self.chat.writeToJSON(data)

        # Check if the data is written correctly


class TestFirstModel(unittest.TestCase):
    def test_preprocess_text(self):
        text = "This is a sample sentence."
        expected_output = ['sample', 'sentence']
        output = firstModel.preprocess_text(text)
        self.assertEqual(output, expected_output)

    def test_runProgramTest(self):
        messages = ["Hello, how are you?", "I'm doing great!", "What about you?"]
        expected_output = {0: [[1.0, 'great']],
 1: [[1.0, 'great']],
 2: [[1.0, 'great']],
 3: [[1.0, 'great']],
 4: [[1.0, 'great']],
 5: [[1.0, 'great']],
 6: [[1.0, 'great']],
 7: [[1.0, 'great']],
 8: [[1.0, 'great']],
 9: [[1.0, 'great']],
 10: [[1.0, 'great']],
 11: [[1.0, 'great']],
 12: [[1.0, 'great']],
 13: [[1.0, 'great']],
 14: [[1.0, 'great']],
 15: [[1.0, 'great']],
 16: [[1.0, 'great']],
 17: [[1.0, 'great']],
 18: [[1.0, 'great']],
 19: [[1.0, 'great']]}

        output = firstModel.runProgramTest(messages)
        self.assertEqual(output, expected_output)

    def test_preprocess_text_empty_input(self):
        text = ""
        expected_output = []
        output = firstModel.preprocess_text(text)
        self.assertEqual(output, expected_output)


class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_checkIfNeedingTranslationForFront(self):
        messages = [
            {"Message": "Hello"},
            {"Message": "你好"},
            {"Message": "Bonjour"}
        ]

        expected_output = [
            {"Message": "Hello"},
            {"Message": "你好|~|"},
            {"Message": "Bonjour"}
        ]

        output = main.checkIfNeedingTranslationForFront(messages)
        self.assertEqual(output, expected_output)

    def test_MockConversationNow(self):
        with patch("main.checkIfNeedingTranslationForFront") as mock_check_translation, \
                patch("main.messages.storeMessagesRecieved"):
            mock_person = "Alex"
            mock_data = {
                "Sender": "Alex",
                "Message": "你好",
                "Receiver": "You"
            }
            mock_check_translation.return_value = [{
                "Sender": "Alex",
                "Message": "你好",
                "Receiver": "You"}]

            output = main.MockConversationNow(mock_person)
            self.assertEqual(output, mock_data)

    def test_runAI(self):
        with patch("main.messages.readFilesAndCreateMessage") as mock_read_files:
            with patch("main.firstModel.mainFunctionTorun") as mock_main_function:
                mock_name = "John"
                mock_messages = [
                    {"Message": "Hello"},
                    {"Message": "How are you?"},
                    {"Message": "Goodbye"}
                ]
                mock_read_files.return_value = mock_messages
                mock_main_function.return_value = [["topic1"], ["topic2"], ["topic3"]]

                output = main.runAI(mock_name)
                expected_output = [["topic1"], ["topic2"], ["topic3"]]
                self.assertEqual(output, expected_output)




if __name__ == '__main__':
    unittest.main()