import spacy
import json

#opening the json file
fjson = open('fakeJson.json')
data = json.load(fjson)


nlp = spacy.load("en_core_web_sm")

for i in data:
        text = data[i]['title']
        doc = nlp(text)
        ents = [(e.label_) for e in doc.ents]
        data[i]['Ordre'] = ents

with open('fakeJosn.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))
fjson.close()



