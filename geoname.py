import geocoder

# Montpellier France
# Larslan
# Larslan Church

# Nettoyage de la chaine
text = "Oregon ".replace(",","").lower() 
ma_chaine = text.split() 
print("-------------------------------------------------")
a = geocoder.geonames("Oregon",key='Lydia_Ouam', maxRows = 5,  isNameRequired = True)
# print(a.geojson)
for i in a:
    g = geocoder.geonames(i.geonames_id, method = 'details', key='Lydia_Ouam')
    for r in g:
        if r.admin4 != '':
            if r.admin4 == r.address:
                if(r.feature_class == 'P'):
                    print('----------------Filtrage-----------------') 
                    # Par la suite on affichera que le premier
                    print([(r.address, r.country, r.description, r.feature_class, r.class_description, r.admin2, r.admin3, r.admin4, r.lat, r.lng)])
        # Maintenant on essaie de regarder si y a une chaine specific dans le text example church, airport et la prendre pour afficher
        
        if r.country_code.lower() in ma_chaine:
            print([(r.address, r.country, r.description, r.feature_class, r.class_description, r.admin2, r.admin3, r.admin4, r.lat, r.lng)])
            if r.description in ma_chaine:
                print([(r.address, r.country, r.description, r.feature_class, r.class_description, r.admin2, r.admin3, r.admin4, r.lat, r.lng)])


# country_code