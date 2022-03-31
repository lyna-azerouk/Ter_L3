# Spacy

import spacy
import geocoder
import locationtagger
from geoname import geo_loc
# Golden hour on the plains of Colorado! Taken next to the airport
# View over the fjord right after taking off from Tromsø airport, northern Norway
# Long Lake - Alpine lake at 2,720 m, 75 km northeast of Fresno, CA airport. Mount Ritter, the Minarets and Mammoth ski mountain visible in background.
# View of Lake Erie -> Geoname retourne le resultat dans differentes country
# View of Lake Erie US -> 
# View of Lake Erie Ohio -> donne directe le bon resultats
# It's beautiful -> location tagger spacy c'est nulle
# Nice view of Lake Tiriara -> Geoname retourne un seul resultat et c'est l'heuristoque 5
# Nice view of Lake Tiriara Cook Islands -> Pareil
# Larslan -> renvoyer le premier resultat de geoname


text  = "Lake Erie US"

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
for entity in doc.ents:
    if(entity.label_ == 'GPE' or entity.label_ == 'LOC'):
        print(entity.text,entity.label_)
       
        # Resultat de l'heuristique 05 
p=""
for token in doc:
    if token.pos_ == "PROPN":
        g = geocoder.geonames(token.text,maxRows =5, key='Lydia_Ouam')
        L=[]
        for r in g:
            l = geocoder.geonames(r.geonames_id, method='details', key='Lydia_Ouam')
            L.append(l.country)
            if len(L)!=0:
                p+=token.text+" "
print("Heuristique 05 :"+p)

print("--------------------------Location Tagger -------------------------")
# Location Tagger 
# text = "Golden hour on the plains of Colorado! Taken next to the airport"

entities = locationtagger.find_locations(text = text)
print(entities.cities)
print(entities.countries)
print(entities.regions)
print(entities.country_regions)
print(entities.country_cities)
print(entities.country_mentions)
print(entities.region_cities)
print(entities.other)
print(entities.address_strings)


print("---------------------------------------------------------------------")

a = geocoder.geonames("Montpellier France",key='Lydia_Ouam', maxRows = 5,  isNameRequired = True)
# print(a.geojson)
for i in a:
    g = geocoder.geonames(i.geonames_id, method = 'details', key='Lydia_Ouam')
    print([(r.address, r.country, r.description, r.feature_class, r.country_code, r.class_description, r.admin2, r.admin3, r.admin4, r.lat, r.lng) for r in g])

print(geo_loc("Oregon"))
print(geo_loc("Montpellier France"))


