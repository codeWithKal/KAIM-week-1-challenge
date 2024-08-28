import pandas as pd
from textblob import TextBlob

"""
Function- catagorize sentiment
"""
def catagorize_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity < 0:
        return "negative"
    elif polarity > 0:
        return "positive"
    else:
        return "neutral"