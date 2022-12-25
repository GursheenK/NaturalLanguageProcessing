#Dependency Parsing

import spacy
from spacy import displacy
from nltk.tokenize import sent_tokenize

nlp=spacy.load('en_core_web_sm')
f=open('nlpfiles/nlp_depparsing.txt')
text=f.read()
sentences=sent_tokenize(text)
for sentence in sentences:
    doc=nlp(sentence)

    print('{:<15}|{:<8}|{:<15}|{:<20}'.format('Token','Relation','Head','Children'))
    print('-'*70)

    for token in doc:
        print('{:<15}|{:<8}|{:<15}|{:<20}'.format(str(token.text),str(token.dep_),str(token.head.text),str([child for child in token.children])))

    displacy.serve(doc,style='dep',options={'distance':120})







    
