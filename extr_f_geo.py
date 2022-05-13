import geocoder
# 1. Valley of
# 2. Lake
# 3. Montpeyroux 
# 4. Church
# 5. Falls 
# 6. Montain -> region en France
# 7. Mountain -> montagne en anglais 
# 8. Park
# 9. City
# 10. River
# Je vais essayer d'ajouter des noms de villages de villes moins connus

text = 'River'

with open('exemples.txt', 'a', encoding = 'utf-8') as f:
    a = geocoder.geonames(text, key='Lydia_Ouam', maxRows = 15)
    for i in a:
        f.write(i.address)
        f.write(' ')
        g = geocoder.geonames(i.geonames_id, method = 'details', key='Lydia_Ouam')
        f.write(g.lng)
        f.write(' ')
        f.write(g.lat)
        f.write('\n')

f.close()
