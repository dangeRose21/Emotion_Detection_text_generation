import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Define the function to process sentiment analysis for bigrams
def analyze_sentiment_bigrams(text):
    """
    Takes in a string of text and returns the sentiment score and classified bigrams
    """
    # Tokenize the text into individual words
    words = nltk.word_tokenize(text.lower())

    # Create bigrams from the list of words
    bigrams = list(nltk.bigrams(words))

    # Check if the text contains a negation word (e.g. not, never, no)
    negation = False
    for word in words:
        if word in ["not", "never", "no"]:
            negation = True
            break

    # If the text contains a negation word, add "not_" before the words to negate
    if negation:
        words = ["not_" + word if word not in ["not", "never", "no"] else word for word in words]
        bigrams = [("not_" + bigram[0], "not_" + bigram[1]) if bigram[0] not in ["not", "never", "no"] else bigram for bigram in bigrams]

    # Calculate the sentiment score using VADER
    sentiment_scores = sia.polarity_scores(" ".join(words))

    # Classify the bigrams as positive, negative, or neutral based on the sentiment score
    classified_bigrams = []
    for bigram in bigrams:
        bigram_score = sia.polarity_scores(" ".join(bigram))["compound"]
        if bigram_score > 0:
            classified_bigrams.append((bigram, "positive"))
        elif bigram_score < 0:
            classified_bigrams.append((bigram, "negative"))
        else:
            classified_bigrams.append((bigram, "neutral"))

    # Create a Pandas DataFrame with the sentiment score and classified bigrams
    df = pd.DataFrame(classified_bigrams, columns=["Bigram", "Sentiment"])
    df["Sentiment Score"] = sentiment_scores["compound"]
    return df

# Read the text file
with open("output.txt", "r") as f:
    text = f.read()

# Process the sentiment analysis for bigrams
result_df = analyze_sentiment_bigrams(text)

# Print the result
print(result_df.head())
