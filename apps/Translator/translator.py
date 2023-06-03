from translate import Translator
from googletrans import Translator, constants
from pprint import pprint

def indentifyLanguage(message):
    #Returns true if the message needs to be translated,
    onlyOneWord = message.split(" ")
    translator = Translator()
    tr = translator.translate(onlyOneWord[0])
    source = tr.src
    if source == "en":
        return False
    else:
        return True


def translateMessage(message):
    translator = Translator()
    tr = translator.translate(message)
    stringOftranslation = tr.text
    return stringOftranslation
