import json
from geoname import geo_loc 

with open( 'data.json') as mon_fichier : 
	data=json.load(mon_fichier)
cptFin=0
cptDebut=0
# cette heuristique detecte l'emplacement du champs ou la localistation est mentionnes (c-a-d fin ou debu)
#pour les images qui ont une seule localisation
for  image  in data :
	if(len(data[image]['SpacyLoc']) == 1):
		s = data[image]['title'] 
		l = s.split() 
		for mot in range ( len(l) - 2) : 
			if (l[mot] == data[image]['SpacyLoc'][0][0]):
					indice = mot
					if ( indice >= (len(l) - 2)/2 ):
						data[image]['heuristique 1']= data[image]['SpacyLoc'][0][0]
						cptFin+=1
					else :
						data[image]['heuristique 1']=data[image]['SpacyLoc'][0][0]
						cptDebut+=1

	if (cptDebut > cptFin):
		resultat_heurisique_1 = "debut"
	else : 
		resultat_heurisique_1 = "fin"

#pour les images qui ont plusierus localisations
for  image  in data : 
	if  ( len (data[image]['SpacyLoc']) > 1):
		if (resultat_heurisique_1 == "debut"):
			liste=geo_loc(str(data[image]['SpacyLoc'][0][0]))
			data[image]['heuristique 2'] = [str(data[image]['SpacyLoc'][0][0])]+liste
		else: 
			longeur=len(data[image]['SpacyLoc'])-1
			liste=geo_loc(str(data[image]['SpacyLoc'][longeur][0]))
			data[image]['heuristique 2'] = [str(data[image]['SpacyLoc'][longeur][0])]+liste
	

with open('data.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))

mon_fichier.close()


			
