input_file = 'text_sentiment_content_tokens.txt'
output_file = "output.txt"

 # Open the input file and read the paragraphs
with open(input_file, "r") as f:
    paragraphs = f.readlines()

# Count the words in each paragraph and write the results to the output file
with open(output_file, "w") as f:
    for i, paragraph in enumerate(paragraphs):
        # Convert paragraph to lowercase and split into words
        words = paragraph.lower().split()
        
        # Count the number of words
        word_count = len(words)
        
        # Write the result to the output file
        f.write(f"Row {i+1} contains {word_count} words.\n")


# Open the input file and read the text
with open(input_file, "r") as f:
    text = f.read()

# Convert the text to lowercase and split into words
words = text.lower().split()

# Count the number of words
word_count = len(words)

# print the result 
print(f"The file contains {word_count} words.")