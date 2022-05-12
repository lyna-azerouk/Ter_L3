import json
import pymongo

fjson = open('data.json')
data = json.load(fjson)

client = pymongo.MongoClient('localhost',27017)
mydb = client["test"]
sinfun = mydb["sin2"]


# the list of records is written to the database in one go:
sinfun.insert_one(data)
print('done')

