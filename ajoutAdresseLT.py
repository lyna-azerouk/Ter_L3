# Ce fichier ajoute l'adresse retourner par locationTagger si y en a au fichier json

import string
import json
from   geopy.geocoders import Nominatim
from     geopy.geocoders import Nominatim
import folium 
import spacy 
from geoname import geo_loc 



#opening the json file
fjson = open('data.json')
data = json.load(fjson)

# Evaluation de l'heuristique adresse de locationTagger

# L'adresse retourner par LocationTagger

for text in data:
	
	adresse = data[text]['LocationTagger'][6]
	adresse_string=""
	if len(adresse['Adresse']) != 0:
		liste=geo_loc(str(adresse['Adresse'][0]))
		data[text]['heuristique_adresse_LT']=[str(adresse['Adresse'][0])]+liste
        
with open('data.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))

fjson.close()


