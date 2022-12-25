#POS tagging
from nltk import pos_tag
from nltk.tokenize import word_tokenize,sent_tokenize

f=open('nlpfiles/nlp_postag.txt')
string=f.read()
string_tokens=word_tokenize(string)
string_tags=pos_tag(string_tokens)
print(string_tags)

