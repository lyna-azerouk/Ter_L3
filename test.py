import geocoder

g = geocoder.geonames('Yosemite Valley', maxRows=20, country=['FR', 'US'], key='Lydia_Ouam')
print([(r.address, r.country) for r in g])
