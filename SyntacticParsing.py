#Syntactic Parsing

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk import RegexpParser

f=open('nlpfiles/nlp_chunker_syntacticparsing.txt')
text=f.read()
sentences=sent_tokenize(text)
for sentence in sentences:
    tokens=word_tokenize(sentence)
    token_tags=nltk.pos_tag(tokens)
    grammar='NP:{<DT>?<JJ.*>*<NN.*>+}'
    chunker=RegexpParser(grammar)
    result=chunker.parse(token_tags)
    print(result)
    result.draw()
