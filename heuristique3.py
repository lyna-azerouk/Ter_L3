import json

# Heuristique 3 LOC,GPE alors Loc appartient a GPE

#opening the json file
fjson = open('data.json')
data = json.load(fjson)


for image in data:
    ordre = data[image]["Ordre"]
    taille_ordre = len(ordre)
    for i in range(taille_ordre-1):
        l_adresse = []
        if(ordre[i] == 'LOC' and ordre[i+1] == 'GPE'):
            l_adresse.append((data[image]['SpacyLoc'][0][0],data[image]['SpacyLoc'][1][0]))
            data[image]['resultatHeuristique3'] = l_adresse

    
with open('data.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))
fjson.close()


