import json
import math
import re
from math import floor
with open( 'data.json') as mon_fichier : 
	data=json.load(mon_fichier)
#evaluation de SpacyLOc

#construction d'heuristique  SpacyLoc 
for image in data : 
	resultat_heurisique=""
	for  lieu_spacy in  (data[image]['SpacyLoc']) :
		sm=lieu_spacy [0].split ()
		for i in sm  :	
			resultat_heurisique=resultat_heurisique+i+" "
			data[image] ['resultat_Spacy'] = resultat_heurisique
			
with open('data.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))

mon_fichier.close()


			

