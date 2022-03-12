import json
import geocoder
import math
import re
from math import floor
with open( 'data.json') as mon_fichier : 
	data=json.load(mon_fichier)
#evaluation de SpacyLOc

#construction d'uristique SpycyLoc  rassempber  les resultats de Spacy
for image in data : 
	resultat_heurisique=""
	for  lieu_spacy in  (data[image]['SpacyLoc']) :
		sm=lieu_spacy [0].split ()
		for i in sm  :	
			resultat_heurisique=resultat_heurisique+i+" "
			data[image] ['resultat_Spacy'] =resultat_heurisique
	


#Evaluation de l'heuristique par rapport a realLoc 
cpt_heurisique=0
cpt_image=0
for  image  in data :
	resultat_contenu = [] 
	cpt_image=cpt_image+1	
    # traitement par comparaison   de l'heuriqtie SpacyLoc  par rapport a realLOc 
	mots= re.split ( ',| ' ,data[image]['realLoc']['Nomreal'])
	chaine1=""
	liste_real_loc=[] 
	for i in mots : 
		if (len(i)!=0):
			chaine1=chaine1+(i.lower())+" "
			liste_real_loc.append (i.lower())
	
	chaine2=data[image] ['resultat_Spacy'].lower()
	if ( chaine1 == chaine2  )   : # comparaison directe (de realLoc de resultat_SpacyLOc)
		print ( image +" " + "resultat bon " + str ( len (chaine1.split())) + "/" + str (  len ( chaine2.split()))   )
		cpt_heurisique=cpt_heurisique+1
	else : 
		liste_spacy = data[image] ['resultat_Spacy'] .split ()
		for mot in  liste_spacy:
			if mot.lower() in liste_real_loc :
				resultat_contenu.append (mot )
	
	if ( len ( resultat_contenu)>= len( liste_real_loc)/2)   :
		print (image + " resultat bon " + str (len( resultat_contenu))+ "/" + str ( len ( liste_real_loc)))
		cpt_heurisique=cpt_heurisique+1
	

	
print ("le nombre d'image vrai " +str (cpt_heurisique)+ "/"+str(cpt_image) )
		

	   
	      



		
		   


			
			 
			

with open('data.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))

mon_fichier.close()


			

