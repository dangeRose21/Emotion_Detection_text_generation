import csv
import nltk

""" with open('text_emotion.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        emotions = nltk.word_tokenize(row[2])
        emotions = nltk.word_tokenize(row[2])
        print(emotions) """

## This code applies the nltk.word_tokenize() function to tokenize the 2nd and 3rd columns of data in each row
with open('filtered_data.txt', 'r') as file, open('output.txt', 'w') as outfile:
    reader = csv.reader(file)
    writer = outfile.write

    # Initialize a set to store unique words
    unique_words = set()

    for row in reader:
        tokens_2 = nltk.word_tokenize(row[1])
        tokens_3 = nltk.word_tokenize(row[3])
        writer(str(tokens_2) + '\n')
        writer(str(tokens_3) + '\n')

        # Add the tokens to the unique words set
        unique_words.update(tokens_2)
        unique_words.update(tokens_3)

    # Write the unique words to the output file
    writer('\n'.join(unique_words))
        

""" ##tokenizes the entire data file using a for loop to iterate over each column in the rown and using the extend() method to add the results
##the list of tokens
with open('text_emotion.csv', 'r') as file:
    reader = csv.reader(file)
    with open('text_emotion_tokens.txt', 'w') as outfile:
        for row in reader:
            tokens = []
            for col in row:
                tokens.extend(nltk.word_tokenize(col))
            outfile.write(' '.join(tokens) + '\n') """