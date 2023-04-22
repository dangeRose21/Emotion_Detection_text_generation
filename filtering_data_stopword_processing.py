import nltk

# Download the stopwords from NLTK
nltk.download('stopwords')

from nltk.corpus import stopwords

# Define the path to your tokenized text file
text_file_path = 'text_emotion_tokens.txt'

# Define a list of stopwords
stop_words = set(stopwords.words('english'))

# Open the text file for reading
with open(text_file_path, 'r') as file:
    # Read the contents of the file
    contents = file.read()
    
    # Tokenize the contents of the file
    tokens = nltk.word_tokenize(contents)
    
    # Separate the stopwords from the list of tokens
    filtered_tokens = []
    unused_words = []
    for token in tokens:
        if token.lower() not in stop_words:
            filtered_tokens.append(token)
        else:
            unused_words.append(token)
    
    # Convert the filtered tokens back into a string
    filtered_text = ' '.join(filtered_tokens)
    
    # Write the filtered text to a new file
    with open('filtered_data.txt', 'w') as filtered_file:
        filtered_file.write(filtered_text)
    
    # Write the unused stopwords to a new file
    with open('unused_words.txt', 'w') as unused_file:
        unused_file.write(' '.join(unused_words))


    
    # Print the filtered text to the console
    #print(filtered_text)


