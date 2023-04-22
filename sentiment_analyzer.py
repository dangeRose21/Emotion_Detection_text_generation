import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Define the function to process sentiment analysis
def analyze_sentiment(text):
    """
    Takes in a single word, a pair of words, or a negated pair of words and returns the sentiment score
    """
    # Tokenize the text into individual words
    words = nltk.word_tokenize(text.lower())

    # Check if the text contains a negation word (e.g. not, never, no)
    negation = False
    for word in words:
        if word in ["not", "never", "no"]:
            negation = True
            break

    # If the text contains a negation word, add "not_" before the words to negate
    if negation:
        words = ["not_" + word if word not in ["not", "never", "no"] else word for word in words]

    # Check if the text contains a pair of words separated by an underscore
    if "_" in text:
        # Join the pair of words with a space
        words = [text.replace("_", " ")]

    # Calculate the sentiment score using VADER
    sentiment_scores = sia.polarity_scores(" ".join(words))

    # Classify the words as positive, negative, or neutral based on the sentiment score
    classified_words = []
    for word in words:
        word_score = sia.polarity_scores(word)["compound"]
        if word_score > 0:
            classified_words.append((word, "positive"))
        elif word_score < 0:
            classified_words.append((word, "negative"))
        else:
            classified_words.append((word, "neutral"))

    # Create a Pandas DataFrame with the sentiment score and classified words
    df = pd.DataFrame(classified_words, columns=["Word", "Sentiment"])
    df["Sentiment Score"] = sentiment_scores["compound"]
    return df

# Test the function with some examples
print(analyze_sentiment("happy"))
print(analyze_sentiment("good bad"))
print(analyze_sentiment("not good"))
print(analyze_sentiment("not_bad"))
