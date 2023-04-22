import nltk

# define the grammar rule
grammar = r"""
  NP: {<DT|PRP\$>?<JJ>*<NN.*>+}
  PP: {<IN><DT|PRP\$>?<JJ>*<NN.*>+}
  VP: {<VB.*><NP|PP|CLAUSE>+$}
  CLAUSE: {<WDT|WP|WRB><VP>}
""" 

## grammar using chinking
grammar = r"""
  NP: {<DT|PRP\$>?<JJ>*<NN.*>+}
  PP: {<IN><DT|PRP\$>?<JJ>*<NN.*>+}
  VP: {<VB.*><NP|PP|CLAUSE>+$}
  CLAUSE: {<WDT|WP|WRB><VP>}
  # Chinking
  NP: {<.*>+} # Chunk everything
        }<VB.*>+{ # Chink sequences of verbs
"""

# define the input and output file paths
input_file = "poem.txt"
output_file = "chunk_chink_file_graphs.txt"

# read input sentences from file
with open(input_file, "r") as f:
    sentences = [nltk.pos_tag(nltk.word_tokenize(line.strip())) for line in f]

# apply the grammar rule to each sentence and write results to output file
with open(output_file, "w") as f:
    for sentence in sentences:
        cp = nltk.RegexpParser(grammar)
        result = cp.parse(sentence)
        f.write(str(result) + "\n")

    result.draw()