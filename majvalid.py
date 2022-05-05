import sys
import json

from numpy import imag

my_file = open("teste.txt", "r", encoding = 'utf-8')
content = my_file.readlines()
for line in content:
    line = line.replace("{","")
    line = line.replace("}","")
    my_string = line.split(",")
    # read the json file
    fjson = open('testData.json')
    data = json.load(fjson)
    for image in data:
        if(my_string[0] == data[image]["url"]):
            if len(my_string) < 3:
                # there is no location
                data[image]['aucun'] = {}
                with open('testData.json', 'w') as mon_fichier:
                    mon_fichier.write(json.dumps(data, indent=4))
            else:
                data[image]['realLoc'] = {}
                data[image]['realLoc']['Nomreal'] = my_string[1]
                data[image]['realLoc']['Latitude'] = my_string[2]
                data[image]['realLoc']['Longitude'] = my_string[3]
            with open('testData.json', 'w') as mon_fichier:
                mon_fichier.write(json.dumps(data, indent=4))
mon_fichier.close()
sys.stdout.close()

# We can delete the data from the test.txt