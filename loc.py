import locationtagger
import json



#opening the json file
fjson = open('fakeJson.json')
data = json.load(fjson)
for image in data:
    title = data[image]['title']
    enti = locationtagger.find_locations(text = title)
    l=[]
    l.append({"Countries":enti.countries})
    l.append({"Cities":enti.cities})
    l.append({"Country_Cities":enti.country_cities})
    l.append({"Region_Cities":enti.region_cities})
    l.append({"Country_mentions":enti.country_mentions})
    l.append({"Citiy_mentions":enti.city_mentions})
    l.append({"Adresse":enti.address_strings})
    data[image]['LocationTagger'] = l
    
with open('fakeJson.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))
fjson.close()


        









