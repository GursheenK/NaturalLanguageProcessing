#Word Tokenization and Sentence segmentation
from nltk.tokenize import sent_tokenize,word_tokenize

f=open('nlpfiles/nlp_tokenization.txt')
content=f.read()
sentences=sent_tokenize(content)
for sentence in sentences:
    print('\nSentence is : ',sentence)
    print('\nWords are : ',word_tokenize(sentence))
