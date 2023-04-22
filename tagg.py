import nltk

nltk.download('tagsets')

#tags info
nltk.help.upenn_tagset('NN')
nltk.help.upenn_tagset('IN')
nltk.help.upenn_tagset('DT')
nltk.help.upenn_tagset('JJ')
nltk.help.upenn_tagset('NNP')
nltk.help.upenn_tagset('POS')
nltk.help.upenn_tagset('CD')

""" ## Tags words from a corpus
from nltk.tokenize import sent_tokenize
from nltk.corpus import gutenberg
sample = gutenberg.raw("blake-poems.txt")
tokenized = sent_tokenize(sample)
for i in tokenized[:2]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
 """

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Open input file and read its contents
with open('text_sentiment_content_tokens.txt', 'r') as f:
    text = f.read()

# Tokenize the text
tokenized = sent_tokenize(text)

# Process the sentences
tagged_sentences = []
for i in tokenized[:2]:
    words = word_tokenize(i)
    tagged = nltk.pos_tag(words)
    tagged_sentences.append(tagged)

# Write the results to the output file
with open('text_emotion_tags.txt', 'w') as f:
    for tagged_sentence in tagged_sentences:
        for word, tag in tagged_sentence:
            f.write(f'{word}({tag}) ')
        f.write('\n')
