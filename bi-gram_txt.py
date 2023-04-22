import nltk

with open('poem.txt', 'r') as f:
    word_data = f.read()

nltk_tokens = nltk.word_tokenize(word_data)
bigrams = list(nltk.bigrams(nltk_tokens))

with open('output_txt_bigram.txt', 'w') as f:
    f.write(str(bigrams))

