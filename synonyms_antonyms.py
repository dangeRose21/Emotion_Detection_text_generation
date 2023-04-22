import nltk

from nltk.corpus import wordnet


""" synonyms = []

#find the synonyms for a word using wordnet
for syn in wordnet.synsets("good"):
    for lm in syn.lemmas():
             synonyms.append(lm.name())
print ("synonyms: ", set(synonyms))



antonyms = []

#find the synonims for a word using wordnet
for syn in wordnet.synsets("good"):
    for lm in syn.lemmas():
        if lm.antonyms():
            antonyms.append(lm.antonyms()[0].name())

print("antonyms: ",set(antonyms)) """

# read input from tokenized file
with open("output.txt", "r") as file:
    words = [word.strip() for word in file.readlines()]

# initialize synonyms and antonyms list
synonyms = {}
antonyms = {}

# find the synonyms and antonyms for each word using wordnet
for word in words:
    synonyms[word] = set()
    antonyms[word] = set()
    for syn in wordnet.synsets(word):
        for lm in syn.lemmas():
            if lm.name() != word:
                synonyms[word].add(lm.name())
            if lm.antonyms():
                antonyms[word].add(lm.antonyms()[0].name())

# write output to file
with open("synonyms_antonyms.txt", "w") as file:
    for word in words:
        file.write(f"Word: {word}\n")
        file.write(f"Synonyms: {', '.join(synonyms[word])}\n")
        file.write(f"Antonyms: {', '.join(antonyms[word])}\n\n")
