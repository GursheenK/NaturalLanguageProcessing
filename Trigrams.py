#Trigram model

import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk import FreqDist
import pandas as pd

f=open('nlpfiles/nlp_ngrams.txt')
sample=f.read()
sample_tokens=word_tokenize(sample)

print('Sample tokens : ',sample_tokens)
print('Length of Sample tokens : ',len(sample_tokens))
print('Type of Sample tokens : ',len(sample_tokens))

sample_freq=FreqDist(sample_tokens)
tokens=[]
sf=[]
for i in sample_freq:
    tokens.append(i)
    sf.append(sample_freq[i])

df=pd.DataFrame({'Tokens':tokens,'Frequency':sf})
print('\n',df)

print('\nBigrams : ',list(nltk.bigrams(sample_tokens)))
print('\nTriigrams : ',list(nltk.trigrams(sample_tokens)))
print('\nN-grams(4) : ',list(nltk.ngrams(sample_tokens,4)))
