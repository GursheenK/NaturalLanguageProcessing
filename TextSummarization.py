#Text summarization
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords

f=open('nlpfiles/nlp_summarization.txt')
text=f.read()

words=word_tokenize(text)
sentences=sent_tokenize(text)
stopwords=set(stopwords.words('english'))

freqTable=dict()
for word in words:
    word=word.lower()
    if word in stopwords:
        continue
    else:
        if word in freqTable:
            freqTable[word]+=1
        else:
            freqTable[word]=1

sentenceValue=dict()
for sentence in sentences:
    for word,freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence]+=freq
            else:
                sentenceValue[sentence]=freq

sumValues=0
for sentence in sentenceValue:
    sumValues+=sentenceValue[sentence]

average=int(sumValues/len(sentences))

summary=''
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence]>1.2*average):
        summary+=''+sentence

print(summary)
