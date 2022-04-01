import string
import json
import re
from math import floor

# Ce fichier evalue les heuritiques adresse de locationTagger et SpacyLoc

#opening the json file
fjson = open('data.json')
data = json.load(fjson)

# Evaluation de l'heuristique adresse de locationTagger

# L'adresse retourner par LocationTagger

compteur_true = 0
compteur_image = 0

for text in data:
    if("heuristique_adresse_LT" in data[text]):
        adresse = data[text]['heuristique_adresse_LT'][0]
        compteur_image = compteur_image + 1
        adresseLT = adresse.replace(",","").lower() #Nettoyer la chaine en supprimant les virgules
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


print("L'heuristique Location Tagger est correcte avec un pourcentage de :",compteur_true/compteur_image*100,"%")



#Evaluation de l'heuristique par rapport a realLoc 
cpt_heurisique=0
cpt_image=0
for  image  in data :
	resultat_contenu = [] 
		
    # traitement par comparaison   de l'heuristique SpacyLoc  par rapport a realLoc 
	mots= re.split ( ',| ' ,data[image]['realLoc']['Nomreal'])
	chaine1=""
	liste_real_loc=[] 
	for i in mots : 
		if (len(i)!=0):
			chaine1=chaine1+(i.lower())+" "
			liste_real_loc.append (i.lower())
	if ("resultat_Spacy" in data[image]):   # que si spacy loc existe 
		cpt_image=cpt_image+1
		
		chaine2=data[image] ['resultat_Spacy'][0].lower()
		if ( chaine1 == chaine2  )   : # comparaison directe (de realLoc de resultat_SpacyLOc)
			# print ( image +" " + "resultat bon " + str ( len (chaine1.split())) + "/" + str (  len ( chaine2.split()))   )
			cpt_heurisique=cpt_heurisique+1
		else : 
			liste_spacy = data[image] ['resultat_Spacy'][0] .split ()
			for mot in  liste_spacy:
				if mot.lower() in liste_real_loc :
					resultat_contenu.append (mot )
		
		if ( len ( resultat_contenu)>= len( liste_real_loc)/2)   :
			# print (image + " resultat bon " + str (len( resultat_contenu))+ "/" + str ( len ( liste_real_loc)))
			cpt_heurisique=cpt_heurisique+1
	
	
print (f"L'heuristique SpacyLoc est correcte a  : {(cpt_heurisique/cpt_image)*100:.2f} %")


fjson.close()


