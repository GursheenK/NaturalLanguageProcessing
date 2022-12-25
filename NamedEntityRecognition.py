#NER
import spacy
import pandas as pd

NER=spacy.load('en_core_web_sm')
f=open('nlpfiles/nlp_NER.txt')
text=f.read()
doc=NER(text)

entities=[]
labels=[]
position_start=[]
position_end=[]

for ent in doc.ents:
    entities.append(ent)
    labels.append(ent.label_)
    position_start.append(ent.start_char)
    position_end.append(ent.end_char)

df=pd.DataFrame({'Entities':entities,'Labels':labels,'Start Position':position_start,'End Position':position_end})
print(df)
