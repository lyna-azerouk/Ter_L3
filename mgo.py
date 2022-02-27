import json
import pymongo

fjson = open('data.json')
data = json.load(fjson)

client = pymongo.MongoClient('localhost',27017)
mydb = client["test"]
sinfun = mydb["sin2"]

l=[]
l.append(data)
# the list of records is written to the database in one go:
sinfun.insert_many(l)
print('done')

















""" print('insert')
data = []
for i in range(100):
    x = i/10.
    y = math.sin(x)
    data.append({'x':x,'y':y}) """


