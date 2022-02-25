#from geopy import geocoders
import geocoder
<<<<<<< HEAD

g = geocoder.geonames('paris', maxRows=5, country=['FR', 'US'], key='Lydia_Ouam')
for r in g:
    print((r.address, r.country))
    l = geocoder.geonames(r.geonames_id, method='details', key='Lydia_Ouam')
    print(l.lat)
    print(l.lng)
    print(l.country)
    print(l.state)

=======
import json

#opening the json file
fjson = open('data.json')

#load the json file into a dict
data = json.load(fjson)
# print(data['image0']['SpacyLoc'][0][0])

for image in data:
    for local in data[image]['SpacyLoc']:
        g = geocoder.geonames(local[0],maxRows=5,key='Lydia_Ouam')
        for r in g:
            print('-----------------------------------------------------------------------------')
            print((r.address, r.country))
            l = geocoder.geonames(r.geonames_id, method='details', key='Lydia_Ouam')
            print(l.lat)
            print(l.lng)
            print(l.country)
            print(l.state)
            print('-----------------------------------------------------------------------------')
            break
>>>>>>> a0d1e096f04323dc5033675cbc696eec12f23e66

    #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



