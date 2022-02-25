#from geopy import geocoders
import geocoder

g = geocoder.geonames('paris', maxRows=5, country=['FR', 'US'], key='Lydia_Ouam')
for r in g:
    print((r.address, r.country))
    l = geocoder.geonames(r.geonames_id, method='details', key='Lydia_Ouam')
    print(l.lat)
    print(l.lng)
    print(l.country)
    print(l.state)


    #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



