import nltk
from nltk.corpus import stopwords
from NLP_Model import trainedTopics
from nltk.stem import WordNetLemmatizer
from gensim import corpora, models
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re
import spacy
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
from rake_nltk import Rake

import yake
import pandas as pd
# Download required NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nlp = spacy.load('en_core_web_sm')
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS

stemmer = SnowballStemmer("english")
rake_nltk_var = Rake()

# Preprocessing steps
def preprocess_text(text):
    sen = nlp(text)
    strList = ""
    for word in sen:
        if word.pos_ == "PRON" or word.pos_ == "CCONJ" or word.pos_ == "INTJ" or word.tag_ == "IN" or word.tag_ == "PRP" or "\'" in word.text or len(word.text) == 1:
            #print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')
            five = 4
        else:
            strList = strList + " " + word.text
        #Remove pronouns, preposition, conjnuction, interjection

    text = strList

    # Tokenize text into individual words
    noRegex = re.sub(r'[^\w\s]', '', text)
    tokens = word_tokenize(noRegex.lower())

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words or token not in spacy_stopwords]

    # Lemmatization
    # lemmatizer = WordNetLemmatizer()
    # tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # ps = PorterStemmer()
    # tokens = [ps.stem(token) for token in tokens]

    return tokens


def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))

    return result

def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

def formsOfEnlish(text):
    sen = nlp(text)
    for word in sen:
        print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')
def keywordExtraction(text):
    # LargeString = ""
    # for m in text:
    #     LargeString = LargeString + " " + m
    # rake_nltk_var.extract_keywords_from_sentences(text)
    # keyword_extracted = rake_nltk_var.get_ranked_phrases()
    # print(keyword_extracted)
    sen = nlp(text)
    print(sen.ents)

def mainFunctionTorun(messages):
    topics = runProgramTest(messages)
    trainedopics = trainedTopics.trainedTopics()
    finalTopics = {}
    for topic in topics:
        print("New Topic Bitchj")
        # ls = []
        # for wo in topics[topic]:
        #     #The string is wo[1]
        #     ls.append(wo[1])
        t = topics[topic]
        deepCopy = t.copy()
        finalllle = trainedopics.classifierIfExist(deepCopy)
        if finalllle == "":
            finalTopics[topic] = topics[topic]
        else:
            strsadssd = finalllle + str(topic)
            finalTopics[strsadssd] = topics[topic]
    for s in finalTopics:
        st = finalTopics[s]
        print(s)
        print("====================")
        print(st)


def runProgramTest(messages):

    preprocessed_messages = [preprocess_text(message) for message in messages]
    # print(preprocessed_messages)

    # preprocessed_messages = []
    # for message in messages:
    #     preprocessed_messages.append(preprocess(message))

    # Create dictionary representation of preprocessed messages
    dictionary = gensim.corpora.Dictionary(preprocessed_messages)

    # Create document-term matrix
    doc_term_matrix = [dictionary.doc2bow(tokens) for tokens in preprocessed_messages]
    num_topics = 20
    # Create LDA model
    lda_model = models.LdaModel(doc_term_matrix, num_topics=num_topics, id2word=dictionary, passes=200)

    # Print topics and associated words
    DictOfTopic = {}
    # lda_model.show_topics()
    for topic_id, topic_words in lda_model.print_topics(-1,10):
        print(f"Topic #{topic_id + 1}: {topic_words}")
        splitByplus = topic_words.split(" + ")
        listOfShit = []
        for asddas in splitByplus:
            temp = []
            splitByStar = asddas.split("*")
            temp.append(float(splitByStar[0]))
            newStr = splitByStar[1].replace("\"","")
            temp.append(newStr)
            listOfShit.append(temp)
        DictOfTopic[topic_id] = listOfShit
    print(DictOfTopic)
    #Now go through each topic and take out all the key words
    return DictOfTopic

    #So if I apply first Model into a chat and then ask for topics reading all of the messages


