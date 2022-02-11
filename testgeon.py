import json  
from     geopy.geocoders import Nominatim
import folium 
import spacy 

from folium.plugins  import MarkerCluster 
nlp = spacy.load("en_core_web_sm")
doc = nlp("Where are you?")
print(doc[2].morph)  
dic={}
geolocalisateur =Nominatim(user_agent="lyna")
with open ('data.json') as monfichier :
     data=json.load(monfichier)
  
for  image in data.items():
	L=[]
	print (image)
	for j in  image[1].items():
		if ( j[0]=='SpacyLoc'):
			for  ville in  j[1]: 

				print (ville)
				x=str( ville[0])
				location=geolocalisateur.geocode(ville[0])
				if(location==None or location.longitude==None or location.latitude):
					L.append([ville[0],ville[1],location.latitude, location.longitude ])
	data[image[0]]['SpacyLoc']=L
	print (data[image[0]]['SpacyLoc'])

with open('data.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))
     

