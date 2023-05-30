# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer
# from gensim import corpora, models
# from nltk.stem import PorterStemmer
# from nltk.tokenize import word_tokenize
# import re
# import spacy
# from spacy import displacy
# from spacy import tokenizer
#
#
# # Download required NLTK resources
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('punkt')
# nlp = spacy.load('en_core_web_sm')
#
# # Preprocessing steps
# def preprocess_text(text):
#
#     # Tokenize text into individual words
#     noRegex = re.sub(r'[^\w\s]', '', text)
#     tokens = word_tokenize(noRegex.lower())
#
#     # Remove stopwords
#     stop_words = set(stopwords.words('english'))
#     tokens = [token for token in tokens if token not in stop_words]
#
#     # Lemmatization
#     lemmatizer = WordNetLemmatizer()
#     tokens = [lemmatizer.lemmatize(token) for token in tokens]
#
#     # ps = PorterStemmer()
#     # tokens = [ps.stem(token) for token in tokens]
#
#     return tokens
# def NER(messages):
#     doc = nlp(messages)
#     # print entities
#     entities = [ent.text.lower() for ent in doc.ents]
#     print(entities)
#     ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
#     print(ents)
#     # now we use displaycy function on doc2
#     # displacy.render(doc, style='ent', jupyter=True)
#
# def runProgramTest(messages):
#     strin = ""
#    #Let us convert messages into one large string
#     for m in messages:
#         strin = strin + " " + m
#     NER(strin)
#     # Preprocess messages
#     preprocessed_messages = [preprocess_text(message) for message in messages]
#     print(preprocessed_messages)
#     # Create dictionary representation of preprocessed messages
#     dictionary = corpora.Dictionary(preprocessed_messages)
#
#     # Create document-term matrix
#     # doc_term_matrix = [dictionary.doc2bow(tokens) for tokens in preprocessed_messages]
#     # num_topics = 3
#     # # Create LDA model
#     # lda_model = models.LdaModel(doc_term_matrix, num_topics=num_topics, id2word=dictionary, passes=10)
#     #
#     # # Print topics and associated words
#     # for topic_id, topic_words in lda_model.print_topics():
#     #     print(f"Topic #{topic_id + 1}: {topic_words}")
#     #
#     # # Assign labels based on dominant topic
#     # for i in range(len(messages)):
#     #     bow = dictionary.doc2bow(preprocessed_messages[i])
#     #     dominant_topic = max(lda_model.get_document_topics(bow), key=lambda x: x[1])[0]
#     #     print(f"Message: {messages[i]}\nTopic: {dominant_topic + 1}\n")
#
#     #So if I apply first Model into a chat and then ask for topics reading all of the messages

