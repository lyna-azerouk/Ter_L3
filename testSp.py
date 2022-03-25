# pip install -U spacy
# python -m spacy download en_core_web_sm
from asyncio.windows_events import NULL
import spacy
import json

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")


#opening the json file

fjson = open('data.json')

#load the json file into a dict
data = json.load(fjson)

# Iterating through the json
# list and extract the title

for i in data:
        text = data[i]['title']
        doc = nlp(text)
        # Find named entities, phrases and concepts
        l=[]
        for entity in doc.ents:
                if(entity.label_ == 'GPE' or entity.label_ == 'LOC'):
                        l.append((entity.text,entity.label_))
                        data[i]['SpacyLoc']=l    

for i in data.copy():
        if('SpacyLoc' not in data[i].keys()):
                del(data[i])



""" for image in data:
        for i in data[image]['SpacyLoc']:
                print(i)        
                g=geocoder.geonames(i[0],key='Lydia_Ouam')
                for r in g:
                        li = geocoder.geonames(r.geonames_id, method='details', key='Lydia_Ouam') """


with open('data.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))
# Closing file     

                                        
# Closing file


# Delete Images without Location

for i in data.copy():
        if('SpacyLoc' not in data[i].keys()):
                del(data[i])

with open('data.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))
fjson.close()

