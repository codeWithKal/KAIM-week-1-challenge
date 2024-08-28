import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


nltk.download('punkt')
nltk.download('stopwords')

def text_processor(text):
    tokens = word_tokenize(text.lower())

    #Removing punctuations and stop words
    stop_words = set(stopwords.words('english'))

    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

    #setting stemmer
    stemmer = PorterStemmer()

    tokens = [stemmer.stem(word) for word in tokens]

    return tokens