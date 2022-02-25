import json

with open( 'data.json') as mon_fichier : 
	data=json.load(mon_fichier)

for image in data  : 
	l=data[image]['LocationTagger'][5]['Citiy_mentions']
	x="false"
	for city in l:
		if city[1]>1:
			x=city[0]
	if x!="false":
		for  country in   data[image]['LocationTagger'][2]['Country_Cities']:
			if ( x in data[image]['LocationTagger'][2]['Country_Cities'][country]):
				data[image]['heuristique3']=""+x+","+country+""
        
liste=["southern","northern","Southern","Northern"]
for image in data:
	title=data[image]['title'].split()
	for mot in title:
		if mot in liste:
			data[image]['heuristique4']=mot+","+data[image]["resultat_heurisique_2"]























with open('data.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))


		