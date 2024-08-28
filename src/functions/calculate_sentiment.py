import pandas as pd
from textblob import TextBlob

def calculate_setiment(text):
    blob = TextBlob(text)
    plarity = blob.sentiment.polarity
    return plarity