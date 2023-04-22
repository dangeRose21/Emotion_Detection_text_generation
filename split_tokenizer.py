import csv

from translate import Translator

""" #Uses the split method to tokenize the data for certain rows
with open('text_emotion.csv', 'r') as file, open('split_tokens.txt', 'w') as outfile:
    reader = csv.reader(file)
    writer = outfile.write
    
    for row in reader:
        tokens_2 = row[1].split()
        tokens_3 = row[3].split()
        
        writer(str(tokens_2) + '\n')
        writer(str(tokens_3) + '\n') """

##processess all data in the file
with open('text_emotion.csv', 'r') as file, open('output.txt', 'w') as outfile:
    reader = csv.reader(file)
    writer = outfile.write
    
    for row in reader:
        tokens = []
        
        # Iterate over all columns in the row
        for col in row:
            # Split the column into individual words based on whitespace
            col_tokens = col.split()
            # Add the individual words to the tokens list
            tokens.extend(col_tokens)
            
        # Write the tokens list to the output file
        writer(str(tokens) + '\n')
