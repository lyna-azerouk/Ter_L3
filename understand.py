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
# Location Tagger 
# text = "Golden hour on the plains of Colorado! Taken next to the airport"


# Une fonction:
def heuristique(text):
    # heuristique adresse LT:
    
    print("--------------------------Location Tagger Adresse -------------------------")
    entities = locationtagger.find_locations(text = text)
    print("Adresse : ",entities.address_strings)
    if(len(entities.address_strings) != 0):
        for h in entities.address_strings:
            heuristique_adresse_LT = h
        # appliquer la fonction geo_loc
        print("Heuristique Adresse LT : ",heuristique_adresse_LT)
        print("Les cordonnees Latitude et Longitude",geo_loc(heuristique_adresse_LT))
    # heuristique country cities
    print("------------------- Location Tagger Country Cities --------------------")
    if(len(entities.country_cities) > 0):
        l = []
        for key in entities.country_cities:
            l.append(key)
            for element in entities.country_cities[key]:
                l.append(element)
        l.reverse()
        ch_ = ' '
        for chaine in l:
            ch_ = ch_ + chaine + ' '
        print("Heuristique Country Cities : ",ch_)
        print("Les cordonnees Latitude et Longitude",geo_loc(ch_))

        # Heuristique Spacy loc
    print("--------------- Heuristique Spacy Loc -------------")
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    ma_cha = ''
    for entity in doc.ents:
        if(entity.label_ == 'GPE' or entity.label_ == 'LOC'):
            ma_cha = ma_cha + entity.text + ' '
    print("Resultat Spacy loc : ",ma_cha)
    print("Les cordonnees Latitude et Longitude",geo_loc(ma_cha))

        # Heuristique 
    print("------------------ Heuristique 05 -------------------------")
    p = ""
    for token in doc:
        if (token.pos_ == "PROPN" and token.text != "OC" and  token.text != "["):
            g = geocoder.geonames(token.text,maxrows =5, key='Lydia_Ouam')
            L=[]
            for r in g:
                l = geocoder.geonames(r.geonames_id, method='details', key='Lydia_Ouam')
                L.append(l.country)
            if len(L)!=0:
                p+=token.text+" "
    print("Resultat heuristque 05 (Nom Compose) : ",p)
    print("Les cordonnees Latitude et Longitude",geo_loc(p))

        # Heuristiuqe 03 
    print("---------------------- Heuristique 03 ---------------------------")
    ents = [(e.label_) for e in doc.ents]
    name = [(e.text) for e in doc.ents]
    print(ents)
    print(name)
    heur3 = []
    for i in range(len(ents)): 
        if(ents[i] == 'LOC' and ents[i+1] == 'GPE'):
            heur3.append((name[i],name[i+1]))
    une_Ch = ''
    for element in heur3:
        for ele in element:
            une_Ch = une_Ch + ele + ' '
    print("Resultat heuristque 03 (Ordre) : ",une_Ch)
    print("Les cordonnees Latitude et Longitude",geo_loc(une_Ch))


