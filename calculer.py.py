import json

#opening the json file
fjson = open('data.json')
data = json.load(fjson)

# L'adresse retourner par LocationTagger
for text in data:
        adresse = data[text]['LocationTagger'][6]
        if len(adresse['Adresse']) != 0:
            print("--------------------------------------")
            print(adresse['Adresse'][0])
            # compare it to the real loc
            realloc = data[text]['realLoc']['Nomreal']
            print(realloc)
            print("--------------------------------------")
fjson.close()


