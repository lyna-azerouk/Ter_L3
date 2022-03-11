import string
import json


#opening the json file
fjson = open('data.json')
data = json.load(fjson)

# L'adresse retourner par LocationTagger

compteur_true = 0
compteur_image = 0

for text in data:
        adresse = data[text]['LocationTagger'][6]
        if len(adresse['Adresse']) != 0:
            data[text]['heuristique_adresse_LT'] = adresse['Adresse'][0]
            compteur_image = compteur_image + 1
            adresseLT = adresse['Adresse'][0].replace(",","").lower() #Nettoyer la chaine en supprimant les virgules
            lLT = adresseLT.split()
            # compare it to the real loc
            realloc = data[text]['realLoc']['Nomreal']
            adresseR = realloc.replace(",","").lower()
            lR = adresseR.split()
            compteur_simi = 0
            for mot in lR:
                if(mot in lLT):
                    compteur_simi = compteur_simi + 1
            if(compteur_simi >= len(lLT)/2):
                compteur_true = compteur_true + 1


# print("L'heuristique est correcte avec un pourcentage de :",compteur_true/compteur_image*100,"%")

with open('data.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))

fjson.close()


