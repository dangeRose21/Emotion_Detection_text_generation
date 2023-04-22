#lemmas
from nltk.corpus import wordnet as wn
res=wn.synset('edge.n.01').lemma_names()
print(res)

#definition
from nltk.corpus import wordnet as wn
resdef = wn.synset('word.n.01').definition()
print(resdef)

#examples
from nltk.corpus import wordnet as wn
res_exm = wn.synset('word.n.01').examples()
print(res_exm)


