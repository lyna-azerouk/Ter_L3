#eval heuristique 2
cpt12=0	
cpt_heurs2=0
for  image  in data :
	resultat = 0
	chaine1=data[image]['realLoc']['Nomreal'].lower()
	if ('heuristique 2' in data[image] ):
		cpt12+=1
		chaine2=data[image] ['heuristique 2'].lower()

	if(chaine1==chaine2):
		cpt_heurs2+=1

	else :
		for i in chaine2 : 
			if i in chaine1:
				resultat+=1
	if (resultat>=len(chaine1)/2):
		cpt_heurs2+=1
print (f"L'heuristique 2 est correcte à  : {(cpt_heurs2/cpt12)*100:.2f} %")	