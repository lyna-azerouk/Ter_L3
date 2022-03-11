import json

# Cette heuristique regarde la cite la plus mentionee dans le champs du texte

with open( 'data.json') as mon_fichier : 
	data=json.load(mon_fichier)

for image in data  : 
	l=data[image]['LocationTagger'][5]['Citiy_mentions']
	x="false"
	if ( len(l)>0):
		max=l[0][1]
		for city in l:
			if ( max < city[1] ):
				max = city[1]
				x = city[0]
		if x!="false":
			for  country in   data[image]['LocationTagger'][2]['Country_Cities']:
				if ( x in data[image]['LocationTagger'][2]['Country_Cities'][country]):
					data[image]['heuristique_mention']=""+x+","+country+""
    # De plus elle regarde si dans le champs du texte il existe un mot comme southern, ...
	# et elle l'ajoute au resultats des heuristiques precedentes. heuristique 2 ou 3
liste=["southern","northern","south","north","west","east","western","eastern"]
for image in data:
	title=data[image]['title'].split()
	for mot in title:
		mot = mot.lower()
		if mot in liste:
			if('heuristique 2' in data[image]):
				data[image]['heuristique 4']=mot+","+data[image]['heuristique 2']
			elif('heuristique3_adresse' in data[image]):
				data[image]['heuristique 4']=mot+","+data[image]['heuristique3_adresse'][0][0]+data[image]['heuristique3_adresse'][0][1]

with open('data.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))
mon_fichier.close()


		
