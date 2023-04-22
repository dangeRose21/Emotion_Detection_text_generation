from nltk.corpus import gutenberg

from nltk.tokenize import sent_tokenize


fields = gutenberg.fileids()

print(fields)

sample = gutenberg.raw("austen-emma.txt")

token = sent_tokenize(sample)

""" for para in range(2):
    print(token[para]) """


with open("poem.txt", "w") as f:
    for para in range(2):
        f.write(token[para] + "\n")