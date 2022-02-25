import json

with open( 'data.json') as mon_fichier : 
	data=json.load(mon_fichier)
cptFin=0
cptDebut=0

#pour les images qui ont une seule localisation
for  image  in data :
	fix=data[image]['SpacyLoc'][0][1] 
	valide=True
	for loc in data[image]['SpacyLoc']:
		if fix!=loc[1]:
			valide=False
	if  valide:
		s= data[image]['title'] 
		l=s.split() 
		localisation=fix
		indice=0
		for mot in range ( len( l )) : 
			if (l[mot] == localisation):
				indice = mot
		if ( indice >= (len(l)-2)/2 ):
			data[image]['heurisique 1: ']="fin"
			cptFin+=1
		else :
			data[image]['heurisique 1:']="debut"
			cptDebut+=1

if (cptDebut>cptFin):
	resultat_heurisique_1 = "debut"
else : 
	resultat_heurisique_1 = "fin"

#pour les images qui ont plusierus localisations
for  image  in data : 
	if  ( len (data[image]['SpacyLoc']) > 1):
		if (resultat_heurisique_1 == "debut"):
			data[image]['resultat_heurisique_2'] = data[image]['SpacyLoc'][0][1]
		else:
			longeur=len(data[image]['SpacyLoc'])-1
			data[image]['resultat_heurisique_2'] = data[image]['SpacyLoc'][longeur][1]
	

with open('data.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))

