import string
import json
import re
from math import floor

# Ce fichier evalue les heuritiques adresse de locationTagger et SpacyLoc

#opening the json file
fjson = open('data.json')
data = json.load(fjson)

for image in data:
    mots= re.split ( ',| ' ,data[image]['realLoc']['Nomreal'])
    chaine1 = ""
    liste_real_loc=[]
    for i in mots : 
        if (len(i)!=0 and i!='-' and i!='.'):
            chaine1=chaine1+(i.lower())+" "
            liste_real_loc.append (i.lower())
    print(chaine1)