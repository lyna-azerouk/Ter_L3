import string
import json
import re
from math import floor
import csv


# Ce fichier evalue les heuritiques adresse de locationTagger et SpacyLoc

#opening the json file
fjson = open('data.json')
data = json.load(fjson)
fjson.close()


# Evaluation de l'heuristique adresse de locationTagger

# L'adresse retourner par LocationTagger

compteur_true = 0
compteur_image = 0

for text in data:
    if("heuristique_adresse_LT" in data[text]):
        adresse = data[text]['heuristique_adresse_LT']
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


print(f"L'heuristique Location Tagger est correcte avec un pourcentage de :",compteur_true/compteur_image*100,"%")



#Evaluation de l'heuristique par rapport a realLoc 
cpt_heurisique=0
cpt_image=0
for  image  in data :
	resultat_contenu = [] 
	cpt_image=cpt_image+1	
    # traitement par comparaison   de l'heuristique SpacyLoc  par rapport a realLoc 
	mots= re.split ( ',| ' ,data[image]['realLoc']['Nomreal'])
	chaine1=""
	liste_real_loc=[] 
	for i in mots : 
		if (len(i)!=0):
			chaine1=chaine1+(i.lower())+" "
			liste_real_loc.append (i.lower())
	
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




#eval heuristique 5
cpt=0	
cpt_heur=0
for  image  in data :
	resultat = "" 
	cpt+=1
	chaine1=data[image]['realLoc']['Nomreal'].lower()
	chaine2=data[image] ['heuristique 5'].lower()

	if(chaine1==chaine2):
		cpt_heur+=1

	else :
		for i in chaine2 : 
			if i in chaine1:
				resultat+=i+" "
	if (len(resultat)>=len(chaine1)):
		cpt_heur+=1
print (f"L'heuristique 5 est correcte à  : {(cpt_heur/cpt)*100:.2f} %")	


#eval heuristique country_cities
cpt2=0	
cpt_heurs=0
for  image  in data :
	resultat = "" 
	chaine1=data[image]['realLoc']['Nomreal'].lower()
	if ('heuristique_country_cities' in data[image] ):
		cpt2+=1
		chaine2=data[image] ['heuristique_country_cities'].lower()

	if(chaine1==chaine2):
		cpt_heurs+=1

	else :
		for i in chaine2 : 
			if i in chaine1:
				resultat+=i+" "
	if (len(resultat)>=len(chaine1)):
		cpt_heurs+=1
print (f"L'heuristique country_cities est correcte à  : {(cpt_heurs/cpt2)*100:.2f} %")	


#eval heuristique 3
cpt3=0	
cpt_heuri=0
for  image  in data :
	resultat = "" 
	chaine1=data[image]['realLoc']['Nomreal'].lower()
	chaine2=""
	if ('heuristique3_adresse' in data[image] ):
		cpt3+=1
		list_heur3=data[image]['heuristique3_adresse'][0]
		for mot in list_heur3:
			chaine2+=mot.lower()+" "

	if(chaine1==chaine2):
		cpt_heuri+=1

	else :
		for i in chaine2 : 
			if i in chaine1:
				resultat+=i+" "
	if (len(resultat)>=len(chaine1)):
		cpt_heuri+=1
print (f"L'heuristique 3 est correcte à  : {(cpt_heuri/cpt3)*100:.2f} %")



heur1=(compteur_true/compteur_image)*100
heur2=(cpt_heurisique/cpt_image)*100
heur3=(cpt_heuri/cpt3)*100
heur5=(cpt_heur/cpt)*100
heur4=(cpt_heurs/cpt2)*100


with open('stat.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Heur","Pourc"])
    writer.writerow(["Heuristique 1",heur1])
    writer.writerow(["Heuristique 2",heur2]) 
    writer.writerow(["Heuristique 3",heur3])
    writer.writerow(["Heuristique 4",heur4])
    writer.writerow(["Heuristique 5",heur5])
