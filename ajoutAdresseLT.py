# Ce fichier ajoute l'adresse retourner par locationTagger si y en a au fichier json

import string
import json


#opening the json file
fjson = open('data.json')
data = json.load(fjson)

# Evaluation de l'heuristique adresse de locationTagger

# L'adresse retourner par LocationTagger

for text in data:
        adresse = data[text]['LocationTagger'][6]
        if len(adresse['Adresse']) != 0:
            data[text]['heuristique_adresse_LT'] = adresse['Adresse'][0]
            
with open('data.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))

fjson.close()


