import re

# Open the text file
with open('poem.txt', 'r') as file:
    # Read the file and extract all words using regex
    text = file.read()
    words = re.findall(r'\w+', text)

# Ask the user for a word to search for
search_word = input("Enter a word to search for: ")

# Use re.match to find the first word that matches the search word
match = re.match(search_word, text, re.IGNORECASE)
if match:
    print(f"Match found: {match.group()}")

# Use re.search to find all words that contain the search word
matches = re.findall(search_word, text, re.IGNORECASE)
if matches:
    print("Matches found:")
    for match in matches:
        print(match)
