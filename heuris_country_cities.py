import json

with open( 'data.json') as mon_fichier : 
    data=json.load(mon_fichier)


for image in data:
    cc = data[image]["LocationTagger"][2]['Country_Cities']
    for country in cc:
        l = cc[country]
        chaine = ""
        for e in range(len(l)):
            chaine+=l[e]+" "
        s = country+","+chaine
        data[image]["heuristique_country_cities"] = s



with open('data.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))


mon_fichier.close()
    