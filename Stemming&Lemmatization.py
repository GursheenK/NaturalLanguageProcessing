#Stemming & Lemmatization

from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import LancasterStemmer

def porterstemming(words):
    ps=PorterStemmer()
    for word in words:
        print(word,'--->',ps.stem(word))

def snowballstemming(words):
    ss=SnowballStemmer(language='english')
    for word in words:
        print(word,'--->',ss.stem(word))

def lancasterstemming(words):
    ls=LancasterStemmer()
    for word in words:
        print(word,'--->',ls.stem(word))

words=input('Enter the words for stemming separated by commas:').split(',')
print('Select Operation:')
print('1. Porter Stemmer')
print('2. Snowball Stemmer')
print('3. Lancaster Stemmer')
while True:
    choice=input('\nEnter choice (1/2/3) :')
    if choice in ('1','2','3'):
        if choice == '1':
            porterstemming(words)
        elif choice == '2':
            snowballstemming(words)
        elif choice == '3':
            lancasterstemming(words)
        cont=input('\nDo you want to continue?:(yes/no)')
        if cont=='no':
            break
    else:
        print('Invalid Input')

#Lemmatization
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize,sent_tokenize

words=input('Enter the words to lemmatize : ').split(',')
word_lemmatizer=WordNetLemmatizer()
for word in words:
    print('Lemma for {} is {}.'.format(word,word_lemmatizer.lemmatize(word)))
