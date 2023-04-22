

""" ##prints memory locations of characters in the file
with open('text_emotion_tokens.txt', 'r') as file:
    string = file.read()
    for i, char in enumerate(string):
        print(f"Character '{char}' at position {i} has memory location: {hex(id(char))}")
 """

##Sorts the lines of a file in alphabetical order
with open('text_sentiment_content_tokens.txt', 'r') as file:
    lines = file.readlines()
    sorted_lines = sorted(lines)
    for line in sorted_lines:
        print(line.strip()) 

""" ##Sorts lines in reverse alphabetical order
with open('text_sentiment_content_tokens.txt', 'r') as file:
    lines = file.readlines()
    sorted_lines = sorted(lines, reverse=True)
    for line in sorted_lines:
        print(line.strip()) """

