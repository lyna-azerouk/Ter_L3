import spacy
import json
from spacy import displacy
import geocoder
from geoname import geo_loc

with open( 'data.json') as mon_fichier : 
    data=json.load(mon_fichier)

nlp = spacy.load("en_core_web_sm")
for image in data :
    text = data[image]['title']
    doc = nlp(text)
    p=""
    for token in doc:
        if token.pos_ == "PROPN" and token.text != "OC" and token.text != "[":
            g = geocoder.geonames(token.text,maxrows =5, key='Lydia_Ouam')
            L=[]
            for r in g:
                l = geocoder.geonames(r.geonames_id, method='details', key='Lydia_Ouam')
                L.append(l.country)
            if len(L)!=0:
                p+=token.text+" "
            liste=geo_loc(p)
            if (liste!=None):
                data[image]['heuristique 5']=[p]+ liste
            else :
                data[image]['heuristique 5']=[p]


with open('data.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))


mon_fichier.close()

    
