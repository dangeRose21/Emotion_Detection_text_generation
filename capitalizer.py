import nltk

nltk.download('punkt')  # download punkt tokenizer if not already downloaded

filename = "text_emotion_tokens.txt"

## This method capitalizes each word in a file
with open(filename, "r") as file:
    text = file.read()

tokens = nltk.word_tokenize(text)

capitalized_tokens = [word.capitalize() for word in tokens]

capitalized_text = " ".join(capitalized_tokens)

#print(capitalized_text)

with open("capitalized_words.txt", "w") as file:
    file.write(capitalized_text)


with open(filename, "r") as file:
    text = file.read()

capitalized_text = text.upper()

with open("capitalized_text.txt", "w") as file:
    file.write(capitalized_text)