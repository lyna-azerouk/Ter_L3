from itertools import count
import json
from geoname import geo_loc 
with open( 'data.json') as mon_fichier : 
    data=json.load(mon_fichier)


for image in data:
    cc = data[image]["LocationTagger"][2]['Country_Cities']
    for country in cc:
        l = cc[country]
        ch_ = country
        for chaine in l:
            ch_ = chaine + " " + ch_  
        liste=geo_loc(ch_)
        if (liste!=None):
            data[image]["heuristique_country_cities"] = [ch_] + liste

with open('data.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))


mon_fichier.close()
    
