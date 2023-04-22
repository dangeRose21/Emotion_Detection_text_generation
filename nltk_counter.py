import nltk
from nltk.corpus import stopwords

input_file = "text_sentiment_content_tokens.txt"

# Open the input file and read the text
with open(input_file, "r") as f:
    text = f.read()

# Tokenize the text into words
words = nltk.word_tokenize(text)

# Count the number of words
word_count = len(words)

# Print the result
print(f"The file contains {word_count} words.")


output_file = "output.txt"

# Open the input file and read the paragraphs
with open(input_file, "r") as f:
    paragraphs = f.readlines()

# Initialize the stopword list
stopwords_list = stopwords.words('english')

# Open the output file and count the words in each paragraph
with open(output_file, "w") as f:
    for i, paragraph in enumerate(paragraphs):
        # Tokenize paragraph into words and remove stopwords
        words = [word.lower() for word in nltk.word_tokenize(paragraph) if word.lower() not in stopwords_list]
        
        # Count the number of words
        word_count = len(words)
        
        # Write the result to the output file
        f.write(f"Paragraph {i+1} contains {word_count} words.\n")