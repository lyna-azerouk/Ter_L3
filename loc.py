import locationtagger
import json


# text = "Brookings, Oregon [OC] [5304x7952]"

# entities = locationtagger.find_locations(text = text)
# print(entities.cities)
# print(entities.countries)
# print(entities.regions)
# print(entities.country_regions)
# print(entities.country_cities)
# print(entities.country_mentions)
# print(entities.region_cities)
# print(entities.other)
# print(entities.address_strings)

# print("-------------------------------------------")

# text2 = "It snows in Hérault, Montpellier, France, In Algeria, Algiers the weather Quebec"

# entities2 = locationtagger.find_locations(text = text2)

# print(entities2.cities)
# print(entities2.countries)
# print(entities2.regions)
# print(entities2.country_regions)
# print(entities2.country_cities)
# print(entities2.country_mentions)
# print(entities2.region_cities)
# print(entities2.address_strings)
# print(entities2.city_mentions)

# tex3 = "A very unique Firefall in Yosemite Valley from 2019"

# enti = locationtagger.find_locations(text = tex3)

# print(enti.cities)
# print(enti.countries)
# print(enti.regions)
# print(enti.country_regions)
# print(enti.country_cities)
# print(enti.country_mentions)
# print(enti.region_cities)
# print(enti.address_strings)
# print(enti.city_mentions)


print("---------------------------------------------------------------------------------------------------------")


#opening the json file
fjson = open('data.json')
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
    data[image]['LocationTagger'] = l
    
with open('data.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(data, indent=4))
fjson.close()


        









