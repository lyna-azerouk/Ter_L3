import json
import math
import re
from math import floor
from geoname import geo_loc

with open( 'data.json') as mon_fichier : 
	data=json.load(mon_fichier)
#evaluation de SpacyLOc

#construction d'heuristique  SpacyLoc 
for image in data : 
	resultat_heurisique=""

	if (len (data[image]['SpacyLoc'])>0):
		
		for  lieu_spacy in  (data[image]['SpacyLoc']) :
			sm=lieu_spacy [0].split ()
			for i in sm  :	
				resultat_heurisique=resultat_heurisique+i+" "
			t=resultat_heurisique.strip()

		liste=geo_loc(resultat_heurisique)
		if (liste!=None):    #dans le cas ou geo_loc ne retourn rien 
<<<<<<< HEAD
			data[image] ['resultat_Spacy'] = [str(t)]+liste
=======
			data[image] ['resultat_Spacy'] = [str(resultat_heurisique.strip())]+liste
		else :
			data[image] ['resultat_Spacy'] = [str(resultat_heurisique.strip())]

>>>>>>> 16678145d540461a046e768ee956dc5cf7fa7fbc
	

with open('data.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))

mon_fichier.close()


			

