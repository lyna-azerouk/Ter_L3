import json  
from   geopy.geocoders import Nominatim
import folium 
import spacy 
import geocoder

from folium.plugins  import MarkerCluster 
nlp = spacy.load("en_core_web_sm")
doc = nlp("Where are you?") 
dic={}
geolocalisateur =Nominatim(user_agent="lyna")
with open ('data.json') as monfichier :
     data=json.load(monfichier)
  
for  image in data.items():
	L=[]
	for j in  image[1].items():
		if ( j[0]=='SpacyLoc'):
			for  ville in  j[1]: 
				g = geocoder.geonames(ville[0], maxRows=5, key='Lydia_Ouam')
				for r in g:
					l = geocoder.geonames(r.geonames_id, method='details', key='Lydia_Ouam')
					L.append([l.country,ville[0],ville[1], l.lat,l.lng])

	data[image[0]]['SpacyLoc']=L

with open('data.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))
