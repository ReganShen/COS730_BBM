
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim import corpora, models
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re

# Download required NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

# Preprocessing steps
def preprocess_text(text):

    # Tokenize text into individual words
    noRegex = re.sub(r'[^\w\s]', '', text)
    tokens = word_tokenize(noRegex.lower())

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # ps = PorterStemmer()
    # tokens = [ps.stem(token) for token in tokens]

    return tokens

def runProgramTest():
    # Example messages
    messages = [
        "I love playing football with my friend. Watch the soccer game",
        "I will be going to the gym because I love all gyms",
        "Gardening is my favorite hobby. I enjoy growing flowers.",
        "I'm really into photography and capturing beautiful landscapes.",
        "Reading books and writing stories are my passions.",
        "I enjoy cooking and experimenting with new recipes in the kitchen."
    ]

    # Preprocess messages
    preprocessed_messages = [preprocess_text(message) for message in messages]
    print(preprocessed_messages)
    


