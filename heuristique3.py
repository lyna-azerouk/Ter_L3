import json
from geoname import geo_loc 
# Heuristique 3 LOC,GPE alors Loc appartient a GPE

#opening the json file
fjson = open('fakeJson.json')
data = json.load(fjson)


for image in data:
    ordre = data[image]["Ordre"]
    taille_ordre = len(ordre)
    for i in range(taille_ordre-1):
        l_adresse = []
        if (len(data[image]['SpacyLoc'])>=2):
            if(ordre[i] == 'LOC' and ordre[i+1] == 'GPE'):
                l_adresse.append((data[image]['SpacyLoc'][0][0],data[image]['SpacyLoc'][1][0]))
                data[image]['heuristique3_adresse'] = l_adresse

    
with open('fakeJson.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))
fjson.close()


