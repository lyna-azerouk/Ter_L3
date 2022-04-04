from unittest import case
import geocoder

# Nettoyage de la chaine
def geo_loc(adr):
    text = adr.replace(",","").lower() 
    ma_chaine = text.split() 

    a = geocoder.geonames(adr,key='Lydia_Ouam', maxRows = 5,  isNameRequired = True)

    for i in a:
        g = geocoder.geonames(i.geonames_id, method = 'details', key='Lydia_Ouam')
        for r in g:

            if r.description in ma_chaine:
                localisation = [r.lat, r.lng]
                if r.country_code.lower() in ma_chaine:
                    localisation = [r.lat, r.lng]
                return localisation

            if(r.feature_class == 'P'):
                localisation = [r.lat, r.lng]
                if r.admin4 != '':
                    if r.admin4 == r.address:
                        localisation = [r.lat, r.lng]
                return localisation
        return [r.lat,r.lng]

