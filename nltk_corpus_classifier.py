import nltk
from nltk.corpus import movie_reviews
from nltk.tokenize import sent_tokenize

# Lets See how the movies are classified
all_cats = []
for w in movie_reviews.categories():
    all_cats.append(w.lower())
print(all_cats)

fields = movie_reviews.fileids()

sample = movie_reviews.raw("pos/cv944_13521.txt")

token = sent_tokenize(sample)
for lines in range(4):
    print(token[lines])


all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(10))