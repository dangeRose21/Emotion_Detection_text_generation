import nltk
from nltk.corpus import conll2000

# Load the CoNLL-2000 corpus
sentences = conll2000.tagged_sents()

# Process each sentence and print the result
results = []
for i in range(5):
    cp = nltk.RegexpParser('''
            NP: {<DT|PP\$>?<JJ>*<NN>} # chunk determiner/possessive, adjectives and noun
            P: {<IN>}           # chunk prepositions
            V: {<V.*>}          # chunk verbs
            PP: {<P> <NP>}      # chunk preposition with noun phrase
            VP: {<V> <NP|PP>*}  # chunk verb and noun phrase, prepositional phrase
            ''')
    result = cp.parse(sentences[i])
    print(result)
    results.append(result)

# Write the results to a file
with open('results.txt', 'w') as f:
    for result in results:
        f.write(str(results) + '\n')


        result.draw()