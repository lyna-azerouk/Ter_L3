# pip install -U spacy
# python -m spacy download en_core_web_sm
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
                                           
with open('data.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))
# Closing file

fjson.close()

# RESTE A FAIRE LE FILTRAGE DES IMAGES QUI NE CONTIENT PAS DES LOC OU GPE OU INDICATION QUI AIDE A TROUVER LA LOCALISATION
